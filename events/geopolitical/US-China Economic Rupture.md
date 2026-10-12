---
title: US-China Economic Rupture
type: note
permalink: events/geopolitical/us-china-economic-rupture
tags:
- event
- type-3
- geopolitical
- economic
- supply-chain
- us-china
- level-1
---

# US-China Economic Rupture

**Type 3 (Contingent) Event** — Crisis-driven escalation to comprehensive economic separation between the United States and China.

---

## Description

Crisis-driven escalation from managed competition to comprehensive economic separation — broad trade embargo, financial exclusion, investment prohibitions, and export controls across sectors. Distinguished from gradual decoupling (ongoing baseline trajectory) by acute onset and comprehensive scope. Distinguished from Taiwan Conflict by non-military trigger — this event captures economic warfare that occurs through diplomatic/political escalation without shots fired.

The discontinuity is *comprehensive rupture implemented under crisis conditions* — forcing immediate supply chain reorganization without the years of adjustment that gradual decoupling allows.

---

## Specification

```yaml
id: US_CHINA_ECONOMIC_RUPTURE
domain: political
scale: global
causal_type: 3
onset: sudden
reversibility: partial
```

*Original classification wording: Domain "Geopolitical / Economic" (`political` chosen because the measures are instruments of great power competition — see Loading Rationale — and the file sits in the geopolitical catalog); Onset Speed "Rapid (weeks to months)"; Reversibility "Partial (supply chains don't easily reconstitute)".*

---

## Causal Type Specification

### Type 3 (Contingent) Event

This event has Type 3 structure: preconditions create crisis windows, and actor decisions (policymakers in US, China, and allied capitals) determine whether comprehensive measures are implemented.

**Probability decomposition**:

- **P(crisis window)**: ~2.5% annually — acute bilateral crisis develops from non-military trigger
- **P(discontinuity | window)**: ~70% — comprehensive or managed separation occurs
- **P(event)**: ~1.75% annually — rounded to ~1.5-2.0%

The ~30% of crisis windows that de-escalate without major policy change are *non-events* — they don't appear in the simulation as discontinuities.

**Window Preconditions**:

| Condition | Threshold |
|-----------|-----------|
| F_GPT (Great Power Tension) | Elevated above baseline |
| Triggering incident | Non-military crisis of sufficient magnitude (see below) |
| Allied alignment | At least partial coordination among US, EU, Japan |

The YAML `preconditions` below realize this table in the expression language's subset: "elevated above baseline" as `F_GPT > 1.0` (the same bar [[events/geopolitical/taiwan-conflict]] uses); the *non-military* trigger as neither the US nor China being in a major external war (`external_conflict_involvement < 3` for both — a shooting war between them is TAIWAN_CONFLICT territory, not this event); and "at least partial coordination among US, EU, Japan" as positive UN-vote alignment with the US for Japan and for Germany as the EU anchor (`un_voting_alignment_us > 0`). The triggering incident itself has no state-variable proxy — it is the stochastic content of the window draw (`window: 0.025`), not a precondition.

**Triggering incident categories** (non-military):

1. **Cyber attack**: Major attributed attack on critical infrastructure (power grid, financial system, telecommunications)
2. **Espionage scandal**: Revelation of systematic penetration of defense systems, technology theft at scale
3. **South China Sea incident**: Vessel collision, standoff, or sovereignty assertion that doesn't escalate to Taiwan-level military action
4. **Retaliation spiral**: Rare earth embargo → counter-sanctions → escalation cycle
5. **Allied coordination**: US + EU + Japan + Korea reach alignment on comprehensive controls
6. **Financial trigger**: Chinese action against US financial interests (asset seizures, debt weaponization) or vice versa

**Historical basis for window probability (~2.5%)**:

Near-miss incidents and crises that could have triggered comprehensive measures:

- 2001 EP-3 incident (aircraft collision, detained crew)
- 2018-2019 trade war escalation (approached comprehensive but pulled back)
- 2020 COVID-origin tensions (political pressure for major action)
- 2023 balloon incident (triggered some measures, could have gone further)
- Ongoing: Huawei/semiconductor escalation, TikTok disputes

Pattern: Bilateral crises reaching acute phase occur roughly every 3-5 years. Most de-escalate or result in targeted (not comprehensive) measures. Window probability reflects crises severe enough to create political space for comprehensive action.

**Historical basis for discontinuity probability given window (~70%)**:

Once a crisis reaches sufficient severity, political dynamics favor action:
- Domestic pressure to "do something" is intense
- Targeted measures may be seen as insufficient
- First-mover advantages in economic warfare create pressure to act decisively
- Allied coordination, once achieved, creates momentum

The 30% non-event probability reflects:
- Economic costs create countervailing pressure
- Business lobbying against comprehensive measures
- Diplomatic off-ramps remain available
- Neither side wants to foreclose future options entirely

---

## Probability

