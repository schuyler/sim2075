---
title: State Transmission
type: note
permalink: methodology/reference/state-transmission
tags:
- methodology
- reference
- state
- transmission
- propagation
- linkages
---

# State Transmission

## How Variables Affect Each Other

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

**Related documents:**
- [[methodology/reference/state-overview]] — Entry point for state model
- [[methodology/reference/state-variables-country]] — Country-level variable catalog
- [[methodology/reference/state-variables-global]] — Global variable catalog
- [[methodology/reference/state-dynamics]] — How variables evolve over time
- [[methodology/reference/factor-loadings]] — Factor → state variable relationships

---

## 1. Purpose & Scope

This document specifies how state variables affect each other—how changes in one variable propagate to others. Transmission mechanisms are distinct from dynamics (how variables evolve on their own) and from event shocks (discrete discontinuities).

### Transmission vs. Dynamics vs. Events

| Mechanism | Description | Example |
|-----------|-------------|---------|
| **Dynamics** | Variable's own time evolution | Oil prices mean-revert to equilibrium |
| **Transmission** | One variable affects another | Oil price ↑ → importing country inflation ↑ |
| **Event shock** | Discontinuity directly impacts variable | War → oil supply ↓ |

In each simulation time step:
1. Events fire and apply direct shocks
2. Transmission propagates effects across variables
3. Dynamics evolve variables toward their attractors

### Scope of This Document

This document provides an overview of transmission channels and their structure. Detailed parameterization (specific coefficients, elasticities) will be specified in the initialization methodology document.

---

## 2. Transmission Categories

Transmission flows in three directions:

| Direction | Description | Primary Channels |
|-----------|-------------|------------------|
| **Global → Country** | Global conditions affect countries differentially | Commodity prices, climate, financial conditions |
| **Country → Country** | Countries affect each other | Trade, financial contagion, migration, conflict spillover |
| **Country → Global** | Large countries affect global variables | Demand shocks, policy spillovers, supply disruptions |

---

## 3. Global → Country Transmission

Global variables affect countries differentially based on country characteristics (exposure coefficients, economic structure, policy buffers).

### 3.1 Commodity Price Transmission

Commodity price changes transmit to countries based on trade position (importer vs. exporter) and consumption patterns.

#### Oil Price Transmission

| Country Type | Transmission Channel | Affected Variables |
|--------------|---------------------|-------------------|
| Net exporters (Saudi, Russia, Iran, UAE, Nigeria, Kazakhstan) | Revenue windfall | `gdp_growth` ↑, `current_account` ↑, `tax_revenue_gdp` ↑ |
| Net importers (Japan, India, Turkey, most of Europe) | Cost shock | `inflation_rate` ↑, `current_account` ↓, `gdp_growth` ↓ |

**Transmission formula (stylized):**
```
Δinflation = oil_passthrough × Δoil_brent
where:
  oil_passthrough = f(energy_import_dependence, fuel_subsidy_policy, energy_intensity)
```

**Passthrough coefficients:** Vary by country based on:
- `energy_import_dependence`: Higher dependence → larger passthrough
- Economic structure: Energy-intensive economies more affected
- Policy buffers: Fuel subsidies dampen passthrough (but strain fiscal)

#### Food Price Transmission

| Country Type | Transmission Channel | Affected Variables |
|--------------|---------------------|-------------------|
| Net exporters (US, Australia, Argentina, Ukraine, Brazil) | Revenue gain | `current_account` ↑, agricultural GDP ↑ |
| Net importers (Egypt, Bangladesh, Nigeria, Sahel) | Cost shock, instability risk | `inflation_rate` ↑, `protest_intensity_annual` ↑ |

**Transmission formula (stylized):**
```
Δinflation_food = food_passthrough × Δwheat_price
where:
  food_passthrough = f(food_import_dependence, food_share_of_consumption)
```

**Note:** Wheat price is used as proxy for food price stress because wheat is the most politically sensitive staple in key vulnerable regions. Regional dependencies vary:
- **MENA (Egypt, Levant, Maghreb):** Heavily wheat-dependent; wheat → unrest transmission strongest
- **South Asia (Bangladesh, parts of India):** Rice-dependent; rice price spikes more relevant
- **Sub-Saharan Africa:** Mixed; rice and maize more important than wheat in many areas

