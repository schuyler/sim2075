"""E6 — impact transmission (ADR-6): the active-shock ledger, vectorized over runs.

Transcribes the impact parts of the reference engine's year step for a block of runs:

    step 5   for each fired (r, e) with drawn codes (res, br), every ``impact_table`` row with
             ``event == e, res_code == res, branch_code == br`` yields a shock of magnitude
             ``M = mean + std · impact_z[r, row]`` (``EventFiring.magnitudes``); the event is set active for
             ``resolves_after[e]`` years counting the firing year (``active_until = year + resolves_after − 1``)
    step 6   live shocks aged by 1 and moved from their previous contribution to the current one (the owner's
             active flag is the one step 5 already set this year); then freed: ``until: resolved`` with its owner
             inactive, ``permanent`` once its onset completes (the level stays in state), ``decay`` once past
             onset with ``|contribution| < epsilon_cull · |M|`` (returned exactly to 0 first). This year's
             shocks are then applied from 0 at age 0 and slotted, except ``permanent`` + ``immediate`` (folded
             into state at firing) and ``M == 0``
    step 8   event active flags cleared where ``year ≥ active_until``

Shock schedule and increments are README §3 "Shock schedule": additive rows move the state by ``cur − prev``,
multiplicative rows by ``(1 + cur) / (1 + prev)``; a multiplicative contribution ≤ −1 is ``ImpactOutOfRange``.

Storage is pinned decision #2/#3: parallel ``[R, max_active]`` slot arrays on the run axis (guide §4.4, plus
``row``, ``prev`` and ``mult``; README §3), slots recycled lowest-free-first. More live shocks than
``max_active`` in any run is a counted hard failure (``LedgerOverflow``), never a drop. Both hard failures
name the year and the list of global run indices (``run_offset`` + row), E5's convention.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..catalog.types import (CompiledCatalog, DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED, ENTITY_GLOBAL,
                             ONSET_DELAYED, ONSET_GRADUAL, ONSET_IMMEDIATE)
from ..reference.model import ImpactOutOfRange, LedgerOverflow, SimParams
from .firing import NEVER_FIRED
from .memory import MAX_ACTIVE


def _onset_end(onset_kind: np.ndarray, onset_years: np.ndarray) -> np.ndarray:
    """Age at which the onset ramp reaches full magnitude: immediate 0, delayed N, gradual N − 1 (int64)."""
    n = onset_years.astype(np.int64)
    return np.where(onset_kind == ONSET_DELAYED, n, np.where(onset_kind == ONSET_GRADUAL, n - 1, 0))


def _contribution(M, onset_kind, onset_years, dur_kind, dur_param, age, owner_active) -> np.ndarray:
    """Current contribution of each shock at its age (README §3 schedule; the reference's ``shock_contribution``).

    All arguments are 1-D and aligned; ``owner_active`` is the owner event's active flag per shock.
    """
    age_f = age.astype(np.float64)
    n = onset_years.astype(np.float64)
    ramp = np.ones_like(M)
    d = onset_kind == ONSET_DELAYED
    ramp[d] = np.where(age_f[d] < n[d], 0.0, 1.0)
    g = onset_kind == ONSET_GRADUAL
    ramp[g] = np.minimum(age_f[g] + 1.0, n[g]) / n[g]
    cur = M * ramp
    end = _onset_end(onset_kind, onset_years)
    dec = (dur_kind == DUR_DECAY) & (age > end)
    cur[dec] = cur[dec] * 0.5 ** ((age_f[dec] - end[dec]) / dur_param[dec])
    cur[(dur_kind == DUR_UNTIL_RESOLVED) & ~owner_active] = 0.0
    return cur


def _apply(country: np.ndarray, global_: np.ndarray, r, ent, var, mult, prev, cur) -> None:
    """Move each shock's contribution from ``prev`` to ``cur`` in state (the reference's ``_apply``, unchecked).

    Shocks sharing a target accumulate (``ufunc.at``); the range check is the caller's, before any mutation.
    """
    ch = cur != prev
    glob = ent == ENTITY_GLOBAL
    add = ch & ~mult
    inc = cur - prev
    k = add & glob
    np.add.at(global_, (r[k], var[k]), inc[k])
    k = add & ~glob
    np.add.at(country, (r[k], ent[k], var[k]), inc[k])
    m = ch & mult
    factor = np.ones_like(cur)
    factor[m] = (1.0 + cur[m]) / (1.0 + prev[m])
    k = m & glob
    np.multiply.at(global_, (r[k], var[k]), factor[k])
    k = m & ~glob
    np.multiply.at(country, (r[k], ent[k], var[k]), factor[k])


@dataclass
class ImpactDraw:
    """Step 5's selection: ``selected`` bool [R, n_rows] (row applies to run r this year), ``magnitude``
    float64 [R, n_rows] (``M``, drawn for every row and run; meaningful only where selected)."""
    selected: np.ndarray
    magnitude: np.ndarray
    row_event: np.ndarray

    def for_firing(self, i: int, e: int) -> list[tuple[int, float]]:
        """``(row, M)`` for event ``e`` in block row ``i``, rows ascending (``EventFiring.magnitudes``)."""
        rows = np.flatnonzero(self.selected[i] & (self.row_event == e))
        return [(int(j), float(self.magnitude[i, j])) for j in rows]


class ImpactLedger:
    """Active-shock ledger and per-event active flags for a block of ``R`` runs starting at ``run_offset``."""

    def __init__(self, catalog: CompiledCatalog, R: int, run_offset: int = 0, max_active: int = MAX_ACTIVE,
                 epsilon_cull: float = SimParams.epsilon_cull):
        self.cat = catalog
        self.R, self.E = int(R), catalog.n_events
        self.run_offset = int(run_offset)
        self.max_active = int(max_active)
        self.epsilon_cull = float(epsilon_cull)
        if self.max_active < 1:
            raise ValueError("max_active must be >= 1")

        it = catalog.impact_table
        self.row_event = it["event"].astype(np.intp)
        self.row_res = it["res_code"].astype(np.int64)
        self.row_branch = it["branch_code"].astype(np.int64)
        self.row_mean = it["mean"].astype(np.float64)
        self.row_std = it["std"].astype(np.float64)
        self.resolves_after = np.asarray(catalog.resolves_after, dtype=np.int64)
        if self.resolves_after.shape != (self.E,):
            raise ValueError(f"resolves_after must be [{self.E}], got {self.resolves_after.shape}")

        shape = (self.R, self.max_active)
        self.active = np.zeros(shape, dtype=bool)
        self.entity_idx = np.zeros(shape, dtype=np.int16)
        self.var_idx = np.zeros(shape, dtype=np.int16)
        self.magnitude = np.zeros(shape, dtype=np.float64)
        self.onset_kind = np.zeros(shape, dtype=np.int8)
        self.onset_years = np.zeros(shape, dtype=np.int8)
        self.dur_kind = np.zeros(shape, dtype=np.int8)
        self.dur_param = np.zeros(shape, dtype=np.float64)
        self.age = np.zeros(shape, dtype=np.int16)
        self.owner_event = np.zeros(shape, dtype=np.int16)
        self.row = np.zeros(shape, dtype=np.int32)          # impact_table row (provenance; ImpactOutOfRange)
        self.prev = np.zeros(shape, dtype=np.float64)       # the contribution currently in state
        self.mult = np.zeros(shape, dtype=bool)             # multiplicative row
        self.overflow_count = np.zeros(self.R, dtype=np.int64)   # shocks that found no slot, per run

        self.event_active = np.zeros((self.R, self.E), dtype=bool)                   # owner flags (until: resolved)
        self.active_until = np.full((self.R, self.E), NEVER_FIRED, dtype=np.int64)
        self._pending: ImpactDraw | None = None

    # -- step 5 ----------------------------------------------------------------
    def resolve(self, fired: np.ndarray, res: np.ndarray, br: np.ndarray, impact_z: np.ndarray,
                year: int) -> ImpactDraw:
        """Select this year's impact rows, draw their magnitudes and set the fired events active.

        ``res``/``br`` are the step-5 codes (``MemoryModel.resolve`` / ``draw_codes``), int [R, E];
        ``impact_z`` [R, n_rows]. The selection is held for this year's ``apply``.
        """
        n_rows = len(self.row_event)
        if fired.shape != (self.R, self.E) or res.shape != fired.shape or br.shape != fired.shape:
            raise ValueError(f"fired/res/br must be [{self.R}, {self.E}], got {fired.shape}, {res.shape}, {br.shape}")
        impact_z = np.asarray(impact_z, dtype=np.float64)
        if impact_z.shape != (self.R, n_rows):
            raise ValueError(f"impact_z must be [{self.R}, {n_rows}], got {impact_z.shape}")
        ev = self.row_event
        selected = fired[:, ev] & (res[:, ev] == self.row_res) & (br[:, ev] == self.row_branch)
        magnitude = self.row_mean + self.row_std * impact_z
        r, e = np.nonzero(fired)
        self.event_active[r, e] = True
        self.active_until[r, e] = year + self.resolves_after[e] - 1   # resolves_after counts the firing year
        self._pending = ImpactDraw(selected, magnitude, ev)
        return self._pending

    # -- step 6 ----------------------------------------------------------------
    def apply(self, country: np.ndarray, global_: np.ndarray, year: int) -> None:
        """Age and apply live shocks, free spent slots, apply and slot this year's shocks (state in place).

        ``country`` float64 [R, N_ent, N_cvar], ``global_`` float64 [R, N_gvar]. Raises ``ImpactOutOfRange``
        (before any mutation) when a multiplicative contribution reaches ≤ −1, and ``LedgerOverflow`` when a run
        would hold more than ``max_active`` live shocks after this year's frees and pushes; both name the year
        and the offending runs' global indices (a list). ``ImpactOutOfRange`` reports the row and contribution
        of the lowest offending run's first offending shock (live slots in slot order, then this year's rows).
        """
        if self._pending is None:
            raise RuntimeError("ImpactLedger.apply called without this year's resolve")
        draw, self._pending = self._pending, None
        idx = self.cat.index
        if country.dtype != np.float64 or country.shape != (self.R, len(idx.entity), len(idx.country_var)):
            raise ValueError(f"country must be float64 [{self.R}, {len(idx.entity)}, {len(idx.country_var)}], "
                             f"got {country.dtype} {country.shape}")
        if global_.dtype != np.float64 or global_.shape != (self.R, len(idx.global_var)):
            raise ValueError(f"global_ must be float64 [{self.R}, {len(idx.global_var)}], got {global_.dtype} {global_.shape}")

        # live shocks, aged by one year; owner flag as already updated by this year's step 5
        if self.active.any() and self.age[self.active].max() >= np.iinfo(self.age.dtype).max:
            raise OverflowError("shock age exceeds the int16 age slot field")
        lr, ls = np.nonzero(self.active)
        age = self.age[lr, ls] + 1
        M = self.magnitude[lr, ls]
        ok, oy, dk = self.onset_kind[lr, ls], self.onset_years[lr, ls], self.dur_kind[lr, ls]
        owner = self.owner_event[lr, ls].astype(np.intp)
        owner_active = self.event_active[lr, owner]
        cur = _contribution(M, ok, oy, dk, self.dur_param[lr, ls], age, owner_active)
        prev = self.prev[lr, ls]
        ent = self.entity_idx[lr, ls].astype(np.intp)
        var = self.var_idx[lr, ls].astype(np.intp)
        mult = self.mult[lr, ls]

        # this year's shocks at age 0, owner active (it just fired)
        it = self.cat.impact_table
        nr, nj = np.nonzero(draw.selected)
        nM = draw.magnitude[nr, nj]
        n_ok, n_oy, n_dk = it["onset_kind"][nj], it["onset_years"][nj], it["dur_kind"][nj]
        n_cur = _contribution(nM, n_ok, n_oy, n_dk, it["dur_param"][nj], np.zeros(len(nj), dtype=np.int64),
                              np.ones(len(nj), dtype=bool))
        n_prev = np.zeros(len(nj))
        n_ent = it["entity_idx"][nj].astype(np.intp)
        n_var = it["var_idx"][nj].astype(np.intp)
        n_mult = it["multiplicative"][nj].astype(bool)

        self._check_range(year, lr, self.row[lr, ls], mult, prev, cur, nr, nj, n_mult, n_prev, n_cur)

        _apply(country, global_, lr, ent, var, mult, prev, cur)
        end = _onset_end(ok, oy)
        free = np.zeros(len(lr), dtype=bool)
        free |= (dk == DUR_UNTIL_RESOLVED) & ~owner_active        # owner resolved: contribution now 0
        free |= (dk == DUR_PERMANENT) & (age >= end)              # fully onset: level shift stays in state
        cull = (dk == DUR_DECAY) & (age > end) & (np.abs(cur) < self.epsilon_cull * np.abs(M))
        _apply(country, global_, lr[cull], ent[cull], var[cull], mult[cull], cur[cull], np.zeros(int(cull.sum())))
        free |= cull                                              # epsilon-cull: returned exactly to 0
        self.age[lr, ls] = age
        self.prev[lr, ls] = np.where(cull, 0.0, cur)
        self.active[lr[free], ls[free]] = False

        _apply(country, global_, nr, n_ent, n_var, n_mult, n_prev, n_cur)
        slot_it = ~((n_dk == DUR_PERMANENT) & (n_ok == ONSET_IMMEDIATE)) & (nM != 0.0)
        nr, nj, nM, n_cur = nr[slot_it], nj[slot_it], nM[slot_it], n_cur[slot_it]

        need = np.bincount(nr, minlength=self.R)
        free_slots = ~self.active
        n_free = free_slots.sum(axis=1)
        over = need > n_free
        if over.any():
            self.overflow_count += np.where(over, need - n_free, 0)
            runs = (np.flatnonzero(over) + self.run_offset).tolist()
            live = self.active.sum(axis=1) + need
            raise LedgerOverflow(runs, year, int(live[over].max()), self.max_active)

        # the k-th new shock of run r (rows ascending) takes run r's k-th free slot (ascending)
        rank = np.arange(len(nr)) - np.concatenate(([0], np.cumsum(need)[:-1]))[nr]
        _, fs = np.nonzero(free_slots)
        first_free = np.concatenate(([0], np.cumsum(n_free)[:-1]))
        slot = fs[first_free[nr] + rank]
        self.active[nr, slot] = True
        self.entity_idx[nr, slot] = it["entity_idx"][nj]
        self.var_idx[nr, slot] = it["var_idx"][nj]
        self.magnitude[nr, slot] = nM
        self.onset_kind[nr, slot] = it["onset_kind"][nj]
        self.onset_years[nr, slot] = it["onset_years"][nj]
        self.dur_kind[nr, slot] = it["dur_kind"][nj]
        self.dur_param[nr, slot] = it["dur_param"][nj]
        self.age[nr, slot] = 0
        self.owner_event[nr, slot] = it["event"][nj]
        self.row[nr, slot] = nj
        self.prev[nr, slot] = n_cur
        self.mult[nr, slot] = it["multiplicative"][nj]

    def _check_range(self, year, lr, lrow, mult, prev, cur, nr, nj, n_mult, n_prev, n_cur) -> None:
        bad = mult & (cur != prev) & (cur <= -1.0)
        n_bad = n_mult & (n_cur != n_prev) & (n_cur <= -1.0)
        if not (bad.any() or n_bad.any()):
            return
        runs = np.unique(np.concatenate((lr[bad], nr[n_bad])))
        first = runs[0]
        k = np.flatnonzero(bad & (lr == first))
        if len(k):
            row, c = int(lrow[k[0]]), float(cur[k[0]])
        else:
            k = np.flatnonzero(n_bad & (nr == first))
            row, c = int(nj[k[0]]), float(n_cur[k[0]])
        raise ImpactOutOfRange((runs + self.run_offset).tolist(), year, row, c)

    # -- step 8 ----------------------------------------------------------------
    def end_of_year(self, year: int) -> None:
        """Clear event active flags whose window ends this year (``year ≥ active_until``)."""
        self.event_active &= ~(year >= self.active_until)

    @property
    def n_live(self) -> np.ndarray:
        """Live shocks per run, int64 [R]."""
        return self.active.sum(axis=1).astype(np.int64)
