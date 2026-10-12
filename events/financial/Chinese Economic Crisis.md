---
title: Chinese Economic Crisis
type: note
permalink: events/financial/chinese-economic-crisis
tags:
- event
- financial
- type-2
- threshold
- china
- economic-crisis
- global
- level-1
---

# Chinese Economic Crisis

**Type 2 (Threshold) Event** — Probability rises as property, debt, demographic and external pressures accumulate past the state's capacity to manage them.

## Specification

```yaml
id: CHINESE_ECONOMIC_CRISIS
domain: economic
scale: global
causal_type: 2
onset: sudden
reversibility: partial
```

*Onset speed: rapid (6-18 months from trigger to full crisis), recorded as `sudden` in the schema's `sudden|gradual` enum. Reversibility: partial (structural damage persists but acute phase resolves).*

## Description

Acute systemic economic crisis in China characterized by banking sector distress requiring emergency intervention beyond normal PBOC operations, sharp currency depreciation overwhelming capital controls, and GDP contraction significantly exceeding gradual slowdown trajectory. This represents a discrete state transition from "managed stress" to "acute crisis"—distinct from China's expected demographic-driven deceleration, which belongs in baseline trajectory. The event marks the failure of the managed economy model to contain accumulated imbalances, with severe global transmission through trade, commodity, and financial channels.

---

## Causal Type Specification

### Type 2: Threshold Dynamics

This event exhibits classic threshold behavior: pressure accumulates through multiple reinforcing channels (property sector distress, local government debt, shadow banking losses, demographic headwinds, trade restrictions), and at some critical point, the state's capacity to manage stress is overwhelmed, triggering acute crisis. China's extensive policy toolkit (capital controls, state-owned banks, fiscal capacity) raises the threshold substantially—but once breached, the same opacity that enabled extend-and-pretend accelerates the confidence collapse.

The gradual deterioration of property sector health, local government finances, and demographic support ratios constitutes pressure-building; the crisis is the discrete state transition when these pressures exceed management capacity.

### Pressure Function

Uses universal state variables per [[methodology/reference/state-variables-country]]. China-specific constructs (property sector stress, LGFV debt, banking NPL ratio) are proxied through observable economic and fiscal indicators.

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `chn.debt_public` | 0.25 | logistic(center=80, k=0.1) | Captures overall fiscal stress including hidden liabilities; official figures understate true burden |
| `chn.gdp_growth` | 0.20 | inverse | Economic deceleration signals stress accumulation; growth below 3% triggers confidence concerns |
| `chn.current_account` | 0.15 | inverse | External balance deterioration signals capital outflow pressure and export weakness |
| `chn.reserves_foreign` | 0.15 | inverse | Reserve buffer in months of imports; depletion signals vulnerability to capital flight |
| `chn.fdi_net` | 0.10 | inverse | FDI outflows signal loss of investor confidence; negative FDI is crisis precursor |
| `chn.unemployment_rate` | 0.10 | linear | Labor market stress; elevated unemployment signals domestic demand weakness |
| Working-age population growth (derived) | 0.05 | inverse | Demographic pressure; negative growth increases fiscal burden, reduces dynamism |

The YAML expression in the Probability section below realizes these transforms in the expression language's subset: the debt logistic exactly as specified (`1 / (1 + exp(-0.1 * (debt - 80)))`); the four "inverse" terms as clipped linear ramps that read 0 at a comfortable level and 1 at a crisis level (growth 8% → 0%, current account +4% → −4% of GDP, reserves 20 → 4 months of imports, FDI +2% → −2% of GDP); unemployment as linear to 15%; and the demographic term, which needs a growth rate the namespace cannot see (no history), as the cumulative decline of the derived `chn.pop_working_age` from its ~980M 2025 level, saturating at 800M (the UN medium projection for ~2050).

**Proxy limitations**: The universal variable set cannot directly capture China's distinctive vulnerabilities (property sector = 25-30% of GDP, LGFV hidden debt = 50-60% of GDP, true NPL ratio 3-5× official figures). The pressure function proxies these through their downstream effects: `debt_public` captures fiscal stress, `gdp_growth` captures real economy impact, `current_account` and `fdi_net` capture capital confidence. This is a known fidelity limitation; probability is calibrated primarily via reference class reasoning rather than mechanical pressure calculation.

**Current pressure estimate (2025)**: ~55 on 0-100 scale
- Public debt: ~80% of GDP officially, higher including LGFV (~120%+ by IMF estimates)
- GDP growth: ~4.5%, declining from historical trend
- Current account: Positive but narrowing; services deficit growing
- FX reserves: ~15 months of imports (adequate but no longer growing)
- FDI: Net negative in recent quarters (unprecedented)
- Unemployment: Official 5%, true urban rate likely 8-10%
- Demographics: Working-age population declining ~0.5% annually

At the official figures above the YAML expression gives ~39/100; at the "true" figures the prose already prices in (debt ~120% of GDP including LGFV, urban unemployment ~9%) it gives ~54, consistent with the ~55 judgment estimate. The compiler's pressure-scale check is skipped for this event because every term reads country variables, which carry no 2025 baseline in the state catalog.

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 75 on 0-100 scale | China's policy toolkit (capital controls, state banks, fiscal space) raises threshold substantially above typical EM |
| **Uncertainty** | ±10 (range 65-85) | Opacity makes true vulnerability difficult to assess; could be more fragile or more resilient than appears |
| **Sharpness (k)** | 10 | Sharp transition—once confidence breaks, state tools become liabilities (capital flight accelerates) |
| **Historical calibration** | Asian Financial Crisis 1997 (acute, different structure); Japan 1990 (threshold breach, prolonged stagnation); Argentina 2001 (confidence collapse) |

### Minimum Probability

**Floor**: 0.5% annually even at low pressure

Rationale: Black swan triggers possible even with healthy fundamentals—major geopolitical shock (Taiwan conflict), global financial crisis transmission, or policy error (premature capital account liberalization) could trigger crisis regardless of pressure level. China's opacity means external observers cannot rule out hidden fragilities.

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.25 * (1.0 / (1.0 + exp(-0.1 * (chn.debt_public - 80)))) +
      0.20 * clip((8.0 - chn.gdp_growth) / 8.0, 0.0, 1.0) +
      0.15 * clip((4.0 - chn.current_account) / 8.0, 0.0, 1.0) +
      0.15 * clip((20.0 - chn.reserves_foreign) / 16.0, 0.0, 1.0) +
      0.10 * clip((2.0 - chn.fdi_net) / 4.0, 0.0, 1.0) +
      0.10 * clip(chn.unemployment_rate / 15.0, 0.0, 1.0) +
      0.05 * clip((980.0 - chn.pop_working_age) / 180.0, 0.0, 1.0)
    )
  threshold: 75
  threshold_std: 10
  sharpness: 10
  floor: 0.005
  annual: 0.020
  range: [0.012, 0.035]
  confidence: medium
