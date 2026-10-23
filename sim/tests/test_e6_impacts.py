"""E6 gates (implementation guide §3): the active-shock ledger on hand-built one-entity catalogs.

(a) a single decaying shock follows the closed-form half-life to rtol 1e-9 and, in the epsilon-cull year,
    returns to exactly the no-shock value and frees its slot; (b) ``permanent`` + ``immediate`` occupies no slot,
    a ramped ``permanent`` holds one until its ramp completes and keeps its level; (c) delayed and gradual onset
    follow the README §3 table year by year; (d) ``until: resolved`` holds for ``resolves_after`` years, then
    drops to 0, and re-firing restarts the window; (e) a decaying multiplicative shock returns the state to its
    no-shock path, a contribution ≤ −1 raises ``ImpactOutOfRange`` naming runs, year and row; (f) overflow at
    ``max_active + 1`` live shocks raises ``LedgerOverflow`` naming runs and year, ``max_active`` does not;
    (g) dtypes and shapes.

Each scenario drives the ledger directly (step 5 → 6 → 8 per year, codes from ``draw_codes``) and, through
``_both``, also runs the reference engine on the same catalog with scripted draws and no dynamics, asserting
the two agree before the closed form is checked. Type 1 events with ``p_annual`` .5 and no loadings fire where
ε = −10 (U ≈ 0) and not where ε = +10.
"""
import math

import numpy as np
import pytest

from sim.catalog.types import (CompiledCatalog, DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED, ONSET_DELAYED,
                               ONSET_GRADUAL, ONSET_IMMEDIATE)
from sim.engine import MAX_ACTIVE, ImpactLedger, draw_codes
from sim.reference import DynamicsSpec, ImpactOutOfRange, InitialConditions, LedgerOverflow, ReferenceRun, SimParams
from sim.rng import DrawShapes, ScriptedDraws
from sim.tests.fixtures import builders as B

START = 2025
X, V, GDP, G = 0, 0, 1, 0          # entity x; country vars v (additive), gdp_real (multiplicative); global g
IC_COUNTRY = np.array([[100.0, 50.0]])
IC_GLOBAL = np.array([0.0])
EPS = SimParams.epsilon_cull


def _row(M, var=V, onset=(ONSET_IMMEDIATE, 0), dur=(DUR_DECAY, 2.0), event=0, res=0, std=0.0, mult=False, glob=False):
    return (event, res, 0, B.GLOBAL if glob else X, var, M, std, onset[0], onset[1], dur[0], dur[1], mult)


def _catalog(rows, resolves_after=(0,), trees=None):
    E = len(resolves_after)
    sc = B.state_catalog(["F"], ["x"], ["v", "gdp_real"], ["g"])
    idx = B.index_for(sc, [f"E{i}" for i in range(E)])
    return CompiledCatalog(event_ids=[f"E{i}" for i in range(E)], lam=np.zeros((E, 1)), sigma_idio=np.ones(E),
                           causal_type=np.ones(E, dtype=np.int8), p_annual=np.full(E, 0.5), type2={}, type3={},
                           resolution_tree=trees or [B.default_tree()] * E, impact_table=B.impact_rows(rows),
                           cascade_edges=[], index=idx, omega=np.eye(1),
                           resolves_after=np.array(resolves_after, dtype=np.int64), meta={})


def _fired(cat, fire, R, t):
    """fire: iterable of (run, year index, event)."""
    out = np.zeros((R, cat.n_events), dtype=bool)
    for r, tt, e in fire:
        if tt == t:
            out[r, e] = True
    return out


def _z(cat, R, T, impact_z):
    n = len(cat.impact_table)
    z = np.zeros((T, R, n)) if impact_z is None else np.broadcast_to(np.asarray(impact_z, dtype=np.float64), (T, R, n))
    return z


