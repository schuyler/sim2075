---
title: eu-fragmentation
type: note
permalink: events/geopolitical/eu-fragmentation
tags:
- event
- geopolitical
- type-2
- eu
- europe
- fragmentation
- eurozone
- level-1
---

# EU Fragmentation

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | EU_FRAGMENTATION |
| **Scale** | Regional (with global implications) |
| **Domain** | Political |
| **Causal Type** | Type 2: Threshold |
| **Onset Speed** | Rapid (crisis unfolds over 1-3 years) |
| **Reversibility** | Irreversible (institutional dissolution cannot be undone) |

## Description

Discontinuity in European integration: the EU or Eurozone ceases to function as a coherent political-economic union. This is not a crisis the EU survives — it is the end of European integration in its current form.

The event fires only when fragmentation becomes inevitable. Severe crises that the EU weathers through extraordinary measures (ECB interventions, fiscal transfers, treaty modifications) are sub-threshold — they represent the system functioning under stress, not discontinuity. Brexit is the canonical example: major stress, but the remaining EU continued governing with the same institutional form.

**Discontinuity requirement**: All resolutions produce a fundamentally different European institutional architecture. "Eurosceptic governments" or "two-speed Europe within existing treaties" is not a discontinuity.

---

## Causal Type Specification

### Type 2 Threshold Structure

Pressure accumulates through fiscal divergence, democratic backsliding, economic asymmetry, and political fragmentation. At critical pressure, fragmentation becomes inevitable.

Unlike some political events with multiple possible resolutions, EU fragmentation has a single outcome: disorderly collapse. "Orderly fragmentation" — negotiated restructuring into formal tiers — is not a discontinuity; it represents managed evolution of the kind the EU has practiced for decades (Schengen opt-outs, Eurozone non-membership, enhanced cooperation). If actors can coordinate an orderly transition, the threshold hasn't truly been crossed.

```
Pressure accumulates → Threshold crossed → Fragmentation inevitable →
Disorderly collapse unfolds
```

### Pressure Function

Per [[methodology/concepts/synthetic-variable-problem]], we use observable indicators rather than synthetic indices like "eu_cohesion" or "regime_stability."

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `ita.debt_public` | 0.25 | threshold(150%) | Italy is the systemic risk; debt dynamics key |
| `deu.gdp_growth` | 0.15 | inverse | German economy anchors EU; weakness undermines capacity |
| `fra.protest_intensity_annual` | 0.15 | linear | French political stress (observable proxy for instability) |
| `global_credit_spread` | 0.15 | linear | Financial stress transmission |
| `ita.gdp_growth` | 0.10 | inverse | Italian economic performance affects debt dynamics |
| `pol.years_since_irregular_transition` | 0.10 | complex | Rule of law pressure; time since democratic consolidation |
| `fra.unemployment_rate` | 0.10 | linear | Economic stress in core member |

**Pressure calculation**:
```
pressure = 0.25 × max(0, (ita_debt_public - 100) / 100)
         + 0.15 × max(0, (1 - deu_gdp_growth) / 5)
         + 0.15 × fra_protest_intensity_annual / 100
         + 0.15 × global_credit_spread / 300
         + 0.10 × max(0, -ita_gdp_growth) / 5
         + 0.10 × (pol_democratic_backsliding_proxy)
         + 0.10 × fra_unemployment_rate / 15
```
*Normalized to 0-100 scale*

**Proxy limitations**: True "EU cohesion" and "political unity" are unobservable. We proxy through economic stress in key members (Italy debt, German growth, French unemployment/protests) and financial market indicators. The key unobservables—Commission-Council dynamics, Franco-German coordination quality, member state political will—cannot be directly captured. Probability calibration relies on reference class reasoning from historical monetary/political union dissolutions.

