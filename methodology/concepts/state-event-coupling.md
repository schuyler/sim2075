---
title: state-event-coupling
type: note
permalink: methodology/concepts/state-event-coupling
tags:
- methodology
- concepts
- architecture
- state
- events
- coupling
- cascades
---

# State-Event Coupling Architecture

This document specifies how events and state variables interact in the simulation. It describes the feedback loops where events change state, and state conditions future events.

---

## The Integration Problem

The simulation has two components that must work together:

**State Model** (per state-specification):
- ~2,600 variables evolving over time
- Baseline dynamics (drift, mean-reversion, regime-dependent)
- Countries, regions, global commons

**Event Model** (per event catalog):
- Discontinuity events with probabilities
- Factor correlation for clustering
- Impact vectors as shocks to state

**Gap to Address**: Event probability must depend on state. P(Pakistan failure) should be higher when Pakistan's `regime_stability` is 30 than when it's 70.

---

## Factors as Pressure Drivers

### Current Interpretation (v1.0)

Factors directly affect event probabilities. High F_CLIM → higher P(AMOC collapse).

### Revised Interpretation (v2.0 Target)

Factors shock pressure variables, which affect state, which conditions event probability.

```
Factor Realization → Pressure Shock → State Variable Update → Event Probability
```

**Example**:

F_CLIM = +1.5σ →
- `global_temp_anomaly` shocked upward
- `amoc_strength` declines faster than baseline
- P(AMOC collapse) increases because `amoc_strength` closer to threshold

**Advantages**:
- State variables are observable/interpretable
- Probability conditioning is explicit
- Cascade effects propagate through state
- Factor correlation still produces event clustering (correlated shocks → correlated state movements → clustered threshold crossings)

---

## State-Conditioned Probability for Type 2

For Type 2 events, probability is a function of relevant state variables:

```
P(event | year t) = f(pressure_variables(t), threshold_estimate, uncertainty)
```

### Functional Forms

**Logistic (smooth threshold)**:
```
P(event) = 1 / (1 + exp(-k × (pressure - threshold)))
```
Where k controls steepness. Low k = gradual increase; high k = sharp threshold.

**Exponential (accelerating)**:
```
P(event) = p_base × exp(λ × (pressure - reference))
```
Probability grows exponentially as pressure exceeds reference level.

**Multi-dimensional threshold**:
```
pressure_composite = w1×var1 + w2×var2 + ... + wn×varn
P(event) = f(pressure_composite, threshold)
```
Multiple variables combine into composite pressure.

### Example: Pakistan State Failure

```yaml
event: PAKISTAN_STATE_FAILURE
type: 2

pressure_variables:
  - variable: pakistan.regime_stability
    weight: 0.35
    transform: inverse  # lower stability = higher pressure
  - variable: pakistan.water_stress  
    weight: 0.25
    transform: linear
  - variable: pakistan.debt_external
    weight: 0.20
    transform: logistic(center=80, steepness=0.1)
  - variable: pakistan.internal_conflict_intensity
    weight: 0.20
    transform: linear

pressure_function: weighted_sum

threshold:
  estimate: 0.70
  uncertainty: normal(std=0.10)
  
probability_function: logistic
probability_parameters:
  steepness: 8  # fairly sharp threshold

current_assessment:
  pressure_level: 0.55
  distance_to_threshold: 0.15
  baseline_annual_probability: 0.015
  state_conditioned_probability: 0.025  # elevated due to current pressure
```

---

## Window-Resolution Structure for Type 3

Type 3 events have explicit two-stage structure:

### Stage 1: Window

- Preconditions define when a window can open
- Window probability = P(window opens | preconditions met)
- Windows may have duration (open for N years if not resolved)

### Stage 2: Resolution

- Multiple possible outcomes, each with probability and impact vector
- Outcomes are mutually exclusive and exhaustive
- Resolution probabilities may depend on state at resolution time

### Example: Taiwan Crisis

```yaml
event: TAIWAN_CRISIS
type: 3

window:
  preconditions:
    - us_china_tension > 70
    - taiwan.alliance_west > 60
    - china.regime_stability < 70 OR china.gdp_growth < 2 for 3 years
  precondition_logic: (tension AND alliance) AND (stability OR growth)
  
  window_probability: 0.08  # annual, given preconditions
  window_duration: 3  # years, if not resolved
  
resolutions:
  - id: military_conflict
    probability: 0.35
    # impact_vector specified separately
    
  - id: peaceful_resolution
    probability: 0.20
    
  - id: status_quo_continuation
    probability: 0.45
```

---

## Simulation Loop Architecture

