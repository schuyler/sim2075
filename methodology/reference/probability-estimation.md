---
title: probability-estimation
type: note
permalink: methodology/probability-estimation
tags:
- methodology
- probability
- estimation
- calibration
---

# Probability Estimation

## Two Complementary Approaches

Use **both** approaches for every event, then reconcile.

### Approach A: Absolute Estimation

Estimate the annual probability directly using available methods.

**Produces:** Point estimate and range (e.g., "1.5% per year, range 0.5% - 3%")

**Weakness:** Hard to know if absolute levels are correct

### Approach B: Comparative Ranking

Rank events relative to each other without committing to absolute probabilities.

**Produces:** Ordered list and pairwise judgments (e.g., "Pakistan state failure is more likely than Egypt state failure")

**Strength:** Comparative judgments are often more reliable than absolute estimates

**Integration:** After absolute estimates (A), cross-check using ranking (B). If they contradict, revise until they cohere.

---

## Absolute Estimation Methods

Select method(s) based on event characteristics. Most events use a combination.

| Method | When to Use | What It Provides |
|--------|-------------|------------------|
| **Historical Base Rate** | Event type has occurred in comparable contexts | Empirical anchor, but past ≠ future |
| **Expert Synthesis** | Published estimates exist | Leverages domain knowledge, but experts disagree |
| **Structural Reasoning** | No precedent; must reason from mechanisms | Can address novel situations, but highly uncertain |

### Historical Base Rate Method

**Step 1: Define reference class (this is the hard part)**

What counts as "this type of event"? Be explicit about:
- Geographic scope: All countries? Similar countries?
- Time period: All history? Post-WWII? Post-Cold War?
- Event definition: What threshold qualifies?

Different reference classes give different answers. If sensitivity is large, report the range.

**Step 2: Calculate and adjust**

```
Base rate = (Number of events) / (Country-years at risk)
```

Adjust for current conditions—but be skeptical of large adjustments (>2-3x) without strong justification.

**Step 3: State uncertainty honestly**

Small samples mean wide confidence intervals. Don't report false precision.

### Expert Synthesis Method

Gather published estimates. Assess source quality. Synthesize.

**When experts disagree:**
- This often reveals genuine uncertainty, not resolvable error
- Default to reporting the range of expert opinion
- If you pick a point in that range, justify why

**Warning:** Experts may share blind spots. Published estimates cluster around conventional wisdom.

### Structural Reasoning Method

For unprecedented events. Decompose into components. Reason about mechanisms.

**This method carries wide uncertainty by nature.** Don't pretend otherwise.

---

## Comparative Ranking Method

When absolute estimation feels groundless, comparative ranking provides structure.

**Step 1:** List events to compare (group by type or region)

**Step 2:** Make pairwise judgments

| Comparison | Judgment | Reasoning |
|------------|----------|-----------|
| Pakistan vs. Egypt | Pakistan > Egypt | Higher current fragility, more severe climate exposure |
| Egypt vs. Saudi | Egypt > Saudi | Weaker fiscal buffers, more food import dependent |

**Step 3:** Construct stack ranking from most to least likely

**Step 4:** Reconcile with absolute estimates—if ranking contradicts absolute estimates, something is wrong

---

## Calibration Heuristics

Rough anchors for sanity checking. **Not derived from rigorous analysis.**

| Annual Probability | Meaning | Intuition Check |
|-------------------|---------|-----------------|
| ~0.1% | Extremely rare, globally unprecedented | Can you name more than 1-2 instances ever? |
| ~0.5% | Very rare, once in 200 years | Has this happened in living memory? |
| ~1% | Rare, once per century | Has this happened since WWII? |
| ~2-3% | Uncommon, several times per century | Multiple clear historical instances? |
| ~5% | Occasional, once per generation | Expect to see this a few times in your lifetime? |
| ~10%+ | Not unusual, once per decade | Is this really a "discontinuity"? |

**Warning:** These assume events are roughly independent over time. Climate events that become more likely over time violate this.

---

## Handling Time-Varying Probability

Some events become more or less likely over the horizon:
- Climate tipping points: Probability increases with cumulative warming
- Demographic crises: Probability increases as populations age

**For v1.0:** Estimate "average probability over horizon" and note the trend direction.