```

No impact row uses `until: resolved`, so the block carries no `resolves_after`. The sharpness value is the prose's documented k = 10; the engine applies it as `expit(k · (pressure − threshold))` on the 0–100 scale, which is a far sharper transition than the 0.15–0.20 the AMOC and Pakistan events use — see the 2026-10-12 changelog row.

| Metric | Value |
|--------|-------|
| **Annual probability** | 2.0% |
| **Low bound** | 1.2% |
| **High bound** | 3.5% |
| **Confidence** | Medium-Low (recorded as `medium` in YAML: the schema enum is `low|medium|high`) |
| **25-year cumulative** | ~40% at point estimate |

### Derivation

**Step 1: Current pressure assessment**

Current pressure (~55) is elevated but below threshold (~75). Distance to threshold suggests crisis is not imminent but vulnerabilities are substantial. The property sector crisis is already partially underway—question is whether it remains contained or cascades.

**Step 2: Pressure trajectory**

Key pressure drivers are structural and worsening:
- Property sector: No resolution in sight; demand fundamentally impaired by demographics and oversupply
- LGFV debt: Rollover wall approaching; central government bailout capacity finite
- Demographics: Inexorable; working-age population declining 0.5-1% annually
- Trade environment: Likely to remain restrictive regardless of US administration

Pressure likely increases 2-3 points annually, reaching threshold zone (65-85) within 5-10 years under baseline assumptions.

**Step 3: Reference class reasoning**

| Reference | Outcome | Relevance |
|-----------|---------|-----------|
| Japan 1990 | Threshold breach → 30-year stagnation | High: similar credit/property bubble, demographic headwinds |
| Asian Financial Crisis 1997 | Acute crisis, recovery within 2-5 years | Medium: different structure (currency peg, external debt) but similar contagion dynamics |
| China 2015 | Stock market crash, contained by intervention | High: showed both vulnerability and state capacity |
| Argentina 2001 | Confidence collapse, severe depression | Medium: smaller economy, less policy capacity |

Japan 1990 is most analogous: credit-fueled property bubble in aging society with high savings rate. Japan's "lost decades" suggest crisis may be slow-motion rather than acute—but China's growth model dependency and political legitimacy linkage to growth create different dynamics.

**Step 4: Expert/market signals**

- IMF Article IV: Repeatedly flags property sector and LGFV risks
- Major investment banks: ~20-30% probability of "hard landing" over 5 years (implies ~4-6% annual)
- Chinese policy actions: Urgency of "common prosperity," property rescue attempts signal internal concern
- Capital outflow pressure: Persistent despite controls; wealthy Chinese diversifying

**Step 5: Comparative calibration**

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Global Financial Crisis | ~3.0% | More frequent; includes all major financial crises |
| Dollar Reserve Crisis | ~1.5% | Less likely; requires specific reserve currency dynamics |
| Turkey Political Crisis | ~1.0% | Less likely; Turkey has fewer resources to delay |
| Pakistan State Failure | ~1.5% | Similar; both have accumulated structural stress |

Chinese Economic Crisis should be somewhat more likely than Dollar Reserve Crisis (vulnerabilities more acute, less policy space remaining after years of stimulus) but less likely than generic Global Financial Crisis (China's specific dynamics, not just any crisis).

**Step 6: Final estimate**

Combining:
- Pressure trajectory suggests rising probability over simulation horizon
- Reference class (Japan, Asian crisis) suggests 2-4% range
- Market/expert estimates cluster around 4-6% annual for "hard landing"
- Our definition (acute crisis, not just slowdown) is narrower than typical "hard landing"

**Point estimate: 2.0% annually** with range 1.2-3.5%.

This implies ~40% cumulative probability over 25 years—a Chinese economic crisis becomes more likely than not to occur at least once during the simulation horizon.

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- More likely than: Dollar reserve crisis, AMOC weakening, Russia state failure
- Similar to: Pakistan state failure, Iran regime change, Egypt state failure
- Less likely than: Global financial crisis, severe pandemic

### Key Uncertainties

**Factors that could push probability higher**:
- Property sector contagion accelerates beyond policy capacity
- LGFV debt crisis forces central government bailout, exhausting fiscal space
- Taiwan conflict or severe trade war triggers capital flight
- Political transition creates policy paralysis or error
- Hidden banking losses larger than estimated

**Factors that could push probability lower**:
- Successful property sector restructuring (managed demolition of bad debt)
- Productivity growth from technological upgrading offsets demographic drag
- Gradual capital account liberalization allows pressure release
- Global demand recovery supports export sector
- Political stability enables sustained reform implementation

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4, the strongest objections to this specification:

**1. "China is different" (state capacity argument)**

China has unprecedented policy tools: $3T+ FX reserves, state-owned banking system, effective capital controls, and demonstrated willingness to intervene. Every prior crisis prediction (2007, 2015, 2020) has been wrong. The party has successfully extended-and-pretended for 15+ years. The threshold may be far higher than estimated, or the system may be able to absorb stress indefinitely through financial repression.

*Counter*: Japan also had exceptional state capacity and still experienced threshold breach. State tools delay crisis but don't eliminate underlying imbalances. Each intervention consumes policy space.

**2. Japan analogy limitations**

Japan had open capital flows when its bubble burst; China's capital controls fundamentally change the confidence cascade mechanism. The 1990 template may not apply. China can force domestic savers to hold yuan assets indefinitely.

*Counter*: Capital controls are porous under stress (2015-16 saw $1T+ outflows). Elite capital flight occurs regardless. And even without external confidence collapse, domestic confidence can erode (property buyers striking, bank runs in rural areas).

**3. Political economy prevents discontinuity**

CCP prioritizes stability above all else. Evergrande was managed, not allowed to cascade. Every potential crisis trigger gets smothered with intervention. "Crisis" becomes a slow leak rather than acute event. This means the event as specified (acute systemic crisis) may never occur—only gradual decline.

*Counter*: This is the Japan-style Stagnation branch (55% probability). The specification acknowledges most likely outcome is managed decline. But management can fail—political transition, policy error, external shock (Taiwan) could overwhelm tools.

**4. No relevant reference class**

China at 18% of global GDP with unique political economy may have no historical comparables. Japan, Asian crisis, Argentina are all structurally different. We may be reasoning from false analogies.

*Counter*: All forecasting involves imperfect analogies. The reference class captures common elements (credit bubble, property dependence, demographic reversal) even if scale differs. Acknowledging uncertainty (medium-low confidence, 1.2-3.5% range) reflects this limitation.

### Probability Evolution

For Type 2 events, probability varies with pressure accumulation over the simulation horizon. The 2.0% annual probability is a period average; actual probability is lower early and higher late.

| Period | Estimated Pressure | Annual Probability | Rationale |
|--------|-------------------|-------------------|-----------|
| 2025-2030 | 55 → 65 | ~1.5% | Current stress elevated but below threshold; policy tools still effective |
| 2030-2040 | 65 → 75 | ~2.0% | Pressure enters threshold zone; demographic decline accelerates; policy space narrowing |
| 2040-2050 | 75 → 85 | ~2.5-3.0% | Threshold likely breached; cumulative stress from demographics, debt, and reduced growth |
| 2050-2075 | 85+ | ~3.0%+ | If no crisis by 2050, either pressure very high (crisis likely) or China found sustainable path (reduce probability) |

**Implementation note**: Current methodology uses fixed annual probabilities. Time-varying Type 2 probabilities are a Phase 2 roadmap item. The values above inform intuition about how probability evolves but are not mechanically implemented in v1.0.

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_CLIM** | 0.07 | Climate stress affects agricultural output, infrastructure costs, regional development |
| **F_FIN** | 0.40 | **Primary**: Global financial conditions affect capital flows, contagion risk, investor sentiment; truly exogenous to China |
| **F_HLTH** | 0.04 | Pandemic aftermath affects consumer confidence, services sector |
| **F_GPT** | 0.22 | **Secondary**: Trade tensions, tech restrictions, geopolitical risk premium |
| **F_FOOD** | 0.04 | Food security concerns add fiscal pressure, affect rural stability |
| **F_TECH** | 0.15 | Semiconductor restrictions, tech war affects growth sectors, investment |
| **F_EUR** | 0.07 | European demand affects exports; European financial stress affects global sentiment |
| F_MENA | 0.0 | Minimal direct linkage |
| **F_SAS** | 0.04 | Regional trade linkages |
| **F_EAS** | 0.33 | **Secondary**: Regional dynamics (Korea, Japan, Taiwan stress) that transmit to China through trade/investment; excludes China-driven component to avoid circularity |
| F_SSA | 0.0 | Minimal direct linkage (China is creditor, not affected) |
| F_LAM | 0.0 | Minimal direct linkage |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.74 from original loadings

**Original (pre-allocation) loadings**, as first specified on 2025-12-29: F_FIN 0.55, F_EAS 0.45, F_GPT 0.30, F_TECH 0.20, F_CLIM 0.10, F_EUR 0.10, F_HLTH 0.05, F_FOOD 0.05, F_SAS 0.05 (F_MENA, F_SSA, F_LAM 0.0). Sum of squared loadings: 0.3025 + 0.2025 + 0.09 + 0.04 + 0.01 + 0.01 + 0.0025 + 0.0025 + 0.0025 = **0.66** ✓ — the pre-Ω check the 2025-12-31 variance allocation replaced; the Loading Rationale below still quotes these original values.

```yaml
factors:
  F_FIN: 0.40   # Primary: global financial conditions, capital flows, contagion; exogenous to China
  F_EAS: 0.33   # Secondary: non-China regional stress (Korea, Japan, Taiwan) via trade/investment
  F_GPT: 0.22   # Secondary: trade tensions, tech restrictions, geopolitical risk premium
  F_TECH: 0.15  # Semiconductor restrictions, tech war
  F_CLIM: 0.07  # Agricultural output, infrastructure costs, regional development
  F_EUR: 0.07   # European demand for exports; European financial stress
  F_HLTH: 0.04  # Pandemic aftermath, consumer confidence
  F_FOOD: 0.04  # Food security adds fiscal pressure, rural stability
  F_SAS: 0.04   # Regional trade linkages
