---
title: State Outputs
type: note
permalink: methodology/reference/state-outputs
tags:
- methodology
- reference
- state
- outputs
- assessments
- distributions
- analysis
---

# State Outputs

## What the Simulation Produces

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

**Related documents:**
- [[methodology/reference/state-overview]] — Entry point for state model
- [[methodology/reference/state-variables-country]] — Country-level variable catalog
- [[methodology/reference/state-variables-global]] — Global variable catalog
- [[methodology/reference/state-dynamics]] — How variables evolve over time
- [[methodology/reference/state-transmission]] — How variables affect each other
- [[methodology/concepts/synthetic-variable-problem]] — Why assessments are outputs, not state variables

---

## 1. Purpose & Scope

This document specifies what the simulation produces: the outputs available for analysis after simulation runs complete. Outputs include raw state data, derived assessments for human interpretation, and distributional summaries across runs.

### Key Principle: Assessments Are Outputs, Not State Variables

Per [[methodology/concepts/synthetic-variable-problem]], interpretive assessments (stability, fragility, alignment profiles, geopolitical tension indices) are **computed from observables at analysis time**. They are outputs for human understanding, not state variables that condition event probabilities.

This distinction matters because:
- **State variables** are tracked during simulation and may condition event probabilities
- **Output assessments** are computed after simulation for interpretation and reporting
- Mixing them creates circular reasoning and opaque update semantics

---

## 2. Output Categories

| Category | Description | When Computed |
|----------|-------------|---------------|
| **Terminal State** | Full state vector at simulation end (or any time point) | Per run |
| **Trajectory Data** | Time series of selected variables | Per run |
| **Event Log** | Record of all events that fired | Per run |
| **Derived Assessments** | Human-interpretable indices computed from observables | Post-run |
| **Distributional Summaries** | Percentiles, scenario counts across all runs | Cross-run |

---

## 3. Terminal State Outputs

At simulation end (2075) or any specified assessment year, each run produces:

### 3.1 Full State Vector

Complete values for all state variables:

| Entity Type | Count | Variables Each | Total Variables |
|-------------|-------|----------------|-----------------|
| Individual countries | 40 | 63 | 2,520 |
| Tier 1 aggregates | 6 | 63 | 378 |
| Tier 2 aggregates | 6 | 22 | 132 |
| Global | 1 | 42 | 42 |
| **Total** | **53** | — | **3,072** |

This is the raw simulation output—every tracked variable for every entity at the assessment time.

### 3.2 Country Summary Statistics

For each country, compute summary measures from the state vector:

| Statistic | Definition | Units |
|-----------|------------|-------|
| `population_change` | (pop_total_end - pop_total_2025) / pop_total_2025 | % |
| `gdp_change` | (gdp_real_end - gdp_real_2025) / gdp_real_2025 | % |
| `gdp_per_capita_change` | (gdp_pc_end - gdp_pc_2025) / gdp_pc_2025 | % |
| `life_expectancy_change` | life_expectancy_end - life_expectancy_2025 | Years |
| `conflict_years` | Count of years with `internal_conflict_intensity` ≥ 2 | Count |
| `regime_changes` | Count of `regime_type` transitions | Count |

### 3.3 Regional Rollups

Aggregate statistics for geographic regions (population-weighted where appropriate):

| Region | Countries Included |
|--------|-------------------|
| North America | US, Canada, Mexico |
| Europe | Germany, UK, France, Italy, Spain, Netherlands, Poland, Ukraine, Rest of EU |
| East Asia | China, Japan, South Korea, Taiwan, North Korea |
| South Asia | India, Pakistan, Bangladesh |
| Southeast Asia | Indonesia, Vietnam, Thailand, Philippines, Singapore, SE Asia (other) |
| MENA | Turkey, Iran, Saudi Arabia, Egypt, Israel, UAE, Gulf States, Levant/Iraq, Maghreb |
| Sub-Saharan Africa | Nigeria, Ethiopia, DRC, South Africa, Kenya, Sahel, East Africa, Southern Africa (other), West/Central Africa (other) |
| Latin America | Brazil, Argentina, Central America, Andean/Caribbean |
| Oceania | Australia |
| Eurasia | Russia, Kazakhstan, Central Asia (other) |

