"""E7 gates (implementation guide §3): step 7 dynamics on FIX-A and a hand-built two-entity catalog.

(a) a no-event FIX-A run shows compounding GDP per capita and linear life-expectancy gains matching closed forms
    to rtol 1e-9; (b) a σ = 0 mean-reverting variable displaced from μ, by initial condition and by an E6 shock,
    sits at μ + d · 0.5^(k/h) after k years (the guide's "recovers with specified half-life"); (c) a
    ``gdp_stock`` compounds by post-reversion growth (growth-rate-first), whatever the declaration order;
    (d) σ > 0 noise uses the entry's ``dyn_z`` column, and permuting columns changes exactly the variables it
    should; (e) additive and multiplicative drifts, and phase-2 declaration-order dependence; (f) loud failures;
    (g) dtypes and shapes.

Each scenario runs, through ``_both``, the vectorized modules (``ImpactLedger`` steps 5, 6, 8 around
``DynamicsModel.step``) and the reference engine on the same catalog with scripted draws, asserting the two
agree on state every year (rtol 1e-9) before the closed form or hand value is checked. Type 1 events with
``p_annual`` .5 and no loadings fire where ε = −10 (U ≈ 0) and not where ε = +10; FIX-A's event (p .10,
σ_idio .8) likewise.
"""
import math

import numpy as np
import pytest

from sim.catalog.types import CompiledCatalog, DUR_PERMANENT, ONSET_IMMEDIATE
from sim.engine import DynamicsModel, ImpactLedger, draw_codes
from sim.reference import DynamicsSpec, InitialConditions, ReferenceRun, SimParams, VarDynamics
from sim.rng import DrawShapes, ScriptedDraws
from sim.tests.fixtures import builders as B
from sim.tests.fixtures import fix_a

START = 2025
CVARS = ["g", "gdp", "v", "u"]        # growth (%/yr), stock, two mean-reverting levels
GVARS = ["o", "p"]
X, Y = 0, 1
G, GDP, V, U = range(4)
O, P = range(2)
IC_COUNTRY = np.array([[2.0, 100.0, 10.0, 5.0], [3.0, 40.0, 20.0, 7.0]])
IC_GLOBAL = np.array([75.0, 130.0])


def _catalog(shock=8.0):
    """Entities x, y; one Type 1 event whose single row is a permanent, immediate additive shock to x.v."""
    sc = B.state_catalog(["F"], ["x", "y"], CVARS, GVARS)
    idx = B.index_for(sc, ["E0"])
    rows = B.impact_rows([(0, 0, 0, X, V, shock, 0.0, ONSET_IMMEDIATE, 0, DUR_PERMANENT, math.nan)])
    return CompiledCatalog(event_ids=["E0"], lam=np.zeros((1, 1)), sigma_idio=np.ones(1),
                           causal_type=np.ones(1, dtype=np.int8), p_annual=np.full(1, 0.5), type2={}, type3={},
                           resolution_tree=[B.default_tree()], impact_table=rows, cascade_edges=[], index=idx,
                           omega=np.eye(1), resolves_after=np.zeros(1, dtype=np.int64), meta={})


def _fired(cat, fire, R, t):
    out = np.zeros((R, cat.n_events), dtype=bool)
    for r, tt, e in fire:
        if tt == t:
            out[r, e] = True
    return out


def _dyn_z(dyn, T, R, dyn_z):
    n = len(dyn.noisy_keys)
    return np.zeros((T, R, n)) if dyn_z is None else np.broadcast_to(np.asarray(dyn_z, dtype=np.float64), (T, R, n))


def _drive(cat, ic, dyn, T, R, fire, dyn_z):
    """Steps 5, 6, 7, 8 of the vectorized modules over T years; returns post-step-7 state per year."""
    led = ImpactLedger(cat, R)
    dm = DynamicsModel(cat, dyn)
    country = np.tile(ic.country, (R, 1, 1))
    global_ = np.tile(ic.global_, (R, 1))
    z = _dyn_z(dyn, T, R, dyn_z)
    res, br = draw_codes(cat, np.full((R, cat.n_events), 0.5), np.full((R, cat.n_events), 0.5))
    n_rows = len(cat.impact_table)
    out_c, out_g = [], []
    for t in range(T):
        year = START + t
        led.resolve(_fired(cat, fire, R, t), res, br, np.zeros((R, n_rows)), year)
        led.apply(country, global_, year)
        dm.step(country, global_, z[t])
        led.end_of_year(year)
        out_c.append(country.copy())
        out_g.append(global_.copy())
    return np.array(out_c), np.array(out_g)


