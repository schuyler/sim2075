---
title: Korean Peninsula Crisis
type: note
permalink: events/geopolitical/korean-peninsula-crisis
tags:
- event
- type-3
- geopolitical
- east-asia
- korea
- dprk
- nuclear
- level-1
---

# Korean Peninsula Crisis

**Type 3 (Contingent) Event** — Military conflict involving North Korea, South Korea, and/or the United States.

---

## Event Classification

```yaml
id: KOREAN_PENINSULA_CRISIS
domain: political
scale: regional
causal_type: 3
onset: sudden
reversibility: partial
```

*Scale: regional (with global implications). Onset speed: sudden (<1yr). Reversibility: partial to irreversible (aftermath-dependent) — recorded as `partial` in YAML, the nearer single enum value for the 85% of outcomes that are not nuclear.*

## Description

Military conflict on the Korean Peninsula — artillery exchanges, missile strikes, naval engagements, or ground operations involving DPRK, ROK, and/or US forces. Distinguished from baseline provocations and sub-threshold tensions by actual combat operations causing military casualties beyond isolated incidents. This is the discontinuity; crises that de-escalate without sustained combat are non-events.

The unique feature of this scenario is the US tripwire: ~28,000 American troops in South Korea mean any significant DPRK attack automatically involves the United States, unlike most regional conflicts.

---

## Causal Type Specification

### Type 3 (Contingent) Event

This event has Type 3 structure: preconditions create crisis windows, and actor decisions determine whether military conflict occurs. The probability decomposition is:

- **P(crisis window)**: ~2.5% annually — acute crisis develops beyond normal provocations
- **P(military conflict | window)**: ~30% — conflict occurs given crisis
- **P(event)**: ~0.75% annually — the discontinuity probability

The 70% of crisis windows that de-escalate without sustained combat are *non-events* — they don't appear in the simulation as discontinuities.

**Window Preconditions**:

| Condition | Threshold |
|-----------|-----------|
| F_EAS (East Asian Tension) | Elevated regional instability |
| F_GPT (Great Power Tension) | US-China relations strained, reducing crisis management capacity |
| Triggering incident | Nuclear/missile test, border incident, leadership transition crisis, or external shock (e.g., Taiwan conflict) |
| DPRK internal dynamics | Regime stress, succession crisis, or miscalculation incentives |

The YAML `preconditions.all` below realizes the two factor rows as `F_EAS > 1.0` and `F_GPT > 1.0` (one standard deviation above the mean, the same realization of "elevated" used by [[events/geopolitical/taiwan-conflict]]). The triggering-incident and DPRK-internal-dynamics rows have no state variable in the catalog (there is no DPRK succession or regime-stress observable, and a nuclear/missile test is an incident, not a state); they are carried by the 2.5% window draw itself rather than by an expression.

**Historical basis for window probability (~2.5%)**:

Acute crises approaching or crossing military threshold:
- 1968 Pueblo Incident and Blue House Raid (near-conflict)
- 1976 Axe Murder Incident (near-conflict, US DEFCON 3)
- 1994 First Nuclear Crisis (war seriously considered)
- 2010 Cheonan sinking and Yeonpyeong shelling (actual combat, limited)
- 2017 "Fire and Fury" crisis (rhetorical escalation, no combat)

Pattern: ~1 acute crisis per 10-15 years historically. Current elevated baseline (DPRK nuclear advancement, US-China tensions, potential Kim succession) suggests modestly above-historical crisis frequency.

**Historical basis for conflict probability given window (~30%)**:

Of the ~5 acute crises since 1968, only 2010 involved actual military operations (Cheonan sinking, Yeonpyeong shelling). However, these were limited and contained. Full-scale conflict has been avoided despite multiple close calls.

The 30% estimate reflects:
- DPRK pattern of calibrating provocations short of war
- Strong deterrence from US-ROK alliance and DPRK's nuclear arsenal
- Both sides have demonstrated ability to de-escalate (1994, 2017)
- BUT: Miscalculation risk, especially during leadership transitions or if DPRK perceives existential threat

