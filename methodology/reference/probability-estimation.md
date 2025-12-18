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
