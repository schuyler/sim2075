"""Run inputs shared (conceptually) by both engines: initial conditions, dynamics, parameters, recording."""
from __future__ import annotations

from dataclasses import dataclass, field
import math

import numpy as np

from ..catalog.types import ExprFn

# Event-state names (expression-language §3) a scenario flag may not read: flags describe outcomes, not firing
# mechanics (README §3 "Recording"); a flag about firings is an event-log query at E9.
FLAG_EXCLUDED_NAMES = ("resolution", "branch", "years_since")


@dataclass
class InitialConditions:
    """Year-0 state. Axes are sized by the CompiledCatalog's index maps (guardrail 7)."""
    country: np.ndarray     # float64 [N_ent, N_cvar]
    global_: np.ndarray     # float64 [N_gvar]


@dataclass
class VarDynamics:
    """One variable's between-event dynamics (mvp-dynamics-scope §5.1).

    kind:
      "additive"       X += rate                       (slow drift, additive: temperature, LE)
      "multiplicative" X *= 1 + rate                   (slow drift, multiplicative: tech costs)
      "mean_revert"    X += theta*(mu - X) + sigma*z   (Tier 2; theta = 1 - 0.5**(1/half_life), the exact one-year
                                                        discretization, so a sigma = 0 displacement halves every
                                                        half_life years; sigma is the sd of the one-year innovation,
                                                        not of the stationary distribution; z from dyn_z)
      "gdp_stock"      X *= 1 + growth/100             (growth variable named by ``growth_key``, in % per year,
                                                        already updated this year — growth-rate-first ordering)
    key is "global_var" or "entity.var". A mean_revert ``half_life`` must be finite and > 0 and every ``sigma``
    >= 0 (``ValueError`` naming the key).
    """
    key: str
    kind: str
    rate: float = 0.0
    mu: float = 0.0
    half_life: float = 1.0
    sigma: float = 0.0
    growth_key: str = ""

    def __post_init__(self):
        if self.kind == "mean_revert" and not (math.isfinite(self.half_life) and self.half_life > 0):
            raise ValueError(f"dynamics {self.key!r}: mean_revert half_life must be finite and > 0, got {self.half_life!r}")
        if not self.sigma >= 0:
            raise ValueError(f"dynamics {self.key!r}: sigma must be >= 0, got {self.sigma!r}")


@dataclass
class DynamicsSpec:
    """Dynamics entries in declaration order. Keys are unique: entries apply sequentially and a mean_revert key
    maps to its ``dyn_z`` column through a dict, so a repeated key would be order-dependent and silently wrong."""
    vars: list[VarDynamics] = field(default_factory=list)

    def __post_init__(self):
        seen = set()
        for v in self.vars:
            if v.key in seen:
                raise ValueError(f"dynamics {v.key!r}: duplicate key in DynamicsSpec.vars")
            seen.add(v.key)

    @property
    def noisy_keys(self) -> list[str]:
        """Mean-reverting variables in declaration order; one dyn_z column each (even if sigma == 0)."""
        return [v.key for v in self.vars if v.kind == "mean_revert"]


@dataclass
class SimParams:
    """Engine parameters. The ``until: resolved`` window is per event (``CompiledCatalog.resolves_after``), not here."""
    start_year: int = 2025
    years: int = 50
    max_active: int = 256
    epsilon_cull: float = 1e-4
    block_size: int = 1024

    def __post_init__(self):
        if self.years < 1 or self.max_active < 1:
            raise ValueError("years and max_active must be >= 1")


