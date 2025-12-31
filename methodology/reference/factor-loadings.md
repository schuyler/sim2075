---
title: factor-loadings
type: note
permalink: methodology/reference/factor-loadings
tags:
- methodology
- factors
- loadings
- correlation
- causal-types
- v2
---

# Factor Loadings

> **Important**: Factor loadings must satisfy a variance constraint based on causal type. See [[methodology/reference/variance-allocation]] before specifying loadings.

## What Factor Loadings Represent

Factor loadings quantify **how strongly an event correlates with latent risk factors**. They are not causal claims—they capture "when this factor is elevated, this event is more likely" without specifying direction of causation.

**Loadings are structured judgment, not empirical estimates.** We have no data on how events correlate with abstract factors. The loadings exist to:
- Ensure events that should cluster together do cluster in simulation
- Force explicit thinking about what drives each event
- Make correlation assumptions transparent and revisable

**Critical distinction**: Factors are latent constructs for dimensionality reduction and correlated event sampling. They are **not causal agents** that directly shock state variables. The relationship is:

```
Latent Factor → (captures underlying conditions) → Events cluster when factor elevated
Event fires → Impact vector → State variables change
```

Factors determine *which events tend to fire together*. The events themselves cause state variable changes through their impact vectors.

---

## Worked Example: Pakistan State Failure

This example traces the complete pathway from factors through event firing to state variable impacts, clarifying what factors do and don't do.

### The Event

**Pakistan State Failure** (Type 2: Threshold) fires in simulation year 2043.

### Factor Loadings Context

The event specification includes these factor loadings:

| Factor | Loading | Role |
|--------|---------|------|
| F_SAS | 0.71 | Primary—this IS the South Asian anchor crisis |
| F_FOOD | 0.42 | Indus water-agriculture nexus vulnerability |
| F_CLIM | 0.38 | Glacial melt, monsoon variability |
| F_FIN | 0.29 | Chronic fiscal crisis, IMF dependency |
| F_GPT | 0.21 | Great power dynamics affect aid flows |

### What the Loadings Mean

In the simulation year when this event fired:
- F_SAS was elevated (correlated factor draw was high)
- F_FOOD and F_CLIM were moderately elevated
- This made Pakistan State Failure more likely to fire *along with* other events loading on these factors

**The factors did NOT cause the state failure.** The elevated factor draws reflect that 2043 was a "bad year" for South Asian stability, food systems, and climate stress—conditions under which Pakistan's collapse became more probable.

Other events that might cluster in this same simulation run (due to shared factor loadings):
- India-Pakistan Conflict (also loads heavily on F_SAS)
- Bangladesh climate displacement (loads on F_SAS, F_CLIM)
- Global food price spike (loads on F_FOOD, F_CLIM)

### State Variable Impacts (From the Event, Not Factors)

When Pakistan State Failure fires, the **event's impact vector** changes state variables:

| Variable | Change | Source |
|----------|--------|--------|
| `pakistan.regime_stability` | → <20 | Event impact vector |
| `pakistan.gdp_real` | -40% | Event impact vector |
| `pakistan.internal_conflict_intensity` | → 4 (civil war) | Event impact vector |
| `nuclear_stability` | -15 points | Event impact vector |
| `india.gdp_real` | -2% | Event impact vector (spillover) |

These changes come from the event specification's impact vector—**not from the factors**. The factors only determined that this event was likely to fire alongside other correlated events.

### The Causal Chain

```
1. Factor draws: F_SAS=high, F_FOOD=moderate-high, F_CLIM=moderate-high
   ↓
2. Event probability elevated (Gaussian copula correlation)
   ↓
3. Event fires (random draw below elevated probability)
   ↓
4. Impact vector applied to state variables
   ↓
5. State variables change: regime_stability↓, gdp_real↓, conflict↑, etc.
```

Factors operate at step 1-2. State variable changes happen at step 4-5.

---

## Loading Scale

