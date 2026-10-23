"""E7 — between-event dynamics (mvp-dynamics-scope §5.1), vectorized over runs.

Transcribes the reference engine's step 7 for a block of runs, in two phases over the ``DynamicsSpec``
entries in declaration order (growth-rate-first ordering, README §3 "Dynamics"):

    phase 1   every ``mean_revert`` entry:  x ← x + θ(μ − x) + σ · dyn_z[:, col],  θ = 1 − 0.5^(1/half_life),
              ``col`` the entry's position in ``DynamicsSpec.noisy_keys`` (drawn every year, even when σ = 0)
    phase 2   ``gdp_stock``:       x ← x · (1 + g/100), g its ``growth_key`` value after phase 1 (% per year)
              ``additive``:        x ← x + rate
              ``multiplicative``:  x ← x · (1 + rate)

Phase 2 keeps declaration order across kinds (a ``gdp_stock`` whose growth variable is itself a phase-2 drift
target reads it before or after the drift as declared). Each entry is one ``(R,)`` operation on a view of the
caller's state, element for element the reference's scalar arithmetic. No clamping: a stock compounded by
growth ≤ −100 falls where the arithmetic puts it. The oil/food → inflation transmission of §5.1 step 6 is
stage E7b (README §4, item 19), not built here.
"""
from __future__ import annotations

import numpy as np

from ..catalog.types import CompiledCatalog
from ..reference.model import DynamicsSpec

KINDS = ("mean_revert", "gdp_stock", "additive", "multiplicative")


class DynamicsModel:
    """Step 7 for a block of runs; every key is resolved once, here."""

    def __init__(self, catalog: CompiledCatalog, dynamics: DynamicsSpec):
        self.cat = catalog
        idx = catalog.index
        self.n_ent, self.n_cvar, self.n_gvar = len(idx.entity), len(idx.country_var), len(idx.global_var)
        self.noisy_keys = list(dynamics.noisy_keys)
        col = {k: i for i, k in enumerate(self.noisy_keys)}
        self.mean_revert: list[tuple[tuple, float, float, float, int]] = []   # (loc, θ, μ, σ, dyn_z column)
        self.phase2: list[tuple[str, tuple, float, tuple | None]] = []      # (kind, loc, rate, growth loc)
        for v in dynamics.vars:
            if v.kind not in KINDS:
                raise ValueError(f"dynamics {v.key!r}: unknown dynamics kind {v.kind!r}")
            loc = self._resolve(v.key)
            if v.kind == "mean_revert":
                theta = 1.0 - 0.5 ** (1.0 / v.half_life)
                self.mean_revert.append((loc, theta, float(v.mu), float(v.sigma), col[v.key]))
            elif v.kind == "gdp_stock":
                self.phase2.append((v.kind, loc, 0.0, self._resolve(v.growth_key)))
            else:
                self.phase2.append((v.kind, loc, float(v.rate), None))

    def _resolve(self, key: str) -> tuple:
        """``("c", entity, var)`` for ``"entity.var"``, ``("g", var)`` for a global; ``KeyError`` otherwise."""
        idx = self.cat.index
        if "." in key:
            ent, var = key.split(".", 1)
            if ent not in idx.entity or var not in idx.country_var:
                raise KeyError(f"unknown state key {key!r}")
            return ("c", idx.entity[ent], idx.country_var[var])
        if key in idx.global_var:
            return ("g", idx.global_var[key])
        raise KeyError(f"unknown state key {key!r}")

    @staticmethod
    def _view(country: np.ndarray, global_: np.ndarray, loc: tuple) -> np.ndarray:
        return country[:, loc[1], loc[2]] if loc[0] == "c" else global_[:, loc[1]]

    def step(self, country: np.ndarray, global_: np.ndarray, dyn_z: np.ndarray) -> None:
        """Apply step 7 to ``country`` float64 [R, N_ent, N_cvar] and ``global_`` float64 [R, N_gvar] in place.

        ``dyn_z`` is this year's [R, len(noisy_keys)] draw block.
        """
        R = country.shape[0]
        if country.dtype != np.float64 or country.shape != (R, self.n_ent, self.n_cvar):
            raise ValueError(f"country must be float64 [R, {self.n_ent}, {self.n_cvar}], got {country.dtype} {country.shape}")
        if global_.dtype != np.float64 or global_.shape != (R, self.n_gvar):
            raise ValueError(f"global_ must be float64 [{R}, {self.n_gvar}], got {global_.dtype} {global_.shape}")
        dyn_z = np.asarray(dyn_z, dtype=np.float64)
        if dyn_z.shape != (R, len(self.noisy_keys)):
            raise ValueError(f"dyn_z must be [{R}, {len(self.noisy_keys)}] (one column per noisy key), got {dyn_z.shape}")

        for loc, theta, mu, sigma, c in self.mean_revert:                     # phase 1
            x = self._view(country, global_, loc)
            x[...] = x + theta * (mu - x) + sigma * dyn_z[:, c]
        for kind, loc, rate, gloc in self.phase2:                              # phase 2, declaration order
            x = self._view(country, global_, loc)
            if kind == "gdp_stock":
                x[...] = x * (1.0 + self._view(country, global_, gloc) / 100.0)
            elif kind == "additive":
                x[...] = x + rate
            else:
                x[...] = x * (1.0 + rate)
