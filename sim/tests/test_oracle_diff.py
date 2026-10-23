"""§5.2 oracle diff: the vectorized modules against the scalar reference engine under SeededDraws at R = 64.

The reference replays run r by generating block r // block_size at full width and consuming row r; the
vectorized modules consume the whole block. Everything the built stages produce is compared:

    E3  factors F and copula uniforms U for every year (state-independent)
    E4  p_base, gate, p_eff and the fire mask for year 0 from initial conditions (no memory active yet)
    E5  every year: p_eff, gate, fire mask, the drawn resolution/branch codes and the cascade bitmask of
        each firing; and the start-of-year memory (sustained counters, live cascades with their source
        bitmask and summed deltas, last resolution/branch/firing year) after every year
    E6  every year: each firing's impact magnitudes (row, M), the per-event ``until: resolved`` flags and
        windows, and the live shock ledger (row, age, M, contribution in state), none of which depends on state

**Fed mode** (``test_oracle_diff_factors_and_firing``). For years > 0 the vectorized namespace is fed the reference's own recorded start-of-year state (``RunRecord.country[t]``,
``RunRecord.global_[t]``), isolating E3–E6 (the ledger applies its increments to a scratch copy). The
reference's internal memory at the start of year t is read from a replay truncated to t years (the draws are
generated year by year, so a shorter horizon consumes the same leading draws).

**Dynamics-free mode** (``test_oracle_diff_dynamics_free*``): both engines run with ``DynamicsSpec([])``, so
end-of-year state is exactly post-impact state and the vectorized engine evolves its own state from initial
conditions (E3–E6 wired in the step order, nothing fed). Diffed every year: the full state trajectory
(rtol 1e-9), the event log (year, event, resolution, branch, cascade mask exactly; magnitudes row-for-row, M,
p_base and p_eff at rtol 1e-9), the per-event active flags and windows, and the live ledger. Run on FIX-A and
FIX-B under ``SeededDraws`` (one and four blocks), and on FIX-B's scripted draws with initial ``x.stress`` 2.0,
which opens T3's precondition so that T3 fires in t = 3 and its ``until: resolved`` shock is exercised (the
seeded FIX-B batch never fires T3: with no dynamics ``x.stress`` stays 0).

The fixtures' impact rows are all immediate-onset and their 5–6 year horizons end before any decaying shock is
culled, so three test-built variants (fixture files unchanged) extend the dynamics-free diff:

    ramped long horizon   FIX-A (20 years) and FIX-B (32 years) with delayed/gradual onsets, ramped
                          permanents and every decay reaching its epsilon-cull
    until: resolved       ramped FIX-B, ``x.stress`` 2.0, T3's sustained condition dropped: T3 re-fires inside,
                          adjacent to and after its windows under ``SeededDraws``
    overflow              ramped FIX-A at ``max_active`` 3 and 5 (values some runs peak at exactly): each block
                          raises ``LedgerOverflow`` in the first year any of its runs overflows, naming exactly the
                          runs the reference fails that year, with its count
    out of range          ramped FIX-A with its multiplicative row widened (mean −0.5, std 0.4): each block raises
                          ``ImpactOutOfRange`` in the reference's first failing year, naming exactly the runs the
                          reference fails that year and the reference's row and contribution for the lowest

**Full-dynamics own-state mode** (``test_oracle_diff_full_dynamics*``, ahead of E8): both engines run with the
fixture's own ``DynamicsSpec`` and the vectorized engine evolves its own state through E3–E7 in step order
(``_step`` with a ``DynamicsModel``), diffed every year exactly as the dynamics-free mode is. Run on FIX-A and
FIX-B under ``SeededDraws`` (one and four blocks); FIX-B also over 20 years, where T3 fires under dynamics; and
on two test-built FIX-A variants: distinct σ > 0 on every mean-reverting variable (FIX-A's σ are all 0, so a
wrong ``dyn_z`` column would otherwise pass), and ``b.gdp_growth`` turned into a phase-2 additive drift declared
just before and just after the ``b.gdp_per_capita`` stock that compounds by it.
"""
import dataclasses

import numpy as np
import pytest

from sim.catalog.types import (DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED, ONSET_DELAYED, ONSET_GRADUAL,
                               ONSET_IMMEDIATE)
