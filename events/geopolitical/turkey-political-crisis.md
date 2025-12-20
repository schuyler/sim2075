---
title: turkey-political-crisis
type: note
permalink: events/geopolitical/turkey-political-crisis
tags:
- event
- type-2
- threshold
- geopolitical
- political-crisis
- turkey
- mena
- europe
- level-1
---

# Turkey Political Crisis

**Type 2 (Threshold) Event** — Probability increases as economic, political, and social pressures accumulate; threshold dynamics govern transition from stressed but functional state to acute political crisis.

This specification follows the pattern established in [[events/geopolitical/egypt-state-failure]] and [[events/geopolitical/iran-regime-change]], adapted for Turkey's distinct vulnerability profile: a middle-income democracy experiencing democratic backsliding, severe currency instability, massive refugee burden, and unresolved Kurdish conflict—but with stronger institutions and economic base than regional comparators.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | TURKEY_POLITICAL_CRISIS |
| **Scale** | National (with significant regional and European consequences) |
| **Domain** | Political |
| **Causal Type** | **Type 2: Threshold** |
| **Onset Speed** | Rapid (1-3 years from trigger to acute phase) |
| **Reversibility** | Partial (democratic recovery possible but institutional damage may persist) |

## Description

Fundamental destabilization of Turkish governance, characterized by economic collapse (currency crisis, hyperinflation), political breakdown (democratic collapse, succession crisis, or military intervention), state fragmentation (loss of control in Kurdish regions), or cascading crisis triggered by natural disaster. Turkey's vulnerability is distinctive: a middle-income NATO member with significant institutional capacity experiencing democratic backsliding, chronic currency instability driven by unorthodox monetary policy, hosting the world's largest refugee population, and facing an unresolved internal conflict.

This is a **state transition**: `turkey.regime_stability` crosses below crisis threshold (~30), triggering shift from "stressed but functional democracy" to "acute political crisis" state.

**What marks occurrence**: Government loses ability to manage economic crisis (hyperinflation, capital flight, banking collapse); political system breaks down (constitutional crisis, military intervention, violent succession struggle); or state loses effective control of significant territory (Kurdish regions, major urban areas).

**Important distinction**: Turkey is qualitatively different from Egypt or Iran—it has functioning (if degraded) democratic institutions, a diversified middle-income economy, and NATO membership. "Crisis" here means something more severe than Turkey's chronic political turbulence; it means a discontinuous breakdown that fundamentally alters the state's trajectory.

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Turkey political crisis exhibits threshold dynamics:
- Multiple stressors accumulate: currency instability, political polarization, refugee burden, Kurdish conflict, earthquake vulnerability
- System absorbs stress through institutional flexibility and economic resilience until capacity exhausted
- No single stochastic trigger (Type 1) or actor decision (Type 3) dominates
- The 2016 coup attempt, 2018 currency crisis, and 2023 earthquake showed the system can absorb major shocks—until it can't

**Type 3 elements exist but are secondary**: Military intervention decisions and Erdoğan succession involve identifiable actors, but the overall dynamic is pressure accumulation toward threshold. These Type 3 elements are captured in severity branches rather than making the event itself Type 3.

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `turkey.currency_stability` | 0.30 | inverse | Lira crises are primary economic vulnerability; unorthodox monetary policy amplifies |
| `turkey.regime_stability` | 0.25 | inverse | Political polarization, democratic backsliding, institutional erosion |
| `turkey.inflation_rate` | 0.20 | threshold(50) | High inflation erodes living standards and political legitimacy |
| `turkey.social_cohesion` | 0.15 | inverse | Refugee-host tensions, Kurdish conflict, secular-religious divide |
| `turkey.external_position` | 0.10 | inverse | NATO/EU relations, sanctions risk, regional conflicts |

**Pressure calculation**:
```
pressure = 0.30 × (100 - currency_stability) / 100
         + 0.25 × (100 - regime_stability) / 100
         + 0.20 × inflation_threshold_function(inflation_rate)
         + 0.15 × (100 - social_cohesion) / 100
         + 0.10 × (100 - external_position) / 100
```
*Normalized to 0-100 scale*

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 68 (on 0-100 pressure scale) |
| **Uncertainty** | ±8 |
| **Sharpness (k)** | 0.15 (moderate; Turkey has absorption capacity but cascade is rapid once triggered) |
| **Historical calibration** | 2001 crisis (~pressure 60, IMF intervention prevented cascade); 2016 coup attempt (~pressure 55, suppressed); 2018 currency crisis (~pressure 50, managed with difficulty); 2023 earthquake (~pressure 55, absorbed) |

