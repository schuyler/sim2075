---
title: entropy-maximization
type: note
permalink: methodology/concepts/entropy-maximization
tags:
- methodology
- concepts
- epistemology
- uncertainty
- calibration
- maximum-entropy
---

# Entropy Maximization

When the simulation requires a quantitative parameter but we lack empirical grounding for its value, the principled default is the distribution (or value) that encodes the least information beyond what we actually know.

This is not a claim about reality. It is a discipline for honest modeling under uncertainty.

---

## The Problem

Simulation requires numbers. Event probabilities, correlation coefficients, impact magnitudes, resolution likelihoods—these must all be specified before the model can run.

Many of these parameters cannot be empirically calibrated:

- **Factor correlations**: Latent factors are not directly observable; we cannot measure historical co-occurrence of "climate stress" and "food system stress" as abstract constructs.
- **Type 3 resolution probabilities**: Small-N actor decisions have no base rate; "probability Xi invades Taiwan" does not refer to a stable frequency.
- **Novel event probabilities**: Events without historical precedent (AMOC collapse, fusion breakthrough) lack calibration anchors.
- **Impact magnitudes**: How much does a given event affect GDP, mortality, institutional capacity? Historical analogues are imperfect; contexts differ.

The temptation is to make educated guesses and present them as estimates. But an "estimate" implies something being estimated—a true value we're approximating. For many parameters, there is no such value. We are not estimating facts about the world; we are making modeling choices under deep uncertainty.

The alternative to principled defaults is arbitrary choice dressed up as knowledge.

---

## The Principle

**Maximum entropy**: Among all distributions consistent with what you actually know, choose the one with the highest entropy.

Entropy measures uncertainty. A maximum entropy distribution is the one that assumes the least beyond your constraints. It encodes your knowledge and nothing more.

This is not a claim that reality is maximally random. It is epistemic hygiene—a refusal to smuggle in certainty you do not possess.

### Why This Matters

Specifying a precise value (or a narrow distribution) when you lack grounds for precision is not cautious. It is overconfident. It embeds unjustified assumptions into the model, where they will propagate through thousands of simulation runs, shaping tail outcomes in ways that may be invisible.

Maximum entropy makes the uncertainty explicit. It says: "I don't know, and I'm not going to pretend otherwise."

---

## What Maximum Entropy Looks Like in Practice

| Parameter Type | Maximum Entropy Default | Example |
|---------------|------------------------|---------|
| Correlation between factors | Zero (independence) | F_TECH and F_SSA: no clear mechanism → ρ = 0 |
| Discrete outcome probabilities | Uniform over plausible outcomes | Three Taiwan resolutions → 33%/33%/33% |
| Correlation magnitude | Weakest value consistent with mechanism | Climate affects food, but how strongly? Start weak. |
| Continuous magnitude | Widest distribution consistent with bounds | Impact could range from X to Y; use full range |
| Event probability (novel) | Informed by loosest defensible reference class | No direct precedent; what's the broadest analogous category? |

The default is ignorance. Knowledge is what lets you narrow the distribution.

---

## What Justifies Deviation

Maximum entropy is the starting point, not the final answer. Deviation is justified when you have genuine grounds for it:

### Mechanism-Based Reasoning

A structural relationship that would produce the pattern you're encoding.

"Climate stress and food system stress are correlated because drought, heat, and flooding directly disrupt agricultural production. The mechanism is physical, not incidental."

This justifies moving F_CLIM ↔ F_FOOD correlation above zero. It does not, by itself, justify 0.50 rather than 0.30.

### Historical Analogues

Past instances that ground magnitude estimates.

"Financial crises have historically produced 5-15% GDP contractions in affected countries; the 2008 crisis produced ~4% global contraction."

This constrains impact magnitude ranges. The constraint is only as strong as the analogy.

### Logical or Structural Constraints

Some outcomes are more constrained than others by the structure of the situation.

"Military conflict requires mobilization, logistical preparation, and domestic political alignment. Diplomatic resolution requires only agreement. The activation energy differs."

This might justify asymmetric resolution probabilities—but note how much work the argument is doing.

### Expert Consensus

When domain experts converge on a range, that convergence is evidence (though not proof).

"Climate scientists broadly agree AMOC collapse probability this century is in the 5-15% range under high emissions scenarios."

Expert consensus is useful but defeasible. Experts are often wrong, especially on unprecedented events.

---

## The Documentation Requirement

