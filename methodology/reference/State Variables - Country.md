---
title: State Variables - Country
type: note
permalink: methodology/reference/state-variables-country
tags:
- methodology
- reference
- state
- variables
- country
- observables
---

# Country-Level State Variables

## Complete Catalog of Country and Regional Aggregate Variables

**Document Version:** 2.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

**Related documents:**
- [[methodology/reference/state-overview]] — Entry point for state model
- [[methodology/reference/state-entities]] — The 40 countries and 12 regional aggregates
- [[methodology/reference/state-variables-global]] — Global variable catalog
- [[methodology/concepts/synthetic-variable-problem]] — Rationale for observable decomposition

---

## 1. Purpose & Scope

This document catalogs all country-level state variables tracked by the simulation. Each of the 40 individually-modeled countries tracks these variables. Tier 1 regional aggregates track the same set; Tier 2 aggregates track a subset (noted below).

### Design Principles

**Observable over synthetic:** Per [[methodology/concepts/synthetic-variable-problem]], we prefer directly measurable variables over expert assessment indices. Variables like "regime stability" and "institutional quality" have been decomposed into observable components. Synthetic assessments (fragility, alignment scores) are computed as outputs for human interpretation, not used as state variables.

**Clear update semantics:** Each variable has a defined measurement procedure and data source. When events shock variables, the magnitudes have real-world referents.

**Calibration-ready:** Observable variables enable comparison against historical data for weight estimation and validation.

### Variable Count Summary

| Category | Variables |
|----------|-----------|
| Demographic stocks | 12 |
| Demographic flows | 8 |
| Economic stocks | 6 |
| Economic flows | 4 |
| Economic structure | 5 |
| Political & governance | 12 |
| Climate & resource | 6 |
| Strategic position | 13 |
| **Total** | **66** |

---

## 2. Demographic Variables

### 2.1 Population Stocks (12 variables)

Compressed population pyramid by sex and functional age cohort.

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `pop_0_14_m` | Male children (0-14) | Millions | UN Pop Division |
| `pop_0_14_f` | Female children (0-14) | Millions | UN Pop Division |
| `pop_15_34_m` | Male young working age (15-34) | Millions | UN Pop Division |
| `pop_15_34_f` | Female young working age (15-34) | Millions | UN Pop Division |
| `pop_35_54_m` | Male prime working age (35-54) | Millions | UN Pop Division |
| `pop_35_54_f` | Female prime working age (35-54) | Millions | UN Pop Division |
| `pop_55_64_m` | Male older working age (55-64) | Millions | UN Pop Division |
| `pop_55_64_f` | Female older working age (55-64) | Millions | UN Pop Division |
| `pop_65_79_m` | Male young elderly (65-79) | Millions | UN Pop Division |
| `pop_65_79_f` | Female young elderly (65-79) | Millions | UN Pop Division |
| `pop_80_plus_m` | Male old elderly (80+) | Millions | UN Pop Division |
| `pop_80_plus_f` | Female old elderly (80+) | Millions | UN Pop Division |

**Dynamics:** Deterministic cohort aging + mortality/fertility/migration flows.

### 2.2 Demographic Flows (8 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `tfr` | Total fertility rate | Children per woman | UN Pop Division |
| `life_expectancy` | Life expectancy at birth | Years | UN Pop Division |
| `infant_mortality` | Infant mortality rate | Deaths per 1,000 live births | UN Pop Division |
| `net_migration_rate` | Net migration as share of population | % per year | UN Pop Division |
| `emigration_skilled_rate` | Emigration rate of skilled workers (15-34 educated) | % per year | World Bank |
| `idp_population` | Internally displaced persons | Millions | IDMC |
| `refugees_abroad` | Refugees from this country living in other countries | Millions | UNHCR |
| `refugees_hosted` | Refugees from other countries hosted here | Millions | UNHCR |

