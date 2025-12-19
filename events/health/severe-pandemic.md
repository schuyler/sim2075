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

This specification demonstrates Type 1 calibration methodology—events with stable historical base rates where probability estimation relies on reference class frequency.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | SEVERE_PANDEMIC |
| **Scale** | Global |
| **Domain** | Health |
| **Causal Type** | **Type 1: Stochastic** |
| **Onset Speed** | Rapid (months to peak impact) |
| **Reversibility** | Partial (deaths permanent; economic/social impacts recover) |

## Description

Global pandemic causing ≥1 million excess deaths within first 24 months AND/OR ≥3% global GDP contraction. This threshold distinguishes "severe" pandemics from endemic disease burden and minor outbreaks.

This is a **state transition**: `global.pandemic_active` flips from 0 to 1, triggering acute-phase dynamics across health, economic, and social systems.

**What marks occurrence**: WHO declares Public Health Emergency of International Concern (PHEIC) AND early epidemiological data indicates trajectory toward severity threshold.

---

## Causal Type Specification (Type 1: Stochastic)

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

**Base rate**: 3 events / 124 years ≈ **2.4%/year**

### Condition Adjustments

Current conditions that may modify base rate:

| Condition | Direction | Magnitude | Rationale |
|-----------|-----------|-----------|-----------|
| Increased zoonotic interface | ↑ | +0.3% | Agricultural intensification, habitat encroachment, wet markets |
| Global connectivity | ↑ | +0.2% | Faster spread means more pandemics reach severity threshold |
| Surveillance capacity | ↓ | -0.2% | Earlier detection enables containment (H5N1 near-misses contained) |
| Vaccine platform technology | ↓ | -0.3% | mRNA platforms reduce time-to-vaccine; may prevent some pandemics from reaching severity threshold |
| Antimicrobial resistance | ↑ | +0.2% | Secondary bacterial infections harder to treat |

**Net adjustment**: Roughly offsetting; retain base rate of ~2%/year

**Adjusted annual probability**: 2.0% (range: 1.5%-3.0%)

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 2.0% |
| **Low bound** | 1.5% |
| **High bound** | 3.0% |
| **Confidence** | Medium-High |
| **25-year cumulative** | ~40% at point estimate |

### Derivation

1. **Historical frequency**: 2-4 severe pandemics per century in reference class
2. **Annualized**: 2-4%/year base rate
3. **Central estimate**: 2.0%/year (emphasizing clear cases over borderline)
4. **Adjustment**: Condition adjustments roughly net to zero
5. **Final estimate**: 2.0%/year

### Comparative Ranking

Per [[methodology/priority-event-ranking]]:
- More likely than: AMOC collapse (~0.5%), major asteroid impact (~0.01%)
- Similar to: Global financial crisis (~3%), major volcanic eruption (~1%)
- Less likely than: Minor recession (~15%), regional conflict (~5%)

This ranking feels correct—severe pandemics are "once per generation" events.

### Key Uncertainties

- **Novel pathogen emergence**: Could be higher if gain-of-function research or bioweapons accident
- **Pandemic preparedness**: Post-COVID investments may reduce severity of future events
- **Pathogen characteristics**: High-CFR + high-transmissibility combination is rare but catastrophic
- **Definition sensitivity**: Threshold choice (1M deaths) significantly affects base rate

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_CLIM** | 0.50 | Primary driver: ecological disruption increases zoonotic spillover rates, vector range shifts, habitat encroachment |
| **F_HLTH** | 0.45 | Affects outbreak→pandemic escalation: detection speed, containment effectiveness, severity once underway |
| **F_FOOD** | 0.40 | Agricultural intensification, wet markets, livestock density, land use change |
| **F_FIN** | 0.20 | Economic stress reduces health investment, increases risky practices |
| **F_GPT** | 0.15 | Great power tension impedes cooperation, information sharing |
| **F_TECH** | 0.05 | Dual-use research risk (marginal) |
| F_SAS | 0.00 | Regional instability ≠ emergence risk; ecological factors already captured above |
| F_EAS | 0.00 | Regional instability ≠ emergence risk; ecological factors already captured above |
| F_SSA | 0.00 | Regional instability ≠ emergence risk; ecological factors already captured above |
| F_MENA | 0.00 | No distinct pathway beyond factors above |
| F_EUR | 0.00 | No distinct pathway beyond factors above |
| F_LAM | 0.00 | No distinct pathway beyond factors above |

