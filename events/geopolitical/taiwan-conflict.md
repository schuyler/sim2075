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

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | `TAIWAN_CONFLICT` |
| **Scale** | Global |
| **Domain** | Geopolitical |
| **Causal Type** | Type 3: Contingent |
| **Onset Speed** | Sudden (<1yr) |
| **Reversibility** | Partial to Irreversible (aftermath-dependent) |

## Description

Military conflict between PRC and Taiwan, or US-brokered great power settlement fundamentally altering cross-strait relations. Distinguished from baseline tensions and sub-threshold crises by either (a) actual military operations or (b) binding agreements backed by great power guarantees that materially change Taiwan's status. This is the discontinuity; crises that de-escalate without combat or formal settlement are non-events.

Bilateral Taiwan-PRC negotiation is not modeled as a plausible path — the preference sets don't overlap. Settlement requires US involvement as broker and guarantor, fundamentally changing the negotiating dynamic.

---

## Causal Type Specification

### Type 3 (Contingent) Event

This event has Type 3 structure: preconditions create crisis windows, and actor decisions determine whether discontinuity occurs. The probability decomposition is:

- **P(crisis window)**: ~3% annually — acute crisis develops
- **P(discontinuity | window)**: ~65% — military conflict or great power settlement occurs
- **P(event)**: ~2% annually — the discontinuity probability

The ~35% of crisis windows that de-escalate without combat or formal agreement are *non-events* — they don't appear in the simulation as discontinuities.

**Window Preconditions**:

| Condition | Threshold |
|-----------|-----------|
| F_GPT (Great Power Tension) | Sustained above threshold for 2+ years |
| F_EAS (East Asian Tension) | Elevated regional instability context |
| Triggering incident | Election result, sovereignty assertion, military accident, or diplomatic provocation |

**Historical basis for window probability (~3%)**:

Acute crises reaching threshold where military action or major diplomatic shift became imminent:
- 1954-55 First Taiwan Strait Crisis (military engagement)
- 1958 Second Taiwan Strait Crisis (military engagement)
- 1995-96 Third Taiwan Strait Crisis (military mobilization, de-escalated)
- 2022 Pelosi visit tensions (did not reach acute phase)

Pattern: ~3-4 acute crises per century when baseline tensions elevated. Current period has elevated baseline due to PRC military modernization, US strategic competition, and semiconductor stakes.

**Historical basis for discontinuity probability given window (~65%)**:

Of the 3 acute crises since 1954, 2 involved actual military operations (1954-55, 1958). The 1995-96 crisis de-escalated without combat — a non-event in our framework. This suggests roughly two-thirds of acute crises produce discontinuous outcomes.

However, the sample is small and the nuclear context has changed (PRC became nuclear-armed in 1964). Modern crises may have different resolution dynamics. The 65% estimate reflects:
- Historical precedent of PRC willingness to use force
- Elevated current stakes (semiconductors, great power competition)
- Uncertainty about whether nuclear deterrence suppresses or redirects conflict

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | ~2.0% |
| **Low bound** | 1.0% |
| **High bound** | 3.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~40% (at least one discontinuity) |

### Derivation

1. **Window probability**: 3% annually (2-5% range)
2. **Discontinuity given window**: 65% (50-80% range)
3. **Combined**: 3% × 65% = 1.95%, rounded to ~2%

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Taiwan Conflict | ~2.0% | — |
| India-Pakistan Military Conflict | ~0.9% | Lower — more frequent crises but lower conflict-given-crisis |
| Pakistan State Failure | ~1.5% | Similar magnitude |
| Chinese Economic Crisis | ~2.0% | Similar magnitude |
| Global Financial Crisis | ~3.0% | Higher — more frequent, less actor-dependent |

### Key Uncertainties

- **PRC military readiness trajectory**: Rapid capability improvements may shift window toward action
- **US commitment credibility**: Strategic ambiguity creates uncertainty about response
- **Semiconductor stakes**: TSMC's value may increase or decrease conflict likelihood (capture vs. destroy calculus)
- **Domestic politics**: Nationalist pressures on both sides affect crisis behavior

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.00 | No direct pathway |
| F_FIN | 0.20 | Economic stress may affect calculus but secondary |
| F_HLTH | 0.00 | No direct pathway |
| F_GPT | 0.70 | Great power tension is primary driver |
| F_FOOD | 0.00 | No direct pathway |
| F_TECH | 0.15 | Semiconductor competition adds stakes but doesn't drive timing |
| F_EUR | 0.00 | No direct pathway |
| F_MENA | 0.00 | No direct pathway |
| F_SAS | 0.00 | No direct pathway |
| F_EAS | 0.80 | Regional instability directly relevant |
| F_SSA | 0.00 | No direct pathway |
| F_LAM | 0.00 | No direct pathway |

