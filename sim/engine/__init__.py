"""Vectorized runtime layer — stages E3–E8 of the implementation guide.

Every module here is diffed against ``sim.reference`` under shared draws
(implementation guide §5.2) before it is considered correct. Built so far:

    factors.py   E3  Ω validation, Cholesky, correlated factor draws, event propensity Z and copula uniforms U
    firing.py    E4  per-type base probabilities and gates (ADR-3), per-run Type 2 thresholds (pinned #1), fire mask
    memory.py    E5  sustained counters, cascade slots (pinned #2/#3), EventState updates, resolution/branch code draw
    impacts.py   E6  active-shock ledger (pinned #2/#3): impact-row selection and magnitudes, shock schedule,
                     epsilon-cull, `until: resolved` event flags
    dynamics.py  E7  step 7: Tier 2 mean reversion, then gdp_stock compounding and Tier 1 drifts (growth-rate-first)
    state.py     E8  block state tensor (guide §4.2), state-key resolution and name binding
    simulation.py E8 `simulate`: the year loop wiring E3–E7 in step order over §4.6 blocks; recording per ADR-9
                     (`RunOutputs`: terminal state, factors, columnar event log with provenance, thin and full
                     trajectories, scenario flags, max_active_seen)

Not yet built: oil/food → inflation transmission (E7b, after D4); analysis and serialization (E9).
"""
from .factors import FactorModel
from .firing import FiringModel, EventState, namespace_from_state
from .memory import MAX_ACTIVE, MemoryModel, draw_codes
from .impacts import ImpactDraw, ImpactLedger
from .dynamics import DynamicsModel
from .state import StateTensor, bind_names, resolve_key
from .simulation import EventLog, RunOutputs, simulate

__all__ = ["FactorModel", "FiringModel", "EventState", "namespace_from_state", "MAX_ACTIVE", "MemoryModel", "draw_codes",
           "ImpactDraw", "ImpactLedger", "DynamicsModel", "StateTensor", "bind_names", "resolve_key",
           "EventLog", "RunOutputs", "simulate"]