**Sum of squared loadings**: 0.68 ✓

### Loading Interpretation (Type 1)

For Type 1 events, factors modify the annual probability directly:
- High F_CLIM → ecological disruption → zoonotic spillover rates increase (primary emergence driver)
- High F_FOOD → agricultural intensification → more human-animal interface, risky practices
- High F_HLTH → healthcare systems stressed → outbreaks more likely to escalate to pandemic scale

**Why regional factors are zeroed**: Pandemic emergence location (e.g., East Asia, South Asia) is driven by ecological and agricultural conditions, not regional political instability. Those ecological conditions are already captured by F_CLIM and F_FOOD. Adding regional factors would double-count through different proxies.

The probability in any given year is: `P_base × (1 + Σ factor_contributions)`

---

## Severity Branches

Unlike Type 3 events with discrete resolutions, Type 1 events have **severity variation**. Once a severe pandemic occurs, its magnitude varies:

```yaml
severity_branches:

  - id: moderate_severe
    probability: 0.55
    description: |
      COVID-19 scale event: 1-5M confirmed excess deaths globally over 2 years.
      Major economic disruption but not civilizational threat.
      Healthcare systems severely stressed but not collapsed in most regions.
      Examples: COVID-19 (2020-22), Asian Flu (1957)
      
    impact_multiplier: 1.0  # baseline for this event class
    
    factor_modifications:
      F_HLTH: +0.40
      F_FIN: +0.30
      F_GPT: +0.15
      
    duration:
      type: decaying
      half_life_years: 3
      floor: 0.05

  - id: severe
    probability: 0.35
    description: |
      1918 Flu scale event: 5-30M excess deaths globally.
      Severe economic contraction (5-10% global GDP).
      Healthcare system collapse in many regions.
      Significant social disruption.
      
    impact_multiplier: 3.0
    
    factor_modifications:
      F_HLTH: +0.70
      F_FIN: +0.50
      F_GPT: +0.25
      F_FOOD: +0.20
      
    duration:
      type: decaying
      half_life_years: 5
      floor: 0.10

  - id: catastrophic
    probability: 0.10
    description: |
      Unprecedented scale: 30M+ excess deaths globally.
      Potential civilizational disruption.
      Could arise from: high-CFR novel pathogen, engineered pathogen,
      antimicrobial resistance crisis, or compound pandemic.
      
    impact_multiplier: 8.0
    
    factor_modifications:
      F_HLTH: +1.00
      F_FIN: +0.80
      F_GPT: +0.50
      F_FOOD: +0.40
      F_CLIM: +0.15  # agricultural labor disruption
      
    duration:
      type: decaying
      half_life_years: 10
      floor: 0.20
      
    cascade_triggers:
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_modifier: 2.0
        rationale: "Economic disruption triggers financial instability"
      - event_id: STATE_FAILURE_VULNERABLE
        probability_modifier: 1.5
        rationale: "Weak states collapse under healthcare/economic burden"

severity_probability_rationale: |
  Distribution based on historical pandemic severity distribution and 
  pathogen characteristics:
  
  - Moderate-severe (0.55): Most pandemics that reach threshold cluster here.
    COVID-19 is the recent example. Limited CFR or limited transmissibility
    caps total impact.
    
  - Severe (0.35): 1918-scale events. Requires combination of high CFR and
    high transmissibility, which is evolutionarily disfavored but possible.
    Historical frequency: ~1 per century.
    
  - Catastrophic (0.10): Tail risk. No clear historical precedent at global
    scale (Black Death was pre-modern). Could arise from:
    - Novel pathogen with unusual characteristics
    - Engineered pathogen (accident or deliberate)
    - Antimicrobial resistance removing treatment options
    - Compound event (pandemic + other crisis)
    
  These probabilities are conditional on a severe pandemic occurring.
```