*Note: Mexico is grouped with North America due to economic integration (USMCA, trade flows). For cultural/linguistic analysis, Mexico may alternatively be grouped with Latin America.*

Regional outputs include:
- Total population
- Aggregate GDP
- Population-weighted average GDP per capita
- Population-weighted average life expectancy
- Count of countries in conflict
- Count of state failures

---

## 4. Trajectory Outputs

Time series data for analyzing paths, not just endpoints.

### 4.1 Key Variable Time Series

For selected high-importance variables, store annual values across the full simulation horizon:

**Global trajectories:**
- `global_temp_anomaly`
- `sea_level_global`
- `oil_brent`
- `usd_reserve_share`
- `global_credit_spread`
- `active_major_conflicts`

**Major country trajectories:**
- GDP for: US, China, India, Germany, Japan, Brazil, Russia
- Population for: India, China, Nigeria, US, Indonesia
- `internal_conflict_intensity` for all countries

### 4.2 Event Occurrence Log

Record of all discontinuity events that fired during the run:

| Field | Description |
|-------|-------------|
| `event_id` | Event identifier (e.g., `TAIWAN_CONFLICT`) |
| `year` | Year of occurrence |
| `branch` | Which aftermath branch was selected |
| `severity` | Severity draw (if applicable) |
| `duration` | Event duration (if applicable) |
| `affected_entities` | List of countries/regions affected |

This log enables:
- Tracing which events drove specific outcomes
- Analyzing event co-occurrence patterns
- Debugging unexpected trajectories

### 4.3 Cumulative Impact Tracking

Running totals of key impacts across the simulation:

| Metric | Definition |
|--------|------------|
| `cumulative_excess_deaths` | Deaths above baseline trajectory (from conflicts, pandemics, climate) |
| `cumulative_displacement` | Person-years of displacement |
| `cumulative_gdp_loss` | GDP shortfall vs. no-event baseline trajectory |
| `cumulative_climate_damage` | Economic losses attributed to climate impacts |

These enable comparison of total human costs across scenarios, not just endpoint states.

---

## 5. Derived Assessments

Computed from observable state variables for human interpretation. These are **outputs only**—they do not condition event probabilities and are not updated during simulation.

### 5.1 Country Stability Assessment

Computed from political, economic, and security observables.

```python
def compute_stability_assessment(state, country) -> float:
    """
    Compute stability assessment from observable state variables.
    Returns value 0-100 where higher = more stable.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    # Political factors (40% weight)
    political = (
        0.15 * tenure_score(state[country].years_since_irregular_transition) +
        0.10 * inverse_score(state[country].coup_attempts_10yr, max_val=5) +
        0.10 * inverse_score(state[country].protest_intensity_annual, max_val=100) +
        0.05 * inverse_score(state[country].cabinet_turnover_annual, max_val=0.8)
    )
    
    # Economic factors (35% weight)
    economic = (
        0.15 * growth_score(state[country].gdp_growth) +
        0.10 * inverse_score(state[country].inflation_rate, max_val=50) +
        0.05 * inverse_score(state[country].unemployment_rate, max_val=30) +
        0.05 * reserves_score(state[country].reserves_foreign)
    )
    
    # Security factors (25% weight)
    security = (
        0.15 * inverse_score(state[country].internal_conflict_intensity, max_val=4) +
        0.10 * inverse_score(state[country].external_conflict_involvement, max_val=4)
    )
    
    return 100 * (political + economic + security)
```

**Helper functions:**
- `tenure_score(years)`: Higher score for longer time since irregular transition; diminishing returns after ~20 years
- `inverse_score(value, max_val)`: Returns (max_val - value) / max_val, clamped to [0, 1]
- `growth_score(growth)`: Positive growth scores high; negative growth scores low; nonlinear
- `reserves_score(months)`: Higher score for more reserve coverage; diminishing returns after ~6 months