| Loading | Meaning |
|---------|---------|
| 0.0 | No meaningful relationship to this factor |
| 0.1 - 0.3 | Weak relationship; factor is marginally relevant |
| 0.4 - 0.6 | Moderate relationship; factor is one of several drivers |
| 0.7 - 0.8 | Strong relationship; factor is a primary driver |
| 0.85+ | Dominant relationship; event essentially expresses this factor |

**Don't over-differentiate.** The difference between 0.35 and 0.45 is not meaningful. Round to nearest 0.1.

---

## The 12 Factors

### Global Systemic Factors

| Factor | ID | Description |
|--------|-----|-------------|
| Climate Stress | F_CLIM | Temperature, extremes, tipping points |
| Financial Fragility | F_FIN | Credit, liquidity, contagion |
| Health/Pandemic | F_HLTH | Pathogen emergence, health systems |
| Great Power Tension | F_GPT | US-China-Russia competition |
| Technology Disruption | F_TECH | AI, cyber, critical infrastructure |
| Food System Stress | F_FOOD | Production, prices, distribution |

### Regional Factors

| Factor | ID | Description |
|--------|-----|-------------|
| European Stress | F_EUR | EU cohesion, fiscal, migration |
| MENA Instability | F_MENA | State fragility, conflict, resources |
| South Asian Stress | F_SAS | India-Pakistan, water, climate |
| East Asian Tension | F_EAS | Taiwan, Korea, South China Sea |
| Sub-Saharan Crisis | F_SSA | Sahel, demographics, fragility |
| Latin American Stress | F_LAM | Economic, political, Amazon |

---

## Factor Loadings by Causal Type

How factor loadings function depends on the event's causal type. This is a key insight from the integrated event-state framework.

### Type 1 (Stochastic) Events

**Interpretation**: Loadings capture shared vulnerability. When F_HLTH is elevated, both pandemic emergence AND health system collapse are more likely—not because one causes the other, but because both respond to the same underlying conditions.

**How loadings work**:
- Factor realization directly modulates event probability
- High factor draw → probability multiplied upward
- Loadings represent "exposure" to the factor

**Example**: Pandemic emergence
- Loads on F_HLTH (0.9): When global health conditions deteriorate, novel pathogen emergence is more likely
- Loads on F_SSA (0.3): African health infrastructure weakness creates emergence risk
- These aren't causal—they're correlated exposures

### Type 2 (Threshold) Events

**Interpretation**: Loadings identify which factors correlate with conditions that stress the pressure variables driving the event toward its threshold.

**How loadings work (v1.0)**:
- Loadings modulate probability like Type 1
- State conditioning adds a multiplier on top

**How loadings work (v2.0 target)**:
- Factor realizations shock pressure variables
- Pressure accumulation drives state toward threshold
- Event probability derived from state, not directly from factors
- Chain: Factor → Pressure Variable → State → Probability

**Example**: Pakistan state failure
- Loads on F_SAS (0.71): Regional stress correlates with regime instability
- Loads on F_CLIM (0.38): Climate stress correlates with water crisis conditions
- Loads on F_FIN (0.29): Financial stress correlates with fiscal pressure
- Each loading indicates "when this factor is elevated, conditions favor this event"

**Key difference from Type 1**: For Type 2, think "what factors correlate with pressure accumulation?" not "what factors make the event more likely in isolation?"

### Type 3 (Contingent) Events

**Interpretation**: Loadings may affect window probability and resolution probability differently.

**How loadings work**:
- Window opening may depend on certain factors (e.g., great power tension for conflict windows)
- Resolution probabilities may depend on different factors (e.g., institutional capacity for peaceful resolution)
- Consider specifying loadings for each stage if they differ substantially

**Example**: Taiwan crisis
- Window loadings: F_GPT (0.8), F_EAS (0.7) — tension creates crisis windows
- Resolution loadings: F_FIN (0.4) — economic interdependence affects resolution
- Peaceful resolution more likely when F_GPT is low at resolution time

**Practical guidance**: For v1.0, specify single loading set representing overall event correlation. Document any window vs. resolution differences in notes for v2.0 implementation.

---

