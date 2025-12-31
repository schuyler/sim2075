---
title: variance-allocation
type: note
permalink: methodology/reference/variance-allocation
tags:
- methodology
- reference
- variance
- factor-model
- epistemology
- causal-types
---

# Variance Allocation Framework

**Purpose**: Specifies how much of each event's variance should be explained by factors vs. idiosyncratic (event-specific) randomness, based on the event's causal type.

**Key Insight**: Different causal types have different epistemologies. Factors can explain more for events that aggregate across large-N processes (Type 1) than for events that depend on intractable small-N actor decisions (Type 3). The variance allocation should reflect what factors *can* explain, not just produce mathematically valid correlations.

---

## The Epistemological Foundation

### What Factors Explain

Factor loadings capture: *"When this latent stress factor is elevated, this event is more likely."*

But the strength of this relationship varies by causal type:

**Type 1 (Stochastic)**: Factors explain *shared vulnerability*. A pandemic is more likely when health systems are stressed (F_HLTH elevated). Because Type 1 events aggregate across many potential trigger points (billions of human-animal interactions for pandemic emergence), individual idiosyncrasies average out. Historical base rates are meaningful. Factors can explain most of the variance in occurrence probability.

**Type 2 (Threshold)**: Factors explain *pressure accumulation*. AMOC collapse is more likely when climate stress is elevated (F_CLIM elevated) because that correlates with faster freshwater input. The pressure process is observable or structurally constrained—it's physics, not actor choice. Factors explain a substantial portion of variance, but threshold uncertainty adds irreducible randomness.

**Type 3 (Contingent)**: Factors explain *why crisis windows open*, but resolution depends on small-N actor decisions that are epistemically intractable. Xi Jinping's specific decision calculus in a Taiwan crisis is not a random draw from a distribution we can estimate. The factors set the stage; the resolution is irreducibly uncertain from our epistemic standpoint. Factors explain less of the variance—the idiosyncratic component is large.

**Type 4 (Breakthrough)**: Factors explain *enabling conditions* for technological breakthroughs. Progress is partly structural (funding, prior knowledge, talent concentration) and partly serendipitous (which specific insight occurs when). Intermediate variance allocation.

### The Small-N Actor Problem (Type 3)

This framework operationalizes the insight from [[methodology/concepts/small-n-actor-problem]]:

> When outcomes depend on the decisions of 1-5 specific people in a specific context, there is no meaningful sense in which we can estimate "the probability" of their choice.

For Type 3 events, we've already acknowledged that resolution probabilities should default to uniform (entropy maximization) because we lack grounds for confident differentiation. The variance allocation extends this logic: **if we can't estimate resolution probabilities, factors can't explain resolution—only window opening.**

A Taiwan crisis (Type 3) loads on F_GPT and F_EAS because great power tension and regional dynamics create crisis windows. But whether Xi decides to invade, and whether the US decides to intervene, are small-N actor decisions. The factor structure explains maybe 40-50% of "does Taiwan conflict occur"—the rest is irreducibly uncertain.

Contrast with AMOC collapse (Type 2): climate stress explains most of the variance in whether the threshold is approached. The remaining uncertainty is about threshold location, not actor decisions. Factor-explained variance can be 60-70%.

---

## Type-Specific Variance Targets

| Causal Type | Target Factor-Explained Variance | Idiosyncratic Variance | Rationale |
|-------------|----------------------------------|------------------------|-----------|
| **Type 1** (Stochastic) | **0.70 – 0.80** | 0.20 – 0.30 | Large-N averaging; base rates meaningful; factors explain shared vulnerability |
| **Type 2** (Threshold) | **0.60 – 0.70** | 0.30 – 0.40 | Pressure observable; threshold uncertain but structurally constrained |
| **Type 3** (Contingent) | **0.40 – 0.50** | 0.50 – 0.60 | Factors explain windows; resolution intractable; small-N actor decisions |
| **Type 4** (Breakthrough) | **0.50 – 0.60** | 0.40 – 0.50 | Partly structural (enabling conditions), partly serendipitous (which insight, when) |

### Guidance on Range Selection

**Use the higher end of the range when:**
- Event has strong structural drivers with clear mechanisms
- Historical data provides calibration for factor relationships
- Pressure/vulnerability processes are observable

**Use the lower end of the range when:**
- Event has multiple competing causal mechanisms
- Historical analogies are weak or contested
- Significant uncertainty about factor relationships

**Default**: Use the midpoint (0.75 for Type 1, 0.65 for Type 2, 0.45 for Type 3, 0.55 for Type 4) unless there's specific reason to deviate.

---

## The Mathematical Constraint

### The Full Factor Model

The event covariance structure is:

```
Σ = ΛΩΛᵀ + Ψ
```

Where:
- **Λ** = factor loading matrix (events × factors)
- **Ω** = factor correlation matrix (factors × factors)
- **ΛΩΛᵀ** = factor-explained covariance
- **Ψ** = diagonal matrix of idiosyncratic variances

### The Constraint

For event *i*, total variance is normalized to 1:

