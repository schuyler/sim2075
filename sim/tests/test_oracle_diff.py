"""§5.2 oracle diff: the vectorized modules against the scalar reference engine under SeededDraws at R = 64.

The reference replays run r by generating block r // block_size at full width and consuming row r; the
vectorized modules consume the whole block. Everything the built stages produce is compared:

    E3  factors F and copula uniforms U for every year (state-independent)
    E4  p_base, gate, p_eff and the fire mask for year 0 from initial conditions (no memory active yet)
    E5  every year: p_eff, gate, fire mask, the drawn resolution/branch codes and the cascade bitmask of
        each firing; and the start-of-year memory (sustained counters, live cascades with their source
        bitmask and summed deltas, last resolution/branch/firing year) after every year

E6/E7 (impacts, dynamics) are not built, so for years > 0 the vectorized namespace is fed the reference's
own recorded start-of-year state (``RunRecord.country[t]``, ``RunRecord.global_[t]``), isolating E3–E5.
The reference's internal memory at the start of year t is read from a replay truncated to t years (the
draws are generated year by year, so a shorter horizon consumes the same leading draws).

As E6–E8 land, this test grows to the full state trajectory (rtol 1e-9) and the exact event log.
"""
import dataclasses

import numpy as np
import pytest

from sim.engine import EventState, FactorModel, FiringModel, MemoryModel, namespace_from_state
from sim.reference import ReferenceRun
from sim.rng import DrawShapes, SeededDraws
from sim.tests.fixtures import fix_a, fix_b

R_DIFF = 64
SEED = 7


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
            country = np.stack([refs[r].country[t] for r in range(start, stop)])
            global_ = np.stack([refs[r].global_[t] for r in range(start, stop)])
            ns = namespace_from_state(cat, F, country, global_)
            res = fr.base(ns, year, mem.events, thr, mem.counters)
            delta, mask = mem.deltas()
            p_eff = res.p_base + delta
            fired = fr.fire(res.gate, U, p_eff)
            codes, branches = mem.resolve(fired, yr["res_u"], yr["branch_u"], ns, year)
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
            mem.end_of_year(res.sustained_now, year)
            seen["cascade"] += int(mem.active.sum())
            seen["counter"] += sum(int((c > 0).sum()) for c in mem.counters.values())
            seen["fired_after_0"] += int(fired.sum()) if t > 0 else 0
        for r in range(start, stop):
            _assert_memory(mem, r - start, snap[params.years][r], f"run {r} end of run")
    # the diff is only meaningful if something fired in year 0 somewhere in the batch, and, beyond year 0,
    # if firings, live cascades and nonzero sustained counters occurred where the fixture has them
    assert any(e.year == params.start_year for ref in refs for e in ref.events)
    assert seen["fired_after_0"] > 0
    if cat.cascade_edges:
        assert seen["cascade"] > 0
    if any(s.sustained for s in cat.type3.values()):
        assert seen["counter"] > 0
