"""FIX-A: 1 Type-1 event, 2 entities, 3 country variables (+1 global), dynamics noise off, 5 years.

Everything below is hand-computable. The expected trajectory is written out in
``expected()`` as literal step-by-step arithmetic following
simulator-architecture §3 and the pinned shock schedule — it does not call the
engine. Draws are scripted so that the single event fires in year 1 only.

World:
  factors FA, FB with Ω = [[1, .5], [.5, 1]]
  countries a, b; country vars gdp_per_capita ($K), gdp_growth (%/yr), life_expectancy (yr); global oil_brent
  event SHOCK: Type 1, annual 0.10, loading FA 0.6 -> factor-explained variance 0.36, σ_idio = 0.8
     impacts (default.default):
        row 0: a.gdp_growth  mag [-4, 1], immediate, decay half-life 1
        row 1: oil_brent     mag [20, 0], immediate, permanent
  dynamics: gdp_growth mean-reverts to 2 with half-life 1 (θ = ln 2), σ = 0, for a and b;
            gdp_per_capita *= 1 + gdp_growth/100 (growth-rate-first); life_expectancy += 0.2 (a), 0.1 (b);
            oil_brent mean-reverts to 75 with half-life 2, σ = 0.
  initial: a = (50, 2, 80), b = (10, 2, 70), oil = 75.

Scripted draws (R = 1): factor z = 0 every year, so F = 0 and Z = 0.8·ε.
  year 1: ε = -2  -> Z = -1.6 -> U = Φ(-1.6) ≈ 0.0548 < 0.10 -> fires
  other years: ε = +1 -> U ≈ 0.79 -> no fire
  impact_z row 0 = 1 (so M = -4 + 1·1 = -3), row 1 = 0 (M = 20).
"""
from __future__ import annotations

import math

import numpy as np

from sim.catalog.types import (CompiledCatalog, DUR_DECAY, DUR_PERMANENT, ONSET_IMMEDIATE)
from sim.reference.model import DynamicsSpec, InitialConditions, SimParams, VarDynamics
from sim.rng import DrawShapes, ScriptedDraws
from . import builders as B

YEARS = 5
P_ANNUAL = 0.10
OMEGA = np.array([[1.0, 0.5], [0.5, 1.0]])


def catalog() -> CompiledCatalog:
    sc = B.state_catalog(["FA", "FB"], ["a", "b"], ["gdp_per_capita", "gdp_growth", "life_expectancy"], ["oil_brent"])
    lam = np.array([[0.6, 0.0]])
    idx = B.index_for(sc, ["SHOCK"])
    rows = B.impact_rows([
        (0, 0, 0, idx.entity["a"], idx.country_var["gdp_growth"], -4.0, 1.0, ONSET_IMMEDIATE, 0, DUR_DECAY, 1.0),
        (0, 0, 0, B.GLOBAL, idx.global_var["oil_brent"], 20.0, 0.0, ONSET_IMMEDIATE, 0, DUR_PERMANENT, math.nan),
    ])
    return CompiledCatalog(event_ids=["SHOCK"], lam=lam, sigma_idio=np.array([0.8]), causal_type=np.array([1], dtype=np.int8),
                           p_annual=np.array([P_ANNUAL]), type2={}, type3={}, resolution_tree=[B.default_tree()],
                           impact_table=rows, cascade_edges=[], index=idx, omega=OMEGA,
                           meta={"fixture": "FIX-A", "state_catalog": sc})


def initial_conditions() -> InitialConditions:
    return InitialConditions(country=np.array([[50.0, 2.0, 80.0], [10.0, 2.0, 70.0]]), global_=np.array([75.0]))


def dynamics() -> DynamicsSpec:
    return DynamicsSpec([
        VarDynamics("a.gdp_growth", "mean_revert", mu=2.0, half_life=1.0, sigma=0.0),
        VarDynamics("b.gdp_growth", "mean_revert", mu=2.0, half_life=1.0, sigma=0.0),
        VarDynamics("oil_brent", "mean_revert", mu=75.0, half_life=2.0, sigma=0.0),
        VarDynamics("a.gdp_per_capita", "gdp_stock", growth_key="a.gdp_growth"),
        VarDynamics("b.gdp_per_capita", "gdp_stock", growth_key="b.gdp_growth"),
        VarDynamics("a.life_expectancy", "additive", rate=0.2),
        VarDynamics("b.life_expectancy", "additive", rate=0.1),
    ])


def params() -> SimParams:
    return SimParams(until_resolved_years=1, start_year=2025, years=YEARS)


def draws() -> ScriptedDraws:
    shapes = DrawShapes(K=2, E=1, E_type2=0, n_impact_rows=2, n_noisy_vars=3)
    years = []
    for t in range(YEARS):
        eps = -2.0 if t == 1 else 1.0
        years.append({"factor": np.zeros((1, 2)), "idio": np.array([[eps]]), "res_u": np.array([[0.5]]),
                      "branch_u": np.array([[0.5]]), "impact_z": np.array([[1.0, 0.0]]), "dyn_z": np.zeros((1, 3))})
    return ScriptedDraws({"t2_offset": np.zeros((1, 0))}, years, shapes)


def expected() -> dict:
    """Hand trace. Returns per-year end-of-year values and the expected event log."""
    ln2 = math.log(2.0)
    a_pc, a_g, a_le = 50.0, 2.0, 80.0
    b_pc, b_g, b_le = 10.0, 2.0, 70.0
    oil = 75.0
    M = -3.0                       # drawn magnitude of the gdp_growth shock
    traj = []
    for t in range(YEARS):
        # step 6: shock contributions (fires in year 1; contribution(age) = M * 0.5**age; increments applied)
        if t == 1:
            a_g += M                      # age 0 contribution
            oil += 20.0                   # permanent, immediate: folded at firing
        elif t > 1:
            age = t - 1
            a_g += M * 0.5 ** age - M * 0.5 ** (age - 1)
        # step 7: mean reversion first (θ = ln2 / half-life), then stocks and drifts
        a_g = a_g + ln2 * (2.0 - a_g)
        b_g = b_g + ln2 * (2.0 - b_g)
        oil = oil + (ln2 / 2.0) * (75.0 - oil)
        a_pc = a_pc * (1.0 + a_g / 100.0)
        b_pc = b_pc * (1.0 + b_g / 100.0)
        a_le += 0.2
        b_le += 0.1
        traj.append(dict(a=(a_pc, a_g, a_le), b=(b_pc, b_g, b_le), oil=oil))
    events = [dict(year=2026, event=0, resolution=0, branch=0, p_base=P_ANNUAL, p_eff=P_ANNUAL, cascade_mask=0,
                   magnitudes=[(0, -3.0), (1, 20.0)])]
    return {"trajectory": traj, "events": events}