```
Var(eventᵢ) = (ΛΩΛᵀ)ᵢᵢ + ψᵢᵢ = 1
```

Therefore:
- Factor-explained variance: **(ΛΩΛᵀ)ᵢᵢ**
- Idiosyncratic variance: **ψᵢᵢ = 1 − (ΛΩΛᵀ)ᵢᵢ**

**The target constraint**: (ΛΩΛᵀ)ᵢᵢ should equal the type-specific target.

### Why Simple Sum-of-Squared-Loadings Is Wrong

The simple calculation Σⱼλᵢⱼ² is only correct when factors are uncorrelated (Ω = I).

When factors have non-zero correlations, factor-explained variance includes cross-terms:

```
(ΛΩΛᵀ)ᵢᵢ = Σⱼλᵢⱼ² + 2·Σⱼ<ₖ λᵢⱼ·λᵢₖ·Ωⱼₖ
```

The cross-terms add variance when:
- Event loads on multiple factors (λᵢⱼ and λᵢₖ both non-zero)
- Those factors are positively correlated (Ωⱼₖ > 0)

**Example**: Taiwan Conflict loads on F_EAS (0.80) and F_GPT (0.70), and Ω(F_GPT, F_EAS) = 0.55.

- Simple sum-of-squares: 0.80² + 0.70² + ... = 1.19
- Cross-term contribution: 2 × 0.80 × 0.70 × 0.55 = 0.616
- True factor-explained variance: ~2.04

This is why Taiwan's current specification is invalid—factor-explained variance exceeds 100%.

---

## Computing Scale Factors

### The Problem

Current event specifications were written without variance targets. Many have (ΛΩΛᵀ)ᵢᵢ > 1 (mathematically impossible) or values inconsistent with their causal type.

### The Solution

For each event:

1. **Determine causal type** and target factor-explained variance (v_target)
2. **Compute current factor-explained variance**: v_current = (ΛΩΛᵀ)ᵢᵢ
3. **Compute scale factor**: s = √(v_target / v_current)
4. **Scale all loadings**: λ'ᵢⱼ = s × λᵢⱼ for all factors j
5. **Verify**: (Λ'ΩΛ'ᵀ)ᵢᵢ = v_target

### Worked Example: Taiwan Conflict (Type 3)

**Current loadings:**
| Factor | Loading |
|--------|---------|
| F_EAS | 0.80 |
| F_GPT | 0.70 |
| F_FIN | 0.20 |
| F_TECH | 0.15 |

**Current factor-explained variance**: (ΛΩΛᵀ)ᵢᵢ = 2.04

**Target** (Type 3, using midpoint): 0.45

**Scale factor**: s = √(0.45 / 2.04) = √0.221 = **0.47**

**Scaled loadings:**
| Factor | Original | Scaled |
|--------|----------|--------|
| F_EAS | 0.80 | 0.38 |
| F_GPT | 0.70 | 0.33 |
| F_FIN | 0.20 | 0.09 |
| F_TECH | 0.15 | 0.07 |

**Interpretation**: "East Asian dynamics and great power tension explain about 45% of Taiwan conflict occurrence probability. The other 55% is the intractable part—Xi's specific decision calculus, US credibility assessments, domestic political moments."

This is an epistemically honest statement that matches our acknowledgment in [[methodology/reference/type-3-calibration]] that resolution probabilities are intractable.

### Worked Example: AMOC Weakening (Type 2)

**Current loadings:**
| Factor | Loading |
|--------|---------|
| F_CLIM | 0.85 |
| F_FOOD | 0.20 |
| F_EUR | 0.15 |
| F_SSA | 0.10 |
| F_LAM | 0.05 |

**Current factor-explained variance**: (ΛΩΛᵀ)ᵢᵢ = 1.05

**Target** (Type 2, using midpoint): 0.65

**Scale factor**: s = √(0.65 / 1.05) = √0.619 = **0.79**

**Scaled loadings:**
| Factor | Original | Scaled |
|--------|----------|--------|
| F_CLIM | 0.85 | 0.67 |
| F_FOOD | 0.20 | 0.16 |
| F_EUR | 0.15 | 0.12 |
| F_SSA | 0.10 | 0.08 |
| F_LAM | 0.05 | 0.04 |

**Interpretation**: "Climate stress explains about 65% of AMOC collapse probability. The other 35% reflects threshold uncertainty—we don't know exactly where the tipping point is, and there's variability in freshwater input rates that factors don't fully capture."

AMOC retains higher loadings than Taiwan because factors genuinely explain more for Type 2 events—the pressure process is observable, the threshold is physically constrained.

---

## Scaling Preserves Relative Structure

A key property of this approach: **scaling preserves the relative importance of factors within each event**.

After scaling Taiwan:
- F_EAS is still the dominant factor (0.38 vs. 0.33 for F_GPT)
- The ratio F_EAS/F_GPT is preserved (0.80/0.70 = 0.38/0.33 ≈ 1.14)
- F_FIN and F_TECH remain minor contributors

