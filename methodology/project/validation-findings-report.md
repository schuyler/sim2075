---
title: validation-findings-report
type: note
permalink: methodology/project/validation-findings-report
tags:
- validation
- findings
- recommendations
- phase-2-blocker
---

# Event Correlation Validation: Detailed Findings Report

> ⚠️ **Partially Superseded**: The problem identification in this document remains valid, but the "Proposed Solutions" and "Specific Recommendations" sections have been superseded by the [[methodology/reference/variance-allocation]] framework. The key insight: idiosyncratic variance should vary by causal type, not be uniform. See [[methodology/project/validation-event-correlations]] for the corrected recommendations.

**Date**: December 30, 2025
**Status**: Problem identification valid; recommendations superseded
**Tasks**: 3.1, 3.2 (complete), 3.3 (partial)

---

## Executive Summary

Analysis of the implied event correlation matrix reveals **significant structural issues** that should be addressed before Phase 2 implementation:

1. **Excessive event correlations**: Multiple event pairs have correlations >0.9, implying they are nearly redundant
2. **Double-counting inflation**: Events that load on multiple shared factors AND correlated factor paths accumulate excessive correlation
3. **Loading constraint violations**: Two events exceed the sum-of-squared-loadings ≤1 guideline
4. **Mean correlation too high**: Average correlation of 0.52 suggests events are insufficiently differentiated

These issues affect the validity of the factor model structure and would produce unrealistic simulation behavior.

---

## Issue 1: Excessive Event Correlations

### Most Problematic Pairs

| Event 1 | Event 2 | Implied ρ | Assessment |
|---------|---------|-----------|------------|
| Global Financial Crisis | Dollar Reserve Crisis | 0.98 | **Severe** — near-redundant |
| AMOC Weakening | Permafrost Methane | 0.98 | **Severe** — climate tipping points overly coupled |
| Dollar Reserve Crisis | Chinese Economic Crisis | 0.96 | **Severe** — financial events near-redundant |
| Global Financial Crisis | Chinese Economic Crisis | 0.96 | **Severe** — financial events near-redundant |
| AMOC Weakening | Amazon Tipping Point | 0.94 | **Significant** — climate tipping points |
| Amazon Tipping Point | Permafrost Methane | 0.93 | **Significant** — climate tipping points |
| Taiwan Conflict | Chinese Economic Crisis | 0.89 | Moderate — plausible connection |

### Interpretation

Correlations above 0.85 imply events will nearly always co-occur or co-not-occur. This effectively collapses multiple events into a single cluster:

- **Climate Cluster**: AMOC, Amazon, Permafrost all fire together (ρ = 0.93-0.98)
- **Financial Cluster**: GFC, Dollar Crisis, China Crisis all fire together (ρ = 0.96-0.98)

This defeats the purpose of modeling them as separate events.

### Root Cause

The correlation structure arises from:
1. **High loadings on same factors**: All climate events load heavily on F_CLIM; all financial events load heavily on F_FIN
2. **Factor correlations compound**: F_CLIM↔F_FOOD (0.50) adds correlation to events that already share F_CLIM
3. **No residual variance**: The Σ = ΛΩΛᵀ calculation doesn't include independent error terms

---

## Issue 2: Double-Counting Inflation

Events correlate through multiple simultaneous pathways, causing correlation inflation.

### Example: AMOC ↔ Amazon

**Direct pathway (shared factors)**:
- Both load on F_CLIM (0.85 × 0.70 = 0.595 contribution)
- Both load on F_FOOD (0.20 × 0.45 = 0.090 contribution)

**Indirect pathway (correlated factors)**:
- AMOC loads on F_CLIM, Amazon loads on F_FOOD, and F_CLIM↔F_FOOD = 0.50
- This adds additional covariance beyond the shared loadings

The combination produces ρ = 0.94, higher than either pathway alone would produce.

### Example: GFC ↔ Dollar Crisis

**Shared factors**:
- F_FIN: 0.80 × 0.70 = 0.56
- F_GPT: 0.30 × 0.40 = 0.12
- F_EUR: 0.20 × 0.20 = 0.04
- F_EAS: 0.25 × 0.20 = 0.05

**Correlated factor paths**:
- F_FIN↔F_GPT (0.25) adds: 0.80 × 0.25 × 0.40 = 0.08
- F_FIN↔F_EUR (0.40) adds: 0.80 × 0.40 × 0.20 = 0.064
- Multiple smaller paths

The compounding produces ρ = 0.98.

---

## Issue 3: Loading Constraint Violations

Two events exceed sum-of-squared-loadings ≤1:

| Event | Sum of Sq. Loadings | Excess |
|-------|---------------------|--------|
| Taiwan Conflict | 1.19 | +0.19 |
| Pakistan State Failure | 1.01 | +0.01 |

### Taiwan Conflict Breakdown
- F_EAS: 0.80² = 0.64
- F_GPT: 0.70² = 0.49
- F_FIN: 0.20² = 0.04
- F_TECH: 0.15² = 0.02
- **Total: 1.19**

The high loadings on both F_EAS and F_GPT, combined with ρ(F_GPT↔F_EAS) = 0.55, produce excessive factor-explained variance.

### Interpretation

When sum of squared loadings >1, the factor model implies the event has more than 100% of its variance explained by factors—a mathematical impossibility that indicates misspecification.

---

## Issue 4: Mean Correlation Too High

