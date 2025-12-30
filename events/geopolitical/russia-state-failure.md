---
title: russia-state-failure
type: note
permalink: events/geopolitical/russia-state-failure
tags:
- event
- type-2
- threshold
- geopolitical
- state-failure
- russia
- europe
- level-1
---

# Russia State Failure

**Type 2 (Threshold) Event** — Probability increases as war exhaustion, sanctions damage, succession uncertainty, and demographic decline accumulate; threshold dynamics govern transition from stressed authoritarian state to failed/fragmented state.

This specification follows the pattern established in [[events/geopolitical/pakistan-state-failure]] and [[events/geopolitical/egypt-state-failure]], adapted for Russia's distinct vulnerability profile centered on war exhaustion, regime succession, sanctions isolation, and demographic collapse.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | RUSSIA_STATE_FAILURE |
| **Scale** | National (with global consequences) |
| **Domain** | Political |
| **Causal Type** | **Type 2: Threshold** |
| **Onset Speed** | Rapid (1-3 years from trigger to acute phase) |
| **Reversibility** | Partial (some form of Russian state likely persists; territorial integrity uncertain) |

## Description

Collapse or severe fragmentation of effective Russian state authority, characterized by loss of central control over regions, military fragmentation or coup, elite faction warfare, potential territorial disintegration, and/or loss of control over nuclear arsenal. Russia's vulnerability is distinctive: extreme personalization of power in Putin, ongoing war exhaustion, unprecedented sanctions isolation, severe demographic decline, and nuclear weapons complexity.

This is a **state transition**: accumulated pressure crosses failure threshold, triggering shift from "authoritarian but functional" regime to "failed/fragmented state" regime. Observable via `internal_conflict_intensity` rising to 3-4, displacement flows activating, and GDP collapse.

**What marks occurrence**: Central government loses ability to command obedience from military/security services across territory; elite factions engage in open conflict; regions assert de facto independence; or nuclear command and control becomes uncertain.

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Russia state failure exhibits threshold dynamics:
- Multiple stressors accumulate: war costs, sanctions damage, succession uncertainty, demographic pressure, regional tensions
- System absorbs stress through repression and resource extraction until critical point
- Soviet collapse (1991) demonstrated threshold dynamics in predecessor state
- No single stochastic trigger (Type 1) or negotiated resolution (Type 3) dominates—cumulative pressure is key

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `rus.external_conflict_involvement` | 0.25 | linear | War intensity (0-4 scale); currently 3-4 for Ukraine |
| `rus.military_spending_deviation` | 0.15 | linear | Abnormal military burden signals war stress |
| `rus.sanctions_level` | 0.20 | linear | Economic isolation (0-100); currently ~75 |
| `rus.years_since_irregular_transition` | 0.10 | inverse | Time builds succession pressure; Putin era = 25+ years |
| `rus.leadership_tenure_years` | 0.10 | threshold(>20) | Hyper-personalization risk; currently 25+ years |
| `rus.gdp_growth` | 0.10 | inverse | Economic stress indicator |
| `rus.emigration_skilled_rate` | 0.10 | linear | Brain drain / elite exit signal |

**Pressure calculation**:
```
pressure = 0.25 × external_conflict_involvement / 4
         + 0.15 × military_spending_deviation / 3  # normalized to ~3 std dev max
         + 0.20 × sanctions_level / 100
         + 0.10 × (1 - years_since_irregular_transition / 50)  # caps at 50 years
         + 0.10 × (leadership_tenure_years > 20 ? 1 : 0)
         + 0.10 × max(0, -gdp_growth) / 10  # only negative growth contributes
         + 0.10 × emigration_skilled_rate / 5  # normalized to ~5% max
```
*Normalized to 0-100 scale*