from sim.engine import (DynamicsModel, EventState, FactorModel, FiringModel, ImpactLedger, MemoryModel,
                        namespace_from_state)
from sim.reference import (DynamicsSpec, ImpactOutOfRange, InitialConditions, LedgerOverflow, ReferenceRun,
                           VarDynamics)
from sim.rng import DrawShapes, SeededDraws
from sim.tests.fixtures import fix_a, fix_b

R_DIFF = 64
SEED = 7
DUR_KINDS = (DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED)


def _assert_memory(mem: MemoryModel, i: int, run: ReferenceRun, where: str) -> None:
    """Vectorized memory row ``i`` equals the reference run's memory (``run`` after its last year's step 8)."""
    for e in mem.type3_order:
        assert mem.counters[e][i].tolist() == run.counters[e], (where, "counters", e)
    assert mem.events.last_res[i].tolist() == run.last_res.tolist(), (where, "last_res")
    assert mem.events.last_branch[i].tolist() == run.last_branch.tolist(), (where, "last_branch")
    assert mem.events.last_fire_year[i].tolist() == run.last_fire_year.tolist(), (where, "last_fire_year")
    live = np.flatnonzero(mem.active[i])
    got = sorted((int(mem.src_event[i, s]), int(mem.dst_event[i, s]), float(mem.delta[i, s]),
                  int(mem.years_remaining[i, s])) for s in live)
    want = sorted((cb.src, cb.dst, cb.delta, cb.remaining) for cb in run.cascades)
    assert got == want, (where, "cascades")
    want_mask = np.zeros(mem.E, dtype=np.int64)
    want_delta = np.zeros(mem.E)
    for cb in run.cascades:
        want_mask[cb.dst] |= 1 << cb.src
        want_delta[cb.dst] += cb.delta
    delta, mask = mem.deltas()
    assert mask[i].tolist() == want_mask.tolist(), (where, "cascade bitmask")
    np.testing.assert_allclose(delta[i], want_delta, rtol=1e-9, atol=0, err_msg=f"{where} cascade deltas")


def _assert_impacts(led: ImpactLedger, i: int, run: ReferenceRun, where: str) -> None:
    """Ledger row ``i`` equals the reference run's ledger and ``until: resolved`` flags (after its last step 8)."""
    assert led.event_active[i].tolist() == run.active.tolist(), (where, "active flags")
    assert led.active_until[i].tolist() == run.active_until.tolist(), (where, "active_until")
    live = np.flatnonzero(led.active[i])
    got = sorted((int(led.row[i, s]), int(led.age[i, s]), float(led.magnitude[i, s]), float(led.prev[i, s]))
                 for s in live)
    want = sorted((s.row, s.age, s.M, s.prev) for s in run.ledger)
    assert [g[:2] for g in got] == [w[:2] for w in want], (where, "ledger rows/ages")
    np.testing.assert_allclose([g[2:] for g in got], [w[2:] for w in want], rtol=1e-9, atol=0,
                               err_msg=f"{where} ledger M/prev")
    for s in live:
        ir = led.cat.impact_table[led.row[i, s]]
        assert (led.entity_idx[i, s], led.var_idx[i, s], led.owner_event[i, s], led.mult[i, s]) == \
            (ir["entity_idx"], ir["var_idx"], ir["event"], ir["multiplicative"]), (where, "ledger provenance")


def _assert_magnitudes(draw, i: int, ev, where: str) -> None:
    got = draw.for_firing(i, ev.event)
    assert [j for j, _ in got] == [j for j, _ in ev.magnitudes], (where, "magnitude rows")
    np.testing.assert_allclose([m for _, m in got], [m for _, m in ev.magnitudes], rtol=1e-9, atol=0,
                               err_msg=f"{where} magnitudes")


