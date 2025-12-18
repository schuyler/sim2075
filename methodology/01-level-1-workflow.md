---
title: level-1-workflow-v2
type: note
permalink: methodology/level-1-workflow-v2
tags:
- methodology
- workflow
- level-1
- process
- causal-types
---

# Level 1 Workflow v2

**Updated per [[methodology/integrated-event-state-framework]]**

Step-by-step process for producing Level 1 event specifications in ~40 minutes using Claude Opus from prior knowledge.

---

## Prerequisites

Before starting:
1. Have [[methodology/event-template-v2]] open for copying
2. Have [[methodology/integrated-event-state-framework]] Section 3 open for causal type reference
3. Have [[methodology/priority-event-ranking]] open for probability cross-check
4. Have [[methodology/calibration-anchors]] open for reference
5. Know which event you're specifying

---

## Steps

### Step 1: Copy Template (1 min)

Copy the template from [[methodology/event-template-v2]] into a new file at:
- `events/climate/[event-name].md` for environmental events
- `events/geopolitical/[event-name].md` for political/state failure events
- `events/financial/[event-name].md` for economic events
- `events/health/[event-name].md` for pandemic/health events
- `events/technology/[event-name].md` for tech discontinuities

Use lowercase-with-dashes for filename.

### Step 2: Classification and Causal Type (3 min)

**2a. Basic classification:**
- **ID**: UPPERCASE_SNAKE_CASE
- **Scale**: Global / Regional / National
- **Domain**: Environmental / Political / Economic / Health / Technological
- **Onset**: Sudden / Rapid / Gradual
- **Reversibility**: Reversible / Partial / Irreversible

**2b. Determine causal type** (critical step):

Use the decision tree from [[methodology/integrated-event-state-framework]] Section 3.5:

```
1. Is this a continuous trajectory (technology adoption, gradual improvement)?
   YES → Not an event. Model as baseline trajectory. STOP.
   NO → Continue.

2. Does it have a stable historical base rate with limited predictability?
   YES → Type 1 (Stochastic)
   NO → Continue.

3. Does probability increase as measurable pressure accumulates?
   YES → Type 2 (Threshold)
   NO → Continue.

4. Does outcome depend on negotiations/decisions among identifiable actors?
   YES → Type 3 (Contingent)
   NO → Reassess.
```

Write 2-3 sentence description focusing on **what state transition** this event represents.

### Step 3: Type-Specific Specification (5-8 min)

**This step varies by causal type.**

#### For Type 1 (Stochastic):

- Identify historical reference class
- Calculate base rate from historical frequency
- Note condition adjustments from current state
- Document factor contributions to clustering (not triggering)

#### For Type 2 (Threshold):

**3a. Specify pressure function:**

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| [variable] | [0.0-1.0] | [linear/inverse/exp/threshold] | [why] |

Weights should sum to ~1.0.

**3b. Specify threshold:**
- Point estimate (on 0-100 pressure scale)
- Uncertainty range (±X)
- Sharpness parameter k (0.1=gradual, 0.3=sharp)
- Historical calibration (what analogous thresholds inform this?)

**3c. Specify minimum probability floor**

#### For Type 3 (Contingent):

**3a. Specify window preconditions:**

| Condition | Threshold |
|-----------|-----------|
| [state_variable] | [> X / < X / in range] |

**3b. Specify annual probability given conditions met**

**3c. Specify resolutions:**

| Resolution | Probability | Notes |
|------------|-------------|-------|
| [outcome_1] | X% | |
| [outcome_2] | Y% | |
| [status_quo] | Z% | |

Probabilities must sum to 100%.

### Step 4: Probability (8 min)

**4a. Find the anchor** (2 min)
- Check [[methodology/calibration-anchors]] for most similar event
- Check [[methodology/priority-event-ranking]] for related events

**4b. Estimate using appropriate method** (4 min)

*For Type 1:*
- Historical base rate from reference class
- Adjustments for current conditions

*For Type 2:*
- Current pressure estimate
- Distance from threshold
- Apply logistic function to get annual probability

*For Type 3:*
- P(window) from state conditions
- P(resolution|window) from analogies/reasoning
- Combined probability = product

**4c. Cross-check against ranking** (2 min)
- Is this more or less likely than anchor events?
- Revise if incoherent

### Step 5: Factor Loadings (5 min)

**New interpretation (per integrated framework):** Factors shock state variables, which affect pressure (Type 2) or preconditions (Type 3).

**5a. Identify primary factor**
- "Which factor, when high, most increases the state variables that feed into this event's probability?"
- Assign 0.6-0.85 loading

**5b. Identify secondary factors**
- For each of 12 factors: "Does this factor shock state variables in the pressure function?"
- If yes: 0.1-0.4 based on strength
- If no: 0.0

**5c. Validate constraint**
- Σ(loading²) ≤ 1.0
- If over, reduce secondary loadings

