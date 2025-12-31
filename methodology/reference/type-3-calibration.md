---
title: type-3-calibration
type: note
permalink: methodology/reference/type-3-calibration
tags:
- methodology
- reference
- type-3
- calibration
- operational-guidance
- entropy-maximization
---

# Type 3 Calibration Guidance

Operational guidance for specifying Type 3 (Contingent) events. Synthesizes the epistemological framework into practical steps.

---

## Core Principle
**Shift modeling effort from resolution probabilities (intractable) to aftermath specification (tractable).**

"What happens if conflict occurs" is more answerable than "will conflict occur."

### Variance Allocation Implication

This intractability has a concrete consequence for factor loadings: **Type 3 events should have the lowest factor-explained variance** of all causal types.

Factors explain *why crisis windows open*, but cannot explain *how small-N actor decisions resolve*. See [[methodology/reference/variance-allocation]] for targets and computation method.

| Component | Tractability | Treatment |
|-----------|--------------|-----------|
| Window preconditions | Moderate | Structural reasoning about tension escalation |
| Window probability | Moderate | Historical frequency of crises reaching critical phase |
| Discontinuity probability | Moderate | Historical rate of crises producing discontinuities |
| Resolution probabilities | **Low** | Entropy maximization → uniform or weakly-informed |
| Aftermath given each resolution | Moderate-High | Supply chain data, financial precedents, escalation logic |

For the underlying reasoning, see:
- [[methodology/concepts/tractability-boundaries]] — Why resolution probabilities are low-tractability
- [[methodology/concepts/entropy-maximization]] — The default principle for intractable parameters
- [[methodology/concepts/small-n-actor-problem]] — Why small-N actor decisions resist estimation

---

## 0. Resolutions Are Discontinuity Types

**Critical framing**: Resolutions enumerate *types of discontinuity*, not *all possible outcomes*.

The event catalog contains discontinuities. A Type 3 event IS a discontinuity — when it fires, something fundamental has changed. Resolutions describe the different *forms* that discontinuity can take.

### What Resolutions Are

- Different types of system break (military conflict vs. great power settlement)
- Different forms of the discontinuity occurring
- Mutually exclusive ways the threshold gets crossed

### What Resolutions Are NOT

- "Status quo restoration" or "crisis de-escalates" — these are **non-events**
- Outcomes where nothing fundamental changed
- The full space of "what could happen given a crisis window"

### The Correct Two-Stage Structure

```
P(event) = P(window opens) × P(discontinuity | window)
```

Where:
- **P(window opens)**: Crisis develops to acute phase
- **P(discontinuity | window)**: Crisis produces a discontinuity (any type)
- **P(non-event | window)** = 1 - P(discontinuity | window): Crisis de-escalates without discontinuity — these are simply non-occurrences of the event

Within the discontinuity cases, resolutions partition the space:
```
P(resolution_i) where Σ P(resolution_i) = 1.0 across all discontinuity types
```

### Example: India-Pakistan Military Conflict

The cleanest example of correct Type 3 structure:

| Component | Value | Meaning |
|-----------|-------|---------|
| P(window) | 2.5% | Acute crisis develops |
| P(discontinuity \| window) | 35% | Military conflict occurs |
| P(non-event \| window) | 65% | Crisis de-escalates — not modeled as resolution |
| P(event) | 0.9% | Annual probability of military conflict |

The event IS military conflict. Non-conflict outcomes are non-events. Aftermath branches (limited, major, nuclear) describe different intensities of the discontinuity that occurred.

See [[events/geopolitical/india-pakistan-military-conflict]] for the full specification.

### Example: Taiwan Conflict (Multiple Discontinuity Types)

Taiwan is more complex because there are two genuinely distinct discontinuity types:

| Component | Value | Meaning |
|-----------|-------|---------|
| P(window) | 3% | Acute crisis develops |
| P(discontinuity \| window) | 65% | Military conflict OR great power settlement |
| P(non-event \| window) | 35% | Crisis de-escalates — not modeled |
| P(event) | ~2% | Annual probability of discontinuity |

Within the 65% discontinuity cases:
- Military conflict: 65% of discontinuities
- Great power settlement: 35% of discontinuities

