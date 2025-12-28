---
title: State Variables - Global
type: note
permalink: methodology/reference/state-variables-global
tags:
- methodology
- reference
- state
- variables
- global
- observables
---

# Global State Variables

## Complete Catalog of Global and Commons Variables

**Document Version:** 2.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

**Related documents:**
- [[methodology/reference/state-overview]] — Entry point for state model
- [[methodology/reference/state-variables-country]] — Country-level variable catalog
- [[methodology/reference/state-outputs]] — Output specifications including derived assessments
- [[methodology/concepts/synthetic-variable-problem]] — Rationale for observable decomposition

---

## 1. Purpose & Scope

This document catalogs all global state variables—variables that affect multiple countries simultaneously and cannot be attributed to any single nation. These include climate and planetary systems, commodity markets, financial system parameters, and global health status.

### Design Principles

**Observable over synthetic:** Consistent with [[methodology/concepts/synthetic-variable-problem]], we prefer directly measurable variables. Synthetic indices for geopolitical structure (`us_china_tension`, `nato_cohesion`, etc.) have been moved to derived outputs. They are computed from country-level observables for human interpretation, not used as state variables conditioning event probabilities.

**Clear measurement procedures:** Each variable has a defined data source and units. Event shocks have magnitudes with real-world referents.

**Separation of state from assessment:** The simulation tracks what can be measured. Interpretive assessments are outputs, not inputs.

### Variable Count Summary

| Category | Variables |
|----------|-----------|
| Climate & Planetary | 8 |
| Commodity Prices | 12 |
| Financial System | 10 |
| Trade & Economic Structure | 5 |
| Technology | 3 |
| Health & Pandemic | 3 |
| Conflict | 1 |
| **Total** | **42** |

*Note: The original specification included 48 global variables. Six synthetic geopolitical structure indices have been moved to derived outputs (see §8).*

---

## 2. Climate & Planetary Variables (8)

Physical measurements of Earth system state. These drive differential impacts across countries based on exposure coefficients.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `global_temp_anomaly` | Global mean temperature above pre-industrial | °C | 1.3 | Slow drift ~+0.03/yr |
| `sea_level_global` | Global mean sea level above 2000 baseline | cm | 10 | Slow drift ~+0.4/yr, accelerating |
| `arctic_sea_ice_sept` | September Arctic sea ice extent | M km² | 4.5 | Declining trend + interannual volatility |
| `amoc_strength` | Atlantic Meridional Overturning Circulation strength | % of 2000 baseline | 95 | Slow decline; collapse threshold ~50% |
| `amazon_forest_cover` | Amazon forest cover | % of 2000 baseline | 85 | Policy-dependent; tipping point risk |
| `permafrost_integrity` | Permafrost integrity index | % intact | 90 | Temperature-driven decline |
| `global_co2_ppm` | Atmospheric CO2 concentration | ppm | 425 | ~+2.5/yr trend |
| `climate_variability` | Climate extremes frequency index | Index (2025=100) | 100 | Rising with temperature |

### Data Sources

| Variable | Primary Source |
|----------|----------------|
| `global_temp_anomaly` | NASA GISS, NOAA, HadCRUT |
| `sea_level_global` | NASA satellite altimetry |
| `arctic_sea_ice_sept` | NSIDC |
| `amoc_strength` | RAPID array, ocean monitoring |
| `amazon_forest_cover` | INPE PRODES, Global Forest Watch |
| `permafrost_integrity` | ESA CCI Permafrost |
| `global_co2_ppm` | NOAA Mauna Loa Observatory |
| `climate_variability` | EM-DAT, Munich Re NatCatSERVICE |

### Dynamics Notes

**Regime-dependent variables:** `amoc_strength` and `amazon_forest_cover` exhibit tipping point behavior. Above threshold, gradual change; below threshold, potential rapid transition to new stable state.

**Slow drift:** Most climate variables change gradually with small interannual noise. Major discontinuities (AMOC collapse, Amazon dieback) are modeled as events that shock the relevant variable.

---

## 3. Commodity Price Variables (12)

