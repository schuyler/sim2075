---
title: amazon-tipping-point
type: note
permalink: events/climate/amazon-tipping-point
tags:
- event
- type-2
- threshold
- climate
- environmental
- amazon
- tipping-point
- level-1
---

# Amazon Tipping Point

**Type 2 (Threshold) Event** — Probability increases as deforestation and climate stress accumulate; threshold dynamics govern transition from rainforest to degraded savanna state.

This specification addresses a well-studied climate tipping point with significant scientific literature providing calibration guidance.

---

## Specification

```yaml
id: AMAZON_TIPPING_POINT
domain: environmental
scale: regional
causal_type: 2
onset: gradual
reversibility: irreversible
```

*Scale: regional (with global consequences via carbon release). Onset speed: gradual (decades for full transition, but tipping point crossing is discrete). Reversibility: irreversible on human timescales (centuries to millennia for recovery).*

## Description

Crossing of critical threshold triggering large-scale Amazon rainforest dieback—transition from closed-canopy rainforest to degraded savanna or seasonal forest across substantial portion (>40%) of the Amazon basin. Driven by interaction of deforestation, climate change (warming + drying), and fire feedback loops.

This is a **state transition**: `amazon_forest_cover` crosses below viability threshold, initiating self-reinforcing dieback that continues even if proximate drivers (deforestation, warming) stabilize.

**What marks occurrence**: Scientific consensus that tipping point has been crossed, evidenced by: large-scale canopy die-off not explained by direct deforestation; failure of forest regeneration in previously cleared areas; persistent shift in regional rainfall patterns; fire incursion into previously fire-resistant intact forest.

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

The Amazon tipping point is a canonical threshold system:
- Forest generates ~30% of its own rainfall via evapotranspiration
- As forest cover declines, rainfall declines, stressing remaining forest
- Below critical forest cover, positive feedback dominates → runaway dieback
- Scientific literature identifies specific thresholds (deforestation %, temperature rise)

This is not stochastic (Type 1)—probability is strongly state-conditioned.
This is not contingent (Type 3)—no small-N actor decisions determine outcome.

### Pressure Function

The pressure function uses global state variables from [[methodology/reference/state-variables-global]] and Brazil-specific variables from [[methodology/reference/state-variables-country]]. Some Amazon-specific dynamics (fire incursion, drought frequency) are not directly tracked and must be proxied through available variables.

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `amazon_forest_cover` | 0.40 | inverse_threshold(80) | Primary driver; sharp increase as 20-25% deforestation (80-75% cover) approached |
| `global_temp_anomaly` | 0.25 | linear | Regional warming tracks global; reduces moisture, increases fire risk |
| `climate_variability` | 0.15 | linear | Proxies drought frequency; elevated extremes stress forest |
| `bra.gdp_share_agriculture` | 0.10 | linear | Agricultural expansion pressure; higher share → more deforestation pressure |
| `global_co2_ppm` | 0.05 | linear | CO2 fertilization partially offsets stress (minor positive effect) |
| `bra.protest_intensity_annual` | 0.05 | inverse | Proxy for governance/enforcement capacity; high protest → weak enforcement |

The YAML expression below realizes these transforms in the expression language's subset: the forest-cover `inverse_threshold(80)` as a clipped linear ramp that is zero at 95% cover and saturates at 75% cover (`min(1, max(0, (95 − cover) / 20))`, reaching 0.75 at the 80% mark and 1.0 at the 25%-deforestation end of the Lovejoy & Nobre band), and every other term as the linear normalization written in the original calculation below.

**Pressure calculation** (original specification):
```
pressure = 0.40 × inverse_threshold(amazon_forest_cover, 80)  # danger accelerates below 80%
         + 0.25 × (global_temp_anomaly - 1.0) / 3.0  # normalized: 1°C baseline, 4°C danger
         + 0.15 × climate_variability / 150  # normalized to elevated variability
         + 0.10 × bra.gdp_share_agriculture / 15  # normalized to Brazil's ~5% share
         - 0.05 × (global_co2_ppm - 420) / 200  # minor offsetting effect
         + 0.05 × bra.protest_intensity_annual / 100  # proxy for governance weakness
```
*Normalized to 0-100 scale*

