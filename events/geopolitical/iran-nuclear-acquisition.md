---
title: iran-nuclear-acquisition
type: note
permalink: events/geopolitical/iran-nuclear-acquisition
tags:
- event
- type-2
- type-3
- hybrid
- geopolitical
- nuclear
- proliferation
- iran
- mena
- level-1
---

# Iran Nuclear Acquisition

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | IRAN_NUCLEAR_ACQUISITION |
| **Scale** | Regional (with global consequences) |
| **Domain** | Political / Strategic |
| **Causal Type** | **Type 2/3 Hybrid**: Threshold (pressure accumulation) + Contingent (weaponization decision) |
| **Onset Speed** | Rapid (6-18 months from decision to confirmed capability) |
| **Reversibility** | Irreversible (knowledge cannot be undone; weapons can be dismantled but capability persists) |

## Description

Iran crosses the threshold from nuclear-capable state to confirmed nuclear weapons possessor. This represents a transition in `iran.nuclear_status` from `Threshold` to `Possessed`.

Iran is already a threshold state with substantial enrichment capability, stockpiles of enriched uranium, and the technical knowledge to construct a device. The discontinuity is the political decision to weaponize plus the time required for assembly and (likely) testing or confirmed intelligence of capability.

**What marks occurrence**: Confirmed nuclear test, credible intelligence of assembled weapon, or Iranian declaration of capability. The event is the crossing of the weaponization Rubicon, not the accumulation of technical prerequisites.

**Important distinction from IRAN_REGIME_CHANGE**: Nuclear acquisition can occur under the current Islamic Republic regime (indeed, this is the most likely pathway). Regime change could either accelerate (chaos scenario) or terminate (reformist scenario) the nuclear program. These events interact but are distinct.

---

## Causal Type Specification (Type 2/3 Hybrid)

### Why Type 2/3?

**Type 2 component (threshold dynamics):**
- Pressure accumulates from regional threats and security environment
- As pressure rises, the perceived benefits of nuclear deterrence increase relative to costs
- Historical pattern: Iran has accelerated enrichment during periods of maximum pressure
- The regime absorbs international pressure until a threshold where deterrence value exceeds isolation cost

**Type 3 component (decision point):**
- Once pressure crosses threshold, Iranian leadership faces explicit weaponization decision
- This is a small-N actor decision (Supreme Leader, IRGC, regime inner circle)
- Resolution probability (whether to weaponize given threshold crossed) has low tractability
- The mode of acquisition (covert vs. breakout vs. contested) also involves actor decisions

### Pressure Function

Per [[methodology/concepts/synthetic-variable-problem]], we use observable indicators. Iran nuclear decision is driven by security environment and regime calculus, proxied through:

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `irn.sanctions_level` | 0.30 | linear | Higher isolation reduces diplomatic alternatives; JCPOA collapse demonstrated |
| `isr.external_conflict_involvement` | 0.25 | exponential | Proxy for strike threat; accelerates as Israel engages regionally |
| `irn.protest_intensity_annual` | 0.15 | inverse | Lower protest = more stable regime with bandwidth for nuclear decision |
| `irn.years_since_irregular_transition` | 0.10 | inverse | Aging regime may seek nuclear guarantee |
| `sau.military_spending` | 0.10 | linear | Saudi military buildup increases Iranian threat perception |
| `global_credit_spread` | 0.10 | linear | Proxy for US-China distraction; higher stress = less crisis management capacity |

**Pressure calculation**:
```
pressure = 0.30 × (sanctions_level / 100)
         + 0.25 × exp(israel_conflict / 2) / exp(2)  # accelerating
         + 0.15 × (100 - protest_intensity_annual) / 100  # inverse: stability enables
         + 0.10 × (years_since_irregular_transition / 50)  # 46 years since 1979
         + 0.10 × (saudi_military / baseline_military)
         + 0.10 × (global_credit_spread / 300)
```
*Normalized to 0-100 scale*