**Proxy limitations**: True "war exhaustion," "elite cohesion," and "military morale" are unobservable. We proxy through measurable indicators: conflict involvement level, spending deviation, sanctions severity, and emigration rates. The key unobservable—elite factional dynamics—cannot be captured directly; probability calibration relies on reference class reasoning from Soviet collapse and comparable authoritarian stress cases.

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 75 (on 0-100 pressure scale) |
| **Uncertainty** | ±8 |
| **Sharpness (k)** | 0.25 (sharp; cascade dynamics once threshold crossed—Soviet collapse pattern) |
| **Historical calibration** | Soviet collapse 1989-91 (~pressure 80+); Russian 1998 crisis (~pressure 55, near-miss for state integrity) |

### Key Vulnerability: Power Personalization

Russia's existential vulnerability deserves emphasis:
- Extreme concentration of power in single individual (Putin)
- No clear succession mechanism; formal institutions hollowed out
- Elite cohesion depends on patronage from center; competition suppressed, not resolved
- Succession crisis could trigger elite faction warfare
- Historical pattern: Russian/Soviet transitions often violent or chaotic (1917, 1953, 1991)

A succession crisis alone could trigger state failure even if other pressures are moderate.

### Minimum Probability

**Floor**: 0.4%/year (residual risk from sudden shocks: assassination, health crisis, military coup, nuclear incident)

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.0% |
| **Low bound** | 0.5% |
| **High bound** | 1.8% |
| **Confidence** | Medium-Low |
| **25-year cumulative** | ~22% at point estimate |

### Current Pressure Estimate

Current pressure: ~55/100 (elevated but below threshold)
- `external_conflict_involvement`: 3-4 (major war in Ukraine)
- `military_spending_deviation`: ~+2 std dev (significantly elevated)
- `sanctions_level`: ~75 (comprehensive Western sanctions)
- `years_since_irregular_transition`: 32 years (since 1993 constitutional crisis)
- `leadership_tenure_years`: 25 years (Putin era)
- `gdp_growth`: ~-2% to +1% (volatile, sanctions-constrained)
- `emigration_skilled_rate`: ~2-3% (accelerated post-2022)

### Derivation

1. **Base rate for war-stressed authoritarian states**: Historical precedent is sparse; major authoritarian collapses (Soviet Union, Yugoslavia) occurred under extreme pressure
2. **Russia-specific factors**:
   - *Stabilizing*: Strong security services; nuclear deterrent prevents external regime change; resource wealth provides cushion; population politically passive
   - *Destabilizing*: Ongoing war of choice; unprecedented sanctions; demographic collapse; succession uncertainty; regional/ethnic fault lines
3. **Comparative assessment**: More resilient than late-Soviet state (no ideological collapse, stronger security apparatus) but facing sustained external pressure Soviet Union didn't face
4. **Central estimate**: 1.0%/year (range 0.5-1.8%)

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- Similar to: Saudi regime instability (~1%)
- Less likely than: Pakistan state failure (~1.5%), Egypt state failure (~1.5%)
- More likely than: China political crisis (~0.8%)

Russia's coercive apparatus is more effective than Pakistan's or Egypt's fractured systems. War exhaustion and succession risk are destabilizers, but the probability here represents *actual state failure*—not mere regime transition, which occurs without the event firing.

### Key Uncertainties

- **War trajectory**: Prolonged stalemate vs. escalation vs. negotiated end dramatically changes pressure
- **Succession timing**: Putin's health/longevity is key variable; sudden vs. managed transition
- **Sanctions durability**: Will Western sanctions persist? Will evasion networks mature?
- **Elite cohesion**: Will elites remain loyal under pressure, or factional competition emerge?
- **Military loyalty**: Will armed forces remain unified command structure?
- **Regional dynamics**: Will ethnic republics (Chechnya, Tatarstan, etc.) or resource regions (Siberia) seek autonomy?

### Case Against This Specification

**Security apparatus is exceptionally strong**: Russia's FSB/security services are among the world's most capable at suppressing dissent and detecting threats. The Wagner mutiny was contained within 24 hours. This argues for lower probability than other state failure events.

**Nuclear weapons create stability**: Both domestic actors and external powers have overwhelming incentives to prevent state failure. Any faction approaching power would need to reassure the international community on nuclear security. This "too big to fail" dynamic may make managed succession far more likely than failure.

