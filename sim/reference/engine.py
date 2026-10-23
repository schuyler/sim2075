"""The scalar reference stepper.

One run at a time; every operation is a plain Python statement over scalars and
tiny arrays so that the code reads as a transcription of
simulator-architecture §3 and the pinned decisions of implementation-guide §0.
Semantics pinned here (and documented in sim/README.md) are the semantics the
vectorized engine must reproduce exactly under shared draws.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math

import numpy as np
from scipy.special import ndtr

from ..catalog.types import (CompiledCatalog, DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED,
                             ENTITY_GLOBAL, ONSET_DELAYED, ONSET_GRADUAL, ONSET_IMMEDIATE)
from ..rng import DrawShapes
from .model import DynamicsSpec, ImpactOutOfRange, InitialConditions, LedgerOverflow, SimParams

NEVER_FIRED = -(10 ** 6)   # last_fire_year sentinel; years_since is then huge (> any horizon)


@dataclass
class EventFiring:
    year: int
    event: int
    resolution: int
    branch: int
    p_base: float
    p_eff: float
    cascade_mask: int                     # bit i set <=> a cascade from source event i was active at firing
    magnitudes: list[tuple[int, float]]   # (impact_table row, drawn magnitude M)


@dataclass
class _Shock:
    row: int
    entity_idx: int
    var_idx: int
    M: float
    onset_kind: int
    onset_years: int
    dur_kind: int
    dur_param: float
    owner_event: int
    mult: bool                # multiplicative (fraction of current value) vs additive in the variable's units
    age: int = 0
    prev: float = 0.0


@dataclass
class _Cascade:
    src: int
    dst: int
    delta: float
    remaining: int


@dataclass
class RunRecord:
    run_index: int
    years: list[int]
    country: np.ndarray        # [T+1, N_ent, N_cvar]; index 0 = initial conditions, t+1 = end of year t
    global_: np.ndarray        # [T+1, N_gvar]
    factors: np.ndarray        # [T, K]
    propensity_u: np.ndarray   # [T, E] the correlated uniforms
    p_eff: np.ndarray          # [T, E]
    gate: np.ndarray           # [T, E] bool
    events: list[EventFiring] = field(default_factory=list)
    max_active_seen: int = 0


def _onset_end(kind: int, n: int) -> int:
    """Age at which the onset ramp reaches full magnitude."""
    if kind == ONSET_IMMEDIATE:
        return 0
    if kind == ONSET_DELAYED:
        return n
    return n - 1   # gradual: min(age+1, N)/N == 1 at age N-1


def _ramp(kind: int, n: int, age: int) -> float:
    if kind == ONSET_IMMEDIATE:
        return 1.0
    if kind == ONSET_DELAYED:
        return 0.0 if age < n else 1.0
    return min(age + 1, n) / n


def shock_contribution(s: _Shock, owner_active: bool) -> float:
    """Current contribution of a shock at its current age (pinned schedule; see README)."""
    r = _ramp(s.onset_kind, s.onset_years, s.age)
    if s.dur_kind == DUR_UNTIL_RESOLVED:
        return s.M * r if owner_active else 0.0
    if s.dur_kind == DUR_PERMANENT:
        return s.M * r
    end = _onset_end(s.onset_kind, s.onset_years)
    if s.age <= end:
        return s.M * r
    return s.M * r * 0.5 ** ((s.age - end) / s.dur_param)


class ReferenceRun:
    def __init__(self, catalog: CompiledCatalog, ic: InitialConditions, dynamics: DynamicsSpec,
                 params: SimParams, draws, run_index: int):
        self.cat = catalog
        self.params = params
        self.run_index = run_index
        self.block, self.row = draws.block_of(run_index)
        self.stream = draws.stream(self.block)
        shapes = DrawShapes.for_catalog(catalog, len(dynamics.noisy_keys))
        if getattr(draws, "shapes", shapes) != shapes:
            raise ValueError(f"draw source shapes {draws.shapes} do not match catalog/dynamics {shapes}")

        idx = catalog.index
        self.n_ent, self.n_cvar, self.n_gvar = len(idx.entity), len(idx.country_var), len(idx.global_var)
        if ic.country.shape != (self.n_ent, self.n_cvar) or ic.global_.shape != (self.n_gvar,):
            raise ValueError("initial conditions do not match catalog axes")
        self.c = np.array(ic.country, dtype=np.float64)
        self.g = np.array(ic.global_, dtype=np.float64)

        # Ω Cholesky (ADR-2): F = L @ z gives N(0, Ω)
        self.L = np.linalg.cholesky(catalog.omega)
        E = catalog.n_events
        self.E = E
        self.type2_order = sorted(catalog.type2)          # column order of t2_offset draws
        self.thr = {}                                     # per-run Type 2 thresholds (pinned #1)
        for j, e in enumerate(self.type2_order):
            s = catalog.type2[e]
            self.thr[e] = s.threshold + s.threshold_std * float(self.stream.init["t2_offset"][self.row, j])

        # per-run memory (ADR-5)
        self.counters = {e: [0] * len(s.sustained) for e, s in catalog.type3.items()}
        self.cascades: list[_Cascade] = []
        self.ledger: list[_Shock] = []
        self.last_res = np.full(E, -1, dtype=np.int64)
        self.last_branch = np.full(E, -1, dtype=np.int64)
        self.last_fire_year = np.full(E, NEVER_FIRED, dtype=np.int64)
        self.active = np.zeros(E, dtype=bool)
        self.active_until = np.full(E, NEVER_FIRED, dtype=np.int64)

        # dynamics bindings
        self.dyn = dynamics
        self._loc = {}
        for v in dynamics.vars:
            self._loc[v.key] = self._resolve(v.key)
            if v.kind == "gdp_stock":
                self._loc[v.growth_key] = self._resolve(v.growth_key)
        self.noisy_col = {k: i for i, k in enumerate(dynamics.noisy_keys)}

        # expression namespace keys
        self.expr_names = sorted(catalog.expression_names())
        self._expr_loc = {n: self._resolve(n) for n in self.expr_names
                          if n not in ("resolution", "branch", "years_since") and n not in idx.factor}

    # -- helpers ------------------------------------------------------------
    def _resolve(self, key: str):
        idx = self.cat.index
        if "." in key:
            ent, var = key.split(".", 1)
            return ("c", idx.entity[ent], idx.country_var[var])
        if key in idx.global_var:
            return ("g", idx.global_var[key])
        raise KeyError(f"unknown state key {key!r}")

    def _get(self, loc) -> float:
        return float(self.c[loc[1], loc[2]]) if loc[0] == "c" else float(self.g[loc[1]])

    def _set(self, loc, val: float) -> None:
        if loc[0] == "c":
            self.c[loc[1], loc[2]] = val
        else:
            self.g[loc[1]] = val

    def _namespace(self, F: np.ndarray) -> dict:
        ns = {"_shape": (1,)}
        for f, k in self.cat.index.factor.items():
            ns[f] = np.array([F[k]])
        for n, loc in self._expr_loc.items():
            ns[n] = np.array([self._get(loc)])
        return ns

    def _event_ns(self, ns: dict, e: int, year: int) -> dict:
        d = dict(ns)
        d["resolution"] = np.array([self.last_res[e]])
        d["branch"] = np.array([self.last_branch[e]])
        d["years_since"] = np.array([year - self.last_fire_year[e]], dtype=np.float64)
        return d

    @staticmethod
    def _draw_code(u: float, probs: np.ndarray) -> int:
        cum = np.cumsum(probs)
        return int(min(np.searchsorted(cum, u, side="right"), len(probs) - 1))

    # -- the run --------------------------------------------------------------
    def run(self) -> RunRecord:
        cat, P, E = self.cat, self.params, self.E
        T = P.years
        rec = RunRecord(self.run_index, [P.start_year + t for t in range(T)],
                        np.zeros((T + 1, self.n_ent, self.n_cvar)), np.zeros((T + 1, self.n_gvar)),
                        np.zeros((T, cat.n_factors)), np.zeros((T, E)), np.zeros((T, E)), np.zeros((T, E), dtype=bool))
        rec.country[0], rec.global_[0] = self.c, self.g
        r = self.row
        for t in range(T):
            year = P.start_year + t
            d = self.stream.year(t)

            # 1. FACTORS
            F = self.L @ d["factor"][r]
            rec.factors[t] = F
            ns = self._namespace(F)

            # 2. PROPENSITY: Z = Λ F + σ ε ; U = Φ(Z)
            Z = cat.lam @ F + cat.sigma_idio * d["idio"][r]
            U = ndtr(Z)
            rec.propensity_u[t] = U

            # 3. THRESHOLD per causal type (ADR-3) + cascade deltas (ADR-5)
            p_base = np.zeros(E)
            gate = np.ones(E, dtype=bool)
            sustained_now = {}
            for e in range(E):
                ct = int(cat.causal_type[e])
                ens = self._event_ns(ns, e, year)
                if ct == 1:
                    p_base[e] = cat.p_annual[e]
                elif ct == 2:
                    s = cat.type2[e]
                    pressure = float(s.pressure(ens)[0])
                    p_base[e] = s.floor + (1.0 - s.floor) / (1.0 + math.exp(-s.sharpness * (pressure - self.thr[e])))
                else:
                    s = cat.type3[e]
                    ok = all(bool(pre(ens)[0]) for pre in s.preconditions)
                    ok = ok and all(self.counters[e][j] >= yrs for j, (_, yrs) in enumerate(s.sustained))
                    gate[e] = ok
                    p_base[e] = s.window * s.resolution
                    sustained_now[e] = [bool(expr(ens)[0]) for expr, _ in s.sustained]
            delta = np.zeros(E)
            mask = np.zeros(E, dtype=np.int64)
            for cb in self.cascades:
                delta[cb.dst] += cb.delta
                mask[cb.dst] |= 1 << cb.src
            p_eff = p_base + delta
            rec.p_eff[t], rec.gate[t] = p_eff, gate

            # 4. FIRE
            fired = gate & (U < p_eff)

            # 5. RESOLVE + cascade pushes (pending until step 8)
            pending: list[_Cascade] = []
            new_shocks: list[_Shock] = []
            for e in np.flatnonzero(fired):
                tree = cat.resolution_tree[e]
                res = self._draw_code(float(d["res_u"][r, e]), tree.resolution_p)
                br = self._draw_code(float(d["branch_u"][r, e]), tree.branch_p[res])
                self.last_res[e], self.last_branch[e], self.last_fire_year[e] = res, br, year
                self.active[e] = True
                self.active_until[e] = year + int(cat.resolves_after[e]) - 1   # resolves_after counts the firing year
                mags = []
                rows = np.flatnonzero((cat.impact_table["event"] == e) & (cat.impact_table["res_code"] == res)
                                      & (cat.impact_table["branch_code"] == br))
                for row in rows:
                    ir = cat.impact_table[row]
                    M = float(ir["mean"] + ir["std"] * d["impact_z"][r, row])
                    mags.append((int(row), M))
                    new_shocks.append(_Shock(int(row), int(ir["entity_idx"]), int(ir["var_idx"]), M, int(ir["onset_kind"]),
                                             int(ir["onset_years"]), int(ir["dur_kind"]), float(ir["dur_param"]), int(e),
                                             bool(ir["multiplicative"])))
                rec.events.append(EventFiring(year, int(e), res, br, float(p_base[e]), float(p_eff[e]), int(mask[e]), mags))
                ens = self._event_ns(ns, int(e), year)
                for edge in cat.cascade_edges:
                    if edge.src_event == e and (edge.cond is None or bool(edge.cond(ens)[0])):
                        pending.append(_Cascade(int(e), edge.dst_event, edge.delta, edge.years))

            # 6. IMPACTS: age existing shocks and apply increments; then push this year's shocks
            keep: list[_Shock] = []
            for s in self.ledger:
                s.age += 1
                cur = shock_contribution(s, bool(self.active[s.owner_event]))
                self._apply(s, s.prev, cur, year)
                s.prev = cur
                keep.append(s)
                if s.dur_kind == DUR_UNTIL_RESOLVED and not self.active[s.owner_event]:
                    keep.pop()                                   # owner resolved: contribution now 0, slot freed
                elif s.dur_kind == DUR_PERMANENT and s.age >= _onset_end(s.onset_kind, s.onset_years):
                    keep.pop()                                   # fully onset: level shift stays in state, slot freed
                elif s.dur_kind == DUR_DECAY and s.age > _onset_end(s.onset_kind, s.onset_years) \
                        and abs(cur) < P.epsilon_cull * abs(s.M):
                    self._apply(s, cur, 0.0, year)               # epsilon-cull: return to exactly zero, free slot
                    keep.pop()
            self.ledger = keep
            for s in new_shocks:
                cur = shock_contribution(s, True)
                self._apply(s, 0.0, cur, year)
                s.prev = cur
                if s.dur_kind == DUR_PERMANENT and s.onset_kind == ONSET_IMMEDIATE:
                    continue                                     # folded into state at firing; no slot (ADR-6 rule 1)
                if s.M == 0.0:
                    continue                                     # nothing to carry
                self.ledger.append(s)
            if len(self.ledger) > P.max_active:
                raise LedgerOverflow(self.run_index, year, len(self.ledger), P.max_active)
            rec.max_active_seen = max(rec.max_active_seen, len(self.ledger))

            # 7. DYNAMICS (growth-rate-first ordering, mvp-dynamics-scope §5.1 implementation note)
            for v in self.dyn.vars:
                if v.kind == "mean_revert":
                    x = self._get(self._loc[v.key])
                    theta = 1.0 - 0.5 ** (1.0 / v.half_life)   # exact one-year step: README §3 "Dynamics"
                    z = float(d["dyn_z"][r, self.noisy_col[v.key]])
                    self._set(self._loc[v.key], x + theta * (v.mu - x) + v.sigma * z)
            for v in self.dyn.vars:
                if v.kind == "gdp_stock":
                    growth = self._get(self._loc[v.growth_key])
                    self._set(self._loc[v.key], self._get(self._loc[v.key]) * (1.0 + growth / 100.0))
                elif v.kind == "additive":
                    self._set(self._loc[v.key], self._get(self._loc[v.key]) + v.rate)
                elif v.kind == "multiplicative":
                    self._set(self._loc[v.key], self._get(self._loc[v.key]) * (1.0 + v.rate))
                elif v.kind != "mean_revert":
                    raise ValueError(f"unknown dynamics kind {v.kind!r}")

            # 8. MEMORY: sustained counters, cascade buffers, until-resolved flags
            for e, flags in sustained_now.items():
                for j, ok in enumerate(flags):
                    self.counters[e][j] = self.counters[e][j] + 1 if ok else 0
            for cb in self.cascades:
                cb.remaining -= 1
            self.cascades = [cb for cb in self.cascades if cb.remaining > 0] + pending
            for e in np.flatnonzero(self.active):
                if year >= self.active_until[e]:
                    self.active[e] = False

            # 9. RECORD
            rec.country[t + 1], rec.global_[t + 1] = self.c, self.g
        return rec

    def _apply(self, s: _Shock, prev: float, cur: float, year: int) -> None:
        """Move a shock's contribution from ``prev`` to ``cur`` (the increment model, README §3).

        Additive rows: ``state += cur - prev``. Multiplicative rows (fraction of current value):
        ``state *= (1 + cur) / (1 + prev)``, which is ``state *= 1 + cur`` at firing (prev = 0) and returns the
        state to its pre-shock level when the contribution returns to zero. A contribution <= -1 is a hard failure.
        """
        if cur == prev:
            return
        if s.mult:
            if cur <= -1.0:
                raise ImpactOutOfRange(self.run_index, year, s.row, cur)
            factor = (1.0 + cur) / (1.0 + prev)
            if s.entity_idx == ENTITY_GLOBAL:
                self.g[s.var_idx] *= factor
            else:
                self.c[s.entity_idx, s.var_idx] *= factor
            return
        increment = cur - prev
        if s.entity_idx == ENTITY_GLOBAL:
            self.g[s.var_idx] += increment
        else:
            self.c[s.entity_idx, s.var_idx] += increment


def simulate_reference(catalog: CompiledCatalog, ic: InitialConditions, dynamics: DynamicsSpec,
                       params: SimParams, draws, run_indices) -> list[RunRecord]:
    return [ReferenceRun(catalog, ic, dynamics, params, draws, int(r)).run() for r in run_indices]
