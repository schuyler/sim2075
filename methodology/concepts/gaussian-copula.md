---
title: gaussian-copula
type: note
permalink: methodology/concepts/gaussian-copula
tags:
- methodology
- concepts
- correlation
- copula
- sampling
- factor-model
---

# Gaussian Copula: Conceptual Foundation

## The Problem

The simulation needs to generate correlated binary events. Each event has its own probability (5%, 2%, 10%, etc.), but events should cluster—when one occurs, related events are more likely.

The naive approach draws independent random numbers for each event:

```python
if random() < 0.05: event_A = True
if random() < 0.02: event_B = True
```

This assumes independence. How do we introduce correlation while preserving each event's marginal probability?

---

## What a Copula Does

A copula separates two concerns:

1. **Marginal distributions**: Each variable's individual probability distribution
2. **Dependence structure**: How variables co-move

The copula handles dependence. It transforms independent uniform random variables into *correlated* uniform random variables, while preserving the property that each individual variable remains uniform on [0,1].

Once you have correlated uniforms, you compare each to its threshold—the correlation carries through to the binary outcomes.

---

## The Gaussian Copula Method

**Step 1: Draw correlated normals**

Generate a vector of standard normal variables with a specified correlation matrix:

```
Z = [Z₁, Z₂, ..., Zₙ] ~ N(0, Σ)
```

where Σ is an n×n correlation matrix. The Z values are correlated with each other.

**Step 2: Transform to uniform**

Apply the standard normal CDF (Φ) to each draw:

```
Uᵢ = Φ(Zᵢ)
```

This maps each value to [0,1]. Crucially, each Uᵢ is marginally uniform, but the U values inherit their correlation from Z.

**Step 3: Compare to thresholds**

```
event_i_occurs = (Uᵢ < pᵢ)
```

When Z₁ and Z₂ are positively correlated and both happen to be low, both U₁ and U₂ will be low, and both events trigger.

---

## Why "Gaussian"?

The multivariate normal distribution has convenient properties:

- **Fully specified by correlations**: The correlation matrix completely determines the dependence structure
- **Composable**: Factor models naturally produce Gaussian structure
- **Mathematically tractable**: Well-understood, easy to validate, guaranteed positive semi-definite matrices work

Other copulas exist (Clayton, Gumbel, t-copula) with different tail dependence properties, but Gaussian is standard for factor models and sufficient for our purposes.

---

## Connection to the Factor Model

The factor model is a structured way to build the correlation matrix Σ without specifying all pairwise correlations directly.

Instead of specifying Σ directly (which would require n(n-1)/2 parameters for n events), we define:

```
Zᵢ = λᵢ₁F₁ + λᵢ₂F₂ + ... + λᵢₖFₖ + εᵢ
```

where:
- Fⱼ are k latent factors (standard normals)
- λᵢⱼ is event i's loading on factor j
- εᵢ is idiosyncratic noise

The implied correlation between events i and j is:

```
Corr(Zᵢ, Zⱼ) = Σₖ λᵢₖ × λⱼₖ
```

Events correlate when they load on the same factors. With 75 events and 12 factors, this reduces parameters from 2,775 correlations to 900 loadings.

---

## The Factor Independence Assumption

The current model assumes factors are independent:

```
F ~ N(0, I)    # Identity matrix: factors uncorrelated
```

This means event correlation comes *only* from shared factor loadings. If two events load on different factors, they're uncorrelated—even if those factors might logically co-move (e.g., climate stress and food stress).

An alternative is to allow factor correlation:

```
F ~ N(0, Ω)    # Ω specifies inter-factor correlations
```

This would amplify event clustering when the underlying factors themselves tend to occur together. See [[methodology/project/open-questions]] for discussion of this design choice.

---

## Implementation Reference

The sampling procedure is implemented in [[methodology/concepts/monte-carlo-framework]], Section 8 (Simulation Mechanics). The factor copula approach appears in Section 8.3.

---

*See also: [[methodology/reference/factor-loadings]] for how loadings are specified*
