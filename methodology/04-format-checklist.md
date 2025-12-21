---
title: 04-format-checklist
type: note
permalink: methodology/04-format-checklist
tags:
- methodology
- checklist
- quality
- verification
- format
---

# Format Checklist

**Updated per [[methodology/integrated-event-state-framework]]**

Run this checklist before marking any event specification complete.

**Prerequisite**: Run [[methodology/03-critical-review]] first. A specification that passes format checks but fails the critical review is wrong in ways that matter more than missing fields.

---

## Causal Type Classification

- [ ] Causal type assigned (Type 1, 2, or 3)
- [ ] Type classification rationale documented
- [ ] Hybrid events have both primary and secondary type noted
- [ ] Type 4 candidates moved to baseline trajectories (not events)

### For Type 1 (Stochastic) Events:

- [ ] Historical base rate identified with reference class
- [ ] Condition adjustments documented
- [ ] Factor contributions to clustering specified

### For Type 2 (Threshold) Events:

- [ ] Pressure function specified with variables and weights
- [ ] Threshold estimate provided with uncertainty range
- [ ] Historical calibration for threshold documented
- [ ] Minimum probability floor specified
- [ ] Sharpness parameter (k) chosen

### For Type 3 (Contingent) Events:

- [ ] Window preconditions specified as state variable conditions
- [ ] Annual probability given conditions documented
- [ ] All resolutions listed with probabilities (must sum to 100%)
- [ ] Each resolution has separate impact vector
- [ ] Anti-correlated resolutions identified (mutually exclusive outcomes)
- [ ] **Critical review**: For each resolution, could these state trajectories be reached through 10 years of gradual drift? If yes, it's not a discontinuity — remove the resolution or raise the threshold.

---

## Probability

- [ ] Point estimate provided with range
- [ ] Range is honestly wide (not false precision)
- [ ] Derivation documents which method(s) used
- [ ] Comparative ranking against related events completed
- [ ] Key uncertainties explicitly identified
- [ ] Confidence level (Low/Medium/High) assigned

---

## Factor Loadings

- [ ] Sum of squared loadings ≤ 1.0
- [ ] Primary factor identified with rationale
- [ ] Non-zero loadings have brief justification
- [ ] Similar events have consistent patterns
- [ ] For Type 2/3: loadings describe factor→state relationship (not direct event triggering)

---

## Impact Vector

### Structure

- [ ] All significant variables affected are listed
- [ ] Direction (↑/↓) specified for each
- [ ] Magnitude specified as mean ± std (not point estimate)
- [ ] Onset timing specified (immediate / delayed / gradual)

### Durability

- [ ] Durability type assigned for each impact
- [ ] Durability parameters specified where required:
  - [ ] `permanent`: no parameters needed
  - [ ] `decaying`: half_life and floor specified
  - [ ] `maintenance_required`: annual_failure_prob and failure_conditions
  - [ ] `shock_vulnerable`: vulnerable_to events and reversal_fraction
  - [ ] `regime_dependent`: persists_in_regimes specified

### Differential Impacts

- [ ] Country/region-specific impacts documented where significant
- [ ] Exposure variable identified if impacts scale with country characteristics
- [ ] Differential function (linear/threshold) specified

### Estimation

- [ ] Method documented (analog / transmission / scaling)
- [ ] Reference cases cited if using analog method
- [ ] Transmission channels enumerated if using that method

---

## Cascade Effects

- [ ] Cascade pathways documented (how this event affects other event probabilities)
- [ ] Target events identified
- [ ] Probability modifiers specified (+X% or ×Y multiplier)
- [ ] Duration of cascade effect specified
- [ ] Mechanism described

---

## Documentation

- [ ] All template sections completed
- [ ] Research tier noted (Level 1/2/3)
- [ ] Open questions documented
- [ ] Cross-references to related events included
- [ ] Sources cited

---

## Honesty Check

- [ ] Uncertainty is honestly expressed (not hidden)
- [ ] Limitations are acknowledged
- [ ] Reasoning is auditable (another analyst could understand and critique)
- [ ] No implicit positive/negative valence assigned to event
- [ ] Impact vector captures multi-dimensional effects

---

## Quick Reference: Common Mistakes

| Mistake | Correction |
|---------|------------|
| Assigning "positive" or "negative" to event | Events have impact vectors, not valence |
| Type 4 dynamics as discrete events | Move to baseline trajectory uncertainty |
| Same durability for all impacts | Durability depends on impact type |
| Type 2 without pressure function | Specify variables, weights, threshold |
| Type 3 with single outcome | Specify multiple resolutions with probabilities |
| Factor loadings > 1.0 sum of squares | Rescale loadings |
| Point estimates for impacts | Always provide ranges |
| Missing cascade documentation | Document how state changes affect other events |