"""E8 gate (guide §3): the year loop behind ``simulate()`` and recording per ADR-9.

The §5.2 oracle diff runs **through ``simulate()``** here: FIX-A and FIX-B at R = 64 under ``SeededDraws``, one
block and four, with ``n_full = R``, three thin keys and scenario flags of which at least one is true in some
runs and false in others. Everything ``RunOutputs`` holds is compared with ``simulate_reference`` under the same
seed and block size: full trajectories, terminal state, factors and thin trajectories at rtol 1e-9; flags and
``max_active_seen`` exactly; the event log exactly (year, event, resolution, branch, cascade mask), magnitudes
row for row with M, p_base and p_eff at rtol 1e-9. ``test_oracle_diff.py`` runs the same diff on its variants
(noisy FIX-A, drift on a growth key, FIX-B over 20 years) and the hard failures on its ramped variants.

Recording semantics are then checked on their own terms: trajectory index 0 is the initial conditions; the
first ``n_full`` runs' full trajectories are those of the same batch recorded in full; a flag equals a direct
consecutive count over the recorded end-of-year trajectories (E9's gate); the log is ordered by (run, year,
event) with each firing's magnitudes in impact-table row order; results depend on ``(seed, block_size)`` only;
hard failures name global run indices and the reference's year; the step order of README §3 is pinned.

The performance smoke (E8-D5) is opt-in: ``SIM2075_SMOKE=1 python -m pytest sim/tests/test_e8_simulation.py
-k smoke -s`` (README §1). It measures the loop's cost at the real axis sizes, not realism: every migrated event
except those whose compile notes carry the multiplicative "mean <= -1" WARNING (today Taiwan, README §4 item 9),
each global's ``baseline_2025`` as initial condition, and smoke-only dynamics built here from MVP scope §2.2
and §3 (never committed under ``sim/data/``). R = 10,000 × 50 years must run in under 60 s.
"""
from __future__ import annotations

import cProfile
import dataclasses
import os
import platform
import pstats
import sys
import time
from io import StringIO
from pathlib import Path

import numpy as np
import pytest

from sim.engine import (DynamicsModel, FactorModel, FiringModel, ImpactLedger, MemoryModel, RunOutputs,
                        resolve_key, simulate)
from sim.reference import (DynamicsSpec, ImpactOutOfRange, InitialConditions, LedgerOverflow, RecordingSpec,
                           ReferenceRun, ScenarioFlag, SimParams, VarDynamics, simulate_reference)
from sim.rng import DrawShapes, SeededDraws
from sim.tests.fixtures import builders as B, fix_a, fix_b

R_DIFF = 64
SEED = 7
REPO = Path(__file__).resolve().parents[2]


def _flag(name, names, fn, min_years) -> ScenarioFlag:
    return ScenarioFlag(name, B.expr(names, fn, "boolean"), min_years)


def recording_for(mod, n_full=R_DIFF) -> RecordingSpec:
    """Thin keys and flags for a fixture. Each list has a flag that is mixed across the R = 64 batch and, for
    FIX-B, one set only at the horizon's end (``x.stress > 2.2`` for 2 years: end-of-year stress is 2.5, 3.0 in
    t = 4, 5), which a start-of-year evaluation would miss."""
    if mod is fix_a:
        flags = [_flag("growth_hit", ["a.gdp_growth"], lambda ns: ns["a.gdp_growth"] < 1.5, 1),
                 _flag("fa_high2", ["FA"], lambda ns: ns["FA"] > 0.5, 2),
                 _flag("oil_high3", ["oil_brent"], lambda ns: ns["oil_brent"] > 80.0, 3)]
        thin = ["a.gdp_per_capita", "oil_brent", "b.life_expectancy"]
    else:
        flags = [_flag("gdp_hit", ["x.gdp"], lambda ns: ns["x.gdp"] < 95.0, 1),
                 _flag("fg_stress2", ["FG", "x.stress"], lambda ns: (ns["FG"] > 1.0) & (ns["x.stress"] > 0.7), 2),
                 _flag("late2", ["x.stress"], lambda ns: ns["x.stress"] > 2.2, 2)]
        thin = ["x.gdp", "temp", "x.stress"]
    return RecordingSpec(scenario_flags=flags, thin_keys=thin, n_full=n_full)


