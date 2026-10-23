"""E1 gate: the scalar reference implementation reproduces FIX-A exactly and FIX-B's hand-traced event log."""
import numpy as np
import pytest

from sim.reference import ReferenceRun, LedgerOverflow, SimParams
from sim.tests.fixtures import fix_a, fix_b


def _event_dicts(rec):
    return [dict(year=e.year, event=e.event, resolution=e.resolution, branch=e.branch, p_base=e.p_base,
                 p_eff=e.p_eff, cascade_mask=e.cascade_mask, magnitudes=e.magnitudes) for e in rec.events]


def _assert_events(got, want):
    assert len(got) == len(want), (got, want)
    for g, w in zip(got, want):
        for k in ("year", "event", "resolution", "branch", "cascade_mask"):
            assert g[k] == w[k], (k, g, w)
        assert g["p_base"] == pytest.approx(w["p_base"], rel=1e-12)
        assert g["p_eff"] == pytest.approx(w["p_eff"], rel=1e-12)
        assert [m[0] for m in g["magnitudes"]] == [m[0] for m in w["magnitudes"]]
        np.testing.assert_allclose([m[1] for m in g["magnitudes"]], [m[1] for m in w["magnitudes"]], rtol=1e-12)


def test_fix_a_matches_hand_trace():
    cat = fix_a.catalog()
    rec = ReferenceRun(cat, fix_a.initial_conditions(), fix_a.dynamics(), fix_a.params(), fix_a.draws(), 0).run()
    want = fix_a.expected()
    _assert_events(_event_dicts(rec), want["events"])
    ia, ib = cat.index.entity["a"], cat.index.entity["b"]
    for t, w in enumerate(want["trajectory"]):
        np.testing.assert_allclose(rec.country[t + 1, ia], w["a"], rtol=1e-12)
        np.testing.assert_allclose(rec.country[t + 1, ib], w["b"], rtol=1e-12)
        assert rec.global_[t + 1, 0] == pytest.approx(w["oil"], rel=1e-12)
    # the copula uniform in the firing year is Φ(-1.6), elsewhere Φ(0.8)
    from scipy.special import ndtr
    assert rec.propensity_u[1, 0] == pytest.approx(ndtr(-1.6))
    assert rec.propensity_u[0, 0] == pytest.approx(ndtr(0.8))
    assert rec.max_active_seen == 2          # the two decaying shocks hold a slot each; the permanent one none
    # the multiplicative row leaves gdp_per_capita at 0.9 × its no-shock compounding path only at age 0; by the end
    # of the horizon the ratio to the no-shock path is (1 + c(3)) = 0.9875 — decay is recovery for both row kinds
    ia = cat.index.entity["a"]
    base = 50.0
    for t, w in enumerate(want["trajectory"]):
        base *= 1.0 + w["a"][1] / 100.0
    assert rec.country[-1, ia, 0] / base == pytest.approx(1.0 - 0.10 * 0.5 ** 3, rel=1e-12)


def test_fix_b_matches_hand_trace():
    cat = fix_b.catalog()
    rec = ReferenceRun(cat, fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params(), fix_b.draws(), 0).run()
    want = fix_b.expected()
    _assert_events(_event_dicts(rec), want["events"])
    gdp = cat.index.country_var["gdp"]; stress = cat.index.country_var["stress"]
    temp = cat.index.global_var["temp"]; conf = cat.index.global_var["conflicts"]
    np.testing.assert_allclose(rec.country[1:, 0, gdp], want["gdp"], rtol=1e-12)
    np.testing.assert_allclose(rec.country[1:, 0, stress], want["stress"], rtol=1e-12)
    np.testing.assert_allclose(rec.global_[1:, temp], want["temp"], rtol=1e-12)
    np.testing.assert_allclose(rec.global_[1:, conf], want["conflicts"], rtol=1e-12)
    assert rec.gate[:, 2].tolist() == want["gate_t3"]
    np.testing.assert_allclose(rec.p_eff[:, 2], want["p_eff_t3"], rtol=1e-12)


def test_ledger_overflow_is_a_loud_failure():
    # FIX-B holds one slot from 2026 (gdp decay) and a second from 2028 (conflicts until-resolved)
    p = SimParams(start_year=2025, years=fix_b.YEARS, max_active=1)
    with pytest.raises(LedgerOverflow) as ei:
        ReferenceRun(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), p, fix_b.draws(), 0).run()
    assert ei.value.run_index == 0 and ei.value.year == 2028 and ei.value.count == 2


def test_multiplicative_contribution_at_or_below_minus_one_is_a_loud_failure():
    from sim.reference import ImpactOutOfRange
    cat = fix_a.catalog()
    cat.impact_table["mean"][2] = -1.0          # a -100% fraction-of-current-value shock
    with pytest.raises(ImpactOutOfRange) as ei:
        ReferenceRun(cat, fix_a.initial_conditions(), fix_a.dynamics(), fix_a.params(), fix_a.draws(), 0).run()
    assert (ei.value.run_index, ei.value.year, ei.value.row) == (0, 2026, 2)