This is lower than India-Pakistan (35%) because:
- Clearer asymmetry (DPRK cannot conventionally defeat US-ROK)
- Stronger external crisis management (China has leverage over DPRK)
- No equivalent to Kashmir's ongoing low-level conflict creating friction

---

## Probability

```yaml
probability:
  window: 0.025
  preconditions:
    all:
      - "F_EAS > 1.0"
      - "F_GPT > 1.0"
  resolution: 0.30
  resolves_after: 2
  annual: 0.0075
  range: [0.004, 0.012]
  confidence: medium
```

`resolves_after: 2` — the `until: resolved` rows (conflict involvement, active major conflicts) hold for two years per firing, counting the firing year: the modal limited-conflict branch (55%) lasts "days to weeks" and resolves within the firing year, but the major-war branch runs "months to potentially years" (the 1950-53 war ran three), so a branch-weighted window rounds to two.

| Metric | Value |
|--------|-------|
| **Annual probability** | ~0.75% |
| **Low bound** | 0.4% |
| **High bound** | 1.2% |
| **Confidence** | Medium |
| **25-year cumulative** | ~17% (at least one conflict) |

### Derivation

1. **Window probability**: 2.5% annually (1.5-4.0% range)
2. **Conflict given window**: 30% (20-40% range)
3. **Combined**: 2.5% × 30% = 0.75%

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Korean Peninsula Crisis | ~0.75% | — |
| India-Pakistan Military Conflict | ~0.9% | Higher — more frequent crises, similar conflict-given-crisis |
| Taiwan Conflict | ~2.0% | Higher — larger stakes, higher window probability |
| Pakistan State Failure | ~1.5% | Higher — structural pressures more sustained |
| US Constitutional Crisis | ~0.5% | Lower — more institutional resilience |

### Key Uncertainties

- **Kim succession**: Unclear succession could create instability window or desperate action incentives
- **DPRK nuclear doctrine**: "Use before you lose" posture affects escalation dynamics
- **US commitment credibility**: Changes in US posture affect deterrence
- **China-DPRK relationship**: Beijing's ability and willingness to restrain Pyongyang
- **Taiwan linkage**: Simultaneous Taiwan crisis could enable DPRK opportunism or US force constraints

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 3 target (ΛΩΛᵀ)ᵢᵢ = 0.45*

```yaml
factors:
  F_EAS: 0.48   # Primary driver: regional tension directly conditions crisis probability
  F_GPT: 0.23   # Great power dynamics affect crisis management, US-China coordination
  F_FIN: 0.08   # Sanctions pressure, DPRK economic stress affects regime calculus
  F_FOOD: 0.06  # DPRK food insecurity creates regime stress
  F_CLIM: 0.03  # Marginal — food security stress could add to DPRK pressure
  F_TECH: 0.03  # Marginal — missile/nuclear technology affects capability
variance: 0.45  # Type 3 target
```