Market prices for globally traded commodities. These transmit to countries based on import/export dependence.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `oil_brent` | Brent crude oil price | $/barrel (2025 real) | 75 | Mean-reverting + supply shocks |
| `gas_europe_ttf` | European natural gas (TTF) | €/MWh (2025 real) | 35 | Regional, volatile |
| `gas_asia_lng` | Asian LNG spot price | $/MMBtu (2025 real) | 12 | Linked to oil + regional factors |
| `gold_price` | Gold spot price | $/oz (2025 real) | 2,000 | Crisis-responsive, store of value |
| `wheat_price` | Wheat price | $/bushel (2025 real) | 6 | Weather + stocks + policy |
| `rice_price` | Rice price | $/ton (2025 real) | 500 | Weather + export restrictions |
| `corn_price` | Corn price | $/bushel (2025 real) | 5 | Weather + ethanol demand |
| `fertilizer_price_index` | Fertilizer price composite | Index (2025=100) | 100 | Energy costs + supply concentration |
| `food_stocks_grains` | Global grain stocks-to-use ratio | % | 28 | Buffer against price spikes |
| `copper_price` | Copper price | $/ton (2025 real) | 8,500 | Industrial demand, energy transition |
| `lithium_price` | Lithium carbonate price | $/ton (2025 real) | 20,000 | Battery demand, volatile |
| `rare_earths_index` | Rare earths price composite | Index (2025=100) | 100 | China supply concentration, tech demand |

### Data Sources

| Variable | Primary Source |
|----------|----------------|
| Oil, gas, metals | ICE, CME, LME |
| Food commodities | CBOT, World Bank Commodity Markets |
| `food_stocks_grains` | USDA, FAO |
| `fertilizer_price_index` | World Bank, Green Markets |
| `rare_earths_index` | Asian Metal, Argus |

### Dynamics Notes

**Mean-reverting:** Most commodity prices fluctuate around equilibrium levels determined by production costs and demand. Shocks dissipate over 1-3 years.

**Supply shocks:** Events (conflict, natural disaster, policy) can cause sudden price spikes. Oil supply shocks, for example, transmit to `oil_brent` which then affects importing countries' inflation and current accounts.

**Food-energy nexus:** Fertilizer prices link to energy costs; corn prices link to ethanol policy; all food prices respond to climate events.

---

## 4. Financial System Variables (10)

Global financial conditions that affect borrowing costs, capital flows, and currency dynamics.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `usd_reserve_share` | USD share of global FX reserves | % | 58 | Slow structural decline |
| `eur_reserve_share` | EUR share of global FX reserves | % | 20 | Stable to rising |
| `cny_reserve_share` | CNY share of global FX reserves | % | 3 | Policy-driven rise |
| `gold_reserve_share` | Gold share of global reserves | % | 15 | Rising trend |
| `us_10yr_yield` | US 10-year Treasury yield | % nominal | 4.5 | Policy + market |
| `us_real_rate` | US real interest rate (TIPS) | % | 2.0 | Fed policy driven |
| `global_credit_spread` | Global investment grade credit spread | bps over risk-free | 120 | Mean-reverting; crisis-responsive |
| `fed_funds_rate` | Federal Reserve policy rate | % | 4.5 | Policy variable |
| `ecb_rate` | ECB main refinancing rate | % | 3.0 | Policy variable |
| `pboc_rate` | PBoC policy rate (LPR 1Y) | % | 3.5 | Policy variable |

### Data Sources

| Variable | Primary Source |
|----------|----------------|
| Reserve shares | IMF COFER |
| US yields and rates | Federal Reserve |
| `global_credit_spread` | ICE BofA indices |
| ECB, PBoC rates | Central bank publications |

### Dynamics Notes

**Policy-driven:** Central bank rates follow reaction functions (e.g., Taylor rule) with discretionary shocks. They respond to inflation, output gaps, and financial stability concerns.

**Reserve share dynamics:** `usd_reserve_share` changes slowly through portfolio reallocation and trade invoicing shifts. Major events (dollar reserve crisis, sanctions weaponization) can accelerate transitions.

**Credit spreads:** Mean-reverting around ~100-150 bps; widen sharply during risk-off episodes; narrow during risk-on periods.

---

## 5. Trade & Economic Structure Variables (5)

Global trade and supply chain conditions.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `global_trade_volume` | Global goods trade volume | Index (2025=100) | 100 | GDP-linked trend + cycle |
| `container_freight_index` | Container shipping cost | Index (2025=100) | 100 | Volatile; supply-chain shocks |
| `semiconductor_supply` | Global semiconductor availability | Index (2025=100) | 100 | Concentrated risk (Taiwan) |
| `swift_share` | SWIFT share of cross-border messaging | % | 75 | Declining if alternatives grow |
| `cips_share` | CIPS share of cross-border messaging | % | 8 | Rising with China trade |

