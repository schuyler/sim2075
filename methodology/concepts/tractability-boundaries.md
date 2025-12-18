---
title: tractability-boundaries
type: note
permalink: methodology/concepts/tractability-boundaries
tags:
- methodology
- concepts
- epistemology
- tractability
- uncertainty
- modeling
---

# Tractability Boundaries

The simulation requires modeling many aspects of the world. Some we can reason about with structural arguments, historical analogues, and observable data. Others we cannot. Honest modeling requires identifying these boundaries and respecting them.

This note operationalizes the intellectual honesty framing in [[methodology/concepts/epistemology]] into practical guidance for where to invest analytical effort and where to apply maximum entropy defaults.

---

## The Core Insight

Not all parameters are equally knowable. The simulation's credibility depends on:

1. **Identifying what we can reason about** — and putting analytical effort there
2. **Identifying what we cannot reason about** — and applying [[methodology/concepts/entropy-maximization]] there
3. **Not confusing the two** — which is the most common failure mode

Effort invested in intractable domains produces false precision. Effort invested in tractable domains produces genuine insight. The meta-skill is distinguishing them.

---

## Tractability Stratification

### High Tractability

Domains where structural reasoning, historical data, and observable constraints allow meaningful estimation.

| Domain | Why Tractable | Example |
|--------|---------------|---------|
| Physical dynamics | Obeys conservation laws, measurable | AMOC freshwater input rates |
| Accounting identities | Must balance by definition | Fiscal deficit accumulation |
| Supply chain structure | Observable, documented | Semiconductor production concentration |
| Historical base rates | Repeated events, stable processes | Pandemic emergence frequency |
| Demographic trajectories | High inertia, well-measured | Working-age population 2040 |

**Treatment**: Invest analytical effort. Calibrate against data. Narrow uncertainty ranges where evidence permits.

### Moderate Tractability

Domains where mechanisms are understood but magnitudes are uncertain, or where analogues exist but transfer is imperfect.

| Domain | Why Partially Tractable | Example |
|--------|------------------------|---------|
| Factor correlations | Mechanisms clear; magnitudes judgment-based | Climate-food linkage strength |
| Impact magnitudes | Historical analogues exist; context differs | GDP effect of financial crisis |
| Threshold locations | Process understood; exact trigger uncertain | State failure threshold |
| Technology trajectories | S-curves documented; timing uncertain | Renewable cost declines |

**Treatment**: Use mechanism-based reasoning to justify non-zero/non-uniform values. Accept magnitude uncertainty. Document reasoning. Flag for sensitivity analysis.

### Low Tractability

Domains where we lack structural purchase—no base rates, no transferable analogues, radical context-dependence.

| Domain | Why Intractable | Example |
|--------|-----------------|---------|
| Small-N actor decisions | Singular context, unobservable preferences | Will Xi invade Taiwan? |
| Novel event probabilities | No precedent, no reference class | AMOC collapse probability |
| Coordination outcomes | Multiple equilibria, belief-dependent | Climate agreement success |
| Regime transitions | Path-dependent, contingent on sequence | Democratic consolidation |

**Treatment**: Apply entropy maximization. Use uniform distributions or weakest defensible priors. Do not invest effort pretending to estimate. Shift effort to conditional consequences.

### The Critical Boundary

The most important boundary is between moderate and low tractability. This is where false precision typically enters.

The temptation: "I've read a lot about China-Taiwan relations; surely I can estimate conflict probability better than a uniform prior."

The reality: Reading about a domain increases your understanding of mechanisms and context. It does not give you access to Xi Jinping's private reasoning, his read of domestic political constraints, or his information environment on a particular day. The Small-N Actor Problem is not solved by domain expertise.

Expertise helps you identify *what would matter* if you could observe it. It does not help you observe it.

---

## Practical Application

### When Specifying an Event

Ask: **Which components of this event specification are tractable?**

For a Type 3 event like Taiwan conflict:

| Component | Tractability | Treatment |
|-----------|--------------|-----------|
| Preconditions for window opening | Moderate | Structural reasoning about tension escalation |
| Window probability given preconditions | Moderate | Historical frequency of crises reaching critical phase |
| Resolution probabilities | Low | Small-N actor decisions → entropy maximization |
| Aftermath given military conflict | Moderate-High | Supply chain data, financial precedents, escalation logic |
| Aftermath given accommodation | Moderate | Precedent analysis, structural constraints |

The insight: **Resolution probabilities are intractable, but aftermath consequences are more tractable.** Shift analytical effort from "guessing what actors do" to "reasoning about consequences conditional on what they do."