def _drive(cat, fire, T, R=1, impact_z=None, run_offset=0, max_active=MAX_ACTIVE, res_u=0.5):
    """The ledger alone over T years; returns per-year post-step-6 state, live counts, flags, draws, and the ledger."""
    led = ImpactLedger(cat, R, run_offset=run_offset, max_active=max_active)
    country = np.tile(IC_COUNTRY, (R, 1, 1))
    global_ = np.tile(IC_GLOBAL, (R, 1))
    z = _z(cat, R, T, impact_z)
    res, br = draw_codes(cat, np.broadcast_to(res_u, (R, cat.n_events)), np.full((R, cat.n_events), 0.5))
    out = dict(country=[], global_=[], live=[], flags=[], until=[], draws=[])
    for t in range(T):
        year = START + t
        draw = led.resolve(_fired(cat, fire, R, t), res, br, z[t], year)
        led.apply(country, global_, year)
        led.end_of_year(year)
        out["country"].append(country.copy())
        out["global_"].append(global_.copy())
        out["live"].append(led.n_live.copy())
        out["flags"].append(led.event_active.copy())
        out["until"].append(led.active_until.copy())
        out["draws"].append(draw)
    return {k: (np.array(v) if k != "draws" else v) for k, v in out.items()}, led


def _reference_draws(cat, fire, T, R, impact_z, res_u=0.5):
    shapes = DrawShapes.for_catalog(cat, 0)
    z = _z(cat, R, T, impact_z)
    years = [{"factor": np.zeros((R, 1)), "idio": np.where(_fired(cat, fire, R, t), -10.0, 10.0),
              "res_u": np.broadcast_to(res_u, (R, cat.n_events)).copy(), "branch_u": np.full((R, cat.n_events), 0.5),
              "impact_z": z[t].copy(), "dyn_z": np.zeros((R, 0))} for t in range(T)]
    return ScriptedDraws({"t2_offset": np.zeros((R, 0))}, years, shapes)


def _reference(cat, fire, T, R=1, impact_z=None, max_active=MAX_ACTIVE, res_u=0.5, r=0):
    draws = _reference_draws(cat, fire, T, R, impact_z, res_u)
    run = ReferenceRun(cat, InitialConditions(IC_COUNTRY.copy(), IC_GLOBAL.copy()), DynamicsSpec([]),
                       SimParams(start_year=START, years=T, max_active=max_active), draws, r)
    return run.run(), run


def _both(cat, fire, T, R=1, impact_z=None, max_active=MAX_ACTIVE, res_u=0.5):
    """Drive the ledger and the reference; assert they agree on state (rtol 1e-9) and magnitudes."""
    out, led = _drive(cat, fire, T, R, impact_z, max_active=max_active, res_u=res_u)
    for r in range(R):
        rec, _ = _reference(cat, fire, T, R, impact_z, max_active, res_u, r)
        np.testing.assert_allclose(out["country"][:, r], rec.country[1:], rtol=1e-9, atol=0)
        np.testing.assert_allclose(out["global_"][:, r], rec.global_[1:], rtol=1e-9, atol=0)
        for ev in rec.events:
            got = out["draws"][ev.year - START].for_firing(r, ev.event)
            assert [j for j, _ in got] == [j for j, _ in ev.magnitudes]
            np.testing.assert_allclose([m for _, m in got], [m for _, m in ev.magnitudes], rtol=1e-9, atol=0)
        assert rec.max_active_seen == out["live"][:, r].max()
    return out, led


def _readme_contribution(M, onset, n, dur, h, age, owner_active=True):
    """README §3 table, written out independently of the engine."""
    if onset == ONSET_IMMEDIATE:
        ramp, end = 1.0, 0
    elif onset == ONSET_DELAYED:
        ramp, end = (0.0 if age < n else 1.0), n
    else:
        ramp, end = min(age + 1, n) / n, n - 1
    if dur == DUR_UNTIL_RESOLVED:
        return M * ramp if owner_active else 0.0
    if dur == DUR_PERMANENT or age <= end:
        return M * ramp
    return M * ramp * 0.5 ** ((age - end) / h)