@pytest.mark.parametrize("mod", [fix_a, fix_b], ids=["FIX-A", "FIX-B"])
@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_factors_and_firing(mod, block_size):
    cat, ic, dyn, params = mod.catalog(), mod.initial_conditions(), mod.dynamics(), mod.params()
    shapes = DrawShapes.for_catalog(cat, len(dyn.noisy_keys))
    draws = SeededDraws(SEED, R=R_DIFF, shapes=shapes, block_size=block_size, years=params.years)
    # snap[t][r]: reference run r after t years (its memory at the start of year t); snap[T] is the full run
    snap = [[ReferenceRun(cat, ic, dyn, params, draws, r) for r in range(R_DIFF)]]
    for t in range(1, params.years + 1):
        runs = [ReferenceRun(cat, ic, dyn, dataclasses.replace(params, years=t), draws, r) for r in range(R_DIFF)]
        recs = [run.run() for run in runs]
        snap.append(runs)
    refs = recs

    fm, fr = FactorModel.from_catalog(cat), FiringModel(cat)
    seen = dict(cascade=0, counter=0, fired_after_0=0)
    for b in range(draws.n_blocks):
        start, stop = draws.block_rows(b)
        rb = stop - start
        stream = draws.stream(b)
        thr = fr.thresholds(stream.init["t2_offset"])
        mem = MemoryModel(cat, rb, run_offset=start)
        led = ImpactLedger(cat, rb, run_offset=start, max_active=params.max_active, epsilon_cull=params.epsilon_cull)
        for t in range(params.years):
            year = params.start_year + t
            yr = stream.year(t)
            F, U = fm.year(yr)
            for r in range(start, stop):
                np.testing.assert_allclose(F[r - start], refs[r].factors[t], rtol=1e-9, atol=0)
                np.testing.assert_allclose(U[r - start], refs[r].propensity_u[t], rtol=1e-9, atol=0)
            if t == 0:
                country = np.broadcast_to(ic.country, (rb,) + ic.country.shape)
                global_ = np.broadcast_to(ic.global_, (rb,) + ic.global_.shape)
                ns = namespace_from_state(cat, F, country, global_)
                counters = {e: np.zeros((rb, len(s.sustained)), dtype=np.int64) for e, s in cat.type3.items()}
                res = fr.base(ns, params.start_year, EventState.fresh(rb, cat.n_events), thr, counters)
                fired = fr.fire(res.gate, U, res.p_base)
                for r in range(start, stop):
                    ref = refs[r]
                    np.testing.assert_allclose(res.p_base[r - start], ref.p_eff[0], rtol=1e-9, atol=0)
                    assert res.gate[r - start].tolist() == ref.gate[0].tolist()
                    want = sorted(e.event for e in ref.events if e.year == params.start_year)
                    assert np.flatnonzero(fired[r - start]).tolist() == want

            # E3–E5 for year t from the reference's recorded start-of-year state
            for r in range(start, stop):
                _assert_memory(mem, r - start, snap[t][r], f"run {r} start of {year}")
                _assert_impacts(led, r - start, snap[t][r], f"run {r} start of {year}")
            country = np.stack([refs[r].country[t] for r in range(start, stop)])
            global_ = np.stack([refs[r].global_[t] for r in range(start, stop)])
            ns = namespace_from_state(cat, F, country, global_)
            res = fr.base(ns, year, mem.events, thr, mem.counters)
            delta, mask = mem.deltas()
            p_eff = res.p_base + delta
            fired = fr.fire(res.gate, U, p_eff)
            codes, branches = mem.resolve(fired, yr["res_u"], yr["branch_u"], ns, year)
            draw = led.resolve(fired, codes, branches, yr["impact_z"], year)
            led.apply(country.copy(), global_.copy(), year)   # ledger contents do not depend on state
            for r in range(start, stop):
                i, ref = r - start, refs[r]
                np.testing.assert_allclose(p_eff[i], ref.p_eff[t], rtol=1e-9, atol=0)
                assert res.gate[i].tolist() == ref.gate[t].tolist()
                firings = [ev for ev in ref.events if ev.year == year]
                assert np.flatnonzero(fired[i]).tolist() == [ev.event for ev in firings], (r, year)
                for ev in firings:
                    assert (codes[i, ev.event], branches[i, ev.event]) == (ev.resolution, ev.branch), (r, year)
                    assert mask[i, ev.event] == ev.cascade_mask, (r, year)
                    np.testing.assert_allclose(res.p_base[i, ev.event], ev.p_base, rtol=1e-9, atol=0)
                    np.testing.assert_allclose(p_eff[i, ev.event], ev.p_eff, rtol=1e-9, atol=0)
                    _assert_magnitudes(draw, i, ev, f"run {r} {year}")
            mem.end_of_year(res.sustained_now, year)
            led.end_of_year(year)
            seen["cascade"] += int(mem.active.sum())
            seen["counter"] += sum(int((c > 0).sum()) for c in mem.counters.values())
            seen["fired_after_0"] += int(fired.sum()) if t > 0 else 0
        for r in range(start, stop):
            _assert_memory(mem, r - start, snap[params.years][r], f"run {r} end of run")
            _assert_impacts(led, r - start, snap[params.years][r], f"run {r} end of run")
    # the diff is only meaningful if something fired in year 0 somewhere in the batch, and, beyond year 0,
    # if firings, live cascades and nonzero sustained counters occurred where the fixture has them
    assert any(e.year == params.start_year for ref in refs for e in ref.events)
    assert seen["fired_after_0"] > 0
    if cat.cascade_edges:
        assert seen["cascade"] > 0
    if any(s.sustained for s in cat.type3.values()):
        assert seen["counter"] > 0