*Note: Italy debt is the single most dangerous variable — a debt crisis in the third-largest eurozone economy exceeds ECB capacity.*

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 80 on 0-100 scale | High threshold — EU has survived multiple severe crises |
| **Uncertainty** | ±12 (range 68-92) | Uncertainty about ECB capacity limits |
| **Sharpness (k)** | 12 | Fairly sharp — markets force resolution once confidence breaks |
| **Historical calibration** | 2010-12 debt crisis (sub-threshold, ~60-65); Brexit (sub-threshold, ~55); 1992 ERM crisis (sub-threshold, ~50) |

### Current Pressure Assessment (2025)

**Estimated pressure**: ~30-35 on 0-100 scale

| Component | Status | Contribution |
|-----------|--------|--------------|
| EU cohesion | Stressed but functional | Moderate |
| Italian debt | High but stable (~140% GDP) | Moderate |
| German economy | Sluggish but not crisis | Low-moderate |
| French politics | Turbulent but institutions hold | Moderate |
| Financial conditions | Normal range | Low |
| Rule of law (Poland/Hungary) | Contested but managed | Low-moderate |

Distance to threshold (~45-50 points) is substantial.

### Minimum Probability

**Floor**: 0.15% annually even at low pressure

Black swan triggers: simultaneous bank failures across multiple countries, catastrophic ECB policy error, or external shock (major war involving EU territory) that overwhelms coordination capacity.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 0.4% |
| **Low bound** | 0.2% |
| **High bound** | 0.7% |
| **Confidence** | Low |
| **25-year cumulative** | ~10% at point estimate |

### Derivation

**Step 1: Reference class — dissolution of multinational political unions**

| Reference | Outcome | Duration | Annual Rate | Notes |
|-----------|---------|----------|-------------|-------|
| USSR | Dissolved | 69 years | ~1.4% | Coercive empire; different structure |
| Yugoslavia | Dissolved | 45 years | ~2.2% | Held together by strongman |
| Czechoslovakia | Dissolved | 74 years | ~1.4% | Velvet divorce; peaceful |
| EU (Maastricht) | Ongoing | 33 years | 0% realized | Has survived multiple crises |
| Habsburg Empire | Dissolved | ~400 years | ~0.25% | Long-lived but ultimately fragile |

Voluntary unions with distributed power and wealthy members are more durable than empires or strongman states. EU most resembles a novel institutional form — no clean historical analog.

**Step 2: Structural factors**

Factors increasing probability:
- Eurozone design flaw (monetary without fiscal union)
- Democratic legitimacy deficit in EU institutions
- Core-periphery economic divergence
- Rising nationalism across member states
- Unanimous decision-making creates gridlock risk

Factors decreasing probability:
- Deep integration (70+ years of institution-building)
- Distributed power (no single point of failure)
- Strong rule of law in core members
- Wealthy membership with fiscal capacity
- Track record of crisis survival (2010-12, Brexit, COVID, Ukraine)
- ECB "whatever it takes" demonstrated effectiveness

**Step 3: Brexit as calibration anchor**

Brexit was a major member exiting — and the EU survived. This is evidence that:
- The threshold for *fragmentation* (not just exit) is high
- Remaining members consolidated rather than followed
- Institutions proved resilient under stress

Brexit : EU :: Tiananmen : CCP — both were existential tests that the system passed.

**Step 4: Conditional probability from cascades**

- GLOBAL_FINANCIAL_CRISIS: +1.5% for 3 years
- DOLLAR_RESERVE_CRISIS: +0.5% for 3 years (euro under stress)
- Italian fiscal crisis (not separately modeled): would dramatically increase pressure

**Step 5: Final estimate**

**Point estimate: 0.4% annually** with range 0.2%-0.7%.

This is low because we're modeling actual institutional dissolution — the EU ceasing to function as a coherent union — not severe political crises or policy disagreements.

### Comparative Ranking