A weighted composite of `wheat_price`, `rice_price`, and `corn_price` with region-specific weights could be a future refinement. For v1.0, wheat serves as the primary proxy given its importance in the historically unrest-prone MENA region.

**Political transmission:** For countries with high food import dependence and low income, food price spikes transmit to political stress:
```
Δprotest_intensity = food_stress_coefficient × Δwheat_price × food_import_dependence
```

Historical reference: 2008 and 2011 food price spikes correlated with unrest in food-importing countries.

### 3.2 Climate Transmission

Global climate variables transmit to countries based on geographic exposure.

#### Temperature Transmission

| Exposure Type | Affected Countries | Transmission |
|---------------|-------------------|--------------|
| Heat stress | High `heat_exposure`: India, Pakistan, Gulf, Sahel, Southeast Asia | Labor productivity ↓, mortality ↑, cooling demand ↑ |
| Agricultural | High `agricultural_climate_risk`: Sahel, South Asia, Southern Africa | Crop yields ↓, food security ↓ |
| Mixed (some benefit) | High latitude: Russia, Canada, Scandinavia | Some agricultural benefit, but permafrost/infrastructure risk |

**Transmission formula:**
```
Δagricultural_output = climate_sensitivity × Δglobal_temp_anomaly × agricultural_climate_risk
```

**Nonlinear effects:** Beyond certain temperature thresholds, impacts accelerate. Wet-bulb temperatures above 35°C create unsurvivable conditions for outdoor labor.

#### Sea Level Transmission

| Exposure Type | Affected Countries | Transmission |
|---------------|-------------------|--------------|
| High exposure | Bangladesh, Netherlands, Vietnam, coastal cities globally | Infrastructure damage, displacement, adaptation costs |

**Transmission formula:**
```
Δinfrastructure_damage = sea_level_sensitivity × Δsea_level_global × sea_level_exposure
```

#### AMOC Transmission

AMOC weakening or collapse has asymmetric geographic effects:

| Region | Effect |
|--------|--------|
| Northwestern Europe (UK, France, Germany, Netherlands, Scandinavia) | Cooling 2-5°C, agricultural disruption, energy demand ↑ |
| North America (eastern seaboard) | Accelerated sea level rise |
| Tropical Atlantic | Shifted precipitation patterns |

This is a regime-dependent transmission: minimal effect above AMOC threshold, large effects if collapse occurs.

### 3.3 Financial Condition Transmission

Global financial variables transmit to countries based on external vulnerability.

#### Interest Rate Transmission

| Country Type | Transmission Channel | Affected Variables |
|--------------|---------------------|-------------------|
| High `debt_external` (Argentina, Turkey, Egypt, Pakistan) | Borrowing cost shock | `gdp_growth` ↓, `debt_service_ratio` ↑, default risk ↑ |
| Low external debt, strong reserves | Limited direct effect | Portfolio flows may shift |

**Transmission formula:**
```
Δborrowing_cost = beta × Δus_10yr_yield + gamma × Δglobal_credit_spread
where:
  beta, gamma = f(debt_external, reserves_foreign, current_account)
```

Countries with high external debt, low reserves, and current account deficits face larger borrowing cost transmission.

#### Credit Spread Transmission

Global risk-off episodes (widening `global_credit_spread`) affect emerging markets more than advanced economies:

```
Δcapital_flows = -sensitivity × Δglobal_credit_spread × em_vulnerability
where:
  em_vulnerability = f(current_account, reserves_foreign, debt_external)
```

### 3.4 Technology Transmission

Technology cost improvements transmit globally but with adoption lags based on income and infrastructure.

| Variable | Transmission |
|----------|--------------|
| `renewable_cost_index` ↓ | Energy transition accelerates; benefits countries with solar/wind resources |
| `battery_cost_kwh` ↓ | EV adoption accelerates; affects oil demand trajectory |
| `ai_capability_index` ↑ | Productivity effects; labor market disruption; uneven by sector/country |

Technology transmission is slower than financial transmission—adoption requires investment, infrastructure, and skills.