**Sum of squared loadings**: 1.18 ✓

### Loading Rationale

F_EAS and F_GPT are dominant because Taiwan conflict sits at the intersection of regional East Asian dynamics and US-China great power competition. F_FIN and F_TECH provide secondary influence through economic interdependence and semiconductor stakes.

---

## Resolutions

Once a crisis window opens *and* a discontinuity occurs (65% of windows), one of two resolutions:

```yaml
resolutions:
  - id: military_conflict
    probability: 0.65
    description: |
      PRC initiates military action against Taiwan.
      Ranges from blockade to limited strikes to full invasion.
      
  - id: great_power_settlement
    probability: 0.35
    description: |
      US brokers binding settlement between PRC and Taiwan.
      Agreement backed by great power guarantees, materially changing
      Taiwan's status, security arrangements, or governance framework.
      Taiwan's agency is constrained — this is the least-bad option
      that greater powers have arranged, not Taiwan's preferred outcome.

resolution_probability_rationale:
  default: "uniform (50/50)"
  specified: "65/35"
  justification: |
    Settlement faces higher structural barriers than military conflict:
    
    Military conflict barriers:
    - Activation energy for military action
    - Nuclear escalation risk with US involvement
    - Economic costs of conflict with major trading partners
    - Uncertainty about military success
    
    Great power settlement barriers (all of the above, plus):
    - Requires US willingness to reduce its position (domestic political cost)
    - Requires PRC trust in US commitments (historically low)
    - Requires Taiwan acquiescence (democratic legitimacy problems)
    - Must find formula acceptable to all three parties simultaneously
    
    Military conflict only requires one actor (PRC) to decide to act.
    Settlement requires three actors to agree on terms none would accept
    under normal circumstances. This structural asymmetry justifies
    weighting military conflict higher.
    
  confidence: "medium — structural reasoning, not historical base rate"
```

### Concrete Settlement Scenarios

The following scenarios illustrate what a great power settlement might look like. Each requires crisis conditions severe enough to shift preferences away from peacetime positions.

**Scenario 1: Crisis-Driven Grand Bargain**

During acute crisis with imminent military action, US and PRC negotiate directly. US offers reduced military presence in western Pacific (no new bases, reduced exercises, arms sales constraints). PRC accepts formalized Taiwan autonomy with US security guarantee. Taiwan accepts because alternative is war without guaranteed US support.

*Historical analog*: Austrian State Treaty (1955) — four-power agreement establishing Austrian neutrality, ending occupation.

**Scenario 2: Post-Limited-Conflict Settlement**

After limited PRC military action (e.g., seizure of Kinmen/Matsu or brief blockade), US brokers ceasefire. Settlement formalizes new status quo rather than risking escalation. Taiwan accepts loss of outlying islands in exchange for guarantees on Taiwan proper.

*Historical analog*: Korean Armistice (1953) — great power settlement freezing conflict at status quo ante (roughly).

**Scenario 3: Preemptive Accommodation**

US, seeing crisis approaching and doubting ability to prevail militarily, offers PRC a deal addressing core interests (formal diplomatic recognition, reduced military posture) in exchange for binding commitments on Taiwan autonomy. Taiwan accepts under intense US pressure, framed as "peace with dignity."

*Historical analog*: US-brokered Israel-Egypt peace (1978) — superpower pressure on both parties to accept terms neither would choose independently.

**Common features**: In all scenarios, Taiwan's agency is constrained. The settlement isn't Taiwan choosing a good option; it's Taiwan accepting the least-bad option that greater powers have arranged.

---

## Aftermath Branches

### Military Conflict Aftermath