@dataclass
class ScenarioFlag:
    """ADR-9 scenario flag: ``condition`` held for ``min_years`` consecutive years (README §3 "Recording").

    ``condition`` is an expression compiled by the catalog's expression compiler (``sim.catalog.expr``) with its
    names validated against the state catalog; it may read factors and state variables only. Both engines
    evaluate it in step 9 on end-of-year state with that year's factors, keep a per-run consecutive counter
    (+1 while it holds, reset to 0 when it fails) and set the flag, which then stays set, once the counter
    reaches ``min_years``. A condition reading ``resolution``, ``branch`` or ``years_since``, one that is not
    boolean, or ``min_years < 1`` is a ``ValueError`` naming the flag.
    """
    name: str
    condition: ExprFn
    min_years: int

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError(f"scenario flag {self.name!r}: name must be a non-empty string")
        if not isinstance(self.condition, ExprFn):
            raise ValueError(f"scenario flag {self.name!r}: condition must be a compiled ExprFn")
        if self.condition.result != "boolean":
            raise ValueError(f"scenario flag {self.name!r}: condition must be boolean, got {self.condition.result!r}")
        bad = [n for n in self.condition.names if n in FLAG_EXCLUDED_NAMES]
        if bad:
            raise ValueError(f"scenario flag {self.name!r}: condition reads event state {bad}; flags may read factors "
                             f"and state variables only")
        if int(self.min_years) != self.min_years or self.min_years < 1:
            raise ValueError(f"scenario flag {self.name!r}: min_years must be an integer >= 1, got {self.min_years!r}")
        self.min_years = int(self.min_years)


@dataclass
class RecordingSpec:
    """What a run records beyond terminal state, factors and the event log (ADR-9; README §3 "Recording").

    ``scenario_flags``: evaluated for every run. ``thin_keys``: state keys (``"entity.var"`` / ``"global_var"``)
    whose annual values are kept for every run. ``n_full``: the runs with the lowest global indices that keep
    full state trajectories. Defaults to nothing, so fixtures run without it. A duplicate flag name or thin
    key, or ``n_full < 0``, is a ``ValueError`` naming it. The production lists are data loaded at E9
    (README §4, items 20–21).
    """
    scenario_flags: list[ScenarioFlag] = field(default_factory=list)
    thin_keys: list[str] = field(default_factory=list)
    n_full: int = 0

    def __post_init__(self):
        seen: set[str] = set()
        for f in self.scenario_flags:
            if not isinstance(f, ScenarioFlag):
                raise ValueError(f"recording: scenario_flags entries must be ScenarioFlag, got {type(f).__name__}")
            if f.name in seen:
                raise ValueError(f"recording: duplicate scenario flag name {f.name!r}")
            seen.add(f.name)
        seen = set()
        for k in self.thin_keys:
            if not isinstance(k, str) or not k:
                raise ValueError(f"recording: thin keys must be non-empty state keys, got {k!r}")
            if k in seen:
                raise ValueError(f"recording: duplicate thin key {k!r}")
            seen.add(k)
        if int(self.n_full) != self.n_full or self.n_full < 0:
            raise ValueError(f"recording: n_full must be an integer >= 0, got {self.n_full!r}")
        self.n_full = int(self.n_full)

    @property
    def flag_names(self) -> list[str]:
        return [f.name for f in self.scenario_flags]


class LedgerOverflow(RuntimeError):
    """Active-shock ledger exceeded max_active (pinned decision #3: counted hard failure, never a silent drop).

    ``run_index`` is the failing run (``int``) when the reference engine raises, and the list of every failing
    run's global index (``list[int]``) when a vectorized engine raises for a block; ``count`` is then the largest.
    """

    def __init__(self, run_index: int | list[int], year: int, count: int, max_active: int):
        self.run_index, self.year, self.count, self.max_active = run_index, year, count, max_active
        super().__init__(f"ledger overflow in run {run_index}, year {year}: {count} active shocks > max_active={max_active}")


class ImpactOutOfRange(RuntimeError):
    """A multiplicative shock's contribution reached <= -1 (state would go to zero or negative): hard failure, never a clamp.

    ``run_index`` as for ``LedgerOverflow``; with a list, ``row`` and ``contribution`` are those the reference
    would report for the lowest listed run.
    """

    def __init__(self, run_index: int | list[int], year: int, row: int, contribution: float):
        self.run_index, self.year, self.row, self.contribution = run_index, year, row, contribution
        super().__init__(f"multiplicative impact out of range in run {run_index}, year {year}: impact_table row {row} "
                         f"contribution {contribution:.6g} <= -1")
