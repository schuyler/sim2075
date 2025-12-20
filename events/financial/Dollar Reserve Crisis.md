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

| Attribute | Value |
|-----------|-------|
| **ID** | DOLLAR_RESERVE_CRISIS |
| **Scale** | Global |
| **Domain** | Economic |
| **Causal Type** | Type 2: Threshold |
| **Onset Speed** | Rapid (1-3 years for full impact transmission) |
| **Reversibility** | Partial (can stabilize at new equilibrium but not fully reverse) |

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

**Current pressure estimate (2025)**: ~45 on 0-100 scale
- Dollar share: 57.7% (moderate pressure)
- Debt-to-GDP: 124% (elevated)
- Foreign Treasury holdings: 30% (declining from 50%+ in 2008)
- Deficit: 6.4% of GDP (high)
- BRICS infrastructure: Early operational (mBridge pilot, SGEI vaults)

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 70 on 0-100 scale | Crisis requires multiple indicators in danger zone simultaneously |
| **Uncertainty** | ±10 (range 60-80) | No historical precedent for reserve currency crisis of this magnitude |
| **Sharpness (k)** | 8 | Moderately sharp—crisis dynamics accelerate near threshold |
| **Historical calibration** | Partial analogs only | UK sterling decline (gradual), Asian crisis 1997 (acute but different), Greek crisis 2010 (acute, smaller scale) |

### Minimum Probability

**Floor**: 0.3% annually even at low pressure

Rationale: Black swan Treasury auction failure possible even with healthy fundamentals. External shocks (major war, terrorist attack on financial infrastructure, sudden loss of Fed credibility) could trigger crisis regardless of pressure level.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 3.0% |
| **Confidence** | Medium-Low |
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

Per [[methodology/reference/priority-event-ranking]]:
- More likely than: AMOC collapse, Russia state failure
- Similar to: Pakistan state failure, Iran regime change
- Less likely than: Global financial crisis, severe pandemic

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.0 | No direct climate linkage |
| F_FIN | 0.7 | **Primary driver**: Financial fragility directly affects Treasury market stress, yield dynamics, reserve demand |
| F_HLTH | 0.0 | No direct health linkage |
| F_GPT | 0.4 | **Secondary**: Geopolitical tensions accelerate reserve diversification, sanctions concerns |
| F_FOOD | 0.0 | No direct food system linkage |
| F_TECH | 0.2 | **Tertiary**: Alternative payment infrastructure (mBridge, CBDC) maturity |
| F_EUR | 0.2 | European stress affects euro as alternative; European positioning matters |
| F_MENA | 0.1 | Petrodollar dynamics; Gulf state positioning |
| F_SAS | 0.0 | Minimal direct linkage |
| F_EAS | 0.2 | Chinese infrastructure development; yuan internationalization pace |
| F_SSA | 0.0 | Minimal direct linkage |
| F_LAM | 0.0 | Minimal direct linkage |

**Sum of squared loadings**: 0.49 + 0.16 + 0.04 + 0.04 + 0.01 + 0.04 = **0.78** ✓

### Loading Rationale

Factors operate by shocking state variables that feed the pressure function:

**F_FIN (0.7)**: High F_FIN draws manifest as Treasury market stress, yield volatility, credit spread widening, and Fed credibility questions. These directly increase fiscal deficit pressure (higher debt service), reduce foreign Treasury holdings (flight to safety elsewhere), and potentially trigger the confidence cascade that defines the crisis event.

**F_GPT (0.4)**: Elevated geopolitical tension accelerates the "sanctions weaponization" concern that drives reserve diversification. The 2022 Russia sanctions precedent demonstrated that dollar reserves can be frozen—high F_GPT years reinforce this lesson and accelerate `usd_reserve_share` decline.

**F_TECH (0.2)**: Technology factor captures alternative payment infrastructure maturity. High F_TECH years may see faster mBridge operationalization, CBDC adoption, or blockchain-based settlement systems that increase `cips_share` and make exit from dollar system more feasible.

**F_EUR (0.2)**: European stress creates complex effects. High F_EUR may weaken euro as alternative (supporting dollar) but also signals broader Western financial system fragility (undermining dollar). Net effect is mild pressure increase.

**F_EAS (0.2)**: East Asian tension and Chinese development affect yuan internationalization pace and Shanghai Gold Exchange infrastructure. High F_EAS may accelerate or impede alternative infrastructure depending on specific manifestation.

---

## Impact Vector

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

---

## Aftermath Branches

The crisis event triggers one of three post-event trajectories, determined by policy response and external conditions.

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

---

## Cascade Effects

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| EU_FRAGMENTATION | +1.5% | 3 years | Stress on euro as sudden alternative; divergent member state responses |
| CHINESE_POLITICAL_CRISIS | +0.5% | 2 years | Export collapse creates economic pressure; legitimacy challenge |
| EGYPT_STATE_FAILURE | +1.0% | 3 years | Dollar debt burden; import cost surge; forex crisis |
| PAKISTAN_STATE_FAILURE | +1.0% | 3 years | Dollar debt burden; import cost surge; IMF conditionality |
| TURKEY_POLITICAL_CRISIS | +0.8% | 3 years | Lira crisis amplification; dollar debt exposure |
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

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-19 |
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
