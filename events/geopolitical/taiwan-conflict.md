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

**Type 3 (Contingent) Event** — Resolution depends on small-N actor decisions during crisis window.

This specification demonstrates Type 3 calibration methodology. See [[methodology/reference/type-3-calibration]] for the operational guidance this example follows.

---

## Event Summary

| Attribute | Value |
|-----------|-------|
| Event ID | `taiwan_conflict` |
| Type | 3 (Contingent) |
| Domain | Geopolitical |
| Primary Region | East Asia |
| Status | Level 1 complete |

**Description**: Acute cross-strait crisis escalating to potential military confrontation between PRC and Taiwan, with high probability of US involvement.

---

## Factor Loadings

How systemic factors affect window probability:

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_GPT | 0.70 | Great power tension is primary driver |
| F_EAS | 0.80 | Regional instability directly relevant |
| F_FIN | 0.20 | Economic stress may affect calculus but secondary |
| F_TECH | 0.15 | Semiconductor competition adds stakes but doesn't drive timing |

---

## Window Specification

The event requires a crisis window to open before resolution is sampled.

```yaml
window:
  description: |
    Acute crisis phase where military action becomes imminent possibility.
    Characterized by: military mobilization indicators, diplomatic breakdown,
    public ultimatums, or triggering incident requiring response.
  
  preconditions:
    - "F_GPT sustained above threshold for 2+ years"
    - "F_EAS elevated (regional instability context)"
    - "Triggering incident occurs (election, sovereignty assertion, accident)"
  
  annual_window_probability: 0.03
  
  probability_rationale: |
    Historical frequency of Taiwan Strait crises reaching acute phase:
    - 1954-55 First Taiwan Strait Crisis
    - 1958 Second Taiwan Strait Crisis  
    - 1995-96 Third Taiwan Strait Crisis
    - 2022 Pelosi visit tensions (did not reach acute phase)
    
    Roughly 3-4 crises per century when baseline tensions elevated.
    Current period has elevated baseline; estimate 3% annual window probability.
    
    Level 1 estimate. Would benefit from:
    - Systematic crisis cataloging with severity classification
    - Analysis of what distinguishes acute vs. sub-acute crises
```

---

## Resolutions

Once window opens, one of three resolutions occurs:

```yaml
resolutions:
  - id: military_conflict
    probability: 0.33
    description: |
      PRC initiates military action against Taiwan.
      Ranges from blockade to limited strikes to full invasion.
      
  - id: negotiated_accommodation
    probability: 0.33
    description: |
      Crisis de-escalates through diplomatic engagement.
      May involve formal or informal agreements modifying status quo.
      
  - id: status_quo_restoration
    probability: 0.33
    description: |
      Crisis de-escalates without substantive resolution.
      Return to prior tension baseline with crisis memory effects.

resolution_probability_rationale:
  default: "uniform (33/33/33)"
  specified: "33/33/33"
  justification: |
    No structural asymmetry identified at Level 1 justifying deviation.
    
    Considered and rejected:
    - "Military action has higher activation energy" — true, but PRC has
      invested heavily in rapid-strike capabilities reducing this gap
    - "Accommodation requires mutual agreement" — also a barrier, faces
      domestic political constraints on both sides
    - "Status quo is path of least resistance" — but crisis window implies
      pressure that makes status quo uncomfortable
    
    Defaulting to uniform. Level 2 research could examine:
    - Structural constraints on each resolution
    - Historical crisis resolution patterns (with analogy limitations noted)
    - Activation energy asymmetries in current military posture
  confidence: "n/a (using default)"
```

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
      - event_id: us_china_direct_conflict
        window_opens: true
        probability: 0.60
        rationale: "US treaty ambiguity but strong political pressure for response"
      - event_id: korean_peninsula_crisis
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
      - event_id: global_nuclear_reconfiguration
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

### Negotiated Accommodation Aftermath

