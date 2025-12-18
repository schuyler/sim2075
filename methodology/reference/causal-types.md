---
title: causal-types
type: note
permalink: methodology/reference/causal-types
tags:
- methodology
- reference
- causal-types
- type-1
- type-2
- type-3
- type-4
---

# Causal Types Reference

Events are classified by their generative mechanism. **Causal type determines the appropriate modeling approach.**

---

## Type 1: Stochastic Arrivals

**Definition**: Events with relatively stable base rates that occur without clear proximate cause. Timing is unpredictable, but the rate is estimable from history.

**Characteristics**:
- Approximately Poisson-distributed
- Limited leading indicators
- Base rate is primary probability input
- Correlation with other events through shared vulnerability, not shared pressure

**Examples**:
- Novel pandemic emergence (~3 per century historically)
- Major earthquakes on known faults
- Certain financial crises (idiosyncratic triggers)
- Scientific breakthroughs (specific fields)

**Modeling Approach**:
- Annual probability from historical base rate, adjusted for known condition changes
- Factor correlation captures shared vulnerability (e.g., pandemic + financial crisis both hit fragile states harder)
- No state-conditioning required (probability doesn't accumulate)

**Probability Estimation**: Historical frequency → adjustment for current conditions → annual probability with confidence interval

---

## Type 2: Threshold/Accumulation

**Definition**: Gradual pressure accumulates on state variables until a threshold is crossed. The system appears stable until it suddenly isn't.

**Characteristics**:
- Probability increases as pressure accumulates
- State variables track pressure (observable or latent)
- Threshold may be known, uncertain, or stochastic
- Often exhibits "critical slowing down" as threshold approaches
- Frequently irreversible once triggered

**Examples**:
- AMOC collapse (freshwater input accumulates)
- State failure (legitimacy erodes, fiscal stress accumulates)
- Hyperinflation (deficit monetization accumulates)
- Currency crisis (reserves deplete, current account worsens)
- Amazon tipping point (deforestation + temperature accumulate)

**Modeling Approach**:
- Track pressure variables as part of state
- Event probability conditioned on pressure level: P(event|state)
- Threshold can be deterministic, stochastic, or multi-dimensional surface
- Factor shocks affect pressure variables, not event probability directly

**Probability Estimation**: 
1. Identify pressure variables
2. Estimate current pressure level
3. Estimate threshold (with uncertainty)
4. Probability = f(pressure, threshold, trend)

### Type 2 Specification Format

```yaml
type_2_specification:
  pressure_variables:
    - variable: [state_variable_id]
      weight: [0.0 - 1.0]
      transform: [linear | logistic | exponential | inverse]
      current_value: [assessed value]
      trend: [increasing | stable | decreasing]
  pressure_function: [weighted_sum | max | product | custom]
  threshold:
    estimate: [0.0 - 1.0 or natural units]
    uncertainty: [distribution or range]
    basis: "[Historical thresholds, structural analysis, etc.]"
  probability_function:
    form: [logistic | exponential | step | custom]
    parameters:
      steepness: [higher = sharper transition]
      minimum_prob: [floor even at low pressure]
```

**Key Insight**: Type 2 events are where state-conditioning matters most. The same "60% chance of state failure" means very different things if pressure is low vs. high.

---

## Type 3: Contingent/Window-Resolution

**Definition**: Events heavily dependent on specific decisions, negotiations, or coordination outcomes. Preconditions create windows; resolution within windows is uncertain.

**Characteristics**:
- High sensitivity to individual decisions and small-N actors
- Two-stage structure: window opens, then resolution
- Preconditions necessary but not sufficient
- Game-theoretic dynamics (negotiation, brinksmanship)
- Path-dependent (sequence of moves matters)

**Examples**:
- Peace agreements (Good Friday, Camp David)
- Political transitions (South Africa, German reunification)
- Deliberate conflicts (invasion decisions, escalation choices)
- Major international agreements (climate, arms control)
- Post-crisis coordination (G20 2008)

**Modeling Approach**:
- Two-stage sampling:
  1. P(window opens) based on preconditions
  2. P(resolution | window open) with multiple possible outcomes
- Preconditions often involve state variables (tension level, leadership alignment)
- Resolution probabilities reflect coordination difficulty
- Different resolutions have different impact vectors

### Type 3 Specification Format

```yaml
type_3_specification:
  window:
    preconditions:
      - condition: "[State condition description]"
        variable: [state_variable_id]
        operator: [< | > | == | in_range]
        value: [threshold or range]
    precondition_logic: "[How conditions combine: AND, OR, etc.]"
    window_probability: [annual probability given preconditions met]
    window_duration: [years window stays open if not resolved]
  resolutions:
    - id: [resolution_id]
      name: "[Resolution name]"
      probability: [0.0 - 1.0, must sum to 1.0 across resolutions]
      description: "[What this resolution means]"
      # Impact vector specified separately, keyed by resolution_id
```

**Key Insight**: The same window can produce very different outcomes. "Taiwan crisis" is a window; resolution could be war, peaceful accommodation, or status quo. These aren't three separate events—they're three resolutions of one contingent situation.

---

## Type 4: S-Curve Dynamics — NOT EVENTS

**Definition**: Processes following predictable adoption curves once initiated. Slow start, rapid acceleration, eventual saturation.

**Characteristics**:
- Driven by reinforcing feedback loops (network effects, learning curves)
- Early stages look like noise; late stages look inevitable
- Once underway, trajectory is somewhat predictable
- Key uncertainty is timing of inflection, not direction

**Examples**:
- Technology adoption (internet, mobile, EVs)
- Cost declines (solar, batteries, sequencing)
- Capability growth (AI, if scaling continues)
- Infrastructure deployment (charging networks, renewables capacity)

**Critical Realization**: These are NOT discontinuities. A 90% cost decline over 15 years following a known learning curve is not a discrete event—it's a baseline trajectory with parameter uncertainty.

**What to do instead**: Model as baseline trajectory uncertainty, not events:

```yaml
# Instead of: P(solar breakthrough) = 0.03/year
# Model as:
variable: renewable_cost_index
dynamics: learning_curve
parameters:
  learning_rate:
    distribution: normal
    mean: 0.20  # 20% cost decline per doubling
    std: 0.05
  deployment_growth:
    distribution: normal
    mean: 0.15
    std: 0.08
```

**Exception**: If there's a genuine discontinuity threshold (e.g., fusion achieves net energy gain), model that specific threshold crossing as a **Type 2 event**. The subsequent deployment is trajectory uncertainty.

---

## Classification Decision Tree

```
Is there a historical base rate with no clear accumulating precursors?
├── YES → Type 1 (Stochastic)
└── NO ↓

Does probability increase as some measurable pressure accumulates?
├── YES → Type 2 (Threshold)
└── NO ↓

Does outcome depend critically on negotiation/coordination among small-N actors?
├── YES → Type 3 (Contingent)
└── NO ↓

Does it follow a predictable adoption/diffusion curve once initiated?
├── YES → Type 4 → MOVE TO BASELINE, not event catalog
└── NO → Reassess classification or consider hybrid
```

---

## Hybrid Types

Many events combine types:

**Type 2 + Type 3**: Pressure accumulates (Type 2), creating a window, but resolution depends on agency (Type 3). 
- Example: Cold War end—pressure accumulated, but peaceful resolution required Gorbachev/Reagan decisions.

**Type 1 + Type 2**: Stochastic trigger initiates threshold process.
- Example: Pandemic emergence (Type 1) triggers cascade if health systems already stressed (Type 2).

For hybrids, model the dominant mechanism and note the secondary.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| S-curve as event | Move to baseline trajectory uncertainty |
| Type 2 without pressure function | Specify which state variables accumulate pressure |
| Type 3 without multiple resolutions | Define resolution options (conflict/negotiation/status quo) |
| Type 1 when pressure clearly accumulates | Reclassify as Type 2 |
| Treating all state failures as identical | Each has different pressure variables and thresholds |

---

*See [[methodology/00-start-here]] for navigation | [[methodology/level-1-workflow]] for production process*