Both are genuine discontinuities — both fundamentally change Taiwan's status. They're different *types* of system break, not "discontinuity vs. non-discontinuity."

See [[events/geopolitical/taiwan-conflict]] for the full specification.

### Why This Matters

The old pattern included "status quo restoration" as a resolution. This was wrong because:

1. **Catalog coherence**: The event catalog enumerates discontinuities. Including non-discontinuities as resolutions conflates "event types" with "all possible outcomes."

2. **Probability interpretation**: If P(event) = 2% and one resolution is "nothing changed," then P(event) doesn't mean what it should mean.

3. **Simulation mechanics**: When an event fires, it should produce impacts. "Status quo restoration" produces no meaningful impact — so why is it firing?

The correct approach: non-discontinuity outcomes are captured in P(non-event | window). They don't appear in the resolution set because they're not resolutions — they're non-occurrences.
## 1. Resolution Probability Defaults

### The Default: Uniform Distribution

When specifying resolution probabilities for a Type 3 event, **start with uniform distribution across plausible outcomes**.

| Resolutions | Default Probabilities |
|-------------|----------------------|
| 2 outcomes | 50% / 50% |
| 3 outcomes | 33% / 33% / 33% |
| 4 outcomes | 25% / 25% / 25% / 25% |

This is not a claim that outcomes are equally likely. It is an acknowledgment that we lack grounds for confident differentiation.

### What Justifies Deviation

Deviation from uniform requires **structural asymmetry** — features of the situation that constrain outcomes independent of actor preferences.

**Valid justifications:**

| Type | Example | Deviation |
|------|---------|-----------|
| Activation energy asymmetry | Military action requires mobilization, logistics, domestic alignment; accommodation requires only agreement | Weight toward status quo/accommodation |
| Irreversibility asymmetry | Some outcomes foreclose others; reversible options stay open longer | Weight toward reversible options |
| Observable commitment | Public commitments, mobilized forces, burned bridges | Weight toward committed direction |
| Structural lock-in | Geography, economics, or institutions that constrain choice space | Weight per constraint direction |

**Invalid justifications:**

| Claim | Why Invalid |
|-------|-------------|
| "Experts think X is more likely" | Expert intuition ≠ structural constraint; experts have poor track records on small-N decisions |
| "Historical analogies suggest X" | Analogies rarely transfer; different actors, contexts, constraints |
| "I've read extensively about this" | Domain knowledge ≠ forecasting ability; you understand mechanisms, not actor decisions |
| "It would be irrational to do X" | Actors may have different information, preferences, or rationality than you assume |

### Deviation Limits

Even with valid structural justification, **cap deviation at 2:1 ratios** without extraordinary evidence.

| Resolutions | Uniform | Maximum Deviation |
|-------------|---------|-------------------|
| 2 outcomes | 50/50 | 67/33 |
| 3 outcomes | 33/33/33 | 50/25/25 or similar |

Rationale: Structural arguments constrain but rarely determine. A 2:1 ratio represents "notably more likely" without claiming precision we don't have.

### Documentation Requirement

Every non-uniform resolution specification must include:

```yaml
resolution_probability_rationale:
  default: "uniform (33/33/33)"
  specified: "45/30/25"
  justification: |
    [Specific structural asymmetry cited]
  confidence: "weak/moderate"  # never "strong" for Type 3
```

---

## 2. Aftermath Specification Emphasis

### Why Aftermath Is Tractable

Once we condition on "conflict occurred" or "accommodation reached," we can reason structurally:

- **Supply chains**: Semiconductor production locations, shipping routes, inventory levels — observable
- **Financial linkages**: Cross-border exposures, currency dependencies, trade volumes — documented
- **Escalation logic**: What military options exist, what thresholds matter — analyzable
- **Precedent effects**: How similar past events affected related variables — comparable

This is where domain expertise pays off. Understanding the *mechanisms* of consequence transmission is tractable even when predicting actor choices is not.

### Structure Aftermath Branches Per Resolution

Each resolution should have its own aftermath specification. The resolution determines *what happened*; the aftermath determines *what follows*.

