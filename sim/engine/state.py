"""E8 — the block state tensor (guide §4.2) and state-key binding for the year loop.

``StateTensor`` holds one block's ``country`` float64 [R, N_ent, N_cvar] and ``global_`` float64 [R, N_gvar],
sized by the ``CompiledCatalog`` index maps (guardrail 7) and initialised by broadcasting the
``InitialConditions`` over the run axis. Every module of the year step mutates these arrays in place
(``ImpactLedger.apply``, ``DynamicsModel.step``); the recorder reads them after step 8.

``resolve_key`` maps a state key (``"entity.var"`` or ``"global_var"``, the ``DynamicsSpec`` / ``RecordingSpec``
convention) to a location, and ``bind_names`` builds an expression namespace (guide §4.3: every name an
``(R,)`` view) from this year's factors and the *current* state. The year loop uses it for scenario flags in
step 9, built afresh from end-of-year state rather than reusing step 2's namespace (README §3 "Recording").
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..catalog.types import CompiledCatalog
from ..reference.model import InitialConditions


def resolve_key(catalog: CompiledCatalog, key: str) -> tuple:
    """``("c", entity, var)`` for ``"entity.var"``, ``("g", var)`` for a global; ``KeyError`` otherwise."""
    idx = catalog.index
    if "." in key:
        ent, var = key.split(".", 1)
        if ent not in idx.entity or var not in idx.country_var:
            raise KeyError(f"unknown state key {key!r}")
        return ("c", idx.entity[ent], idx.country_var[var])
    if key in idx.global_var:
        return ("g", idx.global_var[key])
    raise KeyError(f"unknown state key {key!r}")


@dataclass
class StateTensor:
    country: np.ndarray    # float64 [R, N_ent, N_cvar]
    global_: np.ndarray    # float64 [R, N_gvar]

    @classmethod
    def from_initial_conditions(cls, catalog: CompiledCatalog, ic: InitialConditions, R: int) -> "StateTensor":
        """Year-0 state for a block of ``R`` runs: the initial conditions broadcast over the run axis, copied."""
        idx = catalog.index
        n_ent, n_cvar, n_gvar = len(idx.entity), len(idx.country_var), len(idx.global_var)
        country = np.asarray(ic.country, dtype=np.float64)
        global_ = np.asarray(ic.global_, dtype=np.float64)
        if country.shape != (n_ent, n_cvar) or global_.shape != (n_gvar,):
            raise ValueError(f"initial conditions {country.shape}, {global_.shape} do not match catalog axes "
                             f"({n_ent}, {n_cvar}), ({n_gvar},)")
        R = int(R)
        if R < 1:
            raise ValueError("R must be >= 1")
        return cls(np.array(np.broadcast_to(country, (R, n_ent, n_cvar)), dtype=np.float64),
                   np.array(np.broadcast_to(global_, (R, n_gvar)), dtype=np.float64))

    @property
    def R(self) -> int:
        return self.country.shape[0]

    def view(self, loc: tuple) -> np.ndarray:
        """The ``(R,)`` view of a resolved state key (writes reach the tensor)."""
        return self.country[:, loc[1], loc[2]] if loc[0] == "c" else self.global_[:, loc[1]]


def bind_names(catalog: CompiledCatalog, names, F: np.ndarray, state: StateTensor) -> dict:
    """Namespace binding each name in ``names`` to an ``(R,)`` view: factor IDs to columns of ``F`` [R, K],
    state keys to the current state. Event-state names are not bound (``KeyError``)."""
    R = state.R
    if F.shape[0] != R:
        raise ValueError("state tensor and factor draws disagree on R")
    idx = catalog.index
    ns: dict = {"_shape": (R,)}
    for name in names:
        ns[name] = F[:, idx.factor[name]] if name in idx.factor else state.view(resolve_key(catalog, name))
    return ns
