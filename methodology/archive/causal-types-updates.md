---
title: causal-types-updates
type: note
permalink: methodology/reference/causal-types-updates
tags:
- methodology
- reference
- type-3
- causal-types
- stub
- planning
---

# Causal Types Update Plan

**Status:** APPLIED — changes incorporated into [[methodology/reference/causal-types]] on December 2025 (Task 1.2)

This document outlines changes to incorporate the tractability framework into the Type 3 section of the causal types reference.

---

## Current State

The existing causal-types document correctly describes the Type 3 window-resolution structure but doesn't address:

1. The epistemic status of resolution probabilities
2. Where analytical effort should be invested
3. How to handle the Small-N Actor Problem
4. The relationship between tractability and specification strategy

---

## Planned Changes

### 1. Add Tractability Framing to Type 3 Section

Insert after the current Type 3 specification format:

```markdown
### Tractability Note

Type 3 events present a unique calibration challenge. See [[methodology/reference/type-3-calibration]] for full guidance.

**Key insight:** Resolution probabilities are low-tractability (Small-N Actor Problem); aftermath consequences are moderate-to-high tractability.

| Component | Tractability | Default Treatment |
|-----------|--------------|-------------------|
| Window preconditions | Moderate | Structural reasoning |
| Resolution probabilities | Low | Uniform / entropy maximization |
| Aftermath per resolution | Moderate-High | Invest analytical effort here |

This means: don't agonize over resolution probability estimates. Use uniform distributions unless you have strong structural reasons for asymmetry. Put your effort into specifying what happens *given* each resolution.
```

### 2. Update "Key Insight" Box

Current:
> **Key Insight**: The same window can produce very different outcomes. "Taiwan crisis" is a window; resolution could be war, peaceful accommodation, or status quo. These aren't three separate events—they're three resolutions of one contingent situation.

Proposed addition:
> **Calibration Insight**: Resolution probabilities are inherently difficult to estimate (see [[methodology/concepts/small-n-actor-problem]]). Default to uniform distribution across plausible resolutions; deviation requires explicit structural justification. The value of Type 3 modeling comes from specifying *what follows* each resolution, not from estimating *which* resolution occurs.

### 3. Add Cross-References

Add to Related Documents section:
- [[methodology/reference/type-3-calibration]] — Operational guidance for Type 3 specification
- [[methodology/concepts/tractability-boundaries]] — What is/isn't tractable
- [[methodology/concepts/entropy-maximization]] — Default principle for uncalibrated parameters
- [[methodology/concepts/small-n-actor-problem]] — Why resolution probabilities resist estimation

### 4. Update Common Mistakes Table

Add row:
| Investing effort in resolution probability estimation | Accept uniform default; invest in aftermath specification instead |

---

## Dependencies

- Complete [[methodology/reference/type-3-calibration]] first (Task 1.1)
- Then apply these updates (Task 1.2)

The calibration guidance document provides the full rationale; causal-types just needs to reference it and incorporate the key framing.

---

## Validation

After updates, the causal-types document should:
- [ ] Reference type-3-calibration for operational guidance
- [ ] Include tractability framing in Type 3 section
- [ ] Link to epistemology concept notes
- [ ] Update common mistakes table
- [ ] Maintain consistency with existing Type 1/2/4 sections

---

*Stub created: December 2025*
*To be applied as Task 1.2 after Task 1.1 completion*