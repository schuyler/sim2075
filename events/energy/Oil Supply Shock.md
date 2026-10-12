---
title: Oil Supply Shock
type: note
permalink: events/energy/oil-supply-shock
tags:
- event
- type-1
- energy
- oil
- supply-shock
- level-1
---

# Oil Supply Shock

**Type 1 (Stochastic) Event** — Sustained major disruption to global oil supply forcing structural adaptation in energy systems, trade patterns, and geopolitical alignments.

---

## Event Classification

```yaml
id: OIL_SUPPLY_SHOCK
domain: economic
scale: global
causal_type: 1
onset: sudden
reversibility: partial
```

*Domain: Economic / Geopolitical (recorded as `economic` in YAML: the schema enum admits one value, and the discontinuity is an economic one — structural adaptation of energy systems and trade — even though its triggers are geopolitical). Onset speed: sudden (weeks). Reversibility: partial.*

## Description

Sustained major disruption (>15% of global supply for 6+ months) to oil supply from conflict, infrastructure destruction, or producer collapse—forcing structural adaptation rather than temporary market adjustment. Distinguished from routine price volatility by duration and magnitude sufficient to trigger permanent changes in energy infrastructure, trade relationships, and efficiency investments.

The discontinuity is the *structural adaptation forced by sustained shortage*, not the price spike itself. Price spikes that resolve within months without forcing structural change are sub-threshold stress, not discontinuities.

---

## Causal Type Specification

### Type 1 (Stochastic) Event

This event has Type 1 structure: triggering events (wars, infrastructure attacks, regime collapses) have stochastic timing with limited predictability. While geopolitical tension creates conditions for disruption, the timing and specific trigger remain fundamentally unpredictable.

**Base rate derivation**:

Historical discontinuity-level supply shocks since 1970:

| Event | Year | Supply Impact | Duration | Structural Change |
|-------|------|---------------|----------|-------------------|
| 1973 OPEC Embargo | 1973 | ~9% of global supply | 5 months | **Yes** — IEA formation, efficiency standards, strategic reserves, producer-consumer restructuring |
| 1979 Iranian Revolution | 1979 | ~7% of global supply | 12+ months | **Yes** — accelerated efficiency, OPEC cohesion undermined, non-OPEC development |
| 1990 Gulf War | 1990 | ~9% (Iraq+Kuwait) | 6 months | **No** — Saudi spare capacity compensated; temporary spike |
| 2022 Russia-Ukraine | 2022 | ~5% (European gas, partial oil) | Ongoing | **Partial** — European infrastructure restructuring; global oil less affected |

Genuine discontinuities: 2 clear cases (1973, 1979) + 1 partial (2022) in 55 years.

**Raw base rate**: ~2-3 events / 55 years ≈ **3.6-5.5% per year**

**Condition adjustments**:

| Factor | Direction | Magnitude | Rationale |
|--------|-----------|-----------|-----------|
| Supply diversification | ↓ | -25% | Shale, non-OPEC growth reduce single-point-of-failure risk |
| SPR/IEA coordination | ↓ | -15% | 90-day reserves provide buffer against short disruptions |
| Demand elasticity improvement | ↓ | -10% | Economy less oil-intensive; some substitution possible |
| Geopolitical tension elevation | ↑ | +20% | US-China competition, Middle East instability, Russia confrontation |
| Infrastructure concentration | ↑ | +15% | Strait of Hormuz still handles 20% of global supply |

**Net adjustment**: Approximately -15% from raw base rate.

**Adjusted estimate**: 3.6% × 0.85 ≈ **3.0%**, or conservatively **2.0-2.5%** given increased system resilience.

---

## Probability

```yaml
probability:
  annual: 0.025
  range: [0.015, 0.040]
  confidence: medium
```

| Metric | Value |
|--------|-------|
| **Annual probability** | ~2.5% |
| **Low bound** | 1.5% |
| **High bound** | 4.0% |
| **Confidence** | Medium |
| **25-year cumulative** | ~47% (at least one discontinuity) |

### Derivation

1. **Reference class**: Major supply disruptions forcing structural adaptation (1973, 1979 as clear cases)
2. **Historical frequency**: ~2 discontinuities in 55 years = 3.6%/year raw rate
3. **Condition adjustments**: Net -15% for increased resilience, partially offset by elevated tension
4. **Final estimate**: 2.5% (range 1.5-4.0%)

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Global Financial Crisis | ~3.0% | Higher — more pathways, less concentrated |
| **Oil Supply Shock** | ~2.5% | — |
| Severe Pandemic | ~2.0% | Similar — both Type 1 with historical base rates |
| Taiwan Conflict | ~2.0% | Similar — but Taiwan more geographically concentrated |
| Dollar Reserve Crisis | ~1.5% | Lower — requires more coordinated action |

### Key Uncertainties

- **Strait of Hormuz vulnerability**: Single chokepoint for 20% of global supply
- **Saudi internal stability**: Production concentration in one regime
- **Shale response capacity**: How quickly can US production scale?
- **Chinese SPR**: Size and willingness to deploy unknown
- **Demand destruction speed**: How fast can economies adjust?

---

## Disruption Pathways

Multiple stochastic triggers can produce discontinuity-level effects:

### Strait of Hormuz Closure

| Attribute | Value |
|-----------|-------|
| **Supply at risk** | ~20% of global oil, ~25% of LNG |
| **Trigger scenarios** | Iran-US conflict, Iran-Saudi conflict, Iranian domestic instability |
| **Duration if occurs** | 3-12 months (mine clearing, infrastructure repair) |
| **Substitution options** | Limited — pipelines exist but insufficient capacity |

### Major Producer Collapse

| Producer | Supply Share | Trigger Scenarios |
|----------|--------------|-------------------|
| Saudi Arabia | ~12% | Regime instability, Houthi infrastructure attacks at scale |
| Russia | ~10% | State failure, comprehensive sanctions, infrastructure degradation |
| Iraq | ~5% | Renewed civil conflict, Iran-US spillover |
| UAE/Kuwait | ~5% combined | Regional conflict spillover |

### Multi-Producer Disruption

Regional conflict spreading across multiple producers simultaneously — lower probability but higher severity. Examples:
- Iran-Saudi war affecting Gulf production broadly
- Wider Middle East conflict drawing in multiple producers
- Cascade of producer state failures

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 1 target (ΛΩΛᵀ)ᵢᵢ = 0.75*