def _cull_age(M, onset, n, h):
    end = {ONSET_IMMEDIATE: 0, ONSET_DELAYED: n, ONSET_GRADUAL: n - 1}[onset]
    age = end + 1
    while abs(_readme_contribution(M, onset, n, DUR_DECAY, h, age)) >= EPS * abs(M):
        age += 1
    return age


# ------------------------------------------------------------------ (a) decay ----
def test_e6_decay_matches_closed_form_half_life_and_culls_to_the_no_shock_value():
    M, h = -10.0, 2.0
    cull = _cull_age(M, ONSET_IMMEDIATE, 0, h)
    assert cull == math.ceil(h * math.log2(1.0 / EPS) + 1e-12)                  # 27: 0.5^(27/2) < 1e-4 ≤ 0.5^(26/2)
    T = cull + 3
    out, led = _both(_catalog([_row(M, dur=(DUR_DECAY, h))]), [(0, 0, 0)], T)
    want = [100.0 + M * 0.5 ** (t / h) if t < cull else 100.0 for t in range(T)]
    np.testing.assert_allclose(out["country"][:, 0, X, V], want, rtol=1e-9, atol=0)
    assert out["live"][:, 0].tolist() == [1] * cull + [0] * (T - cull)
    assert abs(out["country"][cull - 1, 0, X, V] - 100.0) == pytest.approx(10 * 0.5 ** (26 / 2), rel=1e-9)
    assert not led.active.any() and (out["country"][:, 0, X, GDP] == 50.0).all()


def test_e6_epsilon_cull_returns_exactly_to_zero():
    # powers of two: every contribution and increment is exact, so the cull year must give exactly 100.0
    M = -8.0
    cull = _cull_age(M, ONSET_IMMEDIATE, 0, 1.0)
    assert cull == 14                                                             # 2^-14 < 1e-4 ≤ 2^-13
    out, _ = _both(_catalog([_row(M, dur=(DUR_DECAY, 1.0))]), [(0, 0, 0)], cull + 2)
    v = out["country"][:, 0, X, V]
    assert v[:cull].tolist() == [100.0 + M * 2.0 ** -t for t in range(cull)]
    assert v[cull] == 100.0 and v[cull + 1] == 100.0
    assert out["live"][:, 0].tolist() == [1] * cull + [0, 0]


# -------------------------------------------------------------- (b) permanent ----
def test_e6_permanent_immediate_takes_no_slot():
    cat = _catalog([_row(5.0, var=G, glob=True, dur=(DUR_PERMANENT, math.nan))])
    out, _ = _both(cat, [(0, 0, 0), (0, 2, 0)], 4)
    assert out["global_"][:, 0, G].tolist() == [5.0, 5.0, 10.0, 10.0]
    assert out["live"][:, 0].tolist() == [0, 0, 0, 0]


@pytest.mark.parametrize("onset,n,want,live", [
    ((ONSET_GRADUAL, 4), 4, [102.0, 104.0, 106.0, 108.0, 108.0, 108.0], [1, 1, 1, 0, 0, 0]),
    ((ONSET_DELAYED, 2), 2, [100.0, 100.0, 108.0, 108.0, 108.0, 108.0], [1, 1, 0, 0, 0, 0]),
], ids=["gradual-4", "delayed-2"])
def test_e6_ramped_permanent_holds_a_slot_until_onset_completes_then_keeps_its_level(onset, n, want, live):
    out, _ = _both(_catalog([_row(8.0, onset=onset, dur=(DUR_PERMANENT, math.nan))]), [(0, 0, 0)], 6)
    np.testing.assert_allclose(out["country"][:, 0, X, V], want, rtol=1e-9, atol=0)
    assert out["live"][:, 0].tolist() == live


def test_e6_zero_magnitude_takes_no_slot():
    cat = _catalog([_row(1.0, std=1.0, dur=(DUR_DECAY, 5.0))])
    out, _ = _both(cat, [(0, 0, 0)], 3, impact_z=[-1.0])                             # M = 1 + 1·(−1) = 0
    assert out["draws"][0].for_firing(0, 0) == [(0, 0.0)]                          # still recorded in the log
    assert out["live"][:, 0].tolist() == [0, 0, 0] and (out["country"][:, 0, X, V] == 100.0).all()