- Similar to: Chinese Political Crisis (~0.4%), AMOC Weakening (~0.5%)
- Less likely than: Russia State Failure (~1.0%), Turkey Political Crisis (~1.0%)
- More likely than: Permafrost Methane Release (~0.3% for severe)

EU institutions are more robust than personalist regimes (Russia, Turkey) but remain a voluntary political construct unlike physical systems (climate).

### Key Uncertainties

- **Italian debt trajectory**: Could push probability to 0.8%+ if unsustainable
- **German political evolution**: AfD in government could fundamentally alter dynamics
- **ECB capacity limits**: Unknown where "whatever it takes" actually fails
- **External shocks**: Major war, pandemic, or financial crisis could accelerate

### Case Against This Specification

**The EU has survived everything**: The EU survived the 2010-12 debt crisis, Brexit, COVID, and the Ukraine war. Each time forecasters predicted collapse; each time institutions adapted. 0.4%/year may be too high given this track record.

**ECB "whatever it takes" has no known limit**: Draghi's 2012 pledge ended the debt crisis instantly. There's no evidence ECB couldn't repeat this. The specification assumes ECB capacity has a limit, but we've never observed it.

**Brexit proved fragmentation doesn't cascade**: The UK's exit was supposed to trigger others. Instead, EU approval ratings rose and remaining members consolidated. The "domino effect" theory failed its major test.

**Voluntary wealthy unions don't dissolve**: Unlike the USSR (coercive) or Yugoslavia (held together by strongman), the EU is a voluntary association of wealthy democracies. No comparable entity has ever dissolved. Reference class is effectively empty.

**Counterargument**: The Eurozone design flaw (monetary without fiscal union) is real and creates genuine vulnerability. Italian debt dynamics are unsustainable long-term. The 0.4%/year estimate is already low—it reflects these stabilizing factors while acknowledging structural vulnerability.

### Probability Evolution

As a Type 2 event, probability depends on pressure trajectory, primarily Italian debt dynamics and energy transition stress on Germany:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2035 | 0.3-0.5% | Italian debt stable; ECB credible; Franco-German coordination functional |
| 2035-2050 | 0.4-0.8% | Italian demographics worsen fiscal trajectory; German energy transition stress |
| 2050-2075 | 0.5-1.0% | Long-term fiscal pressures accumulate; climate stress on southern members |

**Key inflection points**:
- Italian debt crossing 160% GDP (if not offset by growth) opens danger zone
- German economic model failure (energy transition, China competition) weakens anchor
- Major external shock (financial crisis, war) during period of elevated pressure

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2 target (ΛΩΛᵀ)ᵢᵢ = 0.65*

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.10 | Climate stress drives migration pressure, agricultural disruption |
| **F_FIN** | 0.28 | **Secondary**: Financial stress is primary transmission mechanism |
| F_HLTH | 0.03 | Pandemic stress tests coordination capacity |
| F_GPT | 0.17 | Great power tension affects transatlantic relations, defense burden |
| F_FOOD | 0.07 | Food price spikes stress periphery budgets |
| F_TECH | 0.00 | Limited direct relevance |
| **F_EUR** | 0.45 | **Primary**: European stress is definitional |
| F_MENA | 0.14 | MENA instability drives migration pressure |
| F_SAS | 0.00 | No direct linkage |
| F_EAS | 0.03 | China trade relations, Taiwan scenario implications |
| F_SSA | 0.07 | African instability drives migration |
| F_LAM | 0.00 | No direct linkage |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.70 from original loadings

### Loading Rationale

F_EUR is primary because it directly captures European-specific political stress. F_FIN is secondary because the Eurozone's design flaw means financial stress is the most likely trigger mechanism. F_GPT captures how great power dynamics (US reliability, Russia threat) affect European cohesion. F_MENA and F_SSA capture migration pressure as a key political stress vector.

---

## Impact Vector

**Valid variable IDs**: See [[methodology/reference/state-specification]] Appendix A (country-level) and Appendix A.2 (global).

### Analog Basis

