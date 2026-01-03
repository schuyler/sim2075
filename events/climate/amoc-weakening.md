---
title: amoc-weakening
type: note
permalink: events/climate/amoc-weakening
tags:
- event
- climate
- tipping-point
- amoc
- europe
- type-2
- threshold
- irreversible
- level-1
---

# AMOC Significant Weakening

**Type 2 (Threshold) Event** — Probability rises as climate pressure accumulates toward tipping point.

---

## Description

Significant weakening or collapse of the Atlantic Meridional Overturning Circulation — the system of ocean currents that transports warm water northward, giving Northwestern Europe its anomalously mild climate. Event defined as `amoc_strength` falling below 50% of 20th century baseline, triggering major climate reorganization.

This is a **state transition**: the system shifts from "stable circulation" regime to "weakened/collapsed" regime.

---

## Specification

```yaml
id: AMOC_WEAKENING
domain: environmental
scale: global
causal_type: 2
onset: gradual
reversibility: irreversible
```

---

## Probability

```yaml
probability:
  pressure: |
    0.50 * (global_temp_anomaly / 2.0) +
    0.25 * (1.0 - arctic_sea_ice_sept / 4.5) +
    0.25 * (1.0 - amoc_strength / 95)
  threshold: 65
  threshold_std: 15
  sharpness: 0.15
  floor: 0.002
  annual: 0.010
  range: [0.005, 0.020]
  confidence: low
```

### Current Pressure Estimate

- `global_temp_anomaly`: ~1.3°C (rising ~0.03°C/year)
- `arctic_sea_ice_sept`: ~4.5 M km² (declining)
- `amoc_strength`: ~95% of baseline (early weakening signal)
- **Current pressure**: ~45/100 (below threshold but accumulating)

### Probability Evolution

| Global Temp | Est. Pressure | Annual P |
|-------------|---------------|----------|
| 1.3°C (current) | ~45 | 1.0% |
| 1.5°C | ~52 | 1.5% |
| 2.0°C | ~65 | 3.0% |
| 2.5°C | ~78 | 5.0% |

### Case Against

**Threshold may be much further than estimated**: If true threshold is at 2.5-3.5°C rather than near current levels, probability should be <0.3%/year for coming decades. The Ditlevsen paper suggesting early tipping has been contested.

**Process may be gradual, not abrupt**: Some models show AMOC declining over centuries without a tipping point. If so, this belongs in baseline dynamics, not event catalog.

**Impact magnitudes may be overstated**: European economies are wealthy and adaptive. The -12% GDP may underestimate recovery capacity.

### Key Uncertainties

- Threshold location (deep uncertainty; could be much closer or further)
- Greenland melt rate (accelerating faster than models predicted)
- Model structural uncertainty (climate models may miss critical dynamics)
- Feedback strength (self-reinforcing dynamics uncertain)

---

## Factor Loadings

```yaml
factors:
  F_CLIM: 0.67  # This IS a climate system event
  F_FOOD: 0.16  # Agricultural impacts feed back to policy (weak)
  F_EUR: 0.12   # European emissions policy marginally affects forcing rate
  F_SSA: 0.08   # Sahel rainfall affected; minor feedback
  F_LAM: 0.04   # Amazon affects Atlantic circulation patterns
variance: 0.65  # Type 2 target
```

---

## Impacts

### Transmission Channels

**Direct Climate**: Northwestern Europe cools 3-8°C relative to global trend (partially offsetting greenhouse warming). Growing seasons shorten 30-60 days. Storm tracks shift southward. These physical changes transmit to observable economic and demographic variables.

**Agricultural**: Northern Europe loses climatic advantage. Captured via shift in `gdp_share_agriculture` and GDP impacts.

**Energy**: Heating demand rises ~25% in NW Europe. Captured via increased `energy_import_dependence`.

**Displacement**: Climate-driven internal migration within Europe. Modeled via `idp_population`.

**Mortality**: Cold exposure and disruption cause excess deaths. Modeled via `life_expectancy` depression.

