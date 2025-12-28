---
title: State Dynamics
type: note
permalink: methodology/reference/state-dynamics
tags:
- methodology
- reference
- state
- dynamics
- modeling
- time-evolution
---

# State Dynamics

## How Variables Evolve Between Events

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

**Related documents:**
- [[methodology/reference/state-overview]] — Entry point for state model
- [[methodology/reference/state-variables-country]] — Country-level variable catalog
- [[methodology/reference/state-variables-global]] — Global variable catalog
- [[methodology/reference/state-transmission]] — How variables affect each other

---

## 1. Purpose & Scope

This document specifies how state variables evolve over time in the absence of discontinuity events. The simulation operates in annual time steps; between event shocks, variables follow baseline dynamics determined by their type.

Understanding dynamics types is essential for:
- **Initialization:** Some variables require trend parameters, others equilibrium levels
- **Event impact modeling:** Shock persistence depends on underlying dynamics
- **Validation:** Expected trajectories provide sanity checks on simulation output

### Dynamics vs. Transmission

**Dynamics** describes how a variable evolves on its own trajectory (e.g., population aging, mean-reverting commodity prices).

**Transmission** describes how variables affect each other (e.g., oil prices → inflation). See [[methodology/reference/state-transmission]].

Events shock variables; dynamics and transmission determine how shocks propagate and dissipate.

---

## 2. Dynamics Taxonomy

Variables are classified into six dynamics types based on how they evolve over time.

| Type | Key Characteristic | Modeling Approach |
|------|-------------------|-------------------|
| **Slow Drift** | Deterministic trend with small noise | Trend function + Gaussian noise |
| **Mean-Reverting** | Fluctuates around equilibrium | Ornstein-Uhlenbeck or similar |
| **Regime-Dependent** | Behavior differs across regimes | Markov switching or threshold models |
| **Policy-Driven** | Determined by deliberate decisions | Reaction functions + discretionary shocks |
| **Event-Driven** | Dominated by discrete discontinuities | Baseline stability + event shocks |
| **Derived** | Computed from other variables | Deterministic functions |

---

## 3. Slow Drift Variables

### Characteristics

- Deterministic trend dominates stochastic noise
- Changes gradually over years or decades
- Direction largely predictable; magnitude less so
- Shocks cause temporary deviations from trend

### Modeling Approach

```
X(t+1) = X(t) + trend(t) + ε
where:
  trend(t) = baseline annual change (may accelerate/decelerate)
  ε ~ N(0, σ²) with σ small relative to trend
```

### Examples

| Variable | Category | Typical Dynamics |
|----------|----------|------------------|
| `global_temp_anomaly` | Global-Climate | +0.03°C/yr ± 0.01 |
| `sea_level_global` | Global-Climate | +0.4 cm/yr, accelerating |
| `global_co2_ppm` | Global-Climate | +2.5 ppm/yr |
| `antibiotic_resistance` | Global-Health | +1%/yr index increase |
| `battery_cost_kwh` | Global-Tech | -8%/yr learning curve |
| `renewable_cost_index` | Global-Tech | -6%/yr learning curve |
| Population cohort aging | Country-Demo | Deterministic cohort flow |
| `usd_reserve_share` | Global-Financial | -0.5%/yr baseline decline |

### Implementation Notes

**Trend specification:** Each slow-drift variable requires:
- Baseline trend (constant or time-varying function)
- Noise standard deviation
- Bounds (if applicable, e.g., reserve shares ∈ [0, 100])

**Shock interaction:** Events can temporarily accelerate or reverse trends. After shock dissipates, variable returns to trend trajectory (not necessarily to pre-shock level).

---

## 4. Mean-Reverting Variables

### Characteristics

- Fluctuates around an equilibrium level
- Shocks dissipate over time (half-life parameter)
- Has a "normal" range it tends to return to
- Equilibrium may shift due to structural changes

### Modeling Approach

Ornstein-Uhlenbeck process:
```
dX = θ(μ - X)dt + σdW
where:
  μ = equilibrium level
  θ = reversion speed (higher = faster return to equilibrium)
  σ = volatility
  
Discrete approximation:
X(t+1) = X(t) + θ(μ - X(t)) + ε
where ε ~ N(0, σ²)
```

Half-life relationship: `half_life = ln(2) / θ`

### Examples

| Variable | Category | Equilibrium | Half-life |
|----------|----------|-------------|-----------|
| `oil_brent` | Global-Commodity | $70-80/barrel | ~2 years |
| `global_credit_spread` | Global-Financial | 100-150 bps | ~1 year |
| `container_freight_index` | Global-Trade | 100 | ~6 months |
| `unemployment_rate` | Country-Economic | Country NAIRU | ~3 years |
| `inflation_rate` | Country-Economic | Central bank target | ~2 years |
| `gdp_growth` | Country-Economic | Country potential growth | ~2 years |

### Implementation Notes

**Equilibrium estimation:** For commodity prices, use long-run production cost estimates. For country economic variables, use structural estimates (NAIRU, potential growth).