| Analog | Event Type | Key Observations | Relevance |
|--------|------------|------------------|-----------|
| **Argentina 2001** | Currency board collapse | GDP -11% single year; banking crisis; 5+ year recovery | Disorderly eurozone exit |
| **Eurozone 2010-12** | Debt crisis (contained) | GDP -2 to -8% in periphery; ECB saved system | Sub-threshold calibration |
| **USSR dissolution** | Political union collapse | Trade collapsed 50%+; GDP -15 to -50% across successors | Extreme disorderly case |
| **Czechoslovak divorce** | Orderly separation | Minimal GDP impact; successful transition | Orderly template |
| **Brexit** | Single member exit | UK GDP -2 to -4% vs counterfactual; EU minimal impact | Below threshold |

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `eu_cohesion` | ↓ | Falls to <20 | immediate | permanent | Definitional |
| `nato_cohesion` | ↓ | -20 ± 10 points | delayed(6mo) | decaying: half_life=5yr | European defense capacity degraded |
| `eur_reserve_share` | ↓ | -10 ± 5 pp | gradual(3yr) | permanent | Euro ceases to exist or loses credibility |
| `global_trade_volume` | ↓ | -6 ± 3% | delayed(3mo) | decaying: half_life=4yr | Single market collapse, supply chain chaos |
| `global_credit_spread` | ↑ | +120 ± 50 bps | immediate | decaying: half_life=2yr | Full financial contagion |
| `nuclear_stability` | ↓ | -5 ± 3 points | delayed(1yr) | decaying: half_life=5yr | French nuclear doctrine uncertainty |

### EU Member State Impacts

**Germany:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `deu.gdp_growth` | ↓ | -4 ± 2 pp | immediate | decaying: half_life=3yr | Export collapse, Target2 losses (~€1T) |
| `deu.current_account` | ↓ | -5 ± 2.5 pp GDP | delayed(6mo) | decaying: half_life=3yr | Trade rebalancing forced |
| `deu.regime_stability` | ↓ | -20 ± 10 points | delayed(6mo) | decaying: half_life=5yr | Political fallout, blame dynamics |

**France:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `fra.gdp_growth` | ↓ | -3.0 ± 1.5 pp | immediate | decaying: half_life=2yr | Trade, confidence, banking exposure |
| `fra.debt_public` | ↑ | +12 ± 6 pp GDP | gradual(2yr) | permanent | Fiscal stress, bank bailouts |
| `fra.regime_stability` | ↓ | -25 ± 12 points | immediate | decaying: half_life=3yr | Political crisis, Fifth Republic stress |

**Italy:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `ita.gdp_growth` | ↓ | -8 ± 4 pp | immediate | decaying: half_life=4yr | Argentina 2001 reference; banking collapse |
| `ita.debt_public` | ↑ | +20 ± 10 pp GDP | immediate | permanent | Loss of ECB backstop, new lira devaluation |
| `ita.inflation_rate` | ↑ | +8 ± 5 pp | delayed(3mo) | decaying: half_life=2yr | New currency devaluation |
| `ita.regime_stability` | ↓ | -30 ± 15 points | immediate | decaying: half_life=5yr | Political upheaval |

**Poland:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `pol.gdp_growth` | ↓ | -4.0 ± 2.0 pp | delayed(3mo) | decaying: half_life=2yr | Trade disruption, EU funds loss |
| `pol.fdi_net` | ↓ | -3.0 ± 1.5 pp GDP | immediate | decaying: half_life=3yr | Investment freeze |

**Rest of EU (aggregate):**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `rest_eu.gdp_growth` | ↓ | -3.5 ± 2.0 pp | immediate | decaying: half_life=2yr | Weighted average disruption |
| `rest_eu.regime_stability` | ↓ | -20 ± 10 points | delayed(3mo) | decaying: half_life=4yr | Political contagion |

### External Impacts