**Proxy limitations**: True "regime security perception" and "weaponization intent" are unobservable. We proxy through sanctions (isolation), Israeli activity (threat), Saudi spending (regional competition), and domestic stability indicators. The key unobservables—Supreme Leader calculus, IRGC faction preferences—cannot be directly captured. Probability calibration relies on reference class reasoning from other proliferation cases (North Korea, Pakistan, Libya).

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 70 (on 0-100 pressure scale) |
| **Uncertainty** | ±12 |
| **Sharpness (k)** | 0.15 (moderate; decision involves deliberation, not snap judgment) |
| **Historical calibration** | Post-JCPOA collapse acceleration (~pressure 55); 2003 suspension (~pressure 40, diplomatic alternative available); current 2025 (~pressure 50) |

### Key Context: Technical Readiness

Iran's technical position means the barrier is political, not technical:
- 60%+ enriched uranium stockpile sufficient for multiple devices
- Declared 18-day breakout timeline (per IAEA)
- Weaponization knowledge from historical program
- Delivery systems (ballistic missiles) already deployed

The pressure function reflects *political incentive* to weaponize, not technical capability.

### Minimum Probability

**Floor**: 0.5%/year (residual risk from sudden decision triggered by crisis, assassination of key figure, or intelligence of imminent Israeli strike)

---

## Resolution Branches

Once pressure crosses threshold and decision to weaponize is made, the mode of acquisition varies:

```yaml
resolutions:

  - id: covert_acquisition
    probability: 0.33
    description: |
      Iran develops weapons capability secretly at undisclosed facilities.
      Eventually detected through intelligence or inadvertent disclosure.
      Fait accompli when revealed. International community faces established
      nuclear state rather than preventable program. North Korea pathway.
      
  - id: breakout_acquisition  
    probability: 0.33
    description: |
      Iran openly withdraws from NPT and races to weapon capability.
      Declared nuclear state. Maximum international isolation but also
      maximum domestic legitimacy ("standing up to pressure"). Fastest
      pathway but most visible.
      
  - id: contested_acquisition
    probability: 0.33
    description: |
      Israeli and/or US preemptive strike fails to prevent weaponization.
      Iran completes program despite military action, possibly accelerated
      by rally-around-flag effect. Acquires weapons while engaged in
      active or recent conflict. Most destabilizing pathway.

resolution_probability_rationale:
  default: "uniform (33/33/33)"
  specified: "33/33/33"
  justification: |
    No clear structural asymmetry among acquisition modes.
    
    Arguments for covert: North Korea precedent; Iran has undisclosed
    facilities history; maximizes strategic ambiguity.
    
    Arguments for breakout: Faster timeline; domestic legitimacy gains;
    NPT withdrawal is reversible until late stage.
    
    Arguments for contested: If Israel/US strikes, rally effect may
    accelerate rather than prevent; Osirak/Syria precedents show
    strikes delay but don't prevent determined programs.
    
    Defaulting to uniform per entropy maximization. Mode of acquisition
    is small-N actor decision (Iranian leadership response to circumstances)
    with low tractability.
  confidence: "n/a (using default)"
```

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 2.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~31% at point estimate |

### Current Pressure Estimate

Current pressure: ~50/100 (elevated but below threshold)
- `irn.sanctions_level`: ~80 (comprehensive Western sanctions)
- `isr.external_conflict_involvement`: ~2.5 (active regional operations)
- `irn.protest_intensity_annual`: ~40 (elevated post-2022; suppressed but present)
- `irn.years_since_irregular_transition`: 46 years (since 1979 revolution)
- `sau.military_spending`: ~6% GDP (elevated but stable)
- `global_credit_spread`: ~120 bps (normal range)

### Derivation

1. **Historical base rate**: No clear reference class. Pakistan and North Korea acquired despite pressure; Libya, South Africa, Ukraine gave up programs. Iran-specific factors dominate.