```yaml
probability:
  window: 0.025
  preconditions:
    all:
      - "F_GPT > 1.0"
      - "usa.external_conflict_involvement < 3"
      - "chn.external_conflict_involvement < 3"
      - "jpn.un_voting_alignment_us > 0"
      - "deu.un_voting_alignment_us > 0"
  resolution: 0.70
  annual: 0.0175
  range: [0.010, 0.030]
  confidence: medium
```

No impact row uses `until: resolved` (every row decays or persists on its own clock), so the event carries no `resolves_after`.

| Metric | Value |
|--------|-------|
| **Annual probability** | ~1.75% |
| **Low bound** | 1.0% |
| **High bound** | 3.0% |
| **Confidence** | Medium |
| **25-year cumulative** | ~35% (at least one discontinuity) |

### Derivation

1. **Window probability**: 2.5% annually (2-4% range)
2. **Discontinuity given window**: 70% (60-80% range)
3. **Combined**: 2.5% × 70% = 1.75%

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Taiwan Conflict | ~2.0% | Slightly higher — military trigger more binary |
| US-China Economic Rupture | ~1.75% | — |
| Dollar Reserve Crisis | ~1.5% | Similar — different trigger, overlapping consequences |
| Chinese Economic Crisis | ~2.0% | Higher — multiple pathways |
| Global Financial Crisis | ~3.0% | Higher — more frequent, less actor-dependent |

### Key Uncertainties

- **Allied coordination trajectory**: EU/Japan/Korea alignment dramatically affects feasibility and impact
- **Domestic political dynamics**: US election cycles affect appetite for disruptive action
- **Business lobby effectiveness**: Can economic interests restrain escalation?
- **Chinese retaliation capacity**: Rare earth, pharmaceutical, manufacturing leverage
- **Financial interdependence**: Treasury holdings, cross-border investment exposure

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 3 target (ΛΩΛᵀ)ᵢᵢ = 0.45*

```yaml
factors:
  F_GPT: 0.39   # Great power tension is primary driver
  F_EAS: 0.21   # Regional dynamics contribute to tension
  F_FIN: 0.16   # Financial stress may precipitate crisis or amplify effects
  F_TECH: 0.13  # Technology competition fuels tensions
  F_EUR: 0.08   # European alignment affects scope and impact
  F_HLTH: 0.03  # Pandemic-related supply chain stress could contribute
variance: 0.45  # Type 3 target
```

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.00 | No direct pathway |
| **F_FIN** | 0.16 | Financial stress may precipitate crisis or amplify effects |
| F_HLTH | 0.03 | Pandemic-related supply chain stress could contribute |
| **F_GPT** | 0.39 | Great power tension is primary driver |
| F_FOOD | 0.00 | No direct pathway |
| F_TECH | 0.13 | Technology competition fuels tensions |
| F_EUR | 0.08 | European alignment affects scope and impact |
| F_MENA | 0.00 | No direct pathway |
| F_SAS | 0.00 | No direct pathway |
| **F_EAS** | 0.21 | Regional dynamics contribute to tension |
| F_SSA | 0.00 | No direct pathway |
| F_LAM | 0.00 | No direct pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.45 (Type 3 target); scale factor = 0.52 from original loadings. The original (pre-scaling) Level 1 loadings were F_FIN 0.30, F_HLTH 0.05, F_GPT 0.75, F_TECH 0.25, F_EUR 0.15, F_EAS 0.40 (sum of squared loadings 0.87 ✓ under the pre-variance-allocation check); the documented scaled loadings achieve 0.453 against Ω.

### Loading Rationale

F_GPT is dominant because economic rupture is fundamentally a great power competition phenomenon — the economic measures are instruments of strategic competition, not responses to economic conditions per se. F_EAS contributes because regional incidents (South China Sea, Taiwan-adjacent tensions) are primary crisis triggers. F_FIN and F_TECH reflect the financial and technological dimensions of competition. F_EUR matters because European alignment (or non-alignment) affects both the likelihood of coordinated action and the severity of global impacts.

---

## Resolutions

Once a crisis window opens *and* a discontinuity occurs (70% of windows), one of two resolutions:

**Full Rupture** (50%): Comprehensive economic separation implemented under crisis conditions. Broad trade embargo (majority of bilateral trade affected). Financial exclusion (SWIFT-adjacent measures, asset freezes, investment prohibitions). Export controls across sectors (not just semiconductors). Forced rapid supply chain reorganization.

**Managed Separation** (50%): Accelerated but targeted decoupling. Sector-specific comprehensive measures (technology, critical minerals, strategic goods). Financial restrictions short of full exclusion. Longer adjustment timeline than full rupture. Represents discontinuity from baseline trajectory but less severe than full rupture.

```yaml
resolutions:
  - id: full_rupture
    p: 0.50
    branches:
      - {id: sustained_separation,   p: 0.65, desc: "Comprehensive separation persists and deepens; two economic blocs"}
      - {id: partial_reconciliation, p: 0.35, desc: "Partial walkback after initial measures; hybrid state"}
  - id: managed_separation
    p: 0.50
    branches:
      - {id: controlled_decoupling,       p: 0.60, desc: "Accelerated but orderly sectoral decoupling over 3-5 years"}
      - {id: escalation_to_full_rupture,  p: 0.40, desc: "Managed separation proves unstable; delayed escalation to full rupture"}
```

