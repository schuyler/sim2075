---
title: event-template-v2
type: note
permalink: methodology/event-template-v2
tags:
- methodology
- template
- events
- causal-types
- impact-vectors
---

# Event Template v2

**Updated per [[methodology/integrated-event-state-framework]]**

Canonical template for event specifications. Copy this when creating new events.

**Reference**: For valid variable IDs, see [[methodology/reference/state-specification]] Appendix A.

---

## Template (Copy Below This Line)

```markdown
# [Event Name]

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | [UPPERCASE_SNAKE_CASE] |
| **Scale** | [Global / Regional / National] |
| **Domain** | [Environmental / Political / Economic / Health / Technological] |
| **Causal Type** | [Type 1: Stochastic / Type 2: Threshold / Type 3: Contingent] |
| **Onset Speed** | [Sudden (<1yr) / Rapid (1-5yr) / Gradual (5-20yr)] |
| **Reversibility** | [Reversible / Partial / Irreversible] |

## Description

[2-3 sentences: What state transition does this event represent? What marks occurrence?]

---

## Causal Type Specification

### For Type 1 (Stochastic) Events:

**Base rate derivation**: [Historical frequency in reference class]

**Condition adjustments**: [What current conditions modify the base rate?]

### For Type 2 (Threshold) Events:

**Pressure Function**:

| State Variable | Weight | Transform |
|----------------|--------|-----------|
| [variable_id] | [0.0-1.0] | [linear / inverse / exponential / threshold(X)] |
| [variable_id] | [0.0-1.0] | |

**Threshold**:
| Parameter | Value |
|-----------|-------|
| **Estimate** | [X on 0-100 pressure scale] |
| **Uncertainty** | [±Y or distribution] |
| **Sharpness (k)** | [Higher = sharper transition] |
| **Historical calibration** | [What analogous thresholds inform this?] |

**Minimum probability**: [Floor even at low pressure]

### For Type 3 (Contingent) Events:

**Window Preconditions**:

| Condition | Threshold |
|-----------|-----------|
| [state_variable] | [> X / < X / in [X,Y]] |
| [state_variable] | |

**Annual probability given conditions met**: [X%]

**Resolutions**:

| Resolution | Probability | Impact Vector Section |
|------------|-------------|----------------------|
| [resolution_1_id] | [X%] | See below |
| [resolution_2_id] | [X%] | See below |
| [status_quo] | [X%] | No impact |

*Probabilities must sum to 100%*

---

## Probability (Type 1) or Base Parameters (Type 2/3)

| Metric | Value |
|--------|-------|
| **Annual probability** | [X%] |
| **Low bound** | [X%] |
| **High bound** | [X%] |
| **Confidence** | [Low / Medium / High] |
| **25-year cumulative** | [~X% at point estimate] |

### Derivation

[Step-by-step reasoning. Include:]
- Base rate or reference class (if historical method)
- Expert estimates consulted
- Structural reasoning
- Adjustments made and why

### Comparative Ranking

[How does this compare to similar events? Reference [[methodology/priority-event-ranking]]]

### Key Uncertainties

- [What could make probability much higher or lower?]

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.0 | [one-line reason] |
| F_FIN | 0.0 | |
| F_HLTH | 0.0 | |
| F_GPT | 0.0 | |
| F_FOOD | 0.0 | |
| F_TECH | 0.0 | |
| F_EUR | 0.0 | |
| F_MENA | 0.0 | |
| F_SAS | 0.0 | |
| F_EAS | 0.0 | |
| F_SSA | 0.0 | |
| F_LAM | 0.0 | |

**Sum of squared loadings**: [X.XX] ✓ [must be ≤ 1.0]

### Loading Rationale

[For Type 2/3: Factors primarily shock state variables, which then affect pressure/preconditions]

---

## Impact Vector

**Valid variable IDs**: See [[methodology/reference/state-specification]] Appendix A (country-level) and Appendix A.2 (global).

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| [variable_id] | ↑/↓ | [X ± Y] | [immediate/delayed(N)/gradual(N)] | [type + params] |
| | | | | |

### Regional/Country Impacts

**[Region/Country]:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| [variable_id] | ↑/↓ | [X ± Y] | | |

### Differential Impacts

**Exposure variable**: [state_variable_id]
**Function**: [linear / threshold / custom]
**Effect**: [Higher X → larger/smaller impact because...]

### Durability Specifications

For each impact, specify durability type:

| Durability Type | Parameters | Used For |
|-----------------|------------|----------|
| **permanent** | N/A | [which impacts] |
| **decaying** | half_life: [N years], floor: [X] | [which impacts] |
| **maintenance_required** | annual_failure_prob: [X%], failure_conditions: [...] | [which impacts] |
| **shock_vulnerable** | vulnerable_to: [...], reversal_fraction: [X] | [which impacts] |
| **regime_dependent** | persists_in: [...] | [which impacts] |

### Impact Derivation

[How were impacts estimated? Which method—analog, transmission, scaling?]

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration |
|---------|--------------|-------------------|----------|
| [describe mechanism] | [EVENT_ID] | [+X% or ×Y] | [N years] |

### Impact Chains

**Pathway 1**: [Event] → [Impact 1] → [Impact 2] → [P(Event B) changes]

[Describe the causal chain]

---

## Transmission Channels

### [Channel Name]

**Mechanism**: [How does event affect outcomes through this channel?]
**Affected regions**: [List]
**Affected variables**: [List]

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 / Level 2 / Level 3 |
| **Last updated** | [YYYY-MM-DD] |
| **Upgrade candidate** | Yes / No |
| **Upgrade rationale** | [If yes, why] |

## Sources

- [Source 1]

## Open Questions

- [What don't we know?]
```