# ------------------------------------------------------------------ (c) onset ----
@pytest.mark.parametrize("onset,n,first", [
    (ONSET_DELAYED, 3, [0, 0, 0, 8, 4, 2, 1]),
    (ONSET_GRADUAL, 4, [2, 4, 6, 8, 4, 2, 1]),
    (ONSET_GRADUAL, 1, [8, 4, 2, 1, 0.5, 0.25, 0.125]),
    (ONSET_DELAYED, 0, [8, 4, 2, 1, 0.5, 0.25, 0.125]),
    (ONSET_IMMEDIATE, 0, [8, 4, 2, 1, 0.5, 0.25, 0.125]),
], ids=["delayed-3", "gradual-4", "gradual-1", "delayed-0", "immediate"])
def test_e6_onset_schedule_follows_the_readme_table(onset, n, first):
    M, h = 8.0, 1.0
    cull = _cull_age(M, onset, n, h)
    T = cull + 2
    out, _ = _both(_catalog([_row(M, onset=(onset, n), dur=(DUR_DECAY, h))]), [(0, 0, 0)], T)
    contrib = out["country"][:, 0, X, V] - 100.0
    assert contrib[:7].tolist() == first                                           # exact in binary
    want = [_readme_contribution(M, onset, n, DUR_DECAY, h, a) if a < cull else 0.0 for a in range(T)]
    np.testing.assert_allclose(contrib, want, rtol=1e-9, atol=1e-12)
    # a delayed shock is never culled during its delay (contribution 0 < eps·|M| there): the slot is held
    assert out["live"][:, 0].tolist() == [1] * cull + [0] * (T - cull)


def test_e6_gradual_until_resolved_ramps_while_owner_active():
    cat = _catalog([_row(9.0, onset=(ONSET_GRADUAL, 3), dur=(DUR_UNTIL_RESOLVED, math.nan))], resolves_after=(5,))
    out, _ = _both(cat, [(0, 0, 0)], 7)
    np.testing.assert_allclose(out["country"][:, 0, X, V] - 100.0, [3, 6, 9, 9, 9, 0, 0], rtol=1e-12, atol=1e-12)
    assert out["live"][:, 0].tolist() == [1, 1, 1, 1, 1, 0, 0]


# --------------------------------------------------------- (d) until: resolved ----
@pytest.mark.parametrize("fire_at,resolves_after,want,flags", [
    ([0], 3, [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0]),
    ([0], 1, [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]),
    ([0, 2], 3, [1, 1, 2, 2, 2, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]),     # re-fire while active: window restarts
    ([0, 3], 3, [1, 1, 1, 2, 2, 2, 0, 0], [1, 1, 0, 1, 1, 0, 0, 0]),     # step 5 re-activates before step 6 reads
    ([0, 4], 3, [1, 1, 1, 0, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0]),     # gap: the first shock is gone at t = 3
], ids=["once", "resolves-after-1", "refire-inside", "refire-adjacent", "refire-after-gap"])
def test_e6_until_resolved_holds_for_the_window_and_refiring_restarts_it(fire_at, resolves_after, want, flags):
    cat = _catalog([_row(1.0, var=G, glob=True, dur=(DUR_UNTIL_RESOLVED, math.nan))], resolves_after=(resolves_after,))
    T = 8
    out, led = _both(cat, [(0, t, 0) for t in fire_at], T)
    assert out["global_"][:, 0, G].tolist() == want
    assert out["flags"][:, 0, 0].astype(int).tolist() == flags                   # after step 8
    assert out["until"][-1, 0, 0] == START + fire_at[-1] + resolves_after - 1
    assert out["live"][:, 0].tolist() == want                                    # M = 1: one slot per unit
    _, run = _reference(cat, [(0, t, 0) for t in fire_at], T)
    assert led.event_active[0].tolist() == run.active.tolist()
    assert led.active_until[0].tolist() == run.active_until.tolist()


