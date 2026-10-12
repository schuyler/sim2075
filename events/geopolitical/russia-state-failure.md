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

## Description

Collapse or severe fragmentation of effective Russian state authority, characterized by loss of central control over regions, military fragmentation or coup, elite faction warfare, potential territorial disintegration, and/or loss of control over nuclear arsenal. Russia's vulnerability is distinctive: extreme personalization of power in Putin, ongoing war exhaustion, unprecedented sanctions isolation, severe demographic decline, and nuclear weapons complexity.

This is a **state transition**: accumulated pressure crosses failure threshold, triggering shift from "authoritarian but functional" regime to "failed/fragmented state" regime. Observable via `internal_conflict_intensity` rising to 3-4, displacement flows activating, and GDP collapse.

**What marks occurrence**: Central government loses ability to command obedience from military/security services across territory; elite factions engage in open conflict; regions assert de facto independence; or nuclear command and control becomes uncertain.

---

## Specification

```yaml
id: RUSSIA_STATE_FAILURE
domain: political
scale: national
causal_type: 2
onset: sudden
reversibility: partial
```

*Scale: national (with global consequences). Onset speed: rapid (1-3 years from trigger to acute phase), recorded as `sudden` in the schema enum. Reversibility: partial (some form of Russian state likely persists; territorial integrity uncertain).*

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

**Pressure calculation** (original specification):
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

The YAML expression below realizes these transforms in the expression language's subset: the spending-deviation, negative-growth and emigration terms are clipped linear ramps capped at 1 (`min(1, max(0, x / scale))`), the transition-recency "inverse" term is `1 − min(1, years / 50)` so it floors at zero beyond 50 years, the tenure threshold is `where(rus.leadership_tenure_years > 20, 1, 0)` in place of the ternary, and the whole weighted sum is wrapped `100 * (...)` to sit on `threshold`'s 0-100 scale.

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

```yaml
probability:
  pressure: |
    100 * (
      0.25 * (rus.external_conflict_involvement / 4) +
      0.15 * min(1.0, max(0, rus.military_spending_deviation / 3)) +
      0.20 * (rus.sanctions_level / 100) +
      0.10 * (1.0 - min(1.0, rus.years_since_irregular_transition / 50)) +
      0.10 * where(rus.leadership_tenure_years > 20, 1.0, 0.0) +
      0.10 * min(1.0, max(0, -rus.gdp_growth) / 10) +
      0.10 * min(1.0, rus.emigration_skilled_rate / 5)
    )
  threshold: 75
  threshold_std: 8
  sharpness: 0.25
  floor: 0.004
  resolves_after: 5
  annual: 0.010
  range: [0.005, 0.018]
  confidence: medium
```

`resolves_after: 5` — `active_major_conflicts` counts the failure for five years per firing, counting the firing year: Russian state collapses in the reference class ran about that long (Russian Civil War 1917-22; the late-Soviet unravelling 1989-91 followed by the 1990s chaos; the Yugoslav dissolution wars 1991-95), and five is the shortest window consistent with the 10-year conflict-intensity half-life below.

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.0% |
| **Low bound** | 0.5% |
| **High bound** | 1.8% |
| **Confidence** | Medium-Low (recorded as `medium` in YAML: the schema enum is `low|medium|high`) |
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

*The "~55" is a judgment estimate: evaluated at the midpoints of the values listed above (conflict 3.5, deviation +2, sanctions 75, 32 years, tenure 25, growth −0.5%, emigration 2.5%), the YAML expression gives ~66, inside the threshold band (75 ± 8) but not yet at it. The compiler's baseline check is skipped for this event because every term reads a country variable, which the state catalog carries without a 2025 baseline.*

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

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

```yaml
factors:
  F_GPT: 0.49   # Great power competition is existential; Ukraine war is US/NATO proxy conflict
  F_EUR: 0.33   # European regional dynamics; Ukraine, NATO expansion, energy relationship
  F_FIN: 0.20   # Sanctions, SWIFT exclusion, reserve seizure, trade disruption
  F_CLIM: 0.10  # Permafrost infrastructure degradation; Arctic access; agricultural shifts
  F_TECH: 0.07  # Technology sanctions; semiconductor access; military modernization blocked
  F_FOOD: 0.03  # Russia is net food exporter; minimal vulnerability
  F_EAS: 0.03   # China relationship provides economic/diplomatic buffer
variance: 0.65  # Type 2 target
```