**Proxy limitations**: The universal variable set cannot directly capture Amazon-specific dynamics like fire penetration into intact forest, dry season lengthening, or regional (vs. global) temperature anomaly. The pressure function proxies these through their drivers (`global_temp_anomaly`, `climate_variability`) and correlates (`bra.gdp_share_agriculture` as deforestation pressure). This is a known fidelity limitation; probability is calibrated primarily via scientific literature estimates rather than mechanical pressure calculation.

### Threshold Specification

| Parameter | Value |
|-----------|-------|
| **Estimate** | 70 (on 0-100 pressure scale) |
| **Uncertainty** | ±15 (significant scientific uncertainty) |
| **Sharpness (k)** | 0.25 (sharp; once threshold crossed, dieback accelerates rapidly) |
| **Historical calibration** | No direct historical analog at this scale; calibrated from paleoecological transitions, regional dieback events, and process models |

### Scientific Basis for Threshold

Key estimates from literature:
- **Deforestation threshold**: 20-25% total deforestation may trigger basin-wide dieback (Lovejoy & Nobre 2018)
- **Temperature threshold**: +3-4°C regional warming significantly increases dieback risk
- **Combined threshold**: Interaction effects—lower deforestation can trigger dieback if warming is high, and vice versa
- **Current state**: ~17-20% deforested (~80-83% forest cover); ~1.2°C regional warming already

The 70/100 pressure threshold reflects the combined interaction, with current pressure estimated at ~55-60/100 (dangerously elevated).

### Minimum Probability

**Floor**: 0.2%/year (residual risk from extreme drought or fire even at low pressure)

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.40 * min(1.0, max(0.0, (95 - amazon_forest_cover) / 20)) +
      0.25 * ((global_temp_anomaly - 1.0) / 3.0) +
      0.15 * (climate_variability / 150) +
      0.10 * (bra.gdp_share_agriculture / 15) -
      0.05 * ((global_co2_ppm - 420) / 200) +
      0.05 * (bra.protest_intensity_annual / 100)
    )
  threshold: 70
  threshold_std: 15
  sharpness: 0.25
  floor: 0.002
  annual: 0.010
  range: [0.002, 0.080]
  confidence: medium
