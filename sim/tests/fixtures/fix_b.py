"""FIX-B: one event of each causal type; one conditional cascade; one `until: resolved` impact;
one `sustained` precondition; one permanent and one decaying impact. Hand-traced event log below.

World:
  factors FG, FC with Ω = [[1, .5], [.5, 1]]  ->  L = [[1, 0], [.5, √.75]], so FG = z0, FC = .5·z0 + .866·z1
  country x with vars stress, gdp; globals temp, conflicts
  dynamics: temp += 0.1/yr; x.stress += 0.5/yr (no mean-reverting variables: dyn_z has width 0)
  initial: x.stress = 0, x.gdp = 100, temp = 1.0, conflicts = 0
  params: until_resolved_years = 2, start 2025, 6 years

Events (index: id):
  0: T1  Type 1, annual .05, loading FG .5 (σ_idio = √.75)
         resolutions bad (p .6) / good (p .4), each with the single branch `default`
         impacts bad.default: x.gdp mag [-10, 0] immediate decay 2;  good.default: x.gdp mag [+5, 0] immediate decay 2
         cascade -> T3: delta .5 for 2 years, if resolution == 'bad'
  1: T2  Type 2, pressure = temp, threshold 2.0 (std .5, per-run offset draw 0 -> 2.0), sharpness 10, floor .01,
         loading FC .5; impacts default: temp mag [1, 0] immediate permanent
  2: T3  Type 3, preconditions all: x.stress > 1; sustained: FG > 1.0 for 2 years; window .2 × resolution .5 = .1
         loading FG .4 (σ_idio = √.84); impacts default: conflicts mag [1, 0] immediate until: resolved

Scripted draws (R = 1):
  factor z = (1.5, 0) in years 0-3 (FG = 1.5, FC = .75), (0, 0) in years 4-5.
  idio ε = 0 except: T1 year 1: -3;  T3 year 3: -1;  T2 year 5: -3.
  res_u = .3 (T1 -> 'bad'), branch_u = .5, impact_z = 0 everywhere.

Hand trace (year index t, calendar 2025 + t):
  t=0  nothing fires (T1: Z=.75 -> U≈.77; T2: p≈.0100, Z=.375; T3 gate closed: stress 0). After: stress .5, temp 1.1,
       sustained counter(T3) = 1 (FG 1.5 > 1).
  t=1  T1: Z = .5·1.5 + .866·(-3) = -1.848 -> U ≈ .032 < .05 -> fires, res 'bad' (code 0), branch 0, M = -10 -> gdp 90.
       Cascade T1->T3 (if resolution=='bad' holds) pushed: active for years t=2,3. After: stress 1.0, temp 1.2, counter 2.
  t=2  T3 gate: x.stress = 1.0 is not > 1 -> closed (p_eff = .1 + .5 = .6 but no fire). gdp shock age 1: -10·.5^(1/2) ->
       gdp = 100 - 7.0710678. After: stress 1.5, temp 1.3, counter 3; cascade remaining 1.
  t=3  T3 gate open (stress 1.5 > 1, counter 3 >= 2); p_base .1, cascade delta .5 -> p_eff .6, mask = 1<<0 = 1.
       Z = .4·1.5 + √.84·(-1) = .6 - .9165 = -.3165 -> U ≈ .376 < .6 -> fires; conflicts = 1 (until resolved; owner
       active through t=4). gdp: age 2 -> 100 - 5 = 95. After: stress 2.0, temp 1.4, counter 4; cascade expires.
  t=4  FG = 0: T3 p_eff .1, U = .5 -> no fire. conflicts shock age 1, owner active -> stays 1. gdp: age 3 -> 100 - 3.5355339.
       After: temp 1.5, stress 2.5, counter resets to 0, T3 owner flag cleared (year >= active_until).
  t=5  conflicts shock: owner inactive -> contribution 0 -> conflicts 0, slot freed. T3 gate closed (counter 0).
       T2: pressure temp = 1.5, p = .01 + .99/(1+e^{10·(2.0-1.5)}) = .01 + .99/(1+e^5); Z = .5·0 + √.75·(-3) = -2.598
       -> U ≈ .0047 < p -> fires; temp = 1.5 + 1 (permanent, immediate), then drift -> 2.6. gdp: age 4 -> 100 - 2.5.
"""
from __future__ import annotations

import math

import numpy as np

from sim.catalog.types import (CascadeEdge, CompiledCatalog, DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED,
                               ONSET_IMMEDIATE, Type2Spec, Type3Spec)
from sim.reference.model import DynamicsSpec, InitialConditions, SimParams, VarDynamics
from sim.rng import DrawShapes, ScriptedDraws
from . import builders as B

YEARS = 6
OMEGA = np.array([[1.0, 0.5], [0.5, 1.0]])
EVENTS = ["T1", "T2", "T3"]