def _ref_trajectory(ref, loc):
    return ref.country[:, loc[1], loc[2]] if loc[0] == "c" else ref.global_[:, loc[1]]


def assert_matches_reference(out: RunOutputs, refs, cat, recording: RecordingSpec) -> None:
    """Everything in ``out`` equals the reference runs ``refs`` (global run index = list position)."""
    R = len(refs)
    assert out.R == R and out.T == len(refs[0].years) and out.years.tolist() == refs[0].years
    assert out.flag_names == recording.flag_names and out.thin_keys == list(recording.thin_keys)
    assert out.full_country.shape[0] == out.full_global.shape[0] == recording.n_full
    locs = [resolve_key(cat, k) for k in recording.thin_keys]
    ev = out.events
    for r, ref in enumerate(refs):
        where = f"run {r}"
        if r < recording.n_full:
            np.testing.assert_allclose(out.full_country[r], ref.country, rtol=1e-9, atol=0, err_msg=where)
            np.testing.assert_allclose(out.full_global[r], ref.global_, rtol=1e-9, atol=0, err_msg=where)
        np.testing.assert_allclose(out.country[r], ref.country[-1], rtol=1e-9, atol=0, err_msg=where)
        np.testing.assert_allclose(out.global_[r], ref.global_[-1], rtol=1e-9, atol=0, err_msg=where)
        np.testing.assert_allclose(out.factors[r], ref.factors.T, rtol=1e-9, atol=0, err_msg=where)
        for k, loc in enumerate(locs):
            np.testing.assert_allclose(out.thin[r, k], _ref_trajectory(ref, loc), rtol=1e-9, atol=0,
                                       err_msg=f"{where} thin {recording.thin_keys[k]}")
        assert out.scenario_flags[r].tolist() == ref.scenario_flags.tolist(), (where, "flags")
        assert int(out.max_active_seen[r]) == ref.max_active_seen, (where, "max_active_seen")
        ks = ev.firings_of(r)
        got = [(int(ev.year[k]), int(ev.event[k]), int(ev.resolution[k]), int(ev.branch[k]), int(ev.cascade_mask[k]))
               for k in ks]
        assert got == [(e.year, e.event, e.resolution, e.branch, e.cascade_mask) for e in ref.events], (where, "log")
        np.testing.assert_allclose(ev.p_base[ks], [e.p_base for e in ref.events], rtol=1e-9, atol=0, err_msg=where)
        np.testing.assert_allclose(ev.p_eff[ks], [e.p_eff for e in ref.events], rtol=1e-9, atol=0, err_msg=where)
        for k, e in zip(ks, ref.events):
            mags = ev.magnitudes(k)
            assert [j for j, _ in mags] == [j for j, _ in e.magnitudes], (where, "magnitude rows", e.year, e.event)
            np.testing.assert_allclose([m for _, m in mags], [m for _, m in e.magnitudes], rtol=1e-9, atol=0,
                                       err_msg=f"{where} magnitudes {e.year} {e.event}")
    # the whole log is (run, year, event)-ordered and every magnitude row belongs to a logged firing
    key = np.stack([ev.run, ev.year, ev.event], axis=1)
    assert (np.diff(key, axis=0)[:, 0] >= 0).all() and (np.lexsort((ev.event, ev.year, ev.run)) == np.arange(len(ev))).all()
    assert len(ev.mag_firing) == sum(len(e.magnitudes) for ref in refs for e in ref.events)


def diff_simulate(cat, ic, dyn, params, block_size, recording, seed=SEED, R=R_DIFF) -> RunOutputs:
    """Run ``simulate`` and the reference under the same (seed, block_size); diff everything; return the outputs."""
    params = dataclasses.replace(params, block_size=block_size)
    out = simulate(cat, ic, dyn, params, R, seed, recording)
    draws = SeededDraws(seed, R, DrawShapes.for_catalog(cat, len(dyn.noisy_keys)), block_size=block_size,
                        years=params.years)
    refs = simulate_reference(cat, ic, dyn, params, draws, range(R), recording)
    assert_matches_reference(out, refs, cat, recording)
    return out


def _mixed(flags: np.ndarray) -> list[bool]:
    return [0.0 < flags[:, j].mean() < 1.0 for j in range(flags.shape[1])]


