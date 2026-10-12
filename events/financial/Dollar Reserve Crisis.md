---
title: Dollar Reserve Crisis
type: note
permalink: events/financial/dollar-reserve-crisis
tags:
- event
- financial
- type-2
- threshold
- dollar
- reserve-currency
- global
- level-1
---

# Dollar Reserve Crisis

## Event Classification

```yaml
id: DOLLAR_RESERVE_CRISIS
domain: economic
scale: global
causal_type: 2
onset: sudden
reversibility: partial
```

*Onset speed: rapid (1-3 years for full impact transmission), recorded as `sudden` (the schema enum is `sudden|gradual`). Reversibility: partial (can stabilize at new equilibrium but not fully reverse).*

## Description

Acute loss of confidence in the dollar-based reserve system, manifesting as sharp Treasury yield spikes (150+ bps within months), rapid foreign reserve diversification, and potential failed auction dynamics. This represents a discrete crisis event distinct from gradual reserve share erosion—the moment when accumulated pressure triggers a confidence cascade. The event marks transition from "dominant reserve currency" to "first among equals" in a multipolar system, with severe near-term disruption followed by structural adjustment.

---

## Causal Type Specification

### Type 2: Threshold Dynamics

This event exhibits classic threshold behavior: pressure accumulates through multiple channels (fiscal deterioration, reserve diversification, sanctions weaponization precedent, alternative infrastructure maturation), and at some critical point, a confidence cascade triggers acute crisis. The gradual erosion of dollar reserve share (~1.5-2 pp/year) is the pressure-building process; the crisis is the discrete state transition.

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `usd_reserve_share` | 0.30 | inverse | Lower share → higher pressure; crisis more likely as dollar approaches 50% threshold |
| `usa.debt_public` | 0.25 | linear | Higher debt burden (% GDP) → greater vulnerability to confidence loss |
| *foreign_treasury_holdings_pct* | 0.20 | inverse | Lower foreign holdings → less structural demand, auction risk |
| *fiscal_deficit_pct_gdp* | 0.15 | linear | Larger deficits → more issuance requiring buyers |
| `cips_share` | 0.10 | linear | Higher CIPS share as proxy for alternative infrastructure maturity |

*Note: Variables in italics are not in current state-specification and would need to be added or derived. `foreign_treasury_holdings_pct` could be derived from TIC data; `fiscal_deficit_pct_gdp` could be derived from `debt_public` changes plus interest payments.*

The YAML expression below realizes these transforms in the expression language's subset as clipped linear ramps: the dollar-share term as `(70 − share) / 30` (zero at a 70% share, one at 40%, so "approaching 50%" reads as two-thirds pressure); the debt term as `debt_public / 200`; the CIPS term as `cips_share / 40`. The two variables the state catalog lacks are replaced by catalog observables of the same channel: `foreign_treasury_holdings_pct` by `us_10yr_yield` (the auction-risk symptom of weaker structural Treasury demand, ramp `(yield − 2) / 5` from 2% to 7%; note this variable is also an impact target of the event, so a firing raises its own subsequent pressure) and `fiscal_deficit_pct_gdp` by `usa.current_account` (the external financing need that deficits create — the twin-deficit observable; ramp `−current_account / 8`, zero at balance, one at an 8%-of-GDP deficit). The weights are unchanged.

**Current pressure estimate (2025)**: ~45 on 0-100 scale
- Dollar share: 57.7% (moderate pressure)
- Debt-to-GDP: 124% (elevated)
- Foreign Treasury holdings: 30% (declining from 50%+ in 2008)
- Deficit: 6.4% of GDP (high)
- BRICS infrastructure: Early operational (mBridge pilot, SGEI vaults)

At the catalog's 2025 baselines (dollar share 58%, 10-year yield 4.5%, CIPS 8%) with debt at 124% of GDP and a current-account deficit of ~3.8% of GDP, the expression gives ~46.5, consistent with the "~45" estimate. The compiler's pressure-scale check is skipped for this event because the expression reads country variables, which carry no recorded baseline.

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 70 on 0-100 scale | Crisis requires multiple indicators in danger zone simultaneously |
| **Uncertainty** | ±10 (range 60-80) | No historical precedent for reserve currency crisis of this magnitude |
| **Sharpness (k)** | 8 | Moderately sharp—crisis dynamics accelerate near threshold |
| **Historical calibration** | Partial analogs only | UK sterling decline (gradual), Asian crisis 1997 (acute but different), Greek crisis 2010 (acute, smaller scale) |

*The sharpness of 8 was written against a 0–1 pressure scale (the same convention as the original [0, 1] pressure weights). The engine's logistic, `floor + (1 − floor) / (1 + exp(−k · (pressure − threshold)))`, takes k per unit of the 0–100 scale ([[methodology/reference/probability-estimation]]), on which 8 is a step function at the drawn threshold rather than "moderately sharp". The YAML carries the documented 8 unchanged: the sharpness convention is mixed across the catalog (0.15–0.25 in AMOC and Pakistan, 8–15 here and in the EU, Chinese and US political events) and is recorded as an open data-track item in sim/README.md §4 rather than re-tuned file by file.*

### Minimum Probability

**Floor**: 0.3% annually even at low pressure