What changes is the *total* factor explanation—from "factors explain everything" to "factors explain about half, the rest is intractable."

---

## Correlation Implications

### Event Correlations After Scaling

When loadings are scaled down, event correlations decrease. This is correct behavior.

**Before scaling**, Taiwan ↔ Chinese Economic Crisis had an implied correlation driven by shared F_EAS and F_FIN loadings plus factor correlations.

**After scaling**, this correlation decreases because:
- Both events now have substantial idiosyncratic variance
- The idiosyncratic components are uncorrelated by definition
- The factor-driven correlation is diluted by independent noise

**Interpretation**: Two Type 3 events occurring together still cluster somewhat (shared great power tension environment), but they're not near-deterministic—each has its own small-N actor decision component.

### Correlation Formula With Idiosyncratic Variance

The correlation between events i and j is:

```
ρᵢⱼ = (ΛΩΛᵀ)ᵢⱼ / √[(ΛΩΛᵀ)ᵢᵢ + ψᵢᵢ] × √[(ΛΩΛᵀ)ⱼⱼ + ψⱼⱼ]
```

With unit total variance (factor-explained + idiosyncratic = 1):

```
ρᵢⱼ = (ΛΩΛᵀ)ᵢⱼ
```

The factor covariance IS the correlation.

### Expected Correlation Ranges by Type Pairing

| Pairing | Expected Correlation Range | Rationale |
|---------|---------------------------|-----------|
| Type 1 ↔ Type 1 | 0.20 – 0.60 | High factor explanation both sides; correlation through shared factors |
| Type 2 ↔ Type 2 | 0.15 – 0.50 | Moderate factor explanation; threshold uncertainty adds independence |
| Type 3 ↔ Type 3 | 0.10 – 0.35 | Low factor explanation; small-N decisions are largely independent |
| Type 1 ↔ Type 3 | 0.10 – 0.40 | Asymmetric; Type 3's high idiosyncratic variance limits correlation |

These are rough expectations. Actual correlations depend on factor loading overlap and Ω structure.

---

## Event-Specific Overrides

### When to Deviate from Type Default

Some events may warrant variance allocation different from their type's default. Document any deviation with explicit rationale.

**Valid reasons for higher factor-explained variance:**
- Event is "anchor" for a regional factor (Pakistan for F_SAS, Taiwan for F_EAS)
- Structural constraints are unusually strong
- Observable leading indicators have strong predictive power

**Valid reasons for lower factor-explained variance:**
- Event depends on especially intractable actor decisions (even for Type 1/2)
- Mechanism is poorly understood
- Historical base rate is unreliable

### Documentation Requirement

```yaml
variance_allocation:
  target: 0.45  # Type 3 default
  override: 0.55  # Higher than default
  override_rationale: |
    Taiwan is the anchor event for F_EAS. Regional dynamics are
    unusually tightly coupled to Taiwan outcomes—more than other
    Type 3 events where small-N decisions are the dominant factor.
```

---

## Implementation Workflow

### For New Event Specifications

1. Determine causal type
2. Select target variance (type default or justified override)
3. Specify relative loadings (which factors matter, relative magnitudes)
4. Compute (ΛΩΛᵀ)ᵢᵢ for the relative loadings
5. Scale loadings so (ΛΩΛᵀ)ᵢᵢ = target
6. Document the scaled loadings and variance allocation

### For Existing Event Specifications

See Task 3.11: Implement variance allocation across all events.

1. Compute current (ΛΩΛᵀ)ᵢᵢ for all events
2. Group by causal type
3. Compute scale factors
4. Update event files with scaled loadings
5. Re-run validation
6. Document changes in changelogs

---

## Validation Checks

After implementing variance allocation:

- [ ] All events have (ΛΩΛᵀ)ᵢᵢ ≤ 1.0 (no negative idiosyncratic variance)
- [ ] All events have (ΛΩΛᵀ)ᵢᵢ ≈ type-specific target (within ±0.05)
- [ ] Type 3 events have lower factor-explained variance than Type 1/2 events
- [ ] Resulting correlation matrix is positive semi-definite
- [ ] No event pairs have correlation > 0.80 unless genuinely coupled
- [ ] Mean correlation is 0.15-0.35 (reasonable differentiation)

---

## Related Documents

### Epistemological Framework
- [[methodology/concepts/small-n-actor-problem]] — Why Type 3 resolution is intractable
- [[methodology/concepts/tractability-boundaries]] — What factors can/cannot explain
- [[methodology/concepts/entropy-maximization]] — Default for intractable parameters

### Operational References
- [[methodology/reference/causal-types]] — Type definitions and characteristics
- [[methodology/reference/factor-loadings]] — Loading specification guidance
- [[methodology/reference/type-3-calibration]] — Type 3 operational guidance
- [[methodology/reference/factor-correlation-matrix]] — The Ω matrix specification

### Validation
- [[methodology/project/validation-event-correlations]] — Problem identification
- [[methodology/project/validation-findings-report]] — Detailed findings

---

*Created: December 2025 (Task 3.6)*
