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

## Specification

```yaml
id: IRAN_REGIME_CHANGE
domain: political
scale: national
causal_type: 2
onset: sudden
reversibility: partial
```

*Scale: national, with major regional and global consequences. Onset speed: rapid (1-3 years from trigger to resolution). Reversibility: partial (regime may reconstitute in different form; full revolutionary transition possible but uncertain).*

## Description

Fundamental destabilization of the Islamic Republic regime, characterized by loss of coercive control, elite fragmentation (particularly IRGC-clerical split), mass popular uprising beyond suppression capacity, or systemic breakdown of governance. Iran's vulnerability is distinctive: an aging revolutionary ideology facing a young, increasingly secular population; severe economic isolation from Western sanctions; and an accelerating water crisis that threatens the habitability of the central plateau including Tehran.

This is a **state transition**: accumulated pressure crosses crisis threshold, triggering shift from "stable theocratic state" to "regime crisis" state. Observable via `protest_intensity_annual` spiking beyond suppression capacity, `internal_conflict_intensity` rising, and economic indicators collapsing.

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
| `irn.sanctions_level` | 0.25 | linear | Economic isolation; currently ~80 |
| `irn.gdp_growth` | 0.20 | inverse | Economic performance under sanctions |
| `irn.unemployment_rate` | 0.15 | linear | Youth unemployment particularly high |
| `irn.water_stress` | 0.15 | exponential | Aquifer depletion, desertification; existential threat |
| `irn.protest_intensity_annual` | 0.10 | linear | Observable dissent (2022 protests elevated this) |
| `irn.years_since_irregular_transition` | 0.10 | complex | 1979 was last transition; 46 years of regime stability |
| `irn.inflation_rate` | 0.05 | linear | Currency crisis, purchasing power erosion |

**Pressure calculation** (as originally specified):
```
pressure = 0.25 × sanctions_level / 100
         + 0.20 × max(0, -gdp_growth) / 10  # negative growth contributes
         + 0.15 × unemployment_rate / 30
         + 0.15 × exp(water_stress / 50) / exp(2)  # accelerating
         + 0.10 × protest_intensity_annual / 100
         + 0.10 × (years_since_irregular_transition > 40 ? 0.3 : 0)  # aging revolution
         + 0.05 × min(inflation_rate, 50) / 50  # capped contribution
```
*Normalized to 0-100 scale*

The YAML expression below realizes these transforms in the expression language's subset: the inverse growth term as `max(0, -gdp_growth) / 10` (only contraction contributes), the exponential water term as `exp(water_stress / 50) / exp(2)` (saturating at 1.0 when `water_stress` = 100), the "complex" aging-revolution step as `where(years_since_irregular_transition > 40, 0.3, 0)` in place of the original ternary, the capped inflation term as `min(inflation_rate, 50) / 50`, and the whole weighted sum wrapped in `100 * (...)` to put it on `threshold`'s 0-100 scale.

**Proxy limitations**: True "regime legitimacy," "elite cohesion," and "social contract stress" are unobservable. We proxy through economic indicators (sanctions, GDP, unemployment, inflation), water stress (measurable), and protest intensity. The key unobservables—IRGC-clerical faction dynamics, succession positioning—cannot be directly captured. Probability calibration relies on reference class reasoning from comparable ideological authoritarian regimes.

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

```yaml
probability:
  pressure: |
    100 * (
      0.25 * (irn.sanctions_level / 100) +
      0.20 * (max(0, -irn.gdp_growth) / 10) +
      0.15 * (irn.unemployment_rate / 30) +
      0.15 * (exp(irn.water_stress / 50) / exp(2)) +
      0.10 * (irn.protest_intensity_annual / 100) +
      0.10 * where(irn.years_since_irregular_transition > 40, 0.3, 0) +
      0.05 * (min(irn.inflation_rate, 50) / 50)
    )
  threshold: 65
  threshold_std: 10
  sharpness: 0.20
  floor: 0.004
  annual: 0.012
  range: [0.008, 0.018]
  confidence: medium
```

No impact row uses `until: resolved`, so the probability block carries no `resolves_after`; every impact decays on its own half-life.

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.2% |
| **Low bound** | 0.8% |
| **High bound** | 1.8% |
| **Confidence** | Medium |
| **25-year cumulative** | ~26% at point estimate |

