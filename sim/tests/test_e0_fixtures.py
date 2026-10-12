"""E0 gate: pytest collects and runs; fixtures construct and are internally consistent."""
import numpy as np

from sim.catalog.omega import validate_omega
from sim.catalog.types import IMPACT_DTYPE
from sim.rng import DrawShapes, SeededDraws
from sim.tests.fixtures import fix_a, fix_b


def _check_catalog(cat):
    E, K = cat.lam.shape
    assert cat.causal_type.shape == (E,) and cat.sigma_idio.shape == (E,) and cat.p_annual.shape == (E,)
    assert len(cat.resolution_tree) == E
    assert cat.impact_table.dtype == IMPACT_DTYPE
    validate_omega(cat.omega, list(cat.index.factor))
    achieved = np.einsum("ik,kl,il->i", cat.lam, cat.omega, cat.lam)
    np.testing.assert_allclose(cat.sigma_idio, np.sqrt(1 - achieved))
    for t in cat.resolution_tree:
        assert abs(t.resolution_p.sum() - 1) < 1e-12
        for bp in t.branch_p:
            assert abs(bp.sum() - 1) < 1e-12
    for e in range(E):
        assert (cat.causal_type[e] == 1) == (not np.isnan(cat.p_annual[e]))
        assert (cat.causal_type[e] == 2) == (e in cat.type2)
        assert (cat.causal_type[e] == 3) == (e in cat.type3)


def test_fix_a_constructs():
    cat = fix_a.catalog()
    _check_catalog(cat)
    assert cat.sigma_idio[0] == 0.8
    assert fix_a.draws().years == fix_a.YEARS


def test_fix_b_constructs():
    cat = fix_b.catalog()
    _check_catalog(cat)
    assert len(cat.cascade_edges) == 1 and cat.cascade_edges[0].cond is not None
    assert fix_b.draws().years == fix_b.YEARS


def test_seeded_draws_are_deterministic_and_block_invariant():
    shapes = DrawShapes(K=2, E=3, E_type2=1, n_impact_rows=4, n_noisy_vars=2)
    a = SeededDraws(123, R=10, shapes=shapes, block_size=4, years=3)
    b = SeededDraws(123, R=10, shapes=shapes, block_size=4, years=3)
    assert a.n_blocks == 3 and a.block_rows(2) == (8, 10)
    sa, sb = a.stream(1), b.stream(1)
    np.testing.assert_array_equal(sa.init["t2_offset"], sb.init["t2_offset"])
    for t in range(3):
        ya, yb = sa.year(t), sb.year(t)
        for k in ya:
            np.testing.assert_array_equal(ya[k], yb[k])
        assert ya["factor"].shape == (4, 2) and ya["impact_z"].shape == (4, 4) and ya["dyn_z"].shape == (4, 2)
    # a different seed changes draws; the draw for a run depends only on (seed, block_size, block index)
    c = SeededDraws(124, R=10, shapes=shapes, block_size=4, years=3).stream(1)
    assert not np.array_equal(c.year(0)["factor"], a.stream(1).year(0)["factor"])
