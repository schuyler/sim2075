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

---

## Description

Military conflict between PRC and Taiwan, or US-brokered great power settlement fundamentally altering cross-strait relations. Distinguished from baseline tensions and sub-threshold crises by either (a) actual military operations or (b) binding agreements backed by great power guarantees that materially change Taiwan's status. This is the discontinuity; crises that de-escalate without combat or formal settlement are non-events.

Bilateral Taiwan-PRC negotiation is not modeled as a plausible path — the preference sets don't overlap. Settlement requires US involvement as broker and guarantor, fundamentally changing the negotiating dynamic.

---

## Specification

```yaml
id: TAIWAN_CONFLICT
domain: political
scale: global
causal_type: 3
onset: sudden
reversibility: partial
```

---

## Probability

```yaml
probability:
  window: 0.03
  preconditions:
    all:
      - "F_GPT > 1.0"
      - "F_EAS > 1.0"
      - "chn.military_spending_deviation > 0.15"
      - "usa.external_conflict_involvement < 3"
    sustained:
      - expr: "F_GPT > 1.0"
        years: 2
  resolution: 0.65
  annual: 0.020
  range: [0.010, 0.035]
  confidence: medium
```

### Derivation

Window probability (3%/year) derived from historical acute crises:
- 1954-55 First Taiwan Strait Crisis (military engagement)
- 1958 Second Taiwan Strait Crisis (military engagement)
- 1995-96 Third Taiwan Strait Crisis (de-escalated — non-event)

Of three acute crises since 1954, two produced discontinuous outcomes → 65% resolution probability.

### Window Probability Evolution

| Period | Annual P | Rationale |
|--------|----------|-----------|
| 2025-2030 | ~3% | Current elevated baseline; PRC military modernization continuing |
| 2030-2035 | ~4% | PRC likely reaches peak military readiness relative to US |
| 2035-2075 | ~3-4% | Path-dependent on prior resolution |

### Key Uncertainties

- PRC military readiness trajectory
- US commitment credibility
- Semiconductor stakes (TSMC value may increase or decrease conflict likelihood)
- Domestic nationalist pressures on both sides

### Case Against

**Probability may be too high**: Nuclear deterrence and economic interdependence make conflict substantially less likely than historical crises suggest. The 1954-58 crises occurred before PRC nuclear weapons and deep economic integration.

*Counter*: PRC has invested heavily in military capabilities specifically for Taiwan scenarios. Nationalist pressures may override economic rationality.

**Great power settlement may be implausible**: Even at 35%, weight on settlement may be too high. Requires US willingness to reduce position, PRC trust in US commitments, Taiwan acquiescence — each faces severe barriers.

*Counter*: Crisis dynamics differ from peacetime analysis. Historical precedents (Austria 1955, Korea 1953) show great powers can impose settlements when alternatives are unacceptable.

**Type 3 structure may impose false precision**: The decomposition into window × resolution may give false confidence when these are deeply entangled.

*Counter*: The decomposition is a modeling choice, not a claim about underlying structure. It helps organize reasoning.

---

## Factor Loadings

```yaml
factors:
  F_EAS: 0.38   # Regional instability directly relevant
  F_GPT: 0.33   # Great power tension primary driver
  F_FIN: 0.09   # Economic stress may affect calculus
  F_TECH: 0.07  # Semiconductor competition adds stakes
variance: 0.45  # Type 3 target
```

---

## Resolutions

Once a crisis window opens *and* a discontinuity occurs (65% of windows), one of two resolutions:

**Military Conflict** (65%): PRC initiates military action against Taiwan. Ranges from blockade to limited strikes to full invasion. Requires only one actor (PRC) to decide to act.

**Great Power Settlement** (35%): US brokers binding settlement between PRC and Taiwan. Requires three actors to agree on terms none would accept under normal circumstances — structural asymmetry justifies lower weight.