**Dynamics:** Fertility, mortality, and migration rates are slow-moving with event shocks (pandemic mortality, conflict displacement, economic pull/push).

**Displacement dynamics:** Displacement variables are event-driven with slow decay:
- `idp_population`: Event-driven increase; half-life ~10-15 years; conflict resolution enables faster return
- `refugees_abroad`: Event-driven increase; half-life ~15-20 years; repatriation is slow even after crisis resolution
- `refugees_hosted`: Driven by `refugees_abroad` in neighboring countries; policy-dependent

Cross-country refugee transfers maintain global consistency per [[methodology/reference/state-transmission]].

**Derived displacement measures** (computed, not stored):
| Measure | Formula | Meaning |
|---------|---------|---------|
| `displaced_present` | `idp_population` + `refugees_hosted` | Total displaced persons physically IN this country (burden measure) |
| `displacement_caused` | `idp_population` + `refugees_abroad` | Total displacement originating FROM this country's crisis (severity measure) |

### 2.3 Derived Demographic Indicators

Computed from population stocks, not stored separately:

| Indicator | Formula |
|-----------|---------|
| `pop_total` | Sum of all cohorts |
| `pop_working_age` | Sum of 15-64 cohorts |
| `dependency_ratio` | (0-14 + 65+) / (15-64) |
| `youth_bulge_index` | (15-34) / (15+) |
| `median_age` | Estimated from cohort distribution |
| `military_age_males` | `pop_15_34_m` |

---

## 3. Economic Variables

### 3.1 Economic Stocks (6 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `gdp_real` | Real GDP (2025 base) | $T | IMF WEO |
| `gdp_per_capita` | Real GDP per capita (2025 base) | $K | IMF WEO |
| `debt_public` | Public debt | % of GDP | IMF Fiscal Monitor |
| `debt_external` | External debt | % of GDP | World Bank IDS |
| `reserves_foreign` | Foreign exchange reserves | Months of imports | IMF IFS |
| `current_account` | Current account balance | % of GDP | IMF WEO |

**Dynamics:** Stock variables evolve via flow dynamics and event shocks.

### 3.2 Economic Flows (4 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `gdp_growth` | Real GDP growth rate | % per year | IMF WEO |
| `inflation_rate` | Consumer price inflation | % per year | IMF WEO |
| `unemployment_rate` | Unemployment rate | % of labor force | ILO |
| `fdi_net` | Net foreign direct investment | % of GDP | UNCTAD |

**Dynamics:** Mean-reverting around country-specific equilibria; event shocks.

### 3.3 Economic Structure (5 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `gdp_share_agriculture` | Agriculture share of GDP | % | World Bank WDI |
| `gdp_share_industry` | Industry share of GDP | % | World Bank WDI |
| `gdp_share_services` | Services share of GDP | % | World Bank WDI |
| `export_concentration` | Export concentration (Herfindahl index) | 0-1 | UNCTAD |
| `trade_openness` | Trade openness (exports + imports) | % of GDP | World Bank WDI |

**Dynamics:** Slow structural change; major events (commodity shocks, trade ruptures) can shift.

### 3.4 Derived Economic Indicators

Computed from economic variables:

| Indicator | Formula |
|-----------|---------|
| `debt_service_ratio` | Annual debt service / government revenue |
| `fiscal_space` | Composite of debt, reserves, current account |
| `default_probability` | Derived from debt dynamics model |

---

## 4. Political & Governance Variables

### 4.1 Design Rationale

This category has been substantially revised from the original specification. Per [[methodology/concepts/synthetic-variable-problem]], we eliminated synthetic indices (`regime_stability`, `institutional_quality`, `state_capacity`, `corruption_index`, `civil_liberties`) and replaced them with observable indicators.

**What we eliminated and why:**

