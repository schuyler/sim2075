---
title: level-1-workflow
type: note
permalink: methodology/level-1-workflow
tags:
- methodology
- workflow
- level-1
- process
- placeholder
---

# Level 1 Workflow

**Status: PLACEHOLDER - To be filled in**

Step-by-step process for producing Level 1 event specifications in ~30 minutes.

## Prerequisites

[TO BE ADDED]

## Steps

[TO BE ADDED]

## Prompting Guide

[TO BE ADDED]

## Common Pitfalls

[TO BE ADDED]


## Level 1 Workflow
# Level 1 Workflow

**Updated per [[methodology/integrated-event-state-framework]]**

Step-by-step process for producing Level 1 event specifications in ~40 minutes using Claude Opus from prior knowledge.

---

## Prerequisites

Before starting:
1. Have [[methodology/event-template-v2]] open for copying
2. Have [[methodology/priority-event-ranking]] open for probability cross-check
3. Have [[methodology/calibration-anchors]] open for reference
4. Have [[methodology/integrated-event-state-framework]] Section 3 (Causal Types) for reference
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

### Step 2: Causal Type Classification (3 min)

**This is the critical first decision that shapes everything else.**

Ask: What kind of causal structure does this event have?

| Question | If Yes → |
|----------|----------|
| Does it have a stable historical base rate with unpredictable timing? | **Type 1 (Stochastic)** |
| Does probability increase as measurable pressure accumulates? | **Type 2 (Threshold)** |
| Does outcome depend on negotiations/decisions among identifiable actors? | **Type 3 (Contingent)** |
| Is this a gradual S-curve (technology adoption, cost decline)? | **NOT AN EVENT** — model as baseline |

**If uncertain:** Most state failures and tipping points are Type 2. Most great power conflicts and agreements are Type 3. Most pandemics and natural disasters are Type 1.

Document your rationale for the classification.

### Step 3: Basic Classification (2 min)

Fill in the classification table:
- **ID**: UPPERCASE_SNAKE_CASE version of event name
- **Scale**: Is this global, regional, or national?
- **Domain**: Primary category
- **Causal Type**: From Step 2
- **Onset**: How fast would this unfold?
- **Reversibility**: Can it be undone?

Write 2-3 sentence description focusing on: What state transition does this represent?

### Step 4: Type-Specific Parameters (5 min)

**If Type 1 (Stochastic):**
- Identify reference class for base rate
- Note condition adjustments

**If Type 2 (Threshold):**
- List 3-5 state variables that contribute to pressure
- Assign relative weights (should sum to ~1.0)
- Estimate threshold level on 0-100 pressure scale
- Note uncertainty range on threshold
- Cite historical analogs for threshold calibration

**If Type 3 (Contingent):**
- List preconditions (state variable thresholds) that open window
- Estimate P(window opens | preconditions met)
- List 2-4 possible resolutions
- Assign probabilities to each resolution (must sum to 100%)

### Step 5: Probability (8 min)

**5a. Find the anchor** (2 min)
- Check [[methodology/calibration-anchors]] for most similar event
- Check [[methodology/priority-event-ranking]] for related events

**5b. Estimate using appropriate method** (4 min)

*For Type 1 (base rate):*
- What's the reference class?
- How many occurrences in how many country-years?
- What adjustments for current conditions?

*For Type 2 (state-conditioned):*
- What's the base probability at low pressure?
- What's the probability at high pressure?
- What's current pressure level?

*For Type 3 (two-stage):*
- P(window) × P(resolution | window) = P(outcome)
- Estimate each component separately

**5c. Cross-check against ranking** (1 min)
- Is this more or less likely than the anchor event?
- Does that match your probability estimate?

**5d. Document derivation** (1 min)
- Write out the reasoning, not just the number

### Step 6: Factor Loadings (5 min)

**Note:** In the integrated framework, factors primarily shock state variables, which then affect pressure/preconditions. But for simulation efficiency, we still assign loadings to events.

**6a. Identify primary factor**
- "Which factor's realization most affects the state variables that drive this event?"
- Assign 0.6-0.85 loading

**6b. Identify secondary factors**
- Go through all 12 factors
- For each: "Does this factor affect relevant state variables?"
- If yes: assign 0.1-0.4 based on strength
- If no: assign 0.0

**6c. Validate constraint**
- Sum the squares: Σ(loading²)
- Must be ≤ 1.0
- If over, reduce secondary loadings

**6d. Write rationale**
- For Type 2/3: Note which state variables the factors shock

