---
title: India-Pakistan Military Conflict
type: note
permalink: events/geopolitical/india-pakistan-military-conflict
tags:
- event
- type-3
- geopolitical
- south-asia
- india
- pakistan
- nuclear
- level-1
---

# India-Pakistan Military Conflict

**Type 3 (Contingent) Event** — Military conflict between two nuclear-armed states.

---

## Description

Military conflict between India and Pakistan — airstrikes, artillery exchanges, ground operations, or naval engagement. Distinguished from baseline tensions and sub-threshold crises by actual combat operations causing military casualties. This is the discontinuity; crises that de-escalate without combat are non-events.

---

## Specification

```yaml
id: INDIA_PAKISTAN_MILITARY_CONFLICT
domain: political
scale: regional
causal_type: 3
onset: sudden
reversibility: partial
```

*Onset speed: sudden (<1yr). Reversibility: partial to irreversible (aftermath-dependent) — recorded as `partial` in YAML because the two branches that make up 90% of outcomes recover; the nuclear-escalation branch is irreversible and its impact rows are `permanent: true`.*

---

## Causal Type Specification

### Type 3 (Contingent) Event

This event has Type 3 structure: preconditions create crisis windows, and actor decisions determine whether military conflict occurs. The probability decomposition is:

- **P(crisis window)**: ~2.5% annually — acute crisis develops
- **P(military conflict | window)**: ~35% — conflict occurs given crisis
- **P(event)**: ~0.9% annually — the discontinuity probability

The 65% of crisis windows that de-escalate without combat are *non-events* — they don't appear in the simulation as discontinuities.

**Window Preconditions**:

| Condition | Threshold |
|-----------|-----------|
| F_SAS (South Asian Stress) | Elevated (sustained high tension baseline) |
| Triggering incident | Major terrorist attack, border incident, or political provocation |
| Domestic political context | Electoral pressures, nationalism spike, or weak government seeking legitimacy |

The YAML preconditions below realize this table in the expression language's subset: the F_SAS condition as `F_SAS > 1.0`, current and sustained for two years; the triggering-incident condition by its observable prerequisite, an active militant ecosystem inside Pakistan (`pak.internal_conflict_intensity >= 1`), with the incident itself being what the 2.5% window rate counts. The domestic-political-context condition has no observable in the state catalog (electoral calendars and nationalist sentiment are not state variables); it stays here as prose and is absorbed into the window rate and the 35% resolution probability.

**Historical basis for window probability (~2.5%)**:

Acute crises approaching or crossing military threshold:
- 1965 Second Kashmir War (combat)
- 1971 Bangladesh Liberation War (combat)
- 1999 Kargil War (combat)
- 2001-02 Twin Peaks Crisis (mobilization, no combat)
- 2008 Mumbai attacks (considered strikes, de-escalated)
- 2016 Uri attack and surgical strikes (limited combat)
- 2019 Pulwama/Balakot exchange (limited combat)

Pattern: ~1 acute crisis per 5-8 years. Of these, roughly one-third escalate to actual military operations. Current elevated baseline (Kashmir status change, nationalist politics, water stress) suggests above-historical crisis frequency.

**Historical basis for conflict probability given window (~35%)**:

Of the ~7 acute crises since 1965, 4-5 involved actual military operations (1965, 1971, 1999, 2016, 2019). This is higher than naive "will they or won't they" framing suggests — both sides have demonstrated willingness to use force.

---

## Probability

```yaml
probability:
  window: 0.025
  preconditions:
    all:
      - "F_SAS > 1.0"
      - "pak.internal_conflict_intensity >= 1"
    sustained:
      - expr: "F_SAS > 1.0"
        years: 2
  resolution: 0.35
  resolves_after: 2
  annual: 0.009
  range: [0.005, 0.015]
  confidence: medium
```