**Historical resilience**: Russia survived the 1990s chaos, 1998 default, 2008 crisis, 2014 sanctions, and COVID without state failure. The regime has demonstrated adaptability. 1.0%/year may be too high.

**War could end**: If Ukraine conflict reaches negotiated end, the primary pressure driver diminishes substantially. Current pressure estimate assumes sustained conflict.

**Counterargument**: Soviet collapse demonstrates that apparently stable authoritarian systems can fail rapidly when pressure exceeds threshold. Wagner mutiny showed cracks exist. Hyper-personalization creates succession vulnerability that didn't exist in collective Soviet leadership. The estimate acknowledges resilience in the relatively low 1.0%/year rate.

### Probability Evolution

As a Type 2 event, probability depends on pressure trajectory:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | 0.8-1.2% | War ongoing; Putin in power; pressure elevated but contained |
| 2030-2040 | 1.0-2.0% | Succession window opens (Putin aging); war outcome uncertain |
| 2040-2050 | 0.8-1.5% | Post-succession; depends heavily on successor regime stability |
| 2050-2075 | 0.5-1.5% | Long-term demographic decline; path-dependent on earlier outcomes |

**Key inflection points**:
- Putin succession (whenever it occurs) opens high-risk window
- War termination scenarios affect pressure substantially
- Sanctions erosion vs. persistence affects economic resilience

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_GPT** | 0.75 | Great power competition is existential; Ukraine war is US/NATO proxy conflict |
| **F_EUR** | 0.50 | European regional dynamics; Ukraine, NATO expansion, energy relationship |
| **F_FIN** | 0.30 | Sanctions, SWIFT exclusion, reserve seizure, trade disruption |
| F_CLIM | 0.15 | Permafrost infrastructure degradation; Arctic access; agricultural shifts |
| F_TECH | 0.10 | Technology sanctions; semiconductor access; military modernization blocked |
| F_FOOD | 0.05 | Russia is net food exporter; minimal vulnerability |
| F_HLTH | 0.00 | No distinct pathway |
| F_MENA | 0.00 | Limited direct linkage |
| F_SAS | 0.00 | No significant pathway |
| F_EAS | 0.05 | China relationship provides economic/diplomatic buffer |
| F_SSA | 0.00 | Wagner presence but not state-stability relevant |
| F_LAM | 0.00 | No significant pathway |

**Sum of squared loadings**: 0.93 ✓

### Loading Interpretation (Type 2)

Factors shock state variables that feed into pressure function:
- High F_GPT → intensified great power competition → war escalation, sanctions tightening → `war_exhaustion`, `economic_resilience` pressure rises
- High F_EUR → European hardening → sustained Ukraine support, NATO expansion → `war_exhaustion` rises
- High F_FIN → global financial stress → sanctions enforcement, reserve currency shifts → `economic_resilience` drops
- High F_CLIM → infrastructure stress in permafrost regions → `economic_resilience` pressure
- High F_TECH → technology decoupling accelerates → military capability degradation → `military_cohesion` drops

---

## Severity Branches

Once threshold is crossed, the depth of dysfunction varies. All branches represent genuine state failure—smooth succession scenarios are not modeled here, as they occur without the event firing.