Rationale: Black swan Treasury auction failure possible even with healthy fundamentals. External shocks (major war, terrorist attack on financial infrastructure, sudden loss of Fed credibility) could trigger crisis regardless of pressure level.

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.30 * clip((70 - usd_reserve_share) / 30, 0, 1) +
      0.25 * clip(usa.debt_public / 200, 0, 1) +
      0.20 * clip((us_10yr_yield - 2) / 5, 0, 1) +
      0.15 * clip(-usa.current_account / 8, 0, 1) +
      0.10 * clip(cips_share / 40, 0, 1)
    )
  threshold: 70
  threshold_std: 10
  sharpness: 8
  floor: 0.003
  annual: 0.015
  range: [0.008, 0.030]
  confidence: medium
```

| Metric | Value |
|--------|-------|
| **Annual probability** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 3.0% |
| **Confidence** | Medium-Low (recorded as `medium` in YAML: the schema enum is `low|medium|high`) |
| **25-year cumulative** | ~31% at point estimate |

### Derivation

**Step 1: Research foundation estimate**

The [[research/brics-de-dollarization]] analysis assigns 15-25% probability to "accelerated collapse" scenario over 20 years. Converting to annual:
- 15% over 20 years → ~0.8% annual
- 25% over 20 years → ~1.4% annual

This provides a baseline range of 0.8-1.4% for acute crisis.

**Step 2: Pressure trajectory adjustment**

The research assumes current (2025) conditions. If pressure increases as projected:
- Dollar share falling toward 50% by 2030
- Debt-to-GDP rising toward 140% by 2035
- Foreign holdings declining toward 20%

Higher pressure in later years implies higher conditional probability. Averaging across the simulation horizon suggests adjusting upward to ~1.5%.

**Step 3: Comparative calibration**

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Global Financial Crisis | ~3.0% | More frequent; financial crises recur regularly |
| AMOC Weakening | ~1.0% | Comparable rarity; threshold dynamics similar |
| Pakistan State Failure | ~1.5% | Similar probability; pressure accumulation dynamic |

Dollar Reserve Crisis is rarer than generic financial crisis (requires specific reserve currency dynamics, not just credit cycle) but comparable to major geopolitical threshold events.

**Step 4: Uncertainty assessment**

Key factors that could push probability higher:
- Faster BRICS infrastructure maturation than expected
- US political dysfunction preventing fiscal adjustment
- Major geopolitical rupture (Taiwan conflict) accelerating diversification
- Loss of Fed independence

Key factors that could push probability lower:
- Successful US fiscal consolidation post-2028
- Chinese economic/political crisis reducing yuan alternative viability
- European active support for dollar system
- Bretton Woods III negotiated transition

Given unprecedented nature and wide scenario range, confidence is Medium-Low.

### Comparative Ranking

- More likely than: AMOC collapse, Russia state failure
- Similar to: Pakistan state failure, Iran regime change
- Less likely than: Global financial crisis, severe pandemic

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4:

**1. No precedent for reserve currency crisis**

The dollar system has no historical analog for acute collapse. Sterling's decline was gradual (1945-1970). The 2008 crisis strengthened dollar demand (flight to safety). The "crisis" scenario may be a category error—reserve currency transitions may only happen gradually.

*Counter*: Gradual decline is the baseline trajectory, not this event. The event specifically models the tail scenario where gradual becomes acute. The absence of precedent doesn't mean impossibility—it means high uncertainty, which we acknowledge.

**2. Network effects protect incumbency**

The dollar's dominance is self-reinforcing through invoicing, settlement, and liquidity. Even if alternatives mature, switching costs are enormous. The threshold for crisis may be much higher than estimated.

*Counter*: Network effects explain why crisis is low probability (1.5%/year), not why it's impossible. Network effects can collapse suddenly when alternatives become "good enough"—see technology platform disruptions.

**3. China won't want the responsibility**

Reserve currency status brings burdens (Triffin dilemma, overvaluation). China may prefer dollar dominance to continue, limiting the drive for alternatives.

*Counter*: China doesn't need to replace the dollar—a multipolar system with reduced dollar share is sufficient. And China's revealed preference (mBridge, gold accumulation, bilateral settlement) contradicts the "China prefers dollar" hypothesis.

**4. Crisis would hurt everyone, forcing cooperation**

The systemic importance of dollar markets means all major economies have incentive to prevent collapse. The "Bretton Woods III" response would likely emerge before full crisis.

*Counter*: This is a plausible path (10% probability to Bretton Woods III branch). But coordination during crisis is hard—2008 showed cooperation is possible but imperfect. The question is whether cooperation comes fast enough.

### Probability Evolution

For Type 2 events, probability varies with pressure accumulation.

| Period | Estimated Pressure | Annual Probability | Rationale |
|--------|-------------------|-------------------|-----------|
| 2025-2030 | 45 → 52 | ~1.3% | Current trajectory; slow dollar share erosion |
| 2030-2040 | 52 → 62 | ~1.8% | Dollar approaches 50% threshold; alternatives maturing |
| 2040-2050 | 62 → 72 | ~2.5% | Entering threshold zone if no prior crisis |
| 2050-2075 | 72+ | ~3.0%+ | High pressure if no prior resolution |

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

```yaml
factors:
  F_FIN: 0.48   # Primary driver: financial fragility directly affects Treasury market stress, yield dynamics, reserve demand
  F_GPT: 0.27   # Secondary: geopolitical tensions accelerate reserve diversification, sanctions concerns
  F_TECH: 0.14  # Tertiary: alternative payment infrastructure (mBridge, CBDC) maturity
  F_EUR: 0.14   # European stress affects euro as alternative; European positioning matters
  F_EAS: 0.14   # Chinese infrastructure development; yuan internationalization pace
  F_MENA: 0.07  # Petrodollar dynamics; Gulf state positioning
