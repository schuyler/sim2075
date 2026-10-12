"""FIX-C: TAIWAN_CONFLICT + AMOC_WEAKENING compiled from the real repo markdown, checked against a
hand-built description of the structure the compiler must produce. Compiler ground truth.

Hand computations recorded here:
  Taiwan loadings EAS .38, GPT .33, FIN .09, TECH .07; Ω entries EAS-GPT .55, EAS-FIN .30, GPT-FIN .25,
  GPT-TECH .25, FIN-TECH .20 (others 0):
     Σλ² = .1444 + .1089 + .0081 + .0049 = .2663
     2·Σλᵢλⱼρᵢⱼ = 2·(.38·.33·.55 + .38·.09·.30 + .33·.09·.25 + .33·.07·.25 + .09·.07·.20) = 2·.09369 = .18738
     (ΛΩΛᵀ) = .45368  (declared .45)
  AMOC loadings CLIM .67, FOOD .16, EUR .12, SSA .08, LAM .04; Ω CLIM-FOOD .5, CLIM-SSA .35, FOOD-SSA .4, EUR-SSA .2:
     Σλ² = .4489 + .0256 + .0144 + .0064 + .0016 = .4969
     2·Σλᵢλⱼρᵢⱼ = 2·(.67·.16·.5 + .67·.08·.35 + .16·.08·.4 + .12·.08·.2) = 2·.0794 = .1588
     (ΛΩΛᵀ) = .6557  (declared .65)
  Impact rows: Taiwan military_conflict.limited 10 rows × 3 branches (inherit/scale 1.5, 3.0) = 30, settlement 3 × 2
  (scale .5) = 6 -> 36; AMOC default 21 -> 57 total.
  AMOC pressure at the 2025 baselines (temp 1.3, ice 4.5, amoc 95) = 100·(.5·(1.3/2) + .25·0 + .25·0) = 32.5
  (the schema's 0-100 pressure scale, 2026-10-12), inside threshold 65 ± 4·15.
"""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TAIWAN = REPO / "events" / "geopolitical" / "taiwan-conflict.md"
AMOC = REPO / "events" / "climate" / "amoc-weakening.md"

TAIWAN_VARIANCE = 0.45368
AMOC_VARIANCE = 0.6557
TAIWAN_LOADINGS = {"F_EAS": 0.38, "F_GPT": 0.33, "F_FIN": 0.09, "F_TECH": 0.07}
AMOC_LOADINGS = {"F_CLIM": 0.67, "F_FOOD": 0.16, "F_EUR": 0.12, "F_SSA": 0.08, "F_LAM": 0.04}
TAIWAN_TREE = (["military_conflict", "settlement"], [0.65, 0.35],
               [["limited", "full_invasion", "nuclear"], ["stable", "unstable"]], [[0.55, 0.30, 0.15], [0.40, 0.60]])
N_ROWS_TAIWAN, N_ROWS_AMOC = 36, 21
RESOLVES_AFTER = [3, 0]
# gdp_real rows are multiplicative: Taiwan 3 (twn, chn, usa) × 3 branches + settlement 2 (twn, chn) × 2 = 13; AMOC 5 = 18
N_MULTIPLICATIVE_ROWS = 18   # Taiwan declares resolves_after: 3; AMOC has no until: resolved rows
AMOC_PRESSURE_AT_BASELINE = 32.5
AMOC_BASELINE_NS = {"global_temp_anomaly": 1.3, "arctic_sea_ice_sept": 4.5, "amoc_strength": 95.0}
# cascade targets of both events are unmigrated as of E0: all 5 edges are dropped with warnings
N_DROPPED_EDGES = 5