def _step(cat, fm, fr, mem, led, thr, yr, year, country, global_, dm=None) -> dict:
    """One year of E3–E7 in the reference's step order; ``country``/``global_`` mutated in place. With ``dm``
    None, step 7 is skipped (dynamics-free); otherwise ``dm`` applies step 7 with this year's ``dyn_z``."""
    F, U = fm.year(yr)                                              # 1-2
    ns = namespace_from_state(cat, F, country, global_)
    res = fr.base(ns, year, mem.events, thr, mem.counters)          # 3
    delta, mask = mem.deltas()
    p_eff = res.p_base + delta
    fired = fr.fire(res.gate, U, p_eff)                             # 4
    codes, branches = mem.resolve(fired, yr["res_u"], yr["branch_u"], ns, year)    # 5
    draw = led.resolve(fired, codes, branches, yr["impact_z"], year)
    led.apply(country, global_, year)                               # 6
    if dm is not None:
        dm.step(country, global_, yr["dyn_z"])                      # 7
    mem.end_of_year(res.sustained_now, year)                        # 8
    led.end_of_year(year)
    return dict(res=res, mask=mask, p_eff=p_eff, fired=fired, codes=codes, branches=branches, draw=draw)


def _block_state(ic, rb):
    country = np.array(np.broadcast_to(ic.country, (rb,) + ic.country.shape), dtype=np.float64)
    global_ = np.array(np.broadcast_to(ic.global_, (rb,) + ic.global_.shape), dtype=np.float64)
    return country, global_


def _ramped(cat, changes):
    """A copy of ``cat`` whose impact rows ``{row: (onset_kind, onset_years, dur_kind, dur_param)}`` are replaced."""
    it = cat.impact_table.copy()
    for j, (ok, oy, dk, dp) in changes.items():
        it["onset_kind"][j], it["onset_years"][j], it["dur_kind"][j], it["dur_param"][j] = ok, oy, dk, dp
    return dataclasses.replace(cat, impact_table=it)


def _diff_dynamics_free(cat, ic, params, draws) -> dict:
    """E3–E6 wired in the step order with no dynamics, own state from ``ic``, diffed against the reference."""
    return _diff_own_state(cat, ic, params, draws, DynamicsSpec([]))


