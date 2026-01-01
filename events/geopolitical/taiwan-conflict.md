---
title: taiwan-conflict
type: note
permalink: events/geopolitical/taiwan-conflict
tags:
- event
- type-3
- geopolitical
- east-asia
- taiwan
- china
- level-1
---

# Taiwan Conflict

**Type 3 (Contingent) Event** — Military conflict or great power settlement following acute cross-strait crisis.

## Description

Military conflict between PRC and Taiwan, or US-brokered great power settlement fundamentally altering cross-strait relations. Distinguished from baseline tensions and sub-threshold crises by either (a) actual military operations or (b) binding agreements backed by great power guarantees that materially change Taiwan's status. This is the discontinuity; crises that de-escalate without combat or formal settlement are non-events.

Bilateral Taiwan-PRC negotiation is not modeled as a plausible path — the preference sets don't overlap. Settlement requires US involvement as broker and guarantor, fundamentally changing the negotiating dynamic.

---

## Specification

```yaml
id: TAIWAN_CONFLICT
scale: global
domain: political
causal_type: 3
onset: sudden
reversibility: partial
```

---

## Causal Type Specification

This event has Type 3 structure: preconditions create crisis windows, and actor decisions determine whether discontinuity occurs. The ~35% of crisis windows that de-escalate without combat or formal agreement are *non-events* — they don't appear in the simulation as discontinuities.

```yaml
window:
  annual_probability: 0.03
  preconditions:
    - variable: F_GPT
      condition: "> 1.0 sustained 2+ years"
    - variable: F_EAS
      condition: "> 1.0"
    - variable: chn.military_spending_deviation
      condition: "> 0.15"
    - variable: usa.external_conflict_involvement
      condition: "< 3"
resolution_given_window: 0.65
```

**Historical basis for window probability (~3%)**:

Acute crises reaching threshold where military action or major diplomatic shift became imminent:
- 1954-55 First Taiwan Strait Crisis (military engagement)
- 1958 Second Taiwan Strait Crisis (military engagement)
- 1995-96 Third Taiwan Strait Crisis (military mobilization, de-escalated)
- 2022 Pelosi visit tensions (did not reach acute phase)

Pattern: ~3-4 acute crises per century when baseline tensions elevated. Current period has elevated baseline due to PRC military modernization, US strategic competition, and semiconductor stakes.

**Historical basis for discontinuity probability given window (~65%)**:

Of the 3 acute crises since 1954, 2 involved actual military operations (1954-55, 1958). The 1995-96 crisis de-escalated without combat — a non-event in our framework. This suggests roughly two-thirds of acute crises produce discontinuous outcomes.

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4:

**1. Probability may be too high**

Nuclear deterrence and economic interdependence make Taiwan conflict substantially less likely than historical crises suggest. The 1954-58 crises occurred before PRC had nuclear weapons and before deep economic integration. Modern conflict would be catastrophic for both sides in ways that didn't apply historically.

*Counter*: PRC has invested heavily in military capabilities specifically designed for Taiwan scenarios. This investment is not consistent with deterrence-only posture. Additionally, nationalist pressures and "century of humiliation" narrative create political incentives that may override economic rationality.

**2. Great power settlement may be implausible**

Even at 35%, the weight on settlement may be too high. The scenarios require US willingness to reduce its position, PRC trust in US commitments, and Taiwan acquiescence to constrained autonomy. Each of these faces severe barriers.

*Counter*: Crisis dynamics differ from peacetime analysis. Faced with imminent catastrophic conflict, preferences may shift. Historical precedents (Austria 1955, Korea 1953) show great powers can impose settlements when the alternative is unacceptable.

**3. Non-event probability may be too low**

35% non-event probability may understate crisis management capacity. The 1995-96 crisis de-escalated despite military mobilization.

*Counter*: If this is true, it argues for lower window probability rather than higher non-event share. The window is meant to capture crises where discontinuity is genuinely imminent.

**4. Type 3 structure may impose false precision**

The decomposition into window probability × resolution probability may give false confidence. In reality, these are deeply entangled.

*Counter*: The decomposition is a modeling choice, not a claim about underlying structure. It helps organize reasoning even if imperfect.

