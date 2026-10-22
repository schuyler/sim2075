"""E5 gates (implementation guide §3): per-run memory on FIX-B under hand-built ScriptedDraws.

(a) a hand-built factor path opens the T3 sustained gate (FG > 1.0 for 2 years) in exactly the specified year
    and resets on interruption; (b) a cascade delta is present for exactly ``years`` years after firing, absent
    in the firing year and after expiry, overlapping cascades sum; (c) the conditional cascade fires only under
    ``resolution == 'bad'``, with the resolution draw matching the reference's ``_draw_code`` at the cumulative
    boundaries; (d) a 257th live cascade raises ``LedgerOverflow`` naming the run and year; (e) dtypes and shapes.
Plus FIX-B's hand-traced event log reproduced by E3–E5 fed the reference's recorded state (no E6/E7 yet).

FIX-B: FG = z0 (Ω's Cholesky first row is [1, 0]), T1 loads FG .5, T3 loads FG .4; ε = +10 forces U ≈ 1 (no fire),
ε = −10 forces U ≈ 0 (fire wherever gated and p_eff > 0).
"""
import dataclasses

import numpy as np
import pytest

from sim.catalog.types import CascadeEdge
from sim.engine import MAX_ACTIVE, FactorModel, FiringModel, MemoryModel, draw_codes, namespace_from_state
from sim.reference import LedgerOverflow, ReferenceRun
from sim.rng import DrawShapes, ScriptedDraws
from sim.tests.fixtures import builders as B
from sim.tests.fixtures import fix_b

T1, T2, T3 = 0, 1, 2
NO, YES = 10.0, -10.0     # idio values forcing U ≈ 1 / U ≈ 0


def _draws(cat, fg, idio, res_u=0.3, branch_u=0.5):
    """fg [R, T] FG values; idio [R, T, E]; res_u scalar or [R, E] (constant across years)."""
    fg, idio = np.asarray(fg, dtype=np.float64), np.asarray(idio, dtype=np.float64)
    R, T = fg.shape
    E = cat.n_events
    shapes = DrawShapes.for_catalog(cat, 0)
    years = [{"factor": np.stack([fg[:, t], np.zeros(R)], axis=1), "idio": idio[:, t],
              "res_u": np.broadcast_to(np.asarray(res_u, dtype=np.float64), (R, E)).copy(),
              "branch_u": np.full((R, E), branch_u), "impact_z": np.zeros((R, shapes.n_impact_rows)),
              "dyn_z": np.zeros((R, 0))} for t in range(T)]
    return ScriptedDraws({"t2_offset": np.zeros((R, shapes.E_type2))}, years, shapes)


def _idio(R, T, E, **force):
    """All NO, except force[event-name] = list of (run, year) pairs set to YES."""
    out = np.full((R, T, E), NO)
    for e, pairs in force.items():
        for r, t in pairs:
            out[r, t, {"T1": T1, "T2": T2, "T3": T3}[e]] = YES
    return out


def _constant_state(R, stress=2.0):
    def states(t):
        return np.tile(np.array([[[stress, 100.0]]]), (R, 1, 1)), np.tile(np.array([1.0, 0.0]), (R, 1))
    return states


def _run(cat, draws, states, start_year=2025, run_offset=0, max_active=MAX_ACTIVE):
    """E3–E5 over one scripted block; ``states(t)`` gives the start-of-year (country, global_) tensors."""
    fm, fr = FactorModel.from_catalog(cat), FiringModel(cat)
    stream = draws.stream(0)
    thr = fr.thresholds(stream.init["t2_offset"])
    mem = MemoryModel(cat, draws.R, run_offset=run_offset, max_active=max_active)
    out = []
    for t in range(draws.years):
        year = start_year + t
        yr = stream.year(t)
        F, U = fm.year(yr)
        ns = namespace_from_state(cat, F, *states(t))
        counters = {e: c.copy() for e, c in mem.counters.items()}
        res = fr.base(ns, year, mem.events, thr, mem.counters)
        delta, mask = mem.deltas()
        p_eff = res.p_base + delta
        fired = fr.fire(res.gate, U, p_eff)
        codes, branches = mem.resolve(fired, yr["res_u"], yr["branch_u"], ns, year)
        mem.end_of_year(res.sustained_now, year)
        out.append(dict(year=year, counters=counters, gate=res.gate, p_base=res.p_base, delta=delta, mask=mask,
                        p_eff=p_eff, fired=fired, codes=codes, branches=branches))
    return out, mem