variance: 0.65  # Type 2 target
```

F_MENA, F_SSA and F_LAM carry no loading (minimal direct linkage; China is creditor to SSA, not affected by it). With the catalog's Ω the listed loadings achieve (ΛΩΛᵀ)ᵢᵢ = 0.645.

### Loading Rationale

Factors operate by shocking state variables that feed the pressure function. A key design principle: factors should represent *exogenous* conditions that affect China, not conditions *caused by* China. This avoids tautological circularity.

**F_FIN (0.55)**: Global financial fragility is the primary driver because it is genuinely exogenous to China. High F_FIN years feature tighter global liquidity (Fed tightening), wider credit spreads, reduced risk appetite for EM assets, and potential contagion from other financial crises. These conditions stress China's dollar-denominated corporate debt (~$1T), reduce FDI inflows, and increase capital outflow pressure. Global financial stress also reduces external demand, amplifying domestic property/consumption weakness. F_FIN captures the external financial environment that China cannot control.

**F_EAS (0.45)**: East Asian regional stress affects China through trade and investment channels—but we must avoid the circularity of "Chinese stress causes F_EAS which causes Chinese crisis." The loading here captures the *non-China* components of regional stress: Korean financial instability, Japanese recession, Taiwan supply chain disruption, or broader Asian contagion originating elsewhere. High F_EAS years see regional conditions that reduce demand for Chinese exports, disrupt supply chains, and create capital flow volatility—external shocks that increase pressure on China's already-stressed system.

**F_GPT (0.30)**: Great power tension directly affects China through trade restrictions, technology access, and investment uncertainty. High F_GPT years see intensified US-China friction—tariffs, semiconductor export controls, investment screening, potential secondary sanctions. These reduce export revenue, constrain technological upgrading, and create political pressure for nationalist response. Trade war escalation directly feeds pressure function through export performance variable.

**F_TECH (0.20)**: Technology disruption and restriction affects China's growth model. High F_TECH years may see accelerated semiconductor restrictions, AI compute limitations, or alternatively breakthrough innovations that China captures or is excluded from. Technology restrictions particularly affect high-value manufacturing, R&D investment returns, and the "common prosperity" sectors Beijing has prioritized.

---

## Impact Vector

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| *global_gdp_growth* | ↓ | -1.5 ± 0.6 pp | immediate | decaying: half_life=2yr, floor=-0.3 |
| `global_trade_volume` | ↓ | -6 ± 3% | immediate | decaying: half_life=2yr, floor=-2% |
| *commodity_price_index* | ↓ | -25 ± 10% | immediate | decaying: half_life=3yr |
| `oil_price` | ↓ | -20 ± 10% | immediate | decaying: half_life=2yr |
| `copper_price` | ↓ | -30 ± 12% | immediate | decaying: half_life=3yr |
| *global_financial_volatility* | ↑ | +50 ± 20% (VIX equivalent) | immediate | decaying: half_life=1yr |
| `cny_reserve_share` | ↓ | -1.5 ± 0.8 pp | gradual(3yr) | permanent |

### China Impacts

*Variables marked with * are illustrative but not tracked in the v1.0 state model. They document expected real-world effects for completeness and potential Level 2 expansion.*

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.gdp_real` | ↓ | -8 ± 3% (cumulative over 2-3 years) | gradual(2yr) | decaying: half_life=5yr, floor=-4% |
| `chn.gdp_growth` | ↓ | -4 ± 1.5 pp (relative to trend) | immediate | decaying: half_life=3yr |
| `chn.unemployment_rate` | ↑ | +6 ± 2 pp | delayed(6mo) | decaying: half_life=4yr |
| `chn.inflation_rate` | ↑ | +4 ± 2 pp (currency depreciation) | delayed(3mo) | decaying: half_life=2yr |
| `chn.debt_public` | ↑ | +15 ± 5 pp GDP (bailouts, stimulus) | gradual(2yr) | permanent |
| `chn.reserves_foreign` | ↓ | -6 ± 2 months of imports | gradual(2yr) | permanent |
| `chn.fdi_net` | ↓ | -3 ± 1 pp GDP | immediate | decaying: half_life=3yr |
| `chn.protest_intensity_annual` | ↑ | +25 ± 10 | delayed(6mo) | decaying: half_life=3yr |
| `chn.years_since_irregular_transition` | — | Potential reset to 0 (Hard Landing branch only) | conditional | regime-dependent |
| *chn.youth_unemployment* | ↑ | +12 ± 5 pp | delayed(6mo) | decaying: half_life=5yr |
| *cny_usd_rate* | ↓ | -25 ± 10% (depreciation) | immediate | permanent (new equilibrium -15%) |
| *chn.fx_reserves_usd* | ↓ | -$800B ± 300B | gradual(2yr) | permanent |
| *chn.property_prices* | ↓ | -35 ± 12% (national average) | gradual(3yr) | permanent |
| *chn.household_wealth* | ↓ | -25 ± 10% | gradual(2yr) | decaying: half_life=8yr |

**Political stress transmission**: Economic crisis increases political stress through observable indicators rather than synthetic `regime_stability`. The primary channels are elevated `protest_intensity_annual` (economic grievances), potential cabinet reshuffles (`cabinet_turnover_annual`), and in severe cases (Hard Landing branch), irregular political transition that would reset `years_since_irregular_transition` to zero.

### Regional Impacts

