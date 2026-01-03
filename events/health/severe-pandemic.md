---
title: severe-pandemic
type: note
permalink: events/health/severe-pandemic
tags:
- event
- type-1
- stochastic
- health
- pandemic
- global
- level-1
---

# Severe Pandemic

**Type 1 (Stochastic) Event** — Base rate from historical frequency; timing unpredictable; factor loadings modify annual probability.

---

## Description

Global pandemic causing ≥1 million excess deaths within first 24 months AND/OR ≥3% global GDP contraction. This threshold distinguishes "severe" pandemics from endemic disease burden and minor outbreaks.

**What marks occurrence**: WHO declares Public Health Emergency of International Concern (PHEIC) AND early epidemiological data indicates trajectory toward severity threshold.

---

## Specification

```yaml
id: SEVERE_PANDEMIC
domain: health
scale: global
causal_type: 1
onset: sudden
reversibility: partial
```

---

## Probability

```yaml
probability:
  annual: 0.020
  range: [0.015, 0.030]
  confidence: medium-high
```

### Base Rate Derivation

**Reference class**: Global pandemics meeting severity threshold (≥1M deaths or ≥3% GDP impact)

| Year | Event | Deaths | Included? |
|------|-------|--------|-----------|
| 1918-19 | Spanish Flu | 50-100M | ✓ |
| 1957-58 | Asian Flu | 1-2M | ✓ (borderline) |
| 1968-69 | Hong Kong Flu | 1-4M | ✓ (borderline) |
| 2009-10 | H1N1 Swine Flu | 150-575K | ✗ (below threshold) |
| 2020-22 | COVID-19 | 15-25M | ✓ |

**Calculation**: 3 events / 124 years ≈ 2.4%/year → rounded to 2.0%

### Condition Adjustments

| Condition | Adjustment | Rationale |
|-----------|------------|-----------|
| Increased zoonotic interface | +0.3% | Agricultural intensification, habitat encroachment |
| Global connectivity | +0.2% | Faster spread means more pandemics reach threshold |
| Surveillance capacity | -0.2% | Earlier detection enables containment |
| Vaccine platform technology | -0.3% | mRNA platforms reduce time-to-vaccine |
| Antimicrobial resistance | +0.2% | Secondary infections harder to treat |

**Net adjustment**: Roughly offsetting; retain ~2%/year

### Probability Evolution

| Period | Annual P | Rationale |
|--------|----------|-----------|
| 2025-2035 | ~1.8% | Post-COVID preparedness may slightly reduce |
| 2035-2050 | ~2.0% | Preparedness decays; ecological disruption continues |
| 2050-2075 | ~2.2% | Possible slight increase from climate-driven ecological change |

### Case Against

**COVID-19 was an outlier, not a new baseline**: The 2020-22 pandemic may have been a "100-year event." True base rate for 1M+ death pandemics may be closer to 1%/year.

*Counter*: COVID-19 confirms conditions for severe pandemics exist. Increased connectivity and ecological disruption suggest rate may be increasing.

**Post-COVID preparedness reduces future severity**: Massive investments in pandemic preparedness, surveillance, and vaccine platforms mean future pandemics less likely to reach severity threshold.

*Counter*: Preparedness investment decays without political will. Pattern after 2009 H1N1 was rapid erosion.

**The threshold is arbitrary**: Why 1M deaths? Different thresholds give very different base rates.

*Counter*: The estimate is robust to reasonable variations — whether 2, 3, or 4 events per century, annual rate is 1.5-3%.

---

## Factor Loadings

```yaml
factors:
  F_CLIM: 0.44  # Ecological disruption increases zoonotic spillover
  F_HLTH: 0.40  # Affects outbreak→pandemic escalation
  F_FOOD: 0.35  # Agricultural intensification, wet markets
  F_FIN: 0.18   # Economic stress reduces health investment
  F_GPT: 0.13   # Great power tension impedes cooperation
  F_TECH: 0.04  # Dual-use research risk (marginal)
variance: 0.75  # Type 1 target
```

---

## Branches

```yaml
branches:
  - {id: moderate, p: 0.55, desc: "COVID-19 scale: 1-5M deaths, major disruption"}
  - {id: severe, p: 0.35, desc: "1918 Flu scale: 5-30M deaths, 5-10% GDP"}
  - {id: catastrophic, p: 0.10, desc: "Unprecedented: 30M+ deaths"}
```

---

## Impacts

### Transmission Channels

**Direct Health**: Pathogen causes morbidity and mortality. Modeled via temporary depression of `life_expectancy` and shock to elderly population cohorts. Excess mortality is computed as an output by comparing actual vs. counterfactual population trajectories.

**Economic Disruption**: Containment measures + illness reduce economic activity.

**Fiscal**: Emergency spending increases public debt.

```yaml
impacts:
  moderate:
    # Global
    - {var: pandemic_status,           mag: [3.5, 0.5],    onset: immediate, until: resolved}
    - {var: global_trade_volume,       mag: [-0.08, 0.04], onset: immediate, decay: 1.5}
    - {var: global_credit_spread,      mag: [150, 75],     onset: immediate, decay: 1}
    
    # Country-level (applied to all countries with capacity multiplier)
    - {var: "*.gdp_real",              mag: [-0.04, 0.02], onset: immediate, decay: 2}
    - {var: "*.unemployment_rate",     mag: [0.04, 0.02],  onset: immediate, decay: 1.5}
    - {var: "*.debt_public",           mag: [0.10, 0.05],  onset: {gradual: 2}, permanent: true}
    - {var: "*.life_expectancy",       mag: [-0.5, 0.3],   onset: immediate, decay: 3}

  severe:
    inherit: moderate
    scale: 3.0

  catastrophic:
    inherit: moderate
    scale: 8.0
```

### Differential Exposure

Countries with lower `tax_revenue_gdp` (proxy for state capacity) experience 1.3-1.5× impact multiplier on GDP and unemployment effects. Implementation applies exposure coefficient based on this observable.

### Mortality Modeling Note

Deaths are represented via:
1. Temporary depression of `life_expectancy` (observable, recovers post-pandemic)
2. For catastrophic branch: direct shock to elderly cohorts (`pop_65_79_*`, `pop_80_plus_*`)

Cumulative excess mortality is an *output* computed by comparing population trajectories to no-event baseline — not a state variable.

---

## Cascades

```yaml
cascades:
  triggers:
    - {event: GLOBAL_FINANCIAL_CRISIS, delta: 0.020, years: 3}
    - {event: PAKISTAN_STATE_FAILURE,  delta: 0.005, years: 5}
    - {event: EGYPT_STATE_FAILURE,     delta: 0.005, years: 5}
    - {event: CHINESE_ECONOMIC_CRISIS, delta: 0.008, years: 3}
  triggered_by: []  # Type 1 event is fundamentally stochastic
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

- Emerging pathogen surveillance data
- Gain-of-function risk assessment
- Antimicrobial resistance scenarios

## Open Questions

1. How much does lab research increase catastrophic branch probability?
2. Will mRNA platforms meaningfully reduce future severity?
3. Should AMR pandemic be separate event or branch?
4. How quickly does post-pandemic investment erode?

---

## Changelog

| Date | Change |
|------|--------|
| 2025-12-18 | Initial Level 1 specification |
| 2025-12-30 | Critical review complete |
| 2025-01-01 | Migrated to YAML-embedded schema |
| 2025-01-02 | Fixed variable names; clarified mortality modeling via observables |

---

*See [[methodology/reference/probability-estimation]] for Type 1 methodology*