### Data Sources

| Variable | Primary Source |
|----------|----------------|
| `global_trade_volume` | CPB World Trade Monitor, WTO |
| `container_freight_index` | Drewry, Freightos |
| `semiconductor_supply` | SIA, industry reports |
| `swift_share`, `cips_share` | SWIFT, PBoC, BIS |

### Dynamics Notes

**`semiconductor_supply`:** This index represents global chip availability. It's normalized to 2025=100, with values <100 indicating shortage. Taiwan conflict or major fab disruption would shock this variable, transmitting to technology-dependent economies.

**Payment system shares:** Gradual structural change driven by trade patterns and sanctions policy. Major rupture events could accelerate SWIFT-to-alternatives shift.

---

## 6. Technology Variables (3)

Technology capability and cost trajectories. These are treated as scenario assumptions about technology evolution rather than measured quantities.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `ai_capability_index` | AI capability level | Index (2025=100) | 100 | Rapid growth trajectory |
| `renewable_cost_index` | Solar/wind LCOE | Index (2025=100) | 100 | Declining ~5-8%/yr |
| `battery_cost_kwh` | Lithium-ion battery pack cost | $/kWh | 130 | Declining ~8-10%/yr |

### Data Sources

| Variable | Primary Source |
|----------|----------------|
| `ai_capability_index` | Composite (benchmarks, compute) |
| `renewable_cost_index` | IRENA, Lazard LCOE |
| `battery_cost_kwh` | BNEF, battery industry reports |

### Dynamics Notes

**Trend-driven:** Technology variables follow learning curves with potential for breakthrough shocks (positive discontinuities).

**`ai_capability_index`:** This is a modeling assumption rather than a precise measurement. It captures the general trajectory of AI capabilities relevant for economic and strategic impacts. Breakthrough events can accelerate the trajectory.

**Cost indices:** `renewable_cost_index` and `battery_cost_kwh` are more directly measurable. They follow learning curves with ~8% annual cost reduction as baseline, subject to supply chain disruptions (lithium, rare earths) or breakthrough acceleration.

---

## 7. Health & Pandemic Variables (3)

Global health system state and pandemic status.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `pandemic_status` | Global pandemic status | Categorical (0-4) | 0 | Event-driven |
| `pandemic_severity` | Pandemic severity if active | % GDP impact | 0 | Drawn when triggered |
| `antibiotic_resistance` | Antibiotic resistance index | Index (2025=100) | 100 | Slow rising trend ~1%/yr |

### Pandemic Status Scale

| Level | Description | Historical Examples |
|-------|-------------|---------------------|
| 0 | No significant global outbreak | Normal years |
| 1 | Regional epidemic (localized) | Ebola 2014-16 |
| 2 | Multi-region epidemic | MERS, H5N1 outbreaks |
| 3 | Pandemic (global, moderate) | 2009 H1N1 |
| 4 | Severe pandemic (global, high severity) | COVID-19, 1918 flu |

### Data Sources

| Variable | Primary Source |
|----------|----------------|
| `pandemic_status` | WHO declarations, event-based |
| `antibiotic_resistance` | WHO GLASS, CDC |

### Dynamics Notes

**`pandemic_status`:** Normally 0. Pandemic events set status to 1-4 based on severity draw. Status persists for event duration, then returns to 0.

**`pandemic_severity`:** Only meaningful when `pandemic_status` > 0. Drawn from severity distribution when pandemic event fires.

**`antibiotic_resistance`:** Slow structural deterioration. Major antimicrobial platform breakthrough would shock this downward.

---

## 8. Conflict Variables (1)

Observable count of major armed conflicts.

| Variable ID | Description | Units | 2025 Baseline | Dynamics |
|-------------|-------------|-------|---------------|----------|
| `active_major_conflicts` | Count of major active armed conflicts | Count | 3 | Event-driven |

### Definition

A "major conflict" meets UCDP criteria for war (1,000+ battle deaths/year) OR involves direct military engagement between major powers OR nuclear-armed states.

### Data Source

UCDP/PRIO Armed Conflict Dataset