`resolves_after: 2` — the `until: resolved` rows (conflict involvement, active major conflicts) hold for two years per firing, counting the firing year: combat in the limited branch (55%) lasts weeks to months, but in every historical case the mobilized, militarized posture outlasted the fighting into the following year (1965 → Tashkent, January 1966; 1971 → Simla, July 1972; Kargil 1999 → LoC normalization in 2000; the 2001-02 mobilization ran ten months), and the major-war branch is specified as "months to potentially years".

| Metric | Value |
|--------|-------|
| **Annual probability** | ~0.9% |
| **Low bound** | 0.5% |
| **High bound** | 1.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~20% (at least one conflict) |

### Derivation

1. **Window probability**: 2.5% annually (1.5-4.0% range)
2. **Conflict given window**: 35% (25-45% range)
3. **Combined**: 2.5% × 35% = 0.875%, rounded to ~0.9%

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| India-Pakistan Military Conflict | ~0.9% | — |
| Taiwan Conflict (military) | ~1.0% (3% × 33%) | Similar magnitude |
| Pakistan State Failure | ~1.5% | Higher — structural pressures more sustained |
| Russia State Failure | ~1.0% | Similar — both actor-dependent |
| US Constitutional Crisis | ~0.5% | Lower — more institutional resilience |

### Key Uncertainties

- **Water stress trajectory**: Indus Waters Treaty under strain; collapse could double crisis frequency
- **Domestic politics**: Nationalist consolidation affects willingness to use force
- **Non-state actors**: Pakistan's control over militant groups affects triggering
- **Great power attention**: US/China crisis management capacity affects de-escalation probability

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 3 target (ΛΩΛᵀ)ᵢᵢ = 0.45*

```yaml
factors:
  F_SAS: 0.54   # Primary driver: regional stress conditions crises
  F_GPT: 0.17   # Great power dynamics affect crisis management
  F_CLIM: 0.13  # Water stress amplifies tensions; Indus basin vulnerability
  F_MENA: 0.07  # Pakistan's western border competing for attention
  F_FOOD: 0.07  # Food security stress overlaps with water/climate
  F_FIN: 0.07   # Economic stress amplifies domestic pressure
  F_TECH: 0.03  # Cyber capabilities matter but marginal
  F_EAS: 0.03   # China-India tensions create secondary pressure
variance: 0.45  # Type 3 target
```

F_HLTH, F_EUR, F_SSA and F_LAM carry no loading (no direct pathway).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.45 (Type 3 target); scale factor = 0.67 from original loadings. The original (pre-Task 3.11) loadings were F_SAS 0.80, F_GPT 0.25, F_CLIM 0.20, F_MENA 0.10, F_FOOD 0.10, F_FIN 0.10, F_TECH 0.05, F_EAS 0.05, with a sum of squared loadings of 0.78 (the check in use before the correlation-weighted variance target replaced it).

### Loading Rationale

Factors shock state variables (`regime_stability`, `water_stress`, `internal_conflict_intensity`) which affect both crisis window probability and conflict probability given window. F_SAS is dominant because South Asian regional dynamics are the primary driver of both stages. (`regime_stability` is a synthetic variable since replaced by observables in the state catalog; its role here is carried by `protest_intensity_annual` and `years_since_irregular_transition`.)

---

## Aftermath Branches

Once military conflict occurs, the form it takes:

```yaml
branches:
  - {id: limited_border_conflict, p: 0.55, desc: "Airstrikes, artillery, localized ground operations in Kashmir / along the LoC; weeks to months; no nuclear use"}
  - {id: major_conventional_war,  p: 0.35, desc: "Sustained conventional operations beyond Kashmir; months to years; nuclear threshold approached but not crossed"}
  - {id: nuclear_escalation,      p: 0.10, desc: "Conflict escalates to nuclear weapons use"}
```

### Branch 1: Limited Border Conflict (55%)

Limited military operations: airstrikes, artillery exchanges, localized ground operations in Kashmir or along the LoC. Similar to Kargil (1999) or Balakot (2019) but potentially more intense. Duration: weeks to months. No use of nuclear weapons.

