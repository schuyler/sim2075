---
title: validation-event-correlations
type: note
permalink: methodology/project/validation-event-correlations
tags:
- methodology
- validation
- correlation
- factor-model
- phase-2-blocker
---

# Event Correlation Validation Analysis

**Date**: December 30, 2025
**Status**: Issues identified — recommendations pending review
**Tasks**: 3.1 (implied correlations), 3.2 (double-counting), 3.3 (historical proxy analysis partial)

---

## Summary

Computed implied event correlation matrix from factor loadings and factor correlation matrix (Ω) for 11 events. Analysis reveals **significant structural issues** requiring resolution before Phase 2 implementation.

---

## Key Findings

### 1. Excessive Event Correlations

Multiple event pairs have correlations approaching 1.0, implying near-redundancy:

| Event 1 | Event 2 | Implied ρ |
|---------|---------|-----------|
| Global Financial Crisis | Dollar Reserve Crisis | 0.98 |
| AMOC Weakening | Permafrost Methane | 0.98 |
| Dollar Reserve Crisis | Chinese Economic Crisis | 0.96 |
| Global Financial Crisis | Chinese Economic Crisis | 0.96 |
| AMOC Weakening | Amazon Tipping Point | 0.94 |

**Assessment**: These correlations imply events will nearly always co-occur, effectively collapsing multiple events into single clusters:
- **Climate Cluster**: AMOC, Amazon, Permafrost (ρ = 0.93-0.98)
- **Financial Cluster**: GFC, Dollar Crisis, China Crisis (ρ = 0.96-0.98)

### 2. Double-Counting Inflation

Events correlate through multiple simultaneous pathways:
- **Direct**: Shared factor loadings (e.g., both load on F_CLIM)
- **Indirect**: Correlated factor paths (e.g., F_CLIM↔F_FOOD adds correlation)

The combination produces higher correlation than either pathway alone.

### 3. Loading Constraint Violations

Two events exceed sum-of-squared-loadings ≤1:

| Event | Sum Sq. Loadings | Status |
|-------|------------------|--------|
| Taiwan Conflict | 1.19 | ⚠️ Violation |
| Pakistan State Failure | 1.01 | ⚠️ Borderline |

### 4. Mean Correlation Too High

| Statistic | Value |
|-----------|-------|
| Mean correlation | 0.52 |
| Correlations >0.5 | 51% of pairs |
| Correlations >0.3 | 71% of pairs |

Expected for distinct events: mean 0.15-0.25, most pairs <0.3.

---

## Root Causes

1. **High factor loadings**: Events load heavily on dominant factors (F_CLIM ≥0.70, F_FIN ≥0.70)
2. **Factor correlation compounding**: Ω correlations (e.g., F_CLIM↔F_FOOD = 0.50) add to shared loading effects
3. **No residual variance**: Current model is Σ = ΛΩΛᵀ without independent error terms

---

## Proposed Solutions

> **Note**: The original proposed solutions (A: reduce loadings uniformly, B: reduce Ω correlations, C: add residual variance, D: event consolidation) were superseded by a principled framework. See **Critical Correction** section below and [[methodology/reference/variance-allocation]] for the final approach.

The key insight was that idiosyncratic variance should vary by causal type, not be uniform across all events. Type 3 events (like Taiwan) should have *higher* idiosyncratic variance than Type 2 events (like AMOC) because Type 3 resolution depends on intractable small-N actor decisions.

---

## Specific Recommendations

> **Superseded**: See [[methodology/reference/variance-allocation]] for type-based recommendations.

The original specific recommendations for climate tipping points, financial events, and Taiwan were superseded by the variance allocation framework which provides principled, type-specific guidance rather than ad-hoc adjustments.

---

## Validation Targets

After implementing type-based variance allocation, verify:

1. All (ΛΩΛᵀ)ᵢᵢ ≤ 1.0 (no negative idiosyncratic variance)
2. All (ΛΩΛᵀ)ᵢᵢ ≈ type-specific target (within ±0.05):
   - Type 1: 0.70–0.80
   - Type 2: 0.60–0.70
   - Type 3: 0.40–0.50
   - Type 4: 0.50–0.60
3. Type 3 events have lower factor-explained variance than Type 1/2
4. Resulting correlation matrix is positive semi-definite
5. No event pairs have correlation > 0.80 unless genuinely coupled
6. Mean correlation 0.15–0.35 (reasonable differentiation)

---

## Status

- [x] Task 3.1: Compute implied correlations — **Complete**
- [x] Task 3.2: Identify double-counting — **Complete**
- [ ] Task 3.3: Historical proxy analysis — **Deferred** (requires observable proxy data)
- [x] Task 3.6: Create variance allocation framework — **Complete** ([[methodology/reference/variance-allocation]])
- [x] Task 3.7-3.9: Update methodology docs with framework — **Complete**
- [x] Task 3.10: Revise validation notes — **Complete** (this document)
- [ ] Task 3.11: Implement across all events — **Pending**
- [ ] Re-validate — **Blocked on 3.11**

