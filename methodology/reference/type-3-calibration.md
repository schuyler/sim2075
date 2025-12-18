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

| Component | Tractability | Treatment |
|-----------|--------------|-----------|
| Window preconditions | Moderate | Structural reasoning about tension escalation |
| Window probability | Moderate | Historical frequency of crises reaching critical phase |
| Resolution probabilities | **Low** | Entropy maximization → uniform or weakly-informed |
| Aftermath given each resolution | Moderate-High | Supply chain data, financial precedents, escalation logic |

For the underlying reasoning, see:
- [[methodology/concepts/tractability-boundaries]] — Why resolution probabilities are low-tractability
- [[methodology/concepts/entropy-maximization]] — The default principle for intractable parameters
- [[methodology/concepts/small-n-actor-problem]] — Why small-N actor decisions resist estimation

---

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

Note: Aftermath branch probabilities *within* a resolution are also subject to entropy maximization, but often have more structural grounding than the resolution itself.

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

This example demonstrates Level 1 specification of a Type 3 event. See [[events/geopolitical/taiwan-conflict]] for the full event file.

### Window Definition

The event requires a **crisis window** to open before resolution is sampled.

```yaml
window:
  description: "Acute crisis phase where military action becomes imminent possibility"
  preconditions:
    - "Sustained elevation of F_GPT and F_EAS factors"
    - "Triggering incident (election outcome, sovereignty assertion, military accident)"
  annual_probability_given_preconditions: 0.03
  rationale: |
    Historical frequency of Taiwan Strait crises reaching acute phase: 
    roughly 3-4 per century when baseline tensions are elevated.
    Level 1 estimate; would benefit from systematic crisis cataloging.
```

Window probability is *moderate tractability* — we can look at historical crisis frequency, though context changes limit precision.

### Resolution Options

```yaml
resolutions:
  - id: military_conflict
    probability: 0.33
    description: "PRC initiates military action (blockade, strikes, or invasion)"
    
  - id: negotiated_accommodation  
    probability: 0.33
    description: "Crisis de-escalates through diplomatic engagement; status quo modified"
    
  - id: status_quo_restoration
    probability: 0.33
    description: "Crisis de-escalates without resolution; return to prior tensions"

resolution_probability_rationale:
  default: "uniform (33/33/33)"
  specified: "33/33/33"
  justification: |
    No structural asymmetry identified at Level 1 that justifies deviation.
    Military action has higher activation energy (mobilization, logistics),
    but PRC has been investing in rapid-strike capabilities that reduce this gap.
    Accommodation requires both parties to accept terms, which faces its own barriers.
    Defaulting to uniform pending Level 2 analysis of structural constraints.
  confidence: "n/a (using default)"
```

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
        probability: 0.60
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

**Negotiated Accommodation Aftermath:**

```yaml
# Under resolution: negotiated_accommodation
aftermath_branches:
  - id: stable_new_framework
    probability: 0.40
    description: |
      New cross-strait framework accepted by both parties.
      Reduced tensions, increased economic integration.
    factor_modifications:
      F_GPT: -0.10  # tension reduction
      F_EAS: -0.15
    duration:
      type: maintenance_required
      annual_failure_probability: 0.05
    impact_vector:
      taiwan.sovereignty: "ambiguous_but_stable"
      
  - id: unstable_settlement
    probability: 0.60
    description: |
      Face-saving de-escalation without fundamental resolution.
      Tensions remain elevated; future crisis more likely.
    factor_modifications:
      F_GPT: +0.15
      F_EAS: +0.20
    duration:
      type: decaying
      half_life: 5
      floor: 0.10
```

**Status Quo Restoration Aftermath:**

```yaml
# Under resolution: status_quo_restoration
aftermath_branches:
  - id: default
    probability: 1.0
    description: |
      Crisis passes without resolution. Return to baseline tensions
      with modest elevation from crisis memory.
    factor_modifications:
      F_GPT: +0.10
      F_EAS: +0.15
    duration:
      type: decaying
      half_life: 3
      floor: 0.05
```

### What This Example Shows

1. **Resolution probabilities are uniform** — no structural justification for deviation at Level 1
2. **Analytical effort is in aftermath branches** — supply chain impacts, escalation triggers, duration modeling
3. **Aftermath probabilities have more grounding** — military logistics, precedent analysis, structural constraints
4. **Documentation traces reasoning** — rationale blocks explain each choice

---

## 5. Common Mistakes

| Mistake | Why It's Wrong | Correction |
|---------|----------------|------------|
| Investing 10 hours in resolution probability research | Time doesn't create tractability; small-N decisions remain opaque | Invest those hours in aftermath specification |
| "Experts assess 60% conflict probability" | Expert intuitions on small-N decisions have poor track records | Use structural constraints, not intuitions |
| Adjusting probabilities based on recent news | News updates your *understanding* but doesn't make the decision predictable | Update preconditions or aftermath branches, not resolution probs |
| Precise probabilities (e.g., 37.5%) | False precision; implies calibration that doesn't exist | Round to nearest 5% or 10%; use uniform when possible |
| Treating historical analogies as base rates | Cuban Missile Crisis ≠ Taiwan 2030; actors and contexts differ radically | Use analogies for mechanism insight, not probability calibration |
| Skipping aftermath specification because resolution is uncertain | Uncertainty about *which* outcome makes consequence analysis *more* valuable | Specify full aftermath for each resolution |

---

## Checklist for Type 3 Event Specification

Before finalizing a Type 3 event:

- [ ] Window preconditions defined with structural reasoning
- [ ] Window probability grounded in historical crisis frequency
- [ ] Resolution options are mutually exclusive and collectively exhaustive
- [ ] Resolution probabilities are uniform OR deviation is structurally justified and documented
- [ ] Deviation does not exceed 2:1 ratio without extraordinary evidence
- [ ] Each resolution has aftermath branches specified
- [ ] Aftermath branches include factor modifications, duration, and impact vectors
- [ ] Aftermath probability rationale documents structural reasoning
- [ ] High-consequence branches include cascade triggers where appropriate

---

## Related Documents

- [[methodology/reference/causal-types]] — Type 3 definition (event-type framework)
- [[methodology/reference/aftermath-branches]] — Full aftermath specification guide
- [[methodology/concepts/tractability-boundaries]] — Why resolution probabilities are intractable
- [[methodology/concepts/entropy-maximization]] — Default principle for uncalibrated parameters
- [[methodology/concepts/small-n-actor-problem]] — Deep dive on small-N forecasting limits
- [[events/geopolitical/taiwan-conflict]] — Full worked example

---

*Completed: December 2025 (Task 1.1)*