**East Asia (Japan, Korea, Taiwan):**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].gdp_growth` | ↓ | -2.0 ± 0.8 pp | delayed(3mo) | decaying: half_life=2yr |
| `[country].exports` | ↓ | -12 ± 5% | immediate | decaying: half_life=2yr |

Korea most exposed (China = 25% of exports); Japan and Taiwan significant but more diversified.

**Hong Kong (illustrative — not a modeled entity):**

*Hong Kong is not among the 40 individually modeled countries or 12 regional aggregates. The impacts below document expected real-world effects for completeness. In the simulation, Hong Kong effects would transmit through the broader East Asian regional dynamics and global financial system variables.*

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| *hkg.gdp_growth* | ↓ | -5.0 ± 2.0 pp | immediate | decaying: half_life=3yr |
| *hkg.property_prices* | ↓ | -30 ± 12% | immediate | permanent |
| *hkg.banking_stress* | ↑ | Significant | immediate | decaying: half_life=3yr |
| *hkg.unemployment_rate* | ↑ | +4 ± 1.5 pp | delayed(3mo) | decaying: half_life=3yr |

Hong Kong is uniquely exposed through direct financial integration with mainland, property market linkage, and role as offshore yuan center. Banking sector faces acute stress from mainland corporate exposures. Property prices, already elevated, face severe correction as mainland capital flows reverse and local demand collapses. The "one country, two systems" financial architecture provides limited insulation when the crisis originates in the dominant economy.

**Simulation treatment**: Hong Kong's financial system stress would manifest through `global_credit_spread` increases and capital flow effects on regional economies (Japan, Korea, Singapore). Hong Kong-specific dynamics are a potential Level 2 refinement if entity coverage expands.

**Southeast Asia (ASEAN aggregate):**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `asean.gdp_growth` | ↓ | -1.5 ± 0.6 pp | delayed(3mo) | decaying: half_life=2yr |
| *asean.fdi_inflows* | ↑ | +15 ± 8% | delayed(1yr) | permanent |

Mixed impact: demand shock from China but supply chain relocation accelerates (Vietnam, Indonesia benefit from "China+1" strategies).

**Australia:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `aus.gdp_growth` | ↓ | -2.5 ± 1.0 pp | immediate | decaying: half_life=2yr |
| *aus.terms_of_trade* | ↓ | -20 ± 8% | immediate | decaying: half_life=3yr |

Severe exposure through commodity exports (iron ore, coal, LNG). Australia's first recession in 30+ years likely.

**Europe:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `deu.gdp_growth` | ↓ | -1.0 ± 0.4 pp | delayed(6mo) | decaying: half_life=2yr |
| `[eu_countries].gdp_growth` | ↓ | -0.6 ± 0.3 pp | delayed(6mo) | decaying: half_life=2yr |

Germany most exposed through automotive and machinery exports; broader EU affected through German supply chains and reduced Chinese investment.

**United States:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `usa.gdp_growth` | ↓ | -0.5 ± 0.3 pp | delayed(6mo) | decaying: half_life=2yr |
| *usa.corporate_profits_china_exposed* | ↓ | -15 ± 6% | immediate | decaying: half_life=2yr |
| *usa.inflation_rate* | ↓ | -0.5 ± 0.3 pp | delayed(6mo) | decaying: half_life=1yr |

Moderate direct impact due to limited trade exposure (~8% of exports), but financial contagion and multinational earnings effects matter. Lower commodity prices are deflationary tailwind.

**Commodity Exporters (Brazil, Chile, South Africa, Indonesia, Russia):**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].gdp_growth` | ↓ | -2.0 ± 1.0 pp | immediate | decaying: half_life=2yr |
| `[country].fiscal_balance` | ↓ | -3 ± 1.5 pp GDP | immediate | decaying: half_life=3yr |

Severe terms-of-trade shock; fiscal stress from reduced resource revenues.

**Belt and Road Debtor Countries:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| *bri_debt_relief_probability* | ↑ | +20 ± 10 pp | delayed(1yr) | permanent |

Crisis may force China to restructure BRI loans, providing debt relief to African/Asian borrowers—a rare positive second-order effect.

### Differential Impacts

**Exposure variable**: `country.china_export_share`

**Function**: linear

**Effect**: Countries with >15% of exports to China experience amplified GDP impacts (1.5× magnitude). High exposure countries: Australia, Korea, Taiwan, Chile, Brazil, Angola.

**Exposure variable**: `country.commodity_export_share`

**Function**: linear

**Effect**: Commodity-dependent exporters experience additional terms-of-trade shock proportional to commodity share of exports.

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| China GDP level | decaying | half_life=5yr, floor=-4% | Permanent structural damage; lost investment, human capital scarring |
| China property prices | permanent | — | Demographic fundamentals don't support recovery; Japan precedent |
| China FX reserves | permanent | — | Spent defending currency; rebuilding takes decades |
| Regional GDP | decaying | half_life=2yr | Trading partners recover as China stabilizes |
| Commodity prices | decaying | half_life=3yr | Demand eventually stabilizes at lower level |
| Global trade volume | decaying | half_life=2yr, floor=-2% | Supply chain restructuring creates permanent friction |
| Yuan reserve share | permanent | — | Crisis damages internationalization project |
| ASEAN FDI | permanent | — | Supply chain relocation is structural |

### Impact Derivation

**Method**: Analog-based with transmission analysis

**Primary analogs**:
- Japan 1990-1995: Property bubble burst; GDP impact ~-2% level, but Japan's crisis was slow-motion
- Asian Financial Crisis 1997: Regional transmission; affected countries saw 5-15% GDP contractions
- Global Financial Crisis 2008: Financial contagion mechanisms; commodity price collapse
- China 2015: Stock market intervention; limited real economy impact but showed contagion potential

**China-specific considerations**:
- Larger economy than 1997 Asian crisis countries (18% of global GDP vs. <5%)
- Less external debt exposure than 1997 (crisis is domestic-driven)
- Greater state capacity than typical EM (can prevent worst-case scenarios)
- But higher global integration means larger transmission multiplier
- Property sector more important than in Japan (household wealth concentration)

**Commodity price transmission**: China consumes ~50% of global copper, ~55% of iron ore, ~15% of oil. Demand collapse of 20-30% implies severe price impact.

### Impact Specification

The YAML below re-expresses the tables above in state-catalog names and units; the tables keep the original magnitudes, sub-year onsets and durability floors. Mapping decisions:

- **Units**: `chn.gdp_real` is a fraction of current value (−8% ± 3% → `[-0.08, 0.03]`); every other row is additive in the variable's units. Percentages on absolute-unit variables are converted against the catalog's 2025 baselines: `global_trade_volume` −6 ± 3% of index 100 → −6 ± 3 points; `oil_price` −20 ± 10% of Brent $75 → `oil_brent` −15 ± 7.5 $/bbl; `copper_price` −30 ± 12% of $8,500/t → −2,550 ± 1,020 $/t.
- **Onset**: the schema's onset is annual; the tables' 3- and 6-month delays are written `immediate`, the 2- and 3-year ramps as `{gradual: N}`.
- **Entities**: `[country]` East Asia → `jpn`, `kor`, `twn`; `asean` (not a catalog aggregate) → `vnm`, `tha`, `phl`, `sgp` and `southeast_asia_other`, with Indonesia carried under the commodity-exporter rows instead (the larger of its two memberships); `[eu_countries]` → `fra`, `ita`, `esp`, `nld`, `pol` and `eu_other` (Germany has its own row; the UK is not an EU member); Chile (not an entity) → the `andean_caribbean` aggregate that contains it and Peru.
- **Variables**: `[country].fiscal_balance` is not in the catalog; the row is carried on `tax_revenue_gdp` (same units, % of GDP, same durability), since the stated mechanism is "reduced resource revenues". `usa.inflation_rate` is included although the table starred it: the catalog does track `inflation_rate`.
- **Rows kept in prose only**: starred illustrative variables (`global_gdp_growth`, `commodity_price_index`, `global_financial_volatility`, `chn.youth_unemployment`, `cny_usd_rate`, `chn.fx_reserves_usd`, `chn.property_prices`, `chn.household_wealth`, `asean.fdi_inflows`, `aus.terms_of_trade`, `usa.corporate_profits_china_exposed`, `bri_debt_relief_probability`, all Hong Kong rows); `[country].exports` (no exports variable in the catalog); and the conditional reset of `chn.years_since_irregular_transition` to 0 on the Hard Landing branch, which is a value reset rather than an additive impact and has no v0.1 form.
- **Branches**: the Japan-style Stagnation branch is the ×1.0 base. Hard Landing and Reform Breakthrough are written as explicit lists rather than `inherit`/`scale` because their modifiers are per-category: Hard Landing multiplies GDP rows ×1.8, unemployment ×2.0, currency (`chn.inflation_rate`, the depreciation proxy) ×1.6 and every non-China country row ×1.5 (regional transmission), leaving global and other China rows at ×1.0; Reform Breakthrough multiplies GDP rows ×0.7 and shortens every half-life by 40% (×0.6), leaving magnitudes otherwise unchanged. The post-event factor-loading modifications in the branch descriptions are not a v0.1 construct and stay in prose.

