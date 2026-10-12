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


def state_catalog_from_dict(raw: dict) -> StateCatalog:
    factors = tuple(raw["factors"])
    entities = tuple(e["id"] for e in raw["entities"])
    kinds = {e["id"]: e["kind"] for e in raw["entities"]}
    cvars = tuple(v["name"] for v in raw["country_variables"])
    derived = {v["name"]: bool(v.get("derived", False)) for v in raw["country_variables"]}
    gvars = tuple(v["name"] for v in raw["global_variables"])
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
    return StateCatalog(factors, entities, kinds, cvars, derived, gvars)