| Former Variable | Problem | Replacement Approach |
|-----------------|---------|---------------------|
| `regime_stability` | Circular: used to predict what it purports to measure | Observable stress indicators |
| `institutional_quality` | Expert assessment; opaque update semantics | Observable governance metrics |
| `state_capacity` | Overlapped with institutional_quality | Merged into governance metrics |
| `corruption_index` | Perception-based; unclear causal role | Track consequences via FDI, efficiency |
| `civil_liberties` | Expert-coded index | Captured by `regime_type`; detailed assessment moved to outputs |

The observable replacements enable:
- **Auditability:** Can trace why P(state_failure) is high — which specific indicators are elevated?
- **Calibration:** Historical cases provide ground truth for observable values before failures
- **Clear shocks:** Event impacts have magnitudes with real-world referents

### 4.2 Political Stress Indicators (6 variables)

Observable indicators of political instability risk.

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `years_since_irregular_transition` | Years since last coup, revolution, or unconstitutional transfer | Integer | Polity, historical record |
| `coup_attempts_10yr` | Coup attempts in past 10 years (successful or failed) | Count | Powell-Thyne dataset, ACLED |
| `leadership_tenure_years` | Current head of state/government tenure | Integer | Observable |
| `cabinet_turnover_annual` | Proportion of cabinet replaced in past year | 0-1 | News monitoring |
| `political_prisoner_estimate` | Estimated political prisoners held | Count | Amnesty, HRW |
| `press_freedom_events` | Journalist arrests + outlet closures (annual) | Count | CPJ, RSF |

**Dynamics:** `years_since_irregular_transition` increments annually, resets on transition events. Others updated by events and annual monitoring.

**Usage:** These condition Type 2 event probabilities (state failure, regime change) via explicit functions rather than opaque "stability" scores.

### 4.3 Governance Indicators (3 variables)

Observable measures of government effectiveness.

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `tax_revenue_gdp` | General government tax revenue | % of GDP | IMF GFS |
| `budget_execution_rate` | Actual spending / approved budget | % | IMF, World Bank PFM data |
| `public_investment_efficiency` | Output per dollar of public investment | Index (country avg = 100) | IMF PIMA |

**Dynamics:** Slow-moving structural parameters; shocks from institutional crises.

**Note:** These replace the former `institutional_quality` and `state_capacity` with measurable outcomes rather than expert assessments.

### 4.4 Political Structure (2 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `regime_type` | Basic political system character | Categorical | Polity, V-Dem, Freedom House |
| `protest_intensity_annual` | Mass protest/unrest activity level | 0-100 index | ACLED event counts |

**Regime type categories:**
- **Democracy:** Competitive elections, peaceful transfers, basic civil liberties
- **Hybrid:** Elections occur but flawed; contested legitimacy; partial civil liberties  
- **Authoritarian:** No competitive elections; single party/leader/military rule; limited civil liberties

**Dynamics:** `regime_type` changes via discrete events (democratic_breakdown, democratic_transition), not gradual drift. `protest_intensity_annual` updated from event data.

### 4.5 Conflict Indicators (1 variable)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `internal_conflict_intensity` | Internal armed conflict intensity | 0-4 scale | UCDP/PRIO |

**Scale:**
- 0: No significant armed conflict
- 1: Minor armed conflict (<25 battle deaths/year)
- 2: Intermediate conflict (25-999 battle deaths/year)
- 3: War (1,000+ battle deaths/year)
- 4: Major war (10,000+ battle deaths/year or state collapse)

**Dynamics:** Event-driven (conflict onset, escalation, resolution).

---

## 5. Climate & Resource Variables

### 5.1 Climate Exposure (4 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `water_stress` | Water stress index (withdrawals/supply) | 0-100 | WRI Aqueduct |
| `heat_exposure` | Heat exposure index (wet-bulb risk) | 0-100 | Climate models |
| `agricultural_climate_risk` | Agricultural climate vulnerability | 0-100 | FAO, climate models |
| `sea_level_exposure` | Population exposed to sea level rise | % of total | Climate Central |