**Regime shifts:** Equilibrium levels can shift due to structural changes. A technology breakthrough might permanently lower `renewable_cost_index` equilibrium. Model as equilibrium parameter update, not just shock.

**Asymmetric reversion:** Some variables may revert faster from one direction than the other (e.g., credit spreads widen fast, narrow slowly). Can model with direction-dependent θ.

---

## 5. Regime-Dependent Variables

### Characteristics

- Behavior differs qualitatively across regimes
- May have tipping points or thresholds
- Stable within regime; discontinuous transitions across regimes
- Regime identification often requires judgment

### Modeling Approach

Markov regime-switching or threshold models:
```
Regime 1: X follows dynamics D1
Regime 2: X follows dynamics D2
Transition: P(regime switch) = f(state variables, thresholds)
```

### Examples

| Variable | Regimes | Transition Logic |
|----------|---------|------------------|
| `amoc_strength` | Stable / Weakening / Collapsed | Threshold at ~50% triggers collapse risk |
| `amazon_forest_cover` | Forest / Transition / Savanna | Deforestation + temperature thresholds |
| `pandemic_status` | None (0) / Active (1-4) | Event-triggered onset; duration-based recovery |
| `regime_type` | Democracy / Hybrid / Authoritarian | Event-triggered transitions |
| Currency regimes | Stable / Crisis / Hyperinflation | Threshold-based on inflation, reserves |

### Implementation Notes

**Tipping points:** For climate variables (`amoc_strength`, `amazon_forest_cover`, `permafrost_integrity`), model as:
- Above threshold: slow drift dynamics
- Below threshold: accelerating decline or rapid transition to new stable state

**Hysteresis:** Some regime transitions are irreversible or difficult to reverse. AMOC collapse, once triggered, may not recover on policy-relevant timescales. Model with asymmetric transition probabilities.

**Regime identification:** At each time step, classify regime based on observable criteria before applying regime-specific dynamics.

---

## 6. Policy-Driven Variables

### Characteristics

- Primarily determined by deliberate policy choices
- Responds to other state variables through decision-making
- Not mechanical relationships; involves judgment and discretion
- Policy reaction functions provide baseline; discretionary shocks capture deviations

### Modeling Approach

```
X(t+1) = reaction_function(state(t)) + discretionary_shock
where:
  reaction_function captures systematic policy response
  discretionary_shock ~ distribution capturing policy uncertainty
```

### Examples

| Variable | Primary Decision-Maker | Reaction Function Basis |
|----------|----------------------|------------------------|
| `fed_funds_rate` | Federal Reserve | Taylor rule (inflation, output gap) |
| `ecb_rate` | European Central Bank | Modified Taylor rule |
| `pboc_rate` | People's Bank of China | Growth + financial stability |
| `military_spending` | National governments | Threat environment, fiscal capacity |

### Implementation Notes

**Taylor rule example:**
```
fed_funds_rate = r* + π* + 1.5(π - π*) + 0.5(y - y*)
where:
  r* = neutral real rate (~2%)
  π* = inflation target (2%)
  π = current inflation
  y - y* = output gap
```

**Discretionary component:** Policy doesn't follow rules mechanically. Add noise term to capture:
- Political constraints
- Judgment calls
- Communication/credibility considerations

---

## 7. Event-Driven Variables

### Characteristics

- Dominated by discrete discontinuities rather than continuous evolution
- Long periods of stability punctuated by sudden shifts
- Baseline dynamics minimal; events are the primary driver
- Often categorical or count variables

### Modeling Approach

```
X(t+1) = X(t) + baseline_drift + Σ(event_shocks)
where:
  baseline_drift is small or zero
  event_shocks dominate when events fire
```

### Examples

| Variable | Category | Baseline | Event Examples |
|----------|----------|----------|----------------|
| `active_major_conflicts` | Global-Conflict | Stable | War onset (+1), peace agreement (-1) |
| `nuclear_status` | Country-Strategic | Stable | Proliferation event (categorical shift) |
| `alliance_status` | Country-Strategic | Stable | Alliance formation/dissolution |
| `internal_conflict_intensity` | Country-Political | Low drift | Conflict escalation, resolution |
| `semiconductor_supply` | Global-Trade | 100 (stable) | Taiwan conflict, fab disaster |
| `years_since_irregular_transition` | Country-Political | +1/year | Resets to 0 on transition event |
| `sanctions_level` | Country-Strategic | Stable | Sanctions imposition/removal events |

### Implementation Notes

**Count variables:** `active_major_conflicts`, `coup_attempts_10yr` increment/decrement discretely. No continuous dynamics.

**Categorical variables:** `regime_type`, `nuclear_status`, `alliance_status` change only via discrete events, not gradual drift.

**Stability counters:** Variables like `years_since_irregular_transition` increment deterministically each year, reset to zero when relevant event fires.

**Sanctions:** `sanctions_level` changes via discrete policy decisions (imposition, escalation, removal), not continuous adjustment. Policy reaction functions may condition the probability of sanctions events, but the variable itself is event-driven.

---

## 8. Derived Variables

### Characteristics