def _with_edges(edges):
    return dataclasses.replace(fix_b.catalog(), cascade_edges=edges)


# ------------------------------------------------------------- (a) sustained ----
def test_e5_sustained_gate_opens_in_specified_year_and_resets_on_interruption():
    cat = fix_b.catalog()
    T = 7
    fg = [[1.5] * T,                                  # held every year: open from t = 2 (two prior years)
          [1.5, 1.5, 0.5, 1.5, 1.5, 1.5, 1.5],        # dip in t = 2: gate still open in t = 2 (reads t ≤ 1), then
                                                      # counter 0 after t = 2, closed t = 3, 4, open again t = 5
          [1.5, 0.5, 1.5, 0.5, 1.5, 0.5, 1.5],        # never two consecutive years: never open
          [1.0] * T]                                  # FG > 1.0 is strict: never open
    R = len(fg)
    draws = _draws(cat, fg, _idio(R, T, cat.n_events, T3=[(r, t) for r in range(R) for t in range(T)]))
    out, _ = _run(cat, draws, _constant_state(R))     # x.stress = 2 > 1: the gate is the sustained condition alone

    counter = np.array([[o["counters"][T3][r, 0] for o in out] for r in range(R)])
    gate = np.array([[o["gate"][r, T3] for o in out] for r in range(R)])
    fired = np.array([[o["fired"][r, T3] for o in out] for r in range(R)])
    assert counter.tolist() == [[0, 1, 2, 3, 4, 5, 6],
                                [0, 1, 2, 0, 1, 2, 3],
                                [0, 1, 0, 1, 0, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0]]
    want = [[False, False, True, True, True, True, True],
            [False, False, True, False, False, True, True],
            [False] * T,
            [False] * T]
    assert gate.tolist() == want
    assert fired.tolist() == want                     # U ≈ 0 < p_eff = .1: fires exactly where the gate is open


def test_e5_sustained_gate_respects_preconditions_too():
    cat = fix_b.catalog()
    T = 4
    draws = _draws(cat, [[1.5] * T], _idio(1, T, cat.n_events))
    out, _ = _run(cat, draws, _constant_state(1, stress=1.0))       # x.stress > 1 fails: counters run, gate stays shut
    assert [o["counters"][T3][0, 0] for o in out] == [0, 1, 2, 3]
    assert not any(o["gate"][0, T3] for o in out)


# -------------------------------------------------------------- (b) duration ----
@pytest.mark.parametrize("years", [1, 2, 3])
def test_e5_cascade_present_for_exactly_years_years_after_firing(years):
    edge = fix_b.catalog().cascade_edges[0]
    cat = _with_edges([dataclasses.replace(edge, years=years)])
    T = 8
    fire_at = [[1], [1, 2]]                           # run 1 fires twice: overlapping cascades sum
    R = len(fire_at)
    draws = _draws(cat, np.zeros((R, T)), _idio(R, T, cat.n_events, T1=[(r, t) for r in range(R) for t in fire_at[r]]))
    out, _ = _run(cat, draws, _constant_state(R))     # FG = 0: T3's sustained gate never opens, so nothing else moves
    for r in range(R):
        assert [t for t in range(T) if out[t]["fired"][r, T1]] == fire_at[r]
        for t in range(T):
            n_live = sum(f + 1 <= t <= f + years for f in fire_at[r])
            assert out[t]["delta"][r, T3] == 0.5 * n_live, (r, t)
            assert out[t]["mask"][r, T3] == (1 << T1 if n_live else 0), (r, t)
            assert out[t]["delta"][r, [T1, T2]].tolist() == [0.0, 0.0]
            assert out[t]["p_eff"][r, T3] == out[t]["p_base"][r, T3] + 0.5 * n_live      # unclamped sum
    # the firing year itself never sees its own cascade, and the year after expiry sees none
    assert out[1]["delta"][0, T3] == 0.0 and out[1 + years + 1]["delta"][0, T3] == 0.0


