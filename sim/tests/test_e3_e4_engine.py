"""E3/E4 gates (implementation guide §3), statistical gates at R = 100k under fixed seeds (§5.3).

E3: empirical factor correlation within ±0.02 of Ω entrywise; per-event Z variance within ±0.02 of 1.0.
E4: Type 1 firing frequency within 3σ (binomial) of spec for every fixture event; Type 2 probability monotone
    in pressure across a sweep; Type 3 never fires while the gate is false.
"""
import numpy as np
import pytest

from sim.catalog import compile_catalog, load_omega, load_state_catalog
from sim.catalog.extract import extract_all
from sim.engine import EventState, FactorModel, FiringModel, namespace_from_state
from sim.rng import DrawShapes, SeededDraws
from sim.tests.fixtures import fix_a, fix_b, fix_c

R_GATE = 100_000
SEED = 20261012


def _block(catalog, n_noisy, seed=SEED, R=R_GATE):
    shapes = DrawShapes.for_catalog(catalog, n_noisy)
    draws = SeededDraws(seed, R=R, shapes=shapes, block_size=R, years=1)
    stream = draws.stream(0)
    return stream.init, stream.year(0)


@pytest.fixture(scope="module")
def real_catalog():
    sc = load_state_catalog()
    _, omega = load_omega(factors=sc.factors)
    _, known, _ = extract_all(fix_c.REPO / "events")
    return compile_catalog([fix_c.TAIWAN, fix_c.AMOC], omega, sc, known_event_ids=known, strict_cascades=False)


# ------------------------------------------------------------------ E3 ----
@pytest.mark.parametrize("name", ["fix_b", "real"])
def test_e3_factor_correlation_and_z_variance(name, real_catalog):
    cat = fix_b.catalog() if name == "fix_b" else real_catalog
    fm = FactorModel.from_catalog(cat)
    _, yr = _block(cat, 0)
    F = fm.factors(yr["factor"])
    Z = fm.propensity(F, yr["idio"])
    assert F.dtype == Z.dtype == np.float64 and F.shape == (R_GATE, cat.n_factors) and Z.shape == (R_GATE, cat.n_events)
    corr = np.corrcoef(F, rowvar=False)
    assert np.abs(corr - cat.omega).max() < 0.02
    zvar = Z.var(axis=0)
    assert np.abs(zvar - 1.0).max() < 0.02
    # the copula uniforms are marginally uniform: mean 1/2, variance 1/12 (sanity on Φ)
    U = fm.uniforms(Z)
    assert np.abs(U.mean(axis=0) - 0.5).max() < 0.01 and np.abs(U.var(axis=0) - 1 / 12).max() < 0.002


def test_e3_rejects_inconsistent_sigma_and_bad_omega():
    cat = fix_b.catalog()
    cat.sigma_idio = cat.sigma_idio * 0.5
    with pytest.raises(ValueError, match="sigma_idio"):
        FactorModel.from_catalog(cat)
    cat = fix_b.catalog()
    cat.omega = np.array([[1.0, 1.5], [1.5, 1.0]])
    with pytest.raises(Exception, match="Ω"):
        FactorModel.from_catalog(cat)


# ------------------------------------------------------------------ E4 ----
def _firing_year0(mod, catalog, ic, R=R_GATE, seed=SEED, n_noisy=0):
    fm, fr = FactorModel.from_catalog(catalog), FiringModel(catalog)
    init, yr = _block(catalog, n_noisy, seed=seed, R=R)
    F, U = fm.year(yr)
    country = np.broadcast_to(ic.country, (R,) + ic.country.shape)
    global_ = np.broadcast_to(ic.global_, (R,) + ic.global_.shape)
    ns = namespace_from_state(catalog, F, country, global_)
    thr = fr.thresholds(init["t2_offset"])
    counters = {e: np.zeros((R, len(s.sustained)), dtype=np.int64) for e, s in catalog.type3.items()}
    res = fr.base(ns, 2025, EventState.fresh(R, catalog.n_events), thr, counters)
    fired = fr.fire(res.gate, U, res.p_base)
    return fr, res, U, fired


