---
title: quality-checklist
type: note
permalink: methodology/quality-checklist
tags:
- methodology
- checklist
- quality
---

# Quality Checklist

**Updated per [[methodology/integrated-event-state-framework]]**

Run this checklist before marking any event specification complete.

---

## Causal Type Classification

- [ ] **Causal type assigned** (Type 1, 2, or 3)
- [ ] **Rationale documented** — why this type, not another?
- [ ] **Not Type 4** — if S-curve dynamics, move to baseline trajectory, not event catalog

### Type-Specific Requirements

**If Type 1 (Stochastic):**
- [ ] Base rate derived from reference class or expert elicitation
- [ ] Condition adjustments documented

**If Type 2 (Threshold):**
- [ ] Pressure function specified with state variables and weights
- [ ] Threshold estimate provided with uncertainty range
- [ ] Sharpness parameter (k) specified
- [ ] Historical calibration for threshold cited
- [ ] Minimum probability floor set

**If Type 3 (Contingent):**
- [ ] Window preconditions specified (state variable conditions)
- [ ] Annual probability given conditions met
- [ ] Multiple resolutions defined with probabilities summing to 100%
- [ ] Separate impact vectors for each resolution
- [ ] Resolution probabilities have rationale

---

## Probability

- [ ] Point estimate provided with range
- [ ] Range is honestly wide (not false precision)
- [ ] Derivation documents which method(s) used
- [ ] Comparative ranking against related events completed
- [ ] Key uncertainties explicitly identified
- [ ] Confidence level (Low/Medium/High) assigned
- [ ] 25-year cumulative probability calculated for intuition check

---

## Factor Loadings

- [ ] Sum of squared loadings ≤ 1.0
- [ ] Primary factor identified with rationale
- [ ] Non-zero loadings have brief justification
- [ ] Similar events have consistent patterns
- [ ] **For Type 2/3:** Loadings describe factor→state relationship (factors shock pressure variables)

---

## Impact Vector

- [ ] **All significant affected variables identified**
- [ ] Direction (↑/↓) specified for each
- [ ] Magnitude with uncertainty (mean ± std) for each
- [ ] **Onset timing** specified (immediate / delayed(N) / gradual(N))
- [ ] **Durability type** assigned for each impact based on impact type:
  - permanent (deaths, knowledge, resource depletion)
  - decaying (financial shocks, confidence)
  - maintenance_required (agreements, treaties)
  - shock_vulnerable (development gains)
  - regime_dependent (political achievements)
- [ ] Durability parameters provided where required
- [ ] Differential impacts documented if relevant (by country exposure)
- [ ] Method (analog/transmission/scaling) documented
- [ ] Reference cases cited

---

## Cascade Effects

- [ ] Cascade pathways documented (event → state change → P(other events))
- [ ] Target events identified with probability modifiers
- [ ] Duration of cascade effects specified
- [ ] No circular cascades without explicit feedback documentation

---

## Documentation

- [ ] All template sections completed (using [[methodology/event-template-v2]])
- [ ] Research tier noted (Level 1/2/3)
- [ ] Upgrade candidate status noted
- [ ] Open questions documented
- [ ] Cross-references to related events included
- [ ] Last updated date current

---

## Honesty Check

- [ ] Uncertainty is honestly expressed (not hidden)
- [ ] Limitations are acknowledged
- [ ] Reasoning is auditable
- [ ] Another analyst could understand and critique
- [ ] **No implicit valence** — event described as state transition, not "good" or "bad"

---

## Quick Reference: Common Mistakes

| Mistake | Fix |
|---------|-----|
| S-curve dynamics as event | Move to baseline trajectory uncertainty |
| "Positive event" / "negative event" framing | Describe as state transition with impact vector |
| Durability assigned by event valence | Assign by impact type (deaths=permanent, agreements=maintenance_required) |
| Type 2 without pressure function | Specify which state variables accumulate pressure |
| Type 3 without multiple resolutions | Define resolution options (conflict/negotiation/status quo) |
| Factor loadings sum-of-squares > 1.0 | Rescale loadings |
| Single-point impact estimates | Always provide range |
| Missing onset timing | Specify immediate/delayed/gradual |
| Cascades asserted but not specified | Document target events and probability modifiers |