@pytest.mark.parametrize("mod", [fix_a, fix_b], ids=["FIX-A", "FIX-B"])
@pytest.mark.parametrize("block_size", [64, 16], ids=["one-block", "four-blocks"])
def test_oracle_diff_through_simulate(mod, block_size):
    rec = recording_for(mod)
    out = diff_simulate(mod.catalog(), mod.initial_conditions(), mod.dynamics(), mod.params(), block_size, rec)
    assert len(out.events) > 0
    mixed = _mixed(out.scenario_flags)
    assert any(mixed), out.scenario_flags.mean(axis=0)
    if mod is fix_b:
        assert out.scenario_flags[:, 2].all()            # late2: set at t = 5 in every run (end-of-year stress 3.0)


# ---- recording semantics --------------------------------------------------------------------------------------

def _run(mod, block_size=16, n_full=R_DIFF, seed=SEED, **params):
    rec = recording_for(mod, n_full)
    p = dataclasses.replace(mod.params(), block_size=block_size, **params)
    return simulate(mod.catalog(), mod.initial_conditions(), mod.dynamics(), p, R_DIFF, seed, rec), rec


def test_outputs_shapes_dtypes_and_year_axis():
    cat = fix_a.catalog()
    out, rec = _run(fix_a, n_full=5)
    T, n_ent, n_cvar, n_gvar, K = fix_a.YEARS, cat.n_entities, cat.n_country_vars, cat.n_global_vars, cat.n_factors
    assert out.years.tolist() == [2025 + t for t in range(T)] and out.years.dtype == np.int64
    assert out.country.shape == (R_DIFF, n_ent, n_cvar) and out.global_.shape == (R_DIFF, n_gvar)
    assert out.factors.shape == (R_DIFF, K, T)
    assert out.thin.shape == (R_DIFF, 3, T + 1) and out.thin_keys == rec.thin_keys
    assert out.full_country.shape == (5, T + 1, n_ent, n_cvar) and out.full_global.shape == (5, T + 1, n_gvar)
    assert out.scenario_flags.shape == (R_DIFF, 3) and out.scenario_flags.dtype == bool
    assert out.max_active_seen.shape == (R_DIFF,) and out.max_active_seen.dtype == np.int64
    for a in (out.country, out.global_, out.factors, out.thin, out.full_country, out.full_global, out.events.p_base,
              out.events.p_eff, out.events.mag_M):
        assert a.dtype == np.float64
    for a in (out.events.run, out.events.year, out.events.event, out.events.resolution, out.events.branch,
              out.events.cascade_mask, out.events.mag_firing, out.events.mag_row):
        assert a.dtype == np.int64
    # index 0 of every trajectory is the initial conditions
    ic = fix_a.initial_conditions()
    for k, key in enumerate(rec.thin_keys):
        loc = resolve_key(cat, key)
        want = ic.country[loc[1], loc[2]] if loc[0] == "c" else ic.global_[loc[1]]
        assert (out.thin[:, k, 0] == want).all()
    assert (out.full_country[:, 0] == ic.country).all() and (out.full_global[:, 0] == ic.global_).all()
    # terminal state is the last trajectory entry; thin rows are slices of the full ones
    assert (out.full_country[:, -1] == out.country[:5]).all() and (out.full_global[:, -1] == out.global_[:5]).all()
    for k, key in enumerate(rec.thin_keys):
        loc = resolve_key(cat, key)
        full = out.full_country[:, :, loc[1], loc[2]] if loc[0] == "c" else out.full_global[:, :, loc[1]]
        assert (out.thin[:5, k] == full).all()


def test_n_full_keeps_the_lowest_run_indices_and_changes_nothing_else():
    full, _ = _run(fix_b, n_full=R_DIFF)
    part, _ = _run(fix_b, n_full=3)
    none, _ = _run(fix_b, n_full=0)
    assert none.full_country.shape == (0, fix_b.YEARS + 1, 1, 2) and none.full_global.shape[0] == 0
    assert (part.full_country == full.full_country[:3]).all() and (part.full_global == full.full_global[:3]).all()
    for a in ("country", "global_", "factors", "thin", "scenario_flags", "max_active_seen"):
        assert (getattr(part, a) == getattr(full, a)).all() and (getattr(none, a) == getattr(full, a)).all()
    for a in ("run", "year", "event", "resolution", "branch", "cascade_mask", "mag_firing", "mag_row", "mag_M",
              "p_base", "p_eff"):
        assert (getattr(part.events, a) == getattr(full.events, a)).all()