F_HLTH, F_EUR, F_MENA, F_SAS, F_SSA and F_LAM carry no loading (no direct pathway).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.45 (Type 3 target); scale factor = 0.56 from original loadings. The original (pre-allocation) loadings were F_EAS 0.85, F_GPT 0.40, F_FIN 0.15, F_FOOD 0.10, F_CLIM 0.05, F_TECH 0.05; sum of squared loadings 0.92 ✓ (the initial specification's check before Ω-weighted variance replaced it). With Ω the current loadings achieve 0.455.

### Loading Rationale

F_EAS is dominant because Korean Peninsula dynamics are embedded in broader East Asian regional tensions — US-China competition, Japan's security posture, and cross-strait dynamics all affect the peninsula's stability. F_GPT captures great power crisis management capacity; when US-China relations deteriorate, their ability to jointly manage Korean crises declines.

Factors shock state variables (`regime_stability`, `us_china_tension`, DPRK internal stress) which affect both crisis window probability and conflict probability given window.

---

## Aftermath Branches

Once military conflict occurs, the form it takes:

```yaml
branches:
  - {id: limited_conflict,        p: 0.55, desc: "Artillery exchanges, naval skirmishes, targeted strikes; days to weeks"}
  - {id: major_conventional_war,  p: 0.30, desc: "DPRK crosses DMZ or sustained bombardment of Seoul; months to years"}
  - {id: nuclear_escalation,      p: 0.15, desc: "DPRK nuclear use; civilizational-scale consequences for the peninsula"}
```

### Branch 1: Limited Conflict (55%)

Limited military operations: artillery exchanges across DMZ, naval skirmishes, targeted missile strikes on military facilities. Similar to Yeonpyeong (2010) but more sustained and intense. Duration: days to weeks. Seoul likely takes some artillery damage but no ground invasion. No nuclear weapons use. US forces engaged but conflict contained to peninsula.

**Factor modifications** (post-event factor shifts; not a v0.1 engine construct, kept for the schema v0.2 backlog): F_EAS +0.50, F_GPT +0.30, F_FIN +0.20.

**Duration** (original form): decaying, half-life 3 years, floor 0.10.

**Original impact vector** (the YAML `impacts:` block below re-expresses these in catalog variables and units):

| Entity | Variable | Magnitude |
|--------|----------|-----------|
| South Korea | gdp_growth | −4.0 ± 2.0 pp |
| South Korea | gdp_real | −2 ± 1 % |
| South Korea | military_spending | +0.5 ± 0.2 pp of GDP |
| South Korea | external_conflict_involvement | 3 (major limited war) |
| South Korea | regime_stability | −5 ± 5 |
| North Korea | gdp_growth | −8.0 ± 4.0 pp |
| North Korea | regime_stability | −10 ± 8 |
| North Korea | sanctions_level | +15 ± 5 |
| Japan | gdp_growth | −1.0 ± 0.5 pp |
| Japan | military_spending | +0.3 ± 0.1 pp of GDP |
| China | gdp_growth | −0.5 ± 0.3 pp |
| United States | military_spending | +0.1 ± 0.05 pp of GDP |
| United States | external_conflict_involvement | 2 (limited engagement) |
| Global | semiconductor_supply | −0.15 ± 0.10 |
| Global | oil_brent | +10 ± 5 $/barrel (temporary) |
| Global | active_major_conflicts | +1 |
| Global | us_china_tension | +15 ± 5 |

### Branch 2: Major Conventional War (30%)

Escalation to large-scale conventional operations. DPRK ground forces cross DMZ or sustained artillery bombardment of Seoul. Massive casualties — Seoul (25M metro) highly vulnerable. US deploys major reinforcements; full US-ROK counteroffensive. Duration: months to potentially years. China faces difficult choice: intervene, tolerate regime collapse, or try diplomacy. Nuclear threshold not crossed but repeatedly approached.

**Factor modifications** (not a v0.1 construct): F_EAS +0.80, F_GPT +0.60, F_FIN +0.40.

**Duration** (original form): decaying, half-life 6 years, floor 0.20.

**Branch cascade triggers** (prose only; the Cascade Effects section below says why neither is compiled):

- **DPRK_REGIME_COLLAPSE** — probability modifier ×2.5. Rationale: "Major military defeat would likely end Kim regime."
- **US_CHINA_DIRECT_CONFLICT** — probability 0.35. Rationale: Chinese intervention is small-N actor decision with low tractability. Structural factors toward intervention: buffer state preservation (Korean War precedent); preventing US forces on Chinese border; refugee crisis prevention. Structural factors against: US nuclear deterrence; economic costs during own domestic stress; no formal alliance with DPRK (1961 treaty ambiguous). Weighting toward non-intervention (35% intervention) based on costs of direct conflict with US being catastrophic.

**Original impact vector**:

| Entity | Variable | Magnitude |
|--------|----------|-----------|
| South Korea | gdp_growth | −15.0 ± 5.0 pp |
| South Korea | gdp_real | −10 ± 5 % |
| South Korea | military_spending | +2.0 ± 0.5 pp of GDP |
| South Korea | external_conflict_involvement | 4 (major war) |
| South Korea | pop_total | −0.5 ± 0.3 % (casualties, Seoul vulnerability) |
| South Korea | regime_stability | −15 ± 10 |
| North Korea | gdp_real | −30 ± 15 % |
| North Korea | regime_stability | −40 ± 15 |
| North Korea | external_conflict_involvement | 4 (major war) |
| North Korea | pop_total | −2 ± 1 % (casualties) |
| Japan | gdp_growth | −3.0 ± 1.5 pp |
| Japan | military_spending | +0.5 ± 0.2 pp of GDP |
| China | gdp_growth | −2.0 ± 1.0 pp |
| China | net_migration_rate | +0.2 ± 0.1 pp (refugee inflows) |
| United States | gdp_growth | −1.0 ± 0.5 pp |
| United States | military_spending | +0.5 ± 0.2 pp of GDP |
| United States | external_conflict_involvement | 3 (major limited war) |
| United States | pop_15_34_m | −0.01 ± 0.005 % (casualties) |
| Global | semiconductor_supply | −0.40 ± 0.15 |
| Global | global_trade_volume | −5 ± 3 % |
| Global | oil_brent | +20 ± 10 $/barrel |
| Global | active_major_conflicts | +1 |
| Global | us_china_tension | +25 ± 10 |

### Branch 3: Nuclear Escalation (15%)

Conflict escalates to nuclear weapons use by DPRK. Most likely pathway: DPRK first use against US/ROK military concentration or South Korean cities as regime faces collapse ("use before you lose" doctrine). Could also occur via demonstration strike intended to force negotiation, or through command-and-control breakdown. US nuclear response uncertain but likely if DPRK strikes US forces. Civilizational-scale consequences for Korean Peninsula.

**Factor modifications** (not a v0.1 construct): F_EAS +1.50, F_GPT +1.30, F_FIN +0.80, F_HLTH +0.30.

**Duration** (original form): persistent, no exit conditions.

**Branch cascade triggers** (prose only):

- **GLOBAL_NUCLEAR_RECONFIGURATION** — window opens, probability 1.0. Rationale: "Nuclear taboo broken; proliferation incentives transform."
- **DPRK_REGIME_COLLAPSE** — probability 0.90. Rationale: "Regime unlikely to survive nuclear war regardless of military outcome."

**Original impact vector**:

| Entity | Variable | Magnitude |
|--------|----------|-----------|
| South Korea | gdp_real | −25 ± 15 % |
| South Korea | pop_total | −3.0 ± 2.0 % (casualties; Seoul vulnerability extreme) |
| South Korea | life_expectancy | −5 ± 3 years |
| South Korea | institutional_quality | −0.5 ± 0.3 |
| South Korea | regime_stability | −30 ± 15 |
| North Korea | gdp_real | −50 ± 20 % |
| North Korea | pop_total | −5.0 ± 3.0 % (casualties from US response) |
| North Korea | regime_stability | −60 ± 20 |
| North Korea | life_expectancy | −8 ± 4 years |
| Japan | gdp_real | −8 ± 5 % |
| Japan | regime_stability | −10 ± 5 |
| China | gdp_real | −5 ± 3 % |
| China | net_migration_rate | +0.5 ± 0.3 pp (refugee crisis) |
| United States | gdp_real | −3 ± 2 % |
| United States | alliance_west | −10 ± 5 (alliance credibility questioned) |
| Global | nuclear_stability | −50 ± 15 |
| Global | global_trade_volume | −15 ± 8 % |
| Global | semiconductor_supply | −0.60 ± 0.20 |
| Global | oil_brent | +35 ± 15 $/barrel |
| Global | active_major_conflicts | +1 |

### Aftermath Probability Rationale

Limited conflict (55%): Historical precedent (Cheonan, Yeonpyeong) shows both sides can calibrate. DPRK has consistently limited provocations short of actions that would trigger overwhelming US response. Strong incentives for all parties to contain escalation.

Major war (30%): Once operations begin, escalation pressures substantial. DPRK's conventional inferiority creates "escalate or lose" dynamic. Kim regime may view major war as better than slow strangulation. Accidental escalation from initial exchange possible.

Nuclear (15%): DPRK has explicitly stated nuclear weapons exist to guarantee regime survival. If regime faces collapse, nuclear use becomes thinkable. But 15% conditional may be conservative — DPRK doctrine suggests tactical nuclear use against military concentrations is explicitly contemplated, unlike India-Pakistan where nuclear threshold is less clearly articulated.

---

## Impacts

```yaml
impacts:
  limited_conflict:
    # South Korea
    - {var: kor.gdp_growth,                    mag: [-4.0, 2.0],   onset: immediate, decay: 3}
    - {var: kor.gdp_real,                      mag: [-0.02, 0.01], onset: immediate, decay: 3}
    - {var: kor.military_spending,             mag: [0.5, 0.2],    onset: immediate, decay: 3}
    - {var: kor.external_conflict_involvement, mag: [3, 0],        onset: immediate, until: resolved}
    - {var: kor.protest_intensity_annual,      mag: [5, 5],        onset: immediate, decay: 3}
    # North Korea
    - {var: prk.gdp_growth,                    mag: [-8.0, 4.0],   onset: immediate, decay: 3}
    - {var: prk.protest_intensity_annual,      mag: [10, 8],       onset: immediate, decay: 3}
    - {var: prk.sanctions_level,               mag: [15, 5],       onset: immediate, decay: 3}
    # Japan
    - {var: jpn.gdp_growth,                    mag: [-1.0, 0.5],   onset: immediate, decay: 3}
    - {var: jpn.military_spending,             mag: [0.3, 0.1],    onset: immediate, decay: 3}
    # China
    - {var: chn.gdp_growth,                    mag: [-0.5, 0.3],   onset: immediate, decay: 3}
    # United States
    - {var: usa.military_spending,             mag: [0.1, 0.05],   onset: immediate, decay: 3}
    - {var: usa.external_conflict_involvement, mag: [2, 0],        onset: immediate, until: resolved}
    # Global
    - {var: semiconductor_supply,              mag: [-15, 10],     onset: immediate, decay: 3}
    - {var: oil_brent,                         mag: [10, 5],       onset: immediate, decay: 1}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}

  major_conventional_war:
    # South Korea
    - {var: kor.gdp_growth,                    mag: [-15.0, 5.0],  onset: immediate, decay: 6}
    - {var: kor.gdp_real,                      mag: [-0.10, 0.05], onset: immediate, decay: 6}
    - {var: kor.military_spending,             mag: [2.0, 0.5],    onset: immediate, decay: 6}
    - {var: kor.external_conflict_involvement, mag: [4, 0],        onset: immediate, until: resolved}
    - {var: kor.protest_intensity_annual,      mag: [15, 10],      onset: immediate, decay: 6}
    # North Korea
    - {var: prk.gdp_real,                      mag: [-0.30, 0.15], onset: immediate, decay: 6}
    - {var: prk.protest_intensity_annual,      mag: [40, 15],      onset: immediate, decay: 6}
    - {var: prk.external_conflict_involvement, mag: [4, 0],        onset: immediate, until: resolved}
    # Japan
    - {var: jpn.gdp_growth,                    mag: [-3.0, 1.5],   onset: immediate, decay: 6}
    - {var: jpn.military_spending,             mag: [0.5, 0.2],    onset: immediate, decay: 6}
    # China
    - {var: chn.gdp_growth,                    mag: [-2.0, 1.0],   onset: immediate, decay: 6}
    - {var: chn.net_migration_rate,            mag: [0.2, 0.1],    onset: immediate, decay: 6}
    # United States
    - {var: usa.gdp_growth,                    mag: [-1.0, 0.5],   onset: immediate, decay: 6}
    - {var: usa.military_spending,             mag: [0.5, 0.2],    onset: immediate, decay: 6}
    - {var: usa.external_conflict_involvement, mag: [3, 0],        onset: immediate, until: resolved}
    - {var: usa.pop_15_34_m,                   mag: [-0.0045, 0.0023], onset: immediate, permanent: true}
    # Global
    - {var: semiconductor_supply,              mag: [-40, 15],     onset: immediate, decay: 6}
    - {var: global_trade_volume,               mag: [-5, 3],       onset: immediate, decay: 6}
    - {var: oil_brent,                         mag: [20, 10],      onset: immediate, decay: 6}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}

  nuclear_escalation:
    # South Korea
    - {var: kor.gdp_real,                      mag: [-0.25, 0.15], onset: immediate, permanent: true}
    - {var: kor.life_expectancy,               mag: [-5, 3],       onset: immediate, permanent: true}
    - {var: kor.protest_intensity_annual,      mag: [30, 15],      onset: immediate, permanent: true}
    # North Korea
    - {var: prk.gdp_real,                      mag: [-0.50, 0.20], onset: immediate, permanent: true}
    - {var: prk.protest_intensity_annual,      mag: [60, 20],      onset: immediate, permanent: true}
    - {var: prk.life_expectancy,               mag: [-8, 4],       onset: immediate, permanent: true}
    # Japan
    - {var: jpn.gdp_real,                      mag: [-0.08, 0.05], onset: immediate, permanent: true}
    - {var: jpn.protest_intensity_annual,      mag: [10, 5],       onset: immediate, permanent: true}
    # China
    - {var: chn.gdp_real,                      mag: [-0.05, 0.03], onset: immediate, permanent: true}
    - {var: chn.net_migration_rate,            mag: [0.5, 0.3],    onset: immediate, permanent: true}
    # United States
    - {var: usa.gdp_real,                      mag: [-0.03, 0.02], onset: immediate, permanent: true}
    # Global
    - {var: global_trade_volume,               mag: [-15, 8],      onset: immediate, permanent: true}
    - {var: semiconductor_supply,              mag: [-60, 20],     onset: immediate, permanent: true}
    - {var: oil_brent,                         mag: [35, 15],      onset: immediate, permanent: true}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}
```

*Units: `gdp_real` rows are fractions of the entity's current value (−2% ± 1% for South Korea in the limited branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). `gdp_growth` and `military_spending` rows are in percentage points, as in the original vectors. Index variables were converted against their 2025 baselines of 100: `semiconductor_supply` −0.15/−0.40/−0.60 (fractions) → −15/−40/−60 index points, `global_trade_volume` −5%/−15% → −5/−15 index points. `oil_brent` is already in $/barrel. The `external_conflict_involvement` rows follow the taiwan-conflict convention of adding the stated level to the 0-4 scale. `usa.pop_15_34_m` is in millions: −0.01% ± 0.005% of a ~45M cohort (US males aged 15-34) → −0.0045 ± 0.0023 M.*

### Variable Substitutions and Dropped Rows

The original impact vectors used some synthetic variables (flagged at the 2025-12-30 critical review for replacement with observables at Level 2). At migration:

- **`regime_stability` → `protest_intensity_annual`** (sign flipped, same 0-100 scale) for kor, prk and jpn in every branch. The state catalog's observable political-stress measure is `protest_intensity_annual` (see the proxy note in [[events/geopolitical/pakistan-state-failure]]); for the DPRK, where organized protest is suppressed, the index stands in for regime stress rather than literal street protest.
- **`pop_total` rows dropped** (kor −0.5% and prk −2% in major war; kor −3.0% and prk −5.0% in nuclear escalation): `pop_total` is a derived variable and cannot be an impact target, and allocating the casualties across the twelve age-sex cohorts would be invention. The casualty channel stays in the original vectors above and in the mortality note below; `life_expectancy` rows carry the nuclear-branch mortality.
- **`us_china_tension` rows dropped** (+15 limited, +25 major war): no global tension variable exists in the catalog; the channel is represented by the F_GPT loading and the US_CHINA_DIRECT_CONFLICT cascade in prose.
- **`kor.institutional_quality` dropped** (−0.5 ± 0.3, nuclear): not a catalog variable and no governance variable shares its scale.
- **`usa.alliance_west` dropped** (−10 ± 5, nuclear): the catalog's `alliance_status` is categorical; alliance credibility has no numeric observable.
- **`nuclear_stability` dropped** (−50 ± 15, nuclear): not a global variable; the nuclear-precedent channel is carried by the GLOBAL_NUCLEAR_RECONFIGURATION cascade (prose) pending `NPT_REGIME_COLLAPSE`.

### Durability Rationale

| Branch | Original form | YAML form | Note |
|--------|---------------|-----------|------|
| Limited conflict | decaying, half-life 3 yr, floor 0.10 | `decay: 3` | Decay-to-floor is schema v0.2 backlog; plain half-life used. `oil_brent` marked "(temporary)" in the original vector gets `decay: 1` |
| Major conventional war | decaying, half-life 6 yr, floor 0.20 | `decay: 6` | As above. The `usa.pop_15_34_m` casualty row is `permanent: true` because deaths do not reverse |
| Nuclear escalation | persistent, exit conditions null | `permanent: true` | Nearest implementable form; applies to every row including the global commodity and trade rows |
| All branches | conflict involvement and active conflict count | `until: resolved` | Per `resolves_after: 2` above |

### Mortality Note

Casualties (ROK −0.5%/−3.0% of population, DPRK −2%/−5%, US cohort −0.01%) are not tracked as a state variable except through the `usa.pop_15_34_m` row and the nuclear-branch `life_expectancy` depressions. Cumulative excess mortality is an output computed by comparing population trajectories to baseline.

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - {event: TAIWAN_CONFLICT,          delta: 0.006, years: 3}
    - {event: CHINESE_ECONOMIC_CRISIS,  delta: 0.004, years: 3}
  triggered_by:
    - {event: TAIWAN_CONFLICT,          delta: 0.015}
```

| Pathway | Target Event | Effect | Duration |
|---------|--------------|--------|----------|
| Major war → DPRK collapse | DPRK_REGIME_COLLAPSE | ×2.5 | 5 years |
| Nuclear use → global reconfiguration | GLOBAL_NUCLEAR_RECONFIGURATION | Window opens | Permanent |
| Regional instability → Taiwan | TAIWAN_CONFLICT | ×1.3 | 3 years |
| Economic disruption → China | CHINESE_ECONOMIC_CRISIS | ×1.2 | 3 years |
| China intervention → US-China conflict | US_CHINA_DIRECT_CONFLICT | Window opens (35%) | Immediate |

The two compiled triggers convert the multiplicative modifiers to absolute annual deltas against the target events' annual probabilities: TAIWAN_CONFLICT ×1.3 on 2.0% = +0.6%/year (`delta: 0.006`); CHINESE_ECONOMIC_CRISIS ×1.2 on 2.0% = +0.4%/year (`delta: 0.004`). The other three rows are not compiled: `DPRK_REGIME_COLLAPSE` is a fold into this event per [[events/backlog-registry]] §2 (a self-reference), and `GLOBAL_NUCLEAR_RECONFIGURATION` (→ `NPT_REGIME_COLLAPSE`) and `US_CHINA_DIRECT_CONFLICT` are registry §1 promotions whose files do not yet exist. They stay here until the round-2 events are specified.

### Reciprocal Cascade: Taiwan → Korea

Per [[events/geopolitical/taiwan-conflict]], Taiwan conflict creates ×1.5 modifier on Korean Peninsula Crisis. The mechanism works both ways:
- Taiwan conflict could enable DPRK opportunism while US is distracted
- Korean conflict could provide PRC opportunity or create US force constraints

---

## Transmission Channels

### Semiconductor Channel
South Korea (Samsung) produces ~15-20% of global advanced semiconductors. Conflict disrupts production and potentially destroys facilities. Effects compound Taiwan semiconductor risk.

### Trade Channel
Conflict disrupts major shipping lanes in Yellow Sea and Sea of Japan. South Korea is major trading economy; disruption affects global supply chains for electronics, automobiles, chemicals.

### Financial Channel
Korean Won volatility, capital flight from Asia, risk repricing across emerging markets. Japan Yen as safe-haven currency creates complex dynamics.

### Nuclear Precedent Channel
Nuclear use transforms global security architecture permanently. Breaks nuclear taboo, transforms proliferation incentives in Middle East, East Asia, and globally.

### Refugee Channel
Major war or nuclear exchange creates massive displacement. China faces refugee influx across Yalu River. Japan may face outflows. Humanitarian crisis affects regional stability.

---

## Probability Evolution

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | ~0.75% | Baseline estimate |
| 2030-2040 | ~0.85% | Potential Kim succession; DPRK nuclear arsenal matures |
| 2040-2050 | ~0.70% | Uncertain — depends on peninsula trajectory |
| 2050-2075 | Highly uncertain | Could be unified, frozen, or collapsed by then |

---

## Case Against

1. **Deterrence is stable**: Both sides have avoided war since 1953 despite numerous provocations. DPRK's nuclear arsenal may actually stabilize the situation by making regime change prohibitively costly.

2. **DPRK is rational**: Kim regime consistently calibrates provocations short of triggers for war. Nuclear weapons are for deterrence and bargaining, not use.

3. **China management works**: Beijing has leverage over DPRK and strong incentives to prevent war. Has successfully restrained DPRK during past crises.

4. **Probability may be lower**: Post-2017 diplomatic period shows crisis de-escalation is possible. Inter-Korean summits created temporary thaw.

5. **Nuclear escalation too high**: 15% conditional may overstate risk. DPRK knows nuclear use means regime annihilation. Even facing collapse, nuclear use may not improve outcomes.

**What would change estimate 2x+**:
- Kim succession crisis → higher window probability
- DPRK perceives imminent US strike → much higher conflict probability
- Simultaneous Taiwan crisis → higher (US distraction/DPRK opportunism)
- Successful denuclearization → much lower
- Formal peace treaty → much lower

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

DPRK nuclear doctrine; succession dynamics; China intervention scenarios; Seoul vulnerability modeling; impact vectors use some synthetic variables that should be replaced with observables in Level 2.

## Open Questions

- DPRK nuclear doctrine and "use before you lose" threshold
- Kim succession planning and transition risk
- China intervention decision calculus
- US force posture changes affecting deterrence
- Seoul evacuation/damage modeling for casualty estimates
- Post-conflict peninsula scenarios (unification? occupation? frozen conflict?)
- Economic integration with South Korea's semiconductor role

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/taiwan-conflict]] for related event | [[events/geopolitical/india-pakistan-military-conflict]] for comparable Type 3 specification*

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-22 | Initial Level 1 specification | Type 3 contingent event |
| 2025-12-30 | Critical review complete; noted synthetic variable issue in impact vectors (synthetic variables for Level 2 upgrade) | Task 2.4 systematic review |
| 2025-12-30 | Variance allocation: scaled loadings to Type 3 target | Task 3.11 — Factor-explained variance reduced to Type 3 target (0.45); scale factor 0.56 |
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.14. Classification, probability, loadings, branches, impacts, cascades and research tables converted; the legacy `aftermath_branches` YAML block merged into `branches:`/`impacts:` with its descriptions, factor modifications, durations, branch cascade triggers, original impact vectors and probability rationale kept as prose. Causal type 3 (not hybrid); variance 0.45 (achieved 0.455). Enums: `scale: regional` ("regional with global implications"), `reversibility: partial` ("partial to irreversible, aftermath-dependent"). Preconditions realized as `F_EAS > 1.0`, `F_GPT > 1.0`; the triggering-incident and DPRK-internal-dynamics rows have no state variable and are carried by the window draw. `resolves_after: 2` (branch-weighted duration). Durability: decay-to-floor (3 yr/0.10, 6 yr/0.20) → plain `decay`; `persistent` → `permanent: true`; "(temporary)" oil row → `decay: 1`; US casualty cohort row `permanent: true`. Factor modifications kept in prose (not a v0.1 construct). Variable substitution: `regime_stability` → `protest_intensity_annual` (sign flipped). Dropped rows: `pop_total` (derived; 4 rows), `us_china_tension` (2), `kor.institutional_quality`, `usa.alliance_west`, `nuclear_stability` — channels kept in prose. Unit conversions: `semiconductor_supply` and `global_trade_volume` fractions/percentages → index points against baseline 100; `usa.pop_15_34_m` −0.01% → −0.0045 M. Cascades: ×1.3 and ×1.2 modifiers → `delta: 0.006` and `0.004` against the targets' 2.0% annual probabilities; `DPRK_REGIME_COLLAPSE` (registry §2 fold into this event), `GLOBAL_NUCLEAR_RECONFIGURATION` (registry §1 → `NPT_REGIME_COLLAPSE`) and `US_CHINA_DIRECT_CONFLICT` (registry §1 promotion) kept in prose only. Restored from history: the pre-allocation loadings and the "sum of squared loadings 0.92" check from the 2025-12-22 revision; the 2025-12-30 variance-allocation change, which the earlier changelog did not record. The two duplicate changelog sections merged into one |