```

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.0% |
| **At low pressure (floor)** | 0.2% |
| **At high pressure** | 5-8% |
| **Confidence** | Medium (significant model uncertainty) |
| **25-year cumulative** | ~22% at point estimate |

### Current Pressure Estimate

Current pressure: ~58/100 (elevated, approaching danger zone)
- `amazon_forest_cover`: ~80-83% (approaching 75-80% threshold)
- `global_temp_anomaly`: ~1.3°C
- `climate_variability`: elevated (major droughts 2005, 2010, 2015-16, 2023-24)
- `bra.gdp_share_agriculture`: ~5%
- `global_co2_ppm`: ~425 ppm (slight offsetting effect)

*The ~58 figure is a judgment estimate of the combined-interaction pressure, not the expression's value: at the state catalog's 2025 baselines (forest cover 85, 1.3°C, variability index 100, 425 ppm) with Brazil's agriculture share at 5% and protest intensity at ~30, the YAML expression gives ~37; at the prose's 82% cover it gives ~43, and it reaches ~57 only at 75% cover. The expression tracks the drivers' direction and the 70 ± 15 threshold is calibrated against the literature, not against this arithmetic (see Proxy limitations above).*

### Derivation

1. **Process model estimates**: Multiple Earth system models suggest 10-30% probability of major Amazon dieback by 2100 under high-emission scenarios
2. **Annualization**: ~0.5-1.5%/year implied
3. **Current trajectory adjustment**: Deforestation accelerated 2019-2022 (Bolsonaro era); recent slowdown but cumulative damage persists
4. **Central estimate**: 1.0%/year at current pressure

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- More likely than: AMOC collapse (~0.5%)
- Similar to: Permafrost methane release (~1%), severe pandemic (~2%)
- Less likely than: Global financial crisis (~3%)

This ranking aligns with scientific assessments placing Amazon among the higher-risk near-term tipping points.

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4:

**1. Threshold uncertainty is enormous**

The 20-25% deforestation threshold comes primarily from Lovejoy & Nobre (2018), but this is based on models of the moisture recycling system, not empirical observation. Some models show the forest is more resilient; others show it's more fragile. The difference between "threshold at 20%" and "threshold at 30%" is the difference between "imminent danger" and "decades of buffer." We simply don't know.

*Counter*: The uncertainty is acknowledged (±15 on pressure scale). But multiple lines of evidence converge on the 20-25% range, and we're already at 17-20% deforested. Even if the threshold is higher, current trajectory crosses it.

**2. CO2 fertilization may dominate**

Elevated CO2 enhances plant water-use efficiency and may substantially offset drought stress. Some studies suggest the Amazon could remain stable even with significant warming if CO2 fertilization effects are strong. We may be underweighting this negative feedback.

*Counter*: CO2 fertilization is included (minor negative pressure). But empirical evidence shows the effect saturates and is offset by heat stress, ozone damage, and nutrient limitations. Most integrated assessments conclude warming effects dominate.

**3. Dieback may be slow, not a discontinuity**

Even if the threshold is crossed, dieback may proceed over decades to centuries. A 50-year decline isn't really a "discontinuity" in the simulation sense—it's a baseline trajectory shift. The framing as a discrete event may not match the physical reality.

*Counter*: The event marks threshold-crossing, which is discrete even if consequences unfold gradually. Once crossed, the trajectory is qualitatively different from baseline (self-reinforcing dieback vs. stable forest). The severity branches capture the range of transition speeds.

**4. Policy can reverse trajectory**

Brazilian deforestation rates dropped dramatically after 2004 and again after 2022. If effective governance is maintained, forest cover could stabilize or even increase. The probability should be more sensitive to policy scenarios than the specification implies.

*Counter*: Policy is captured through `bra.gdp_share_agriculture` and `bra.protest_intensity_annual` proxies, imperfectly. But even with strong policy, climate change continues increasing stress. And policy is not guaranteed—the Bolsonaro years showed rapid reversal is possible.

### Probability Evolution

For Type 2 events, probability varies with pressure accumulation over the simulation horizon. The 1.0% annual probability is calibrated to current conditions; actual probability evolves as pressure changes.

| Period | Estimated Pressure | Annual Probability | Rationale |
|--------|-------------------|-------------------|-----------|
| 2025-2035 | 55 → 65 | ~0.8% | Current stress high but below threshold; policy uncertain |
| 2035-2050 | 65 → 75 | ~1.5% | Pressure enters threshold zone; cumulative warming + deforestation |
| 2050-2075 | 75+ | ~2.5-4.0% | If no tipping by 2050, either pressure very high (transition likely) or system more resilient than modeled |

### Key Uncertainties

- **Threshold location**: 20% or 25% deforestation? Uncertainty is policy-relevant
- **Resilience vs. fragility**: Some models show more resilience than others
- **CO2 fertilization**: Magnitude of offsetting effect uncertain
- **Policy trajectory**: Brazilian governance is swing variable for deforestation rate
- **Interaction with ENSO**: El Niño events dramatically increase drought/fire risk

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

```yaml
factors:
  F_CLIM: 0.54  # Dominant: warming, drought, precipitation changes are primary drivers
  F_FOOD: 0.34  # Agricultural expansion (soy, cattle) drives deforestation
  F_LAM: 0.15   # Regional instability affects governance capacity; imperfect proxy for environmental policy
  F_FIN: 0.11   # Commodity prices affect deforestation economics
  F_GPT: 0.08   # International pressure/trade policy affects deforestation incentives