Factors with no loading: F_HLTH (no distinct pathway), F_MENA (limited direct linkage), F_SAS (no significant pathway), F_SSA (Wagner presence but not state-stability relevant), F_LAM (no significant pathway).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.66 from original loadings. The original Level 1 loadings (before Task 3.11 scaling) were F_GPT 0.75, F_EUR 0.50, F_FIN 0.30, F_CLIM 0.15, F_TECH 0.10, F_FOOD 0.05, F_EAS 0.05, with the same rationales; that specification recorded "Sum of squared loadings: 0.93 ✓" (the pre-Ω check in use at the time).

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
branches:
  - {id: regional_fragmentation, p: 0.45, desc: "Center weakens but does not collapse; regions gain de facto autonomy; late-Soviet pattern"}
  - {id: civil_conflict,         p: 0.35, desc: "Elite faction fighting escalates to armed conflict; territorial control contested"}
  - {id: catastrophic_collapse,  p: 0.20, desc: "State disintegration; successor states; nuclear arsenal disposition becomes international crisis"}
```

### Branch 1: Regional Fragmentation (45%)

Center weakens significantly but doesn't fully collapse. Regional power centers gain de facto autonomy (Chechnya, Siberian regions, Far East). Multiple elite factions compete openly. Formal unity nominally maintained but effective central control severely reduced. "Late Soviet" pattern before formal dissolution. Nuclear command stressed but probably intact. Economic dysfunction but not collapse.

**Impact multiplier**: 1.0× (baseline for this event). **Factor modifications**: F_GPT +0.30, F_EUR +0.25, F_EAS +0.15. **Duration**: decaying, half-life 8 years, floor 0.15.

### Branch 2: Civil Conflict (35%)

Elite faction fighting escalates to armed conflict. Military units align with different factions. Wagner-style mutiny but successful or prolonged. Territorial control actively contested. Some regions assert independence. Nuclear command and control stressed; military professionals likely maintain security but uncertainty is high. Significant population displacement.

**Impact multiplier**: 2.0×. **Factor modifications**: F_GPT +0.50, F_EUR +0.40, F_FIN +0.30. **Duration**: decaying, half-life 12 years, floor 0.20.

### Branch 3: Catastrophic Collapse (20%)

State disintegration comparable to Soviet collapse but more chaotic. Multiple successor states emerge. Nuclear arsenal disposition becomes international crisis. Moscow loses control over Far East, Caucasus, possibly Siberian regions. Mass displacement. Great power intervention likely (nuclear security). Economic collapse. "Yugoslavia with nukes" worst-case scenario.

**Impact multiplier**: 3.5×. **Factor modifications**: F_GPT +0.80, F_EUR +0.60, F_FIN +0.45, F_EAS +0.30. **Duration**: decaying, half-life 20 years, floor 0.30.

*The branch-level factor modifications and the decaying-to-floor branch durations above come from the original severity-branch block. Neither is a v0.1 schema construct (post-firing factor shifts and decay-to-floor durability are schema v0.2 backlog), so they stay here as prose; the YAML `impacts:` block carries the impact multipliers as `inherit`/`scale` and per-row half-lives. The branch-level cascade modifiers from the same block are tabulated under Cascade Effects.*

### Severity Probability Rationale

Distribution reflects Russia's structural features, conditional on actual state failure occurring (smooth successions don't trigger this event):

- **Regional fragmentation (0.45)**: Most likely failure mode. Historical pattern—late Soviet period showed gradual weakening before formal collapse. Regional governors and security figures have power bases. Nuclear deterrent prevents external regime change, allowing prolonged dysfunction short of complete collapse.
- **Civil conflict (0.35)**: Wagner mutiny showed fragility exists beneath surface. Elite factions are suppressed but present. Military has shown unity so far but is degraded by war. Succession crisis without clear winner could trigger factional fighting.
- **Catastrophic collapse (0.20)**: Russia's security apparatus is robust, and nuclear weapons create strong incentives for all parties (domestic and international) to prevent complete collapse. However, once civil conflict begins, cascades can accelerate beyond control. Historical Russian state collapses (1917, 1991) were severe.

---

## Impacts

The explicit list is the regional-fragmentation branch (the 1.0× baseline); `civil_conflict` and `catastrophic_collapse` inherit it at the 2.0× and 3.5× impact multipliers above.

```yaml
impacts:
  regional_fragmentation:
    # Russia
    - {var: rus.gdp_real,                    mag: [-0.20, 0.10], onset: {gradual: 2}, decay: 8}
    - {var: rus.gdp_growth,                  mag: [-8, 4],       onset: immediate,    decay: 3}
    - {var: rus.internal_conflict_intensity, mag: [2, 0.5],      onset: immediate,    decay: 10}
    - {var: rus.net_migration_rate,          mag: [-2, 1],       onset: {gradual: 2}, decay: 5}
    - {var: rus.emigration_skilled_rate,     mag: [3, 1.5],      onset: immediate,    decay: 5}
    - {var: rus.refugees_abroad,             mag: [2, 1],        onset: {gradual: 3}, decay: 15}
    - {var: rus.idp_population,              mag: [3, 2],        onset: {gradual: 2}, decay: 10}

    # Global
    - {var: oil_brent,                       mag: [22.5, 15],    onset: immediate,    decay: 2}
    - {var: gas_europe_ttf,                  mag: [17.5, 10.5],  onset: immediate,    decay: 2}
    - {var: global_credit_spread,            mag: [50, 30],      onset: immediate,    decay: 1}
    - {var: active_major_conflicts,          mag: [1, 0],        onset: immediate,    until: resolved}

    # Regional
    - {var: ukr.external_conflict_involvement, mag: [-2, 0],     onset: {gradual: 1}, permanent: true}
    - {var: kaz.internal_conflict_intensity, mag: [1, 0],        onset: {gradual: 2}, decay: 5}
    - {var: deu.gdp_growth,                  mag: [-1, 0.5],     onset: {gradual: 1}, decay: 2}

  civil_conflict:
    inherit: regional_fragmentation
    scale: 2.0

  catastrophic_collapse:
    inherit: regional_fragmentation
    scale: 3.5