```yaml
severity_branches:

  - id: regional_fragmentation
    probability: 0.45
    description: |
      Center weakens significantly but doesn't fully collapse. Regional power 
      centers gain de facto autonomy (Chechnya, Siberian regions, Far East).
      Multiple elite factions compete openly. Formal unity nominally maintained
      but effective central control severely reduced. "Late Soviet" pattern
      before formal dissolution. Nuclear command stressed but probably intact.
      Economic dysfunction but not collapse.
      
    impact_multiplier: 1.0  # baseline for this event
    
    factor_modifications:
      F_GPT: +0.30
      F_EUR: +0.25
      F_EAS: +0.15
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.15
      
    cascade_triggers:
      # Note: CENTRAL_ASIA_INSTABILITY and CAUCASUS_CONFLICT not yet in catalog
      - event_id: OIL_SUPPLY_SHOCK
        probability_modifier: 1.5
        rationale: "Energy supply disruption"

  - id: civil_conflict
    probability: 0.35
    description: |
      Elite faction fighting escalates to armed conflict. Military units
      align with different factions. Wagner-style mutiny but successful
      or prolonged. Territorial control actively contested. Some regions
      assert independence. Nuclear command and control stressed; military
      professionals likely maintain security but uncertainty is high.
      Significant population displacement.
      
    impact_multiplier: 2.0
    
    factor_modifications:
      F_GPT: +0.50
      F_EUR: +0.40
      F_FIN: +0.30
      
    duration:
      type: decaying
      half_life_years: 12
      floor: 0.20
      
    cascade_triggers:
      # Note: NUCLEAR_SECURITY_CRISIS, UKRAINE_CONFLICT_RESOLUTION, EUROPEAN_REFUGEE_CRISIS not in catalog
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_modifier: 1.5
        rationale: "Market panic from major power instability"
      - event_id: OIL_SUPPLY_SHOCK
        probability_modifier: 2.0
        rationale: "Russian energy export disruption"

  - id: catastrophic_collapse
    probability: 0.20
    description: |
      State disintegration comparable to Soviet collapse but more chaotic.
      Multiple successor states emerge. Nuclear arsenal disposition becomes
      international crisis. Moscow loses control over Far East, Caucasus,
      possibly Siberian regions. Mass displacement. Great power intervention
      likely (nuclear security). Economic collapse. "Yugoslavia with nukes"
      worst-case scenario.
      
    impact_multiplier: 3.5
    
    factor_modifications:
      F_GPT: +0.80
      F_EUR: +0.60
      F_FIN: +0.45
      F_EAS: +0.30
      
    duration:
      type: decaying
      half_life_years: 20
      floor: 0.30
      
    cascade_triggers:
      # Note: NUCLEAR_SECURITY_CRISIS, GREAT_POWER_INTERVENTION, CHINA_FAR_EAST_ASSERTION not in catalog
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_modifier: 2.0
        rationale: "Systemic shock from major power collapse"
      - event_id: OIL_SUPPLY_SHOCK
        probability_modifier: 2.5
        rationale: "Severe energy supply disruption"
      - event_id: TAIWAN_CONFLICT
        probability_modifier: 1.3
        rationale: "Strategic distraction; US attention divided"

severity_probability_rationale: |
  Distribution reflects Russia's structural features, conditional on actual
  state failure occurring (smooth successions don't trigger this event):
  
  - Regional fragmentation (0.45): Most likely failure mode. Historical 
    pattern—late Soviet period showed gradual weakening before formal 
    collapse. Regional governors and security figures have power bases.
    Nuclear deterrent prevents external regime change, allowing prolonged
    dysfunction short of complete collapse.
    
  - Civil conflict (0.35): Wagner mutiny showed fragility exists beneath
    surface. Elite factions are suppressed but present. Military has shown
    unity so far but is degraded by war. Succession crisis without clear
    winner could trigger factional fighting.
    
  - Catastrophic collapse (0.20): Russia's security apparatus is robust,
    and nuclear weapons create strong incentives for all parties (domestic
    and international) to prevent complete collapse. However, once civil
    conflict begins, cascades can accelerate beyond control. Historical
    Russian state collapses (1917, 1991) were severe.
```

---

## Impact Vector

