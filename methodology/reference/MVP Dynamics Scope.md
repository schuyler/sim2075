---
title: MVP Dynamics Scope
type: note
permalink: methodology/reference/mvp-dynamics-scope
tags:
- methodology
- reference
- dynamics
- mvp
- scope
- v0.1
- implementation
---

# MVP Dynamics Scope

## Minimum Viable Dynamics for v0.1 Prototype

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Design specification

**Related documents:**
- [[methodology/reference/state-dynamics]] — Full dynamics taxonomy
- [[methodology/reference/state-transmission]] — Transmission mechanisms
- [[methodology/reference/state-variables-country]] — Country variable catalog
- [[methodology/reference/state-variables-global]] — Global variable catalog
- [[methodology/project/tasks]] — Task 4 series implements this specification

---

## 1. Purpose & Context

### Core Insight

**Progress is continuous; catastrophe is discontinuous.**

Most of what improves human welfare—GDP growth, life expectancy gains, technology cost declines, institutional strengthening—accumulates gradually through compounding effects. Discontinuity events are predominantly negative: wars, state failures, financial crises, pandemics, climate tipping points.

The simulation's event catalog contains 29 discontinuity events. Of these:
- ~24 are unambiguously negative (conflicts, crises, failures, tipping points)
- ~5 are positive breakthroughs (fusion, agricultural, medical, energy storage)

Even accounting for positive breakthroughs, the event catalog is net-negative in expectation. Without baseline dynamics capturing gradual improvement, every simulation run produces civilizational decline—not because the world is doomed, but because the model is missing half the picture.

### Implication

**Baseline dynamics are essential, not optional.**

The "progress engine"—trend growth rates, life expectancy improvements, technology cost curves—provides the countervailing positive force against discontinuity shocks. A simulation without these dynamics doesn't validate the factor correlation structure; it produces an artifact of incomplete modeling.

### This Document Specifies

The minimum viable dynamics scope for v0.1:
- **Tier 1 (Essential):** Parameters required for valid simulation—baseline trends for core variables
- **Tier 2 (Defaults):** Parameters that use literature defaults rather than country-specific calibration
- **Tier 3 (Deferred):** Features excluded from v0.1, to be added if sensitivity analysis shows they matter

---

## 2. Tier 1: Essential Parameters ("Progress Engine")

These parameters carry the positive side of the ledger. Without them, simulation outputs are systematically biased toward decline.

### 2.1 Country-Level Baseline Trends

For each of 40 countries + 6 Tier 1 aggregates = **46 entities**:

| Variable | Parameters | Units | Primary Source |
|----------|------------|-------|----------------|
| `gdp_per_capita` | 2025 baseline | $K (2025 real) | IMF WEO |
| `gdp_per_capita` | Trend growth rate | %/year | IMF WEO medium-term projections |
| `life_expectancy` | 2025 baseline | Years | UN Population Division |
| `life_expectancy` | Trend improvement | Years/year | UN Population Division projections |

**Count: 46 entities × 4 parameters = 184 parameters**

### 2.2 Global Baseline Trends

| Variable | 2025 Baseline | Trend | Source | Notes |
|----------|---------------|-------|--------|-------|
| `global_temp_anomaly` | 1.3°C | +0.03°C/yr | IPCC | Accelerating; use scenario-dependent |
| `sea_level_global` | 10 cm | +0.4 cm/yr | NASA | Accelerating |
| `global_co2_ppm` | 425 ppm | +2.5 ppm/yr | NOAA Mauna Loa | |
| `battery_cost_kwh` | $130 | -8%/yr | BNEF | Learning curve |
| `renewable_cost_index` | 100 | -6%/yr | IRENA | Learning curve |
| `antibiotic_resistance` | 100 | +1%/yr | WHO GLASS | Slow deterioration |

**Count: 6 variables × 2 parameters = 12 parameters**

*Note: Several global variables are already specified in [[methodology/reference/state-variables-global]]. Task 4.3 will consolidate and verify these values.*

### 2.3 Tier 1 Summary

| Category | Entities | Parameters per Entity | Total |
|----------|----------|----------------------|-------|
| Country GDP + life expectancy | 46 | 4 | 184 |
| Global trends | 1 | 12 | 12 |
| **Tier 1 Total** | — | — | **~196** |

