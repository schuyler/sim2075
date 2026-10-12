"""Scalar reference implementation (ADR-1): the verification oracle and the narrator.

Plain per-run, per-year imperative code that transcribes the year step of
simulator-architecture §3 directly. Shares the compile layer and the RNG
contract (``sim.rng``) with the vectorized engine; shares no engine code.
"""
from .model import InitialConditions, VarDynamics, DynamicsSpec, SimParams, LedgerOverflow
from .engine import ReferenceRun, RunRecord, EventFiring, simulate_reference

__all__ = ["InitialConditions", "VarDynamics", "DynamicsSpec", "SimParams", "LedgerOverflow",
           "ReferenceRun", "RunRecord", "EventFiring", "simulate_reference"]