@pytest.mark.parametrize("mod", [fix_a, fix_b], ids=["FIX-A", "FIX-B"])
def test_scenario_flag_equals_direct_count_over_recorded_trajectories(mod):
    """A flag is a consecutive count of its condition over the recorded end-of-year states with that year's
    factors (ADR-9 / README §3 "Recording"), so it can be recomputed from the full trajectories and the factor
    record alone; evaluating on start-of-year state gives a different answer for FIX-B's ``late2``."""
    cat = mod.catalog()
    out, rec = _run(mod, n_full=R_DIFF)
    T = out.T
    for j, flag in enumerate(rec.scenario_flags):
        end_of_year = np.zeros(R_DIFF, dtype=bool)
        start_of_year = np.zeros(R_DIFF, dtype=bool)
        for state_offset, target in ((1, end_of_year), (0, start_of_year)):
            counter = np.zeros(R_DIFF, dtype=np.int64)
            for t in range(T):
                ns = {"_shape": (R_DIFF,)}
                for n in flag.condition.names:
                    if n in cat.index.factor:
                        ns[n] = out.factors[:, cat.index.factor[n], t]
                    else:
                        loc = resolve_key(cat, n)
                        ns[n] = (out.full_country[:, t + state_offset, loc[1], loc[2]] if loc[0] == "c"
                                 else out.full_global[:, t + state_offset, loc[1]])
                counter = np.where(flag.condition(ns), counter + 1, 0)
                target |= counter >= flag.min_years
        assert out.scenario_flags[:, j].tolist() == end_of_year.tolist(), flag.name
        if mod is fix_b and flag.name == "late2":
            assert end_of_year.all() and not start_of_year.any()


def test_event_log_order_provenance_and_magnitude_rows():
    # FIX-B with T3's sustained condition dropped and x.stress starting at 2.0 (the oracle diff's re-firing
    # variant), so T3 fires at its base rate and often while the T1 cascade is active
    cat = fix_b.catalog()
    T3 = cat.index.event["T3"]
    cat = dataclasses.replace(cat, type3={T3: dataclasses.replace(cat.type3[T3], sustained=[])})
    country = fix_b.initial_conditions().country.copy()
    country[0, cat.index.country_var["stress"]] = 2.0
    ic = InitialConditions(country=country, global_=fix_b.initial_conditions().global_.copy())
    p = dataclasses.replace(fix_b.params(), block_size=16, years=20)
    out = simulate(cat, ic, fix_b.dynamics(), p, R_DIFF, SEED, recording_for(fix_b))
    ev = out.events
    assert len(ev) > 0
    assert (np.lexsort((ev.event, ev.year, ev.run)) == np.arange(len(ev))).all()
    assert (np.diff(ev.mag_firing) >= 0).all()
    assert (ev.mag_firing >= 0).all() and (ev.mag_firing < len(ev)).all()
    it = cat.impact_table
    for i in range(len(ev)):
        rows = [j for j, _ in ev.magnitudes(i)]
        want = np.flatnonzero((it["event"] == ev.event[i]) & (it["res_code"] == ev.resolution[i])
                              & (it["branch_code"] == ev.branch[i])).tolist()
        assert rows == want, i
        assert 0.0 <= ev.p_base[i] <= 1.0 and ev.p_eff[i] >= ev.p_base[i]
    # T3's firings carry the T1 cascade bit when its delta was active, and p_eff − p_base is then a positive
    # multiple of 0.5 (overlapping cascades sum)
    T1 = cat.index.event["T1"]
    k = np.flatnonzero((ev.event == T3) & (ev.cascade_mask == (1 << T1)))
    assert len(k) > 0
    n = (ev.p_eff[k] - ev.p_base[k]) / 0.5
    assert (n >= 1).all()
    np.testing.assert_allclose(n, np.round(n), rtol=0, atol=1e-12)
    assert ((ev.cascade_mask[ev.event == T3] == 0) == (ev.p_eff[ev.event == T3] == ev.p_base[ev.event == T3])).all()