---

## 4. Country → Country Transmission

Countries affect each other through economic linkages, financial connections, migration, and conflict spillover.

### 4.1 Trade Linkages

Major bilateral trade relationships create demand transmission:

| Relationship | Transmission |
|--------------|--------------|
| US ↔ China | Largest bilateral; decoupling shocks transmit both directions |
| Germany → EU periphery | German demand affects Southern European exports |
| China → commodity exporters | Chinese demand drives commodity prices, affects Brazil, Australia, Chile, Africa |
| Russia → Europe (declining) | Energy supply; decoupling in progress |

**Transmission formula:**
```
Δexport_demand_i = Σⱼ (trade_share_ij × Δgdp_j)
```

Where `trade_share_ij` is country i's exports to country j as share of i's total exports.

**Trade rupture events:** US-China economic rupture or similar events directly shock bilateral trade flows, forcing supply chain reorganization.

### 4.2 Financial Contagion

Financial crises tend to spread across countries through:

| Channel | Mechanism |
|---------|-----------|
| Portfolio rebalancing | Investors sell EM assets broadly when one EM enters crisis |
| Banking linkages | Cross-border bank exposures transmit losses |
| Confidence effects | Crisis in one country raises risk perception for peers |

**Contagion pattern:** Emerging market crises are correlated—a crisis in Turkey raises credit spreads for other EMs (Argentina, South Africa, Indonesia) even without direct bilateral linkages.

**Eurozone-specific:** European sovereign stress spreads within the eurozone due to shared currency and banking system integration.

### 4.3 Remittance Transmission

Remittance flows create vulnerability to source-country economic conditions:

| Source Region | Destination Countries | Flow ($B/yr) | Vulnerability |
|---------------|----------------------|--------------|---------------|
| Gulf States | Pakistan, Bangladesh, India, Philippines, Egypt | ~$100 | Gulf crisis → remittance collapse + returnee surge |
| United States | Mexico, Central America, Philippines | ~$80 | US recession → reduced flows |
| Europe | Turkey, North Africa, Eastern Europe | ~$50 | European recession → reduced flows |

**Transmission formula:**
```
Δremittance_income_i = remittance_elasticity × Δgdp_source × remittance_share_i
```

**Asymmetry note:** Remittance flows exhibit asymmetric elasticity—they fall faster during source-country recessions than they rise during booms. Workers may be laid off quickly but hiring lags recovery; migrants may return home during downturns but outmigration takes longer to resume. Consider modeling with direction-dependent elasticity (higher magnitude for negative Δgdp_source).

**Compound shock:** Gulf economic crisis or conflict would simultaneously reduce remittances AND trigger return migration, compounding pressure on origin countries.

### 4.4 Migration and Displacement Transmission

Conflict and crisis generate displacement that affects neighboring countries:

| Origin Country | Primary Spillover Targets | Transmission |
|----------------|--------------------------|--------------|
| Ukraine | Poland, Rest of EU, Moldova | Refugee flows, fiscal pressure, labor market effects |
| Syria/Levant | Turkey, Jordan, Lebanon, EU | Large refugee populations, political stress |
| Sahel | Coastal West Africa, Maghreb | Displacement, conflict spillover |
| Ethiopia | Kenya, Sudan, East Africa | Refugee flows, regional instability |
| Venezuela | Colombia, Brazil, Peru, Caribbean | Economic migration, fiscal pressure |

**Transmission variables:**
- Receiving country `net_migration_rate` ↑
- Receiving country `protest_intensity_annual` may ↑ (political backlash)
- Receiving country fiscal costs ↑

### 4.5 Conflict Spillover

Armed conflict affects neighboring countries through multiple channels:

| Channel | Transmission |
|---------|--------------|
| Refugee flows | As above |
| Trade disruption | Closed borders, destroyed infrastructure |
| Armed group movement | Cross-border violence, destabilization |
| Economic confidence | Reduced investment in conflict-adjacent regions |

**Geographic decay:** Conflict spillover effects decay with distance but can be substantial for immediate neighbors.

---

## 5. Country → Global Transmission

Some countries are large enough or strategically positioned to affect global variables.

