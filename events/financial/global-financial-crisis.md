---
title: global-financial-crisis
type: note
permalink: events/financial/global-financial-crisis
tags:
- event
- type-2
- threshold
- financial
- economic
- global
- level-1
- hybrid
---

# Global Financial Crisis

**Type 2 (Threshold) Event with Type 1 Floor** — Probability increases as financial pressure accumulates, but maintains meaningful base rate even at low pressure.

This specification demonstrates hybrid Type 1/2 calibration—events with both historical base rates AND state-conditioned probability dynamics.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | GLOBAL_FINANCIAL_CRISIS |
| **Scale** | Global |
| **Domain** | Economic |
| **Causal Type** | **Type 2: Threshold** (with Type 1 floor) |
| **Onset Speed** | Sudden (weeks to months from trigger to acute phase) |
| **Reversibility** | Partial (financial losses permanent; systemic function recovers) |

## Description

Systemic financial crisis causing ≥10% peak-to-trough decline in global equity markets, credit market seizure, AND requiring coordinated central bank/government intervention. Distinguished from normal market corrections by systemic contagion and institutional stress.

This is a **state transition**: `global.financial_stability` crosses below crisis threshold, triggering acute deleveraging, credit contraction, and institutional stress across multiple major economies simultaneously.

**What marks occurrence**: Multiple major financial institutions face insolvency or require emergency support; interbank lending freezes; central banks initiate emergency liquidity facilities; equity markets decline >20% within weeks.

---

## Causal Type Specification (Type 2: Threshold with Floor)

### Why Hybrid Type 1/2?

Financial crises exhibit both patterns:
- **Type 1 (base rate)**: Even well-regulated systems experience periodic crises; some triggers are exogenous (geopolitical shocks, pandemics, natural disasters)
- **Type 2 (threshold)**: Probability rises dramatically as leverage, asset bubbles, and imbalances accumulate

Modeling approach: Type 2 pressure function with elevated floor (1.5%/year) representing irreducible base rate.

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `global.private_debt_gdp` | 0.25 | threshold(250) | Sharp increase above 250% private debt/GDP |
| `global.asset_valuation_deviation` | 0.25 | linear | Distance from historical valuation norms (CAPE, etc.) |
| `global.credit_growth_3yr` | 0.20 | exponential | Rapid credit expansion precedes crises |
| `global.leverage_financial_sector` | 0.15 | linear | Bank/shadow bank leverage ratios |
| `global.current_account_imbalances` | 0.10 | linear | Capital flow imbalances create fragility |
| `global.interest_rate_deviation` | 0.05 | inverse | Low rates → reach for yield → risk accumulation |

**Pressure calculation**:
```
pressure = 0.25 × debt_threshold_function(private_debt_gdp)
         + 0.25 × asset_valuation_deviation / 100
         + 0.20 × exp_transform(credit_growth_3yr)
         + 0.15 × leverage_financial_sector / 100
         + 0.10 × current_account_imbalances / 100
         + 0.05 × inverse_transform(interest_rate_deviation)
```
*Normalized to 0-100 scale*

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 65 (on 0-100 pressure scale) |
| **Uncertainty** | ±12 |
| **Sharpness (k)** | 0.15 (moderate; crises can occur across range of pressure levels) |
| **Historical calibration** | 2008 GFC (pressure ~80), 1997 Asian Crisis (pressure ~60), 2000 Dot-com (pressure ~55) |

### Minimum Probability (Type 1 Floor)

**Floor**: 1.5%/year

Even with low systemic pressure, exogenous shocks can trigger crises:
- Geopolitical events (war, sanctions) disrupting financial flows
- Pandemic-induced sudden stops
- Natural disasters affecting financial centers
- Policy errors by major central banks
- Fraud/failure of systemically important institution

This floor represents the irreducible Type 1 base rate.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 3.0% |
| **At low pressure (floor)** | 1.5% |
| **At high pressure** | 8-12% |
| **Confidence** | Medium |
| **25-year cumulative** | ~55% at point estimate |

### Current Pressure Estimate

Current pressure: ~55/100 (elevated but below threshold)
- `private_debt_gdp`: ~260% (above threshold in major economies)
- `asset_valuation_deviation`: ~+25% (elevated but not extreme)
- `credit_growth_3yr`: moderate (post-2022 tightening)
- `leverage_financial_sector`: ~reduced post-2008 regulation
- `current_account_imbalances`: ~moderate
- `interest_rate_deviation`: normalizing from ZIRP era