**Dynamics:** Driven by global climate variables (`global_temp_anomaly`, `sea_level_global`) with country-specific exposure coefficients.

### 5.2 Resource Dependence (2 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `energy_import_dependence` | Net energy imports | % of consumption | IEA |
| `food_import_dependence` | Net food imports | % of consumption | FAO |

**Note:** Negative values indicate net exporter status.

**Dynamics:** Slow structural change; shocks from supply disruptions, demand shifts.

---

## 6. Strategic Position Variables

### 6.1 Design Rationale

The original specification included continuous alignment scores (`alliance_west`, `alliance_china`, `alliance_nonaligned`) with no clear measurement procedure. Per [[methodology/concepts/synthetic-variable-problem]], we replaced these with:

1. A **categorical alliance status** with observable criteria
2. **Observable alignment indicators** that can be measured from data

This enables clear update semantics: an event can shift `arms_import_share_west` by a defined amount, whereas "reduce alliance_west by 10 points" had no real-world referent.

### 6.2 Alliance Status (1 variable)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `alliance_status` | Formal alliance/security arrangement | Categorical | Treaty records |

**Categories:**
- `NATO_MEMBER`: Full NATO membership
- `NATO_PARTNER`: NATO partnership (PfP, Enhanced Opportunities, etc.)
- `US_BILATERAL_ALLY`: Bilateral defense treaty with US (Japan, Korea, Philippines, Australia, Thailand)
- `SCO_MEMBER`: Shanghai Cooperation Organisation full member
- `CHINA_SECURITY_PARTNER`: Formal security arrangement with China
- `MULTI_ALIGNED`: Formal arrangements with both blocs
- `NON_ALIGNED`: No formal security arrangement with major powers

**Dynamics:** Event-driven (alliance formation, dissolution, switching).

### 6.3 Alignment Indicators (6 variables)

Observable behavioral measures of alignment.

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `un_voting_alignment_us` | Correlation of UNGA votes with US | -1 to +1 | UN voting records |
| `un_voting_alignment_china` | Correlation of UNGA votes with China | -1 to +1 | UN voting records |
| `arms_import_share_west` | Arms imports from NATO countries | % of total | SIPRI |
| `arms_import_share_east` | Arms imports from Russia/China | % of total | SIPRI |
| `trade_share_west` | Trade with US + EU + allies | % of total trade | UN Comtrade |
| `trade_share_china` | Trade with China | % of total trade | UN Comtrade |

**Dynamics:** Slow drift + event shocks (trade ruptures, sanctions, realignment).

**Note:** For human interpretation, an "alignment profile" can be computed from these observables at analysis time — but the profile is an output, not a state variable conditioning probabilities.

### 6.4 Security Indicators (4 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `military_spending` | Military expenditure | % of GDP | SIPRI |
| `military_spending_deviation` | Deviation from country's 10-year average | Standard deviations | Computed |
| `armed_forces_per_capita` | Active military personnel | Per 1,000 population | IISS Military Balance |
| `external_conflict_involvement` | External armed conflict involvement | 0-4 scale | UCDP |

**External conflict scale:** Same as internal conflict (0=none through 4=major war).

**Note:** `military_spending_deviation` captures unusual military buildups that may signal preparation for conflict, independent of baseline spending levels.

### 6.5 Sanctions & Nuclear Status (2 variables)

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `sanctions_level` | Aggregate sanctions severity | 0-100 | GSDB, observable |
| `nuclear_status` | Nuclear weapons status | Categorical | Observable |

**Sanctions scale:**
- 0: No significant sanctions
- 25: Targeted/limited sanctions (individuals, specific sectors)
- 50: Broad sectoral sanctions
- 75: Comprehensive sanctions with carve-outs
- 100: Maximum pressure / near-complete isolation

**Nuclear status categories:**
- `NONE`: No nuclear weapons program
- `THRESHOLD`: Latent capability or suspected program
- `POSSESSED`: Confirmed nuclear weapons state