2. **Structural reasoning**:
   - *Toward acquisition*: Technical threshold already crossed; JCPOA collapse removed diplomatic alternative; regional threat environment (Israel, Saudi); North Korea demonstrates value of possession
   - *Against acquisition*: Supreme Leader fatwa (religious prohibition, though interpretable); acquisition triggers regional cascade and further isolation; current regime benefits from threshold ambiguity without possession costs

3. **Current position**: Iran benefits from threshold status—maximum leverage with reduced isolation costs. Acquisition decision requires either (a) perceived imminent threat justifying crossing Rubicon, or (b) regime instability making deterrence value paramount.

4. **Probability derivation**:
   - P(pressure crosses threshold in given year) ≈ 3%
   - P(weaponization | threshold crossed) ≈ 50% (entropy maximization; could be deterred even at high pressure)
   - Combined: ~1.5% annual probability

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- More likely than: AMOC collapse (~1.0%), Chinese Political Crisis (~0.4%)—technical prerequisites exist, political decision is limiting factor
- Similar to: Dollar Reserve Crisis (~1.5%), Egypt State Failure (~1.5%)—significant structural pressures with uncertain trigger
- Less likely than: Global Financial Crisis (~3.0%), Severe Pandemic (~2.0%)—latter have higher stochastic components

### Key Uncertainties

- **Israeli strike decision**: Would preemptive strike delay or accelerate?
- **US policy trajectory**: Maximum pressure vs. diplomatic engagement
- **Supreme Leader succession**: New leader may recalculate
- **Regional normalization**: Abraham Accords expansion reduces or increases pressure?
- **IRGC institutional interests**: Does IRGC benefit more from threshold or possession?

### Case Against This Specification

**Threshold status is optimal for Iran**: Iran currently enjoys the benefits of nuclear capability (leverage, deterrence perception) without the costs of possession (maximum isolation, regional cascade trigger). Rational actors should prefer this stable equilibrium. The 1.5%/year estimate may be too high for crossing a threshold that serves Iranian interests to preserve.

**The fatwa is more binding than outsiders assume**: Supreme Leader Khamenei has issued a fatwa declaring nuclear weapons un-Islamic. Western analysts tend to dismiss this as tactical, but religious rulings carry weight in the Islamic Republic's legitimacy structure. Crossing this line would require theological reinterpretation that may be genuinely difficult.

**International pressure has consistently delayed, not accelerated**: When pressure increases, Iran has accelerated enrichment but not weaponized. The pressure-to-weaponization link may be weaker than the pressure function assumes. Iran may absorb very high pressure while remaining at threshold.

**Regional cascade fears are overstated**: Pakistan's 1998 tests didn't trigger regional cascade despite predictions. Saudi nuclear acquisition faces enormous obstacles (technical, political, international). The cascade effects may not materialize even with Iranian acquisition.

**Counterargument**: North Korea demonstrates that threshold states do cross the Rubicon when incentives align. Iran's security environment has deteriorated since JCPOA collapse. The fatwa can be reinterpreted (defensive weapons, existential threat exception). The estimate acknowledges uncertainty in the 0.8-2.5% range.

### Probability Evolution

As a Type 2/3 hybrid, probability depends on pressure trajectory and decision windows:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | 1.5-2.0% | JCPOA dead; enrichment advancing; succession approaching |
| 2030-2040 | 1.2-2.0% | Post-succession period; depends on new leader's calculus |
| 2040-2050 | 1.0-1.8% | Path-dependent on whether acquisition occurred or regional dynamics shifted |
| 2050-2075 | 0.5-1.5% | If no acquisition by 2050, regional equilibrium may have stabilized |