### 5.1 Demand Shocks

| Country | Global Variable Affected | Mechanism |
|---------|-------------------------|-----------|
| China | Commodity prices (oil, metals, food) | Demand shock from growth slowdown |
| United States | `global_trade_volume`, financial conditions | Demand shock, policy spillover |
| EU (aggregate) | `global_trade_volume` | Major trading bloc |

**China slowdown transmission:**
```
Δoil_brent = oil_demand_elasticity × Δchina_gdp_growth
Δcopper_price = copper_demand_elasticity × Δchina_gdp_growth
```

Chinese economic crisis would depress global commodity prices, benefiting importers but hurting exporters.

### 5.2 Policy Spillovers

| Country | Global Variable Affected | Mechanism |
|---------|-------------------------|-----------|
| United States (Fed) | `us_10yr_yield`, `global_credit_spread`, capital flows | Monetary policy transmission |
| United States | `sanctions_level` (on targets) | Sanctions policy |
| China (PBoC) | `cny_reserve_share`, capital flows | Monetary/capital policy |
| Brazil | `amazon_forest_cover` | Deforestation policy |

**Fed policy transmission:** US monetary tightening raises global borrowing costs, triggers capital outflows from emerging markets, appreciates dollar.

### 5.3 Supply Disruptions

| Country/Region | Global Variable Affected | Mechanism |
|----------------|-------------------------|-----------|
| Saudi Arabia / OPEC | `oil_brent` | Supply policy, disruption |
| Russia | `gas_europe_ttf`, `oil_brent` | Supply disruption/weaponization |
| Taiwan | `semiconductor_supply` | TSMC concentration risk |
| Ukraine | `wheat_price` | Major grain exporter |

**Taiwan disruption:** Taiwan conflict would shock `semiconductor_supply`, transmitting to technology-dependent economies globally. This is a concentrated, low-substitutability supply chain risk.

### 5.4 Reserve Currency Dynamics

| Country | Global Variable Affected | Mechanism |
|---------|-------------------------|-----------|
| United States | `usd_reserve_share` | Dollar policy, sanctions use, debt trajectory |
| China | `cny_reserve_share`, `cips_share` | Internationalization policy |
| BRICS collectively | Reserve diversification | Coordinated de-dollarization efforts |

**Feedback loop:** Aggressive US sanctions use may accelerate reserve diversification, reducing `usd_reserve_share`, which in turn may constrain future sanctions effectiveness.

---

## 6. Transmission Timing and Lags

Different transmission channels operate at different speeds:

| Transmission Type | Typical Lag | Notes |
|-------------------|-------------|-------|
| Financial market | Days to weeks | Near-instantaneous in model (same time step) |
| Commodity prices | Weeks to months | Near-instantaneous in annual model |
| Trade flows | Quarters to years | 1-2 year lag for demand transmission |
| Migration | Months to years | Event-driven, then gradual flow |
| Climate impacts | Years to decades | Slow accumulation, threshold effects |
| Technology adoption | Years to decades | Diffusion curves vary by technology and country |

**Modeling implication:** In an annual time-step model, financial and commodity transmission can be treated as contemporaneous. Trade and migration effects may warrant lagged implementation.

---

## 7. Transmission Coefficients: Structure

This section outlines the coefficient structure. Specific values require empirical estimation and will be documented in the initialization methodology.

### 7.1 Commodity Passthrough Coefficients

For each country, define:

| Coefficient | Determines | Estimation Basis |
|-------------|------------|------------------|
| `oil_passthrough` | Δinflation per Δoil | Energy import dependence, historical regressions |
| `food_passthrough` | Δinflation per Δwheat | Food import dependence, consumption shares |
| `food_stress_coefficient` | Δprotest per Δwheat | Historical food-unrest correlations |

### 7.2 Financial Transmission Coefficients

For each country, define:

| Coefficient | Determines | Estimation Basis |
|-------------|------------|------------------|
| `rate_sensitivity` | Δborrowing_cost per Δus_10yr | External debt, reserves, historical spreads |
| `spread_sensitivity` | Δcapital_flows per Δcredit_spread | EM vulnerability indicators |
| `contagion_exposure` | Correlation with EM crisis index | Historical crisis episodes |

