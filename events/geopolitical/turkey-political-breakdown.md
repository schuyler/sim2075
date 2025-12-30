---
title: turkey-political-breakdown
type: note
permalink: events/geopolitical/turkey-political-breakdown
tags:
- event
- type-2
- threshold
- geopolitical
- political-breakdown
- turkey
- mena
- europe
- level-1
---

# Turkey Political Breakdown

**Type 2 (Threshold) Event** — Probability increases as economic, political, and social pressures accumulate; threshold dynamics govern transition from stressed but functional state to genuine political breakdown.

This specification follows the pattern established in [[events/geopolitical/egypt-state-failure]] and [[events/geopolitical/iran-regime-change]], adapted for Turkey's distinct vulnerability profile: a middle-income democracy experiencing democratic backsliding, severe currency instability, massive refugee burden, and unresolved Kurdish conflict—but with stronger institutions and economic base than regional comparators.

**Critical framing**: This event models genuine political breakdown—not severe economic crises that the system absorbs. Turkey's 2001 crisis, 2018 currency crisis, and 2023 earthquake were severe shocks, but the political system remained intact. Those outcomes are *not* discontinuities. The event fires only when the political system itself breaks down.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | TURKEY_POLITICAL_BREAKDOWN |
| **Scale** | National (with significant regional and European consequences) |
| **Domain** | Political |
| **Causal Type** | **Type 2: Threshold** |
| **Onset Speed** | Rapid (1-3 years from trigger to acute phase) |
| **Reversibility** | Partial (democratic recovery possible but institutional damage may persist) |

## Description

Fundamental breakdown of the Turkish political system, characterized by: political system collapse (constitutional crisis, military intervention, violent succession struggle), state fragmentation (loss of control in Kurdish regions), or cascading crisis triggered by natural disaster that overwhelms governance capacity. Turkey's vulnerability is distinctive: a middle-income NATO member with significant institutional capacity experiencing democratic backsliding, chronic currency instability driven by unorthodox monetary policy, hosting the world's largest refugee population, and facing an unresolved internal conflict.

This is a **state transition**: accumulated pressure crosses crisis threshold, triggering shift from "stressed but functional democracy" to "political breakdown" state. Observable via `internal_conflict_intensity` spiking, economic indicators collapsing (inflation, currency), and `protest_intensity_annual` rising beyond suppression capacity.

**What marks occurrence**: Political system breaks down (constitutional crisis, military intervention, violent succession struggle); state loses effective control of significant territory (Kurdish regions, major urban areas); or earthquake/disaster triggers political collapse beyond recovery capacity.

**What is NOT this event**: Severe economic crises that the political system absorbs—even with IMF intervention, government change through elections, or significant economic damage—are not discontinuities. Turkey 2001, 2018, and 2023 demonstrate the system's absorption capacity. This event fires only when that capacity is exceeded and the political system itself breaks.

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
| `tur.inflation_rate` | 0.25 | threshold(50) | High inflation erodes living standards and political legitimacy |
| `tur.current_account` | 0.20 | inverse | External financing vulnerability; currency pressure |
| `tur.unemployment_rate` | 0.15 | linear | Economic stress indicator |
| `tur.protest_intensity_annual` | 0.15 | linear | Observable political dissent |
| `tur.internal_conflict_intensity` | 0.10 | linear | Kurdish conflict level |
| `tur.reserves_foreign` | 0.10 | inverse | Buffer capacity for currency defense |
| `tur.leadership_tenure_years` | 0.05 | threshold(20) | Succession risk with prolonged leadership |

**Pressure calculation**:
```
pressure = 0.25 × min(inflation_rate, 100) / 100
         + 0.20 × max(0, -current_account) / 10  # deficit contributes
         + 0.15 × unemployment_rate / 25
         + 0.15 × protest_intensity_annual / 100
         + 0.10 × internal_conflict_intensity / 4
         + 0.10 × (6 - reserves_foreign) / 6  # months of imports
         + 0.05 × (leadership_tenure_years > 20 ? 0.5 : 0)
```
*Normalized to 0-100 scale*

