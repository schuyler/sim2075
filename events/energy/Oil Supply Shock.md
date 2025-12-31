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

| Attribute | Value |
|-----------|-------|
| **ID** | `OIL_SUPPLY_SHOCK` |
| **Scale** | Global |
| **Domain** | Economic / Geopolitical |
| **Causal Type** | Type 1: Stochastic |
| **Onset Speed** | Sudden (weeks) |
| **Reversibility** | Partial |

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

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_MENA** | 0.46 | Primary production region; regional instability directly threatens supply |
| **F_GPT** | 0.34 | Great power tension increases conflict probability in oil-producing regions |
| **F_FIN** | 0.29 | Financial stress correlates with geopolitical risk-taking; oil shocks stress financial systems |
| F_EUR | 0.13 | European energy dependence creates exposure; Russia-Europe dynamics |
| F_EAS | 0.08 | Major demand region; supply competition dynamics |
| F_LAM | 0.08 | Venezuela instability; regional production |
| F_FOOD | 0.08 | Oil-intensive agriculture; food price correlation with energy prices |
| F_SSA | 0.04 | Minor production (Nigeria, Angola) |
| F_CLIM | 0.00 | No direct pathway |
| F_HLTH | 0.00 | No direct pathway |
| F_SAS | 0.00 | No direct pathway |
| F_TECH | 0.00 | No direct pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.75 (Type 1 target); scale factor = 0.84 from original loadings

### Loading Rationale

F_MENA is dominant (0.55) because the majority of supply concentration and chokepoint risk is in the Middle East — Saudi Arabia, Iraq, Iran, UAE, Kuwait, and the Strait of Hormuz are all MENA. F_GPT is secondary (0.40) because great power competition increases the probability of conflicts that disrupt supply (US-Iran, US-Russia, regional proxy conflicts). F_FIN (0.35) captures the correlation between financial stress and geopolitical risk-taking, plus the financial system's vulnerability to oil shocks.

The interpretation for Type 1 events: factors affect the *clustering* of events, not the triggering. When F_MENA and F_GPT are elevated, multiple supply-threatening events become more likely to occur in proximity.

---

## Resolutions

For Type 1 events, resolutions represent different manifestations of the discontinuity when it occurs. Not whether it occurs, but what form it takes.

```yaml
resolutions:
  - id: accelerated_transition
    probability: 0.40
    description: |
      Supply shock triggers permanent demand destruction and accelerated
      energy transition. Efficiency investments, renewables deployment,
      and electrification accelerate. Oil demand never returns to
      pre-shock trajectory.
      
  - id: producer_restructuring
    probability: 0.35
    description: |
      Geopolitical realignment of energy relationships. New suppliers
      emerge or gain prominence. Trade patterns restructure around
      new partnerships. OPEC cohesion affected. Producer-consumer
      power balance shifts.
      
  - id: extended_crisis
    probability: 0.25
    description: |
      Prolonged shortage without clear resolution. Rationing,
      economic contraction, political instability in dependent
      economies. Eventually resolves through combination of
      demand destruction and supply recovery, but extended
      duration (18+ months) causes deeper structural damage.

resolution_probability_rationale:
  default: "Maximum entropy would be 33/33/33"
  specified: "40/35/25"
  justification: |
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
    
  confidence: "Medium — historical sample is small (n=2 clear cases)"
```

---

## Aftermath Branches

### Accelerated Transition Aftermath

```yaml
resolution: accelerated_transition
aftermath_branches:

  - id: successful_transition
    probability: 0.60
    description: |
      Shock catalyzes successful acceleration of energy transition.
      Renewables and efficiency investments surge. Electric vehicle
      adoption accelerates. Oil demand peaks earlier than baseline
      trajectory. Energy security improves long-term despite short-term pain.
      
    factor_modifications:
      F_MENA: -0.15  # Reduced relevance of oil producers
      F_CLIM: -0.10  # Lower emissions trajectory
      F_FIN: +0.20   # Transition investment stress
      
    duration:
      type: permanent
      note: Demand destruction and efficiency gains don't reverse
      
    impact_vector:
      global:
        oil_price: [+0.80, 0.30]  # 80% spike during transition
        inflation: [+0.03, 0.01]  # percentage points
        gdp_growth: [-0.015, 0.008]  # annual drag during adjustment
        renewable_investment: [+0.40, 0.15]  # acceleration vs. baseline
        oil_demand_peak: [-5, 2]  # years earlier than baseline
      oil_importers:
        gdp: [-0.025, 0.01]  # short-term pain
        energy_intensity: [-0.15, 0.05]  # permanent efficiency gain
        current_account: [-0.02, 0.01]  # temporary worsening
      oil_exporters:
        gdp: [+0.10, 0.05]  # short-term windfall
        fiscal_sustainability: [-0.20, 0.10]  # long-term demand loss
        diversification_pressure: [+0.30, 0.10]
        
  - id: chaotic_transition
    probability: 0.40
    description: |
      Transition acceleration is disorderly. Investment flows are
      volatile. Grid instability from rapid renewable integration.
      Political backlash in some jurisdictions. Transition occurs
      but with higher costs and more disruption than successful scenario.
      
    factor_modifications:
      F_MENA: -0.10
      F_FIN: +0.35
      F_GPT: +0.15  # Energy competition intensifies
      
    duration:
      type: decaying
      half_life_years: 5
      floor: 0.20
      
    impact_vector:
      global:
        oil_price: [+1.00, 0.40]  # larger spike, more volatility
        inflation: [+0.04, 0.015]
        gdp_growth: [-0.025, 0.01]
        financial_stability: [-0.20, 0.08]
      developed_economies:
        political_stability: [-0.15, 0.08]  # energy price backlash
      emerging_economies:
        gdp: [-0.04, 0.015]  # harder hit by transition costs
```