```yaml
impacts:
  stagnation:
    # Global
    - {var: global_trade_volume,             mag: [-6, 3],         onset: immediate,     decay: 2}
    - {var: oil_brent,                       mag: [-15, 7.5],      onset: immediate,     decay: 2}
    - {var: copper_price,                    mag: [-2550, 1020],   onset: immediate,     decay: 3}
    - {var: cny_reserve_share,               mag: [-1.5, 0.8],     onset: {gradual: 3},  permanent: true}
    # China
    - {var: chn.gdp_real,                    mag: [-0.08, 0.03],   onset: {gradual: 2},  decay: 5}
    - {var: chn.gdp_growth,                  mag: [-4, 1.5],       onset: immediate,     decay: 3}
    - {var: chn.unemployment_rate,           mag: [6, 2],          onset: immediate,     decay: 4}
    - {var: chn.inflation_rate,              mag: [4, 2],          onset: immediate,     decay: 2}
    - {var: chn.debt_public,                 mag: [15, 5],         onset: {gradual: 2},  permanent: true}
    - {var: chn.reserves_foreign,            mag: [-6, 2],         onset: {gradual: 2},  permanent: true}
    - {var: chn.fdi_net,                     mag: [-3, 1],         onset: immediate,     decay: 3}
    - {var: chn.protest_intensity_annual,    mag: [25, 10],        onset: immediate,     decay: 3}
    # East Asia
    - {var: jpn.gdp_growth,                  mag: [-2, 0.8],       onset: immediate,     decay: 2}
    - {var: kor.gdp_growth,                  mag: [-2, 0.8],       onset: immediate,     decay: 2}
    - {var: twn.gdp_growth,                  mag: [-2, 0.8],       onset: immediate,     decay: 2}
    # Southeast Asia (ASEAN members in the catalog; Indonesia carried under commodity exporters)
    - {var: vnm.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 2}
    - {var: tha.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 2}
    - {var: phl.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 2}
    - {var: sgp.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 2}
    - {var: southeast_asia_other.gdp_growth, mag: [-1.5, 0.6],     onset: immediate,     decay: 2}
    # Australia
    - {var: aus.gdp_growth,                  mag: [-2.5, 1],       onset: immediate,     decay: 2}
    # Europe
    - {var: deu.gdp_growth,                  mag: [-1, 0.4],       onset: immediate,     decay: 2}
    - {var: fra.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 2}
    - {var: ita.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 2}
    - {var: esp.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 2}
    - {var: nld.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 2}
    - {var: pol.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 2}
    - {var: eu_other.gdp_growth,             mag: [-0.6, 0.3],     onset: immediate,     decay: 2}
    # United States
    - {var: usa.gdp_growth,                  mag: [-0.5, 0.3],     onset: immediate,     decay: 2}
    - {var: usa.inflation_rate,              mag: [-0.5, 0.3],     onset: immediate,     decay: 1}
    # Commodity exporters (Chile via the Andean/Caribbean aggregate)
    - {var: bra.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 2}
    - {var: zaf.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 2}
    - {var: idn.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 2}
    - {var: rus.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 2}
    - {var: andean_caribbean.gdp_growth,     mag: [-2, 1],         onset: immediate,     decay: 2}
    - {var: bra.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 3}
    - {var: zaf.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 3}
    - {var: idn.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 3}
    - {var: rus.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 3}
    - {var: andean_caribbean.tax_revenue_gdp, mag: [-3, 1.5],      onset: immediate,     decay: 3}

  hard_landing:
    # Global (x1.0)
    - {var: global_trade_volume,             mag: [-6, 3],         onset: immediate,     decay: 2}
    - {var: oil_brent,                       mag: [-15, 7.5],      onset: immediate,     decay: 2}
    - {var: copper_price,                    mag: [-2550, 1020],   onset: immediate,     decay: 3}
    - {var: cny_reserve_share,               mag: [-1.5, 0.8],     onset: {gradual: 3},  permanent: true}
    # China (GDP x1.8, unemployment x2.0, currency x1.6, other x1.0)
    - {var: chn.gdp_real,                    mag: [-0.144, 0.054], onset: {gradual: 2},  decay: 5}
    - {var: chn.gdp_growth,                  mag: [-7.2, 2.7],     onset: immediate,     decay: 3}
    - {var: chn.unemployment_rate,           mag: [12, 4],         onset: immediate,     decay: 4}
    - {var: chn.inflation_rate,              mag: [6.4, 3.2],      onset: immediate,     decay: 2}
    - {var: chn.debt_public,                 mag: [15, 5],         onset: {gradual: 2},  permanent: true}
    - {var: chn.reserves_foreign,            mag: [-6, 2],         onset: {gradual: 2},  permanent: true}
    - {var: chn.fdi_net,                     mag: [-3, 1],         onset: immediate,     decay: 3}
    - {var: chn.protest_intensity_annual,    mag: [25, 10],        onset: immediate,     decay: 3}
    # Regional transmission (x1.5)
    - {var: jpn.gdp_growth,                  mag: [-3, 1.2],       onset: immediate,     decay: 2}
    - {var: kor.gdp_growth,                  mag: [-3, 1.2],       onset: immediate,     decay: 2}
    - {var: twn.gdp_growth,                  mag: [-3, 1.2],       onset: immediate,     decay: 2}
    - {var: vnm.gdp_growth,                  mag: [-2.25, 0.9],    onset: immediate,     decay: 2}
    - {var: tha.gdp_growth,                  mag: [-2.25, 0.9],    onset: immediate,     decay: 2}
    - {var: phl.gdp_growth,                  mag: [-2.25, 0.9],    onset: immediate,     decay: 2}
    - {var: sgp.gdp_growth,                  mag: [-2.25, 0.9],    onset: immediate,     decay: 2}
    - {var: southeast_asia_other.gdp_growth, mag: [-2.25, 0.9],    onset: immediate,     decay: 2}
    - {var: aus.gdp_growth,                  mag: [-3.75, 1.5],    onset: immediate,     decay: 2}
    - {var: deu.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 2}
    - {var: fra.gdp_growth,                  mag: [-0.9, 0.45],    onset: immediate,     decay: 2}
    - {var: ita.gdp_growth,                  mag: [-0.9, 0.45],    onset: immediate,     decay: 2}
    - {var: esp.gdp_growth,                  mag: [-0.9, 0.45],    onset: immediate,     decay: 2}
    - {var: nld.gdp_growth,                  mag: [-0.9, 0.45],    onset: immediate,     decay: 2}
    - {var: pol.gdp_growth,                  mag: [-0.9, 0.45],    onset: immediate,     decay: 2}
    - {var: eu_other.gdp_growth,             mag: [-0.9, 0.45],    onset: immediate,     decay: 2}
    - {var: usa.gdp_growth,                  mag: [-0.75, 0.45],   onset: immediate,     decay: 2}
    - {var: usa.inflation_rate,              mag: [-0.75, 0.45],   onset: immediate,     decay: 1}
    - {var: bra.gdp_growth,                  mag: [-3, 1.5],       onset: immediate,     decay: 2}
    - {var: zaf.gdp_growth,                  mag: [-3, 1.5],       onset: immediate,     decay: 2}
    - {var: idn.gdp_growth,                  mag: [-3, 1.5],       onset: immediate,     decay: 2}
    - {var: rus.gdp_growth,                  mag: [-3, 1.5],       onset: immediate,     decay: 2}
    - {var: andean_caribbean.gdp_growth,     mag: [-3, 1.5],       onset: immediate,     decay: 2}
    - {var: bra.tax_revenue_gdp,             mag: [-4.5, 2.25],    onset: immediate,     decay: 3}
    - {var: zaf.tax_revenue_gdp,             mag: [-4.5, 2.25],    onset: immediate,     decay: 3}
    - {var: idn.tax_revenue_gdp,             mag: [-4.5, 2.25],    onset: immediate,     decay: 3}
    - {var: rus.tax_revenue_gdp,             mag: [-4.5, 2.25],    onset: immediate,     decay: 3}
    - {var: andean_caribbean.tax_revenue_gdp, mag: [-4.5, 2.25],   onset: immediate,     decay: 3}

  reform:
    # Global (x1.0, half-lives x0.6)
    - {var: global_trade_volume,             mag: [-6, 3],         onset: immediate,     decay: 1.2}
    - {var: oil_brent,                       mag: [-15, 7.5],      onset: immediate,     decay: 1.2}
    - {var: copper_price,                    mag: [-2550, 1020],   onset: immediate,     decay: 1.8}
    - {var: cny_reserve_share,               mag: [-1.5, 0.8],     onset: {gradual: 3},  permanent: true}
    # China (GDP x0.7, half-lives x0.6)
    - {var: chn.gdp_real,                    mag: [-0.056, 0.021], onset: {gradual: 2},  decay: 3}
    - {var: chn.gdp_growth,                  mag: [-2.8, 1.05],    onset: immediate,     decay: 1.8}
    - {var: chn.unemployment_rate,           mag: [6, 2],          onset: immediate,     decay: 2.4}
    - {var: chn.inflation_rate,              mag: [4, 2],          onset: immediate,     decay: 1.2}
    - {var: chn.debt_public,                 mag: [15, 5],         onset: {gradual: 2},  permanent: true}
    - {var: chn.reserves_foreign,            mag: [-6, 2],         onset: {gradual: 2},  permanent: true}
    - {var: chn.fdi_net,                     mag: [-3, 1],         onset: immediate,     decay: 1.8}
    - {var: chn.protest_intensity_annual,    mag: [25, 10],        onset: immediate,     decay: 1.8}
    # Regional transmission (x1.0, half-lives x0.6)
    - {var: jpn.gdp_growth,                  mag: [-2, 0.8],       onset: immediate,     decay: 1.2}
    - {var: kor.gdp_growth,                  mag: [-2, 0.8],       onset: immediate,     decay: 1.2}
    - {var: twn.gdp_growth,                  mag: [-2, 0.8],       onset: immediate,     decay: 1.2}
    - {var: vnm.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 1.2}
    - {var: tha.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 1.2}
    - {var: phl.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 1.2}
    - {var: sgp.gdp_growth,                  mag: [-1.5, 0.6],     onset: immediate,     decay: 1.2}
    - {var: southeast_asia_other.gdp_growth, mag: [-1.5, 0.6],     onset: immediate,     decay: 1.2}
    - {var: aus.gdp_growth,                  mag: [-2.5, 1],       onset: immediate,     decay: 1.2}
    - {var: deu.gdp_growth,                  mag: [-1, 0.4],       onset: immediate,     decay: 1.2}
    - {var: fra.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 1.2}
    - {var: ita.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 1.2}
    - {var: esp.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 1.2}
    - {var: nld.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 1.2}
    - {var: pol.gdp_growth,                  mag: [-0.6, 0.3],     onset: immediate,     decay: 1.2}
    - {var: eu_other.gdp_growth,             mag: [-0.6, 0.3],     onset: immediate,     decay: 1.2}
    - {var: usa.gdp_growth,                  mag: [-0.5, 0.3],     onset: immediate,     decay: 1.2}
    - {var: usa.inflation_rate,              mag: [-0.5, 0.3],     onset: immediate,     decay: 0.6}
    - {var: bra.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 1.2}
    - {var: zaf.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 1.2}
    - {var: idn.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 1.2}
    - {var: rus.gdp_growth,                  mag: [-2, 1],         onset: immediate,     decay: 1.2}
    - {var: andean_caribbean.gdp_growth,     mag: [-2, 1],         onset: immediate,     decay: 1.2}
    - {var: bra.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 1.8}
    - {var: zaf.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 1.8}
    - {var: idn.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 1.8}
    - {var: rus.tax_revenue_gdp,             mag: [-3, 1.5],       onset: immediate,     decay: 1.8}
    - {var: andean_caribbean.tax_revenue_gdp, mag: [-3, 1.5],      onset: immediate,     decay: 1.8}
```

