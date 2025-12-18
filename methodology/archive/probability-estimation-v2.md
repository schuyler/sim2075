---
title: probability-estimation-v2
type: note
permalink: methodology/probability-estimation-v2
tags:
- methodology
- probability
- estimation
- calibration
- causal-types
---

# Probability Estimation v2

**Updated per [[methodology/integrated-event-state-framework]]**

## Overview

Probability estimation differs by causal type. This document covers:
1. Type-specific estimation approaches
2. General methods (historical base rate, expert synthesis, structural reasoning)
3. Comparative ranking for cross-validation
4. Calibration heuristics

---

## Type-Specific Estimation

### Type 1 (Stochastic) Events

**Core approach**: Historical base rate

Type 1 events have reasonably stable base rates with limited predictability. The probability comes from counting occurrences in appropriate reference classes.

**Steps**:

1. **Define reference class** (this is the hard part)
   - What counts as "this type of event"?
   - What countries/regions are "at risk"?
   - What time period is relevant?

2. **Calculate base rate**
   ```
   Base rate = (Number of events) / (Country-years at risk)
   ```

3. **Adjust for current conditions** (conservatively)
   - What factors make current conditions different from reference period?
   - Adjustments >2-3x require strong justification

4. **Note factor contributions to clustering**
   - Type 1 events cluster when factors are elevated
   - The base rate is the unconditional probability; factor model creates clustering

**Example**: Severe Pandemic
- Reference class: Pandemics causing >0.1% global mortality
- Historical frequency: ~3-4 per century (1918, 1957, 1968, 2020+)
- Base rate: ~3%/year
- Current conditions: Higher population density, more travel, but better surveillance
- Estimate: ~2%/year (range 1-4%)

---

### Type 2 (Threshold) Events

**Core approach**: State-conditioned probability via pressure function

Type 2 events have probability that increases as measurable pressure accumulates. Estimation requires:

1. **Specify the pressure function** (see [[methodology/integrated-event-state-framework]] Section 4.2)
   - Which state variables contribute to pressure?
   - What weights on each variable?
   - What transforms (linear, exponential, threshold)?

2. **Estimate current pressure**
   - What are current values of pressure variables?
   - Calculate current pressure score (0-100)

3. **Estimate the threshold**
   - At what pressure level does probability become significant?
   - This is the key calibration point
   - Use historical analogs: what pressure levels preceded similar events?

4. **Choose sharpness parameter (k)**
   - k = 0.1: Gradual increase around threshold
   - k = 0.3: Sharp transition at threshold
   - Most events: k = 0.15-0.25

5. **Calculate probability from pressure**
   ```
   P(event | year) = min_prob + (max_prob - min_prob) × logistic(k × (pressure - threshold))
   ```
   
   Where logistic(x) = 1 / (1 + exp(-x))

6. **Specify minimum probability**
   - Even at low pressure, non-zero probability exists
   - Typically 0.1-0.5%/year

**Example**: Pakistan State Failure

Current pressure estimate:
- `regime_stability`: 45/100 → contributes 0.35 × (100-45)/100 = 0.19
- `water_stress`: 70/100 → contributes 0.25 × 70/100 = 0.175
- `debt_external`: 75% GDP → contributes 0.15 × threshold_fn(75) ≈ 0.10
- `conflict_intensity`: 2/4 → contributes 0.15 × exp_fn(2) ≈ 0.08
- `food_import`: 35% → contributes 0.10 × 35/100 = 0.035

**Current pressure ≈ 55/100**

Threshold estimate: 70 ± 10 (calibrated from Syria ~2011, Yugoslavia ~1991)

With k=0.20, current probability ≈ 1.5%/year

---

### Type 3 (Contingent) Events

**Core approach**: Two-stage estimation

Type 3 events require estimating:
1. P(window opens | state conditions)
2. P(resolution = X | window open)

**Steps**:

1. **Specify window preconditions**
   - What state variable thresholds must be met?
   - AND or OR logic?

2. **Estimate P(conditions met) for each year**
   - Given current state trajectories, how likely are conditions to be met?
   - This is often Type 2-like: pressure accumulates toward threshold

3. **Estimate resolution probabilities**
   - Given window is open, what's the probability of each resolution?
   - Use historical analogs for similar decisions
   - Consider actor incentives and constraints

4. **Calculate combined probability**
   ```
   P(resolution X in year t) = P(window | t) × P(resolution X | window)
   ```

**Example**: Taiwan Conflict

Window conditions:
- `us_china_tension` > 70 AND
- China faces significant domestic pressure (economic/political crisis) OR
- Taiwan makes status change that triggers