### Branch 2: Major Conventional War (35%)

Sustained conventional military operations beyond Kashmir. Large-scale ground forces engaged, significant casualties. Duration: months to potentially years. International intervention likely to contain but not immediately stop. Nuclear threshold not crossed but repeatedly approached.

### Branch 3: Nuclear Escalation (10%)

Conflict escalates to nuclear weapons use. Most likely pathway: Pakistan first use against Indian military concentration after conventional setbacks (Pakistani doctrine emphasizes tactical nuclear weapons for battlefield use). Could also occur through accident, miscalculation, or unauthorized use.

**Aftermath probability rationale**:

- **Limited conflict (55%)**: Historical precedent (Kargil, Balakot) shows both sides can calibrate. International pressure effective at containment.
- **Major war (35%)**: Escalation pressures substantial once operations begin. Pakistan's conventional inferiority creates escalate-or-lose dynamic.
- **Nuclear (10%)**: Both sides have strong avoidance incentives. But Pakistan's tactical nuclear doctrine is explicitly for battlefield use against Indian concentrations.

### Aftermath Factor Modifications

The original specification attached post-event factor shifts to each branch. Aftermath factor modification is not part of the v0.1 schema (schema v0.2 backlog); the values are kept here.

| Branch | F_SAS | F_GPT | F_FIN | F_HLTH |
|--------|-------|-------|-------|--------|
| Limited border conflict | +0.50 | +0.25 | +0.15 | — |
| Major conventional war | +0.80 | +0.50 | +0.30 | — |
| Nuclear escalation | +1.50 | +1.20 | +0.80 | +0.40 |

---

## Impacts

```yaml
impacts:
  limited_border_conflict:
    # India
    - {var: ind.gdp_growth,                    mag: [-2.0, 1.0],   onset: immediate, decay: 3}
    - {var: ind.military_spending,             mag: [0.5, 0.2],    onset: immediate, decay: 3}
    - {var: ind.external_conflict_involvement, mag: [2, 0],        onset: immediate, until: resolved}
    - {var: ind.protest_intensity_annual,      mag: [5, 5],        onset: immediate, decay: 3}
    # Pakistan
    - {var: pak.gdp_growth,                    mag: [-4.0, 2.0],   onset: immediate, decay: 3}
    - {var: pak.military_spending,             mag: [1.0, 0.5],    onset: immediate, decay: 3}
    - {var: pak.external_conflict_involvement, mag: [2, 0],        onset: immediate, until: resolved}
    - {var: pak.protest_intensity_annual,      mag: [10, 8],       onset: immediate, decay: 3}
    - {var: pak.debt_external,                 mag: [5, 3],        onset: immediate, decay: 3}
    # Global
    - {var: oil_brent,                         mag: [8, 5],        onset: immediate, decay: 1}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}

  major_conventional_war:
    # India
    - {var: ind.gdp_growth,                    mag: [-5.0, 2.0],   onset: immediate, decay: 6}
    - {var: ind.gdp_real,                      mag: [-0.03, 0.02], onset: immediate, decay: 6}
    - {var: ind.military_spending,             mag: [1.5, 0.5],    onset: immediate, decay: 6}
    - {var: ind.external_conflict_involvement, mag: [3, 0],        onset: immediate, until: resolved}
    - {var: ind.pop_15_34_m,                   mag: [-0.24, 0.12], onset: immediate, permanent: true}
    # Pakistan
    - {var: pak.gdp_growth,                    mag: [-10.0, 4.0],  onset: immediate, decay: 6}
    - {var: pak.gdp_real,                      mag: [-0.08, 0.04], onset: immediate, decay: 6}
    - {var: pak.military_spending,             mag: [2.0, 1.0],    onset: immediate, decay: 6}
    - {var: pak.external_conflict_involvement, mag: [3, 0],        onset: immediate, until: resolved}
    - {var: pak.protest_intensity_annual,      mag: [25, 10],      onset: immediate, decay: 6}
    - {var: pak.debt_external,                 mag: [15, 5],       onset: immediate, decay: 6}
    - {var: pak.pop_15_34_m,                   mag: [-0.13, 0.06], onset: immediate, permanent: true}
    # Bangladesh
    - {var: bgd.gdp_growth,                    mag: [-1.5, 1.0],   onset: immediate, decay: 6}
    - {var: bgd.net_migration_rate,            mag: [0.5, 0.3],    onset: immediate, decay: 6}
    # Global
    - {var: oil_brent,                         mag: [15, 10],      onset: immediate, decay: 6}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}
    - {var: global_trade_volume,               mag: [-3, 2],       onset: immediate, decay: 6}

  nuclear_escalation:
    # India
    - {var: ind.gdp_real,                      mag: [-0.15, 0.10], onset: immediate, permanent: true}
    - {var: ind.life_expectancy,               mag: [-3, 2],       onset: immediate, permanent: true}
    # Pakistan
    - {var: pak.gdp_real,                      mag: [-0.25, 0.15], onset: immediate, permanent: true}
    - {var: pak.life_expectancy,               mag: [-5, 3],       onset: immediate, permanent: true}
    - {var: pak.protest_intensity_annual,      mag: [50, 20],      onset: immediate, permanent: true}
    # Global
    - {var: global_trade_volume,               mag: [-15, 8],      onset: immediate, permanent: true}
    - {var: oil_brent,                         mag: [40, 20],      onset: immediate, permanent: true}
    - {var: food_stocks_grains,                mag: [-2.8, 1.4],   onset: immediate, permanent: true}
    - {var: active_major_conflicts,            mag: [1, 0],        onset: immediate, until: resolved}
```

