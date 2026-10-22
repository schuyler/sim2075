"""E5 — per-run memory (ADR-5), vectorized over runs: sustained counters, cascade slots, event state.

Transcribes the memory parts of the reference engine's year step for a block of runs:

    step 3   cascade deltas:  p_eff = p_base + Σ active deltas into each event, plus the source bitmask
             (bit ``src`` set in ``[r, dst]`` for each active cascade, as ``EventFiring.cascade_mask``)
    step 5   resolution/branch codes by inverse CDF over the resolution tree (``res_u`` then ``branch_u``);
             ``EventState`` updated where fired; each ``triggers`` edge's ``if`` evaluated with the source
             event's just-drawn codes and pushed as pending
    step 8   sustained counters from the same evaluation the step-3 gate used (+1 held, 0 failed); active
             cascades decremented and expired at 0; pending pushes admitted (README §3: a cascade pushed in
             year t is active in t+1 … t+years, never in t)

Cascade storage is pinned decision #2/#3: parallel ``[R, max_active]`` slot arrays on the run axis
(``active``, ``dst_event``, ``delta``, ``years_remaining``, ``src_event``), slots recycled lowest-free-first.
More live cascades than ``max_active`` in any run is a counted hard failure (``LedgerOverflow``), never a drop.

``draw_codes`` is the step-5 resolution/branch draw for every event and run; E6 reuses it for impact rows.
"""
from __future__ import annotations

import numpy as np

from ..catalog.types import CompiledCatalog
from ..reference.model import LedgerOverflow
from .firing import EventState

MAX_ACTIVE = 256   # pinned decision #3: slots per run


