---
title: Sahel Catastrophe
type: note
permalink: events/geopolitical/sahel-catastrophe
tags:
- event
- type-2
- threshold
- geopolitical
- humanitarian
- sahel
- sub-saharan-africa
- climate
- conflict
- level-1
---

# Sahel Catastrophe

**Type 2 (Threshold) Event** — Probability rises as compound pressures (climate, food, conflict, displacement, governance) accumulate toward the catastrophe threshold.

---

## Description

Regional catastrophe in the Sahel zone—Mali, Niger, Burkina Faso, Chad, and potentially Mauritania—characterized by simultaneous multi-country crisis exceeding the baseline assumption of "troubled but contained" instability. The Sahel represents the world's most vulnerable region to compounding climate, governance, and conflict pressures.

**What marks occurrence**: Multiple Sahel states simultaneously in acute crisis; humanitarian emergency at catastrophic scale (>10M displaced, widespread famine conditions); jihadist or armed group control of significant territory across multiple countries; international humanitarian response overwhelmed; regional contagion threatening coastal West Africa.

**Distinction from baseline**: The baseline trajectory already includes chronic instability—coups, insurgencies, food insecurity, displacement. This event captures the transition from chronic dysfunction to acute regional catastrophe. The difference is scale (multiple countries simultaneously), severity (famine rather than food insecurity), and consequences (mass mortality, regional contagion).

**Key regional characteristics**:
- **Climate**: Sahel is among the most climate-vulnerable regions globally; rainfall variability directly affects food production
- **Demographics**: Highest fertility rates in the world (Niger TFR >6); population doubling every ~20 years
- **Governance**: Military coups in Mali (2020, 2021), Burkina Faso (2022), Niger (2023); governance collapse ongoing
- **Conflict**: Jihadist insurgencies (JNIM, ISGS) control significant rural territory; ethnic violence; state security forces implicated in atrocities
- **Food**: Chronic food insecurity affecting 20-30M people annually; periodic acute crises

---

## Specification

```yaml
id: SAHEL_CATASTROPHE
domain: political
scale: regional
causal_type: 2
onset: gradual
reversibility: partial
```

*Scale: regional (multi-country). Domain: political / humanitarian (recorded as `political`: the schema enum has no humanitarian value). Onset speed: gradual to rapid (crisis builds over years, acute phase 1-3 years; recorded as `gradual` because the Type 2 build-up, not the acute phase, is what the engine times). Reversibility: partial (stabilization possible but long-term development setback).*

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Sahel catastrophe exhibits threshold dynamics:
- Multiple pressures accumulate over years: climate stress, governance decay, demographic pressure, conflict expansion
- System absorbs stress through humanitarian response, resilience, international support
- Threshold crossing occurs when multiple stressors spike simultaneously, overwhelming coping capacity
- No single actor decision (Type 3) or unpredictable shock (Type 1) dominates—this is pressure accumulation

### Pressure Function

The Sahel's pressure function integrates stress across multiple observable state variables. Using the Sahel regional aggregate:

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `sahel.agricultural_climate_risk` | 0.20 | linear (0-100 → 0-1) | Structural climate vulnerability; annual shocks via F_CLIM |
| `sahel.food_import_dependence` | 0.20 | linear (0-100 → 0-1) | Proxy for food insecurity vulnerability |
| `sahel.internal_conflict_intensity` | 0.20 | linear (0-4 → 0-1) | Conflict escalation indicator |
| `sahel.idp_population` | 0.15 | linear, cap at 10M | Displacement as crisis severity measure |
| `sahel.years_since_irregular_transition` | 0.10 | inverse (recent = high) | Recent coups indicate instability |
| `sahel.coup_attempts_10yr` | 0.08 | linear, cap at 5 | Frequency of irregular transition attempts |
| `sahel.tax_revenue_gdp` | 0.07 | inverse (low = high) | State capacity proxy |

**Pressure calculation**:
```
pressure = 0.20 × (agricultural_climate_risk / 100)
         + 0.20 × (food_import_dependence / 100)
         + 0.20 × (internal_conflict_intensity / 4)
         + 0.15 × min(idp_population / 10, 1.0)
         + 0.10 × (10 - min(years_since_irregular_transition, 10)) / 10
         + 0.08 × min(coup_attempts_10yr, 5) / 5
         + 0.07 × (15 - min(tax_revenue_gdp, 15)) / 15
```
*Normalized to 0-1 scale; multiply by 100 for 0-100 scale*

The YAML expression below realizes these transforms in the expression language's subset: the two "cap at" terms and the two inverse terms use the whitelisted two-argument `min()` exactly as written above (the inverse transforms are linear ramps that reach zero at 10 years since the last irregular transition and at 15% tax revenue/GDP), and the whole weighted sum is wrapped in `100 * (...)` so the expression sits on `threshold`'s 0-100 scale.

**Variable sources**: All variables are defined in [[methodology/reference/state-variables-country]]. Climate shocks are delivered through F_CLIM factor draws affecting `agricultural_climate_risk`.

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 68 (on 0-100 pressure scale) |
| **Uncertainty** | ±12 |
| **Sharpness (k)** | 0.15 (moderate; gradual transition as multiple systems fail) |
| **Historical calibration** | 2012 Mali crisis (~pressure 60); 1984-85 Sahel famine (~pressure 75); current trajectory ~55 |

### Minimum Probability

**Floor**: 0.8%/year (residual risk from sudden climate shocks, rapid jihadist expansion, or cascade from coastal state collapse)

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.20 * (sahel.agricultural_climate_risk / 100) +
      0.20 * (sahel.food_import_dependence / 100) +
      0.20 * (sahel.internal_conflict_intensity / 4) +
      0.15 * min(sahel.idp_population / 10, 1.0) +
      0.10 * ((10 - min(sahel.years_since_irregular_transition, 10)) / 10) +
      0.08 * (min(sahel.coup_attempts_10yr, 5) / 5) +
      0.07 * ((15 - min(sahel.tax_revenue_gdp, 15)) / 15)
    )
  threshold: 68
  threshold_std: 12
  sharpness: 0.15
  floor: 0.008
  resolves_after: 10
  annual: 0.018
  range: [0.010, 0.030]
  confidence: medium