**Proxy limitations**: True "currency stability," "regime stability," and "social cohesion" are unobservable. We proxy through economic indicators (inflation, current account, reserves, unemployment) and conflict/protest measures. The key unobservables—elite loyalty, succession planning, military political orientation post-purges—cannot be directly captured. Probability calibration relies on reference class reasoning from middle-income democracies under stress.

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
| **Annual probability (current pressure)** | 0.55% |
| **Low bound** | 0.3% |
| **High bound** | 0.9% |
| **Confidence** | Medium |
| **25-year cumulative** | ~13% at point estimate |

### Probability Decomposition

This event uses internal probability decomposition similar to [[events/geopolitical/india-pakistan-military-conflict]]:

- **Crisis window probability**: ~1.0%/year (pressure crosses threshold producing acute instability)
- **P(breakdown | crisis)**: ~55% (probability that crisis produces genuine political breakdown vs. system absorption)
- **Annual discontinuity probability**: 1.0% × 0.55 = **0.55%**

The ~45% of crisis windows where the system absorbs the shock (2001/2018/2023 pattern) are simply years where the discontinuity doesn't occur—they don't need separate modeling.

### Current Pressure Estimate

Current pressure: ~45/100 (elevated but well below threshold)
- `inflation_rate`: ~50-60% (elevated but declining from peak)
- `current_account`: ~-4% GDP (chronic deficit but manageable)
- `unemployment_rate`: ~10% (elevated)
- `protest_intensity_annual`: ~25 (periodic but suppressed)
- `internal_conflict_intensity`: ~2 (Kurdish conflict contained but ongoing)
- `reserves_foreign`: ~4 months (limited but functional)
- `leadership_tenure_years`: 22 years (Erdoğan since 2003)

### Derivation

1. **Base rate for middle-income democracies with economic stress**: Variable; ranges from stable (Poland, Chile) to crisis-prone (Argentina, Brazil in 1990s)
2. **Turkey-specific factors**:
   - *Stabilizing*: Larger and more diversified economy than Egypt/Iran; NATO membership; functioning democratic opposition; export competitiveness; demonstrated shock absorption (2016, 2018, 2023)
   - *Destabilizing*: Chronic currency instability; unorthodox monetary policy; democratic backsliding; refugee burden; Kurdish conflict; earthquake exposure; succession uncertainty
3. **Comparative assessment**: More resilient than Egypt (stronger institutions, diversified economy); more volatile than Iran (currency instability more acute, though regime is less consolidated); Turkey has demonstrated ability to absorb severe economic shocks without political breakdown
4. **Central estimate**: 0.55%/year (range 0.3-0.9%)

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- Lower than: Egypt state failure (~1.5%), Pakistan state failure (~1.5%), Russia state failure (~1.0%), Iran regime change (~1.2%)
- Similar to: EU fragmentation (~0.4%), Chinese political crisis (~0.4%)
- Higher than: Saudi regime instability (~0.8%) only if counting crisis windows; lower if counting actual breakdown

Turkey's demonstrated shock absorption capacity (2001, 2018, 2023) justifies lower probability than other regional events. The system has been tested and survived.

### Key Uncertainties

- **Monetary policy trajectory**: Return to orthodoxy would reduce economic pressure; continued heterodoxy maintains vulnerability
- **Erdoğan succession**: Smooth transition vs. contested succession dramatically affects near-term probability
- **Earthquake timing**: Major Istanbul earthquake would stress-test all systems simultaneously
- **Refugee dynamics**: Mass return to Syria would reduce pressure; new influx would increase it
- **Kurdish conflict trajectory**: Resolution vs. escalation
- **NATO/EU relationship**: Further deterioration vs. rapprochement
- **Global financial conditions**: Strong dollar, rising rates increase Turkey's external vulnerability

### Case Against

**Turkey's shock absorption is underweighted**: The system has survived the 2001 crisis, 2016 coup attempt, 2018 currency crisis, and 2023 earthquake. This track record suggests the threshold is higher than modeled, and 0.55%/year may be too high.

