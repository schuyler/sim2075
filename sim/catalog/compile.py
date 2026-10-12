"""ADR-7 step 3: validated records -> CompiledCatalog with every name resolved to an index."""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from . import schema
from .expr import ExprContext, compile_expression
from .extract import extract_all, extract_record, event_id_from_filename
from .omega import validate_omega
from .types import (CascadeEdge, CatalogError, CatalogIndex, CompiledCatalog, ENTITY_GLOBAL,
                    IMPACT_DTYPE, ResolutionTree, StateCatalog, Type2Spec, Type3Spec)

DEFAULT_VARIANCE_TOL = 0.02
PRESSURE_BASELINE_SIGMAS = 4.0   # schema §Type 2: pressure at the 2025 baselines must lie within threshold ± 4·threshold_std


def check_pressure_scale(spec: Type2Spec, state: StateCatalog, event: str) -> tuple[float | None, str]:
    """Evaluate a Type 2 pressure expression at the catalog's 2025 baselines (schema §Type 2 pressure scale).

    Returns ``(value, note)``. ``value`` is None when a name the expression reads has no recorded
    baseline (country variables, factors, event state); the note then says which, so a skipped check is
    reported rather than silent. Raises CatalogError when the value is outside
    ``threshold ± PRESSURE_BASELINE_SIGMAS·threshold_std``.
    """
    missing = [n for n in spec.pressure.names if n not in state.baseline_2025]
    if missing:
        return None, f"pressure-scale check skipped: no 2025 baseline for {missing}"
    ns = {"_shape": (1,), **{n: np.array([state.baseline_2025[n]], dtype=np.float64) for n in spec.pressure.names}}
    value = float(spec.pressure(ns)[0])
    lo = spec.threshold - PRESSURE_BASELINE_SIGMAS * spec.threshold_std
    hi = spec.threshold + PRESSURE_BASELINE_SIGMAS * spec.threshold_std
    if not (lo <= value <= hi):
        raise CatalogError(
            f"{event}: Type 2 pressure at the 2025 baselines is {value:.4g}, outside [{lo:.4g}, {hi:.4g}] "
            f"(threshold {spec.threshold:g} ± {PRESSURE_BASELINE_SIGMAS:g}·{spec.threshold_std:g}); pressure expressions "
            f"share threshold's 0-100 scale (schema §Type 2)")
    return value, f"pressure at 2025 baselines = {value:.4g} (threshold {spec.threshold:g} ± {spec.threshold_std:g})"


def _resolve_var(var: str, state: StateCatalog, event: str, where: str) -> list[tuple[int, int, str]]:
    """'global_var' | 'ent.var' | '*.var' -> [(entity_idx, var_idx, key)], wildcard expanded to countries."""
    ent_idx = {e: i for i, e in enumerate(state.entities)}
    cvar_idx = {v: i for i, v in enumerate(state.country_vars)}
    gvar_idx = {v: i for i, v in enumerate(state.global_vars)}
    if "." not in var:
        if var in gvar_idx:
            return [(ENTITY_GLOBAL, gvar_idx[var], var)]
        if var in cvar_idx:
            raise CatalogError(f"{event}: {where} var {var!r} is a country variable; write entity.{var} or *.{var}")
        raise CatalogError(f"{event}: {where} unknown global variable {var!r}")
    ent, v = var.split(".", 1)
    if v not in cvar_idx:
        raise CatalogError(f"{event}: {where} unknown country variable {v!r} in {var!r}")
    if state.country_var_derived.get(v):
        raise CatalogError(f"{event}: {where} {var!r} targets derived variable {v!r}; impact an underlying variable instead")
    if ent == "*":
        return [(ent_idx[c], cvar_idx[v], f"{c}.{v}") for c in state.countries]
    if ent not in ent_idx:
        raise CatalogError(f"{event}: {where} unknown entity {ent!r} in {var!r}")
    return [(ent_idx[ent], cvar_idx[v], var)]