```

`resolves_after: 10` — the `until: resolved` conflict-intensity rows (Sahel, coastal West Africa, Nigeria) stay at full magnitude for ten years per firing, counting the firing year: the Regional Crisis branch's acute phase runs 5-10 years and the Humanitarian Catastrophe branch's 10-15, so ten is the boundary shared by the two branches carrying 80% of the mass, and it matches the region's own record (Mali's 2012 crisis was unresolved a decade later; see Durability Specifications for the per-branch durations the schema cannot yet express).

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.8% |
| **Low bound** | 1.0% |
| **High bound** | 3.0% |
| **Confidence** | Medium-Low (recorded as `medium` in YAML: the schema enum is `low|medium|high`) |
| **25-year cumulative** | ~37% at point estimate |

### Current Pressure Estimate

Current pressure: ~55/100 (elevated and rising)
- `agricultural_climate_risk`: High (~70/100); Sahel among most climate-vulnerable regions
- `food_import_dependence`: Moderate-high (~50%); urban populations import-dependent
- `internal_conflict_intensity`: 2-3 (intermediate to war); ~8,000-10,000 deaths/year
- `idp_population`: ~3M internally displaced
- `years_since_irregular_transition`: 1-2 years (Niger 2023, Burkina Faso 2022)
- `coup_attempts_10yr`: 4-5 (Mali 2020/2021, Burkina Faso 2022, Niger 2023)
- `tax_revenue_gdp`: Very low (~8-10%); weak state capacity

At the lower ends of these ranges (conflict 2, 2 years since transition, 4 coup attempts, 10% tax revenue) the YAML expression gives 55.2; at the upper ends it gives ~64. The compiler's pressure-scale check is skipped for this event because the state catalog records no 2025 baselines for country/aggregate variables.

### Derivation

1. **Base rate for regional catastrophes**: ~1-2% annual probability for high-vulnerability regions
2. **Sahel-specific elevation**: Current governance collapse (three coup governments), rising conflict trajectory, climate trends all point upward
3. **Trajectory**: Pressure has increased significantly since 2020; coups accelerating instability
4. **Central estimate**: 1.8%/year (range 1.0-3.0%)

### Probability Evolution

This is a Type 2 event where probability is rising over the simulation period:

| Period | Estimated Annual Probability | Rationale |
|--------|------------------------------|-----------|
| 2025-2030 | 1.5-2.0% | Current trajectory; recent coups creating instability |
| 2030-2040 | 2.0-2.5% | Climate stress increasing; demographic pressure growing; conflict likely expanded |
| 2040-2050 | 2.5-3.5% | Climate impacts more severe; population nearly doubled; governance unlikely improved |
| 2050-2075 | 3.0-4.0% | Peak vulnerability period; full climate impact; massive youth population |

### Comparative Ranking

- **Higher than**: Egypt state failure (1.5%); Egypt has stronger institutions
- **Higher than**: Pakistan state failure (1.5%); nuclear deterrent and international attention provide some stability
- **Lower than**: Some Sub-Saharan aggregates that include Sahel; this is the most vulnerable sub-region

### Key Uncertainties

- **Climate trajectory**: Sahel rainfall is highly variable; models disagree on direction
- **Jihadist trajectory**: Will insurgencies consolidate or fragment?
- **International response**: Will humanitarian system maintain engagement or fatigue?
- **Coastal contagion**: Will instability spread to Ghana, Côte d'Ivoire, Benin?
- **Great power competition**: Russia (Wagner/Africa Corps) vs. Western engagement—does competition help or hurt?

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

```yaml
factors:
  F_SSA: 0.43   # Primary regional factor; Sahel is core of Sub-Saharan stress
  F_CLIM: 0.28  # Climate is existential for Sahel; rainfall determines food production
  F_FOOD: 0.25  # Global food prices affect import-dependent urban populations; regional production critical
  F_GPT: 0.11   # Great power competition affects intervention, support; Russia/Wagner presence
  F_HLTH: 0.08  # Health system collapse amplifies mortality; disease outbreaks in displacement settings
  F_FIN: 0.06   # Aid flows depend on donor fiscal space
  F_MENA: 0.06  # Libya instability affects northern Mali; weapons flows
  F_EUR: 0.03   # European migration concern drives some engagement
variance: 0.65  # Type 2 target
```

F_TECH, F_EAS, F_SAS and F_LAM carry no loading (no significant pathway).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.59 from original loadings. The compiled value with the catalog's Ω is 0.645.

**Original loadings (2025-12-28, before variance allocation)**: F_SSA 0.72, F_CLIM 0.48, F_FOOD 0.43, F_GPT 0.19, F_HLTH 0.14, F_FIN 0.10, F_MENA 0.10, F_EUR 0.05 — normalized to sum of squared loadings 0.52 + 0.23 + 0.18 + 0.04 + 0.02 + 0.01 + 0.01 + 0.003 ≈ 1.01 under the pre-Task-3.11 convention. The 2025-12-31 variance allocation scaled every loading by 0.59; the relative weights are unchanged.

### Loading Interpretation (Type 2)

Factors shock state variables feeding the pressure function:
- High F_SSA → regional instability, conflict escalation → pressure rises
- High F_CLIM → rainfall failure, temperature stress → food production drops → pressure rises
- High F_FOOD → global food prices spike → import costs rise, humanitarian response strained → pressure rises
- High F_GPT → great power competition intensifies → intervention patterns shift, potentially destabilizing

---

## Severity Branches

Once threshold is crossed:

```yaml
branches:
  - {id: regional_crisis, p: 0.40, desc: "Multiple Sahel states in acute crisis; some state functions persist; displacement >10M, primarily internal; coastal West Africa stable"}
  - {id: humanitarian_catastrophe, p: 0.40, desc: "Region-wide famine; state collapse in 2+ countries; displacement >15M with refugee flows to coastal states; coastal contagion begins"}
  - {id: civilizational_collapse, p: 0.20, desc: "Sustained region-wide catastrophe at 1984-85 famine scale with 5x the population; multiple states cease to function; displacement 30M+"}
