---
title: US-China Economic Rupture
type: note
permalink: events/geopolitical/us-china-economic-rupture
tags:
- event
- type-3
- geopolitical
- economic
- supply-chain
- us-china
- level-1
---

# US-China Economic Rupture

**Type 3 (Contingent) Event** — Crisis-driven escalation to comprehensive economic separation between the United States and China.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | `US_CHINA_ECONOMIC_RUPTURE` |
| **Scale** | Global |
| **Domain** | Geopolitical / Economic |
| **Causal Type** | Type 3: Contingent |
| **Onset Speed** | Rapid (weeks to months) |
| **Reversibility** | Partial (supply chains don't easily reconstitute) |

## Description

Crisis-driven escalation from managed competition to comprehensive economic separation — broad trade embargo, financial exclusion, investment prohibitions, and export controls across sectors. Distinguished from gradual decoupling (ongoing baseline trajectory) by acute onset and comprehensive scope. Distinguished from Taiwan Conflict by non-military trigger — this event captures economic warfare that occurs through diplomatic/political escalation without shots fired.

The discontinuity is *comprehensive rupture implemented under crisis conditions* — forcing immediate supply chain reorganization without the years of adjustment that gradual decoupling allows.

---

## Causal Type Specification

### Type 3 (Contingent) Event

This event has Type 3 structure: preconditions create crisis windows, and actor decisions (policymakers in US, China, and allied capitals) determine whether comprehensive measures are implemented.

**Probability decomposition**:

- **P(crisis window)**: ~2.5% annually — acute bilateral crisis develops from non-military trigger
- **P(discontinuity | window)**: ~70% — comprehensive or managed separation occurs
- **P(event)**: ~1.75% annually — rounded to ~1.5-2.0%

The ~30% of crisis windows that de-escalate without major policy change are *non-events* — they don't appear in the simulation as discontinuities.

**Window Preconditions**:

| Condition | Threshold |
|-----------|-----------|
| F_GPT (Great Power Tension) | Elevated above baseline |
| Triggering incident | Non-military crisis of sufficient magnitude (see below) |
| Allied alignment | At least partial coordination among US, EU, Japan |

**Triggering incident categories** (non-military):

1. **Cyber attack**: Major attributed attack on critical infrastructure (power grid, financial system, telecommunications)
2. **Espionage scandal**: Revelation of systematic penetration of defense systems, technology theft at scale
3. **South China Sea incident**: Vessel collision, standoff, or sovereignty assertion that doesn't escalate to Taiwan-level military action
4. **Retaliation spiral**: Rare earth embargo → counter-sanctions → escalation cycle
5. **Allied coordination**: US + EU + Japan + Korea reach alignment on comprehensive controls
6. **Financial trigger**: Chinese action against US financial interests (asset seizures, debt weaponization) or vice versa

**Historical basis for window probability (~2.5%)**:

Near-miss incidents and crises that could have triggered comprehensive measures:

- 2001 EP-3 incident (aircraft collision, detained crew)
- 2018-2019 trade war escalation (approached comprehensive but pulled back)
- 2020 COVID-origin tensions (political pressure for major action)
- 2023 balloon incident (triggered some measures, could have gone further)
- Ongoing: Huawei/semiconductor escalation, TikTok disputes

Pattern: Bilateral crises reaching acute phase occur roughly every 3-5 years. Most de-escalate or result in targeted (not comprehensive) measures. Window probability reflects crises severe enough to create political space for comprehensive action.

**Historical basis for discontinuity probability given window (~70%)**:

Once a crisis reaches sufficient severity, political dynamics favor action:
- Domestic pressure to "do something" is intense
- Targeted measures may be seen as insufficient
- First-mover advantages in economic warfare create pressure to act decisively
- Allied coordination, once achieved, creates momentum

The 30% non-event probability reflects:
- Economic costs create countervailing pressure
- Business lobbying against comprehensive measures
- Diplomatic off-ramps remain available
- Neither side wants to foreclose future options entirely

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | ~1.75% |
| **Low bound** | 1.0% |
| **High bound** | 3.0% |
| **Confidence** | Medium |
| **25-year cumulative** | ~35% (at least one discontinuity) |

### Derivation

1. **Window probability**: 2.5% annually (2-4% range)
2. **Discontinuity given window**: 70% (60-80% range)
3. **Combined**: 2.5% × 70% = 1.75%

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Taiwan Conflict | ~2.0% | Slightly higher — military trigger more binary |
| US-China Economic Rupture | ~1.75% | — |
| Dollar Reserve Crisis | ~1.5% | Similar — different trigger, overlapping consequences |
| Chinese Economic Crisis | ~2.0% | Higher — multiple pathways |
| Global Financial Crisis | ~3.0% | Higher — more frequent, less actor-dependent |

### Key Uncertainties

- **Allied coordination trajectory**: EU/Japan/Korea alignment dramatically affects feasibility and impact
- **Domestic political dynamics**: US election cycles affect appetite for disruptive action
- **Business lobby effectiveness**: Can economic interests restrain escalation?
- **Chinese retaliation capacity**: Rare earth, pharmaceutical, manufacturing leverage
- **Financial interdependence**: Treasury holdings, cross-border investment exposure

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.00 | No direct pathway |
| F_FIN | 0.30 | Financial stress may precipitate crisis or amplify effects |
| F_HLTH | 0.05 | Pandemic-related supply chain stress could contribute |
| F_GPT | 0.75 | Great power tension is primary driver |
| F_FOOD | 0.00 | No direct pathway |
| F_TECH | 0.25 | Technology competition fuels tensions |
| F_EUR | 0.15 | European alignment affects scope and impact |
| F_MENA | 0.00 | No direct pathway |
| F_SAS | 0.00 | No direct pathway |
| F_EAS | 0.40 | Regional dynamics contribute to tension |
| F_SSA | 0.00 | No direct pathway |
| F_LAM | 0.00 | No direct pathway |

**Sum of squared loadings**: 0.87 ✓

### Loading Rationale

F_GPT is dominant because economic rupture is fundamentally a great power competition phenomenon — the economic measures are instruments of strategic competition, not responses to economic conditions per se. F_EAS contributes because regional incidents (South China Sea, Taiwan-adjacent tensions) are primary crisis triggers. F_FIN and F_TECH reflect the financial and technological dimensions of competition. F_EUR matters because European alignment (or non-alignment) affects both the likelihood of coordinated action and the severity of global impacts.

---

## Resolutions

Once a crisis window opens *and* a discontinuity occurs (70% of windows), one of two resolutions:

```yaml
resolutions:
  - id: full_rupture
    probability: 0.50
    description: |
      Comprehensive economic separation implemented under crisis conditions.
      Broad trade embargo (majority of bilateral trade affected).
      Financial exclusion (SWIFT-adjacent measures, asset freezes, investment prohibitions).
      Export controls across sectors (not just semiconductors).
      Forced rapid supply chain reorganization.
      
  - id: managed_separation
    probability: 0.50
    description: |
      Accelerated but targeted decoupling.
      Sector-specific comprehensive measures (technology, critical minerals, strategic goods).
      Financial restrictions short of full exclusion.
      Longer adjustment timeline than full rupture.
      Represents discontinuity from baseline trajectory but less severe than full rupture.

resolution_probability_rationale:
  default: "uniform (50/50)"
  specified: "50/50"
  justification: |
    No clear structural asymmetry identified at Level 1.
    
    Arguments for full rupture dominance:
    - Crisis dynamics favor decisive action
    - Targeted measures may be seen as half-measures
    - Domestic political pressure for strong response
    
    Arguments for managed separation dominance:
    - Economic costs create powerful resistance
    - Business lobbying for carve-outs
    - Allied partners may not support full measures
    - Off-ramps remain attractive to both sides
    
    These factors roughly balance. Defaulting to uniform pending
    Level 2 analysis of crisis decision-making dynamics.
    
  confidence: "n/a (using default)"
```

---

## Aftermath Branches

### Full Rupture Aftermath

```yaml
resolution: full_rupture
aftermath_branches:

  - id: sustained_separation
    probability: 0.65
    description: |
      Comprehensive separation persists and deepens.
      Two economic blocs emerge with limited cross-bloc trade.
      Supply chains reorganize around bloc boundaries.
      New trade/financial architecture develops within blocs.
      
    factor_modifications:
      F_GPT: +0.50
      F_FIN: +0.60
      F_EAS: +0.40
      F_TECH: +0.35
      F_EUR: +0.25
      
    duration:
      type: decaying
      half_life_years: 8
      floor: 0.30
      
    impact_vector:
      global:
        trade_volume: [-0.25, 0.08]  # mean, std
        inflation: [+0.04, 0.02]  # percentage points
        gdp_growth: [-0.02, 0.01]  # percentage points annually
        supply_chain_resilience: [-0.40, 0.15]
        financial_stability: [-0.35, 0.10]
      united_states:
        consumer_prices: [+0.08, 0.03]  # one-time level shift
        manufacturing_capacity: [-0.15, 0.05]  # short-term
        gdp: [-0.03, 0.01]
        strategic_autonomy: [+0.30, 0.10]
      china:
        gdp: [-0.06, 0.02]
        export_revenue: [-0.25, 0.08]
        technology_access: [-0.50, 0.15]
        domestic_consumption_share: [+0.10, 0.05]
      european_union:
        gdp: [-0.02, 0.01]
        strategic_autonomy_pressure: [+0.40, 0.15]
        alliance_cohesion: [-0.20, 0.10]  # differential impacts create strain
      japan:
        gdp: [-0.03, 0.01]
        supply_chain_disruption: [-0.30, 0.10]
      southeast_asia:
        manufacturing_relocation: [+0.25, 0.10]  # "friendshoring" beneficiary
        gdp: [+0.01, 0.01]  # net positive from relocation despite disruption

  - id: partial_reconciliation
    probability: 0.35
    description: |
      After initial comprehensive measures, partial walkback occurs.
      Economic pain forces negotiation.
      Some trade/financial links restored, but not to pre-crisis levels.
      Hybrid state: neither full integration nor full separation.
      
    factor_modifications:
      F_GPT: +0.30
      F_FIN: +0.35
      F_EAS: +0.25
      
    duration:
      type: decaying
      half_life_years: 5
      floor: 0.15
      
    impact_vector:
      global:
        trade_volume: [-0.12, 0.05]
        inflation: [+0.02, 0.01]
        supply_chain_resilience: [-0.20, 0.08]
      united_states:
        consumer_prices: [+0.04, 0.02]
        gdp: [-0.015, 0.008]
      china:
        gdp: [-0.03, 0.01]
        export_revenue: [-0.12, 0.05]

aftermath_probability_rationale: |
  Sustained separation weighted higher (0.65) based on:
  - Path dependence: once supply chains reorganize, reconstitution is costly
  - Political dynamics: admitting failure of comprehensive measures is difficult
  - Sunk costs in new arrangements (friendshoring investments, alternative suppliers)
  - Trust destruction: even if formal measures lift, business behavior changes
  
  Partial reconciliation possible (0.35) if:
  - Economic pain exceeds political tolerance in one or both countries
  - Leadership change creates political space for de-escalation
  - Third-party mediation (unlikely but possible)
  - Specific trigger incident is resolved or attribution is questioned
```

### Managed Separation Aftermath

```yaml
resolution: managed_separation
aftermath_branches:

  - id: controlled_decoupling
    probability: 0.60
    description: |
      Accelerated but orderly decoupling continues.
      Clear sector boundaries (technology/strategic vs. consumer goods).
      Supply chain adjustment proceeds over 3-5 years.
      Financial links partially preserved.
      
    factor_modifications:
      F_GPT: +0.25
      F_FIN: +0.20
      F_TECH: +0.30
      
    duration:
      type: decaying
      half_life_years: 6
      floor: 0.15
      
    impact_vector:
      global:
        trade_volume: [-0.10, 0.04]
        inflation: [+0.015, 0.008]
        supply_chain_resilience: [-0.15, 0.06]
      united_states:
        consumer_prices: [+0.03, 0.015]
        gdp: [-0.01, 0.005]
        technology_leadership: [+0.10, 0.05]
      china:
        gdp: [-0.025, 0.01]
        technology_access: [-0.30, 0.10]

  - id: escalation_to_full_rupture
    probability: 0.40
    description: |
      Managed separation proves unstable.
      Retaliation cycles, enforcement disputes, or new incidents
      trigger escalation to full rupture.
      Delay but not prevention of comprehensive separation.
      
    factor_modifications:
      F_GPT: +0.45
      F_FIN: +0.50
      
    duration:
      type: decaying
      half_life_years: 7
      floor: 0.25
      
    cascade_triggers:
      - event_id: US_CHINA_ECONOMIC_RUPTURE
        note: "Effectively transitions to full_rupture aftermath"
        
    impact_vector:
      # Similar to sustained_separation but delayed onset
      global:
        trade_volume: [-0.22, 0.07]
        inflation: [+0.035, 0.015]

aftermath_probability_rationale: |
  Controlled decoupling weighted higher (0.60) because:
  - Managed separation by definition reflects some restraint
  - Economic interests that prevented full rupture continue to operate
  - Sector boundaries create natural stopping points
  
  Escalation risk significant (0.40) because:
  - Managed separation creates grievances without resolution
  - Enforcement disputes are likely
  - New incidents can occur during adjustment period
  - Domestic political pressure for "finishing the job"
```

---

## Supply Chain Impact Detail

### Critical Categories

| Category | US Import Dependence | Substitution Timeline | Acute Impact |
|----------|---------------------|----------------------|--------------|
| Consumer electronics | ~70% | 2-4 years | High |
| Pharmaceutical APIs | ~80% | 3-5 years | Critical |
| Rare earth elements | ~80% | 5-10 years | Critical |
| Industrial machinery | ~25% | 1-2 years | Moderate |
| Textiles/apparel | ~35% | 1-2 years | Low-Moderate |
| Furniture/household | ~50% | 1-2 years | Moderate |
| Auto parts | ~15% | 1-2 years | Moderate |
| Solar panels | ~80% | 3-5 years | High |
| Batteries/EVs | ~70% | 3-5 years | High |

### Chinese Retaliation Vectors

| Vector | US Vulnerability | Impact Severity |
|--------|-----------------|-----------------|
| Rare earth export ban | High (defense, electronics, EVs) | Critical |
| Pharmaceutical API cutoff | High (generic drugs, antibiotics) | Critical |
| Treasury holdings sale | Moderate (market disruption, rates) | High |
| Manufacturing exit costs | High (Apple, auto supply chains) | High |
| Critical minerals | High (lithium, cobalt processing) | Critical |

### Differential Country Impacts

**Exposure variable**: bilateral_trade_china_share

**High exposure (GDP impact 1.5-2x base)**:
- Australia, South Korea, Taiwan, Vietnam, Malaysia
- Germany, Netherlands (European manufacturing hubs)

**Moderate exposure (GDP impact 1x base)**:
- Japan, United Kingdom, France, Canada

**Low exposure / beneficiaries**:
- India, Mexico, Indonesia (friendshoring recipients)
- Some ASEAN (depends on bloc alignment)

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Financial stress | CHINESE_ECONOMIC_CRISIS | ×1.5 | 5 years | Export collapse, capital flight, confidence shock |
| De-dollarization pressure | DOLLAR_RESERVE_CRISIS | ×1.3 | 10 years | Accelerated reserve diversification, alternative payment systems |
| Systemic financial risk | GLOBAL_FINANCIAL_CRISIS | +1.5% | 3 years | Asset freezes, counterparty uncertainty, trade finance collapse |
| Alliance strain | EU_FRAGMENTATION | ×1.2 | 5 years | Differential impacts, strategic autonomy debates |
| Opportunistic action | TAIWAN_CONFLICT | Note | — | Complex: may increase (use it or lose it) or decrease (economic costs) |

### Impact Chains

**Chain 1**: Rupture → Pharmaceutical shortage → Health system stress → F_HLTH elevation → Pandemic vulnerability

**Chain 2**: Rupture → Rare earth shortage → Defense production constraints → Alliance credibility questions → F_GPT elevation

**Chain 3**: Rupture → Inflation shock → Central bank tightening → Financial stress → GLOBAL_FINANCIAL_CRISIS probability increase

---

## Transmission Channels

### Trade Channel
**Mechanism**: Direct interruption of goods flows; tariffs/embargoes make bilateral trade uneconomic
**Affected regions**: US, China, East Asia, Europe (through supply chains)
**Affected variables**: trade_volume, consumer_prices, manufacturing_output, gdp

### Financial Channel
**Mechanism**: Asset freezes, payment system exclusion, investment prohibitions, currency volatility
**Affected regions**: Global (through financial linkages)
**Affected variables**: financial_stability, exchange_rates, capital_flows, credit_availability

### Supply Chain Channel
**Mechanism**: Intermediate goods shortages, production bottlenecks, forced supplier switching
**Affected regions**: Global manufacturing (autos, electronics, machinery)
**Affected variables**: manufacturing_output, supply_chain_resilience, inventory_costs

### Technology Channel
**Mechanism**: Export controls, IP restrictions, talent mobility constraints
**Affected regions**: US, China, technology-intensive economies
**Affected variables**: technology_access, innovation_capacity, productivity_growth

### Signaling Channel
**Mechanism**: Demonstration effects on other relationships; precedent for economic warfare
**Affected regions**: Global (affects all trade relationships)
**Affected variables**: trade_policy_uncertainty, alliance_dynamics, investment_decisions

---

## Interaction with Taiwan Conflict

**If Taiwan Conflict occurs first**: Economic rupture is likely subsumed — the military conflict triggers economic separation as a consequence, and the economic impacts are captured in Taiwan Conflict aftermath. In simulation terms, this event's window probability should drop significantly (to ~0.5%) if Taiwan Conflict has occurred in prior 5 years.

**If Economic Rupture occurs first**: Does not preclude Taiwan Conflict but may affect its probability:
- Argument for increase: Economic separation removes interdependence constraints on military action
- Argument for decrease: Economic costs already imposed; less to lose from military restraint
- Net effect: Uncertain; default to no modification pending Level 2 analysis

**Modeling note**: These events are partially substitutable in their economic consequences but have different triggers and different probability structures. Both belong in the catalog.

---

## Case Against

### 1. Gradual decoupling makes acute rupture less likely

**Argument**: Ongoing decoupling (reshoring, friendshoring, diversification) reduces the stakes of any single crisis. By the time a triggering incident occurs, supply chains may already be sufficiently diversified that comprehensive measures are unnecessary or less costly.

**Counter**: Gradual decoupling is proceeding slowly and faces business resistance. As of 2025, China remains deeply embedded in global supply chains. A crisis in the next 5-10 years would still cause severe disruption. Moreover, partial decoupling may create false confidence that comprehensive measures are manageable.

### 2. Mutual economic destruction prevents escalation

**Argument**: Both sides understand that comprehensive rupture would be economically devastating. Rational actors will pull back from the brink, as they have in previous crises (2018-2019 trade war, 2020 COVID tensions).

**Counter**: Previous crises occurred before the most recent escalation in strategic competition. Semiconductor export controls, entity lists, and investment screening represent a new baseline. The "rationality" argument assumes economic interests dominate, but nationalist/security concerns may override economic logic, especially in crisis conditions.

### 3. Allied coordination is too difficult

**Argument**: Full rupture requires coordination among US, EU, Japan, Korea. European and Asian allies have stronger economic ties to China and weaker security motivations. They will defect from comprehensive measures, limiting scope to managed separation at most.

**Counter**: Allied coordination has improved significantly (AUKUS, semiconductor export controls, critical minerals agreements). A sufficiently severe trigger (major cyber attack, direct provocation) could generate aligned response. Moreover, US secondary sanctions can force alignment even without voluntary cooperation.

### What would change estimate 2x+

| Change | Direction | Magnitude |
|--------|-----------|-----------|
| Major attributed cyber attack on US infrastructure | ↑ | +100% window probability |
| EU-US comprehensive trade/tech alignment | ↑ | +50% probability given window |
| Chinese rare earth preemptive embargo | ↑ | +75% window probability |
| Successful US-China crisis management framework | ↓ | -40% probability given window |
| Rapid supply chain diversification (5+ years) | ↓ | -30% impact severity |
| Chinese financial/Treasury retaliation threat credible | ↓ | -25% probability given window |

---

## Sensitivity Analysis Notes

Key uncertainties for Phase 3 sensitivity testing:

| Parameter | Range to Test | Why It Matters |
|-----------|---------------|----------------|
| Window probability | 0.015 - 0.04 | Drives expected timing |
| Discontinuity given window | 0.55 - 0.85 | Determines how many crises produce lasting change |
| Full vs. managed split | 0.35/0.65 to 0.65/0.35 | Major difference in severity |
| Supply chain adjustment time | 2-5 years vs. 5-10 years | Affects duration of acute impacts |
| Chinese retaliation effectiveness | 0.3 - 0.7 | Rare earth, pharma, financial vectors |
| Allied coordination | 0.4 - 0.8 | Affects scope and enforceability |

---

## Research Upgrade Path

**Level 2 (4-8 hours)**:
- Detailed supply chain mapping for critical categories
- Chinese retaliation capacity assessment (rare earths, pharma, financial)
- Allied coordination precedents and constraints
- Historical economic warfare cases (Russia sanctions, Iran sanctions) for impact calibration
- Business lobby effectiveness in crisis conditions

**Level 3 (20+ hours)**:
- Expert elicitation on supply chain adjustment timelines
- Pharmaceutical API dependency deep-dive
- Rare earth substitution and alternative source analysis
- Financial system stress testing for asset freeze scenarios
- Sector-by-sector impact modeling

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-22 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Supply chain adjustment timelines; pharmaceutical/rare earth vulnerability; Chinese retaliation capacity |

## Sources

- Level 1 specification from prior knowledge
- Calibration against existing catalog events (Taiwan Conflict, Dollar Reserve Crisis, Chinese Economic Crisis)

## Open Questions

- Pharmaceutical API substitution timeline and feasibility
- Rare earth alternative sources and processing capacity
- Chinese Treasury holdings as leverage: credible threat or mutual destruction?
- Allied coordination dynamics under crisis pressure
- Supply chain adjustment costs and timelines by sector
- Interaction effects with Taiwan Conflict probability
- Financial system resilience to asset freeze scenarios
- Secondary sanctions effectiveness and allied response

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/taiwan-conflict]] for comparable Type 3 specification*