```yaml
resolutions:
  - id: military_conflict
    probability: 0.33
    aftermath_branches:
      - id: limited_conflict
        probability: 0.60
        description: "Blockade or limited strikes; no invasion"
        # detailed impacts here
      - id: full_invasion
        probability: 0.40
        description: "Amphibious assault and occupation attempt"
        # detailed impacts here
        
  - id: negotiated_accommodation
    probability: 0.33
    aftermath_branches:
      - id: stable_settlement
        probability: 0.50
        # ...
      - id: unstable_settlement
        probability: 0.50
        # ...
```

### Aftermath Probability Limits

Aftermath branch probabilities have **more structural grounding** than resolution probabilities — military logistics, escalation dynamics, supply chain constraints, and historical precedent provide traction. But they are not fully tractable. The same epistemic discipline applies, with relaxed limits.

**Default**: When structural reasoning doesn't clearly differentiate branches, use uniform or near-uniform probabilities.

**Deviation limits**: Cap at **3:1 ratios** without strong structural justification. This is more permissive than the 2:1 limit for resolution probabilities, reflecting the higher tractability.

| Branches | Uniform | Maximum Deviation |
|----------|---------|-------------------|
| 2 branches | 50/50 | 75/25 |
| 3 branches | 33/33/33 | 60/20/20 or similar |

**What justifies deviation**:

| Justification Type | Example | Validity |
|--------------------|---------|----------|
| Military logistics | "Amphibious assault requires 6 months preparation; blockade can begin immediately" | Valid — observable constraint |
| Escalation dynamics | "Limited conflict preserves off-ramps; full invasion forecloses them" | Valid — structural asymmetry |
| Precedent analysis | "Historical blockades rarely escalate to invasion within 6 months" | Partially valid — context may differ |
| Expert intuition | "Analysts believe full invasion is unlikely" | Invalid — same problem as resolution probabilities |

**Documentation requirement**: Same as resolution probabilities. Every non-uniform aftermath specification needs a rationale block:

```yaml
aftermath_probability_rationale:
  default: "uniform (50/50)"
  specified: "70/30"
  justification: |
    [Specific structural reasoning]
  confidence: "weak/moderate"
```

### Cascade Trigger Probabilities

Aftermath branches may specify **cascade triggers** — other events whose windows open or whose probabilities increase as a consequence. Some cascade triggers involve small-N actor decisions.

**Example**: "If full Taiwan invasion occurs, what is the probability the US enters direct military conflict?"

This is a small-N decision (US leadership choosing intervention). The same intractability applies:
- No base rate for "US military intervention in Taiwan conflict"
- Radical context-dependence (who is president, domestic political situation, alliance posture)
- Strategic interaction (intervention decision affects PRC decisions, which affect intervention calculus)

**Treatment**: Cascade trigger probabilities involving actor decisions receive the **same entropy-maximization treatment** as resolution probabilities.

| Cascade Type | Tractability | Treatment |
|--------------|--------------|-----------|
| Structural/automatic | High | Specify based on mechanism (e.g., "supply chain disruption triggers shortages") |
| Actor decision (single) | Low | Default toward 50%, cap deviation at 2:1 |
| Actor decision (multiple parties) | Very Low | Default toward uniform across plausible responses |

**Documentation requirement**: Cascade triggers involving actor decisions must include rationale:

```yaml
cascade_triggers:
  - event_id: us_china_direct_conflict
    window_opens: true
    probability: 0.50
    probability_rationale: |
      US intervention is a small-N actor decision with low tractability.
      Structural factors that might push toward intervention:
      - Taiwan Relations Act creates political pressure
      - Credibility concerns vis-à-vis other allies
      Structural factors that might push against:
      - Nuclear escalation risk
      - Economic interdependence costs
      No clear structural asymmetry; defaulting to 50%.
      Subject to sensitivity analysis.
```

**Common mistake**: Treating cascade triggers as "downstream consequences" exempt from epistemic discipline. They are not. If the trigger depends on an actor decision, the intractability follows the decision, not the event structure.

### Link to Aftermath Framework

See [[methodology/reference/aftermath-branches]] for:
- Full aftermath specification structure
- Duration and exit condition modeling
- Factor modification syntax
- Examples across event types

