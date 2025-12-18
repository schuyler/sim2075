---
title: small-n-actor-problem
type: note
permalink: methodology/concepts/small-n-actor-problem
tags:
- methodology
- concepts
- epistemology
- type-3
- forecasting
- uncertainty
---

# The Small-N Actor Problem

Type 3 (Contingent) event resolutions depend on decisions made by a small number of specific actors—individual leaders, particular governments, specific negotiating parties. This creates a fundamental epistemic challenge that does not apply to Type 1 or Type 2 events.

---

## The Core Problem

When outcomes depend on the decisions of 1-5 specific people in a specific context, there is no meaningful sense in which we can estimate "the probability" of their choice.

Xi Jinping's specific psychology, his read of domestic political constraints, his assessment of US resolve, his information environment on a particular day—these are not random draws from a distribution. They are singular facts about a singular situation. We can construct arguments for many different choices being "rational" given different assumptions about his beliefs and preferences.

This is not parameter uncertainty (knowing there's a true value we're estimating imprecisely). It's closer to ontological uncertainty—it's unclear whether "the probability Xi invades Taiwan given crisis conditions" refers to anything stable enough to estimate.

---

## Contrast with Type 1 and Type 2

### Type 1 (Stochastic) events don't have this problem

Novel pandemic emergence aggregates across billions of human-animal interactions, millions of potential spillover events, thousands of local outbreak opportunities. Individual idiosyncrasies average out. We can reason about base rates because we're implicitly aggregating across a large space of possibilities.

Historical frequency provides genuine calibration: ~3 novel pandemics per century gives us something to anchor on, even with substantial uncertainty about the next one.

### Type 2 (Threshold) events don't have this problem

Pressure accumulation is often observable or at least structurally constrained. AMOC freshwater input can be measured. Fiscal deficits are public. Reserve depletion follows accounting identities.

The threshold may be uncertain, but the *process* generating the event has structure we can reason about. When Pakistan's fiscal position deteriorates, we're tracking something real that constrains what can happen, regardless of any individual's preferences.

### Type 3 events are different

Resolution depends on choices by specific actors who:
- Have private information we cannot observe
- Have preferences we can only infer (and infer poorly)
- Are embedded in strategic interactions where optimal choice depends on beliefs about others' choices
- Face contexts that are never repeated identically

There is no large-N averaging. There is no observable pressure variable. There is only judgment about how particular people would act in hypothetical situations.

---

## Why This Is Intractable

Four features combine to make Type 3 resolution probabilities resistant to principled estimation:

### 1. No base rate

"How often do Chinese leaders invade Taiwan?" has a sample size of zero. We can look at historical analogies—Khrushchev and Cuba, various Taiwan Strait crises, other great power confrontations—but these are *suggestive*, not *calibrating*. Different actors, different contexts, different constraints.

Base rate reasoning requires repeated draws from a stable process. Small-N decisions are not repeated draws from anything.

### 2. Radical context-dependence

Even perfect knowledge of an actor's "type" would not suffice. The same leader makes different decisions under:
- Different domestic political pressures
- Different economic conditions  
- Different assessments of adversary capability and resolve
- Different information environments
- Different positions in their political lifecycle

Gorbachev in 1985 and Gorbachev in 1991 made very different choices, not because he changed but because everything around him changed.

### 3. Strategic interaction

Type 3 resolutions typically involve multiple actors, each modeling the others. Game-theoretic analysis can identify equilibria, but:
- Equilibria are sensitive to assumptions about payoffs (which are unobserved)
- Equilibria are sensitive to assumptions about beliefs (which are unobserved)
- Multiple equilibria often exist, with no principled way to select among them
- Real actors may not play equilibrium strategies

The Cuban Missile Crisis could have ended in nuclear war or peaceful resolution depending on decisions made over 13 days. Both outcomes were "possible" in a way that resists probabilistic summary.

### 4. Unobservable preferences

We do not actually know what actors want. We infer from behavior, but:
- Behavior is strategic (actors may misrepresent preferences)
- Behavior is context-dependent (revealed preference in one context doesn't transfer)
- Stated preferences are often propaganda
- Internal preference orderings may be unstable or inconsistent

Does Putin "want" to restore Soviet borders, maintain regime security, achieve personal legacy, or something else? His revealed behavior is consistent with multiple preference structures that would imply different choices in novel situations.

---

## Empirical Evidence: Forecasting Limits

This is not just philosophical hand-wringing. We have empirical evidence that humans—including experts—are poor at predicting small-N actor decisions.

### Superforecaster accuracy bounds

The Good Judgment Project and successor efforts represent the best-documented attempts at rigorous geopolitical forecasting. Key findings:

- Top forecasters achieve ~70-75% accuracy on well-defined geopolitical questions over 1-2 year horizons
- Accuracy degrades significantly at longer horizons
- Performance is notably worse on questions involving specific leader decisions versus structural/aggregate outcomes
- Even superforecasters show limited ability to outperform simple base-rate models on many question types

### Expert prediction failures

Tetlock's original Expert Political Judgment study (2005) found that experts predicting political outcomes performed barely better than chance, and worse than simple extrapolation algorithms. Expertise in a domain did not translate to forecasting accuracy in that domain.

### Structural versus agentic questions

Forecasters perform relatively better on structural questions ("Will GDP growth exceed X%?") than on agentic questions ("Will leader Y take action Z?"). This matches the theoretical expectation: structural outcomes aggregate across many factors; agentic outcomes depend on small-N decisions.

---

## Implications for the Simulation

### What this means for Type 3 specifications

1. **Resolution probabilities are not estimates of stable quantities.** When we write "P(military conflict | Taiwan crisis window) = 0.35", we are not estimating a fact about the world. We are making a modeling choice that enables simulation.

2. **Point estimates convey false precision.** Any single number for a Type 3 resolution probability obscures the genuine uncertainty about whether that number is meaningful.

3. **Calibration anchors have limited value.** Unlike Type 1 events (where historical frequency grounds estimates) or Type 2 events (where pressure-threshold relationships can be studied), Type 3 resolutions lack natural calibration targets.

4. **Sensitivity analysis is essential.** Because Type 3 resolution probabilities are poorly grounded, understanding how tail outcomes depend on these assumptions is critical. If civilizational-risk conclusions depend heavily on Taiwan resolution probabilities, that's important to surface.

5. **Epistemic humility must be structural, not cosmetic.** Adding error bars to point estimates doesn't solve the problem if the point estimate itself has no principled basis. The simulation architecture must reflect genuine uncertainty, not just acknowledge it in documentation.

---

## Not Addressed Here

This note identifies the problem. It does not propose solutions.

The question of how to specify Type 3 events given this fundamental limitation is tracked in [[methodology/project/open-questions]] under "Type 3 Event Calibration."

Candidate approaches include maximum entropy defaults, scenario-based sensitivity analysis, calibration shrinkage based on forecaster track records, and explicit epistemic categorization. These are methodological choices to be made, not consequences of the problem statement.

---

## Related Documents

- [[methodology/concepts/tractability-boundaries]] — General framework for what is/isn't tractable (this note explains one cause of low tractability)
- [[methodology/concepts/entropy-maximization]] — General principle for uncalibrated parameters (this note is a special case)
- [[methodology/reference/causal-types]] — Type 1/2/3/4 definitions
- [[methodology/project/open-questions]] — Type 3 calibration as active question
- [[methodology/concepts/epistemology]] — Intellectual honesty framing

---

*Added: December 2025*