# ----------------------------------------------------------- (c) conditional ----
def test_e5_conditional_cascade_only_under_bad_resolution():
    cat = fix_b.catalog()                             # T1 -> T3 if resolution == 'bad'; bad p .6, good .4
    T = 4
    res_u = np.full((3, cat.n_events), 0.3)
    res_u[:, T1] = [0.3, 0.7, 0.6]                    # bad; good; exactly on the cumulative boundary -> good
    draws = _draws(cat, np.zeros((3, T)), _idio(3, T, cat.n_events, T1=[(0, 1), (1, 1), (2, 1)]), res_u=res_u)
    out, mem = _run(cat, draws, _constant_state(3))
    tree = cat.resolution_tree[T1]
    assert out[1]["fired"][:, T1].all()
    assert out[1]["codes"][:, T1].tolist() == [tree.resolution_code["bad"], tree.resolution_code["good"],
                                               tree.resolution_code["good"]]
    assert [ReferenceRun._draw_code(u, tree.resolution_p) for u in res_u[:, T1]] == out[1]["codes"][:, T1].tolist()
    assert [out[t]["delta"][:, T3].tolist() for t in range(T)] == [[0, 0, 0], [0, 0, 0], [.5, 0, 0], [.5, 0, 0]]
    # EventState records the firing (memory E6 will read)
    assert mem.events.last_res[:, T1].tolist() == [0, 1, 1]
    assert mem.events.last_branch[:, T1].tolist() == [0, 0, 0]
    assert mem.events.last_fire_year[:, T1].tolist() == [2026] * 3
    assert mem.events.last_res[:, T3].tolist() == [-1] * 3


def test_e5_cascade_if_sees_the_sources_fresh_years_since():
    edge = fix_b.catalog().cascade_edges[0]
    cond = B.expr(["years_since"], lambda ns: ns["years_since"] == 0, "boolean")
    cat = _with_edges([dataclasses.replace(edge, cond=cond)])
    draws = _draws(cat, np.zeros((1, 3)), _idio(1, 3, cat.n_events, T1=[(0, 1)]))
    out, _ = _run(cat, draws, _constant_state(1))
    assert out[2]["delta"][0, T3] == 0.5


def test_e5_draw_codes_match_reference_including_cumulative_boundaries():
    trees = [B.tree([("a", 0.25, [("x", 0.5), ("y", 0.5)]), ("b", 0.25, [("z", 1.0)]),
                     ("c", 0.5, [("p", 0.125), ("q", 0.875)])]),
             B.tree([("bad", 0.6, [("default", 1.0)]), ("good", 0.4, [("default", 1.0)])]),
             B.default_tree()]
    cat = dataclasses.replace(fix_b.catalog(), resolution_tree=trees)
    edges = [0.0, 0.0625, 0.125, 0.25, 0.5, 0.5625, 0.6, 0.75, 1.0, np.nextafter(0.25, 0), np.nextafter(0.6, 1)]
    rng = np.random.default_rng(5)
    u = np.concatenate([edges, rng.random(200)])
    res_u = np.stack([u, u, u], axis=1)
    branch_u = np.stack([np.roll(u, 3)] * 3, axis=1)
    res, br = draw_codes(cat, res_u, branch_u)
    assert res.dtype == br.dtype == np.int64 and res.shape == br.shape == res_u.shape
    for e, tree in enumerate(trees):
        want_res = [ReferenceRun._draw_code(float(x), tree.resolution_p) for x in res_u[:, e]]
        want_br = [ReferenceRun._draw_code(float(x), tree.branch_p[k]) for x, k in zip(branch_u[:, e], want_res)]
        assert res[:, e].tolist() == want_res and br[:, e].tolist() == want_br


# -------------------------------------------------------------- (d) overflow ----
def _overflow_run(n_edges, years=1, fire_at=((1, 1),), R=3, run_offset=0, T=3):
    cat = _with_edges([CascadeEdge(T1, T3, 0.001, years, None)] * n_edges)
    draws = _draws(cat, np.zeros((R, T)), _idio(R, T, cat.n_events, T1=list(fire_at)))
    return _run(cat, draws, _constant_state(R), run_offset=run_offset)


def test_e5_256_live_cascades_fit():
    out, mem = _overflow_run(MAX_ACTIVE)
    assert out[2]["delta"][1, T3] == pytest.approx(MAX_ACTIVE * 0.001, rel=1e-12)
    assert out[2]["mask"][1, T3] == 1 << T1 and (mem.overflow_count == 0).all()


@pytest.mark.parametrize("run_offset", [0, 128])
def test_e5_overflow_at_257_live_cascades_names_run_and_year(run_offset):
    with pytest.raises(LedgerOverflow) as exc:
        _overflow_run(MAX_ACTIVE + 1, run_offset=run_offset)
    assert exc.value.run_index == [1 + run_offset] and exc.value.year == 2026
    assert exc.value.count == MAX_ACTIVE + 1 and exc.value.max_active == MAX_ACTIVE
    assert "year 2026" in str(exc.value)