### 2.4 Note on Population Dynamics

Population cohorts (12 per country) evolve via deterministic aging mechanics, not parameterized trend rates:
- Each year, cohorts age into the next bracket
- Mortality rates (from `life_expectancy`) determine deaths
- Fertility rates (`tfr`) determine births
- Migration rates determine cross-border flows

These mechanics are specified in [[methodology/reference/state-dynamics]] §3 (Slow Drift Variables). They require initial 2025 population pyramids (from UN data) but not trend parameters—the trends emerge from the mechanics.

**For v0.1:** Use UN 2025 population estimates for initial conditions. Demographic evolution follows from cohort mechanics + life expectancy/fertility trends.

---

## 3. Tier 2: Default Parameters (Mean Reversion)

Mean-reverting variables require three parameters: equilibrium level, reversion speed (half-life), and volatility. For v0.1, use simple defaults rather than country-specific or historically-calibrated values.

### Quick Reference: Mean-Reverting Variables

Per [[methodology/reference/state-dynamics]], these variables are mean-reverting:

| Level | Variables |
|-------|-----------|
| **Country** | `gdp_growth`, `inflation_rate`, `unemployment_rate`, `fdi_net` |
| **Global** | Commodity prices (`oil_brent`, `wheat_price`, `rice_price`, `corn_price`, etc.), `global_credit_spread` |

Variables **not** mean-reverting (handled differently):
- **Slow drift:** GDP level, life expectancy, population, climate variables, technology costs
- **Event-driven:** Conflict intensity, regime type, nuclear status, sanctions level
- **Derived:** Dependency ratio, debt service ratio

### 3.1 Half-Life Defaults

| Variable Class | Default Half-Life | Rationale |
|----------------|-------------------|-----------|
| `gdp_growth` | 2 years | Business cycle duration; recessions typically recover within 2-3 years |
| `inflation_rate` | 2 years | Monetary policy transmission lag |
| `unemployment_rate` | 3 years | Labor market hysteresis; slower than output recovery |
| Commodity prices | 2 years | Supply/demand adjustment; historical mean reversion |
| `global_credit_spread` | 1 year | Financial markets revert faster than real economy |
| `fdi_net` | 3 years | Investment decisions have longer cycles |

**Implementation:** Half-life τ converts to reversion speed θ via: θ = ln(2) / τ

### 3.2 Equilibrium Defaults

| Variable | Equilibrium Approach |
|----------|---------------------|
| `gdp_growth` | Country's Tier 1 trend growth rate |
| `inflation_rate` | 2% (advanced), 4% (emerging), 6% (frontier) |
| `unemployment_rate` | 5% (advanced), 7% (emerging), 10% (frontier) |
| `oil_brent` | $75/barrel (2025 real) |
| `wheat_price` | $6/bushel (2025 real) |
| `global_credit_spread` | 120 bps |

*Country classification for defaults:*
- **Advanced:** G7 + Australia, South Korea, Taiwan, Israel, Singapore, Spain, Netherlands
- **Emerging:** China, India, Brazil, Mexico, Turkey, Saudi Arabia, UAE, South Africa, Poland, Thailand, Indonesia, Vietnam, Argentina, Egypt, Iran, Kazakhstan
- **Frontier:** Pakistan, Bangladesh, Nigeria, Ethiopia, DRC, Kenya, Ukraine, North Korea + all Tier 1/2 aggregates except Rest of EU (advanced)

*Known outliers requiring manual override:*
- **Argentina:** Structural inflation ~30%+; use 25% equilibrium instead of 4% emerging default
- **Turkey:** Elevated inflation in recent years; consider 10-15% equilibrium

### 3.3 Volatility Defaults

For v0.1, use placeholder volatilities based on typical ranges:

| Variable | Default σ (annual) | Notes |
|----------|-------------------|-------|
| `gdp_growth` | 2 percentage points | Typical advanced economy; higher for emerging |
| `inflation_rate` | 2 percentage points | Around target; higher for high-inflation countries |
| `unemployment_rate` | 1 percentage point | Relatively stable |
| `oil_brent` | $15/barrel | ~20% of baseline |
| `global_credit_spread` | 50 bps | Can spike much higher in crises |

**Simplification:** v0.1 uses single default volatility per variable class. Sensitivity analysis will reveal if country-specific volatilities matter.

