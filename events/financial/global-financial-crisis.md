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

**What marks occurrence**: Multiple major financial institutions face insolvency or require emergency support; interbank lending freezes; central banks initiate emergency liquidity facilities; equity markets decline >20% within weeks.

---

## Causal Type Specification (Type 2 with Type 1 Floor)

### Why Hybrid Type 1/2?

Financial crises exhibit both patterns:
- **Type 1 (base rate)**: Even well-regulated systems experience periodic crises; some triggers are exogenous (geopolitical shocks, pandemics)
- **Type 2 (threshold)**: Probability rises dramatically as leverage, asset bubbles, and imbalances accumulate

Modeling approach: Type 2 pressure function with elevated floor (1.5%/year) representing irreducible base rate.

### Pressure Function

Uses global state variables from [[methodology/reference/state-variables-global]]. Many ideal pressure indicators (private debt/GDP, asset valuations, leverage ratios) are not tracked in v1.0; we proxy through available variables.

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `global_credit_spread` | 0.30 | inverse_threshold(200) | Tight spreads = risk accumulation; wide spreads = stress |
| `us_real_rate` | 0.20 | inverse | Low real rates → reach for yield → risk accumulation |
| `fed_funds_rate` (deviation from neutral) | 0.20 | U-shaped | Both very low (bubbles) and very high (stress) increase risk |
| `us_10yr_yield` | 0.15 | trend | Rapid tightening increases stress |
| F_FIN factor realization | 0.15 | linear | Captures unmeasured financial stress |

**Proxy limitations**: The universal variable set cannot directly capture private debt levels, asset valuations, shadow banking leverage, or current account imbalances. The pressure function relies heavily on the F_FIN factor to capture these unmeasured dimensions. This is a known fidelity limitation; probability is calibrated primarily via reference class reasoning rather than mechanical pressure calculation.

### Threshold Specification

| Parameter | Value |
|-----------|-------|
| **Estimate** | 65 (on 0-100 pressure scale) |
| **Uncertainty** | ±12 |
| **Sharpness (k)** | 0.15 (moderate; crises can occur across range of pressure levels) |
| **Historical calibration** | 2008 GFC, 1997 Asian Crisis, 2000 Dot-com |

### Minimum Probability (Type 1 Floor)

**Floor**: 1.5%/year

Even with low systemic pressure, exogenous shocks can trigger crises: geopolitical events, pandemics, policy errors, fraud. This floor represents the irreducible Type 1 base rate.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 3.0% |
| **At low pressure (floor)** | 1.5% |
| **At high pressure** | 8-12% |
| **Confidence** | Medium |
| **25-year cumulative** | ~55% at point estimate |

### Derivation

**Historical base rate**:
- Observation period: 1929-2024 (95 years)
- Major global/regional crises reaching threshold: ~8
- Base rate: ~8%/decade or ~3%/year with current-like conditions

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4:

**1. Post-2008 regulation has reduced systemic risk**

Dodd-Frank, Basel III, and other post-GFC reforms have substantially increased capital requirements, reduced leverage, and improved oversight. The 3%/year estimate may be calibrated to a pre-2008 world. The true current rate may be closer to 2%/year.

*Counter*: Regulation addresses *known* vulnerabilities. Shadow banking has grown substantially (now ~$200T+ globally), much of it outside regulatory perimeter. Crypto, private credit, and new derivatives create new transmission channels. History shows regulation erodes (Glass-Steagall → 2008).

**2. Central banks have proven capacity**

2008 and 2020 showed central banks can prevent moderate crises from becoming catastrophic through aggressive intervention. The "catastrophic" branch probability (15%) may be too high given demonstrated policy competence.

*Counter*: Central bank balance sheets are already expanded. Real rates near zero leave less room for cuts. The tools that worked in 2008-2020 may be exhausted. And political constraints on bailouts may bind harder next time.

**3. The definition is too broad**

Lumping together 2008 (systemic crisis) and 2020 (exogenous shock with rapid recovery) into the same category conflates very different phenomena. The 3%/year rate includes events with very different causal structures.

*Counter*: The event is defined by *systemic stress requiring intervention*, not by cause or duration. 2020 met the threshold (>20% market decline, credit market seizure, massive intervention needed). The severity branches capture the difference between moderate and severe outcomes.

**4. Pressure function is too crude**

Given that most key variables (private debt, leverage, asset valuations) aren't tracked, the pressure function is mostly F_FIN factor and a few rates. This may not meaningfully capture state-conditioning.

*Counter*: Acknowledged limitation. The calibration relies more on reference class reasoning than mechanical pressure calculation. But this is transparent—we know we're uncertain about state-conditioning and say so.

### Probability Evolution

For Type 2 events, probability varies with pressure.

| Period | Estimated Pressure | Annual Probability | Rationale |
|--------|-------------------|-------------------|-----------|
| 2025-2030 | ~55 | ~3.0% | Current elevated baseline; post-2022 rate normalization |
| 2030-2040 | ~50-60 | ~2.5-3.5% | Depends on whether imbalances build or resolve |
| 2040-2075 | Uncertain | ~2-4% | Long-term depends on regulatory regime, financial innovation |

### Key Uncertainties