```

### Regional Crisis (40%)

Multiple Sahel states in acute crisis, but some state functions persist. Humanitarian response strained but operational. Displacement exceeds 10M but primarily internal. Famine conditions in localized areas, not region-wide. Jihadist territorial control expands but doesn't threaten capitals. Coastal West Africa remains stable.

| Attribute | Value |
|-----------|-------|
| **Impact multiplier** | 1.0× (baseline) |
| **Excess mortality** | 500K-1M over crisis period |
| **Displacement** | 10-15M |
| **Duration** | 5-10 years of acute phase |

**Factor modifications**: F_SSA +0.35, F_FIN +0.20

**Duration**: decaying, half_life: 8 years, floor: 0.10

### Humanitarian Catastrophe (40%)

Regional famine conditions across multiple countries simultaneously. State collapse in 2+ countries (beyond current dysfunction). Displacement exceeds 15M including mass refugee flows to coastal states. Jihadist groups control major population centers. Humanitarian response overwhelmed; donor fatigue. Coastal contagion begins.

| Attribute | Value |
|-----------|-------|
| **Impact multiplier** | 2.5× |
| **Excess mortality** | 2-5M over crisis period |
| **Displacement** | 15-25M |
| **Duration** | 10-15 years of elevated crisis |

**Factor modifications**: F_SSA +0.55, F_FIN +0.35, F_FOOD +0.25

**Duration**: decaying, half_life: 12 years, floor: 0.15

**Cascade triggers**:
- COASTAL_WEST_AFRICA_DESTABILIZATION: +2%/year for 15 years (jihadist expansion, refugee pressure)
- EU_MIGRATION_CRISIS: +0.5%/year for duration (Mediterranean route pressure)

### Civilizational Collapse (20%)

Sustained, region-wide catastrophe approaching 1984-85 famine scale but with 5× the population. Multiple states cease to function as states. Mass mortality from famine and violence. Displacement at unprecedented scale (potentially 30M+). Jihadist governance in significant areas. International community unable to respond at required scale. Long-term development reversal of decades.

| Attribute | Value |
|-----------|-------|
| **Impact multiplier** | 5.0× |
| **Excess mortality** | 5-15M over crisis period |
| **Displacement** | 25-40M |
| **Duration** | 15-25 years of crisis and recovery |

**Factor modifications**: F_SSA +0.80, F_FIN +0.45, F_FOOD +0.40, F_GPT +0.25 (great power intervention likely)

**Duration**: decaying, half_life: 18 years, floor: 0.20

**Cascade triggers**:
- WEST_AFRICA_REGIONAL_COLLAPSE: +4%/year for 20 years
- GLOBAL_REFUGEE_CRISIS: significant contribution
- NIGERIA_NORTHERN_DESTABILIZATION: +2%/year for 15 years

*The per-branch factor modifications, branch-level durations (decay-to-floor) and branch-conditional cascade triggers above have no schema v0.1 construct: the factor modifications and branch durations stay here as prose, and the branch-conditional triggers all name events that exist only as round-2 stubs or registry dispositions (see Cascade Effects), so none is written into the YAML.*

### Branch Probability Rationale

- **Regional Crisis (0.40)**: Most likely because international community will prioritize preventing worst outcomes; some state capacity remains even in collapsed states; localized coping mechanisms persist. Historical pattern is that Sahel crises remain "crises" rather than becoming "catastrophes" due to humanitarian response.

- **Humanitarian Catastrophe (0.40)**: High probability because current trajectory suggests response capacity is being overwhelmed; multiple simultaneous state failures already occurring; climate trends worsen the outlook; donor fatigue is real.

- **Civilizational Collapse (0.20)**: Lower but not negligible because the structural factors (climate, demographics, governance) are genuinely severe; 1984-85 occurred with smaller population and less conflict overlay; international system's ability to respond at scale in contested territory is limited.

---

## Impact Vector

### Sahel Regional Impacts (Baseline: Regional Crisis)

The original specification, kept here because the YAML had to re-express several rows:

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `sahel.gdp_real` | ↓ | -30% ± 15% | gradual(3yr) | decaying (half_life: 12yr) |
| `sahel.pop_total` | ↓ | -3% to -8% (mortality + emigration) | gradual(5yr) | permanent (mortality component) |
| `sahel.food_import_dependence` | ↑ | +30% ± 15% | immediate | decaying (half_life: 10yr) |
| `sahel.internal_conflict_intensity` | ↑ | to 4 (major war) | immediate | regime_dependent |
| `sahel.idp_population` | ↑ | +6-10M | gradual(3yr) | decaying (half_life: 15yr) |
| `sahel.refugees_abroad` | ↑ | +4-5M | gradual(4yr) | decaying (half_life: 18yr) |

**Population row re-expressed**: `pop_total` is a derived variable in the state catalog (computed from the age-sex population stocks) and cannot be an impact target. Its emigration component is already carried by the `refugees_abroad` row (+4-5M is 4-5% of the Sahel's ~100M people); its mortality component (500K-1M excess deaths in the baseline branch, ~1% of population) is modeled as a `life_expectancy` depression of −3 ± 1.5 years, the same device [[events/geopolitical/pakistan-state-failure]] uses for excess mortality. Because the target is now a flow variable rather than a population stock, the row decays (half-life 10 years, the economic-damage/IDP recovery timescale) instead of being permanent; the deaths themselves remain permanent in the durability table below.

### Coastal West Africa and Nigeria Impacts

Coastal states (Ghana, Côte d'Ivoire, Benin, Togo) are part of the **West/Central Africa (other)** Tier 2 aggregate. Nigeria is individually modeled (`nga`).

| Entity | Variable | Direction | Magnitude | Onset | Durability |
|--------|----------|-----------|-----------|-------|------------|
| `west_central_africa_other` | `protest_intensity_annual` | ↑ | +15 ± 8 | gradual(2yr) | decaying (half_life: 5yr) |
| `west_central_africa_other` | `refugees_hosted` | ↑ | +2-4M | gradual(3yr) | decaying (half_life: 12yr) |
| `west_central_africa_other` | `internal_conflict_intensity` | ↑ | +0.5 ± 0.3 | gradual(3yr) | regime_dependent |
| `nigeria` | `internal_conflict_intensity` | ↑ | +0.5 ± 0.3 | gradual(2yr) | regime_dependent |
| `nigeria` | `refugees_hosted` | ↑ | +0.3-0.7M | gradual(3yr) | decaying (half_life: 10yr) |

### Global and European Impacts

| Entity | Variable | Direction | Magnitude | Onset | Durability |
|--------|----------|-----------|-----------|-------|------------|
| `italy` | `net_migration_rate` | ↑ | +0.15% ± 0.08% | gradual(3yr) | decaying |
| `spain` | `net_migration_rate` | ↑ | +0.10% ± 0.05% | gradual(3yr) | decaying |
| `france` | `net_migration_rate` | ↑ | +0.05% ± 0.03% | gradual(4yr) | decaying |

**Note**: "Global displaced persons" and "Humanitarian funding demand" are simulation outputs derived from entity-level displacement variables, not state variables to be shocked.

### Differential Impacts by Severity Branch

| Branch | Impact Multiplier | Additional Effects |
|--------|-------------------|-------------------|
| Regional Crisis | 1.0× | Contained to Sahel; coastal states stressed but stable |
| Humanitarian Catastrophe | 2.5× | Coastal contagion begins; global humanitarian system strained |
| Civilizational Collapse | 5.0× | West Africa regional destabilization; global refugee crisis; jihadist expansion |

**How the multipliers are realized in YAML.** The 2.5× and 5.0× multipliers cannot be applied literally to every row: `gdp_real` impacts are fractions of current GDP (5 × −30% = −150%, and even 2.5 × −30% ± 15% = −75% ± 37.5% draws a run-killing contribution ≤ −1 about a quarter of the time), `internal_conflict_intensity` is a 0-4 scale whose baseline row already reaches the top, `food_import_dependence` is a share of consumption, and the branch tables above give their own displacement totals (15-25M and 25-40M), which the multipliers overshoot (2.5 × 10-15M = 25-37M; 5 × 10-15M = 50-75M). The three branches are therefore written as explicit lists:

- **Applied literally (unbounded additive variables)**: `refugees_hosted` (both entities), `protest_intensity_annual` and `internal_conflict_intensity` for the coastal aggregate, and the three `net_migration_rate` rows.
- **Taken from the branch tables instead of the multiplier**: displacement, split in the baseline's ~64:36 IDP:refugee ratio — 13 ± 3M IDPs and 7 ± 1.5M refugees (20M, the Humanitarian Catastrophe midpoint); 21 ± 5M and 11.5 ± 2.5M (32.5M, the Civilizational Collapse midpoint). Excess mortality (0.5-1M, 2-5M, 5-15M) as a saturating life-expectancy depression of −3, −7, −12 years (the Great Leap famine's ~−20 at trough bounds the top).
- **Capped by the variable's range**: `sahel.gdp_real` −30% / −45% / −60% (Syria's 2011-2020 contraction of ~60% is the collapse analogue); `sahel.food_import_dependence` +30 / +40 / +45 points (from ~50% toward ~95%); `sahel.internal_conflict_intensity` +1.5 ± 0.5 in every branch (to 4, the top of the scale); `nga.internal_conflict_intensity` capped at +1.5 ± 0.5 in the collapse branch (Nigeria starts near 2-3); `west_central_africa_other.protest_intensity_annual` capped at +60 ± 25 in the collapse branch (a 0-100 index).

```yaml
impacts:
  regional_crisis:
    # Sahel
    - {var: sahel.gdp_real,                                       mag: [-0.30, 0.15], onset: {gradual: 3}, decay: 12}
    - {var: sahel.life_expectancy,                                mag: [-3, 1.5],     onset: {gradual: 5}, decay: 10}
    - {var: sahel.food_import_dependence,                         mag: [30, 15],      onset: immediate,    decay: 10}
    - {var: sahel.internal_conflict_intensity,                    mag: [1.5, 0.5],    onset: immediate,    until: resolved}
    - {var: sahel.idp_population,                                 mag: [8, 2],        onset: {gradual: 3}, decay: 15}
    - {var: sahel.refugees_abroad,                                mag: [4.5, 0.5],    onset: {gradual: 4}, decay: 18}
    # Coastal West Africa and Nigeria
    - {var: west_central_africa_other.protest_intensity_annual,   mag: [15, 8],       onset: {gradual: 2}, decay: 5}
    - {var: west_central_africa_other.refugees_hosted,            mag: [3, 1],        onset: {gradual: 3}, decay: 12}
    - {var: west_central_africa_other.internal_conflict_intensity, mag: [0.5, 0.3],   onset: {gradual: 3}, until: resolved}
    - {var: nga.internal_conflict_intensity,                      mag: [0.5, 0.3],    onset: {gradual: 2}, until: resolved}
    - {var: nga.refugees_hosted,                                  mag: [0.5, 0.2],    onset: {gradual: 3}, decay: 10}
    # Europe
    - {var: ita.net_migration_rate,                               mag: [0.15, 0.08],  onset: {gradual: 3}, decay: 8}
    - {var: esp.net_migration_rate,                               mag: [0.10, 0.05],  onset: {gradual: 3}, decay: 8}
    - {var: fra.net_migration_rate,                               mag: [0.05, 0.03],  onset: {gradual: 4}, decay: 8}

  humanitarian_catastrophe:
    # Sahel
    - {var: sahel.gdp_real,                                       mag: [-0.45, 0.15], onset: {gradual: 3}, decay: 12}
    - {var: sahel.life_expectancy,                                mag: [-7, 3],       onset: {gradual: 5}, decay: 10}
    - {var: sahel.food_import_dependence,                         mag: [40, 15],      onset: immediate,    decay: 10}
    - {var: sahel.internal_conflict_intensity,                    mag: [1.5, 0.5],    onset: immediate,    until: resolved}
    - {var: sahel.idp_population,                                 mag: [13, 3],       onset: {gradual: 3}, decay: 15}
    - {var: sahel.refugees_abroad,                                mag: [7, 1.5],      onset: {gradual: 4}, decay: 18}
    # Coastal West Africa and Nigeria
    - {var: west_central_africa_other.protest_intensity_annual,   mag: [37.5, 20],    onset: {gradual: 2}, decay: 5}
    - {var: west_central_africa_other.refugees_hosted,            mag: [7.5, 2.5],    onset: {gradual: 3}, decay: 12}
    - {var: west_central_africa_other.internal_conflict_intensity, mag: [1.25, 0.75], onset: {gradual: 3}, until: resolved}
    - {var: nga.internal_conflict_intensity,                      mag: [1.25, 0.75],  onset: {gradual: 2}, until: resolved}
    - {var: nga.refugees_hosted,                                  mag: [1.25, 0.5],   onset: {gradual: 3}, decay: 10}
    # Europe
    - {var: ita.net_migration_rate,                               mag: [0.375, 0.2],  onset: {gradual: 3}, decay: 8}
    - {var: esp.net_migration_rate,                               mag: [0.25, 0.125], onset: {gradual: 3}, decay: 8}
    - {var: fra.net_migration_rate,                               mag: [0.125, 0.075], onset: {gradual: 4}, decay: 8}

  civilizational_collapse:
    # Sahel
    - {var: sahel.gdp_real,                                       mag: [-0.60, 0.15], onset: {gradual: 3}, decay: 12}
    - {var: sahel.life_expectancy,                                mag: [-12, 5],      onset: {gradual: 5}, decay: 10}
    - {var: sahel.food_import_dependence,                         mag: [45, 15],      onset: immediate,    decay: 10}
    - {var: sahel.internal_conflict_intensity,                    mag: [1.5, 0.5],    onset: immediate,    until: resolved}
    - {var: sahel.idp_population,                                 mag: [21, 5],       onset: {gradual: 3}, decay: 15}
    - {var: sahel.refugees_abroad,                                mag: [11.5, 2.5],   onset: {gradual: 4}, decay: 18}
    # Coastal West Africa and Nigeria
    - {var: west_central_africa_other.protest_intensity_annual,   mag: [60, 25],      onset: {gradual: 2}, decay: 5}
    - {var: west_central_africa_other.refugees_hosted,            mag: [15, 5],       onset: {gradual: 3}, decay: 12}
    - {var: west_central_africa_other.internal_conflict_intensity, mag: [2.5, 1.5],   onset: {gradual: 3}, until: resolved}
    - {var: nga.internal_conflict_intensity,                      mag: [1.5, 0.5],    onset: {gradual: 2}, until: resolved}
    - {var: nga.refugees_hosted,                                  mag: [2.5, 1.0],    onset: {gradual: 3}, decay: 10}
    # Europe
    - {var: ita.net_migration_rate,                               mag: [0.75, 0.4],   onset: {gradual: 3}, decay: 8}
    - {var: esp.net_migration_rate,                               mag: [0.5, 0.25],   onset: {gradual: 3}, decay: 8}
    - {var: fra.net_migration_rate,                               mag: [0.25, 0.15],  onset: {gradual: 4}, decay: 8}
