---
title: event-yaml-schema
type: note
permalink: methodology/reference/event-yaml-schema
tags:
- methodology
- reference
- schema
- yaml
- events
- machine-readable
---

# Event YAML Schema

Reference for machine-readable event specifications embedded in markdown files.

**Status**: v0.1 engine/catalog contract — normative for Task 4.2 migrations and the catalog compiler ([[methodology/reference/simulator-architecture]] ADR-7). Changes are versioned and deliberate; the formal freeze is [[strategy/roadmap]] Phase 1 item 3, and schema-breaking war lessons live in the v0.2 backlog (Task 6.4), not here.

---

## Design Principles

1. **Python expressions for logic** — preconditions, pressure functions, conditional effects
2. **YAML for structure** — hierarchical, readable, standard tooling
3. **Signed magnitudes** — no redundant direction field; sign encodes direction
4. **Minimal schema** — don't invent what Python already does
5. **Explicit over implicit** — but not verbose

---

## Schema by Section

### Metadata

```yaml
id: EVENT_ID                    # SCREAMING_SNAKE_CASE
domain: political|economic|environmental|health|technological
scale: global|regional|national
causal_type: 1|2|3              # Type 1=stochastic, 2=threshold, 3=contingent
onset: sudden|gradual
reversibility: reversible|partial|irreversible
```

### Probability

Structure varies by causal type.

#### Type 1 (Stochastic)

```yaml
probability:
  annual: 0.020
  range: [0.015, 0.030]
  confidence: low|medium|high
```

#### Type 2 (Threshold)

```yaml
probability:
  pressure: |
    0.50 * (global_temp_anomaly / 2.0) +
    0.25 * (1.0 - arctic_ice_extent / 6.0) +
    0.25 * (1.0 - amoc_strength / 18.0)
  threshold: 65              # On 0-100 scale
  threshold_std: 15          # Uncertainty in threshold location
  sharpness: 0.15            # Steepness of sigmoid
  floor: 0.002               # Minimum annual probability
  annual: 0.010              # Current estimate for reference
  range: [0.005, 0.020]
  confidence: low|medium|high
```

#### Type 3 (Contingent)

```yaml
probability:
  window: 0.03               # Annual P(crisis window opens)
  preconditions:
    all:                     # All must be true (Python expressions)
      - "F_GPT > 1.0"
      - "chn.military_spending_deviation > 0.15"
    sustained:               # Must hold for N years
      - expr: "F_GPT > 1.0"
        years: 2
  resolution: 0.65           # P(discontinuity | window open)
  annual: 0.020              # window × resolution, for reference
  range: [0.010, 0.035]
  confidence: low|medium|high
```

### Factor Loadings

```yaml
factors:
  F_EAS: 0.38    # Inline comment for rationale
  F_GPT: 0.33
  F_FIN: 0.09
# Unlisted factors = 0
variance: 0.45   # Target factor-explained variance (ΛΩΛᵀ)ᵢᵢ
```

### Resolutions & Branches

For events with multiple possible outcomes:

```yaml
resolutions:
  - id: military_conflict
    p: 0.65
    branches:
      - {id: limited, p: 0.55}
      - {id: full_invasion, p: 0.30}
      - {id: nuclear, p: 0.15}
  
  - id: settlement
    p: 0.35
    branches:
      - {id: stable, p: 0.40}
      - {id: unstable, p: 0.60}
```

For events with severity tiers but single resolution:

```yaml
branches:
  - {id: moderate, p: 0.55}
  - {id: severe, p: 0.35}
  - {id: catastrophic, p: 0.10}
```

For events with no branches at all (single outcome), use `default:` as the impact key:

```yaml
impacts:
  default:
    - {var: amoc_strength, mag: [-45, 10], ...}
```

### Impacts

Keyed by `resolution.branch` or just `branch` if no resolutions.

```yaml
impacts:
  military_conflict.limited:
    - {var: semiconductor_supply, mag: [-0.70, 0.15], onset: immediate, decay: 2}
    - {var: chn.sanctions_level,  mag: [50, 20],      onset: immediate, permanent: true}
    - {var: twn.conflict_status,  mag: [4, 0],        onset: immediate, until: resolved}
```

#### Impact Fields

| Field | Required | Format | Notes |
|-------|----------|--------|-------|
| `var` | Yes | `variable` or `entity.variable` | State variable affected |
| `mag` | Yes | `[mean, std]` | Sign indicates direction |
| `onset` | Yes | See below | When impact begins |
| Durability | Yes | One of: `decay`, `permanent`, `until`, or full form | How impact persists |

#### Onset Values

- `immediate` — Instant effect
- `{delayed: N}` — Starts after N years
- `{gradual: N}` — Ramps linearly over N years

#### Durability Shorthand

| Shorthand | Meaning |
|-----------|---------|
| `decay: N` | Half-life of N years |
| `permanent: true` | Never recovers |
| `until: resolved` | Persists until event resolves |
| `until: policy_change` | Regime-dependent |