# ------------------------------------------------------- (e) multiplicative ----
def test_e6_multiplicative_decay_returns_to_the_no_shock_path():
    M = -0.2
    cull = _cull_age(M, ONSET_IMMEDIATE, 0, 1.0)
    T = cull + 2
    cat = _catalog([_row(M, var=GDP, dur=(DUR_DECAY, 1.0), mult=True)])
    out, _ = _both(cat, [(0, 0, 0)], T)
    want = [50.0 * (1.0 + M * 0.5 ** t) if t < cull else 50.0 for t in range(T)]
    np.testing.assert_allclose(out["country"][:, 0, X, GDP], want, rtol=1e-9, atol=0)
    assert out["live"][:, 0].tolist() == [1] * cull + [0, 0]


def test_e6_overlapping_multiplicative_shocks_compose_by_product():
    M = -0.2
    cat = _catalog([_row(M, var=GDP, dur=(DUR_DECAY, 1.0), mult=True), _row(3.0, dur=(DUR_DECAY, 1.0))])
    out, _ = _both(cat, [(0, 0, 0), (0, 1, 0)], 6)
    for t in range(6):
        c0, c1 = M * 0.5 ** t, (M * 0.5 ** (t - 1) if t >= 1 else 0.0)
        assert out["country"][t, 0, X, GDP] == pytest.approx(50.0 * (1 + c0) * (1 + c1), rel=1e-9)
        a0, a1 = 3.0 * 0.5 ** t, (3.0 * 0.5 ** (t - 1) if t >= 1 else 0.0)
        assert out["country"][t, 0, X, V] == pytest.approx(100.0 + a0 + a1, rel=1e-9)


@pytest.mark.parametrize("run_offset", [0, 100])
def test_e6_multiplicative_contribution_at_or_below_minus_one_raises(run_offset):
    rows = [_row(1.0, dur=(DUR_DECAY, 1.0)), _row(-0.5, var=GDP, std=0.5, dur=(DUR_DECAY, 1.0), mult=True)]
    cat = _catalog(rows)
    R = 3
    z = np.array([[0.0, -1.0], [0.0, 0.0], [0.0, -3.0]])                        # M = −1.0, −0.5, −2.0
    fire = [(r, 1, 0) for r in range(R)]
    led = ImpactLedger(cat, R, run_offset=run_offset)
    country, global_ = np.tile(IC_COUNTRY, (R, 1, 1)), np.tile(IC_GLOBAL, (R, 1))
    res, br = draw_codes(cat, np.full((R, 1), 0.5), np.full((R, 1), 0.5))
    led.resolve(_fired(cat, fire, R, 0), res, br, z, START)
    led.apply(country, global_, START)
    led.end_of_year(START)
    led.resolve(_fired(cat, fire, R, 1), res, br, z, START + 1)
    before = country.copy()
    with pytest.raises(ImpactOutOfRange) as exc:
        led.apply(country, global_, START + 1)
    assert exc.value.run_index == [run_offset, run_offset + 2] and exc.value.year == START + 1
    assert exc.value.row == 1 and exc.value.contribution == -1.0
    assert "year 2026" in str(exc.value) and "row 1" in str(exc.value)
    assert (country == before).all()                                              # nothing applied before the raise
    for r, M in ((0, -1.0), (2, -2.0)):
        with pytest.raises(ImpactOutOfRange) as ref:
            _reference(cat, fire, 3, R, z, r=r)
        assert (ref.value.run_index, ref.value.year, ref.value.row, ref.value.contribution) == (r, START + 1, 1, M)
    _reference(cat, fire, 3, R, z, r=1)                                           # −0.5 is in range


def test_e6_multiplicative_range_is_checked_when_a_delayed_onset_arrives():
    cat = _catalog([_row(-1.5, var=GDP, onset=(ONSET_DELAYED, 2), dur=(DUR_DECAY, 1.0), mult=True)])
    with pytest.raises(ImpactOutOfRange) as exc:
        _drive(cat, [(0, 0, 0)], 4)
    assert exc.value.run_index == [0] and exc.value.year == START + 2 and exc.value.row == 0
    out, _ = _both(_catalog([_row(-0.999, var=GDP, dur=(DUR_DECAY, 1.0), mult=True)]), [(0, 0, 0)], 2)
    assert out["country"][0, 0, X, GDP] == pytest.approx(50.0 * 0.001, rel=1e-9)  # just inside the bound