---

## Related Documents

- [[methodology/project/validation-findings-report]] — Detailed analysis with recommendations
- [[methodology/project/validation-correlation-matrix-data]] — Raw correlation matrices and loadings
- [[methodology/reference/factor-correlation-matrix]] — Factor Ω specification
- [[methodology/reference/factor-loadings]] — Factor loading guidance
- [[methodology/project/tasks]] — Task tracking

---

*Analysis performed using Python numpy/pandas on sample of 11 events. Full analysis pending complete event catalog.*


---

## Methodological Clarification (Added December 30, 2025)

### The Correlation Calculation Error

The initial analysis computed correlations by normalizing factor covariances:

```
ρᵢⱼ = (ΛΩΛᵀ)ᵢⱼ / √[(ΛΩΛᵀ)ᵢᵢ × (ΛΩΛᵀ)ⱼⱼ]
```

This answers: *"How correlated are the factor components of events?"*

But this **ignores idiosyncratic variance**—the event-specific randomness that factors don't explain. The standard factor model is:

```
Σ = ΛΩΛᵀ + Ψ
```

Where Ψ is the diagonal matrix of idiosyncratic (event-specific) variance.

### What the Correlation Should Be

If we assume events have unit total variance (standard for latent variables):
- Factor-explained variance: (ΛΩΛᵀ)ᵢᵢ
- Idiosyncratic variance: ψᵢᵢ = 1 − (ΛΩΛᵀ)ᵢᵢ
- Total variance: 1

The **true correlation** is then simply:

```
ρᵢⱼ = (ΛΩΛᵀ)ᵢⱼ
```

Because when total variance = 1, covariance equals correlation.

### Why the Initial Calculation Overstated Correlations

Dividing by √[(ΛΩΛᵀ)ᵢᵢ × (ΛΩΛᵀ)ⱼⱼ] (which is typically < 1) inflates the result.

**Example:**
- Factor covariance: 0.60
- Factor-explained variances: 0.80 and 0.75
- Initial calculation: 0.60 / √(0.60) = 0.78 ← **overstated**
- True correlation: 0.60 ← **correct**

### The Real Problem: SSL > 1

Two events have factor-explained variance exceeding 100%:
- **Taiwan Conflict**: SSL = 1.19
- **Pakistan State Failure**: SSL = 1.01

This implies **negative idiosyncratic variance**, which is mathematically impossible. These loadings must be reduced regardless of how we interpret correlations.

### Interpretation of Idiosyncratic Variance

What does Ψ represent substantively? It captures:

1. **Threshold dynamics unique to each event** — The specific pressure level that triggers AMOC collapse vs. Pakistan state failure vs. a pandemic involves event-specific uncertainties not captured by shared factors.

2. **Trigger-specific conditions** — Even when factors are elevated, specific triggering events (a particular policy decision, a specific pathogen mutation, a particular market panic) involve irreducible randomness.

3. **Timing uncertainty** — Factors may explain *whether* conditions are ripe for an event, but not precisely *when* within a given period it fires.

4. **Specification error** — Our factor structure is an approximation; Ψ absorbs what we haven't modeled.

### Revised Conclusions

1. **The 0.98 correlations are overstated.** True correlations are the raw factor covariances, which are substantially lower.

2. **SSL > 1 remains a hard constraint violation.** Taiwan and Pakistan loadings must be reduced because negative variance is impossible.

3. **After proper accounting**, the correlation structure may be acceptable, though some high correlations may still warrant review.

### Recommendation Update

**Primary fix**: Reduce loadings for Taiwan (target SSL ≤ 0.70) and Pakistan (target SSL ≤ 0.85).

**Secondary**: Re-run correlation analysis using the correct formula (raw factor covariances) to assess whether further adjustments are needed.

**Tertiary**: If any correlations remain above ~0.70 after correction, evaluate whether those event pairs should be differentiated further or whether high correlation is substantively appropriate.


---

## Critical Correction (December 30, 2025)

### The Initial Analysis Was Wrong

The initial analysis computed "sum of squared loadings" as Σⱼλᵢⱼ². But this is only correct when factors are **uncorrelated**.

When factors have non-zero correlations (our Ω matrix), the true factor-explained variance is **(ΛΩΛᵀ)ᵢᵢ**, which includes cross-terms. These cross-terms **add variance** when factors are positively correlated.

### The Problem Is Systemic

**8 out of 11 events** have factor-explained variance exceeding 1.0:

| Event | Simple SSL | True (ΛΩΛᵀ)ᵢᵢ | Status |
|-------|-----------|--------------|--------|
| Taiwan Conflict | 1.19 | **2.04** | Severe |
| Pakistan State Failure | 1.01 | **1.74** | Severe |
| Global Financial Crisis | 0.88 | **1.48** | Severe |
| Dollar Reserve Crisis | 0.78 | **1.39** | Severe |
| Chinese Economic Crisis | 0.66 | **1.20** | Violation |
| Amazon Tipping Point | 0.77 | **1.11** | Violation |
| Oil Supply Shock | 0.64 | **1.07** | Violation |
| AMOC Weakening | 0.80 | **1.05** | Violation |
| Severe Pandemic | 0.68 | 0.95 | OK |
| Permafrost Methane | 0.76 | 0.88 | OK |
| Fusion Commercialization | 0.65 | 0.86 | OK |

### Why This Matters

When factor-explained variance > 1:
- Idiosyncratic variance (Ψ) would be negative (impossible)
- Computed correlations exceed 1.0 (meaningless)
- The covariance structure is mathematically invalid
- Simulation results would be unreliable

### Root Cause

The combination of:
1. **High loadings on dominant factors**: F_CLIM at 0.85, F_FIN at 0.80, F_EAS at 0.80
2. **Significant factor correlations**: F_GPT↔F_EAS = 0.55, F_CLIM↔F_FOOD = 0.50, F_FIN↔F_EUR = 0.40

The cross-terms (λᵢₖ × λᵢₗ × Ωₖₗ for k≠l) accumulate and push total factor-explained variance above 1.

### Corrected Recommendation: Type-Based Variance Allocation

The earlier recommendations (uniform scaling to 1.0, or to 0.70) were superseded by a principled framework based on causal type epistemology.

**Key Insight**: Different causal types have different epistemologies. Idiosyncratic variance should reflect what factors *can* explain for each type:

| Type | Target (ΛΩΛᵀ)ᵢᵢ | Idiosyncratic | Rationale |
|------|-----------------|---------------|-----------|
| Type 1 | 0.70–0.80 | 0.20–0.30 | Large-N averaging; base rates meaningful |
| Type 2 | 0.60–0.70 | 0.30–0.40 | Observable pressure; threshold uncertainty |
| Type 3 | 0.40–0.50 | 0.50–0.60 | Factors explain windows; resolution intractable |
| Type 4 | 0.50–0.60 | 0.40–0.50 | Partly structural, partly serendipitous |

**Why Type 3 gets lowest factor-explained variance**: The [[methodology/concepts/small-n-actor-problem]] established that Type 3 resolution probabilities are epistemically intractable—small-N actor decisions cannot be estimated from historical data or structural reasoning. This intractability means factors can explain *why crisis windows open*, but not *how resolutions occur*. The 50-60% idiosyncratic variance represents "the part we can't predict."

**Example**: Taiwan Conflict (Type 3)
- Current (ΛΩΛᵀ)ᵢᵢ = 2.04
- Target = 0.45 (Type 3 midpoint)
- Scale factor = √(0.45 / 2.04) = 0.47
- Scaled loadings: F_EAS 0.38, F_GPT 0.33, F_FIN 0.09, F_TECH 0.07
- Interpretation: "East Asian dynamics and great power tension explain ~45% of Taiwan conflict probability; the other 55% is Xi's specific decision calculus—irreducibly uncertain."

**Contrast**: AMOC Weakening (Type 2)
- Current (ΛΩΛᵀ)ᵢᵢ = 1.05
- Target = 0.65 (Type 2 midpoint)
- Scale factor = √(0.65 / 1.05) = 0.79
- Scaled loadings: F_CLIM 0.67, F_FOOD 0.16, F_EUR 0.12, F_SSA 0.08, F_LAM 0.04
- Interpretation: "Climate stress explains ~65% of AMOC collapse probability; the other 35% is threshold uncertainty—we don't know exactly where the tipping point is."

AMOC retains higher loadings than Taiwan because factors genuinely explain more for Type 2 events.

**Full Framework**: See [[methodology/reference/variance-allocation]] for:
- Detailed epistemological justification
- Mathematical derivation
- Complete worked examples
- Implementation workflow
- Validation checks

### Implementation Priority

This is a **Phase 2 blocker**. The current factor structure cannot produce valid correlation matrices. Before any simulation code:

1. ~~Choose solution approach~~ → **Resolved**: Type-based variance allocation
2. Compute scale factors for all 28 events by causal type (Task 3.11)
3. Update event specifications with scaled loadings
4. Re-run validation to confirm (ΛΩΛᵀ)ᵢᵢ ≤ target for all events
5. Verify resulting correlation matrix is positive semi-definite
6. Document changes in event changelogs