def test_e5_overflow_counts_live_cascades_across_years():
    # 200 pushes in 2025 still live (years 5) when 200 more arrive in 2026: 400 > 256 in runs 0 and 2
    cat = _with_edges([CascadeEdge(T1, T3, 0.001, 5, None)] * 200)
    R, T = 3, 3
    draws = _draws(cat, np.zeros((R, T)), _idio(R, T, cat.n_events, T1=[(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]))
    with pytest.raises(LedgerOverflow) as exc:
        _run(cat, draws, _constant_state(R))
    assert exc.value.run_index == [0, 2] and exc.value.year == 2026 and exc.value.count == 400


# ------------------------------------------------------------ (e) dtypes ----
def test_e5_dtypes_and_shapes():
    cat = fix_b.catalog()
    R, T, E = 5, 3, cat.n_events
    draws = _draws(cat, np.full((R, T), 1.5), _idio(R, T, E, T1=[(r, 0) for r in range(R)]))
    out, mem = _run(cat, draws, _constant_state(R))
    for o in out:
        assert o["delta"].dtype == np.float64 and o["delta"].shape == (R, E)
        assert o["p_eff"].dtype == np.float64 and o["p_eff"].shape == (R, E)
        assert o["mask"].dtype == np.int64 and o["mask"].shape == (R, E)
        assert o["codes"].dtype == o["branches"].dtype == np.int64 and o["codes"].shape == (R, E)
    assert list(mem.counters) == sorted(cat.type3)
    for e, c in mem.counters.items():
        assert c.dtype == np.int64 and c.shape == (R, len(cat.type3[e].sustained))
    for a in (mem.events.last_res, mem.events.last_branch, mem.events.last_fire_year):
        assert a.dtype == np.int64 and a.shape == (R, E)
    assert MAX_ACTIVE == 256
    for a, dt in ((mem.active, bool), (mem.dst_event, np.int16), (mem.delta, np.float64),
                  (mem.years_remaining, np.int16), (mem.src_event, np.int16)):
        assert a.dtype == dt and a.shape == (R, MAX_ACTIVE)
    assert mem.overflow_count.dtype == np.int64 and mem.overflow_count.shape == (R,)


def test_e5_bitmask_width_is_checked():
    cat = dataclasses.replace(fix_b.catalog(), event_ids=[f"E{i}" for i in range(64)])
    with pytest.raises(ValueError, match="bitmask"):
        MemoryModel(cat, 1)


# ------------------------------------------- FIX-B hand trace through E3–E5 ----
def test_e5_reproduces_fix_b_hand_traced_firings():
    cat, ic, dyn, params = fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params()
    draws = fix_b.draws()
    rec = ReferenceRun(cat, ic, dyn, params, draws, 0).run()   # supplies start-of-year state until E6/E7 exist
    out, mem = _run(cat, fix_b.draws(), lambda t: (rec.country[t][None], rec.global_[t][None]))
    exp = fix_b.expected()
    log = [dict(year=o["year"], event=int(e), resolution=int(o["codes"][0, e]), branch=int(o["branches"][0, e]),
                p_base=float(o["p_base"][0, e]), p_eff=float(o["p_eff"][0, e]), cascade_mask=int(o["mask"][0, e]))
           for o in out for e in np.flatnonzero(o["fired"][0])]
    assert len(log) == len(exp["events"])
    for got, want in zip(log, exp["events"]):
        for k in ("year", "event", "resolution", "branch", "cascade_mask"):
            assert got[k] == want[k], (k, got, want)
        assert got["p_base"] == pytest.approx(want["p_base"], rel=1e-12)
        assert got["p_eff"] == pytest.approx(want["p_eff"], rel=1e-12)
    assert [bool(o["gate"][0, T3]) for o in out] == exp["gate_t3"]
    np.testing.assert_allclose([o["p_eff"][0, T3] for o in out], exp["p_eff_t3"], rtol=1e-12)
    assert [int(o["counters"][T3][0, 0]) for o in out] == [0, 1, 2, 3, 4, 0]
    assert mem.counters[T3][0, 0] == 0                                     # FG = 0 in t = 5
    assert mem.events.last_fire_year[0].tolist() == [2026, 2030, 2028]
