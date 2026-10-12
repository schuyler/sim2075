"""E3 — factor sampling (ADR-2) and event propensity (ADR-3's copula half), vectorized over runs.

Transcribes the reference engine's steps 1–2 for a whole block of runs at once:

    F = z @ Lᵀ                      correlated standard-normal factors, Ω = L Lᵀ
    Z = F @ Λᵀ + σ_idio · ε         event propensity; Var(Zᵢ) = (ΛΩΛᵀ)ᵢᵢ + σ²_idio,i = 1
    U = Φ(Z)                        correlated uniforms, the only cross-event correlation in the model

All axis sizes come from the ``CompiledCatalog`` (guardrail 7). The draw arrays are the ``factor`` and
``idio`` entries of the §4.6 year block, consumed whole; nothing here depends on outcomes.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.special import ndtr

from ..catalog.omega import validate_omega
from ..catalog.types import CompiledCatalog


@dataclass(frozen=True)
class FactorModel:
    omega: np.ndarray        # float64 [K, K], validated correlation matrix
    L: np.ndarray            # float64 [K, K], lower Cholesky factor
    lam: np.ndarray          # float64 [E, K]
    sigma_idio: np.ndarray   # float64 [E]

    @classmethod
    def from_catalog(cls, catalog: CompiledCatalog, tol: float = 1e-12) -> "FactorModel":
        omega = validate_omega(catalog.omega, list(catalog.index.factor))
        lam = np.asarray(catalog.lam, dtype=np.float64)
        E, K = lam.shape
        if omega.shape != (K, K):
            raise ValueError(f"Ω shape {omega.shape} does not match {K} factors in lam")
        if catalog.sigma_idio.shape != (E,):
            raise ValueError(f"sigma_idio shape {catalog.sigma_idio.shape} does not match {E} events")
        explained = np.einsum("ik,kl,il->i", lam, omega, lam)
        if (explained > 1.0 + tol).any():
            raise ValueError("factor-explained variance exceeds 1 for events " + str(np.flatnonzero(explained > 1.0 + tol).tolist()))
        sigma = np.sqrt(np.maximum(1.0 - explained, 0.0))
        if not np.allclose(sigma, catalog.sigma_idio, rtol=0, atol=1e-9):
            raise ValueError("catalog sigma_idio is not sqrt(1 - (ΛΩΛᵀ)ᵢᵢ) for its own Ω and loadings")
        L = np.linalg.cholesky(omega)   # raises LinAlgError if Ω is not positive definite — never patched
        return cls(omega=omega, L=L, lam=lam, sigma_idio=np.asarray(catalog.sigma_idio, dtype=np.float64))

    @property
    def K(self) -> int:
        return self.L.shape[0]

    @property
    def E(self) -> int:
        return self.lam.shape[0]

    def factors(self, z: np.ndarray) -> np.ndarray:
        """``z`` float64 [R, K] standard normals (the ``factor`` draw) -> correlated factors F [R, K]."""
        z = np.asarray(z, dtype=np.float64)
        if z.ndim != 2 or z.shape[1] != self.K:
            raise ValueError(f"factor draws must be [R, {self.K}], got {z.shape}")
        return z @ self.L.T

    def propensity(self, F: np.ndarray, idio: np.ndarray) -> np.ndarray:
        """``F`` [R, K], ``idio`` [R, E] standard normals (the ``idio`` draw) -> Z [R, E]."""
        F = np.asarray(F, dtype=np.float64)
        idio = np.asarray(idio, dtype=np.float64)
        if F.ndim != 2 or F.shape[1] != self.K:
            raise ValueError(f"F must be [R, {self.K}], got {F.shape}")
        if idio.shape != (F.shape[0], self.E):
            raise ValueError(f"idio draws must be [R, {self.E}], got {idio.shape}")
        return F @ self.lam.T + self.sigma_idio * idio

    @staticmethod
    def uniforms(Z: np.ndarray) -> np.ndarray:
        """Correlated uniforms U = Φ(Z), [R, E]."""
        return ndtr(np.asarray(Z, dtype=np.float64))

    def year(self, draws: dict) -> tuple[np.ndarray, np.ndarray]:
        """One year's draws (``factor``, ``idio`` keys of a §4.6 block) -> (F [R, K], U [R, E])."""
        F = self.factors(draws["factor"])
        return F, self.uniforms(self.propensity(F, draws["idio"]))
