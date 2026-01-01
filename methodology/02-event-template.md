---
title: 02-event-template
type: note
permalink: methodology/02-event-template
tags:
- methodology
- template
- events
- yaml
- machine-readable
---

# Event Template

Canonical template for event specifications. Copy this when creating new events.

**Design principle**: YAML blocks are the machine-readable specification. Prose sections provide rationale and context. The simulation engine parses YAML directly from these markdown files—no separate catalog needed.

**References**:
- [[methodology/reference/state-variables-country]] — Valid country variable IDs
- [[methodology/reference/state-variables-global]] — Valid global variable IDs
- [[methodology/reference/variance-allocation]] — Factor loading targets by type
- [[methodology/reference/causal-types]] — Type 1/2/3 definitions

---

## Template (Copy Below This Line)

```markdown
---
title: [event-name]
type: event
permalink: events/[domain]/[event-name]
tags:
  - event
  - [type-1|type-2|type-3]
  - [domain]
  - [region]
  - level-1
---

# [Event Name]

**Type [N] ([Stochastic|Threshold|Contingent]) Event** — [One-line summary]

## Description

[2-3 paragraphs: What state transition does this represent? What distinguishes occurrence from non-occurrence? What is the discontinuity?]

---

## Specification

```yaml
id: EVENT_ID
scale: global | regional | national
domain: environmental | political | economic | health | technological
causal_type: 1 | 2 | 3
onset: sudden | rapid | gradual
reversibility: reversible | partial | irreversible
```

---

## Causal Type Specification

[Prose section explaining the causal logic. Content varies by type:]

**Type 1**: Base rate derivation, reference class, condition adjustments

**Type 2**: Pressure accumulation mechanism, threshold dynamics, historical calibration

**Type 3**: Window preconditions, resolution logic, historical basis for probabilities

### Case Against This Specification

[Per [[methodology/03-critical-review]] Q4 — strongest arguments against your probability estimate or structure]

---

## Probability

```yaml
probability:
  annual: 0.020       # Point estimate
  low: 0.010          # Low bound
  high: 0.035         # High bound  
  confidence: medium  # low | medium | high
```

For **Type 2**, add pressure function:

```yaml
pressure_function:
  variables:
    - id: state_variable_id
      weight: 0.4
      transform: linear | inverse | exponential | threshold
    - id: another_variable
      weight: 0.3
      transform: linear
  threshold:
    estimate: 65      # 0-100 pressure scale
    uncertainty: 10
    sharpness: 8      # Higher = sharper transition
  minimum_probability: 0.005
```

For **Type 3**, add window structure:

```yaml
window:
  annual_probability: 0.03    # P(window opens)
  preconditions:
    - variable: F_GPT
      condition: "> 1.5 for 2+ years"
    - variable: some.state_var
      condition: "< threshold"
resolution_given_window: 0.65   # P(discontinuity | window)
# Note: annual probability = window.annual_probability × resolution_given_window
```

### Derivation

[Step-by-step reasoning: base rates, expert estimates, structural reasoning, adjustments]

### Comparative Ranking

[How does this compare to similar events? Higher/lower than X because...]

### Key Uncertainties

- [What could make probability much higher?]
- [What could make it much lower?]

---

## Factor Loadings

*Scaled per [[methodology/reference/variance-allocation]] for Type [N] target.*

```yaml
factor_loadings:
  F_EAS: 0.38   # Dominant factor - rationale
  F_GPT: 0.33   # Secondary factor - rationale
  F_FIN: 0.09   # Tertiary - rationale
# Omit factors with zero loading
variance_explained: 0.45  # Type-specific target
scale_factor: 0.47        # From scaling calculation
```

[Brief prose on loading rationale if needed beyond inline comments]

---

## Resolutions

[Prose explaining resolution structure — why these branches exist, probability rationale]

```yaml
resolutions:
  - id: resolution_one
    probability: 0.65
    branches:
      - id: branch_a
        probability: 0.55
      - id: branch_b
        probability: 0.30
      - id: branch_c
        probability: 0.15
  - id: resolution_two
    probability: 0.35
    branches:
      - id: branch_d
        probability: 0.40
      - id: branch_e
        probability: 0.60