### 3.4 Tier 2 Summary

| Parameter Type | Approach | Count |
|----------------|----------|-------|
| Half-lives | 6 variable-class defaults | 6 |
| Equilibria | Tier-based defaults | ~10 rules |
| Volatilities | Variable-class defaults | ~6 |
| **Tier 2 Total** | Rule-based, not entity-specific | ~22 rules |

---

## 4. Tier 3: Deferred Features

The following are excluded from v0.1. They add realism but also complexity. Sensitivity analysis will reveal which matter for tail outcomes.

### 4.1 Deferred Transmission Mechanisms

| Mechanism | Description | Why Deferred |
|-----------|-------------|--------------|
| Financial contagion | EM crisis correlation matrix | Requires historical calibration; may be second-order |
| Trade transmission | Country→country demand effects | Complex bilateral matrix; trade rupture events capture acute shocks |
| Climate damage functions | Country-specific yield/productivity impacts | Requires detailed exposure modeling |
| Remittance transmission | Source country GDP → recipient remittances | Important for specific countries; not system-wide |
| Policy reaction functions | Central bank Taylor rules | Treat rates as exogenous for v0.1 |

**v0.1 Transmission Scope:** Only oil→inflation and food→inflation, using single global passthrough coefficients scaled by country import dependence. See Task 4.5.

### 4.2 Deferred Parameterization

| Feature | Description | Why Deferred |
|---------|-------------|--------------|
| Country-specific half-lives | Each country's reversion speed | Default by tier is sufficient for v0.1 |
| Country-specific volatilities | Each country's shock variance | Historical calibration needed |
| Tipping thresholds | AMOC, Amazon collapse points | Use literature values; refine if sensitivity shows importance |
| Asymmetric reversion | Different speeds for positive vs. negative shocks | Adds complexity; unclear if material |
| Cross-variable transmission coefficients | How unemployment affects inflation, etc. | Within-country Phillips curves, etc. |

### 4.3 Deferred Entity Coverage

| Feature | Description | Why Deferred |
|---------|-------------|--------------|
| Tier 2 aggregate dynamics | Full variable set for 6 Tier 2 aggregates | Reduced variable set is sufficient |
| Additional countries | Expand beyond 40 | Sensitivity will show if regional gaps matter |

### 4.4 Triggers for Inclusion

Each deferred feature should be added if sensitivity analysis shows:

| Feature | Inclusion Trigger |
|---------|-------------------|
| Financial contagion | EM crisis events drive >10% of tail outcome variance |
| Trade transmission | Trade rupture impacts are underestimated vs. historical cases |
| Country-specific parameters | Cross-country variance in outcomes is unrealistically low |
| Climate damage functions | Climate events have implausibly uniform impacts |

---

## 5. Implementation Architecture

### 5.1 Simulation Loop (Conceptual)

```
For each year t from 2025 to 2075:
    
    1. FACTOR SAMPLING
       Draw correlated factor realizations F(t) from Gaussian copula
    
    2. EVENT FIRING
       For each event e:
           Compute P(e fires | F(t), state(t-1))
           Sample occurrence
           If fires: select aftermath branch, record impacts
    
    3. SHOCK APPLICATION
       Apply event impact vectors to state(t-1)
       Result: shocked_state(t)
    
    4. BASELINE DRIFT (Tier 1)
       For each entity:
           gdp_per_capita(t) = shocked_state.gdp_pc + trend_growth
           life_expectancy(t) = shocked_state.le + trend_improvement
       For global variables:
           Apply trend rates (temperature, CO2, tech costs, etc.)
    
    5. MEAN REVERSION (Tier 2)
       For mean-reverting variables:
           X(t) = X(t) + θ × (μ - X(t)) + ε
           where θ from half-life, μ from equilibrium, ε from volatility
    
    6. TRANSMISSION (Simplified)
       inflation(t) = f(oil_price, food_price, import_dependence)
    
    7. RECORD STATE
       Store state(t) for trajectory output
```

### 5.2 What v0.1 Validates

With Tier 1 + Tier 2 parameters, the prototype can validate:

| Component | Validation Question |
|-----------|---------------------|
| Factor sampling | Do correlated factors produce realistic event clustering? |
| Event firing | Do event frequencies match specified probabilities? |
| Impact application | Do shock magnitudes produce plausible state changes? |
| Baseline drift | Do no-event trajectories show reasonable progress? |
| Mean reversion | Do shocked variables recover appropriately? |
| Overall trajectories | Do simulation runs produce interpretable futures? |

### 5.3 What v0.1 Cannot Validate

| Component | Why Not |
|-----------|---------|
| Transmission realism | Simplified; only oil/food→inflation |
| Country-specific dynamics | Using defaults, not calibrated values |
| Tail outcome drivers | Need sensitivity analysis |
| Historical fit | Need backtesting against past decades |

---

## 6. Parameter Sourcing Notes

### 6.1 IMF WEO (GDP)

The IMF World Economic Outlook provides:
- Current year GDP estimates
- 5-year projections with growth rates
- Long-term (2029+) growth assumptions

**For v0.1:** Use WEO medium-term growth projections as trend rates. These are available for all 40 countries.

**Limitation:** IMF projections are typically optimistic; they don't account for discontinuities. This is acceptable because events provide the shocks; baseline is the counterfactual "no discontinuity" path.

### 6.2 UN Population Division (Life Expectancy)

UN World Population Prospects provides:
- Current life expectancy estimates by country
- Projections to 2100 under multiple scenarios

**For v0.1:** Use UN medium-variant projections. Extract trend improvement rate as (LE_2030 - LE_2025) / 5.

**Typical values:** Advanced economies: +0.1 to +0.15 years/year. Emerging: +0.15 to +0.25 years/year. Countries with HIV/conflict burden may be lower or negative.

### 6.3 Technology Costs

Already specified in [[methodology/reference/state-variables-global]]:
- Battery: -8%/year learning curve
- Renewables: -6%/year learning curve

These are based on historical trends and industry projections (BNEF, IRENA, Lazard).

### 6.4 Climate Trajectories

Already specified in [[methodology/reference/state-variables-global]]:
- Temperature: +0.03°C/year (varies by emissions scenario)
- Sea level: +0.4 cm/year (accelerating)
- CO2: +2.5 ppm/year

For v0.1, use central estimates. Scenario branching (SSP1 vs SSP5) is a future refinement.

---

## 7. Simplifications Register

Explicit documentation of v0.1 simplifications for future reference.

| Simplification | Description | Risk | Mitigation |
|----------------|-------------|------|------------|
| Single half-life per variable class | All countries use same reversion speed | May miss country-specific dynamics | Sensitivity analysis; refine if variance is too low |
| Tier-based equilibria | Advanced/emerging/frontier defaults | May miss outliers | Review extremes (Argentina inflation, etc.) |
| Placeholder volatilities | Single σ per variable | May understate uncertainty | Conservative default (higher σ) |
| Minimal transmission | Only oil/food→inflation | May miss contagion dynamics | Events capture acute transmission; add continuous if needed |
| No policy reaction functions | Central bank rates exogenous | May miss feedback loops | Rates are slow-moving; events capture crises |
| Linear trends | No acceleration/deceleration | May miss S-curves | Sufficient for 50-year horizon |

---

## 8. Success Criteria for v0.1

The MVP dynamics implementation is successful if:

1. **No degenerate trajectories:** Variables stay within plausible bounds (no negative populations, no infinite GDP)

2. **Progress is visible:** In no-event runs, countries show improvement on GDP and life expectancy

3. **Shocks are absorbed:** After events, mean-reverting variables recover toward equilibria

4. **Distributional plausibility:** Cross-run distributions show reasonable spread (not all runs identical, not all runs catastrophic)

5. **Event frequencies match:** Observed event counts approximate specified probabilities × years

---

## 9. Cross-References

| Topic | Document |
|-------|----------|
| Full dynamics taxonomy | [[methodology/reference/state-dynamics]] |
| Transmission mechanisms | [[methodology/reference/state-transmission]] |
| Country variables | [[methodology/reference/state-variables-country]] |
| Global variables | [[methodology/reference/state-variables-global]] |
| Implementation tasks | [[methodology/project/tasks]] — Section 4 |
| Event catalog | [[events/]] directory |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial specification |

---

*This document specifies minimum viable dynamics scope. For full dynamics taxonomy see [[methodology/reference/state-dynamics]]. For implementation tasks see [[methodology/project/tasks]].*