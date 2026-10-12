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

This is a **state transition**: `pandemic_status` (global) shifts from 0 to 3-4, triggering acute-phase dynamics across health, economic, and social systems.

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

*Onset speed: rapid (months to peak impact). Reversibility: partial (deaths permanent; economic/social impacts recover).*

---

## Causal Type Specification (Type 1: Stochastic)

### Why Type 1?

Pandemic emergence is fundamentally stochastic at the annual level:
- Zoonotic spillover events are unpredictable
- Which spillovers become pandemics depends on pathogen characteristics that are random
- No clear pressure accumulation—a pandemic could occur any year
- Historical frequency provides the best probability estimate

Not Type 2: No observable pressure variable predicts timing
Not Type 3: No small-N actor decision determines occurrence

---

## Probability

```yaml
probability:
  annual: 0.020
  resolves_after: 3
  range: [0.015, 0.030]
  confidence: medium
```

`resolves_after: 3` — `pandemic_status` stays elevated for three years per firing, counting the firing year: the severity definition counts excess deaths over the first 24 months, and COVID-19's acute phase (PHEIC January 2020 to May 2023) ran about three years.

| Metric | Value |
|--------|-------|
| **Annual probability** | 2.0% |
| **Low bound** | 1.5% |
| **High bound** | 3.0% |
| **Confidence** | Medium-High (recorded as `medium` in YAML: the schema enum is `low|medium|high`) |
| **25-year cumulative** | ~40% at point estimate |

### Base Rate Derivation

**Reference class**: Global pandemics meeting severity threshold (≥1M deaths or ≥3% GDP impact)

| Year | Event | Deaths | GDP Impact | Included? |
|------|-------|--------|------------|-----------|
| 1918-19 | Spanish Flu | 50-100M | ~5% | ✓ |
| 1957-58 | Asian Flu | 1-2M | <1% | ✓ (borderline) |
| 1968-69 | Hong Kong Flu | 1-4M | <1% | ✓ (borderline) |
| 2009-10 | H1N1 Swine Flu | 150-575K | <0.5% | ✗ (below threshold) |
| 2020-22 | COVID-19 | 15-25M | ~3-4% | ✓ |

**Frequency calculation**:
- Observation period: 1900-2024 (124 years)
- Clear severe events: 2 (1918, COVID-19)
- Borderline events: 2 (1957, 1968)
- Estimated severe events: 2.5-3.5 depending on threshold interpretation

**Base rate**: 3 events / 124 years ≈ **2.4%/year** → rounded to 2.0%

### Condition Adjustments

| Condition | Adjustment | Rationale |
|-----------|------------|-----------|
| Increased zoonotic interface | +0.3% | Agricultural intensification, habitat encroachment |
| Global connectivity | +0.2% | Faster spread means more pandemics reach threshold |
| Surveillance capacity | -0.2% | Earlier detection enables containment |
| Vaccine platform technology | -0.3% | mRNA platforms reduce time-to-vaccine |
| Antimicrobial resistance | +0.2% | Secondary infections harder to treat |

**Net adjustment**: Roughly offsetting; retain ~2%/year

### Derivation

1. **Historical frequency**: 2-4 severe pandemics per century
2. **Annualized**: 2-4%/year base rate
3. **Central estimate**: 2.0%/year (emphasizing clear cases)
4. **Adjustment**: Condition adjustments roughly net to zero

### Comparative Ranking

- More likely than: AMOC collapse (~0.5%), state failures (~1-2%)
- Similar to: Global financial crisis (~3%)
- This ranking feels correct—severe pandemics are "once per generation" events.

### Probability Evolution

For Type 1 events, the key question is whether the base rate is stable or trending.

| Period | Annual P | Rationale |
|--------|----------|-----------|
| 2025-2035 | ~1.8% | Post-COVID preparedness may slightly reduce; but also higher vigilance |
| 2035-2050 | ~2.0% | Preparedness decays; ecological disruption continues |
| 2050-2075 | ~2.2% | Possible slight increase from climate-driven ecological change |