### 5.2 Country Fragility Assessment

Simply the inverse of stability:

```python
def compute_fragility_assessment(state, country) -> float:
    """
    Compute fragility assessment from observable state variables.
    Returns value 0-100 where higher = more fragile.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    return 100 - compute_stability_assessment(state, country)
```

### 5.3 Country Alignment Profile

Computed from alliance status and observable alignment indicators.

```python
def compute_alignment_profile(state, country) -> dict:
    """
    Compute alignment profile from observable indicators.
    Returns dict with west/china/nonaligned scores (0-100 each).
    
    FOR HUMAN INTERPRETATION ONLY - NOT STATE VARIABLES
    """
    # Alliance status contribution (25%)
    alliance_west = alliance_status_west_score(state[country].alliance_status)
    alliance_china = alliance_status_china_score(state[country].alliance_status)
    
    # Behavioral indicators (75%)
    # UN voting (25%)
    un_west = (state[country].un_voting_alignment_us + 1) / 2 * 100  # Convert -1,+1 to 0-100
    un_china = (state[country].un_voting_alignment_china + 1) / 2 * 100
    
    # Arms imports (25%)
    arms_west = state[country].arms_import_share_west
    arms_china = state[country].arms_import_share_east
    
    # Trade (25%)
    trade_west = min(100, state[country].trade_share_west * 2)  # Scale up; 50% trade = 100 score
    trade_china = min(100, state[country].trade_share_china * 4)  # Scale up; 25% trade = 100 score
    
    # Composite scores
    west = 0.25 * alliance_west + 0.25 * un_west + 0.25 * arms_west + 0.25 * trade_west
    china = 0.25 * alliance_china + 0.25 * un_china + 0.25 * arms_china + 0.25 * trade_china
    
    # Non-aligned is residual
    nonaligned = max(0, 100 - max(west, china))
    
    return {'west': west, 'china': china, 'nonaligned': nonaligned}
```

**Alliance status scoring:**
- `NATO_MEMBER`, `US_BILATERAL_ALLY`: west=100, china=0
- `SCO_MEMBER`, `CHINA_SECURITY_PARTNER`: west=0, china=100
- `MULTI_ALIGNED`: west=50, china=50
- `NON_ALIGNED`, `NATO_PARTNER`: west=25, china=0 (or country-specific)

### 5.4 Climate Vulnerability Assessment

Computed from climate exposure variables and economic structure.

```python
def compute_climate_vulnerability(state, country) -> float:
    """
    Compute climate vulnerability from exposure and capacity indicators.
    Returns value 0-100 where higher = more vulnerable.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    # Exposure factors (60%)
    exposure = (
        0.20 * state[country].heat_exposure +
        0.15 * state[country].water_stress +
        0.15 * state[country].agricultural_climate_risk +
        0.10 * state[country].sea_level_exposure * 10  # Scale up from % to 0-100
    )
    
    # Sensitivity factors (25%)
    # GDP/capita threshold ~$50K: above this, sensitivity approaches zero
    # Below this, lower income = higher sensitivity to climate shocks
    gdp_pc = state[country].gdp_per_capita  # in $K
    income_sensitivity = max(0, 100 - gdp_pc * 2)  # $50K → 0, $0 → 100
    
    sensitivity = (
        0.15 * state[country].food_import_dependence +
        0.10 * income_sensitivity
    )
    
    # Adaptive capacity inverse (15%)
    # Lower GDP/capita = lower capacity to adapt
    capacity_inverse = 0.15 * income_sensitivity
    
    return min(100, exposure + sensitivity + capacity_inverse)
```

### 5.5 Fiscal Sustainability Assessment

Computed from debt, reserves, and fiscal flow indicators.

