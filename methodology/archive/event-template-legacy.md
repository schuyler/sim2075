---
title: event-template
type: note
permalink: methodology/event-template
tags:
- methodology
- template
- events
- v2
---

# Event Template v2.0

Canonical template for event specifications per [[methodology/integrated-event-state-framework]].

**Key changes from v1.0:**
- Added causal type classification (Type 1/2/3)
- Added type-specific probability specification
- Structured impact vectors with durability
- Cascade pathway documentation
- Removed implicit valence assumptions

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

### Causal Type Rationale

[2-3 sentences: Why this type? What makes it stochastic/threshold/contingent?]

## Description

[2-3 sentences: What state transition this event represents. What defines occurrence. Key characteristics.]

---

## Probability Specification

### For Type 1 (Stochastic)

| Metric | Value |
|--------|-------|
| **Annual probability** | [X%] |
| **Low bound** | [X%] |
| **High bound** | [X%] |
| **Confidence** | [Low / Medium / High] |
| **Base rate source** | [Historical frequency, expert judgment, etc.] |

### For Type 2 (Threshold)

| Pressure Variable | Weight | Current Value | Trend |
|-------------------|--------|---------------|-------|
| [state_variable_1] | [0.0-1.0] | [value] | [↑ / ↔ / ↓] |
| [state_variable_2] | [0.0-1.0] | [value] | [↑ / ↔ / ↓] |

| Threshold Specification | Value |
|------------------------|-------|
| **Threshold estimate** | [value or composite score] |
| **Threshold uncertainty** | [± range or distribution] |
| **Probability function** | [logistic / exponential / step] |
| **Current pressure level** | [value] |
| **Distance to threshold** | [value] |
| **Current annual probability** | [X%] |

### For Type 3 (Contingent)

**Window Preconditions:**
- [ ] [Condition 1: state_variable operator value]
- [ ] [Condition 2: state_variable operator value]
- Logic: [AND / OR / complex expression]

| Window Parameters | Value |
|-------------------|-------|
| **Annual window probability** | [X%] (given preconditions met) |
| **Window duration** | [X years] (if not resolved) |

**Resolutions:**

| Resolution | Probability | Description |
|------------|-------------|-------------|
| [resolution_1] | [X%] | [Brief description] |
| [resolution_2] | [X%] | [Brief description] |
| [status_quo] | [X%] | Window closes without resolution |

---

### Probability Derivation

[Step-by-step reasoning:]
- Base rate or reference class (Type 1)
- Pressure accumulation dynamics (Type 2)
- Window conditions and coordination difficulty (Type 3)
- Adjustments made and why

### Comparative Ranking

[How does this compare to similar events? Reference [[methodology/priority-event-ranking]]]

### Key Uncertainties

- [What could make probability much higher or lower?]
- [What are we most uncertain about?]

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.0 | [one-line reason or "No mechanism"] |
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

[1-2 sentences: Which factor(s) drive this? How do factors shock relevant pressure variables?]

---

## Impact Vector

### Global Impacts

| Variable | Magnitude | Delay | Duration | Uncertainty |
|----------|-----------|-------|----------|-------------|
| [gdp_real] | [X% to Y%] | [years] | [years / permanent] | [low/med/high] |
| [variable_2] | [range] | [years] | [duration] | [uncertainty] |

### Entity-Specific Impacts

**[Entity or Entity Group]:**

| Variable | Magnitude | Delay | Duration | Uncertainty |
|----------|-----------|-------|----------|-------------|
| [variable] | [range] | [years] | [duration] | [uncertainty] |

### For Type 3: Resolution-Specific Impacts

**[Resolution 1]:**
| Variable | Magnitude | Notes |
|----------|-----------|-------|
| [variable] | [range] | |

**[Resolution 2]:**
| Variable | Magnitude | Notes |
|----------|-----------|-------|
| [variable] | [range] | |

### Conditional Modifiers

| Condition | Target Impact | Modifier |
|-----------|---------------|----------|
| If [state_condition] | [which impact] | [×1.5 / +X / etc.] |
| If concurrent [event] | [which impact] | [modifier] |

