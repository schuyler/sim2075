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

- [[methodology/reference/factor-correlation-matrix]] — Factor Ω specification
- [[methodology/reference/factor-loadings]] — Factor loading guidance
- [[methodology/project/tasks]] — Task tracking

---

*Analysis performed using Python numpy/pandas on sample of 11 events. Full analysis pending complete event catalog.*