**5d. Write rationale**
- Describe the factor→state→pressure pathway

### Step 6: Impact Vector (10 min)

**6a. Identify affected variables** (2 min)
- Which state variables change when this event occurs?
- Global, regional, and country-specific

**6b. Specify magnitude and direction** (3 min)
- Use ranges (mean ± std), not point estimates
- Reference [[methodology/impact-estimation-v2]] anchors
- Scale from analogous historical events

**6c. Specify onset timing** (1 min)
- Immediate / Delayed(N years) / Gradual(N years)

**6d. Specify durability type** (2 min)

For each impact, assign one of:
- **permanent**: Deaths, resource depletion, knowledge
- **decaying**: GDP shocks, reputational damage (specify half_life, floor)
- **maintenance_required**: Treaties, agreements (specify annual_failure_prob)
- **shock_vulnerable**: Development gains (specify vulnerable_to)
- **regime_dependent**: Policy achievements (specify persists_in)

**6e. Document differential impacts** (2 min)
- Which countries affected more/less?
- What exposure variable determines differential?

### Step 7: Cascade Effects (3 min)

Document how this event changes probability of other events:

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| [describe] | [EVENT_ID] | [+X% or ×Y] | [N years] | [how] |

At least 2-3 cascade pathways for significant events.

### Step 8: Transmission Channels (2 min)

List 2-4 main pathways from event to impact:
- Name the channel
- One sentence on mechanism
- Which regions affected
- Which variables affected

### Step 9: Final Checks (2 min)

Run [[methodology/quality-checklist-v2]]:

**Causal Type:**
- [ ] Type assigned with rationale
- [ ] Type-specific fields completed

**Probability:**
- [ ] Derivation documented
- [ ] Cross-checked against ranking

**Factor Loadings:**
- [ ] Σ(loading²) ≤ 1.0
- [ ] Factor→state pathway described

**Impact Vector:**
- [ ] All significant variables listed
- [ ] Durability type assigned for each
- [ ] Estimation method cited

**Cascades:**
- [ ] At least 2 pathways documented

**Metadata:**
- [ ] Research tier = Level 1
- [ ] Open questions listed

Save the file.

---

## Type-Specific Quick Reference

### Type 1 (Stochastic) Checklist
- [ ] Reference class identified
- [ ] Historical base rate calculated
- [ ] Condition adjustments documented
- [ ] Factor loadings describe clustering, not triggering

### Type 2 (Threshold) Checklist
- [ ] Pressure function variables and weights specified
- [ ] Threshold estimate with uncertainty
- [ ] Current pressure estimate
- [ ] Minimum probability floor
- [ ] Factor loadings describe factor→state→pressure path

### Type 3 (Contingent) Checklist
- [ ] Window preconditions specified
- [ ] Annual probability given conditions
- [ ] All resolutions listed with probabilities (sum to 100%)
- [ ] Separate impact vector for each resolution
- [ ] Factor loadings describe factor→state→preconditions path

---

## Time Budget

| Step | Minutes |
|------|---------|
| Copy template | 1 |
| Classification + causal type | 3 |
| Type-specific specification | 5-8 |
| Probability | 8 |
| Factor loadings | 5 |
| Impact vector | 10 |
| Cascade effects | 3 |
| Transmission channels | 2 |
| Final checks | 2 |
| **Total** | **~40 min** |

With practice, this compresses to 25-30 minutes.

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Skipping causal type determination** | This is foundational—affects everything else |
| **Type 4 dynamics as events** | Move to baseline trajectory; not a discrete event |
| **Type 2 without pressure function** | Must specify which state variables and thresholds |
| **Type 3 with single outcome** | Specify multiple resolutions with probabilities |
| **Same durability for all impacts** | Durability depends on impact type, not event |
| **Factor loadings describe event triggering** | Factors shock state; state conditions probability |
| **Point estimates without ranges** | Always give mean ± std |
| **Missing cascade documentation** | How does this event affect other event probabilities? |
| **Skipping comparative ranking** | This catches miscalibration |

---

## Prompting Guide

If using Claude to assist with Level 1 specification:

```
I'm specifying the event "[Event Name]" for a geopolitical Monte Carlo simulation.

Context:
- [1-2 sentences on what state transition this represents]
- Causal type: [Type 1/2/3] because [rationale]
- Similar events in our catalog: [list anchors]
- This is a Level 1 (prior knowledge) specification

Please help me fill in:
1. [For Type 2: Pressure function and threshold]
   [For Type 3: Window conditions and resolutions]
2. Annual probability estimate with derivation
3. Factor loadings (12 factors, Σsquares ≤ 1.0) with factor→state interpretation
4. Impact vector with durability types
5. Cascade effects (which events become more/less likely)

Use ranges, not false precision. Acknowledge uncertainty.
```