variance: 0.65  # Type 2 target
```

F_CLIM, F_HLTH and F_FOOD carry no loading (no direct climate, health or food system linkage); F_SAS, F_SSA and F_LAM carry none (minimal direct linkage).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.68 from original loadings

**Original (pre-scaling) loadings**: F_FIN 0.7, F_GPT 0.4, F_TECH 0.2, F_EUR 0.2, F_MENA 0.1, F_EAS 0.2. **Sum of squared loadings**: 0.49 + 0.16 + 0.04 + 0.04 + 0.01 + 0.04 = **0.78** ✓ (the pre-allocation check; the scaled loadings above achieve 0.655 under the inter-factor correlation matrix Ω)

### Loading Rationale

Factors operate by shocking state variables that feed the pressure function:

**F_FIN (0.7)**: High F_FIN draws manifest as Treasury market stress, yield volatility, credit spread widening, and Fed credibility questions. These directly increase fiscal deficit pressure (higher debt service), reduce foreign Treasury holdings (flight to safety elsewhere), and potentially trigger the confidence cascade that defines the crisis event.

**F_GPT (0.4)**: Elevated geopolitical tension accelerates the "sanctions weaponization" concern that drives reserve diversification. The 2022 Russia sanctions precedent demonstrated that dollar reserves can be frozen—high F_GPT years reinforce this lesson and accelerate `usd_reserve_share` decline.

**F_TECH (0.2)**: Technology factor captures alternative payment infrastructure maturity. High F_TECH years may see faster mBridge operationalization, CBDC adoption, or blockchain-based settlement systems that increase `cips_share` and make exit from dollar system more feasible.

**F_EUR (0.2)**: European stress creates complex effects. High F_EUR may weaken euro as alternative (supporting dollar) but also signals broader Western financial system fragility (undermining dollar). Net effect is mild pressure increase.

**F_EAS (0.2)**: East Asian tension and Chinese development affect yuan internationalization pace and Shanghai Gold Exchange infrastructure. High F_EAS may accelerate or impede alternative infrastructure depending on specific manifestation.

---

## Impact Vector

The tables in this section are the original (pre-migration) impact specification, kept because they record forms the YAML block at the end of the section had to re-express: percentage magnitudes on index/price variables, sub-year onset delays, decay-to-floor durabilities, and variables the state catalog lacks. The YAML is the compiled record; where the two differ, the differences are listed under "Impact Specification (YAML)" below and in the changelog.

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| *global_gdp_growth* | ↓ | -2.0 ± 0.8 pp | immediate | decaying: half_life=3yr, floor=-0.5 |
| `global_trade_volume` | ↓ | -8 ± 3% | immediate | decaying: half_life=2yr, floor=-2% |
| `gold_price` | ↑ | +40 ± 15% | immediate | permanent (new equilibrium) |
| *global_financial_volatility* | ↑ | +80 ± 30% (VIX equivalent) | immediate | decaying: half_life=1yr |
| `usd_reserve_share` | ↓ | -12 ± 5 pp | gradual(3yr) | permanent |
| `gold_reserve_share` | ↑ | +5 ± 2 pp | gradual(3yr) | permanent |
| `cny_reserve_share` | ↑ | +3 ± 2 pp | gradual(5yr) | permanent |

*Note: Variables in italics would need to be added to state-specification or derived (e.g., `global_gdp_growth` aggregated from country GDP growth rates).*

### United States Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `usa.gdp_real` | ↓ | -10 ± 4% (peak-to-trough) | gradual(2yr) | decaying: half_life=5yr, floor=-3% |
| `us_10yr_yield` | ↑ | +350 ± 100 bps (acute) | immediate | permanent (new equilibrium +150bps) |
| `usa.unemployment_rate` | ↑ | +6 ± 2 pp | delayed(6mo) | decaying: half_life=4yr |
| `usa.inflation_rate` | ↑ | +3 ± 1.5 pp | delayed(3mo) | decaying: half_life=2yr |
| *dxy_index* | ↓ | -30 ± 10% | immediate | permanent (new equilibrium -20%) |
| *usa.debt_service_pct_revenue* | ↑ | +8 ± 3 pp | delayed(1yr) | permanent |

*Note: `us_10yr_yield` is a global variable in the state-spec. Variables in italics (`dxy_index`, `debt_service_pct_revenue`) are not in current state-specification.*

### Regional Impacts

**Eurozone** (modeled via individual countries: Germany, France, Italy, Spain, Netherlands, Poland + Rest of EU aggregate):

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].gdp_growth` | ↓ | -1.5 ± 0.8 pp | delayed(6mo) | decaying: half_life=2yr |
| `eur_reserve_share` | ↑ | +3 ± 1.5 pp | gradual(3yr) | permanent |

Mixed impact: Euro gains reserve share but Eurozone hurt by US recession transmission and euro appreciation reducing export competitiveness.

**China:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.gdp_growth` | ↓ | -1.0 ± 0.5 pp | delayed(6mo) | decaying: half_life=2yr |
| `cny_reserve_share` | ↑ | +3 ± 2 pp | gradual(5yr) | permanent |

Mixed impact: Yuan gains reserve share but loses US export market; net strategic gain with near-term economic cost.

**Emerging Markets with High Dollar Debt** (Turkey, Egypt, Pakistan, Argentina, South Africa, Indonesia):

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].debt_external` | ↑ | +15 ± 8 pp effective burden | immediate | decaying: half_life=3yr |
| `[country].gdp_growth` | ↓ | -2.5 ± 1.5 pp | delayed(6mo) | decaying: half_life=3yr |
| `[country].regime_stability` | ↓ | -10 ± 5 | delayed(1yr) | decaying: half_life=4yr |

