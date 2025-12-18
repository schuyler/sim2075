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

**Pure Type 1 events are rarer than they appear.** Truly stochastic events (Poisson-like arrival, no pressure accumulation) may be limited to:
- Natural disasters (volcanic eruptions, earthquakes, asteroid impacts)
- Novel pathogen emergence (zoonotic spillover timing)
- Certain technological breakthroughs (eureka moments)

Many events classified as Type 1 have Type 2 enabling conditions that were overlooked.

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