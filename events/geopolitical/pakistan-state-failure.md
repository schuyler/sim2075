---
title: pakistan-state-failure
type: note
permalink: events/geopolitical/pakistan-state-failure
tags:
- event
- type-2
- geopolitical
- south-asia
- pakistan
- nuclear
- level-1
---

# Pakistan State Failure

**Type 2 (Threshold) Event** — Probability rises as compound pressures (water, debt, governance, conflict) accumulate toward collapse threshold.

---

## Description

Collapse of effective Pakistani state authority: loss of territorial control over significant portions of the country, failure to provide basic services, potential military fragmentation, and mass displacement.

This is a **state transition**: Pakistan crosses from "stressed but functional" to "failed state" regime, marked by `pak.internal_conflict_intensity` rising to 4 (major war/state collapse) and loss of effective territorial control.

**What marks occurrence**: Central government loses control over multiple provinces; military fragments or cannot maintain order; mass displacement begins; basic services collapse outside major cities.

---

## Specification

```yaml
id: PAKISTAN_STATE_FAILURE
domain: political
scale: national
causal_type: 2
onset: sudden
reversibility: partial
```

*Onset speed: rapid (1-3 years from trigger to acute phase). Reversibility: partial (recovery possible but incomplete).*

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Pakistan exhibits classic pressure accumulation:
- Multiple stressors compound over time (water, debt, governance, conflict)
- State appears stable until threshold crossed, then rapid cascade
- No single actor decision determines outcome (unlike Type 3)
- Not random timing (unlike Type 1)—probability increases with stress

### Pressure Function

Uses observable state variables per [[methodology/reference/state-variables-country]]. Note that `regime_stability` has been replaced by observable indicators.

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `pak.water_stress` | 0.25 | linear | Indus water is binding constraint; civilizational risk |
| `pak.debt_external` | 0.20 | threshold(80) | Sharp increase above 80% debt/GDP; IMF dependency |
| `pak.internal_conflict_intensity` | 0.20 | exponential | Conflict accelerates pressure; currently ~2 |
| `pak.years_since_irregular_transition` | 0.15 | inverse_log | Recent coups/irregular transitions signal fragility |
| `pak.protest_intensity_annual` | 0.10 | linear | Mass unrest indicates stress |
| `pak.food_import_dependence` | 0.10 | linear | Fiscal vulnerability to food prices |

The YAML expression below realizes these transforms in the expression language's subset: the debt threshold as a clipped linear ramp from 60% to 100% of GDP (`min(1, max(0, (debt − 60) / 40))`), the conflict term as linear in the 0-4 scale, and the transition-recency term as `1 / (1 + years / 5)`.

**Proxy note**: The original specification used `regime_stability` as a composite variable. Per [[methodology/concepts/synthetic-variable-problem]], this has been replaced with observable indicators. The pressure function now directly uses `years_since_irregular_transition`, `protest_intensity_annual`, and `internal_conflict_intensity` as the political stress measures.

### Threshold Specification

| Parameter | Value |
|-----------|-------|
| **Estimate** | 70 (on 0-100 pressure scale) |
| **Uncertainty** | ±10 |
| **Sharpness (k)** | 0.20 (moderate-sharp; compound crises cascade quickly) |
| **Historical calibration** | Syria (crossed ~2011), Venezuela (crossed ~2017), Yugoslavia (crossed ~1991) |

### Minimum Probability

**Floor**: 0.3%/year (military cohesion provides backstop, but not absolute)

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.25 * (pak.water_stress / 100) +
      0.20 * min(1.0, max(0, (pak.debt_external - 60) / 40)) +
      0.20 * (pak.internal_conflict_intensity / 4) +
      0.15 * (1.0 / (1 + pak.years_since_irregular_transition / 5)) +
      0.10 * (pak.protest_intensity_annual / 100) +
      0.10 * (pak.food_import_dependence / 100)
    )
  threshold: 70
  threshold_std: 10
  sharpness: 0.20
  floor: 0.003
  resolves_after: 5
  annual: 0.015
  range: [0.008, 0.025]
  confidence: medium
