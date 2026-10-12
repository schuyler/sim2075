"""Run inputs shared (conceptually) by both engines: initial conditions, dynamics, parameters."""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


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
      "mean_revert"    X += theta*(mu - X) + sigma*z   (Tier 2; theta = ln2/half_life; z from dyn_z)
      "gdp_stock"      X *= 1 + growth/100             (growth variable named by ``growth_key``, in % per year,
                                                        already updated this year — growth-rate-first ordering)
    key is "global_var" or "entity.var".
    """
    key: str
    kind: str
    rate: float = 0.0
    mu: float = 0.0
    half_life: float = 1.0
    sigma: float = 0.0
    growth_key: str = ""


@dataclass
class DynamicsSpec:
    vars: list[VarDynamics] = field(default_factory=list)

    @property
    def noisy_keys(self) -> list[str]:
        """Mean-reverting variables in declaration order; one dyn_z column each (even if sigma == 0)."""
        return [v.key for v in self.vars if v.kind == "mean_revert"]


@dataclass
class SimParams:
    """Engine parameters. ``until_resolved_years`` has no default on purpose — see sim/README.md (open question)."""
    until_resolved_years: int
    start_year: int = 2025
    years: int = 50
    max_active: int = 256
    epsilon_cull: float = 1e-4
    block_size: int = 1024

    def __post_init__(self):
        if self.until_resolved_years < 1:
            raise ValueError("until_resolved_years must be >= 1")
        if self.years < 1 or self.max_active < 1:
            raise ValueError("years and max_active must be >= 1")


class LedgerOverflow(RuntimeError):
    """Active-shock ledger exceeded max_active (pinned decision #3: counted hard failure, never a silent drop)."""

    def __init__(self, run_index: int, year: int, count: int, max_active: int):
        self.run_index, self.year, self.count, self.max_active = run_index, year, count, max_active
        super().__init__(f"ledger overflow in run {run_index}, year {year}: {count} active shocks > max_active={max_active}")