```

*Units: `gdp_real` rows are fractions of the entity's current value (−20% ± 10% for the regional-fragmentation branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). "Rapid (N yr)" onsets in the original tables are written `{gradual: N}`.*

### Rows re-expressed or dropped at migration

The original impact tables gave some rows in forms the YAML cannot carry directly; the original wording is kept here.

| Variable | Original specification | In YAML |
|----------|------------------------|---------|
| `rus.gdp_real` | −20% ± 10%, rapid (2yr), decaying (half_life: 8yr, floor: −10%) | −0.20 ± 0.10 fraction, half-life 8; the −10% recovery floor is schema v0.2 backlog |
| `rus.internal_conflict_intensity` | ↑ to 3-4, immediate, decaying (half_life: 10yr) | +2 ± 0.5 from Russia's ~1 baseline (minor North Caucasus conflict), reaching ~3 in the baseline branch; the inherited branches scale it higher |
| `rus.sanctions_level` | complex; may decrease if regime changes | Dropped: no magnitude or direction is specifiable. Sanctions relief on regime change is a channel the sanctions-level variable carries only through later policy, not an event impact |
| `oil_brent` | +30% ± 20%, immediate, half-life 2yr | +22.5 ± 15 $/bbl against the 2025 baseline of $75/bbl |
| `gas_europe_ttf` | +50% ± 30%, immediate, half-life 2yr | +17.5 ± 10.5 €/MWh against the 2025 baseline of €35/MWh |
| `active_major_conflicts` | +1, immediate, event-dependent | `until: resolved` with `resolves_after: 5` |
| `ukr.external_conflict_involvement` | −2 levels, rapid (1yr), persistent | −2 ± 0 (no std given), `permanent: true` |
| `kaz.internal_conflict_intensity` | +1 level, rapid (2yr), decaying (no half-life given) | +1 ± 0, half-life 5 years (judgment: a spillover shorter-lived than Russia's own 10-year conflict decay) |
| `chn.trade_share_china` | — regional reorientation, gradual, persistent | Dropped: no magnitude; the channel (Russia's trade reorienting toward China, which would read on `rus.trade_share_china`) stays in the Strategic realignment pathway below |

**Note**: Many intuitive impact channels (nuclear security indices, great power stability measures) are derived outputs, not state variables. The simulation tracks observable impacts on GDP, conflict levels, commodity prices, and displacement—interpretive assessments are computed from these.

### Nuclear Consideration

Russia possesses ~6,000 nuclear warheads—the world's largest arsenal. State failure raises unique concerns:
- **Regional fragmentation**: Nuclear command probably intact but chain of control stressed; uncertainty increases
- **Civil conflict**: Serious concerns; military professionals likely maintain security but uncertainty high
- **Catastrophic collapse**: Major international crisis; intervention likely; 1990s "loose nukes" fears but worse

Nuclear security concerns dominate international response calculus and create strong incentives for managed outcomes—which is why smooth successions (not modeled here) are the most likely response to regime stress.

### Durability Rationale

- **GDP**: Decaying; Russia has recovered from crises before (1998, 2014) but structural damage accumulates. The original specification carried a −10% floor on the GDP recovery; decay-to-floor durability is schema v0.2 backlog, so the YAML uses a plain 8-year half-life.
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

```yaml
cascades:
  triggers:
    - {event: OIL_SUPPLY_SHOCK,        delta: 0.030, years: 3}
    - {event: GLOBAL_FINANCIAL_CRISIS, delta: 0.010, years: 2}
    - {event: IRAN_REGIME_CHANGE,      delta: 0.005, years: 5}
  triggered_by: []  # no inbound cascades specified; Type 2 event driven by pressure accumulation