### Russia Impacts (Baseline: Regional Fragmentation Branch)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `rus.gdp_real` | ↓ | -20% ± 10% | rapid(2yr) | decaying (half_life: 8yr, floor: -10%) |
| `rus.gdp_growth` | ↓ | -8% ± 4% | immediate | decaying (half_life: 3yr) |
| `rus.internal_conflict_intensity` | ↑ | to 3-4 | immediate | decaying (half_life: 10yr) |
| `rus.sanctions_level` | — | complex | — | May decrease if regime changes |
| `rus.net_migration_rate` | ↓ | -2% ± 1% | rapid(2yr) | decaying (half_life: 5yr) |
| `rus.emigration_skilled_rate` | ↑ | +3% ± 1.5% | immediate | decaying (half_life: 5yr) |
| `rus.refugees_abroad` | ↑ | +2M ± 1M | rapid(3yr) | decaying (half_life: 15yr) |
| `rus.idp_population` | ↑ | +3M ± 2M | rapid(2yr) | decaying (half_life: 10yr) |

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `oil_brent` | ↑ | +30% ± 20% | immediate | decaying (half_life: 2yr) |
| `gas_europe_ttf` | ↑ | +50% ± 30% | immediate | decaying (half_life: 2yr) |
| `global_credit_spread` | ↑ | +50bps ± 30bps | immediate | decaying (half_life: 1yr) |
| `active_major_conflicts` | ↑ | +1 | immediate | event-dependent |

### Regional Impacts (Selected Countries)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `ukr.external_conflict_involvement` | ↓ | -2 levels | rapid(1yr) | persistent |
| `kaz.internal_conflict_intensity` | ↑ | +1 level | rapid(2yr) | decaying |
| `deu.gdp_growth` | ↓ | -1% ± 0.5% | rapid(1yr) | decaying (half_life: 2yr) |
| `chn.trade_share_china` | — | regional reorientation | gradual | persistent |

**Note**: Many intuitive impact channels (nuclear security indices, great power stability measures) are derived outputs, not state variables. The simulation tracks observable impacts on GDP, conflict levels, commodity prices, and displacement—interpretive assessments are computed from these.

### Nuclear Consideration

Russia possesses ~6,000 nuclear warheads—the world's largest arsenal. State failure raises unique concerns:
- **Regional fragmentation**: Nuclear command probably intact but chain of control stressed; uncertainty increases
- **Civil conflict**: Serious concerns; military professionals likely maintain security but uncertainty high
- **Catastrophic collapse**: Major international crisis; intervention likely; 1990s "loose nukes" fears but worse

Nuclear security concerns dominate international response calculus and create strong incentives for managed outcomes—which is why smooth successions (not modeled here) are the most likely response to regime stress.

### Durability Rationale

- **GDP**: Decaying; Russia has recovered from crises before (1998, 2014) but structural damage accumulates
- **Military capability**: Long-term degradation from war losses, sanctions on technology
- **Population**: Permanent emigration losses; demographic trajectory was already severe
- **Nuclear security**: Maintenance-required; depends on successor regime's capacity and intent
- **Regional stability**: Varies by region and Russia's successor arrangements

---

## Cascade Effects

### Narrative Cascade Pathways

Russia state failure would trigger significant cascade effects, but most target events are not yet specified in the catalog. Key pathways include:

**Nuclear security pathway**: State failure → command and control uncertainty → international crisis over arsenal security → potential great power intervention

**Energy market pathway**: State failure → energy production/export disruption → global price spikes → inflation surge → financial stress

**Regional destabilization pathway**: State failure → Russian security guarantees void → Central Asian and Caucasus conflicts activate → displacement cascades

**Strategic realignment pathway**: State failure → Russia becomes Chinese client/dependency → power transition acceleration → shifts in Taiwan calculus

### Specified Event Cascades

| Pathway | Target Event | Probability Change | Mechanism |
|---------|--------------|-------------------|-----------|
| Energy disruption | OIL_SUPPLY_SHOCK | +3%/year for 3 years | Russian supply uncertainty |
| Financial contagion | GLOBAL_FINANCIAL_CRISIS | +1%/year for 2 years | Market panic, commodity volatility |
| Regional instability | IRAN_REGIME_CHANGE | +0.5%/year for 5 years | Russian support withdrawn |

**Note**: Many intuitive cascade targets (Central Asian instability, Caucasus conflicts, nuclear security crisis) are not yet specified in the event catalog. These should be considered for future event development.

---

## Transmission Channels

### Nuclear Security Channel

**Mechanism**: State failure creates uncertainty about nuclear command, control, custody
**Affected regions**: Global (existential risk); Europe, US, China (direct concern)
**Affected variables**: `global.nuclear_risk`, `global.great_power_stability`
**Differential exposure**: All states vulnerable; proximity increases concern
**Notes**: This channel dominates international response; strong incentives to prevent or manage collapse