```yaml
impacts:
  default:
    # Global climate state
    - {var: amoc_strength,              mag: [-45, 10],     onset: {gradual: 5}, permanent: true}
    
    # NW Europe - most exposed (UK, Netherlands)
    - {var: gbr.gdp_real,               mag: [-0.15, 0.06], onset: {gradual: 15}, decay: 25}
    - {var: gbr.gdp_share_agriculture,  mag: [-0.02, 0.01], onset: {gradual: 10}, permanent: true}
    - {var: gbr.energy_import_dependence, mag: [0.15, 0.05], onset: {gradual: 10}, permanent: true}
    - {var: gbr.life_expectancy,        mag: [-1.5, 0.5],   onset: {gradual: 20}, decay: 30}
    - {var: gbr.idp_population,         mag: [0.5, 0.3],    onset: {gradual: 15}, decay: 25}
    
    - {var: nld.gdp_real,               mag: [-0.15, 0.06], onset: {gradual: 15}, decay: 25}
    - {var: nld.gdp_share_agriculture,  mag: [-0.03, 0.01], onset: {gradual: 10}, permanent: true}
    - {var: nld.energy_import_dependence, mag: [0.15, 0.05], onset: {gradual: 10}, permanent: true}
    - {var: nld.life_expectancy,        mag: [-1.5, 0.5],   onset: {gradual: 20}, decay: 30}
    
    # Central Europe - moderate exposure (Germany, France)
    - {var: deu.gdp_real,               mag: [-0.10, 0.04], onset: {gradual: 15}, decay: 25}
    - {var: deu.gdp_share_agriculture,  mag: [-0.015, 0.005], onset: {gradual: 10}, permanent: true}
    - {var: deu.energy_import_dependence, mag: [0.10, 0.04], onset: {gradual: 10}, permanent: true}
    - {var: deu.life_expectancy,        mag: [-1.0, 0.4],   onset: {gradual: 20}, decay: 30}
    
    - {var: fra.gdp_real,               mag: [-0.10, 0.04], onset: {gradual: 15}, decay: 25}
    - {var: fra.gdp_share_agriculture,  mag: [-0.02, 0.01], onset: {gradual: 10}, permanent: true}
    - {var: fra.energy_import_dependence, mag: [0.10, 0.04], onset: {gradual: 10}, permanent: true}
    - {var: fra.life_expectancy,        mag: [-1.0, 0.4],   onset: {gradual: 20}, decay: 30}
    
    # Rest of EU aggregate - mixed exposure
    - {var: eu_other.gdp_real,          mag: [-0.06, 0.03], onset: {gradual: 15}, decay: 25}
    
    # Global spillovers
    - {var: global_trade_volume,        mag: [-0.03, 0.015], onset: {gradual: 10}, decay: 15}
    - {var: wheat_price,                mag: [0.20, 0.10],  onset: {gradual: 5}, decay: 10}
```

### Exposure Rationale

| Country Group | GDP Multiplier | Mechanism |
|---------------|----------------|-----------|
| NW Europe (UK, Netherlands) | 1.5× | Direct cooling; North Sea exposure |
| Central Europe (Germany, France) | 1.0× | Moderate cooling; continental buffer |
| Southern Europe | 0.5× | May partially benefit from reduced heat stress |
| Rest of world | 0.3× | Trade/spillover only |

### Mortality Note

Excess deaths arise from cold exposure, agricultural disruption, and economic stress. Modeled via temporary depression of `life_expectancy` in affected countries. Cumulative mortality impact is computed as an output by comparing population trajectories to baseline.

---

## Cascades

```yaml
cascades:
  triggers:
    - {event: EU_FRAGMENTATION,         delta: 0.020, years: 20}
    - {event: GLOBAL_FINANCIAL_CRISIS,  delta: 0.010, years: 10}
  triggered_by: []  # Type 2 event driven by physical accumulation
```

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-01-02
  review: complete
  upgrade: true
```

### Upgrade Rationale

- Threshold location is load-bearing uncertainty
- Recent research suggests tipping may be closer than IPCC estimates
- Country-specific impact calibration needs refinement

## Open Questions

1. How close is actual threshold? Range of 1.5-3.5°C in literature.
2. Will early warning signals provide advance notice?
3. How does AMOC interact with other tipping elements (cascading)?
4. What is realistic European adaptation capacity?
5. Sahel precipitation effects — direction uncertain in models.

---

## Changelog

| Date | Change |
|------|--------|
| 2025-12-17 | Initial Level 1 specification |
| 2025-12-30 | Variance allocation: scaled loadings to Type 2 target |
| 2025-12-30 | Critical review complete |
| 2025-01-01 | Migrated to YAML-embedded schema |
| 2025-01-02 | Revised impacts to use only observable state variables |

---

*See [[methodology/reference/causal-types]] for Type 2 definition | [[research/21st-century-assessment]] for climate context*