### Resolution Probability Rationale

Default: uniform (50/50). Specified: 50/50. Confidence: n/a (using default).

No clear structural asymmetry identified at Level 1.

Arguments for full rupture dominance:
- Crisis dynamics favor decisive action
- Targeted measures may be seen as half-measures
- Domestic political pressure for strong response

Arguments for managed separation dominance:
- Economic costs create powerful resistance
- Business lobbying for carve-outs
- Allied partners may not support full measures
- Off-ramps remain attractive to both sides

These factors roughly balance. Defaulting to uniform pending Level 2 analysis of crisis decision-making dynamics.

---

## Aftermath Branches

The original specification carried per-branch `factor_modifications` (post-event shifts in the correlated factors) and decay-to-floor `duration` blocks. Neither is a schema v0.1 construct: factor modifications are kept here as prose for the schema v0.2 backlog, and the durations are realized as plain half-lives in the `impacts:` block (see Durability Specifications).

### Full Rupture Aftermath

**Sustained Separation** (0.65): Comprehensive separation persists and deepens. Two economic blocs emerge with limited cross-bloc trade. Supply chains reorganize around bloc boundaries. New trade/financial architecture develops within blocs.

**Partial Reconciliation** (0.35): After initial comprehensive measures, partial walkback occurs. Economic pain forces negotiation. Some trade/financial links restored, but not to pre-crisis levels. Hybrid state: neither full integration nor full separation.

| Branch | Factor modifications | Duration (original) |
|--------|---------------------|---------------------|
| sustained_separation | F_GPT +0.50, F_FIN +0.60, F_EAS +0.40, F_TECH +0.35, F_EUR +0.25 | decaying, half-life 8 years, floor 0.30 |
| partial_reconciliation | F_GPT +0.30, F_FIN +0.35, F_EAS +0.25 | decaying, half-life 5 years, floor 0.15 |

**Aftermath probability rationale**:

Sustained separation weighted higher (0.65) based on:
- Path dependence: once supply chains reorganize, reconstitution is costly
- Political dynamics: admitting failure of comprehensive measures is difficult
- Sunk costs in new arrangements (friendshoring investments, alternative suppliers)
- Trust destruction: even if formal measures lift, business behavior changes

Partial reconciliation possible (0.35) if:
- Economic pain exceeds political tolerance in one or both countries
- Leadership change creates political space for de-escalation
- Third-party mediation (unlikely but possible)
- Specific trigger incident is resolved or attribution is questioned

### Managed Separation Aftermath

**Controlled Decoupling** (0.60): Accelerated but orderly decoupling continues. Clear sector boundaries (technology/strategic vs. consumer goods). Supply chain adjustment proceeds over 3-5 years. Financial links partially preserved.

**Escalation to Full Rupture** (0.40): Managed separation proves unstable. Retaliation cycles, enforcement disputes, or new incidents trigger escalation to full rupture. Delay but not prevention of comprehensive separation. The original specification attached a self-referencing cascade trigger to this branch (`US_CHINA_ECONOMIC_RUPTURE`, "effectively transitions to full_rupture aftermath"); a self-trigger is not written into `cascades.triggers` — the branch instead carries sustained-separation-sized impacts directly (below).

| Branch | Factor modifications | Duration (original) |
|--------|---------------------|---------------------|
| controlled_decoupling | F_GPT +0.25, F_FIN +0.20, F_TECH +0.30 | decaying, half-life 6 years, floor 0.15 |
| escalation_to_full_rupture | F_GPT +0.45, F_FIN +0.50 | decaying, half-life 7 years, floor 0.25 |

**Aftermath probability rationale**:

Controlled decoupling weighted higher (0.60) because:
- Managed separation by definition reflects some restraint
- Economic interests that prevented full rupture continue to operate
- Sector boundaries create natural stopping points

Escalation risk significant (0.40) because:
- Managed separation creates grievances without resolution
- Enforcement disputes are likely
- New incidents can occur during adjustment period
- Domestic political pressure for "finishing the job"

---

## Impacts

### Original Impact Vectors

The Level 1 specification expressed impacts against pre-catalog variable names. They are kept here verbatim (mean, std) as the calibration record; the `impacts:` block below re-expresses them against the state catalog.

**Full rupture — sustained_separation**:

| Scope | Variable | [mean, std] | Note |
|-------|----------|-------------|------|
| global | trade_volume | [-0.25, 0.08] | |
| global | inflation | [+0.04, 0.02] | percentage points |
| global | gdp_growth | [-0.02, 0.01] | percentage points annually |
| global | supply_chain_resilience | [-0.40, 0.15] | |
| global | financial_stability | [-0.35, 0.10] | |
| united_states | consumer_prices | [+0.08, 0.03] | one-time level shift |
| united_states | manufacturing_capacity | [-0.15, 0.05] | short-term |
| united_states | gdp | [-0.03, 0.01] | |
| united_states | strategic_autonomy | [+0.30, 0.10] | |
| china | gdp | [-0.06, 0.02] | |
| china | export_revenue | [-0.25, 0.08] | |
| china | technology_access | [-0.50, 0.15] | |
| china | domestic_consumption_share | [+0.10, 0.05] | |
| european_union | gdp | [-0.02, 0.01] | |
| european_union | strategic_autonomy_pressure | [+0.40, 0.15] | |
| european_union | alliance_cohesion | [-0.20, 0.10] | differential impacts create strain |
| japan | gdp | [-0.03, 0.01] | |
| japan | supply_chain_disruption | [-0.30, 0.10] | |
| southeast_asia | manufacturing_relocation | [+0.25, 0.10] | "friendshoring" beneficiary |
| southeast_asia | gdp | [+0.01, 0.01] | net positive from relocation despite disruption |

**Full rupture — partial_reconciliation**: global trade_volume [-0.12, 0.05], inflation [+0.02, 0.01], supply_chain_resilience [-0.20, 0.08]; united_states consumer_prices [+0.04, 0.02], gdp [-0.015, 0.008]; china gdp [-0.03, 0.01], export_revenue [-0.12, 0.05].

**Managed separation — controlled_decoupling**: global trade_volume [-0.10, 0.04], inflation [+0.015, 0.008], supply_chain_resilience [-0.15, 0.06]; united_states consumer_prices [+0.03, 0.015], gdp [-0.01, 0.005], technology_leadership [+0.10, 0.05]; china gdp [-0.025, 0.01], technology_access [-0.30, 0.10].

**Managed separation — escalation_to_full_rupture**: similar to sustained_separation but delayed onset; global trade_volume [-0.22, 0.07], inflation [+0.035, 0.015].

### Mapping to the State Catalog

- **trade_volume** → `global_trade_volume` (index, 2025 = 100): −25% of the index = −25 points.
- **inflation** (global, pp) → `*.inflation_rate` (+4 pp, all 40 countries). **consumer_prices** (US, one-time +8% level shift) → a `usa.inflation_rate` row of +4 pp with a 1-year half-life, carried as the *increment over* the wildcard row so the US total in the firing year is the prose's +8 pp.
- **gdp_growth** (global, −2 pp annually) → `*.gdp_real` −2% as the base exposure for every country; the named-entity GDP rows are then *increments over that base* so each entity's net matches the prose: US −3%, China −6%, Japan −3%, EU −2% (member states at base; `eu_other` explicit because aggregates are outside the wildcard), Southeast Asia +1%. The Differential Country Impacts section (below) sets the high-exposure entities (Australia, South Korea, Taiwan, Vietnam, Germany, Netherlands) at ~1.75× base (net −3.5%) and the friendshoring recipients (India, Mexico, Indonesia) at net +1%.
- **supply_chain_resilience** (−0.40) → `container_freight_index` +40 points (forced supplier switching and rerouting priced through freight) plus a `rare_earths_index` row (+80 points) for the Critical rare-earth retaliation vector documented below; the 2010-11 embargo on Japan moved rare-earth prices several-fold, so +80 is conservative.
- **financial_stability** (−0.35) → `global_credit_spread` +150 bps (between the +120 bps 2025 baseline doubling and the Taiwan-limited +200 bps row).
- **manufacturing_capacity** (US, −15% short-term) → `usa.gdp_share_industry` −2.5 points (15% of an ~18% industry share), 2-year half-life.
- **export_revenue** (China, −25%) → `chn.trade_openness` −8 points of GDP (a quarter of exports at ~19% of GDP, plus the matching import cut under an embargo, against ~37% openness).
- **technology_access** (China, −0.50) → `chn.sanctions_level` +50 (from today's targeted/sectoral ~20 toward "comprehensive sanctions with carve-outs" at 75 on the catalog's scale).
- **manufacturing_relocation** (SE Asia, +0.25) → `fdi_net` +1.5% of GDP for `southeast_asia_other`, Vietnam, Indonesia, India and Mexico, ramping over 2 years.
- **Not written as rows**: the catalog names `usa.trade_share_china`, `chn.trade_share_west`, `swift_share` and `cips_share` as trade-rupture transmission variables ([[methodology/reference/State Variables - Global]] §Global → Country Transmission), but this specification never quantified them; magnitudes for them are Level 2 authoring, not migration.
- **Dropped (no catalog counterpart; channel stays in prose)**: united_states strategic_autonomy, china domestic_consumption_share, european_union strategic_autonomy_pressure and alliance_cohesion (the alliance-strain mechanism is carried by the EU_FRAGMENTATION cascade), japan supply_chain_disruption (covered by the global freight row), united_states technology_leadership.