*Units: `gdp_real` rows are fractions of the entity's current value (−3% ± 2% for India in the major-war branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields) — `gdp_growth` and `military_spending` in percentage points, `debt_external` in points of GDP, `net_migration_rate` in points of population per year, `oil_brent` in $/barrel, `pop_15_34_m` in millions, `protest_intensity_annual` on its 0-100 index.*

### Original Impact Vectors and Re-expressed Rows

The original specification gave several rows in forms the YAML re-expresses. The originals, kept for reference:

| Branch | Original row | YAML row | Conversion |
|--------|--------------|----------|------------|
| All | `external_conflict_involvement: 3 (major limited war)` / `4 (major war)` | `[2, 0]` / `[3, 0]` | Target levels on the 0-4 UCDP scale, made additive from an assumed 2025 baseline of 1 (standing LoC hostilities) |
| Limited / Major / Nuclear | `regime_stability` −5 ± 5 (India); −10 ± 8, −25 ± 10, −50 ± 20 (Pakistan) | `protest_intensity_annual` +5 ± 5; +10 ± 8, +25 ± 10, +50 ± 20 | `regime_stability` is a synthetic variable the catalog eliminated; the observable replacement on the same 0-100 scale, sign flipped ([[methodology/reference/state-variables-country]] §4) |
| Major | `pop_15_34_m` −0.1 ± 0.05 % (India), −0.3 ± 0.15 % (Pakistan) (casualties) | −0.24 ± 0.12 M, −0.13 ± 0.06 M | Against ≈ 240 M (India) and ≈ 43 M (Pakistan) males aged 15-34 in 2025 |
| Major / Nuclear | `global_trade_volume` −3 ± 2 %, −15 ± 8 % | −3 ± 2, −15 ± 8 index points | Index 2025 = 100 |
| Nuclear | `food_stocks_grains` −10 ± 5 % | −2.8 ± 1.4 points | Read as relative to the 28% stocks-to-use baseline; if read as percentage points the row would be −10 ± 5 |
| Nuclear | `pop_total` −1.0 ± 0.5 % (India), −2.0 ± 1.0 % (Pakistan) (immediate casualties) | — | `pop_total` is a derived variable and cannot be an impact target; see Mortality Note |
| Nuclear | `institutional_quality` −0.5 ± 0.3 (India), −1.0 ± 0.5 (Pakistan) | — | Synthetic variable with no catalog observable on a comparable scale; row dropped, channel kept in prose |
| Nuclear | `nuclear_stability` −40 ± 15 (global) | — | No global nuclear-stability variable in the catalog; see Nuclear Precedent Channel |