```python
def compute_fiscal_sustainability(state, country) -> float:
    """
    Compute fiscal sustainability score.
    Returns value 0-100 where higher = more sustainable.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    # Debt burden (40% weight, inverse)
    debt_score = max(0, 100 - state[country].debt_public)  # 100% debt = 0 score
    
    # External position (30% weight)
    external = (
        0.15 * min(100, state[country].reserves_foreign * 10) +  # 10 months = 100
        0.15 * max(0, 50 + state[country].current_account * 5)   # +10% CA = 100, -10% = 0
    )
    
    # Fiscal capacity (30% weight)
    fiscal = (
        0.15 * min(100, state[country].tax_revenue_gdp * 3) +  # 33% tax/GDP = 100
        0.15 * min(100, state[country].budget_execution_rate)
    )
    
    return 0.40 * debt_score + external + fiscal
```

### 5.6 Geopolitical Structure Assessments

Global-level assessments computed from country observables. These were formerly global state variables; now computed as outputs only.

#### US-China Tension Index

```python
def compute_us_china_tension(state) -> float:
    """
    Compute US-China tension index from observable indicators.
    Returns value 0-100 where higher = more tension.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    # Trade relationship (25%)
    trade_tension = 100 - min(100, (
        state['USA'].trade_share_china + state['CHN'].trade_share_west
    ) * 2)  # Lower bilateral trade = higher tension
    
    # Military indicators (35%)
    military = (
        0.15 * state['USA'].military_spending_deviation * 20 +  # Buildup signals tension
        0.15 * state['CHN'].military_spending_deviation * 20 +
        0.05 * (state['TWN'].external_conflict_involvement * 25)  # Taiwan involvement
    )
    
    # Sanctions (20%)
    sanctions = state['CHN'].sanctions_level
    
    # Alliance competition (20%)
    # Count of countries shifting alignment
    alignment_competition = compute_alignment_shift_index(state)
    
    return min(100, 0.25 * trade_tension + military + 0.20 * sanctions + 0.20 * alignment_competition)
```

#### NATO Cohesion Index

```python
def compute_nato_cohesion(state) -> float:
    """
    Compute NATO alliance cohesion from member state indicators.
    Returns value 0-100 where higher = more cohesive.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    nato_members = ['USA', 'GBR', 'FRA', 'DEU', 'ITA', 'ESP', 'POL', 'NLD', 'TUR', ...]
    
    # Defense spending commitment (40%)
    spending_scores = [
        min(100, state[c].military_spending / 0.02 * 100)  # 2% GDP = 100
        for c in nato_members
    ]
    avg_spending = sum(spending_scores) / len(spending_scores)
    
    # Alignment consistency (30%)
    alignment_scores = [
        compute_alignment_profile(state, c)['west']
        for c in nato_members
    ]
    alignment_variance = compute_variance(alignment_scores)
    alignment_cohesion = max(0, 100 - alignment_variance)
    
    # Conflict involvement unity (30%)
    # All members involved in same conflicts, or none = high cohesion
    conflict_unity = compute_conflict_unity(state, nato_members)
    
    return 0.40 * avg_spending + 0.30 * alignment_cohesion + 0.30 * conflict_unity
```

#### EU Cohesion Index

```python
def compute_eu_cohesion(state) -> float:
    """
    Compute EU political cohesion from member state indicators.
    Returns value 0-100 where higher = more cohesive.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    eu_members = ['DEU', 'FRA', 'ITA', 'ESP', 'NLD', 'POL', ...]  # Plus Rest of EU aggregate
    
    # Economic convergence (40%)
    gdp_growth_rates = [state[c].gdp_growth for c in eu_members]
    growth_variance = compute_variance(gdp_growth_rates)
    economic_cohesion = max(0, 100 - growth_variance * 10)
    
    # Political alignment (30%)
    # Based on regime_type consistency and protest levels
    political_stress = sum(state[c].protest_intensity_annual for c in eu_members) / len(eu_members)
    political_cohesion = max(0, 100 - political_stress)
    
    # Fiscal solidarity (30%)
    # Based on debt dispersion and external positions
    debt_levels = [state[c].debt_public for c in eu_members]
    debt_variance = compute_variance(debt_levels)
    fiscal_cohesion = max(0, 100 - debt_variance / 2)
    
    return 0.40 * economic_cohesion + 0.30 * political_cohesion + 0.30 * fiscal_cohesion
```