Severe impact through interest rate channel and own-currency depreciation.

**Gulf States** (aggregate):

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `gulf.gdp_growth` | ↓ | -0.5 ± 0.3 pp | delayed(6mo) | decaying: half_life=2yr |

Transition disruption but strategic positioning for multipolar system; relatively insulated due to sovereign wealth reserves.

### Differential Impacts

**Exposure variable**: `country.dollar_debt_to_gdp`

**Function**: threshold(15%)

**Effect**: Countries with dollar-denominated debt exceeding 15% of GDP experience amplified negative impacts (1.5× magnitude on GDP, unemployment, inflation). High exposure countries include: Argentina, Turkey, Egypt, Pakistan, South Africa, Indonesia.

**Exposure variable**: `country.export_dependence_on_us`

**Function**: linear

**Effect**: Countries with high US export dependence (>15% of exports to US) experience larger GDP impacts proportional to exposure.

*Neither exposure variable is in the state catalog; the differential exposure is carried in prose only (the high-exposure country list is what the explicit emerging-market rows in the YAML implement).*

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| GDP contraction | decaying | half_life=5yr, floor=-3% | Economy restructures but permanent loss of "exorbitant privilege" |
| Unemployment spike | decaying | half_life=4yr | Labor market eventually adjusts |
| Inflation surge | decaying | half_life=2yr | One-time import price shock, not persistent |
| Interest rate increase | permanent | — | New equilibrium; US must pay market rates without privilege |
| Dollar depreciation | permanent | — | New equilibrium at more competitive level |
| Reserve composition | permanent | — | Structural shift to multipolar system |
| Trade disruption | decaying | half_life=2yr | Settlement systems adapt |

*Decay-to-floor durability (the −3% GDP floor, the −2% trade floor, the −0.5 pp global-growth floor) is schema v0.2 backlog; the YAML uses plain half-lives. The interest-rate row's "permanent (new equilibrium +150 bps)" is an acute +350 bps shock settling to a permanent +150 bps: the YAML carries it as two rows, a permanent +150 bps and an acute +200 bps with a 2-year half-life (the managed-crisis trajectory's "recovery begins within 2 years"), which expresses the floor with v0.1 constructs. The dollar-depreciation row has no catalog variable (see below).*

### Impact Derivation

**Method**: Primarily analog-based with scaling adjustments

**Primary analogs**:
- UK sterling decline (1945-1970): Gradual reserve share loss; eventual stabilization at reduced level
- Asian Financial Crisis (1997): Acute confidence crisis with ~10% GDP contractions in affected countries
- Greek Sovereign Debt Crisis (2010): Yield spikes, forced austerity, 25% GDP decline peak-to-trough
- Global Financial Crisis (2008): Transmission mechanisms, recovery dynamics

**Scaling considerations**:
- US economy is ~25% of global GDP; shock transmission is significant but not catastrophic for world
- Dollar system is more deeply embedded than any historical analog; transition costs higher
- Modern financial system has both greater interconnection (amplifies shock) and better crisis tools (dampens shock)

**Transmission analysis**: See Section below for channel-by-channel breakdown.

### Impact Specification (YAML)

The `managed` branch (×1.0) is the explicit list; the other two aftermath branches scale it (see "Aftermath Branches" below). Re-expressions relative to the tables above:

- **Units**: `global_trade_volume` −8% → −8 index points (2025 = 100); `gold_price` +40% → +$800/oz on the $2,000 baseline; `us_10yr_yield` +350 bps → +3.5 in the variable's % units. `gdp_real` rows are fractions of the entity's current value (−10% ± 4% for the US); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields).
- **Onsets**: the sub-year delays (3mo, 6mo) become `immediate` on the annual timestep; delayed(1yr) becomes `{delayed: 1}`.
- **Proxies**: `global_financial_volatility` (+80% ± 30%, VIX equivalent) is carried on `global_credit_spread`, the catalog's financial-stress variable, as +96 ± 36 bps (80% of the 120 bps baseline) with the 1-year half-life. The emerging-market `regime_stability` row (−10 ± 5) is carried on `protest_intensity_annual` (+10 ± 5, sign flipped), the observable that replaced the synthetic stability index per [[methodology/concepts/synthetic-variable-problem]]. The Gulf aggregate's catalog ID is `gulf_states`.
- **Dropped rows (channel kept in prose)**: `global_gdp_growth` (−2.0 ± 0.8 pp) is not a state variable; global growth is the aggregate of the country rows. `dxy_index` (−30 ± 10%, permanent −20%): the catalog has no exchange-rate variable; the depreciation's inflation effect is in the `usa.inflation_rate` row. `usa.debt_service_pct_revenue` (+8 ± 3 pp): `debt_service_ratio` is a derived variable and cannot be an impact target; it moves with the `us_10yr_yield` rows.
- `cny_reserve_share` appears in both the global and the China tables; it is one row.

