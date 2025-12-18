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

### 1. Factor Correlation Structure

**Status:** Unresolved  
**Added:** December 2025  
**Source:** Methodology review

The 12-factor model is well-designed conceptually, and the sum-of-squared-loadings constraint ensures valid correlation matrices for individual events. But the correlation structure *between factors themselves* is underspecified.

**Key issues:**
- If F_CLIM and F_FIN are correlated (climate stress → economic disruption), this should be captured
- The documents mention a "Gaussian copula" approach but no actual inter-factor correlation matrix exists
- How should regional factors correlate with global systemic factors?

**Session goal:** Define the factor correlation matrix with explicit rationale for each correlation estimate.

---

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

### 4. Time Horizon Tractability

**Status:** Unresolved  
**Added:** December 2025  
**Source:** Methodology review

The 50-year horizon (to 2075) strains the methodology. Most calibration anchors (Venezuela, Syria, 2008 GFC) cover 5-15 year windows. Compounding uncertainty over 50 years produces extremely wide distributions.

**Key issues:**
- Are 50-year distributions decision-relevant, or just noise?
- Should 2050 (25 years) be the primary horizon with 2075 as secondary?
- How should confidence intervals widen with time, and does the model capture this correctly?

**Session goal:** Evaluate whether the time horizon should be adjusted; if not, clarify how to interpret very-long-term distributions.

---

### 5. Recovery Dynamics

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

*(Move items here when addressed, with date and resolution summary)*

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