*Durability note: the tables' decay-to-floor forms (China GDP level floor −4%, global trade floor −2%, global GDP growth floor −0.3 pp) are schema v0.2 backlog; the YAML uses plain half-lives. The differential-exposure multipliers (1.5× for >15% China export share; commodity share scaling) remain an implementation coefficient documented in prose, as in [[events/health/severe-pandemic]].*

---

## Aftermath Branches

The crisis event triggers one of three post-event trajectories, determined by policy response and structural adaptation.

```yaml
branches:
  - {id: hard_landing, p: 0.30, desc: "Policy intervention fails; banking recapitalization beyond fiscal capacity; capital flight overwhelms controls"}
  - {id: stagnation,   p: 0.55, desc: "Japan-style: acute collapse prevented but structural issues unaddressed; decade-plus near-zero growth"}
  - {id: reform,       p: 0.15, desc: "Crisis forces genuine structural reform; sharp contraction then V-shaped recovery"}
```

### Branch Probability Calibration Note

**Entropy maximization default**: With three branches and no calibrating data, the principled default would be 33.3% / 33.3% / 33.3%.

**Ordinal adjustment rationale**: We deviate from entropy based on structural reasoning about historical precedent and state capacity:

| Branch | Historical Frequency | Structural Factors |
|--------|---------------------|-------------------|
| Hard Landing | Rare for large economies with state capacity | China has tools; but may be overwhelmed |
| Japan-style Stagnation | Common for credit/property bubbles | Most likely given demographic similarity, policy pattern |
| Reform Breakthrough | Rare; requires crisis to force change | Possible but requires political conditions |

Japan 1990 is the most analogous case: credit-fueled property bubble in an aging society with high savings and state capacity. Japan's outcome was prolonged stagnation—neither collapse nor reform breakthrough. This suggests P(Stagnation) > P(Hard Landing) > P(Reform).

**Cardinal uncertainty**: The ordering is more defensible than specific probabilities. Values below respect the ordering while acknowledging we cannot distinguish between, say, 25/60/15 and 35/50/15 on principled grounds.

### Branch 1: Hard Landing

**Probability given event**: 30%

**Trigger conditions**: Policy intervention fails; banking system requires recapitalization beyond fiscal capacity; capital flight overwhelms controls; political instability

**Trajectory**:
- GDP contracts 12-18% over 2-3 years
- Unemployment reaches 15-20% (including migrant workers)
- Yuan depreciates 40-50% despite intervention
- FX reserves depleted to critical levels (<$1T)
- Social unrest in affected regions; political stress
- Potential CCP legitimacy crisis; leadership challenge

**Impact modifiers** (multiply base impacts):
- GDP impact: ×1.8
- Unemployment impact: ×2.0
- Currency depreciation: ×1.6
- Regional transmission: ×1.5

**Factor modifications during aftermath**:
- F_EAS: +0.4 loading for 5 years (severe regional stress)
- F_FIN: +0.3 loading for 3 years (global financial contagion)
- F_GPT: +0.2 loading for 5 years (geopolitical instability from Chinese weakness/nationalism)

### Branch 2: Japan-style Stagnation

**Probability given event**: 55%

**Trigger conditions**: State intervention prevents acute collapse but fails to address structural issues; extend-and-pretend continues; demographic headwinds dominate

**Trajectory**:
- GDP contracts 5-8% then stagnates near zero growth for decade+
- "Zombification" of banking sector; NPLs hidden but constraining
- Property prices decline 30-40% then stagnate (no recovery)
- Youth unemployment remains elevated (15-20%) long-term
- Gradual managed decline in living standards vs. expectations
- Political stability maintained through nationalism, control

**Distinguishing from baseline trajectory**: The baseline assumes China's demographic-driven slowdown proceeds *gradually* without discrete crisis—growth declines from ~5% to ~2-3% over 15 years, property prices decline 15-20% over a decade, and adjustment is managed. The post-crisis stagnation branch differs in:

| Marker | Baseline Trajectory | Post-Crisis Stagnation |
|--------|--------------------|-----------------------|
| GDP contraction | None (gradual slowdown) | 5-8% discrete drop |
| Property price decline | -15-20% over 10 years | -30-40% within 3 years |
| Growth rate (post-adjustment) | 2-3% | ~0% for decade |
| Banking sector | Stressed but functional | Zombified; NPLs constrain lending |
| Unemployment spike | Gradual rise | Sharp spike (+6 pp) then elevated plateau |
| Trigger | No discrete event | Confidence cascade / policy failure |

The crisis event is the discrete threshold-crossing; the stagnation branch describes a post-crisis equilibrium that is *worse* than what baseline trajectory would have produced.

**Impact modifiers**: Base case (×1.0)

**Factor modifications during aftermath**:
- F_EAS: +0.2 loading for 10 years (prolonged regional drag)
- F_FIN: +0.1 loading for 5 years (mild ongoing stress)

### Branch 3: Reform Breakthrough

**Probability given event**: 15%

**Trigger conditions**: Crisis forces genuine structural reform; property sector restructured; SOE reform proceeds; capital allocation improves; productivity growth resumes

**Trajectory**:
- Sharp initial contraction (6-10%) but V-shaped recovery
- Banking sector recapitalized with genuine NPL resolution
- Property sector finds new equilibrium at sustainable levels
- Labor market reforms improve allocation
- Growth resumes at 3-4% (lower but sustainable)
- Transition to consumption-led model succeeds

**Impact modifiers** (reduce base impacts):
- GDP impact: ×0.7
- Duration: half-lives reduced by 40%
- Recovery: V-shaped rather than L-shaped

**Factor modifications during aftermath**:
- F_EAS: +0.1 loading for 2 years (short-term stress only)
- F_FIN: No modification (contained crisis)

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - {event: CHINESE_POLITICAL_CRISIS,  delta: 0.020,  years: 5}
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.015,  years: 2}
    - {event: DOLLAR_RESERVE_CRISIS,     delta: -0.010, years: 5}
    - {event: TAIWAN_CONFLICT,           delta: 0.004,  years: 3}
    - {event: PAKISTAN_STATE_FAILURE,    delta: 0.005,  years: 3}
    - {event: EGYPT_STATE_FAILURE,       delta: 0.003,  years: 3}
    - {event: RUSSIA_STATE_FAILURE,      delta: 0.003,  years: 3}
    - {event: SAUDI_REGIME_INSTABILITY,  delta: 0.003,  years: 3}
    - {event: KOREAN_PENINSULA_CRISIS,   delta: 0.004,  years: 3}
  triggered_by:
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.020}
    - {event: TAIWAN_CONFLICT,           delta: 0.030}
    - {event: US_CHINA_ECONOMIC_RUPTURE, delta: 0.010}   # prose: US_CHINA_TRADE_WAR, registry alias
    - {event: SEVERE_PANDEMIC,           delta: 0.008}
    - {event: DOLLAR_RESERVE_CRISIS,     delta: 0.010}
```

The TAIWAN_CONFLICT edge is the unconditional net +0.4%; the branch-dependent variants discussed in the special case below (+1.0% or more under Hard Landing, −0.5% under Reform Breakthrough) are hedged illustrations, not specification, and stay in prose.

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| CHINESE_POLITICAL_CRISIS | +2.0% | 5 years | Economic failure challenges CCP performance legitimacy; see Task 2.1.13 |
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 2 years | Financial contagion; EM stress; risk-off sentiment |
| DOLLAR_RESERVE_CRISIS | -1.0% | 5 years | Yuan alternative becomes less viable; flight to dollar safety |
| TAIWAN_CONFLICT | +0.4% | 3 years | Nationalist distraction dynamics likely outweigh capacity constraints; see special case below |
| PAKISTAN_STATE_FAILURE | +0.5% | 3 years | BRI debt burden; reduced Chinese support capacity |
| EGYPT_STATE_FAILURE | +0.3% | 3 years | Reduced Chinese investment; commodity price effects |
| RUSSIA_STATE_FAILURE | +0.3% | 3 years | Reduced Chinese economic support; commodity revenue collapse |
| SAUDI_REGIME_INSTABILITY | +0.3% | 3 years | Oil price collapse stresses fiscal model |
| KOREAN_PENINSULA_CRISIS | +0.4% | 3 years | Regional instability; potential DPRK opportunism |

### Taiwan Conflict Special Case

The effect on Taiwan Conflict probability requires careful reasoning about competing dynamics:

**Factors reducing probability**:
- Reduced military modernization budget (fiscal constraints)
- Economic crisis creates domestic priority
- International reputation cost if seen as distraction
- Reduced capacity for sustained conflict

**Factors increasing probability**:
- Nationalist distraction from economic failure (historical pattern: regimes under domestic pressure turn to external conflicts)
- "Window closing" logic (act before further weakness erodes capabilities)
- Military pressure as regime legitimacy substitute when economic performance fails
- Hardliner faction gains influence from crisis; reformers discredited

**Net assessment: +0.4% with high uncertainty**

We assign a small positive effect because the historical pattern of nationalist mobilization during domestic crises is strong, and CCP legitimacy is unusually tied to performance metrics that a crisis would undermine. The "rally around the flag" dynamic is well-documented across authoritarian regimes facing internal stress.

However, uncertainty is high because this depends heavily on leadership faction dynamics, crisis severity, and international context. A Hard Landing branch (with severe political stress) might see +1.0% or higher; a Reform Breakthrough branch might see -0.5% (successful reform reduces need for nationalist distraction).

### Triggered By (Probability Increases)

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +2.0% | Capital flight; external demand collapse; contagion |
| TAIWAN_CONFLICT | +3.0% | Sanctions, trade disruption, investor flight |
| US_CHINA_TRADE_WAR (alias; canonical `US_CHINA_ECONOMIC_RUPTURE` per [[events/backlog-registry]] §3) | +1.0% | Export collapse; supply chain disruption; tech restrictions |
| SEVERE_PANDEMIC | +0.8% | Demand shock; healthcare spending; confidence |
| DOLLAR_RESERVE_CRISIS | +1.0% | Global financial disruption; but yuan gains may partially offset |

### Impact Chains

**Chain 1**: Chinese Economic Crisis → Commodity price collapse → Resource exporter stress
- Crisis sharply reduces Chinese commodity demand
- Iron ore, copper, oil prices fall 20-30%
- Australia, Brazil, Chile, Indonesia, Russia face fiscal stress
- Political instability in commodity-dependent economies

**Chain 2**: Chinese Economic Crisis → Supply chain disruption → Global manufacturing stress
- Crisis disrupts Chinese manufacturing (labor unrest, firm failures)
- Global supply chains face acute shortages
- Accelerated reshoring/friendshoring
- Short-term inflation spike; long-term supply chain restructuring

**Chain 3**: Chinese Economic Crisis → EM financial contagion → Broader crisis
- Investors flee EM assets broadly (risk-off)
- EM currencies depreciate; debt stress emerges
- Potential cascade into Global Financial Crisis

**Chain 4**: Chinese Economic Crisis → BRI debt stress → African/Asian debt relief
- China loses capacity/willingness to extend BRI credit
- Existing BRI loans restructured (debt relief)
- Debtor countries gain fiscal space but lose infrastructure investment
- IMF/World Bank increase relative influence

---

## Transmission Channels

### 1. Trade Channel (Primary)

**Mechanism**: China is the largest trading partner for >120 countries. Crisis reduces Chinese import demand sharply. Export-dependent economies face demand shock.

**Magnitude**: Each 1% Chinese GDP contraction → ~0.2-0.3% reduction in trading partner exports to China. For highly exposed countries (Australia, Korea), effect is 2-3× larger.

**Affected regions**: East Asia (severe), Australia (severe), Europe (moderate), Americas (mild)

**Affected variables**: `[country].exports`, `[country].gdp_growth`, `[country].current_account`

### 2. Commodity Channel

**Mechanism**: China consumes dominant share of industrial commodities. Demand collapse causes price crash. Commodity exporters face terms-of-trade shock.

**Magnitude**: Chinese construction/manufacturing contraction of 20% → commodity price declines of 25-35% for base metals, 15-25% for energy.

**Affected regions**: Australia, Latin America (Chile, Brazil, Peru), Sub-Saharan Africa, Russia, Middle East

**Affected variables**: `[country].terms_of_trade`, `[country].fiscal_revenue`, `commodity_prices`

### 3. Financial Contagion Channel

**Mechanism**: Crisis triggers risk-off sentiment. Investors flee EM assets broadly. Dollar strengthens. Credit spreads widen. Potential margin calls and deleveraging cascade.

**Magnitude**: Comparable to 2015 episode but potentially larger. EM currency depreciation 10-20%; EM equity decline 20-30%.

**Affected regions**: All emerging markets, particularly those with external financing needs

**Affected variables**: `[country].currency`, `[country].equity_valuations`, `[country].credit_spreads`

### 4. Supply Chain Channel

**Mechanism**: Chinese manufacturing disruption (firm failures, labor unrest, logistics breakdown) creates shortages in global supply chains. Affects intermediate goods, consumer electronics, industrial equipment.

**Magnitude**: Specific sectors (electronics, automotive, machinery) may face 10-30% supply disruption for 6-18 months.

**Affected regions**: Global, but particularly US, Europe, Japan (dependent on Chinese manufacturing)

**Affected variables**: `global_manufacturing_output`, `[country].inflation`, `[country].industrial_production`

### 5. Investment Channel

**Mechanism**: Chinese outward FDI collapses. BRI investment halts. Property investment in major cities (Sydney, Vancouver, London) declines.

**Magnitude**: Chinese outward FDI falls 50-70% from crisis onset. Property markets in Chinese-buyer-dependent cities decline 5-15%.

**Affected regions**: BRI recipient countries, global cities with Chinese property investment

**Affected variables**: `[country].fdi_inflows`, `[city].property_prices`

### 6. Confidence Channel

**Mechanism**: Crisis damages "China model" credibility. Emerging markets reassess development strategies. Global growth expectations decline.

**Magnitude**: Difficult to quantify. May shift development discourse away from state-directed model.

**Affected regions**: Global, particularly developing countries considering development models

**Affected variables**: Business confidence indices, investment growth rates

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-29
  review: complete
  upgrade: true
```

