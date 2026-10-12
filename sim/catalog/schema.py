"""Structural validation of one event record against methodology/reference/event-yaml-schema.md.

This module checks shape, enums, and probability sums — the parts of the schema
that need no state catalog. Reference resolution (variables, entities, factors,
cascade targets, expressions) happens in ``compile.py``.
"""
from __future__ import annotations

import math
import re

from .types import (CatalogError, DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED,
                    ONSET_DELAYED, ONSET_GRADUAL, ONSET_IMMEDIATE)

ENUMS = {
    "domain": {"political", "economic", "environmental", "health", "technological"},
    "scale": {"global", "regional", "national"},
    "onset": {"sudden", "gradual"},
    "reversibility": {"reversible", "partial", "irreversible"},
}
CONFIDENCE = {"low", "medium", "high"}
P_TOL = 1e-6
_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")
_LOWER_ID = re.compile(r"^[a-z][a-z0-9_]*$")


def _num(x, event: str, what: str, lo: float | None = None, hi: float | None = None) -> float:
    if isinstance(x, bool) or not isinstance(x, (int, float)) or (isinstance(x, float) and math.isnan(x)):
        raise CatalogError(f"{event}: {what} must be a number, got {x!r}")
    if lo is not None and x < lo:
        raise CatalogError(f"{event}: {what} must be >= {lo}, got {x}")
    if hi is not None and x > hi:
        raise CatalogError(f"{event}: {what} must be <= {hi}, got {x}")
    return float(x)


def validate_header(rec: dict) -> str:
    event = rec.get("id")
    if not isinstance(event, str) or not _ID.match(event):
        raise CatalogError(f"{rec.get('_source', '?')}: id {event!r} is not SCREAMING_SNAKE_CASE")
    for key, allowed in ENUMS.items():
        if key not in rec:
            raise CatalogError(f"{event}: missing required field {key!r}")
        if rec[key] not in allowed:
            raise CatalogError(f"{event}: {key} must be one of {sorted(allowed)}, got {rec[key]!r}")
    ct = rec.get("causal_type")
    if ct not in (1, 2, 3) or isinstance(ct, bool):
        raise CatalogError(f"{event}: causal_type must be 1, 2, or 3, got {ct!r}")
    return event


def validate_probability(rec: dict, event: str) -> dict:
    p = rec.get("probability")
    if not isinstance(p, dict):
        raise CatalogError(f"{event}: missing probability block")
    ct = rec["causal_type"]
    if "confidence" in p and p["confidence"] not in CONFIDENCE:
        raise CatalogError(f"{event}: probability.confidence must be one of {sorted(CONFIDENCE)}, got {p['confidence']!r}")
    if "range" in p:
        r = p["range"]
        if not (isinstance(r, list) and len(r) == 2):
            raise CatalogError(f"{event}: probability.range must be [low, high]")
        lo, hi = (_num(v, event, "probability.range", 0.0, 1.0) for v in r)
        if lo > hi:
            raise CatalogError(f"{event}: probability.range low > high")
    if ct == 1:
        if "annual" not in p:
            raise CatalogError(f"{event}: Type 1 probability needs 'annual'")
        _num(p["annual"], event, "probability.annual", 0.0, 1.0)
    elif ct == 2:
        for k in ("pressure", "threshold", "threshold_std", "sharpness", "floor"):
            if k not in p:
                raise CatalogError(f"{event}: Type 2 probability needs {k!r}")
        _num(p["threshold"], event, "probability.threshold")
        _num(p["threshold_std"], event, "probability.threshold_std", 0.0)
        _num(p["sharpness"], event, "probability.sharpness", 0.0)
        _num(p["floor"], event, "probability.floor", 0.0, 1.0)
    else:
        for k in ("window", "resolution", "preconditions"):
            if k not in p:
                raise CatalogError(f"{event}: Type 3 probability needs {k!r}")
        _num(p["window"], event, "probability.window", 0.0, 1.0)
        _num(p["resolution"], event, "probability.resolution", 0.0, 1.0)
        pre = p["preconditions"]
        if not isinstance(pre, dict) or not (pre.get("all") or pre.get("sustained")):
            raise CatalogError(f"{event}: Type 3 preconditions need 'all' and/or 'sustained' lists")
        for s in pre.get("sustained") or []:
            if not isinstance(s, dict) or "expr" not in s or "years" not in s:
                raise CatalogError(f"{event}: each sustained precondition needs 'expr' and 'years'")
            y = s["years"]
            if isinstance(y, bool) or not isinstance(y, int) or y < 1:
                raise CatalogError(f"{event}: sustained.years must be an integer >= 1, got {y!r}")
    return p


def validate_factors(rec: dict, event: str) -> tuple[dict[str, float], float]:
    f = rec.get("factors")
    if not isinstance(f, dict) or not f:
        raise CatalogError(f"{event}: missing or empty factors block")
    if "variance" not in rec:
        raise CatalogError(f"{event}: missing 'variance' (declared factor-explained variance target)")
    loadings = {k: _num(v, event, f"factors.{k}", -1.0, 1.0) for k, v in f.items()}
    return loadings, _num(rec["variance"], event, "variance", 0.0, 1.0)