### Current Pressure Estimate

Current pressure: ~50/100 (elevated but below threshold)
- `sanctions_level`: ~80 (comprehensive Western sanctions)
- `gdp_growth`: ~-2% to +2% (volatile under sanctions)
- `unemployment_rate`: ~12% official, likely higher for youth
- `water_stress`: ~70 (severe and worsening; capital relocation discussed)
- `protest_intensity_annual`: ~40 (elevated post-2022; suppressed but persistent)
- `years_since_irregular_transition`: 46 years (1979 revolution)
- `inflation_rate`: ~40% (severe currency depreciation)

At these values the YAML expression gives 45.2 with `gdp_growth` at 0 and 49.2 at −2%, consistent with the "~50/100" estimate. The compiler's pressure-scale check at 2025 baselines is skipped for this event because every term reads an `irn.*` country variable, which has no recorded baseline in the state catalog.

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

### Case Against This Specification

**The regime has survived worse**: The Islamic Republic survived eight years of war with Iraq (1980-88) with hundreds of thousands of casualties, the 2009 Green Movement, 2019 fuel protests with 1,500+ deaths, and 2022 Mahsa Amini protests. Each time, forecasters predicted collapse and were wrong. 1.2%/year may significantly overstate probability given demonstrated resilience.

**Coercive capacity is exceptional**: Iran's security apparatus is among the world's most effective at suppressing dissent. The IRGC has deep economic interests in regime survival. Unlike Egypt 2011 or Romania 1989, there's no evidence of security force wavering. The 2022 protests, despite unprecedented scale, were eventually suppressed without elite defection.

**No organized opposition**: Iranian opposition is fragmented (reformists, monarchists, ethnic movements, MEK) with no unified leadership or credible alternative. Even if protests succeed, what replaces the regime is deeply uncertain—which may make elites less willing to defect.

**Water crisis timeline is longer than implied**: While Iran's water crisis is severe, major cities can be supplied through infrastructure investment and imports for decades. Tehran relocation discussion may reflect long-term planning rather than imminent crisis. Environmental pressure adds to baseline stress but isn't an acute trigger.

**External intervention is unlikely to cause collapse**: Historical evidence (Iraq 2003, Libya 2011) suggests external intervention produces chaos rather than stable transition. More importantly, a strike on nuclear facilities might trigger rally-around-flag rather than collapse—rallying moderates to the regime. The 10% probability for this branch may overstate how reliably intervention produces regime change.

**Counterargument**: The counterarguments are valid but don't eliminate risk. Soviet collapse demonstrated that ideological regimes can appear stable until they suddenly aren't. Generational change is real—today's protesters have no memory of revolutionary legitimacy. The water crisis is genuinely unprecedented. And the specification acknowledges regime survival as the most likely crisis outcome (40% suppressed uprising branch). The estimate reflects genuine uncertainty, not confident prediction of collapse.

### Probability Evolution

As a Type 2 event, probability depends on pressure trajectory:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | 1.0-1.5% | Khamenei succession window; sanctions maintained; water crisis worsening |
| 2030-2040 | 1.0-1.8% | Post-succession period (if transition occurs); water crisis acute in many regions |
| 2040-2050 | 0.8-2.0% | Depends heavily on successor regime legitimacy; water crisis potentially critical |
| 2050-2075 | 0.5-2.5% | Wide range; climate impacts accelerate; long-term institutional trajectory uncertain |

**Key inflection points**:
- Khamenei succession (timing uncertain but within decade): High-risk window regardless of outcome
- Major water infrastructure failure (city-level water crisis): Would accelerate pressure dramatically
- Sanctions trajectory: Relief could reduce pressure substantially; escalation increases it
- Regional developments: Major proxy network success/failure affects regime legitimacy

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

```yaml
factors:
  F_MENA: 0.43  # Core MENA power; instability would transform regional dynamics
  F_GPT: 0.30   # US sanctions regime, great power competition, nuclear negotiations
  F_CLIM: 0.23  # Water crisis is existential; affects agricultural base and habitability
  F_FIN: 0.20   # Oil prices, sanctions effects, global finance exclusion
  F_EAS: 0.10   # China relationship; alternative economic partner
  F_TECH: 0.07  # Information control challenges; nuclear program trajectory
  F_FOOD: 0.07  # Agricultural stress from water; food import dependence
  F_EUR: 0.07   # European policy on sanctions, nuclear deal
  F_SAS: 0.03   # Limited direct linkage; some Afghanistan spillover
variance: 0.65  # Type 2 target
```