---

## Probability

```yaml
probability:
  annual: 0.020
  low: 0.010
  high: 0.035
  confidence: medium
```

### Derivation

1. **Window probability**: 3% annually (2-5% range)
2. **Discontinuity given window**: 65% (50-80% range)
3. **Combined**: 3% × 65% = 1.95%, rounded to ~2%

### Comparative Ranking

- **India-Pakistan Military Conflict** (~0.9%): Lower — more frequent crises but lower conflict-given-crisis
- **Pakistan State Failure** (~1.5%): Similar magnitude
- **Chinese Economic Crisis** (~2.0%): Similar magnitude
- **Global Financial Crisis** (~3.0%): Higher — more frequent, less actor-dependent

### Window Probability Evolution

| Period | Estimated | Rationale |
|--------|-----------|-----------|
| 2025-2030 | ~3%/year | Current elevated baseline; PRC military modernization continuing |
| 2030-2035 | ~4%/year | PRC likely reaches peak military readiness relative to US |
| 2035-2045 | ~3-4%/year | Depends on resolution of current trajectory |
| 2045-2075 | Uncertain | Either accommodation reached or permanent tension |

### Key Uncertainties

- **PRC military readiness trajectory**: Rapid capability improvements may shift window toward action
- **US commitment credibility**: Strategic ambiguity creates uncertainty about response
- **Semiconductor stakes**: TSMC's value may increase or decrease conflict likelihood
- **Domestic politics**: Nationalist pressures on both sides affect crisis behavior

---

## Factor Loadings

*Scaled per [[methodology/reference/variance-allocation]] for Type 3 target.*

```yaml
factor_loadings:
  F_EAS: 0.38  # Regional instability directly relevant
  F_GPT: 0.33  # Great power tension primary driver
  F_FIN: 0.09  # Economic stress may affect calculus
  F_TECH: 0.07 # Semiconductor competition adds stakes
variance_explained: 0.45
scale_factor: 0.47
```

---

## Resolutions

Once a crisis window opens *and* a discontinuity occurs (65% of windows), one of two resolutions:

**Military Conflict** (65%): PRC initiates military action against Taiwan. Ranges from blockade to limited strikes to full invasion. Requires only one actor (PRC) to decide to act.

**Great Power Settlement** (35%): US brokers binding settlement between PRC and Taiwan. Agreement backed by great power guarantees, materially changing Taiwan's status, security arrangements, or governance framework. Requires three actors to agree on terms none would accept under normal circumstances—structural asymmetry justifies lower weight.

```yaml
resolutions:
  - id: military_conflict
    probability: 0.65
    branches:
      - id: limited_conflict
        probability: 0.55
        description: "Blockade or limited strikes without amphibious invasion"
      - id: full_invasion
        probability: 0.30
        description: "Amphibious assault and occupation attempt"
      - id: nuclear_escalation
        probability: 0.15
        description: "Conflict escalates to nuclear weapons use"
  - id: great_power_settlement
    probability: 0.35
    branches:
      - id: stable_framework
        probability: 0.40
        description: "Durable settlement with credible guarantees"
      - id: unstable_framework
        probability: 0.60
        description: "Agreement with structural weaknesses; elevated collapse risk"
```

---

## Impact Vectors

### Transmission Channels

**Semiconductor Channel**: Taiwan produces ~90% of advanced semiconductors. Any conflict scenario severely disrupts global technology supply chains.

**Trade Channel**: Cross-strait conflict disrupts major shipping lanes. Impacts depend on conflict intensity and duration.

**Financial Channel**: Conflict triggers capital flight, currency volatility, and risk repricing.