def _diff_own_state(cat, ic, params, draws, dyn) -> dict:
    """E3–E6 (and E7 when ``dyn`` has entries) wired in the step order, own state from ``ic``, both engines on
    ``dyn``, diffed against the reference every year."""
    R = draws.R
    snap = [[ReferenceRun(cat, ic, dyn, params, draws, r) for r in range(R)]]
    for t in range(1, params.years + 1):
        runs = [ReferenceRun(cat, ic, dyn, dataclasses.replace(params, years=t), draws, r) for r in range(R)]
        recs = [run.run() for run in runs]
        snap.append(runs)
    refs = recs

    fm, fr = FactorModel.from_catalog(cat), FiringModel(cat)
    dm = DynamicsModel(cat, dyn) if dyn.vars else None
    seen = dict(firings=0, shocks=0, live=0, owner_active=0, freed={k: 0 for k in DUR_KINDS},
                log=[[] for _ in range(R)], country=np.zeros((R, params.years) + ic.country.shape),
                global_=np.zeros((R, params.years) + ic.global_.shape))
    for b in range(draws.n_blocks):
        start, stop = draws.block_rows(b)
        rb = stop - start
        stream = draws.stream(b)
        thr = fr.thresholds(stream.init["t2_offset"])
        mem = MemoryModel(cat, rb, run_offset=start)
        led = ImpactLedger(cat, rb, run_offset=start, max_active=params.max_active, epsilon_cull=params.epsilon_cull)
        country, global_ = _block_state(ic, rb)
        max_live = np.zeros(rb, dtype=np.int64)
        for t in range(params.years):
            year = params.start_year + t
            live0, kind0 = led.active.copy(), led.dur_kind.copy()
            o = _step(cat, fm, fr, mem, led, thr, stream.year(t), year, country, global_, dm)
            seen["country"][start:stop, t], seen["global_"][start:stop, t] = country, global_
            freed = live0 & (~led.active | (led.age == 0))     # freed this year (a reused slot restarts at age 0)
            for k in DUR_KINDS:
                seen["freed"][k] += int((freed & (kind0 == k)).sum())
            res, mask, p_eff, fired = o["res"], o["mask"], o["p_eff"], o["fired"]
            codes, branches, draw = o["codes"], o["branches"], o["draw"]
            max_live = np.maximum(max_live, led.n_live)
            for r in range(start, stop):
                i, ref, where = r - start, refs[r], f"run {r} {year}"
                np.testing.assert_allclose(country[i], ref.country[t + 1], rtol=1e-9, atol=0, err_msg=where)
                np.testing.assert_allclose(global_[i], ref.global_[t + 1], rtol=1e-9, atol=0, err_msg=where)
                firings = [ev for ev in ref.events if ev.year == year]
                got = [(year, int(e), int(codes[i, e]), int(branches[i, e]), int(mask[i, e]))
                       for e in np.flatnonzero(fired[i])]
                assert got == [(ev.year, ev.event, ev.resolution, ev.branch, ev.cascade_mask) for ev in firings], where
                for ev in firings:
                    _assert_magnitudes(draw, i, ev, where)
                    np.testing.assert_allclose(res.p_base[i, ev.event], ev.p_base, rtol=1e-9, atol=0, err_msg=where)
                    np.testing.assert_allclose(p_eff[i, ev.event], ev.p_eff, rtol=1e-9, atol=0, err_msg=where)
                    seen["shocks"] += len(ev.magnitudes)
                    seen["log"][r].append((ev.year, ev.event))
                _assert_memory(mem, i, snap[t + 1][r], where)
                _assert_impacts(led, i, snap[t + 1][r], where)
            seen["firings"] += int(fired.sum())
            seen["live"] += int(led.n_live.sum())
            seen["owner_active"] += int((led.active & (led.dur_kind == DUR_UNTIL_RESOLVED)).sum())
        for r in range(start, stop):
            assert refs[r].max_active_seen == max_live[r - start], f"run {r} max_active_seen"
    return seen


@pytest.mark.parametrize("mod", [fix_a, fix_b], ids=["FIX-A", "FIX-B"])
@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_dynamics_free(mod, block_size):
    cat, ic, params = mod.catalog(), mod.initial_conditions(), mod.params()
    draws = SeededDraws(SEED, R=R_DIFF, shapes=DrawShapes.for_catalog(cat, 0), block_size=block_size,
                        years=params.years)
    seen = _diff_dynamics_free(cat, ic, params, draws)
    assert seen["firings"] > 0 and seen["shocks"] > 0 and seen["live"] > 0


def test_oracle_diff_dynamics_free_scripted_fix_b_until_resolved():
    cat, base, params = fix_b.catalog(), fix_b.initial_conditions(), fix_b.params()
    country = base.country.copy()
    country[cat.index.entity["x"], cat.index.country_var["stress"]] = 2.0
    ic = InitialConditions(country=country, global_=base.global_.copy())
    seen = _diff_dynamics_free(cat, ic, params, fix_b.draws())
    # T1 fires in 2026 ('bad', cascade to T3), T3 in 2028 (its until: resolved shock), T2 in 2030
    assert seen["log"][0] == [(2026, 0), (2028, 2), (2030, 1)]
    assert seen["owner_active"] == 2                                       # the T3 shock is live after 2028 and 2029
    rec = ReferenceRun(cat, ic, DynamicsSpec([]), params, fix_b.draws(), 0).run()
    conflicts = rec.global_[1:, cat.index.global_var["conflicts"]]
    assert conflicts.tolist() == [0.0, 0.0, 0.0, 1.0, 1.0, 0.0]            # holds 2028-2029, drops to 0 in 2030