```yaml
impacts:
  managed:
    # Global
    - {var: global_trade_volume,        mag: [-8, 3],       onset: immediate,    decay: 2}
    - {var: gold_price,                 mag: [800, 300],    onset: immediate,    permanent: true}
    - {var: global_credit_spread,       mag: [96, 36],      onset: immediate,    decay: 1}
    - {var: usd_reserve_share,          mag: [-12, 5],      onset: {gradual: 3}, permanent: true}
    - {var: gold_reserve_share,         mag: [5, 2],        onset: {gradual: 3}, permanent: true}
    - {var: cny_reserve_share,          mag: [3, 2],        onset: {gradual: 5}, permanent: true}
    - {var: eur_reserve_share,          mag: [3, 1.5],      onset: {gradual: 3}, permanent: true}

    # United States
    - {var: usa.gdp_real,               mag: [-0.10, 0.04], onset: {gradual: 2}, decay: 5}
    - {var: us_10yr_yield,              mag: [1.5, 0.5],    onset: immediate,    permanent: true}
    - {var: us_10yr_yield,              mag: [2.0, 0.9],    onset: immediate,    decay: 2}
    - {var: usa.unemployment_rate,      mag: [6, 2],        onset: immediate,    decay: 4}
    - {var: usa.inflation_rate,         mag: [3, 1.5],      onset: immediate,    decay: 2}

    # Eurozone + Rest of EU
    - {var: deu.gdp_growth,             mag: [-1.5, 0.8],   onset: immediate,    decay: 2}
    - {var: fra.gdp_growth,             mag: [-1.5, 0.8],   onset: immediate,    decay: 2}
    - {var: ita.gdp_growth,             mag: [-1.5, 0.8],   onset: immediate,    decay: 2}
    - {var: esp.gdp_growth,             mag: [-1.5, 0.8],   onset: immediate,    decay: 2}
    - {var: nld.gdp_growth,             mag: [-1.5, 0.8],   onset: immediate,    decay: 2}
    - {var: pol.gdp_growth,             mag: [-1.5, 0.8],   onset: immediate,    decay: 2}
    - {var: eu_other.gdp_growth,        mag: [-1.5, 0.8],   onset: immediate,    decay: 2}

    # China
    - {var: chn.gdp_growth,             mag: [-1.0, 0.5],   onset: immediate,    decay: 2}

    # Emerging markets with high dollar debt
    - {var: tur.debt_external,          mag: [15, 8],       onset: immediate,    decay: 3}
    - {var: tur.gdp_growth,             mag: [-2.5, 1.5],   onset: immediate,    decay: 3}
    - {var: tur.protest_intensity_annual, mag: [10, 5],     onset: {delayed: 1}, decay: 4}
    - {var: egy.debt_external,          mag: [15, 8],       onset: immediate,    decay: 3}
    - {var: egy.gdp_growth,             mag: [-2.5, 1.5],   onset: immediate,    decay: 3}
    - {var: egy.protest_intensity_annual, mag: [10, 5],     onset: {delayed: 1}, decay: 4}
    - {var: pak.debt_external,          mag: [15, 8],       onset: immediate,    decay: 3}
    - {var: pak.gdp_growth,             mag: [-2.5, 1.5],   onset: immediate,    decay: 3}
    - {var: pak.protest_intensity_annual, mag: [10, 5],     onset: {delayed: 1}, decay: 4}
    - {var: arg.debt_external,          mag: [15, 8],       onset: immediate,    decay: 3}
    - {var: arg.gdp_growth,             mag: [-2.5, 1.5],   onset: immediate,    decay: 3}
    - {var: arg.protest_intensity_annual, mag: [10, 5],     onset: {delayed: 1}, decay: 4}
    - {var: zaf.debt_external,          mag: [15, 8],       onset: immediate,    decay: 3}
    - {var: zaf.gdp_growth,             mag: [-2.5, 1.5],   onset: immediate,    decay: 3}
    - {var: zaf.protest_intensity_annual, mag: [10, 5],     onset: {delayed: 1}, decay: 4}
    - {var: idn.debt_external,          mag: [15, 8],       onset: immediate,    decay: 3}
    - {var: idn.gdp_growth,             mag: [-2.5, 1.5],   onset: immediate,    decay: 3}
    - {var: idn.protest_intensity_annual, mag: [10, 5],     onset: {delayed: 1}, decay: 4}

    # Gulf States aggregate
    - {var: gulf_states.gdp_growth,     mag: [-0.5, 0.3],   onset: immediate,    decay: 2}

  disorderly:
    inherit: managed
    scale: 1.8

  bretton_woods_iii:
    inherit: managed
    scale: 0.6
```

---

## Aftermath Branches

The crisis event triggers one of three post-event trajectories, determined by policy response and external conditions.

```yaml
branches:
  - {id: disorderly, p: 0.35, desc: "Disorderly Collapse: failed policy response; dollar to 30-35% of reserves; depression-level US contraction"}
  - {id: managed, p: 0.55, desc: "Managed Crisis: Fed/Treasury stabilize acute phase; orderly fiscal adjustment; multipolar context"}
  - {id: bretton_woods_iii, p: 0.10, desc: "Bretton Woods III: negotiated transition to multipolar reserve system"}
```

*The YAML `impacts:` block takes the managed branch (×1.0) as its explicit list and scales the others from it with single-scale inheritance: `disorderly` 1.8 and `bretton_woods_iii` 0.6, the branches' GDP multipliers. The per-variable modifiers below (unemployment ×2.0, half-lives ±50%/−30%, moderated permanent impacts) are not representable under single-scale inheritance and remain documented here; the uniform scales reproduce the branch trajectories (dollar share ~36% / ~46% / ~51%, US GDP −18% / −10% / −6%, acute yield +630 / +350 / +210 bps) to first order.*

