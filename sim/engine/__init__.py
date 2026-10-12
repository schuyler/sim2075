"""Vectorized runtime layer — stages E3–E8 of the implementation guide.

Every module here is diffed against ``sim.reference`` under shared draws
(implementation guide §5.2) before it is considered correct. Built so far:

    factors.py   E3  Ω validation, Cholesky, correlated factor draws, event propensity Z and copula uniforms U
    firing.py    E4  per-type base probabilities and gates (ADR-3), per-run Type 2 thresholds (pinned #1), fire mask

Not yet built: memory.py (E5), impacts.py (E6), dynamics.py (E7), state.py / simulation.py (E8).
"""
from .factors import FactorModel
from .firing import FiringModel, EventState, namespace_from_state

__all__ = ["FactorModel", "FiringModel", "EventState", "namespace_from_state"]