# Full-dynamics own-state mode (ahead of E8): both engines run with the fixture's own DynamicsSpec and the
# vectorized engine evolves its own state through E3–E7 in step order. FIX-A's mean-reverting variables all
# have σ = 0, so a variant gives each a distinct σ > 0 (a wrong dyn_z column would otherwise pass), and a
# second puts a phase-2 additive drift on a gdp_stock's growth variable, declared before and after the stock.
FIX_A_SIGMA = {"a.gdp_growth": 0.7, "b.gdp_growth": 1.9, "oil_brent": 11.0}


def _noisy_fix_a_dynamics() -> DynamicsSpec:
    return DynamicsSpec([dataclasses.replace(v, sigma=FIX_A_SIGMA[v.key]) if v.kind == "mean_revert" else v
                         for v in fix_a.dynamics().vars])


def _drifted_growth_fix_a_dynamics(drift_first: bool) -> DynamicsSpec:
    """Noisy FIX-A with b.gdp_growth an additive drift (−0.25/yr) instead of mean-reverting (keys are unique),
    declared just before or just after the b.gdp_per_capita stock that compounds by it."""
    drift = VarDynamics("b.gdp_growth", "additive", rate=-0.25)
    vs = [v for v in _noisy_fix_a_dynamics().vars if v.key != "b.gdp_growth"]
    k = next(i for i, v in enumerate(vs) if v.key == "b.gdp_per_capita")
    vs.insert(k if drift_first else k + 1, drift)
    return DynamicsSpec(vs)


def _diff_full(mod, dyn, block_size, years=None) -> dict:
    cat, ic = mod.catalog(), mod.initial_conditions()
    params = mod.params() if years is None else dataclasses.replace(mod.params(), years=years)
    draws = SeededDraws(SEED, R=R_DIFF, shapes=DrawShapes.for_catalog(cat, len(dyn.noisy_keys)),
                        block_size=block_size, years=params.years)
    seen = _diff_own_state(cat, ic, params, draws, dyn)
    assert seen["firings"] > 0 and seen["shocks"] > 0 and seen["live"] > 0
    return seen


@pytest.mark.parametrize("mod", [fix_a, fix_b], ids=["FIX-A", "FIX-B"])
@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_full_dynamics(mod, block_size):
    _diff_full(mod, mod.dynamics(), block_size)


@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_full_dynamics_fix_b_long_horizon(block_size):
    """FIX-B over 20 years: with x.stress drifting +0.5/yr T3's precondition opens from 2027, and its sustained
    condition (FG > 1 two years running) is met often enough that T3 fires and its until: resolved shock is
    diffed under dynamics (over FIX-B's own 6 years the one-block batch never fires T3)."""
    seen = _diff_full(fix_b, fix_b.dynamics(), block_size, years=20)
    T3 = fix_b.catalog().index.event["T3"]
    assert any(e == T3 for log in seen["log"] for _, e in log) and seen["owner_active"] > 0


@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_full_dynamics_noisy_fix_a(block_size):
    dyn = _noisy_fix_a_dynamics()
    assert [v.sigma for v in dyn.vars if v.kind == "mean_revert"] == [0.7, 1.9, 11.0]
    seen = _diff_full(fix_a, dyn, block_size)
    quiet = _diff_full(fix_a, fix_a.dynamics(), block_size)
    idx = fix_a.catalog().index
    # the noise reached every mean-reverting variable (and so differs from the σ = 0 run)
    for e in ("a", "b"):
        g = idx.country_var["gdp_growth"]
        assert (seen["country"][:, :, idx.entity[e], g] != quiet["country"][:, :, idx.entity[e], g]).all()
    assert (seen["global_"][..., idx.global_var["oil_brent"]] != quiet["global_"][..., idx.global_var["oil_brent"]]).all()


