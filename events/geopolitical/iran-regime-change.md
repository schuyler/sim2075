---
title: iran-regime-change
type: note
permalink: events/geopolitical/iran-regime-change
tags:
- event
- type-2
- threshold
- geopolitical
- regime-change
- iran
- mena
- level-1
---

# Iran Regime Change

**Type 2 (Threshold) Event** — Probability increases as economic isolation, legitimacy erosion, water crisis, and generational pressure accumulate; threshold dynamics govern transition from stable theocratic state to regime crisis.

This specification follows the pattern established in [[events/geopolitical/saudi-regime-instability]], adapted for Iran's distinct vulnerability profile: ideologically coherent but aging revolutionary regime facing severe economic sanctions, acute water crisis, and deep generational legitimacy gap—offset by effective security services and history of surviving major challenges.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | IRAN_REGIME_CHANGE |
| **Scale** | National (with major regional and global consequences) |
| **Domain** | Political |
| **Causal Type** | **Type 2: Threshold** |
| **Onset Speed** | Rapid (1-3 years from trigger to resolution) |
| **Reversibility** | Partial (regime may reconstitute in different form; full revolutionary transition possible but uncertain) |

## Description

Fundamental destabilization of the Islamic Republic regime, characterized by loss of coercive control, elite fragmentation (particularly IRGC-clerical split), mass popular uprising beyond suppression capacity, or systemic breakdown of governance. Iran's vulnerability is distinctive: an aging revolutionary ideology facing a young, increasingly secular population; severe economic isolation from Western sanctions; and an accelerating water crisis that threatens the habitability of the central plateau including Tehran.

This is a **state transition**: `iran.regime_stability` crosses below crisis threshold (~35), triggering shift from "stable theocratic state" to "regime crisis" state.

**What marks occurrence**: Security forces (IRGC, Basij) fragment or refuse orders to suppress protests; elite defections from revolutionary establishment; Supreme Leader succession crisis that cannot be resolved through normal mechanisms; or economic/environmental collapse that overwhelms regime capacity.

**Important distinction**: This event models regime crisis, not necessarily a specific successor outcome. The Islamic Republic could be replaced by: a reformed Islamic system, a secular democratic government, military rule, fragmentation, or prolonged civil conflict. The aftermath branches capture this uncertainty.

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Iran regime change exhibits threshold dynamics:
- Multiple stressors accumulate: sanctions pressure, legitimacy erosion, water crisis, generational change
- System absorbs stress through ideological mobilization and coercion until capacity exhausted
- No single stochastic trigger (Type 1) or negotiated resolution (Type 3) dominates
- The 2009 Green Movement and 2022 Mahsa Amini protests show the system can absorb major shocks—until it can't

**Type 3 elements exist but are secondary**: External military intervention (US/Israel strike) and elite defection decisions involve identifiable actors, but the overall dynamic is pressure accumulation toward threshold. These Type 3 elements are captured in severity branches rather than making the event itself Type 3.

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `iran.economic_stress` | 0.30 | linear | Sanctions bite; inflation, unemployment, currency collapse |
| `iran.regime_legitimacy` | 0.25 | inverse | Revolutionary ideology fading; reform frustration; religious authority eroding |
| `iran.water_crisis` | 0.20 | exponential | Aquifer depletion, desertification accelerating; existential threat to central plateau |
| `iran.social_contract_stress` | 0.15 | linear | Youth unemployment, gender restrictions, cultural gap with population |
| `iran.elite_cohesion` | 0.10 | inverse | IRGC vs. clerical establishment; succession uncertainty |

**Pressure calculation**:
```
pressure = 0.30 × economic_stress / 100
         + 0.25 × (100 - regime_legitimacy) / 100
         + 0.20 × exp(water_crisis / 50) / exp(2)  # accelerating
         + 0.15 × social_contract_stress / 100
         + 0.10 × (100 - elite_cohesion) / 100
```
*Normalized to 0-100 scale*

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 65 (on 0-100 pressure scale) |
| **Uncertainty** | ±10 |
| **Sharpness (k)** | 0.20 (moderate-sharp; Iranian protests can escalate rapidly when triggered) |
| **Historical calibration** | 1979 Revolution (~pressure crossed 70); 2009 Green Movement (~pressure 55, contained); 2022 protests (~pressure 50-55, contained with difficulty) |

