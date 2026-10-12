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