**Document:** "Probability is ~1%/year early in horizon, rising to ~3%/year by 2060. We use 2% as horizon average."

---

## Reconciling Methods When They Conflict

Different methods often give different answers.

**Step 1: Understand the disagreement** — Why do methods diverge?

**Step 2: Assess method applicability** — For this event, which method is most appropriate?

**Step 3: Weight and combine** — Use range that spans methods; weight toward most applicable

**Step 4: Flag high disagreement** — If methods diverge by >3x, mark confidence as "Low"

### When to Defer to Each Method

**Defer to historical base rate when:** Event type has occurred multiple times in similar conditions

**Defer to expert synthesis when:** Experts have specific knowledge and largely agree

**Defer to structural reasoning when:** Event is unprecedented and mechanisms are understood

**Prefer wider ranges when:** Methods significantly disagree or all have clear limitations

---

## Documentation Requirements

| Field | Description |
|-------|-------------|
| **Point estimate** | Best single value (annual probability) |
| **Range** | Plausible range (not false precision—1-3%, not 1.5-2.5%) |
| **Confidence** | How confident in this range? (Low / Medium / High) |
| **Method(s)** | Which estimation methods were used? |
| **Derivation** | Step-by-step reasoning from evidence to estimate |
| **Comparative ranking** | How does this compare to related events? |
| **Key uncertainties** | What could make this much higher or lower? |
| **Trend** | Does probability increase/decrease over horizon? |


---

## Type-Specific Probability Estimation

Different causal types require different estimation approaches. The general methods above apply to all types, but their relative importance and application differs.

### Quick Reference

| Type | Core Method | Key Challenge | Detailed Guidance |
|------|-------------|---------------|-------------------|
| **Type 1** (Stochastic) | Reference class → base rate → adjustment | Defining the reference class | This section |
| **Type 2** (Threshold) | Pressure variables → threshold → P(event) | Threshold location uncertainty | This section |
| **Type 3** (Contingent) | Window probability × resolution branches | Resolution probability intractability | [[methodology/reference/type-3-calibration]] |

---

### Type 1: Stochastic Events

**Core insight**: Historical base rate is the primary anchor. Adjustments should be modest and structurally justified.

Type 1 events occur without clear accumulating precursors—timing is unpredictable, but the rate is estimable from history. The challenge is defining the right reference class and resisting the temptation to over-adjust.

#### Reference Class Definition

This is the hard part. The reference class determines your base rate, and different definitions can give very different answers.

**Scope decisions**:

| Dimension | Options | Guidance |
|-----------|---------|----------|
| Geographic | Global vs. regional vs. country-specific | Use broadest class with comparable conditions |
| Temporal | All history vs. post-WWII vs. recent decades | Match to structural similarity, not convenience |
| Definitional | What threshold qualifies as "this event"? | Be explicit; sensitivity-test the threshold |

**Example: Novel Pandemic Emergence**

| Reference Class | Events | Entity-Years | Base Rate |
|-----------------|--------|--------------|-----------|
| All pandemics since 1900 | ~5 | 125 years | 4%/year |
| Pandemics with >1M deaths since 1900 | ~3 | 125 years | 2.4%/year |
| Novel respiratory pandemics since 1900 | ~3 | 125 years | 2.4%/year |
| Novel pandemics in era of global air travel (1970+) | ~2 | 55 years | 3.6%/year |

Different definitions give 2.4-4%/year. Report the range; pick a point estimate with justification.

**When reference classes diverge significantly** (>2x): This often reflects genuine structural ambiguity. Report the range rather than forcing a point estimate.

#### Base Rate Calculation

```
Base rate = (Number of events) / (Entity-years at risk)
```

**For global events**: Entity-years = calendar years in scope

**For country-level events**: Entity-years = country-years at risk (countries × years)

**Example: State failure in fragile states**
- Events: ~15 state failures since 1990
- Entity-years: ~40 fragile states × 35 years = 1,400 country-years
- Base rate: 15/1,400 ≈ 1.1%/year per fragile state

#### Adjustment Discipline

Adjustments from base rate should be **modest and structurally justified**.

| Adjustment | Justification Required |
|------------|----------------------|
| 0.8x - 1.25x | Minimal—reasonable default range |
| 0.5x - 2x | Specific structural change identified |
| 0.25x - 4x | Strong evidence of regime change |
| Beyond 4x | Extraordinary evidence; consider whether base rate is wrong |