### Key Vulnerability: Water Crisis

Iran's water crisis deserves emphasis as an underappreciated pressure driver:
- Central plateau aquifers (including Tehran region) are being depleted at unsustainable rates
- Lake Urmia has lost ~90% of its surface area
- Agricultural regions face accelerating desertification
- **Government has discussed relocating the capital to the coast** — an extraordinary indicator of crisis severity
- Unlike economic sanctions, water stress cannot be relieved by policy change or sanctions lifting
- Timeline: Crisis intensifies through 2030s-2040s regardless of political developments

The water crisis creates a slow-moving but irreversible pressure component that distinguishes Iran from other regime instability cases.

### Key Vulnerability: Generational Legitimacy Gap

The Islamic Republic was founded in 1979. By 2025:
- ~70% of population born after the revolution
- Revolutionary ideology is inherited doctrine, not lived experience
- Social values (especially among urban youth and women) diverge sharply from regime ideology
- Regime relies increasingly on coercion rather than legitimacy
- Supreme Leader Khamenei is 85+ years old; succession is uncertain

### Key Strength: Coercive Capacity

Despite vulnerabilities, the regime possesses:
- IRGC: ~190,000 personnel with economic interests tied to regime survival
- Basij: Millions of militia members for internal security
- Proven ability to suppress major uprisings (2009, 2019, 2022)
- Sophisticated surveillance and information control
- Ideological core that genuinely believes in the system

### Minimum Probability

**Floor**: 0.4%/year (residual risk from sudden shocks: Supreme Leader death, external military strike, black swan protest trigger)

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.2% |
| **Low bound** | 0.8% |
| **High bound** | 1.8% |
| **Confidence** | Medium |
| **25-year cumulative** | ~26% at point estimate |

### Current Pressure Estimate

Current pressure: ~45/100 (elevated but below threshold)
- `economic_stress`: ~65 (severe sanctions, high inflation, currency crisis)
- `regime_legitimacy`: ~40 (eroded but core supporters remain)
- `water_crisis`: ~55 (severe and worsening; capital relocation discussed)
- `social_contract_stress`: ~60 (youth unemployment high, gender restrictions resented)
- `elite_cohesion`: ~50 (IRGC consolidated but succession uncertainty looms)

### Derivation

1. **Base rate for ideological revolutionary regimes**: Variable; some persist for decades (Cuba, North Korea), others collapse suddenly (Soviet bloc 1989-91, Arab Spring states)
2. **Iran-specific factors**:
   - *Stabilizing*: Effective security services; ideologically committed core; history of surviving major challenges (war with Iraq, 2009/2019/2022 protests); no viable organized opposition; sanctions create rally-around-flag effects
   - *Destabilizing*: Severe economic pressure with no relief path; water crisis accelerating; generational legitimacy gap widening; succession uncertainty; regional position weakening
3. **Comparative assessment**: More resilient than Egypt or pre-2011 Syria (ideological coherence, effective security); less financially cushioned than Saudi Arabia; similar structural position to late Soviet Union (ideological exhaustion, economic stagnation, generational change)
4. **Central estimate**: 1.2%/year (range 0.8-1.8%)

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- More likely than: Saudi regime instability (~0.8%) due to active sanctions pressure and water crisis
- Similar to: Russia state failure (~1.0%), though different vulnerability profile
- Less likely than: Egypt state failure (~1.5%), Pakistan state failure (~1.5%) due to more effective coercive apparatus

### Key Uncertainties