variance: 0.65  # Type 2 target
```

Factors carrying no loading:

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_TECH | 0.00 | No significant pathway |
| F_HLTH | 0.00 | No significant pathway |
| F_EUR | 0.00 | No direct pathway (EU deforestation regulation effect is via F_GPT/F_FIN) |
| F_EAS | 0.00 | China demand effect captured in F_FOOD/F_FIN |
| F_SAS | 0.00 | No significant pathway |
| F_MENA | 0.00 | No significant pathway |
| F_SSA | 0.00 | No significant pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.77 from original loadings. The original (2025-12-18) loadings were F_CLIM 0.70, F_FOOD 0.45, F_LAM 0.20, F_FIN 0.15, F_GPT 0.10, with sum of squared loadings 0.49 + 0.20 + 0.04 + 0.02 + 0.01 = 0.76; the scaled loadings above achieve 0.648 against the Ω matrix.

### Loading Interpretation (Type 2)

Factors shock state variables that feed into pressure function:
- High F_CLIM → `global_temp_anomaly` and `climate_variability` increase → pressure rises
- High F_FOOD → agricultural commodity demand → deforestation pressure (proxied through Brazil agriculture share)
- High F_LAM → governance instability → enforcement failure → deforestation accelerates
- High F_FIN → commodity price boom → deforestation economics favor clearing

---

## Severity Branches

Once tipping point is crossed, the extent and speed of dieback varies:

```yaml
branches:
  - {id: partial, p: 0.45, desc: "Eastern/southern Amazon to savanna; ~40-50% of basin; 30-50 Gt C"}
  - {id: major, p: 0.40, desc: "50-70% of basin; only wettest northwest keeps closed forest; 50-80 Gt C"}
  - {id: catastrophic, p: 0.15, desc: "Near-complete collapse (>80%); 80-120 Gt C; regional desertification"}