```yaml
factors:
  F_MENA: 0.46  # Primary production region; regional instability directly threatens supply
  F_GPT: 0.34   # Great power tension increases conflict probability in oil-producing regions
  F_FIN: 0.29   # Financial stress correlates with geopolitical risk-taking; oil shocks stress financial systems
  F_EUR: 0.13   # European energy dependence creates exposure; Russia-Europe dynamics
  F_EAS: 0.08   # Major demand region; supply competition dynamics
  F_LAM: 0.08   # Venezuela instability; regional production
  F_FOOD: 0.08  # Oil-intensive agriculture; food price correlation with energy prices
  F_SSA: 0.04   # Minor production (Nigeria, Angola)
variance: 0.75  # Type 1 target
```

| Factor | Loading | Original loading (pre-Task 3.11) | Rationale |
|--------|---------|----------------------------------|-----------|
| **F_MENA** | 0.46 | 0.55 | Primary production region; regional instability directly threatens supply |
| **F_GPT** | 0.34 | 0.40 | Great power tension increases conflict probability in oil-producing regions |
| **F_FIN** | 0.29 | 0.35 | Financial stress correlates with geopolitical risk-taking; oil shocks stress financial systems |
| F_EUR | 0.13 | 0.15 | European energy dependence creates exposure; Russia-Europe dynamics |
| F_EAS | 0.08 | 0.10 | Major demand region; supply competition dynamics |
| F_LAM | 0.08 | 0.10 | Venezuela instability; regional production |
| F_FOOD | 0.08 | 0.10 | Oil-intensive agriculture; food price correlation with energy prices |
| F_SSA | 0.04 | 0.05 | Minor production (Nigeria, Angola) |
| F_CLIM | 0.00 | 0.00 | No direct pathway |
| F_HLTH | 0.00 | 0.00 | No direct pathway |
| F_SAS | 0.00 | 0.00 | No direct pathway |
| F_TECH | 0.00 | 0.00 | No direct pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.75 (Type 1 target); scale factor = 0.84 from original loadings. The scaled loadings achieve 0.748 against the catalog's Ω.

**Sum of squared loadings (original specification, before variance scaling)**: 0.55² + 0.40² + 0.35² + 0.15² + 0.10² + 0.10² + 0.10² + 0.05² = 0.30 + 0.16 + 0.12 + 0.02 + 0.01 + 0.01 + 0.01 + 0.00 = **0.63** ✓ — the original loadings' uncorrelated sum; with factor correlations the original loadings would have over-explained the event's variance (1.07 against Ω), which is why Task 3.11 scaled them by 0.84.

### Loading Rationale

F_MENA is dominant (0.55) because the majority of supply concentration and chokepoint risk is in the Middle East — Saudi Arabia, Iraq, Iran, UAE, Kuwait, and the Strait of Hormuz are all MENA. F_GPT is secondary (0.40) because great power competition increases the probability of conflicts that disrupt supply (US-Iran, US-Russia, regional proxy conflicts). F_FIN (0.35) captures the correlation between financial stress and geopolitical risk-taking, plus the financial system's vulnerability to oil shocks. (The figures in this paragraph are the original loadings; the YAML carries the 0.84-scaled values.)

The interpretation for Type 1 events: factors affect the *clustering* of events, not the triggering. When F_MENA and F_GPT are elevated, multiple supply-threatening events become more likely to occur in proximity.

---

## Resolutions

For Type 1 events, resolutions represent different manifestations of the discontinuity when it occurs. Not whether it occurs, but what form it takes. Each resolution has two aftermath branches (see [[methodology/reference/aftermath-branches]]); the branch probabilities below are conditional on the resolution.

```yaml
resolutions:
  - id: accelerated_transition
    p: 0.40
    branches:
      - {id: successful_transition, p: 0.60, desc: "Shock catalyzes orderly acceleration of the energy transition"}
      - {id: chaotic_transition,    p: 0.40, desc: "Transition accelerates but disorderly: volatile investment, grid stress, backlash"}
  - id: producer_restructuring
    p: 0.35
    branches:
      - {id: new_equilibrium,    p: 0.55, desc: "New producer-consumer relationships stabilize; non-OPEC gains share"}
      - {id: fragmented_markets, p: 0.45, desc: "Energy markets fragment into competing blocs; pricing diverges"}
  - id: extended_crisis
    p: 0.25
    branches:
      - {id: managed_recovery,   p: 0.50, desc: "18-24 months of crisis, then supply recovers and demand adjusts"}
      - {id: cascading_failures, p: 0.50, desc: "Crisis triggers state failures and financial contagion; depression in worst cases"}
```

### Accelerated Transition (40%)

Supply shock triggers permanent demand destruction and accelerated energy transition. Efficiency investments, renewables deployment, and electrification accelerate. Oil demand never returns to pre-shock trajectory.

### Producer Restructuring (35%)

Geopolitical realignment of energy relationships. New suppliers emerge or gain prominence. Trade patterns restructure around new partnerships. OPEC cohesion affected. Producer-consumer power balance shifts.

### Extended Crisis (25%)

Prolonged shortage without clear resolution. Rationing, economic contraction, political instability in dependent economies. Eventually resolves through combination of demand destruction and supply recovery, but extended duration (18+ months) causes deeper structural damage.

### Resolution Probability Rationale

- **Default**: Maximum entropy would be 33/33/33
- **Specified**: 40/35/25
- **Confidence**: Medium — historical sample is small (n=2 clear cases)

Accelerated transition weighted slightly higher (0.40) because:
- Historical pattern: both 1973 and 1979 produced efficiency gains
- Current context: transition technologies more mature than in past
- Policy readiness: many jurisdictions have transition plans awaiting trigger

Producer restructuring weighted at 0.35 because:
- Geopolitical competition makes restructuring likely
- Non-OPEC capacity (shale, alternatives) can grow
- But restructuring alone without demand destruction is less common historically

Extended crisis weighted lower (0.25) because:
- SPR and coordination mechanisms provide buffers
- Demand elasticity higher than in 1970s
- But remains plausible for severe scenarios (Hormuz closure + producer collapse)

---

## Aftermath Branches

