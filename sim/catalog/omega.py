"""Load and validate the inter-factor correlation matrix Ω (ADR-2)."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import yaml

from .types import CatalogError

_HERE = Path(__file__).resolve().parent


def default_omega_path() -> Path:
    return _HERE.parent / "data" / "omega.yaml"


def validate_omega(omega: np.ndarray, factors: tuple[str, ...] | list[str], tol: float = 1e-10) -> np.ndarray:
    """Hard-fail on anything that is not a valid correlation matrix over ``factors``."""
    omega = np.asarray(omega, dtype=np.float64)
    k = len(factors)
    if omega.shape != (k, k):
        raise CatalogError(f"Ω: expected shape {(k, k)} for {k} factors, got {omega.shape}")
    if not np.allclose(omega, omega.T, atol=tol):
        raise CatalogError("Ω: not symmetric")
    if not np.allclose(np.diag(omega), 1.0, atol=tol):
        raise CatalogError("Ω: diagonal not all 1")
    eig = np.linalg.eigvalsh(omega)
    if eig.min() < -tol:
        raise CatalogError(f"Ω: not positive semi-definite (min eigenvalue {eig.min():.4g})")
    return omega


def load_omega(path: str | Path | None = None, factors: tuple[str, ...] | None = None) -> tuple[list[str], np.ndarray]:
    """Return (factor_ids, Ω). If ``factors`` is given, the file's order must match it."""
    path = Path(path) if path else default_omega_path()
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    ids = list(raw["factors"])
    omega = validate_omega(np.array(raw["matrix"], dtype=np.float64), ids)
    if factors is not None and tuple(ids) != tuple(factors):
        raise CatalogError(f"Ω factor order {ids} does not match state catalog {list(factors)}")
    return ids, omega