Full form when needed:
```yaml
durability: {type: maintenance, annual_failure: 0.05}
durability: {type: decaying, half_life: 5, floor: 0.02}
```

#### Inheritance

For branches that scale a baseline:

```yaml
military_conflict.full_invasion:
  inherit: military_conflict.limited
  scale: 1.5
```

### Cascades

```yaml
cascades:
  triggers:                  # This event increases other event probabilities
    - {event: OTHER_EVENT, delta: 0.015, years: 3}
    - {event: ANOTHER,     delta: 0.010, years: 5, if: "resolution == 'military_conflict'"}

  triggered_by:              # Other events increase this event's probability
    - {event: PRIOR_EVENT, delta: 0.005}
```

- `delta`: Absolute change in annual probability
- `years`: Duration of elevated probability
- `if`: Python expression for conditional cascades (optional)

### Research Status

```yaml
research:
  tier: 1|2|3
  updated: 2025-12-31
  review: complete|pending
  upgrade: true|false
```

---

## Entity and Variable References

### Entity ID Conventions

Entity IDs follow consistent patterns for machine parsing.

#### Countries (40)

Use **ISO 3166-1 alpha-3 codes in lowercase**:

| Example | Country |
|---------|---------|
| `usa` | United States |
| `chn` | China |
| `gbr` | United Kingdom |
| `deu` | Germany |
| `sau` | Saudi Arabia |
| `twn` | Taiwan |

Full list: See [[methodology/reference/state-entities]] for all 40 countries.

#### Tier 1 Aggregates (6)

Use **descriptive lowercase with underscores**:

| ID | Aggregate |
|----|-----------|
| `gulf_states` | Gulf States (Kuwait, Qatar, Bahrain, Oman) |
| `central_america` | Central America |
| `sahel` | Sahel |
| `east_africa` | East Africa |
| `eu_other` | Rest of EU |
| `levant_iraq` | Levant/Iraq |

#### Tier 2 Aggregates (6)

| ID | Aggregate |
|----|-----------|
| `central_asia_other` | Central Asia (other) |
| `southeast_asia_other` | Southeast Asia (other) |
| `andean_caribbean` | Andean/Caribbean |
| `maghreb` | Maghreb |
| `southern_africa_other` | Southern Africa (other) |
| `west_central_africa_other` | West/Central Africa (other) |

### Variable Reference Syntax

#### Global Variables

Reference directly by name:

```yaml
- {var: oil_brent, mag: [-25, 10], ...}
- {var: global_trade_volume, mag: [-0.08, 0.04], ...}
```

#### Country/Aggregate Variables

Use `entity.variable` format:

```yaml
- {var: chn.gdp_real, mag: [-0.15, 0.08], ...}
- {var: sau.current_account, mag: [-0.12, 0.05], ...}
- {var: eu_other.gdp_real, mag: [-0.06, 0.03], ...}
```

#### Wildcard Syntax

Use `*` to apply an impact to all countries (not aggregates):

```yaml
# Applies to all 40 individual countries
- {var: "*.gdp_real", mag: [-0.04, 0.02], onset: immediate, decay: 2}
- {var: "*.life_expectancy", mag: [-0.5, 0.3], onset: immediate, decay: 3}
```

**Wildcard behavior:**
- Expands to 40 individual country impacts at parse time
- Does NOT include regional aggregates (apply those explicitly if needed)
- Differential exposure can be applied via multiplier coefficients defined in event prose

**When to use wildcards:**
- Pandemic impacts affecting all countries
- Global financial crisis transmission
- Climate effects with universal (but scaled) exposure

**When NOT to use wildcards:**
- Regionally concentrated impacts (use explicit entity list)
- Impacts that only affect a subset of countries

---

## Python Expression Context

Python expressions are evaluated against a context dict containing:

- All factor values: `F_GPT`, `F_EAS`, `F_FIN`, etc.
- All state variables: `global_temp_anomaly`, `chn.gdp_real`, etc.
- Event state: `resolution`, `branch`, `years_since`

Expressions must be valid Python that returns a boolean (preconditions) or numeric (pressure functions).

**Normative subset:** because the simulator evaluates expressions vectorized across all runs, only a defined subset of Python is permitted, with specific semantic rules (e.g. `and`/`or` are rewritten elementwise; guarding idioms don't guard; ternaries are rejected in favor of `where()`). See [[methodology/reference/expression-language]] for the full contract, the function whitelist, and what to do when an expression needs history or aggregation.

---

## Validation Rules

1. Resolution probabilities must sum to 1.0
2. Branch probabilities within each resolution must sum to 1.0
3. All referenced variables must exist in state model
4. All referenced events must exist in event catalog
5. Factor loadings should produce target variance (within tolerance)

---

## Changelog

| Date | Change |
|------|--------|
| 2025-01-01 | Initial draft during Task 4.2 schema design |
| 2025-01-02 | Added Entity and Variable References section: entity ID conventions, wildcard syntax |
| 2026-07-12 | Status promoted from "Draft — refining" to v0.1 engine/catalog contract (normative for migrations and the compiler; formal freeze at [[strategy/roadmap]] Phase 1) |
