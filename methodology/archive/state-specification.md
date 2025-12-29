---
permalink: methodology/reference/state-specification
---

# Geopolitical Monte Carlo Simulation: State Specification

## A Comprehensive Inventory of Entities, Variables, and Outputs

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)  
**Companion Documents:** 
- `geopolitical-monte-carlo-methodology.md` — Discontinuity event modeling and factor structure
- `collapse-patterns-predictive-framework.md` — Historical collapse patterns and risk parameters
- `21st_century_assessment.md` — Regional trajectory assessments

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Entity Inventory](#2-entity-inventory)
3. [Country-Level State Variables](#3-country-level-state-variables)
4. [Global State Variables](#4-global-state-variables)
5. [Variable Dynamics Classification](#5-variable-dynamics-classification)
6. [Transmission Mechanisms](#6-transmission-mechanisms)
7. [Outputs and Assessments](#7-outputs-and-assessments)
8. [Open Questions and Future Work](#8-open-questions-and-future-work)
9. [Appendices](#9-appendices)

---

## 1. Executive Summary

### 1.1 Purpose

This document specifies the complete state space for a Monte Carlo simulation of geopolitical trajectories through 2075. The simulation generates probability distributions of outcomes for countries, regions, and the global system by:

1. Tracking **state variables** that evolve over time for 40 individually-modeled countries, regional aggregates, and the global commons
2. Sampling **discontinuity events** that shock the system (per companion methodology document)
3. Modeling **transmission mechanisms** through which shocks propagate
4. Producing **distributional outputs** across thousands of simulation runs

### 1.2 Scope

| Dimension | Coverage |
|-----------|----------|
| **Time horizon** | 2025-2075 (50 years) |
| **Time step** | Annual |
| **Individual countries** | 40 |
| **Regional aggregates** | 12 (6 Tier 1, 6 Tier 2) |
| **Country-level variables** | ~45 per entity |
| **Global variables** | ~48 |
| **Simulation runs** | 10,000-50,000 for stable distributions |

### 1.3 Coverage Statistics

The 40-country model captures:

| Metric | Coverage |
|--------|----------|
| World GDP | ~85% |
| World Population | ~74% |
| Nuclear States | 9 of 9 (100%) |
| G7 | 7 of 7 (100%) |
| G20 | 19 of 19 country members (100%) |
| BRICS (2024 expansion) | 10 of 10 (100%) |
| UN Security Council Permanent Members | 5 of 5 (100%) |

### 1.4 Design Philosophy

**Granularity where it matters:** Demographics are tracked at cohort level because they drive fiscal capacity, labor supply, instability risk, and military potential. Economic variables are tracked at sufficient detail to model debt dynamics and external vulnerability.

**Global commons explicitly modeled:** Climate, commodity prices, and financial system variables are tracked globally because they affect countries differentially and cannot be attributed to any single nation.

**Events as shocks to state:** The discontinuity event model (companion document) generates discrete shocks; this state specification defines what gets shocked and how the system evolves between shocks.

**Outputs support both terminal assessment and distributional analysis:** The simulation produces full state vectors at any time point, enabling both "what does 2050 look like in this run?" and "what is the distribution of outcomes across runs?"

---

## 2. Entity Inventory

### 2.1 The 40 Countries

Countries selected to capture 85% of world GDP, 74% of world population, all nuclear states, all major regional powers, and key strategic chokepoints/nodes.

#### North America (3)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **United States** | 340 | 28.0 | Global hegemon, reserve currency issuer, NATO anchor |
| **Canada** | 40 | 2.1 | G7, climate refuge potential, US economic integration |
| **Mexico** | 130 | 1.8 | US migration pressure, nearshoring destination, G20 |

#### Europe (8)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Germany** | 84 | 4.5 | EU anchor, industrial economy, energy transition leader |
| **United Kingdom** | 68 | 3.5 | Nuclear state, financial center, post-Brexit trajectory |
| **France** | 68 | 3.0 | Nuclear state, EU co-leader, African ties |
| **Italy** | 59 | 2.3 | G7, EU fiscal stress case, Mediterranean migration |
| **Spain** | 48 | 1.6 | Mediterranean economy, Latin American ties |
| **Netherlands** | 18 | 1.1 | Trade hub, below sea level (climate), EU core |
| **Poland** | 38 | 0.8 | Largest Eastern EU member, NATO frontline, demographic stress |
| **Ukraine** | 37 | 0.2 | Active conflict zone, European security pivot, grain exporter |

#### East Asia (5)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **China** | 1,425 | 18.0 | Primary US rival, demographic crisis, BRICS anchor |
| **Japan** | 124 | 4.2 | G7, demographic pioneer, US ally, China neighbor |
| **South Korea** | 52 | 1.7 | Extreme low fertility, semiconductor producer, divided peninsula |
| **Taiwan** | 24 | 0.8 | Semiconductor chokepoint (TSMC), most likely great power flashpoint |
| **North Korea** | 26 | 0.03 | Nuclear state, Korean peninsula wildcard, potential collapse |

#### South Asia (3)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **India** | 1,440 | 3.9 | Largest population, demographic dividend, BRICS, non-aligned rising power |
| **Pakistan** | 240 | 0.4 | Nuclear state, climate-fragile, India rival, Afghan border |
| **Bangladesh** | 175 | 0.5 | Climate existential risk (sea level), garment economy, density extreme |

#### Southeast Asia (5)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Indonesia** | 280 | 1.4 | Largest SE Asian economy, archipelagic, BRICS, G20 |
| **Vietnam** | 100 | 0.4 | Manufacturing growth, China alternative, BRICS partner |
| **Thailand** | 72 | 0.5 | Regional hub, aging demographics, BRICS partner |
| **Philippines** | 117 | 0.5 | US ally, South China Sea claimant, remittance dependent |
| **Singapore** | 6 | 0.5 | Financial hub, Malacca Strait chokepoint, ASEAN anchor |

#### Central Asia (1)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Kazakhstan** | 20 | 0.3 | Central Asian anchor, Russia-China buffer, energy exporter, BRICS partner |

#### West/Central Asia (2)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Iran** | 90 | 0.4 | Nuclear threshold state, BRICS, sanctions case, regional power |
| **Turkey** | 85 | 1.1 | NATO member, regional power, migration gateway, BRICS aspirant |

#### Middle East (4)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Saudi Arabia** | 36 | 1.1 | OPEC leader, petrodollar anchor, BRICS, de-dollarization actor |
| **Egypt** | 105 | 0.4 | Largest Arab state, Suez Canal, Nile dependent, BRICS |
| **Israel** | 9 | 0.5 | Nuclear state, regional flashpoint, US ally |
| **UAE** | 10 | 0.5 | Financial hub, logistics center, remittance source, BRICS |

#### Sub-Saharan Africa (5)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Nigeria** | 230 | 0.5 | Largest African population, oil producer, demographic giant |
| **Ethiopia** | 126 | 0.15 | BRICS, Nile upstream, East African anchor, high fragility |
| **DR Congo** | 100 | 0.07 | Critical minerals, chronic instability, population giant |
| **South Africa** | 60 | 0.4 | BRICS, only industrialized African economy, regional anchor |
| **Kenya** | 55 | 0.1 | East African economic hub, regional stabilizer |

#### Latin America (2)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Brazil** | 215 | 2.2 | BRICS founder, Amazon custodian, regional anchor, G20 |
| **Argentina** | 46 | 0.6 | G20, chronic crisis case, Southern Cone anchor |

#### Oceania (1)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Australia** | 26 | 1.7 | G20, US ally, Pacific anchor, climate refuge potential |

#### Eurasia (1)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Russia** | 144 | 2.0 | Nuclear superpower, energy exporter, BRICS, Ukraine conflict |

---

### 2.2 Regional Aggregates

For areas not covered by the 40 individual countries, regional aggregates track population, economic activity, and humanitarian outcomes.

#### Tier 1 Aggregates (Full State Variable Treatment)

These aggregates are populous enough or strategically important enough to require demographic structure and economic detail comparable to individual countries.

| Aggregate | Countries Included | Pop (M) | GDP ($T) | Rationale |
|-----------|-------------------|---------|----------|-----------|
| **Gulf States** | Kuwait, Qatar, Bahrain, Oman | 15 | 0.5 | Remittance source, energy, UAE spillover |
| **Central America** | Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica, Panama | 55 | 0.4 | US migration pressure, humanitarian outcomes |
| **Sahel** | Mali, Niger, Burkina Faso, Chad, Mauritania, Senegal | 100 | 0.15 | Highest-risk humanitarian zone |
| **East Africa** | Tanzania, Uganda, Somalia, Sudan, South Sudan, Rwanda, Burundi, Eritrea | 200 | 0.3 | Climate displacement, fragility cluster |
| **Rest of EU** | Belgium, Austria, Sweden, Denmark, Finland, Ireland, Portugal, Greece, Czechia, Romania, Hungary, others | 130 | 3.0 | EU fiscal/political dynamics |
| **Levant/Iraq** | Iraq, Syria, Jordan, Lebanon | 75 | 0.3 | Ongoing instability, refugee dynamics |

**Tier 1 total: 6 aggregates, ~575M population, ~$4.65T GDP**

#### Tier 2 Aggregates (Simplified Treatment)

These aggregates track population, GDP, and key stress indicators but not full demographic structure.

| Aggregate | Countries Included | Pop (M) | GDP ($T) | Primary Purpose |
|-----------|-------------------|---------|----------|-----------------|
| **Central Asia (other)** | Uzbekistan, Tajikistan, Kyrgyzstan, Turkmenistan | 60 | 0.15 | Water crisis, spillover from Kazakhstan |
| **Southeast Asia (other)** | Myanmar, Malaysia, Cambodia, Laos | 100 | 0.7 | Regional contagion, ASEAN dynamics |
| **Andean/Caribbean** | Colombia, Peru, Chile, Venezuela, Ecuador, Bolivia, Caribbean states | 180 | 1.2 | Venezuela spillover, regional economics |
| **Maghreb** | Morocco, Algeria, Tunisia, Libya | 110 | 0.5 | EU migration transit, gas supply |
| **Southern Africa (other)** | Zimbabwe, Zambia, Mozambique, Angola, Botswana, others | 150 | 0.4 | South Africa spillover, climate |
| **West/Central Africa (other)** | Ghana, Côte d'Ivoire, Cameroon, others (ex-Nigeria, Ethiopia, DRC) | 300 | 0.6 | Demographics, climate, fragility |

**Tier 2 total: 6 aggregates, ~900M population, ~$3.55T GDP**

#### Coverage Summary

| Category | Population (M) | % World | GDP ($T) | % World |
|----------|---------------|---------|----------|---------|
| 40 Individual Countries | 5,900 | 74% | 89 | 85% |
| Tier 1 Aggregates | 575 | 7% | 4.7 | 4% |
| Tier 2 Aggregates | 900 | 11% | 3.5 | 3% |
| **Model Total** | **7,375** | **92%** | **97.2** | **92%** |
| Unmodeled Remainder | 625 | 8% | 8 | 8% |

---

## 3. Country-Level State Variables

Each of the 40 countries tracks the following state variables. Tier 1 regional aggregates track the same variables. Tier 2 aggregates track a subset (marked with †).

### 3.1 Demographic Variables

#### 3.1.1 Population Stocks (12 variables)

Compressed population pyramid by sex and functional age cohort.

| Variable ID | Description | Units |
|-------------|-------------|-------|
| `pop_0_14_m` | Male children (0-14) | Millions |
| `pop_0_14_f` | Female children (0-14) | Millions |
| `pop_15_34_m` | Male young working age (15-34) | Millions |
| `pop_15_34_f` | Female young working age (15-34) | Millions |
| `pop_35_54_m` | Male prime working age (35-54) | Millions |
| `pop_35_54_f` | Female prime working age (35-54) | Millions |
| `pop_55_64_m` | Male older working age (55-64) | Millions |
| `pop_55_64_f` | Female older working age (55-64) | Millions |
| `pop_65_79_m` | Male young elderly (65-79) | Millions |
| `pop_65_79_f` | Female young elderly (65-79) | Millions |
| `pop_80_plus_m` | Male old elderly (80+) | Millions |
| `pop_80_plus_f` | Female old elderly (80+) | Millions |

**Derived indicators** (computed, not stored):
- `pop_total`: Sum of all cohorts
- `pop_working_age`: 15-64 cohorts
- `dependency_ratio`: (0-14 + 65+) / (15-64)
- `youth_bulge_index`: (15-34) / (15+)
- `median_age`: Estimated from cohort distribution
- `military_age_males`: `pop_15_34_m`
- `sex_ratio_reproductive`: `pop_15_49_m` / `pop_15_49_f`

#### 3.1.2 Demographic Flow Variables (5 variables)

| Variable ID | Description | Units |
|-------------|-------------|-------|
| `tfr` † | Total fertility rate | Children per woman |
| `life_expectancy` † | Life expectancy at birth | Years |
| `infant_mortality` | Infant mortality rate | Deaths per 1,000 live births |
| `net_migration_rate` † | Net migration as share of population | % per year |
| `emigration_skilled_rate` | Emigration rate of skilled workers (15-34 educated) | % per year |

---

### 3.2 Economic Variables

#### 3.2.1 Economic Stock Variables (6 variables)

| Variable ID | Description | Units |
|-------------|-------------|-------|
| `gdp_real` † | Real GDP (2025 base) | $T |
| `gdp_per_capita` † | Real GDP per capita (2025 base) | $K |
| `debt_public` | Public debt | % of GDP |
| `debt_external` | External debt | % of GDP |
| `reserves_foreign` | Foreign exchange reserves | Months of imports |
| `current_account` | Current account balance | % of GDP |

**Derived indicators**:
- `debt_service_ratio`: Annual debt service / government revenue
- `fiscal_space`: Composite of debt, reserves, current account
- `default_probability`: Derived from debt dynamics

#### 3.2.2 Economic Flow Variables (4 variables)

| Variable ID | Description | Units |
|-------------|-------------|-------|
| `gdp_growth` † | Real GDP growth rate | % per year |
| `inflation_rate` † | Consumer price inflation | % per year |
| `unemployment_rate` | Unemployment rate | % of labor force |
| `fdi_net` | Net foreign direct investment | % of GDP |

#### 3.2.3 Economic Structure Variables (5 variables)

| Variable ID | Description | Units |
|-------------|-------------|-------|
| `gdp_share_agriculture` | Agriculture share of GDP | % |
| `gdp_share_industry` | Industry share of GDP | % |
| `gdp_share_services` | Services share of GDP | % |
| `export_concentration` | Export concentration (Herfindahl index) | 0-1 |
| `trade_openness` | Trade openness (exports + imports) | % of GDP |

---

### 3.3 Political and Institutional Variables

| Variable ID | Description | Units | Notes |
|-------------|-------------|-------|-------|
| `regime_stability` | Regime stability index | 0-100 | Higher = more stable |
| `institutional_quality` | Institutional quality (WGI-style composite) | -2.5 to +2.5 | Higher = better |
| `corruption_index` | Corruption perceptions | 0-100 | Higher = less corrupt |
| `civil_liberties` | Civil liberties index | 0-100 | Higher = more free |
| `state_capacity` | State capacity/effectiveness | 0-100 | Ability to implement policy |
| `internal_conflict_intensity` † | Internal conflict intensity | 0-4 | 0=none, 4=civil war |
| `protest_activity` | Protest/unrest activity level | 0-100 | Higher = more unrest |
| `regime_type` | Regime type categorical | Categorical | Democracy/Hybrid/Authoritarian |

**Derived indicators**:
- `fragility_score`: Composite of stability, institutional quality, conflict
- `regime_change_probability`: Derived from stability trajectory

---

### 3.4 Climate and Resource Variables

| Variable ID | Description | Units | Notes |
|-------------|-------------|-------|-------|
| `water_stress` | Water stress index | 0-100 | Higher = more stressed |
| `heat_exposure` | Heat exposure index (wet-bulb risk) | 0-100 | Higher = more dangerous |
| `agricultural_climate_risk` | Agricultural climate vulnerability | 0-100 | Yield variability, drought risk |
| `sea_level_exposure` | Population exposed to sea level rise | % of total | Coastal vulnerability |
| `energy_import_dependence` | Net energy imports | % of consumption | Negative = exporter |
| `food_import_dependence` | Net food imports | % of consumption | Negative = exporter |

**Derived indicators**:
- `climate_vulnerability_composite`: Weighted combination of above
- `resource_security_index`: Composite of energy, food, water

---

### 3.5 Strategic Position Variables

| Variable ID | Description | Units | Notes |
|-------------|-------------|-------|-------|
| `alliance_west` | Western alliance alignment | 0-100 | NATO/US alignment |
| `alliance_china` | China alignment | 0-100 | SCO/BRI integration |
| `alliance_nonaligned` | Non-aligned position | 0-100 | Neither bloc |
| `sanctions_level` | Sanctions severity | 0-100 | 0=none, 100=comprehensive |
| `nuclear_status` | Nuclear weapons status | Categorical | None/Threshold/Possessed |
| `military_spending` | Military expenditure | % of GDP | Defense burden |
| `external_conflict_involvement` | External conflict involvement | 0-4 | 0=none, 4=major war |

**Derived indicators**:
- `geopolitical_risk_premium`: Derived from conflict, sanctions, alignment
- `alliance_reliability`: How much entity can count on allies

---

### 3.6 Summary: Country-Level State Variables

| Category | Variables | Tier 1 Aggregates | Tier 2 Aggregates |
|----------|-----------|-------------------|-------------------|
| Demographic stocks | 12 | 12 | 4 (totals only) |
| Demographic flows | 5 | 5 | 3 |
| Economic stocks | 6 | 6 | 3 |
| Economic flows | 4 | 4 | 2 |
| Economic structure | 5 | 5 | 0 |
| Political/institutional | 8 | 8 | 3 |
| Climate/resource | 6 | 6 | 3 |
| Strategic position | 7 | 7 | 2 |
| **Total** | **53** | **53** | **20** |

**Total country-level state variables:**
- 40 countries × 53 variables = 2,120
- 6 Tier 1 aggregates × 53 variables = 318
- 6 Tier 2 aggregates × 20 variables = 120
- **Grand total: 2,558 country/regional variables**

---

## 4. Global State Variables

Variables that affect multiple countries simultaneously and cannot be attributed to any single nation.

### 4.1 Climate and Planetary Variables (8 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `global_temp_anomaly` | Global mean temperature above pre-industrial | °C | 1.3 | Slow drift +0.03/yr |
| `sea_level_global` | Global mean sea level above 2000 baseline | cm | 10 | Slow drift +0.4/yr accelerating |
| `arctic_sea_ice_sept` | September Arctic sea ice extent | M km² | 4.5 | Declining trend + volatility |
| `amoc_strength` | AMOC strength index | % of 2000 baseline | 95 | Slow decline, collapse risk |
| `amazon_forest_cover` | Amazon forest cover | % of 2000 baseline | 85 | Policy-dependent decline |
| `permafrost_integrity` | Permafrost integrity index | 0-100 | 90 | Temperature-driven decline |
| `global_co2_ppm` | Atmospheric CO2 concentration | ppm | 425 | +2.5/yr trend |
| `climate_variability` | Climate variability/extremes index | Index (2025=100) | 100 | Rising with temperature |

---

### 4.2 Commodity Price Variables (12 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `oil_brent` | Brent crude oil price | $/barrel (2025 real) | 75 | Mean-reverting + shocks |
| `gas_europe_ttf` | European natural gas (TTF) | €/MWh (2025 real) | 35 | Regional, volatile |
| `gas_asia_lng` | Asian LNG price | $/MMBtu (2025 real) | 12 | Linked but distinct |
| `gold_price` | Gold spot price | $/oz (2025 real) | 2,000 | Crisis-responsive |
| `wheat_price` | Wheat price | $/bushel (2025 real) | 6 | Weather + stocks |
| `rice_price` | Rice price | $/ton (2025 real) | 500 | Weather + policy |
| `corn_price` | Corn price | $/bushel (2025 real) | 5 | Weather + ethanol |
| `fertilizer_price_index` | Fertilizer price index | Index (2025=100) | 100 | Energy + supply |
| `food_stocks_grains` | Global grain stocks-to-use ratio | % | 28 | Buffer for price spikes |
| `copper_price` | Copper price | $/ton (2025 real) | 8,500 | Industrial demand |
| `lithium_price` | Lithium price | $/ton (2025 real) | 20,000 | Energy transition |
| `rare_earths_index` | Rare earths price index | Index (2025=100) | 100 | China supply, tech demand |

---

### 4.3 Financial System Variables (10 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `usd_reserve_share` | USD share of global reserves | % | 58 | Slow decline baseline |
| `eur_reserve_share` | EUR share of global reserves | % | 20 | Slow potential rise |
| `cny_reserve_share` | CNY share of global reserves | % | 3 | Policy-driven rise |
| `gold_reserve_share` | Gold share of global reserves | % | 15 | Rising trend |
| `us_10yr_yield` | US 10-year Treasury yield | % nominal | 4.5 | Policy + market |
| `us_real_rate` | US real interest rate (TIPS) | % | 2.0 | Policy-driven |
| `global_credit_spread` | Global investment grade credit spread | bps | 120 | Mean-reverting + crisis |
| `fed_funds_rate` | Federal Reserve policy rate | % | 4.5 | Policy variable |
| `ecb_rate` | ECB policy rate | % | 3.0 | Policy variable |
| `pboc_rate` | PBoC policy rate | % | 3.5 | Policy variable |

---

### 4.4 Trade and Economic Structure Variables (5 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `global_trade_volume` | Global trade volume index | Index (2025=100) | 100 | Trend + cycle |
| `container_freight_index` | Container shipping cost index | Index (2025=100) | 100 | Volatile, shock-prone |
| `semiconductor_supply` | Global semiconductor supply index | Index (2025=100) | 100 | Concentrated risk |
| `swift_share` | SWIFT share of cross-border payments | % | 75 | Declining if alternatives grow |
| `cips_share` | CIPS share of cross-border payments | % | 8 | Rising |

---

### 4.5 Technology Variables (3 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `ai_capability_index` | AI capability index | Index (2025=100) | 100 | Rapid growth |
| `renewable_cost_index` | Renewable energy cost | Index (2025=100) | 100 | Declining |
| `battery_cost_kwh` | Battery cost | $/kWh | 130 | Declining |

---

### 4.6 Health and Pandemic Variables (3 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `pandemic_status` | Global pandemic status | 0-4 categorical | 0 | Event-driven |
| `pandemic_severity` | Pandemic severity (if active) | % GDP impact | 0 | Drawn when triggered |
| `antibiotic_resistance` | Antibiotic resistance index | Index (2025=100) | 100 | Slow rising trend |

**Pandemic status levels:**
- 0: No significant outbreak
- 1: Regional epidemic (localized)
- 2: Multi-region epidemic
- 3: Pandemic (global, moderate severity)
- 4: Severe pandemic (global, high severity)

---

### 4.7 Geopolitical Structure Variables (7 variables)

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `us_china_tension` | US-China tension index | 0-100 | 60 | Event-driven |
| `nato_cohesion` | NATO alliance cohesion | 0-100 | 70 | Event-driven |
| `eu_cohesion` | EU political cohesion | 0-100 | 60 | Event-driven |
| `brics_integration` | BRICS bloc integration | 0-100 | 40 | Rising trend |
| `un_effectiveness` | UN system effectiveness | 0-100 | 50 | Potentially declining |
| `active_major_conflicts` | Count of major active conflicts | Count | 3 | Event-driven |
| `nuclear_stability` | Nuclear escalation stability | 0-100 (higher=stable) | 85 | Event-driven |

---

### 4.8 Summary: Global State Variables

| Category | Variables |
|----------|-----------|
| Climate/Planetary | 8 |
| Commodity Prices | 12 |
| Financial System | 10 |
| Trade/Economic Structure | 5 |
| Technology | 3 |
| Health/Pandemic | 3 |
| Geopolitical Structure | 7 |
| **Total Global Variables** | **48** |

---

## 5. Variable Dynamics Classification

Different variables require different modeling approaches based on how they evolve over time.

### 5.1 Slow Drift Variables

**Characteristics:** Deterministic trend with small stochastic noise. Changes gradually over years/decades. Largely predictable in direction if not magnitude.

| Variable Examples | Typical Dynamics |
|-------------------|------------------|
| `global_temp_anomaly` | +0.03°C/yr ± 0.01 |
| `sea_level_global` | +0.4 cm/yr, accelerating |
| `global_co2_ppm` | +2.5 ppm/yr |
| `antibiotic_resistance` | +1%/yr index increase |
| Population cohort aging | Deterministic cohort flow |
| `battery_cost_kwh` | -8%/yr learning curve |

**Modeling approach:** Trend function + small Gaussian noise.

### 5.2 Mean-Reverting Variables

**Characteristics:** Fluctuates around an equilibrium level. Shocks dissipate over time. Has a "normal" range it tends to return to.

| Variable Examples | Equilibrium | Half-life |
|-------------------|-------------|-----------|
| `oil_brent` | $70-80/barrel | ~2 years |
| `global_credit_spread` | 100-150 bps | ~1 year |
| `container_freight_index` | 100 | ~6 months |
| `unemployment_rate` | Country NAIRU | ~3 years |
| `inflation_rate` | Central bank target | ~2 years |

**Modeling approach:** Ornstein-Uhlenbeck process or similar mean-reverting model with parameters for equilibrium level, reversion speed, and volatility.

### 5.3 Regime-Dependent Variables

**Characteristics:** Behavior differs qualitatively across regimes. May have tipping points or thresholds. Stable within regime, discontinuous across regimes.

| Variable | Regimes | Dynamics |
|----------|---------|----------|
| `amoc_strength` | Stable / Weakening / Collapsed | Stable until threshold, then rapid collapse |
| `amazon_forest_cover` | Forest / Transition / Savanna | Depends on deforestation policy + climate |
| `regime_stability` | Stable / Fragile / Failed | Different volatility in each regime |
| `pandemic_status` | None / Active | Binary with severity conditional |
| Currency regimes | Stable / Crisis / Hyperinflation | Different dynamics in each |

**Modeling approach:** Markov regime-switching models or threshold models with regime-specific dynamics.

### 5.4 Policy-Driven Variables

**Characteristics:** Primarily determined by deliberate policy choices. Responds to other state variables but through decision-making, not mechanical relationships.

| Variable | Primary Decision-Maker |
|----------|----------------------|
| `fed_funds_rate` | Federal Reserve |
| `ecb_rate` | European Central Bank |
| `pboc_rate` | People's Bank of China |
| `sanctions_level` | US/EU governments |
| `amazon_forest_cover` | Brazilian government |
| `military_spending` | National governments |

**Modeling approach:** Policy reaction functions (e.g., Taylor rule for interest rates) with discretionary shocks.

### 5.5 Event-Driven Variables

**Characteristics:** Dominated by discrete discontinuities rather than continuous evolution. Long periods of stability punctuated by sudden shifts.

| Variable | Event Examples |
|----------|----------------|
| `us_china_tension` | Taiwan crisis, trade war escalation |
| `active_major_conflicts` | War outbreak, peace agreement |
| `nuclear_stability` | Proliferation event, use/near-use |
| `semiconductor_supply` | Taiwan conflict, fab disaster |
| `regime_stability` (fragile states) | Coup, revolution, invasion |

**Modeling approach:** Baseline slow evolution + discontinuity shocks from event model (companion methodology document).

### 5.6 Derived Variables

**Characteristics:** Computed from other state variables rather than evolving independently. Updated each time step based on current state.

| Variable | Derived From |
|----------|--------------|
| `dependency_ratio` | Population cohorts |
| `fragility_score` | Stability, institutions, conflict, economics |
| `debt_service_ratio` | Debt stock, interest rates, growth |
| `climate_vulnerability_composite` | Water, heat, agriculture, sea level |
| `default_probability` | Debt dynamics, reserves, spreads |
| `fiscal_space` | Debt, deficit, reserves, growth |

**Modeling approach:** Deterministic functions of underlying state variables.

---

## 6. Transmission Mechanisms

This section provides an overview of how variables interact. Detailed parameterization will be specified in a separate document.

**Cross-reference:** For how the simulation's 12 latent factors map to these state variable categories and transmission channels, see [[methodology/reference/factor-loadings]] §Factor → State Variable Categories.

### 6.1 Global → Country Transmission

Global variables affect countries differentially based on country characteristics.

#### 6.1.1 Commodity Price Transmission

| Global Variable | Affected Countries | Mechanism |
|----------------|-------------------|-----------|
| `oil_brent` ↑ | Exporters: Saudi, UAE, Russia, Iran, Nigeria, Kazakhstan | GDP ↑, fiscal ↑, current account ↑ |
| `oil_brent` ↑ | Importers: Japan, India, Turkey, most of Europe | GDP ↓, inflation ↑, current account ↓ |
| `wheat_price` ↑ | Exporters: US, Australia, Argentina, Kazakhstan, Ukraine | Farm income ↑, current account ↑ |
| `wheat_price` ↑ | Importers: Egypt, Bangladesh, Algeria, Nigeria | Inflation ↑, fiscal strain ↑, instability ↑ |
| `gold_price` ↑ | Gold holders (central banks with high gold reserves) | Reserve value ↑ |

**Transmission formula (stylized):**
```
Country_inflation = base_inflation + oil_passthrough × Δoil + food_passthrough × Δfood
  where:
    oil_passthrough = f(energy_import_dependence, fuel_subsidy_policy)
    food_passthrough = f(food_import_dependence, food_share_of_consumption)
```

#### 6.1.2 Climate Transmission

| Global Variable | Affected Countries | Mechanism |
|----------------|-------------------|-----------|
| `global_temp_anomaly` ↑ | High `heat_exposure`: India, Pakistan, Gulf, Sahel | Labor productivity ↓, mortality ↑, habitability ↓ |
| `global_temp_anomaly` ↑ | High `agricultural_climate_risk`: Sahel, South Asia | Crop yields ↓, food security ↓ |
| `global_temp_anomaly` ↑ | Low-latitude countries generally | Net negative |
| `global_temp_anomaly` ↑ | High-latitude: Russia, Canada | Mixed (some agricultural benefit) |
| `sea_level_global` ↑ | High `sea_level_exposure`: Bangladesh, Netherlands, Vietnam | Infrastructure damage, displacement |
| `amoc_strength` ↓↓ | Northwestern Europe: UK, France, Germany, Netherlands | Temperature ↓↓, agriculture disruption |

#### 6.1.3 Financial Transmission

| Global Variable | Affected Countries | Mechanism |
|----------------|-------------------|-----------|
| `us_10yr_yield` ↑ | High `debt_external`: Argentina, Turkey, Egypt | Borrowing costs ↑, capital flight risk ↑ |
| `global_credit_spread` ↑ | All emerging markets | External financing ↓, growth ↓ |
| `usd_reserve_share` ↓ | United States | Financing costs ↑, seigniorage ↓ |
| `usd_reserve_share` ↓ | Dollar-indebted countries | Depends on currency movement |

### 6.2 Country → Country Transmission

Countries affect each other through trade, finance, migration, and contagion.

#### 6.2.1 Trade Linkages

Major bilateral trade dependencies (illustrative):
- US ↔ China: Largest bilateral trade relationship
- Germany → EU periphery: Export demand
- China → commodity exporters: Demand for oil, metals, food
- Russia → Europe: Energy supply (declining)

#### 6.2.2 Financial Contagion

- Emerging market crises tend to spread across EMs (correlated risk-off)
- European sovereign stress spreads within eurozone
- Banking crises in major financial centers (US, UK, EU) go global

#### 6.2.3 Migration and Remittances

| Source | Destination | Remittance Flow ($B/yr) |
|--------|-------------|------------------------|
| Gulf States | South Asia, Philippines, Egypt | ~$100 |
| United States | Mexico, Central America, Philippines | ~$80 |
| Europe | Turkey, North Africa, Eastern Europe | ~$50 |

**Gulf crisis → South Asian shock:** If Gulf economies contract and expel workers, remittance collapse + returnee surge in Pakistan, Bangladesh, India, Philippines, Egypt.

#### 6.2.4 Conflict Spillover

- Refugees flow to neighboring countries
- Armed groups cross borders
- Economic disruption in neighbors (trade routes, confidence)

| Conflict Country | Primary Spillover Targets |
|-----------------|--------------------------|
| Ukraine | Poland, Rest of EU, Moldova |
| Syria/Levant | Turkey, Jordan, Lebanon, EU |
| Sahel | Coastal West Africa, Maghreb |
| Ethiopia | Kenya, Sudan, East Africa |
| Venezuela | Colombia, Brazil, Caribbean |

### 6.3 Country → Global Transmission

Some countries are large enough or strategically positioned to affect global variables.

| Country | Global Variable Affected | Mechanism |
|---------|-------------------------|-----------|
| United States | `fed_funds_rate`, `us_10yr_yield`, `usd_reserve_share` | Policy, market |
| China | `global_trade_volume`, `commodity_prices`, `cny_reserve_share` | Demand, policy |
| Saudi Arabia | `oil_brent` | OPEC policy, supply |
| Russia | `gas_europe_ttf`, `oil_brent` | Supply |
| Taiwan | `semiconductor_supply` | TSMC concentration |
| Brazil | `amazon_forest_cover` | Deforestation policy |

---

## 7. Outputs and Assessments

### 7.1 Terminal State Outputs

At simulation end (or any specified time), the model produces:

#### 7.1.1 Full State Vector
Complete values for all state variables:
- 40 countries × 53 variables = 2,120 country values
- 6 Tier 1 aggregates × 53 variables = 318 aggregate values
- 6 Tier 2 aggregates × 20 variables = 120 aggregate values
- 48 global variables
- **Total: ~2,600 state values per simulation run**

#### 7.1.2 Country Summary Statistics

For each country, compute derived summary measures:

| Summary Statistic | Definition |
|-------------------|------------|
| `population_change` | % change from 2025 baseline |
| `gdp_change` | % change from 2025 baseline |
| `gdp_per_capita_change` | % change from 2025 baseline |
| `living_standards_index` | Composite of GDP/capita, life expectancy, security |
| `fragility_score` | Current fragility assessment |
| `climate_damage_cumulative` | Accumulated climate-related losses |
| `conflict_years` | Count of years in significant conflict |
| `regime_changes` | Count of regime transitions |

#### 7.1.3 Regional Rollups

Aggregate statistics for regions:
- Europe (all modeled European countries + Rest of EU)
- East Asia (China, Japan, Korea, Taiwan, North Korea)
- South Asia (India, Pakistan, Bangladesh)
- Middle East / North Africa (Turkey, Iran, Gulf, Egypt, Israel, Levant, Maghreb)
- Sub-Saharan Africa (all modeled + aggregates)
- Americas (US, Canada, Mexico, Brazil, Argentina, Central America, Andean/Caribbean)

### 7.2 Trajectory Outputs

Time series data for analysis of paths, not just endpoints:

#### 7.2.1 Key Variable Time Series
For selected variables, store full annual trajectory:
- `global_temp_anomaly` path
- `oil_brent` path
- `usd_reserve_share` path
- Major country GDP paths
- Major country population paths

#### 7.2.2 Event Occurrence Log
Record of all discontinuity events (from event model):
- Event ID
- Year of occurrence
- Severity (if variable)
- Duration (if applicable)
- Affected entities

#### 7.2.3 Cumulative Impact Tracking
Running totals of key impacts:
- Cumulative excess mortality (global, by region)
- Cumulative displacement (global, by region)
- Cumulative GDP loss vs. baseline
- Cumulative climate damage

### 7.3 Distributional Outputs

Across simulation runs (e.g., 10,000 runs), produce:

#### 7.3.1 Percentile Distributions

For each key output variable:

| Percentile | Interpretation |
|------------|----------------|
| 5th | Near-worst case (1 in 20) |
| 25th | Pessimistic but plausible |
| 50th | Median outcome |
| 75th | Optimistic but plausible |
| 95th | Near-best case (1 in 20) |

Example output table:
```
US GDP per Capita 2050 (% change from 2025):
  5th percentile:  -25%
  25th percentile: -5%
  50th percentile: +15%
  75th percentile: +30%
  95th percentile: +45%
```

#### 7.3.2 Scenario Frequency Counts

Count how often defined scenarios occur across runs:

| Scenario | Definition | Frequency |
|----------|------------|-----------|
| US severe decline | GDP/capita -20% or worse | X% of runs |
| Dollar displacement | USD reserve share <40% | X% of runs |
| Great power war | US-China conflict event | X% of runs |
| Climate catastrophe | AMOC collapse or Amazon tipping | X% of runs |
| Humanitarian crisis | >100M displaced cumulative | X% of runs |
| European fragmentation | EU cohesion <30 | X% of runs |
| Chinese crisis | China regime_stability <30 | X% of runs |
| Multi-state failure | ≥3 major state failures | X% of runs |

#### 7.3.3 Conditional Distributions

Distributions of outcomes given specific conditions:
- "Distribution of US living standards given AMOC collapse occurred"
- "Distribution of global displacement given 3+ major conflicts"
- "Distribution of dollar reserve share given China GDP exceeds US"

#### 7.3.4 Contribution Analysis

Which events/factors drive tail outcomes?
- In runs where US GDP declines >20%, which events occurred most frequently?
- What is the correlation of factor realizations with worst-case outcomes?
- Which countries' failures most often precede global crisis scenarios?

### 7.4 Qualitative Assessment Framework

Mapping quantitative state to interpretable categories.

#### 7.4.1 Country Status Classification

For each country at any time point, classify into status categories:

| Status | Criteria | Examples (current) |
|--------|----------|-------------------|
| **Thriving** | GDP/capita growing >2%/yr, stability >80, no major crises | Singapore, Netherlands |
| **Stable** | GDP/capita growing, stability >60, manageable challenges | US, Germany, Japan |
| **Stressed** | Slow/no growth, stability 40-60, significant challenges | Turkey, South Africa |
| **Crisis** | GDP/capita declining, stability 20-40, active severe problems | Lebanon, Venezuela |
| **Collapsed** | State failure, stability <20, humanitarian emergency | Syria, Somalia |
| **Recovering** | Improving from crisis, stability rising, growth resuming | (context-dependent) |

#### 7.4.2 Trajectory Classification

Classify trajectory (change from 2025 to assessment year):

| Trajectory | GDP/capita Change | Stability Change |
|------------|------------------|------------------|
| **Rising** | >+25% | Improved or stable |
| **Stable** | -10% to +25% | Within ±15 points |
| **Declining** | -25% to -10% | Dropped >15 points |
| **Collapsing** | <-25% | Dropped >30 points |
| **Recovering** | Improving from prior collapse | Rising >20 points |

#### 7.4.3 Comparative Assessment

Relative to 2025 starting position and peer group:
- "India has improved relative to 2025 and relative to South Asian peers"
- "Germany has declined relative to 2025 but remains above EU average"
- "Nigeria has declined absolutely and relative to Sub-Saharan African peers"

#### 7.4.4 Global System Assessment

Aggregate assessment of international system state:

| System State | Criteria |
|--------------|----------|
| **Stable Order** | <2 major conflicts, great power tension <50, institutions functional |
| **Stressed Order** | 2-3 conflicts, tension 50-70, institutions strained |
| **Fragmenting Order** | 3+ conflicts, tension >70, bloc formation accelerating, institutions failing |
| **Systemic Crisis** | Major power war, or >5 state failures, or global economic collapse |

---

## 8. Open Questions and Future Work

### 8.1 Variables Requiring Further Specification

| Variable Category | Open Questions |
|-------------------|----------------|
| Political/institutional | How to model institutional decay vs. sudden collapse? What drives regime_stability? |
| Climate/resource | How to translate global temp to country-specific heat exposure damage? |
| Strategic position | How to model alliance switching? Sanctions imposition/removal? |
| Migration | Should we track bilateral migration flows? Refugee stocks? |

### 8.2 Dynamics Requiring Parameterization

| Dynamics | Open Questions |
|----------|----------------|
| Demographic cohort flow | Mortality schedules by country? Fertility response to income/crisis? |
| Economic mean reversion | Country-specific equilibrium growth rates? Adjustment speeds? |
| Regime tipping points | What thresholds trigger state failure? Democratic collapse? |
| Climate tipping points | AMOC collapse threshold? Amazon tipping point? |

### 8.3 Transmission Mechanisms to Elaborate

| Mechanism | Needed Specification |
|-----------|---------------------|
| Commodity → inflation | Country-specific passthrough coefficients |
| Climate → agriculture | Yield impact functions by crop and region |
| Conflict → displacement | Displacement rates by conflict intensity |
| Financial contagion | Correlation structure across EMs |
| Remittance shock | Bilateral remittance matrices |

### 8.4 Integration with Discontinuity Event Model

The companion methodology document specifies:
- Event catalog with probabilities
- Factor model for event correlation
- Impact vectors for events

This document specifies:
- State variables that events shock
- Baseline dynamics between events
- Output interpretation framework

**Integration needed:**
- Map event impact vectors to state variable effects
- Specify how state variables affect event probabilities (conditional triggering)
- Define recovery dynamics after event shocks

### 8.5 Computational Considerations

| Consideration | Notes |
|---------------|-------|
| State space size | ~2,600 variables × 50 years × 10,000+ runs |
| Storage | Selective storage of trajectories vs. terminal states |
| Parallelization | Runs are independent; embarrassingly parallel |
| Validation | Historical backtesting approach |
| Sensitivity analysis | Parameter uncertainty quantification |

### 8.6 Potential Extensions

| Extension | Description |
|-----------|-------------|
| Higher demographic resolution | Full 5-year cohort pyramid |
| Bilateral trade network | Explicit trade flow matrix |
| Financial network | Cross-border banking exposures |
| Migration flow model | Bilateral migration matrices |
| Subnational modeling | Regions within large countries (China, India, US) |
| Shorter time steps | Quarterly for financial dynamics |

---

## 9. Appendices

### Appendix A: Complete Variable Reference Tables

#### A.1 Country-Level Variables (Full List)

| # | Variable ID | Category | Description | Units | Tier 2? |
|---|-------------|----------|-------------|-------|---------|
| 1 | `pop_0_14_m` | Demo-Stock | Male children | M | Agg |
| 2 | `pop_0_14_f` | Demo-Stock | Female children | M | Agg |
| 3 | `pop_15_34_m` | Demo-Stock | Male young workers | M | Agg |
| 4 | `pop_15_34_f` | Demo-Stock | Female young workers | M | Agg |
| 5 | `pop_35_54_m` | Demo-Stock | Male prime workers | M | ✗ |
| 6 | `pop_35_54_f` | Demo-Stock | Female prime workers | M | ✗ |
| 7 | `pop_55_64_m` | Demo-Stock | Male older workers | M | ✗ |
| 8 | `pop_55_64_f` | Demo-Stock | Female older workers | M | ✗ |
| 9 | `pop_65_79_m` | Demo-Stock | Male young elderly | M | ✗ |
| 10 | `pop_65_79_f` | Demo-Stock | Female young elderly | M | ✗ |
| 11 | `pop_80_plus_m` | Demo-Stock | Male old elderly | M | ✗ |
| 12 | `pop_80_plus_f` | Demo-Stock | Female old elderly | M | ✗ |
| 13 | `tfr` | Demo-Flow | Total fertility rate | Children/woman | ✓ |
| 14 | `life_expectancy` | Demo-Flow | Life expectancy at birth | Years | ✓ |
| 15 | `infant_mortality` | Demo-Flow | Infant mortality rate | /1000 births | ✗ |
| 16 | `net_migration_rate` | Demo-Flow | Net migration rate | %/yr | ✓ |
| 17 | `emigration_skilled_rate` | Demo-Flow | Skilled emigration rate | %/yr | ✗ |
| 18 | `gdp_real` | Econ-Stock | Real GDP | $T (2025) | ✓ |
| 19 | `gdp_per_capita` | Econ-Stock | Real GDP per capita | $K (2025) | ✓ |
| 20 | `debt_public` | Econ-Stock | Public debt | % GDP | ✗ |
| 21 | `debt_external` | Econ-Stock | External debt | % GDP | ✓ |
| 22 | `reserves_foreign` | Econ-Stock | Foreign reserves | Months imports | ✗ |
| 23 | `current_account` | Econ-Stock | Current account balance | % GDP | ✗ |
| 24 | `gdp_growth` | Econ-Flow | GDP growth rate | %/yr | ✓ |
| 25 | `inflation_rate` | Econ-Flow | Inflation rate | %/yr | ✗ |
| 26 | `unemployment_rate` | Econ-Flow | Unemployment rate | % labor | ✗ |
| 27 | `fdi_net` | Econ-Flow | Net FDI | % GDP | ✗ |
| 28 | `gdp_share_agriculture` | Econ-Struct | Agriculture % of GDP | % | ✗ |
| 29 | `gdp_share_industry` | Econ-Struct | Industry % of GDP | % | ✗ |
| 30 | `gdp_share_services` | Econ-Struct | Services % of GDP | % | ✗ |
| 31 | `export_concentration` | Econ-Struct | Export concentration | HHI 0-1 | ✗ |
| 32 | `trade_openness` | Econ-Struct | Trade openness | % GDP | ✗ |
| 33 | `regime_stability` | Political | Regime stability | 0-100 | ✓ |
| 34 | `institutional_quality` | Political | Institutional quality | -2.5 to +2.5 | ✗ |
| 35 | `corruption_index` | Political | Corruption perception | 0-100 | ✗ |
| 36 | `civil_liberties` | Political | Civil liberties | 0-100 | ✗ |
| 37 | `state_capacity` | Political | State capacity | 0-100 | ✗ |
| 38 | `internal_conflict_intensity` | Political | Internal conflict | 0-4 | ✓ |
| 39 | `protest_activity` | Political | Protest/unrest level | 0-100 | ✗ |
| 40 | `regime_type` | Political | Regime type | Categorical | ✓ |
| 41 | `water_stress` | Climate | Water stress index | 0-100 | ✓ |
| 42 | `heat_exposure` | Climate | Heat exposure index | 0-100 | ✗ |
| 43 | `agricultural_climate_risk` | Climate | Ag climate vulnerability | 0-100 | ✗ |
| 44 | `sea_level_exposure` | Climate | Sea level exposure | % pop | ✗ |
| 45 | `energy_import_dependence` | Climate | Net energy imports | % consumption | ✓ |
| 46 | `food_import_dependence` | Climate | Net food imports | % consumption | ✓ |
| 47 | `alliance_west` | Strategic | Western alignment | 0-100 | ✗ |
| 48 | `alliance_china` | Strategic | China alignment | 0-100 | ✗ |
| 49 | `alliance_nonaligned` | Strategic | Non-aligned position | 0-100 | ✗ |
| 50 | `sanctions_level` | Strategic | Sanctions severity | 0-100 | ✓ |
| 51 | `nuclear_status` | Strategic | Nuclear status | Categorical | ✗ |
| 52 | `military_spending` | Strategic | Military spending | % GDP | ✗ |
| 53 | `external_conflict_involvement` | Strategic | External conflict | 0-4 | ✗ |

**Total: 53 variables per country/Tier 1 aggregate**
**Tier 2 aggregates: 20 variables (marked ✓ or Agg)**

#### A.2 Global Variables (Full List)

| # | Variable ID | Category | Description | Units |
|---|-------------|----------|-------------|-------|
| 1 | `global_temp_anomaly` | Climate | Temperature above pre-industrial | °C |
| 2 | `sea_level_global` | Climate | Sea level above 2000 | cm |
| 3 | `arctic_sea_ice_sept` | Climate | September Arctic ice | M km² |
| 4 | `amoc_strength` | Climate | AMOC strength | % of 2000 |
| 5 | `amazon_forest_cover` | Climate | Amazon forest | % of 2000 |
| 6 | `permafrost_integrity` | Climate | Permafrost integrity | 0-100 |
| 7 | `global_co2_ppm` | Climate | Atmospheric CO2 | ppm |
| 8 | `climate_variability` | Climate | Extremes index | Index |
| 9 | `oil_brent` | Commodity | Brent crude | $/barrel |
| 10 | `gas_europe_ttf` | Commodity | European gas | €/MWh |
| 11 | `gas_asia_lng` | Commodity | Asian LNG | $/MMBtu |
| 12 | `gold_price` | Commodity | Gold spot | $/oz |
| 13 | `wheat_price` | Commodity | Wheat | $/bushel |
| 14 | `rice_price` | Commodity | Rice | $/ton |
| 15 | `corn_price` | Commodity | Corn | $/bushel |
| 16 | `fertilizer_price_index` | Commodity | Fertilizer index | Index |
| 17 | `food_stocks_grains` | Commodity | Grain stocks-to-use | % |
| 18 | `copper_price` | Commodity | Copper | $/ton |
| 19 | `lithium_price` | Commodity | Lithium | $/ton |
| 20 | `rare_earths_index` | Commodity | Rare earths index | Index |
| 21 | `usd_reserve_share` | Financial | USD reserve share | % |
| 22 | `eur_reserve_share` | Financial | EUR reserve share | % |
| 23 | `cny_reserve_share` | Financial | CNY reserve share | % |
| 24 | `gold_reserve_share` | Financial | Gold reserve share | % |
| 25 | `us_10yr_yield` | Financial | US 10yr Treasury | % |
| 26 | `us_real_rate` | Financial | US real rate | % |
| 27 | `global_credit_spread` | Financial | IG credit spread | bps |
| 28 | `fed_funds_rate` | Financial | Fed policy rate | % |
| 29 | `ecb_rate` | Financial | ECB policy rate | % |
| 30 | `pboc_rate` | Financial | PBoC policy rate | % |
| 31 | `global_trade_volume` | Trade | Trade volume index | Index |
| 32 | `container_freight_index` | Trade | Container freight | Index |
| 33 | `semiconductor_supply` | Trade | Semiconductor supply | Index |
| 34 | `swift_share` | Trade | SWIFT payment share | % |
| 35 | `cips_share` | Trade | CIPS payment share | % |
| 36 | `ai_capability_index` | Tech | AI capability | Index |
| 37 | `renewable_cost_index` | Tech | Renewable cost | Index |
| 38 | `battery_cost_kwh` | Tech | Battery cost | $/kWh |
| 39 | `pandemic_status` | Health | Pandemic status | 0-4 |
| 40 | `pandemic_severity` | Health | Pandemic severity | % GDP |
| 41 | `antibiotic_resistance` | Health | Antibiotic resistance | Index |
| 42 | `us_china_tension` | Geopolitical | US-China tension | 0-100 |
| 43 | `nato_cohesion` | Geopolitical | NATO cohesion | 0-100 |
| 44 | `eu_cohesion` | Geopolitical | EU cohesion | 0-100 |
| 45 | `brics_integration` | Geopolitical | BRICS integration | 0-100 |
| 46 | `un_effectiveness` | Geopolitical | UN effectiveness | 0-100 |
| 47 | `active_major_conflicts` | Geopolitical | Major conflict count | Count |
| 48 | `nuclear_stability` | Geopolitical | Nuclear stability | 0-100 |

**Total: 48 global variables**

### Appendix B: Regional Aggregate Composition

#### B.1 Tier 1 Aggregates

| Aggregate | Member Countries | 2025 Pop (M) | 2025 GDP ($B) |
|-----------|-----------------|--------------|---------------|
| **Gulf States** | Kuwait, Qatar, Bahrain, Oman | 15 | 500 |
| **Central America** | Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica, Panama | 55 | 400 |
| **Sahel** | Mali, Niger, Burkina Faso, Chad, Mauritania, Senegal | 100 | 150 |
| **East Africa** | Tanzania, Uganda, Somalia, Sudan, South Sudan, Rwanda, Burundi, Eritrea | 200 | 300 |
| **Rest of EU** | Belgium, Austria, Sweden, Denmark, Finland, Ireland, Portugal, Greece, Czechia, Romania, Hungary, Slovakia, Bulgaria, Croatia, Slovenia, Lithuania, Latvia, Estonia, Luxembourg, Malta, Cyprus | 130 | 3,000 |
| **Levant/Iraq** | Iraq, Syria, Jordan, Lebanon | 75 | 300 |

#### B.2 Tier 2 Aggregates

| Aggregate | Member Countries | 2025 Pop (M) | 2025 GDP ($B) |
|-----------|-----------------|--------------|---------------|
| **Central Asia (other)** | Uzbekistan, Tajikistan, Kyrgyzstan, Turkmenistan | 60 | 150 |
| **Southeast Asia (other)** | Myanmar, Malaysia, Cambodia, Laos | 100 | 700 |
| **Andean/Caribbean** | Colombia, Peru, Chile, Venezuela, Ecuador, Bolivia, Caribbean states | 180 | 1,200 |
| **Maghreb** | Morocco, Algeria, Tunisia, Libya | 110 | 500 |
| **Southern Africa (other)** | Zimbabwe, Zambia, Mozambique, Angola, Botswana, Namibia, Malawi, others | 150 | 400 |
| **West/Central Africa (other)** | Ghana, Côte d'Ivoire, Cameroon, others (ex-Nigeria, Ethiopia, DRC) | 300 | 600 |

### Appendix C: Initial Conditions Data Sources

Initial values (2025 baseline) will be populated from:

| Variable Category | Primary Data Sources |
|-------------------|---------------------|
| Demographics | UN Population Division, national statistical agencies |
| GDP/Economics | IMF World Economic Outlook, World Bank WDI |
| Debt/Fiscal | IMF Fiscal Monitor, national treasury data |
| Trade | WTO, UNCTAD, World Bank WITS |
| Political/Institutional | V-Dem, World Bank WGI, Freedom House, Polity |
| Climate/Resource | WRI Aqueduct, FAO, IEA, World Bank climate data |
| Strategic | SIPRI, various indices |
| Global financial | BIS, IMF COFER, Federal Reserve |
| Commodities | World Bank Commodity Markets, exchanges |

---

## Document Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial comprehensive specification |

---

*This specification document defines the state space for geopolitical Monte Carlo simulation. Companion documents specify the discontinuity event model (probability, correlation, impact) and historical reference patterns. Implementation will require parameterization of dynamics, transmission mechanisms, and initial conditions.*