```yaml
impacts:
  full_rupture.sustained_separation:
    # Global
    - {var: global_trade_volume,           mag: [-25, 8],        onset: immediate, decay: 8}
    - {var: container_freight_index,       mag: [40, 15],        onset: immediate, decay: 3}
    - {var: rare_earths_index,             mag: [80, 40],        onset: immediate, decay: 3}
    - {var: global_credit_spread,          mag: [150, 60],       onset: immediate, decay: 2}
    - {var: "*.inflation_rate",            mag: [4, 2],          onset: immediate, decay: 2}
    - {var: "*.gdp_real",                  mag: [-0.02, 0.01],   onset: immediate, decay: 8}

    # United States (increments over the wildcard rows)
    - {var: usa.inflation_rate,            mag: [4, 1.5],        onset: immediate, decay: 1}
    - {var: usa.gdp_share_industry,        mag: [-2.5, 1.0],     onset: immediate, decay: 2}
    - {var: usa.gdp_real,                  mag: [-0.01, 0.005],  onset: immediate, decay: 8}

    # China (increments over the wildcard rows)
    - {var: chn.gdp_real,                  mag: [-0.04, 0.015],  onset: immediate, decay: 8}
    - {var: chn.trade_openness,            mag: [-8, 3],         onset: immediate, decay: 8}
    - {var: chn.sanctions_level,           mag: [50, 15],        onset: immediate, decay: 8}

    # Europe and Japan
    - {var: eu_other.gdp_real,             mag: [-0.02, 0.01],   onset: immediate, decay: 8}
    - {var: deu.gdp_real,                  mag: [-0.015, 0.008], onset: immediate, decay: 8}
    - {var: nld.gdp_real,                  mag: [-0.015, 0.008], onset: immediate, decay: 8}
    - {var: jpn.gdp_real,                  mag: [-0.01, 0.005],  onset: immediate, decay: 8}

    # Other high-exposure economies
    - {var: aus.gdp_real,                  mag: [-0.015, 0.008], onset: immediate, decay: 8}
    - {var: kor.gdp_real,                  mag: [-0.015, 0.008], onset: immediate, decay: 8}
    - {var: twn.gdp_real,                  mag: [-0.015, 0.008], onset: immediate, decay: 8}
    - {var: vnm.gdp_real,                  mag: [-0.015, 0.008], onset: immediate, decay: 8}

    # Friendshoring recipients (net +1% after the wildcard base)
    - {var: southeast_asia_other.gdp_real, mag: [0.01, 0.01],    onset: {gradual: 2}, decay: 8}
    - {var: ind.gdp_real,                  mag: [0.03, 0.015],   onset: {gradual: 2}, decay: 8}
    - {var: mex.gdp_real,                  mag: [0.03, 0.015],   onset: {gradual: 2}, decay: 8}
    - {var: idn.gdp_real,                  mag: [0.03, 0.015],   onset: {gradual: 2}, decay: 8}
    - {var: southeast_asia_other.fdi_net,  mag: [1.5, 0.8],      onset: {gradual: 2}, decay: 8}
    - {var: vnm.fdi_net,                   mag: [1.5, 0.8],      onset: {gradual: 2}, decay: 8}
    - {var: idn.fdi_net,                   mag: [1.5, 0.8],      onset: {gradual: 2}, decay: 8}
    - {var: ind.fdi_net,                   mag: [1.5, 0.8],      onset: {gradual: 2}, decay: 8}
    - {var: mex.fdi_net,                   mag: [1.5, 0.8],      onset: {gradual: 2}, decay: 8}

  full_rupture.partial_reconciliation:
    inherit: full_rupture.sustained_separation
    scale: 0.5

  managed_separation.controlled_decoupling:
    inherit: full_rupture.sustained_separation
    scale: 0.4

  managed_separation.escalation_to_full_rupture:
    inherit: full_rupture.sustained_separation
    scale: 0.9
```

*Units: `gdp_real` rows are fractions of the entity's current value (the wildcard base is −2% ± 1%); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). The three inheriting branches scale the sustained-separation list: 0.5 reproduces the partial-reconciliation magnitudes (trade −12.5 vs −12, inflation +2, US prices +4, US GDP −1.5%, China GDP −3%, exports −12.5 vs −12), 0.4 the controlled-decoupling ones (trade −10, inflation +1.6 vs +1.5, US GDP −1.2% vs −1%, China GDP −2.4% vs −2.5%), and 0.9 the escalation ones (trade −22.5 vs −22, inflation +3.6 vs +3.5). Inheritance cannot change onset or half-life, so the escalation branch's "delayed onset" and the branch-specific half-lives (5, 6, 7 years) are not carried — see Durability Specifications.*

### Durability Specifications

| Impact | Original durability | YAML realization | Rationale |
|--------|--------------------|------------------|-----------|
| All sustained_separation rows | decaying, half-life 8, floor 0.30 | `decay: 8` | Decay-to-floor is schema v0.2 backlog; plain half-life is the nearest v0.1 form. The 30% floor (bloc structure that never reconstitutes) is lost |
| partial_reconciliation rows | decaying, half-life 5, floor 0.15 | inherited `decay: 8` | Inheritance keeps the parent's half-life |
| controlled_decoupling rows | decaying, half-life 6, floor 0.15 | inherited `decay: 8` | As above |
| escalation_to_full_rupture rows | decaying, half-life 7, floor 0.25; delayed onset | inherited `decay: 8`, immediate | As above; delayed onset not carried |
| Credit spread, freight, rare earths, inflation | (branch duration) | `decay: 2` / `3` / `3` / `2` | These catalog variables are documented as mean-reverting within 1-3 years; an 8-year half-life on a spread or a price index would contradict their dynamics |
| US consumer prices | one-time level shift | `decay: 1` | Level shift, not persistent inflation |
| US manufacturing capacity | short-term | `decay: 2` | As stated in the original row |