#### Additional Global Assessments

Similar computation patterns for:
- **BRICS Integration Index:** Trade among BRICS, CIPS usage, reserve diversification
- **UN Effectiveness Index:** Based on `active_major_conflicts` trend, peacekeeping capacity
- **Nuclear Stability Index:** Based on nuclear states' conflict involvement, arms control status

---

## 6. Qualitative Assessment Framework

Mapping quantitative state to interpretable categories for reporting.

### 6.1 Country Status Classification

At any assessment point, classify each country:

| Status | Criteria |
|--------|----------|
| **Thriving** | GDP/capita growing >2%/yr, stability assessment >80, no major conflict |
| **Stable** | GDP/capita growing, stability assessment >60, manageable challenges |
| **Stressed** | Slow/no growth, stability assessment 40-60, significant challenges |
| **Crisis** | GDP/capita declining, stability assessment 20-40, active severe problems |
| **Collapsed** | State failure event occurred, stability assessment <20, humanitarian emergency |
| **Recovering** | Improving from crisis/collapse, stability assessment rising >10 points |

### 6.2 Trajectory Classification

Classify change from 2025 to assessment year:

| Trajectory | GDP/capita Change | Stability Change |
|------------|------------------|------------------|
| **Rising** | >+25% | Improved or stable (within ±10) |
| **Stable** | -10% to +25% | Within ±15 points |
| **Declining** | -25% to -10% | Dropped >15 points |
| **Collapsing** | <-25% | Dropped >30 points |
| **Recovering** | Improving from prior collapse | Rising >20 points from trough |

### 6.3 Comparative Assessment

Relative to starting position and peer group:

**Peer groups:**
- G7 advanced economies
- BRICS
- Emerging markets (non-BRICS)
- Frontier markets
- Fragile states

**Assessment dimensions:**
- Absolute change from 2025
- Change relative to peer group average
- Rank change within peer group

### 6.4 Global System Assessment

Aggregate characterization of international system state:

| System State | Criteria |
|--------------|----------|
| **Stable Order** | `active_major_conflicts` ≤ 2, US-China tension <50, major institutions functional |
| **Stressed Order** | 2-3 major conflicts, tension 50-70, institutions strained but operating |
| **Fragmenting Order** | 3+ major conflicts, tension >70, bloc formation accelerating, institutions weakening |
| **Systemic Crisis** | Great power war, or >5 state failures, or global economic collapse (GDP -10%) |

---

## 7. Distributional Outputs

Across simulation runs (e.g., 10,000+ runs), compute:

### 7.1 Percentile Distributions

For each key output variable, report distribution across runs:

| Percentile | Interpretation |
|------------|----------------|
| 5th | Near-worst case (1 in 20 runs) |
| 25th | Pessimistic but plausible |
| 50th | Median outcome |
| 75th | Optimistic but plausible |
| 95th | Near-best case (1 in 20 runs) |

**Example output:**
```
US GDP per Capita 2050 (% change from 2025):
  5th percentile:  -25%
  25th percentile: -5%
  50th percentile: +15%
  75th percentile: +30%
  95th percentile: +45%
```

### 7.2 Scenario Frequency Counts

Count how often defined scenarios occur:

| Scenario | Definition | Example Output |
|----------|------------|----------------|
| US severe decline | GDP/capita -20% or worse | 8% of runs |
| Dollar displacement | `usd_reserve_share` <40% | 15% of runs |
| Great power war | Taiwan conflict or US-China war event | 22% of runs |
| Climate tipping point | AMOC collapse OR Amazon dieback | 12% of runs |
| Humanitarian catastrophe | >100M cumulative displaced | 18% of runs |
| European fragmentation | EU cohesion <30 | 7% of runs |
| Chinese political crisis | China stability assessment <30 | 11% of runs |
| Multi-state collapse | ≥3 state failure events | 9% of runs |