### Derivation

**Historical base rate (Type 1 component)**:
| Crisis | Year | Severity |
|--------|------|----------|
| Great Depression | 1929 | Catastrophic |
| Oil Shock recession | 1973 | Severe |
| Latin American debt | 1982 | Severe (regional) |
| Black Monday | 1987 | Moderate (rapid recovery) |
| Asian Financial Crisis | 1997 | Severe (regional, contagion) |
| Dot-com crash | 2000 | Moderate |
| Global Financial Crisis | 2008 | Severe |
| COVID shock | 2020 | Moderate (rapid policy response) |

Observation period: 1929-2024 (95 years)
Severe+ global crises: ~5-6
Base rate: ~5%/decade or ~2-3%/year

**State-conditioned adjustment (Type 2 component)**:
- Current pressure ~55/100
- Sigmoid function: P = floor + (ceiling - floor) × sigmoid(pressure - threshold)
- At pressure 55, threshold 65: probability ~3%

### Comparative Ranking

Per [[methodology/priority-event-ranking]]:
- More likely than: AMOC collapse (~0.5%), severe pandemic (~2%)
- Similar to: Major regional conflict (~3-5%)
- Less likely than: Minor recession (~15%), market correction (~25%)

Financial crises are "once per decade" events at current pressure levels.

### Key Uncertainties

- **Shadow banking**: Less regulated sector may have hidden leverage
- **Central bank capacity**: Balance sheets already expanded; less room for intervention
- **Interconnection complexity**: Derivatives, cross-border flows create unknown linkages
- **China financial system**: Opacity makes pressure assessment difficult
- **Cryptocurrency/DeFi**: New transmission channels, untested under stress

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_FIN** | 0.80 | Dominant: this IS the financial instability factor expressing itself |
| **F_GPT** | 0.30 | Great power tension → sanctions, trade disruption, capital flow disruption |
| **F_EAS** | 0.25 | China financial stress is major global risk; regional contagion |
| **F_EUR** | 0.20 | Eurozone fragmentation risk; banking sector vulnerabilities |
| **F_CLIM** | 0.15 | Climate physical risks → stranded assets, insurance losses |
| **F_TECH** | 0.10 | Tech bubble dynamics; algorithmic trading amplification |
| F_HLTH | 0.00 | Pandemic trigger captured in Type 1 floor, not factor loading |
| F_FOOD | 0.00 | Indirect effect via inflation already in pressure function |
| F_SAS | 0.00 | Marginal to global financial system |
| F_MENA | 0.00 | Oil price channel captured elsewhere |
| F_SSA | 0.00 | Marginal to global financial system |
| F_LAM | 0.00 | Contagion risk lower post-1990s reforms |

**Sum of squared loadings**: 0.87 ✓

### Loading Interpretation (Type 2)

Factors shock state variables that feed into pressure function:
- High F_FIN → credit conditions tighten → `leverage` increases as rollover fails → pressure rises
- High F_GPT → capital flight, sanctions → `current_account_imbalances` spike → pressure rises
- High F_EAS → China stress → `asset_valuation` falls, contagion → pressure rises
- High F_EUR → eurozone stress → banking sector pressure → European component of global pressure rises

---

## Severity Branches

Financial crises vary substantially in severity. Once crisis occurs, severity is determined:

```yaml
severity_branches:

  - id: moderate
    probability: 0.45
    description: |
      2000 dot-com or 2020 COVID-shock scale: Sharp market decline (25-40%),
      credit tightening, but rapid policy response prevents systemic collapse.
      Recovery within 2-3 years. Limited real economy spillover.
      
    impact_multiplier: 1.0  # baseline
    
    factor_modifications:
      F_FIN: +0.35
      F_GPT: +0.10
      
    duration:
      type: decaying
      half_life_years: 2
      floor: 0.05

  - id: severe
    probability: 0.40
    description: |
      2008 GFC or 1997 Asian Crisis scale: Major institutional failures,
      credit market seizure, significant real economy impact.
      Requires massive policy intervention. Recovery takes 5-7 years.
      Permanent loss of some financial capacity.
      
    impact_multiplier: 2.5
    
    factor_modifications:
      F_FIN: +0.60
      F_GPT: +0.25
      F_EUR: +0.20
      F_EAS: +0.20
      
    duration:
      type: decaying
      half_life_years: 5
      floor: 0.15

  - id: catastrophic
    probability: 0.15
    description: |
      1929 Great Depression scale: Systemic collapse across multiple major
      economies. Policy response inadequate or counterproductive.
      Decade-scale recovery. Permanent institutional restructuring.
      Potential political/social cascades.
      
    impact_multiplier: 6.0
    
    factor_modifications:
      F_FIN: +1.00
      F_GPT: +0.50
      F_EUR: +0.40
      F_EAS: +0.40
      
    duration:
      type: decaying
      half_life_years: 10
      floor: 0.25
      
    cascade_triggers:
      - event_id: STATE_FAILURE_VULNERABLE
        probability_modifier: 2.0
        rationale: "Economic devastation triggers political instability"
      - event_id: POLITICAL_EXTREMISM_RISE
        probability_modifier: 2.5
        rationale: "1930s pattern: depression → political radicalization"

severity_probability_rationale: |
  Distribution based on historical crisis severity and policy response capacity:
  
  - Moderate (0.45): Post-2008 regulatory improvements and central bank
    experience make rapid response more likely. 2020 COVID shock showed
    ability to stabilize quickly. Most crises now contained before systemic.
    
  - Severe (0.40): 2008-scale events still plausible despite improvements.
    Shadow banking, interconnection, and novel instruments create channels
    for contagion that regulation hasn't fully addressed.
    
  - Catastrophic (0.15): Requires policy failure (1930s-style procyclical
    response) OR unprecedented shock overwhelming response capacity.
    Less likely given institutional learning, but tail risk remains.
    Could arise from: China hard landing + eurozone crisis + US political
    dysfunction preventing response.
```

---

## Impact Vector

### Global Impacts (Baseline: Moderate Branch)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.gdp_real` | ↓ | -3% ± 1.5% | immediate | decaying (half_life: 2yr) |
| `global.equity_markets` | ↓ | -35% ± 12% | immediate | decaying (half_life: 1.5yr) |
| `global.credit_availability` | ↓ | -25% ± 10% | immediate | decaying (half_life: 2yr) |
| `global.trade_volume` | ↓ | -10% ± 5% | delayed(3mo) | decaying (half_life: 2yr) |
| `global.unemployment` | ↑ | +2pp ± 1pp | delayed(6mo) | decaying (half_life: 3yr) |
| `global.sovereign_debt` | ↑ | +10pp ± 5pp | delayed(1yr) | shock_vulnerable |

*Scale by impact_multiplier for severe (2.5×) and catastrophic (6.0×) branches*

### Regional Differential Impacts

**Exposure variables**: Financial sector size, current account balance, policy space

| Region | GDP Multiplier | Rationale |
|--------|----------------|-----------|
| Financial centers (US, UK, CH) | 1.2× | Direct exposure to financial sector losses |
| Current account deficit (emerging) | 1.5× | Capital flight, currency crisis risk |
| Current account surplus (DE, CN, JP) | 0.8× | Buffers against capital flight |
| Commodity exporters | 1.3× | Demand collapse hits commodity prices |

### Durability Specifications

| Impact Type | Durability | Parameters | Rationale |
|-------------|------------|------------|-----------|
| Market losses | decaying | half_life: 1.5yr | Markets recover faster than real economy |
| GDP contraction | decaying | half_life: 2yr | Standard recovery pattern |
| Unemployment | decaying | half_life: 3yr | Labor market adjustment slower |
| Sovereign debt | shock_vulnerable | vulnerable_to: [growth, inflation] | Can be reduced by growth or inflated away |
| Institutional failures | permanent | N/A | Failed institutions don't return |
| Regulatory changes | maintenance_required | annual_failure: 8% | Regulations erode over time (1930s→2008 pattern) |

### Impact Derivation

Primary method: **Historical analog scaling**

| Analog | GDP Impact | Market Decline | Recovery Time |
|--------|------------|----------------|---------------|
| 2008 GFC | -4% global | -55% (S&P) | 4-5 years |
| 2000 Dot-com | -1% (US) | -45% (NASDAQ) | 2-3 years |
| 1997 Asian | -2% Asia, spillover | -15% global | 2-3 years |
| 1929 Depression | -27% (US) | -85% | 10+ years |
| 2020 COVID | -3% | -35% | <1 year (policy) |