### Key Vulnerability: Currency/Monetary Policy

Turkey's primary economic vulnerability deserves emphasis:
- Lira has lost ~80% of value against USD since 2018
- Unorthodox monetary policy (low rates during high inflation) amplifies instability
- Large external financing needs (~$200B+ annual rollover)
- Foreign currency debt exposure in corporate sector
- Central bank credibility severely damaged
- **Political economy trap**: Erdoğan's commitment to low rates makes orthodox stabilization politically difficult

A severe currency crisis could trigger political crisis even if other pressures are moderate—the 2001 crisis demonstrated this pathway.

### Key Vulnerability: Political Succession

Turkey lacks a clear succession mechanism:
- Erdoğan has dominated Turkish politics since 2003 (PM then President)
- No obvious successor within AKP; potential rivals marginalized
- Opposition fragmented but showed strength in 2023 elections
- Constitutional system highly personalized around Erdoğan
- Health or death of Erdoğan would create immediate uncertainty

### Key Vulnerability: Earthquake Risk

Turkey sits on major fault lines; Istanbul particularly vulnerable:
- 2023 earthquake (50,000+ deaths) demonstrated vulnerability and state capacity limits
- Istanbul earthquake (modeled at M7.0+) could cause 30,000-100,000 deaths and massive economic damage
- Earthquake could trigger cascade: economic damage → financial crisis → political crisis
- This is partly Type 1 (seismic risk) but integrated into Type 2 pressure accumulation

### Key Strength: Institutional Resilience

Despite vulnerabilities, Turkey possesses:
- Diversified middle-income economy ($900B+ GDP)
- Functioning (if stressed) institutions
- NATO membership provides security umbrella
- Strong export sector and tourism industry
- Demonstrated ability to absorb major shocks (2016, 2018, 2023)
- Geographic position gives strategic leverage

### Minimum Probability

**Floor**: 0.4%/year (residual risk from sudden shocks: Erdoğan death/incapacitation, major earthquake, external military incident)

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.0% |
| **Low bound** | 0.6% |
| **High bound** | 1.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~22% at point estimate |

### Current Pressure Estimate

Current pressure: ~48/100 (elevated but well below threshold)
- `currency_stability`: ~30 (chronic lira weakness; repeated crises)
- `regime_stability`: ~45 (functioning but degraded; 2023 elections showed resilience)
- `inflation_rate`: ~50-60% (elevated but declining from peak)
- `social_cohesion`: ~40 (refugee tensions, polarization, but not acute)
- `external_position`: ~50 (NATO member but relations strained; regional entanglements)

### Derivation

1. **Base rate for middle-income democracies with economic stress**: Variable; ranges from stable (Poland, Chile) to crisis-prone (Argentina, Brazil in 1990s)
2. **Turkey-specific factors**:
   - *Stabilizing*: Larger and more diversified economy than Egypt/Iran; NATO membership; functioning democratic opposition; export competitiveness; demonstrated shock absorption (2016, 2018, 2023)
   - *Destabilizing*: Chronic currency instability; unorthodox monetary policy; democratic backsliding; refugee burden; Kurdish conflict; earthquake exposure; succession uncertainty
3. **Comparative assessment**: More resilient than Egypt (stronger institutions, diversified economy); more volatile than Iran (currency instability more acute, though regime is less consolidated); comparable to historical Argentina/Turkey in 1990s-2000s crisis-prone period
4. **Central estimate**: 1.0%/year (range 0.6-1.5%)

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- Lower than: Egypt state failure (~1.5%), Pakistan state failure (~1.5%) due to stronger economic/institutional base
- Similar to: Russia state failure (~1.0%), Iran regime change (~1.2%)
- Higher than: Saudi regime instability (~0.8%) due to currency vulnerability and political competition

### Key Uncertainties