### Supply Chain Impact Detail

#### Critical Categories

| Category | US Import Dependence | Substitution Timeline | Acute Impact |
|----------|---------------------|----------------------|--------------|
| Consumer electronics | ~70% | 2-4 years | High |
| Pharmaceutical APIs | ~80% | 3-5 years | Critical |
| Rare earth elements | ~80% | 5-10 years | Critical |
| Industrial machinery | ~25% | 1-2 years | Moderate |
| Textiles/apparel | ~35% | 1-2 years | Low-Moderate |
| Furniture/household | ~50% | 1-2 years | Moderate |
| Auto parts | ~15% | 1-2 years | Moderate |
| Solar panels | ~80% | 3-5 years | High |
| Batteries/EVs | ~70% | 3-5 years | High |

#### Chinese Retaliation Vectors

| Vector | US Vulnerability | Impact Severity |
|--------|-----------------|-----------------|
| Rare earth export ban | High (defense, electronics, EVs) | Critical |
| Pharmaceutical API cutoff | High (generic drugs, antibiotics) | Critical |
| Treasury holdings sale | Moderate (market disruption, rates) | High |
| Manufacturing exit costs | High (Apple, auto supply chains) | High |
| Critical minerals | High (lithium, cobalt processing) | Critical |

#### Differential Country Impacts