- **Shadow banking**: Less regulated sector may have hidden leverage
- **Central bank capacity**: Balance sheets already expanded
- **China financial system**: Opacity makes pressure assessment difficult
- **Cryptocurrency/DeFi**: New transmission channels, untested under stress

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_FIN** | 0.80 | Dominant: this IS the financial instability factor |
| **F_GPT** | 0.30 | Great power tension → sanctions, capital flow disruption |
| **F_EAS** | 0.25 | China financial stress is major global risk |
| **F_EUR** | 0.20 | Eurozone fragmentation risk; banking vulnerabilities |
| **F_CLIM** | 0.15 | Climate risks → stranded assets, insurance losses |
| **F_MENA** | 0.12 | Oil shock → inflation → tightening → stress |
| **F_TECH** | 0.10 | Tech bubble dynamics; algorithmic amplification |
| F_HLTH | 0.00 | Pandemic trigger in Type 1 floor |
| F_FOOD | 0.00 | Indirect via inflation |
| F_SAS | 0.00 | Marginal to global financial system |
| F_SSA | 0.00 | Marginal to global financial system |
| F_LAM | 0.00 | Lower contagion risk post-1990s |

**Sum of squared loadings**: 0.88 ✓

---

## Severity Branches

### Branch 1: Moderate (35%)

2000 dot-com or 2020 COVID-shock scale. Sharp market decline (25-40%), credit tightening, but rapid policy response prevents systemic collapse. Recovery within 2-3 years.

**Impact modifiers**: 1.0× baseline

### Branch 2: Severe (50%)

2008 GFC scale. Major institutional failures, credit market seizure, significant real economy impact. Requires massive policy intervention. Recovery takes 5-7 years.

**Impact modifiers**: 2.5× baseline

### Branch 3: Catastrophic (15%)

1929 Great Depression scale. Systemic collapse across multiple major economies. Policy response inadequate. Decade-scale recovery.

**Impact modifiers**: 6.0× baseline

---

## Impact Vector

### Global Impacts (Baseline: Moderate Branch)

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `global_trade_volume` | ↓ | -10% ± 5% | immediate | decaying: half_life=2yr |
| `global_credit_spread` | ↑ | +300 ± 100 bps | immediate | decaying: half_life=1yr |

### Country-Level Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].gdp_real` | ↓ | -4% ± 2% | immediate | decaying: half_life=2yr |
| `[country].gdp_growth` | ↓ | -3 ± 1.5 pp | immediate | decaying: half_life=1.5yr |
| `[country].unemployment_rate` | ↑ | +3 ± 1.5 pp | delayed(6mo) | decaying: half_life=2.5yr |
| `[country].debt_public` | ↑ | +15 ± 8 pp GDP | gradual(2yr) | permanent |
| `[country].fdi_net` | ↓ | -3 ± 1.5 pp GDP | immediate | decaying: half_life=2yr |

*Scale by impact_multiplier for severe (2.5×) and catastrophic (6.0×) branches*

### Differential Impacts

**Exposure variable**: Financial sector size, current account balance

| Country Profile | GDP Multiplier | Rationale |
|-----------------|----------------|-----------|
| Financial centers (US, UK) | 1.2× | Direct exposure |
| Current account deficit (EM) | 1.5× | Capital flight risk |
| Current account surplus (DE, CN, JP) | 0.8× | Buffers |

---

## Cascade Effects

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| PAKISTAN_STATE_FAILURE | +0.8%/year | 5 years | Fiscal exhaustion, capital flight |
| EGYPT_STATE_FAILURE | +0.8%/year | 5 years | Fiscal exhaustion, capital flight |
| CHINESE_ECONOMIC_CRISIS | +1.5%/year | 3 years | Financial contagion, confidence |
| EU_FRAGMENTATION | +1.0%/year | 5 years | Sovereign stress, bank-sovereign loop |

### Triggered By

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| CHINESE_ECONOMIC_CRISIS | +2.0%/year | Major financial contagion |
| TAIWAN_CONFLICT | +3.0%/year | Trade disruption, risk-off, sanctions |
| SEVERE_PANDEMIC | +2.0%/year | Economic shutdown, credit stress |

---

## Historical Analogues

| Case | Year | Severity | Key Lesson |
|------|------|----------|------------|
| Great Depression | 1929 | Catastrophic | Policy response matters enormously |
| Asian Financial Crisis | 1997 | Severe (regional) | Contagion through capital flows |
| Global Financial Crisis | 2008 | Severe | Interconnection, shadow banking |
| COVID shock | 2020 | Moderate | Rapid policy response effective |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete (2025-12-30) |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Shadow banking assessment; China opacity; climate-finance linkages |

## Open Questions

1. **Shadow banking measurement**: How to assess non-bank financial risk?
2. **China opacity**: How stressed is Chinese financial system?
3. **Central bank limits**: Have unconventional policies exhausted capacity?
4. **Climate-finance linkages**: How do stranded assets transmit to financial system?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-18 | Initial Level 1 specification | Hybrid Type 1/2 event |
| 2025-12-30 | Critical review complete | Task 2.4.5 - Added Case Against, Probability Evolution; fixed variable/event references |

---

*See [[methodology/reference/state-variables-global]] for global variables | [[methodology/03-critical-review]] for review methodology*