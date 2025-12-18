---
title: factor-loadings
type: note
permalink: methodology/factor-loadings
tags:
- methodology
- factors
- loadings
- correlation
- causal-types
- v2
---

# Factor Loadings

## What Factor Loadings Represent

Factor loadings quantify **how strongly an event correlates with latent risk factors**. They are not causal claims—they capture "when this factor is elevated, this event is more likely" without specifying direction of causation.

**Loadings are structured judgment, not empirical estimates.** We have no data on how events correlate with abstract factors. The loadings exist to:
- Ensure events that should cluster together do cluster in simulation
- Force explicit thinking about what drives each event
- Make correlation assumptions transparent and revisable

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

**Interpretation**: Loadings identify which factors stress the pressure variables that drive the event toward its threshold.

**How loadings work (v1.0)**:
- Loadings modulate probability like Type 1
- State conditioning adds a multiplier on top

**How loadings work (v2.0 target)**:
- Factor realizations shock pressure variables
- Pressure accumulation drives state toward threshold
- Event probability derived from state, not directly from factors
- Chain: Factor → Pressure Variable → State → Probability

**Example**: Pakistan state failure
- Loads on F_SAS (0.85): Regional stress directly pressures regime stability
- Loads on F_CLIM (0.4): Climate stress pressures water availability
- Loads on F_FIN (0.3): Financial stress pressures fiscal capacity
- Each loading indicates "this factor shocks a pressure variable relevant to the threshold"

**Key difference from Type 1**: For Type 2, think "what factors accelerate pressure accumulation?" not "what factors make the event more likely in isolation?"

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

## Revised Interpretation: Factors as Pressure Drivers (v2.0)

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

**v2.0**: Ask "which pressure variables does this factor shock, and how much does that matter for this event's threshold?"

For now (v1.0), specify loadings using the direct probability interpretation. Document the pressure pathway in notes for v2.0 migration:

```yaml
factor_loadings:
  F_CLIM: 0.85
  
loading_notes:
  v2_pressure_pathway: |
    F_CLIM shocks global_temp_anomaly and regional climate variables.
    For AMOC: temperature affects freshwater input rate, which drives
    amoc_strength toward collapse threshold.
```

---

## Loading Estimation Process

### Step 1: Identify Causal Type

Before assigning loadings, confirm the event's causal type. This determines how to interpret the loadings.

### Step 2: Identify the Primary Factor

Ask: "If I could only load this event on one factor, which would it be?"

- For Type 1: What shared vulnerability matters most?
- For Type 2: What factor most directly stresses the pressure variables?
- For Type 3: What factor most strongly creates crisis windows?

This forces clarity about what fundamentally drives the event.

### Step 3: Identify Secondary Linkages

For each factor, ask:
- Is there a plausible mechanism linking this factor to the event?
- Is the linkage direct or indirect?
- Would the event be noticeably more likely when this factor is elevated?

For Type 2, also ask:
- Does this factor shock any of the event's pressure variables?
- How strong is the transmission from factor to pressure?

Assign secondary loadings only where genuine linkage exists. **Zero is a valid loading.**

### Step 4: Check the Constraint

Sum of squared loadings must be ≤ 1.0 for mathematical validity.

```
Σ(loading²) ≤ 1.0
```

If over 1.0, you've overestimated some loadings.

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
F_CLIM: 0.80 - 0.90 (primary pressure driver)
F_FOOD: 0.2 - 0.4 (if agricultural feedback)
Regional: 0.1 - 0.3 (regional exposure variation)
```

Rationale: Climate stress is the dominant pressure; loadings reflect which factors accelerate approach to threshold.

**State Failure Events**
```
Regional factor: 0.70 - 0.85 (dominant pressure)
F_CLIM or F_FOOD: 0.3 - 0.5 (for climate-stressed states)
F_FIN: 0.2 - 0.4 (fiscal pressure)
F_GPT: 0.1 - 0.3 (if great power involvement)
```

Rationale: Regional instability is primary; climate/food/financial stress are secondary pressure channels.

**Economic Threshold Events** (hyperinflation, currency crisis)
```
F_FIN: 0.75 - 0.85 (primary pressure)
Regional factor: 0.3 - 0.5 (regional contagion)
F_GPT: 0.1 - 0.3 (if sanctions/geopolitical exposure)
```

### Type 3 Patterns

**Deliberate Conflict Events** (Taiwan, Korea, India-Pakistan)
```
F_GPT: 0.60 - 0.80 (window driver)
Regional factor: 0.50 - 0.70 (local dynamics)
F_FIN: 0.2 - 0.4 (economic interdependence affects resolution)
```

Rationale: Great power tension and regional dynamics create windows; resolution depends on additional factors.

**International Agreement Events** (climate, arms control)
```
F_GPT: 0.4 - 0.6 (tension reduces window probability)
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
| **Pressure pathway** | Which pressure variables each factor shocks |
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
1. Factor realizations shock pressure variables (not probability directly)
2. State evolves based on pressure shocks + baseline dynamics
3. Event probability computed from state position relative to threshold
4. Factor correlation still produces event clustering (via correlated pressure shocks)

Type 1 and Type 3 continue using loadings for direct probability correlation.

---

## Migration Checklist

When upgrading an event specification from v1 to v2:

- [ ] Confirm causal type classification
- [ ] For Type 2: Document which pressure variables each loaded factor shocks
- [ ] For Type 2: Estimate factor → pressure transmission strength
- [ ] For Type 3: Note if window vs resolution loadings should differ
- [ ] Verify loading patterns are consistent with similar events
- [ ] Update loading rationale to reflect type-specific interpretation