**Valid adjustment reasons**:
- Structural change (new technology, demographic shift, institutional change)
- Known trend with physical basis (climate forcing increasing)
- Specific vulnerability difference from reference class average

**Invalid adjustment reasons**:
- "This time is different" without mechanism
- Recent near-miss or long quiet period (gambler's fallacy)
- Gut feeling that base rate "seems too high/low"

#### Sparse Data: When N < 10

Small samples mean wide uncertainty. Acknowledge it.

**Poisson confidence intervals** for rare events:

| Observed Events (N) | 95% CI for Rate (per unit time) |
|---------------------|--------------------------------|
| 0 | 0 - 3.0/T |
| 1 | 0.03 - 5.6/T |
| 2 | 0.24 - 7.2/T |
| 3 | 0.62 - 8.8/T |
| 5 | 1.6 - 11.7/T |
| 10 | 4.8 - 18.4/T |

Where T = observation period. With N=2 events over 100 years, the 95% CI is 0.24-7.2%, not "2%."

**Rule of Three**: If N=0 in T years, the 95% upper bound on the rate is approximately 3/T per year.

#### Type 1 Checklist

Before finalizing a Type 1 probability estimate:

- [ ] Reference class explicitly defined (geographic, temporal, definitional scope)
- [ ] Base rate calculated with entity-years denominator
- [ ] Alternative reference classes considered; range reported if they diverge >2x
- [ ] Adjustments from base rate are ≤2x OR have specific structural justification
- [ ] Confidence interval acknowledges sample size uncertainty
- [ ] Comparative ranking cross-check performed

---

### Type 2: Threshold Events

**Core insight**: Probability depends on current pressure level, not just historical frequency. The same "1.5%/year" means different things at different pressure levels.

Type 2 events occur when accumulated pressure crosses a threshold. The system appears stable until it suddenly isn't. Estimation requires specifying pressure variables, threshold location, and the probability function connecting them.

#### Pressure Variable Specification

Identify the state variables whose accumulation drives the event. Specify their contribution to overall pressure.

**Format**:

| Variable | Weight | Transform | Current Value | Trend |
|----------|--------|-----------|---------------|-------|
| `variable_id` | 0.0-1.0 | linear/inverse/threshold/exponential | assessed | ↑/→/↓ |

**Weights** must sum to 1.0. They represent relative importance in driving the event.

**Transforms** convert raw variable values to pressure contributions:

| Transform | When to Use | Example |
|-----------|-------------|---------|
| `linear` | Pressure scales proportionally | Temperature → climate stress |
| `inverse` | Lower values = higher pressure | Regime stability → failure pressure |
| `threshold(X)` | Sharp increase above/below X | Debt above 80% GDP |
| `exponential` | Accelerating pressure at extremes | Conflict intensity |

**Example: Pakistan State Failure**

| Variable | Weight | Transform | Rationale |
|----------|--------|-----------|-----------|
| `regime_stability` | 0.35 | inverse | Core measure of state capacity |
| `water_stress` | 0.25 | linear | Binding physical constraint |
| `debt_external` | 0.15 | threshold(80) | Fiscal crisis trigger |
| `internal_conflict` | 0.15 | exponential | Conflict accelerates other pressures |
| `food_import_dependence` | 0.10 | linear | Vulnerability to external shocks |

#### Pressure Function Forms

How do pressure variables combine?

| Form | Formula | When to Use |
|------|---------|-------------|
| **Weighted sum** | Σ(weight × transformed_value) | Default; pressures are additive |
| **Maximum** | max(transformed_values) | Any single variable can trigger |
| **Product** | Π(transformed_values) | All conditions must be present |

**Weighted sum** is appropriate for most Type 2 events. Normalize output to 0-100 scale.

#### Threshold Estimation

The threshold is where probability transitions from "low" to "high." It's rarely known precisely.

**Estimation approaches**:

| Approach | Method | Applicability |
|----------|--------|---------------|
| **Historical calibration** | What pressure level preceded past occurrences? | When comparable events exist |
| **Structural analysis** | Is there a known physical/institutional threshold? | Climate tipping points, debt limits |
| **Expert elicitation** | What do domain experts believe? | When history and structure are ambiguous |

**Always specify uncertainty**. Thresholds are distributions, not points.

```yaml
threshold:
  estimate: 70  # on 0-100 pressure scale
  uncertainty: ±10  # or specify distribution
  basis: "Historical state failures occurred at pressure 60-80"
```

**Threshold sharpness (k)**: How quickly does probability rise around the threshold?

| k value | Interpretation | Example |
|---------|----------------|---------|
| 0.05 | Very gradual | Long warning period |
| 0.15 | Moderate | Some warning |
| 0.30 | Sharp | Rapid transition |
| 0.50+ | Near-step function | Binary threshold |

Most social/political events: k = 0.10-0.25 (gradual to moderate)

Physical tipping points: k = 0.20-0.40 (moderate to sharp)

#### Probability Function

Convert pressure to annual probability using a logistic function:

```
P(event) = floor + (ceiling - floor) / (1 + exp(-k × (pressure - threshold)))
```

**Parameters**:
- `floor`: Minimum probability even at low pressure (irreducible uncertainty)
- `ceiling`: Maximum probability at high pressure (usually 1.0 or lower if event isn't certain)
- `k`: Steepness (see above)
- `threshold`: Center of transition

**Typical values**:
- `floor`: 0.1% - 0.5% (rare events have irreducible uncertainty)
- `ceiling`: Often 1.0, but may be lower if other factors constrain
- `k`: 0.10 - 0.30 for most events

**Example: AMOC Weakening**

```yaml
probability_function:
  form: logistic
  floor: 0.002  # 0.2%/year minimum
  ceiling: 1.0
  k: 0.15
  threshold: 65

# At pressure = 45 (current): P ≈ 1.0%/year
# At pressure = 65 (threshold): P ≈ 50%/year
# At pressure = 80: P ≈ 90%/year
```

#### Time-Varying Probability

When pressure is expected to change over the simulation horizon:

**Option 1: Trajectory-dependent** (preferred for v2.0)
- Pressure evolves based on dynamics and events
- Probability recalculated each period
- Captures feedback loops

**Option 2: Horizon-averaged** (acceptable for v1.0)
- Estimate average pressure over horizon
- Use single probability estimate
- Document the trend

```yaml
# Horizon-averaged approach
probability:
  point_estimate: 1.5%  # horizon average
  trend: "Rising from ~1% early to ~2.5% late in horizon"
  rationale: "Pressure variables trending upward; threshold unchanged"
```

#### Type 2 Checklist

Before finalizing a Type 2 probability estimate:

- [ ] Pressure variables identified with weights summing to 1.0
- [ ] Transforms specified for each variable
- [ ] Current pressure level assessed (0-100 scale)
- [ ] Threshold estimated with uncertainty range
- [ ] Threshold basis documented (historical, structural, or expert)
- [ ] Probability function parameters specified (floor, ceiling, k)
- [ ] Time trend documented if pressure is expected to change
- [ ] Cross-check: does implied probability match comparative ranking?

---

### Type 3: Contingent Events

**Core insight**: Window probability is moderately tractable; resolution probability is not. Invest effort in specifying what happens *given* each resolution, not in estimating *which* resolution occurs.

Type 3 events depend on specific decisions, negotiations, or coordination outcomes. They have a two-stage structure:

1. **Window opens**: Preconditions create a situation where the event could occur
2. **Resolution**: Within the window, one of several outcomes materializes

**The key methodological challenge**: Resolution probabilities involve small-N actor decisions that resist estimation. Historical base rates don't transfer; expert intuitions are unreliable; structural reasoning provides weak constraints.

**Default treatment**: Use uniform probability across plausible resolutions. Deviation requires structural justification and is capped at 2:1 ratios.

**Where to invest effort**: Aftermath specification—what happens given each resolution. This is tractable and is where analytical effort pays off.

For full operational guidance, see [[methodology/reference/type-3-calibration]].

For a worked example, see [[events/geopolitical/taiwan-conflict]].

#### Type 3 Quick Checklist

- [ ] Window preconditions defined
- [ ] Window probability estimated (historical crisis frequency)
- [ ] Resolutions are mutually exclusive and collectively exhaustive
- [ ] Resolution probabilities are uniform OR deviation is structurally justified
- [ ] Aftermath branches fully specified for each resolution
- [ ] Cascade triggers documented with rationale