---

## Impact Vector

### Global Impacts (Baseline: Moderate-Severe Branch)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.excess_mortality` | ↑ | 3M ± 2M | immediate | permanent |
| `global.gdp_real` | ↓ | -4% ± 2% | immediate | decaying (half_life: 2yr) |
| `global.trade_volume` | ↓ | -8% ± 4% | immediate | decaying (half_life: 1.5yr) |
| `global.healthcare_capacity` | ↓ | -25% ± 10% | immediate | decaying (half_life: 2yr) |
| `global.tourism` | ↓ | -60% ± 20% | immediate | decaying (half_life: 1yr) |
| `global.supply_chain_resilience` | ↓ | -20% ± 10% | delayed(6mo) | decaying (half_life: 3yr) |

*Scale by impact_multiplier for severe (3.0×) and catastrophic (8.0×) branches*

### Regional Differential Impacts

**Exposure variables**: Healthcare capacity, population density, age structure

| Region | GDP Multiplier | Mortality Multiplier | Rationale |
|--------|----------------|---------------------|-----------|
| High-income (NA, EUR, EAS-developed) | 0.8× | 0.7× | Better healthcare, faster vaccine access |
| Middle-income (LAM, MENA, EAS-developing) | 1.0× | 1.0× | Baseline |
| Low-income (SSA, SAS) | 1.3× | 1.5× | Weaker healthcare, slower vaccine access |

### Durability Specifications

| Impact Type | Durability | Parameters | Rationale |
|-------------|------------|------------|-----------|
| Excess mortality | permanent | N/A | Deaths are irreversible |
| GDP contraction | decaying | half_life: 2yr | V-shaped or U-shaped recovery typical |
| Trade disruption | decaying | half_life: 1.5yr | Supply chains rebuild |
| Healthcare capacity | decaying | half_life: 2yr | Systems recover but with lag |
| Behavioral changes | decaying | half_life: 5yr | Some permanent (remote work), most fade |
| Public health investment | maintenance_required | annual_failure: 10% | Post-pandemic investment erodes without political will |

### Impact Derivation

Primary method: **Historical analog scaling**

| Analog | Deaths | GDP Impact | Scaling Factor |
|--------|--------|------------|----------------|
| COVID-19 (2020-22) | 15-25M | -3% (2020) | 1.0× (anchor) |
| 1918 Flu | 50-100M | -5% estimated | 3-4× mortality, similar GDP |
| 1957 Asian Flu | 1-2M | <1% | 0.3× (below threshold) |

COVID-19 serves as the primary anchor for moderate-severe branch.

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Economic stress → financial crisis | GLOBAL_FINANCIAL_CRISIS | +2%/year | 3 years | Debt accumulation, market disruption |
| Healthcare collapse → state failure | STATE_FAILURE_VULNERABLE | +1.5%/year per affected state | 5 years | Legitimacy crisis, fiscal exhaustion |
| Supply disruption → food crisis | FOOD_CRISIS_REGIONAL | +2%/year | 2 years | Agricultural labor, logistics disruption |
| Social stress → political instability | POLITICAL_CRISIS_DOMESTIC | +1%/year (multiple countries) | 5 years | Legitimacy challenges, polarization |
| Pandemic fatigue → reduced preparedness | SEVERE_PANDEMIC (next) | -0.5%/year | 10 years | Investment and vigilance post-crisis |

### Impact Chains

**Pathway 1**: Pandemic → Economic disruption → Financial crisis
```
Severe pandemic → GDP contraction → corporate defaults → banking stress → 
credit contraction → P(financial crisis) ↑
```