F_HLTH carries no loading (no distinct pathway); F_SSA and F_LAM carry no loading (no significant pathway).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.66 from original loadings. The original (pre-scaling, Level 1) loadings were F_MENA 0.65, F_GPT 0.45, F_CLIM 0.35, F_FIN 0.30, F_EAS 0.15, F_TECH 0.10, F_FOOD 0.10, F_EUR 0.10, F_SAS 0.05, with a sum of squared loadings of 0.88 — the pre-variance-allocation check the specification originally recorded.

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
branches:
  - {id: popular_uprising_suppressed,  p: 0.40, desc: "Mass protests beyond 2022 scale; suppressed at great cost; regime survives but durably weakened"}
  - {id: revolutionary_transition,     p: 0.35, desc: "Security forces fragment; regime falls; successor deeply uncertain"}
  - {id: failed_succession_crisis,     p: 0.15, desc: "Supreme Leader succession mechanism breaks down; open elite conflict"}
  - {id: external_intervention_trigger, p: 0.10, desc: "US/Israeli strike catalyzes broader collapse; regional war risk"}
```

### Branch 1: Popular Uprising Suppressed (40%)

Mass protests exceed 2022 scale—potentially triggered by economic collapse, environmental disaster, or political catalyst. Regime deploys maximum force; significant casualties (thousands). Uprising eventually suppressed but regime fundamentally weakened. Significant international isolation. Brain drain accelerates. Economy further damaged. Regime survives but severely delegitimized and weakened; future instability more likely. This is a genuine discontinuity because the regime's coercive legitimacy and capacity are permanently degraded.

**Impact multiplier**: 1.0× (baseline).

### Branch 2: Revolutionary Transition (35%)

Regime actually falls—security forces fragment or refuse orders, elite defections cascade, protests cannot be suppressed. What emerges is deeply uncertain: secular democratic government, reformed Islamic system, military transitional authority, regional fragmentation, or civil conflict. Nuclear facilities become major international concern. Proxy networks lose central direction. Regional power vacuum.

**Impact multiplier**: 3.0× baseline.

### Branch 3: Failed Succession Crisis (15%)

Supreme Leader death or incapacitation triggers succession process that fails to resolve. IRGC and clerical factions cannot agree on successor or power-sharing arrangement. Open elite conflict emerges. This is distinct from managed succession (which doesn't trigger this event)—here the succession mechanism breaks down, producing prolonged institutional paralysis, factional violence, or civil conflict. System may eventually reconstitute but only after significant instability and permanent damage to institutional legitimacy.

**Impact multiplier**: 2.0× baseline.

### Branch 4: External Intervention Trigger (10%)

US or Israeli military strike on nuclear facilities or leadership targets triggers regime destabilization. Initial strike may produce rally-around-flag effect, but if combined with existing pressures, could catalyze broader collapse. Distinct from other branches because external action is proximate cause. High escalation risk—Iran may retaliate against Gulf states, Israel; regional war possible.

**Impact multiplier**: 4.0× baseline.

### Branch Factor Modifications and Durations

The original specification attached per-branch factor modifications (post-firing shifts to the factor draws) and a branch-level duration profile to each severity branch. Neither construct exists in the v0.1 schema (factor modifications are not compiled; branch-level decay-to-floor is schema v0.2 backlog), so both are kept here as the documented intent.

| Branch | Factor modifications | Duration (original form) |
|--------|---------------------|--------------------------|
| Popular uprising suppressed | F_MENA +0.25, F_GPT +0.20 | decaying, half-life 4 years, floor 0.10 |
| Revolutionary transition | F_MENA +0.65, F_GPT +0.55, F_FIN +0.35, F_HLTH +0.10 (potential for violence, humanitarian crisis) | decaying, half-life 12 years, floor 0.20 |
| Failed succession crisis | F_MENA +0.40, F_GPT +0.30, F_FIN +0.25 | decaying, half-life 8 years, floor 0.15 |
| External intervention trigger | F_MENA +0.80, F_GPT +0.70, F_FIN +0.50, F_FOOD +0.20 (oil disruption affects food prices) | decaying, half-life 10 years, floor 0.25 |

### Severity Probability Rationale

Distribution reflects Iran's structural features, conditional on actual regime crisis occurring. Smooth successions where the Islamic Republic continues with a new Supreme Leader don't trigger this event.

- **Popular uprising suppressed (0.40)**: Most likely crisis mode. 2009 and 2022 showed regime can suppress major protests, but a crisis-level uprising would be larger and suppression more costly. Regime survives but permanently weakened—this is a discontinuity because coercive capacity and legitimacy are durably degraded, unlike normal protest cycles.
- **Revolutionary transition (0.35)**: Requires multiple failures: elite fragmentation AND security force defection AND mass mobilization. 1979 shows it can happen in Iran specifically. Higher probability than in Russia because ideological exhaustion is more advanced and population is more mobilized.
- **Failed succession crisis (0.15)**: Khamenei is 85+; succession will eventually occur. Most successions will be managed (not triggering this event). This branch captures scenarios where the succession mechanism fails—factional deadlock, open conflict, institutional breakdown. Lower probability because IRGC has strong interest in managed transition.
- **External intervention trigger (0.10)**: Requires deliberate US/Israeli decision to strike AND that strike catalyzes regime collapse rather than rally-around-flag. Both conditions are uncertain. However, the consequences of this pathway are severe enough to warrant distinct modeling.

---

## Impact Vector

The YAML `impacts:` block takes the popular-uprising-suppressed branch as its explicit baseline list and scales the others from it with the branch multipliers above (`revolutionary_transition` 3.0, `failed_succession_crisis` 2.0, `external_intervention_trigger` 4.0). The multipliers apply uniformly to every row, so bounded-scale variables (`internal_conflict_intensity`, 0-4) overshoot their range in the heavier branches exactly as the original multiplier table implied.

```yaml
impacts:
  popular_uprising_suppressed:
    # Iran
    - {var: irn.gdp_real,                    mag: [-0.12, 0.08], onset: {gradual: 1}, decay: 4}
    - {var: irn.gdp_growth,                  mag: [-8, 4],       onset: immediate,    decay: 2}
    - {var: irn.internal_conflict_intensity, mag: [2.5, 0.5],    onset: immediate,    decay: 5}
    - {var: irn.protest_intensity_annual,    mag: [40, 20],      onset: immediate,    decay: 3}
    - {var: irn.fdi_net,                     mag: [-2, 1],       onset: immediate,    decay: 6}
    - {var: irn.emigration_skilled_rate,     mag: [3, 1.5],      onset: {gradual: 1}, decay: 5}
    - {var: irn.refugees_abroad,             mag: [1, 0.5],      onset: {gradual: 2}, decay: 10}

    # Global
    - {var: oil_brent,                       mag: [15, 9],       onset: immediate,    decay: 1}
    - {var: global_credit_spread,            mag: [25, 15],      onset: immediate,    decay: 1}

    # Regional
    - {var: levant_iraq.gdp_growth,                  mag: [-0.25, 0.15], onset: {gradual: 1}, decay: 10}
    - {var: levant_iraq.internal_conflict_intensity, mag: [0.6, 0.3],    onset: {gradual: 1}, decay: 5}
    - {var: tur.refugees_hosted,             mag: [0.5, 0.3],    onset: {gradual: 2}, decay: 10}

  revolutionary_transition:
    inherit: popular_uprising_suppressed
    scale: 3.0

  failed_succession_crisis:
    inherit: popular_uprising_suppressed
    scale: 2.0

  external_intervention_trigger:
    inherit: popular_uprising_suppressed
    scale: 4.0