### Producer Restructuring Aftermath

```yaml
resolution: producer_restructuring
aftermath_branches:

  - id: new_equilibrium
    probability: 0.55
    description: |
      New producer-consumer relationships stabilize. Non-OPEC
      production (US shale, Brazil, Guyana, others) gains share.
      Bilateral energy partnerships replace multilateral frameworks.
      New trade routes and infrastructure develop.
      
    factor_modifications:
      F_GPT: +0.20  # Energy competition component of great power rivalry
      F_MENA: -0.10  # Reduced MENA centrality
      F_LAM: +0.10  # Latin American producers gain importance
      
    duration:
      type: regime_dependent
      persists_in: ["current_trade_architecture"]
      
    impact_vector:
      global:
        oil_price: [+0.40, 0.20]  # elevated but stable
        trade_volume: [-0.05, 0.02]  # some fragmentation
        supply_chain_resilience: [-0.10, 0.05]  # new dependencies
      united_states:
        energy_production: [+0.15, 0.08]  # shale expansion
        energy_exports: [+0.25, 0.10]
      mena_exporters:
        gdp: [-0.08, 0.04]  # market share loss
        political_influence: [-0.20, 0.10]
        
  - id: fragmented_markets
    probability: 0.45
    description: |
      Energy markets fragment into competing blocs. Pricing
      mechanisms diverge. Arbitrage constrained by political
      barriers. Long-term inefficiency in global energy allocation.
      
    factor_modifications:
      F_GPT: +0.35
      F_FIN: +0.25
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.25
      
    impact_vector:
      global:
        oil_price: [+0.60, 0.25]  # higher due to inefficiency
        trade_volume: [-0.10, 0.04]
        economic_efficiency: [-0.08, 0.03]
      non_aligned_countries:
        energy_access: [-0.15, 0.08]  # caught between blocs
```

### Extended Crisis Aftermath

```yaml
resolution: extended_crisis
aftermath_branches:

  - id: managed_recovery
    probability: 0.50
    description: |
      After 18-24 months of crisis, supply recovers and demand
      adjusts. Deep economic damage during crisis period but
      eventual stabilization. Lessons learned improve future
      resilience.
      
    factor_modifications:
      F_FIN: +0.40
      F_GPT: +0.25
      
    duration:
      type: decaying
      half_life_years: 4
      floor: 0.15
      
    impact_vector:
      global:
        oil_price: [+1.50, 0.50]  # major spike during crisis
        gdp_growth: [-0.04, 0.015]  # significant recession
        inflation: [+0.06, 0.02]  # cost-push inflation
        financial_stability: [-0.30, 0.12]
      oil_importers:
        gdp: [-0.06, 0.02]
        current_account: [-0.04, 0.015]
        political_stability: [-0.20, 0.10]
      emerging_economies:
        poverty_rate: [+0.05, 0.02]  # percentage point increase
        food_security: [-0.15, 0.06]  # fertilizer/transport costs
        
  - id: cascading_failures
    probability: 0.50
    description: |
      Extended crisis triggers cascading failures in vulnerable
      economies. State failures in oil-dependent or food-insecure
      countries. Financial contagion. Global recession deepens
      into depression in worst cases.
      
    factor_modifications:
      F_FIN: +0.60
      F_GPT: +0.40
      F_FOOD: +0.35
      F_MENA: +0.25
      F_SSA: +0.30
      
    duration:
      type: decaying
      half_life_years: 6
      floor: 0.30
      
    cascade_triggers:
      - event_id: GLOBAL_FINANCIAL_CRISIS
        probability_multiplier: 2.0
        duration_years: 3
      - event_id: EGYPT_STATE_FAILURE
        probability_multiplier: 1.8
        duration_years: 3
      - event_id: PAKISTAN_STATE_FAILURE
        probability_multiplier: 1.5
        duration_years: 3
        
    impact_vector:
      global:
        oil_price: [+2.00, 0.70]  # extreme spike
        gdp_growth: [-0.06, 0.02]  # deep recession
        inflation: [+0.08, 0.03]
        financial_stability: [-0.45, 0.15]
        displacement: [+15000000, 8000000]  # from cascading state failures
```

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

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Financial stress | GLOBAL_FINANCIAL_CRISIS | ×1.5-2.0 | 3 years | Energy cost shock → corporate defaults → financial contagion |
| Food price transmission | EGYPT_STATE_FAILURE | ×1.5 | 3 years | Fertilizer/transport costs → food prices → bread subsidies unsustainable |
| Fiscal stress (importers) | PAKISTAN_STATE_FAILURE | ×1.3 | 3 years | Import bill → forex reserves → IMF dependency deepens |
| Political backlash | EU_FRAGMENTATION | ×1.2 | 5 years | Differential impacts → solidarity strain → populist surge |
| Revenue windfall end | SAUDI_REGIME_INSTABILITY | ×0.7 initially, ×1.3 after | 5+ years | Windfall delays stress; demand destruction accelerates it |

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

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Hormuz scenario detail; shale response capacity; food security cascade |

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