def test_resolves_after_is_per_event_and_counts_the_firing_year():
    """T3 fires in 2028 with resolves_after = 2: conflicts holds through 2029 and is 0 from 2030 (FIX-B trace).
    With resolves_after = 1 the shock lasts the firing year only; with 3 it holds through 2030."""
    for n, want in ((1, [0, 0, 0, 1, 0, 0]), (2, [0, 0, 0, 1, 1, 0]), (3, [0, 0, 0, 1, 1, 1])):
        cat = fix_b.catalog()
        cat.resolves_after = np.array([0, 0, n])
        rec = ReferenceRun(cat, fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params(), fix_b.draws(), 0).run()
        assert rec.global_[1:, cat.index.global_var["conflicts"]].tolist() == want, n


@pytest.mark.parametrize("half_life", [0.0, -1.0, float("nan"), float("inf")])
def test_mean_revert_half_life_must_be_finite_and_positive(half_life):
    from sim.reference import VarDynamics
    with pytest.raises(ValueError, match="'a.gdp_growth'.*half_life"):
        VarDynamics("a.gdp_growth", "mean_revert", mu=2.0, half_life=half_life)


@pytest.mark.parametrize("kind", ["mean_revert", "additive"])
def test_dynamics_sigma_must_be_non_negative(kind):
    from sim.reference import VarDynamics
    with pytest.raises(ValueError, match="'oil_brent'.*sigma"):
        VarDynamics("oil_brent", kind, mu=75.0, half_life=2.0, sigma=-0.5)


def test_dynamics_duplicate_key_is_rejected():
    from sim.reference import DynamicsSpec, VarDynamics
    with pytest.raises(ValueError, match="'oil_brent'.*duplicate"):
        DynamicsSpec([VarDynamics("oil_brent", "mean_revert", mu=75.0, half_life=2.0),
                      VarDynamics("a.gdp_growth", "mean_revert", mu=2.0),
                      VarDynamics("oil_brent", "additive", rate=1.0)])


# ---- Recording (ADR-9): scenario flags and RecordingSpec, reference first ---------------------------------------

def _flag(name, names, fn, min_years):
    from sim.reference import ScenarioFlag
    from sim.tests.fixtures import builders as B
    return ScenarioFlag(name, B.expr(names, fn, "boolean"), min_years)


def _fix_b_flags(years, flags):
    from sim.reference import RecordingSpec
    p = SimParams(start_year=2025, years=years)
    rec = ReferenceRun(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), p, fix_b.draws(), 0,
                       RecordingSpec(scenario_flags=flags)).run()
    return rec.scenario_flags.tolist()


def test_scenario_flag_becomes_true_in_the_hand_computed_year():
    """FIX-B's end-of-year x.stress is 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 (t = 0..5). ``x.stress > 1.2`` holds from the
    end of t = 2, so a 2-year flag is set at the end of t = 3 (2028): false after 3 years, true after 4; a 4-year
    flag at t = 5 (2030). Flags are evaluated on end-of-year state: on start-of-year state (0, 0.5, ..., 2.5) the
    2-year flag would be set a year later (2029) and ``x.stress > 2.2`` for 2 years would never be set within the
    horizon, whereas on end-of-year state it is set at t = 5."""
    stress2 = _flag("stress2", ["x.stress"], lambda ns: ns["x.stress"] > 1.2, 2)
    stress4 = _flag("stress4", ["x.stress"], lambda ns: ns["x.stress"] > 1.2, 4)
    late2 = _flag("late2", ["x.stress"], lambda ns: ns["x.stress"] > 2.2, 2)
    assert _fix_b_flags(3, [stress2, stress4, late2]) == [False, False, False]
    assert _fix_b_flags(4, [stress2, stress4, late2]) == [True, False, False]
    assert _fix_b_flags(5, [stress2, stress4, late2]) == [True, False, False]
    assert _fix_b_flags(6, [stress2, stress4, late2]) == [True, True, True]


def test_scenario_flag_reads_factors_and_resets_when_the_condition_fails():
    """FG is 1.5 in t = 0..3 and 0 in t = 4..5: ``FG > 1.0`` for 4 years is set at t = 3 (2028) and stays set;
    for 5 years it is never set, because the counter resets to 0 at t = 4. A flag mixing a factor and a state
    variable (``FG > 1.0 and x.stress > 0.7``) holds in t = 1..3 only: set for 3 years, never for 4."""
    fg4 = _flag("fg4", ["FG"], lambda ns: ns["FG"] > 1.0, 4)
    fg5 = _flag("fg5", ["FG"], lambda ns: ns["FG"] > 1.0, 5)
    mix3 = _flag("mix3", ["FG", "x.stress"], lambda ns: (ns["FG"] > 1.0) & (ns["x.stress"] > 0.7), 3)
    mix4 = _flag("mix4", ["FG", "x.stress"], lambda ns: (ns["FG"] > 1.0) & (ns["x.stress"] > 0.7), 4)
    assert _fix_b_flags(3, [fg4, fg5, mix3, mix4]) == [False, False, False, False]
    assert _fix_b_flags(4, [fg4, fg5, mix3, mix4]) == [True, False, True, False]
    assert _fix_b_flags(6, [fg4, fg5, mix3, mix4]) == [True, False, True, False]