def _check_psum(ps: list[float], event: str, what: str) -> None:
    if abs(sum(ps) - 1.0) > P_TOL:
        raise CatalogError(f"{event}: {what} probabilities sum to {sum(ps):.6f}, not 1.0")


def validate_resolution_tree(rec: dict, event: str) -> tuple[list[str], list[float], list[list[str]], list[list[float]]]:
    """Normalize resolutions/branches to (res_ids, res_p, branch_ids, branch_p); implicit 'default' as needed."""
    if "resolutions" in rec and "branches" in rec:
        raise CatalogError(f"{event}: use either 'resolutions' or 'branches', not both")

    def branches_of(lst, where) -> tuple[list[str], list[float]]:
        if not isinstance(lst, list) or not lst:
            raise CatalogError(f"{event}: {where} must be a non-empty list")
        ids, ps = [], []
        for b in lst:
            if not isinstance(b, dict) or "id" not in b or "p" not in b:
                raise CatalogError(f"{event}: each entry of {where} needs 'id' and 'p'")
            if not _LOWER_ID.match(str(b["id"])):
                raise CatalogError(f"{event}: {where} id {b['id']!r} must be lower_snake_case")
            if b["id"] in ids:
                raise CatalogError(f"{event}: duplicate id {b['id']!r} in {where}")
            ids.append(b["id"]); ps.append(_num(b["p"], event, f"{where}.{b['id']}.p", 0.0, 1.0))
        _check_psum(ps, event, where)
        return ids, ps

    if "resolutions" in rec:
        res_ids, res_p, b_ids, b_p = [], [], [], []
        for r in (rec["resolutions"] if isinstance(rec["resolutions"], list) else []):
            if not isinstance(r, dict) or "id" not in r or "p" not in r:
                raise CatalogError(f"{event}: each resolution needs 'id' and 'p'")
            if not _LOWER_ID.match(str(r["id"])):
                raise CatalogError(f"{event}: resolution id {r['id']!r} must be lower_snake_case")
            if r["id"] in res_ids:
                raise CatalogError(f"{event}: duplicate resolution id {r['id']!r}")
            res_ids.append(r["id"]); res_p.append(_num(r["p"], event, f"resolutions.{r['id']}.p", 0.0, 1.0))
            if "branches" in r:
                ids, ps = branches_of(r["branches"], f"resolutions.{r['id']}.branches")
            else:
                ids, ps = ["default"], [1.0]
            b_ids.append(ids); b_p.append(ps)
        if not res_ids:
            raise CatalogError(f"{event}: resolutions must be a non-empty list")
        _check_psum(res_p, event, "resolutions")
        return res_ids, res_p, b_ids, b_p
    if "branches" in rec:
        ids, ps = branches_of(rec["branches"], "branches")
        return ["default"], [1.0], [ids], [ps]
    return ["default"], [1.0], [["default"]], [[1.0]]


def parse_onset(x, event: str, where: str) -> tuple[int, int]:
    if x == "immediate":
        return ONSET_IMMEDIATE, 0
    if isinstance(x, dict) and len(x) == 1:
        (k, v), = x.items()
        if k in ("delayed", "gradual"):
            if isinstance(v, bool) or not isinstance(v, int) or v < 1:
                raise CatalogError(f"{event}: {where} onset {k} must be an integer >= 1, got {v!r}")
            return (ONSET_DELAYED if k == "delayed" else ONSET_GRADUAL), v
    raise CatalogError(f"{event}: {where} onset must be 'immediate', {{delayed: N}} or {{gradual: N}}, got {x!r}")


def parse_durability(row: dict, event: str, where: str) -> tuple[int, float]:
    """Exactly one durability form per impact row. v0.1 implements decay / permanent / until: resolved."""
    forms = [k for k in ("decay", "permanent", "until", "durability") if k in row]
    if len(forms) != 1:
        raise CatalogError(f"{event}: {where} must carry exactly one durability form (decay | permanent | until | durability), has {forms}")
    k = forms[0]
    if k == "decay":
        return DUR_DECAY, _num(row["decay"], event, f"{where} decay (half-life)", 1e-9)
    if k == "permanent":
        if row["permanent"] is not True:
            raise CatalogError(f"{event}: {where} 'permanent' must be true")
        return DUR_PERMANENT, math.nan
    if k == "until":
        if row["until"] == "resolved":
            return DUR_UNTIL_RESOLVED, math.nan
        raise CatalogError(f"{event}: {where} durability 'until: {row['until']}' is not implemented in the v0.1 engine (schema v0.2 backlog)")
    d = row["durability"]
    if isinstance(d, dict) and d.get("type") == "decaying" and "floor" not in d and "half_life" in d:
        return DUR_DECAY, _num(d["half_life"], event, f"{where} durability.half_life", 1e-9)
    raise CatalogError(f"{event}: {where} full-form durability {d!r} is not implemented in the v0.1 engine (only {{type: decaying, half_life: N}}; decay-to-floor and maintenance are schema v0.2 backlog)")