def _reference_draws(cat, dyn, T, R, fire, dyn_z):
    shapes = DrawShapes.for_catalog(cat, len(dyn.noisy_keys))
    z = _dyn_z(dyn, T, R, dyn_z)
    E, K, n_rows = cat.n_events, cat.n_factors, len(cat.impact_table)
    years = [{"factor": np.zeros((R, K)), "idio": np.where(_fired(cat, fire, R, t), -10.0, 10.0),
              "res_u": np.full((R, E), 0.5), "branch_u": np.full((R, E), 0.5), "impact_z": np.zeros((R, n_rows)),
              "dyn_z": z[t].copy()} for t in range(T)]
    return ScriptedDraws({"t2_offset": np.zeros((R, len(cat.type2)))}, years, shapes)


def _both(cat, ic, dyn, T, R=1, fire=(), dyn_z=None):
    """Drive the vectorized modules and the reference; assert they agree on state every year (rtol 1e-9).

    Returns country [T, R, N_ent, N_cvar] and global [T, R, N_gvar], end of each year."""
    country, global_ = _drive(cat, ic, dyn, T, R, fire, dyn_z)
    draws = _reference_draws(cat, dyn, T, R, fire, dyn_z)
    for r in range(R):
        rec = ReferenceRun(cat, ic, dyn, SimParams(start_year=START, years=T), draws, r).run()
        np.testing.assert_allclose(country[:, r], rec.country[1:], rtol=1e-9, atol=0)
        np.testing.assert_allclose(global_[:, r], rec.global_[1:], rtol=1e-9, atol=0)
        assert sorted((ev.year - START, ev.event) for ev in rec.events) == sorted((t, e) for rr, t, e in fire if rr == r)
    return country, global_


def _ic():
    return InitialConditions(IC_COUNTRY.copy(), IC_GLOBAL.copy())


# ------------------------------------------------------- (a) no-event FIX-A ----
def test_e7_no_event_fix_a_compounds_gdp_and_adds_life_expectancy():
    """The guide's gate: from FIX-A's initial conditions with idio +10 every year (nothing fires), gdp_growth
    sits at its equilibrium 2, so gdp_per_capita compounds at exactly 2%/yr and life expectancy gains linearly."""
    cat, ic, dyn = fix_a.catalog(), fix_a.initial_conditions(), fix_a.dynamics()
    T = 12
    country, global_ = _both(cat, ic, dyn, T)
    a, b = cat.index.entity["a"], cat.index.entity["b"]
    pc, gr, le = (cat.index.country_var[k] for k in ("gdp_per_capita", "gdp_growth", "life_expectancy"))
    k = np.arange(1, T + 1)
    np.testing.assert_allclose(country[:, 0, a, pc], 50.0 * 1.02 ** k, rtol=1e-9, atol=0)
    np.testing.assert_allclose(country[:, 0, b, pc], 10.0 * 1.02 ** k, rtol=1e-9, atol=0)
    np.testing.assert_allclose(country[:, 0, a, le], 80.0 + 0.2 * k, rtol=1e-9, atol=0)
    np.testing.assert_allclose(country[:, 0, b, le], 70.0 + 0.1 * k, rtol=1e-9, atol=0)
    assert (country[:, 0, :, gr] == 2.0).all() and (global_[:, 0, 0] == 75.0).all()