```yaml
resolution: military_conflict
aftermath_branches:

  - id: limited_conflict
    probability: 0.55
    description: |
      Blockade or limited strikes without amphibious invasion.
      Semiconductor supply severely disrupted for 1-3 years.
      No direct US-China military engagement (US provides support but avoids combat).
      
    factor_modifications:
      F_GPT: +0.60
      F_EAS: +0.70
      F_FIN: +0.40
      F_TECH: +0.50
      
    duration:
      type: decaying
      half_life_years: 4
      floor: 0.15
      
    impact_vector:
      global:
        semiconductor_supply: -0.70
        trade_volume: -0.25
        financial_stability: -0.30
      taiwan:
        gdp: -0.40
        sovereignty_status: "contested"
      china:
        gdp: -0.15
        international_standing: -0.40
      united_states:
        gdp: -0.08
        alliance_credibility: -0.20

  - id: full_invasion
    probability: 0.30
    description: |
      Amphibious assault and occupation attempt.
      Catastrophic semiconductor disruption (TSMC facilities damaged or destroyed).
      High probability of US military involvement.
      Prolonged conflict likely (months to years).
      
    factor_modifications:
      F_GPT: +0.90
      F_EAS: +0.85
      F_FIN: +0.60
      F_TECH: +0.80
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.25
      
    cascade_triggers:
      - event_id: US_CHINA_DIRECT_CONFLICT
        window_opens: true
        probability: 0.50
        probability_rationale: |
          US intervention is a small-N actor decision (presidential/congressional choice)
          with the same intractability as resolution probabilities.
          
          Structural factors toward intervention:
          - Taiwan Relations Act creates political/legal pressure
          - Alliance credibility concerns (Japan, Korea, Philippines watching)
          - Domestic political pressure if invasion is televised
          
          Structural factors against intervention:
          - Nuclear escalation risk with peer adversary
          - Economic interdependence costs
          - War-weariness, competing priorities
          
          No clear structural asymmetry identified. Defaulting to 0.50 per entropy
          maximization. Subject to sensitivity analysis.
      - event_id: KOREAN_PENINSULA_CRISIS
        probability_modifier: 1.5
        rationale: "North Korea may see opportunity during US distraction"
        
    impact_vector:
      global:
        semiconductor_supply: -0.95
        trade_volume: -0.40
        financial_stability: -0.50
      taiwan:
        gdp: -0.70
        sovereignty_status: "occupied_or_destroyed"
        population: -0.05  # conflict casualties
      china:
        gdp: -0.25
        military_capacity: -0.15
        international_standing: -0.60
      united_states:
        gdp: -0.12
        military_capacity: -0.10

  - id: nuclear_escalation
    probability: 0.15
    description: |
      Conflict escalates to nuclear weapons use.
      Most likely: tactical use against military targets or demonstration strike.
      Civilizational-scale consequences regardless of limited vs. full exchange.
      
    factor_modifications:
      F_GPT: +1.50
      F_EAS: +1.20
      F_FIN: +1.00
      F_CLIM: +0.10  # nuclear winter effects if large exchange
      F_HLTH: +0.30
      
    duration:
      type: persistent
      exit_conditions: null  # permanent regime shift in international system
      
    cascade_triggers:
      - event_id: GLOBAL_NUCLEAR_RECONFIGURATION
        window_opens: true
        probability: 1.0
        rationale: "Nuclear taboo broken; proliferation incentives transform"
        
    impact_vector:
      global:
        semiconductor_supply: -0.98
        trade_volume: -0.70
        nuclear_taboo: "broken"
        institutional_capacity: -0.40
      # Regional impacts depend heavily on exchange scale
      # Level 2 research needed for detailed specification

aftermath_probability_rationale: |
  Limited conflict weighted highest (0.55) based on:
  - Amphibious assault is logistically demanding; blockade-first is militarily rational
  - Full invasion triggers near-certain US response; limited action may not
  - TSMC value as intact asset creates incentive to avoid destruction
  - PRC stated preference for peaceful unification (revealed preference uncertain)
  
  Full invasion weighted 0.30:
  - Once conflict begins, escalation pressures are strong
  - Limited conflict may not achieve political objectives
  - Sunk cost and domestic politics push toward decisive action
  
  Nuclear escalation weighted 0.15:
  - PRC no-first-use policy (though may not hold if regime survival threatened)
  - US extended deterrence creates escalation risk
  - Tactical nuclear use increasingly discussed in military literature
  - Low but non-negligible given stakes
  
  These aftermath probabilities have more structural grounding than resolution
  probabilities — military logistics, escalation dynamics, and precedent analysis
  provide traction that small-N actor decisions do not.
```

### Great Power Settlement Aftermath