### Impact Derivation

[How were impacts estimated? Which method—analog, transmission, scaling?]
[Reference historical cases if used]

---

## Durability Specification

| Impact Component | Durability Type | Parameters |
|------------------|-----------------|------------|
| [impact_1] | Permanent | — |
| [impact_2] | Recoverable | Half-life: X years, Scarring: Y% |
| [impact_3] | Maintenance required | Annual survival: X%, Failure mode: [partial/full/gradual] |

### Maintenance Requirements (if applicable)

| Parameter | Value |
|-----------|-------|
| Annual survival probability | [X%] |
| Failure triggers | [leadership change, stress threshold, defection] |
| On failure | [partial reversal X%, full reversal Y%, gradual Z%] |

---

## Cascade Pathways

### [Cascade 1: Name]

| Parameter | Value |
|-----------|-------|
| **Target variable** | [state_variable_id] |
| **Target entity** | [entity_id or "global"] |
| **Magnitude** | [change to variable] |
| **Delay** | [years] |
| **Mechanism** | [How does this cascade work?] |
| **Conditions** | [When does this apply?] |

### Events This May Trigger

| Event | Mechanism |
|-------|-----------|
| [Event ID] | [How this event changes state to increase P(that event)] |

### Events That May Trigger This

| Event | Mechanism |
|-------|-----------|
| [Event ID] | [How that event changes state to increase P(this event)] |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 / Level 2 / Level 3 |
| **Created** | [YYYY-MM-DD] |
| **Last updated** | [YYYY-MM-DD] |
| **Template version** | 2.0 |

## Sources

- [Source 1]
- [Source 2]

## Open Questions

- [What don't we know?]
- [What would change our estimates?]
```

---

## Field Definitions

### Classification Fields

| Field | Definition |
|-------|------------|
| **ID** | Unique identifier for simulation. UPPERCASE_SNAKE_CASE. |
| **Scale** | Geographic scope: Global (worldwide), Regional (multi-country), National (single country) |
| **Domain** | Primary category: Environmental, Political, Economic, Health, Technological |
| **Causal Type** | Type 1 (stochastic arrival), Type 2 (threshold/accumulation), Type 3 (contingent/window). See [[methodology/integrated-event-state-framework]] Section 3. |
| **Onset Speed** | How fast from trigger to full effect |
| **Reversibility** | Can system return to prior state? |

### Probability Fields by Type

**Type 1:**
- Standard annual probability with bounds and confidence

**Type 2:**
- Pressure variables with weights
- Threshold estimate with uncertainty
- Probability function (how P increases with pressure)
- Current state assessment

**Type 3:**
- Window preconditions (state requirements)
- Window probability (annual, given preconditions)
- Resolution distribution (mutually exclusive outcomes)

### Impact Vector Fields

| Field | Definition |
|-------|------------|
| **Magnitude** | Size of impact. Use ranges, not point estimates. |
| **Delay** | Years until impact manifests. 0 = immediate. |
| **Duration** | How long impact persists: years, permanent, or maintenance_required |
| **Uncertainty** | Confidence in the estimate: low, medium, high |

### Durability Types

| Type | Meaning |
|------|---------|
| **Permanent** | Impact never reverses (deaths, resource depletion, technology adoption) |
| **Recoverable** | Impact recovers over time with half-life and possible permanent scarring |
| **Maintenance required** | Impact persists only while maintained (agreements, coordination) |

---

## Checklist Before Saving

- [ ] Causal type assigned with rationale
- [ ] Type-appropriate probability specification completed
- [ ] Factor loadings sum-of-squares ≤ 1.0
- [ ] Impact vector structured with magnitude, delay, duration, uncertainty
- [ ] Durability type specified for major impacts
- [ ] At least one cascade pathway documented
- [ ] Research tier marked
- [ ] Open questions listed

---

## Migration Notes

**Events using v1.0 template** should be updated to v2.0 by adding:
1. Causal type classification
2. Type-specific probability section
3. Structured impact vector
4. Durability specification
5. Cascade pathways

Existing probability and impact estimates can usually be retained; the new template provides additional structure.