# -------------------------------------------------- (b) specified half-life ----
@pytest.mark.parametrize("h", [1.0, 2.0, 3.0, 0.5])
def test_e7_displaced_by_initial_condition_recovers_with_the_specified_half_life(h):
    mu, T = 10.0, 8
    ic = _ic()
    ic.country[X, V] = mu - 6.0                       # d = −6 on x.v
    ic.global_[O] = 75.0 + 20.0                       # d = +20 on o
    dyn = DynamicsSpec([VarDynamics("x.v", "mean_revert", mu=mu, half_life=h),
                        VarDynamics("o", "mean_revert", mu=75.0, half_life=h)])
    country, global_ = _both(_catalog(), ic, dyn, T)
    k = np.arange(1, T + 1)
    np.testing.assert_allclose(country[:, 0, X, V] - mu, -6.0 * 0.5 ** (k / h), rtol=1e-9, atol=0)
    np.testing.assert_allclose(global_[:, 0, O] - 75.0, 20.0 * 0.5 ** (k / h), rtol=1e-9, atol=0)
    # exactly one half-life: the displacement has halved (integer h; h = .5 halves twice a year)
    if h == int(h):
        np.testing.assert_allclose(country[int(h) - 1, 0, X, V] - mu, -3.0, rtol=1e-9, atol=0)


@pytest.mark.parametrize("h", [1.0, 2.0, 3.0, 0.5])
def test_e7_displaced_by_a_shock_recovers_with_the_specified_half_life(h):
    """A permanent, immediate +8 shock to x.v (folded into state at firing, no slot) in year 2 of run 0. Step 6
    precedes step 7, so the shocked value already reverts in the firing year: k years of reversion by the end of
    year 2 + k − 1. Run 1 never fires and stays at μ exactly."""
    mu, T, t0 = 10.0, 9, 2
    dyn = DynamicsSpec([VarDynamics("x.v", "mean_revert", mu=mu, half_life=h)])
    country, _ = _both(_catalog(8.0), _ic(), dyn, T, R=2, fire=[(0, t0, 0)])
    v = country[:, 0, X, V]
    assert (v[:t0] == mu).all()
    k = np.arange(1, T - t0 + 1)
    np.testing.assert_allclose(v[t0:] - mu, 8.0 * 0.5 ** (k / h), rtol=1e-9, atol=0)
    assert (country[:, 1, X, V] == mu).all()


# ------------------------------------------------- (c) growth-rate-first ----
@pytest.mark.parametrize("stock_first", [False, True], ids=["declared-after", "declared-before"])
def test_e7_gdp_stock_compounds_by_post_reversion_growth(stock_first):
    """x.g starts at 6 and reverts to 2 with h = 1 (θ = .5): 4 after year 0, 3 after year 1. The stock compounds
    by the reverted rate: 100 · 1.04 = 104, then 104 · 1.03 = 107.12. Reading pre-reversion growth would give
    100 · 1.06 = 106, then 106 · 1.04 = 110.24. Mean reversion is phase 1 whatever the declaration order."""
    ic = _ic()
    ic.country[X, G] = 6.0
    rev = VarDynamics("x.g", "mean_revert", mu=2.0, half_life=1.0)
    stock = VarDynamics("x.gdp", "gdp_stock", growth_key="x.g")
    dyn = DynamicsSpec([stock, rev] if stock_first else [rev, stock])
    country, _ = _both(_catalog(), ic, dyn, 2)
    assert country[:, 0, X, G].tolist() == [4.0, 3.0]
    np.testing.assert_allclose(country[:, 0, X, GDP], [104.0, 104.0 * 1.03], rtol=1e-12, atol=0)
    assert abs(country[1, 0, X, GDP] - 107.12) < 1e-9 and abs(country[1, 0, X, GDP] - 110.24) > 3.0


# ----------------------------------------------------------------- (d) noise ----
SIGMA = {"o": 3.0, "x.g": 0.5, "y.u": 1.25}
NOISY = DynamicsSpec([
    VarDynamics("o", "mean_revert", mu=75.0, half_life=2.0, sigma=SIGMA["o"]),
    VarDynamics("p", "multiplicative", rate=-0.08),                  # no dyn_z column
    VarDynamics("x.g", "mean_revert", mu=2.0, half_life=1.0, sigma=SIGMA["x.g"]),
    VarDynamics("x.gdp", "gdp_stock", growth_key="x.g"),            # no dyn_z column
    VarDynamics("y.u", "mean_revert", mu=6.0, half_life=3.0, sigma=SIGMA["y.u"]),
])
Z0 = np.array([0.7, -1.3, 2.1])                                   # columns: o, x.g, y.u (noisy_keys order)