**Dynamics:** Event-driven (sanctions imposition/removal, proliferation events).

---

## 7. Summary

### 7.1 Variable Count by Category

| Category | Variables | Tier 2 Subset |
|----------|-----------|---------------|
| Demographic stocks | 12 | 4 (totals only) |
| Demographic flows | 8 | 6 |
| Economic stocks | 6 | 3 |
| Economic flows | 4 | 2 |
| Economic structure | 5 | 0 |
| Political & governance | 12 | 4 |
| Climate & resource | 6 | 3 |
| Strategic position | 13 | 3 |
| **Total** | **66** | **25** |

### 7.2 Tier 2 Aggregate Treatment

Tier 2 aggregates (Central Asia other, Southeast Asia other, Andean/Caribbean, Maghreb, Southern Africa other, West/Central Africa other) track a reduced variable set for computational tractability.

**Tier 2 variables (25):**

| Category | Variables Tracked |
|----------|-------------------|
| Demographics | `pop_total`, `pop_working_age`, `tfr`, `life_expectancy`, `net_migration_rate`, `idp_population`, `refugees_abroad`, `refugees_hosted` |
| Economics | `gdp_real`, `gdp_per_capita`, `debt_external`, `gdp_growth`, `inflation_rate` |
| Political | `regime_type`, `internal_conflict_intensity`, `protest_intensity_annual`, `years_since_irregular_transition` |
| Climate | `water_stress`, `heat_exposure`, `food_import_dependence` |
| Strategic | `alliance_status`, `sanctions_level`, `external_conflict_involvement` |

### 7.3 Total State Space

| Entity Type | Count | Variables Each | Total |
|-------------|-------|----------------|-------|
| Individual countries | 40 | 66 | 2,640 |
| Tier 1 aggregates | 6 | 66 | 396 |
| Tier 2 aggregates | 6 | 25 | 150 |
| **Total country/regional** | **52** | — | **3,186** |

---

## 8. Data Sources Summary

| Source | Variables Covered |
|--------|-------------------|
| UN Population Division | All demographic stocks and flows (except displacement) |
| IMF WEO | GDP, growth, inflation, current account |
| IMF Fiscal Monitor | Public debt |
| IMF GFS | Tax revenue |
| World Bank WDI | Economic structure, development indicators |
| World Bank IDS | External debt |
| SIPRI | Military spending, arms transfers |
| IISS Military Balance | Armed forces |
| UCDP/PRIO | Conflict intensity |
| ACLED | Protests, political violence events |
| Polity/V-Dem | Regime type, transitions |
| Powell-Thyne | Coup attempts |
| CPJ/RSF | Press freedom events |
| Amnesty/HRW | Political prisoners |
| WRI Aqueduct | Water stress |
| FAO | Food security, agricultural data |
| IEA | Energy data |
| UN Comtrade | Trade flows |
| UN DGACM | UNGA voting records |
| UNHCR | Refugees abroad, refugees hosted |
| IDMC | Internally displaced persons |

---

## 9. Derived Assessments (Outputs Only)

The following assessments are computed from observables for human interpretation. They are **outputs**, not state variables — they don't condition event probabilities or get updated by shocks.

See [[methodology/reference/state-outputs]] for computation specifications.

| Assessment | Computed From |
|------------|---------------|
| Stability assessment | Political stress indicators, economic stress, conflict |
| Fragility assessment | Inverse of stability |
| Alignment profile | Alliance status + alignment indicators |
| Climate vulnerability | Climate exposure variables + economic structure |
| Fiscal sustainability | Debt, reserves, growth, tax capacity |

---

*This catalog specifies what the simulation tracks at country level. For dynamics (how variables evolve) see [[methodology/reference/state-dynamics]]. For transmission (how variables affect each other) see [[methodology/reference/state-transmission]].*