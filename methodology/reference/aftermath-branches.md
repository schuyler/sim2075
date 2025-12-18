---
title: aftermath-branches
type: note
permalink: methodology/reference/aftermath-branches
tags:
- methodology
- reference
- aftermath
- recovery
- durability
- state-transitions
---

# Aftermath Branches Reference

**How to model post-event trajectories when "which kind of aftermath" matters for ongoing dynamics.**

---

## The Problem

The durability framework handles how *effects fade over time*—GDP shocks decay with half-lives, agreements fail with annual probability, deaths are permanent. But durability doesn't capture *which trajectory the affected entity follows* after a major discontinuity.

Consider Pakistan state failure:

| Aftermath | Description | Ongoing Dynamics |
|-----------|-------------|------------------|
| Gradual recovery | Military-led stabilization, slow rebuilding | Elevated regional stress for ~10 years, then normalization |
| Persistent failure | Weak central government, endemic instability | Permanently elevated regional stress, ongoing event source |
| Fragmentation | Effective partition into regional power centers | Different entity structure, altered regional dynamics |
| Cascade trigger | Collapse triggers wider regional crisis | Immediate secondary events, severe factor elevation |

These aren't different *magnitudes* of the same outcome—they're qualitatively different trajectories with different implications for the simulation. Pure impact-decay can't distinguish between "Pakistan had a bad decade but recovered" and "Pakistan became a persistent failed state that destabilized South Asia for 30 years."

---

## The Solution: Aftermath Branches

**Aftermath branches** extend the Type 3 resolution structure to any event where post-event trajectory matters.

When an event with aftermath branches fires:
1. Sample which branch obtains (weighted by branch probabilities)
2. Apply the branch-specific factor modifications
3. Track the branch as an active aftermath with its duration/exit conditions
4. Each simulation year, evaluate whether active aftermaths persist or exit

This is **event-attached, not entity-attached**. We're not classifying Pakistan as a "fragile state" with regime tracking. We're specifying that the event "Pakistan state failure," if it fires, has branching post-event trajectories.

---

## When to Use Aftermath Branches

**Use aftermath branches when:**
- The event has qualitatively different post-event trajectories
- Those trajectories affect *ongoing dynamics* (factor loadings, event eligibility), not just impact magnitude
- The distinction matters for understanding cascade potential and tail outcomes

**Don't use aftermath branches when:**
- Impact decay adequately captures recovery (most financial shocks)
- Post-event trajectory is primarily about magnitude, not kind
- The event is transient without persistent structural effects

### Decision Heuristic

Ask: "If I read a trajectory narrative, would I need to know *which kind* of aftermath occurred to understand what happened next?"

- Pakistan state failure → Yes, aftermath type determines regional dynamics for decades
- Global financial crisis → Probably not, severity and duration matter but not qualitative trajectory
- Pandemic → Maybe, depends on whether institutional response diverges

---

## Structure Specification

### Full Multi-Branch Specification

```yaml
aftermath_branches:
  - id: gradual_recovery
    probability: 0.35
    description: "Military-led stabilization, slow institutional rebuilding"
    factor_modifications:
      F_SAS: +0.25
      F_GPT: +0.10
    duration:
      type: decaying
      half_life: 8
      floor: 0.05  # small permanent elevation
    exit_conditions: null  # pure decay
    
  - id: persistent_failure
    probability: 0.40
    description: "Weak central government, endemic instability, ongoing violence"
    factor_modifications:
      F_SAS: +0.50
      F_GPT: +0.15
    duration:
      type: persistent
      exit_conditions:
        - id: external_stabilization
          annual_probability: 0.02
          requires: [international_intervention_event]
        - id: organic_recovery
          annual_probability: 0.03
          requires:
            - regional_conflict_intensity < 2
            - pakistan.gdp_growth > 0 for 3 consecutive years
    
  - id: fragmentation
    probability: 0.20
    description: "Effective partition into Punjab core and ungoverned periphery"
    factor_modifications:
      F_SAS: +0.60
      F_GPT: +0.25
    duration:
      type: persistent
      exit_conditions:
        - id: reunification
          annual_probability: 0.01
          # very unlikely
    entity_modifications:
      # For v2.0: spawn successor entities
      note: "May require entity model changes in future versions"
          
  - id: cascade_trigger
    probability: 0.05
    description: "Collapse triggers immediate regional crisis"
    factor_modifications:
      F_SAS: +0.80
      F_GPT: +0.30
    duration:
      type: decaying
      half_life: 5
      floor: 0.30  # settles into persistent_failure equivalent
    triggers:
      - event: india_pakistan_crisis
        window_opens: true
      - event: afghanistan_spillover
        probability_modifier: 2.0
```