```

`resolves_after: 5` — `active_major_conflicts` counts the collapse for five years per firing, counting the firing year: state-failure civil conflicts in the reference class (Syria from 2011, Somalia from 1991, Yugoslavia from 1991) ran well past five years, and five is the shortest window consistent with the 8-year conflict-intensity half-life below.

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 2.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~30% at point estimate |

### Current Pressure Estimate

- `pak.water_stress`: ~70 (severe, worsening)
- `pak.debt_external`: ~75% GDP (near threshold)
- `pak.internal_conflict_intensity`: 2 (intermediate)
- `pak.years_since_irregular_transition`: ~2 (recent PTI crisis counts)
- `pak.protest_intensity_annual`: ~45 (elevated)
- `pak.food_import_dependence`: ~35%
- **Current pressure**: ~55/100 (elevated but below threshold; the expression gives 53.7 at these values)

### Derivation

1. **Base rate**: 15-25% over 25 years for high-vulnerability states (from historical collapse patterns)
2. **Annualization**: ~0.9%/year assuming constant hazard
3. **Adjustment for worsening baseline**: Water stress accelerating; IMF dependency chronic; Indus glacier melt accelerating
4. **Adjusted estimate**: 1.5%/year (range: 0.8-2.5%)

### Probability Evolution

For Type 2 events, probability varies with pressure accumulation.

| Period | Pressure | Annual P | Rationale |
|--------|----------|----------|-----------|
| 2025-2035 | 55→62 | ~1.3% | Current trajectory; water stress worsening |
| 2035-2045 | 62→72 | ~2.0% | Entering threshold zone; glacier melt accelerating |
| 2045-2060 | 72→80+ | ~2.5-3.5% | Peak water stress period |
| 2060-2075 | 80+ | ~3.0%+ | If no prior failure, either very high pressure or adaptation |

### Case Against

Per [[methodology/03-critical-review]] Q4:

**1. Military has always intervened before failure**

Pakistan's military has a history of seizing power when civilian governance fails—1958, 1969, 1977, 1999. The military is more coherent than the civilian state. "State failure" in the Syria/Somalia sense may be impossible because the military would impose order first. The event as specified may not be reachable.

*Counter*: Military intervention is a different outcome from state failure, but military fragmentation IS possible. The military's coherence depends on ethnic/provincial balance (Punjabi dominated), institutional discipline, and external support. Under severe enough stress (especially combined with India-Pakistan conflict), even the military could fragment. The 1971 breakup of Pakistan demonstrates this is possible.

**2. External support will always arrive**

Pakistan is "too nuclear to fail." China has $60B+ invested in CPEC. The US cares about nuclear security. Gulf states care about remittances. Saudi/UAE/IMF have repeatedly bailed out Pakistan. Someone will always provide enough support to prevent collapse.

*Counter*: External support has been sufficient for "muddle through" but not for structural resolution. Each bailout creates more debt; at some point, bailout fatigue sets in. China's appetite for throwing good money after bad is limited. And if collapse begins rapidly (e.g., triggered by severe climate event), external support may not arrive fast enough.

**3. 1.5%/year is too high for a nuclear state**

The international community's interest in preventing nuclear state failure creates enormous stabilization pressure. No nuclear-armed state has ever failed. The 1.5%/year estimate may be 2-3× too high compared to what the nuclear dimension justifies.

*Counter*: The nuclear dimension creates intervention incentive but doesn't guarantee intervention success. A rapid cascade could outrun international response. And internal dynamics—not external intervention—determine collapse. The Soviet Union was nuclear-armed and did fragment (though not into "failed state" conditions).

**4. Water stress timeline is longer than implied**

Indus water stress is severe but the crisis timeline is decades, not years. Glacier melt increases flow in the medium term before reducing it. The binding constraint may be 2040s-2050s, not 2025-2035. Current probability may be lower than estimated.

*Counter*: Fair point on timeline. But the 2022 floods showed acute shocks can accelerate stress. And water stress interacts with other pressures—it doesn't need to reach peak to contribute to failure. The probability estimate includes uncertainty about timeline.

### Key Uncertainties

- **Indus water trajectory**: Faster glacial melt → pressure rises faster
- **Military cohesion**: Military fracture vs. military intervention is the key swing variable
- **External support**: IMF, China, Gulf states willingness to provide bailouts
- **Climate shock timing**: 2022 floods were preview; worse shocks possible
- **India-Pakistan dynamics**: External conflict could trigger cascade

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

```yaml
factors:
  F_SAS: 0.43  # This IS the South Asian anchor crisis; dominant regional loading
  F_FOOD: 0.26 # Indus water-agriculture nexus is core vulnerability
  F_CLIM: 0.23 # Glacial melt, monsoon variability, flood risk
  F_FIN: 0.18  # Chronic fiscal crisis; IMF dependency
  F_GPT: 0.13  # US-China competition affects aid flows
  F_MENA: 0.10 # Afghan border, Gulf remittances
  F_HLTH: 0.08 # Healthcare vulnerability, population density
  F_EAS: 0.05  # Via China relationship
  F_TECH: 0.02 # Marginal
  F_EUR: 0.02  # Diaspora link