```

*Units: `gdp_real` rows are fractions of the entity's current value (−12% ± 8% for the baseline branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields) — percentage points for `gdp_growth`, `fdi_net` (% of GDP) and `emigration_skilled_rate`, levels on the 0-4 scale for `internal_conflict_intensity`, index points for `protest_intensity_annual`, millions for refugee stocks, $/bbl for `oil_brent`, bps for `global_credit_spread`.*

### Iran Impacts (Baseline: Popular Uprising Suppressed Branch) — original specification

The YAML rows above carry the original magnitudes with three re-expressions: `irn.gdp_real` was specified as −12% ± 8%, rapid (1yr) onset, *decaying (half_life: 4yr, floor: −5%)* — decay-to-floor durability is schema v0.2 backlog, so the YAML uses a plain 4-year half-life and the −5% floor is recorded here; `irn.internal_conflict_intensity` was specified as "+2-3 levels", written as 2.5 ± 0.5; and the two "rapid (1yr)" / "rapid (2yr)" onsets became `{gradual: 1}` / `{gradual: 2}`. The remaining Iran rows (`gdp_growth` −8% ± 4%, half-life 2yr; `protest_intensity_annual` +40 ± 20, half-life 3yr; `fdi_net` −2% GDP ± 1%, half-life 6yr; `emigration_skilled_rate` +3% ± 1.5%, half-life 5yr; `refugees_abroad` +1M ± 0.5M, half-life 10yr) convert one-to-one.

### Global Impacts — original specification

`oil_brent` was specified as **+20% ± 12%** (immediate, half-life 1yr); against the catalog's 2025 baseline of $75/bbl this is +$15 ± $9, which is what the YAML carries. `global_credit_spread` +25bps ± 15bps (immediate, half-life 1yr) converts one-to-one.

### Regional Impacts (Selected Countries) — original specification

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability | Disposition at migration |
|----------|-----------|------------------------|-------|------------|--------------------------|
| `lbn.gdp_growth` | ↓ | -3% ± 2% | rapid(1yr) | persistent (Hezbollah funding cut) | Lebanon is not a state-catalog entity; it is a member of the `levant_iraq` Tier 1 aggregate. Re-expressed as `levant_iraq.gdp_growth` −0.25 ± 0.15 pp (Lebanon is ~8% of the aggregate's $300B GDP). "Persistent" (decay-to-floor class) is schema v0.2 backlog; written as a 10-year half-life |
| `irq.internal_conflict_intensity` | ↑ | +1 level | rapid(1yr) | decaying (militia fragmentation) | Iraq is not a state-catalog entity; it is ~60% of `levant_iraq` by population. Re-expressed as `levant_iraq.internal_conflict_intensity` +0.6 ± 0.3; the unspecified half-life is written as 5 years, matching the Iran conflict-intensity row |
| `yem.internal_conflict_intensity` | variable | ±1 level | rapid(6mo) | uncertain (Houthi support cut) | **Dropped**: Yemen is not one of the 40 countries and belongs to no Tier 1 or Tier 2 aggregate ([[methodology/reference/state-entities]]); the channel stays in the Proxy Network Effects prose below |
| `tur.refugees_hosted` | ↑ | +0.5M ± 0.3M | rapid(2yr) | decaying (half_life: 10yr) | Converts one-to-one |

**Note**: Many intuitive impact channels (proxy network capacity, regional influence indices, nuclear proliferation risk) are derived outputs, not state variables. The simulation tracks observable impacts on GDP, conflict levels, commodity prices, and migration flows.

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

- **GDP**: Decaying; economy can recover under new management or sanctions relief. The original specification carried a −5% floor on the GDP recovery; decay-to-floor durability is schema v0.2 backlog, so the YAML uses a plain 4-year half-life.
- **Oil production**: Decaying; infrastructure persists, sanctions relief possible
- **Brain drain**: Persistent; departed talent doesn't return quickly
- **Proxy network effects**: Persistent; rebuilding state sponsorship takes years (the Lebanon growth row's "persistent" form is written as a 10-year half-life for the same backlog reason)
- **Nuclear status**: Regime-dependent; successor government makes new choices

---

## Cascade Effects

### Narrative Cascade Pathways

Iran regime change would trigger significant cascade effects. Key pathways include:

**Proxy network pathway**: Regime crisis → Hezbollah/Houthi/militia funding disrupted → regional balance shifts → new equilibrium or power competition

**Nuclear uncertainty pathway**: Regime crisis → nuclear program status uncertain → regional proliferation incentives shift → Saudi/Turkey may reassess nuclear restraint

**Oil supply pathway**: Regime crisis → production disruption + Hormuz risk → oil price spike → global economic stress

**Refugee pathway**: Revolutionary transition → millions flee → Turkey, Iraq, Gulf states receive refugees → regional migration stress

### Specified Event Cascades

```yaml
cascades:
  triggers:
    - {event: OIL_SUPPLY_SHOCK,          delta: 0.050,  years: 3}
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.015,  years: 2}
    - {event: SAUDI_REGIME_INSTABILITY,  delta: -0.003, years: 5}
    - {event: SAUDI_NUCLEAR_ACQUISITION, delta: 0.010,  years: 10}
  triggered_by: []  # none specified; the external-strike pathway is modeled as the external_intervention_trigger branch
