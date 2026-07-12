---
permalink: methodology/concepts/monte-carlo-framework
---

# Discontinuity Effects Model: Methodology Framework

## A Monte Carlo Framework for Geopolitical Shock Distribution Analysis

**Document Version:** 1.1  
**Date:** December 2025  
**Status:** Methodology specification (pre-implementation)

> ⚠️ **Partially superseded** (July 2026). §§8–9 (Simulation Mechanics,
> Implementation Architecture) describe the original independent-factor, static
> sampler and predate the current schema. The v0.1 engine is defined by
> [[methodology/reference/simulator-architecture]] (ADRs) and executed per
> [[methodology/project/implementation-guide]]. In particular: factor draws are
> correlated over Ω (ADR-2 — not §8's independent normals), idiosyncratic
> variance is `1 − (ΛΩΛᵀ)ᵢᵢ` (not §8's `1 − Σλ²`), the sampler is a stateful
> path-dependent stepper (not §8's static `U < p` comparison), and §8.6
> compound multipliers are **retired** (implementation-guide pinned decision #5).
> The earlier sections remain live conceptual foundations; wherever this
> document conflicts with the ADRs or [[methodology/reference/event-yaml-schema]],
> they win.

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Foundational Assumptions](#2-foundational-assumptions)
3. [Architectural Approach](#3-architectural-approach)
4. [Event Taxonomy](#4-event-taxonomy)
5. [Probability Estimation Methodology](#5-probability-estimation-methodology)
6. [Factor Model for Event Correlation](#6-factor-model-for-event-correlation)
7. [Outcome Variables](#7-outcome-variables)
8. [Simulation Mechanics](#8-simulation-mechanics)
9. [Implementation Architecture](#9-implementation-architecture)
10. [Validation and Sensitivity Analysis](#10-validation-and-sensitivity-analysis)
11. [Limitations and Future Extensions](#11-limitations-and-future-extensions)
12. [Event Catalog Template](#12-event-catalog-template)

---

## 1. Purpose and Scope

### 1.1 Objective

This document specifies a **discontinuity effects model**—a Monte Carlo framework for characterizing the distribution of geopolitical, environmental, and economic shocks over multi-decade time horizons. 

The model will:

- Catalog discrete discontinuities (events that materially alter trajectories)
- Estimate occurrence probabilities with explicit uncertainty
- Capture event clustering through a latent factor correlation structure
- Generate thousands of simulated shock sequences
- Produce distributions of cumulative impacts for planning-relevant variables

### 1.2 What This Model Does and Does Not Do

**This model answers:**
- What is the distribution of cumulative shocks over 20-50 years?
- How often do "severe" vs. "moderate" vs. "benign" shock scenarios occur?
- Which events and factors contribute most to tail risk?
- How much does event clustering (correlation) affect outcome distributions?

**This model does NOT answer:**
- What will GDP/inflation/etc. be in 2045? (We model shocks, not levels)
- What is the optimal investment strategy? (We don't model asset returns)
- What happens if we prevent Event X? (No causal/counterfactual reasoning)
- How do specific transmission mechanisms work? (Impacts are directly estimated)

The model produces **shock distributions**, not **world-state predictions**. It is one component of a broader scenario analysis effort, not a complete forecasting system.

### 1.3 Planning Context

This model supports long-horizon strategic planning (15-30 year timeframes) under conditions of deep uncertainty. It is designed to:

- Characterize tail risk from correlated discontinuities
- Test intuitions about crisis probability (e.g., "60% chance of severe crisis")
- Identify which risk factors drive worst-case outcomes
- Inform defensive positioning against severe but plausible scenarios

The model explicitly acknowledges that precise prediction is impossible. The goal is **calibrated uncertainty**—shock distributions that honestly reflect what we don't know while incorporating what we do.

### 1.4 Scope Boundaries

**In scope:**
- Discrete discontinuities at global, regional, and selected national scales
- Environmental, political, economic, health, and technological domains
- Time horizon: 2025-2075 (50 years), with focus on 2025-2050
- Cumulative shock impacts on planning-relevant variables

**Out of scope (this model):**
- Baseline trajectory modeling (handled separately)
- State variables and dynamic probability updating (future extension)
- Transmission mechanism modeling (future extension)
- Agent-based strategic interaction
- Asset return modeling

### 1.5 Relationship to Broader Simulation Effort

This discontinuity effects model is designed as a **module** within a larger scenario simulation architecture:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SCENARIO SIMULATION (Future)                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐ │
│  │ Baseline        │    │ DISCONTINUITY   │    │ State Variable  │ │
│  │ Trajectories    │ +  │ EFFECTS MODEL   │ +  │ Dynamics        │ │
│  │ (deterministic) │    │ (this document) │    │ (future)        │ │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘ │
│           │                      │                      │          │
│           └──────────────────────┼──────────────────────┘          │
│                                  ▼                                  │
│                    ┌─────────────────────────┐                     │
│                    │ Integrated World-State  │                     │
│                    │ Distributions           │                     │
│                    └─────────────────────────┘                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

The current document specifies only the discontinuity effects module.

### 1.6 Relationship to Existing Analysis

This model builds on and operationalizes analysis contained in companion documents:

- `21st_century_assessment.md` — Regional demographic and climate trajectories
- `collapse-patterns-predictive-framework.md` — Historical collapse patterns and risk factors
- `brics-dedollarization-us-impact-research-2025.md` — Financial system transition analysis
- `financial-strategy-analysis-2025.md` — Personal planning context and constraints

The event catalog will draw heavily on these documents for probability estimation and impact quantification.

---

## 2. Foundational Assumptions

### 2.1 Epistemological Stance

**Deep uncertainty, not calculable risk**: We are estimating probabilities for events without reliable base rates. Expert judgment, historical analogy, and structural analysis inform estimates, but precision is illusory. All probabilities should be understood as distributions, not point estimates.

**Correlations are real but imprecisely known**: Events cluster. Climate stress, economic crisis, and political instability are not independent. We capture this through explicit correlation structure while acknowledging that correlation estimates are themselves uncertain.

**Fat tails matter**: Extreme outcomes are more likely than normal distributions suggest. The model should not assume away tail risk through convenient distributional assumptions.

**Path dependence exists but is simplified**: In reality, events in Year 5 depend on the specific sequence of events in Years 1-4. The initial model treats years as largely independent draws from a correlated distribution, accepting this as a simplification. Future extensions may add state variables that carry forward.

### 2.2 Structural Assumptions

**No sudden technological salvation**: The model does not assume breakthrough technologies (fusion, strong AI, geoengineering) that would fundamentally alter constraints. If such breakthroughs occur, they can be modeled as discontinuities with low probability and high impact.

**Political systems respond slowly**: Democracies and authoritarian systems alike face constraints on rapid policy change. The model assumes policy responses lag emerging crises, consistent with historical patterns.

**Climate trajectory is largely locked in**: Emissions reductions may alter the 2050-2100 trajectory but have limited effect on 2025-2050. The model assumes continued high emissions as the base case.

**Geographic and demographic fundamentals persist**: Countries cannot relocate; populations change slowly. The structural advantages and vulnerabilities identified in the 21st century assessment are relatively fixed.

### 2.3 Baseline Trajectory

The model defines a "baseline" against which discontinuities are measured:

- **Climate**: 2.5-3.5°C warming by 2100, with proportional impacts by mid-century
- **Demographics**: UN median projections with adjustments for climate mortality in vulnerable regions
- **Economics**: Trend growth rates by region, with gradual shift toward multipolarity
- **Politics**: Continuation of current institutional arrangements absent discontinuities

Discontinuities represent **departures from this baseline**—events that materially alter the expected trajectory.

---

## 3. Architectural Approach

### 3.1 Selected Approach: Correlation-Based Sampling (Approach A)

The initial implementation uses a correlation-based Monte Carlo approach:

1. **Event catalog**: Comprehensive list of discontinuities with base probabilities
2. **Correlation matrix**: Pairwise correlations capturing tendency to co-occur
3. **Correlated sampling**: Generate correlated random draws each simulation period
4. **Threshold comparison**: Events occur when draws fall below probability thresholds
5. **Impact accumulation**: Aggregate impacts across events and time periods
6. **Distribution analysis**: Analyze outcome distributions across simulation runs

### 3.2 Rationale for Approach A

**Advantages:**
- Tractable implementation with standard tools
- Forces systematic probability estimation
- Captures the most important feature (event clustering) without excessive complexity
- Interpretable parameters (correlations have intuitive meaning)
- Fast simulation allows many runs for stable percentile estimates

**Accepted limitations:**
- Does not capture causal direction (correlation is symmetric)
- Limited dynamic updating (each period largely independent)
- Cannot answer counterfactual queries ("what if we prevented X?")
- Correlations are static across simulation horizon

These limitations are acceptable for initial implementation. The approach provides useful output while building the foundation for future enhancement.

### 3.3 Path to Future Enhancement

Approach A provides scaffolding for later transition to causal modeling (Approach B):

```
APPROACH A                          APPROACH B
───────────────────────────────     ───────────────────────────────
Event catalog          ─────────►   Event catalog (same)
                                    
Correlation matrix     ─────────►   Guides causal edge placement
                                    
                                    Directed acyclic graph
                                    
                                    Conditional probability tables
                                    
                                    State variables (continuous)
                                    
                                    Dynamic updating across periods
```

The event catalog and probability estimates transfer directly. Correlation estimates guide where to place causal edges. The transition adds structure without discarding initial work.

---

## 4. Event Taxonomy

### 4.1 Scale Hierarchy

Events are categorized by geographic scale:

#### Global Scale
Events affecting multiple regions or the entire world system:
- Climate tipping points (AMOC, Amazon, permafrost)
- Pandemics
- Global financial crises
- Major power conflicts
- Technological discontinuities

#### Regional Scale
Events affecting a geographic region or bloc:
- Regional conflicts
- Economic bloc restructuring (EU integration/fragmentation)
- Regional climate impacts (monsoon failure, regional drought)
- Migration crises
- Regional financial contagion

#### National Scale
Events affecting individual countries with significant spillovers:
- State failure in major countries
- Political discontinuities in key states
- Sovereign defaults with systemic implications
- National-level climate catastrophe

### 4.2 Domain Categories

Events are cross-classified by domain:

#### Environmental
- Climate tipping points
- Extreme weather events (drought, flood, storm)
- Sea level rise thresholds
- Ecosystem collapse
- Resource depletion

#### Health
- Novel pandemics (various severity levels)
- Antibiotic resistance crisis
- Climate-disease interaction
- Healthcare system failures

#### Political
- State failure / collapse
- Regime change (authoritarian, democratic, fragmentation)
- Secession / territorial change
- International conflict
- Institutional transformation (EU, UN, etc.)

#### Economic/Financial
- Currency crises
- Sovereign defaults
- Banking system failures
- Trade system disruption
- Reserve currency transition

#### Technological
- AI disruption (various scenarios)
- Energy breakthroughs
- Cybersecurity failures
- Infrastructure collapse

### 4.3 Event Classification Matrix

Each event in the catalog will be tagged with:

| Attribute | Values |
|-----------|--------|
| Scale | Global, Regional, National |
| Domain | Environmental, Health, Political, Economic, Technological |
| Onset speed | Sudden (<1 year), Rapid (1-5 years), Gradual (5-20 years) |
| Reversibility | Reversible, Partially reversible, Irreversible |
| Precedent | Historical precedent exists, No direct precedent |

---

## 5. Probability Estimation Methodology

### 5.1 The Challenge

We are estimating probabilities for events that:
- May never have occurred (AMOC collapse)
- Have occurred but in different contexts (pandemics, state failures)
- Involve complex causal chains (climate → food → instability)
- Are subject to deep uncertainty and expert disagreement

No methodology produces "correct" probabilities. The goal is **transparent, defensible estimates** that can be updated as understanding improves.

### 5.2 Estimation Approaches by Event Type

#### Events with Historical Base Rates

For events with meaningful historical frequency (e.g., sovereign defaults, coups, recessions):

1. Calculate historical base rate from appropriate reference class
2. Adjust for current conditions (vulnerability indicators, trends)
3. Express uncertainty as probability range, not point estimate

**Example**: Sovereign default in Country X
- Historical base rate for countries with similar debt/GDP: 3% per year
- Current conditions (IMF program, rising stress): Adjustment factor 1.5x
- Estimate: 4-5% per year (expressed as range)

#### Events without Historical Precedent

For unprecedented events (AMOC collapse, AI transformation):

1. Decompose into component conditions that do have precedent
2. Use expert elicitation ranges (published estimates)
3. Apply structural reasoning about mechanisms
4. Express high uncertainty explicitly

**Example**: AMOC collapse
- Expert estimates range from 10% to 40% this century
- Recent research suggests systematic underestimation in models
- Mechanism-based reasoning suggests tipping point dynamics
- Estimate: 15-35% by 2100, with most weight on 2040-2080 window

#### Conditional Events

For events whose probability depends heavily on other events:

1. Estimate unconditional (base) probability
2. Estimate conditional probability given key precursors
3. Use correlation structure to capture dependency

**Example**: Egyptian state failure
- Base probability (current conditions): 3% per year
- Conditional on severe Nile water crisis: 25% per year
- Correlation with Nile crisis event: 0.5+

### 5.3 Probability Representation

All probabilities are specified as:

```
Annual probability: Point estimate (low bound - high bound)
```

**Example**:
```
AMOC significant weakening: 0.015/year (0.008 - 0.025)
                           [~50% chance by 2060 at point estimate]
```

The simulation can use:
- Point estimates for base case
- Low/high bounds for sensitivity analysis
- Full distribution sampling for uncertainty quantification

### 5.4 Calibration Heuristics

To promote calibrated estimates:

| Probability | Interpretation | Calibration anchor |
|-------------|----------------|-------------------|
| 0.01/year | Once per century | AMOC collapse, supervolcano |
| 0.03/year | Once per 30 years | Severe pandemic, major power war |
| 0.05/year | Once per 20 years | Significant regional conflict, major financial crisis |
| 0.10/year | Once per decade | Moderate recession, significant political transition |
| 0.20/year | Once per 5 years | Minor regional crisis, policy discontinuity |

Events with >0.30/year probability are arguably not "discontinuities" but features of the baseline trajectory.

### 5.5 Documentation Requirements

Each probability estimate in the catalog must include:

1. **Point estimate**: Best single value
2. **Range**: Low and high bounds reflecting uncertainty
3. **Basis**: What informs the estimate (historical data, expert opinion, structural reasoning)
4. **Key sensitivities**: What could make the probability much higher or lower
5. **Confidence level**: Self-assessed confidence in the estimate (Low/Medium/High)

---

## 6. Factor Model for Event Correlation

### 6.1 Why Correlations Matter

Independent sampling dramatically underestimates tail risk. If bad events were independent, the probability of multiple simultaneous crises would be the product of individual probabilities (very small). In reality, crises cluster because:

- **Common causes**: Climate stress drives both drought and instability
- **Causal chains**: Drought → food prices → instability
- **Contagion**: Financial crisis in one country spreads to others
- **Feedback loops**: Instability → capital flight → economic crisis → more instability

Correlation structure captures this clustering without requiring full causal specification.

### 6.2 The Factor Model Approach

#### Why Not Direct Pairwise Correlations?

With n events, a correlation matrix requires n(n-1)/2 unique entries. For 75 events, that's 2,775 correlations to estimate. This creates two problems:

1. **Estimation burden**: We cannot meaningfully estimate thousands of pairwise correlations
2. **Validity**: Manually estimated correlation matrices often fail to be positive semi-definite, causing the simulation to fail

#### Factor Model Solution

Instead of estimating pairwise correlations directly, we:

1. Define k **latent factors** representing underlying drivers of event clustering
2. Estimate **factor loadings** for each event (how much does this event respond to each factor?)
3. **Derive** the correlation matrix mathematically from the factor structure

This reduces parameters from O(n²) to O(n×k), guarantees a valid correlation matrix, and provides interpretable structure.

#### Mathematical Structure

Each event i is modeled as:
```
Zᵢ = λᵢ₁F₁ + λᵢ₂F₂ + ... + λᵢₖFₖ + εᵢ
```

Where:
- Zᵢ is the latent propensity for event i (event occurs if Zᵢ exceeds threshold)
- Fⱼ are independent standard normal latent factors
- λᵢⱼ is the loading of event i on factor j
- εᵢ is idiosyncratic noise (independent across events)

The correlation between events i and j is then:
```
corr(Zᵢ, Zⱼ) = Σₖ λᵢₖ × λⱼₖ
```

Events that load heavily on the same factors will be highly correlated.

### 6.3 Latent Factor Definitions

We define 12 latent factors capturing the major drivers of event clustering:

#### Global Systemic Factors

| Factor | ID | Description |
|--------|-----|-------------|
| **Climate Stress** | F_CLIM | Global climate pressure; drives drought, heat events, tipping points, and downstream instability in climate-vulnerable regions |
| **Financial Fragility** | F_FIN | Global financial system stress; drives sovereign defaults, banking crises, currency crises, and contagion |
| **Pandemic/Health** | F_HLTH | Global health system stress; drives pandemics, healthcare failures, and economic disruption |
| **Great Power Tension** | F_GPT | US-China-Russia strategic tension; drives conflicts, trade disruption, and bloc formation |
| **Technology Disruption** | F_TECH | Pace of technological change; drives AI disruption, cybersecurity events, and economic restructuring |

#### Regional Instability Factors

| Factor | ID | Description |
|--------|-----|-------------|
| **European Stress** | F_EUR | European political and economic pressure; drives EU fragmentation, migration crises, fiscal crises |
| **MENA Instability** | F_MENA | Middle East/North Africa stress; drives state failures, conflicts, refugee flows, oil disruption |
| **South Asian Stress** | F_SAS | India-Pakistan-Bangladesh pressure; drives water conflicts, state fragility, nuclear risk |
| **East Asian Tension** | F_EAS | Taiwan, Korea, South China Sea pressure; drives regional conflicts, economic disruption |
| **Sub-Saharan Crisis** | F_SSA | African climate, demographic, governance pressure; drives famines, state failures, displacement |
| **Latin American Stress** | F_LAM | Regional economic and political pressure; drives crises in major economies, migration |

#### Cross-Cutting Factor

| Factor | ID | Description |
|--------|-----|-------------|
| **Food System Stress** | F_FOOD | Global food production and distribution pressure; loads on climate events, amplifies instability in import-dependent regions |

### 6.4 Factor Loading Specification

Each event in the catalog receives a loading on each relevant factor. Loadings range from 0 (no relationship) to ~0.9 (factor almost fully determines event).

#### Loading Strength Guidelines

| Loading | Interpretation |
|---------|----------------|
| 0.0 | No relationship to factor |
| 0.1 - 0.2 | Weak relationship; factor marginally relevant |
| 0.3 - 0.4 | Moderate relationship; factor is one of several drivers |
| 0.5 - 0.6 | Strong relationship; factor is a primary driver |
| 0.7 - 0.8 | Very strong relationship; factor is dominant driver |
| 0.8 - 0.9 | Near-deterministic; event is essentially an expression of factor |

#### Example Factor Loadings

```
EVENT                      F_CLIM  F_FIN  F_HLTH  F_GPT  F_FOOD  F_EUR  F_MENA  F_SAS  F_EAS  F_SSA  F_LAM  F_TECH
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
AMOC_COLLAPSE               0.85    0.0    0.0    0.0    0.3    0.4    0.1    0.0    0.0    0.1    0.0    0.0
AMAZON_TIPPING              0.80    0.0    0.0    0.0    0.4    0.0    0.0    0.0    0.0    0.0    0.3    0.0
SEVERE_PANDEMIC             0.1     0.2    0.90   0.1    0.1    0.2    0.2    0.2    0.2    0.3    0.2    0.0
TAIWAN_CONFLICT             0.0     0.3    0.0    0.85   0.1    0.1    0.0    0.1    0.80   0.0    0.0    0.2
GLOBAL_FINANCIAL_CRISIS     0.1     0.90   0.1    0.2    0.1    0.4    0.2    0.2    0.3    0.2    0.4    0.1
EU_FRAGMENTATION            0.2     0.4    0.1    0.2    0.1    0.85   0.3    0.0    0.0    0.0    0.0    0.0
EGYPT_STATE_FAILURE         0.4     0.2    0.1    0.1    0.5    0.2    0.80   0.0    0.0    0.2    0.0    0.0
PAKISTAN_STATE_FAILURE      0.3     0.2    0.1    0.3    0.4    0.0    0.2    0.85   0.1    0.0    0.0    0.0
SAHEL_CATASTROPHE           0.6     0.1    0.2    0.0    0.6    0.1    0.3    0.0    0.0    0.85   0.0    0.0
US_POLITICAL_CRISIS         0.1     0.3    0.1    0.4    0.1    0.2    0.0    0.0    0.1    0.0    0.1    0.2
DOLLAR_RESERVE_CRISIS       0.0     0.7    0.0    0.5    0.0    0.3    0.1    0.1    0.2    0.0    0.1    0.0
AI_DISRUPTION_SEVERE        0.0     0.3    0.0    0.3    0.0    0.2    0.0    0.0    0.2    0.0    0.0    0.85
```

#### Interpreting the Loading Matrix

Reading across a row shows what drives an event:
- **EGYPT_STATE_FAILURE** loads on F_MENA (0.80), F_FOOD (0.5), and F_CLIM (0.4) — regional instability, food stress, and climate are the drivers

Reading down a column shows what a factor affects:
- **F_FOOD** affects SAHEL_CATASTROPHE (0.6), EGYPT_STATE_FAILURE (0.5), AMAZON_TIPPING (0.4), etc. — food system stress propagates widely

The implied correlation between two events is the sum of products of their loadings:
```
corr(EGYPT_STATE_FAILURE, SAHEL_CATASTROPHE) = 
    (0.4×0.6) + (0.2×0.1) + (0.1×0.2) + ... + (0.80×0.3) + (0.2×0.85) + ...
  = 0.24 + 0.02 + 0.02 + ... + 0.24 + 0.17 + ...
  ≈ 0.45
```

This moderate-high correlation makes sense: both events are driven by climate stress, food system stress, and partially share regional instability factors.

### 6.5 Idiosyncratic Variance

Each event also has idiosyncratic variance (εᵢ) representing event-specific randomness not captured by factors. The total variance is:

```
var(Zᵢ) = Σₖ λᵢₖ² + var(εᵢ) = 1  (standardized)
```

We set idiosyncratic variance as:
```
var(εᵢ) = 1 - Σₖ λᵢₖ²
```

This ensures:
- Events with high factor loadings are mostly driven by systematic factors
- Events with low factor loadings are mostly idiosyncratic
- All events have unit variance (required for copula)

**Constraint**: The sum of squared loadings must be ≤ 1 for each event. If loadings sum to more, they must be rescaled.

### 6.6 Deriving the Correlation Matrix

Given the factor loading matrix Λ (n events × k factors), the correlation matrix is:

```
Σ = ΛΛ' + Ψ
```

Where:
- Λ is the n × k loading matrix
- Ψ is a diagonal matrix of idiosyncratic variances

This matrix is guaranteed to be positive semi-definite (valid for simulation) as long as the loading constraints are satisfied.

### 6.7 Factor Model Benefits

1. **Fewer parameters**: 75 events × 12 factors = 900 loadings vs. 2,775 correlations

2. **Guaranteed validity**: Factor structure produces valid correlation matrix by construction

3. **Interpretability**: Can ask "what factors drive this event?" and "what events does this factor affect?"

4. **Easier updating**: To add a new event, specify its 12 loadings rather than 74 new correlations

5. **Structural insight**: Factor loadings reveal the underlying structure of risk clustering

6. **Scenario analysis**: Can ask "what if F_CLIM realizes high?" and trace through affected events

### 6.8 Limitations of the Factor Model

1. **Correlation is still symmetric**: Loadings don't capture that drought causes food prices (not vice versa). Causal direction is documented but not modeled.

2. **Static structure**: Loadings don't change over time. If climate stress intensifies, we don't model that F_CLIM becomes more influential.

3. **Linear relationships**: Correlations are linear. Threshold effects (moderate drought = no instability, severe drought = high instability) aren't captured.

4. **Factor definitions are judgment**: The choice of 12 factors and their definitions is analyst judgment, not derived from data.

These limitations are accepted for the current model scope. Addressing them requires the transmission mechanism modeling and state variable dynamics planned for future extensions.

---

## 7. Outcome Variables

### 7.1 Primary Outcome Variables

The simulation tracks these outcome variables across runs:

#### Economic Outcomes

| Variable | Definition | Units |
|----------|------------|-------|
| Global GDP deviation | Cumulative % deviation from baseline trajectory | % |
| US GDP deviation | US-specific deviation | % |
| Developed world GDP deviation | OECD aggregate | % |
| Emerging market GDP deviation | Non-OECD aggregate | % |

#### Financial System Outcomes

| Variable | Definition | Units |
|----------|------------|-------|
| Dollar reserve share | USD % of global reserves | % |
| Inflation trajectory (US) | Cumulative deviation from 2% target | percentage points |
| US Treasury yield premium | Additional yield required due to instability | basis points |
| Gold price trajectory | % change from baseline | % |

#### Humanitarian Outcomes

| Variable | Definition | Units |
|----------|------------|-------|
| Excess mortality | Deaths above baseline demographic projection | millions |
| Mass displacement | Population displaced from home regions | millions |
| Population in crisis | Population in regions experiencing collapse | millions |

#### Geopolitical Outcomes

| Variable | Definition | Units |
|----------|------------|-------|
| State failures | Count of states meeting failure criteria | count |
| Major conflicts | Count of interstate or major civil conflicts | count |
| Climate catastrophe regions | Regions experiencing severe climate impact | count |

### 7.2 Impact Vectors

Each event in the catalog specifies an **impact vector** describing its effect on outcome variables:

```
Event: AMOC Significant Weakening

Impact Vector:
  global_gdp_impact: -0.02 to -0.05 (2-5% GDP reduction)
  us_gdp_impact: -0.01 to -0.02
  europe_gdp_impact: -0.08 to -0.15
  inflation_impact: +0.01 to +0.03 (via food prices)
  displacement: 5-20 million (European agricultural zones)
  excess_mortality: 0.5-2 million (cold, food disruption)
  duration: 20+ years (effectively permanent)
```

Impact vectors are specified as ranges to capture uncertainty. Simulation draws from these ranges.

### 7.3 Impact Aggregation

When multiple events occur:

1. **Additive impacts**: Most economic effects sum (GDP hits accumulate)
2. **Compounding impacts**: Some combinations are worse than sum of parts (e.g., financial crisis during pandemic)
3. **Offsetting impacts**: Some combinations partially cancel (rare)

The model uses additive aggregation as default, with specified multipliers for known compound scenarios:

```
Compound Scenario: Financial Crisis + Pandemic
  Multiplier: 1.3x (compounding effect)
  
Compound Scenario: Climate Disaster + State Failure
  Multiplier: 1.5x (capacity to respond degraded)
```

### 7.4 Reporting Outputs

Simulation produces:

1. **Outcome distributions**: Percentile distributions for each outcome variable (5th, 25th, 50th, 75th, 95th)

2. **Scenario frequency**: How often do various defined scenarios occur?
   - "Severe crisis" (>20% GDP loss)
   - "Dollar displacement" (<40% reserve share)
   - "Humanitarian catastrophe" (>50M displaced)

3. **Conditional distributions**: Outcomes given specific events occurred
   - "Distribution of outcomes given AMOC collapse"
   - "Distribution of outcomes given Taiwan conflict"

4. **Contribution analysis**: Which events contribute most to tail outcomes?

---

## 8. Simulation Mechanics

### 8.1 Time Structure

- **Time step**: Annual
- **Horizon**: 50 years (2025-2075), with primary focus on 2025-2050
- **Iterations**: Minimum 10,000 runs for stable percentile estimates; 50,000+ for tail analysis

### 8.2 Sampling Procedure

For each simulation run:

```
FOR each year t in [2025, 2026, ..., 2075]:
    
    1. GENERATE factor realizations
       - Draw k independent standard normal values: F = [F₁, F₂, ..., Fₖ]
       - These represent the "state of the world" on each risk dimension
    
    2. COMPUTE event propensities
       - For each event i: Zᵢ = Σⱼ λᵢⱼFⱼ + εᵢ
       - Where εᵢ ~ N(0, σᵢ²) is idiosyncratic noise
       - σᵢ² = 1 - Σⱼ λᵢⱼ² (ensures var(Zᵢ) = 1)
    
    3. TRANSFORM to uniform draws
       - Uᵢ = Φ(Zᵢ) where Φ is standard normal CDF
       - U values are correlated uniforms on [0,1]
    
    4. DETERMINE which events occur
       - Event i occurs if Uᵢ < probabilityᵢ
       - Record occurred events for year t
    
    5. SAMPLE impact magnitudes
       - For each occurred event, draw impact from specified distribution
       - Apply compound multipliers if multiple related events occur
    
    6. ACCUMULATE impacts
       - Add year t impacts to running totals for each outcome variable
    
    7. RECORD year t state
       - Event occurrences
       - Factor realizations (for analysis)
       - Cumulative impacts
       - Outcome variable values

END FOR

STORE simulation run results
```

### 8.3 Factor Copula Implementation

The factor model induces correlation through shared factor exposure. Implementation:

```python
# Pseudocode for one year's sampling

# 1. Draw factor realizations (k independent standard normals)
F = np.random.normal(0, 1, size=k)  # e.g., k=12 factors

# 2. Compute systematic component for each event
# Lambda is n×k matrix of factor loadings
systematic = Lambda @ F  # n×1 vector

# 3. Compute idiosyncratic component
# idio_std[i] = sqrt(1 - sum(Lambda[i,:]²))
idiosyncratic = np.random.normal(0, 1, size=n) * idio_std

# 4. Total propensity
Z = systematic + idiosyncratic  # n×1 vector, each element ~ N(0,1)

# 5. Transform to uniform
U = scipy.stats.norm.cdf(Z)  # n×1 vector, each element ~ Uniform(0,1)

# 6. Determine occurrences
occurred = U < probabilities  # boolean array
```

This is computationally efficient: O(n×k) per time step rather than O(n²) for Cholesky-based sampling.

### 8.4 Handling Event Types

#### One-Time Events (Irreversible)

Some events can only occur once (e.g., AMOC collapse, Amazon tipping point). Once triggered:
- Remove from sampling pool for remaining years
- Impact persists according to duration specification

```python
if event.reversible == False and event in occurred_events:
    # Already occurred in previous year, skip sampling
    continue
```

#### Recurring Events

Most events can recur (e.g., financial crisis, drought). Each year is an independent draw given the factor realization.

#### Persistent Events

Some events, once triggered, persist for multiple years (e.g., civil war, state failure). Implementation:
- Event has `duration_distribution` (e.g., Geometric with mean 5 years)
- When triggered, draw duration
- Event remains "active" for duration, suppressing new occurrence but maintaining impact

### 8.5 Impact Sampling

For each occurred event, sample impact magnitude from specified distribution:

```python
for event in occurred_events:
    for outcome_var in outcome_variables:
        impact_spec = event.impacts[outcome_var]
        
        # Draw from distribution (typically normal or log-normal)
        if impact_spec.distribution == 'normal':
            impact = np.random.normal(impact_spec.mean, impact_spec.std)
        elif impact_spec.distribution == 'lognormal':
            impact = np.random.lognormal(impact_spec.log_mean, impact_spec.log_std)
        
        # Accumulate
        cumulative_impacts[outcome_var] += impact
```

### 8.6 Compound Event Handling

When multiple related events occur in the same year, impacts may compound non-linearly:

```python
# Check for compound scenarios
if 'FINANCIAL_CRISIS' in occurred and 'PANDEMIC' in occurred:
    # Apply compound multiplier to GDP impact
    cumulative_impacts['global_gdp'] *= COMPOUND_MULTIPLIERS[('FINANCIAL_CRISIS', 'PANDEMIC')]
```

Compound multipliers are specified in a separate configuration for known dangerous combinations.

### 8.7 Handling Rare Events

For very low probability events (p < 0.01/year):

- **Standard simulation**: May produce few occurrences across runs
- **Solution**: Run sufficient iterations (50,000+) to characterize conditional distributions
- **Alternative**: Importance sampling for tail analysis (oversample rare events, reweight)

For p = 0.01/year over 50 years:
- P(occurs at least once) ≈ 40%
- Expected occurrences per run: 0.5
- In 10,000 runs: ~4,000 runs will see the event at least once
- Sufficient for distribution characterization

### 8.8 Stationarity Assumption

The base implementation assumes **stationary probabilities**—the annual probability of each event is constant across the simulation horizon.

This is a simplification. In reality:
- Climate events become more likely over time
- Some political risks may resolve or intensify
- Demographic pressures accumulate

**Workaround for v1.0**: Use probabilities calibrated to mid-horizon (2040-2050) as representative of the full period.

**Future extension**: Time-varying probabilities via state variables (see Section 11).

---

## 9. Implementation Architecture

### 9.1 Technology Stack

**Core implementation**: Python with NumPy and pandas
- NumPy: Random number generation, linear algebra, array operations
- pandas: Data management, result aggregation, analysis
- scipy.stats: Distribution functions, CDF transformations

**Supporting libraries**:
- matplotlib/seaborn: Visualization of distributions
- JSON or YAML: Event catalog and factor loading storage

### 9.2 Module Structure

```
discontinuity_model/
│
├── data/
│   ├── event_catalog.json          # Event definitions, probabilities, impacts
│   ├── factor_definitions.json     # Factor names and descriptions
│   ├── factor_loadings.csv         # n×k matrix of event-factor loadings
│   └── compound_scenarios.json     # Compound effect multipliers
│
├── core/
│   ├── events.py                   # Event class, catalog loading
│   ├── factors.py                  # Factor model, loading matrix, correlation derivation
│   ├── sampler.py                  # Factor copula sampling logic
│   ├── impacts.py                  # Impact calculation, aggregation
│   └── simulation.py               # Main simulation loop
│
├── analysis/
│   ├── distributions.py            # Outcome distribution analysis
│   ├── scenarios.py                # Scenario frequency analysis
│   ├── contribution.py             # Event/factor contribution to outcomes
│   └── sensitivity.py              # Sensitivity analysis
│
├── visualization/
│   ├── distributions.py            # Distribution plots
│   ├── factor_analysis.py          # Factor realization plots
│   └── heatmaps.py                 # Loading matrix, implied correlations
│
└── notebooks/
    ├── exploration.ipynb           # Interactive analysis
    └── reporting.ipynb             # Summary report generation
```

### 9.3 Data Structures

#### Event Catalog (JSON)

```json
{
  "events": [
    {
      "id": "AMOC_COLLAPSE",
      "name": "AMOC Significant Weakening",
      "scale": "global",
      "domain": "environmental",
      "probability": {
        "annual": 0.015,
        "low": 0.008,
        "high": 0.025,
        "confidence": "low"
      },
      "impacts": {
        "global_gdp": {"mean": -0.03, "std": 0.01, "distribution": "normal"},
        "europe_gdp": {"mean": -0.12, "std": 0.03, "distribution": "normal"},
        "displacement_millions": {"mean": 10, "std": 5, "distribution": "normal"},
        "excess_mortality_millions": {"mean": 1, "std": 0.5, "distribution": "normal"}
      },
      "duration_years": 999,
      "reversible": false,
      "basis": {
        "method": "Expert elicitation synthesis",
        "sources": ["IPCC AR6", "Ditlevsen & Ditlevsen 2023"],
        "key_uncertainties": "Threshold uncertainty, model disagreement"
      },
      "notes": "Effectively permanent once triggered"
    }
  ]
}
```

#### Factor Definitions (JSON)

```json
{
  "factors": [
    {
      "id": "F_CLIM",
      "name": "Climate Stress",
      "description": "Global climate pressure driving extreme weather, tipping points, and downstream instability",
      "type": "global_systemic"
    },
    {
      "id": "F_FIN",
      "name": "Financial Fragility",
      "description": "Global financial system stress driving defaults, banking crises, and contagion",
      "type": "global_systemic"
    },
    {
      "id": "F_MENA",
      "name": "MENA Instability",
      "description": "Middle East/North Africa regional stress",
      "type": "regional"
    }
  ]
}
```

#### Factor Loadings (CSV)

```csv
event_id,F_CLIM,F_FIN,F_HLTH,F_GPT,F_FOOD,F_EUR,F_MENA,F_SAS,F_EAS,F_SSA,F_LAM,F_TECH
AMOC_COLLAPSE,0.85,0.00,0.00,0.00,0.30,0.40,0.10,0.00,0.00,0.10,0.00,0.00
AMAZON_TIPPING,0.80,0.00,0.00,0.00,0.40,0.00,0.00,0.00,0.00,0.00,0.30,0.00
SEVERE_PANDEMIC,0.10,0.20,0.90,0.10,0.10,0.20,0.20,0.20,0.20,0.30,0.20,0.00
TAIWAN_CONFLICT,0.00,0.30,0.00,0.85,0.10,0.10,0.00,0.10,0.80,0.00,0.00,0.20
```

#### Derived Correlation Matrix

Not stored directly; computed from factor loadings:

```python
def compute_correlation_matrix(loadings: np.ndarray) -> np.ndarray:
    """
    Compute implied correlation matrix from factor loadings.
    
    Args:
        loadings: n×k matrix of factor loadings
        
    Returns:
        n×n correlation matrix
    """
    # Σ = ΛΛ' + Ψ where Ψ is diagonal idiosyncratic variance
    systematic = loadings @ loadings.T
    
    # Idiosyncratic variance ensures diagonal = 1
    idio_var = 1 - np.diag(systematic)
    idio_var = np.maximum(idio_var, 0.01)  # Floor to avoid numerical issues
    
    correlation = systematic + np.diag(idio_var)
    return correlation
```

### 9.4 Key Classes

```python
@dataclass
class Event:
    id: str
    name: str
    scale: str  # global, regional, national
    domain: str  # environmental, health, political, economic, technological
    annual_probability: float
    probability_low: float
    probability_high: float
    impacts: Dict[str, ImpactSpec]
    duration_years: int
    reversible: bool
    
@dataclass
class ImpactSpec:
    mean: float
    std: float
    distribution: str  # normal, lognormal
    
@dataclass
class FactorModel:
    factor_ids: List[str]
    event_ids: List[str]
    loadings: np.ndarray  # n_events × n_factors
    
    def sample_year(self) -> Dict[str, bool]:
        """Sample one year of event occurrences."""
        ...
    
    def implied_correlation(self, event_i: str, event_j: str) -> float:
        """Compute implied correlation between two events."""
        ...

@dataclass  
class SimulationResult:
    years: np.ndarray
    event_occurrences: Dict[str, np.ndarray]  # event_id -> boolean array by year
    factor_realizations: np.ndarray  # years × factors
    cumulative_impacts: Dict[str, np.ndarray]  # outcome -> value by year
```

### 9.5 Performance Considerations

Target: 10,000 simulations of 50 years each in <30 seconds on standard hardware

Key optimizations:
- Vectorized factor sampling (all events simultaneously)
- Pre-compute idiosyncratic standard deviations
- Batch simulations (run multiple simulations in parallel via matrix operations)
- Efficient storage: only store occurred events (sparse), not full boolean matrix

Estimated computation per simulation:
- 50 years × (12 factor draws + 75 event propensities + 75 CDF evaluations)
- ~5,000 floating point operations per run
- 10,000 runs: ~50 million operations → sub-second with NumPy vectorization

---

## 10. Validation and Sensitivity Analysis

### 10.1 The Validation Challenge

We cannot validate predictions against future outcomes. Available validation approaches:

#### Internal Consistency
- Does the model produce sensible correlation structure?
- Do outcome distributions have reasonable shape (not degenerate)?
- Do extreme scenarios have appropriate rarity?

#### Historical Backtesting (Limited)
- Can the model produce historical-like outcomes when run with historical parameters?
- Note: Overfitting risk is high; past is limited guide to future

#### Expert Review
- Do outcome distributions match expert intuitions?
- Are tail scenarios plausible but not absurd?

#### Cross-Model Comparison
- How do results compare to other forecasting approaches?
- Where do they diverge, and why?

### 10.2 Sensitivity Analysis

Systematic exploration of how results change with assumptions:

#### Probability Sensitivity
- Run with low-bound probabilities vs. high-bound
- Identify which events' probabilities matter most for outcomes

#### Correlation Sensitivity
- Run with correlation matrix scaled (0.5x, 1.5x)
- Run with independence assumption (diagonal correlation matrix)
- Identify how much correlation structure affects tail outcomes

#### Impact Sensitivity
- Run with low-bound impacts vs. high-bound
- Identify which events' impacts matter most

#### Structural Sensitivity
- Run with different event definitions
- Run with different outcome variable specifications

### 10.3 Robustness Criteria

Results are considered robust if:
- Qualitative conclusions hold across sensitivity ranges
- Rank ordering of risks is stable
- Tail risk characterization (severe outcomes possible) is consistent

Results are fragile if:
- Small parameter changes produce large outcome changes
- Conclusions flip under alternative assumptions

Fragile results should be flagged; decisions should not depend on them.

---

## 11. Limitations and Future Extensions

### 11.1 Explicit Limitations of This Model

This discontinuity effects model has deliberate limitations that bound its scope:

#### What the Model Does NOT Capture

| Limitation | Implication | Future Extension |
|------------|-------------|------------------|
| **No baseline trajectories** | Outputs are shock distributions, not world-state predictions | Integrate with separate baseline model |
| **No state variables** | Probabilities are static; no accumulating pressure | Add state variable dynamics (v2.0) |
| **No time-varying probabilities** | Climate risk in 2025 = climate risk in 2070 | State-dependent probability functions |
| **No transmission mechanisms** | Impacts directly estimated, not derived from structure | Transmission channel modeling (Approach B) |
| **No feedback loops** | Outcomes don't affect future probabilities | Dynamic Bayesian network |
| **No causal direction** | Correlation is symmetric; can't do counterfactuals | Causal graph (Approach B) |
| **No asset returns** | Can't directly answer "what happens to my portfolio?" | Financial modeling layer |

#### Correlation Structure Limitations

The factor model captures clustering but not:
- **Asymmetric influence**: Drought affects food prices more than food prices affect drought
- **Threshold effects**: Moderate stress may not trigger instability; severe stress does
- **Contagion dynamics**: How fast does financial crisis spread? Model doesn't represent velocity
- **Recovery dynamics**: How long until correlation structure returns to baseline after a shock?

#### Temporal Limitations

- **Annual time steps**: Can't model intra-year dynamics (Q1 crisis affecting Q4)
- **Static loadings**: Factor structure doesn't evolve over time
- **No persistence modeling**: Events are independent year-to-year (except via explicit duration)

### 11.2 Appropriate Uses

Given these limitations, the model is appropriate for:

✓ Characterizing the **distribution of cumulative shocks** over planning horizons
✓ Testing intuitions about **crisis probability** (e.g., "60% chance of severe scenario")
✓ Identifying which **events and factors** drive tail risk
✓ Quantifying the importance of **correlation/clustering** vs. independence
✓ Informing **defensive allocation** based on tail risk exposure

The model is NOT appropriate for:

✗ Predicting specific future outcomes
✗ Timing when shocks will occur
✗ Detailed scenario narratives
✗ Asset allocation optimization
✗ Causal inference ("what if we prevented X?")

### 11.3 Future Extension Roadmap

#### Version 2.0: State Variable Integration

Add continuous state variables that evolve over time and condition event probabilities:

```
State Variables:
  - cumulative_warming(t): °C above pre-industrial, increasing ~0.03/year
  - dollar_reserve_share(t): % of global reserves, declining ~0.5/year baseline
  - european_stress_index(t): mean-reverting, shocked by events

Probability Conditioning:
  P(severe_drought | t) = base_rate × f(cumulative_warming(t))
  P(EU_fragmentation | t) = base_rate × g(european_stress_index(t))
```

This allows probabilities to increase with accumulating pressure (climate) or in response to shocks (political stress).

#### Version 2.1: Event Persistence and Recovery

Model events with explicit lifecycle:

```
States: latent → triggered → active → recovering → resolved

Transitions:
  - triggered → active: immediate
  - active → recovering: duration drawn from distribution
  - recovering → resolved: recovery time drawn from distribution
  
Effects:
  - Active events suppress re-triggering
  - Recovery affects factor loadings (stressed region remains elevated)
```

#### Version 3.0: Transmission Channel Modeling (Approach B)

Replace direct impact estimation with structural transmission:

```
TAIWAN_CONFLICT
    → SEMICONDUCTOR_SUPPLY (severity: 0-1)
        → US_GDP_IMPACT = f(severity, US_exposure)
        → CHINA_GDP_IMPACT = f(severity, China_exposure)
    → SHIPPING_DISRUPTION (severity: 0-1)
        → TRADE_COST_INCREASE = g(severity)
    → FINANCIAL_CONTAGION (severity: 0-1)
        → MARKET_DECLINE = h(severity, exposure)
```

Benefits:
- Consistent impact estimation across events using same channel
- Differential exposure modeling (countries with different semiconductor dependence)
- Counterfactual analysis ("if shipping routes remained open...")

#### Version 3.1: Causal Graph Integration

Convert factor correlations to directed causal structure:

```
For high correlations, determine:
  - Causal direction (drought → food prices, not reverse)
  - Mediated pathways (drought → food → instability)
  - Common causes vs. direct causation

Implement:
  - Directed acyclic graph per time slice
  - Conditional probability tables
  - Forward sampling through DAG
```

Benefits:
- Causal direction captured
- Counterfactual queries supported
- Interventional analysis possible

#### Version 4.0: Baseline Integration

Combine discontinuity effects with baseline trajectories:

```
World_State(t) = Baseline_Trajectory(t) + Cumulative_Shocks(t)

Where:
  - Baseline_Trajectory: Deterministic or stochastic trend
  - Cumulative_Shocks: Output of discontinuity model
  
Interaction:
  - Shocks can bend baseline (permanent level shift)
  - Baseline affects shock probabilities (via state variables)
```

This produces actual world-state distributions, not just shock distributions.

### 11.4 Integration with Broader Simulation Architecture

This discontinuity effects model is designed to be one module in a larger architecture:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    INTEGRATED SCENARIO SIMULATION                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ BASELINE MODULE                                                  │   │
│  │ - Demographic trajectories (from UN projections)                 │   │
│  │ - Climate trajectory (from IPCC scenarios)                       │   │
│  │ - Economic trend growth (from IMF/WB projections)                │   │
│  │ - Technology/productivity trends                                 │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ STATE VARIABLES MODULE (Future)                                  │   │
│  │ - Evolving risk indicators                                       │   │
│  │ - Accumulated pressures (climate, demographic, fiscal)           │   │
│  │ - Recovery/stress trajectories                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ DISCONTINUITY EFFECTS MODULE (This Document)                     │   │
│  │ - Event catalog with probabilities                               │   │
│  │ - Factor model for correlation                                   │   │
│  │ - Shock sampling and impact accumulation                         │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ INTEGRATION MODULE (Future)                                      │   │
│  │ - Combine baseline + shocks → world-state                        │   │
│  │ - Feedback from shocks to state variables                        │   │
│  │ - Outcome variable computation                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                      │
│                                  ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ APPLICATION MODULES (Future)                                     │   │
│  │ - Financial planning (asset returns, portfolio analysis)         │   │
│  │ - Migration modeling                                             │   │
│  │ - Regional deep-dives                                            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

The discontinuity effects model provides the **shock distribution** component. Other modules (to be specified separately) handle baseline trajectories, state variable dynamics, and application-specific analysis.

---

## 12. Event Catalog Template

### 12.1 Catalog Structure

The event catalog is maintained as a structured document (JSON or YAML) with the following schema for each event:

```yaml
event:
  # IDENTIFICATION
  id: string                    # Unique identifier (e.g., "AMOC_COLLAPSE")
  name: string                  # Human-readable name
  description: string           # Brief description of what this event represents
  
  # CLASSIFICATION
  scale: enum                   # global | regional | national
  region: string                # If regional/national, which region/country
  domain: enum                  # environmental | health | political | economic | technological
  onset_speed: enum             # sudden | rapid | gradual
  reversibility: enum           # reversible | partial | irreversible
  
  # PROBABILITY
  probability:
    annual: float               # Point estimate of annual probability
    low: float                  # Low bound (10th percentile of uncertainty)
    high: float                 # High bound (90th percentile of uncertainty)
    confidence: enum            # low | medium | high
  
  # PROBABILITY ESTIMATION BASIS
  basis:
    method: string              # How probability was estimated
    historical_reference: string # Historical analogs if any
    expert_sources: list        # Published estimates or expert opinion
    key_uncertainties: string   # What could make this much higher/lower
  
  # FACTOR LOADINGS
  factor_loadings:
    F_CLIM: float               # Climate stress factor (0.0 - 0.9)
    F_FIN: float                # Financial fragility factor
    F_HLTH: float               # Health/pandemic factor
    F_GPT: float                # Great power tension factor
    F_FOOD: float               # Food system stress factor
    F_EUR: float                # European stress factor
    F_MENA: float               # MENA instability factor
    F_SAS: float                # South Asian stress factor
    F_EAS: float                # East Asian tension factor
    F_SSA: float                # Sub-Saharan Africa crisis factor
    F_LAM: float                # Latin American stress factor
    F_TECH: float               # Technology disruption factor
  
  loading_rationale: string     # Brief explanation of why these loadings
  
  # IMPACTS
  impacts:
    global_gdp:                 # Impact on global GDP (% deviation)
      mean: float
      std: float
      distribution: string      # normal | lognormal
    regional_gdp:               # Map of region -> impact
      region_name:
        mean: float
        std: float
    inflation:                  # Impact on inflation (percentage points)
      mean: float
      std: float
    displacement:               # Millions of people displaced
      mean: float
      std: float
    excess_mortality:           # Millions of excess deaths
      mean: float
      std: float
    dollar_reserve_share:       # Change in dollar share (percentage points)
      mean: float
      std: float
    # Additional impact dimensions as relevant
  
  impact_duration: integer      # Years over which impact persists (999 = permanent)
  
  impact_rationale: string      # Brief explanation of impact estimates
  
  # TRANSMISSION NOTES (Documentation for future Approach B)
  transmission_channels:        # How does this event affect outcomes?
    - channel: string           # e.g., "semiconductor_supply", "food_prices", "migration"
      description: string       # How this channel operates
      affected_regions: list    # Which regions are exposed via this channel
  
  # CAUSAL NOTES (Documentation for future Approach B)
  causal_relationships:
    causes:                     # Events this event tends to cause
      - event_id: string
        mechanism: string
    caused_by:                  # Events that tend to cause this event
      - event_id: string
        mechanism: string
  
  # METADATA
  created: date
  last_updated: date
  notes: string                 # Additional context, caveats, considerations
```

### 12.2 Example Entry

```yaml
event:
  id: EGYPT_STATE_FAILURE
  name: Egyptian State Failure
  description: >
    Collapse of effective Egyptian state authority, characterized by loss of 
    territorial control, inability to provide basic services, potential military 
    fragmentation, and mass displacement. Triggered by compound water, food, 
    and economic crises overwhelming institutional capacity.
  
  scale: national
  region: Egypt
  domain: political
  onset_speed: rapid
  reversibility: partial
  
  probability:
    annual: 0.025
    low: 0.015
    high: 0.045
    confidence: medium
  
  basis:
    method: >
      Historical base rate of state failure in similar risk profile countries,
      adjusted for specific Egyptian vulnerabilities (water dependency, food
      import dependency, demographic pressure, fiscal constraints).
    historical_reference: >
      Arab Spring instability (survived), historical Egyptian state resilience,
      but noting Syrian collapse as potential analog under compound stress.
    expert_sources:
      - "Fund for Peace Fragile States Index"
      - "MENA regional stability assessments"
    key_uncertainties: >
      GERD filling and Nile flow impacts; global food price trajectory;
      regime succession dynamics; external support (Gulf states, IMF).
  
  factor_loadings:
    F_CLIM: 0.35    # Climate affects Nile flows, agricultural stress
    F_FIN: 0.25     # Fiscal crisis, currency pressure
    F_HLTH: 0.10    # Healthcare system stress
    F_GPT: 0.10     # Geopolitical positioning, great power support
    F_FOOD: 0.50    # Heavy food import dependency
    F_EUR: 0.20     # European interest in stability, migration
    F_MENA: 0.80    # Core regional event
    F_SAS: 0.00     # No direct link
    F_EAS: 0.00     # No direct link
    F_SSA: 0.15     # Sudanese instability spillover
    F_LAM: 0.00     # No direct link
    F_TECH: 0.00    # Not primarily technology-driven
  
  loading_rationale: >
    Dominant loading on F_MENA as a core regional event. High F_FOOD loading
    reflects 50%+ wheat import dependency. Moderate F_CLIM via Nile dependency.
    F_FIN reflects fiscal fragility and IMF dependency.
  
  impacts:
    global_gdp:
      mean: -0.003
      std: 0.001
      distribution: normal
    regional_gdp:
      MENA:
        mean: -0.05
        std: 0.02
      Europe:
        mean: -0.01
        std: 0.005
    inflation:
      mean: 0.005
      std: 0.002
      distribution: normal
    displacement:
      mean: 8.0
      std: 4.0
      distribution: lognormal
    excess_mortality:
      mean: 0.3
      std: 0.2
      distribution: lognormal
    dollar_reserve_share:
      mean: 0.0
      std: 0.0
      distribution: normal
  
  impact_duration: 15
  
  impact_rationale: >
    GDP impacts modest at global level but significant for MENA. Displacement
    estimate based on Syrian precedent scaled for Egyptian population, with
    geographic constraints on exit routes. Mortality estimate conservative
    assuming gradual collapse rather than acute conflict.
  
  transmission_channels:
    - channel: migration
      description: >
        Mass displacement toward Europe via Mediterranean; toward Gulf states
        via established labor migration networks
      affected_regions: [Europe, Gulf_States, North_Africa]
    - channel: suez_canal
      description: >
        Potential disruption of Suez Canal traffic affecting global shipping
      affected_regions: [Global]
    - channel: regional_contagion
      description: >
        Instability spillover to Libya, Sudan, Gaza; demonstration effects
      affected_regions: [MENA]
  
  causal_relationships:
    causes:
      - event_id: SUEZ_DISRUPTION
        mechanism: "State failure likely disrupts canal operations"
      - event_id: MENA_REGIONAL_WAR
        mechanism: "Power vacuum invites intervention"
    caused_by:
      - event_id: NILE_WATER_CRISIS
        mechanism: "Water scarcity is primary structural driver"
      - event_id: GLOBAL_FOOD_SPIKE
        mechanism: "Food import dependency creates acute vulnerability"
      - event_id: GULF_STATES_CRISIS
        mechanism: "Loss of external financial support"
  
  created: 2025-12-15
  last_updated: 2025-12-15
  notes: >
    Egypt's size (105M+), location (Suez Canal), and historical role as regional
    stabilizer make its failure a Tier 1 concern. Compound scenario of water
    crisis + food crisis + economic crisis is the primary pathway. Sum of squared
    loadings = 1.02, within acceptable range (rescale if implementing strictly).
```

### 12.3 Catalog Organization

The full catalog will be organized into sections:

```
EVENT CATALOG
│
├── 1. Global Events
│   ├── 1.1 Environmental (AMOC, Amazon, permafrost, etc.)
│   ├── 1.2 Health (pandemics, antibiotic resistance)
│   ├── 1.3 Economic/Financial (global crisis, reserve currency shift)
│   └── 1.4 Technological (AI disruption, cyber events)
│
├── 2. Regional Events
│   ├── 2.1 Europe (EU fragmentation, migration crisis, fiscal crisis)
│   ├── 2.2 East Asia (Taiwan, Korea, China instability)
│   ├── 2.3 South Asia (India-Pakistan, Bangladesh, water conflict)
│   ├── 2.4 Middle East & North Africa (state failures, regional war)
│   ├── 2.5 Sub-Saharan Africa (Sahel, Nigeria, South Africa)
│   ├── 2.6 Americas (US political, Central America, Venezuela)
│   └── 2.7 Central Asia & Russia (water crisis, Russian instability)
│
├── 3. National Events (Selected High-Impact)
│   ├── 3.1 United States (political crisis variants)
│   ├── 3.2 China (economic, political, demographic crisis)
│   ├── 3.3 Key Regional Powers (Turkey, Iran, Saudi Arabia, etc.)
│   └── 3.4 Fragile States with Global Implications (Pakistan, Egypt, Nigeria)
│
└── Appendices
    ├── A. Factor Definitions and Loading Guidelines
    ├── B. Compound Scenario Multipliers
    ├── C. Probability Estimation References
    ├── D. Impact Estimation References
    └── E. Implied Correlation Matrix (computed from loadings)
```

### 12.4 Loading Constraint Validation

Before using the catalog, validate that factor loadings satisfy constraints:

```python
def validate_loadings(event: dict) -> bool:
    """
    Validate that event factor loadings satisfy constraints.
    
    Constraints:
    1. All loadings in [0, 0.95]
    2. Sum of squared loadings <= 1.0 (ensures positive idiosyncratic variance)
    """
    loadings = event['factor_loadings']
    
    # Check individual loading bounds
    for factor, loading in loadings.items():
        if not (0 <= loading <= 0.95):
            print(f"Warning: {event['id']} has out-of-bounds loading {factor}={loading}")
            return False
    
    # Check sum of squared loadings
    sum_sq = sum(l**2 for l in loadings.values())
    if sum_sq > 1.0:
        print(f"Warning: {event['id']} has sum of squared loadings = {sum_sq:.2f} > 1.0")
        print(f"  Rescale loadings by factor of {(0.95/sum_sq)**0.5:.3f}")
        return False
    
    return True
```

---

## Document Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial methodology specification |
| 1.1 | December 2025 | Reframed as Discontinuity Effects Model; adopted factor model for correlations; added explicit limitations section |
| 1.1 + banner | July 2026 | Partial-supersession banner added: §§8–9 (independent factors, static sampler, §8.6 compound multipliers) replaced by [[methodology/reference/simulator-architecture]] ADRs; body text left as historical record |

---

## Next Steps

1. **Event catalog population**: Systematic entry of events following template
2. **Factor loading estimation**: Assign loadings based on causal reasoning
3. **Implementation**: Python/NumPy/pandas codebase
4. **Validation**: Sensitivity analysis, implied correlation review
5. **Application**: Generate shock distributions for planning purposes

---

*This methodology document establishes the framework for the discontinuity effects model. The companion Event Catalog document will contain the detailed event entries that populate the model. This module is designed to integrate with a broader scenario simulation architecture to be specified separately.*