variance: 0.65  # Type 2 target
```

F_SSA and F_LAM carry no loading (no link).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.61 from original loadings.

---

## Branches

```yaml
branches:
  - {id: controlled, p: 0.40, desc: "Military maintains core; periphery autonomous; international intervention"}
  - {id: fragmentation, p: 0.45, desc: "State fragments along provincial lines; prolonged civil conflict"}
  - {id: collapse, p: 0.15, desc: "Military fragments; no coherent authority; nuclear security crisis"}
```

### Branch 1: Controlled Collapse (40%)

Central government loses control of periphery but military maintains core territorial integrity. Baluchistan, parts of KPK effectively autonomous. Major humanitarian crisis but not complete state dissolution. International intervention helps stabilize.

**Impact modifiers**: 0.7× the fragmentation baseline.

### Branch 2: Fragmentation (45%)

State fragments along provincial/ethnic lines. Multiple power centers emerge. Sindh-Punjab core barely holds together. Mass displacement. Prolonged civil conflict. Nuclear security uncertain but probably maintained.

**Impact modifiers**: 1.0× baseline.

### Branch 3: Complete Collapse (15%)

Military fragments. No coherent central authority. Nuclear security becomes acute international concern. External intervention likely. Mortality and displacement at upper end of range.

**Impact modifiers**: 1.8× baseline.

*The YAML `impacts:` block takes the controlled branch as its explicit list and scales the others from it: `fragmentation` 1.4 (≈ 1.0/0.7) and `collapse` 2.5 (≈ 1.8/0.7), so the three branches keep the relative magnitudes above.*

---

## Impacts

### Transmission Channels

**Migration**: Pakistan → constrained in all directions. India: militarized border, minimal acceptance expected. Afghanistan: no capacity, already in crisis. Iran: limited willingness. Gulf states: would likely expel existing workers. Implication: "trapped population" dynamic — displacement is internal or results in mortality.

**Nuclear Security**: State failure raises arsenal security concerns. Military cohesion is the key variable; external intervention likely if fragmentation occurs; India's response is the critical unknown; the US and international community would prioritize arsenal security.

**Regional Contagion**: Afghanistan — further destabilization from border pressure (not modeled as an impact row: Afghanistan is not a state-catalog entity; see [[events/backlog-registry]]). India — refugee pressure, terrorism risk, Kashmir opportunism; the original specification expressed India's economic exposure as a growth-rate hit (−1.0 ± 0.5 pp for 3 years), re-expressed at migration as a fraction of `ind.gdp_real`. China — CPEC investments at risk ($60B+); potential intervention to protect assets.

**Remittance Collapse**: ~$30B/year in remittances; Gulf workers expelled during crisis; remittance collapse deepens economic crisis (feedback loop).

```yaml
impacts:
  controlled:
    # Pakistan
    - {var: pak.gdp_real,                    mag: [-0.28, 0.08], onset: {gradual: 2}, decay: 15}
    - {var: pak.internal_conflict_intensity, mag: [2, 0.5],      onset: immediate, decay: 8}
    - {var: pak.idp_population,              mag: [17, 7],       onset: {gradual: 2}, decay: 15}
    - {var: pak.refugees_abroad,             mag: [3.5, 2],      onset: {gradual: 3}, decay: 20}
    - {var: pak.unemployment_rate,           mag: [0.14, 0.06],  onset: immediate, decay: 10}
    - {var: pak.life_expectancy,             mag: [-4, 2],       onset: {gradual: 3}, decay: 15}
    
    # Regional
    - {var: ind.gdp_real,                    mag: [-0.007, 0.004], onset: {delayed: 1}, decay: 3}
    - {var: ind.refugees_hosted,             mag: [1.4, 1],      onset: {gradual: 2}, decay: 15}
    
    # Global
    - {var: active_major_conflicts,          mag: [1, 0],        onset: immediate, until: resolved}

  fragmentation:
    inherit: controlled
    scale: 1.4

  collapse:
    inherit: controlled
    scale: 2.5
