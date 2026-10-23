"""Vectorized runtime layer — stages E3–E8 of the implementation guide.

Every module here is diffed against ``sim.reference`` under shared draws
(implementation guide §5.2) before it is considered correct. Built so far:

    factors.py   E3  Ω validation, Cholesky, correlated factor draws, event propensity Z and copula uniforms U
    firing.py    E4  per-type base probabilities and gates (ADR-3), per-run Type 2 thresholds (pinned #1), fire mask
    memory.py    E5  sustained counters, cascade slots (pinned #2/#3), EventState updates, resolution/branch code draw
    impacts.py   E6  active-shock ledger (pinned #2/#3): impact-row selection and magnitudes, shock schedule,
                     epsilon-cull, `until: resolved` event flags

Not yet built: dynamics.py (E7), state.py / simulation.py (E8).
"""
from .factors import FactorModel
from .firing import FiringModel, EventState, namespace_from_state
from .memory import MAX_ACTIVE, MemoryModel, draw_codes
from .impacts import ImpactDraw, ImpactLedger

__all__ = ["FactorModel", "FiringModel", "EventState", "namespace_from_state", "MAX_ACTIVE", "MemoryModel", "draw_codes",
           "ImpactDraw", "ImpactLedger"]
