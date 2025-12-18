---
title: implementation-roadmap
type: note
permalink: methodology/concepts/implementation-roadmap
tags:
- methodology
- concepts
- implementation
- roadmap
- v1
- v2
---

# Implementation Roadmap

**Phased approach to building the simulation architecture.**

---

## v1.0: State-Conditioned Multipliers (Current Target)

**Scope**: Minimal changes to existing factor model architecture.

### Changes

1. **Classify all events by causal type** in the catalog

2. **For Type 2 events, add trigger conditions**:
   ```yaml
   trigger_conditions:
     - variable: [state variable]
       function: [linear | logistic | exponential]
       parameters: [function-specific]
       baseline_multiplier: 1.0  # at reference level
   ```

3. **Modify sampling loop**:
   ```python
   for event in events:
       if event.type == 2:
           multiplier = compute_state_multiplier(event, state)
           p = event.base_probability * multiplier * factor_adjustment
       else:
           p = event.base_probability * factor_adjustment
       # ... sample as before
   ```

4. **For Type 3 events, implement two-stage sampling**:
   ```python
   if event.type == 3:
       if preconditions_met(event, state):
           if random() < event.window_probability:
               resolution = sample_multinomial(event.resolution_probabilities)
               apply_resolution_impacts(event, resolution, state)
   ```

5. **Move clear Type 4 events to baseline** (solar, batteries, general AI trend)

6. **Document cascade pathways** without implementing dynamic state feedback within year

7. **Implement aftermath branches (single-branch MVP)**:
   - Every event with significant persistent effects gets a single-branch aftermath
   - Structure supports future multi-branch refinement
   - Simulation tracks active aftermaths and applies factor modifications
   - See [[methodology/reference/aftermath-branches]] for full specification

### Limitations Accepted

- State updates still annual (no within-year cascades)
- Factor shocks go to event probability, not to pressure variables
- Type 4 baseline uncertainty simplified

---

## v2.0: Full Hybrid Factor-State Model (Future)

**Scope**: Fundamental restructuring of factor interpretation and state coupling.

### Changes

1. **Redefine factors as pressure drivers**:
   - Each factor maps to one or more state variables
   - Factor realization = shock to those state variables
   - Event probability derived from state, not directly from factors

2. **Implement pressure accumulation**:
   - Track pressure variables explicitly
   - Baseline pressure trends (some things worsen over time)
   - Factor shocks add volatility around trend
   - Threshold surfaces defined in state space

3. **Sub-annual resolution for fast cascades**:
   - Monthly or quarterly time steps for financial/conflict dynamics
   - Annual aggregation for slow-moving variables (demographics, climate)

4. **Full cascade implementation**:
   - Events update state immediately
   - Updated state conditions subsequent event probabilities within same time step
   - Cascade chains can propagate (A → state change → B → state change → C)

5. **Validation infrastructure**:
   - Historical backtesting against known events
   - Sensitivity analysis for threshold estimates
   - Cross-validation of pressure functions

---

## Migration Path

| Component | v1.0 State | v2.0 Target | Migration Effort |
|-----------|------------|-------------|------------------|
| Event catalog | Add type, trigger conditions | Pressure mappings | Moderate |
| Factor model | Unchanged interpretation | Pressure driver interpretation | Significant |
| Probability | Static + multipliers | Fully state-conditioned | Moderate |
| Type 3 | Two-stage sampling | Same, refined | Low |
| Type 4 | Removed to baseline | Same | Done in v1.0 |
| Cascades | Documented only | Implemented | Significant |
| Aftermath branches | Single-branch MVP | Multi-branch where warranted | Low-Moderate |
| Time step | Annual | Sub-annual option | Moderate |

---

## Required Event Template Changes

**Add to template:**

```yaml
# Causal classification
causal_type: 1 | 2 | 3  # No Type 4 in event catalog
causal_type_rationale: "Brief explanation"

# For Type 2
pressure_specification:
  variables: [list of state variables]
  weights: [relative importance]
  threshold: [estimate with uncertainty]
  probability_function: [functional form]

# For Type 3  
window_specification:
  preconditions: [state conditions]
  window_probability: [annual, given preconditions]
  resolutions: [list with probabilities and separate impact vectors]

# Structured impact vector
impact_vector:
  global: [...]
  by_entity: [...]
  conditional: [...]
  cascades: [...]

# Durability specification
durability:
  type: permanent | decaying | maintenance_required | shock_vulnerable | regime_dependent
  parameters: [type-specific]

# Aftermath branches (for events with persistent trajectory effects)
aftermath_branches:
  - id: [branch identifier]
    probability: [0-1, must sum to 1 across branches]
    factor_modifications: {factor: magnitude}
    duration: {type, parameters}
```

**Remove:**
- Any implicit valence classification
- Simple scalar "impact" fields

---

## Events to Reclassify or Remove

| Event | Action |
|-------|--------|
| Solar breakthrough | **Remove**: baseline trajectory |
| Battery breakthrough | **Remove**: baseline trajectory |
| AI productivity gains | **Reclassify**: Type 2 if specific threshold, else baseline |
| Accelerated decarbonization | **Reclassify**: Type 3 (requires coordination) |
| Energy storage breakthrough | **Type 2** if specific cost threshold, else baseline |
| AMOC collapse | **Confirm Type 2** with pressure specification |
| Pakistan failure | **Confirm Type 2** with pressure specification |
| Taiwan conflict | **Confirm Type 3** with window/resolution structure |
| Climate agreement | **Add as Type 3** |

---

## Specification Requirements

Every event in the catalog must have:

1. **Causal type** with rationale
2. **Type-appropriate probability specification**:
   - Type 1: Base rate + adjustment factors
   - Type 2: Pressure variables + threshold + conditioning function
   - Type 3: Preconditions + window probability + resolution distribution
3. **Structured impact vector** with:
   - Multi-dimensional impacts
   - Actor-specific differentiation
   - Time profile (immediate, delayed, duration)
   - Durability specification
4. **Aftermath branches** (at minimum single-branch for events with persistent effects)
5. **Cascade documentation** (what state changes condition what other events)
6. **Uncertainty characterization** (where confidence is low, say so)

---

## Further Reading

- [[methodology/concepts/state-event-coupling]] — The coupling architecture
- [[methodology/reference/causal-types]] — Type definitions
- [[methodology/project/development-roadmap]] — Overall project plan