Critical review completed 2025-12-29.

### Upgrade Rationale

High-impact event with extensive existing research; Level 2 could add China-specific tracking variables (property sector, LGFV debt, NPL ratios) for mechanical pressure calculation rather than reference-class calibration.

## Sources

- IMF Article IV Consultations — China (various years)
- People's Bank of China — Financial Stability Reports
- Rhodium Group — China economic analysis
- Peterson Institute for International Economics — China research
- Michael Pettis (Carnegie) — China financial imbalances analysis
- Logan Wright (Rhodium) — Local government debt research
- World Bank — China Economic Update series
- [[research/21st-century-assessment]] — Demographic and regional trajectory analysis

## Open Questions

1. **True NPL ratio**: What is the actual non-performing loan ratio in Chinese banks? Official figures (~1.6%) are widely considered unreliable. True ratio could be 5-15%, dramatically affecting threshold estimates.

2. **LGFV resolution mechanism**: How will local government financing vehicle debt be resolved? Central government bailout, restructuring, or default cascade? Resolution mechanism affects crisis severity.

3. **Capital control effectiveness**: How effective are China's capital controls under acute stress? 2015-2016 showed $1T+ outflows despite controls. In crisis, could accelerate dramatically.

4. **Property sector equilibrium**: Where does property sector stabilize? Japan precedent suggests 50-70% decline possible over long period. Chinese household wealth concentration in property makes this critical.

5. **Political economy of response**: Will CCP prioritize stability (extend-and-pretend) or reform (take short-term pain)? Historical pattern strongly suggests stability, implying Japan-style stagnation.

6. **Taiwan interaction**: Does economic crisis increase or decrease Taiwan conflict probability? Arguments exist both ways; may depend on leadership faction dynamics.

7. **Global policy response**: Will major economies coordinate response (swap lines, IMF involvement) or engage in beggar-thy-neighbor policies? Affects global transmission.

8. **Supply chain resilience**: How quickly can global supply chains adapt to Chinese disruption? COVID experience suggests 6-18 months for major adjustments.

9. **Time-varying probability**: The 2.0% annual probability is an average across the simulation horizon, but pressure is increasing over time. Early years (2025-2030) might be ~1.5% while later years (2040-2050) might be ~3.0%+ as pressure approaches threshold. Current methodology uses fixed annual probabilities; time-varying Type 2 probabilities are a roadmap item.

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Verified critical review complete | Task 2.4 systematic review |
| 2025-12-29 | Full Level 1 specification with critical review | Task 2.1 financial crisis events |
| 2025-12-31 | Variance allocation: scaled loadings to Type 2 target | Task 3.11 — scale factor 0.74; replaced the original sum-of-squares check (0.66) with (ΛΩΛᵀ)ᵢᵢ = 0.65 |
| 2026-10-12 | Migrated to YAML-embedded schema; restored lost prose | Task 4.2 format migration. Prose restored from history: the original pre-allocation loadings and their sum-of-squares line (0.66), condensed away on 2025-12-31, now sit beside the factor YAML; the 2025-12-31 change itself gained a changelog row. Judgment calls: (1) `onset: sudden` for the prose's "rapid (6-18 months)"; `confidence: medium` for "Medium-Low" (enum), wording kept. (2) Pressure transforms realized with `exp`/`clip` (sentence under the pressure table); the demographic term reads the derived `chn.pop_working_age` as cumulative decline from 980M because a growth rate needs history the namespace lacks; expression gives ~39 at official 2025 figures, ~54 at the prose's "true" figures. Compiler's baseline check skipped (country variables). (3) `sharpness: 10` kept as documented although the engine's `expit(k·Δ)` makes it a near-step versus 0.15–0.20 elsewhere — flagged for review, not changed. (4) No `until: resolved` rows, so no `resolves_after`. (5) Durability: decay-to-floor rows (China GDP floor −4%, trade floor −2%) written as plain decays; the conditional `years_since_irregular_transition` reset and the aftermath factor-loading modifications are not v0.1 constructs and stay in prose. (6) Unit conversions against 2025 baselines: trade −6% → −6 index points; oil −20% → `oil_brent` −15 ± 7.5 $/bbl; copper −30% → −2,550 ± 1,020 $/t; sub-year onsets → `immediate`. (7) Entity alternatives: `asean` → `vnm`/`tha`/`phl`/`sgp`/`southeast_asia_other` (Indonesia under commodity exporters); `[eu_countries]` → `fra`/`ita`/`esp`/`nld`/`pol`/`eu_other`; Chile → `andean_caribbean`. (8) Variable alternatives: `fiscal_balance` → `tax_revenue_gdp` (same units; mechanism is revenue loss); `usa.inflation_rate` included despite the table's asterisk (the catalog tracks it). (9) Dropped rows, kept in prose: `[country].exports` (no catalog variable), all starred illustrative variables, Hong Kong (not an entity), BRI debt-relief probability. (10) Branches explicit per branch rather than `inherit`/`scale` because Hard Landing and Reform modifiers are per-category (GDP ×1.8/×0.7, unemployment ×2.0, currency ×1.6, regional ×1.5, Reform half-lives ×0.6); unlisted categories ×1.0. (11) Cascades: all nine targets exist as files; `US_CHINA_TRADE_WAR` normalized to `US_CHINA_ECONOMIC_RUPTURE` (registry alias); Taiwan edge unconditional at +0.4%. Achieved variance 0.645 against the 0.65 target |

---

*Cross-references*: [[methodology/reference/causal-types]], [[methodology/reference/probability-estimation]], [[methodology/reference/factor-loadings]], [[events/financial/global-financial-crisis]], [[events/financial/dollar-reserve-crisis]], [[events/geopolitical/taiwan-conflict]], [[research/21st-century-assessment]]