def catalog() -> CompiledCatalog:
    sc = B.state_catalog(["FG", "FC"], ["x"], ["stress", "gdp"], ["temp", "conflicts"])
    idx = B.index_for(sc, EVENTS)
    lam = np.array([[0.5, 0.0], [0.0, 0.5], [0.4, 0.0]])
    trees = [
        B.tree([("bad", 0.6, [("default", 1.0)]), ("good", 0.4, [("default", 1.0)])]),
        B.default_tree(),
        B.default_tree(),
    ]
    rows = B.impact_rows([
        (0, 0, 0, idx.entity["x"], idx.country_var["gdp"], -10.0, 0.0, ONSET_IMMEDIATE, 0, DUR_DECAY, 2.0),
        (0, 1, 0, idx.entity["x"], idx.country_var["gdp"], 5.0, 0.0, ONSET_IMMEDIATE, 0, DUR_DECAY, 2.0),
        (1, 0, 0, B.GLOBAL, idx.global_var["temp"], 1.0, 0.0, ONSET_IMMEDIATE, 0, DUR_PERMANENT, math.nan),
        (2, 0, 0, B.GLOBAL, idx.global_var["conflicts"], 1.0, 0.0, ONSET_IMMEDIATE, 0, DUR_UNTIL_RESOLVED, math.nan),
    ])
    type2 = {1: Type2Spec(B.expr(["temp"], lambda ns: ns["temp"], "numeric"), 2.0, 0.5, 10.0, 0.01)}
    type3 = {2: Type3Spec([B.expr(["x.stress"], lambda ns: ns["x.stress"] > 1, "boolean")],
                          [(B.expr(["FG"], lambda ns: ns["FG"] > 1.0, "boolean"), 2)], 0.2, 0.5)}
    edges = [CascadeEdge(0, 2, 0.5, 2, B.expr(["resolution"], lambda ns: ns["resolution"] == 0, "boolean"))]
    return CompiledCatalog(event_ids=EVENTS, lam=lam, sigma_idio=B.sigma_from(lam, OMEGA),
                           causal_type=np.array([1, 2, 3], dtype=np.int8), p_annual=np.array([0.05, np.nan, np.nan]),
                           type2=type2, type3=type3, resolution_tree=trees, impact_table=rows, cascade_edges=edges,
                           index=idx, omega=OMEGA, meta={"fixture": "FIX-B", "state_catalog": sc})


def initial_conditions() -> InitialConditions:
    return InitialConditions(country=np.array([[0.0, 100.0]]), global_=np.array([1.0, 0.0]))


def dynamics() -> DynamicsSpec:
    return DynamicsSpec([VarDynamics("temp", "additive", rate=0.1), VarDynamics("x.stress", "additive", rate=0.5)])


def params() -> SimParams:
    return SimParams(until_resolved_years=2, start_year=2025, years=YEARS)


def draws() -> ScriptedDraws:
    shapes = DrawShapes(K=2, E=3, E_type2=1, n_impact_rows=4, n_noisy_vars=0)
    years = []
    for t in range(YEARS):
        z = np.array([[1.5, 0.0]]) if t <= 3 else np.zeros((1, 2))
        eps = np.zeros((1, 3))
        if t == 1:
            eps[0, 0] = -3.0
        if t == 3:
            eps[0, 2] = -1.0
        if t == 5:
            eps[0, 1] = -3.0
        years.append({"factor": z, "idio": eps, "res_u": np.full((1, 3), 0.3), "branch_u": np.full((1, 3), 0.5),
                      "impact_z": np.zeros((1, 4)), "dyn_z": np.zeros((1, 0))})
    return ScriptedDraws({"t2_offset": np.zeros((1, 1))}, years, shapes)


def expected() -> dict:
    p_t2_year5 = 0.01 + 0.99 / (1.0 + math.exp(10.0 * (2.0 - 1.5)))
    events = [
        dict(year=2026, event=0, resolution=0, branch=0, p_base=0.05, p_eff=0.05, cascade_mask=0, magnitudes=[(0, -10.0)]),
        dict(year=2028, event=2, resolution=0, branch=0, p_base=0.1, p_eff=0.6, cascade_mask=1, magnitudes=[(3, 1.0)]),
        dict(year=2030, event=1, resolution=0, branch=0, p_base=p_t2_year5, p_eff=p_t2_year5, cascade_mask=0, magnitudes=[(2, 1.0)]),
    ]
    gdp = [100.0, 90.0, 100 - 10 * 0.5 ** 0.5, 95.0, 100 - 10 * 0.5 ** 1.5, 97.5]      # end of years 0..5
    conflicts = [0.0, 0.0, 0.0, 1.0, 1.0, 0.0]
    temp = [1.1, 1.2, 1.3, 1.4, 1.5, 2.6]
    stress = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    gate_t3 = [False, False, False, True, True, False]
    p_eff_t3 = [0.1, 0.1, 0.6, 0.6, 0.1, 0.1]
    return dict(events=events, gdp=gdp, conflicts=conflicts, temp=temp, stress=stress, gate_t3=gate_t3, p_eff_t3=p_eff_t3)
