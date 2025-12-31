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

### Solution A: Reduce Factor Loadings (Recommended)

Rescale loadings so sum-of-squared-loadings ≤0.70:
- Taiwan Conflict: Scale all loadings by 0.7× → SSL = 0.58
- All climate events: Cap F_CLIM loading at 0.50
- All financial events: Cap F_FIN loading at 0.50

### Solution B: Reduce Factor Correlations

Lower Ω values for problematic pairs:
- F_CLIM↔F_FOOD: 0.50 → 0.30
- F_GPT↔F_EAS: 0.55 → 0.35
- F_FIN↔F_EUR: 0.40 → 0.25

### Solution C: Introduce Residual Variance

Add diagonal Ψ to correlation model:
```
Σ = ΛΩΛᵀ + Ψ
```
Where ψᵢᵢ = 1 - Σⱼλᵢⱼ² ensures events retain independent variation.

### Solution D: Event Consolidation

Consider merging highly-correlated events:
- Climate tipping points → single "Climate Cascade" event with branches
- Financial crises → retain separate but reduce correlation through loading rescaling

---

## Specific Recommendations

### Climate Tipping Points

**Recommended**: Model as single "Climate Tipping Cascade" event OR reduce F_CLIM loadings to ≤0.50

**Rationale**: Events ARE genuinely correlated through shared climate forcing, but modeling three near-redundant events inflates climate importance unrealistically.

### Financial Events

**Recommended**: Reduce all F_FIN loadings by 30% and reduce F_FIN correlations with other factors

**Rationale**: Events are conceptually distinct (global credit vs. reserve currency vs. China-specific). Excessive correlation is methodological artifact.

### Taiwan Conflict

**Recommended**: Reduce F_EAS 0.80→0.60, F_GPT 0.70→0.50
- New SSL: 0.67 (acceptable)

---

## Validation Targets

After implementing fixes, verify:

1. All sum-of-squared-loadings < 1.0 (preferably <0.8)
2. Mean correlation 0.25-0.35
3. Maximum correlation <0.75 except genuinely coupled events
4. Ω remains positive semi-definite
5. Factor structure still captures intended relationships

---

## Status

- [x] Task 3.1: Compute implied correlations — **Complete**
- [x] Task 3.2: Identify double-counting — **Complete**
- [ ] Task 3.3: Historical proxy analysis — **Deferred** (requires observable proxy data)
- [ ] Implement solutions — **Pending decision**
- [ ] Re-validate — **Blocked on implementation**

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

### Corrected Recommendation

**Option A: Per-Event Scaling (Recommended)**

Scale each event's loadings by 1/√(ΛΩΛᵀ)ᵢᵢ to achieve unit factor-explained variance:

| Event | Current (ΛΩΛᵀ)ᵢᵢ | Scale Factor | Result |
|-------|-----------------|--------------|--------|
| Taiwan | 2.04 | 0.70 | 1.00 |
| Pakistan | 1.74 | 0.76 | 1.00 |
| GFC | 1.48 | 0.82 | 1.00 |
| Dollar | 1.39 | 0.85 | 1.00 |
| China | 1.20 | 0.91 | 1.00 |
| Amazon | 1.11 | 0.95 | 1.00 |
| Oil | 1.07 | 0.97 | 1.00 |
| AMOC | 1.05 | 0.98 | 1.00 |

This preserves the relative loading structure within each event while ensuring mathematical validity.

**Option B: Reduce Factor Correlations**

Lower Ω entries to reduce cross-term amplification:
- F_GPT↔F_EAS: 0.55 → 0.35
- F_CLIM↔F_FOOD: 0.50 → 0.30
- F_FIN↔F_EUR: 0.40 → 0.25

Would require re-justifying the reduced correlations.

**Option C: Combination**

Modest reduction in both loadings and Ω values. May be most defensible—acknowledges uncertainty in both.

### Implementation Priority

This is a **Phase 2 blocker**. The current factor structure cannot produce valid correlation matrices. Before any simulation code:

1. Choose solution approach (A, B, or C)
2. Compute revised loadings or Ω values
3. Verify (ΛΩΛᵀ)ᵢᵢ ≤ 1.0 for all events
4. Verify resulting correlation matrix is positive semi-definite
5. Update event specifications with corrected loadings
