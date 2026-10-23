"""E8 — the year loop (architecture §3) wiring E3–E7 in step order, with recording per ADR-9.

``simulate(catalog, initial_conditions, dynamics, params, R, seed, recording=RecordingSpec()) -> RunOutputs``
(guide §4.5 as amended at E8; README §4 item 21). ``SimParams`` is the single source for ``years``,
``start_year``, ``max_active``, ``epsilon_cull`` and ``block_size``.

Blocks (guide §4.6): one per ``params.block_size`` runs, drawn from ``SeededDraws(seed, R, ...)``, each with
``run_offset = start`` so hard failures name global run indices; Type 2 thresholds come once per block from
``stream.init["t2_offset"]``. Within a block, each year runs the pinned step order (README §3 "Year step"):

    1-2  FactorModel.year                     F [R, K], U [R, E]
    2    namespace_from_state                 start-of-year state + this year's F
    3    FiringModel.base; p_eff = p_base + MemoryModel.deltas()
    4    FiringModel.fire
    5    MemoryModel.resolve, then ImpactLedger.resolve
    6    ImpactLedger.apply                    state in place
    7    DynamicsModel.step(country, global_, dyn_z)
    8    MemoryModel.end_of_year(sustained_now, year), then ImpactLedger.end_of_year(year)
    9    record: factors, event log, thin and full trajectories, max_active_seen, scenario flags on a namespace
         built afresh from end-of-year state with this year's F (README §3 "Recording")

Outputs are assembled by global run index; results depend only on ``(seed, block_size)``. ``LedgerOverflow``
and ``ImpactOutOfRange`` propagate with their global run indices; nothing is caught. Everything is kept in
memory: serialization (Parquet/JSON) is ``run.py`` at E9, and the State Outputs §8.4 validation statistics are
cross-run analyses of what is recorded here (E9/E10).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..catalog.types import CompiledCatalog
from ..reference.model import DynamicsSpec, InitialConditions, RecordingSpec, SimParams
from ..rng import DrawShapes, SeededDraws
from .dynamics import DynamicsModel
from .factors import FactorModel
from .firing import FiringModel, namespace_from_state
from .impacts import ImpactLedger
from .memory import MemoryModel
from .state import StateTensor, bind_names, resolve_key


@dataclass
class EventLog:
    """Columnar event log with provenance (ADR-9), one row per firing, ordered by (run, year, event).

    ``magnitudes`` is a second table in row order: for each firing, its impact rows ``(firing, row, M)`` with
    ``firing`` the index into this log and ``row`` the ``impact_table`` row, ascending within a firing
    (``EventFiring.magnitudes`` of the reference).
    """
    run: np.ndarray            # int64 [n]  global run index
    year: np.ndarray           # int64 [n]
    event: np.ndarray          # int64 [n]
    resolution: np.ndarray     # int64 [n]
    branch: np.ndarray         # int64 [n]
    p_base: np.ndarray         # float64 [n]
    p_eff: np.ndarray          # float64 [n]
    cascade_mask: np.ndarray   # int64 [n]  bit i set <=> a cascade from source event i was active at firing
    mag_firing: np.ndarray     # int64 [m]
    mag_row: np.ndarray        # int64 [m]
    mag_M: np.ndarray          # float64 [m]

    def __len__(self) -> int:
        return len(self.run)

    def magnitudes(self, i: int) -> list[tuple[int, float]]:
        """``(row, M)`` of firing ``i``, rows ascending."""
        k = np.flatnonzero(self.mag_firing == i)
        return [(int(self.mag_row[j]), float(self.mag_M[j])) for j in k]

    def firings_of(self, run: int) -> np.ndarray:
        """Indices of the log rows of global run ``run``, in (year, event) order."""
        return np.flatnonzero(self.run == run)


@dataclass
class RunOutputs:
    """In-memory outputs of ``simulate`` (README §4 item 21). ``T = params.years``; trajectories have ``T + 1``
    entries with index 0 the initial conditions and ``t + 1`` the end of year ``years[t]``."""
    years: np.ndarray            # int64 [T]
    country: np.ndarray          # float64 [R, N_ent, N_cvar]   terminal state
    global_: np.ndarray          # float64 [R, N_gvar]
    factors: np.ndarray          # float64 [R, K, T]
    thin_keys: list[str]
    thin: np.ndarray             # float64 [R, n_thin, T + 1]
    full_country: np.ndarray     # float64 [n_full, T + 1, N_ent, N_cvar]   runs 0 .. n_full − 1
    full_global: np.ndarray      # float64 [n_full, T + 1, N_gvar]
    flag_names: list[str]
    scenario_flags: np.ndarray   # bool [R, n_flags]
    max_active_seen: np.ndarray  # int64 [R]   peak live shocks in the ledger
    events: EventLog

    @property
    def R(self) -> int:
        return self.country.shape[0]

    @property
    def T(self) -> int:
        return len(self.years)


def simulate(catalog: CompiledCatalog, initial_conditions: InitialConditions, dynamics: DynamicsSpec,
             params: SimParams, R: int, seed: int, recording: RecordingSpec | None = None) -> RunOutputs:
    """Run ``R`` runs over ``params.years`` years from ``seed`` (guide §4.6) and record per ``recording``."""
    recording = RecordingSpec() if recording is None else recording
    R = int(R)
    if R < 1:
        raise ValueError("R must be >= 1")
    if recording.n_full > R:
        raise ValueError(f"recording.n_full ({recording.n_full}) exceeds R ({R})")
    T = params.years
    idx = catalog.index
    n_ent, n_cvar, n_gvar = len(idx.entity), len(idx.country_var), len(idx.global_var)
    E, K = catalog.n_events, catalog.n_factors

    fm, fr, dm = FactorModel.from_catalog(catalog), FiringModel(catalog), DynamicsModel(catalog, dynamics)
    thin_loc = [resolve_key(catalog, k) for k in recording.thin_keys]
    flags = recording.scenario_flags
    flag_names = sorted({n for f in flags for n in f.condition.names})
    for n in flag_names:
        if n not in idx.factor:
            resolve_key(catalog, n)                       # KeyError at the seam, not in year 0
    min_years = np.array([f.min_years for f in flags], dtype=np.int64)
    n_full, n_thin, n_flags = recording.n_full, len(thin_loc), len(flags)

    draws = SeededDraws(seed, R, DrawShapes.for_catalog(catalog, len(dynamics.noisy_keys)),
                        block_size=params.block_size, years=T)
    years = params.start_year + np.arange(T, dtype=np.int64)
    out_country = np.zeros((R, n_ent, n_cvar))
    out_global = np.zeros((R, n_gvar))
    factors = np.zeros((R, K, T))
    thin = np.zeros((R, n_thin, T + 1))
    full_country = np.zeros((n_full, T + 1, n_ent, n_cvar))
    full_global = np.zeros((n_full, T + 1, n_gvar))
    scenario_flags = np.zeros((R, n_flags), dtype=bool)
    max_active_seen = np.zeros(R, dtype=np.int64)
    log_cols: dict[str, list[np.ndarray]] = {k: [] for k in ("run", "year", "event", "resolution", "branch",
                                                             "p_base", "p_eff", "cascade_mask")}
    mag_cols: dict[str, list[np.ndarray]] = {k: [] for k in ("firing", "row", "M")}
    row_event = catalog.impact_table["event"].astype(np.int64)
    n_logged = 0

    for b in range(draws.n_blocks):
        start, stop = draws.block_rows(b)
        rb = stop - start
        stream = draws.stream(b)
        thr = fr.thresholds(stream.init["t2_offset"])
        mem = MemoryModel(catalog, rb, run_offset=start)
        led = ImpactLedger(catalog, rb, run_offset=start, max_active=params.max_active,
                           epsilon_cull=params.epsilon_cull)
        st = StateTensor.from_initial_conditions(catalog, initial_conditions, rb)
        counters = np.zeros((rb, n_flags), dtype=np.int64)
        flags_set = np.zeros((rb, n_flags), dtype=bool)
        full_lo, full_hi = start, min(stop, n_full)        # this block's runs with full trajectories

        def record_state(t1: int) -> None:
            for k, loc in enumerate(thin_loc):
                thin[start:stop, k, t1] = st.view(loc)
            if full_lo < full_hi:
                full_country[full_lo:full_hi, t1] = st.country[:full_hi - full_lo]
                full_global[full_lo:full_hi, t1] = st.global_[:full_hi - full_lo]

        record_state(0)
        for t in range(T):
            year = int(years[t])
            yr = stream.year(t)
            F, U = fm.year(yr)                                                          # 1-2
            ns = namespace_from_state(catalog, F, st.country, st.global_)
            res = fr.base(ns, year, mem.events, thr, mem.counters)                      # 3
            delta, mask = mem.deltas()
            p_eff = res.p_base + delta
            fired = fr.fire(res.gate, U, p_eff)                                         # 4
            codes, branches = mem.resolve(fired, yr["res_u"], yr["branch_u"], ns, year)  # 5
            draw = led.resolve(fired, codes, branches, yr["impact_z"], year)
            led.apply(st.country, st.global_, year)                                     # 6
            max_active_seen[start:stop] = np.maximum(max_active_seen[start:stop], led.n_live)
            dm.step(st.country, st.global_, yr["dyn_z"])                                # 7
            mem.end_of_year(res.sustained_now, year)                                    # 8
            led.end_of_year(year)

            # 9. RECORD
            factors[start:stop, :, t] = F
            r, e = np.nonzero(fired)                                                    # (run, event) ascending
            log_cols["run"].append(r.astype(np.int64) + start)
            log_cols["year"].append(np.full(len(r), year, dtype=np.int64))
            log_cols["event"].append(e.astype(np.int64))
            log_cols["resolution"].append(codes[r, e].astype(np.int64))
            log_cols["branch"].append(branches[r, e].astype(np.int64))
            log_cols["p_base"].append(res.p_base[r, e])
            log_cols["p_eff"].append(p_eff[r, e])
            log_cols["cascade_mask"].append(mask[r, e].astype(np.int64))
            mr, mj = np.nonzero(draw.selected)                                          # (run, row) ascending
            firing_key = r.astype(np.int64) * E + e
            mag_key = mr.astype(np.int64) * E + row_event[mj]
            fi = np.searchsorted(firing_key, mag_key)
            if len(mj) and ((fi >= len(firing_key)).any() or (firing_key[np.minimum(fi, len(firing_key) - 1)] != mag_key).any()):
                raise RuntimeError("impact rows selected for an event that did not fire")
            mag_cols["firing"].append(fi.astype(np.int64) + n_logged)
            mag_cols["row"].append(mj.astype(np.int64))
            mag_cols["M"].append(draw.magnitude[mr, mj])
            n_logged += len(r)
            record_state(t + 1)
            if n_flags:
                fns = bind_names(catalog, flag_names, F, st)                            # end-of-year state
                for j, flag in enumerate(flags):
                    held = flag.condition(fns)
                    counters[:, j] = np.where(held, counters[:, j] + 1, 0)
                flags_set |= counters >= min_years
        out_country[start:stop], out_global[start:stop] = st.country, st.global_
        scenario_flags[start:stop] = flags_set

    cols = {k: np.concatenate(v) if v else np.zeros(0, dtype=np.int64 if k not in ("p_base", "p_eff") else np.float64)
            for k, v in log_cols.items()}
    mags = {k: np.concatenate(v) if v else np.zeros(0, dtype=np.float64 if k == "M" else np.int64)
            for k, v in mag_cols.items()}
    order = np.lexsort((cols["event"], cols["year"], cols["run"]))                     # (run, year, event)
    inverse = np.empty(len(order), dtype=np.int64)
    inverse[order] = np.arange(len(order))
    cols = {k: v[order] for k, v in cols.items()}
    mag_firing = inverse[mags["firing"]]
    morder = np.lexsort((mags["row"], mag_firing))
    events = EventLog(cols["run"], cols["year"], cols["event"], cols["resolution"], cols["branch"],
                      cols["p_base"], cols["p_eff"], cols["cascade_mask"],
                      mag_firing[morder], mags["row"][morder], mags["M"][morder])
    return RunOutputs(years, out_country, out_global, factors, list(recording.thin_keys), thin,
                      full_country, full_global, list(recording.flag_names), scenario_flags, max_active_seen, events)