**Key inflection points**:
- Supreme Leader succession (whenever it occurs): Window for policy recalculation
- Israeli strike decision: Would accelerate timeline if program survives
- Saudi nuclear pathway activation: Would increase pressure substantially
- US-Iran diplomatic breakthrough: Would decrease pressure substantially

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2/3 Hybrid target (ΛΩΛᵀ)ᵢᵢ = 0.55*

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_MENA** | 0.48 | Regional threat environment; Saudi/Israel tensions drive pressure |
| **F_GPT** | 0.37 | US-Iran confrontation; great power competition affects enforcement |
| F_EAS | 0.14 | China relationship; alternative economic/diplomatic partner |
| F_FIN | 0.10 | Sanctions effectiveness depends on global financial system |
| F_EUR | 0.07 | European role in diplomacy and sanctions |
| F_TECH | 0.03 | Marginal; technical capability already sufficient |
| F_CLIM | 0.00 | No significant pathway |
| F_HLTH | 0.00 | No significant pathway |
| F_SAS | 0.00 | Limited direct linkage |
| F_SSA | 0.00 | No significant pathway |
| F_LAM | 0.00 | No significant pathway |
| F_FOOD | 0.00 | No significant pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.55 (Type 2/3 Hybrid target); scale factor = 0.68 from original loadings

### Loading Interpretation (Type 2/3)

Factors shock state variables in pressure function:
- High F_MENA → Israeli military activity increases, Saudi buildup accelerates → `israel.external_conflict_involvement` and `saudi_arabia.military_spending` rise → pressure increases
- High F_GPT → US-Iran tension escalates, sanctions tighten → `iran.sanctions_level` rises; also US distraction increases → pressure increases
- High F_EAS → China provides more economic/diplomatic cover → may slightly reduce pressure or provide alternative pathway

---

## Aftermath Branches (by Resolution)

### Covert Acquisition Aftermath

```yaml
# Under resolution: covert_acquisition
aftermath_branches:

  - id: fait_accompli_acceptance
    probability: 0.60
    description: |
      International community accepts nuclear Iran as fait accompli.
      Containment/deterrence posture replaces prevention. Similar to
      India/Pakistan post-1998 trajectory. Maximum sanctions but no
      military response. Iran gains deterrent; regional dynamics shift
      toward accommodation.
      
    factor_modifications:
      F_MENA: +0.30
      F_GPT: +0.25
      
    duration:
      type: permanent
      
    cascade_triggers:
      - event_id: SAUDI_NUCLEAR_ACQUISITION
        probability_modifier: "+5%/year for 10 years"
        rationale: "Stated Saudi policy to match Iranian capability"
      - event_id: NPT_REGIME_EROSION
        probability_modifier: "+3%/year permanent"
        rationale: "Successful proliferation weakens nonproliferation norm"

  - id: delayed_military_response
    probability: 0.40
    description: |
      Israel and/or US conducts military strikes despite fait accompli.
      Limited effectiveness against dispersed, hardened capability.
      Escalation risk. Iran retaliates against Gulf states/Israel.
      Worst-case scenario: strikes trigger regional war without
      eliminating capability.
      
    factor_modifications:
      F_MENA: +0.70
      F_GPT: +0.50
      F_FIN: +0.25
      
    duration:
      type: decaying
      half_life_years: 5
      floor: 0.15
      
    cascade_triggers:
      - event_id: STRAIT_OF_HORMUZ_CRISIS
        probability: 0.50
        rationale: "Iran retaliates against shipping"
      - event_id: OIL_SUPPLY_SHOCK
        probability: 0.60
        rationale: "Regional conflict disrupts supply"
      - event_id: ISRAEL_IRAN_WAR
        probability: 0.70
        rationale: "Strikes escalate to broader conflict"
```

### Breakout Acquisition Aftermath