2008 GFC serves as primary anchor for severe branch; 2020 for moderate.

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Credit contraction → sovereign stress | SOVEREIGN_DEBT_CRISIS | +3%/year | 5 years | Bank bailouts → fiscal stress |
| Economic stress → state failure | STATE_FAILURE_VULNERABLE | +1.5%/year per affected state | 5 years | Fiscal exhaustion, legitimacy crisis |
| Unemployment → political instability | POLITICAL_CRISIS_DOMESTIC | +2%/year (multiple countries) | 5 years | Economic grievance → populism |
| Risk-off → emerging market crisis | EMERGING_MARKET_CRISIS | +4%/year | 3 years | Capital flight, currency crisis |
| Deleveraging → deflation | DEFLATION_SPIRAL | +2%/year | 3 years | Debt deflation dynamics |

### Impact Chains

**Pathway 1**: Financial crisis → Sovereign debt crisis → Austerity → Political crisis
```
GFC → bank bailouts → sovereign debt spike → fiscal austerity → 
social unrest → P(political instability) ↑
```

**Pathway 2**: Financial crisis → Emerging market contagion → Regional instability
```
GFC → risk-off sentiment → capital flight from EM → currency crises →
import collapse → P(state failure in vulnerable states) ↑
```

**Pathway 3**: Financial crisis → Deflation → Prolonged stagnation
```
GFC → deleveraging → demand collapse → deflation pressure →
debt burden increases → P(deflation spiral) ↑
```

---

## Transmission Channels

### Credit Channel

**Mechanism**: Banks and shadow banks reduce lending; credit spreads widen
**Affected regions**: All, especially credit-dependent economies
**Affected variables**: `investment`, `consumption`, `housing`, `corporate_debt_rollover`
**Differential exposure**: Private debt levels, banking sector health

### Wealth Effect Channel

**Mechanism**: Asset price declines reduce household/corporate wealth
**Affected regions**: All, especially high-equity-ownership economies
**Affected variables**: `consumption`, `retirement_security`, `collateral_values`
**Differential exposure**: Equity ownership rates, pension fund exposure

### Trade Finance Channel

**Mechanism**: Letters of credit and trade finance dry up
**Affected regions**: Trade-dependent economies
**Affected variables**: `exports`, `imports`, `supply_chains`
**Differential exposure**: Trade openness, reliance on imported inputs

### Confidence Channel

**Mechanism**: Uncertainty leads to postponed investment and consumption
**Affected regions**: All
**Affected variables**: `business_investment`, `consumer_durables`, `hiring`
**Differential exposure**: Business cycle position, consumer sentiment baseline

### Contagion Channel

**Mechanism**: Counterparty risk spreads through interconnected institutions
**Affected regions**: Financially integrated economies
**Affected variables**: `interbank_lending`, `derivatives_markets`, `money_markets`
**Differential exposure**: Financial sector interconnection, derivative exposure

---

## Historical Analogues

| Case | Year | Trigger | Severity | Key Lesson |
|------|------|---------|----------|------------|
| Great Depression | 1929 | Equity bubble burst | Catastrophic | Policy response matters enormously |
| Latin American debt | 1982 | Interest rate shock | Severe (regional) | Sovereign-bank doom loop |
| Black Monday | 1987 | Portfolio insurance cascade | Moderate | Algorithmic amplification |
| Asian Financial Crisis | 1997 | Currency crisis cascade | Severe (regional) | Contagion through capital flows |
| Dot-com crash | 2000 | Tech bubble burst | Moderate | Sector-specific can be contained |
| Global Financial Crisis | 2008 | Housing/mortgage bubble | Severe | Interconnection, shadow banking |
| COVID shock | 2020 | Exogenous pandemic | Moderate | Rapid policy response effective |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-18 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Shadow banking exposure assessment; China financial system opacity; climate-finance linkages |

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- Reinhart & Rogoff "This Time Is Different" (crisis frequency)
- BIS financial stability reports
- IMF Global Financial Stability Reports
- Fed financial stability assessments
- 2008 GFC post-mortems (FCIC report)

## Open Questions

- **Shadow banking measurement**: How to assess non-bank financial intermediation risk?
- **China opacity**: How stressed is the Chinese financial system really?
- **Central bank limits**: Have unconventional policies exhausted capacity for next crisis?
- **Climate-finance linkages**: How do stranded asset risks transmit to financial system?
- **Cryptocurrency contagion**: Could crypto collapse trigger traditional finance stress?
- **Compound risk**: How to model financial crisis during/after pandemic or geopolitical crisis?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-18 | Initial Level 1 specification | Task 2.1.3 - hybrid Type 1/2 event |

---

*See [[methodology/reference/probability-estimation]] for hybrid calibration | [[methodology/reference/calibration-anchors]] for reference events*