```yaml
impacts:
  military_conflict.limited_conflict:
    global:
      - var: semiconductor_supply
        dir: -1
        mag: [0.70, 0.15]
        onset: immediate
        durability: {type: decaying, half_life: 2}
      - var: global_trade_volume
        dir: -1
        mag: [0.15, 0.05]
        onset: immediate
        durability: {type: decaying, half_life: 3}
      - var: global_credit_spread
        dir: +1
        mag: [200, 80]
        onset: immediate
        durability: {type: decaying, half_life: 1}
      - var: active_major_conflicts
        dir: +1
        mag: [1, 0]
        onset: immediate
        durability: {type: regime_dependent, persists_until: resolution}
    twn:
      - var: gdp_real
        dir: -1
        mag: [0.40, 0.15]
        onset: immediate
        durability: {type: decaying, half_life: 5}
      - var: external_conflict_involvement
        dir: +1
        mag: [4, 0]
        onset: immediate
        durability: {type: regime_dependent, persists_until: resolution}
    chn:
      - var: gdp_real
        dir: -1
        mag: [0.15, 0.08]
        onset: immediate
        durability: {type: decaying, half_life: 3}
      - var: sanctions_level
        dir: +1
        mag: [50, 20]
        onset: immediate
        durability: {type: permanent}
      - var: external_conflict_involvement
        dir: +1
        mag: [3.5, 0.5]
        onset: immediate
        durability: {type: regime_dependent, persists_until: resolution}
    usa:
      - var: gdp_real
        dir: -1
        mag: [0.08, 0.04]
        onset: immediate
        durability: {type: decaying, half_life: 2}

  military_conflict.full_invasion:
    _base: military_conflict.limited_conflict
    _multiplier: 1.5

  military_conflict.nuclear_escalation:
    _base: military_conflict.limited_conflict
    _multiplier: 3.0

  great_power_settlement.stable_framework:
    global:
      - var: global_credit_spread
        dir: -1
        mag: [50, 20]
        onset: immediate
        durability: {type: decaying, half_life: 2}
    twn:
      - var: gdp_real
        dir: -1
        mag: [0.05, 0.03]
        onset: immediate
        durability: {type: decaying, half_life: 3}
    chn:
      - var: gdp_real
        dir: +1
        mag: [0.02, 0.01]
        onset: delayed(1)
        durability: {type: decaying, half_life: 5}

  great_power_settlement.unstable_framework:
    _base: great_power_settlement.stable_framework
    _multiplier: 0.5
```

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - target: KOREAN_PENINSULA_CRISIS
      delta: +0.015
      duration: 3
      mechanism: "North Korea may see opportunity"
    - target: CHINESE_ECONOMIC_CRISIS
      delta: +0.020
      duration: 5
      mechanism: "Sanctions, trade disruption, confidence shock"
    - target: CHINESE_POLITICAL_CRISIS
      delta: +0.010
      duration: 5
      mechanism: "If military failure, regime stress"
  triggered_by:
    - source: CHINESE_ECONOMIC_CRISIS
      delta: +0.005
      mechanism: "Nationalist distraction; domestic pressure"
    - source: CHINESE_POLITICAL_CRISIS
      delta: +0.010
      mechanism: "Leadership instability may trigger action"
    - source: US_CONSTITUTIONAL_CRISIS
      delta: +0.005
      mechanism: "US distraction creates perceived window"
```

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-31
  critical_review: complete
  upgrade_candidate: true
  upgrade_rationale: "Semiconductor impact modeling; great power settlement plausibility; nuclear escalation pathways"
```

## Open Questions

1. **Great power settlement precedent**: How do Austria 1955, Korea 1953, Camp David 1978 inform plausibility?
2. **US domestic constraints**: What are realistic limits on accommodation given domestic politics?
3. **PRC military readiness**: What is realistic timeline for peak capability relative to US?
4. **TSMC destruction calculus**: Would PRC destroy or try to capture facilities?
5. **Nuclear escalation pathways**: Under what scenarios does nuclear use become plausible?

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-22 | Initial Level 1 specification | Type 3 worked example |
| 2025-12-22 | Revised resolution structure | Removed status quo as resolution; added great power settlement frame |
| 2025-12-30 | Variance allocation: scaled loadings | Factor-explained variance reduced to Type 3 target (0.45) |
| 2025-12-30 | Critical review complete | Fixed event/variable references; added Case Against section |
| 2025-12-31 | Migrated to YAML-embedded format | Task 4.2 - literate specification structure |

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/india-pakistan-military-conflict]] for comparable Type 3 specification*