```

*Resolution probabilities must sum to 1.0. Branch probabilities within each resolution must sum to 1.0.*

---

## Impact Vectors

[Prose on transmission channels, differential exposure, derivation methodology]

```yaml
impacts:
  # Key format: resolution_id.branch_id (or just resolution_id if no branches)
  resolution_one.branch_a:
    global:
      - var: global_variable_id
        dir: -1                    # -1 = decrease, +1 = increase
        mag: [0.15, 0.05]          # [mean, std]
        onset: immediate           # immediate | delayed(years) | gradual(years)
        durability:
          type: decaying           # permanent | decaying | maintenance_required | shock_vulnerable | regime_dependent
          half_life: 3
      - var: another_global_var
        dir: +1
        mag: [200, 80]
        onset: immediate
        durability:
          type: permanent
    
    # Country-specific impacts use ISO3 codes
    chn:
      - var: gdp_real
        dir: -1
        mag: [0.15, 0.08]
        onset: immediate
        durability:
          type: decaying
          half_life: 3
      - var: sanctions_level
        dir: +1
        mag: [50, 20]
        onset: immediate
        durability:
          type: permanent

  resolution_one.branch_b:
    # Can use multiplier for scaled variants
    _base: resolution_one.branch_a
    _multiplier: 1.5
```

### Durability Types

| Type | Parameters | Use For |
|------|------------|---------|
| `permanent` | none | Deaths, resource depletion, knowledge |
| `decaying` | `half_life`, optional `floor` | Financial shocks, reputational damage |
| `maintenance_required` | `annual_failure_prob` | Treaties, alliances |
| `shock_vulnerable` | `vulnerable_to: [EVENT_IDS]` | Development gains |
| `regime_dependent` | `persists_in: [conditions]` | Political achievements |

---

## Cascade Effects

```yaml
cascades:
  triggers:  # This event increases probability of other events
    - target: TARGET_EVENT_ID
      delta: +0.015          # Additive change to annual probability
      duration: 3            # Years the effect persists
      mechanism: "Brief explanation"
    - target: ANOTHER_EVENT
      delta: +0.020
      duration: 5
      mechanism: "Causal pathway"
  
  triggered_by:  # Other events increase this event's probability
    - source: SOURCE_EVENT_ID
      delta: +0.005
      mechanism: "Why this increases probability"
```

---

## Research Status

```yaml
research:
  tier: 1                    # 1 | 2 | 3
  updated: 2025-12-31
  critical_review: complete  # pending | complete
  upgrade_candidate: true
  upgrade_rationale: "What would Level 2 research improve?"
```

## Open Questions

- [What don't we know?]
- [What assumptions are most uncertain?]

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| YYYY-MM-DD | Initial specification | Level 1 |
```

---

## Checklist Before Saving

### Classification
- [ ] Causal type selected with rationale
- [ ] Specification YAML block complete

### Type-Specific
- [ ] **Type 1**: Base rate derivation in prose
- [ ] **Type 2**: `pressure_function` YAML complete
- [ ] **Type 3**: `window` YAML complete, resolution probabilities sum to 1.0

### Probability
- [ ] `probability` YAML block complete
- [ ] Derivation prose explains reasoning
- [ ] Comparative ranking completed
- [ ] Case Against section populated

### Factor Loadings
- [ ] `factor_loadings` YAML with non-zero factors only
- [ ] `variance_explained` matches type target
- [ ] `scale_factor` documented

### Resolutions & Impacts
- [ ] `resolutions` YAML with probabilities summing to 1.0
- [ ] `impacts` YAML keyed by resolution.branch
- [ ] Durability specified for each impact

### Cascades
- [ ] `cascades` YAML documents trigger relationships
- [ ] Mechanisms briefly explained

### Metadata
- [ ] `research` YAML block complete
- [ ] Open questions listed

---

## Parser Notes

The simulation engine extracts YAML blocks from markdown using fenced code blocks. Requirements:

1. YAML blocks must use triple-backtick fencing with `yaml` language identifier
2. Each conceptual section (specification, probability, factor_loadings, etc.) is a separate block
3. The parser merges all YAML blocks into a single event object
4. Missing factors default to 0.0
5. Comments are preserved for documentation but ignored by parser

---

*See [[methodology/01-level-1-workflow]] for production workflow | [[events/geopolitical/taiwan-conflict]] for worked example*