P(window in any year): ~5-8% (rising over time as tension accumulates)

Resolutions given window:
- Military conflict: 30%
- Negotiated accommodation: 25%
- Status quo preserved (window closes without resolution): 45%

P(military conflict in year t) = 0.06 × 0.30 = ~1.8%/year
P(accommodation in year t) = 0.06 × 0.25 = ~1.5%/year

---

## General Estimation Methods

Use regardless of causal type, then integrate with type-specific approach.

### Historical Base Rate Method

**When to use**: Event type has occurred in comparable contexts.

**Step 1: Define reference class**
- Geographic scope: All countries? Similar countries?
- Time period: All history? Post-WWII?
- Event definition: What threshold qualifies?

Different reference classes give different answers. Report the range.

**Step 2: Calculate and adjust**
```
Base rate = (Number of events) / (Country-years at risk)
```

**Step 3: State uncertainty honestly**

Small samples mean wide confidence intervals.

### Expert Synthesis Method

**When to use**: Published estimates exist from domain experts.

Gather estimates. Assess quality. Synthesize range.

**When experts disagree**: This reveals genuine uncertainty. Report the range.

### Structural Reasoning Method

**When to use**: Unprecedented events where mechanisms can be analyzed.

Decompose into components. Reason about each. Combine.

**Carries wide uncertainty by nature.**

---

## Comparative Ranking

**Purpose**: Cross-validate absolute estimates.

Comparative judgments are often more reliable than absolute estimates.

### Process

1. **List events to compare** (group by type or region)

2. **Make pairwise judgments**

| Comparison | Judgment | Reasoning |
|------------|----------|-----------|
| Pakistan vs. Egypt | Pakistan > Egypt | Higher current pressure |
| AMOC vs. Amazon | AMOC ≈ Amazon | Both ~1%, similar threshold dynamics |

3. **Construct ranking** from most to least likely

4. **Check coherence** — If ranking contradicts absolute estimates, revise

### Type-Specific Ranking Considerations

**Type 1**: Compare base rates directly

**Type 2**: Compare current pressure levels and distance from threshold

**Type 3**: Compare P(window) and P(severe resolution | window) separately

---

## Calibration Heuristics

Rough anchors for sanity checking.

| Annual Probability | Meaning | Example |
|-------------------|---------|---------|
| ~0.5% | Very rare, once in 200 years | AMOC collapse, major nuclear use |
| ~1% | Rare, once per century | Major climate tipping point |
| ~2% | Uncommon, several per century | Severe pandemic |
| ~3% | Occasional, once per generation | Major financial crisis |
| ~5% | Regular occurrence | Regional conflict, minor crisis |
| ~10%+ | Not unusual | Consider: is this really a "discontinuity"? |

---

## Time-Varying Probability

### For Type 2 Events

Probability naturally increases as pressure accumulates over time. Document:
- Current pressure level
- Expected pressure trajectory
- When threshold might be approached

### For Type 3 Events

Window probability may increase over time. Document:
- What drives window probability change?
- Expected trajectory of precondition variables

### For All Events

Provide horizon-average if probability varies significantly:

"Probability is ~0.8%/year early in horizon, rising to ~2.5%/year by 2060 as climate pressure accumulates. We use ~1.5% as horizon average."

---

## Reconciling Methods

When methods conflict:

1. **Understand the disagreement** — Why do they diverge?

2. **Assess applicability** — For this event/type, which method is most appropriate?

3. **Weight and combine** — Use range spanning methods

4. **Flag high disagreement** — If methods diverge >3x, mark confidence "Low"

### When to Defer to Each

| Method | Defer to when... |
|--------|------------------|
| Historical base rate | Type 1 events with good reference class |
| Pressure function | Type 2 events with clear state variable linkage |
| Window-resolution | Type 3 events with identifiable decision points |
| Expert synthesis | Experts have specific knowledge and largely agree |
| Structural reasoning | Unprecedented event, mechanisms understood |

---

## Documentation Requirements

| Field | Description |
|-------|-------------|
| **Causal type** | Type 1/2/3 determines primary estimation approach |
| **Point estimate** | Best single value (annual probability) |
| **Range** | Plausible range (not false precision) |
| **Confidence** | Low / Medium / High |
| **Type-specific details** | Base rate (Type 1), pressure function + threshold (Type 2), window + resolutions (Type 3) |
| **Method(s)** | Which estimation methods were used? |
| **Derivation** | Step-by-step reasoning |
| **Comparative ranking** | How does this compare to related events? |
| **Key uncertainties** | What could make this much higher/lower? |
| **Trend** | Does probability increase/decrease over horizon? |