| Statistic | Value | Assessment |
|-----------|-------|------------|
| Mean correlation | 0.52 | Too high |
| Correlations >0.5 | 28/55 (51%) | Majority |
| Correlations >0.3 | 39/55 (71%) | Nearly all |
| Correlations <0.2 | 3/55 (5%) | Very few |

For a portfolio of 11 genuinely distinct discontinuity events, we would expect most correlations to be in the 0.1-0.3 range, with occasional higher values for related events.

The current structure implies that when "something bad happens," almost everything bad happens together—an implausibly tight coupling.

---

## Proposed Solutions

### Solution A: Reduce Factor Loadings (Recommended)

Rescale loadings so that sum-of-squared-loadings stays below ~0.6 for most events:

**Current vs. Proposed for Taiwan Conflict:**

| Factor | Current | Proposed (0.7× scale) |
|--------|---------|----------------------|
| F_EAS | 0.80 | 0.56 |
| F_GPT | 0.70 | 0.49 |
| F_FIN | 0.20 | 0.14 |
| F_TECH | 0.15 | 0.11 |
| **Sum sq.** | **1.19** | **0.58** |

This preserves the relative structure while reducing excessive correlation.

### Solution B: Reduce Factor Correlations

Lower correlations in Ω for the most problematic pairs:

| Factor Pair | Current ρ | Proposed ρ |
|-------------|-----------|------------|
| F_CLIM↔F_FOOD | 0.50 | 0.30 |
| F_GPT↔F_EAS | 0.55 | 0.35 |
| F_FIN↔F_EUR | 0.40 | 0.25 |

This requires re-validating the PSD property of Ω after changes.

### Solution C: Introduce Residual Variance

Modify the correlation model to include event-specific residual variance:

```
Σ = ΛΩΛᵀ + Ψ
```

Where Ψ is diagonal with ψᵢᵢ = 1 - Σⱼλᵢⱼ² (residual unexplained variance).

This ensures events retain independent variation even when factor correlations are high.

### Solution D: Event Differentiation Review

Review whether overly-correlated events should be:
1. **Merged**: Combined into a single event with severity branches
2. **Causally linked**: One triggers the other rather than correlated occurrence
3. **Factor-differentiated**: Given more distinct factor loading profiles

---

## Specific Recommendations

### 1. Climate Tipping Points (AMOC, Amazon, Permafrost)

**Problem**: ρ = 0.93-0.98 between all three

**Options**:
- **Option A (Recommended)**: Model as single "Climate Tipping Cascade" event with branches for which tipping points are crossed
- **Option B**: Reduce F_CLIM loadings to ~0.50 for all three, accepting lower factor explanation
- **Option C**: Introduce causal chains (AMOC triggers Permafrost) rather than correlation

**Rationale for Option A**: In reality, these events ARE highly correlated through shared climate forcing. But modeling three nearly-redundant events inflates the importance of climate tipping points in the simulation. A single event with branches better represents the structural uncertainty.

### 2. Financial Events (GFC, Dollar Crisis, China Crisis)

**Problem**: ρ = 0.96-0.98 between all three

**Options**:
- **Option A (Recommended)**: Reduce all F_FIN loadings by ~30% and reduce F_FIN correlations with other factors
- **Option B**: Model "Major Financial Crisis" as single event with regional/type branches
- **Option C**: Introduce explicit cascade triggers (GFC → China Crisis, etc.)

**Rationale for Option A**: These events are conceptually distinct (global credit, reserve currency, China-specific). The excessive correlation comes from methodological over-specification, not genuine redundancy.

### 3. Taiwan Conflict

**Problem**: Sum of squared loadings = 1.19

**Recommendation**: Reduce F_EAS loading from 0.80 to 0.60 and F_GPT from 0.70 to 0.50:
- New sum of squared loadings: 0.36 + 0.25 + 0.04 + 0.02 = 0.67
- Still captures the key drivers without mathematical impossibility

### 4. Pakistan State Failure

**Problem**: Sum of squared loadings = 1.01 (borderline)

**Recommendation**: Reduce F_SAS from 0.71 to 0.60 and F_FOOD from 0.42 to 0.35:
- New sum of squared loadings: 0.36 + 0.12 + 0.14 + 0.08 + ... ≈ 0.85
- Acceptable level

---

## Validation After Fixes

After implementing solutions, verify:

1. **No sum-of-squared-loadings >1**: All events should have SSL < 1.0, preferably < 0.8
2. **Reduced mean correlation**: Target 0.25-0.35 for typical event pairs
3. **Reduced maximum correlation**: No pairs above 0.75 except where genuinely coupled
4. **Maintained factor structure**: Factor loadings still capture the intended causal relationships
5. **PSD property preserved**: Ω remains positive semi-definite after any modifications

---

## Next Steps

> **Status**: Steps 1-5 complete; Step 6 pending Task 3.11.

1. ~~Review findings with stakeholder~~ — **Complete**
2. ~~Select solution approach~~ — **Complete**: Type-based variance allocation framework
3. ~~Implement fixes to methodology docs~~ — **Complete**: Tasks 3.6-3.10
4. Implement variance allocation across all 28 events — **Pending** (Task 3.11)
5. Re-run validation — **Blocked on Task 3.11**
6. Proceed to Phase 2 — **Blocked on validation**

See [[methodology/reference/variance-allocation]] for the resolution framework.

---

## Related Documents

- [[methodology/project/validation-event-correlations]] — Summary note
- [[methodology/project/validation-correlation-matrix-data]] — Raw data tables
- [[methodology/reference/factor-correlation-matrix]] — Factor Ω specification
- [[methodology/reference/factor-loadings]] — Factor loading guidance