- **Monetary policy trajectory**: Return to orthodoxy would reduce economic pressure; continued heterodoxy maintains vulnerability
- **Erdoğan succession**: Smooth transition vs. contested succession dramatically affects near-term probability
- **Earthquake timing**: Major Istanbul earthquake would stress-test all systems simultaneously
- **Refugee dynamics**: Mass return to Syria would reduce pressure; new influx would increase it
- **Kurdish conflict trajectory**: Resolution vs. escalation
- **NATO/EU relationship**: Further deterioration vs. rapprochement
- **Global financial conditions**: Strong dollar, rising rates increase Turkey's external vulnerability

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_MENA** | 0.50 | Regional spillover, Kurdish dimension spans Syria/Iraq, refugee source |
| **F_FIN** | 0.45 | Currency vulnerability, external financing needs, EM contagion |
| **F_EUR** | 0.40 | NATO member, EU candidate, migration route, democratic standards |
| **F_GPT** | 0.35 | Russia-West balancing, sanctions risk, strategic positioning |
| F_CLIM | 0.15 | Heat stress, agricultural impacts, water management (as upstream power) |
| F_FOOD | 0.10 | Agricultural exporter but inflation affects food access domestically |
| F_SAS | 0.05 | Limited; some Afghanistan refugee pathway |
| F_EAS | 0.00 | No significant pathway |
| F_SSA | 0.00 | No significant pathway |
| F_LAM | 0.00 | No significant pathway |
| F_HLTH | 0.00 | No distinct pathway beyond general state capacity |
| F_TECH | 0.00 | No significant pathway |

**Sum of squared loadings**: 0.73 ✓

### Loading Interpretation (Type 2)

Factors shock state variables that feed into pressure function:
- High F_MENA → regional instability, Kurdish conflict escalation, refugee flows → `social_cohesion` pressure, conflict costs
- High F_FIN → EM currency pressure, capital flight, external financing stress → `currency_stability` drops sharply
- High F_EUR → EU/NATO tensions, democratic conditionality, sanctions risk → `external_position` pressure
- High F_GPT → geopolitical pressure, forced alignment choices, sanctions risk → `external_position` and `regime_stability` pressure
- High F_CLIM → agricultural stress, internal migration → modest `social_cohesion` pressure

---

## Severity Branches

Once threshold is crossed, the form of crisis varies:

```yaml
severity_branches:

  - id: economic_crisis_managed
    probability: 0.45
    description: |
      Severe economic crisis—currency collapse, hyperinflation, banking stress—
      but political system absorbs shock. Government implements emergency 
      measures (capital controls, IMF program, policy U-turn). Significant 
      GDP contraction, living standards decline, political damage to 
      incumbent government. May lead to electoral defeat but not regime 
      breakdown. 2001 crisis pattern: severe but recoverable.
      
    impact_multiplier: 1.0  # baseline
    
    factor_modifications:
      F_FIN: +0.30
      F_EUR: +0.15
      
    duration:
      type: decaying
      half_life_years: 4
      floor: 0.10

  - id: political_breakdown
    probability: 0.30
    description: |
      Political system breaks down beyond normal crisis management.
      Possibilities include: Erdoğan succession crisis (contested or 
      chaotic), constitutional crisis, prolonged political paralysis,
      or democratic collapse into authoritarian consolidation. State
      continues to function but political trajectory fundamentally
      altered. International isolation likely deepens. May involve
      significant political violence or repression.
      
    impact_multiplier: 2.0
    
    factor_modifications:
      F_EUR: +0.40
      F_GPT: +0.30
      F_MENA: +0.25
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.15
      
    cascade_triggers:
      - event_id: NATO_CRISIS
        probability_modifier: 1.5
        rationale: "Turkey's NATO status becomes contested"
      - event_id: KURDISH_AUTONOMY_EXPANSION
        probability_modifier: 1.8
        rationale: "Political weakness creates Kurdish opportunity"

  - id: state_fragmentation
    probability: 0.15
    description: |
      State loses effective control over significant territory or 
      functions. Most likely pathway is Kurdish regions achieving
      de facto autonomy during central government crisis. Could also
      involve military fragmentation, regional power centers, or 
      prolonged civil conflict. Less severe than Syria-style collapse
      due to stronger institutions, but represents fundamental state
      failure. Massive refugee outflows likely.
      
    impact_multiplier: 3.5
    
    factor_modifications:
      F_EUR: +0.55
      F_MENA: +0.50
      F_GPT: +0.35
      F_FIN: +0.30
      
    duration:
      type: decaying
      half_life_years: 12
      floor: 0.20
      
    cascade_triggers:
      - event_id: KURDISH_STATE_FORMATION
        probability: 0.40
        rationale: "Turkish Kurdistan joins Syrian/Iraqi Kurdish autonomy"
      - event_id: EUROPEAN_MIGRATION_CRISIS
        probability_modifier: 2.5
        rationale: "80M+ population; geographic position on migration route"
      - event_id: NATO_ARTICLE_5_CRISIS
        probability: 0.30
        rationale: "What are NATO obligations during internal collapse?"
      - event_id: BOSPHORUS_TRANSIT_DISRUPTION
        probability: 0.50
        rationale: "Strategic chokepoint affected"

  - id: earthquake_cascade
    probability: 0.10
    description: |
      Major earthquake (likely Istanbul, M7.0+) triggers cascading
      crisis across economic, political, and social dimensions 
      simultaneously. Massive casualties (50,000-100,000+), economic
      destruction ($100B+), state capacity overwhelmed, political 
      legitimacy crisis. International assistance mobilized but 
      recovery takes decade+. Distinct from other branches because
      natural disaster is proximate cause and damage profile is 
      different (concentrated physical destruction).
      
    impact_multiplier: 4.0
    
    factor_modifications:
      F_EUR: +0.45
      F_FIN: +0.50
      F_MENA: +0.30
      
    duration:
      type: decaying
      half_life_years: 15
      floor: 0.25
      
    cascade_triggers:
      - event_id: GLOBAL_REINSURANCE_CRISIS
        probability_modifier: 1.5
        rationale: "Istanbul earthquake is reinsurance industry nightmare scenario"
      - event_id: BOSPHORUS_TRANSIT_DISRUPTION
        probability: 0.60
        rationale: "Port and transit infrastructure damaged"

severity_probability_rationale: |
  Distribution reflects Turkey's structural features:
  
  - Economic crisis managed (0.45): Most likely crisis mode. Turkey has
    absorbed multiple economic shocks (2001, 2018) through IMF programs
    and policy adjustment. Institutions remain functional enough for
    crisis management. This is painful but recoverable.
    
  - Political breakdown (0.30): Requires either succession crisis or
    political system failure. Erdoğan succession is genuine uncertainty.
    Democratic opposition showed strength in 2023 but system is stacked.
    Military has intervened historically but 2016 coup attempt and
    subsequent purges make this less likely.
    
  - State fragmentation (0.15): Requires multiple failures: central
    authority collapse AND Kurdish regions seize opportunity AND 
    military cannot restore control. Lower than Egypt/Iran equivalent
    because Turkey has stronger institutional base and NATO membership
    creates external stabilization incentive. But Kurdish dimension
    creates fragmentation pathway that Egypt/Iran lack.
    
  - Earthquake cascade (0.10): Conditional on this event occurring
    during a period when earthquake also occurs. The probability here
    is P(earthquake triggers cascade | crisis threshold crossed), not
    P(earthquake). Major Istanbul earthquake is ~2%/year; this branch
    captures cases where earthquake is the trigger that pushes system
    over threshold.
```

---

## Impact Vector

### Turkey Impacts (Baseline: Economic Crisis Managed Branch)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `turkey.gdp_real` | ↓ | -15% ± 8% | rapid(1yr) | decaying (half_life: 5yr, floor: -5%) |
| `turkey.regime_stability` | ↓ | to <35 | immediate | regime_dependent |
| `turkey.currency_value` | ↓ | -50% ± 25% | immediate | decaying (half_life: 3yr) |
| `turkey.inflation_rate` | ↑ | +40% ± 20% | immediate | decaying (half_life: 2yr) |
| `turkey.fdi_inflows` | ↓ | -60% ± 25% | rapid(6mo) | decaying (half_life: 5yr) |
| `turkey.unemployment` | ↑ | +8% ± 4% | rapid(1yr) | decaying (half_life: 4yr) |