```yaml
resolution: great_power_settlement
aftermath_branches:

  - id: stable_framework
    probability: 0.40
    description: |
      Durable settlement backed by credible great power guarantees.
      Key features: explicit US security commitment to Taiwan, PRC commitment
      to non-use of force, Taiwan constraints on independence/alliance options,
      verification mechanisms, and defined escalation procedures.
      Represents genuine tension reduction through binding commitments.
      
    factor_modifications:
      F_GPT: -0.15
      F_EAS: -0.20
      
    duration:
      type: maintenance_required
      annual_failure_probability: 0.05
      failure_modes:
        - "US domestic political change withdraws commitment"
        - "PRC leadership change repudiates constraints"
        - "Taiwan election produces government that rejects framework"
        - "External shock (e.g., North Korea crisis) strains guarantees"
        
    impact_vector:
      global:
        trade_confidence: +0.10
        semiconductor_supply_security: +0.15
        great_power_tension: -0.15
      taiwan:
        sovereignty_status: "defined_autonomy_guaranteed"
        economic_integration_prc: +0.20
        security_guarantee_status: "formalized_us_commitment"
        political_autonomy: "constrained_but_protected"
      china:
        international_standing: +0.15
        taiwan_policy_objective: "partially_achieved"
        us_military_presence: "reduced"
      united_states:
        alliance_credibility: -0.10  # some allies view as partial abandonment
        military_posture_asia: "reduced"
        great_power_management: +0.20  # demonstrated crisis resolution capacity

  - id: unstable_framework
    probability: 0.60
    description: |
      Settlement reached under crisis pressure, but with structural weaknesses.
      Agreement is binding and represents discontinuity from status quo ante,
      but contains ambiguities (creative or otherwise), lacks robust enforcement,
      or faces domestic opposition in one or more parties.
      Creates period of formal framework with elevated collapse risk.
      
    factor_modifications:
      F_GPT: +0.10
      F_EAS: +0.15
      
    duration:
      type: maintenance_required
      annual_failure_probability: 0.12
      failure_modes:
        - "Domestic political change in any party repudiates agreement"
        - "Ambiguous terms lead to conflicting interpretations"
        - "One party tests boundaries, triggering escalation"
        - "Verification failures erode trust"
        
    modifies_future_events:
      - event_id: TAIWAN_CONFLICT
        window_probability_modifier: 1.5
        rationale: "Framework collapse creates new crisis with higher stakes — previous failure raises costs of backing down"
        
    impact_vector:
      taiwan:
        sovereignty_status: "formally_redefined_unstable"
        governance_autonomy: "contested"
        security_guarantee_status: "ambiguous"
      china:
        credibility: +0.05  # achieved formal agreement
        taiwan_policy_objective: "partially_achieved_fragile"
      united_states:
        alliance_credibility: -0.15
        commitment_clarity: "reduced"

aftermath_probability_rationale: |
  Unstable framework weighted higher (0.60) because:
  - Crisis-driven agreements prioritize speed over durability
  - Three-party agreements are inherently harder to stabilize than bilateral
  - Each party has domestic audiences that may reject compromise
  - Historical precedent: 1992 Consensus was ambiguous and eventually contested
  - Verification and enforcement mechanisms are difficult to design
  
  Stable framework possible (0.40) if:
  - Crisis severity creates political space for substantive compromise
  - US provides credible enforcement mechanism (e.g., explicit treaty)
  - Agreement structure allows face-saving for all parties
  - Subsequent political transitions in all parties accept framework
  
  Key distinction: Both aftermath branches represent genuine discontinuities.
  An unstable framework is still a binding agreement that changes Taiwan's
  legal/political status — it can fail later, but its existence is itself
  a break from the status quo ante.

---

## Case Against

### 1. Probability may be too high

**Argument**: Nuclear deterrence and economic interdependence make Taiwan conflict substantially less likely than historical crises suggest. The 1954-58 crises occurred before PRC had nuclear weapons and before deep economic integration. Modern conflict would be catastrophic for both sides in ways that didn't apply historically.

**Counter**: PRC has invested heavily in military capabilities specifically designed for Taiwan scenarios. This investment is not consistent with deterrence-only posture. Additionally, nationalist pressures and "century of humiliation" narrative create political incentives that may override economic rationality.

### 2. Great power settlement may still be implausible

**Argument**: Even at 35%, the weight on settlement may be too high. The scenarios require US willingness to reduce its position, PRC trust in US commitments, and Taiwan acquiescence to constrained autonomy. Each of these faces severe barriers. The US has no domestic constituency for accommodation; PRC has no reason to trust US commitments given historical record; Taiwan's democracy would likely reject any framework imposed by great powers.

**Counter**: Crisis dynamics differ from peacetime analysis. Faced with imminent catastrophic conflict, preferences may shift in ways current politics don't reveal. Historical precedents (Austria 1955, Korea 1953) show great powers can impose settlements when the alternative is unacceptable. The 35% weight may even be conservative if PRC military capabilities make US conventional defense untenable.

### 3. Non-event probability may be too low

**Argument**: 35% non-event probability may understate crisis management capacity. The 1995-96 crisis de-escalated despite military mobilization. International pressure, economic stakes, and nuclear risks all push toward de-escalation.

**Counter**: If this is true, it argues for lower window probability rather than higher non-event share. The window is meant to capture crises where discontinuity is genuinely imminent.

### What would change estimate 2x+

| Change | Direction | Magnitude |
|--------|-----------|-----------|
| PRC successful amphibious exercise | ↑ | +50-100% window probability |
| Taiwan nuclear latency revelation | ↑ | +100% conflict probability |
| US explicit defense commitment | ↓ | -30-50% (deterrence) or ↑ +30% (commitment trap) |
| Major cross-strait economic agreement | ↓ | -40% window probability |
| PRC leadership succession crisis | ↑ | +50% window probability |

---

## Cascade Effects

| Pathway | Target Event | Effect | Duration |
|---------|--------------|--------|----------|
| Full invasion → US involvement | US_CHINA_DIRECT_CONFLICT | Window opens (50%) | Immediate |
| Nuclear use → global reconfiguration | GLOBAL_NUCLEAR_RECONFIGURATION | Window opens (100%) | Permanent |
| Regional instability | KOREAN_PENINSULA_CRISIS | ×1.5 | 3 years |
| Economic disruption → China stress | CHINESE_ECONOMIC_CRISIS | ×1.3 | 5 years |

---

## Transmission Channels

### Semiconductor Channel
Taiwan produces ~90% of advanced semiconductors. Any conflict scenario severely disrupts global technology supply chains. Effects persist for years even after conflict ends due to infrastructure damage and supply chain reconfiguration.

### Trade Channel
Cross-strait conflict disrupts major shipping lanes. Global trade volume impacts depend on conflict intensity and duration.

### Financial Channel
Conflict triggers capital flight, currency volatility, and risk repricing across Asian markets. Effects transmit globally through financial linkages.

### Alliance Channel
US response (or non-response) affects alliance credibility in Japan, Korea, Philippines, and beyond. Framework agreements affect perceptions of US commitment.

---

## Sensitivity Analysis Notes

Key uncertainties for Phase 3 sensitivity testing:

| Parameter | Range to Test | Why It Matters |
|-----------|---------------|----------------|
| Window probability | 0.02 - 0.05 | Drives expected timing of crisis |
| Discontinuity given window | 0.50 - 0.80 | Determines how many crises produce lasting change |
| Military vs. settlement split | 0.50/0.50 to 0.80/0.20 | Different tail risk profiles |
| Limited vs. full invasion split | 0.40/0.45 to 0.70/0.15 | Major difference in semiconductor/escalation outcomes |
| Nuclear escalation probability | 0.05 - 0.25 | Tail risk driver |
| US involvement probability | 0.40 - 0.80 | Determines whether conflict stays regional |

---

## Research Upgrade Path

**Level 2 (4-8 hours):**
- Systematic analysis of historical crisis resolution patterns
- Military logistics literature on invasion vs. blockade scenarios
- Semiconductor supply chain resilience analysis
- US alliance credibility and commitment literature
- Great power settlement precedents (Austria 1955, Korea 1953, Camp David 1978)
- US domestic politics constraints on accommodation

**Level 3 (20+ hours):**
- Expert elicitation on aftermath probabilities (not resolution probabilities)
- Detailed supply chain modeling for impact vectors
- War-gaming literature synthesis
- Nuclear escalation scenario analysis
- Taiwan domestic politics deep-dive
- PRC decision-making under crisis conditions

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-22 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Semiconductor impact modeling; great power settlement plausibility; nuclear escalation pathways |

## Open Questions

- Great power settlement precedent analysis (Austria, Korea, Camp David)
- US domestic political constraints on accommodation
- PRC trust in US commitments under different scenarios
- Taiwan democratic legitimacy constraints on imposed settlements
- PRC military readiness assessment and timeline
- US commitment credibility under different political scenarios
- TSMC destruction vs. capture calculus
- Nuclear escalation pathways specific to Taiwan scenario

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| Dec 2025 | Initial Level 1 specification | Task 1.1 worked example |
| Dec 2025 | Critical review revision | Applied critical review rubric: removed status quo restoration as resolution (fails discontinuity test), rebalanced to 50/50 military/negotiated, added Case Against section, clarified probability decomposition following India-Pakistan template |
| Dec 2025 | Great power settlement reframe | Reframed "negotiated resolution" as "great power settlement" requiring US brokerage. Lowered probability to 35% (from 50%) based on structural asymmetry analysis. Added concrete settlement scenarios with historical analogs. Bilateral Taiwan-PRC negotiation implausible — preference sets don't overlap. |

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/india-pakistan-military-conflict]] for comparable Type 3 specification*