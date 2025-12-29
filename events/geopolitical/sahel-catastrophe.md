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

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | SAHEL_CATASTROPHE |
| **Scale** | Regional (multi-country) |
| **Domain** | Political / Humanitarian |
| **Causal Type** | Type 2: Threshold |
| **Onset Speed** | Gradual to Rapid (crisis builds over years, acute phase 1-3 years) |
| **Reversibility** | Partial (stabilization possible but long-term development setback) |

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

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Sahel catastrophe exhibits threshold dynamics:
- Multiple pressures accumulate over years: climate stress, governance decay, demographic pressure, conflict expansion
- System absorbs stress through humanitarian response, resilience, international support
- Threshold crossing occurs when multiple stressors spike simultaneously, overwhelming coping capacity
- No single actor decision (Type 3) or unpredictable shock (Type 1) dominates—this is pressure accumulation

### Pressure Function

The Sahel's pressure function integrates stress across multiple countries. Using regional aggregate indicators:

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `sahel.rainfall_anomaly` | 0.25 | threshold(-1.5σ) | Rainfall below -1.5 standard deviations triggers acute food crisis |
| `sahel.food_insecurity_population` | 0.25 | linear | Baseline ~25M; catastrophe threshold ~40M+ |
| `sahel.conflict_deaths_annual` | 0.20 | threshold(10000) | Sharp increase above 10K deaths/year indicates escalation |
| `sahel.displaced_population` | 0.15 | threshold(5M) | Current ~3M; catastrophe threshold ~10M+ |
| `sahel.governance_index` | 0.15 | inverse | Aggregate of coup events, territorial control loss |

**Pressure calculation**:
```
pressure = 0.25 × rainfall_anomaly_function(rainfall)
         + 0.25 × food_insecurity_population / 50M
         + 0.20 × conflict_deaths_threshold(deaths)
         + 0.15 × displaced_population / 10M
         + 0.15 × (100 - governance_index) / 100
```
*Normalized to 0-100 scale*

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

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.8% |
| **Low bound** | 1.0% |
| **High bound** | 3.0% |
| **Confidence** | Medium-Low |
| **25-year cumulative** | ~37% at point estimate |

### Current Pressure Estimate

Current pressure: ~55/100 (elevated and rising)
- `rainfall_anomaly`: Increasingly variable; 2024 below average in key zones
- `food_insecurity_population`: ~25-30M annually requiring assistance
- `conflict_deaths`: ~8,000-10,000/year (ACLED data); rising trend
- `displaced_population`: ~3M internally displaced; ~1M refugees
- `governance_index`: Very low; three coup governments; territorial control fragmented

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

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_SSA** | 0.75 | Primary regional factor; Sahel is core of Sub-Saharan stress |
| **F_CLIM** | 0.50 | Climate is existential for Sahel; rainfall determines food production |
| **F_FOOD** | 0.45 | Global food prices affect import-dependent urban populations; regional production critical |
| **F_GPT** | 0.20 | Great power competition affects intervention, support; Russia/Wagner presence |
| **F_HLTH** | 0.15 | Health system collapse amplifies mortality; disease outbreaks in displacement settings |
| **F_FIN** | 0.10 | Aid flows depend on donor fiscal space |
| F_MENA | 0.10 | Libya instability affects northern Mali; weapons flows |
| F_EUR | 0.05 | European migration concern drives some engagement |
| F_TECH | 0.00 | No significant pathway |
| F_EAS | 0.00 | No significant pathway |
| F_SAS | 0.00 | No significant pathway |
| F_LAM | 0.00 | No significant pathway |

**Sum of squared loadings**: 0.56 + 0.25 + 0.20 + 0.04 + 0.02 + 0.01 + 0.01 + 0.003 = 1.09

**Note**: Sum of squares slightly exceeds 1.0, indicating this event is highly exposed to correlated factor stress. This is intentional—Sahel catastrophe occurs precisely when multiple stressors align. For implementation, may need to rescale or accept as modeling choice reflecting extreme multi-factor vulnerability.

### Loading Interpretation (Type 2)

Factors shock state variables feeding the pressure function:
- High F_SSA → regional instability, conflict escalation → pressure rises
- High F_CLIM → rainfall failure, temperature stress → food production drops → pressure rises
- High F_FOOD → global food prices spike → import costs rise, humanitarian response strained → pressure rises
- High F_GPT → great power competition intensifies → intervention patterns shift, potentially destabilizing

---

## Severity Branches

Once threshold is crossed:

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

### Branch Probability Rationale

- **Regional Crisis (0.40)**: Most likely because international community will prioritize preventing worst outcomes; some state capacity remains even in collapsed states; localized coping mechanisms persist. Historical pattern is that Sahel crises remain "crises" rather than becoming "catastrophes" due to humanitarian response.

- **Humanitarian Catastrophe (0.40)**: High probability because current trajectory suggests response capacity is being overwhelmed; multiple simultaneous state failures already occurring; climate trends worsen the outlook; donor fatigue is real.