## Revised Interpretation: Factors as Correlation Drivers (v2.0)

The v2.0 architecture reinterprets factor loadings for Type 2 events:

### Current Model (v1.0)

```
Factor Realization → Event Probability Adjustment
```

High F_CLIM → P(AMOC collapse) multiplied by factor loading

### Target Model (v2.0)

```
Factor Realization → Pressure Variable Shock → State Update → Event Probability
```

High F_CLIM → `global_temp_anomaly` shocked upward → `amoc_strength` declines → P(AMOC collapse) increases because closer to threshold

### Implications for Loading Specification

**v1.0**: Ask "how much more likely is this event when this factor is elevated?"

**v2.0**: Ask "which pressure variables does this factor correlate with, and how much does that matter for this event's threshold?"

For now (v1.0), specify loadings using the direct probability interpretation. Document the pressure pathway in notes for v2.0 migration:

```yaml
factor_loadings:
  F_CLIM: 0.85
  
loading_notes:
  v2_pressure_pathway: |
    F_CLIM correlates with elevated global_temp_anomaly and regional climate variables.
    For AMOC: temperature affects freshwater input rate, which drives
    amoc_strength toward collapse threshold.
```

---

## Factor → State Variable Mapping

Factor loadings connect events to abstract latent factors. But what do those factors *mean* in terms of the simulation's state variables? This section maps each factor to observable indicators and affected variables.