### MVP Single-Branch Specification

For events that don't warrant multi-branch complexity yet:

```yaml
aftermath_branches:
  - id: default
    probability: 1.0
    description: "Standard post-event trajectory"
    factor_modifications:
      F_SAS: +0.40
    duration:
      type: decaying
      half_life: 10
      floor: 0.10
```

This is functionally equivalent to current impact-decay, but:
- Structured for future branch addition
- Labeled for narrative interpretability
- Factor modifications explicit (not just state variable impacts)

---

## MVP Approach

**For v1.0, every event with significant persistent effects gets a single-branch aftermath.**

This gives us:
- Consistent structure across events
- Interpretable trajectory labels
- Foundation for multi-branch refinement
- No upfront complexity cost

**Refinement trigger**: Sensitivity analysis in Phase 3. If tail outcomes are sensitive to "what happens after Event X," add branches to Event X.

Specifically:
1. Run Monte Carlo with single-branch aftermaths
2. Identify events whose aftermath duration/magnitude significantly affects tail distributions
3. For those events, research and specify multiple branches
4. Re-run and compare

---

## Relationship to Type 3 Resolutions

Type 3 events already have resolution branches—Taiwan crisis resolves as military_conflict, negotiated_accommodation, or status_quo.

| Aspect | Type 3 Resolution | Aftermath Branch |
|--------|-------------------|------------------|
| When sampled | At window resolution | At event occurrence |
| What it determines | Whether/how event occurs | What trajectory follows |
| Applies to | Type 3 only | Any event type |
| Impact vector | Resolution-specific | Branch-specific factor mods |

**Type 3 events can have both**: resolution determines *what happened*, aftermath determines *what follows*.

```yaml
event: taiwan_crisis
type: 3

resolutions:
  - id: military_conflict
    probability: 0.35
    impact_vector: [severe impacts]
    aftermath_branches:
      - id: prolonged_war
        probability: 0.30
        ...
      - id: quick_resolution
        probability: 0.70
        ...
        
  - id: negotiated_accommodation
    probability: 0.25
    impact_vector: [moderate impacts]
    aftermath_branches:
      - id: stable_new_status_quo
        probability: 0.60
        ...
      - id: unstable_settlement
        probability: 0.40
        ...
```

---

## Relationship to Durability

Aftermath branches and durability are **complementary, not competing**:

- **Durability** describes how individual impact components fade (GDP shock half-life, agreement failure probability)
- **Aftermath branches** describe which *trajectory* the entity follows, determining which durability parameters apply