def validate_impact_row(row, event: str, where: str) -> dict:
    if not isinstance(row, dict) or "var" not in row or "mag" not in row or "onset" not in row:
        raise CatalogError(f"{event}: {where} impact rows need var, mag, onset and a durability")
    mag = row["mag"]
    if not (isinstance(mag, list) and len(mag) == 2):
        raise CatalogError(f"{event}: {where} mag must be [mean, std]")
    mean = _num(mag[0], event, f"{where} mag mean")
    std = _num(mag[1], event, f"{where} mag std", 0.0)
    onset_kind, onset_years = parse_onset(row["onset"], event, where)
    dur_kind, dur_param = parse_durability(row, event, where)
    extra = set(row) - {"var", "mag", "onset", "decay", "permanent", "until", "durability"}
    if extra:
        raise CatalogError(f"{event}: {where} has unknown impact fields {sorted(extra)}")
    return dict(var=str(row["var"]), mean=mean, std=std, onset_kind=onset_kind,
                onset_years=onset_years, dur_kind=dur_kind, dur_param=dur_param)


def validate_impacts(rec: dict, event: str, res_ids: list[str], b_ids: list[list[str]]) -> dict[tuple[int, int], list[dict]]:
    """Resolve impact keys to (res_code, branch_code) and expand inherit/scale. Wildcards stay as '*.var' here."""
    imp = rec.get("impacts")
    if not isinstance(imp, dict) or not imp:
        raise CatalogError(f"{event}: missing or empty impacts block")
    codes: dict[str, tuple[int, int]] = {}
    for ri, rid in enumerate(res_ids):
        for bi, bid in enumerate(b_ids[ri]):
            if rid == "default":
                codes[bid] = (ri, bi)
                codes[f"default.{bid}"] = (ri, bi)
            else:
                codes[f"{rid}.{bid}"] = (ri, bi)
    for k in imp:
        if k not in codes:
            raise CatalogError(f"{event}: impacts key {k!r} does not name a declared resolution.branch (declared: {sorted(codes)})")
    # direct lists first, then inheritance (single-level; inherit from another inheriting key is an error)
    out: dict[tuple[int, int], list[dict]] = {}
    for k, v in imp.items():
        if isinstance(v, list):
            out[codes[k]] = [validate_impact_row(r, event, f"impacts.{k}") for r in v]
    for k, v in imp.items():
        if isinstance(v, dict):
            if set(v) != {"inherit", "scale"}:
                raise CatalogError(f"{event}: impacts.{k} inheritance must have exactly 'inherit' and 'scale'")
            src = v["inherit"]
            if src not in imp or not isinstance(imp[src], list):
                raise CatalogError(f"{event}: impacts.{k} inherits from {src!r}, which is not a directly specified impact list")
            scale = _num(v["scale"], event, f"impacts.{k}.scale")
            out[codes[k]] = [dict(r, mean=r["mean"] * scale, std=r["std"] * scale) for r in out[codes[src]]]
        elif not isinstance(v, list):
            raise CatalogError(f"{event}: impacts.{k} must be a list of rows or an inherit/scale mapping")
    missing = [k for k, c in codes.items() if c not in out and not k.startswith("default.")]
    if missing:
        raise CatalogError(f"{event}: no impacts specified for declared outcome(s) {sorted(set(missing))}")
    return out


def validate_cascades(rec: dict, event: str) -> list[dict]:
    """Return the outgoing ('triggers') edges. 'triggered_by' is informational and only checked for shape."""
    c = rec.get("cascades")
    if c is None:
        return []
    if not isinstance(c, dict):
        raise CatalogError(f"{event}: cascades must be a mapping")
    trig = c.get("triggers") or []
    for t in c.get("triggered_by") or []:
        if not isinstance(t, dict) or "event" not in t:
            raise CatalogError(f"{event}: cascades.triggered_by entries need 'event'")
    out = []
    for t in trig:
        if not isinstance(t, dict) or "event" not in t or "delta" not in t or "years" not in t:
            raise CatalogError(f"{event}: cascades.triggers entries need event, delta, years")
        y = t["years"]
        if isinstance(y, bool) or not isinstance(y, int) or y < 1:
            raise CatalogError(f"{event}: cascades.triggers years must be an integer >= 1, got {y!r}")
        out.append(dict(event=str(t["event"]), delta=_num(t["delta"], event, "cascade delta", -1.0, 1.0),
                        years=y, cond=t.get("if")))
    return out


def validate_research(rec: dict, event: str) -> None:
    r = rec.get("research")
    if r is None:
        return
    if not isinstance(r, dict):
        raise CatalogError(f"{event}: research must be a mapping")
    if "tier" in r and r["tier"] not in (1, 2, 3):
        raise CatalogError(f"{event}: research.tier must be 1, 2 or 3")
    if "review" in r and r["review"] not in ("complete", "pending"):
        raise CatalogError(f"{event}: research.review must be complete|pending")