```

| Pathway | Target Event | Probability Change | Mechanism |
|---------|--------------|-------------------|-----------|
| Oil disruption | OIL_SUPPLY_SHOCK | +5%/year for 3 years | Iranian production disruption; Hormuz risk |
| Financial contagion | GLOBAL_FINANCIAL_CRISIS | +1.5%/year for 2 years | Oil shock, regional instability |
| Regional shift | SAUDI_REGIME_INSTABILITY | -0.3%/year for 5 years | External threat consolidates Gulf regimes |
| Nuclear cascade | SAUDI_NUCLEAR_ACQUISITION | +1%/year for 10 years | Primary restraint removed |
| Nuclear acceleration | IRAN_NUCLEAR_ACQUISITION | uncertain | Could accelerate or collapse with regime |

The IRAN_NUCLEAR_ACQUISITION edge has no specified magnitude or sign ("uncertain"), so it is not written into `triggers:`; it stays here as a documented pathway.

### Branch-Conditional Cascade Modifiers (original specification)

The original severity-branch block expressed cascades as per-branch *multipliers* on the target's annual probability rather than the absolute deltas the schema compiles. The flat deltas above are the specified cascade table; the branch modifiers are kept here as the documented intent for a conditional (`if: branch == ...`) refinement.

| Branch | Target | Probability modifier | Rationale |
|--------|--------|---------------------|-----------|
| Popular uprising suppressed | OIL_SUPPLY_SHOCK | 1.4× | Production disruption during crisis |
| Revolutionary transition | OIL_SUPPLY_SHOCK | 2.5× | Major production disruption |
| Revolutionary transition | GLOBAL_FINANCIAL_CRISIS | 1.5× | Oil shock, regional instability |
| Revolutionary transition | SAUDI_REGIME_INSTABILITY | 0.7× | External threat may consolidate Gulf regimes |
| Failed succession crisis | OIL_SUPPLY_SHOCK | 1.5× | Production uncertainty during crisis |
| Failed succession crisis | IRAN_NUCLEAR_ACQUISITION | 1.3× | Factional competition may accelerate program |
| External intervention trigger | OIL_SUPPLY_SHOCK | 4.0× | Regional conflict disrupts ~20% of global oil |
| External intervention trigger | GLOBAL_FINANCIAL_CRISIS | 2.0× | Oil spike, market panic |
| External intervention trigger | SAUDI_REGIME_INSTABILITY | 1.5× | Iran retaliation against Gulf states |

### Cascade Targets Not in the Catalog

The original branch block named cascade targets that have no event file. Per [[events/backlog-registry]] they are not written into `triggers:`; each is listed there with a disposition.

| Branch | Referenced ID | Registry disposition |
|--------|---------------|---------------------|
| Popular uprising suppressed | REFUGEE_CRISIS_MENA | promote → `EUROPEAN_MIGRATION_CRISIS` (stub in round-2 catalog) |
| Popular uprising suppressed | SANCTIONS_INTENSIFICATION | decline (policy action; expressible as a `sanctions_level` impact row) |
| Revolutionary transition | NUCLEAR_SECURITY_CRISIS | promote (stub in round-2 catalog) |
| Revolutionary transition | PROXY_NETWORK_COLLAPSE | fold into `IRAN_REGIME_CHANGE` / `ISRAEL_IRAN_WAR` branch content |
| Revolutionary transition | KURDISH_AUTONOMY_EXPANSION | promote → `KURDISH_STATE_FORMATION` (low-priority queue) |
| Revolutionary transition | REFUGEE_CRISIS_MAJOR | promote → `EUROPEAN_MIGRATION_CRISIS` |
| Failed succession crisis | PROXY_NETWORK_WEAKENING | fold into `IRAN_REGIME_CHANGE` / `ISRAEL_IRAN_WAR` branch content |
| Failed succession crisis | NUCLEAR_PROGRAM_UNCERTAINTY | fold into `IRAN_NUCLEAR_ACQUISITION` |
| External intervention trigger | STRAIT_OF_HORMUZ_CRISIS | promote (stub in round-2 catalog; Task 6.1) |
| External intervention trigger | GULF_STATE_ATTACKS | promote (stub in round-2 catalog; Task 6.1) |
| External intervention trigger | ISRAEL_IRAN_WAR | promote (stub in round-2 catalog; Task 6.1) |

**Note**: Many intuitive cascade targets (proxy network collapse, Lebanon political crisis, Kurdish autonomy, Hormuz crisis) are not yet specified in the event catalog.

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

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

### Upgrade Rationale

Water crisis modeling; IRGC political economy; succession dynamics; nuclear program trajectory; proxy network dependencies.

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
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.9. Classification, probability, factor, branch, impact, cascade and research tables converted to the schema's blocks; the legacy `severity_branches` block merged into `branches:` / `impacts:` / `cascades:` with its descriptions, factor modifications, durations, multipliers and probability rationale kept in prose. Causal type: Type 2 as documented (not a hybrid); variance target 0.65, achieved 0.666 with the documented loadings. Pressure: the original ternary became `where()`, the weighted sum is wrapped in `100 * (...)`; at the prose's current values the expression gives 45.2-49.2, consistent with "~50/100"; the compiler's baseline check is skipped (all `irn.*` terms). Onset "rapid (1-3 years)" → `sudden`; "rapid (1yr/2yr)" row onsets → `{gradual: 1}`/`{gradual: 2}`. Durability substitutions (schema v0.2 backlog): `irn.gdp_real` decay-to-floor (half-life 4, floor −5%) → `decay: 4`; Lebanon "persistent" → `decay: 10`; per-branch decay-to-floor durations and factor modifications kept in a prose table, not compiled. Unit conversion: `oil_brent` +20% ± 12% → +$15 ± $9 against the $75 2025 baseline. Entity alternatives: `lbn.gdp_growth` −3 ± 2 pp → `levant_iraq.gdp_growth` −0.25 ± 0.15 (GDP-share weighted); `irq.internal_conflict_intensity` +1 → `levant_iraq.internal_conflict_intensity` +0.6 ± 0.3 (population-share weighted, half-life 5 assigned); "+2-3 levels" → 2.5 ± 0.5. Dropped row: `yem.internal_conflict_intensity` (Yemen is in no catalog entity or aggregate); channel kept in prose. Cascades: four flat deltas written; IRAN_NUCLEAR_ACQUISITION ("uncertain", no magnitude) kept in prose; eleven branch-block targets with no event file (REFUGEE_CRISIS_MENA, SANCTIONS_INTENSIFICATION, NUCLEAR_SECURITY_CRISIS, PROXY_NETWORK_COLLAPSE, KURDISH_AUTONOMY_EXPANSION, REFUGEE_CRISIS_MAJOR, PROXY_NETWORK_WEAKENING, NUCLEAR_PROGRAM_UNCERTAINTY, STRAIT_OF_HORMUZ_CRISIS, GULF_STATE_ATTACKS, ISRAEL_IRAN_WAR) kept in a prose table per [[events/backlog-registry]]; no aliases to normalize. No `until: resolved` rows, so no `resolves_after`. Restored from history: the original pre-scaling loadings (F_MENA 0.65 … F_SAS 0.05) and their sum-of-squares check (0.88) removed by the 2025-12-31 variance scaling |
| 2025-12-30 | Critical review: replaced synthetic variables with observables; added Case Against and Probability Evolution; fixed cascade/impact references | Task 2.4 systematic review |
| 2025-12-19 | Revised severity branches; removed "managed succession crisis" | Smooth succession isn't regime crisis; replaced with "failed succession crisis" where mechanism breaks down |
| 2025-12-19 | Initial Level 1 specification | Task 2.1.9 - Type 2 regime change event |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/saudi-regime-instability]] for regional comparison | [[factors/f-mena]] for regional factor*
