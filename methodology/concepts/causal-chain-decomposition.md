---
title: causal-chain-decomposition
type: note
permalink: methodology/concepts/causal-chain-decomposition
tags:
- methodology
- concepts
- causal-types
- epistemology
- open-question
---

# Causal Chain Decomposition

**Status:** Concept note — captures an insight for future development. Not yet integrated into event specification workflow.

**Origin:** Emerged from [[methodology/reference/calibration-anchors]] revision (December 2025). Attempting to classify historical reference events by causal type revealed that many events resist single-type classification because they involve multi-stage causal chains with different types at each stage.

---

## The Problem

The Type 1/2/3 taxonomy (see [[methodology/reference/causal-types]]) treats causal type as a property of *events*. But many discontinuities involve causal chains where:

- **Enabling conditions** accumulate via Type 2 pressure dynamics
- **Triggers** may be Type 1 stochastic or Type 3 contingent
- **Resolutions** depend on Type 3 actor decisions or Type 2 emergent dynamics

Assigning a single type to the whole event forces false choices and creates internal inconsistencies.

---

## Examples

### 1973 Oil Shock

| Stage | Type | Mechanism |
|-------|------|-----------|
| **Enabling conditions** | Type 2 | OPEC market power accumulated; Arab-Israeli tensions escalated over decades |
| **Trigger** | Type 1/3 | Yom Kippur War — Egypt/Syria decision to attack (T3), timing partly stochastic (T1) |
| **Resolution** | Type 3 | OPEC embargo decision — small-N actor choice by oil ministers |

Classifying this as "Type 1 stochastic" (as attempted in calibration-anchors) obscures that the *window* for an oil weapon was a Type 2 threshold phenomenon, and the *use* of that weapon was Type 3 contingent.

### Korean War (1950)

| Stage | Type | Mechanism |
|-------|------|-----------|
| **Enabling conditions** | Type 2 | Soviet armament of DPRK; US signaling (Acheson speech); post-colonial vacuum; PRC victory securing northern border |
| **Trigger** | Type 3 | Kim Il-sung's decision to invade — contingent on Stalin's approval |
| **Resolution** | Type 3 | US decision to intervene; PRC decision to enter; armistice negotiations |

The invasion was not independent of accumulated structural conditions. Framing it as purely "Type 3 contingent" obscures that the window was largely determined by Type 2 dynamics.

### Taiwan Conflict (prospective)

| Stage | Type | Mechanism |
|-------|------|-----------|
| **Enabling conditions** | Type 2 | US-China tension accumulation; PLA capability development; economic interdependence erosion |
| **Trigger** | Type 1/3 | Incident or provocation — could be accidental (T1) or deliberate (T3) |
| **Resolution** | Type 3 | Escalation/de-escalation choices by Xi, US President, Taiwan leadership |

The current specification in [[events/geopolitical/taiwan-conflict]] models this as Type 3 with window preconditions — which implicitly captures the decomposition. But the Type 3 label on the event as a whole understates how much of the probability comes from Type 2 pressure accumulation.

### Pakistan State Failure

| Stage | Type | Mechanism |
|-------|------|-----------|
| **Enabling conditions** | Type 2 | Water stress, debt accumulation, institutional decay, internal conflict |
| **Trigger** | Type 2 | Threshold crossing — no single decision point |
| **Resolution** | Type 2 | Collapse dynamics are emergent, not contingent on specific actor choices |

This is a "pure Type 2" event — all stages follow threshold/pressure dynamics. No small-N actor decisions gate the outcome. This is why it can be modeled as Type 2 without internal contradiction.

---

## The Insight

**Type 3 events are typically Type 2 in their enabling conditions.** The "window opens" language in Type 3 specifications is doing the same analytical work as "threshold approached" in Type 2 specifications. The difference is not in how windows open — it's in what happens after:

| After threshold... | Classification | Example |
|--------------------|----------------|---------|
| Outcome is mechanistic/emergent | Type 2 | AMOC collapse, state failure |
| Outcome depends on tractable actor choices | Still Type 2 | Mass behavior, market dynamics |
| Outcome depends on intractable small-N choices | Type 3 | Great power crises, coordinated agreements |

**Pure Type 1 events may not exist.** Events that appear truly stochastic (Poisson-like arrival, no observable pressure accumulation) include:
- Natural disasters (volcanic eruptions, earthquakes, asteroid impacts)
- Novel pathogen emergence (zoonotic spillover timing)
- Certain technological breakthroughs (eureka moments)

But see "The Epistemic Nature of Type 1" below — these may be Type 2 processes with unobservable pressure variables. What we call "Type 1" may be an epistemic category (we can't see the pressure) rather than an ontological one (no pressure exists).

---

## Implications for Modeling

### Current Approach (v1.0)

Assign single type to events. Accept that this is a simplification. Use "Type 1/2 hybrid" or "Type 2/3" labels where needed. Document the limitation.

**Advantage:** Simpler specification workflow; tractable for Level 1 estimates.

**Disadvantage:** Obscures causal structure; may produce inconsistent probability estimates when enabling conditions are shared across events.

### Potential Future Approach (v2.0+)

Decompose events into stages with separate type assignments:

```yaml
event: taiwan_conflict
causal_chain:
  enabling:
    type: 2
    pressure_variables: [us_china_tension, pla_capability, economic_decoupling]
    threshold: composite > 75
  trigger:
    type: 1/3
    stochastic_component: incident_arrival_rate
    contingent_component: deliberate_provocation
  resolution:
    type: 3
    actors: [prc_leadership, us_leadership, taiwan_leadership]
    branches: [military_conflict, accommodation, coercion_only, status_quo]
```

**Advantage:** More accurate causal representation; enables modeling shared enabling conditions across events; clarifies where epistemic uncertainty concentrates.

**Disadvantage:** Significantly more complex specification; may not improve predictions given uncertainty at each stage; requires rethinking factor loading architecture.

### Correlation Implications

If Type 3 events share Type 2 enabling conditions, their correlations should reflect this:

- Taiwan conflict and Korean crisis both depend on `us_china_tension` (Type 2 accumulation)
- If we model them as independent Type 3 events with separate window probabilities, we may understate their correlation
- The factor model partially captures this (both load on F_GPT, F_EAS), but factor loadings were designed for the event-as-unit abstraction

This is related to the double-counting concern in [[methodology/project/tasks]] (Task 3.2).

---

## The Epistemic Nature of Type 1

A further refinement: many apparently Type 1 events may be Type 2 processes with **unobservable pressure variables**.

### The Pinatubo Example

Mount Pinatubo (1991) appears stochastic from the surface. But underground:
- Magma accumulated in the chamber over centuries
- Pressure built against the rock cap
- A threshold was crossed when pressure exceeded containment strength
- Eruption followed

This is textbook Type 2 dynamics — pressure accumulation toward threshold, then rapid transition. It only *appears* Type 1 because the pressure variables (magma volume, chamber pressure, rock integrity) are invisible until days before eruption.

### Generalization

| Apparent Type 1 | Hidden Type 2 mechanism |
|-----------------|-------------------------|
| Volcanic eruption | Magma pressure accumulation |
| Earthquake | Tectonic strain accumulation along fault |
| Novel pandemic | Viral evolution toward human transmissibility; habitat encroachment increasing spillover probability |
| Technology breakthrough | Capability accumulation across research frontier; threshold = sufficient pieces in place |

The "Poisson-like arrival" we observe may be the visible signature of many independent Type 2 processes whose pressure variables we cannot track, crossing their thresholds at times that appear random to us.

### Implication

**The Type 1/Type 2 distinction is epistemic, not ontological — but this doesn't change how we model.**

Pinatubo has Type 2 mechanics underneath, but for modeling purposes it's functionally random. We can't observe magma chamber pressure in real time across thousands of volcanoes. Historical base rates are the right tool.

The epistemic framing leads to a three-way distinction:

| Category | Ontology | Epistemology | Modeling approach |
|----------|----------|--------------|-------------------|
| **Ontologically stochastic** | No pressure process exists (on Earth) | Irreducibly random | Historical base rate |
| **Epistemically stochastic** | Pressure process exists but unobservable | Appears random | Historical base rate |
| **Observable accumulation** | Pressure process exists and trackable | Predictable buildup | Pressure function |

**Ontologically stochastic** (true Type 1):
- Asteroid/meteor impacts — trajectory determined by orbital mechanics, not earthly pressure
- Extraterrestrial contact — no accumulating process on Earth
- Possibly novel pandemic emergence — though habitat encroachment creates some pressure signal

**Epistemically stochastic** (Type 2 underneath, modeled as Type 1):
- Volcanic eruptions — magma pressure real but unobservable at scale
- Earthquakes — tectonic strain real but prediction remains intractable
- Many technology breakthroughs — capability accumulation real but threshold unclear

**Observable accumulation** (true Type 2):
- State failure — debt, instability, water stress are measurable
- Climate tipping points — temperature, ice extent, AMOC strength are tracked
- Financial crises — leverage, credit spreads, imbalances are visible

The practical consequence: for v1.0, both ontologically and epistemically stochastic events use the same modeling approach (historical base rates). The distinction matters for:
- Whether proxy variables might exist that could upgrade an event to Type 2
- How we interpret base rate stability over time (true randomness vs. changing unobserved pressure)
- Whether improved observation technology could change classification

### Practical Consequence

When specifying a "Type 1" event, ask:
1. Is there a plausible hidden pressure mechanism?
2. Are *any* proxy variables observable that might indicate pressure?
3. If proxies exist, should this be reclassified as Type 2?

Example: Pandemic emergence looks Type 1, but:
- Deforestation rates (habitat encroachment) are observable
- Wet market activity is observable  
- Lab biosafety incidents are partially observable

A sophisticated model might treat pandemic risk as Type 2 with these pressure variables, rather than pure Type 1 with fixed base rate. For v1.0 we use Type 1, but this is a simplification, not a fact about the world.

---

## Open Questions

1. **Does decomposition improve predictions?** The extra complexity is only justified if it produces meaningfully different simulation outputs. This could be tested in sensitivity analysis (Phase 3).

2. **How to handle shared enabling conditions?** If multiple Type 3 events share the same Type 2 pressure buildup, should the enabling stage be modeled once with multiple contingent branches, rather than as separate events?

3. **Where does uncertainty concentrate?** If Type 2 enabling conditions are relatively tractable (we can estimate pressure accumulation) and Type 3 resolutions are intractable (we can't predict actor choices), should we invest more in modeling the former and use maximum entropy for the latter?

4. **Interaction with aftermath modeling.** Event resolutions feed back into state variables, which affect enabling conditions for future events. The current architecture handles this, but decomposition might require rethinking how aftermaths propagate.

---

## Recommendation

For v1.0: Continue with event-level type assignments. Note hybrid types explicitly. Accept the simplification.

Revisit this concept during Phase 3 sensitivity analysis. If simulations show that events with shared enabling conditions produce implausible correlation structures, decomposition may be worth the complexity cost.

---

## Cross-References

- [[methodology/reference/causal-types]] — Current Type 1/2/3 definitions
- [[methodology/reference/calibration-anchors]] — Where this insight emerged; historical examples with implicit decomposition
- [[methodology/reference/type-3-calibration]] — Type 3 specification guidance (window-resolution structure)
- [[methodology/concepts/small-n-actor-problem]] — Why Type 3 resolutions are intractable
- [[methodology/concepts/factor-correlation-structure]] — How factor model captures event correlations
- [[methodology/project/tasks]] — Task 3.2 (double-counting) is related

---

*Created: December 2025*