def test_e7_noise_uses_the_entry_s_dyn_z_column():
    assert NOISY.noisy_keys == ["o", "x.g", "y.u"]
    country, global_ = _both(_catalog(), _ic(), NOISY, 1, dyn_z=Z0)
    th = lambda h: 1.0 - 0.5 ** (1.0 / h)
    o = 75.0 + th(2.0) * (75.0 - 75.0) + 3.0 * 0.7
    g = 2.0 + th(1.0) * (2.0 - 2.0) + 0.5 * -1.3
    u = 7.0 + th(3.0) * (6.0 - 7.0) + 1.25 * 2.1
    assert global_[0, 0, O] == pytest.approx(o, rel=1e-12)
    assert country[0, 0, X, G] == pytest.approx(g, rel=1e-12)
    assert country[0, 0, Y, U] == pytest.approx(u, rel=1e-12)
    assert country[0, 0, X, GDP] == pytest.approx(100.0 * (1.0 + g / 100.0), rel=1e-12)
    assert global_[0, 0, P] == pytest.approx(130.0 * 0.92, rel=1e-12)


@pytest.mark.parametrize("perm,changed", [
    ([2, 1, 0], {"o", "y.u"}),
    ([1, 0, 2], {"o", "x.g", "x.gdp"}),
    ([0, 2, 1], {"x.g", "x.gdp", "y.u"}),
], ids=["swap-o-u", "swap-o-g", "swap-g-u"])
def test_e7_permuting_dyn_z_columns_changes_exactly_the_matching_variables(perm, changed):
    T = 3
    z = np.array([Z0, -Z0[::-1], Z0 * 0.5])[:, None, :]           # [T, R = 1, 3], distinct per column and year
    base_c, base_g = _both(_catalog(), _ic(), NOISY, T, dyn_z=z)
    c, g = _both(_catalog(), _ic(), NOISY, T, dyn_z=z[:, :, perm])
    loc = {"o": (None, O), "p": (None, P), "x.g": (X, G), "x.gdp": (X, GDP), "y.u": (Y, U)}
    for key, (e, v) in loc.items():
        a, b = (base_g[:, 0, v], g[:, 0, v]) if e is None else (base_c[:, 0, e, v], c[:, 0, e, v])
        assert (a != b).any() == (key in changed), key
    untouched = np.ones(c.shape[2:], dtype=bool)
    untouched[X, G] = untouched[X, GDP] = untouched[Y, U] = False
    assert (c[:, 0][:, untouched] == base_c[:, 0][:, untouched]).all()


# ------------------------------------------------------ (e) drifts, order ----
def test_e7_additive_and_multiplicative_drifts():
    dyn = DynamicsSpec([VarDynamics("o", "additive", rate=0.03), VarDynamics("p", "multiplicative", rate=-0.08),
                        VarDynamics("y.v", "additive", rate=-0.5), VarDynamics("x.u", "multiplicative", rate=0.01)])
    T = 10
    country, global_ = _both(_catalog(), _ic(), dyn, T)
    k = np.arange(1, T + 1)
    np.testing.assert_allclose(global_[:, 0, O], 75.0 + 0.03 * k, rtol=1e-9, atol=0)
    np.testing.assert_allclose(global_[:, 0, P], 130.0 * 0.92 ** k, rtol=1e-9, atol=0)
    np.testing.assert_allclose(country[:, 0, Y, V], 20.0 - 0.5 * k, rtol=1e-9, atol=0)
    np.testing.assert_allclose(country[:, 0, X, U], 5.0 * 1.01 ** k, rtol=1e-9, atol=0)
    assert (country[:, 0, X, V] == 10.0).all() and (country[:, 0, Y, U] == 7.0).all()   # undeclared: untouched


@pytest.mark.parametrize("drift_first,want", [
    (True, [100.0 * 1.03, 100.0 * 1.03 * 1.04]),          # the stock reads g after this year's +1
    (False, [100.0 * 1.02, 100.0 * 1.02 * 1.03]),         # the stock reads g before it
], ids=["drift-before-stock", "drift-after-stock"])
def test_e7_phase_two_follows_declaration_order(drift_first, want):
    drift = VarDynamics("x.g", "additive", rate=1.0)
    stock = VarDynamics("x.gdp", "gdp_stock", growth_key="x.g")
    dyn = DynamicsSpec([drift, stock] if drift_first else [stock, drift])
    country, _ = _both(_catalog(), _ic(), dyn, 2)
    np.testing.assert_allclose(country[:, 0, X, GDP], want, rtol=1e-12, atol=0)
    assert country[:, 0, X, G].tolist() == [3.0, 4.0]