---

## 3. Sensitivity Analysis Framing

### Run Scenarios by Resolution

Rather than varying resolution probabilities (which have no ground truth to converge toward), **run the simulation conditional on each resolution** and examine the consequences.

This produces insight like:
- "If Taiwan conflict occurs, tail risk of civilizational stress increases by X%"
- "The difference between limited and full conflict scenarios is Y impact on Z variable"
- "Accommodation scenarios show W pattern of regional dynamics"

### What Sensitivity Analysis Can Answer

| Question Type | Answerable? | Method |
|---------------|-------------|--------|
| "What happens if X resolution occurs?" | Yes | Conditional simulation runs |
| "How do aftermath assumptions affect outcomes?" | Yes | Vary aftermath parameters |
| "Which events drive tail outcomes?" | Yes | Event contribution analysis |
| "What is the integrated probability of outcome Y?" | **Partially** | Requires resolution probability assumptions |

### What Sensitivity Analysis Cannot Answer

Sensitivity analysis cannot tell you the "true" resolution probabilities. It can tell you:
- How much your conclusions depend on resolution probability assumptions
- What the world looks like conditional on different resolutions
- Which parameters matter most for tail outcomes

If conclusions are highly sensitive to Type 3 resolution probabilities, the honest response is to report results conditionally, not to invest more effort in probability estimation.

---

## 4. Worked Example: Taiwan Conflict
This example demonstrates Level 1 specification of a Type 3 event with multiple discontinuity types. See [[events/geopolitical/taiwan-conflict]] for the full event file.

For a simpler example with a single discontinuity type, see [[events/geopolitical/india-pakistan-military-conflict]].

### Window Definition

The event requires a **crisis window** to open before discontinuity is sampled.

```yaml
window:
  description: "Acute crisis phase where military action or major diplomatic shift becomes imminent"
  preconditions:
    - "Sustained elevation of F_GPT and F_EAS factors"
    - "Triggering incident (election outcome, sovereignty assertion, military accident)"
  annual_probability: 0.03
  rationale: |
    Historical frequency of Taiwan Strait crises reaching acute phase: 
    roughly 3-4 per century when baseline tensions are elevated.
    Level 1 estimate; would benefit from systematic crisis cataloging.
```

Window probability is *moderate tractability* — we can look at historical crisis frequency, though context changes limit precision.

### Probability Decomposition

```yaml
probability_structure:
  window_probability: 0.03
  discontinuity_given_window: 0.65
  non_event_given_window: 0.35  # crises that de-escalate — NOT a resolution
  annual_event_probability: 0.02  # 3% × 65% ≈ 2%
  
  rationale: |
    Of historical Taiwan Strait crises (1954-55, 1958, 1995-96), two of three
    produced military operations. The 1995-96 crisis de-escalated without
    combat — a non-event in our framework, not a "status quo resolution."
    
    The 65% discontinuity rate reflects:
    - Historical precedent of PRC willingness to use force
    - Elevated current stakes (semiconductors, great power competition)
    - Some crises will de-escalate through crisis management (the 35%)
```

### Resolution Options (Discontinuity Types Only)

Once a discontinuity occurs (65% of windows), it takes one of two forms:

```yaml
resolutions:
  - id: military_conflict
    probability: 0.65
    description: "PRC initiates military action (blockade, strikes, or invasion)"
    
  - id: great_power_settlement
    probability: 0.35
    description: |
      US brokers binding settlement between PRC and Taiwan.
      Agreement backed by great power guarantees, materially changing
      Taiwan's status, security arrangements, or governance framework.

resolution_probability_rationale:
  default: "uniform (50/50)"
  specified: "65/35"
  justification: |
    Settlement faces higher structural barriers than military conflict:
    
    Military conflict barriers:
    - Activation energy for military action
    - Nuclear escalation risk
    - Economic costs
    
    Settlement barriers (all of the above, plus):
    - Requires US willingness to reduce its position
    - Requires PRC trust in US commitments
    - Requires Taiwan acquiescence
    - Must find formula acceptable to all three parties
    
    Military conflict requires one actor to decide to act.
    Settlement requires three actors to agree. This structural
    asymmetry justifies weighting military conflict higher.
  confidence: "moderate — structural reasoning, not historical base rate"
```