```yaml
# Under resolution: breakout_acquisition
aftermath_branches:

  - id: isolation_consolidation
    probability: 0.55
    description: |
      Iran weathers maximum pressure, consolidates nuclear deterrent.
      North Korea pathway. Comprehensive sanctions; diplomatic isolation;
      but regime survives with nuclear security guarantee. Domestic
      rally effect may temporarily stabilize regime.
      
    factor_modifications:
      F_MENA: +0.35
      F_GPT: +0.30
      
    duration:
      type: permanent
      
    cascade_triggers:
      - event_id: SAUDI_NUCLEAR_ACQUISITION
        probability_modifier: "+6%/year for 10 years"
        rationale: "Declared Iranian capability maximizes Saudi response pressure"
      - event_id: TURKEY_NUCLEAR_RECONSIDERATION
        probability_modifier: "+2%/year for 10 years"
        rationale: "NATO member may reassess given regional dynamics"

  - id: preemptive_strike_during_breakout
    probability: 0.45
    description: |
      Israel/US strikes during declared breakout attempt. Window is
      narrow (weeks to months). Success uncertain—may delay but not
      prevent. If strikes occur during breakout, likely escalation
      to regional conflict.
      
    factor_modifications:
      F_MENA: +0.75
      F_GPT: +0.55
      F_FIN: +0.30
      
    duration:
      type: decaying
      half_life_years: 6
      floor: 0.20
      
    cascade_triggers:
      - event_id: OIL_SUPPLY_SHOCK
        probability: 0.70
        rationale: "Hormuz disruption during conflict"
      - event_id: IRAN_REGIME_CHANGE
        probability_modifier: "×1.5"
        rationale: "Military conflict may destabilize regime"
```

### Contested Acquisition Aftermath

```yaml
# Under resolution: contested_acquisition
aftermath_branches:

  - id: acquisition_despite_strikes
    probability: 0.70
    description: |
      Iran completes program despite Israeli/US military action.
      Strongest rally effect. Regime legitimacy enhanced by "resisting
      aggression." Nuclear capability achieved under fire. Most
      destabilizing outcome—demonstrates strikes cannot prevent
      determined proliferators.
      
    factor_modifications:
      F_MENA: +0.80
      F_GPT: +0.60
      F_FIN: +0.35
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.25
      
    cascade_triggers:
      - event_id: SAUDI_NUCLEAR_ACQUISITION
        probability_modifier: "+8%/year for 10 years"
        rationale: "Demonstrated failure of prevention accelerates Saudi timeline"
      - event_id: NPT_REGIME_COLLAPSE
        probability_modifier: "+5%/year permanent"
        rationale: "Prevention failure + retaliation severely damages regime"
      - event_id: STRAIT_OF_HORMUZ_CRISIS
        probability: 0.80
        rationale: "Active conflict includes shipping disruption"

  - id: mutual_exhaustion
    probability: 0.30
    description: |
      Extended conflict leads to exhaustion on all sides. Iran
      possesses weapons but faces severe damage. Israel/US have
      expended military options without prevention. Unstable
      deterrence emerges from mutual exhaustion rather than
      deliberate architecture.
      
    factor_modifications:
      F_MENA: +0.50
      F_GPT: +0.40
      F_FIN: +0.25
      
    duration:
      type: decaying
      half_life_years: 10
      floor: 0.15

aftermath_probability_rationale: |
  Contested acquisition branch probabilities reflect that if strikes
  fail to prevent (which is the definition of this resolution), Iran
  is highly likely to complete the program. The 70/30 split reflects
  whether the outcome is decisive Iranian success vs. mutual exhaustion.
  
  Historical precedent: Osirak (1981) delayed but didn't prevent Iraqi
  program; Syrian reactor strike (2007) was more successful but Syria
  was earlier in development. Iran's dispersed, hardened infrastructure
  and technical readiness make prevention harder.
```

---

## Impact Vector