**NATO membership provides external stabilization**: Unlike Egypt or Iran, Turkey has a formal security alliance with major powers who have strong incentives to prevent breakdown. This external anchor isn't fully captured in the probability.

**Economic crises don't produce political breakdown in middle-income democracies**: Argentina 2001, Greece 2010-15, and Turkey 2001 all produced severe economic damage but democratic continuity. The political_breakdown and state_fragmentation branches may be drawing too heavily on MENA analogies that don't apply to a NATO democracy.

**What would change the estimate by 2× or more**: Evidence of military political ambitions post-purges; Erdoğan health crisis with no succession mechanism; major Istanbul earthquake during economic stress; Kurdish conflict escalation to civil war intensity.

### Probability Evolution

As a Type 2 event, probability depends on pressure trajectory:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2035 | 0.4-0.7% | Erdoğan consolidation continues; currency stress manageable; earthquake risk constant |
| 2035-2050 | 0.5-1.0% | Succession window opens (Erdoğan aging); economic trajectory uncertain; climate stress rising |
| 2050-2075 | 0.4-1.2% | Depends heavily on successor regime stability and economic trajectory |

**Key inflection points**:
- Erdoğan succession (timing uncertain): Opens high-risk window regardless of mechanism
- Major Istanbul earthquake (timing unpredictable): Could accelerate pressure dramatically if occurs during other stress
- Monetary policy normalization (if achieved): Would reduce economic pressure substantially
- Kurdish political resolution (if achieved): Would remove major fragmentation pathway

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

Once threshold is crossed AND the political system breaks down (rather than absorbing the shock), the form of breakdown varies. All branches represent genuine discontinuities—the political system does not survive intact.

