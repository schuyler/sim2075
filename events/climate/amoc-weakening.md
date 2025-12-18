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

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | AMOC_WEAKENING |
| **Scale** | Global |
| **Domain** | Environmental |
| **Causal Type** | **Type 2: Threshold/Accumulation** |
| **Onset Speed** | Gradual (5-20 years for full effects) |
| **Reversibility** | Irreversible (centuries to recover) |

## Description

Significant weakening or collapse of the Atlantic Meridional Overturning Circulation—the system of ocean currents that transports warm water northward, giving Northwestern Europe its anomalously mild climate. Event defined as `amoc_strength` falling below 50% of 20th century baseline, triggering major climate reorganization.

This is a **state transition**: the system shifts from "stable circulation" regime to "weakened/collapsed" regime.

---

## Causal Type Specification (Type 2: Threshold)

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `global_temp_anomaly` | 0.50 | linear | Primary driver of Greenland melt |
| `arctic_ice_extent` | 0.25 | inverse | Lower ice → more freshwater input |
| `amoc_strength` | 0.25 | inverse | Self-reinforcing: weaker AMOC → more vulnerable |

**Pressure calculation**:
```
pressure = 0.50 × (temp_anomaly / 2.0) + 0.25 × (1 - arctic_ice/baseline) + 0.25 × (1 - amoc_strength/baseline)
```
*Normalized to 0-100 scale*

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 65 (on 0-100 pressure scale) |
| **Uncertainty** | ±15 (reflects deep uncertainty about tipping point) |
| **Sharpness (k)** | 0.15 (moderate; not knife-edge threshold) |
| **Historical calibration** | Paleoclimate records of abrupt AMOC transitions |

### Minimum Probability

**Floor**: 0.2%/year even at low pressure (acknowledges irreducible uncertainty about threshold location)

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.0% |
| **Low bound** | 0.5% |
| **High bound** | 2.0% |
| **Confidence** | Low |
| **50-year cumulative** | ~40% at point estimate |

### Derivation

From scientific literature:
- IPCC AR6: Low confidence, but non-negligible risk
- Ditlevsen & Ditlevsen 2023: Tipping point potentially as early as 2025-2095
- Expert elicitation studies: 10-40% this century

Current pressure estimate: ~45/100 (below threshold but accumulating)
- Global temp anomaly: ~1.3°C (rising ~0.03°C/year)
- Arctic ice: ~75% of baseline (declining)
- AMOC strength: ~95% (early weakening signal)

Probability rises over simulation horizon as pressure accumulates.

### Key Uncertainties

- **Threshold location**: Deep uncertainty; could be much closer or further than estimated
- **Greenland melt rate**: Accelerating faster than models predicted
- **Model structural uncertainty**: Climate models may miss critical dynamics
- **Feedback strength**: Self-reinforcing dynamics uncertain

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| [[f-clim]] | 0.85 | This IS a climate system event; factors shock `global_temp_anomaly` |
| [[f-food]] | 0.20 | Via agricultural impacts that feed back to policy (weak) |
| [[f-eur]] | 0.15 | European emissions policy marginally affects forcing rate |
| [[f-ssa]] | 0.10 | Sahel rainfall affected; minor feedback |
| [[f-lam]] | 0.05 | Amazon affects Atlantic circulation patterns |
| All others | 0.00 | No mechanism |

**Sum of squared loadings**: 0.80 ✓

### Loading Interpretation (per Integrated Framework)

Factors shock state variables that feed into pressure function:
- High F_CLIM → `global_temp_anomaly` increases faster → pressure accumulates faster → P(AMOC collapse) rises
- This is the Type 2 factor→state→pressure→probability pathway

---

## Impact Vector

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `global_temp_regional` (NW Europe) | ↓ | -5°C ± 2°C | gradual(10) | permanent |
| `global_gdp` | ↓ | -2.5% ± 1.5% | gradual(15) | decaying (half_life: 20yr, floor: -1%) |
| `food_stocks_grains` | ↓ | -10% ± 5% | gradual(5) | decaying (half_life: 10yr) |