### 7.3 Climate Transmission Coefficients

For each country, define:

| Coefficient | Determines | Estimation Basis |
|-------------|------------|------------------|
| `agricultural_climate_sensitivity` | Yield impact per Δtemp | Crop models, historical data |
| `heat_productivity_impact` | Labor productivity loss per Δtemp | Occupational exposure, wet-bulb thresholds |
| `sea_level_damage_function` | Infrastructure cost per Δsea_level | Coastal exposure, elevation data |

### 7.4 Trade Transmission Coefficients

| Coefficient | Determines | Estimation Basis |
|-------------|------------|------------------|
| `bilateral_trade_matrix` | Export exposure by partner | UN Comtrade data |
| `demand_elasticity` | Export response to partner GDP | Trade elasticity literature |

---

## 8. Implementation Considerations

### 8.1 Avoiding Double-Counting

Some transmission channels overlap with event impacts. For example:
- Oil supply shock event may directly shock `oil_brent`
- Transmission then propagates oil price to importing country inflation

Ensure events shock *source* variables; transmission propagates to *dependent* variables. Don't have events directly shock both.

### 8.2 Simultaneity

Some transmission is simultaneous (oil price affects inflation which affects policy which affects growth which affects oil demand). In annual time steps:
- Use lagged values for feedback loops, OR
- Iterate to equilibrium within time step, OR
- Accept that annual aggregation smooths these dynamics

Recommendation: Use lagged values for simplicity in v1.0; refine if sensitivity analysis shows it matters.

### 8.3 Nonlinearity and Thresholds

Several transmission channels are nonlinear:
- Climate impacts accelerate beyond temperature thresholds
- Financial stress may be absorbed up to a point, then trigger crisis
- Food price transmission to unrest may have threshold effects

Model with piecewise linear or logistic functions where nonlinearity is important.

### 8.4 Transmission vs. Event Probability Conditioning

Political stress observables require careful treatment. The key distinction:

**Direct transmission** (appropriate for continuous variables that fluctuate with conditions):
- Food prices → `protest_intensity_annual`: Protests rise with food costs even absent discrete events
- Economic stress (unemployment, inflation) → `protest_intensity_annual`: Same logic
- These are genuine variable → variable transmissions

**Event probability conditioning** (appropriate for discrete events):
- Economic stress → P(coup attempt): Coups are discrete events; stress raises probability but doesn't directly increment `coup_attempts_10yr`
- External conflict → P(spillover conflict onset): Conflict spread is event-driven
- These belong in event specifications, not transmission

**Implementation:** For `protest_intensity_annual`, model direct transmission from economic stress indicators:
```
Δprotest_intensity = α × Δwheat_price × food_import_dependence
                   + β × Δunemployment_rate
                   + γ × max(0, Δinflation_rate - threshold)
```

For other political stress observables (`coup_attempts_10yr`, `internal_conflict_intensity`, `years_since_irregular_transition`), changes occur via events whose probabilities are conditioned on state variables. See individual event specifications.

### 8.5 Open Questions

The following require further specification:

1. **Passthrough coefficient estimation:** What are country-specific oil and food passthrough coefficients? Historical regression analysis needed.

2. **Financial contagion structure:** How correlated are EM crises? What's the contagion matrix?

3. **Climate damage functions:** What are the specific yield and productivity impacts per degree of warming by country?

4. **Trade elasticities:** How responsive are trade flows to GDP changes?

These will be addressed in the initialization methodology document (future work).

---

## 9. Cross-References

| Topic | See Document |
|-------|--------------|
| Variable definitions | [[methodology/reference/state-variables-country]], [[methodology/reference/state-variables-global]] |
| How variables evolve over time | [[methodology/reference/state-dynamics]] |
| Factor → event → state relationships | [[methodology/reference/factor-loadings]] |
| Event impact specifications | Individual event documents in [[events/]] |
| Output computations | [[methodology/reference/state-outputs]] |

---

*This document specifies how variables affect each other. For how variables evolve independently see [[methodology/reference/state-dynamics]]. For output specifications see [[methodology/reference/state-outputs]].*