@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_full_dynamics_drift_on_growth_key(block_size):
    before = _diff_full(fix_a, _drifted_growth_fix_a_dynamics(True), block_size)
    after = _diff_full(fix_a, _drifted_growth_fix_a_dynamics(False), block_size)
    idx = fix_a.catalog().index
    b, pc = idx.entity["b"], idx.country_var["gdp_per_capita"]
    # declared before the stock, the drift lowers this year's compounding rate: b's stock is lower every year
    assert (before["country"][:, :, b, pc] < after["country"][:, :, b, pc]).all()


# Ramped variants, built here (the fixtures stay as committed): FIX-A/FIX-B rows given delayed and gradual
# onsets, over horizons long enough for every decaying row to reach its epsilon-cull (FIX-A half-life 1: cull
# 14 years after onset; FIX-B half-life 2: 27 years after), so the diff covers onset ends, culls and frees.
RAMPED = {
    "FIX-A": (fix_a, 20, {0: (ONSET_DELAYED, 2, DUR_DECAY, 1.0),               # a.gdp_growth
                          1: (ONSET_GRADUAL, 3, DUR_PERMANENT, np.nan),        # oil_brent: ramped permanent
                          2: (ONSET_GRADUAL, 2, DUR_DECAY, 1.0)}),             # a.gdp_per_capita, multiplicative
    "FIX-B": (fix_b, 32, {0: (ONSET_GRADUAL, 3, DUR_DECAY, 2.0),               # x.gdp, 'bad'
                          1: (ONSET_DELAYED, 2, DUR_DECAY, 2.0),               # x.gdp, 'good'
                          2: (ONSET_GRADUAL, 2, DUR_PERMANENT, np.nan)}),      # temp: ramped permanent
}


@pytest.mark.parametrize("name", list(RAMPED))
def test_oracle_diff_dynamics_free_ramped_long_horizon(name):
    mod, years, changes = RAMPED[name]
    cat = _ramped(mod.catalog(), changes)
    params = dataclasses.replace(mod.params(), years=years)
    draws = SeededDraws(SEED, R=R_DIFF, shapes=DrawShapes.for_catalog(cat, 0), block_size=R_DIFF, years=years)
    seen = _diff_dynamics_free(cat, mod.initial_conditions(), params, draws)
    assert seen["freed"][DUR_DECAY] > 0 and seen["freed"][DUR_PERMANENT] > 0     # culls and onset-end frees diffed


@pytest.mark.parametrize("max_active", [3, 5])
@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_ledger_overflow_runs_and_year(block_size, max_active):
    """With a small ``max_active``, the vectorized block raises in the first year any of its runs overflows,
    naming exactly the runs whose reference replay overflows that year, with the reference's count. At both
    ``max_active`` values some runs peak at exactly ``max_active`` live shocks, which must not raise."""
    mod, years, changes = RAMPED["FIX-A"]
    cat, ic = _ramped(mod.catalog(), changes), mod.initial_conditions()
    params = dataclasses.replace(mod.params(), years=years, max_active=max_active)
    draws = SeededDraws(SEED, R=R_DIFF, shapes=DrawShapes.for_catalog(cat, 0), block_size=block_size, years=years)
    ref = {}
    for r in range(R_DIFF):
        try:
            ReferenceRun(cat, ic, DynamicsSpec([]), params, draws, r).run()
        except LedgerOverflow as exc:
            ref[r] = (exc.year, exc.count)
    assert ref and len(ref) < R_DIFF                       # the bound binds in some runs, not all
    fm, fr = FactorModel.from_catalog(cat), FiringModel(cat)
    raised = 0
    for b in range(draws.n_blocks):
        start, stop = draws.block_rows(b)
        rb = stop - start
        stream = draws.stream(b)
        thr = fr.thresholds(stream.init["t2_offset"])
        mem = MemoryModel(cat, rb, run_offset=start)
        led = ImpactLedger(cat, rb, run_offset=start, max_active=params.max_active, epsilon_cull=params.epsilon_cull)
        country, global_ = _block_state(ic, rb)
        block_ref = {r: v for r, v in ref.items() if start <= r < stop}
        first = min((y for y, _ in block_ref.values()), default=None)
        try:
            for t in range(years):
                _step(cat, fm, fr, mem, led, thr, stream.year(t), params.start_year + t, country, global_)
        except LedgerOverflow as exc:
            raised += 1
            want = sorted(r for r, (y, _) in block_ref.items() if y == first)
            assert (exc.run_index, exc.year) == (want, first), b
            assert exc.count == max(block_ref[r][1] for r in want)
            assert np.flatnonzero(led.overflow_count).tolist() == [r - start for r in want]
            assert (led.overflow_count[[r - start for r in want]] == [block_ref[r][1] - params.max_active
                                                                     for r in want]).all()
        else:
            assert first is None, b
    assert raised > 0