def _all_arrays(out: RunOutputs) -> list[np.ndarray]:
    return [out.years, out.country, out.global_, out.factors, out.thin, out.full_country, out.full_global,
            out.scenario_flags, out.max_active_seen] + [getattr(out.events, f.name) for f in dataclasses.fields(out.events)]


def test_results_depend_on_seed_and_block_size_only():
    a, _ = _run(fix_b, block_size=16, seed=SEED)
    b, _ = _run(fix_b, block_size=16, seed=SEED)
    for x, y in zip(_all_arrays(a), _all_arrays(b)):
        assert x.shape == y.shape and (x == y).all()
    c, _ = _run(fix_b, block_size=16, seed=SEED + 1)
    assert not (c.country == a.country).all()


def test_hard_failures_name_global_runs_and_the_reference_year():
    """FIX-B at max_active = 1 (the gdp decay plus the conflicts shock overflow it) and FIX-A with its
    multiplicative row widened to mean −0.5, std 0.4: ``simulate`` raises for the first block any of whose runs
    fail, in that block's first failing year, naming exactly the runs the reference fails that year. Seed 8 is
    chosen so that the first failing block is not block 0 in either case (blocks 1 and 2), where a block-local
    run index would coincide with the global one and a missing ``run_offset`` would pass."""
    seed = 8
    cases = []
    p = dataclasses.replace(fix_b.params(), max_active=1, block_size=16)
    cases.append((fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), p, LedgerOverflow))
    cat = fix_a.catalog()
    cat.impact_table["mean"][2], cat.impact_table["std"][2] = -0.5, 0.4
    cases.append((cat, fix_a.initial_conditions(), fix_a.dynamics(), dataclasses.replace(fix_a.params(), block_size=16),
                  ImpactOutOfRange))
    for cat, ic, dyn, p, exc_type in cases:
        draws = SeededDraws(seed, R_DIFF, DrawShapes.for_catalog(cat, len(dyn.noisy_keys)), block_size=16, years=p.years)
        ref = {}
        for r in range(R_DIFF):
            try:
                ReferenceRun(cat, ic, dyn, p, draws, r).run()
            except exc_type as exc:
                ref[r] = exc
        assert ref and len(ref) < R_DIFF
        first_block = min(r // 16 for r in ref)
        assert first_block > 0, (exc_type.__name__, first_block)
        in_block = {r: e for r, e in ref.items() if r // 16 == first_block}
        year = min(e.year for e in in_block.values())
        want = sorted(r for r, e in in_block.items() if e.year == year)
        with pytest.raises(exc_type) as ei:
            simulate(cat, ic, dyn, p, R_DIFF, seed)
        assert (ei.value.run_index, ei.value.year) == (want, year)
        assert min(want) >= 16 * first_block
        if exc_type is ImpactOutOfRange:
            assert ei.value.row == ref[want[0]].row
            np.testing.assert_allclose(ei.value.contribution, ref[want[0]].contribution, rtol=1e-9, atol=0)
        else:
            assert ei.value.count == max(ref[r].count for r in want)


def test_simulate_validation():
    cat, ic, dyn, p = fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), fix_b.params()
    with pytest.raises(ValueError, match="n_full"):
        simulate(cat, ic, dyn, p, 8, SEED, RecordingSpec(n_full=9))
    with pytest.raises(KeyError, match="nope"):
        simulate(cat, ic, dyn, p, 8, SEED, RecordingSpec(thin_keys=["x.nope"]))
    with pytest.raises(KeyError, match="nope"):
        simulate(cat, ic, dyn, p, 8, SEED, RecordingSpec(scenario_flags=[_flag("f", ["nope"], lambda ns: ns["nope"] > 0, 1)]))
    with pytest.raises(ValueError, match="event state"):
        RecordingSpec(scenario_flags=[_flag("f", ["years_since"], lambda ns: ns["years_since"] > 0, 1)])
    with pytest.raises(ValueError, match="R"):
        simulate(cat, ic, dyn, p, 0, SEED)
    with pytest.raises(TypeError):
        simulate(cat, ic, dyn, p, 8, SEED, years=3)           # the horizon lives in SimParams (E8-D1)
    with pytest.raises(ValueError, match="initial conditions"):
        simulate(cat, InitialConditions(np.zeros((2, 2)), np.zeros(2)), dyn, p, 8, SEED)
    # the horizon and start year come from SimParams
    out = simulate(cat, ic, dyn, dataclasses.replace(p, years=3, start_year=2030), 8, SEED)
    assert out.years.tolist() == [2030, 2031, 2032] and out.factors.shape[2] == 3 and out.thin.shape == (8, 0, 4)
    assert out.full_country.shape == (0, 4, 1, 2) and out.scenario_flags.shape == (8, 0)


def test_year_step_order_is_pinned(monkeypatch):
    """README §3 "Year step": per year, factors → namespace/base → deltas → fire → memory resolve → ledger resolve
    → ledger apply → dynamics → memory end-of-year → ledger end-of-year → record. The step-8 pair touch disjoint
    state, so their order is observable only here."""
    calls: list[str] = []

    def spy(cls, name):
        orig = getattr(cls, name)
        is_static = isinstance(cls.__dict__.get(name), staticmethod)

        def wrapped(*a, **k):
            calls.append(f"{cls.__name__}.{name}")
            return orig(*a, **k)
        monkeypatch.setattr(cls, name, staticmethod(wrapped) if is_static else wrapped)

    for cls, name in ((FactorModel, "year"), (FiringModel, "base"), (MemoryModel, "deltas"), (FiringModel, "fire"),
                      (MemoryModel, "resolve"), (ImpactLedger, "resolve"), (ImpactLedger, "apply"),
                      (DynamicsModel, "step"), (MemoryModel, "end_of_year"), (ImpactLedger, "end_of_year")):
        spy(cls, name)
    p = dataclasses.replace(fix_b.params(), years=2, block_size=4)
    simulate(fix_b.catalog(), fix_b.initial_conditions(), fix_b.dynamics(), p, 8, SEED)
    year = ["FactorModel.year", "FiringModel.base", "MemoryModel.deltas", "FiringModel.fire", "MemoryModel.resolve",
            "ImpactLedger.resolve", "ImpactLedger.apply", "DynamicsModel.step", "MemoryModel.end_of_year",
            "ImpactLedger.end_of_year"]
    assert calls == year * 4                                  # 2 blocks × 2 years


# ---- performance smoke (E8-D5), opt-in ------------------------------------------------------------------------

SMOKE = os.environ.get("SIM2075_SMOKE") == "1"
SMOKE_R, SMOKE_YEARS, SMOKE_SEED, SMOKE_LIMIT_S = 10_000, 50, 20261023, 60.0
# State Outputs §4.1 with GDP = gdp_real (README §4 item 20); population dropped (pop_total is derived and
# nothing computes derived variables); internal_conflict_intensity for all countries would be 40 more keys.
SMOKE_THIN_KEYS = ["global_temp_anomaly", "sea_level_global", "oil_brent", "usd_reserve_share", "global_credit_spread",
                   "active_major_conflicts"] + [f"{c}.gdp_real" for c in ("usa", "chn", "ind", "deu", "jpn", "bra", "rus")]
SMOKE_EXCLUDED_EVENTS = ["TAIWAN_CONFLICT"]      # README §4 item 9: the only multiplicative "mean <= -1" WARNING today


def smoke_catalog():
    """Every migrated event compiled with ``strict_cascades=False`` except those whose compile notes carry the
    multiplicative "mean <= -1" WARNING; the exclusion is derived from the notes, never listed by hand."""
    from sim.catalog import compile_event_records, load_omega, load_state_catalog
    from sim.catalog.extract import extract_all
    sc = load_state_catalog()
    _, omega = load_omega(factors=sc.factors)
    records, known, _ = extract_all(REPO / "events")
    full = compile_event_records(records, omega, sc, known_event_ids=known, strict_cascades=False)
    excluded = sorted({n.split(":", 1)[0] for n in full.meta["notes"] if "WARNING" in n and "is <= -1 on a multiplicative" in n})
    kept = [r for r in records if r["id"] not in excluded]
    cat = compile_event_records(kept, omega, sc, known_event_ids=known, strict_cascades=False)
    return cat, sc, excluded, list(cat.meta["warnings"])


def smoke_dynamics(cat, sc) -> DynamicsSpec:
    """Smoke-only dynamics (never data): for every country, MVP §3 class defaults for gdp_growth, inflation_rate
    and unemployment_rate (half-life §3.1, σ §3.3, μ §3.2 "advanced": inflation 2, unemployment 5; gdp_growth's
    §3.2 equilibrium is the country's Tier 1 trend, which the scope leaves to D3, so 2 %/yr stands in), a
    gdp_stock on gdp_real with growth_key gdp_growth (item 20), life_expectancy +0.2/yr; and the §2.2 global
    trends present in the catalog, additive or multiplicative as §2.2 states them."""
    vs = []
    for c in sc.countries:
        vs += [VarDynamics(f"{c}.gdp_growth", "mean_revert", mu=2.0, half_life=2.0, sigma=2.0),
               VarDynamics(f"{c}.inflation_rate", "mean_revert", mu=2.0, half_life=2.0, sigma=2.0),
               VarDynamics(f"{c}.unemployment_rate", "mean_revert", mu=5.0, half_life=3.0, sigma=1.0),
               VarDynamics(f"{c}.gdp_real", "gdp_stock", growth_key=f"{c}.gdp_growth"),
               VarDynamics(f"{c}.life_expectancy", "additive", rate=0.2)]
    trends = [("global_temp_anomaly", "additive", 0.03), ("sea_level_global", "additive", 0.4),
              ("global_co2_ppm", "additive", 2.5), ("battery_cost_kwh", "multiplicative", -0.08),
              ("renewable_cost_index", "multiplicative", -0.06), ("antibiotic_resistance", "multiplicative", 0.01)]
    vs += [VarDynamics(k, kind, rate=rate) for k, kind, rate in trends if k in cat.index.global_var]
    return DynamicsSpec(vs)


def smoke_initial_conditions(cat, sc) -> InitialConditions:
    """Each global's ``baseline_2025`` where the state catalog has one; 0 elsewhere (no country baselines exist)."""
    g = np.zeros(cat.n_global_vars)
    for name, k in cat.index.global_var.items():
        g[k] = sc.baseline_2025.get(name, 0.0)
    return InitialConditions(country=np.zeros((cat.n_entities, cat.n_country_vars)), global_=g)


@pytest.mark.skipif(not SMOKE, reason="performance smoke: opt in with SIM2075_SMOKE=1 (README §1)")
def test_performance_smoke_r10000_50_years_under_60s():
    cat, sc, excluded, dropped = smoke_catalog()
    assert excluded == SMOKE_EXCLUDED_EVENTS, excluded
    assert len(cat.event_ids) == 29 - len(excluded)
    dyn = smoke_dynamics(cat, sc)
    ic = smoke_initial_conditions(cat, sc)
    rec = RecordingSpec(thin_keys=SMOKE_THIN_KEYS, n_full=0)
    params = SimParams(start_year=2025, years=SMOKE_YEARS)
    prof = cProfile.Profile()
    t0 = time.perf_counter()
    prof.enable()
    out = simulate(cat, ic, dyn, params, SMOKE_R, SMOKE_SEED, rec)
    prof.disable()
    elapsed = time.perf_counter() - t0
    top = StringIO()
    pstats.Stats(prof, stream=top).sort_stats("cumulative").print_stats(10)
    print(f"\nsmoke: R={SMOKE_R} years={SMOKE_YEARS} block_size={params.block_size} seed={SMOKE_SEED}: {elapsed:.1f} s "
          f"(limit {SMOKE_LIMIT_S:.0f} s); events {len(cat.event_ids)} (excluded {excluded}), impact rows "
          f"{len(cat.impact_table)}, cascade edges {len(cat.cascade_edges)}, dropped edges {len(dropped)}: {dropped}")
    print(f"machine: {os.cpu_count()} CPUs, {platform.machine()} {platform.system()} {platform.release()}, "
          f"python {sys.version.split()[0]}, numpy {np.__version__}")
    print(f"firings {len(out.events)}, max_active_seen max {out.max_active_seen.max()}, thin {out.thin.shape}")
    print(top.getvalue())
    assert out.R == SMOKE_R and out.T == SMOKE_YEARS and out.thin.shape == (SMOKE_R, len(SMOKE_THIN_KEYS), SMOKE_YEARS + 1)
    assert elapsed < SMOKE_LIMIT_S, f"{elapsed:.1f} s"