- **Civilizational Collapse (0.20)**: Lower but not negligible because the structural factors (climate, demographics, governance) are genuinely severe; 1984-85 occurred with smaller population and less conflict overlay; international system's ability to respond at scale in contested territory is limited.

---

## Impact Vector

### Sahel Regional Impacts (Baseline: Regional Crisis)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `sahel_aggregate.gdp_real` | ↓ | -30% ± 15% | gradual(3yr) | decaying (half_life: 12yr) |
| `sahel_aggregate.pop_total` | ↓ | -3% to -8% (mortality + emigration) | gradual(5yr) | permanent (mortality component) |
| `sahel_aggregate.food_import_dependence` | ↑ | +30% ± 15% | immediate | decaying (half_life: 10yr) |
| `sahel_aggregate.internal_conflict_intensity` | ↑ | to 4 (major war) | immediate | regime_dependent |
| Displaced population | ↑ | +10-15M | gradual(3yr) | decaying (half_life: 15yr) |
| Excess mortality | ↑ | 500K-1M | gradual(5yr) | permanent |

### Coastal West Africa Impacts

| Country/Region | Variable | Direction | Magnitude | Onset |
|----------------|----------|-----------|-----------|-------|
| Ghana | `regime_stability` | ↓ | -10 ± 5 | gradual(3yr) |
| Côte d'Ivoire | `regime_stability` | ↓ | -15 ± 8 | gradual(2yr) |
| Benin | `regime_stability` | ↓ | -15 ± 8 | gradual(2yr) |
| Togo | `regime_stability` | ↓ | -12 ± 6 | gradual(2yr) |
| Nigeria (north) | `internal_conflict_intensity` | ↑ | +0.5 ± 0.3 | gradual(2yr) |
| Coastal aggregate | Refugee population | ↑ | +2-5M | gradual(3yr) |

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| Global displaced persons | ↑ | +10-20M | gradual(3yr) | decaying |
| Humanitarian funding demand | ↑ | +$10-20B/year | immediate | duration of crisis |
| `europe.net_migration_rate` | ↑ | +0.1% ± 0.05% | gradual(5yr) | decaying |

### Differential Impacts by Severity Branch

| Branch | Impact Multiplier | Additional Effects |
|--------|-------------------|-------------------|
| Regional Crisis | 1.0× | Contained to Sahel; coastal states stressed but stable |
| Humanitarian Catastrophe | 2.5× | Coastal contagion begins; global humanitarian system strained |
| Civilizational Collapse | 5.0× | West Africa regional destabilization; global refugee crisis; jihadist expansion |

### Durability Specifications

| Impact Type | Durability | Parameters | Rationale |
|-------------|------------|------------|-----------|
| Mortality | permanent | N/A | Deaths cannot be undone |
| Displacement | decaying | half_life: 15yr | Return/resettlement very slow in conflict zones |
| Economic damage | decaying | half_life: 12yr | Development setback; infrastructure destruction |
| Human development | shock_vulnerable | Can be reversed by subsequent crises | Fragile gains |
| Territorial control | regime_dependent | Persists until governance restored | Jihadist consolidation |
| Coastal state pressure | decaying | half_life: 8yr | Pressure eases as crisis stabilizes |

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Coastal contagion | NIGERIA_NORTHERN_CRISIS | +1.5%/year | 15 years | Jihadist expansion; refugee pressure; governance demonstration effect |
| Coastal contagion | GHANA_POLITICAL_CRISIS | +1%/year | 10 years | Refugee burden; economic shock; security spillover |
| Coastal contagion | COTE_DIVOIRE_INSTABILITY | +1.5%/year | 10 years | History of instability; northern border exposure |
| European politics | EU_COHESION_STRESS | +0.3%/year | Duration of crisis | Migration politics |
| Jihadist expansion | MAGHREB_INSTABILITY | +0.5%/year | 15 years | Trans-Saharan networks; Libya corridor |
| Humanitarian system | GLOBAL_HUMANITARIAN_CAPACITY_CRISIS | +1%/year | Duration | System overwhelmed; donor fatigue |

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

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| Rainfall anomaly (seasonal) | Variable; 2024 below average in key zones | <-1.5σ is danger zone |
| Food insecurity population (IPC 3+) | ~25-30M | >40M is catastrophe threshold |
| Conflict deaths (ACLED annual) | ~8-10K | >15K indicates escalation |
| Internally displaced persons | ~3M | >6M indicates acceleration |
| Coup/transition events | 3 coup governments (Mali, Niger, Burkina Faso) | Additional coups, or coastal coups, is major warning |
| Humanitarian funding gap | ~50% funded | <40% funded indicates system strain |
| Jihadist territorial control | Significant rural areas | Urban capture or capital threats would be escalation |
| Coastal state indicators | Currently stable | Rising instability in Ghana, Côte d'Ivoire, Benin is warning |

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

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-28 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Climate model projections for Sahel rainfall; jihadist group capability assessment; humanitarian system capacity analysis; coastal state vulnerability assessment |

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

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/egypt-state-failure]] for comparable regional state failure | [[factors/f-ssa]] for Sub-Saharan Africa factor | [[factors/f-clim]] for climate factor*