def test_oracle_diff_dynamics_free_until_resolved_refiring():
    """Seeded ``until: resolved`` coverage: FIX-B (ramped) with initial ``x.stress`` 2.0 and T3's sustained
    condition dropped, so T3 fires at its base rate (p .1, plus the T1 cascade) and re-fires inside, adjacent to
    and after its 2-year windows. Adjacent re-firing (the year after a window closes) is the case where step 6
    must read the owner flag step 5 has already set."""
    mod, years, changes = RAMPED["FIX-B"]
    cat = _ramped(mod.catalog(), changes)
    T3 = cat.index.event["T3"]
    cat = dataclasses.replace(cat, type3={T3: dataclasses.replace(cat.type3[T3], sustained=[])})
    base = mod.initial_conditions()
    country = base.country.copy()
    country[cat.index.entity["x"], cat.index.country_var["stress"]] = 2.0
    ic = InitialConditions(country=country, global_=base.global_.copy())
    params = dataclasses.replace(mod.params(), years=years)
    draws = SeededDraws(SEED, R=R_DIFF, shapes=DrawShapes.for_catalog(cat, 0), block_size=R_DIFF, years=years)
    seen = _diff_dynamics_free(cat, ic, params, draws)
    gaps = []                                                      # years between successive T3 firings, per run
    for log in seen["log"]:
        ys = [y for y, e in log if e == T3]
        gaps += [b - a for a, b in zip(ys, ys[1:])]
    window = int(cat.resolves_after[T3])
    assert any(g < window for g in gaps)                           # re-fire while active
    assert any(g == window for g in gaps)                          # re-fire the year after the window closed
    assert seen["freed"][DUR_UNTIL_RESOLVED] > 0


@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_impact_out_of_range_runs_year_and_row(block_size):
    mod, years, changes = RAMPED["FIX-A"]
    cat, ic = _ramped(mod.catalog(), changes), mod.initial_conditions()
    it = cat.impact_table.copy()
    it["mean"][2], it["std"][2] = -0.5, 0.4                # a.gdp_per_capita, multiplicative, gradual 2
    cat = dataclasses.replace(cat, impact_table=it)
    params = dataclasses.replace(mod.params(), years=years)
    draws = SeededDraws(SEED, R=R_DIFF, shapes=DrawShapes.for_catalog(cat, 0), block_size=block_size, years=years)
    ref = {}
    for r in range(R_DIFF):
        try:
            ReferenceRun(cat, ic, DynamicsSpec([]), params, draws, r).run()
        except ImpactOutOfRange as exc:
            ref[r] = (exc.year, exc.row, exc.contribution)
    assert ref and len(ref) < R_DIFF
    fm, fr = FactorModel.from_catalog(cat), FiringModel(cat)
    raised = 0
    for b in range(draws.n_blocks):
        start, stop = draws.block_rows(b)
        rb = stop - start
        stream = draws.stream(b)
        thr = fr.thresholds(stream.init["t2_offset"])
        mem = MemoryModel(cat, rb, run_offset=start)
        led = ImpactLedger(cat, rb, run_offset=start, max_active=params.max_active, epsilon_cull=params.epsilon_cull)
        country, global_ = _block_state(ic, rb)
        block_ref = {r: v for r, v in ref.items() if start <= r < stop}
        first = min((v[0] for v in block_ref.values()), default=None)
        try:
            for t in range(years):
                _step(cat, fm, fr, mem, led, thr, stream.year(t), params.start_year + t, country, global_)
        except ImpactOutOfRange as exc:
            raised += 1
            want = sorted(r for r, v in block_ref.items() if v[0] == first)
            assert (exc.run_index, exc.year) == (want, first), b
            _, row, contribution = block_ref[want[0]]
            assert exc.row == row
            np.testing.assert_allclose(exc.contribution, contribution, rtol=1e-9, atol=0)
        else:
            assert first is None, b
    assert raised > 0