```yaml
resolution: negotiated_accommodation
aftermath_branches:

  - id: stable_new_framework
    probability: 0.40
    description: |
      New cross-strait framework accepted by both parties.
      May involve: formal diplomatic ties, economic integration agreements,
      security guarantees, or modified "one China" formulation.
      Represents genuine tension reduction.
      
    factor_modifications:
      F_GPT: -0.10  # tension reduction
      F_EAS: -0.15
      
    duration:
      type: maintenance_required
      annual_failure_probability: 0.05
      failure_modes:
        - "Domestic political change invalidates agreement"
        - "External shock disrupts framework"
        - "Gradual erosion through non-compliance"
        
    impact_vector:
      global:
        trade_confidence: +0.10
      taiwan:
        sovereignty_status: "ambiguous_but_stable"
        economic_integration_prc: +0.30
      china:
        international_standing: +0.15

  - id: unstable_settlement
    probability: 0.60
    description: |
      Face-saving de-escalation without fundamental resolution.
      Both sides claim victory; underlying issues unaddressed.
      Tensions remain elevated; future crisis probability increased.
      
    factor_modifications:
      F_GPT: +0.15
      F_EAS: +0.20
      
    duration:
      type: decaying
      half_life_years: 5
      floor: 0.10
      
    modifies_future_events:
      - event_id: taiwan_conflict
        window_probability_modifier: 1.3
        rationale: "Unresolved crisis increases future crisis likelihood"
        
    impact_vector:
      taiwan:
        sovereignty_status: "unchanged_but_precarious"
      china:
        credibility: -0.10  # failed to achieve objectives

aftermath_probability_rationale: |
  Unstable settlement weighted higher (0.60) because:
  - Fundamental issues (sovereignty, security) are difficult to resolve
  - Domestic politics on both sides constrain genuine compromise
  - Face-saving exits are easier than substantive agreements
  - Historical pattern of crises ending without resolution
  
  Stable framework possible (0.40) if:
  - Crisis severity creates political space for compromise
  - External pressure (US, international) pushes toward settlement
  - Leadership on both sides willing to spend political capital
```

### Status Quo Restoration Aftermath

```yaml
resolution: status_quo_restoration
aftermath_branches:

  - id: default
    probability: 1.0
    description: |
      Crisis passes without military action or formal resolution.
      Return to baseline tensions with modest elevation from crisis memory.
      Neither side achieved objectives; underlying dynamics unchanged.
      
    factor_modifications:
      F_GPT: +0.10
      F_EAS: +0.15
      
    duration:
      type: decaying
      half_life_years: 3
      floor: 0.05
      
    impact_vector:
      # Minimal lasting impact; crisis becomes historical reference point
      global:
        crisis_precedent: "taiwan_2030s"  # for future scenario analysis
```

---

## Sensitivity Analysis Notes

Key uncertainties for Phase 3 sensitivity testing:

| Parameter | Range to Test | Why It Matters |
|-----------|---------------|----------------|
| Window probability | 0.01 - 0.05 | Drives expected timing of crisis |
| Limited vs. full invasion split | 0.40/0.45 to 0.70/0.15 | Major difference in semiconductor/escalation outcomes |
| Nuclear escalation probability | 0.05 - 0.25 | Tail risk driver |
| US involvement probability | 0.40 - 0.80 | Determines whether conflict stays regional |
| Semiconductor recovery half-life | 2-6 years | Duration of tech disruption |

---

## Research Upgrade Path

**Level 2 (4-8 hours):**
- Systematic analysis of historical crisis resolution patterns
- Military logistics literature on invasion vs. blockade scenarios
- Semiconductor supply chain resilience analysis
- US alliance credibility and commitment literature

**Level 3 (20+ hours):**
- Expert elicitation on aftermath probabilities (not resolution probabilities)
- Detailed supply chain modeling for impact vectors
- War-gaming literature synthesis
- Nuclear escalation scenario analysis

---

## Sources and Calibration

*Level 1 specification based on general knowledge. Source documentation to be added per [[methodology/project/tasks]] Task 1.6 (research documentation standards).*

Key references for future documentation:
- Taiwan Strait crisis history (1954-55, 1958, 1995-96)
- TSMC and semiconductor supply chain analysis
- US-Taiwan Relations Act and strategic ambiguity literature
- PLA amphibious assault capability assessments

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| Dec 2025 | Initial Level 1 specification | Task 1.1 worked example |

---

*See [[methodology/reference/type-3-calibration]] for calibration methodology | [[methodology/reference/aftermath-branches]] for aftermath framework*