```python
def simulate_year(state, factors, events):
    # 1. Draw factor realizations (correlated)
    factor_realization = sample_correlated_factors()
    
    # 2. Apply factor shocks to pressure variables
    for pressure_var in pressure_variables:
        factor_shock = compute_factor_shock(pressure_var, factor_realization)
        baseline_change = baseline_dynamics(pressure_var, state)
        state[pressure_var] += baseline_change + factor_shock
    
    # 3. Apply other baseline dynamics to non-pressure variables
    state = apply_baseline_dynamics(state)
    
    # 4. Sample Type 1 events (factor-correlated, not state-conditioned)
    for event in type_1_events:
        p = factor_adjusted_probability(event, factor_realization)
        if random() < p:
            state = apply_impacts(event, state)
    
    # 5. Check Type 2 thresholds (state-conditioned)
    for event in type_2_events:
        p = state_conditioned_probability(event, state)
        if random() < p:
            state = apply_impacts(event, state)
    
    # 6. Sample Type 3 events (window + resolution)
    for event in type_3_events:
        if window_conditions_met(event, state):
            if random() < event.window_probability:
                resolution = sample_resolution(event)
                state = apply_impacts(event, resolution, state)
    
    return state
```

---

## Cascade Effects

When events occur, they change state variables that condition other events:

### Example: AMOC Collapse Cascades

```yaml
event: AMOC_COLLAPSE
cascades:
  - target: europe.agricultural_climate_risk
    magnitude: +40 points
    delay: 2 years
    mechanism: "Temperature drop devastates European agriculture"
    
  - target: europe.regime_stability (aggregate)
    magnitude: -15 points
    delay: 3-5 years
    mechanism: "Economic disruption + migration creates political stress"
    
  - target: sahel.water_stress
    magnitude: -10 points (improvement)
    delay: 5 years
    mechanism: "Changed Atlantic circulation may increase Sahel rainfall"
    uncertainty: high
    
  - target: global.food_stocks_grains
    magnitude: -30%
    delay: 1-2 years
    mechanism: "European production collapse tightens global supply"
```

These cascade impacts change state variables that condition other events:
- Higher `europe.agricultural_climate_risk` → higher P(European food crisis)
- Lower `europe.regime_stability` → higher P(EU fragmentation)
- Lower `global.food_stocks` → higher P(food price spike) → higher P(MENA instability)

---

## Implementation Phases

### v1.0: State-Conditioned Multipliers (Current)

Minimal changes to factor model:

1. Classify all events by causal type
2. For Type 2 events, add state-conditioned multipliers
3. For Type 3 events, implement two-stage window-resolution
4. Move Type 4 to baseline trajectory
5. Document cascade pathways (don't implement within-year cascades yet)

**Limitations accepted**:
- State updates still annual (no within-year cascades)
- Factor shocks go to probability, not pressure variables
- Type 4 baseline uncertainty simplified

### v2.0: Full Hybrid Factor-State Model (Future)

Fundamental restructuring:

1. Factors shock pressure variables (not probability directly)
2. Explicit pressure accumulation tracking
3. Sub-annual resolution for fast cascades
4. Full cascade implementation within time steps

---

## State Variable → Event Probability Mappings

### Type 2 Events

| Event | Primary Pressure Variables | Threshold | Probability Function |
|-------|---------------------------|-----------|---------------------|
| AMOC_COLLAPSE | amoc_strength, global_temp_anomaly | amoc_strength < 40% | Logistic (steep) |
| PAKISTAN_STATE_FAILURE | regime_stability, water_stress, debt | Composite > 0.70 | Logistic (moderate) |
| EGYPT_STATE_FAILURE | regime_stability, nile_water, food_stress | Composite > 0.75 | Logistic (moderate) |
| AMAZON_TIPPING | forest_cover, global_temp, deforestation | forest_cover < 60% | Logistic (steep) |
| CHINA_ECONOMIC_CRISIS | debt_public, gdp_growth, property_stress | Composite > 0.65 | Exponential |

### Type 3 Events

| Event | Window Preconditions | P(window) | Resolutions |
|-------|---------------------|-----------|-------------|
| TAIWAN_CRISIS | tension > 75, alliance > 60, trigger | 0.08/yr | Conflict 35%, Peaceful 25%, Status quo 40% |
| MAJOR_CLIMATE_AGREEMENT | temp > 1.5, recent_disaster, tension < 65 | 0.06/yr | Strong 30%, Weak 40%, None 30% |
| US_CHINA_ACCOMMODATION | tension < 60, leadership aligned | 0.05/yr | Success 25%, Partial 35%, Failure 40% |

---

*See [[methodology/reference/causal-types]] for type definitions | [[methodology/concepts/monte-carlo-framework]] for full simulation architecture*