Every deviation from maximum entropy should be explicitly documented:

1. **What is the default?** (What would maximum entropy specify?)
2. **What are we specifying instead?** (The actual parameter value)
3. **What justifies the deviation?** (Mechanism, analogue, constraint, or consensus)
4. **How confident are we in the justification?** (Strong/moderate/weak)

This creates an audit trail. When sensitivity analysis reveals that tail outcomes depend on a particular parameter, we can trace back to the justification and assess whether it bears the weight.

---

## Instances in This Simulation

### Factor Correlations

The current approach in [[methodology/reference/factor-correlation-matrix]] already approximates entropy maximization:

- Default correlation is zero
- Non-zero correlations require mechanism-based justification
- Magnitudes are kept moderate (nothing above 0.55)

What's missing: explicit justification for *magnitude* choices. Why 0.50 for F_CLIM ↔ F_FOOD rather than 0.35 or 0.65? The mechanism justifies non-zero; it doesn't pin down the value.

### Type 3 Resolution Probabilities

See [[methodology/concepts/small-n-actor-problem]] for why this case is particularly resistant to justified deviation.

The Small-N Actor Problem means:
- No base rates to anchor on
- Radical context-dependence undermines analogies
- Strategic interaction makes structural reasoning fragile

For Type 3 events, uniform resolution probabilities are often the most defensible specification. Deviation requires unusually strong structural arguments.

### Event Probabilities

Some events have historical base rates (pandemics, financial crises). Others are unprecedented (AMOC collapse, specific state failures).

For unprecedented events, maximum entropy suggests:
- Use the loosest defensible reference class
- Acknowledge wide uncertainty bounds
- Flag for sensitivity analysis

### Impact Magnitudes

Less developed in current methodology. Impact vectors specify how events affect state variables, but the calibration approach is not yet systematic.

Maximum entropy would suggest:
- Start with wide ranges based on historical analogues
- Narrow only when specific mechanisms constrain magnitude
- Document analogues and their limitations

---

## Relationship to Sensitivity Analysis

Maximum entropy defaults and sensitivity analysis are complementary:

1. **Maximum entropy flags uncertainty**: Parameters set by maximum entropy (or with weak justification for deviation) are explicitly uncertain.

2. **Sensitivity analysis tests dependence**: Run simulations with parameter variations to see which assumptions drive tail outcomes.

3. **Results guide research**: If outcomes depend heavily on a weakly-justified parameter, that parameter deserves deeper investigation (Level 2/3 research).

4. **Honest reporting**: Report tail outcome distributions with explicit conditioning on key uncertain parameters.

Parameters where deviation from maximum entropy materially affects conclusions deserve scrutiny. Parameters where the maximum entropy default is robust to perturbation can be left as-is.

---

## What This Is Not

### Not a claim that reality is maximally entropic

The world has structure. Events are correlated. Outcomes are not uniform. Maximum entropy is not a metaphysical thesis; it's a modeling discipline.

### Not an excuse to avoid research

Evidence that justifies deviation from maximum entropy is valuable. The principle doesn't say "don't investigate"—it says "don't pretend to know what you haven't established."

### Not a substitute for domain expertise

Expertise helps identify constraints, mechanisms, and analogues. The principle provides a framework for deploying expertise honestly, not a replacement for it.

### Not unique to this simulation

Maximum entropy is a general principle in Bayesian reasoning and information theory. We are applying a well-established idea to a specific modeling context.

---

## Summary

When you must specify a parameter but cannot calibrate it:

1. **Start with maximum entropy** — the least presumptuous default
2. **Deviate only with justification** — mechanism, analogue, constraint, or consensus
3. **Document the reasoning** — create an audit trail
4. **Test sensitivity** — see if conclusions depend on the assumption
5. **Report honestly** — distinguish grounded parameters from modeling choices

The goal is not to eliminate uncertainty—that's impossible. The goal is to avoid burying uncertainty under false precision.

---

## Related Documents

- [[methodology/concepts/tractability-boundaries]] — When to apply this principle (diagnostic for low-tractability parameters)
- [[methodology/concepts/small-n-actor-problem]] — Why Type 3 events are particularly resistant to justified deviation
- [[methodology/concepts/epistemology]] — General intellectual honesty framing
- [[methodology/reference/factor-correlation-matrix]] — Factor correlations (implicit application of this principle)
- [[methodology/project/open-questions]] — Type 3 calibration as active question

---

*Added: December 2025*