def test_e7_growth_at_or_below_minus_100_is_not_clamped():
    ic = _ic()
    ic.country[X, G] = -150.0
    dyn = DynamicsSpec([VarDynamics("x.gdp", "gdp_stock", growth_key="x.g")])
    country, _ = _both(_catalog(), ic, dyn, 2)
    assert country[:, 0, X, GDP].tolist() == [-50.0, 25.0]


# ------------------------------------------------------------- (f) failures ----
@pytest.mark.parametrize("v", [
    VarDynamics("z.v", "additive", rate=1.0),
    VarDynamics("x.nope", "additive", rate=1.0),
    VarDynamics("nope", "mean_revert", mu=1.0),
    VarDynamics("x.gdp", "gdp_stock", growth_key="x.nope"),
    VarDynamics("x.gdp", "gdp_stock"),                        # growth_key missing
], ids=["unknown-entity", "unknown-country-var", "unknown-global", "unknown-growth-key", "empty-growth-key"])
def test_e7_unknown_key_is_a_loud_error_at_construction(v):
    cat, dyn = _catalog(), DynamicsSpec([v])
    with pytest.raises(KeyError):
        DynamicsModel(cat, dyn)
    with pytest.raises(KeyError):                             # the oracle agrees
        ReferenceRun(cat, _ic(), dyn, SimParams(start_year=START, years=1), _reference_draws(cat, dyn, 1, 1, (), None), 0)


def test_e7_unknown_kind_raises():
    cat, dyn = _catalog(), DynamicsSpec([VarDynamics("x.v", "logistic", rate=1.0)])
    with pytest.raises(ValueError, match="'x.v'.*logistic"):
        DynamicsModel(cat, dyn)
    with pytest.raises(ValueError, match="logistic"):
        ReferenceRun(cat, _ic(), dyn, SimParams(start_year=START, years=1),
                     _reference_draws(cat, dyn, 1, 1, (), None), 0).run()


def _state(R=2):
    return np.tile(IC_COUNTRY, (R, 1, 1)), np.tile(IC_GLOBAL, (R, 1))


@pytest.mark.parametrize("shape", [(2, 2), (2, 4), (1, 3), (3, 3), (6,)], ids=str)
def test_e7_wrong_dyn_z_shape_raises(shape):
    dm = DynamicsModel(_catalog(), NOISY)
    country, global_ = _state()
    with pytest.raises(ValueError, match="dyn_z"):
        dm.step(country, global_, np.zeros(shape))
    assert (country == np.tile(IC_COUNTRY, (2, 1, 1))).all()                  # nothing applied


@pytest.mark.parametrize("which", ["country-f32", "global-int", "country-shape", "global-R"])
def test_e7_bad_state_dtype_or_shape_raises(which):
    dm = DynamicsModel(_catalog(), NOISY)
    country, global_ = _state()
    if which == "country-f32":
        country = country.astype(np.float32)
    elif which == "global-int":
        global_ = global_.astype(np.int64)
    elif which == "country-shape":
        country = country[:, :, :3].copy()
    else:
        global_ = global_[:1].copy()
    with pytest.raises(ValueError):
        dm.step(country, global_, np.zeros((2, 3)))


# --------------------------------------------------------------- (g) dtypes ----
def test_e7_dtypes_shapes_and_in_place():
    cat = _catalog()
    dm = DynamicsModel(cat, NOISY)
    assert dm.noisy_keys == NOISY.noisy_keys
    country, global_ = _state(R=5)
    c_id, g_id = id(country), id(global_)
    assert dm.step(country, global_, np.zeros((5, 3))) is None
    assert id(country) == c_id and id(global_) == g_id
    assert country.dtype == np.float64 and country.shape == (5, 2, 4)
    assert global_.dtype == np.float64 and global_.shape == (5, 2)
    empty = DynamicsModel(cat, DynamicsSpec([VarDynamics("o", "additive", rate=1.0)]))
    empty.step(country, global_, np.zeros((5, 0)))                           # no noisy keys: width-0 block
    assert (global_[:, O] == 76.0).all()