def compile_event_records(records: list[dict], omega: np.ndarray, state: StateCatalog, *,
                          known_event_ids: list[str] | None = None, strict_cascades: bool = True,
                          variance_tol: float = DEFAULT_VARIANCE_TOL) -> CompiledCatalog:
    """Compile already-extracted records.

    ``known_event_ids``: event IDs that exist in the catalog but are not in
    ``records`` (unmigrated files). Cascade edges to them are dropped with a
    recorded warning when ``strict_cascades`` is False, and are errors when it
    is True. Edges to IDs known nowhere are always errors (schema rule 4).
    """
    omega = validate_omega(omega, state.factors)
    K = len(state.factors)
    f_idx = {f: i for i, f in enumerate(state.factors)}

    # ---- pass 1: headers and IDs
    ids: list[str] = []
    for rec in records:
        eid = schema.validate_header(rec)
        if eid in ids:
            raise CatalogError(f"{eid}: duplicate event id")
        ids.append(eid)
    e_idx = {e: i for i, e in enumerate(ids)}
    E = len(ids)
    known = set(ids) | set(known_event_ids or [])

    lam = np.zeros((E, K), dtype=np.float64)
    causal = np.zeros(E, dtype=np.int8)
    p_annual = np.full(E, np.nan, dtype=np.float64)
    type2: dict[int, Type2Spec] = {}
    type3: dict[int, Type3Spec] = {}
    trees: list[ResolutionTree] = []
    rows: list[tuple] = []
    edges: list[CascadeEdge] = []
    warnings: list[str] = []
    declared_var = np.zeros(E, dtype=np.float64)
    meta_events: dict[str, dict] = {}
    pressure_at_baseline: dict[str, float | None] = {}
    notes: list[str] = []

    for i, rec in enumerate(records):
        eid = ids[i]
        causal[i] = rec["causal_type"]
        p = schema.validate_probability(rec, eid)
        loadings, declared_var[i] = schema.validate_factors(rec, eid)
        for f, v in loadings.items():
            if f not in f_idx:
                raise CatalogError(f"{eid}: unknown factor {f!r} (known: {list(state.factors)})")
            lam[i, f_idx[f]] = v

        res_ids, res_p, b_ids, b_p = schema.validate_resolution_tree(rec, eid)
        res_code = {r: k for k, r in enumerate(res_ids)}
        b_code = [{b: k for k, b in enumerate(bl)} for bl in b_ids]
        trees.append(ResolutionTree(res_ids, np.array(res_p), b_ids, [np.array(x) for x in b_p], res_code, b_code))

        # branch names usable in expressions: unique across resolutions only
        all_b = [b for bl in b_ids for b in bl]
        ambiguous = {b for b in all_b if all_b.count(b) > 1}
        flat_b = {b: b_code[ri][b] for ri, bl in enumerate(b_ids) for b in bl if b not in ambiguous}
        ctx = ExprContext(state, eid, res_code, flat_b, ambiguous)

        if causal[i] == 1:
            p_annual[i] = float(p["annual"])
        elif causal[i] == 2:
            type2[i] = Type2Spec(
                compile_expression(p["pressure"], ctx, "probability.pressure", "numeric"),
                float(p["threshold"]), float(p["threshold_std"]), float(p["sharpness"]), float(p["floor"]))
            pressure_at_baseline[eid], note = check_pressure_scale(type2[i], state, eid)
            notes.append(f"{eid}: {note}")
        else:
            pre = p["preconditions"]
            type3[i] = Type3Spec(
                [compile_expression(s, ctx, f"preconditions.all[{k}]", "boolean") for k, s in enumerate(pre.get("all") or [])],
                [(compile_expression(s["expr"], ctx, f"preconditions.sustained[{k}]", "boolean"), int(s["years"]))
                 for k, s in enumerate(pre.get("sustained") or [])],
                float(p["window"]), float(p["resolution"]))

        impacts = schema.validate_impacts(rec, eid, res_ids, b_ids)
        for (rc, bc), lst in impacts.items():
            for r in lst:
                for ent_i, var_i, _key in _resolve_var(r["var"], state, eid, f"impacts.{res_ids[rc]}.{b_ids[rc][bc]}"):
                    rows.append((i, rc, bc, ent_i, var_i, r["mean"], r["std"],
                                 r["onset_kind"], r["onset_years"], r["dur_kind"], r["dur_param"]))

        for c in schema.validate_cascades(rec, eid):
            # validate the edge fully (including its `if`) before deciding whether it can be kept
            cond = compile_expression(c["cond"], ctx, f"cascades.triggers[{c['event']}].if", "boolean") if c["cond"] is not None else None
            if c["event"] not in known:
                raise CatalogError(f"{eid}: cascade target {c['event']!r} is not an event in the catalog")
            if c["event"] not in e_idx:
                msg = f"{eid}: cascade target {c['event']!r} exists in the catalog but is not compiled (unmigrated); edge dropped"
                if strict_cascades:
                    raise CatalogError(msg)
                warnings.append(msg)
                continue
            edges.append(CascadeEdge(i, e_idx[c["event"]], c["delta"], c["years"], cond))
        schema.validate_research(rec, eid)
        meta_events[eid] = {k: rec.get(k) for k in ("domain", "scale", "onset", "reversibility")}
        meta_events[eid]["source"] = rec.get("_source")

    # ---- factor-explained variance and idiosyncratic sigma (ADR-2)
    achieved = np.einsum("ik,kl,il->i", lam, omega, lam)
    bad = np.abs(achieved - declared_var) > variance_tol
    if bad.any():
        detail = "; ".join(f"{ids[j]}: declared {declared_var[j]:.3f}, achieved {achieved[j]:.3f}" for j in np.flatnonzero(bad))
        raise CatalogError(f"factor variance outside tolerance {variance_tol}: {detail}")
    if (achieved > 1.0).any():
        raise CatalogError("factor-explained variance exceeds 1 for " + ", ".join(ids[j] for j in np.flatnonzero(achieved > 1.0)))
    sigma_idio = np.sqrt(1.0 - achieved)

    index = CatalogIndex(
        entity={e: k for k, e in enumerate(state.entities)},
        country_var={v: k for k, v in enumerate(state.country_vars)},
        global_var={v: k for k, v in enumerate(state.global_vars)},
        factor=dict(f_idx), event=dict(e_idx))
    table = np.array(rows, dtype=IMPACT_DTYPE) if rows else np.zeros(0, dtype=IMPACT_DTYPE)
    return CompiledCatalog(
        event_ids=ids, lam=lam, sigma_idio=sigma_idio, causal_type=causal, p_annual=p_annual,
        type2=type2, type3=type3, resolution_tree=trees, impact_table=table, cascade_edges=edges,
        index=index, omega=omega,
        meta={"declared_variance": declared_var, "achieved_variance": achieved,
              "warnings": warnings, "notes": notes, "pressure_at_baseline": pressure_at_baseline,
              "events": meta_events, "state_catalog": state})