**Key distinction**:
- **Indicator Variables**: What we observe to infer that a factor is elevated (the factor's "symptoms")
- **Affected Variables**: What changes when events correlated with this factor fire (via event impact vectors, not factor causation)

**For v1.0:** This mapping helps specifiers reason about *why* an event loads on a factor—what underlying dynamics connect them. Factors currently drive event correlation, not state variables directly.

**For v2.0:** This mapping becomes operational. Factor realizations will shock indicator variables, which then drive event probabilities through threshold and conditioning mechanisms.

For full variable definitions and dynamics, see [[methodology/reference/state-specification]].

---

### F_CLIM: Climate Stress

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `global_temp_anomaly`, `climate_variability`, `arctic_sea_ice_sept`, `global_co2_ppm`
- Country: `water_stress`, `heat_exposure` (aggregated across climate-exposed countries)

**Affected Variables** (changed when F_CLIM-correlated events fire):
- Global: `amoc_strength`, `amazon_forest_cover`, `permafrost_integrity`, `sea_level_global`
- Country: `agricultural_climate_risk`, `gdp_real` (climate-exposed countries), `regime_stability` (climate-stressed states), `food_import_dependence`
- Commodity: `wheat_price`, `rice_price`, `corn_price`, `food_stocks_grains`

**Causal Pathway**: F_CLIM represents underlying climate stress conditions—the accumulated effect of warming, extreme weather frequency, and proximity to tipping points. When F_CLIM is elevated in a simulation run, events like AMOC weakening, Amazon tipping point, permafrost release, and climate-driven state failures (Pakistan, Egypt, Bangladesh) are more likely to fire together. The state variable impacts come from the events themselves: AMOC collapse affects `amoc_strength` and Northwest European climate; Amazon tipping affects `amazon_forest_cover` and regional precipitation; state failures affect `regime_stability` and `gdp_real` through their impact vectors.

**Cross-reference**: See state-specification §4.1 (Climate and Planetary Variables), §3.4 (Climate and Resource Variables), §4.2 (Commodity Price Variables).

---

### F_FIN: Financial Fragility

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `global_credit_spread`, `us_10yr_yield`, `us_real_rate`
- Country: `debt_public`, `debt_external`, `current_account`, `reserves_foreign` (aggregated stress indicators)

**Affected Variables** (changed when F_FIN-correlated events fire):
- Global: `usd_reserve_share`, `global_trade_volume`, `global_credit_spread`
- Country: `gdp_real`, `gdp_growth`, `inflation_rate`, `debt_external`, `reserves_foreign`, `regime_stability` (for fiscally fragile states)
- Commodity: Most commodity prices (demand channel)

**Causal Pathway**: F_FIN captures global financial system fragility—credit conditions, liquidity stress, and contagion potential. When F_FIN is elevated, events like global financial crises, emerging market debt crises, currency collapses, and financially-triggered state failures cluster together. A global financial crisis event changes `global_credit_spread`, country `gdp_growth`, and `debt_external` through its impact vector. An EM debt crisis changes specific country variables. The factor determines clustering; events determine state changes.

**Cross-reference**: See state-specification §4.3 (Financial System Variables), §3.2 (Economic Variables).

---

### F_HLTH: Health/Pandemic

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `antibiotic_resistance`, surveillance system quality (not directly modeled)
- Country: `life_expectancy`, `infant_mortality`, `state_capacity` (health system proxy)

**Affected Variables** (changed when F_HLTH-correlated events fire):
- Global: `pandemic_status`, `pandemic_severity`, `global_trade_volume` (disruption)
- Country: `life_expectancy`, `gdp_real`, `gdp_growth`, `regime_stability` (if severe)
- Demographic: Excess mortality affects population cohorts

**Causal Pathway**: F_HLTH represents health system stress and pathogen emergence risk—the conditions that make both novel pathogen emergence and health system collapse more likely. When F_HLTH is elevated, pandemic events, antibiotic resistance crises, and health-system-driven state instability cluster. A severe pandemic event changes `pandemic_status`, country `gdp_real`, and population variables through mortality. The factor reflects underlying vulnerability; the event causes the damage.

**Cross-reference**: See state-specification §4.6 (Health and Pandemic Variables), §3.1.2 (Demographic Flow Variables).

---

### F_GPT: Great Power Tension

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `us_china_tension`, `nato_cohesion`, `active_major_conflicts`, `nuclear_stability`
- Country: `sanctions_level` (for targeted countries), `alliance_west`, `alliance_china`

**Affected Variables** (changed when F_GPT-correlated events fire):
- Global: `us_china_tension`, `nato_cohesion`, `nuclear_stability`, `semiconductor_supply`, `global_trade_volume`
- Country: `external_conflict_involvement`, `sanctions_level`, `gdp_real` (war-affected), `regime_stability` (war-affected)

**Causal Pathway**: F_GPT captures US-China-Russia strategic competition intensity—the tension level that creates crisis windows and affects conflict resolution probabilities. When F_GPT is elevated, great power conflicts (Taiwan crisis, Korean peninsula), proxy conflicts, and sanctions escalations cluster. A Taiwan conflict event changes `us_china_tension`, `semiconductor_supply`, affected country `gdp_real`, and potentially `nuclear_stability`. The factor represents the competitive environment; events produce the state changes.

**Cross-reference**: See state-specification §4.7 (Geopolitical Structure Variables), §3.5 (Strategic Position Variables), §4.4 (Trade and Economic Structure Variables).

---

### F_TECH: Technology Disruption

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `ai_capability_index`, `semiconductor_supply` stress indicators
- Country: Technology adoption rates, cyber incident frequency (not directly modeled)

**Affected Variables** (changed when F_TECH-correlated events fire):
- Global: `semiconductor_supply`, `ai_capability_index`
- Country: `gdp_growth` (productivity channel), `institutional_quality` (governance challenges), `unemployment_rate` (labor disruption)

**Causal Pathway**: F_TECH represents technology disruption potential—rapid AI advancement, semiconductor supply concentration, and cyber vulnerability. When F_TECH is elevated, AI disruption events, semiconductor crises, and major cyber attacks cluster. These events change `semiconductor_supply`, country `gdp_growth` (through productivity shocks), and potentially `institutional_quality` (governance stress from rapid change). This factor has fewer specified events currently; its role may expand.

**Cross-reference**: See state-specification §4.5 (Technology Variables), §4.4 (Trade and Economic Structure Variables), §3.2.2 (Economic Flow Variables).

---

### F_FOOD: Food System Stress

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `wheat_price`, `rice_price`, `corn_price`, `fertilizer_price_index`, `food_stocks_grains`
- Country: `food_import_dependence` (for vulnerable importers), agricultural output indicators

**Affected Variables** (changed when F_FOOD-correlated events fire):
- Global: `wheat_price`, `rice_price`, `corn_price`, `food_stocks_grains`
- Country: `inflation_rate`, `regime_stability` (for food-import-dependent states), `gdp_real`

**Causal Pathway**: F_FOOD captures food system stress—production shortfalls, price spikes, and distribution failures. This factor is strongly correlated with F_CLIM (climate affects harvests) but also responds to conflict (Ukraine grain disruption), policy (export bans), and input costs (fertilizer). When F_FOOD is elevated, food price spike events, famine events, and food-security-driven instability cluster. A major food crisis event changes commodity prices and affected country `inflation_rate`, `regime_stability`, and potentially triggers state failure events in vulnerable importers (Egypt, Bangladesh).

**Cross-reference**: See state-specification §4.2 (Commodity Price Variables), §3.4 (Climate and Resource Variables), §3.3 (Political and Institutional Variables).

---

### F_EUR: European Stress

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `eu_cohesion`
- Country (European): `regime_stability`, `debt_public`, `gdp_growth`, `protest_activity`, `net_migration_rate`

**Affected Variables** (changed when F_EUR-correlated events fire):
- Global: `eu_cohesion`, `eur_reserve_share`
- Country (European): `regime_stability`, `gdp_real`, `debt_public`, `institutional_quality`
- Country (neighbors): `net_migration_rate` (migration pressure)

**Causal Pathway**: F_EUR captures European institutional and economic stress—EU cohesion challenges, fiscal crises, migration pressure, and political instability across member states. When F_EUR is elevated, EU fragmentation events, eurozone fiscal crises, and European political instability cluster. An EU fragmentation event changes `eu_cohesion`, affected country `gdp_real` and `regime_stability`. The factor reflects continental stress conditions; events produce specific state changes.

**Cross-reference**: See state-specification §4.7 (Geopolitical Structure Variables—`eu_cohesion`), §3.2 (Economic Variables), §3.3 (Political and Institutional Variables).

---

### F_MENA: MENA Instability

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `oil_brent`, `gas_europe_ttf` (supply disruption indicators)
- Country (MENA): `regime_stability`, `internal_conflict_intensity`, `water_stress`, `food_import_dependence`

**Affected Variables** (changed when F_MENA-correlated events fire):
- Global: `oil_brent`, `gas_europe_ttf`, `active_major_conflicts`
- Country (MENA): `regime_stability`, `gdp_real`, `internal_conflict_intensity`
- Country (Europe): `net_migration_rate` (refugee pressure)

**Causal Pathway**: F_MENA captures Middle East and North Africa instability—state fragility, sectarian conflict, resource stress, and regional power competition. When F_MENA is elevated, MENA state failures (Egypt, Saudi instability), regional conflicts, and oil supply disruptions cluster. An Egypt state failure event changes Egypt's `regime_stability` and `gdp_real`, affects `oil_brent` (Suez disruption), and increases European `net_migration_rate`. The factor represents regional volatility; events produce the impacts.

**Cross-reference**: See state-specification §4.2 (Commodity Price Variables—energy), §3.3 (Political and Institutional Variables), §3.4 (Climate and Resource Variables).

---

### F_SAS: South Asian Stress

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `nuclear_stability`
- Country (South Asia): `regime_stability`, `water_stress`, `internal_conflict_intensity`, `external_conflict_involvement`

**Affected Variables** (changed when F_SAS-correlated events fire):
- Global: `nuclear_stability`, `active_major_conflicts`
- Country (South Asia): `regime_stability`, `gdp_real`, `internal_conflict_intensity`, `external_conflict_involvement`
- Demographic: Population variables (excess mortality, displacement)

**Causal Pathway**: F_SAS captures South Asian stress—India-Pakistan rivalry, climate-water interactions, demographic pressure, and nuclear risk. When F_SAS is elevated, Pakistan state failure, India-Pakistan conflict, Bangladesh climate displacement, and regional instability cluster. Pakistan state failure changes Pakistan's state variables plus `nuclear_stability`; India-Pakistan conflict changes both countries' `external_conflict_involvement` and `gdp_real`. This is a high-consequence regional factor due to nuclear dimension.

**Cross-reference**: See state-specification §4.7 (Geopolitical Structure Variables—`nuclear_stability`), §3.3 (Political and Institutional Variables), §3.4 (Climate and Resource Variables), §3.5 (Strategic Position Variables).

---

### F_EAS: East Asian Tension

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `us_china_tension`, `semiconductor_supply`
- Country (East Asia): `external_conflict_involvement`, `alliance_west`, `alliance_china`, `trade_openness`

**Affected Variables** (changed when F_EAS-correlated events fire):
- Global: `us_china_tension`, `semiconductor_supply`, `global_trade_volume`
- Country (East Asia): `external_conflict_involvement`, `gdp_real`, `trade_openness`
- Country (global): Supply chain disruption affects manufacturing countries

**Causal Pathway**: F_EAS captures East Asian tension—Taiwan Strait dynamics, Korean peninsula risk, South China Sea disputes, and semiconductor supply concentration. When F_EAS is elevated, Taiwan conflict, Korean peninsula crisis, and regional military incidents cluster. A Taiwan conflict event changes `semiconductor_supply` (TSMC disruption), `us_china_tension`, and affected country `gdp_real`. F_EAS is correlated with F_GPT but captures regional dynamics distinct from global great power competition.

**Cross-reference**: See state-specification §4.4 (Trade and Economic Structure Variables—`semiconductor_supply`), §4.7 (Geopolitical Structure Variables), §3.5 (Strategic Position Variables).

---

### F_SSA: Sub-Saharan Crisis

**Indicator Variables** (what we observe to infer factor elevation):
- Country (SSA): `regime_stability`, `internal_conflict_intensity`, `food_import_dependence`, `net_migration_rate` (emigration)

**Affected Variables** (changed when F_SSA-correlated events fire):
- Country (SSA): `regime_stability`, `gdp_real`, `internal_conflict_intensity`, `life_expectancy`
- Demographic: Population variables (excess mortality, displacement)
- Global: Commodity prices (for major exporters like Nigeria)

**Causal Pathway**: F_SSA captures Sub-Saharan African crisis conditions—state fragility, climate stress, demographic pressure, and humanitarian emergencies. When F_SSA is elevated, Sahel catastrophe, Nigerian instability, Ethiopian crisis, and DRC collapse cluster. A Sahel catastrophe event changes regional `regime_stability`, produces massive displacement, and affects `life_expectancy` through excess mortality. This factor primarily affects humanitarian outcomes rather than global economic variables.

**Cross-reference**: See state-specification §3.3 (Political and Institutional Variables), §3.1 (Demographic Variables), §3.4 (Climate and Resource Variables).

---

### F_LAM: Latin American Stress

**Indicator Variables** (what we observe to infer factor elevation):
- Global: `amazon_forest_cover` (Brazil policy indicator)
- Country (LAM): `regime_stability`, `gdp_growth`, `inflation_rate`, `debt_public`

**Affected Variables** (changed when F_LAM-correlated events fire):
- Global: `amazon_forest_cover` (if Brazil involved)
- Country (LAM): `regime_stability`, `gdp_real`, `inflation_rate`, `debt_external`

**Causal Pathway**: F_LAM captures Latin American stress—economic volatility, political instability, and (for Brazil) global climate stakes via Amazon deforestation. When F_LAM is elevated, Argentine default, Venezuelan further collapse, Brazilian political crisis, and regional instability cluster. A Brazilian political crisis event could accelerate Amazon deforestation (changing `amazon_forest_cover`) while affecting Brazil's `gdp_real` and `regime_stability`. This factor has moderate global impact primarily through the Amazon pathway.

**Cross-reference**: See state-specification §4.1 (Climate and Planetary Variables—`amazon_forest_cover`), §3.2 (Economic Variables), §3.3 (Political and Institutional Variables).

---

## Using the Factor-Variable Mapping

When assigning factor loadings to an event:

1. **Identify which state variables the event directly affects** (its impact vector targets)
2. **Check which factors have those variables in their "Affected Variables" lists**
3. **Factors whose affected variables overlap with the event's impacts should have non-zero loadings**
4. **The strength of loading reflects how central that factor is to the event's causal mechanism**
5. **Also consider indicator variables**: If the event's preconditions are captured by a factor's indicators, that suggests correlation

If an event affects variables outside all factors' affected variable lists, either:
- The event has high idiosyncratic variance (Ψ), or
- A factor's variable coverage should be reconsidered

---

## Loading Estimation Process

### Step 1: Identify Causal Type

Before assigning loadings, confirm the event's causal type. This determines how to interpret the loadings.

### Step 2: Identify the Primary Factor

Ask: "If I could only load this event on one factor, which would it be?"

- For Type 1: What shared vulnerability matters most?
- For Type 2: What factor's indicator variables best capture the pressure conditions?
- For Type 3: What factor most strongly creates crisis windows?

Consult the **Factor → State Variable Mapping** sections above. Which factor's affected variables best overlap with the event's impact targets and causal mechanisms?

This forces clarity about what fundamentally drives the event.

### Step 3: Identify Secondary Linkages

For each factor, ask:
- Is there a plausible mechanism linking this factor to the event?
- Is the linkage direct or indirect?
- Would the event be noticeably more likely when this factor is elevated?

For Type 2, also ask:
- Does this factor's indicator variables capture conditions that stress the event's pressure variables?
- How strong is the correlation between factor elevation and pressure accumulation?

Assign secondary loadings only where genuine linkage exists. **Zero is a valid loading.**

### Step 4: Check the Variance Constraint

**The correct constraint** is based on factor-explained variance including factor correlations:

```
(ΛΩΛᵀ)ᵢᵢ = target for event's causal type
```

Where target depends on causal type (see [[methodology/reference/variance-allocation]]):
- Type 1: 0.70 – 0.80
- Type 2: 0.60 – 0.70
- Type 3: 0.40 – 0.50
- Type 4: 0.50 – 0.60

**Why simple sum-of-squared-loadings is insufficient**: When factors are correlated, factor-explained variance includes cross-terms:

```
(ΛΩΛᵀ)ᵢᵢ = Σⱼλᵢⱼ² + 2·Σⱼ<ₖ λᵢⱼ·λᵢₖ·Ωⱼₖ
```

The cross-terms add variance when an event loads on multiple correlated factors. An event with simple Σλ² = 0.80 might have true (ΛΩΛᵀ)ᵢᵢ = 1.20 after accounting for factor correlations.

**The workflow**:
1. Specify *relative* loadings (which factors, relative magnitudes)
2. Compute (ΛΩΛᵀ)ᵢᵢ for those loadings using the factor correlation matrix Ω
3. Compute scale factor: s = √(target / current)
4. Scale all loadings: λ'ᵢⱼ = s × λᵢⱼ
5. Verify scaled loadings achieve target

**Interpretation**: The scaled loadings represent factor *correlations*, not causal strengths. A Type 3 event with F_EAS = 0.38 (after scaling) says "this event correlates moderately with East Asian tension, but factors only explain ~45% of its occurrence—the rest is irreducibly uncertain."

### Step 5: Cross-Validate

Compare loading patterns across similar events:
- Do all MENA state failures have similar patterns?
- Do all climate events load heavily on F_CLIM?
- Do Type 2 events with similar pressure variables have similar loadings?
- Are there inconsistencies?

---

## Common Patterns by Causal Type

### Type 1 Patterns

**Pandemic/Health Events**
```
F_HLTH: 0.85 - 0.90 (dominant)
Regional factors: 0.2 - 0.3 (emergence location)
F_FIN: 0.1 - 0.2 (economic disruption correlation)
```

**Idiosyncratic Financial Crises**
```
F_FIN: 0.80 - 0.90 (dominant)
Regional factors: 0.2 - 0.4 (contagion exposure)
```

### Type 2 Patterns

**Climate Threshold Events** (AMOC, Amazon, permafrost)
```
F_CLIM: 0.80 - 0.90 (primary—indicator variables capture threshold approach)
F_FOOD: 0.2 - 0.4 (if agricultural feedback)
Regional: 0.1 - 0.3 (regional exposure variation)
```

Rationale: Climate stress indicators directly capture threshold approach; loadings reflect which factors' elevation correlates with faster approach.

**State Failure Events**
```
Regional factor: 0.70 - 0.85 (dominant—captures regional instability conditions)
F_CLIM or F_FOOD: 0.3 - 0.5 (for climate-stressed states)
F_FIN: 0.2 - 0.4 (fiscal pressure correlation)
F_GPT: 0.1 - 0.3 (if great power involvement)
```

Rationale: Regional instability is primary correlate; climate/food/financial stress are secondary pressure correlates.

**Economic Threshold Events** (hyperinflation, currency crisis)
```
F_FIN: 0.75 - 0.85 (primary—indicator variables capture financial stress)
Regional factor: 0.3 - 0.5 (regional contagion)
F_GPT: 0.1 - 0.3 (if sanctions/geopolitical exposure)
```

### Type 3 Patterns

**Deliberate Conflict Events** (Taiwan, Korea, India-Pakistan)
```
F_GPT: 0.60 - 0.80 (window driver—tension creates crisis opportunities)
Regional factor: 0.50 - 0.70 (local dynamics)
F_FIN: 0.2 - 0.4 (economic interdependence affects resolution)
```

Rationale: Great power tension and regional dynamics create windows; resolution depends on additional factors.

**International Agreement Events** (climate, arms control)
```
F_GPT: 0.4 - 0.6 (tension reduces agreement probability)
F_CLIM: 0.3 - 0.5 (for climate agreements—urgency driver)
Regional factors: 0.2 - 0.4 (regional buy-in requirements)
```

Note: For agreements, high factor values may *reduce* positive resolution probability. Document this in loading rationale.

---

## Documentation Requirements

| Field | Description |
|-------|-------------|
| **All 12 loadings** | Numerical values, rounded to nearest 0.1 |
| **Sum of squares** | Must be ≤ 1.0 |
| **Primary factor** | Which factor dominates and why |
| **Loading rationale** | Brief justification for non-zero loadings |
| **Similar events** | Other events with similar patterns for consistency check |
| **Causal type context** | How loadings relate to event's causal mechanism |

For Type 2 events, also document:

| Field | Description |
|-------|-------------|
| **Indicator correlation** | Which factor indicator variables correlate with event's pressure variables |
| **v2.0 notes** | How loadings will translate to pressure driver model |

For Type 3 events, also document:

| Field | Description |
|-------|-------------|
| **Window vs resolution** | Whether loadings differ by stage (for v2.0) |

---

## Implementation Notes

### v1.0 Implementation

All event types use factor loadings the same way:
1. Draw correlated factor realizations
2. Convert to correlated uniform draws via factor copula
3. Compare to probability threshold (adjusted for Type 2 state conditioning)

Loadings determine correlation structure regardless of causal type.

### v2.0 Implementation (Target)

Type 2 events will use loadings differently:
1. Factor realizations shock indicator variables (not probability directly)
2. State evolves based on indicator shocks + baseline dynamics
3. Event probability computed from state position relative to threshold
4. Factor correlation still produces event clustering (via correlated indicator shocks)

Type 1 and Type 3 continue using loadings for direct probability correlation.

---

## Migration Checklist

When upgrading an event specification from v1 to v2:

- [ ] Confirm causal type classification
- [ ] For Type 2: Document which indicator variables each loaded factor correlates with
- [ ] For Type 2: Estimate factor → indicator transmission strength
- [ ] For Type 3: Note if window vs resolution loadings should differ
- [ ] Verify loading patterns are consistent with similar events
- [ ] Update loading rationale to reflect type-specific interpretation