### 7.3 Conditional Distributions

Distribution of outcome Y given condition X occurred:

**Examples:**
- "Distribution of US GDP given AMOC collapse occurred"
- "Distribution of global displacement given 3+ major conflicts"
- "Distribution of `usd_reserve_share` given Chinese economic crisis"

These reveal how specific events shape outcome distributions.

### 7.4 Contribution Analysis

Which events/factors drive tail outcomes?

**Analysis questions:**
- In runs where US GDP declines >20%, which events occurred most frequently?
- What is the correlation of factor realizations (F_GPT, F_CLIM, etc.) with worst-case outcomes?
- Which country failures most often precede global crisis scenarios?

**Output:** Ranked list of events/factors by contribution to tail outcomes, enabling prioritization of Level 2/3 research.

---

## 8. Computational Considerations

### 8.1 Storage Requirements

| Data Type | Per Run | 10,000 Runs |
|-----------|---------|-------------|
| Terminal state vector | ~25 KB | ~250 MB |
| Full trajectories (50 years) | ~1.5 MB | ~15 GB |
| Event log | ~5 KB | ~50 MB |
| Summary statistics | ~2 KB | ~20 MB |

**Recommendation:** Store full trajectories for a subset of runs (e.g., 1,000); store terminal state and event log for all runs.

### 8.2 Parallelization

Simulation runs are independent—embarrassingly parallel. Each run:
1. Samples factor realizations
2. Determines event occurrences
3. Applies shocks and transmission
4. Evolves dynamics
5. Records outputs

Can distribute across cores/nodes with no inter-run communication.

### 8.3 Derived Assessment Computation

Derived assessments can be computed:
- **On-demand:** When analyzing specific runs or scenarios
- **Batch:** For all runs after simulation completes
- **Incremental:** Update running statistics as runs complete

Recommendation: Compute country summary statistics and scenario flags during simulation; compute detailed assessments on-demand for selected runs.

### 8.4 Validation Outputs

For model validation, additionally output:

| Validation Output | Purpose |
|-------------------|---------|
| Event frequency by type | Compare to specified annual probabilities |
| Factor correlation realized | Compare to specified Ω matrix |
| Variable trajectory statistics | Check for degenerate behavior (explosions, negative populations) |
| Baseline trajectory (no events) | Verify dynamics behave sensibly |

---

## 9. Output File Formats

### 9.1 Per-Run Outputs

```
run_XXXXX/
├── terminal_state.parquet      # Full state vector at end year
├── event_log.json              # All events that fired
├── trajectories.parquet        # Time series (if stored)
├── summary_statistics.json     # Country summaries, scenario flags
└── assessments.json            # Derived assessments (if computed)
```

### 9.2 Cross-Run Outputs

```
analysis/
├── distributions.parquet       # Percentile distributions for key variables
├── scenario_counts.json        # Frequency of defined scenarios
├── conditional_distributions/  # Distributions given conditions
├── contribution_analysis.json  # Event/factor contribution to tails
└── validation_statistics.json  # Event frequencies, correlations, sanity checks
```

---

## 10. Summary

The simulation produces:

1. **Raw state data:** ~3,072 variables per run, optionally with 50-year trajectories
2. **Event logs:** Complete record of what happened in each run
3. **Derived assessments:** Human-interpretable stability, fragility, alignment, vulnerability scores computed from observables
4. **Distributional summaries:** Percentiles, scenario frequencies, conditional distributions, contribution analysis across runs

The key architectural decision is that **assessments are outputs, not state variables**. The simulation tracks observables; interpretive indices are computed afterward. This eliminates circular reasoning and enables transparent analysis of what drives outcomes.

---

*This document specifies simulation outputs. For state variable definitions see [[methodology/reference/state-variables-country]] and [[methodology/reference/state-variables-global]]. For dynamics and transmission see [[methodology/reference/state-dynamics]] and [[methodology/reference/state-transmission]].*