**United States:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.gdp_growth` | ↓ | -0.8 ± 0.4 pp | delayed(6mo) | decaying: half_life=2yr | Trade and financial linkage |
| `usa.military_spending` | ↑ | +0.3 ± 0.2 pp GDP | gradual(2yr) | permanent | European defense gap |

**United Kingdom:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `gbr.gdp_growth` | ↓ | -1.2 ± 0.6 pp | delayed(3mo) | decaying: half_life=2yr | Financial exposure, trade |
| `gbr.regime_stability` | — | +5 ± 10 points | delayed(1yr) | decaying: half_life=3yr | Brexit vindication narrative |

**China:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.gdp_growth` | ↓ | -0.5 ± 0.3 pp | delayed(6mo) | decaying: half_life=2yr | Export market disruption |
| `chn.alliance_west` | — | Complex | — | — | May attempt to exploit divisions |

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| EU institutional collapse | permanent | N/A | Dissolution is irreversible |
| GDP shocks | decaying | half_life=2-4yr | Economies eventually adapt |
| Trade volume | decaying | half_life=3-4yr | New arrangements form slowly |
| Credit spreads | decaying | half_life=1.5-2yr | Markets reprice over time |
| Regime stability | decaying | half_life=3-5yr | Political systems eventually stabilize |
| NATO cohesion | decaying | half_life=5yr | New security arrangements develop |
| EUR reserve share | permanent | N/A | Euro ceases to exist or loses reserve status |
| Debt increases | permanent | N/A | Accumulated during crisis |

---

## Cascade Effects

### Triggered By

| Source Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 3 years | Financial stress exposes Eurozone weakness |
| DOLLAR_RESERVE_CRISIS | +0.5% | 3 years | Euro under stress as alternative fails |
| RUSSIA_STATE_FAILURE | +0.3% | 2 years | Refugee flows, energy disruption |
| TURKEY_POLITICAL_CRISIS | +0.3% | 2 years | Migration pressure, NATO stress |
| SEVERE_PANDEMIC | +0.4% | 2 years | Coordination failure, fiscal stress |

### Triggers

| Target Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +1.0% | 2 years | European banking contagion |
| DOLLAR_RESERVE_CRISIS | -0.5% | 3 years | Euro alternative eliminated |
| RUSSIA_STATE_FAILURE | +0.2% | 2 years | European instability emboldens challengers |
| TURKEY_POLITICAL_CRISIS | +0.3% | 3 years | NATO weakening, regional instability |

### NATO Interaction

EU fragmentation directly damages NATO through:
- Reduced European defense capacity
- Franco-German coordination collapse
- Eastern European security vacuum
- US strategic reassessment

Impact: `nato_cohesion` -20 ± 10 points (incorporated in global impacts above).

---

## Transmission Channels

### 1. Financial Contagion Channel (Primary)

Banking system interconnections, Target2 imbalances, and sovereign-bank doom loops transmit stress across borders. ECB loss of credibility triggers capital flight.

**Mechanism**: Loss of lender of last resort → bank runs → sovereign stress → deeper bank stress
**Affected regions**: All Eurozone members, UK financial system
**Affected variables**: `gdp_growth`, `debt_public`, `global_credit_spread`, `inflation_rate`

### 2. Trade Disruption Channel

Single market dissolution creates customs barriers, regulatory divergence, and supply chain breaks.

**Mechanism**: Border controls return → just-in-time manufacturing fails → trade volume collapses
**Affected regions**: All EU members, major trading partners
**Affected variables**: `gdp_growth`, `current_account`, `global_trade_volume`

### 3. Political Contagion Channel

EU collapse triggers nationalist movements, coalition collapses, and regime instability across members.

**Mechanism**: EU failure narrative → domestic opposition empowered → government instability
**Affected regions**: All EU members
**Affected variables**: `regime_stability`, `institutional_quality`

### 4. Security Vacuum Channel

European defense capacity degraded; NATO coordination impaired.