### Dynamics Notes

Increments when conflict events fire; decrements when conflicts resolve. This is a simple observable count, not an assessment.

---

## 9. Derived Geopolitical Assessments (Outputs Only)

The following were state variables in the original specification. Per [[methodology/concepts/synthetic-variable-problem]], they have been moved to derived outputs. They are computed from country-level observables for human interpretation, **not used as state variables** conditioning event probabilities.

| Former Variable | Computed From | See |
|-----------------|---------------|-----|
| `us_china_tension` | US-China trade share, sanctions, military incidents, diplomatic actions | [[methodology/reference/state-outputs]] |
| `nato_cohesion` | Member defense spending, joint exercises, voting alignment, burden-sharing | [[methodology/reference/state-outputs]] |
| `eu_cohesion` | EU budget disputes, infringement proceedings, political alignment | [[methodology/reference/state-outputs]] |
| `brics_integration` | Intra-BRICS trade, CIPS usage, reserve diversification, summit outcomes | [[methodology/reference/state-outputs]] |
| `un_effectiveness` | Resolution passage rates, peacekeeping deployments, treaty compliance | [[methodology/reference/state-outputs]] |
| `nuclear_stability` | Active conflicts involving nuclear states, arms control status, incident counts | [[methodology/reference/state-outputs]] |

### Rationale for Moving to Outputs

These indices suffered from the same validity problems identified for country-level synthetic variables:

1. **No clear measurement procedure:** What observable yields `nato_cohesion = 70` vs `65`?

2. **Opaque update semantics:** How does a trade dispute change `us_china_tension`? By how much?

3. **Potential circularity:** Using `nuclear_stability` to condition nuclear escalation probability risks restating assumptions as predictions.

The simulation now tracks observables at country level (alliance status, trade shares, military spending, conflict involvement) and aggregates them into interpretive indices at analysis time.

---

## 10. Summary

### Total Global State Space

| Category | Variables |
|----------|-----------|
| Climate & Planetary | 8 |
| Commodity Prices | 12 |
| Financial System | 10 |
| Trade & Economic Structure | 5 |
| Technology | 3 |
| Health & Pandemic | 3 |
| Conflict | 1 |
| **Total Global Variables** | **42** |

### Combined with Country-Level

| Entity Type | Variables |
|-------------|-----------|
| 40 countries × 63 variables | 2,520 |
| 6 Tier 1 aggregates × 63 variables | 378 |
| 6 Tier 2 aggregates × 22 variables | 132 |
| Global variables | 42 |
| **Total State Space** | **3,072** |

### Dynamics Classification

| Dynamics Type | Global Variables |
|---------------|------------------|
| Slow drift | Climate variables, technology costs, antibiotic resistance, reserve shares |
| Mean-reverting | Commodity prices, credit spreads |
| Policy-driven | Central bank rates |
| Event-driven | Pandemic status, conflict count, tipping points |
| Regime-dependent | AMOC, Amazon (stable until threshold, then transition) |

---

## 11. Integration with Event Model

### Events That Shock Global Variables

| Event Category | Global Variables Affected |
|----------------|---------------------------|
| Climate tipping points | `amoc_strength`, `amazon_forest_cover`, `permafrost_integrity` |
| Oil supply shock | `oil_brent`, transmission to other energy prices |
| Financial crisis | `global_credit_spread`, capital flow reversals |
| Pandemic | `pandemic_status`, `pandemic_severity` |
| Taiwan conflict | `semiconductor_supply` |
| Trade rupture | `global_trade_volume`, `swift_share`/`cips_share` |
| Technology breakthrough | `ai_capability_index`, `renewable_cost_index`, `battery_cost_kwh` |

### Global → Country Transmission

Global variables affect countries via transmission coefficients defined in [[methodology/reference/state-transmission]]:

- **Commodity prices → Inflation:** Via import dependence and consumption shares
- **Climate variables → Exposure:** Via country-specific exposure coefficients
- **Financial conditions → Borrowing costs:** Via external debt and reserve adequacy
- **Pandemic status → GDP/mortality:** Via health system capacity and demographic structure

---

*This catalog specifies what the simulation tracks at global level. For country-level variables see [[methodology/reference/state-variables-country]]. For dynamics see [[methodology/reference/state-dynamics]]. For transmission mechanisms see [[methodology/reference/state-transmission]].*