@pytest.mark.parametrize("mod,event,p", [(fix_a, 0, fix_a.P_ANNUAL), (fix_b, 0, 0.05)])
def test_e4_type1_frequency_within_3_sigma(mod, event, p):
    cat = mod.catalog()
    _, res, U, fired = _firing_year0(mod, cat, mod.initial_conditions(), n_noisy=len(mod.dynamics().noisy_keys))
    assert (res.p_base[:, event] == p).all() and res.gate[:, event].all()
    freq = fired[:, event].mean()
    assert abs(freq - p) <= 3 * np.sqrt(p * (1 - p) / R_GATE), (freq, p)


def test_e4_type2_probability_monotone_in_pressure():
    cat = fix_b.catalog()
    fr = FiringModel(cat)
    R = 10_000
    init, yr = _block(cat, 0, R=R)
    thr = fr.thresholds(init["t2_offset"])
    assert thr.shape == (R, 1) and np.allclose(thr[:, 0], 2.0 + 0.5 * init["t2_offset"][:, 0])
    s = cat.type2[1]
    sweep = np.linspace(s.threshold - 4 * s.threshold_std, s.threshold + 4 * s.threshold_std, 41)
    ev = EventState.fresh(R, cat.n_events)
    counters = {2: np.zeros((R, 1), dtype=np.int64)}
    prev = None
    for temp in sweep:
        ns = {"_shape": (R,), "temp": np.full(R, temp), "x.stress": np.zeros(R), "FG": np.zeros(R)}
        p = fr.base(ns, 2025, ev, thr, counters).p_base[:, 1]
        assert (p >= s.floor).all() and (p <= 1.0).all()
        if prev is not None:
            assert (p >= prev).all()           # monotone per run, each at its own drawn threshold
        prev = p
    # at the per-run threshold the probability is the midpoint floor + (1 - floor)/2
    ns = {"_shape": (R,), "temp": thr[:, 0], "x.stress": np.zeros(R), "FG": np.zeros(R)}
    np.testing.assert_allclose(fr.base(ns, 2025, ev, thr, counters).p_base[:, 1], s.floor + (1 - s.floor) / 2, rtol=1e-12)


def test_e4_type3_never_fires_while_gate_is_false():
    cat = fix_b.catalog()
    fr = FiringModel(cat)
    R = R_GATE
    init, yr = _block(cat, 0, R=R)
    thr = fr.thresholds(init["t2_offset"])
    ev = EventState.fresh(R, cat.n_events)
    rng = np.random.default_rng(SEED)
    stress = rng.choice([0.0, 2.0], size=R)                 # precondition x.stress > 1 holds for half the runs
    counters = {2: rng.choice([0, 1, 2, 3], size=(R, 1)).astype(np.int64)}   # sustained needs >= 2
    ns = {"_shape": (R,), "temp": np.full(R, 1.0), "x.stress": stress, "FG": rng.choice([0.0, 1.5], size=R)}
    res = fr.base(ns, 2025, ev, thr, counters)
    want_gate = (stress > 1) & (counters[2][:, 0] >= 2)
    assert (res.gate[:, 2] == want_gate).all() and 0 < want_gate.mean() < 1
    assert (res.sustained_now[2][:, 0] == (ns["FG"] > 1.0)).all()
    U = np.zeros((R, cat.n_events))                        # U = 0 < any positive p_eff: fires wherever gated
    fired = fr.fire(res.gate, U, res.p_base + 10.0)       # p_eff far above 1 — unclamped, still gated
    assert (fired[:, 2] == want_gate).all()
    assert not fired[~want_gate, 2].any()


def test_e4_fire_is_unclamped_and_shape_checked():
    fr = FiringModel(fix_a.catalog())
    gate = np.ones((3, 1), dtype=bool)
    U = np.array([[0.5], [0.5], [0.0]])
    assert fr.fire(gate, U, np.array([[-0.1], [1.5], [0.0]])).ravel().tolist() == [False, True, False]
    with pytest.raises(ValueError, match="shape mismatch"):
        fr.fire(gate, U, np.zeros((2, 1)))
