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
- irreversible
- level-1
---

---
title: amoc-weakening
type: note
permalink: events/climate/amoc-weakening
tags:
- event
- climate
- deprecated
---

# ⚠️ SUPERSEDED

**This event specification has been superseded by [[events/climate/amoc-weakening-v2]].**

The v2 specification adds:
- Causal type classification (Type 2: Threshold)
- Pressure function specification
- Impact vectors with durability types
- Cascade effects documentation

---

# AMOC Significant Weakening

## Event Overview

| Field | Value |
|-------|-------|
| **ID** | AMOC_WEAKENING |
| **Scale** | Global |
| **Domain** | Environmental |
| **Onset Speed** | Gradual (5-20 years for full effects) |
| **Reversibility** | Irreversible (centuries to recover) |

## Description

Significant weakening or collapse of the Atlantic Meridional Overturning Circulation—the system of ocean currents that transports warm water northward, giving Northwestern Europe its anomalously mild climate. Event defined as AMOC strength falling below 50% of 20th century baseline, triggering major climate reorganization.

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 1.0% |
| **Low bound** | 0.5% |
| **High bound** | 2.0% |
| **Confidence** | Low |
| **50-year cumulative** | ~40% at point estimate |

### Derivation

From scientific literature:
- IPCC AR6: Low confidence, but non-negligible risk
- Ditlevsen & Ditlevsen 2023: Tipping point potentially as early as 2025-2095 (wide uncertainty)
- Expert elicitation studies: 10-40% this century

Conversion approach:
- Used 15-35% probability over 75 years (2025-2100) as central range
- This implies ~0.2-0.6% annual hazard rate if constant
- Adjusted upward to 1.0% for 2025-2075 window because:
  - If tipping point exists, more likely in earlier window as Greenland melt accelerates
  - Recent research suggests models systematically underestimate risk
  - Precautionary weighting toward higher estimates

### Key Uncertainties

- **Threshold location**: How close is the system to tipping?
- **Greenland melt rate**: Primary freshwater forcing
- **Deep water formation sensitivity**: How much freshwater triggers collapse?
- **Model structural uncertainty**: Models may miss critical dynamics
- **Emissions trajectory**: Affects forcing rate

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| [[f-clim]] | 0.85 | This IS a climate system event |
| [[f-food]] | 0.20 | Affects fisheries, European agriculture (weak feedback) |
| [[f-eur]] | 0.15 | European emissions policy has marginal effect |
| [[f-ssa]] | 0.10 | Affects Sahel rainfall patterns |
| [[f-lam]] | 0.05 | Amazon affects Atlantic circulation |
| [[f-fin]] | 0.00 | Financial system doesn't affect ocean circulation |
| [[f-hlth]] | 0.00 | No mechanism |
| [[f-gpt]] | 0.00 | Great power politics doesn't affect physics |
| [[f-tech]] | 0.00 | No mechanism |
| [[f-mena]] | 0.00 | No significant linkage |
| [[f-sas]] | 0.00 | No significant linkage |
| [[f-eas]] | 0.00 | No significant linkage |

**Sum of squared loadings**: 0.80 ✓ (under 1.0 constraint)

### Loading Rationale

Single-factor dominant structure:
- F_CLIM is overwhelmingly dominant (0.85) because AMOC weakening is essentially a manifestation of climate system stress
- Other loadings are weak and represent minor feedbacks or affected systems, not drivers
- Human political/economic systems have almost no short-term influence on whether this occurs

## Impacts

### Economic

| Variable | Mean | Std | Distribution |
|----------|------|-----|--------------|
| Global GDP | -2.5% | 1.5% | Normal |
| European GDP | -12% | 5% | Normal |
| UK GDP | -15% | 6% | Normal |
| Germany GDP | -12% | 5% | Normal |
| France GDP | -10% | 4% | Normal |

### Climate

| Variable | Mean | Std | Distribution |
|----------|------|-----|--------------|
| NW Europe temperature | -5°C | 2°C | Normal |
| European precipitation | -20% | 10% | Normal |
| Sahel rainfall change | ±15% | 10% | Normal (direction uncertain) |

### Humanitarian

