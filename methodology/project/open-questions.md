---
title: open-questions
type: note
permalink: methodology/project/open-questions
tags:
- methodology
- planning
- open-questions
- todo
---

# Open Questions

Higher-level methodological and structural questions that warrant dedicated exploratory sessions. These are distinct from the task-oriented progress tracker—each item here represents an area of uncertainty or potential improvement in the simulation architecture itself.

---

## Active Questions

### 2. Type 3 Event Calibration

**Status:** Unresolved  
**Added:** December 2025  
**Source:** Methodology review

Type 3 (Contingent) events—Taiwan, climate agreements, great power negotiations—depend on decisions by specific actors in ways that Type 1 base rates and Type 2 pressure accumulation don't capture well.

**Key issues:**
- The window-resolution structure is reasonable, but calibrating resolution probabilities ("35% military conflict, 25% negotiated accommodation") is essentially geopolitical forecasting
- Geopolitical forecasting has poor track records
- How should epistemic humility be reflected in Type 3 specifications?

**Session goal:** Develop guidance for Type 3 calibration that honestly reflects uncertainty about actor decisions.

---

### 3. Positive Discontinuity Coverage

**Status:** Unresolved  
**Added:** December 2025  
**Source:** Methodology review

The priority event list of 20 events includes no breakthrough energy deployment, no major de-escalation, no institutional innovation success. This creates asymmetric uncertainty: the model will explore negative tails well but may underweight scenarios where things go unexpectedly right.

**Key issues:**
- Does this reflect considered judgment (positive discontinuities are genuinely rare/unlikely) or selection bias?
- The framework explicitly handles "positive" events through impact vectors—but the catalog doesn't include them
- Which positive discontinuities are plausible enough to model?

**Session goal:** Evaluate whether positive discontinuities belong in the catalog; if so, identify 3-5 candidates and specify at least one.

---

### 4. Recovery Dynamics

**Status:** Unresolved  
**Added:** December 2025  
**Source:** Methodology review

The collapse-patterns document covers how things fall apart in detail, but recovery trajectories are thinner. If the simulation produces "Pakistan state failure in 2035," what happens next matters for cumulative outcomes.

**Key issues:**
- Does collapsed state remain collapsed, partially recover, or cascade further?
- Recovery conditions are listed but not parameterized for simulation
- Durability types handle impact persistence, but not state recovery trajectories

**Session goal:** Specify recovery dynamics sufficiently for the simulation to model post-collapse trajectories.

---

## Resolved Questions

### 1. Factor Correlation Structure

**Status:** Resolved  
**Added:** December 2025  
**Resolved:** December 2025  
**Source:** Methodology review

**Original question:** The correlation structure *between factors themselves* was underspecified. Should factors be independent, correlated via a matrix, or structured hierarchically via meta-factors?

**Resolution:** Adopted inter-factor correlation matrix (Ω). 

**Key decisions:**
- Independent factors underestimate clustering when multiple systemic factors are elevated
- Meta-factors don't fit our case—the correlations we need are pairwise with specific mechanisms, not manifestations of higher-order constructs
- Direct correlation matrix is transparent, mechanism-specific, and revisable

**Deliverables:**
- [[methodology/concepts/gaussian-copula]] — Conceptual foundation for correlated sampling
- [[methodology/concepts/factor-correlation-structure]] — Design rationale for choosing Ω over alternatives
- [[methodology/reference/factor-correlation-matrix]] — The 12×12 matrix with 19 non-zero correlations

**Remaining work:**
- Compute implied event correlations once more events are specified
- Verify double-counting doesn't inflate correlations unreasonably
- Sensitivity analysis on key correlations (F_CLIM↔F_FOOD, F_GPT↔F_EAS)

**Known limitations documented in factor-correlation-matrix:**
- Double-counting through direct loadings + factor correlation
- Symmetric correlation misrepresents causal direction
- No empirical calibration (structured judgment only)

---

### 4. Time Horizon Tractability

**Status:** Resolved (partial)  
**Added:** December 2025  
**Resolved:** December 2025  
**Source:** Methodology review

**Original question:** The 50-year horizon (to 2075) strains the methodology. Calibration anchors cover 5-15 year windows. Are 50-year distributions decision-relevant or just noise? Should 2050 be primary?

**Resolution:** Adopted dual-horizon interpretation. Simulation runs through 2075; interpretation distinguishes decision-relevant from exploratory horizons.

**Key decisions:**
- Truncating at 2050 would systematically underweight slow-burn discontinuities (climate tipping points, demographic crunches, institutional decay, climate migration) in favor of acute shocks
- 50-year distributions are not decision-relevant in the policy sense, but are useful for tail exploration—understanding which cascade patterns produce civilizational-scale disruption
- Report distributions at multiple horizons (2035, 2050, 2075) with explicit confidence degradation at longer horizons

**Interpretation framework:**
- **2050 (25 years):** Primary horizon for decision-relevant claims. Outer bound of meaningful action-consequence linkage.
- **2075 (50 years):** Horizon for tail exploration. "What fraction of trajectories lead to catastrophic outcomes?" Not forecasting—exploring possibility space.

**Deferred to implementation (Phase 2):**
- How confidence intervals widen mechanically with time horizon
- Whether Monte Carlo variance growth naturally produces appropriate uncertainty, or whether epistemic uncertainty needs separate modeling
- Validation that longer-horizon outputs aren't false precision

**Known limitations:**
- "Tail exploration" is interpretively useful but not rigorously defined
- No formal confidence degradation model yet
- Calibration anchors remain 5-15 year phenomena; extrapolation to 50 years is acknowledged weakness

---

## How to Use This Document

Each open question should get a dedicated exploratory session when bandwidth permits. Sessions should:

1. Review the question and any relevant existing documentation
2. Explore options and tradeoffs
3. Make a decision or explicitly defer with rationale
4. Update relevant methodology documents
5. Move the question to "Resolved" with summary

Questions may spawn sub-questions or reveal new issues—add those as new entries rather than expanding existing items indefinitely.

---

*Last updated: December 2025*