### Durability

| Branch / rows | Original specification | YAML form |
|---------------|------------------------|-----------|
| Limited border conflict | decaying, half-life 3 years, floor 0.10 | `decay: 3` — decay-to-floor is schema v0.2 backlog; the floor is dropped |
| Major conventional war | decaying, half-life 6 years, floor 0.20 | `decay: 6` — floor dropped as above |
| Nuclear escalation | persistent, no exit conditions | `permanent: true` |
| Conflict-status rows (`external_conflict_involvement`, `active_major_conflicts`), all branches | branch duration | `until: resolved` (two years per firing; see `resolves_after`) |
| `oil_brent`, limited branch | "+8 ± 5 $/barrel (temporary)" | `decay: 1` |
| Casualty cohort rows (`pop_15_34_m`), major-war branch | branch duration (half-life 6, floor 0.20) | `permanent: true` — deaths do not reverse |

### Mortality Note

Immediate nuclear casualties (−1.0% ± 0.5% of India's population, −2.0% ± 1.0% of Pakistan's, in the original specification) are not applied to a population variable: `pop_total` is derived from the cohort stocks and the original gave no cohort split. Mortality in the nuclear branch is carried by the `life_expectancy` rows (−3 ± 2 years India, −5 ± 3 years Pakistan); cumulative excess deaths are an output computed against the no-event baseline, as in [[events/health/severe-pandemic]].

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - {event: PAKISTAN_STATE_FAILURE, delta: 0.012, years: 5,
       if: "branch == 'major_conventional_war'"}
    - {event: IRAN_REGIME_CHANGE,     delta: 0.002, years: 3}
  triggered_by:
    - {event: PAKISTAN_STATE_FAILURE, delta: 0.015}