```yaml
resolutions:
  - id: military_conflict
    p: 0.65
    branches:
      - {id: limited, p: 0.55, desc: "Blockade or limited strikes"}
      - {id: full_invasion, p: 0.30, desc: "Amphibious assault attempt"}
      - {id: nuclear, p: 0.15, desc: "Escalation to nuclear use"}
  - id: settlement
    p: 0.35
    branches:
      - {id: stable, p: 0.40, desc: "Durable framework with credible guarantees"}
      - {id: unstable, p: 0.60, desc: "Agreement with structural weaknesses"}
```

---

## Impacts

### Transmission Channels

**Semiconductor**: Taiwan produces ~90% of advanced semiconductors. Any conflict severely disrupts global technology supply chains.

**Trade**: Cross-strait conflict disrupts major shipping lanes.

**Financial**: Conflict triggers capital flight, currency volatility, risk repricing.

```yaml
impacts:
  military_conflict.limited:
    - {var: semiconductor_supply,              mag: [-0.70, 0.15], onset: immediate, decay: 2}
    - {var: global_trade_volume,               mag: [-0.15, 0.05], onset: immediate, decay: 3}
    - {var: global_credit_spread,              mag: [200, 80],     onset: immediate, decay: 1}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}
    - {var: twn.gdp_real,                      mag: [-0.40, 0.15], onset: immediate, decay: 5}
    - {var: twn.external_conflict_involvement, mag: [4, 0],        onset: immediate, until: resolved}
    - {var: chn.gdp_real,                      mag: [-0.15, 0.08], onset: immediate, decay: 3}
    - {var: chn.sanctions_level,               mag: [50, 20],      onset: immediate, permanent: true}
    - {var: chn.external_conflict_involvement, mag: [3.5, 0.5],    onset: immediate, until: resolved}
    - {var: usa.gdp_real,                      mag: [-0.08, 0.04], onset: immediate, decay: 2}

  military_conflict.full_invasion:
    inherit: military_conflict.limited
    scale: 1.5

  military_conflict.nuclear:
    inherit: military_conflict.limited
    scale: 3.0

  settlement.stable:
    - {var: global_credit_spread,              mag: [-50, 20],     onset: immediate, decay: 2}
    - {var: twn.gdp_real,                      mag: [-0.05, 0.03], onset: immediate, decay: 3}
    - {var: chn.gdp_real,                      mag: [0.02, 0.01],  onset: {delayed: 1}, decay: 5}

  settlement.unstable:
    inherit: settlement.stable
    scale: 0.5
```

---

## Cascades

```yaml
cascades:
  triggers:
    - {event: KOREAN_PENINSULA_CRISIS,  delta: 0.015, years: 3}
    - {event: CHINESE_ECONOMIC_CRISIS,  delta: 0.020, years: 5}
    - {event: CHINESE_POLITICAL_CRISIS, delta: 0.010, years: 5,
       if: "resolution == 'military_conflict'"}
  triggered_by:
    - {event: CHINESE_ECONOMIC_CRISIS,  delta: 0.005}
    - {event: CHINESE_POLITICAL_CRISIS, delta: 0.010}
    - {event: US_CONSTITUTIONAL_CRISIS, delta: 0.005}
```

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-01-02
  review: complete
  upgrade: true
```

### Upgrade Rationale

- Semiconductor impact modeling
- Great power settlement plausibility
- Nuclear escalation pathways

## Open Questions

1. How do Austria 1955, Korea 1953, Camp David 1978 inform settlement plausibility?
2. What are realistic limits on US accommodation given domestic politics?
3. What is realistic PRC military readiness timeline relative to US?
4. Would PRC destroy or try to capture TSMC facilities?
5. Under what scenarios does nuclear use become plausible?

---

## Changelog

| Date | Change |
|------|--------|
| 2025-12-22 | Initial Level 1 specification |
| 2025-12-22 | Revised resolution structure — removed status quo |
| 2025-12-30 | Variance allocation: scaled loadings to Type 3 target |
| 2025-12-30 | Critical review complete |
| 2025-01-01 | Migrated to YAML-embedded schema |
| 2025-01-02 | Fixed variable names to match state catalog |

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/india-pakistan-military-conflict]] for comparable Type 3*
