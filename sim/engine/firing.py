"""E4 — per-type thresholds, gates and the fire mask (ADR-3), vectorized over runs.

Transcribes the reference engine's steps 3–4 for a block of runs:

    Type 1   p_base = annual
    Type 2   p_base = floor + (1 − floor) · σ(k · (pressure(ns) − threshold_r)),  threshold_r drawn once per run
    Type 3   p_base = window · resolution;  gate = all(preconditions(ns)) ∧ all(counter ≥ years)
    fired    = gate & (U < p_eff),  p_eff = p_base + cascade deltas (E5 supplies the deltas; 0 until then)

Expressions are the catalog's §4.3 callables, evaluated once over ``(R,)`` views. The namespace is built
by ``namespace_from_state`` from the state tensor and this year's factors; each event adds its own
``resolution`` / ``branch`` / ``years_since`` columns from ``EventState`` (per-run memory that E5 will own
the updates of; E4 only reads it).

``p_eff`` is not clamped (README §3): ≤ 0 never fires, ≥ 1 always fires. Sustained-condition evaluations
are returned so that step 8 (E5) updates counters from the same evaluation the gate used.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.special import expit

from ..catalog.types import CompiledCatalog

NEVER_FIRED = -(10 ** 6)   # same sentinel as the reference engine: years_since is then huge


@dataclass
class EventState:
    """Per-run event memory read by expressions: last resolution/branch codes and last firing year, [R, E]."""
    last_res: np.ndarray         # int64 [R, E], -1 = never
    last_branch: np.ndarray      # int64 [R, E], -1 = never
    last_fire_year: np.ndarray   # int64 [R, E], NEVER_FIRED = never

    @classmethod
    def fresh(cls, R: int, E: int) -> "EventState":
        return cls(np.full((R, E), -1, dtype=np.int64), np.full((R, E), -1, dtype=np.int64),
                   np.full((R, E), NEVER_FIRED, dtype=np.int64))


@dataclass
class FiringResult:
    p_base: np.ndarray                           # float64 [R, E]
    gate: np.ndarray                             # bool [R, E]
    sustained_now: dict[int, np.ndarray] = field(default_factory=dict)   # event -> bool [R, n_sustained]


def namespace_from_state(catalog: CompiledCatalog, F: np.ndarray, country: np.ndarray, global_: np.ndarray) -> dict:
    """Bind every name any catalog expression reads (except event state) to an ``(R,)`` view.

    ``F`` [R, K] this year's factors; ``country`` [R, N_ent, N_cvar]; ``global_`` [R, N_gvar].
    """
    R = F.shape[0]
    idx = catalog.index
    if country.shape[0] != R or global_.shape[0] != R:
        raise ValueError("state tensors and factor draws disagree on R")
    ns: dict = {"_shape": (R,)}
    for name in catalog.expression_names():
        if name in ("resolution", "branch", "years_since"):
            continue
        if name in idx.factor:
            ns[name] = F[:, idx.factor[name]]
        elif "." in name:
            ent, var = name.split(".", 1)
            ns[name] = country[:, idx.entity[ent], idx.country_var[var]]
        elif name in idx.global_var:
            ns[name] = global_[:, idx.global_var[name]]
        else:
            raise KeyError(f"expression name {name!r} is not a factor, global variable or entity.variable")
    return ns


class FiringModel:
    def __init__(self, catalog: CompiledCatalog):
        self.cat = catalog
        self.E = catalog.n_events
        self.causal_type = np.asarray(catalog.causal_type)
        self.type2_order = sorted(catalog.type2)          # column order of the t2_offset draw (shared with reference)
        self.p_annual = np.asarray(catalog.p_annual, dtype=np.float64)
        if np.isnan(self.p_annual[self.causal_type == 1]).any():
            raise ValueError("Type 1 event without p_annual")

    # -- init-time -----------------------------------------------------------
    def thresholds(self, t2_offset: np.ndarray) -> np.ndarray:
        """Per-run Type 2 thresholds (pinned #1): threshold + threshold_std · z, [R, E_type2] in ``type2_order``."""
        t2_offset = np.asarray(t2_offset, dtype=np.float64)
        if t2_offset.ndim != 2 or t2_offset.shape[1] != len(self.type2_order):
            raise ValueError(f"t2_offset must be [R, {len(self.type2_order)}], got {t2_offset.shape}")
        base = np.array([self.cat.type2[e].threshold for e in self.type2_order], dtype=np.float64)
        std = np.array([self.cat.type2[e].threshold_std for e in self.type2_order], dtype=np.float64)
        return base + std * t2_offset

    # -- per year --------------------------------------------------------------
    def event_namespace(self, ns: dict, e: int, year: int, ev: EventState) -> dict:
        d = dict(ns)
        d["resolution"] = ev.last_res[:, e]
        d["branch"] = ev.last_branch[:, e]
        d["years_since"] = (year - ev.last_fire_year[:, e]).astype(np.float64)
        return d

    def base(self, ns: dict, year: int, ev: EventState, thresholds: np.ndarray,
             counters: dict[int, np.ndarray]) -> FiringResult:
        """Step 3 without cascade deltas: p_base [R, E], gate [R, E], and this year's sustained evaluations.

        ``counters``: Type 3 event -> int array [R, n_sustained] reflecting years ≤ year − 1 (README §3).
        """
        R = ns["_shape"][0]
        p_base = np.zeros((R, self.E), dtype=np.float64)
        gate = np.ones((R, self.E), dtype=bool)
        sustained_now: dict[int, np.ndarray] = {}
        for e in range(self.E):
            ct = int(self.causal_type[e])
            if ct == 1:
                p_base[:, e] = self.p_annual[e]
                continue
            ens = self.event_namespace(ns, e, year, ev)
            if ct == 2:
                s = self.cat.type2[e]
                thr = thresholds[:, self.type2_order.index(e)]
                pressure = s.pressure(ens)
                p_base[:, e] = s.floor + (1.0 - s.floor) * expit(s.sharpness * (pressure - thr))
            else:
                s = self.cat.type3[e]
                ok = np.ones(R, dtype=bool)
                for pre in s.preconditions:
                    ok &= pre(ens)
                c = counters.get(e)
                if len(s.sustained):
                    if c is None or c.shape != (R, len(s.sustained)):
                        raise ValueError(f"event {e}: sustained counters must be [R, {len(s.sustained)}]")
                    for j, (_expr, yrs) in enumerate(s.sustained):
                        ok &= c[:, j] >= yrs
                gate[:, e] = ok
                p_base[:, e] = s.window * s.resolution
                sustained_now[e] = np.stack([expr(ens) for expr, _ in s.sustained], axis=1) if s.sustained \
                    else np.zeros((R, 0), dtype=bool)
        return FiringResult(p_base, gate, sustained_now)

    @staticmethod
    def fire(gate: np.ndarray, U: np.ndarray, p_eff: np.ndarray) -> np.ndarray:
        """Step 4: fired = gate & (U < p_eff), bool [R, E]. No clamping of p_eff."""
        if not (gate.shape == U.shape == p_eff.shape):
            raise ValueError(f"shape mismatch: gate {gate.shape}, U {U.shape}, p_eff {p_eff.shape}")
        return gate & (U < p_eff)