```

| Pathway | Target Event | Effect | Duration |
|---------|--------------|--------|----------|
| Military defeat → Pakistan instability | PAKISTAN_STATE_FAILURE | ×1.8 | 5 years |
| Nuclear use → global reconfiguration | GLOBAL_NUCLEAR_RECONFIGURATION | Window opens | Permanent |
| Economic disruption | IRAN_REGIME_CHANGE | ×1.15 | 3 years |

The multipliers are converted to absolute annual deltas against the target events' current annual probabilities: ×1.8 on Pakistan State Failure's 1.5%/year is +1.2%/year (the original attached this cascade to the major-conventional-war branch, with the rationale "major military defeat or prolonged war stress could trigger state failure"); ×1.15 on Iran Regime Change's 1.2%/year is +0.2%/year. The GLOBAL_NUCLEAR_RECONFIGURATION cascade (nuclear taboo broken; proliferation incentives transform; window opens with probability 1.0 on the nuclear branch) is not in the YAML: [[events/backlog-registry]] §1 lists the ID as a promotion to `NPT_REGIME_COLLAPSE`, which has no event file yet. The `triggered_by` entry mirrors the +1.5%/year for 10 years that [[events/geopolitical/pakistan-state-failure]] declares toward this event.

---

## Transmission Channels

### Energy Market Channel
Conflict near shipping lanes raises oil risk premium. Affects global `oil_brent`, `inflation_rate`.

### Remittance Channel
Gulf-based South Asian workers affected; remittance disruption hits Pakistan, Bangladesh, India.

### Nuclear Precedent Channel
Nuclear use transforms global security architecture permanently. `nuclear_stability` shock is irreversible. (No global nuclear-stability variable exists in the state catalog; the original −40 ± 15 shock is recorded above and the systemic consequence belongs to the planned `NPT_REGIME_COLLAPSE` event.)

---

## Probability Evolution

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | ~0.9% | Baseline estimate |
| 2030-2040 | ~1.1% | Water stress increasing |
| 2040-2050 | ~1.3% | Water scarcity acute if trends continue |
| 2050-2075 | Uncertain | Depends on water management, political evolution |

---

## Case Against

1. **Nuclear deterrence is stable**: Both sides have managed crises without war since 1999. The stability-instability paradox holds.

2. **International management works**: US and China successfully de-escalated every crisis since 1998 tests.

3. **Probability may be lower**: Recent crises (2016, 2019) de-escalated quickly despite limited strikes.

4. **Nuclear escalation probability too high**: 10% conditional may overstate risk given zero nuclear use since 1945.

**What would change estimate 2x+**:
- Indus Waters Treaty collapse → higher
- India-Pakistan rapprochement → lower
- Loss of nuclear command control → much higher nuclear risk

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

Nuclear escalation pathways; water stress dynamics; Pakistan tactical nuclear doctrine; impact vector uses synthetic variables (regime_stability, institutional_quality) that should be replaced with observables in Level 2.

## Open Questions

- Water stress trajectory and Indus Waters Treaty threshold
- Pakistan tactical nuclear doctrine credibility
- China military intervention scenarios
- Non-state actor triggering probability
- US/international management capacity trends

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.13. Classification, probability, loadings, aftermath branches, impacts, cascades and research status converted; the legacy `aftermath_branches` block merged into `branches:` / `impacts:` / `cascades:`. Judgment calls: (1) `reversibility: partial` for the prose's "partial to irreversible (aftermath-dependent)", wording kept in prose; (2) preconditions realized as `F_SAS > 1.0` (current and sustained 2 years) plus `pak.internal_conflict_intensity >= 1` as the observable prerequisite of a triggering incident; the domestic-political-context condition has no catalog observable and stays in prose; (3) `resolves_after: 2` with rationale under the probability block; (4) `regime_stability` rows re-targeted to `protest_intensity_annual` (same 0-100 scale, sign flipped; the catalog's own replacement for the eliminated synthetic variable); (5) `pop_total` (derived), `institutional_quality` and `nuclear_stability` rows dropped, channels kept in prose; (6) unit conversions: `external_conflict_involvement` levels 3/4 → +2/+3 from an assumed baseline of 1; `pop_15_34_m` casualty percentages → millions against ≈240 M (India) and ≈43 M (Pakistan); `global_trade_volume` % → index points; `food_stocks_grains` −10% → −2.8 points against the 28% baseline; (7) durability: decay-to-floor (floors 0.10 / 0.20) → plain `decay: 3` / `decay: 6`; nuclear "persistent" → `permanent: true`; conflict-status rows → `until: resolved`; the "temporary" oil row → `decay: 1`; casualty cohort rows → `permanent: true`; originals in the Durability table; (8) aftermath factor modifications kept in a prose table (not in schema v0.1); (9) cascades: ×1.8 on Pakistan State Failure → `delta: 0.012` for 5 years on the major-war branch; ×1.15 on Iran Regime Change → `delta: 0.002` for 3 years; `GLOBAL_NUCLEAR_RECONFIGURATION` kept in prose only (registry promotion to `NPT_REGIME_COLLAPSE`, no file yet); `triggered_by` added from pakistan-state-failure's declared edge; (10) restored from history: the original pre-Task 3.11 loadings and their sum-of-squares figure (0.78), dropped at a126d92 |
| 2025-12-30 | Critical review complete; noted synthetic variable issue in impact vectors | Task 2.4 systematic review |
| 2025-12-21 | Initial Level 1 specification | Type 3 contingent event |

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/pakistan-state-failure]] for related event*
