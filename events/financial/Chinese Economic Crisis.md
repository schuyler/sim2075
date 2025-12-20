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

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | CHINESE_ECONOMIC_CRISIS |
| **Scale** | Global |
| **Domain** | Economic |
| **Causal Type** | Type 2: Threshold |
| **Onset Speed** | Rapid (6-18 months from trigger to full crisis) |
| **Reversibility** | Partial (structural damage persists but acute phase resolves) |

## Description

Acute systemic economic crisis in China characterized by banking sector distress requiring emergency intervention beyond normal PBOC operations, sharp currency depreciation overwhelming capital controls, and GDP contraction significantly exceeding gradual slowdown trajectory. This represents a discrete state transition from "managed stress" to "acute crisis"—distinct from China's expected demographic-driven deceleration, which belongs in baseline trajectory. The event marks the failure of the managed economy model to contain accumulated imbalances, with severe global transmission through trade, commodity, and financial channels.

---

## Causal Type Specification

### Type 2: Threshold Dynamics

This event exhibits classic threshold behavior: pressure accumulates through multiple reinforcing channels (property sector distress, local government debt, shadow banking losses, demographic headwinds, trade restrictions), and at some critical point, the state's capacity to manage stress is overwhelmed, triggering acute crisis. China's extensive policy toolkit (capital controls, state-owned banks, fiscal capacity) raises the threshold substantially—but once breached, the same opacity that enabled extend-and-pretend accelerates the confidence collapse.

The gradual deterioration of property sector health, local government finances, and demographic support ratios constitutes pressure-building; the crisis is the discrete state transition when these pressures exceed management capacity.

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| *property_sector_stress* | 0.30 | linear | Real estate = ~25-30% of GDP; Evergrande-style contagion; household wealth concentration |
| *lgfv_debt_to_gdp* | 0.25 | linear | Local government financing vehicle debt; hidden fiscal liabilities; rollover risk |
| *banking_npl_ratio* | 0.20 | threshold(8%) | Non-performing loans; accelerates above 8% as confidence erodes |
| `chn.working_age_population_growth` | 0.15 | inverse | Demographic pressure; negative growth increases fiscal burden, reduces dynamism |
| *fx_reserve_adequacy* | 0.10 | inverse | Reserves relative to short-term external debt + import cover; capital flight buffer |

*Note: Variables in italics are not in current state-specification and would need to be added or derived. `property_sector_stress` could be constructed from housing price indices, developer default rates, and construction activity. `lgfv_debt_to_gdp` requires aggregation of local government financing vehicle liabilities. `banking_npl_ratio` official figures are widely considered understated; true ratio likely 2-3× reported.*

**Current pressure estimate (2025)**: ~55 on 0-100 scale
- Property sector: Severe stress (Evergrande, Country Garden defaults; prices falling in most cities)
- LGFV debt: ~50-60% of GDP (IMF estimates); rollover increasingly difficult
- Banking NPLs: Officially ~1.6%, true ratio likely 5-8%
- Demographics: Working-age population declining since 2012; accelerating
- FX reserves: $3.2T nominal but $1T+ illiquid; adequate but declining buffer

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

| Metric | Value |
|--------|-------|
| **Annual probability** | 2.0% |
| **Low bound** | 1.2% |
| **High bound** | 3.5% |
| **Confidence** | Medium-Low |
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

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.10 | Climate stress affects agricultural output, infrastructure costs, regional development |
| F_FIN | 0.45 | **Secondary**: Global financial conditions affect capital flows, contagion risk, investor sentiment |
| F_HLTH | 0.05 | Pandemic aftermath affects consumer confidence, services sector |
| F_GPT | 0.30 | **Tertiary**: Trade tensions, tech restrictions, geopolitical risk premium |
| F_FOOD | 0.05 | Food security concerns add fiscal pressure, affect rural stability |
| F_TECH | 0.20 | Semiconductor restrictions, tech war affects growth sectors, investment |
| F_EUR | 0.10 | European demand affects exports; European financial stress affects global sentiment |
| F_MENA | 0.0 | Minimal direct linkage |
| F_SAS | 0.05 | Regional trade linkages |
| F_EAS | 0.70 | **Primary**: China IS the primary driver of East Asian stress; regional contagion, supply chains |
| F_SSA | 0.0 | Minimal direct linkage (China is creditor, not affected) |
| F_LAM | 0.0 | Minimal direct linkage |

**Sum of squared loadings**: 0.49 + 0.20 + 0.09 + 0.04 + 0.01 + 0.01 + 0.01 + 0.0025 + 0.0025 + 0.0025 = **0.76** ✓

### Loading Rationale

Factors operate by shocking state variables that feed the pressure function:

**F_EAS (0.70)**: China is the core of East Asian economic dynamics. High F_EAS draws manifest as regional supply chain disruption, reduced intra-Asian trade, property market stress (Hong Kong linkage), and capital flow volatility. Importantly, F_EAS is partially *caused by* Chinese stress, creating feedback—but the factor also captures regional dynamics (Korea, Japan, Taiwan) that independently affect China through trade and investment channels. High F_EAS years see the regional conditions that make Chinese crisis more likely.

