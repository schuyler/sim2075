"""Core compile-layer types.

``CompiledCatalog`` is the frozen seam between the compile layer and both
engines (implementation guide §4.1). Field names and shapes follow that
contract; anything beyond it lives under ``meta`` and is informational only.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional

import numpy as np

# ---------------------------------------------------------------------------
# Enumerations shared by the compile layer and both engines. The integer codes
# are part of the impact_table row layout (§4.1) and must not be renumbered.
# ---------------------------------------------------------------------------
ONSET_IMMEDIATE = 0
ONSET_DELAYED = 1
ONSET_GRADUAL = 2

DUR_DECAY = 0           # dur_param = half-life in years
DUR_PERMANENT = 1       # dur_param unused (NaN)
DUR_UNTIL_RESOLVED = 2  # dur_param unused (NaN); lifetime tied to owner event's active flag

ENTITY_GLOBAL = -1      # entity_idx value meaning "global variable"


class CatalogError(ValueError):
    """Any compile-time rejection. The message always names the event ID."""


@dataclass(frozen=True)
class StateCatalog:
    """Entity/variable/factor axes the compiler validates against (guardrail 7)."""
    factors: tuple[str, ...]
    entities: tuple[str, ...]
    entity_kind: dict[str, str]            # id -> country | aggregate_tier1 | aggregate_tier2
    country_vars: tuple[str, ...]
    country_var_derived: dict[str, bool]
    global_vars: tuple[str, ...]

    @property
    def countries(self) -> tuple[str, ...]:
        return tuple(e for e in self.entities if self.entity_kind[e] == "country")


@dataclass
class ExprFn:
    """A compiled expression: ``fn(ns) -> (R,) ndarray`` plus what it reads."""
    source: str
    names: tuple[str, ...]     # namespace keys read (e.g. "F_GPT", "chn.gdp_real", "resolution")
    fn: Callable[[dict], np.ndarray]
    result: str                # "numeric" | "boolean"

    def __call__(self, ns: dict) -> np.ndarray:
        return self.fn(ns)


@dataclass
class Type2Spec:
    pressure: ExprFn
    threshold: float
    threshold_std: float
    sharpness: float
    floor: float


@dataclass
class Type3Spec:
    preconditions: list[ExprFn]                 # all must hold
    sustained: list[tuple[ExprFn, int]]         # (expr, years) — counter >= years
    window: float
    resolution: float


@dataclass
class ResolutionTree:
    """Per-event resolution/branch structure with name -> int code maps.

    Every event gets at least one resolution and one branch per resolution:
    events authored with only ``branches:`` get the implicit resolution
    ``default``; events with neither get ``default.default``.
    """
    resolution_ids: list[str]
    resolution_p: np.ndarray                    # [n_res], sums to 1
    branch_ids: list[list[str]]                 # per resolution
    branch_p: list[np.ndarray]                  # per resolution, each sums to 1
    resolution_code: dict[str, int]
    branch_code: list[dict[str, int]]           # per resolution

    @property
    def n_resolutions(self) -> int:
        return len(self.resolution_ids)


@dataclass
class CascadeEdge:
    src_event: int
    dst_event: int
    delta: float
    years: int
    cond: Optional[ExprFn]                      # evaluated at firing time, ns includes src event state


# impact_table column names, in row-layout order (implementation guide §4.1)
IMPACT_COLUMNS = (
    "event", "res_code", "branch_code", "entity_idx", "var_idx",
    "mean", "std", "onset_kind", "onset_years", "dur_kind", "dur_param",
)
IMPACT_DTYPE = np.dtype([
    ("event", np.int16), ("res_code", np.int16), ("branch_code", np.int16),
    ("entity_idx", np.int16), ("var_idx", np.int16),
    ("mean", np.float64), ("std", np.float64),
    ("onset_kind", np.int8), ("onset_years", np.int8),
    ("dur_kind", np.int8), ("dur_param", np.float64),
])


@dataclass
class CatalogIndex:
    entity: dict[str, int]
    country_var: dict[str, int]
    global_var: dict[str, int]
    factor: dict[str, int]
    event: dict[str, int]


@dataclass
class CompiledCatalog:
    """The compile layer's output; see implementation guide §4.1 for the contract."""
    event_ids: list[str]
    lam: np.ndarray                             # float64 [E, K]
    sigma_idio: np.ndarray                      # float64 [E]
    causal_type: np.ndarray                     # int8 [E]
    p_annual: np.ndarray                        # float64 [E]; NaN for Types 2/3
    type2: dict[int, Type2Spec]
    type3: dict[int, Type3Spec]
    resolution_tree: list[ResolutionTree]       # per event
    impact_table: np.ndarray                    # structured, IMPACT_DTYPE
    cascade_edges: list[CascadeEdge]
    index: CatalogIndex
    omega: np.ndarray                           # float64 [K, K] (validated)
    meta: dict = field(default_factory=dict)    # informational: variance targets, warnings, provenance

    # --- convenience -------------------------------------------------------
    @property
    def n_events(self) -> int:
        return len(self.event_ids)

    @property
    def n_factors(self) -> int:
        return self.lam.shape[1]

    @property
    def n_entities(self) -> int:
        return len(self.index.entity)

    @property
    def n_country_vars(self) -> int:
        return len(self.index.country_var)

    @property
    def n_global_vars(self) -> int:
        return len(self.index.global_var)

    def expression_names(self) -> set[str]:
        """Every namespace key any compiled expression reads."""
        out: set[str] = set()
        for s in self.type2.values():
            out.update(s.pressure.names)
        for s in self.type3.values():
            for e in s.preconditions:
                out.update(e.names)
            for e, _ in s.sustained:
                out.update(e.names)
        for c in self.cascade_edges:
            if c.cond is not None:
                out.update(c.cond.names)
        return out