**Pathway 2**: Pandemic → State capacity exhaustion → State failure
```
Severe pandemic → healthcare spending spike → fiscal crisis → 
service delivery failure → legitimacy crisis → P(state failure) ↑
```

**Pathway 3**: Pandemic → Supply chain disruption → Food crisis
```
Severe pandemic → labor shortage → agricultural disruption → 
logistics breakdown → P(regional food crisis) ↑
```

---

## Transmission Channels

### Direct Health Channel

**Mechanism**: Pathogen causes morbidity and mortality directly
**Affected regions**: All (global by definition)
**Affected variables**: `excess_mortality`, `healthcare_capacity`, `disability_burden`
**Differential exposure**: Age structure, baseline health, healthcare access

### Economic Disruption Channel

**Mechanism**: Containment measures + illness reduce economic activity
**Affected regions**: All, but especially service-dependent economies
**Affected variables**: `gdp_real`, `trade_volume`, `employment`, `tourism`
**Differential exposure**: Economic structure, policy response capacity

### Supply Chain Channel

**Mechanism**: Production and logistics disruption
**Affected regions**: Globalized supply chain participants
**Affected variables**: `supply_chain_resilience`, `manufacturing_output`, `inflation`
**Differential exposure**: Import dependence, supply chain position

### Social/Political Channel

**Mechanism**: Stress on social cohesion and political legitimacy
**Affected regions**: All, especially low-trust societies
**Affected variables**: `social_cohesion`, `political_stability`, `institutional_trust`
**Differential exposure**: Pre-existing polarization, government effectiveness

---

## Pathogen Characteristics (Scenario Variants)

Different pathogen profiles produce different impact patterns:

| Characteristic | Moderate-Severe | Severe | Catastrophic |
|----------------|-----------------|--------|--------------|
| **CFR** | 0.5-2% | 2-5% | 5%+ |
| **R₀** | 2-4 | 3-6 | 4+ |
| **Generation time** | 4-7 days | 3-5 days | 2-5 days |
| **Age skew** | Elderly-skewed | All ages | All ages |
| **Vaccine timeline** | 12-24 months | 12-36 months | 18+ months or ineffective |
| **Examples** | COVID-19, H1N1 | 1918 Flu | Novel/engineered |

---

## Historical Analogues

| Case | Year | Deaths | GDP Impact | Key Lesson |
|------|------|--------|------------|------------|
| Spanish Flu | 1918-19 | 50-100M | ~5% | High CFR + high R₀ possible |
| Asian Flu | 1957-58 | 1-2M | <1% | Not all pandemics reach severity threshold |
| Hong Kong Flu | 1968-69 | 1-4M | <1% | Immune memory from prior pandemic helped |
| H1N1 Swine Flu | 2009-10 | 150-575K | <0.5% | Early containment + low CFR limited impact |
| COVID-19 | 2020-22 | 15-25M | -3% (2020) | Modern anchor case |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-18 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Emerging pathogen surveillance data; gain-of-function risk assessment; antimicrobial resistance trajectories |

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- WHO pandemic history and PHEIC declarations
- Global Burden of Disease pandemic mortality estimates
- IMF World Economic Outlook pandemic impact assessments
- Johns Hopkins COVID-19 data (anchor case)
- 1918 Flu historiography (Taubenberger, Barry)

## Open Questions

- **Gain-of-function risk**: How much does lab research increase catastrophic branch probability?
- **Vaccine platform speed**: Will mRNA platforms meaningfully reduce future pandemic severity?
- **Antimicrobial resistance**: Should AMR pandemic be separate event or branch of this one?
- **Preparedness decay**: How quickly does post-pandemic investment erode?
- **Compound risk**: How to model pandemic + other crisis (e.g., pandemic during financial crisis)?
- **Detection threshold**: At what point in emergence does "severe pandemic" event fire?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-18 | Initial Level 1 specification | Task 2.1.2 - first Type 1 event |

---

*See [[methodology/reference/probability-estimation]] for Type 1 base rate methodology | [[methodology/reference/calibration-anchors]] for reference events*