**F_FIN (0.45)**: Global financial fragility affects China through multiple channels. High F_FIN years feature tighter global liquidity (Fed tightening), wider credit spreads, reduced risk appetite for EM assets, and potential contagion from other financial crises. These conditions stress China's dollar-denominated corporate debt (~$1T), reduce FDI inflows, and increase capital outflow pressure. Global financial stress also reduces external demand, amplifying domestic property/consumption weakness.

**F_GPT (0.30)**: Great power tension directly affects China through trade restrictions, technology access, and investment uncertainty. High F_GPT years see intensified US-China friction—tariffs, semiconductor export controls, investment screening, potential secondary sanctions. These reduce export revenue, constrain technological upgrading, and create political pressure for nationalist response (potentially including Taiwan risk-taking). Trade war escalation directly feeds pressure function through export performance variable.

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

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.gdp_real` | ↓ | -8 ± 3% (cumulative over 2-3 years) | gradual(2yr) | decaying: half_life=5yr, floor=-4% |
| `chn.gdp_growth` | ↓ | -4 ± 1.5 pp (relative to trend) | immediate | decaying: half_life=3yr |
| *chn.unemployment_rate* | ↑ | +6 ± 2 pp | delayed(6mo) | decaying: half_life=4yr |
| *chn.youth_unemployment* | ↑ | +12 ± 5 pp | delayed(6mo) | decaying: half_life=5yr |
| `chn.inflation_rate` | ↑ | +4 ± 2 pp (currency depreciation) | delayed(3mo) | decaying: half_life=2yr |
| *cny_usd_rate* | ↓ | -25 ± 10% (depreciation) | immediate | permanent (new equilibrium -15%) |
| *chn.fx_reserves* | ↓ | -$800B ± 300B | gradual(2yr) | permanent |
| *chn.property_prices* | ↓ | -35 ± 12% (national average) | gradual(3yr) | permanent |
| *chn.household_wealth* | ↓ | -25 ± 10% | gradual(2yr) | decaying: half_life=8yr |
| `chn.regime_stability` | ↓ | -15 ± 8 | delayed(1yr) | decaying: half_life=5yr |

### Regional Impacts

**East Asia (Japan, Korea, Taiwan):**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].gdp_growth` | ↓ | -2.0 ± 0.8 pp | delayed(3mo) | decaying: half_life=2yr |
| `[country].exports` | ↓ | -12 ± 5% | immediate | decaying: half_life=2yr |

Korea most exposed (China = 25% of exports); Japan and Taiwan significant but more diversified.

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

---

## Aftermath Branches

The crisis event triggers one of three post-event trajectories, determined by policy response and structural adaptation.

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

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 2 years | Financial contagion; EM stress; risk-off sentiment |
| DOLLAR_RESERVE_CRISIS | -1.0% | 5 years | Yuan alternative becomes less viable; flight to dollar safety |
| TAIWAN_CONFLICT | Ambiguous | 3 years | Reduced capacity but potential nationalist distraction |
| PAKISTAN_STATE_FAILURE | +0.5% | 3 years | BRI debt burden; reduced Chinese support capacity |
| EGYPT_STATE_FAILURE | +0.3% | 3 years | Reduced Chinese investment; commodity price effects |
| RUSSIA_STATE_FAILURE | +0.3% | 3 years | Reduced Chinese economic support; commodity revenue collapse |
| SAUDI_REGIME_INSTABILITY | +0.3% | 3 years | Oil price collapse stresses fiscal model |
| KOREAN_PENINSULA_CRISIS | +0.4% | 3 years | Regional instability; potential DPRK opportunism |

### Taiwan Conflict Special Case

The effect on Taiwan Conflict probability is genuinely ambiguous:

**Factors reducing probability**:
- Reduced military modernization budget (fiscal constraints)
- Economic crisis creates domestic priority
- International reputation cost if seen as distraction
- Reduced capacity for sustained conflict

**Factors increasing probability**:
- Nationalist distraction from economic failure
- "Window closing" logic (act before further weakness)
- Military pressure as regime legitimacy substitute
- Hardliner faction gains from crisis

**Net assessment**: Model as ±0.5% with high uncertainty; could go either direction depending on leadership response.

### Triggered By (Probability Increases)

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +2.0% | Capital flight; external demand collapse; contagion |
| TAIWAN_CONFLICT | +3.0% | Sanctions, trade disruption, investor flight |
| US_CHINA_TRADE_WAR | +1.0% | Export collapse; supply chain disruption; tech restrictions |
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

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-20 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | High-impact event with extensive existing research; Level 2 could model property sector dynamics, LGFV debt resolution scenarios, and banking system stress testing in greater detail |

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

---

*Cross-references*: [[methodology/reference/causal-types]], [[methodology/reference/probability-estimation]], [[methodology/reference/factor-loadings]], [[events/financial/global-financial-crisis]], [[events/financial/dollar-reserve-crisis]], [[events/geopolitical/taiwan-conflict]], [[research/21st-century-assessment]]