**Exposure variable**: bilateral_trade_china_share (the catalog's `trade_share_china`)

**High exposure (GDP impact 1.5-2x base)**:
- Australia, South Korea, Taiwan, Vietnam, Malaysia
- Germany, Netherlands (European manufacturing hubs)

**Moderate exposure (GDP impact 1x base)**:
- Japan, United Kingdom, France, Canada

**Low exposure / beneficiaries**:
- India, Mexico, Indonesia (friendshoring recipients)
- Some ASEAN (depends on bloc alignment)

Malaysia is not a state-catalog entity (it sits inside `southeast_asia_other`, which the prose nets as a beneficiary), so it carries no explicit row.

### Transmission Channels

#### Trade Channel
**Mechanism**: Direct interruption of goods flows; tariffs/embargoes make bilateral trade uneconomic
**Affected regions**: US, China, East Asia, Europe (through supply chains)
**Affected variables**: trade_volume, consumer_prices, manufacturing_output, gdp

#### Financial Channel
**Mechanism**: Asset freezes, payment system exclusion, investment prohibitions, currency volatility
**Affected regions**: Global (through financial linkages)
**Affected variables**: financial_stability, exchange_rates, capital_flows, credit_availability

#### Supply Chain Channel
**Mechanism**: Intermediate goods shortages, production bottlenecks, forced supplier switching
**Affected regions**: Global manufacturing (autos, electronics, machinery)
**Affected variables**: manufacturing_output, supply_chain_resilience, inventory_costs

#### Technology Channel
**Mechanism**: Export controls, IP restrictions, talent mobility constraints
**Affected regions**: US, China, technology-intensive economies
**Affected variables**: technology_access, innovation_capacity, productivity_growth

#### Signaling Channel
**Mechanism**: Demonstration effects on other relationships; precedent for economic warfare
**Affected regions**: Global (affects all trade relationships)
**Affected variables**: trade_policy_uncertainty, alliance_dynamics, investment_decisions

---

## Cascades

```yaml
cascades:
  triggers:
    - {event: CHINESE_ECONOMIC_CRISIS,  delta: 0.010,  years: 5}
    - {event: DOLLAR_RESERVE_CRISIS,    delta: 0.0045, years: 10}
    - {event: GLOBAL_FINANCIAL_CRISIS,  delta: 0.015,  years: 3}
    - {event: EU_FRAGMENTATION,         delta: 0.0008, years: 5}
  triggered_by:
    - {event: TAIWAN_CONFLICT, delta: -0.014}
```

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Financial stress | CHINESE_ECONOMIC_CRISIS | ×1.5 | 5 years | Export collapse, capital flight, confidence shock |
| De-dollarization pressure | DOLLAR_RESERVE_CRISIS | ×1.3 | 10 years | Accelerated reserve diversification, alternative payment systems |
| Systemic financial risk | GLOBAL_FINANCIAL_CRISIS | +1.5% | 3 years | Asset freezes, counterparty uncertainty, trade finance collapse |
| Alliance strain | EU_FRAGMENTATION | ×1.2 | 5 years | Differential impacts, strategic autonomy debates |
| Opportunistic action | TAIWAN_CONFLICT | Note | — | Complex: may increase (use it or lose it) or decrease (economic costs) |

The multiplicative changes are converted to the schema's absolute annual deltas against each target's documented annual probability: CHINESE_ECONOMIC_CRISIS ~2.0% × 0.5 = +1.0% (matching the +1.0% that event's own triggered-by table records for this event under its alias `US_CHINA_TRADE_WAR`); DOLLAR_RESERVE_CRISIS 1.5% × 0.3 = +0.45%; EU_FRAGMENTATION 0.4% × 0.2 = +0.08%. The TAIWAN_CONFLICT row is a note, not a trigger (see Interaction with Taiwan Conflict: net effect uncertain, default to no modification), so it is not in `triggers:`. The `triggered_by` entry records the Taiwan-first suppression described below: window 2.5% → ~0.5% is annual 1.75% → 0.35%, a −1.4 pp change.

### Impact Chains

**Chain 1**: Rupture → Pharmaceutical shortage → Health system stress → F_HLTH elevation → Pandemic vulnerability

**Chain 2**: Rupture → Rare earth shortage → Defense production constraints → Alliance credibility questions → F_GPT elevation

**Chain 3**: Rupture → Inflation shock → Central bank tightening → Financial stress → GLOBAL_FINANCIAL_CRISIS probability increase

---

## Interaction with Taiwan Conflict

**If Taiwan Conflict occurs first**: Economic rupture is likely subsumed — the military conflict triggers economic separation as a consequence, and the economic impacts are captured in Taiwan Conflict aftermath. In simulation terms, this event's window probability should drop significantly (to ~0.5%) if Taiwan Conflict has occurred in prior 5 years.

**If Economic Rupture occurs first**: Does not preclude Taiwan Conflict but may affect its probability:
- Argument for increase: Economic separation removes interdependence constraints on military action
- Argument for decrease: Economic costs already imposed; less to lose from military restraint
- Net effect: Uncertain; default to no modification pending Level 2 analysis

**Modeling note**: These events are partially substitutable in their economic consequences but have different triggers and different probability structures. Both belong in the catalog.

---

## Case Against

### 1. Gradual decoupling makes acute rupture less likely

**Argument**: Ongoing decoupling (reshoring, friendshoring, diversification) reduces the stakes of any single crisis. By the time a triggering incident occurs, supply chains may already be sufficiently diversified that comprehensive measures are unnecessary or less costly.

**Counter**: Gradual decoupling is proceeding slowly and faces business resistance. As of 2025, China remains deeply embedded in global supply chains. A crisis in the next 5-10 years would still cause severe disruption. Moreover, partial decoupling may create false confidence that comprehensive measures are manageable.

### 2. Mutual economic destruction prevents escalation

**Argument**: Both sides understand that comprehensive rupture would be economically devastating. Rational actors will pull back from the brink, as they have in previous crises (2018-2019 trade war, 2020 COVID tensions).

**Counter**: Previous crises occurred before the most recent escalation in strategic competition. Semiconductor export controls, entity lists, and investment screening represent a new baseline. The "rationality" argument assumes economic interests dominate, but nationalist/security concerns may override economic logic, especially in crisis conditions.

### 3. Allied coordination is too difficult

**Argument**: Full rupture requires coordination among US, EU, Japan, Korea. European and Asian allies have stronger economic ties to China and weaker security motivations. They will defect from comprehensive measures, limiting scope to managed separation at most.

**Counter**: Allied coordination has improved significantly (AUKUS, semiconductor export controls, critical minerals agreements). A sufficiently severe trigger (major cyber attack, direct provocation) could generate aligned response. Moreover, US secondary sanctions can force alignment even without voluntary cooperation.

### What would change estimate 2x+

| Change | Direction | Magnitude |
|--------|-----------|-----------|
| Major attributed cyber attack on US infrastructure | ↑ | +100% window probability |
| EU-US comprehensive trade/tech alignment | ↑ | +50% probability given window |
| Chinese rare earth preemptive embargo | ↑ | +75% window probability |
| Successful US-China crisis management framework | ↓ | -40% probability given window |
| Rapid supply chain diversification (5+ years) | ↓ | -30% impact severity |
| Chinese financial/Treasury retaliation threat credible | ↓ | -25% probability given window |

### Probability Evolution

As a Type 3 event, probability evolution depends on structural factors affecting both window probability and discontinuity-given-window probability:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | 1.5-2.0% | Elevated baseline; semiconductor controls expanding; supply chains still deeply integrated |
| 2030-2040 | 1.2-1.8% | Gradual decoupling reduces stakes; but strategic competition intensifies |
| 2040-2050 | 0.8-1.5% | More diversified supply chains reduce both likelihood and impact |
| 2050-2075 | 0.5-1.2% | Depends heavily on whether bloc structure or integration prevails |

**Key inflection points**:
- Allied alignment crystallization (EU, Japan, Korea) affects scope and feasibility
- Supply chain diversification progress affects both stakes and vulnerability
- Taiwan status affects whether economic or military pathway dominates

---

## Sensitivity Analysis Notes

Key uncertainties for Phase 3 sensitivity testing:

| Parameter | Range to Test | Why It Matters |
|-----------|---------------|----------------|
| Window probability | 0.015 - 0.04 | Drives expected timing |
| Discontinuity given window | 0.55 - 0.85 | Determines how many crises produce lasting change |
| Full vs. managed split | 0.35/0.65 to 0.65/0.35 | Major difference in severity |
| Supply chain adjustment time | 2-5 years vs. 5-10 years | Affects duration of acute impacts |
| Chinese retaliation effectiveness | 0.3 - 0.7 | Rare earth, pharma, financial vectors |
| Allied coordination | 0.4 - 0.8 | Affects scope and enforceability |

---

## Research Upgrade Path

**Level 2 (4-8 hours)**:
- Detailed supply chain mapping for critical categories
- Chinese retaliation capacity assessment (rare earths, pharma, financial)
- Allied coordination precedents and constraints
- Historical economic warfare cases (Russia sanctions, Iran sanctions) for impact calibration
- Business lobby effectiveness in crisis conditions

**Level 3 (20+ hours)**:
- Expert elicitation on supply chain adjustment timelines
- Pharmaceutical API dependency deep-dive
- Rare earth substitution and alternative source analysis
- Financial system stress testing for asset freeze scenarios
- Sector-by-sector impact modeling

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

**Upgrade rationale**: Supply chain adjustment timelines; pharmaceutical/rare earth vulnerability; Chinese retaliation capacity

## Sources

- Level 1 specification from prior knowledge
- Calibration against existing catalog events (Taiwan Conflict, Dollar Reserve Crisis, Chinese Economic Crisis)

## Open Questions

- Pharmaceutical API substitution timeline and feasibility
- Rare earth alternative sources and processing capacity
- Chinese Treasury holdings as leverage: credible threat or mutual destruction?
- Allied coordination dynamics under crisis pressure
- Supply chain adjustment costs and timelines by sector
- Interaction effects with Taiwan Conflict probability
- Financial system resilience to asset freeze scenarios
- Secondary sanctions effectiveness and allied response

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/taiwan-conflict]] for comparable Type 3 specification*

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.15. Classification, probability, factors, resolutions/branches, impacts, cascades and research tables converted; legacy `resolutions`/`aftermath_branches` blocks merged (their `probability` → `p`, aftermath branches nested under resolutions, `factor_modifications` and decay-to-floor `duration` kept as prose for schema v0.2). **Judgment calls**: domain "Geopolitical / Economic" → `political` (file's catalog placement; loading rationale). Preconditions realized as `F_GPT > 1.0`, `usa`/`chn.external_conflict_involvement < 3` (non-military trigger), `jpn`/`deu.un_voting_alignment_us > 0` (allied alignment); the triggering incident lives in the window draw. No `until: resolved` rows, so no `resolves_after`. Durability: every decay-to-floor duration became a plain `decay`; inheriting branches keep the parent's 8-year half-life and immediate onset (prose keeps 5/6/7-year half-lives and the escalation branch's delayed onset); mean-reverting price/spread rows given 1-3-year half-lives. Unit conversions: trade_volume −25% → −25 index points; financial_stability −0.35 → +150 bps credit spread; US consumer_prices +8% → +4 pp `inflation_rate` increment over the +4 pp wildcard; global gdp_growth −2 pp → `*.gdp_real` −2% base with named-entity rows as increments (US −3%, China −6%, Japan −3%, EU −2%, high-exposure −3.5%, friendshoring recipients +1%); manufacturing_capacity −15% → `gdp_share_industry` −2.5 points; export_revenue −25% → `trade_openness` −8 points; technology_access −0.50 → `sanctions_level` +50; supply_chain_resilience −0.40 → `container_freight_index` +40; manufacturing_relocation → `fdi_net` +1.5% of GDP. `rare_earths_index` row from the retaliation-vector table; the catalog's unquantified trade-rupture variables (`trade_share_china`, `trade_share_west`, `swift_share`, `cips_share`) are noted, not written. Dropped (no catalog variable; channel in prose): strategic_autonomy, domestic_consumption_share, strategic_autonomy_pressure, alliance_cohesion, japan supply_chain_disruption, technology_leadership. Cascades: ×1.5/×1.3/×1.2 multipliers converted to absolute deltas against target base rates (+0.010, +0.0045, +0.0008); TAIWAN_CONFLICT "Note" row and the escalation branch's self-trigger kept in prose; Taiwan-first suppression recorded as a `triggered_by` delta of −0.014. **Restored from history**: the original pre-scaling loadings (F_FIN 0.30, F_HLTH 0.05, F_GPT 0.75, F_TECH 0.25, F_EUR 0.15, F_EAS 0.40; sum of squares 0.87) condensed to "scale factor = 0.52" at the 2025-12-30 variance allocation |
| 2025-12-30 | Critical review complete; added changelog | Task 2.4 systematic review |
| 2025-12-22 | Initial Level 1 specification | Type 3 contingent event |
