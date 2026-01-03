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

---

## Probability

```yaml
probability:
  pressure: |
    0.25 * (pak.water_stress / 100) +
    0.20 * min(1.0, max(0, (pak.debt_external - 60) / 40)) +
    0.20 * (pak.internal_conflict_intensity / 4) +
    0.15 * (1.0 / (1 + pak.years_since_irregular_transition / 5)) +
    0.10 * (pak.protest_intensity_annual / 100) +
    0.10 * (pak.food_import_dependence / 100)
  threshold: 70
  threshold_std: 10
  sharpness: 0.20
  floor: 0.003
  annual: 0.015
  range: [0.008, 0.025]
  confidence: medium
```

### Current Pressure Estimate

- `pak.water_stress`: ~70 (severe, worsening)
- `pak.debt_external`: ~75% GDP (near threshold)
- `pak.internal_conflict_intensity`: 2 (intermediate)
- `pak.years_since_irregular_transition`: ~2 (recent PTI crisis)
- `pak.protest_intensity_annual`: ~45 (elevated)
- `pak.food_import_dependence`: ~35%
- **Current pressure**: ~55/100 (elevated but below threshold)

### Probability Evolution

| Period | Pressure | Annual P | Rationale |
|--------|----------|----------|-----------|
| 2025-2035 | 55→62 | ~1.3% | Current trajectory; water stress worsening |
| 2035-2045 | 62→72 | ~2.0% | Entering threshold zone; glacier melt accelerating |
| 2045-2060 | 72→80+ | ~2.5-3.5% | Peak water stress period |
| 2060-2075 | 80+ | ~3.0%+ | Very high pressure or adaptation |

### Case Against

**Military has always intervened before failure**: Pakistan's military seizes power when civilian governance fails (1958, 1969, 1977, 1999). "State failure" in the Syria/Somalia sense may be impossible because military would impose order first.

*Counter*: Military fragmentation IS possible under severe stress. The 1971 breakup demonstrates this.

**External support will always arrive**: Pakistan is "too nuclear to fail." China ($60B+ CPEC), US (nuclear security), Gulf states (remittances), IMF have repeatedly bailed out Pakistan.

*Counter*: Each bailout creates more debt; bailout fatigue sets in. Rapid collapse could outrun external response.

**1.5%/year is too high for a nuclear state**: No nuclear-armed state has ever failed. International stabilization pressure is enormous.

*Counter*: Nuclear dimension creates intervention incentive but doesn't guarantee success. Internal dynamics determine collapse.

### Key Uncertainties

- Indus water trajectory (faster glacial melt → pressure rises faster)
- Military cohesion vs. fragmentation
- External support willingness (IMF, China, Gulf states)
- Climate shock timing (2022 floods were preview)
- India-Pakistan dynamics (external conflict could trigger cascade)

---

## Factor Loadings

```yaml
factors:
  F_SAS: 0.43  # This IS the South Asian anchor crisis
  F_FOOD: 0.26 # Indus water-agriculture nexus is core vulnerability
  F_CLIM: 0.23 # Glacial melt, monsoon variability, flood risk
  F_FIN: 0.18  # Chronic fiscal crisis; IMF dependency
  F_GPT: 0.13  # US-China competition affects aid flows
  F_MENA: 0.10 # Afghan border, Gulf remittances
  F_HLTH: 0.08 # Healthcare vulnerability
  F_EAS: 0.05  # Via China relationship
  F_TECH: 0.02 # Marginal
  F_EUR: 0.02  # Diaspora link
variance: 0.65  # Type 2 target
```

---

## Branches

```yaml
branches:
  - {id: controlled, p: 0.40, desc: "Military maintains core; periphery autonomous; international intervention"}
  - {id: fragmentation, p: 0.45, desc: "State fragments along provincial lines; prolonged civil conflict"}
  - {id: collapse, p: 0.15, desc: "Military fragments; no coherent authority; nuclear security crisis"}
```

---

## Impacts

### Transmission Channels

**Migration**: Borders largely closed (India militarized, Afghanistan in crisis, Iran/Gulf limited). "Trapped population" dynamic — displacement is internal or results in mortality.

**Nuclear Security**: Military cohesion is key. External intervention likely if fragmentation occurs.

**Regional Contagion**: Afghanistan destabilization, India refugee/terrorism pressure, China CPEC losses.

**Remittance Collapse**: ~$30B/year; Gulf workers expelled during crisis deepens economic spiral.

```yaml
impacts:
  controlled:
    # Pakistan
    - {var: pak.gdp_real,                    mag: [-0.28, 0.08], onset: {gradual: 2}, decay: 15}
    - {var: pak.internal_conflict_intensity, mag: [2, 0.5],      onset: immediate, decay: 8}
    - {var: pak.idp_population,              mag: [17, 7],       onset: {gradual: 2}, decay: 15}
    - {var: pak.refugee_outflow,             mag: [3.5, 2],      onset: {gradual: 3}, decay: 20}
    - {var: pak.unemployment_rate,           mag: [0.14, 0.06],  onset: immediate, decay: 10}
    - {var: pak.life_expectancy,             mag: [-4, 2],       onset: {gradual: 3}, decay: 15}
    
    # Regional
    - {var: ind.gdp_real,                    mag: [-0.007, 0.004], onset: {delayed: 1}, decay: 3}
    - {var: ind.refugee_inflow,              mag: [1.4, 1],      onset: {gradual: 2}, decay: 15}
    - {var: afg.internal_conflict_intensity, mag: [0.5, 0.3],    onset: {delayed: 1}, decay: 5}
    
    # Global
    - {var: active_major_conflicts,          mag: [1, 0],        onset: immediate, until: resolved}

  fragmentation:
    inherit: controlled
    scale: 1.4

  collapse:
    inherit: controlled
    scale: 2.5
```

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

- Nuclear dimension unprecedented; military cohesion is key swing variable
- Indus water timeline calibration
- External intervention scenarios

## Open Questions

1. Will military fragment or intervene to prevent collapse?
2. How robust are nuclear command-and-control systems under stress?
3. Would US/China/India intervene? How?
4. What are realistic mortality rates with closed borders?
5. What does reconstitution look like — Somalia model or Yugoslavia model?

---

## Changelog

| Date | Change |
|------|--------|
| 2025-12-17 | Initial Level 1 specification |
| 2025-12-30 | Variance allocation: scaled loadings to Type 2 target |
| 2025-12-30 | Critical review complete; replaced regime_stability with observables |
| 2025-01-03 | Migrated to YAML-embedded schema |

---

*See [[methodology/reference/causal-types]] for Type 2 definition | [[research/collapse-patterns-framework]] for historical analogues*