```

*Units: `gdp_real` rows are fractions of the entity's current value (−30% ± 15% in the baseline branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). The `food_import_dependence` rows are read as percentage points of consumption (the prose's "+30% ± 15%" taken additively, from ~50% to ~80%); displacement rows are millions of people; `net_migration_rate` rows are % of population per year; the `internal_conflict_intensity` rows lift the Sahel from its current 2-3 to 4 (major war).*

### Durability Specifications

| Impact Type | Durability | Parameters | Rationale |
|-------------|------------|------------|-----------|
| Mortality | permanent | N/A | Deaths cannot be undone |
| IDP displacement | decaying | half_life: 15yr | Return slow in conflict zones |
| Refugee displacement | decaying | half_life: 18yr | Repatriation even slower than IDP return |
| Economic damage | decaying | half_life: 12yr | Development setback; infrastructure destruction |
| Human development | shock_vulnerable | Can be reversed by subsequent crises | Fragile gains |
| Territorial control | regime_dependent | Persists until governance restored | Jihadist consolidation |
| Coastal/Nigeria pressure | decaying | half_life: 5-10yr | Pressure eases as crisis stabilizes |
| European migration | decaying | half_life: 8yr | Migration pressure eases with stabilization |

*Schema v0.1 compiles only `decay`, `permanent: true`, `until: resolved` and `{type: decaying, half_life: N}`. The `regime_dependent` territorial-control rows (`internal_conflict_intensity` for the Sahel, the coastal aggregate and Nigeria) are written as `until: resolved` with the ten-year `resolves_after` window above; the branch-level decay-to-floor durations (half-life 8/12/18 years, floor 0.10/0.15/0.20) and the `shock_vulnerable` human-development entry have no row of their own and stay in prose; "mortality: permanent" is carried as a decaying `life_expectancy` depression because the population stock cannot be targeted directly (see the population note above).*

---

## Cascade Effects

```yaml
cascades:
  triggers: []   # every target below is a round-2 stub or a registry disposition, not yet an event file
  triggered_by:
    - {event: EGYPT_STATE_FAILURE,             delta: 0.005}   # regional contagion; refugee flows (5 years)
    - {event: AGRICULTURAL_YIELD_BREAKTHROUGH, delta: -0.003}  # agricultural viability in marginal zones (20 years)