```yaml
severity_branches:

  - id: political_breakdown
    probability: 0.55
    description: |
      Political system breaks down beyond normal crisis management.
      Possibilities include: Erdoğan succession crisis (contested or 
      chaotic), constitutional crisis, prolonged political paralysis,
      or democratic collapse into authoritarian consolidation. State
      continues to function but political trajectory fundamentally
      altered. International isolation likely deepens. May involve
      significant political violence or repression. This is the most
      likely form of breakdown given Turkey's institutional strength.
      
    impact_multiplier: 1.0  # baseline
    
    factor_modifications:
      F_EUR: +0.40
      F_GPT: +0.30
      F_MENA: +0.25
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.15
      
    cascade_triggers:
      # Note: NATO_CRISIS, KURDISH_AUTONOMY_EXPANSION not in catalog
      - event_id: EU_FRAGMENTATION
        probability_modifier: 1.3
        rationale: "Migration surge, NATO uncertainty"
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_modifier: 1.4
        rationale: "EM contagion channel"

  - id: state_fragmentation
    probability: 0.27
    description: |
      State loses effective control over significant territory or 
      functions. Most likely pathway is Kurdish regions achieving
      de facto autonomy during central government crisis. Could also
      involve military fragmentation, regional power centers, or 
      prolonged civil conflict. Less severe than Syria-style collapse
      due to stronger institutions, but represents fundamental state
      failure. Massive refugee outflows likely.
      
    impact_multiplier: 2.5
    
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
      # Note: KURDISH_STATE_FORMATION, EUROPEAN_MIGRATION_CRISIS, NATO_ARTICLE_5_CRISIS, BOSPHORUS_TRANSIT_DISRUPTION not in catalog
      - event_id: EU_FRAGMENTATION
        probability_modifier: 1.8
        rationale: "Migration surge from 80M population"
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_modifier: 1.6
        rationale: "EM contagion, banking stress"
      - event_id: OIL_SUPPLY_SHOCK
        probability_modifier: 1.3
        rationale: "Black Sea transit disruption"

  - id: earthquake_cascade
    probability: 0.18
    description: |
      Major earthquake (likely Istanbul, M7.0+) triggers cascading
      crisis across economic, political, and social dimensions 
      simultaneously. Massive casualties (50,000-100,000+), economic
      destruction ($100B+), state capacity overwhelmed, political 
      legitimacy crisis. Unlike 2023, the state does not recover—
      political breakdown follows. International assistance mobilized 
      but recovery takes decade+. Distinct from other branches because
      natural disaster is proximate cause and damage profile is 
      different (concentrated physical destruction).
      
    impact_multiplier: 3.0
    
    factor_modifications:
      F_EUR: +0.45
      F_FIN: +0.50
      F_MENA: +0.30
      
    duration:
      type: decaying
      half_life_years: 15
      floor: 0.25
      
    cascade_triggers:
      # Note: GLOBAL_REINSURANCE_CRISIS, BOSPHORUS_TRANSIT_DISRUPTION not in catalog
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_modifier: 1.5
        rationale: "Reinsurance stress, market panic"
      - event_id: OIL_SUPPLY_SHOCK
        probability_modifier: 1.4
        rationale: "Bosphorus transit disruption"

severity_probability_rationale: |
  Distribution reflects Turkey's structural features, conditional on
  actual political breakdown occurring (not economic crises the system
  absorbs):
  
  - Political breakdown (0.55): Most likely breakdown mode. Erdoğan
    succession is genuine uncertainty—system is highly personalized.
    Constitutional crisis or authoritarian consolidation both represent
    genuine discontinuities that permanently alter Turkey's trajectory.
    This is distinct from managed government change through elections.
    
  - State fragmentation (0.27): Requires multiple failures: central
    authority collapse AND Kurdish regions seize opportunity AND 
    military cannot restore control. Lower than Egypt/Iran equivalent
    because Turkey has stronger institutional base and NATO membership
    creates external stabilization incentive. But Kurdish dimension
    creates fragmentation pathway that Egypt/Iran lack.
    
  - Earthquake cascade (0.18): Conditional on political breakdown
    occurring AND major earthquake being the trigger. The 2023 earthquake
    showed Turkey can absorb major disasters—this branch captures cases
    where the disaster is larger (Istanbul) or occurs during other
    political stress, overwhelming absorption capacity. Higher share
    than before because we've removed the non-discontinuity branch.
```

---

## Impact Vector

### Turkey Impacts (Baseline: Political Breakdown Branch)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `turkey.gdp_real` | ↓ | -20% ± 10% | rapid(1yr) | decaying (half_life: 6yr, floor: -8%) |
| `turkey.regime_stability` | ↓ | to <25 | immediate | regime_dependent |
| `turkey.currency_value` | ↓ | -60% ± 25% | immediate | decaying (half_life: 4yr) |
| `turkey.inflation_rate` | ↑ | +60% ± 30% | immediate | decaying (half_life: 3yr) |
| `turkey.fdi_inflows` | ↓ | -70% ± 20% | rapid(6mo) | decaying (half_life: 8yr) |
| `turkey.unemployment` | ↑ | +12% ± 5% | rapid(1yr) | decaying (half_life: 5yr) |
| `turkey.institutional_quality` | ↓ | -25 ± 10 | delayed(1yr) | regime_dependent |

*Scale by impact_multiplier for state_fragmentation (2.5×) and earthquake_cascade (3.0×) branches*

