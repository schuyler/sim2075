---
title: epistemology
type: note
permalink: methodology/epistemology
tags:
- methodology
- epistemology
- honesty
- uncertainty
---

# Epistemological Honesty

## What This Model Is

This simulation constructs **plausible scenarios and narratives about possible futures**. It is not a prediction engine. The outputs are "futures that could happen and are worth thinking about," not "futures that will happen."

Virtually every parameter in this model—probabilities, impacts, factor loadings—is **educated judgment**. We are not estimating knowable quantities with measurement error; we are quantifying beliefs about deeply uncertain futures. The numbers exist to structure our thinking and enable systematic comparison, not to provide false precision about unknowable outcomes.

## The Standard We Can Meet

**We cannot achieve:**
- Calibrated probability estimates (we can't verify against outcomes)
- Empirically validated impact functions (insufficient data)
- Objectively correct factor loadings (no ground truth exists)

**We can achieve:**
- **Transparency**: Every estimate has documented reasoning
- **Internal consistency**: Similar events get similar treatment
- **Evidentiary grounding**: Judgments cite factual basis where available
- **Honest uncertainty**: We acknowledge what we don't know
- **Revisability**: Estimates can be updated as understanding improves

## The Alternative to Honesty

An intellectually dishonest model—one that hides its assumptions, overstates its precision, or cherry-picks convenient estimates—is worse than worthless. It produces false confidence in fantasy.

We would rather have wide uncertainty ranges that honestly reflect our ignorance than narrow ranges that pretend knowledge we don't have.

## What Probabilities Mean Here

When we assign a probability of 2% per year to an event, we mean: **"In our judgment, informed by available evidence, this event occurs in roughly 2% of year-observations across the range of futures we consider plausible."**

This is a belief, not a measurement. It cannot be validated against outcomes on relevant timescales. The probability exists to:
- Force explicit quantification of vague intuitions ("unlikely" → "1-2% per year")
- Enable comparison across events
- Allow Monte Carlo sampling to produce distributions
- Make assumptions auditable and revisable

## Precision Expectations

**Do not overstate precision.** For most events, we cannot meaningfully distinguish between "5% GDP impact" and "7% GDP impact."

**Use ranges, not false precision.** Instead of:
```
GDP impact: mean -5%, std 2%, distribution normal
```

Write:
```
GDP impact: -3% to -8%, most likely around -5%
```

The latter is more honest about what we actually know.

## The Honesty Test

Before finalizing any specification, ask:
- Is uncertainty honestly expressed (not hidden)?
- Are limitations acknowledged?
- Is reasoning auditable?
- Could another analyst understand and critique this?

If no to any of these, revise until yes.

---

## Related Documents

- [[methodology/concepts/tractability-boundaries]] — Operationalizes these principles: what can vs. cannot be reasoned about
- [[methodology/concepts/entropy-maximization]] — What to do when parameters cannot be calibrated
- [[methodology/concepts/small-n-actor-problem]] — A specific class of intractability (Type 3 events)

---

*See [[methodology/00-start-here]] for navigation*