**Note**: There is no "status quo restoration" resolution. Crises that de-escalate without producing either military conflict or settlement are non-events — they're captured in the 35% non-discontinuity rate, not as a resolution type.

### Aftermath Branches

This is where analytical effort concentrates. Each resolution has distinct aftermath trajectories.

**Military Conflict Aftermath:**

```yaml
# Under resolution: military_conflict
aftermath_branches:
  - id: limited_conflict
    probability: 0.55
    description: |
      Blockade or limited strikes without amphibious invasion.
      Semiconductor supply severely disrupted for 1-3 years.
      No direct US-China military engagement.
    factor_modifications:
      F_GPT: +0.60
      F_EAS: +0.70
      F_FIN: +0.40
      F_TECH: +0.50
    duration:
      type: decaying
      half_life: 4
      floor: 0.15
    impact_vector:
      global.semiconductor_supply: -0.70
      global.trade_volume: -0.25
      taiwan.gdp: -0.40
      taiwan.sovereignty: "contested"
      
  - id: full_invasion
    probability: 0.30
    description: |
      Amphibious assault and occupation attempt.
      Catastrophic semiconductor disruption (TSMC facilities damaged/destroyed).
      High risk of US military involvement.
    factor_modifications:
      F_GPT: +0.90
      F_EAS: +0.85
      F_FIN: +0.60
      F_TECH: +0.80
    duration:
      type: decaying
      half_life: 8
      floor: 0.25
    triggers:
      - event: us_china_direct_conflict
        window_opens: true
        probability: 0.50
        probability_rationale: |
          US intervention is small-N actor decision; same intractability applies.
          No clear structural asymmetry — defaulting to 0.50.
          See full specification for detailed reasoning.
    impact_vector:
      global.semiconductor_supply: -0.95
      global.trade_volume: -0.40
      taiwan.gdp: -0.70
      taiwan.sovereignty: "occupied"
      
  - id: nuclear_escalation
    probability: 0.15
    description: |
      Conflict escalates to nuclear weapons use (tactical or demonstration).
      Civilizational-scale consequences.
    factor_modifications:
      F_GPT: +1.50
      F_EAS: +1.20
      F_FIN: +1.00
      F_HLTH: +0.30
    duration:
      type: persistent
      exit_conditions: null  # permanent regime shift
    impact_vector:
      global.nuclear_taboo: "broken"
      global.trade_volume: -0.60
      # additional catastrophic impacts

aftermath_probability_rationale:
  justification: |
    Limited conflict weighted higher than full invasion based on:
    - Amphibious assault logistics favor blockade-first approach
    - Invasion triggers near-certain US response; limited action may not
    - TSMC value as intact asset vs. destroyed
    Nuclear escalation weighted low but non-negligible given:
    - Stated PRC no-first-use policy (though may not hold under existential threat)
    - US extended deterrence ambiguity
    Level 1 estimate; aftermath probabilities more defensible than resolution probs.
```

**Great Power Settlement Aftermath:**

```yaml
# Under resolution: great_power_settlement
aftermath_branches:
  - id: stable_framework
    probability: 0.40
    description: |
      Durable settlement backed by credible great power guarantees.
      Explicit US security commitment, PRC commitment to non-use of force,
      Taiwan constraints on independence options.
    factor_modifications:
      F_GPT: -0.15
      F_EAS: -0.20
    duration:
      type: maintenance_required
      annual_failure_probability: 0.05
    impact_vector:
      taiwan.sovereignty: "defined_autonomy_guaranteed"
      global.great_power_tension: -0.15
      
  - id: unstable_framework
    probability: 0.60
    description: |
      Settlement reached under crisis pressure with structural weaknesses.
      Agreement is binding but contains ambiguities, lacks robust enforcement,
      or faces domestic opposition.
    factor_modifications:
      F_GPT: +0.10
      F_EAS: +0.15
    duration:
      type: maintenance_required
      annual_failure_probability: 0.12
    impact_vector:
      taiwan.sovereignty: "formally_redefined_unstable"

aftermath_probability_rationale:
  justification: |
    Unstable framework weighted higher because:
    - Crisis-driven agreements prioritize speed over durability
    - Three-party agreements are inherently harder to stabilize
    - Each party has domestic audiences that may reject compromise
    - Historical precedent: 1992 Consensus was ambiguous and contested
```