A branch specification includes duration (how long the branch's factor modifications persist), which is conceptually similar to durability. But:
- Durability applies to state variable impacts
- Aftermath duration applies to factor loading modifications

Both can coexist in the same event specification.

---

## Relationship to Entity Regime States

An earlier design considered **entity-attached regime states** (Pakistan has regime = functional/stressed/failed/collapsed).

Aftermath branches are superior because:
- No pre-classification of entities as "fragile" or "stable"
- Any event can have branches if warranted
- States are event-specific, not entity-generic
- Complexity is local to events that need it

The interpretability benefit is preserved: a trajectory can report "Pakistan state failure (2035), persistent_failure branch" and that's a meaningful statement about the simulation path.

---

## Simulation Implementation

### Tracking Active Aftermaths

The simulation maintains a list of active aftermaths:

```python
active_aftermaths = [
    {
        'event': 'pakistan_state_failure',
        'branch': 'persistent_failure',
        'start_year': 2035,
        'factor_modifications': {'F_SAS': 0.50, 'F_GPT': 0.15},
        'duration_type': 'persistent',
        'exit_conditions': [...],
        'current_magnitude': 1.0  # for decaying types
    },
    ...
]
```

### Annual Processing

```python
def process_aftermaths(active_aftermaths, state, year):
    factor_adjustments = defaultdict(float)
    
    for aftermath in active_aftermaths:
        # Check exit conditions
        if should_exit(aftermath, state, year):
            active_aftermaths.remove(aftermath)
            continue
            
        # Apply decay if applicable
        if aftermath['duration_type'] == 'decaying':
            aftermath['current_magnitude'] = compute_decay(
                aftermath, year
            )
        
        # Accumulate factor modifications
        for factor, base_mod in aftermath['factor_modifications'].items():
            effective_mod = base_mod * aftermath['current_magnitude']
            factor_adjustments[factor] += effective_mod
    
    return factor_adjustments
```

### Integration with Factor Sampling

Factor adjustments from active aftermaths shift factor means before sampling:

```python
def sample_factors(base_means, correlation_matrix, aftermath_adjustments):
    adjusted_means = {
        f: base_means[f] + aftermath_adjustments.get(f, 0)
        for f in factors
    }
    return sample_multivariate_normal(adjusted_means, correlation_matrix)
```

---

## Examples

### Example 1: State Failure (Multi-Branch)

Pakistan state failure warrants multiple branches because post-failure trajectory determines decades of regional dynamics.

See full specification above.

### Example 2: Financial Crisis (Single Branch)

Global financial crisis doesn't need branches—severity varies, but trajectory is qualitatively similar (shock → recovery → scarring).

```yaml
event: global_financial_crisis
type: 1

aftermath_branches:
  - id: default
    probability: 1.0
    description: "Standard crisis-recovery trajectory"
    factor_modifications:
      F_FIN: +0.30
      F_EUR: +0.15
      F_LAM: +0.20
    duration:
      type: decaying
      half_life: 3
      floor: 0.05
```

### Example 3: Climate Tipping Point (Single Branch, High Floor)

AMOC weakening is essentially irreversible on policy-relevant timescales.

```yaml
event: amoc_weakening
type: 2

aftermath_branches:
  - id: default
    probability: 1.0
    description: "Permanent circulation regime shift"
    factor_modifications:
      F_CLIM: +0.40
      F_EUR: +0.35
      F_FOOD: +0.25
    duration:
      type: permanent
      # No decay, no exit conditions
```

---

## Adding Branches: The Research Process

When sensitivity analysis indicates an event needs branches:

1. **Identify the branch space**: What are the qualitatively distinct post-event trajectories? (Usually 2-4)

2. **Research branch probabilities**: Historical analogs, expert judgment, scenario analysis. Document uncertainty.

3. **Specify factor modifications per branch**: Which factors are elevated, by how much?

4. **Define duration/exit conditions**: How long does each branch persist? What would cause transition?

5. **Consider triggers**: Does any branch open windows for other events?

6. **Document rationale**: Why these branches? What's excluded and why?

This is Level 2 or Level 3 research (4-8 hours or 20+ hours) for a single event.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Branches that differ only in magnitude | Use single branch with uncertainty in parameters |
| Too many branches (>4) | Collapse similar trajectories; model major distinctions only |
| Branch probabilities that don't sum to 1.0 | Ensure exhaustive, mutually exclusive branches |
| Confusing resolution (Type 3) with aftermath | Resolution = what happens; aftermath = what follows |
| Entity-level thinking ("Pakistan is failed") | Event-level thinking ("Pakistan failure has these aftermath branches") |

---

*See [[methodology/reference/durability-types]] for impact persistence | [[methodology/concepts/state-event-coupling]] for factor-state architecture | [[methodology/reference/impact-estimation]] for impact vectors*