### European Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `gdp_real` (UK, Germany, France, Netherlands) | ↓ | -12% ± 5% | gradual(15) | decaying (half_life: 25yr, floor: -5%) |
| `agricultural_output` | ↓ | -30% ± 15% | gradual(10) | permanent (new climate baseline) |
| `energy_demand` | ↑ | +25% ± 10% | gradual(10) | permanent |
| `displacement` | ↑ | 5M ± 3M | gradual(15) | decaying (half_life: 30yr) |

### Humanitarian Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `excess_mortality` | ↑ | 0.5M ± 0.3M | gradual(20) | permanent (deaths don't reverse) |

### Sahel Impacts (Uncertain)

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `precipitation` | ? | ±15% ± 10% | gradual(10) | permanent |

*Direction uncertain: models disagree on whether Sahel gets wetter or drier*

### Durability Rationale

- **Climate changes**: Permanent—new equilibrium state
- **GDP impacts**: Decaying with long half-life—economies adapt but never fully recover to prior trajectory
- **Agricultural shifts**: Permanent—represents new climate-determined baseline
- **Deaths**: Permanent by definition

---

## Differential Impacts

**Exposure variable**: Geographic latitude and Atlantic proximity

| Country Group | GDP Impact Multiplier | Rationale |
|---------------|----------------------|-----------|
| NW Europe (UK, Ireland, Netherlands, Belgium) | 1.5× | Most exposed |
| Central Europe (Germany, France) | 1.0× | Moderate exposure |
| Southern Europe | 0.5× | May partially benefit (less warming offset) |
| Rest of world | 0.3× | Trade/spillover effects only |

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Temperature shift → European agriculture collapse | EU_FISCAL_CRISIS | +2%/year | 20 years | Agricultural losses strain budgets |
| European recession → financial contagion | GLOBAL_FINANCIAL_CRISIS | +1%/year | 10 years | European banking exposure |
| Sahel rainfall change → food insecurity | SAHEL_CATASTROPHE | ±1.5%/year | Permanent | Monsoon disruption |

### Impact Chains

**Pathway 1**: AMOC → European agriculture → food prices → MENA import pressure
```
Event → Europe ag output -30% → global wheat supply -5% → MENA food stress ↑ → P(MENA instability) ↑
```

**Pathway 2**: AMOC → European economy → global demand
```
Event → Europe GDP -12% → global trade -3% → EM export stress → P(EM financial crisis) ↑
```

---

## Transmission Channels

### Direct Climate Effects

**Affected region**: Northwestern Europe (UK, Ireland, France, Germany, Netherlands, Scandinavia)
- Temperature: 3-8°C cooling (partially offsets greenhouse warming)
- Precipitation: Generally drier
- Growing season: 30-60 days shorter
- Storm tracks: Shift southward

### Agricultural Shock

European agriculture severely disrupted:
- Northern Europe loses climatic advantage
- Wine regions eliminated or shifted
- Crop calendars fundamentally altered
- North Atlantic fisheries collapse

### Energy System

- Heating demand +25% in NW Europe
- Existing infrastructure designed for milder climate
- Natural gas demand spike
- Renewable output changes (wind patterns shift)

### Financial Spillover

- European recession → global financial contagion
- Insurance losses from infrastructure damage
- Stranded assets (agricultural land, coastal infrastructure)

---

## Comparison to Geopolitical Events

| Dimension | AMOC Weakening | Pakistan State Failure |
|-----------|----------------|----------------------|
| Causal Type | Type 2 (threshold) | Type 2 (threshold) |
| Human agency | Minimal (physics-driven) | Significant (policy-responsive) |
| Global GDP | -2.5% | -0.3% |
| Displacement | 5M | 30M |
| Mortality | 0.5M | 6M |
| Primary victims | Wealthy, adaptive populations | Poor, vulnerable populations |

**Key insight**: AMOC has larger economic impact but smaller humanitarian impact because it affects wealthy regions with adaptive capacity.

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-17 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Threshold location is load-bearing uncertainty; recent research suggests tipping may be closer than IPCC estimates |

## Sources

- [[21st-century-assessment]] Europe section
- IPCC AR6 Chapter 9
- Ditlevsen & Ditlevsen 2023, Nature Communications
- Paleoclimate literature on D-O events

## Open Questions

- How close is actual threshold? Range of 1.5-3.5°C in literature
- Will early warning signals provide advance notice?
- How does AMOC interact with other tipping elements (cascading)?
- What is realistic European adaptation capacity?