### When Specifying Factor Correlations

Ask: **Is the mechanism or the magnitude tractable?**

For F_CLIM ↔ F_FOOD correlation:

| Component | Tractability | Treatment |
|-----------|--------------|-----------|
| Existence of correlation | High | Physical mechanism is clear and documented |
| Sign of correlation | High | Climate stress increases food stress, not reverse |
| Magnitude of correlation | Moderate | Mechanism doesn't pin down 0.3 vs 0.5 vs 0.7 |

The insight: **Non-zero is justified; specific magnitude is not.** Document the mechanism, accept magnitude uncertainty, test sensitivity.

### When Interpreting Results

Ask: **Do conclusions depend on tractable or intractable parameters?**

If tail outcomes depend heavily on:
- **Tractable parameters** → Conclusions have some grounding; worth refining estimates
- **Intractable parameters** → Conclusions are conditional; report as "if X, then Y" rather than integrated probabilities

The simulation is most valuable when it reveals structural dependencies, not when it produces integrated forecasts that bury intractable assumptions.

---

## The Effort Allocation Principle

Given limited analytical capacity, allocate effort to tractable domains:

| Priority | Domain | Rationale |
|----------|--------|-----------|
| High | Aftermath specifications | Structural reasoning applies; drives tail outcomes |
| High | Factor mechanisms | Justify non-zero correlations; identifies what clusters |
| Medium | Impact calibration | Historical analogues provide partial grounding |
| Medium | Pressure variable tracking | Observable indicators, threshold logic |
| Low | Type 3 resolution probabilities | Intractable; entropy maximization applies |
| Low | Novel event base rates | No reference class; use wide bounds |

Effort on low-priority domains produces documentation of uncertainty, not reduction of uncertainty. That's valuable—but don't mistake it for progress on estimation.

---

## Relationship to Other Concepts

### Entropy Maximization

[[methodology/concepts/entropy-maximization]] specifies *what to do* when tractability is low: default to maximum entropy.

Tractability boundaries tell you *when* to apply that principle—it's the diagnostic that triggers the treatment.

### Small-N Actor Problem

[[methodology/concepts/small-n-actor-problem]] is a specific *cause* of low tractability for Type 3 events.

Understanding why actor decisions are intractable (no base rates, context-dependence, strategic interaction, unobservable preferences) helps identify the boundary and avoid false confidence.

### Epistemology

[[methodology/concepts/epistemology]] frames *why* we care about these boundaries: intellectual honesty requires not claiming knowledge we don't have.

Tractability boundaries operationalize that principle into practical classification.

---

## Common Failure Modes

### Expertise Conflation

"I know a lot about this domain, therefore I can estimate this parameter."

Knowledge of mechanisms and context is not the same as ability to estimate specific values. Expertise helps you understand *what you don't know*; it doesn't eliminate the not-knowing.

### Effort Justification

"I spent 20 hours researching this; surely my estimate is better than a prior."

Time invested does not equal tractability gained. If the parameter is fundamentally intractable, more research produces more sophisticated uncertainty, not less uncertainty.

### False Precision Through Averaging

"Different sources give different estimates; I'll average them for my central estimate."

Averaging poorly-grounded estimates does not produce a well-grounded estimate. If the underlying estimates lack structural basis, their average lacks structural basis.

### Tractability by Analogy

"A similar situation occurred in 1962; I can use that to estimate this probability."

Historical analogies are useful but defeasible. The question is whether the relevant features transfer. For Small-N actor decisions, the relevant features (specific actors' reasoning in specific contexts) typically do not transfer.

---

## Summary

1. **Stratify by tractability** — Identify which parameters you can reason about structurally
2. **Invest effort in tractable domains** — This is where analysis produces insight
3. **Apply entropy maximization to intractable domains** — Don't pretend to know what you can't
4. **Shift from probabilities to conditionals** — "If X, then Y" is often more tractable than "P(X)"
5. **Report honestly** — Distinguish conclusions that depend on tractable versus intractable assumptions

The simulation's value comes from exploring structural relationships and identifying what drives tail outcomes. It does not come from producing integrated forecasts that bury intractable assumptions under false precision.

---

## Related Documents

- [[methodology/concepts/epistemology]] — Why intellectual honesty matters
- [[methodology/concepts/entropy-maximization]] — What to do when tractability is low
- [[methodology/concepts/small-n-actor-problem]] — Why Type 3 resolutions are intractable
- [[methodology/reference/causal-types]] — Event type definitions
- [[methodology/project/open-questions]] — Type 3 calibration as active question

---

*Added: December 2025*