```

### Branch 1: Partial Dieback

**Probability given event**: 45%

**Description**: Eastern and southern Amazon transition to degraded savanna/seasonal forest. ~40-50% of basin affected. Western Amazon (wetter, less deforested) partially survives.

**Impact magnitudes** (baseline):
- Carbon release: 30-50 Gt C over decades
- Forest cover loss: 40-50%
- Regional rainfall decline: significant but not collapse

**Factor modifications during aftermath**:
- F_CLIM: +0.30 for 20 years
- F_FOOD: +0.20 for 10 years
- F_LAM: +0.25 for 10 years

### Branch 2: Major Dieback

**Probability given event**: 40%

**Description**: Large-scale transition across 50-70% of basin. Only wettest northwestern areas maintain closed forest.

**Impact magnitudes** (2.0× baseline):
- Carbon release: 50-80 Gt C
- Forest cover loss: 50-70%
- Major regional rainfall collapse

**Factor modifications during aftermath**:
- F_CLIM: +0.50 for 30 years
- F_FOOD: +0.35 for 15 years
- F_LAM: +0.40 for 15 years

**Cascade effects**:
- PERMAFROST_METHANE_RELEASE: +0.3%/year probability (warming acceleration)

### Branch 3: Catastrophic Dieback

**Probability given event**: 15%

**Description**: Near-complete Amazon collapse (>80% transition). Carbon release: 80-120 Gt C (equivalent to ~8-12 years global emissions). Regional desertification. Mass extinction of Amazon-endemic species.

**Impact magnitudes** (4.0× baseline):
- Carbon release: 80-120 Gt C
- Forest cover loss: >80%
- Cascading effects on global climate

**Factor modifications during aftermath**:
- F_CLIM: +0.80 for 50 years
- F_FOOD: +0.50 for 20 years
- F_LAM: +0.50 for 20 years

**Cascade effects**:
- PERMAFROST_METHANE_RELEASE: +0.5%/year probability
- AMOC_WEAKENING: +0.2%/year probability (altered Atlantic circulation)

*The aftermath factor modifications are not part of the v0.1 impact schema (factor loadings are static per event); they are retained here as specification intent for a later schema version.*

### Branch Calibration Rationale

Distribution based on process model outputs and spatial heterogeneity:
- Partial (0.45): Eastern/southern Amazon is most vulnerable. Western Amazon is wetter, less deforested, may persist. Partial dieback is modal outcome.
- Major (0.40): If tipping dynamics are strong, feedback loops may propagate beyond initially vulnerable areas.
- Catastrophic (0.15): Requires very strong positive feedbacks OR coincidence with severe drought during transition. Tail risk.

---

## Impact Vector

### Global Impacts

Original specification (partial-dieback baseline):

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `amazon_forest_cover` | ↓ | -45% ± 10% | gradual(30yr) | permanent |
| `global_co2_ppm` | ↑ | +15-25 ppm | gradual(50yr) | permanent |
| `global_temp_anomaly` | ↑ | +0.1-0.2°C | gradual(50yr) | permanent |

*Scale by impact_multiplier for major (2.0×) and catastrophic (4.0×) branches*

### Regional Impacts (Brazil and South America)

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `bra.gdp_growth` | ↓ | -1.0 ± 0.5 pp | gradual(10yr) | permanent |
| `bra.agricultural_climate_risk` | ↑ | +30 ± 10 | gradual(10yr) | permanent |
| `bra.water_stress` | ↑ | +20 ± 8 | gradual(15yr) | permanent |

**Note**: Many intuitive impacts (biodiversity loss, ecosystem service collapse, specific rainfall changes) are not tracked in the v1.0 state model. The impacts above capture what can be expressed through available variables. The carbon/temperature effects are the primary global transmission mechanism.

```yaml
impacts:
  partial:
    # Global climate state
    - {var: amazon_forest_cover,         mag: [-45, 10],    onset: {gradual: 30}, permanent: true}
    - {var: global_co2_ppm,              mag: [20, 5],      onset: {gradual: 50}, permanent: true}
    - {var: global_temp_anomaly,         mag: [0.15, 0.05], onset: {gradual: 50}, permanent: true}

    # Brazil
    - {var: bra.gdp_growth,              mag: [-1.0, 0.5],  onset: {gradual: 10}, permanent: true}
    - {var: bra.agricultural_climate_risk, mag: [30, 10],   onset: {gradual: 10}, permanent: true}
    - {var: bra.water_stress,            mag: [20, 8],      onset: {gradual: 15}, permanent: true}

  major:
    # 2.0x baseline, except forest cover, which takes the branch description's 50-70% loss
    - {var: amazon_forest_cover,         mag: [-60, 10],    onset: {gradual: 30}, permanent: true}
    - {var: global_co2_ppm,              mag: [40, 10],     onset: {gradual: 50}, permanent: true}
    - {var: global_temp_anomaly,         mag: [0.30, 0.10], onset: {gradual: 50}, permanent: true}
    - {var: bra.gdp_growth,              mag: [-2.0, 1.0],  onset: {gradual: 10}, permanent: true}
    - {var: bra.agricultural_climate_risk, mag: [60, 20],   onset: {gradual: 10}, permanent: true}
    - {var: bra.water_stress,            mag: [40, 16],     onset: {gradual: 15}, permanent: true}

  catastrophic:
    # 4.0x baseline, except forest cover, which takes the branch description's >80% loss
    - {var: amazon_forest_cover,         mag: [-85, 8],     onset: {gradual: 30}, permanent: true}
    - {var: global_co2_ppm,              mag: [80, 20],     onset: {gradual: 50}, permanent: true}
    - {var: global_temp_anomaly,         mag: [0.60, 0.20], onset: {gradual: 50}, permanent: true}
    - {var: bra.gdp_growth,              mag: [-4.0, 2.0],  onset: {gradual: 10}, permanent: true}
    - {var: bra.agricultural_climate_risk, mag: [120, 40],  onset: {gradual: 10}, permanent: true}
    - {var: bra.water_stress,            mag: [80, 32],     onset: {gradual: 15}, permanent: true}