### Step 7: Impact Vector (10 min)

**7a. Identify affected variables** (2 min)
- Global variables: GDP, trade, commodities?
- Country variables: Which countries, which variables?
- Humanitarian: Displacement, mortality?

**7b. Estimate magnitudes** (4 min)
- Find most similar historical case from [[methodology/impact-estimation]] anchors
- Scale appropriately
- Express as mean ± std, not point estimate
- Note distribution (normal/lognormal)

**7c. Specify onset timing** (1 min)
- Immediate: Financial shocks, acute events
- Delayed(N): Infrastructure effects, policy changes
- Gradual(N): Climate impacts, behavioral changes

**7d. Assign durability types** (3 min)

For each impact, ask: What kind of impact is this?

| Impact Type | Durability |
|-------------|------------|
| Deaths | permanent |
| Infrastructure damage | decaying (half-life = rebuild time) |
| Treaties/agreements | maintenance_required |
| Economic growth | shock_vulnerable |
| Resource depletion | permanent |
| Market dislocations | decaying |
| Policy achievements | regime_dependent |

Specify parameters where required (half-life, annual_failure_prob, etc.)

**If Type 3:** Create separate impact vector for each resolution.

### Step 8: Cascade Effects (3 min)

Document 2-3 cascade pathways:
- Which state variables does this event change?
- How does that state change affect P(other events)?
- What's the probability modifier and duration?

Example:
```
Pathway: Pakistan failure → regional instability → P(India-Pakistan conflict) increases
Target event: INDIA_PAKISTAN_CONFLICT
Modifier: +3% annual probability
Duration: 10 years
```

### Step 9: Transmission Channels (3 min)

List 2-4 main pathways from event to impact:
- Name the channel
- One sentence on mechanism
- Which regions/variables affected

### Step 10: Final Checks (2 min)

Run [[methodology/quality-checklist]]:
- [ ] Causal type assigned with rationale
- [ ] Type-specific parameters complete (pressure function / resolutions)
- [ ] Probability has derivation
- [ ] Comparative ranking done
- [ ] Sum of squares ≤ 1.0
- [ ] Impact vector with durability types
- [ ] Cascade effects documented
- [ ] Research tier = Level 1
- [ ] Open questions listed

Save the file.

---

## Prompting Guide

If using Claude to assist with Level 1 specification, use this prompt structure:

```
I'm specifying the event "[Event Name]" for a geopolitical Monte Carlo simulation.

Context:
- [1-2 sentences on what state transition this represents]
- Causal type: [Type 1/2/3] because [rationale]
- Similar events in our catalog: [list anchors]
- This is a Level 1 (prior knowledge) specification

Please help me fill in:
1. [For Type 2] Pressure function: which state variables, what weights, threshold estimate
2. [For Type 3] Window preconditions and resolution probabilities
3. Annual probability estimate with derivation
4. Factor loadings (12 factors, must sum-of-squares ≤ 1.0)
5. Impact vector with durability types (permanent/decaying/maintenance_required/shock_vulnerable)
6. Key cascade effects (how does this change P(other events)?)

Use ranges, not false precision. Acknowledge uncertainty.
```

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **S-curve as event** | Not an event. Model as baseline trajectory uncertainty. |
| **"Positive/negative" framing** | Describe as state transition with impact vector |
| **Type 2 without pressure function** | Specify state variables, weights, threshold |
| **Type 3 without resolutions** | Define multiple outcomes (conflict/negotiation/status quo) |
| **Durability by event valence** | Durability by impact type: deaths=permanent, agreements=maintenance_required |
| **Point estimates without ranges** | Always give mean ± std |
| **Probability without derivation** | Show your work—method + reasoning |
| **All factors get small loadings** | Zero is valid. Most events have 1-3 significant factors. |
| **Sum of squares > 1.0** | Reduce secondary loadings |
| **Missing onset timing** | Specify immediate/delayed/gradual |
| **No cascade effects** | Every event changes state → affects P(other events) |
| **Skipping comparative ranking** | This is how you catch miscalibration |

---

## Time Budget

| Step | Minutes |
|------|---------|
| Copy template | 1 |
| Causal type classification | 3 |
| Basic classification | 2 |
| Type-specific parameters | 5 |
| Probability | 8 |
| Factor loadings | 5 |
| Impact vector | 10 |
| Cascade effects | 3 |
| Transmission channels | 3 |
| Final checks | 2 |
| **Total** | **~42 min** |

With practice, this compresses to 30-35 minutes.