def compile_catalog(event_paths, omega: np.ndarray, state_catalog: StateCatalog, *,
                    known_event_ids: list[str] | None = None, strict_cascades: bool = True,
                    variance_tol: float = DEFAULT_VARIANCE_TOL) -> CompiledCatalog:
    """The §4.1 entry point: markdown paths -> CompiledCatalog. Unmigrated files (no id block) are errors here."""
    records = []
    for p in event_paths:
        rec = extract_record(p)
        if rec is None:
            raise CatalogError(f"{p}: no YAML 'id' block (event not migrated)")
        records.append(rec)
    return compile_event_records(records, omega, state_catalog, known_event_ids=known_event_ids,
                                 strict_cascades=strict_cascades, variance_tol=variance_tol)


def compile_events_dir(events_dir: str | Path, omega: np.ndarray, state_catalog: StateCatalog, *,
                       strict_cascades: bool = False, variance_tol: float = DEFAULT_VARIANCE_TOL) -> CompiledCatalog:
    """Compile every migrated event under ``events_dir``; unmigrated files contribute only their IDs."""
    records, known, unmigrated = extract_all(events_dir)
    cat = compile_event_records(records, omega, state_catalog, known_event_ids=known,
                                strict_cascades=strict_cascades, variance_tol=variance_tol)
    cat.meta["unmigrated"] = [str(p) for p in unmigrated]
    return cat


def compile_one(path: str | Path, omega: np.ndarray, state_catalog: StateCatalog, known_event_ids: list[str]) -> CompiledCatalog:
    """Compile a single event file with cascade edges to other events dropped (diagnostic use)."""
    return compile_catalog([path], omega, state_catalog, known_event_ids=known_event_ids, strict_cascades=False)