The trend is speculative. Treating the rate as stable at 2.0% is defensible given data limitations.

### Case Against

Per [[methodology/03-critical-review]] Q4:

**1. COVID-19 was an outlier, not a new baseline**

The 2020-22 pandemic may have been a "100-year event" that shouldn't shift our base rate estimate. Including it gives excessive weight to a single recent observation. The true base rate for 1M+ death pandemics may be closer to 1%/year (once per century).

*Counter*: COVID-19 confirms that conditions for severe pandemics exist in the modern world. If anything, increased connectivity and ecological disruption suggest the rate may be increasing, not that COVID was anomalous.

**2. Post-COVID preparedness reduces future severity**

Massive investments in pandemic preparedness, surveillance, and vaccine platforms post-COVID mean future pandemics are less likely to reach severity threshold. The 2.0% may be calibrated to a pre-2020 world.

*Counter*: Preparedness investment decays without political will. The pattern after 2009 H1N1 was rapid erosion of preparedness. Also, preparedness helps with known pathogens more than novel ones.

**3. The threshold is arbitrary**

Why 1M deaths? Why 3% GDP? Different thresholds give very different base rates. The 1957 and 1968 flu pandemics are "in" or "out" depending on exactly where you draw the line, which significantly affects the estimate.

*Counter*: Fair point. The threshold is a modeling choice. But the estimate is robust to reasonable variations—whether 2, 3, or 4 events per century, the annual rate is in the 1.5-3% range.

**4. Type 1 may be wrong classification**

Pandemic risk may be increasing over time due to ecological disruption, making this more Type 2 (pressure accumulation) than Type 1 (stable base rate). The "stochastic" framing may miss an important trend.

*Counter*: This could be captured by increasing the base rate over time, but we don't have enough data points to estimate a trend reliably. Treating it as Type 1 with acknowledged uncertainty is more honest than fitting a trend to 4 data points.

### Key Uncertainties

- **Novel pathogen emergence**: Could be higher if gain-of-function research or bioweapons accident
- **Pandemic preparedness**: Post-COVID investments may reduce severity
- **Pathogen characteristics**: High-CFR + high-transmissibility combination is rare but catastrophic
- **Definition sensitivity**: Threshold choice significantly affects base rate

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 1 target (ΛΩΛᵀ)ᵢᵢ = 0.75*

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

The regional factors (F_SAS, F_EAS, F_SSA) carry no loading because regional instability is not emergence risk; F_MENA, F_EUR and F_LAM have no distinct pathway.

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.75 (Type 1 target); scale factor = 0.89 from original loadings.

---

## Branches

```yaml
branches:
  - {id: moderate, p: 0.55, desc: "COVID-19 scale: 1-5M deaths, major disruption"}
  - {id: severe, p: 0.35, desc: "1918 Flu scale: 5-30M deaths, 5-10% GDP"}
  - {id: catastrophic, p: 0.10, desc: "Unprecedented: 30M+ deaths"}
```

### Branch 1: Moderate-Severe (55%)

COVID-19 scale event: 1-5M excess deaths globally over 2 years. Major economic disruption but not civilizational threat. **Impact modifiers**: 1.0× baseline.

### Branch 2: Severe (35%)

1918 Flu scale event: 5-30M excess deaths globally. Severe economic contraction (5-10% global GDP). Healthcare system stress in many regions. **Impact modifiers**: 3.0× baseline.

### Branch 3: Catastrophic (10%)

Unprecedented scale: 30M+ excess deaths. Could arise from high-CFR novel pathogen, engineered pathogen, or antimicrobial resistance crisis. **Impact modifiers**: 8.0× baseline.

---

## Impacts

### Transmission Channels

**Direct Health**: Pathogen causes morbidity and mortality. Affected variables: `pandemic_status`, country-level mortality effects. Modeled via temporary depression of `life_expectancy` and shock to elderly population cohorts. Excess mortality is computed as an output by comparing actual vs. counterfactual population trajectories.