| Variable | Mean | Std | Distribution |
|----------|------|-----|--------------|
| Displacement | 5M | 3M | Log-normal |
| Excess mortality | 0.5M | 0.3M | Log-normal |

### Other

| Variable | Mean | Std | Distribution |
|----------|------|-----|--------------|
| Food stocks (global) | -10% | 5% | Normal |
| European agriculture output | -30% | 15% | Normal |

**Duration**: 999 years (effectively permanent; recovery takes centuries)

### Impact Derivation

Economic impacts:
- European GDP -12%: Major but not catastrophic; wealthy region with adaptive capacity
- Lower than naive climate damage estimates because Europe can adapt (heating, trade, agricultural shift)
- Global GDP -2.5%: European share of world economy plus spillovers

Humanitarian impacts relatively low despite massive climate shift:
- Northwestern Europe is wealthy with strong institutions
- Deaths from cold, food disruption, but systems adapt
- Displacement modest: people adjust within Europe, not mass exodus
- Contrast with [[pakistan-state-failure]]: 10x smaller displacement despite much larger economic impact

## Transmission Channels

### Direct Climate Effects

Primary affected region: Northwestern Europe (UK, Ireland, France, Germany, Netherlands, Belgium, Scandinavia)
- Temperature decline: 3-8°C below current (partially offsets greenhouse warming)
- Precipitation changes: Generally drier
- Growing season shortening
- Storm track changes

### Agricultural Shock

European agriculture severely disrupted:
- Northern Europe loses current climatic advantage
- Growing seasons shorten
- Crop failures during transition period
- Wine regions shift or disappear
- Fisheries collapse (North Atlantic ecosystem disruption)

Estimated European agricultural output: -20% to -40%

### Economic Spillover

European recession affects global economy through:
- Trade disruption (Europe is major trading bloc)
- Financial market contagion
- Supply chain reorganization
- Reduced European consumption

### Sahel Rainfall (Uncertain)

AMOC affects Atlantic tropical rainfall patterns. Sahel could see:
- Increased rainfall (some models)
- Decreased rainfall (other models)
- Increased variability (most likely)

This creates potential compound risk with [[f-ssa]] events.

### Energy System

- Heating demand increases dramatically in Northwestern Europe
- Existing infrastructure designed for milder climate
- Natural gas demand spike
- Renewable energy output may change (wind patterns, solar irradiance)

## Causal Relationships

### Caused By (Increases Probability)

| Event | Mechanism |
|-------|-----------|
| Greenland Ice Sheet Acceleration | Freshwater forcing |
| Arctic Warming Extreme | Accelerates ice melt |
| Amazon Tipping Point | Affects Atlantic circulation patterns |

Note: These are all climate events. Human political/economic events have minimal effect on AMOC probability on policy-relevant timescales.

### Causes (Increased Probability If This Occurs)

| Event | Mechanism |
|-------|-----------|
| European Economic Crisis | Direct climate shock to major economy |
| European Political Crisis | Economic stress creates political instability |
| Global Food Price Spike | European agricultural collapse affects global supply |
| Sahel Catastrophe | Potential rainfall disruption (uncertain direction) |
| Energy Crisis (European) | Heating demand spike |

## Comparison: AMOC vs. Geopolitical Events

| Dimension | AMOC | Pakistan State Failure |
|-----------|------|----------------------|
| Scale | Global | National |
| Onset | Gradual (5-20 years) | Rapid (1-3 years) |
| Reversibility | Irreversible | Partial |
| Factor structure | Single-factor dominant | Multi-factor |
| Primary impact | Economic | Humanitarian |
| Global GDP | -2.5% | -0.3% |
| Displacement | 5M | 30M |
| Mortality | 0.5M | 6M |
| Human agency | Minimal | Significant |

Key insight: AMOC is larger economic impact but smaller humanitarian impact because it affects wealthy, adaptive regions. Pakistan is smaller economic impact but larger humanitarian impact because it affects poor, fragile region.

## References

- [[21st-century-assessment]] Europe section, AMOC discussion
- [[f-clim]] (factor definition)
- IPCC AR6 Chapter 9 (Ocean, Cryosphere, and Sea Level Change)
- Ditlevsen & Ditlevsen 2023, Nature Communications