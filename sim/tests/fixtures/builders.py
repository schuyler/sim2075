"""Small helpers for hand-building CompiledCatalog instances. No compile-layer logic is reused here
beyond the data types, so FIX-A/FIX-B stay independent of the compiler they will later check."""
from __future__ import annotations

import numpy as np

from sim.catalog.types import (CatalogIndex, CompiledCatalog, ExprFn, IMPACT_DTYPE, ResolutionTree,
                               StateCatalog, ENTITY_GLOBAL)


def state_catalog(factors, entities, country_vars, global_vars) -> StateCatalog:
    return StateCatalog(tuple(factors), tuple(entities), {e: "country" for e in entities},
                        tuple(country_vars), {v: False for v in country_vars}, tuple(global_vars))


def index_for(sc: StateCatalog, event_ids) -> CatalogIndex:
    return CatalogIndex(entity={e: i for i, e in enumerate(sc.entities)},
                        country_var={v: i for i, v in enumerate(sc.country_vars)},
                        global_var={v: i for i, v in enumerate(sc.global_vars)},
                        factor={f: i for i, f in enumerate(sc.factors)},
                        event={e: i for i, e in enumerate(event_ids)})


def tree(resolutions: list[tuple[str, float, list[tuple[str, float]]]]) -> ResolutionTree:
    """[(res_id, p, [(branch_id, p), ...]), ...]"""
    res_ids = [r for r, _, _ in resolutions]
    res_p = np.array([p for _, p, _ in resolutions])
    b_ids = [[b for b, _ in bl] for _, _, bl in resolutions]
    b_p = [np.array([p for _, p in bl]) for _, _, bl in resolutions]
    return ResolutionTree(res_ids, res_p, b_ids, b_p, {r: i for i, r in enumerate(res_ids)},
                          [{b: i for i, b in enumerate(bl)} for bl in b_ids])


def default_tree() -> ResolutionTree:
    return tree([("default", 1.0, [("default", 1.0)])])


def impact_rows(rows) -> np.ndarray:
    """rows: (event, res, branch, entity_idx|-1, var_idx, mean, std, onset_kind, onset_years, dur_kind, dur_param)"""
    return np.array(rows, dtype=IMPACT_DTYPE)


def expr(names, fn, result) -> ExprFn:
    """Wrap a plain lambda over the namespace dict as an ExprFn (hand-written, not compiled)."""
    return ExprFn(source="<hand-built>", names=tuple(names),
                  fn=lambda ns: np.broadcast_to(np.asarray(fn(ns), dtype=(bool if result == "boolean" else np.float64)), ns["_shape"]),
                  result=result)


def sigma_from(lam: np.ndarray, omega: np.ndarray) -> np.ndarray:
    return np.sqrt(1.0 - np.einsum("ik,kl,il->i", lam, omega, lam))


GLOBAL = ENTITY_GLOBAL