### Branch Probability Calibration Note

**Entropy maximization default**: With three branches and no calibrating data, the principled default would be 33.3% / 33.3% / 33.3%.

**Ordinal adjustment rationale**: We deviate from entropy based on structural reasoning about coordination difficulty:

| Branch | Coordination Required | Structural Difficulty |
|--------|----------------------|----------------------|
| Disorderly Collapse | None (passive failure) | Low—requires only that things go wrong |
| Managed Crisis | Unilateral (Fed/Treasury) | Medium—requires competent response by single government |
| Bretton Woods III | Multilateral (US + China + EU + Japan) | High—requires rivals to cooperate on burden-sharing |

This ordering suggests P(Bretton Woods III) < P(Managed) < P(Disorderly), with Bretton Woods III notably lower because getting four great powers to agree during a crisis is mechanically harder than one government managing its own response.

**Reference class support**: International institutional redesign is rare in the historical reference class of financial crises. Bretton Woods I required World War II; the 2008 crisis produced coordination but no architectural redesign; the 1997 Asian crisis produced no new framework. "Managed but painful adjustment" is the modal outcome.

**Cardinal uncertainty**: The ordinal reasoning supports the direction of adjustment but provides no basis for specific probabilities. The assigned values (35% / 55% / 10%) are placeholders that respect the ordering while acknowledging we cannot distinguish between, say, 30/55/15 and 40/50/10 on principled grounds.

**Recommendation**: Sensitivity analysis should test whether aftermath branch probabilities materially affect tail outcomes. If they do, invest in better calibration.

### Branch 1: Disorderly Collapse

**Probability given event**: 35%

**Trigger conditions**: Failed policy response, additional external shocks, political dysfunction preventing stabilization

**Trajectory**:
- Dollar falls to 30-35% of global reserves within 3 years
- Treasury yields remain elevated (8-10%) for extended period
- US GDP falls 15-20% peak-to-trough (depression-level)
- Emergency IMF intervention required (SDR-based bailout)
- Forced austerity program resembling 1990s Russia or 2010s Greece
- Social and political crisis; potential constitutional implications

**Impact modifiers** (multiply base impacts):
- GDP impact: ×1.8
- Unemployment impact: ×2.0
- Duration: half-lives extended by 50%

**Factor modifications during aftermath**:
- F_FIN: +0.3 loading for 5 years (ongoing financial stress)
- F_GPT: +0.2 loading for 5 years (geopolitical instability from US weakness)

### Branch 2: Managed Crisis

**Probability given event**: 55%

**Trigger conditions**: Fed/Treasury intervention stabilizes acute phase; forced but orderly fiscal adjustment; international coordination prevents cascade

**Trajectory**:
- Dollar stabilizes at 40-45% of global reserves
- Treasury yields normalize at +150-200 bps above pre-crisis (new equilibrium)
- US GDP falls 8-12% peak-to-trough; recovery begins within 2 years
- Significant but manageable fiscal adjustment required
- "Mild stagflation" for 3-5 years (growth 1-2%, inflation 3-4%)
- US retains significant global role but in multipolar context

**Impact modifiers**: Base case (×1.0)

**Factor modifications during aftermath**:
- F_FIN: +0.15 loading for 3 years (elevated but contained stress)

### Branch 3: Bretton Woods III

**Probability given event**: 10%

**Trigger conditions**: Crisis forces unprecedented international coordination; US, China, EU, Japan agree on managed transition framework

**Trajectory**:
- Negotiated transition to multipolar reserve system
- Dollar stabilizes at 45-48% (orderly decline rather than collapse)
- New framework: expanded SDR, gold settlement mechanism, or multi-currency basket
- US GDP impact limited to 5-8% decline
- Global trade/finance disruption minimized
- All major powers accept compromises; system institutionalizes multipolarity

**Impact modifiers** (reduce base impacts):
- GDP impact: ×0.6
- Duration: half-lives reduced by 30%
- Permanent impacts moderated (dollar settles at higher share)

**Factor modifications during aftermath**:
- F_FIN: +0.05 loading for 2 years (mild residual stress)
- F_GPT: -0.1 loading for 5 years (reduced tensions from successful cooperation)

