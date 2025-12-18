---
title: factor-correlation-structure
type: note
permalink: methodology/concepts/factor-correlation-structure
tags:
- methodology
- concepts
- correlation
- factors
- architecture
---

# Factor Correlation Structure

## The Design Question

The simulation's 12 latent factors drive event correlation through shared loadings. But should the factors themselves be correlated?

Three options:

1. **Independent factors** — F ~ N(0, I)
2. **Correlated factors** — F ~ N(0, Ω) where Ω is a correlation matrix
3. **Hierarchical meta-factors** — Factors load on higher-order constructs

This document explains why we chose Option 2.

---

## Option 1: Independent Factors (Status Quo)

The simplest approach assumes factors are uncorrelated:

```
F = [F_CLIM, F_FIN, ..., F_LAM] ~ N(0, I)
```

Event correlation emerges only from shared factor loadings. If AMOC collapse loads on F_CLIM (0.85) and Sahel catastrophe loads on F_CLIM (0.60), they correlate because both respond to the same climate factor.

**Advantages:**
- Simplest to implement and explain
- Fewer parameters to estimate
- Factor loadings carry full interpretive weight

**Limitations:**
- Misses factor-level co-movement
- Climate stress and food stress should co-occur (drought drives crop failure), but independent factors don't capture this
- Underestimates clustering in scenarios where multiple systemic factors are elevated simultaneously

---

## Option 2: Inter-Factor Correlation Matrix

Allow factors to correlate via a 12×12 matrix Ω:

```
F ~ N(0, Ω)
```

When F_CLIM is high, F_FOOD tends to be high too (if positively correlated in Ω). Event correlation becomes:

```
Σ_events = Λ Ω Λ' + Ψ
```

instead of:

```
Σ_events = Λ I Λ' + Ψ = Λ Λ' + Ψ
```

**Advantages:**
- Captures real-world factor co-movement (climate → food, tension → regional stress)
- Each correlation has explicit, documentable rationale
- Transparent — correlations are stated directly
- Mathematically straightforward extension of existing framework

**Limitations:**
- 66 additional parameters (12 × 11 / 2 unique correlations)
- Correlations are symmetric; can't represent "A drives B more than B drives A"
- Requires structured judgment for each correlation estimate

---

## Option 3: Hierarchical Meta-Factors

Add a layer above the 12 factors:

```
M = [M₁, M₂, ..., Mₘ] ~ N(0, I)       # m independent meta-factors
Fⱼ = Σₖ γⱼₖMₖ + ηⱼ                    # Factors load on meta-factors
```

Factor correlation emerges structurally from shared meta-factor loadings:

```
Corr(Fⱼ, Fₖ) = Σₘ γⱼₘ × γₖₘ
```

**When this works well:**
- Genuine higher-order constructs exist with clear interpretation
- The hierarchy is more parsimonious than direct correlation specification
- Empirical factor analysis has revealed hierarchical structure

**Why it doesn't fit our case:**

The correlations we care about are pairwise relationships with specific mechanisms:

| Correlation | Mechanism |
|-------------|-----------|
| F_CLIM ↔ F_FOOD | Drought drives crop failure |
| F_FIN ↔ regional factors | Financial contagion |
| F_GPT ↔ F_EAS | Great power tension centers on East Asia |
| F_CLIM ↔ F_SSA/F_SAS/F_MENA | Climate vulnerability in specific regions |

These don't reduce to a clean hierarchy. Candidate meta-factors like "Global Systemic Stress" or "Climate Cascade" have overlapping scope and don't isolate distinct mechanisms.

With 12 factors and ~4 meta-factors, we'd need ~48 meta-loadings — comparable to the 66 correlations in Option 2, but with added burden of justifying meta-factor definitions.

---

## Decision: Option 2

We adopt the inter-factor correlation matrix for these reasons:

1. **Transparency**: Each correlation is explicit and documented. No hidden structure.

2. **Mechanism-specific**: We can set Corr(F_CLIM, F_FOOD) = 0.5 because "climate stress drives food system stress" without also implying other correlations we don't intend.

3. **Parsimony in practice**: Most factor pairs have no strong theoretical relationship. We expect ~10-15 non-zero correlations, not 66. The matrix will be sparse.

4. **Compatible with existing framework**: The Gaussian copula machinery works identically; we just substitute Ω for I.

5. **Revisable**: If we later discover we overestimated or underestimated a correlation, we adjust one parameter. Meta-factor changes would propagate unpredictably.

---

## Specification Approach

The correlation matrix Ω will be developed in [[methodology/reference/factor-correlation-matrix]] with:

- Each non-zero correlation documented with mechanism
- Correlation magnitude estimated from structural reasoning
- Validation that Ω is positive semi-definite
- Sensitivity analysis on key correlations

Default: Correlations are zero unless there's explicit rationale for non-zero value.

---

## Relationship to Event Correlation

With factor correlation, two events can correlate even if they load on *different* factors, as long as those factors are correlated.

**Example without factor correlation:**
- AMOC collapse loads on F_CLIM (0.85)
- Global financial crisis loads on F_FIN (0.90)
- These events are nearly uncorrelated (only through minor cross-loadings)

**Example with factor correlation:**
- If Corr(F_CLIM, F_FIN) = 0.2 (climate disasters stress financial systems)
- AMOC collapse and financial crisis now have induced correlation
- A severe climate year is slightly more likely to also be a financial stress year

This better reflects reality: systemic stresses propagate across domains.

---

*See [[methodology/concepts/gaussian-copula]] for how factor correlation feeds into event sampling*

*See [[methodology/project/open-questions]] — Question 1 for the original problem statement*