---

## Field Definitions

### Causal Type

| Type | When to Use | Key Specification Required |
|------|-------------|---------------------------|
| **Type 1** | Stable base rate, limited predictability, approximately Poisson | Base rate derivation |
| **Type 2** | Probability increases as pressure accumulates; threshold dynamics | Pressure function, threshold estimate |
| **Type 3** | Outcome depends on negotiations/decisions; preconditions create windows | Window conditions, resolution probabilities |

**Note**: Type 4 (S-curve) dynamics are NOT events. Model as baseline trajectory parameters.

### Durability Types

| Type | Meaning | Example |
|------|---------|---------|
| **permanent** | Impact never reverses | Deaths, resource depletion, knowledge gains |
| **decaying** | Impact fades with half-life | Reputational damage, financial shocks |
| **maintenance_required** | Persists only with ongoing effort; can fail | Treaties, alliances, policy achievements |
| **shock_vulnerable** | Can be reversed by other events | Development gains, living standards |
| **regime_dependent** | Persists only in certain system states | Political achievements tied to regime |

### Impact Vector vs. Valence

Events do NOT have positive/negative valence. The impact vector specifies:
- **Which variables** are affected
- **Direction** (increase/decrease)
- **Magnitude** (with uncertainty)
- **Who** is affected differently
- **How long** it lasts

Whether this is "good" or "bad" depends on whose welfare function you apply.

---

## Checklist Before Saving

### Classification
- [ ] Causal type selected with rationale
- [ ] All classification fields populated

### Type-Specific
- [ ] **Type 1**: Base rate derivation complete
- [ ] **Type 2**: Pressure function specified, threshold estimated
- [ ] **Type 3**: Window conditions specified, resolutions defined with probabilities summing to 100%

### Probability
- [ ] Probability has derivation (not just numbers)
- [ ] Comparative ranking completed
- [ ] Key uncertainties listed

### Factor Loadings
- [ ] Sum of squared loadings ≤ 1.0
- [ ] Primary factor identified with rationale
- [ ] For Type 2/3: loadings describe factor→state relationship

### Impact Vector
- [ ] All significant impacts listed with variables
- [ ] Durability type specified for each impact
- [ ] Differential impacts documented if relevant
- [ ] Impact derivation method cited

### Cascades
- [ ] Cascade pathways documented
- [ ] Target events identified where relevant

### Metadata
- [ ] Research tier marked
- [ ] Open questions listed