### What This Example Shows

1. **Non-discontinuities are non-events** — the 35% of windows that de-escalate don't appear as resolutions
2. **Resolutions are discontinuity types** — military conflict and great power settlement are both genuine system breaks
3. **Analytical effort is in aftermath branches** — supply chain impacts, escalation triggers, duration modeling
4. **Aftermath probabilities have more grounding** — military logistics, precedent analysis, structural constraints
5. **Documentation traces reasoning** — rationale blocks explain each choice

---

## 5. Common Mistakes
| Mistake | Why It's Wrong | Correction |
|---------|----------------|------------|
| **Including "status quo restoration" as a resolution** | Non-discontinuities are non-events, not resolutions. The event catalog enumerates discontinuities; "nothing changed" isn't a discontinuity type. | Capture non-discontinuity outcomes in P(non-event \| window). Resolutions partition only the discontinuity space. |
| Investing 10 hours in resolution probability research | Time doesn't create tractability; small-N decisions remain opaque | Invest those hours in aftermath specification |
| "Experts assess 60% conflict probability" | Expert intuitions on small-N decisions have poor track records | Use structural constraints, not intuitions |
| Adjusting probabilities based on recent news | News updates your *understanding* but doesn't make the decision predictable | Update preconditions or aftermath branches, not resolution probs |
| Precise probabilities (e.g., 37.5%) | False precision; implies calibration that doesn't exist | Round to nearest 5% or 10%; use uniform when possible |
| Treating historical analogies as base rates | Cuban Missile Crisis ≠ Taiwan 2030; actors and contexts differ radically | Use analogies for mechanism insight, not probability calibration |
| Skipping aftermath specification because resolution is uncertain | Uncertainty about *which* outcome makes consequence analysis *more* valuable | Specify full aftermath for each resolution |
| Confusing "resolutions" with "all possible outcomes" | Resolutions are discontinuity types. "Crisis de-escalates" is a non-event, not a resolution. | Ask: "Does this resolution represent a genuine system break?" If no, it's not a resolution. |
## Checklist for Type 3 Event Specification
Before finalizing a Type 3 event:

- [ ] Window preconditions defined with structural reasoning
- [ ] Window probability grounded in historical crisis frequency
- [ ] Discontinuity probability specified (what fraction of windows produce discontinuities)
- [ ] Non-discontinuity outcomes treated as non-events, NOT as resolutions
- [ ] Resolution options are mutually exclusive discontinuity types that sum to 1.0
- [ ] Each resolution represents a genuine system break (not "status quo restoration")
- [ ] Resolution probabilities are uniform OR deviation is structurally justified and documented
- [ ] Deviation does not exceed 2:1 ratio without extraordinary evidence
- [ ] Each resolution has aftermath branches specified
- [ ] Aftermath branches include factor modifications, duration, and impact vectors
- [ ] Aftermath probability rationale documents structural reasoning
- [ ] High-consequence branches include cascade triggers where appropriate
- [ ] Cascade trigger probabilities involving actor decisions use entropy maximization (default ~50%, documented rationale for deviation)
## Related Documents
- [[methodology/reference/causal-types]] — Type 3 definition (event-type framework)
- [[methodology/reference/aftermath-branches]] — Full aftermath specification guide
- [[methodology/concepts/tractability-boundaries]] — Why resolution probabilities are intractable
- [[methodology/concepts/entropy-maximization]] — Default principle for uncalibrated parameters
- [[methodology/concepts/small-n-actor-problem]] — Deep dive on small-N forecasting limits

### Worked Examples

- [[events/geopolitical/india-pakistan-military-conflict]] — **Primary example**: Single discontinuity type (military conflict)
- [[events/geopolitical/taiwan-conflict]] — Multiple discontinuity types (military conflict vs. great power settlement)

---

*Last updated: December 2025 (Task 1.7 revision)*