def test_scenario_flag_condition_compiles_through_the_expression_compiler():
    """A flag condition is compiled like any catalog expression, names validated against the state catalog and
    event state disallowed (``allow_event_state=False``); the hand trace above then holds for the compiled flag."""
    from sim.catalog.expr import ExprContext, compile_expression
    from sim.catalog.types import CatalogError
    from sim.reference import ScenarioFlag
    sc = fix_b.catalog().meta["state_catalog"]
    ctx = ExprContext(sc, "scenario flag 'stress2'", allow_event_state=False)
    cond = compile_expression("x.stress > 1.2", ctx, "condition", "boolean")
    assert cond.names == ("x.stress",)
    assert _fix_b_flags(4, [ScenarioFlag("stress2", cond, 2)]) == [True]
    assert _fix_b_flags(3, [ScenarioFlag("stress2", cond, 2)]) == [False]
    with pytest.raises(CatalogError, match="unknown name 'years_since'"):
        compile_expression("years_since > 3", ctx, "condition", "boolean")
    with pytest.raises(CatalogError, match="event state names are not available"):
        compile_expression("resolution == 'bad'", ctx, "condition", "boolean")
    with pytest.raises(CatalogError, match="unknown name 'nope'"):
        compile_expression("nope > 1", ctx, "condition", "boolean")


def test_existing_callers_need_no_recording():
    rec = ReferenceRun(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params(), fix_b.draws(), 0).run()
    assert rec.scenario_flags.shape == (0,) and rec.scenario_flags.dtype == bool
    from sim.reference import RecordingSpec, simulate_reference
    assert RecordingSpec() == RecordingSpec([], [], 0)
    recs = simulate_reference(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params(),
                              fix_b.draws(), [0])
    assert len(recs) == 1 and recs[0].scenario_flags.shape == (0,)


def test_scenario_flag_validation_failures():
    from sim.reference import ScenarioFlag
    from sim.tests.fixtures import builders as B
    ok = B.expr(["x.stress"], lambda ns: ns["x.stress"] > 1.2, "boolean")
    with pytest.raises(ValueError, match="'f'.*min_years"):
        ScenarioFlag("f", ok, 0)
    with pytest.raises(ValueError, match="'f'.*min_years"):
        ScenarioFlag("f", ok, 1.5)
    for name in ("resolution", "branch", "years_since"):
        with pytest.raises(ValueError, match=f"'f'.*event state.*{name}"):
            ScenarioFlag("f", B.expr([name, "x.stress"], lambda ns: ns["x.stress"] > 1.2, "boolean"), 1)
    with pytest.raises(ValueError, match="'f'.*boolean"):
        ScenarioFlag("f", B.expr(["x.stress"], lambda ns: ns["x.stress"], "numeric"), 1)
    with pytest.raises(ValueError, match="name"):
        ScenarioFlag("", ok, 1)


def test_recording_spec_validation_failures():
    from sim.reference import RecordingSpec
    a = _flag("a", ["x.stress"], lambda ns: ns["x.stress"] > 1.2, 1)
    b = _flag("a", ["x.gdp"], lambda ns: ns["x.gdp"] < 95, 1)
    with pytest.raises(ValueError, match="duplicate scenario flag name 'a'"):
        RecordingSpec(scenario_flags=[a, b])
    with pytest.raises(ValueError, match="duplicate thin key 'x.gdp'"):
        RecordingSpec(thin_keys=["x.gdp", "temp", "x.gdp"])
    with pytest.raises(ValueError, match="n_full.*-1"):
        RecordingSpec(n_full=-1)
    with pytest.raises(ValueError, match="n_full"):
        RecordingSpec(n_full=2.5)
    assert RecordingSpec(scenario_flags=[a], thin_keys=["x.gdp", "temp"], n_full=3).flag_names == ["a"]


def test_reference_rejects_unknown_flag_names_and_thin_keys():
    from sim.reference import RecordingSpec
    bad = _flag("bad", ["x.nope"], lambda ns: ns["x.nope"] > 1, 1)
    with pytest.raises(KeyError):
        ReferenceRun(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params(), fix_b.draws(), 0,
                     RecordingSpec(scenario_flags=[bad]))
    with pytest.raises(KeyError):
        ReferenceRun(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params(), fix_b.draws(), 0,
                     RecordingSpec(thin_keys=["nope"]))