The original specification carried, for each aftermath branch, a set of **factor modifications** (post-event shifts in the event's own factor loadings), an **aftermath duration** (decay-to-floor, permanent, or regime-dependent), and an **impact vector** on named groups of economies. The v0.1 schema carries none of the first two (factor modifications and aftermath-duration forms other than plain decay/permanent are schema v0.2 backlog, Task 6.4); they are preserved here as prose. The impact vectors are re-expressed against the state catalog in the `impacts:` block under Impacts below; the original vectors are kept in the tables here because the YAML had to re-express most of them.

### Accelerated Transition Aftermath

#### Branch: Successful Transition (60%)

Shock catalyzes successful acceleration of energy transition. Renewables and efficiency investments surge. Electric vehicle adoption accelerates. Oil demand peaks earlier than baseline trajectory. Energy security improves long-term despite short-term pain.

| Factor modification | Value | Note |
|---------------------|-------|------|
| F_MENA | −0.15 | Reduced relevance of oil producers |
| F_CLIM | −0.10 | Lower emissions trajectory |
| F_FIN | +0.20 | Transition investment stress |

**Aftermath duration (original)**: permanent — demand destruction and efficiency gains don't reverse.

| Original impact vector | Group | Magnitude | Note |
|------------------------|-------|-----------|------|
| oil_price | global | [+0.80, 0.30] | 80% spike during transition |
| inflation | global | [+0.03, 0.01] | percentage points |
| gdp_growth | global | [−0.015, 0.008] | annual drag during adjustment |
| renewable_investment | global | [+0.40, 0.15] | acceleration vs. baseline |
| oil_demand_peak | global | [−5, 2] | years earlier than baseline |
| gdp | oil_importers | [−0.025, 0.01] | short-term pain |
| energy_intensity | oil_importers | [−0.15, 0.05] | permanent efficiency gain |
| current_account | oil_importers | [−0.02, 0.01] | temporary worsening |
| gdp | oil_exporters | [+0.10, 0.05] | short-term windfall |
| fiscal_sustainability | oil_exporters | [−0.20, 0.10] | long-term demand loss |
| diversification_pressure | oil_exporters | [+0.30, 0.10] | |

#### Branch: Chaotic Transition (40%)

Transition acceleration is disorderly. Investment flows are volatile. Grid instability from rapid renewable integration. Political backlash in some jurisdictions. Transition occurs but with higher costs and more disruption than successful scenario.

| Factor modification | Value | Note |
|---------------------|-------|------|
| F_MENA | −0.10 | |
| F_FIN | +0.35 | |
| F_GPT | +0.15 | Energy competition intensifies |

**Aftermath duration (original)**: decaying, half-life 5 years, floor 0.20.

| Original impact vector | Group | Magnitude | Note |
|------------------------|-------|-----------|------|
| oil_price | global | [+1.00, 0.40] | larger spike, more volatility |
| inflation | global | [+0.04, 0.015] | |
| gdp_growth | global | [−0.025, 0.01] | |
| financial_stability | global | [−0.20, 0.08] | |
| political_stability | developed_economies | [−0.15, 0.08] | energy price backlash |
| gdp | emerging_economies | [−0.04, 0.015] | harder hit by transition costs |

### Producer Restructuring Aftermath

#### Branch: New Equilibrium (55%)

New producer-consumer relationships stabilize. Non-OPEC production (US shale, Brazil, Guyana, others) gains share. Bilateral energy partnerships replace multilateral frameworks. New trade routes and infrastructure develop.

| Factor modification | Value | Note |
|---------------------|-------|------|
| F_GPT | +0.20 | Energy competition component of great power rivalry |
| F_MENA | −0.10 | Reduced MENA centrality |
| F_LAM | +0.10 | Latin American producers gain importance |

**Aftermath duration (original)**: regime-dependent — persists in `current_trade_architecture`.

| Original impact vector | Group | Magnitude | Note |
|------------------------|-------|-----------|------|
| oil_price | global | [+0.40, 0.20] | elevated but stable |
| trade_volume | global | [−0.05, 0.02] | some fragmentation |
| supply_chain_resilience | global | [−0.10, 0.05] | new dependencies |
| energy_production | united_states | [+0.15, 0.08] | shale expansion |
| energy_exports | united_states | [+0.25, 0.10] | |
| gdp | mena_exporters | [−0.08, 0.04] | market share loss |
| political_influence | mena_exporters | [−0.20, 0.10] | |

#### Branch: Fragmented Markets (45%)

Energy markets fragment into competing blocs. Pricing mechanisms diverge. Arbitrage constrained by political barriers. Long-term inefficiency in global energy allocation.

| Factor modification | Value |
|---------------------|-------|
| F_GPT | +0.35 |
| F_FIN | +0.25 |

**Aftermath duration (original)**: decaying, half-life 8 years, floor 0.25.

| Original impact vector | Group | Magnitude | Note |
|------------------------|-------|-----------|------|
| oil_price | global | [+0.60, 0.25] | higher due to inefficiency |
| trade_volume | global | [−0.10, 0.04] | |
| economic_efficiency | global | [−0.08, 0.03] | |
| energy_access | non_aligned_countries | [−0.15, 0.08] | caught between blocs |

### Extended Crisis Aftermath

#### Branch: Managed Recovery (50%)

After 18-24 months of crisis, supply recovers and demand adjusts. Deep economic damage during crisis period but eventual stabilization. Lessons learned improve future resilience.

| Factor modification | Value |
|---------------------|-------|
| F_FIN | +0.40 |
| F_GPT | +0.25 |

**Aftermath duration (original)**: decaying, half-life 4 years, floor 0.15.

| Original impact vector | Group | Magnitude | Note |
|------------------------|-------|-----------|------|
| oil_price | global | [+1.50, 0.50] | major spike during crisis |
| gdp_growth | global | [−0.04, 0.015] | significant recession |
| inflation | global | [+0.06, 0.02] | cost-push inflation |
| financial_stability | global | [−0.30, 0.12] | |
| gdp | oil_importers | [−0.06, 0.02] | |
| current_account | oil_importers | [−0.04, 0.015] | |
| political_stability | oil_importers | [−0.20, 0.10] | |
| poverty_rate | emerging_economies | [+0.05, 0.02] | percentage point increase |
| food_security | emerging_economies | [−0.15, 0.06] | fertilizer/transport costs |

#### Branch: Cascading Failures (50%)

Extended crisis triggers cascading failures in vulnerable economies. State failures in oil-dependent or food-insecure countries. Financial contagion. Global recession deepens into depression in worst cases.

| Factor modification | Value |
|---------------------|-------|
| F_FIN | +0.60 |
| F_GPT | +0.40 |
| F_FOOD | +0.35 |
| F_MENA | +0.25 |
| F_SSA | +0.30 |

**Aftermath duration (original)**: decaying, half-life 6 years, floor 0.30.

**Branch-specific cascade triggers (original)**: GLOBAL_FINANCIAL_CRISIS ×2.0 for 3 years; EGYPT_STATE_FAILURE ×1.8 for 3 years; PAKISTAN_STATE_FAILURE ×1.5 for 3 years. These are carried in the `cascades:` block as conditional (`if: "branch == 'cascading_failures'"`) increments on top of the event-wide edges.

| Original impact vector | Group | Magnitude | Note |
|------------------------|-------|-----------|------|
| oil_price | global | [+2.00, 0.70] | extreme spike |
| gdp_growth | global | [−0.06, 0.02] | deep recession |
| inflation | global | [+0.08, 0.03] | |
| financial_stability | global | [−0.45, 0.15] | |
| displacement | global | [+15000000, 8000000] | from cascading state failures |

---

## Impacts

### Entity Groups

The original impact vectors address groups of economies that the state catalog does not define. The YAML expands each group into explicit catalog entities, drawn from the file's own Vulnerability by Country Type lists and extended with the catalog's other clear net importers/exporters:

| Group (original key) | Entities in YAML | Note |
|----------------------|------------------|------|
| `oil_importers`, high vulnerability | jpn, kor, twn, ind, pak, bgd, egy, eth, ken, cod, east_africa, sahel | GDP rows carry the 1.5-2× multiplier of the vulnerability section at its midpoint (×1.75); other rows at base |
| `oil_importers`, moderate vulnerability | chn, bra, deu, fra, ita, esp, nld, pol, eu_other, gbr, tur, idn | ×1.0 base |
| `oil_exporters` | usa, can, sau, are, gulf_states, irn, rus, kaz, nga, levant_iraq | Net exporters in the catalog; Norway and Guyana are not catalog entities |
| `mena_exporters` | sau, are, gulf_states, irn, levant_iraq | |
| `developed_economies` | usa, can, deu, gbr, fra, ita, esp, nld, pol, eu_other, jpn, kor, twn, aus, sgp, isr | |
| `emerging_economies` | chn, ind, pak, bgd, egy, idn, vnm, tha, phl, tur, bra, arg, mex, nga, eth, cod, zaf, ken | |
| `united_states` | usa | |
| `non_aligned_countries` | — | Group too ill-defined to enumerate; its single row (`energy_access`) has no catalog variable and stays in prose |

Smaller importers not listed (tha, vnm, phl, sgp, zaf, isr, ukr, the Tier 2 aggregates) receive only the global wildcard rows (`*.gdp_growth`, `*.inflation_rate`) at Level 1.

### Variable Re-expression

The original vectors use variables the catalog lacks. Rows were re-expressed as follows (magnitudes are additive in the target's units except `gdp_real`, which is a fraction of the entity's current value — [[methodology/reference/event-yaml-schema]] §Impact Fields):

| Original variable | Catalog target | Conversion |
|-------------------|----------------|------------|
| `oil_price` (fraction of price) | `oil_brent` ($/bbl) | × $75 baseline (2025): +0.80 → +60, +1.00 → +75, +0.40 → +30, +0.60 → +45, +1.50 → +112.5, +2.00 → +150 |
| `inflation` (global, pp) | `*.inflation_rate` (% per year) | ×100; applied to every country as the original's "global" row. The v0.1 engine does not yet implement the oil→inflation passthrough of MVP scope §5.1 step 6; when it does, these rows and the passthrough overlap and one must give way |
| `gdp_growth` (global) | `*.gdp_growth` (% per year) | ×100 (pp) |
| `gdp` (group) | `<entity>.gdp_real` | fraction, unchanged; high-vulnerability importers ×1.75 |
| `current_account` (group) | `<entity>.current_account` (% of GDP) | ×100 (pp) |
| `trade_volume` (global) | `global_trade_volume` (index, 2025=100) | ×100 (index points) |
| `financial_stability` (index) | `global_credit_spread` (bps) | −0.10 of index ≙ +75 bps: −0.20 → +150 (the pandemic's moderate-branch spread), −0.30 → +225, −0.45 → +340 (2008-scale) |
| `political_stability` (index) | `<entity>.protest_intensity_annual` (0-100) | −0.10 of index ≙ +10 points |
| `energy_intensity` (importers, −15%) | `<entity>.energy_import_dependence` (% of consumption) | −15% of energy use for an economy importing 60-90% of it ≈ −10 ± 4 pp of import share |
| `energy_production` (US, +15%) | `usa.energy_import_dependence` | −5 ± 3 pp (the catalog's only production/consumption-balance variable) |
| `food_security` (emerging, −0.15) | `fertilizer_price_index`, `wheat_price`, `rice_price`, `corn_price` | the catalog's food-price variables carry the channel at Chain 1's magnitudes: fertilizer +100% (+100 ± 40 index points), food prices +30-50% (+40% ± 15% of the 2025 baselines: wheat +2.4 ± 0.9 $/bu, rice +200 ± 75 $/t, corn +2.0 ± 0.75 $/bu) |

**Rows not carried** (no catalog variable; the channel stays in the prose above): `renewable_investment`, `oil_demand_peak`, `oil_exporters.fiscal_sustainability`, `oil_exporters.diversification_pressure`, `supply_chain_resilience`, `united_states.energy_exports`, `mena_exporters.political_influence`, `economic_efficiency`, `non_aligned_countries.energy_access`, `emerging_economies.poverty_rate`, `displacement` (state-failure displacement arrives through the cascaded events' own rows).

**Onset.** The original vectors carry no onset. Price, inflation, growth, spread and current-account rows are `immediate`; the structural rows (importer efficiency gains, US production expansion, MENA market-share loss) ramp `gradual` over 3-5 years.

```yaml
impacts:
  accelerated_transition.successful_transition:
    # Global
    - {var: oil_brent,                       mag: [60, 22.5],      onset: immediate, decay: 2}
    - {var: "*.inflation_rate",              mag: [3, 1],          onset: immediate, decay: 2}
    - {var: "*.gdp_growth",                  mag: [-1.5, 0.8],     onset: immediate, decay: 2}
    # Oil importers, high vulnerability (GDP x1.75)
    - {var: jpn.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: kor.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: twn.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: ind.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: pak.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: bgd.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: egy.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: eth.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: ken.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: cod.gdp_real,                    mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: east_africa.gdp_real,            mag: [-0.044, 0.018], onset: immediate, decay: 2}
    - {var: sahel.gdp_real,                  mag: [-0.044, 0.018], onset: immediate, decay: 2}
    # Oil importers, moderate vulnerability
    - {var: chn.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: bra.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: deu.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: fra.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: ita.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: esp.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: nld.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: pol.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: eu_other.gdp_real,               mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: gbr.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: tur.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    - {var: idn.gdp_real,                    mag: [-0.025, 0.01],  onset: immediate, decay: 2}
    # Oil importers (both groups): permanent efficiency gain
    - {var: jpn.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: kor.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: twn.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: ind.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: pak.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: bgd.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: egy.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: eth.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: ken.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: cod.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: east_africa.energy_import_dependence, mag: [-10, 4],   onset: {gradual: 5}, permanent: true}
    - {var: sahel.energy_import_dependence,  mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: chn.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: bra.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: deu.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: fra.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: ita.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: esp.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: nld.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: pol.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: eu_other.energy_import_dependence, mag: [-10, 4],      onset: {gradual: 5}, permanent: true}
    - {var: gbr.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: tur.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    - {var: idn.energy_import_dependence,    mag: [-10, 4],        onset: {gradual: 5}, permanent: true}
    # Oil importers (both groups): temporary current-account worsening
    - {var: jpn.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: kor.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: twn.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: ind.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: pak.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: bgd.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: egy.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: eth.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: ken.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: cod.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: east_africa.current_account,     mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: sahel.current_account,           mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: chn.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: bra.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: deu.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: fra.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: ita.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: esp.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: nld.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: pol.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: eu_other.current_account,        mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: gbr.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: tur.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    - {var: idn.current_account,             mag: [-2, 1],         onset: immediate, decay: 2}
    # Oil exporters: short-term windfall
    - {var: usa.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: can.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: sau.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: are.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: gulf_states.gdp_real,            mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: irn.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: rus.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: kaz.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: nga.gdp_real,                    mag: [0.10, 0.05],    onset: immediate, decay: 2}
    - {var: levant_iraq.gdp_real,            mag: [0.10, 0.05],    onset: immediate, decay: 2}

  accelerated_transition.chaotic_transition:
    # Global
    - {var: oil_brent,                       mag: [75, 30],        onset: immediate, decay: 5}
    - {var: "*.inflation_rate",              mag: [4, 1.5],        onset: immediate, decay: 5}
    - {var: "*.gdp_growth",                  mag: [-2.5, 1.0],     onset: immediate, decay: 5}
    - {var: global_credit_spread,            mag: [150, 60],       onset: immediate, decay: 5}
    # Developed economies: energy price backlash
    - {var: usa.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: can.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: deu.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: gbr.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: fra.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: ita.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: esp.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: nld.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: pol.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: eu_other.protest_intensity_annual, mag: [15, 8],       onset: immediate, decay: 5}
    - {var: jpn.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: kor.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: twn.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: aus.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: sgp.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    - {var: isr.protest_intensity_annual,    mag: [15, 8],         onset: immediate, decay: 5}
    # Emerging economies: harder hit by transition costs
    - {var: chn.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: ind.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: pak.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: bgd.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: egy.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: idn.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: vnm.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: tha.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: phl.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: tur.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: bra.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: arg.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: mex.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: nga.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: eth.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: cod.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: zaf.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}
    - {var: ken.gdp_real,                    mag: [-0.04, 0.015],  onset: immediate, decay: 5}

  producer_restructuring.new_equilibrium:
    # Global: elevated but stable price; some trade fragmentation
    - {var: oil_brent,                       mag: [30, 15],        onset: immediate, permanent: true}
    - {var: global_trade_volume,             mag: [-5, 2],         onset: immediate, permanent: true}
    # United States: shale expansion
    - {var: usa.energy_import_dependence,    mag: [-5, 3],         onset: {gradual: 3}, permanent: true}
    # MENA exporters: market share loss
    - {var: sau.gdp_real,                    mag: [-0.08, 0.04],   onset: {gradual: 3}, permanent: true}
    - {var: are.gdp_real,                    mag: [-0.08, 0.04],   onset: {gradual: 3}, permanent: true}
    - {var: gulf_states.gdp_real,            mag: [-0.08, 0.04],   onset: {gradual: 3}, permanent: true}
    - {var: irn.gdp_real,                    mag: [-0.08, 0.04],   onset: {gradual: 3}, permanent: true}
    - {var: levant_iraq.gdp_real,            mag: [-0.08, 0.04],   onset: {gradual: 3}, permanent: true}

  producer_restructuring.fragmented_markets:
    - {var: oil_brent,                       mag: [45, 18.75],     onset: immediate, decay: 8}
    - {var: global_trade_volume,             mag: [-10, 4],        onset: immediate, decay: 8}

  extended_crisis.managed_recovery:
    # Global
    - {var: oil_brent,                       mag: [112.5, 37.5],   onset: immediate, decay: 4}
    - {var: "*.gdp_growth",                  mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: "*.inflation_rate",              mag: [6, 2],          onset: immediate, decay: 4}
    - {var: global_credit_spread,            mag: [225, 90],       onset: immediate, decay: 4}
    # Food-security channel (fertilizer/transport costs; Chain 1 magnitudes)
    - {var: fertilizer_price_index,          mag: [100, 40],       onset: immediate, decay: 4}
    - {var: wheat_price,                     mag: [2.4, 0.9],      onset: immediate, decay: 4}
    - {var: rice_price,                      mag: [200, 75],       onset: immediate, decay: 4}
    - {var: corn_price,                      mag: [2.0, 0.75],     onset: immediate, decay: 4}
    # Oil importers, high vulnerability (GDP x1.75)
    - {var: jpn.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: kor.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: twn.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: ind.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: pak.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: bgd.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: egy.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: eth.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: ken.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: cod.gdp_real,                    mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: east_africa.gdp_real,            mag: [-0.105, 0.035], onset: immediate, decay: 4}
    - {var: sahel.gdp_real,                  mag: [-0.105, 0.035], onset: immediate, decay: 4}
    # Oil importers, moderate vulnerability
    - {var: chn.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: bra.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: deu.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: fra.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: ita.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: esp.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: nld.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: pol.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: eu_other.gdp_real,               mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: gbr.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: tur.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    - {var: idn.gdp_real,                    mag: [-0.06, 0.02],   onset: immediate, decay: 4}
    # Oil importers (both groups): current account
    - {var: jpn.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: kor.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: twn.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: ind.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: pak.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: bgd.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: egy.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: eth.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: ken.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: cod.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: east_africa.current_account,     mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: sahel.current_account,           mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: chn.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: bra.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: deu.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: fra.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: ita.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: esp.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: nld.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: pol.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: eu_other.current_account,        mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: gbr.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: tur.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    - {var: idn.current_account,             mag: [-4, 1.5],       onset: immediate, decay: 4}
    # Oil importers (both groups): political stress
    - {var: jpn.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: kor.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: twn.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: ind.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: pak.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: bgd.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: egy.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: eth.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: ken.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: cod.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: east_africa.protest_intensity_annual, mag: [20, 10],   onset: immediate, decay: 4}
    - {var: sahel.protest_intensity_annual,  mag: [20, 10],        onset: immediate, decay: 4}
    - {var: chn.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: bra.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: deu.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: fra.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: ita.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: esp.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: nld.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: pol.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: eu_other.protest_intensity_annual, mag: [20, 10],      onset: immediate, decay: 4}
    - {var: gbr.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: tur.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}
    - {var: idn.protest_intensity_annual,    mag: [20, 10],        onset: immediate, decay: 4}

  extended_crisis.cascading_failures:
    # Global
    - {var: oil_brent,                       mag: [150, 52.5],     onset: immediate, decay: 6}
    - {var: "*.gdp_growth",                  mag: [-6, 2],         onset: immediate, decay: 6}
    - {var: "*.inflation_rate",              mag: [8, 3],          onset: immediate, decay: 6}
    - {var: global_credit_spread,            mag: [340, 115],      onset: immediate, decay: 6}
    # Food-security channel (the branch's state failures are in food-insecure countries; Chain 1 magnitudes)
    - {var: fertilizer_price_index,          mag: [100, 40],       onset: immediate, decay: 6}
    - {var: wheat_price,                     mag: [2.4, 0.9],      onset: immediate, decay: 6}
    - {var: rice_price,                      mag: [200, 75],       onset: immediate, decay: 6}
    - {var: corn_price,                      mag: [2.0, 0.75],     onset: immediate, decay: 6}
```

*Units: `gdp_real` rows are fractions of the entity's current value (−2.5% ± 1% for a moderate-vulnerability importer in the successful-transition branch); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). The wildcard rows expand to the 40 countries, not the aggregates.*

### Durability Specifications

The original specification set durability per aftermath branch, not per row. The v0.1 schema compiles only `decay: N`, `permanent: true` and `until: resolved`; decay-to-floor and regime-dependent durability are schema v0.2 backlog (Task 6.4).

| Branch | Original durability | YAML form | Note |
|--------|---------------------|-----------|------|
| successful_transition | permanent (demand destruction and efficiency gains don't reverse) | `permanent` for the efficiency-gain rows; `decay: 2` for the rows the vector itself marks temporary (price spike "during transition", GDP "short-term pain", current account "temporary worsening", exporter "short-term windfall", growth "drag during adjustment", inflation) | A permanent 80% oil-price spike would contradict the vector's own comments |
| chaotic_transition | decaying: half_life=5yr, floor=0.20 | `decay: 5` | Floor dropped (v0.2) |
| new_equilibrium | regime_dependent: persists in `current_trade_architecture` | `permanent: true` | Nearest implementable form; `until: policy_change` is not compiled in v0.1 |
| fragmented_markets | decaying: half_life=8yr, floor=0.25 | `decay: 8` | Floor dropped (v0.2) |
| managed_recovery | decaying: half_life=4yr, floor=0.15 | `decay: 4` | Floor dropped (v0.2) |
| cascading_failures | decaying: half_life=6yr, floor=0.30 | `decay: 6` | Floor dropped (v0.2) |

The floors (0.15-0.30 of the initial magnitude) are the "damage a recovery cannot fix" class: the file's claim is that even a managed recovery leaves a permanently higher price level and permanently lost output. Under plain decay the YAML understates the long-run tail of every decaying branch by that floor.

---

## Vulnerability by Country Type

### High Vulnerability (GDP impact 1.5-2x base)

**Oil-import-dependent economies with limited alternatives:**
- Japan, South Korea, Taiwan (energy island economies)
- India (scale and poverty constraints)
- Pakistan, Bangladesh, Egypt (fiscal constraints + food security linkage)
- Much of Sub-Saharan Africa (limited infrastructure, dollar constraints)

**Exposure variable**: `energy_import_dependence × fiscal_space_inverse`

### Moderate Vulnerability (GDP impact 1x base)

**Diversified economies with some domestic production or alternatives:**
- European Union (some domestic, pipeline alternatives, reserves)
- China (SPR, diversified sources, coal backup)
- Brazil (domestic production, biofuels)

### Low Vulnerability / Beneficiaries

**Net exporters:**
- United States (net exporter, shale flexibility) — short-term beneficiary
- Canada, Norway, Guyana — windfall gains
- Gulf states — revenue windfall but demand destruction risk

**Caveat**: In extended crisis scenario, even exporters face demand destruction risk.

---

## Cascade Effects

```yaml
cascades:
  triggers:
    # Event-wide edges (original multipliers converted against each target's base annual probability)
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.015,  years: 3}
    - {event: EGYPT_STATE_FAILURE,       delta: 0.008,  years: 3}
    - {event: PAKISTAN_STATE_FAILURE,    delta: 0.005,  years: 3}
    - {event: EU_FRAGMENTATION,          delta: 0.001,  years: 5}
    - {event: SAUDI_REGIME_INSTABILITY,  delta: -0.002, years: 3}
    # Cascading-failures branch: increments that lift the edges to the branch's own multipliers
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.015,  years: 3, if: "branch == 'cascading_failures'"}
    - {event: EGYPT_STATE_FAILURE,       delta: 0.004,  years: 3, if: "branch == 'cascading_failures'"}
    - {event: PAKISTAN_STATE_FAILURE,    delta: 0.0025, years: 3, if: "branch == 'cascading_failures'"}
  triggered_by: []  # The original specification carries no source table; the Disruption Pathways above name the trigger classes, and the precursor-war hazard is Task 6.2
```

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Financial stress | GLOBAL_FINANCIAL_CRISIS | ×1.5-2.0 | 3 years | Energy cost shock → corporate defaults → financial contagion |
| Food price transmission | EGYPT_STATE_FAILURE | ×1.5 | 3 years | Fertilizer/transport costs → food prices → bread subsidies unsustainable |
| Fiscal stress (importers) | PAKISTAN_STATE_FAILURE | ×1.3 | 3 years | Import bill → forex reserves → IMF dependency deepens |
| Political backlash | EU_FRAGMENTATION | ×1.2 | 5 years | Differential impacts → solidarity strain → populist surge |
| Revenue windfall end | SAUDI_REGIME_INSTABILITY | ×0.7 initially, ×1.3 after | 5+ years | Windfall delays stress; demand destruction accelerates it |

**Multiplier → delta conversion.** The schema's `delta` is an absolute change in the target's annual probability; the multipliers above were converted against the targets' current base rates: GLOBAL_FINANCIAL_CRISIS 3.0% (×1.5 → +0.015; the cascading-failures branch's ×2.0 → +0.030), EGYPT_STATE_FAILURE 1.5% (×1.5 → +0.0075, written 0.008; ×1.8 → +0.012), PAKISTAN_STATE_FAILURE 1.5% (×1.3 → +0.0045, written 0.005; ×1.5 → +0.0075), EU_FRAGMENTATION 0.4% (×1.2 → +0.0008, written 0.001), SAUDI_REGIME_INSTABILITY 0.8% (×0.7 → −0.0024, written −0.002). The Saudi edge carries only the windfall phase (3 years); the later ×1.3 (demand destruction accelerating fiscal stress once the windfall ends) needs a delayed-start cascade the schema does not have and stays in this table.

### Impact Chains

**Chain 1: Food Security Cascade**
Oil shock → fertilizer prices +100% → agricultural costs surge → food prices +30-50% → import-dependent countries face fiscal crisis → subsidy collapse → political instability → state failure risk

**Chain 2: Financial Contagion**
Oil shock → energy-intensive corporate defaults → banking sector stress → credit contraction → recession deepens → sovereign stress in vulnerable economies → emerging market contagion

**Chain 3: Transition Acceleration**
Oil shock → energy security salience → policy window opens → transition investment surge → stranded asset recognition → fossil fuel divestment → producer revenue decline → producer state instability

---

## Transmission Channels

### Price Channel
**Mechanism**: Supply reduction → price spike → cost-push inflation → real income reduction → demand contraction
**Affected regions**: Global, especially oil importers
**Affected variables**: oil_price, inflation, gdp_growth, real_wages

### Trade Channel
**Mechanism**: Energy costs embedded in all traded goods; transport costs surge; supply chain disruption
**Affected regions**: Global trade networks
**Affected variables**: trade_volume, shipping_costs, supply_chain_resilience

### Fiscal Channel
**Mechanism**: Import bill surge strains forex reserves and government budgets; subsidy costs explode
**Affected regions**: Oil-importing emerging economies
**Affected variables**: fiscal_balance, forex_reserves, debt_sustainability

### Financial Channel
**Mechanism**: Energy-intensive corporate stress → bank losses → credit contraction → growth slowdown
**Affected regions**: Global, especially leveraged economies
**Affected variables**: financial_stability, credit_availability, corporate_defaults

### Geopolitical Channel
**Mechanism**: Energy competition intensifies; alliances restructure around energy security; producer influence shifts
**Affected regions**: Global
**Affected variables**: alliance_dynamics, diplomatic_alignment, trade_partnerships

*The variable names in this section are the original specification's channel labels; the catalog carriers are `oil_brent`, `*.inflation_rate`, `*.gdp_growth`, `global_trade_volume`, `<entity>.current_account`, `global_credit_spread` and `<entity>.protest_intensity_annual` (see Variable Re-expression above). The geopolitical channel has no catalog carrier at Level 1.*

---

## Case Against

### 1. Shale revolution makes 1970s-style shocks impossible

**Argument**: US shale production can ramp up within 6-12 months in response to price signals. Combined with SPR, this provides buffer that makes sustained shortage impossible.

**Counter**: Shale can add ~1-2 mbpd within a year, but Hormuz closure removes ~20 mbpd. The gap is too large to close quickly. Shale also requires investment and drilling that takes time to mobilize.

### 2. Demand elasticity is much higher now

**Argument**: Economy is less oil-intensive. Electric vehicles, work-from-home, efficiency gains mean demand can adjust faster than in 1970s.

**Counter**: Marginal improvements are real but oil remains essential for transport, chemicals, and agriculture. Short-term demand elasticity is still low (-0.1 to -0.2). Structural adjustment takes years.

### 3. Producer self-interest prevents sustained disruption

**Argument**: Even hostile producers need revenue. Disruptions will be brief because no producer wants to forgo income for long.

**Counter**: Some scenarios (war, regime collapse, infrastructure destruction) remove producer choice. Revolutionary Iran didn't prioritize export revenue. Civil conflict doesn't optimize for market access.

### 4. SPR and IEA coordination provide adequate buffer

**Argument**: 90+ days of strategic reserves across OECD, plus coordination mechanisms, can handle any short-term disruption.

**Counter**: SPR is sized for short disruptions. A 12-month crisis would exhaust reserves. Coordination mechanisms have never been tested at scale.

### What would change estimate 2x+

| Change | Direction | Magnitude |
|--------|-----------|-----------|
| Hormuz closure (military conflict) | ↑ | +200% for sustained shortage |
| Saudi regime instability materializes | ↑ | +150% for supply disruption |
| Rapid shale capacity expansion | ↓ | -30% for resilience |
| Global SPR expansion (especially China) | ↓ | -25% for buffer capacity |
| Accelerated EV adoption (50%+ of new sales) | ↓ | -40% for demand elasticity |
| US-Iran military conflict | ↑ | +150% for regional disruption |

### Probability Evolution

As a Type 1 stochastic event, probability is relatively stable but influenced by structural factors:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2035 | 2.0-3.0% | Elevated geopolitical tension; Hormuz chokepoint risk; supply concentration persists |
| 2035-2050 | 1.5-2.5% | Energy transition reduces demand; diversification continues; but producer state instability may rise |
| 2050-2075 | 1.0-2.0% | Lower if transition advanced; but remaining oil demand concentrated in harder-to-substitute uses |

**Key inflection points**:
- Energy transition pace: Faster transition = lower probability and lower impact when shocks occur
- Hormuz alternative infrastructure: Bypass pipelines would reduce chokepoint risk
- Producer state stability: Saudi/Gulf instability would elevate risk
- US-Iran relationship: Military conflict would sharply elevate probability

---

## Sensitivity Analysis Notes

| Parameter | Range to Test | Why It Matters |
|-----------|---------------|----------------|
| Disruption magnitude threshold | 10-20% of global supply | Determines what counts as discontinuity |
| Duration threshold | 3-12 months | Short disruptions may not force structural change |
| Shale response time | 6-18 months | Affects substitution capacity |
| SPR deployment willingness | 30-90 days | Political constraints on reserve use |
| Demand elasticity | -0.05 to -0.20 | Short-term adjustment capacity |
| Financial contagion channel | 0.3-0.8 severity multiplier | Links to GLOBAL_FINANCIAL_CRISIS |

---

## Research Upgrade Path

**Level 2 (4-8 hours)**:
- Strait of Hormuz closure scenarios: military feasibility, mine clearing timelines
- Shale production response capacity: capital constraints, drilling inventory
- SPR deployment history and political constraints
- Producer state stability assessment for supply at risk
- Historical oil shock macroeconomic impact analysis

**Level 3 (20+ hours)**:
- Expert elicitation on supply chokepoint vulnerabilities
- Financial system stress testing for energy shock scenarios
- Food security transmission modeling (fertilizer/transport costs)
- Country-by-country fiscal vulnerability assessment
- Energy transition acceleration modeling under shock conditions

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

**Upgrade rationale**: Hormuz scenario detail; shale response capacity; food security cascade.

## Sources

- Level 1 specification from prior knowledge
- Calibration against [[methodology/reference/calibration-anchors]] Oil Shock anchor
- Historical reference: 1973 OPEC embargo, 1979 Iranian Revolution, 2022 Russia-Ukraine

## Open Questions

- Strait of Hormuz closure: military feasibility and mine clearing timeline
- Chinese SPR: actual size and deployment doctrine
- Shale drilling inventory: how much can be activated quickly?
- Food security transmission: fertilizer price elasticity and timing
- EV adoption acceleration: how much demand destruction is already locked in?
- Saudi infrastructure resilience: Houthi attack capacity vs. redundancy
- Financial system vulnerability: which institutions have concentrated energy exposure?

---

*See [[methodology/reference/calibration-anchors]] for Type 1 methodology | [[methodology/reference/probability-estimation]] for estimation approach*

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Critical review: added Probability Evolution section; updated research status | Task 2.4 systematic review |
| 2025-12-25 | Initial Level 1 specification | Type 1 stochastic event |
| 2025-12-31 | Variance allocation: scaled loadings to Type 1 target | Task 3.11 — loadings ×0.84 to (ΛΩΛᵀ)ᵢᵢ = 0.75; the original loadings and their sum-of-squares line were removed from the table at the time (restored 2026-10-12) |
| 2026-10-12 | **Migrated to YAML-embedded schema** | Task 4.2.24. Classification, probability, factors, resolutions/branches, impacts, cascades and research tables → YAML; the legacy `resolutions`/`aftermath_branches` YAML blocks (schema-less: `probability`/`description` keys, `factor_modifications`, `duration`, `impact_vector`, `cascade_triggers`) merged into the schema blocks, their descriptions and rationale moved to prose. **Judgment calls**: (1) `domain: economic` for the prose's "Economic / Geopolitical". (2) Factor modifications and aftermath-duration forms (decay-to-floor, regime_dependent) are not v0.1 constructs; kept as prose tables per branch; decay-to-floor → plain `decay`, regime_dependent → `permanent: true`; the successful-transition branch's "permanent" applies to its efficiency-gain rows while its price/GDP/current-account/growth/inflation rows take `decay: 2` because the vector's own comments mark them temporary. (3) Group keys (`oil_importers`, `oil_exporters`, `mena_exporters`, `developed_economies`, `emerging_economies`, `united_states`) expanded into explicit catalog entities per the Entity Groups table; high-vulnerability importers' GDP rows ×1.75 (midpoint of the vulnerability section's 1.5-2×); `non_aligned_countries` not enumerable. (4) Variable alternatives: `financial_stability` → `global_credit_spread` (−0.10 ≙ +75 bps), `political_stability` → `protest_intensity_annual` (−0.10 ≙ +10), `energy_intensity` → `energy_import_dependence` (−15% → −10 ± 4 pp), US `energy_production` → `usa.energy_import_dependence` (−5 ± 3 pp), `food_security` → `fertilizer_price_index` and wheat/rice/corn at Chain 1's magnitudes; global `inflation` → `*.inflation_rate`, global `gdp_growth` → `*.gdp_growth`. (5) Unit conversions: `oil_price` fractions × $75 baseline (+0.80 → +60 … +2.00 → +150 $/bbl); inflation, growth, current-account and trade-volume fractions ×100 into pp / index points; food prices +40% ± 15% of the 2025 baselines. (6) Dropped rows (no catalog variable; channel kept in prose): `renewable_investment`, `oil_demand_peak`, exporter `fiscal_sustainability` and `diversification_pressure`, `supply_chain_resilience`, US `energy_exports`, MENA `political_influence`, `economic_efficiency`, non-aligned `energy_access`, emerging `poverty_rate`, `displacement`. (7) Onset (absent in the original) `immediate` except structural rows (`gradual` 3-5). (8) Cascade multipliers converted to absolute deltas against target base rates (table under Cascade Effects); the cascading-failures branch's own multipliers carried as `if: "branch == 'cascading_failures'"` increments; the Saudi edge carries the ×0.7 windfall phase only (−0.002, 3 years), the later ×1.3 stays in prose (no delayed-start cascade construct). All five targets exist as files; no aliases, promotions or unlisted IDs. (9) `triggered_by: []` — the original carries no source table. No `until: resolved` rows, so no `resolves_after`. **Restored from history**: the original (pre-3.11) loadings column and the "Sum of squared loadings = 0.63" line removed by the 2025-12-31 scaling commit; the Loading Rationale paragraph's 0.55/0.40/0.35 figures are labelled as the original loadings. YAML stays Type 1; the precursor-war hazard prose is Task 6.2 |
