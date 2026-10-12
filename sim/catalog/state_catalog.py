"""Load the machine-readable state catalog (sim/data/state_catalog.yaml)."""
from __future__ import annotations

from pathlib import Path

import yaml

from .types import CatalogError, StateCatalog

_HERE = Path(__file__).resolve().parent


def default_state_catalog_path() -> Path:
    return _HERE.parent / "data" / "state_catalog.yaml"


def load_state_catalog(path: str | Path | None = None) -> StateCatalog:
    path = Path(path) if path else default_state_catalog_path()
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return state_catalog_from_dict(raw)


def _baseline(name: str, raw) -> float:
    try:
        v = float(raw)
    except (TypeError, ValueError):
        raise CatalogError(f"state catalog: baseline_2025 of {name!r} is not numeric: {raw!r}") from None
    if v != v:
        raise CatalogError(f"state catalog: baseline_2025 of {name!r} is NaN")
    return v


def state_catalog_from_dict(raw: dict) -> StateCatalog:
    factors = tuple(raw["factors"])
    entities = tuple(e["id"] for e in raw["entities"])
    kinds = {e["id"]: e["kind"] for e in raw["entities"]}
    cvars = tuple(v["name"] for v in raw["country_variables"])
    derived = {v["name"]: bool(v.get("derived", False)) for v in raw["country_variables"]}
    gvars = tuple(v["name"] for v in raw["global_variables"])
    baselines: dict[str, float] = {}
    for v in raw["global_variables"]:
        if "baseline_2025" in v:
            baselines[v["name"]] = _baseline(v["name"], v["baseline_2025"])
    for v in raw["country_variables"]:
        if "baseline_2025" in v:
            # country baselines are per entity when the catalog records them: {entity: value}
            b = v["baseline_2025"]
            if not isinstance(b, dict):
                raise CatalogError(f"state catalog: country variable {v['name']!r} baseline_2025 must map entity -> value")
            for ent, val in b.items():
                baselines[f"{ent}.{v['name']}"] = _baseline(f"{ent}.{v['name']}", val)
    for name, seq in (("factors", factors), ("entities", entities),
                      ("country_variables", cvars), ("global_variables", gvars)):
        if len(set(seq)) != len(seq):
            raise CatalogError(f"state catalog: duplicate names in {name}")
    clash = set(gvars) & set(cvars)
    if clash:
        raise CatalogError(f"state catalog: names in both global and country catalogs: {sorted(clash)}")
    clash = set(gvars) & set(factors)
    if clash:
        raise CatalogError(f"state catalog: names in both global catalog and factors: {sorted(clash)}")
    return StateCatalog(factors, entities, kinds, cvars, derived, gvars, baselines)