```

*Units: every row is additive in the variable's units (`amazon_forest_cover` in percentage points of the 2000 baseline, `global_co2_ppm` in ppm, `global_temp_anomaly` in °C, `bra.gdp_growth` in percentage points per year, the two Brazil indices on their 0-100 scales); no `gdp_real` rows. The `major` and `catastrophic` lists are written out rather than inherited because a uniform 2.0×/4.0× scale would take the forest-cover row to −90 and −180 points, beyond the variable's range; the forest-cover rows therefore use the branch descriptions' own 50-70% and >80% loss figures, and the other rows carry the stated multipliers. Ranges in the original tables (+15-25 ppm, +0.1-0.2°C) are written as mean ± half-range.*

### Durability Specifications

| Impact Type | Durability | Rationale |
|-------------|------------|-----------|
| Forest cover loss | permanent | Recovery requires centuries; hysteresis prevents return |
| Carbon release | permanent | CO2 persists in atmosphere for centuries |
| Temperature increase | permanent | Follows from carbon release |
| Regional climate shift | permanent | Determined by land surface, not policy |

### Impact Derivation

Primary method: **Process model synthesis**

| Source | Carbon Release | Forest Loss | Notes |
|--------|---------------|-------------|-------|
| Nobre et al. 2016 | 50-70 Gt C | 50-70% | High-emission scenario |
| Lovejoy & Nobre 2018 | 30-50 Gt C | 40-60% | Threshold focus |
| IPCC AR6 WG1 | 20-80 Gt C | Variable | Wide uncertainty range |
| Cox et al. 2004 | 80+ Gt C | Near-complete | Early model, high sensitivity |

Central estimates based on Lovejoy & Nobre synthesis; uncertainty reflects model spread.

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - {event: PERMAFROST_METHANE_RELEASE, delta: 0.003, years: 50, if: "branch == 'major'"}
    - {event: PERMAFROST_METHANE_RELEASE, delta: 0.005, years: 50, if: "branch == 'catastrophic'"}
    - {event: AMOC_WEAKENING,             delta: 0.002, years: 50, if: "branch == 'catastrophic'"}
  triggered_by:
    - {event: PERMAFROST_METHANE_RELEASE, delta: 0.003}
    - {event: AMOC_WEAKENING}  # direction uncertain (±); no delta assigned
```

*"Permanent" cascade durations are written as 50 years, the full simulation horizon from firing. The partial-dieback branch carries no cascade, per the branch specifications above.*

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| PERMAFROST_METHANE_RELEASE | +0.3-0.5%/year | Permanent | Warming acceleration from carbon release (+0.1-0.2°C) |
| AMOC_WEAKENING | +0.1-0.2%/year | Permanent | Altered atmospheric circulation; minor coupling |

### Triggered By

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| AMOC_WEAKENING | Mixed (±) | Changed Atlantic circulation may alter Amazon rainfall; direction uncertain |
| PERMAFROST_METHANE_RELEASE | +0.3%/year | Accelerated warming increases drought stress |

---

## Early Warning Indicators

Scientific monitoring provides potential early warning:

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| Cumulative deforestation | ~17-20% | >20% is danger zone |
| Dry season lengthening | Detected in eastern Amazon | Continued trend is warning |
| Forest mortality rate | Elevated after droughts | Sustained elevation is warning |
| Fire penetration | Increasing in intact forest | Fire in wet forest is warning |
| Regional rainfall | Declining in east/south | <threshold for forest persistence |

---

## Historical Analogues