```

### State → Probability Cascades

None of the targets below exists as an event file yet, so the YAML `triggers:` list is empty and the cascades are kept here. [[events/backlog-registry]] records their dispositions: NIGERIA_NORTHERN_CRISIS / NIGERIA_NORTHERN_DESTABILIZATION → promoted as `NIGERIA_STATE_FAILURE`; COASTAL_WEST_AFRICA_DESTABILIZATION and WEST_AFRICA_REGIONAL_COLLAPSE → promoted as `COASTAL_WEST_AFRICA_DESTABILIZATION`; EU_MIGRATION_CRISIS and GLOBAL_REFUGEE_CRISIS → promoted as `EUROPEAN_MIGRATION_CRISIS`; GLOBAL_HUMANITARIAN_CAPACITY_CRISIS → folded into `EUROPEAN_MIGRATION_CRISIS`; GHANA_POLITICAL_CRISIS, COTE_DIVOIRE_INSTABILITY and MAGHREB_INSTABILITY → declined. EU_COHESION_STRESS is not listed in the registry (it reads as a naming drift for the existing EU_FRAGMENTATION, but no alias row says so); it is reported, not normalized.

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Coastal contagion | NIGERIA_NORTHERN_CRISIS | +1.5%/year | 15 years | Jihadist expansion; refugee pressure; governance demonstration effect |
| Coastal contagion | GHANA_POLITICAL_CRISIS | +1%/year | 10 years | Refugee burden; economic shock; security spillover |
| Coastal contagion | COTE_DIVOIRE_INSTABILITY | +1.5%/year | 10 years | History of instability; northern border exposure |
| European politics | EU_COHESION_STRESS | +0.3%/year | Duration of crisis | Migration politics |
| Jihadist expansion | MAGHREB_INSTABILITY | +0.5%/year | 15 years | Trans-Saharan networks; Libya corridor |
| Humanitarian system | GLOBAL_HUMANITARIAN_CAPACITY_CRISIS | +1%/year | Duration | System overwhelmed; donor fatigue |

### Triggered By

Cascades other catalog events declare onto this one (informational; each lives in the source event's YAML):

| Source Event | Effect on This Event | Duration | Mechanism |
|--------------|---------------------|----------|-----------|
| EGYPT_STATE_FAILURE | +0.5%/year | 5 years | Regional contagion; refugee flows |
| AGRICULTURAL_YIELD_BREAKTHROUGH | −0.3%/year | 20 years | Agricultural viability in marginal zones reduces displacement pressure |
| AMOC_WEAKENING | direction uncertain | — | West African monsoon response to Atlantic SST change; models disagree on whether the Sahel gets wetter or drier, so [[events/climate/amoc-weakening]] records the link in prose rather than as a cascade magnitude |

The round-2 stubs `NIGERIA_STATE_FAILURE`, `COASTAL_WEST_AFRICA_DESTABILIZATION` and `MAJOR_BREADBASKET_FAILURE` ([[events/planned-events-round-2]]) list SAHEL_CATASTROPHE as a consumer and will add edges when specified.

### Impact Chains

**Pathway 1**: Sahel catastrophe → Coastal contagion → West African regional collapse
```
Sahel catastrophe → refugee flows to coastal states (Ghana, Côte d'Ivoire, Benin) →
host state resources strained → jihadist networks expand southward →
coastal state instability increases → P(coastal state crisis) ↑
```

**Pathway 2**: Sahel catastrophe → European migration pressure → EU politics
```
Sahel catastrophe → mass displacement → Mediterranean crossing attempts increase →
EU border pressure → political polarization → P(EU cohesion stress) ↑
```

**Pathway 3**: Sahel catastrophe → Jihadist consolidation → Transnational terrorism
```
Sahel catastrophe → ungoverned territory expands → jihadist groups consolidate →
training camps, resource extraction, governance experiments →
transnational terrorism capability ↑ → P(major attack) ↑
```

**Pathway 4**: Sahel catastrophe → Humanitarian system strain → Global response degradation
```
Sahel catastrophe → humanitarian funding demands spike → donor fatigue →
response capacity for other crises degraded → P(cascading humanitarian failures) ↑
```

---

## Transmission Channels

### Climate-Food Channel

**Mechanism**: Rainfall failure directly reduces agricultural output; Sahel is highly rain-dependent with minimal irrigation
**Affected regions**: Entire Sahel zone; urban populations dependent on rural food production
**Affected variables**: Food production, local food prices, nutrition indicators
**Differential exposure**: Rural populations produce food but have some subsistence buffer; urban poor are most vulnerable to price spikes

### Conflict-Displacement Channel

**Mechanism**: Jihadist violence and counter-insurgency operations drive displacement; displaced populations strain host areas
**Affected regions**: Rural conflict zones → urban centers → cross-border to coastal states
**Affected variables**: Displaced population, host area resources, urban infrastructure
**Notes**: Displacement is both symptom and cause of instability—displaced populations create pressure on receiving areas

### Governance-Collapse Channel

**Mechanism**: State failure removes service provision, security, dispute resolution; creates power vacuums for armed groups
**Affected regions**: State-controlled territory shrinks; ungoverned spaces expand
**Affected variables**: Territorial control, state service provision, conflict intensity
**Notes**: Governance collapse is self-reinforcing—state weakness invites challenges, challenges weaken state

### Humanitarian-Fatigue Channel

**Mechanism**: Sustained crisis exhausts donor funding; humanitarian system unable to scale indefinitely
**Affected regions**: Global (donor countries); Sahel (recipient)
**Affected variables**: Humanitarian funding, aid effectiveness, mortality averted
**Notes**: International system has limited capacity for sustained large-scale response in contested territory

### Coastal Contagion Channel

**Mechanism**: Instability spreads through borders via refugees, weapons flows, jihadist networks, and demonstration effects
**Affected regions**: Ghana, Côte d'Ivoire, Benin, Togo, northern Nigeria
**Affected variables**: Coastal state stability, conflict intensity, governance quality
**Notes**: Coastal West Africa has its own fragilities; Sahel catastrophe could trigger latent instability

---

## Historical Analogues

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| Sahel famine 1984-85 | Same region, climate-driven | Scale of mortality possible; population now 5× larger |
| Ethiopian famine 1983-85 | Climate + conflict | Conflict dramatically worsens famine outcomes |
| Somalia 1991-present | State collapse | Recovery from collapse takes decades |
| DRC ongoing | Multi-country regional crisis | Sustained crisis possible without resolution |
| Yemen 2015-present | Conflict + famine | Modern humanitarian system can't prevent catastrophe in active conflict |
| Syria 2011-present | State collapse, mass displacement | Refugee crisis can destabilize neighbors |
| Lake Chad Basin 2010s | Regional crisis, Boko Haram | Multi-country crisis in adjacent region |

---

## Early Warning Indicators

| Indicator | State Variable | Current Status | Warning Level |
|-----------|---------------|---------------|---------------|
| Climate vulnerability | `agricultural_climate_risk` | ~70/100 | >80 is danger zone |
| Food vulnerability | `food_import_dependence` | ~50% | >65% indicates high exposure |
| Conflict intensity | `internal_conflict_intensity` | 2-3 | 4 (major war) is catastrophe |
| Internal displacement | `idp_population` | ~3M | >6M indicates acceleration |
| Governance instability | `years_since_irregular_transition` | 1-2 years | <3 years is elevated risk |
| Transition attempts | `coup_attempts_10yr` | 4-5 | >3 indicates chronic instability |
| State capacity | `tax_revenue_gdp` | ~8-10% | <10% indicates weak state |
| Coastal spillover | `west_central_africa_other.protest_intensity_annual` | Currently stable | Rising intensity is warning |

---

## Critical Review Notes

**Critical review performed**: 2025-12-28

### Question 1: Is this actually a discontinuity?

**Assessment: Pass.**

The baseline includes chronic Sahel instability—coups, insurgencies, food insecurity, displacement at current levels. The event captures transition from "chronic dysfunction" to "acute regional catastrophe." This is a qualitative difference:
- Baseline: 25M food insecure, 3M displaced, localized conflict, humanitarian response managing
- Event: 40M+ food insecure, 10M+ displaced, region-wide famine, humanitarian response overwhelmed

This cannot be reached through gradual drift—it requires threshold crossing where multiple systems fail simultaneously.

### Question 2: Does the probability match the structure?

**Assessment: Pass.**

1.8%/year at current pressure ~55/100, with threshold at 68, implies we're closer to threshold than comfortable. The probability evolution section shows increasing risk over the simulation period as climate and demographic pressures compound.

Sanity check: ~37% cumulative probability over 25 years means "more likely than not to avoid, but not by much." Given the structural factors (climate, demographics, governance), this feels right.

### Question 3: Are the resolutions actually different?

**Assessment: Pass.**

| Branch | Scale | Mortality | Contagion |
|--------|-------|-----------|-----------|
| Regional Crisis | Contained | 500K-1M | Minimal |
| Humanitarian Catastrophe | Expanded | 2-5M | Coastal begins |
| Civilizational Collapse | Full regional | 5-15M | West Africa regional |

These produce qualitatively different world-states. The distinction between Regional Crisis and Humanitarian Catastrophe is primarily scale and contagion; between Humanitarian Catastrophe and Civilizational Collapse is duration and depth of collapse.

### Question 4: What's the strongest case against this specification?

**Case 1: The Sahel has always been in crisis, and it never quite collapses.**

The international humanitarian system has prevented mass famine in the Sahel since 1984-85. Even with coups, conflicts, and climate shocks, mortality has remained manageable. The "catastrophe" threshold may be unreachable because the international system will always intervene enough to prevent it.

*If this case is strong*: Lower catastrophe and collapse branch probabilities; increase Regional Crisis to 60-70%.

*Counter*: The structural trends (climate, demographics, governance) are worsening. The 2020s coups represent a new phase of governance collapse. Humanitarian fatigue is real. The system's capacity is not infinite. Yemen demonstrates that modern humanitarian system cannot prevent catastrophe in active conflict.

**Case 2: "Sahel catastrophe" is too vague—model individual country failures instead.**

Mali, Niger, Burkina Faso, Chad could each be modeled separately. Lumping them together may obscure dynamics and inflate probability.

*If this case is strong*: Create separate events for each country; this event becomes a compound probability of correlated country failures.

*Counter*: The region's dynamics are highly correlated—climate affects all countries simultaneously, jihadist networks cross borders, governance collapse is contagious. A regional event captures the correlation that separate events would miss. The entity model includes regional aggregates for this reason.

**Case 3: Great power competition may actually stabilize the region.**

Russia (Wagner/Africa Corps) and Western engagement create competing incentives to prevent collapse. Both sides prefer client states to ungoverned chaos. Competition may produce more resources and attention than neglect would.

*If this case is strong*: Lower probability by 0.2-0.3%/year; great power competition as stabilizing factor.

*Counter*: Great power competition has so far been destabilizing—Wagner's presence in Mali coincided with governance collapse; French withdrawal created vacuums. Competition produces unpredictable intervention patterns, not coordinated stabilization.

### Question 5: Would another analyst reach similar conclusions?

**Assessment: Pass with caveats.**

The derivation is auditable. Another analyst would likely agree on:
- Sahel is the world's most vulnerable region
- Compounding pressures are real and worsening
- Current trajectory is toward increased risk

Disagreement might be on:
- Whether "regional catastrophe" is the right frame vs. individual country analysis
- The specific probability (1.0-3.0% range covers reasonable disagreement)
- The severity branch distribution (how much does humanitarian system prevent worst outcomes?)

### Summary

| Question | Status | Notes |
|----------|--------|-------|
| 1. Discontinuity | ✅ Pass | Clear threshold between chronic dysfunction and catastrophe |
| 2. Probability-structure match | ✅ Pass | 1.8%/year at pressure 55/100, threshold 68 |
| 3. Resolution distinctiveness | ✅ Pass | Three branches differ in scale, mortality, contagion |
| 4. Case against | ✅ Stated | "Never quite collapses" is strongest objection |
| 5. Analyst agreement | ✅ Pass | Core assessment widely shared; disagreement on framing |

**Overall assessment**: Specification is complete for Level 1. Key questions for Level 2: climate model projections for Sahel rainfall; detailed jihadist capability assessment; humanitarian system capacity modeling; coastal state vulnerability analysis.

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-28
  review: complete
  upgrade: true
```

### Upgrade Rationale

Climate model projections for Sahel rainfall; jihadist group capability assessment; humanitarian system capacity analysis; coastal state vulnerability assessment.

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- ACLED conflict data (Sahel)
- IPC food security assessments
- UNHCR displacement statistics
- IPCC regional climate projections (West Africa)
- ICG Sahel reporting
- World Bank development indicators
- OCHA humanitarian response plans and funding data
- SIPRI data on military spending and arms flows
- Crisis Group reporting on jihadist groups (JNIM, ISGS)

## Open Questions

- **Climate trajectory**: Sahel rainfall models show high uncertainty; is trend toward more or less rain? How does climate variability change?
- **Jihadist evolution**: Will groups consolidate governance capacity or remain focused on insurgency? What is ceiling of territorial control?
- **Coastal state resilience**: How much stress can Ghana, Côte d'Ivoire, Benin absorb before destabilizing? What are their specific vulnerabilities?
- **Great power role**: Will Russia/Western competition stabilize or destabilize? Does competition produce resources or chaos?
- **Humanitarian system limits**: What is the actual capacity ceiling for sustained crisis response in contested territory?
- **Population dynamics**: Does extreme fertility persist or begin to decline? Timeline for demographic transition?
- **Regional aggregation**: Should this be one event or multiple country-specific events with correlation?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-28 | Initial Level 1 specification | Task 2.3 - regional coverage gap; highest-risk humanitarian zone |
| 2025-12-29 | Rescaled factor loadings to sum of squares = 1.0 | Normalization requirement |
| 2025-12-29 | Replaced pressure function variables with observables | Eliminated synthetic `governance_index`; mapped to state model variables per [[methodology/concepts/synthetic-variable-problem]] |
| 2025-12-29 | Updated impact vectors to use correct entities | Coastal states → `west_central_africa_other` aggregate; Europe → Italy/Spain/France; displacement → `idp_population`/`refugees_abroad`/`refugees_hosted` |
| 2025-12-29 | Updated early warning indicators to match state variables | Aligned with pressure function variables |
| 2025-12-31 | Variance allocation: scaled loadings to Type 2 target | Task 3.11 - loadings scaled by 0.59 to (ΛΩΛᵀ)ᵢᵢ = 0.65; the original loadings and their sum-of-squares line are restored above as prose |
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.17. Classification, probability, factor loadings, severity branches, impacts and research tables converted; all prose kept; the pre-allocation loadings removed on 2025-12-31 restored. Judgment calls: (1) enums — `domain: political` for "Political / Humanitarian", `onset: gradual` for "Gradual to Rapid", `confidence: medium` for "Medium-Low" (leading word, as severe-pandemic and fusion-commercialization did), wording kept in prose. (2) Pressure wrapped in `100 * (...)` with the capped/inverse transforms realized via two-argument `min()`; it gives 55.2 at the lower ends of the stated current values (~64 at the upper ends); the compiler's baseline check is skipped (country variables have no 2025 baselines). (3) `resolves_after: 10` for the three `until: resolved` conflict-intensity rows (rationale under the probability block). (4) Entities normalized to catalog IDs: `nigeria` → `nga`, `italy` → `ita`, `spain` → `esp`, `france` → `fra`. (5) `sahel.pop_total` is derived and cannot be targeted: replaced by `sahel.life_expectancy` −3 ± 1.5 years (mortality component; emigration already in `refugees_abroad`), decaying rather than permanent since the target is a flow. (6) Durability substitutions: `regime_dependent` → `until: resolved`; branch decay-to-floor durations, `shock_vulnerable` human development and the per-branch factor modifications stay in prose (schema v0.2 backlog); European migration "decaying" given the durability table's 8-year half-life. (7) `food_import_dependence` "+30% ± 15%" read as additive percentage points `[30, 15]`; `internal_conflict_intensity` "to 4" written as +1.5 ± 0.5 from the current 2-3. (8) The 2.5×/5.0× branch multipliers are not written as `inherit`/`scale`: 5 × −30% GDP is −150% and 2.5 × (−30% ± 15%) kills ~25% of runs on a multiplicative variable, and the multipliers overshoot the branch tables' own displacement totals; the three branches are explicit lists (multiplier applied literally to unbounded rows; displacement and mortality from the branch tables; `gdp_real`, `food_import_dependence`, conflict intensity and the collapse-branch protest row capped by their ranges — detailed under Differential Impacts). The original multipliers stay in prose. (9) Cascades: `triggers: []` — every target is a registry promotion (NIGERIA_STATE_FAILURE, COASTAL_WEST_AFRICA_DESTABILIZATION, EUROPEAN_MIGRATION_CRISIS), fold (GLOBAL_HUMANITARIAN_CAPACITY_CRISIS) or decline (GHANA_POLITICAL_CRISIS, COTE_DIVOIRE_INSTABILITY, MAGHREB_INSTABILITY) with no file yet, kept in the prose table; EU_COHESION_STRESS is not in the registry at all and is reported, not normalized. `triggered_by` added from EGYPT_STATE_FAILURE (+0.5%/yr) and AGRICULTURAL_YIELD_BREAKTHROUGH (−0.3%/yr), whose files declare those edges; AMOC_WEAKENING noted in prose (uncertain direction, no magnitude). (10) No unit conversions against global baselines were needed (no global-variable impact rows). Compiled variance 0.645 against the declared 0.65 |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/egypt-state-failure]] for comparable regional state failure | [[factors/f-ssa]] for Sub-Saharan Africa factor | [[factors/f-clim]] for climate factor*
