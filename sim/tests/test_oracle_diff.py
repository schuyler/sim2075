"""§5.2 oracle diff: the vectorized modules against the scalar reference engine under SeededDraws at R = 64.

The reference replays run r by generating block r // block_size at full width and consuming row r; the
vectorized modules consume the whole block. Everything the built stages produce is compared:

    E3  factors F and copula uniforms U for every year (state-independent)
    E4  p_base, gate, p_eff and the fire mask for year 0 (no cascades or counters can be active yet)

As E5–E8 land, this test grows to the full state trajectory (rtol 1e-9) and the exact event log.
"""
import numpy as np
import pytest

from sim.engine import EventState, FactorModel, FiringModel, namespace_from_state
from sim.reference import ReferenceRun
from sim.rng import DrawShapes, SeededDraws
from sim.tests.fixtures import fix_a, fix_b

R_DIFF = 64
SEED = 7


@pytest.mark.parametrize("mod", [fix_a, fix_b], ids=["FIX-A", "FIX-B"])
@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_factors_and_firing(mod, block_size):
    cat, ic, dyn, params = mod.catalog(), mod.initial_conditions(), mod.dynamics(), mod.params()
    shapes = DrawShapes.for_catalog(cat, len(dyn.noisy_keys))
    draws = SeededDraws(SEED, R=R_DIFF, shapes=shapes, block_size=block_size, years=params.years)
    refs = [ReferenceRun(cat, ic, dyn, params, draws, r).run() for r in range(R_DIFF)]

    fm, fr = FactorModel.from_catalog(cat), FiringModel(cat)
    for b in range(draws.n_blocks):
        start, stop = draws.block_rows(b)
        rb = stop - start
        stream = draws.stream(b)
        thr = fr.thresholds(stream.init["t2_offset"])
        for t in range(params.years):
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
    # the diff is only meaningful if something fired in year 0 somewhere in the batch
    assert any(e.year == params.start_year for ref in refs for e in ref.events)