# ------------------------------------------------------------- (f) overflow ----
def _decaying_rows(n):
    return [_row(1.0, dur=(DUR_DECAY, 50.0)) for _ in range(n)]


def test_e6_max_active_live_shocks_fit():
    out, led = _both(_catalog(_decaying_rows(MAX_ACTIVE)), [(0, 0, 0)], 2)
    assert out["live"][:, 0].tolist() == [MAX_ACTIVE, MAX_ACTIVE] and led.active.all()
    assert (led.overflow_count == 0).all()


@pytest.mark.parametrize("run_offset", [0, 128])
def test_e6_overflow_at_max_active_plus_one_names_runs_and_year(run_offset):
    cat = _catalog(_decaying_rows(MAX_ACTIVE + 1))
    with pytest.raises(LedgerOverflow) as exc:
        _drive(cat, [(1, 1, 0)], 3, R=3, run_offset=run_offset)
    assert exc.value.run_index == [1 + run_offset] and exc.value.year == START + 1
    assert exc.value.count == MAX_ACTIVE + 1 and exc.value.max_active == MAX_ACTIVE
    assert "year 2026" in str(exc.value)
    with pytest.raises(LedgerOverflow) as ref:
        _reference(cat, [(1, 1, 0)], 3, R=3, r=1)
    assert (ref.value.run_index, ref.value.year, ref.value.count) == (1, START + 1, MAX_ACTIVE + 1)


def test_e6_overflow_counts_live_shocks_across_years():
    cat = _catalog(_decaying_rows(3))
    fire = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (2, 0, 0), (2, 1, 0)]
    with pytest.raises(LedgerOverflow) as exc:
        _drive(cat, fire, 3, R=3, max_active=4)
    assert exc.value.run_index == [0, 2] and exc.value.year == START + 1 and exc.value.count == 6
    led = ImpactLedger(cat, 3, max_active=4)
    country, global_ = np.tile(IC_COUNTRY, (3, 1, 1)), np.tile(IC_GLOBAL, (3, 1))
    res, br = draw_codes(cat, np.full((3, 1), 0.5), np.full((3, 1), 0.5))
    for t in range(2):
        led.resolve(_fired(cat, fire, 3, t), res, br, np.zeros((3, 3)), START + t)
        try:
            led.apply(country, global_, START + t)
        except LedgerOverflow:
            pass
    assert led.overflow_count.tolist() == [2, 0, 2]


def test_e6_slots_freed_this_year_count_before_the_overflow_check():
    # two ramped permanents freed at age 1, two more pushed the same year: 2 live ≤ 2 (4 if counted before frees)
    cat = _catalog([_row(1.0, onset=(ONSET_GRADUAL, 2), dur=(DUR_PERMANENT, math.nan))] * 2)
    out, _ = _both(cat, [(0, 0, 0), (0, 1, 0)], 3, max_active=2)
    assert out["live"][:, 0].tolist() == [2, 2, 0]
    np.testing.assert_allclose(out["country"][:, 0, X, V], [101.0, 103.0, 104.0], rtol=1e-12)


def test_e6_freed_slots_are_recycled():
    cat = _catalog(_decaying_rows(2) + [_row(1.0, onset=(ONSET_GRADUAL, 2), dur=(DUR_PERMANENT, math.nan), event=1)],
                   resolves_after=(0, 0))
    fire = [(0, t, 1) for t in range(6)] + [(0, 0, 0)]
    out, led = _both(cat, fire, 6, max_active=3)                                 # each year frees one, pushes one
    assert out["live"][:, 0].tolist() == [3, 3, 3, 3, 3, 3]