```

*Units: `gdp_real` rows are fractions of the entity's current value (−28% ± 8% for the controlled branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields).*

### Durability Rationale

- **GDP**: Decaying with long half-life; recovery possible but slow (Syria analogy: 12+ years, still not recovered). The original specification carried a −20% floor on the GDP recovery; decay-to-floor durability is schema v0.2 backlog, so the YAML uses a plain 15-year half-life.
- **Displacement**: Decaying but slow; "trapped population" dynamics limit return rates; closed borders
- **Conflict intensity**: Decaying as civil war eventually exhausts or resolves

### Mortality Note

Excess deaths not tracked as state variable. Estimated 2-10M over 10 years depending on branch. Modeled via `life_expectancy` depression and conflict intensity effects on population dynamics.

---

## Cascades

```yaml
cascades:
  triggers:
    - {event: INDIA_PAKISTAN_MILITARY_CONFLICT, delta: 0.015, years: 10}
    - {event: CHINESE_ECONOMIC_CRISIS,          delta: 0.002, years: 5}
  triggered_by:
    - {event: INDIA_PAKISTAN_MILITARY_CONFLICT, delta: 0.030}
    - {event: SEVERE_PANDEMIC,                  delta: 0.005}
    - {event: GLOBAL_FINANCIAL_CRISIS,          delta: 0.008}
    - {event: CHINESE_ECONOMIC_CRISIS,          delta: 0.005}
```

### Cascade Mechanisms

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| INDIA_PAKISTAN_MILITARY_CONFLICT | +1.5%/year | 10 years | Chaos creates escalation risk; potential preemptive action |
| CHINESE_ECONOMIC_CRISIS | +0.2%/year | 5 years | CPEC losses; regional instability |

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| INDIA_PAKISTAN_MILITARY_CONFLICT | +3%/year | Military engagement diverts resources; defeat could trigger fragmentation |
| SEVERE_PANDEMIC | +0.5%/year | Healthcare collapse; economic stress |
| GLOBAL_FINANCIAL_CRISIS | +0.8%/year | Capital flight; IMF unable to help |
| CHINESE_ECONOMIC_CRISIS | +0.5%/year | CPEC support collapses; regional contagion |

---

## Historical Analogues

| Case | Relevance | Key Difference |
|------|-----------|----------------|
| Syria (2011-) | Compound crisis → state failure | No nuclear weapons |
| Yugoslavia (1991-) | Multi-ethnic state fragmentation | International intervention earlier |
| Somalia (1991-) | Complete state collapse | Smaller population, no nuclear weapons |
| Pakistan 1971 | Actual fragmentation of Pakistan | External war catalyst; Bangladesh was geographically separate |

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-01-03
  review: complete
  upgrade: true
```

### Upgrade Rationale

- Nuclear dimension unprecedented; military cohesion is key swing variable requiring deeper analysis
- Indus water timeline calibration
- External intervention scenarios

## Sources

- IMF Article IV consultations
- IPCC Indus basin projections
- World Bank Pakistan Climate Assessment
- Historical state failure case studies

## Open Questions

1. **Military cohesion**: Will military fragment or intervene to prevent collapse?
2. **Nuclear security**: How robust are command-and-control systems under stress?
3. **External intervention**: Would US/China/India intervene? How?
4. **Trapped population**: What are realistic mortality rates with closed borders?
5. **Recovery pathway**: What does reconstitution look like — Somalia model or Yugoslavia model?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-17 | Initial Level 1 specification | Type 2 state failure template |
| 2025-12-30 | Variance allocation: scaled loadings to Type 2 target | Task 3.11 - Factor-explained variance reduced to Type 2 target (0.65) per variance allocation framework |
| 2025-12-30 | Critical review complete; replaced regime_stability with observables | Task 2.4.8 - Added Case Against, Probability Evolution; fixed event references |
| 2025-01-03 | Migrated to YAML-embedded schema | Task 4.2 format migration |
| 2026-10-12 | Added `resolves_after: 5` | Schema change of the same date: `until: resolved` rows need an explicit window |
| 2026-10-12 | Pressure expression wrapped in `100 * (...)` | Schema's pressure-scale rule (event-yaml-schema changelog 2026-10-12); at the prose's current values the expression gives 53.7, consistent with "~55/100" |
| 2026-10-12 | **Remediated**: restored lost prose; fixed state-catalog references | Task 4.2.5 / data-track D1 — Restored causal type rationale, pressure function table and proxy note, threshold specification, floor rationale, derivation, Case Against #4, branch descriptions and modifiers, transmission channel detail, durability rationale, historical analogues, sources, changelog rationale. `pak.refugee_outflow` → `pak.refugees_abroad`, `ind.refugee_inflow` → `ind.refugees_hosted` (the catalog's names). Dropped the `afg.internal_conflict_intensity` row: Afghanistan is not a state-catalog entity and belongs to no aggregate; gap recorded in [[events/backlog-registry]] |

---

*See [[methodology/reference/causal-types]] for Type 2 definition | [[methodology/reference/state-variables-country]] for variable definitions | [[research/collapse-patterns-framework]] for historical analogues | [[methodology/03-critical-review]] for review methodology*