### Energy Market Channel

**Mechanism**: Russia is world's largest energy exporter; supply disruption shocks markets
**Affected regions**: Europe (most dependent), global (price effects)
**Affected variables**: `global.energy_prices`, `europe.energy_security`, `global.inflation`
**Differential exposure**: Net importers vulnerable; Europe most exposed; exporters benefit from price
**Notes**: 2022 demonstrated magnitude of Russian energy disruption effects

### Security Architecture Channel

**Mechanism**: Russia's collapse reshapes European and Eurasian security
**Affected regions**: Europe, Central Asia, Caucasus, China's periphery
**Affected variables**: `europe.security_spending`, `central_asia.stability`, `china.strategic_position`
**Differential exposure**: Former Soviet states most affected; NATO faces new questions

### Migration Channel

**Mechanism**: Political/economic collapse drives emigration
**Affected regions**: Europe (primary destination), Central Asia, China
**Affected variables**: `europe.migration_pressure`, regional labor markets
**Notes**: Russia has 144M population; educated diaspora already substantial

---

## Historical Analogues

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| Soviet collapse 1991 | Direct predecessor; threshold dynamics | Ideological collapse enabled rapid disintegration; nuclear arsenal was managed |
| Russia 1998 crisis | Economic near-collapse | State survived severe economic stress; default but not failure |
| Yugoslavia 1991+ | Multi-ethnic state dissolution | Ethnic fault lines can drive fragmentation |
| Wagner mutiny 2023 | Elite fragmentation preview | Security services can fragment; Putin's response showed both strength and vulnerability |
| Russian Civil War 1917-22 | Historical pattern | Russian state collapse historically produces prolonged chaos |

---

## Early Warning Indicators

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| War casualty trajectory | High but absorbed | Acceleration is warning |
| Elite defections/arrests | Sporadic | Clustering is danger sign |
| Ruble stability | Managed decline | Sharp drop is warning |
| Regional governor rhetoric | Compliant | Autonomy assertions are warning |
| Military unit cohesion | Post-Wagner stabilized | New mutiny indicators are warning |
| Putin health signals | Speculation but no confirmation | Visible decline is warning |
| Brain drain acceleration | Ongoing | Further acceleration is warning |
| Security service factional signals | Suppressed | Public conflicts are warning |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | War trajectory assessment; elite cohesion analysis; nuclear security deep-dive; succession scenario modeling |

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- ISW/CSIS Ukraine war assessments (war exhaustion indicators)
- Russia economic analysis (sanctions impact)
- Nuclear security literature (command and control)
- Soviet collapse historiography
- Russia demographic data (Rosstat, independent demographers)
- Elite analysis (Meduza, independent Russian outlets)

## Open Questions

- **War termination scenarios**: How do different war outcomes affect regime stability?
- **Succession mechanics**: What are actual succession pathways if Putin incapacitated?
- **Elite factional map**: Who are the key players and what are their interests?
- **Military loyalty conditions**: Under what conditions would military defect from regime?
- **Regional autonomy dynamics**: Which regions have capacity for de facto independence?
- **Nuclear security protocols**: How robust are Russian nuclear safeguards under state stress?
- **China's role**: Would China prop up Russian state, exploit weakness, or both?
- **International intervention thresholds**: What would trigger external intervention?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Critical review: replaced synthetic variables with observables; added Case Against and Probability Evolution; fixed cascade/impact references | Task 2.4 systematic review |
| 2025-12-18 | Revised severity branches; removed "managed succession" | Smooth succession isn't state failure; all branches should represent genuine dysfunction |
| 2025-12-18 | Adjusted probability to 1.0% (from 1.2%) | Reflects that event now only fires for actual failure, not regime transitions |
| 2025-12-18 | Initial Level 1 specification | Task 2.1.7 - Type 2 state failure event |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/egypt-state-failure]] for comparison | [[factors/f-gpt]] for great power factor*