### Regional Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `syria.reconstruction_prospects` | ↓ | -20 ± 10 | delayed(1yr) | persistent |
| `iraq.kurdish_region_stability` | variable | ±15 | delayed(1yr) | persistent |
| `greece.security_environment` | ↓ | -10 ± 5 | immediate | regime_dependent |
| `bulgaria.economic_exposure` | ↓ | -8% ± 4% | rapid(6mo) | decaying |
| `europe.migration_pressure` | ↑ | +2M ± 1M | rapid(1yr) | decaying |
| `mena_aggregate.stability` | ↓ | -10 ± 5 | delayed(1yr) | decaying |

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.em_risk_premium` | ↑ | +50bp ± 25bp | immediate | decaying (half_life: 1yr) |
| `global.grain_prices` | ↑ | +5% ± 3% | immediate | decaying (half_life: 6mo) |
| `nato.cohesion` | ↓ | -10 ± 5 | delayed(6mo) | regime_dependent |

### Bosphorus/Dardanelles Consideration

Turkey controls the Turkish Straits (~3% of global oil trade, significant grain trade, Black Sea access):
- Economic crisis managed: Straits remain open; normal operations
- Political breakdown: Straits likely remain open but uncertainty affects shipping costs
- State fragmentation: Potential disruption; international pressure to maintain transit
- Earthquake cascade: Physical damage possible; temporary disruption likely

### NATO Dimension

Turkey is NATO's second-largest military and controls the alliance's southeastern flank:
- Economic crisis: NATO relationship strained but functional
- Political breakdown: Article 5 ambiguity; democratic backsliding strains alliance
- State fragmentation: Unprecedented NATO crisis; no framework for member state collapse
- Earthquake cascade: NATO mobilizes humanitarian response

### Durability Rationale

- **GDP**: Decaying with moderate half-life; Turkey has recovery capacity but starting position is damaged
- **Currency**: Decaying; can stabilize with policy change but credibility takes time to rebuild
- **FDI**: Decaying with longer half-life; investor confidence slow to return
- **Regional stability effects**: Persistent; Kurdish dimension creates lasting changes
- **Migration flows**: Decaying; return migration possible but slow

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Kurdish opportunity | KURDISH_STATE_FORMATION | +3%/year | 10 years | Turkish Kurdistan joins Syrian/Iraqi Kurdish autonomy |
| Migration pressure | EU_POLITICAL_CRISIS | +1%/year | 5 years | Turkey-EU deal collapses; migration surge |
| EM contagion | EM_FINANCIAL_CRISIS | +2%/year | 2 years | Contagion to other vulnerable EMs |
| NATO stress | NATO_COHESION_CRISIS | +1%/year | 5 years | Alliance framework tested |
| Regional instability | SYRIA_FRAGMENTATION_DEEPENS | +2%/year | 5 years | Turkish buffer zone collapses |
| Strait disruption | BLACK_SEA_ACCESS_CRISIS | +2%/year | Duration of crisis | Russian/Ukrainian grain exports affected |

### Impact Chains

**Pathway 1**: Turkey crisis → EU migration surge → European politics
```
Political breakdown → Turkey-EU deal collapses → Refugee/migrant flows resume →
European border pressure → Political polarization → P(EU fragmentation dynamics) ↑
```

**Pathway 2**: Turkey crisis → Kurdish consolidation → Regional map change
```
State fragmentation → Central control of Kurdish regions lost →
Turkish Kurdistan seeks autonomy → Links to Syrian/Iraqi Kurdistan →
P(Kurdish state formation) ↑
```

**Pathway 3**: Turkey crisis → EM contagion → Global financial stress
```
Currency collapse → EM risk repricing → Capital flight from vulnerable EMs →
Financial stress → P(broader EM crisis) ↑
```

**Pathway 4**: Turkey crisis → NATO uncertainty → Security vacuum
```
State fragmentation → NATO Article 5 ambiguity → Alliance credibility questioned →
Adversaries test commitments → P(NATO cohesion crisis) ↑
```

---

## Transmission Channels

### Financial/Currency Channel

**Mechanism**: Turkey's currency crisis affects EM asset class broadly; banking sector linkages
**Affected regions**: Europe (bank exposures), other EMs (contagion), global (risk sentiment)
**Affected variables**: `global.em_risk_premium`, `europe.bank_stress`, `turkey.credit_access`
**Differential exposure**: European banks with Turkey exposure; EMs with similar vulnerability profile (current account deficit, external debt)

### Migration Channel

**Mechanism**: Turkey hosts ~4M Syrian refugees plus transit migration; crisis disrupts containment
**Affected regions**: Europe (via Greece, Bulgaria), Middle East (return flows)
**Affected variables**: `europe.migration_pressure`, `greece.border_stress`, `syria.refugee_return`
**Notes**: Turkey-EU migration deal is key policy lever; collapse would produce discontinuous increase

### Kurdish Conflict Channel

**Mechanism**: Turkish state weakness creates opportunity for Kurdish autonomy/independence movement
**Affected regions**: Turkey, Syria, Iraq, Iran (all have Kurdish populations)
**Affected variables**: `[country].territorial_integrity`, `regional.border_stability`
**Notes**: Kurdish dimension is unique to Turkey among the MENA regime crisis events

### NATO/Security Channel

**Mechanism**: Turkey's NATO membership creates alliance-wide implications
**Affected regions**: NATO members, Black Sea region, Eastern Mediterranean
**Affected variables**: `nato.cohesion`, `regional.security_architecture`
**Notes**: No precedent for NATO member state collapse; Article 5 ambiguity

### Strait Transit Channel

**Mechanism**: Bosphorus/Dardanelles control affects Black Sea access and trade
**Affected regions**: Russia, Ukraine (grain exports), global (oil, grain trade)
**Affected variables**: `global.grain_prices`, `global.shipping_costs`
**Notes**: Less critical than Suez (Egypt) but still significant chokepoint

---

## Historical Analogues

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| Turkey 2001 | Same country; economic crisis | IMF intervention can stabilize; but political cost is high |
| Turkey 2016 | Same country; coup attempt | Military intervention pathway exists but was defeated; purges followed |
| Turkey 2018 | Same country; currency crisis | System absorbed shock but damage accumulated |
| Turkey 2023 | Same country; earthquake | State capacity limits revealed; political system survived |
| Argentina 2001-02 | Similar economic crisis | Currency board collapse, default, political chaos, but recovery possible |
| Greece 2010-15 | EU member economic crisis | External support prevents worst outcomes but sovereignty constrained |
| Yugoslavia 1990s | State fragmentation with ethnic dimension | Fragmentation along ethnic/regional lines is possible |

---

## Early Warning Indicators

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| Lira exchange rate | Weak but stable | >50% depreciation in 12 months is warning |
| Inflation rate | ~50-60%, declining | >100% is danger zone |
| Central bank reserves | Depleted then rebuilt | Net reserves <$20B is warning |
| Foreign debt rollover | Manageable | Rollover failures are critical warning |
| Erdoğan health | Functioning | Any serious illness is warning |
| Political violence | Low | Sustained increase is warning |
| Kurdish conflict intensity | Contained | Major escalation is warning |
| Refugee flows | Stable | Large new influx or mass return is warning |
| Istanbul earthquake precursors | Ongoing seismic activity | N/A (unpredictable) |
| Capital flight | Elevated but stable | Acceleration is warning |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-19 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Istanbul earthquake modeling; Kurdish conflict dynamics; Erdoğan succession scenarios; banking sector exposure analysis; NATO contingency planning |

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- IMF Article IV consultations (economic assessment)
- World Bank Turkey data
- Istanbul earthquake risk studies
- Kurdish conflict analysis
- NATO strategic assessments
- European migration data (Frontex, UNHCR)
- Turkish banking sector analysis

## Open Questions

- **Monetary policy trajectory**: Will Turkey return to orthodox policy? Under what conditions?
- **Erdoğan succession**: Who are plausible successors? What is transition mechanism?
- **Istanbul earthquake timing**: When (not if) will major earthquake occur?
- **Kurdish resolution path**: Is political resolution possible? Under what conditions?
- **NATO contingency**: What would NATO do if Turkey fragments? Article 5 implications?
- **EU relationship trajectory**: Accession dead? What replaces it?
- **Refugee deal durability**: What triggers collapse of Turkey-EU migration deal?
- **Military political role**: Is military intervention still possible post-2016 purges?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-19 | Initial Level 1 specification | Task 2.1.10 - Type 2 political crisis event |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/egypt-state-failure]] for regional comparison | [[events/geopolitical/iran-regime-change]] for regional comparison*