# ---------------------------------------------------------- selection / API ----
def test_e6_selection_follows_resolution_codes_and_draws_every_row():
    tree = B.tree([("bad", 0.5, [("default", 1.0)]), ("good", 0.5, [("default", 1.0)])])
    rows = [_row(-2.0, std=1.0, res=0), _row(3.0, var=G, glob=True, res=0, std=2.0), _row(7.0, res=1, std=0.5)]
    cat = _catalog(rows, trees=[tree])
    z = np.array([[1.0, -1.0, 2.0], [0.5, 0.5, 0.5]])
    res_u = np.array([[0.2], [0.8]])                                              # run 0 'bad', run 1 'good'
    out, _ = _both(cat, [(0, 0, 0), (1, 0, 0)], 2, R=2, impact_z=z, res_u=res_u)
    d = out["draws"][0]
    assert d.selected.tolist() == [[True, True, False], [False, False, True]]
    np.testing.assert_array_equal(d.magnitude, [[-1.0, 1.0, 8.0], [-1.5, 4.0, 7.25]])
    assert d.for_firing(0, 0) == [(0, -1.0), (1, 1.0)] and d.for_firing(1, 0) == [(2, 7.25)]
    assert out["draws"][1].selected.sum() == 0


def test_e6_apply_requires_this_years_resolve_and_float64_state():
    cat = _catalog([_row(1.0)])
    led = ImpactLedger(cat, 1)
    country, global_ = IC_COUNTRY[None].copy(), IC_GLOBAL[None].copy()
    with pytest.raises(RuntimeError, match="resolve"):
        led.apply(country, global_, START)
    zero = np.zeros((1, 1), dtype=np.int64)
    led.resolve(np.zeros((1, 1), dtype=bool), zero, zero, np.zeros((1, 1)), START)
    with pytest.raises(ValueError, match="float64"):
        led.apply(country.astype(np.float32), global_, START)


# --------------------------------------------------------------- (g) dtypes ----
def test_e6_dtypes_and_shapes():
    rows = [_row(1.0), _row(2.0, var=G, glob=True, dur=(DUR_UNTIL_RESOLVED, math.nan), event=1)]
    cat = _catalog(rows, resolves_after=(0, 2))
    R, params = 5, SimParams(max_active=7)
    led = ImpactLedger(cat, R, max_active=params.max_active, epsilon_cull=params.epsilon_cull)
    zero = np.zeros((R, 2), dtype=np.int64)
    d = led.resolve(np.ones((R, 2), dtype=bool), zero, zero, np.zeros((R, 2)), START)
    led.apply(np.tile(IC_COUNTRY, (R, 1, 1)), np.tile(IC_GLOBAL, (R, 1)), START)
    led.end_of_year(START)
    assert d.selected.dtype == bool and d.selected.shape == (R, 2)
    assert d.magnitude.dtype == np.float64 and d.magnitude.shape == (R, 2)
    for name, dt in (("active", bool), ("entity_idx", np.int16), ("var_idx", np.int16), ("magnitude", np.float64),
                     ("onset_kind", np.int8), ("onset_years", np.int8), ("dur_kind", np.int8),
                     ("dur_param", np.float64), ("age", np.int16), ("owner_event", np.int16), ("row", np.int32),
                     ("prev", np.float64), ("mult", bool)):
        a = getattr(led, name)
        assert a.dtype == dt and a.shape == (R, params.max_active), name
    assert led.event_active.dtype == bool and led.event_active.shape == (R, 2)
    assert led.active_until.dtype == np.int64 and led.active_until.shape == (R, 2)
    assert led.overflow_count.dtype == np.int64 and led.overflow_count.shape == (R,)
    assert led.n_live.dtype == np.int64 and led.n_live.tolist() == [2] * R
    assert led.epsilon_cull == params.epsilon_cull == 1e-4
    assert ImpactLedger(cat, R).max_active == MAX_ACTIVE == SimParams().max_active
    assert led.row[0, :2].tolist() == [0, 1] and led.owner_event[0, :2].tolist() == [0, 1]