### Regional Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `syria.reconstruction_prospects` | ↓ | -25 ± 12 | delayed(1yr) | persistent |
| `iraq.kurdish_region_stability` | variable | ±20 | delayed(1yr) | persistent |
| `greece.security_environment` | ↓ | -15 ± 8 | immediate | regime_dependent |
| `bulgaria.economic_exposure` | ↓ | -12% ± 6% | rapid(6mo) | decaying |
| `europe.migration_pressure` | ↑ | +3M ± 1.5M | rapid(1yr) | decaying |
| `mena_aggregate.stability` | ↓ | -15 ± 7 | delayed(1yr) | decaying |

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.em_risk_premium` | ↑ | +75bp ± 35bp | immediate | decaying (half_life: 2yr) |
| `global.grain_prices` | ↑ | +8% ± 4% | immediate | decaying (half_life: 9mo) |
| `nato.cohesion` | ↓ | -15 ± 7 | delayed(6mo) | regime_dependent |

### Bosphorus/Dardanelles Consideration

Turkey controls the Turkish Straits (~3% of global oil trade, significant grain trade, Black Sea access):
- Political breakdown: Straits likely remain open but uncertainty affects shipping costs; international pressure to maintain transit
- State fragmentation: Potential disruption; international intervention possible
- Earthquake cascade: Physical damage possible; temporary disruption likely

### NATO Dimension

Turkey is NATO's second-largest military and controls the alliance's southeastern flank:
- Political breakdown: Article 5 ambiguity; democratic backsliding or authoritarian consolidation strains alliance
- State fragmentation: Unprecedented NATO crisis; no framework for member state collapse
- Earthquake cascade: NATO mobilizes humanitarian response; political implications depend on government performance

### Durability Rationale

- **GDP**: Decaying with moderate half-life; Turkey has recovery capacity but political breakdown creates lasting structural damage
- **Currency**: Decaying; can stabilize under new political equilibrium but credibility rebuilding takes years
- **FDI**: Longer decay; investor confidence requires political stability that takes time to re-establish
- **Institutional quality**: Regime-dependent; trajectory depends on successor political order
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

### Events That Are NOT Analogues (System Absorbed Shock)

| Case | Year | Outcome | Why Not Analogous |
|------|------|---------|-------------------|
| Turkey 2001 | Economic crisis | IMF program, recovery, same political system | System absorbed; Erdoğan won 2002 election normally |
| Turkey 2018 | Currency crisis | Policy adjustment, gradual stabilization | System absorbed; no political breakdown |
| Turkey 2023 | Major earthquake | State capacity stressed but held | System absorbed; Erdoğan won 2023 election |
| Argentina 2001-02 | Default, currency collapse | Economic devastation but democratic continuity | System absorbed; multiple presidents but democratic process continued |
| Greece 2010-15 | Debt crisis, bailouts | Severe austerity but democratic continuity | System absorbed; government changed through elections |

These cases inform the ~45% of crisis windows where Turkey's system absorbs the shock without political breakdown.

### Events That ARE Analogues (Actual Breakdown)

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| Turkey 2016 coup attempt | Failed breakdown attempt | Military intervention pathway exists; subsequent purges changed system |
| Yugoslavia 1990s | State fragmentation with ethnic dimension | Fragmentation along ethnic/regional lines is possible; Kurdish parallel |
| Egypt 2011-14 | Regional parallel | Military as key variable; Mubarak fell when military withdrew support |
| Iran 1979 | Regional parallel | Rapid cascade once threshold crossed; successor regime may be very different |
| Pakistan 1971 | State fragmentation | Loss of territorial control possible under sufficient stress |

These cases inform the 55% of crisis windows that produce genuine political breakdown.

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
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete |
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
| 2025-12-30 | Added Probability Evolution section; updated research status | Task 2.4 critical review completion |
| 2025-12-22 | Removed "economic_crisis_managed" branch; renamed to Political Breakdown; lowered probability to 0.55% | Critical review identified that absorbed economic crises (2001, 2018 pattern) are not discontinuities—they're the ~45% of crisis windows where the system survives intact. Event now models only genuine political breakdown. |
| 2025-12-22 | Reweighted remaining branches to 100% (55/27/18); updated impact magnitudes | Political_breakdown now baseline; state_fragmentation and earthquake_cascade retain relative weights |
| 2025-12-22 | Added Case Against section; revised Historical Analogues to distinguish absorbed vs. breakdown cases | Per critical review requirements; clarifies what is and isn't a discontinuity |
| 2025-12-19 | Initial Level 1 specification | Task 2.1.10 - Type 2 political crisis event |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/egypt-state-failure]] for regional comparison | [[events/geopolitical/iran-regime-change]] for regional comparison*