**Economic Disruption**: Containment measures + illness reduce economic activity. Affected variables: `[country].gdp_real`, `[country].unemployment_rate`, `global_trade_volume`.

**Fiscal**: Emergency spending increases public debt. Affected variable: `[country].debt_public`.

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

*Units: `gdp_real` rows are fractions of the entity's current value (−4% ± 2% for the moderate branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). The original specification also carried a `pandemic_severity` row (3-5% GDP, until resolution); the migration dropped it in favor of the direct GDP rows.*

### Differential Exposure

Countries with lower `tax_revenue_gdp` (proxy for state capacity) experience 1.3-1.5× impact multiplier on GDP and unemployment effects. Implementation applies exposure coefficient based on this observable.

### Durability Specifications

| Impact Type | Durability | Rationale |
|-------------|------------|-----------|
| Mortality | permanent | Deaths are irreversible |
| GDP contraction | decaying: half_life=2yr | V-shaped or U-shaped recovery typical |
| Trade disruption | decaying: half_life=1.5yr | Supply chains rebuild |
| Public debt | permanent | Debt incurred persists |

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

### Cascade Mechanisms

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +2.0%/year | 3 years | Debt accumulation, market disruption |
| PAKISTAN_STATE_FAILURE | +0.5%/year | 5 years | Healthcare/fiscal stress on fragile state |
| EGYPT_STATE_FAILURE | +0.5%/year | 5 years | Healthcare/fiscal stress on fragile state |
| CHINESE_ECONOMIC_CRISIS | +0.8%/year | 3 years | Economic disruption, confidence |

No significant triggers: a Type 1 event is fundamentally stochastic.

---

## Historical Analogues

| Case | Year | Deaths | GDP Impact | Key Lesson |
|------|------|--------|------------|------------|
| Spanish Flu | 1918-19 | 50-100M | ~5% | High CFR + high R₀ possible |
| Asian Flu | 1957-58 | 1-2M | <1% | Not all pandemics reach threshold |
| COVID-19 | 2020-22 | 15-25M | ~3-4% | Modern anchor case |

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

## Sources

- WHO pandemic history and PHEIC declarations
- Global Burden of Disease pandemic mortality estimates
- IMF World Economic Outlook pandemic impact assessments
- Johns Hopkins COVID-19 data (anchor case)

## Open Questions

1. **Gain-of-function risk**: How much does lab research increase catastrophic branch probability?
2. **Vaccine platform speed**: Will mRNA platforms meaningfully reduce future severity?
3. **Antimicrobial resistance**: Should AMR pandemic be separate event or branch?
4. **Preparedness decay**: How quickly does post-pandemic investment erode?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-18 | Initial Level 1 specification | Task 2.1.2 - first Type 1 event |
| 2025-12-30 | Critical review complete | Task 2.4.4 - Added Case Against, Probability Stability; fixed variable/event references |
| 2025-01-01 | Migrated to YAML-embedded schema | Task 4.2 format migration |
| 2025-01-02 | Fixed variable names; clarified mortality modeling via observables | Observable-variable discipline |
| 2026-10-12 | Added `resolves_after: 3` | Schema change of the same date: `until: resolved` rows need an explicit window |
| 2026-10-12 | **Remediated**: restored lost prose; `confidence: medium` | Task 4.2.23 / data-track D1 — Restored causal type rationale, state-transition framing, frequency calculation and GDP column, derivation, comparative ranking, Case Against #4, key uncertainties, loading rationale, branch descriptions, differential exposure, durability specifications, cascade mechanisms, historical analogues, sources, changelog rationale. The `medium-high` confidence wording stays in prose; the YAML enum is `low|medium|high` |

---

*See [[methodology/reference/probability-estimation]] for Type 1 methodology | [[methodology/reference/state-variables-global]] for global variables | [[methodology/03-critical-review]] for review methodology*