```

| Pathway | Target Event | Probability Change | Mechanism |
|---------|--------------|-------------------|-----------|
| Energy disruption | OIL_SUPPLY_SHOCK | +3%/year for 3 years | Russian supply uncertainty |
| Financial contagion | GLOBAL_FINANCIAL_CRISIS | +1%/year for 2 years | Market panic, commodity volatility |
| Regional instability | IRAN_REGIME_CHANGE | +0.5%/year for 5 years | Russian support withdrawn |

### Branch-Level Cascade Modifiers

The original severity-branch block also carried per-branch multiplicative modifiers on target-event probabilities. The schema's `triggers:` take an absolute annual `delta`, and converting a multiplier needs the target's own baseline, so these stay as prose rather than being invented into YAML; the `delta` rows above are the specified cascades.

| Branch | Target Event | Probability modifier | Rationale |
|--------|--------------|---------------------|-----------|
| Regional fragmentation | OIL_SUPPLY_SHOCK | ×1.5 | Energy supply disruption |
| Civil conflict | GLOBAL_FINANCIAL_CRISIS | ×1.5 | Market panic from major power instability |
| Civil conflict | OIL_SUPPLY_SHOCK | ×2.0 | Russian energy export disruption |
| Catastrophic collapse | GLOBAL_FINANCIAL_CRISIS | ×2.0 | Systemic shock from major power collapse |
| Catastrophic collapse | OIL_SUPPLY_SHOCK | ×2.5 | Severe energy supply disruption |
| Catastrophic collapse | TAIWAN_CONFLICT | ×1.3 | Strategic distraction; US attention divided |

**Note**: Many intuitive cascade targets (Central Asian instability, Caucasus conflicts, nuclear security crisis) are not yet specified in the event catalog. These should be considered for future event development. The original branch block named them as `CENTRAL_ASIA_INSTABILITY` and `CAUCASUS_CONFLICT` (regional fragmentation), `NUCLEAR_SECURITY_CRISIS`, `UKRAINE_CONFLICT_RESOLUTION` and `EUROPEAN_REFUGEE_CRISIS` (civil conflict), and `NUCLEAR_SECURITY_CRISIS`, `GREAT_POWER_INTERVENTION` and `CHINA_FAR_EAST_ASSERTION` (catastrophic collapse); each has a disposition in [[events/backlog-registry]] (promotions: NUCLEAR_SECURITY_CRISIS, UKRAINE_CONFLICT_RESOLUTION, EUROPEAN_MIGRATION_CRISIS; fold: CHINA_FAR_EAST_ASSERTION into this event's aftermath; declined: CENTRAL_ASIA_INSTABILITY, CAUCASUS_CONFLICT, GREAT_POWER_INTERVENTION) and none is written into `triggers:` until a file exists.

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

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

### Upgrade Rationale

War trajectory assessment; elite cohesion analysis; nuclear security deep-dive; succession scenario modeling.

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
| 2025-12-18 | Initial Level 1 specification | Task 2.1.7 - Type 2 state failure event |
| 2025-12-18 | Adjusted probability to 1.0% (from 1.2%) | Reflects that event now only fires for actual failure, not regime transitions |
| 2025-12-18 | Revised severity branches; removed "managed succession" | Smooth succession isn't state failure; all branches should represent genuine dysfunction |
| 2025-12-30 | Critical review: replaced synthetic variables with observables; added Case Against and Probability Evolution; fixed cascade/impact references | Task 2.4 systematic review |
| 2025-12-30 | Variance allocation: scaled loadings to Type 2 target | Task 3.11 - Factor-explained variance reduced to Type 2 target (0.65); original loadings and the "sum of squared loadings 0.93" line are restored in prose above |
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.7. `causal_type: 2` (not a hybrid). Enums: onset "rapid (1-3 years)" → `sudden`; confidence "Medium-Low" → `medium` (wording kept in prose). Pressure: transforms realized with `min`/`max`/`where` and wrapped `100 * (...)`; at the prose's current values the expression gives ~66 against the "~55" judgment estimate; baseline check skipped (country variables only). `resolves_after: 5` (rationale under the probability block). Legacy `severity_branches` block merged into `branches:`; its factor modifications, decay-to-floor durations and multiplicative cascade modifiers kept in prose (no v0.1 construct). Impacts: regional_fragmentation explicit, civil_conflict `scale: 2.0`, catastrophic_collapse `scale: 3.5` per the impact multipliers; inherited rows on bounded scales (conflict levels) exceed their range in the upper branches, as in pakistan-state-failure. Unit conversions: `oil_brent` +30% ± 20% → +22.5 ± 15 $/bbl (baseline 75); `gas_europe_ttf` +50% ± 30% → +17.5 ± 10.5 €/MWh (baseline 35); `rus.internal_conflict_intensity` "to 3-4" → +2 ± 0.5 from a ~1 baseline. Durability: GDP decay-to-floor(−10%) → `decay: 8`; "persistent" → `permanent: true`; "event-dependent" → `until: resolved`; `kaz` "decaying" with no half-life → `decay: 5` (judgment). Dropped rows (kept in prose): `rus.sanctions_level` ("complex"), `chn.trade_share_china` (no magnitude). Cascades: the three specified delta rows written to `triggers:`; branch-level multipliers kept in prose; `NUCLEAR_SECURITY_CRISIS`, `UKRAINE_CONFLICT_RESOLUTION`, `EUROPEAN_REFUGEE_CRISIS`, `CHINA_FAR_EAST_ASSERTION`, `CENTRAL_ASIA_INSTABILITY`, `CAUCASUS_CONFLICT`, `GREAT_POWER_INTERVENTION` not written (registry promotions/fold/declines). Restored from history: original pre-scaling loadings and sum-of-squares line |

---

*See [[methodology/reference/probability-estimation]] for Type 2 threshold methodology | [[events/geopolitical/egypt-state-failure]] for comparison | [[factors/f-gpt]] for great power factor*