def draw_codes(catalog: CompiledCatalog, res_u: np.ndarray, branch_u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Resolution and branch codes for every run and event, int64 [R, E] each.

    Inverse CDF over each event's ``resolution_p`` with ``res_u[:, e]``, then over the drawn resolution's
    ``branch_p`` with ``branch_u[:, e]``: ``min(searchsorted(cumsum(p), u, side="right"), n − 1)``, the
    reference's ``_draw_code`` arithmetic, so a uniform exactly on a cumulative boundary takes the upper code.
    Drawn for all runs (outcome-independent shapes); callers use the codes only where fired.
    """
    res_u = np.asarray(res_u, dtype=np.float64)
    branch_u = np.asarray(branch_u, dtype=np.float64)
    R, E = res_u.shape
    if E != catalog.n_events or branch_u.shape != (R, E):
        raise ValueError(f"res_u/branch_u must be [R, {catalog.n_events}], got {res_u.shape}, {branch_u.shape}")
    res = np.empty((R, E), dtype=np.int64)
    br = np.empty((R, E), dtype=np.int64)
    for e in range(E):
        tree = catalog.resolution_tree[e]
        cum = np.cumsum(tree.resolution_p)
        res[:, e] = np.minimum(np.searchsorted(cum, res_u[:, e], side="right"), len(cum) - 1)
        for k in range(tree.n_resolutions):
            sel = res[:, e] == k
            bcum = np.cumsum(tree.branch_p[k])
            br[sel, e] = np.minimum(np.searchsorted(bcum, branch_u[sel, e], side="right"), len(bcum) - 1)
    return res, br


class MemoryModel:
    """Per-run memory for a block of ``R`` runs whose first global run index is ``run_offset``."""

    def __init__(self, catalog: CompiledCatalog, R: int, run_offset: int = 0, max_active: int = MAX_ACTIVE):
        self.cat = catalog
        self.R, self.E = int(R), catalog.n_events
        self.run_offset = int(run_offset)
        self.max_active = int(max_active)
        if self.E >= 64:
            raise ValueError(f"{self.E} events: the int64 cascade source bitmask holds at most 63")
        if self.max_active < 1:
            raise ValueError("max_active must be >= 1")

        self.type3_order = sorted(catalog.type3)
        self.counters = {e: np.zeros((self.R, len(catalog.type3[e].sustained)), dtype=np.int64) for e in self.type3_order}
        self.events = EventState.fresh(self.R, self.E)

        edges = catalog.cascade_edges
        self.edge_src = np.array([c.src_event for c in edges], dtype=np.int16)
        self.edge_dst = np.array([c.dst_event for c in edges], dtype=np.int16)
        self.edge_delta = np.array([c.delta for c in edges], dtype=np.float64)
        years = np.array([c.years for c in edges], dtype=np.int64)
        if (years > np.iinfo(np.int16).max).any():
            raise ValueError("cascade years exceed the int16 years_remaining slot field")
        self.edge_years = years.astype(np.int16)

        shape = (self.R, self.max_active)
        self.active = np.zeros(shape, dtype=bool)
        self.dst_event = np.zeros(shape, dtype=np.int16)
        self.delta = np.zeros(shape, dtype=np.float64)
        self.years_remaining = np.zeros(shape, dtype=np.int16)
        self.src_event = np.zeros(shape, dtype=np.int16)
        self.overflow_count = np.zeros(self.R, dtype=np.int64)    # cascades that found no slot, per run
        self._pending = np.zeros((self.R, len(edges)), dtype=bool)

    # -- step 3 ----------------------------------------------------------------
    def deltas(self) -> tuple[np.ndarray, np.ndarray]:
        """Active cascade deltas summed per target, float64 [R, E], and the source bitmask, int64 [R, E]."""
        delta = np.zeros((self.R, self.E), dtype=np.float64)
        mask = np.zeros((self.R, self.E), dtype=np.int64)
        r, s = np.nonzero(self.active)
        dst = self.dst_event[r, s].astype(np.intp)
        np.add.at(delta, (r, dst), self.delta[r, s])
        np.bitwise_or.at(mask, (r, dst), np.left_shift(np.int64(1), self.src_event[r, s].astype(np.int64)))
        return delta, mask

    # -- step 5 ----------------------------------------------------------------
    def resolve(self, fired: np.ndarray, res_u: np.ndarray, branch_u: np.ndarray, ns: dict,
                year: int) -> tuple[np.ndarray, np.ndarray]:
        """Draw codes, record firings in ``EventState``, queue this year's cascade pushes; returns the codes.

        ``ns`` is the start-of-year namespace step 3 used. Each edge's ``if`` sees its source event's new
        ``resolution``/``branch`` and ``years_since`` 0, as the reference's ``_event_ns`` after the update.
        """
        if fired.shape != (self.R, self.E):
            raise ValueError(f"fired must be [{self.R}, {self.E}], got {fired.shape}")
        res, br = draw_codes(self.cat, res_u, branch_u)
        ev = self.events
        ev.last_res[fired] = res[fired]
        ev.last_branch[fired] = br[fired]
        ev.last_fire_year[fired] = year
        for j, edge in enumerate(self.cat.cascade_edges):
            push = fired[:, edge.src_event].copy()
            if edge.cond is not None:
                push &= edge.cond(self._event_ns(ns, edge.src_event, year))
            self._pending[:, j] |= push
        return res, br

    def _event_ns(self, ns: dict, e: int, year: int) -> dict:
        d = dict(ns)
        d["resolution"] = self.events.last_res[:, e]
        d["branch"] = self.events.last_branch[:, e]
        d["years_since"] = (year - self.events.last_fire_year[:, e]).astype(np.float64)
        return d

    # -- step 8 ----------------------------------------------------------------
    def end_of_year(self, sustained_now: dict[int, np.ndarray], year: int) -> None:
        """Update counters from step 3's evaluations, age and expire cascades, admit this year's pushes.

        Raises ``LedgerOverflow`` naming the overflowing runs' global indices (a list) and the year when
        any run would hold more than ``max_active`` live cascades; the shortfall is added to ``overflow_count``.
        """
        for e in self.type3_order:
            now = sustained_now[e]
            c = self.counters[e]
            if now.shape != c.shape:
                raise ValueError(f"event {e}: sustained evaluations {now.shape} do not match counters {c.shape}")
            self.counters[e] = np.where(now, c + 1, 0)

        self.years_remaining[self.active] -= 1
        self.active &= self.years_remaining > 0

        need = self._pending.sum(axis=1)
        free = ~self.active
        n_free = free.sum(axis=1)
        over = need > n_free
        if over.any():
            self.overflow_count += np.where(over, need - n_free, 0)
            runs = (np.flatnonzero(over) + self.run_offset).tolist()
            live = self.active.sum(axis=1) + need
            raise LedgerOverflow(runs, year, int(live[over].max()), self.max_active)

        # the k-th pending push of run r takes run r's k-th free slot (ascending)
        pr, pj = np.nonzero(self._pending)
        rank = (np.cumsum(self._pending, axis=1) - 1)[pr, pj]
        _, free_slots = np.nonzero(free)
        first_free = np.concatenate(([0], np.cumsum(n_free)[:-1]))
        slot = free_slots[first_free[pr] + rank]
        self.active[pr, slot] = True
        self.dst_event[pr, slot] = self.edge_dst[pj]
        self.delta[pr, slot] = self.edge_delta[pj]
        self.years_remaining[pr, slot] = self.edge_years[pj]
        self.src_event[pr, slot] = self.edge_src[pj]
        self._pending[:] = False