- **Sanctions trajectory**: Relief could reduce economic pressure; "maximum pressure" continuation maintains it
- **Supreme Leader succession**: Smooth transition vs. contested succession dramatically affects near-term probability
- **Water crisis acceleration**: Faster-than-expected depletion could push timeline forward
- **External military action**: Israeli/US strike on nuclear facilities could trigger destabilization or rally-around-flag
- **IRGC loyalty**: Under what conditions might IRGC prioritize institutional survival over regime defense?
- **Protest catalyst**: Unpredictable triggers (like Mahsa Amini's death) can rapidly shift dynamics

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_MENA** | 0.65 | Core MENA power; instability would transform regional dynamics |
| **F_GPT** | 0.45 | US sanctions regime, great power competition, nuclear negotiations |
| **F_CLIM** | 0.35 | Water crisis is existential; affects agricultural base and habitability |
| **F_FIN** | 0.30 | Oil prices, sanctions effects, global finance exclusion |
| F_EAS | 0.15 | China relationship; alternative economic partner |
| F_TECH | 0.10 | Information control challenges; nuclear program trajectory |
| F_FOOD | 0.10 | Agricultural stress from water; food import dependence |
| F_EUR | 0.10 | European policy on sanctions, nuclear deal |
| F_SAS | 0.05 | Limited direct linkage; some Afghanistan spillover |
| F_HLTH | 0.00 | No distinct pathway |
| F_SSA | 0.00 | No significant pathway |
| F_LAM | 0.00 | No significant pathway |

**Sum of squared loadings**: 0.88 ✓

### Loading Interpretation (Type 2)

Factors shock state variables that feed into pressure function:
- High F_MENA → regional instability, proxy network stress → `elite_cohesion` pressure, external pressure
- High F_GPT → increased sanctions pressure, military threat → `economic_stress` rises sharply
- High F_CLIM → accelerated water crisis, agricultural failure → `water_crisis` and `social_contract_stress` rise
- High F_FIN → oil price volatility, reduced export revenue → `economic_stress` rises
- High F_EAS → China economic relationship → potential sanctions relief or tightening

---

## Severity Branches

Once threshold is crossed, the form of regime crisis varies. All branches represent genuine regime crisis—protests that are successfully suppressed without fundamental change, or smooth leadership successions that maintain system continuity, don't trigger this event.

```yaml
severity_branches:

  - id: popular_uprising_suppressed
    probability: 0.40
    description: |
      Mass protests exceed 2022 scale—potentially triggered by economic
      collapse, environmental disaster, or political catalyst. Regime
      deploys maximum force; significant casualties (thousands). Uprising
      eventually suppressed but regime fundamentally weakened. Significant
      international isolation. Brain drain accelerates. Economy further
      damaged. Regime survives but severely delegitimized and weakened;
      future instability more likely. This is a genuine discontinuity
      because the regime's coercive legitimacy and capacity are permanently
      degraded.
      
    impact_multiplier: 1.0  # baseline
    
    factor_modifications:
      F_MENA: +0.25
      F_GPT: +0.20
      
    duration:
      type: decaying
      half_life_years: 4
      floor: 0.10
      
    cascade_triggers:
      - event_id: REFUGEE_CRISIS_MENA
        probability_modifier: 1.8
        rationale: "Brain drain and refugee outflow"
      - event_id: SANCTIONS_INTENSIFICATION
        probability_modifier: 2.0
        rationale: "International response to violent suppression"

  - id: revolutionary_transition
    probability: 0.35
    description: |
      Regime actually falls—security forces fragment or refuse orders,
      elite defections cascade, protests cannot be suppressed. What
      emerges is deeply uncertain: secular democratic government,
      reformed Islamic system, military transitional authority,
      regional fragmentation, or civil conflict. Nuclear facilities
      become major international concern. Proxy networks lose central
      direction. Regional power vacuum.
      
    impact_multiplier: 3.0
    
    factor_modifications:
      F_MENA: +0.65
      F_GPT: +0.55
      F_FIN: +0.35
      F_HLTH: +0.10  # potential for violence, humanitarian crisis
      
    duration:
      type: decaying
      half_life_years: 12
      floor: 0.20
      
    cascade_triggers:
      - event_id: NUCLEAR_SECURITY_CRISIS
        probability: 0.40
        rationale: "Regime collapse raises nuclear material security concerns"
      - event_id: PROXY_NETWORK_COLLAPSE
        probability: 0.60
        rationale: "Hezbollah, Houthis, Iraqi militias lose state sponsor"
      - event_id: KURDISH_AUTONOMY_EXPANSION
        probability: 0.50
        rationale: "Iranian Kurdistan may seek autonomy/independence"
      - event_id: REFUGEE_CRISIS_MAJOR
        probability: 0.70
        rationale: "Millions displaced by instability"

  - id: failed_succession_crisis
    probability: 0.15
    description: |
      Supreme Leader death or incapacitation triggers succession process
      that fails to resolve. IRGC and clerical factions cannot agree on
      successor or power-sharing arrangement. Open elite conflict emerges.
      This is distinct from managed succession (which doesn't trigger
      this event)—here the succession mechanism breaks down, producing
      prolonged institutional paralysis, factional violence, or civil
      conflict. System may eventually reconstitute but only after
      significant instability and permanent damage to institutional
      legitimacy.
      
    impact_multiplier: 2.0
    
    factor_modifications:
      F_MENA: +0.40
      F_GPT: +0.30
      F_FIN: +0.25
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.15
      
    cascade_triggers:
      - event_id: PROXY_NETWORK_WEAKENING
        probability_modifier: 1.5
        rationale: "Hezbollah, Houthis, Iraqi militias lose direction during crisis"
      - event_id: NUCLEAR_PROGRAM_UNCERTAINTY
        probability_modifier: 1.8
        rationale: "Factional control over program uncertain"

  - id: external_intervention_trigger
    probability: 0.10
    description: |
      US or Israeli military strike on nuclear facilities or
      leadership targets triggers regime destabilization. Initial
      strike may produce rally-around-flag effect, but if combined
      with existing pressures, could catalyze broader collapse.
      Distinct from other branches because external action is
      proximate cause. High escalation risk—Iran may retaliate
      against Gulf states, Israel; regional war possible.
      
    impact_multiplier: 4.0
    
    factor_modifications:
      F_MENA: +0.80
      F_GPT: +0.70
      F_FIN: +0.50
      F_FOOD: +0.20  # oil disruption affects food prices
      
    duration:
      type: decaying
      half_life_years: 10
      floor: 0.25
      
    cascade_triggers:
      - event_id: STRAIT_OF_HORMUZ_CRISIS
        probability: 0.70
        rationale: "Iran retaliates against oil shipping"
      - event_id: GULF_STATE_ATTACKS
        probability: 0.60
        rationale: "Iran strikes Saudi/UAE/Bahrain"
      - event_id: ISRAEL_IRAN_WAR
        probability: 0.80
        rationale: "Escalation to broader conflict"
      - event_id: OIL_SUPPLY_CRISIS
        probability: 0.75
        rationale: "Regional conflict disrupts ~20% of global oil"

severity_probability_rationale: |
  Distribution reflects Iran's structural features, conditional on
  actual regime crisis occurring. Smooth successions where the Islamic
  Republic continues with a new Supreme Leader don't trigger this event.
  
  - Popular uprising suppressed (0.40): Most likely crisis mode. 2009
    and 2022 showed regime can suppress major protests, but a crisis-level
    uprising would be larger and suppression more costly. Regime survives
    but permanently weakened—this is a discontinuity because coercive
    capacity and legitimacy are durably degraded, unlike normal protest
    cycles.
    
  - Revolutionary transition (0.35): Requires multiple failures: elite
    fragmentation AND security force defection AND mass mobilization.
    1979 shows it can happen in Iran specifically. Higher probability
    than in Russia because ideological exhaustion is more advanced and
    population is more mobilized.
    
  - Failed succession crisis (0.15): Khamenei is 85+; succession will
    eventually occur. Most successions will be managed (not triggering
    this event). This branch captures scenarios where the succession
    mechanism fails—factional deadlock, open conflict, institutional
    breakdown. Lower probability because IRGC has strong interest in
    managed transition.
    
  - External intervention trigger (0.10): Requires deliberate US/Israeli
    decision to strike AND that strike catalyzes regime collapse rather
    than rally-around-flag. Both conditions are uncertain. However, the
    consequences of this pathway are severe enough to warrant distinct
    modeling.
```

---

## Impact Vector

### Iran Impacts (Baseline: Popular Uprising Suppressed Branch)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `iran.gdp_real` | ↓ | -12% ± 8% | rapid(1yr) | decaying (half_life: 4yr, floor: -5%) |
| `iran.regime_stability` | ↓ | to <40 | immediate | regime_dependent |
| `iran.oil_production` | ↓ | -20% ± 15% | rapid(6mo) | decaying (half_life: 3yr) |
| `iran.foreign_investment` | ↓ | -50% ± 25% | immediate | decaying (half_life: 6yr) |
| `iran.brain_drain` | ↑ | +40% ± 20% | rapid(1yr) | persistent |
| `iran.military_capability` | variable | ±20% | delayed(2yr) | regime_dependent |

### Regional Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `lebanon.hezbollah_capacity` | ↓ | -25% ± 15% | rapid(1yr) | persistent until new patron |
| `iraq.militia_coherence` | ↓ | -30% ± 20% | immediate | decaying |
| `yemen.houthi_support` | ↓ | -40% ± 25% | rapid(6mo) | persistent |
| `syria.assad_support` | ↓ | -35% ± 20% | rapid(1yr) | persistent |
| `gulf_states.threat_perception` | ↓ | -20 ± 15 | immediate | regime_dependent |
| `israel.strategic_environment` | ↑ | +15 ± 10 | delayed(1yr) | regime_dependent |
| `mena_aggregate.stability` | variable | ±15 | immediate | uncertain |

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.oil_price` | ↑ | +15% ± 10% | immediate | decaying (half_life: 1yr) |
| `global.nuclear_proliferation_risk` | ↑ | +20 ± 15 | immediate | persistent until resolved |
| `global.terrorism_risk` | variable | ±10 | delayed(1yr) | uncertain |

### Nuclear Dimension

Iran's nuclear program creates unique considerations:
- Regime crisis raises questions about nuclear material security
- Revolutionary transition could mean: abandonment of program, acceleration toward weapon, or uncertain custody
- International community would likely prioritize securing nuclear facilities
- Any successor regime inherits the technical capability

### Proxy Network Effects

Iran's regional proxy network (Hezbollah, Iraqi militias, Houthis, Hamas support) would be significantly affected:
- **Popular uprising suppressed**: Proxy support likely continues but regime distraction may reduce coordination
- **Revolutionary transition**: Proxies lose central coordination and funding; may fragment or seek new patrons
- **Failed succession**: Proxies face uncertainty during crisis; direction unclear
- **External intervention**: Proxies may be activated for retaliation before regime falls

### Durability Rationale

- **GDP**: Decaying; economy can recover under new management or sanctions relief
- **Oil production**: Decaying; infrastructure persists, sanctions relief possible
- **Brain drain**: Persistent; departed talent doesn't return quickly
- **Proxy network effects**: Persistent; rebuilding state sponsorship takes years
- **Nuclear status**: Regime-dependent; successor government makes new choices

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Proxy collapse | LEBANON_POLITICAL_CRISIS | +4%/year | 5 years | Hezbollah loses patron; Lebanese political balance shifts |
| Power vacuum | SAUDI_REGIONAL_EXPANSION | +2%/year | 10 years | Primary rival weakened |
| Nuclear uncertainty | NUCLEAR_PROLIFERATION_REGIONAL | +3%/year | 10 years | Saudi, Turkey may reconsider nuclear options |
| Oil disruption | GLOBAL_ENERGY_CRISIS | +3%/year | 2 years | Supply uncertainty |
| Refugee flows | TURKEY_MIGRATION_STRESS | +2%/year | 5 years | Iranian refugees add to existing pressures |
| Kurdish opportunity | KURDISH_INDEPENDENCE_MOVEMENT | +5%/year | 10 years | Iranian Kurdistan may seek autonomy |

### Impact Chains

**Pathway 1**: Iran regime change → Proxy network collapse → Regional power rebalancing
```
Regime crisis → Hezbollah/Houthi/militia funding disrupted →
Regional balance shifts toward Saudi/Israel →
New equilibrium or power competition
```

**Pathway 2**: Iran regime change → Nuclear uncertainty → Proliferation cascade
```
Regime crisis → Nuclear program status uncertain →
Saudi/Turkey reassess nuclear restraint →
P(regional proliferation) ↑
```

**Pathway 3**: Iran regime change → Oil supply concern → Economic disruption
```
Regime crisis → Production disruption + Hormuz risk →
Oil price spike → Global economic stress
```

**Pathway 4**: Iran regime change → Refugee flows → Regional migration stress
```
Revolutionary transition → Millions flee →
Turkey, Iraq, Gulf states receive refugees →
P(political stress) ↑ in receiving countries
```

---

## Transmission Channels

### Proxy Network Channel

**Mechanism**: Iran funds and directs regional proxy forces; regime crisis disrupts this
**Affected regions**: Lebanon (Hezbollah), Iraq (PMF militias), Yemen (Houthis), Syria (various), Palestine (Hamas/PIJ support)
**Affected variables**: `[country].militia_capacity`, `regional.power_balance`, `israel.security_environment`
**Notes**: Proxy disruption could be stabilizing (reduced conflict capacity) or destabilizing (power vacuums, uncontrolled militias)

### Oil Market Channel

**Mechanism**: Iran is significant oil producer; instability disrupts supply and threatens Hormuz transit
**Affected regions**: Global (price effects); Asia and Europe (import dependence)
**Affected variables**: `global.oil_price`, `global.inflation`, `global.energy_security`
**Differential exposure**: Oil importers vulnerable; exporters benefit from price spike
**Notes**: Hormuz transit (~20% of global oil) is key vulnerability in external intervention scenario

### Nuclear Security Channel

**Mechanism**: Regime crisis raises questions about nuclear material and technology custody
**Affected regions**: Global (nonproliferation regime); Regional (proliferation incentives)
**Affected variables**: `global.nuclear_proliferation_risk`, `regional.nuclear_status`
**Notes**: International community would likely prioritize securing facilities regardless of other policy preferences

### Refugee/Migration Channel

**Mechanism**: Instability produces refugee outflows
**Affected regions**: Turkey (primary), Iraq, Gulf states, Europe
**Affected variables**: `[country].migration_pressure`, `regional.humanitarian_burden`
**Notes**: Iran's 85M population means even small displacement percentages produce large absolute numbers

---

## Historical Analogues

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| Iran 1979 | Same country; revolutionary transition | Revolutionary ideology can motivate rapid regime change; successor regime may be more rather than less extreme |
| Soviet Union 1989-91 | Ideological exhaustion, economic stagnation | Systems that appear stable can collapse rapidly once threshold crossed |
| Syria 2011+ | Regional authoritarian facing uprising | Regimes can survive at catastrophic cost; civil war outcome possible |
| Egypt 2011 | Regional comparison | Military as key variable; Mubarak fell when military withdrew support |
| Libya 2011 | External intervention trigger | External action can catalyze collapse but successor chaos likely |
| Romania 1989 | Security service defection | Rapid collapse when coercive apparatus fragments |

---

## Early Warning Indicators

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| Khamenei health | Elderly (85+) but functioning | Any serious illness is warning |
| IRGC-clerical tensions | Contained | Open conflict or senior defection is warning |
| Protest frequency/scale | Periodic, suppressed | Sustained protests despite repression is warning |
| Security force reliability | Loyal | Any defection or refusal of orders is critical warning |
| Economic indicators | Stressed but stable | Hyperinflation, shortages are warning |
| Water crisis severity | Severe, worsening | Major city water failure is warning |
| Capital relocation progress | Under discussion | Actual relocation planning indicates crisis acceleration |
| Brain drain rate | Elevated | Acceleration indicates elite confidence collapse |
| Succession positioning | Ongoing | Visible factional conflict is warning |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-19 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Water crisis modeling; IRGC political economy; succession dynamics; nuclear program trajectory; proxy network dependencies |

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- Iran water crisis studies (aquifer depletion rates, agricultural impacts)
- IRGC economic holdings analysis
- Succession scenarios analysis
- Nuclear program status (IAEA reports)
- Proxy network funding estimates
- Demographic and public opinion data (where available)

## Open Questions

- **Water crisis timeline**: At what point does water scarcity become regime-threatening?
- **IRGC political role**: Under what conditions might IRGC prioritize institutional survival over regime defense?
- **Succession mechanics**: How contested will post-Khamenei succession be?
- **Sanctions relief path**: What would genuine rapprochement require and produce?
- **External strike effects**: Would military action rally support or catalyze collapse?
- **Proxy network autonomy**: How dependent are proxies on Iranian direction vs. self-sustaining?
- **Diaspora role**: Would Iranian diaspora support or complicate transition?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-19 | Revised severity branches; removed "managed succession crisis" | Smooth succession isn't regime crisis; replaced with "failed succession crisis" where mechanism breaks down |
| 2025-12-19 | Initial Level 1 specification | Task 2.1.9 - Type 2 regime change event |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/saudi-regime-instability]] for regional comparison | [[factors/f-mena]] for regional factor*