**Mechanism**: Franco-German engine fails → European pillar of NATO weakened → US burden increases
**Affected regions**: Europe, transatlantic
**Affected variables**: `nato_cohesion`, `military_spending`, `alliance_west`

---

## Aftermath Branches

Once fragmentation occurs, the aftermath unfolds through one of two trajectories:

**Branch 1: Extended Crisis (60%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Multi-year economic crisis across former EU; slow recovery |
| **Duration** | 5-10 years of elevated stress |
| **Factor modifications** | F_EUR: +0.5 for 10 years; F_FIN: +0.4 for 5 years |

- Banking crises in multiple countries simultaneously
- Debt restructurings (Italy, Greece, Portugal, possibly Spain)
- Political instability throughout former EU
- Recovery begins only after crisis exhaustion
- Model: Eurozone 2010-12 if ECB had failed, but worse

**Branch 2: Rapid Reorganization (40%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Crisis forces rapid new arrangements; faster-than-expected stabilization |
| **Duration** | New order within 3-5 years |
| **Factor modifications** | F_EUR: +0.35 for 5 years; F_FIN: +0.25 for 3 years |

- External pressure (security threats, economic necessity) forces cooperation
- New bilateral or mini-lateral institutions built quickly from necessity
- Northern core may form tighter arrangements post-crisis
- Still significant disruption but contained faster than expected

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete |
| **Revision note** | Removed "Orderly Fragmentation" resolution — negotiated restructuring into differentiated tiers is not a discontinuity but managed evolution (the EU already has opt-outs, multi-speed mechanisms, enhanced cooperation). If actors can coordinate an orderly transition, the threshold hasn't been crossed. Event now models only disorderly collapse. |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | High-impact event; Level 2 could model Italian debt dynamics and ECB capacity limits |

## Sources

- Academic literature on monetary union sustainability
- Eurozone crisis (2010-12) case studies
- Comparative literature on political union dissolution
- ECB policy analysis
- [[research/21st-century-assessment]]
- [[events/financial/global-financial-crisis]]
- [[events/financial/dollar-reserve-crisis]]

## Open Questions

1. **Italian debt threshold**: At what debt/GDP ratio does ECB capacity actually fail? 160%? 180%? 200%?

2. **Target2 crystallization**: How would €1T+ German claims be resolved in collapse? Total loss or partial recovery through successor state negotiations?

3. **French nuclear posture**: Does EU collapse force France to reconsider nuclear sharing or trigger German proliferation pressure?

4. **UK role post-collapse**: Would post-Brexit UK facilitate European reorganization or exploit the chaos?

5. **NATO survival**: Can NATO function effectively with a fragmented Europe, or does EU collapse cascade to NATO dysfunction?

6. **Time-varying probability**: Probability likely increases as Italian demographics worsen fiscal trajectory. Current 0.4% may be an underestimate for 2040s-2050s.

7. **Why not orderly?**: The specification assumes orderly fragmentation is not a discontinuity. This could be wrong if a formal Eurozone dissolution (not just restructuring) could be managed. Historical precedent (Czechoslovakia) suggests orderly separation is possible but EU complexity makes it unlikely.

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Critical review: replaced synthetic variables (eu_cohesion, regime_stability, institutional_quality) with observables; added Case Against and Probability Evolution sections | Task 2.4 systematic review |
| 2025-12-21 | Removed "Orderly Fragmentation" resolution | Negotiated restructuring is managed evolution, not discontinuity |
| 2025-12-20 | Initial Level 1 specification | Type 2 threshold event |

---

*Cross-references*: [[events/financial/global-financial-crisis]], [[events/financial/dollar-reserve-crisis]], [[events/geopolitical/russia-state-failure]], [[events/geopolitical/turkey-political-crisis]], [[methodology/reference/causal-types]], [[methodology/reference/type-3-calibration]], [[research/21st-century-assessment]]