### Iran Impacts (All Resolutions)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `iran.nuclear_status` | → Possessed | Categorical transition | immediate | permanent |
| `iran.sanctions_level` | ↑ | +15 ± 10 | immediate | maintenance_required (depends on int'l consensus) |
| `iran.regime_stability` | ↑ | +10 ± 8 | rapid(1yr) | decaying (half_life: 5yr); rally effect fades |
| `iran.alliance_west` | ↓ | -20 ± 10 | immediate | persistent |
| `iran.alliance_china` | ↑ | +10 ± 8 | rapid(1yr) | maintenance_required |

### Regional Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `saudi_arabia.military_spending` | ↑ | +2% GDP ± 1% | rapid(2yr) | persistent |
| `israel.external_conflict_involvement` | ↑ | +0.5 ± 0.3 | immediate | decaying (half_life: 3yr) |
| `global.us_china_tension` | ↑ | +8 ± 5 | immediate | decaying (half_life: 2yr) |
| Gulf States aggregate: `regime_stability` | ↓ | -5 ± 3 | rapid(1yr) | decaying |

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.nuclear_stability` | ↓ | -15 ± 8 | immediate | permanent (until new equilibrium) |
| `global.oil_brent` | ↑ | +20% ± 15% | immediate | decaying (half_life: 1yr) |
| `global.us_china_tension` | ↑ | +8 ± 5 | immediate | decaying (half_life: 2yr) |

### Durability Specifications

| Durability Type | Parameters | Used For |
|-----------------|------------|----------|
| **permanent** | N/A | `nuclear_status` change; knowledge/capability |
| **decaying** | half_life: varies, floor: 0.1-0.2 | Oil price spike; rally effect; tension spikes |
| **maintenance_required** | annual_failure_prob: 5-10% | Sanctions consensus; isolation |

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Proliferation precedent | SAUDI_NUCLEAR_ACQUISITION | +5-8%/year | 10 years | Stated Saudi policy; Pakistan assistance pathway |
| NPT erosion | TURKEY_NUCLEAR_RECONSIDERATION | +2%/year | 10 years | NATO member reassesses; regional dynamics |
| Regional tension | ISRAEL_IRAN_WAR | +3%/year | 5 years | Israel may strike even after acquisition |
| Oil risk premium | OIL_SUPPLY_SHOCK | +2%/year | 3 years | Hormuz vulnerability; regional instability |
| Regime legitimacy | IRAN_REGIME_CHANGE | -1%/year | 5 years | Rally effect; nuclear security guarantee |

### Impact Chains

**Pathway 1**: Iran nuclear → Saudi response → Regional arms race
```
Iran acquires nuclear weapons →
Saudi Arabia accelerates nuclear program (Pakistan pathway) →
Turkey reconsiders nuclear status →
Regional nuclear arms race; NPT regime collapses
```

**Pathway 2**: Iran nuclear → Israeli response → Regional war
```
Iran acquires nuclear weapons →
Israel conducts strikes (prevention or punishment) →
Iran retaliates (Hormuz, Gulf states, direct strikes) →
Regional war; oil supply disruption
```

**Pathway 3**: Iran nuclear → Deterrence stability
```
Iran acquires nuclear weapons →
Regional powers adjust to nuclear-armed Iran →
Unstable but functioning deterrence emerges →
Reduced conventional conflict risk (nuclear shadow)
```

---

## Transmission Channels

### Proliferation Cascade Channel

**Mechanism**: Iranian acquisition demonstrates successful proliferation pathway; reduces perceived costs for other aspirants; triggers stated Saudi policy
**Affected regions**: Gulf, Turkey, Egypt (potential), East Asia (precedent effects)
**Affected variables**: `[country].nuclear_status`, `global.nuclear_stability`
**Notes**: Saudi Arabia has explicitly stated it would match Iranian capability. Pakistan has provided nuclear assistance historically.

### Oil Market Channel

**Mechanism**: Nuclear crisis raises Hormuz closure risk; general regional instability premium
**Affected regions**: Global (price effects); Asia and Europe (import dependence)
**Affected variables**: `global.oil_brent`, `global.container_freight_index`, importer inflation
**Notes**: Even without Hormuz closure, risk premium affects prices

### Regional Security Channel

**Mechanism**: Nuclear Iran changes regional power balance; affects alliance calculations
**Affected regions**: Gulf states, Israel, Turkey
**Affected variables**: `[country].alliance_west`, `[country].military_spending`, `[country].external_conflict_involvement`
**Notes**: Gulf states may seek closer US alignment or accommodation with Iran

---

## Interaction with IRAN_REGIME_CHANGE

These events have complex bidirectional effects:

### If IRAN_NUCLEAR_ACQUISITION occurs first:
- Regime gains nuclear security guarantee → P(IRAN_REGIME_CHANGE) decreases modestly (-1%/year for 5 years)
- But increased isolation may accelerate economic pressure → effect uncertain
- Net effect: slight stabilization of regime

### If IRAN_REGIME_CHANGE occurs first:
- **Revolutionary transition**: Depends on successor regime
  - Reformist successor: May abandon program (Libya pathway) → P(acquisition) drops substantially
  - Chaotic transition: May accelerate program (secure deterrent amid instability) → P(acquisition) increases
  - Military takeover: Likely continues program → P(acquisition) unchanged
- **Failed succession crisis**: Uncertain control of program → P(acquisition) may increase (use it or lose it dynamics)
- Net effect: Uncertain; model as conditional probability adjustment

---

## Historical Analogues

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| North Korea 2006 | Threshold → acquisition under maximum pressure | Determined state can acquire despite sanctions; fait accompli acceptance likely |
| Pakistan 1998 | Regional rival nuclear acquisition | Tests followed by sanctions, then normalization; proliferation cascade didn't materialize fully |
| India 1974/1998 | Declared nuclear status | International adjustment to new nuclear state; regional stability concerns |
| Iraq 1981-2003 | Failed prevention through strikes and sanctions | Osirak delayed but didn't prevent; regime change ultimately ended program |
| Libya 2003 | Abandonment under pressure | Diplomatic alternative can work—but required regime security guarantee |
| South Africa 1990s | Voluntary denuclearization | Regime transition led to abandonment; unusual case |

---

## Early Warning Indicators

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| Enrichment level | 60%+ (weapons-grade is 90%+) | Already elevated |
| IAEA access | Limited; disputes ongoing | Denial of access is warning |
| Fordow activity | Active | Expansion/hardening is warning |
| Declared stockpile | Sufficient for multiple devices | Already sufficient |
| NPT status | Member (with disputes) | Withdrawal announcement is critical warning |
| Regional tension | Elevated | Israeli strike preparation is warning |
| Diplomatic track | Stalled | Abandonment of diplomacy is warning |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | IAEA technical assessments; Israeli strike capability analysis; Saudi nuclear pathway investigation; Pakistan assistance history |

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- IAEA Iran reports (enrichment levels, stockpiles, access disputes)
- Iranian nuclear program technical assessments
- Saudi statements on nuclear matching
- Israeli military capability assessments
- NPT regime analysis
- Historical proliferation cases (North Korea, Pakistan, India, Iraq, Libya)

## Open Questions

- **Strike effectiveness**: Can Israeli/US strikes actually prevent acquisition given dispersal and hardening?
- **Saudi pathway**: How quickly could Saudi Arabia acquire weapons with Pakistani assistance?
- **Chinese role**: Would China provide diplomatic cover or actively facilitate?
- **Fatwa interpretation**: Is Supreme Leader fatwa against nuclear weapons a binding constraint or interpretable?
- **Deterrence stability**: Would nuclear Iran be more or less aggressive regionally?
- **Successor regime**: What would different post-regime-change governments do with program?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Critical review: replaced synthetic variables (regime_stability, us_china_tension) with observables; added Case Against and Probability Evolution sections | Task 2.4 systematic review |
| 2025-12-25 | Initial Level 1 specification | Task 2.1.20 |

---

*See [[methodology/reference/type-3-calibration]] for Type 2/3 hybrid methodology | [[events/geopolitical/iran-regime-change]] for related event | [[factors/f-mena]] for regional factor*