- Computed from other state variables rather than evolving independently
- Updated each time step based on current state
- No stochastic component in derivation (though inputs may be stochastic)
- Provide convenient summaries for analysis

### Modeling Approach

```
X(t) = f(state(t))
where f is a deterministic function of current state variables
```

### Examples

| Variable | Derived From | Formula |
|----------|--------------|---------|
| `pop_total` | Population cohorts | Sum of all cohort variables |
| `dependency_ratio` | Population cohorts | (0-14 + 65+) / (15-64) |
| `youth_bulge_index` | Population cohorts | (15-34) / (15+) |
| `median_age` | Population cohorts | Estimated from cohort distribution |
| `military_age_males` | Population cohorts | `pop_15_34_m` |

### Implementation Notes

**Computation timing:** Derived variables are recomputed after all dynamics and event shocks have been applied for the time step.

**No direct shocks:** Events don't shock derived variables directly; they shock the underlying components, and derived variables update automatically.

**Distinction from output assessments:** Derived *state variables* (like `pop_total`) are stored in the state vector and may be referenced by event probability functions. *Output assessments* (like stability assessment, fragility assessment, alignment profile) are computed at analysis time for human interpretation but are NOT state variables and do NOT condition event probabilities. See [[methodology/reference/state-outputs]] for output assessment specifications.

---

## 9. Variable Classification Reference

The following tables provide representative examples of how variables map to dynamics types. They are not exhaustive; see [[methodology/reference/state-variables-country]] and [[methodology/reference/state-variables-global]] for complete variable catalogs.

### Country-Level Variables by Dynamics Type

| Dynamics Type | Representative Variables |
|---------------|-----------|
| **Slow Drift** | Population cohorts (aging), `life_expectancy` trend, `gdp_share_agriculture/industry/services` |
| **Mean-Reverting** | `gdp_growth`, `inflation_rate`, `unemployment_rate`, `fdi_net`, `tfr` (country-specific equilibrium) |
| **Regime-Dependent** | `regime_type` |
| **Policy-Driven** | `military_spending` |
| **Event-Driven** | `internal_conflict_intensity`, `external_conflict_involvement`, `nuclear_status`, `alliance_status`, `sanctions_level`, `years_since_irregular_transition`, `coup_attempts_10yr` |
| **Derived** | `pop_total`, `dependency_ratio`, `youth_bulge_index` |

**Notes on demographic flows:** Variables like `tfr`, `net_migration_rate`, and `life_expectancy` exhibit slow drift trends but can experience event shocks (pandemic mortality, conflict displacement, economic crises). Model as slow drift baseline with event-driven shocks.

### Global Variables by Dynamics Type

| Dynamics Type | Representative Variables |
|---------------|-----------|
| **Slow Drift** | `global_temp_anomaly`, `sea_level_global`, `global_co2_ppm`, `antibiotic_resistance`, `battery_cost_kwh`, `renewable_cost_index`, reserve shares (`usd_reserve_share`, etc.) |
| **Mean-Reverting** | Commodity prices (`oil_brent`, `wheat_price`, etc.), `global_credit_spread` |
| **Regime-Dependent** | `amoc_strength`, `amazon_forest_cover`, `permafrost_integrity`, `pandemic_status` |
| **Policy-Driven** | `fed_funds_rate`, `ecb_rate`, `pboc_rate` |
| **Event-Driven** | `active_major_conflicts`, `semiconductor_supply`, `pandemic_severity` |
| **Derived** | None at global level (assessments computed at analysis time) |

---

## 10. Implementation Considerations

### Parameter Requirements by Dynamics Type

| Type | Required Parameters |
|------|---------------------|
| Slow Drift | trend (constant or function), noise σ, bounds |
| Mean-Reverting | equilibrium μ, reversion speed θ, volatility σ |
| Regime-Dependent | regime definitions, transition thresholds/probabilities, per-regime dynamics |
| Policy-Driven | reaction function coefficients, discretionary shock distribution |
| Event-Driven | baseline drift (usually 0), event catalog reference |
| Derived | formula specification |

### Parameterization Sources

| Source | Applicable To |
|--------|---------------|
| Historical time series | Mean-reverting equilibria, volatilities, reversion speeds |
| Climate models | Climate variable trends, tipping thresholds |
| Economic theory | Policy reaction functions, structural relationships |
| Expert judgment | Regime transition thresholds, policy discretion ranges |

### Open Parameterization Questions

The following require further specification before implementation:

1. **Country-specific equilibria:** What are equilibrium growth rates, inflation targets, unemployment rates for each of 40 countries?

2. **Reversion speeds:** How quickly do economic variables return to equilibrium after shocks? Historical estimation needed.

3. **Tipping thresholds:** At what levels do `amoc_strength`, `amazon_forest_cover` transition to collapse dynamics?

4. **Policy reaction functions:** What coefficients best describe major central bank behavior?

These will be addressed in the initialization methodology document (future work).

---

*This document specifies how variables evolve between events. For transmission mechanisms (how variables affect each other) see [[methodology/reference/state-transmission]]. For output specifications see [[methodology/reference/state-outputs]].*