*Aftermath factor-loading modifications (time-limited changes to the event's loadings after firing) are not a v0.1 schema construct; they are kept here as specification intent.*

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - {event: EU_FRAGMENTATION,           delta: 0.015,  years: 3}
    - {event: CHINESE_POLITICAL_CRISIS,   delta: 0.005,  years: 2}
    - {event: EGYPT_STATE_FAILURE,        delta: 0.010,  years: 3}
    - {event: PAKISTAN_STATE_FAILURE,     delta: 0.010,  years: 3}
    - {event: TURKEY_POLITICAL_BREAKDOWN, delta: 0.008,  years: 3}
    - {event: GLOBAL_FINANCIAL_CRISIS,    delta: 0.020,  years: 2}
    - {event: OIL_SUPPLY_SHOCK,           delta: -0.005, years: 5}
  triggered_by:
    - {event: GLOBAL_FINANCIAL_CRISIS,    delta: 0.020}
    - {event: US_CONSTITUTIONAL_CRISIS,   delta: 0.015}
    - {event: TAIWAN_CONFLICT,            delta: 0.015}
    - {event: CHINESE_ECONOMIC_CRISIS,    delta: -0.010}
    - {event: IRAN_REGIME_CHANGE,         delta: 0.003}
```

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| EU_FRAGMENTATION | +1.5% | 3 years | Stress on euro as sudden alternative; divergent member state responses |
| CHINESE_POLITICAL_CRISIS | +0.5% | 2 years | Export collapse creates economic pressure; legitimacy challenge |
| EGYPT_STATE_FAILURE | +1.0% | 3 years | Dollar debt burden; import cost surge; forex crisis |
| PAKISTAN_STATE_FAILURE | +1.0% | 3 years | Dollar debt burden; import cost surge; IMF conditionality |
| TURKEY_POLITICAL_BREAKDOWN (originally written `TURKEY_POLITICAL_CRISIS`; alias normalized per [[events/backlog-registry]] §3) | +0.8% | 3 years | Lira crisis amplification; dollar debt exposure |
| GLOBAL_FINANCIAL_CRISIS | +2.0% | 2 years | Systemic stress; contagion through financial system |
| OIL_SUPPLY_SHOCK | -0.5% | 5 years | Dollar pricing disruption reduces incentive for supply manipulation |

### Triggered By (Probability Increases)

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +2.0% | Financial stress accelerates flight from Treasuries; Fed credibility tested |
| US_CONSTITUTIONAL_CRISIS | +1.5% | Political dysfunction signals inability to address fiscal problems; confidence collapse |
| TAIWAN_CONFLICT | +1.5% | Geopolitical rupture accelerates diversification; potential sanctions on China triggers counter-measures |
| CHINESE_ECONOMIC_CRISIS | -1.0% | Yuan alternative becomes less viable; supports dollar by reducing competition |
| IRAN_REGIME_CHANGE | +0.3% | MENA instability affects petrodollar dynamics |

### Impact Chains

**Chain 1**: Dollar Reserve Crisis → EM debt stress → Pakistan/Egypt state failure risk
- Crisis triggers sharp rise in US Treasury yields (+350 bps)
- EM countries face dual pressure: higher global rates AND own-currency depreciation against dollar
- Dollar debt service burden increases sharply for high-debt EMs
- Countries with high dollar debt and low reserves face default pressure
- Political instability follows economic stress

*Note: The dollar may experience brief flight-to-safety appreciation in the acute phase before sustained depreciation. The EM debt stress operates primarily through the interest rate channel and EM currency weakness, not through dollar strength per se.*

**Chain 2**: Dollar Reserve Crisis → Trade disruption → Global recession → Financial crisis
- Settlement system disruption reduces trade volumes
- Reduced trade triggers demand shock globally
- Corporate earnings fall; credit stress emerges
- Potential cascade into broader financial crisis

**Chain 3**: Dollar Reserve Crisis → US fiscal constraint → Reduced security commitments → Regional instability
- Higher debt service crowds out defense spending
- US forced to reduce overseas commitments
- Regional powers face security vacuum
- Local conflicts more likely (MENA, East Asia)

---

## Transmission Channels

### 1. Interest Rate Channel (Primary)

**Mechanism**: Reduced foreign demand for Treasuries forces higher yields to attract domestic buyers. Higher Treasury yields transmit to all US interest rates (mortgages, corporate debt, municipal bonds). Higher rates reduce investment and consumption.

**Magnitude**: Each 100 bps yield increase reduces GDP growth by ~0.3-0.5 pp annually through investment/consumption effects.

**Affected regions**: US (primary), all countries with dollar-linked rates (secondary)

**Affected variables**: `usa.investment_growth`, `usa.consumption_growth`, `usa.housing_prices`, `usa.corporate_borrowing_cost`

### 2. Currency Channel

**Mechanism**: Reduced dollar demand causes depreciation. Imports become more expensive (inflationary). Exports become more competitive (eventually supportive of growth). US runs large trade deficit, so import price effect dominates initially.

**Magnitude**: 10% dollar depreciation → ~1-1.5 pp inflation increase; export boost emerges with 12-18 month lag.

**Affected regions**: US (primary), trade partners (secondary)

**Affected variables**: `usa.import_prices`, `usa.export_competitiveness`, `usa.inflation`, `usa.trade_balance`

### 3. Wealth Effect Channel

**Mechanism**: Higher interest rates reduce present value of future cash flows. Stock prices decline (P/E compression). Bond prices fall. Real estate prices decline. Household wealth falls, reducing consumption.

**Magnitude**: 20% equity market decline → ~0.6-1.0 pp reduction in consumption growth.

**Affected regions**: US (primary), countries with US asset exposure (secondary)

**Affected variables**: `usa.household_wealth`, `usa.consumption_growth`, `usa.equity_valuations`

### 4. Trade Channel

**Mechanism**: Dollar's role in trade invoicing declines. US loses network externality benefits. Financial services exports decline (transaction fees, currency conversion, banking services).

**Magnitude**: US financial services exports ~$350B annually; 15-25% decline over 5-10 years → $50-90B annual loss.

**Affected regions**: US (primary), financial centers (secondary)

**Affected variables**: `usa.financial_services_exports`, `usa.current_account`, `global.trade_settlement_composition`

### 5. Fiscal Channel

**Mechanism**: Higher debt service costs reduce fiscal space. Forced austerity (spending cuts or tax increases) directly reduces aggregate demand.

**Magnitude**: Each $100B in additional debt service → ~0.3-0.4 pp GDP reduction if offset by spending cuts.

**Affected regions**: US (primary)

**Affected variables**: `usa.fiscal_deficit`, `usa.debt_service_pct_revenue`, `usa.government_spending`, `usa.tax_revenue`

### 6. Confidence Channel

**Mechanism**: Loss of dollar dominance signals reduced US global standing. Risk premiums increase on all US assets. Capital outflows (or reduced inflows). Investment declines.

**Magnitude**: Difficult to quantify; potentially 50-150 bps additional risk premium across asset classes.

**Affected regions**: US (primary)

**Affected variables**: `usa.fdi_inflows`, `usa.risk_premium`, `usa.business_confidence`

*The "affected variables" named in this section are the channels' descriptive variables, most of which are not state-catalog variables; the compiled impacts are the YAML rows above.*

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete (2025-12-30) |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | High-impact event with extensive research foundation; Level 2 could model Treasury auction dynamics, Fed intervention scenarios, and international coordination mechanisms in greater detail |

## Sources

- [[research/brics-de-dollarization]] — Primary research foundation (November 2025)
- IMF COFER database — Reserve currency composition data
- Federal Reserve TIC System — Foreign Treasury holdings data
- World Gold Council — Central bank gold purchases
- BIS Quarterly Review — International financial statistics
- ECB "International Role of the Euro" (June 2025)
- Peterson Institute for International Economics — Dollar dominance research
- Asia Society Policy Institute — Petroyuan analysis

## Open Questions

1. **Trigger mechanism specificity**: What exact event initiates the acute phase? Failed Treasury auction? Sudden large seller? Rating agency action? Or is it emergent from accumulated pressure?

2. **Fed intervention effectiveness**: How quickly and effectively can Fed intervention (emergency Treasury purchases, swap lines) stabilize an acute crisis? Does intervention merely delay or actually prevent cascade?

3. **European positioning**: Will Europe actively support dollar system, remain neutral/hedging, or opportunistically accelerate euro alternatives? European response significantly affects crisis trajectory.

4. **China's strategic patience**: Will China accelerate yuan internationalization during crisis (opportunistic) or slow down to avoid being blamed (strategic patience)? Affects aftermath branch probabilities.

5. **Political economy of adjustment**: Can US political system implement fiscal adjustment required for Branch 2 (Managed Crisis)? Historical evidence is mixed; may require Branch 1 severity to force action.

6. **Contagion dynamics**: How do EM debt crises interact with the main event? Are they absorbed into the crisis or do they amplify it through feedback loops?

7. **Gold price dynamics**: Does gold price surge create its own instabilities (mining country windfalls, central bank balance sheet effects)? Potential second-order effects not fully modeled.

---

*Cross-references*: [[methodology/reference/causal-types]], [[methodology/reference/probability-estimation]], [[methodology/reference/factor-loadings]], [[events/financial/global-financial-crisis]], [[research/brics-de-dollarization]]

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Verified critical review complete | Task 2.4 systematic review |
| 2025-12-30 | Full Level 1 specification with critical review | Task 2.1 financial crisis events |
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.21. Classification, probability, factor, branch, impact, cascade and research tables converted; all prose kept; the original impact and durability tables kept as the record of pre-migration forms. Judgment calls: (1) pressure proxies for the two variables the catalog lacks — `foreign_treasury_holdings_pct` → `us_10yr_yield` (auction-risk observable; also an impact target, so a firing raises its own later pressure), `fiscal_deficit_pct_gdp` → `usa.current_account` (external financing need; sign inverted) — with transforms realized as clipped linear ramps (documented under the pressure table); weights unchanged; the expression gives ~46.5 at the prose's 2025 values; the compiler's baseline check is skipped (country variables). (2) Sharpness 8 kept as documented although the engine's logistic takes k on the 0–100 scale, where 8 is a step function; the catalog-wide sharpness convention is an open item in sim/README.md §4. (3) Confidence Medium-Low → `medium`. (4) Sub-year onset delays (3mo, 6mo) → `immediate`; delayed(1yr) → `{delayed: 1}`. (5) Durability: decay-to-floor GDP (floor −3%) and trade (floor −2%) rows → plain `decay: 5` / `decay: 2` (v0.2 backlog); the yield row "permanent (new equilibrium +150 bps)" → a permanent +150 bps row plus an acute +200 bps row with 2-year half-life. (6) Unit conversions: trade −8% → −8 index points (baseline 100); gold +40% → +$800/oz (baseline $2,000); yield +350 bps → +3.5 (% units). (7) `global_financial_volatility` (+80% VIX) → `global_credit_spread` +96 ± 36 bps (80% of the 120 bps baseline). (8) `[country].regime_stability` −10 → `protest_intensity_annual` +10 (sign flipped; observable replacement); `gulf` → `gulf_states`. (9) Dropped rows, channel kept in prose: `global_gdp_growth` (aggregate of country rows, not a state variable), `dxy_index` (no FX variable in catalog), `usa.debt_service_pct_revenue` (`debt_service_ratio` is derived, not an impact target). (10) Branches via single-scale inheritance from `managed`: `disorderly` ×1.8, `bretton_woods_iii` ×0.6 (the GDP multipliers; per-variable multipliers and half-life changes kept in prose). (11) Cascade `TURKEY_POLITICAL_CRISIS` → `TURKEY_POLITICAL_BREAKDOWN` (registry §3 alias). (12) No `until: resolved` rows, so no `resolves_after`. Restored from history: the original pre-scaling loadings and the "Sum of squared loadings = 0.78" line removed on 2025-12-31. Achieved variance 0.6552 against the declared 0.65 |