No direct analog for Amazon-scale dieback. Partial analogs:

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| Sahara greening→desert (5-6 kya) | Vegetation-rainfall feedback caused rapid transition | Threshold transitions can be fast once initiated |
| 2005/2010/2015 Amazon droughts | Forest mortality spikes; partial recovery | System is stressed; recovery may fail |
| Borneo/Indonesian deforestation | Regional dieback, fire feedback | Fire can cascade in degraded tropical forest |

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

### Upgrade Rationale

Rich scientific literature; Level 2 could add Amazon-specific tracking (regional temperature, drought indices, fire data). Critical review complete 2025-12-30.

## Sources

*Level 1 specification based on general knowledge. Key references:*

- Lovejoy & Nobre 2018, Science Advances (tipping point threshold)
- Nobre et al. 2016 PNAS (Amazon dieback scenarios)
- IPCC AR6 WG1 Chapter 5 (carbon cycle feedbacks)
- Boulton et al. 2022 Nature Climate Change (resilience loss evidence)

## Open Questions

1. **Threshold precision**: Is it 20% or 25% deforestation? Enormous policy relevance
2. **Governance trajectory**: Will Brazilian deforestation policy remain improved or revert?
3. **CO2 fertilization**: How much does elevated CO2 offset drought stress?
4. **Fire feedback strength**: How quickly can fire penetrate degraded forest?
5. **Western Amazon resilience**: Will it serve as refugium or also collapse?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-18 | Initial Level 1 specification | Task 2.1.4 - Type 2 climate tipping point |
| 2025-12-30 | Critical review complete | Task 2.4.6 - Added Case Against, Probability Evolution; fixed variable references to catalog |
| 2025-12-30 | Variance allocation: scaled loadings | Task 3.11 - Factor-explained variance reduced to Type 2 target (0.65); scale factor 0.77 |
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.2. Classification, pressure, threshold, factor, branch, impact, cascade and research tables converted to YAML; all prose kept, original tables kept where they carry rationale or magnitudes the YAML re-expresses. Judgment calls: (1) `inverse_threshold(80)` realized as a clipped ramp zero at 95% cover and saturating at 75%; at the catalog's 2025 baselines (with Brazil agriculture share 5, protest ~30) the expression gives ~37 and at the prose's 82% cover ~43, so the prose's "~58" is a judgment estimate, not the expression's value — threshold, std and sharpness unchanged; the compiler's baseline check is skipped because the two `bra.*` terms have no catalog baseline. (2) `range` set to [0.002, 0.080] from the floor and the "5-8% at high pressure" row. (3) `major` and `catastrophic` impacts written as explicit lists instead of `inherit`/`scale` 2.0/4.0: a uniform scale takes `amazon_forest_cover` to −90/−180 points, so those rows use the branch descriptions' 50-70% and >80% losses; all other rows carry the stated multipliers (the catastrophic `bra.agricultural_climate_risk` +120 and `bra.water_stress` +80 rows exceed 0-100 headroom and are left as the prose states, flagged for review). (4) Range magnitudes written as mean ± half-range (+15-25 ppm → [20, 5]; +0.1-0.2°C → [0.15, 0.05]). (5) "Permanent" cascade durations written as `years: 50`; branch-conditional cascades via `if: "branch == '…'"`; both targets exist as files (no aliases, no backlog-registry IDs involved); AMOC `triggered_by` entry carries no delta (direction uncertain). (6) Aftermath factor modifications (F_CLIM/F_FOOD/F_LAM boosts) have no v0.1 schema form; kept in prose. (7) No durability substitutions (all rows permanent), no `until: resolved` rows so no `resolves_after`, no unit conversions, no dropped rows, no catalog gaps. Restored from history (061d516): the original 2025-12-18 loadings (F_CLIM 0.70, F_FOOD 0.45, F_LAM 0.20, F_FIN 0.15, F_GPT 0.10) and their sum-of-squares line (0.76), plus the missing 2025-12-30 variance-allocation changelog row |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[methodology/reference/state-variables-global]] for global variables | [[methodology/reference/state-variables-country]] for country variables*
