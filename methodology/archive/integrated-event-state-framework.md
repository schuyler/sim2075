---
title: integrated-event-state-framework
type: note
permalink: methodology/integrated-event-state-framework
tags:
- methodology
- framework
- events
- state-coupling
- impact-vectors
- causal-types
- v2-architecture
---

# Integrated Event-State Framework

## A Unified Architecture for Discontinuity Modeling

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Framework specification (supersedes prior asymmetry proposals)

**Supersedes:**
- `asymmetric-modeling-proposal.md` (deprecated)
- `discontinuity-causal-typology.md` (absorbed)
- Portions of `positive-negative-asymmetry-analysis.md` (reframed)

---

## 1. Executive Summary

This document specifies a unified framework for modeling discontinuity events within the geopolitical simulation. It resolves several conceptual problems in prior specifications:

**Problem 1: The Positive/Negative Dichotomy**
Prior analysis framed events as intrinsically "positive" or "negative," then struggled to model asymmetries between them. This framing is flawed—valence is not an event property but an evaluation applied to impact vectors under a welfare function.

**Problem 2: Factor Model Decoupling**
The factor correlation model captures simultaneous event clustering but not the sequential dynamics where events change state, which changes future event probabilities.

**Problem 3: Type 4 Misclassification**
S-curve dynamics (technology diffusion, adoption curves) were treated as discrete events with annual probabilities. This is a category error—they are baseline trajectory uncertainty, not discontinuities.

**Resolution:**

1. **Events are state transitions**, characterized by impact vectors across multiple dimensions and actors, not by valence.

2. **Causal type determines modeling approach**: Type 1 (stochastic) and Type 3 (contingent) use factor-correlated sampling; Type 2 (threshold) uses state-conditioned probability; Type 4 (S-curve) moves to baseline trajectory modeling.

3. **Factors drive pressure dynamics**, which drive state variables, which condition event probabilities. This creates proper feedback loops.

4. **Durability is impact-type-specific**: deaths are permanent, agreements require maintenance, technology adoption is durable post-saturation. This replaces the false "positive events are fragile" generalization.

---

## 2. Foundational Reframing

### 2.1 Why "Positive" and "Negative" Are Not Event Properties

Consider "Major International Climate Agreement":

| Dimension | Impact | Apparent Valence |
|-----------|--------|------------------|
| Global emissions trajectory | Reduced | Positive |
| Climate damages avoided | Substantial | Positive |
| Fossil exporter revenues | Collapsed | Negative (for them) |
| Stranded asset losses | $Trillions | Negative (for holders) |
| Energy transition costs | High | Negative (short-term) |
| Energy security (renewables) | Improved | Positive (long-term) |
| Great power relations | Ambiguous | Depends on burden-sharing |
| Developing country growth | Ambiguous | Depends on transfer mechanisms |

This event cannot be assigned a valence. It has a complex impact vector with winners, losers, tradeoffs, and deep uncertainty. Whether it is "good" depends on whose welfare function you apply, what discount rate, and what counterfactual.

The same analysis applies to supposedly "obvious" cases:

**AMOC Collapse** (seemingly negative):
- Northwestern Europe: severe cooling, agricultural disruption
- Southern Europe: possibly less severe than greenhouse warming alone  
- Global climate politics: might catalyze action (or fatalism)
- US/China relative position: Europe weakened

**AI Productivity Breakthrough** (seemingly positive):
- Aggregate GDP: increases
- Labor displacement: millions of jobs
- Inequality: widens (capital vs. labor)
- Geopolitical: advantage to leaders
- Long-term risk: depends on alignment

**Conclusion**: Events have impact vectors. Summary valence is a post-hoc evaluation, not an intrinsic property. The model should specify impact vectors; users apply welfare functions.

### 2.2 Events as State Transitions

An event is a **discrete change in the trajectory of one or more state variables**.

This framing connects to the state specification document:
- State variables track the condition of entities over time
- Variables have baseline dynamics (drift, mean-reversion, regime-dependent)
- Events are discontinuities—departures from baseline dynamics

**Examples:**

| Event | State Transition |
|-------|------------------|
| AMOC Collapse | `amoc_strength` crosses from "weakened" to "collapsed" regime |
| Pakistan State Failure | `pakistan.regime_stability` crosses below failure threshold; `pakistan.internal_conflict_intensity` shifts to civil war regime |
| Climate Agreement | `global_emissions_trajectory` shifts pathway; triggers cascade to `fossil_exporter.fiscal_stress` |
| Taiwan Conflict | `taiwan.external_conflict_involvement` shifts to war; `semiconductor_supply` drops discontinuously |

The event catalog specifies:
1. What state transition defines the event
2. What conditions make the transition more/less likely
3. What impact vector results from the transition
4. How durable each impact component is

### 2.3 Impact Vectors: Multi-dimensional, Actor-specific, Time-varying

An impact vector specifies effects across:

**Dimensions**: GDP, mortality, displacement, institutional quality, emissions, stability indices, etc.

**Actors**: Global aggregates, specific countries, regional groups, population subgroups

**Time profile**: Immediate shock, delayed onset, duration, recovery trajectory

**Structure:**

```yaml
impact_vector:
  global:
    variable_1:
      immediate: X
      delayed: Y (onset after N years)
      duration: permanent | N years | maintenance_required
      uncertainty: distribution specification
    variable_2: ...
  
  by_country:
    country_or_group:
      variable_1: ...
      variable_2: ...
  
  conditional:
    - condition: "if concurrent_event_X"
      modifier: multiplier or additive adjustment
```

**Example: Major Climate Agreement**

```yaml
impact_vector:
  global:
    emissions_trajectory:
      immediate: -5% vs. baseline
      delayed: -20% by 2040 (if maintained)
      duration: maintenance_required
      maintenance:
        annual_defection_probability: 0.08
        defection_cascade_risk: 0.3  # P(others defect | one defects)
      uncertainty: normal(mean=-20%, std=8%)
    
    energy_investment_reallocation:
      immediate: +$500B/year to renewables
      duration: 10 years (front-loaded)
      uncertainty: lognormal
  
  by_country:
    fossil_exporters:  # Saudi, Russia, Iran, Nigeria, etc.
      fiscal_stress:
        immediate: +15 points
        delayed: +30 points by 2035
        duration: permanent (structural)
      regime_stability:
        delayed: -10 to -25 points (5-10 year lag)
        uncertainty: high (depends on adaptation)
    
    high_emitters:  # US, China, EU, India
      gdp_growth:
        immediate: -0.3% (transition costs)
        delayed: +0.2% (avoided damages, new industries)
        crossover: ~2035
        uncertainty: very high
    
    climate_vulnerable:  # Bangladesh, Sahel, small islands
      climate_damages_avoided:
        delayed: significant (10+ year lag)
        duration: permanent
        uncertainty: depends on warming already locked in
  
  conditional:
    - condition: "if burden_sharing_contested"
      impact: us_china_tension +10, eu_cohesion -5
    - condition: "if technology_transfer_successful"  
      impact: developing_country_growth +0.5%
```

This structure captures the complexity that "positive/negative" labeling obscures.

---

## 3. Causal Typology (Revised)

Events are classified by their generative mechanism. Causal type determines the appropriate modeling approach.

### 3.1 Type 1: Stochastic Arrivals

**Definition**: Events with relatively stable base rates that occur without clear proximate cause. The timing is unpredictable, but the rate is estimable from history.

**Characteristics**:
- Approximately Poisson-distributed
- Limited leading indicators
- Base rate is primary probability input
- Correlation with other events through shared vulnerability, not shared pressure

**Examples**:
- Novel pandemic emergence (~3 per century historically)
- Major earthquakes on known faults
- Certain financial crises (idiosyncratic triggers)
- Scientific breakthroughs (specific fields)

**Modeling Approach**:
- Annual probability from historical base rate, adjusted for known condition changes
- Factor correlation captures shared vulnerability (e.g., pandemic + financial crisis both hit fragile states harder)
- No state-conditioning required (probability doesn't accumulate)

**Probability Estimation**: Historical frequency → adjustment for current conditions → annual probability with confidence interval

### 3.2 Type 2: Threshold/Accumulation

**Definition**: Gradual pressure accumulates on state variables until a threshold is crossed. The system appears stable until it suddenly isn't.

**Characteristics**:
- Probability increases as pressure accumulates
- State variables track pressure (observable or latent)
- Threshold may be known, uncertain, or stochastic
- Often exhibits "critical slowing down" as threshold approaches
- Frequently irreversible once triggered

**Examples**:
- AMOC collapse (freshwater input accumulates)
- State failure (legitimacy erodes, fiscal stress accumulates)
- Hyperinflation (deficit monetization accumulates)
- Currency crisis (reserves deplete, current account worsens)
- Amazon tipping point (deforestation + temperature accumulate)

**Modeling Approach**:
- Track pressure variables as part of state
- Event probability conditioned on pressure level: P(event|state)
- Threshold can be deterministic, stochastic, or multi-dimensional surface
- Factor shocks affect pressure variables, not event probability directly

**Probability Estimation**: 
1. Identify pressure variables
2. Estimate current pressure level
3. Estimate threshold (with uncertainty)
4. Probability = f(pressure, threshold, trend)

**Key Insight**: Type 2 events are where state-conditioning matters most. The same "60% chance of state failure" means very different things if pressure is low vs. high.

### 3.3 Type 3: Contingent/Window-Resolution

**Definition**: Events heavily dependent on specific decisions, negotiations, or coordination outcomes. Preconditions create windows; resolution within windows is uncertain.

**Characteristics**:
- High sensitivity to individual decisions and small-N actors
- Two-stage structure: window opens, then resolution
- Preconditions necessary but not sufficient
- Game-theoretic dynamics (negotiation, brinksmanship)
- Path-dependent (sequence of moves matters)

**Examples**:
- Peace agreements (Good Friday, Camp David)
- Political transitions (South Africa, German reunification)
- Deliberate conflicts (invasion decisions, escalation choices)
- Major international agreements (climate, arms control)
- Post-crisis coordination (G20 2008)

**Modeling Approach**:
- Two-stage sampling:
  1. P(window opens) based on preconditions
  2. P(resolution | window open) with multiple possible outcomes
- Preconditions often involve state variables (tension level, leadership alignment)
- Resolution probabilities reflect coordination difficulty
- Different resolutions have different impact vectors

**Structure:**

```yaml
type_3_event:
  window:
    preconditions:
      - us_china_tension < 70
      - leadership_alignment: specific configuration
      - economic_interdependence > threshold
    annual_window_probability: 0.05  # given preconditions met
    
  resolution:
    given_window_opens:
      positive_resolution: 0.25
      negative_resolution: 0.35
      status_quo: 0.40  # window closes without resolution
    
  impact_vectors:
    positive_resolution: [detailed impact vector]
    negative_resolution: [detailed impact vector]
    status_quo: [minimal impact, possibly increased tension]
```

**Probability Estimation**:
- Window probability from structural analysis of conditions
- Resolution probability from historical coordination success rates, adjusted for specifics
- High uncertainty appropriate—these are genuinely hard to forecast

**Key Insight**: The same window can produce very different outcomes. "Taiwan crisis" is a window; resolution could be war, peaceful accommodation, or status quo. These aren't three separate events—they're three resolutions of one contingent situation.

### 3.4 Type 4: S-Curve Dynamics — Not Events

**Definition**: Processes following predictable adoption curves once initiated. Slow start, rapid acceleration, eventual saturation.

**Characteristics**:
- Driven by reinforcing feedback loops (network effects, learning curves)
- Early stages look like noise; late stages look inevitable
- Once underway, trajectory is somewhat predictable
- Key uncertainty is timing of inflection, not direction

**Examples**:
- Technology adoption (internet, mobile, EVs)
- Cost declines (solar, batteries, sequencing)
- Capability growth (AI, if scaling continues)
- Infrastructure deployment (charging networks, renewables capacity)

**Critical Realization**: These are not discontinuities. A 90% cost decline over 15 years following a known learning curve is not a discrete event—it's a baseline trajectory with parameter uncertainty.

**Modeling Approach**: Remove from event catalog. Model as:

1. **Baseline trajectory uncertainty**: Instead of P(solar breakthrough) = 0.03/year, model solar cost trajectory as:
   ```
   cost(t) = cost_2025 × (1 - learning_rate)^(cumulative_deployment(t))
   learning_rate ~ distribution (uncertainty in slope)
   deployment_trajectory ~ distribution (uncertainty in adoption speed)
   ```

2. **Inflection events only**: If there's a genuine discontinuity (e.g., fusion actually achieves net energy gain), model that specific threshold crossing as a Type 2 event. The subsequent deployment would be trajectory uncertainty, not additional events.

3. **Capability thresholds**: For AI, model as Type 2 if there are meaningful thresholds (e.g., "AI capable of autonomous R&D"). Otherwise, model as trajectory uncertainty in `ai_capability_index` growth rate.

**What Moves to Baseline:**
- Solar/wind cost trajectories
- Battery cost and density
- EV adoption curves
- General AI capability growth (absent specific threshold events)
- mRNA platform development
- Most technology diffusion

**What Remains as Events:**
- Fusion breakeven (Type 2 threshold)
- Transformative AI threshold crossing (Type 2 threshold, if definable)
- Deliberate deployment decisions that shift trajectories (Type 3 policy)

### 3.5 Classification Decision Tree

```
Is there a historical base rate with no clear accumulating precursors?
├── YES → Type 1 (Stochastic)
└── NO ↓

Does probability increase as some measurable pressure accumulates?
├── YES → Type 2 (Threshold)
└── NO ↓

Does outcome depend critically on negotiation/coordination among small-N actors?
├── YES → Type 3 (Contingent)
└── NO ↓

Does it follow a predictable adoption/diffusion curve once initiated?
├── YES → Type 4 → MOVE TO BASELINE, not event catalog
└── NO → Reassess classification or hybrid
```

**Hybrid Types:**

Many events combine types:
- **Type 2 + Type 3**: Pressure accumulates (Type 2), creating a window, but resolution depends on agency (Type 3). Example: Cold War end—pressure accumulated, but peaceful resolution required Gorbachev/Reagan decisions.
- **Type 1 + Type 2**: Stochastic trigger initiates threshold process. Example: Pandemic emergence (Type 1) triggers cascade if health systems already stressed (Type 2).

For hybrids, model the dominant mechanism and note the secondary.

---

## 4. State-Event Coupling Architecture

### 4.1 The Integration Problem

The current design has two decoupled systems:

**State Model** (per state-specification.md):
- ~2,600 variables evolving over time
- Baseline dynamics (drift, mean-reversion, regime-dependent)
- Transmission mechanisms

**Event Model** (per monte-carlo-framework.md):
- Discontinuity catalog with annual probabilities  
- Factor correlation for clustering
- Impact vectors as shocks to state

**Gap**: Event probability is static. P(Pakistan failure) = 1.5%/year regardless of whether Pakistan's `regime_stability` is 70 or 30. This misses the core dynamic of Type 2 events.

**Required**: Events and state must couple bidirectionally:
- Event impacts change state variables
- State variables condition event probabilities
- Factor realizations drive pressure dynamics

### 4.2 Factors as Pressure Drivers (Revised Interpretation)

**Current interpretation** (to be revised): Factors are latent variables that simultaneously affect event probabilities. High F_CLIM → higher P(AMOC collapse) AND higher P(Sahel drought) AND higher P(food crisis).

**Revised interpretation**: Factors are shocks to pressure variables, which affect state, which conditions event probability.

```
Factor Realization → Pressure Shock → State Variable Update → Event Probability
```

**Example:**

Current: F_CLIM = +1.5σ → P(AMOC collapse) multiplied by factor loading

Revised: F_CLIM = +1.5σ → 
  - `global_temp_anomaly` shocked upward
  - `amoc_strength` declines faster than baseline
  - P(AMOC collapse) increases because `amoc_strength` closer to threshold

**Advantages of revised interpretation:**
- State variables are observable/interpretable
- Probability conditioning is explicit
- Cascade effects propagate through state
- Factor correlation still produces event clustering (correlated shocks → correlated state movements → clustered threshold crossings)

**Implementation:**

```python
def simulate_year(state, factors, events):
    # 1. Draw factor realizations (correlated)
    factor_realization = sample_correlated_factors()
    
    # 2. Apply factor shocks to pressure variables
    for pressure_var in pressure_variables:
        factor_shock = compute_factor_shock(pressure_var, factor_realization)
        baseline_change = baseline_dynamics(pressure_var, state)
        state[pressure_var] += baseline_change + factor_shock
    
    # 3. Apply other baseline dynamics to non-pressure variables
    state = apply_baseline_dynamics(state)
    
    # 4. Sample Type 1 events (factor-correlated, not state-conditioned)
    for event in type_1_events:
        p = factor_adjusted_probability(event, factor_realization)
        if random() < p:
            state = apply_impacts(event, state)
    
    # 5. Check Type 2 thresholds (state-conditioned)
    for event in type_2_events:
        p = state_conditioned_probability(event, state)
        if random() < p:
            state = apply_impacts(event, state)
    
    # 6. Sample Type 3 events (window + resolution)
    for event in type_3_events:
        if window_conditions_met(event, state):
            if random() < event.window_probability:
                resolution = sample_resolution(event)
                state = apply_impacts(event, resolution, state)
    
    return state
```

### 4.3 State-Conditioned Probability for Type 2

For Type 2 events, probability is a function of relevant state variables:

```
P(event | year t) = f(pressure_variables(t), threshold_estimate, uncertainty)
```

**Functional Forms:**

1. **Logistic (smooth threshold)**:
   ```
   P(event) = 1 / (1 + exp(-k × (pressure - threshold)))
   ```
   Where k controls steepness. Low k = gradual increase; high k = sharp threshold.

2. **Exponential (accelerating)**:
   ```
   P(event) = p_base × exp(λ × (pressure - reference))
   ```
   Probability grows exponentially as pressure exceeds reference level.

3. **Multi-dimensional threshold**:
   ```
   pressure_composite = w1×var1 + w2×var2 + ... + wn×varn
   P(event) = f(pressure_composite, threshold)
   ```
   Multiple variables combine into composite pressure.

**Example: Pakistan State Failure**

```yaml
event: PAKISTAN_STATE_FAILURE
type: 2
pressure_variables:
  - variable: pakistan.regime_stability
    weight: 0.35
    transform: inverse  # lower stability = higher pressure
  - variable: pakistan.water_stress  
    weight: 0.25
    transform: linear
  - variable: pakistan.debt_external
    weight: 0.20
    transform: logistic(center=80, steepness=0.1)
  - variable: pakistan.internal_conflict_intensity
    weight: 0.20
    transform: linear

pressure_function: weighted_sum
threshold:
  estimate: 0.70
  uncertainty: normal(std=0.10)
  
probability_function: logistic
probability_parameters:
  steepness: 8  # fairly sharp threshold

current_assessment:
  pressure_level: 0.55
  distance_to_threshold: 0.15
  baseline_annual_probability: 0.015
  state_conditioned_probability: 0.025  # elevated due to current pressure
```

### 4.4 Window-Resolution Structure for Type 3

Type 3 events have explicit two-stage structure:

**Stage 1: Window**
- Preconditions define when a window can open
- Window probability = P(window opens | preconditions met)
- Windows may have duration (open for N years if not resolved)

**Stage 2: Resolution**
- Multiple possible outcomes, each with probability and impact vector
- Outcomes are mutually exclusive and exhaustive
- Resolution probabilities may depend on state at resolution time

**Implementation:**

```yaml
event: TAIWAN_CRISIS
type: 3

window:
  preconditions:
    - us_china_tension > 70
    - taiwan.alliance_west > 60
    - china.regime_stability < 70 OR china.gdp_growth < 2 for 3 years
  precondition_logic: (tension AND alliance) AND (stability OR growth)
  
  window_probability: 0.08  # annual, given preconditions
  window_duration: 3  # years, if not resolved
  
resolutions:
  - id: military_conflict
    probability: 0.35
    impact_vector:
      taiwan:
        external_conflict_involvement: 4
        gdp_real: -30% to -50%
        pop_total: -2% to -5% (casualties, emigration)
      china:
        external_conflict_involvement: 4
        gdp_real: -10% to -20%
        regime_stability: -20 to +10 (depends on outcome)
      united_states:
        external_conflict_involvement: 3
        gdp_real: -3% to -8%
      global:
        semiconductor_supply: -50% to -70%
        us_china_tension: 95
        
  - id: peaceful_resolution
    probability: 0.20
    impact_vector:
      taiwan:
        alliance_west: -30 (reduced US commitment)
        regime_stability: -15 (political crisis from accommodation)
      global:
        us_china_tension: -20
        semiconductor_supply: stable
        
  - id: status_quo_continuation
    probability: 0.45
    impact_vector:
      global:
        us_china_tension: +5
      # minimal other impacts; window closes without resolution
```

### 4.5 Removing Type 4 from Event Catalog

Events currently classified as Type 4 S-curves should be reclassified:

| Current Event | Reclassification |
|---------------|------------------|
| Solar cost breakthrough | **Baseline**: trajectory uncertainty in `renewable_cost_index` |
| Battery breakthrough | **Baseline**: trajectory uncertainty in `battery_cost_kwh` |
| EV adoption acceleration | **Baseline**: trajectory in transport sector emissions |
| AI productivity gains | **Baseline**: trajectory in `ai_capability_index`, unless specific threshold defined |
| Energy storage breakthrough | **Type 2**: if specific technical threshold (e.g., cost below $50/kWh), otherwise baseline |
| Accelerated decarbonization | **Type 3**: requires policy coordination; model as agreement event |

**Implementation for baseline trajectory uncertainty:**

Instead of:
```yaml
event: SOLAR_BREAKTHROUGH
annual_probability: 0.03
impact: renewable_cost_index -30%
```

Use:
```yaml
# In state specification, not event catalog
variable: renewable_cost_index
dynamics: learning_curve
parameters:
  learning_rate:
    distribution: normal
    mean: 0.20  # 20% cost decline per doubling
    std: 0.05   # uncertainty in learning rate
  deployment_growth:
    distribution: normal
    mean: 0.15  # 15% annual deployment growth
    std: 0.08   # uncertainty in deployment speed
  floor:
    distribution: uniform
    min: 0.10   # minimum 90% cost reduction possible
    max: 0.05   # maximum 95% cost reduction possible
```

This captures the same uncertainty without the fiction of a discrete "breakthrough event."

---

## 5. Impact Vector Specification

### 5.1 Structure of Impact Vectors

Every event specifies an impact vector with the following structure:

```yaml
impact_vector:
  # Global impacts
  global:
    [variable_id]:
      magnitude: value or distribution
      delay: years until onset (0 = immediate)
      duration: years | permanent | maintenance_required
      uncertainty: distribution specification
      
  # Country/region-specific impacts
  by_entity:
    [entity_id or entity_group]:
      [variable_id]:
        magnitude: value or distribution
        # ... same fields as global
        
  # Conditional modifiers
  conditional:
    - condition: [state condition or concurrent event]
      target: [which impact to modify]
      modifier: [multiplier or additive adjustment]
      
  # Cascade triggers
  cascades:
    - target_variable: [state variable affected]
      magnitude: [change to that variable]
      mechanism: [brief description]
```

### 5.2 Durability by Impact Type

Durability is determined by the nature of the impact, not by event "valence."

| Impact Type | Durability Model | Examples |
|-------------|------------------|----------|
| **Mortality** | Permanent | Conflict deaths, pandemic deaths, famine deaths |
| **Physical destruction** | Recovery time + resources | Infrastructure damage, capital stock destruction |
| **Institutional collapse** | Long recovery, requires coordination | State failure, institutional decay |
| **Coordinated agreement** | Maintenance required | Treaties, international agreements, peace deals |
| **Policy regime** | Until reversed | Sanctions, trade arrangements, monetary policy |
| **Technology adoption** | Permanent post-saturation | Infrastructure built, capabilities acquired |
| **Knowledge/capability** | Permanent (unless lost) | Scientific knowledge, technical capability |
| **Resource depletion** | Permanent | Aquifer exhaustion, species extinction |
| **Displacement** | Variable | Some return, some permanent resettlement |

**Maintenance-Required Model:**

For impacts requiring ongoing commitment (agreements, coordination):

```yaml
durability:
  type: maintenance_required
  annual_survival_probability: 0.92  # 8% annual failure rate
  failure_triggers:
    - leadership_change_in: [key parties]
    - stress_exceeds: [threshold on relevant variable]
    - defection_by: [specific actor]
  cascade_on_failure:
    - partial_reversal: 0.6  # 60% of gains lost
    - full_reversal: 0.3     # all gains lost
    - graceful_degradation: 0.1  # slow erosion
```

**Recovery Model:**

For impacts that recover over time:

```yaml
durability:
  type: recoverable
  recovery_half_life: 5  # years
  recovery_depends_on:
    - state_capacity > 50
    - external_support available
    - no_concurrent_crisis
  full_recovery_possible: true | false
  permanent_scarring: 0.2  # 20% of impact permanent
```

### 5.3 Cascade Pathways

Impact vectors should specify how impacts feed forward to state variables that condition other events.

**Example: AMOC Collapse Cascades**

```yaml
event: AMOC_COLLAPSE
cascades:
  - target: europe.agricultural_climate_risk
    magnitude: +40 points
    delay: 2 years
    mechanism: "Temperature drop devastates European agriculture"
    
  - target: europe.regime_stability (aggregate)
    magnitude: -15 points
    delay: 3-5 years
    mechanism: "Economic disruption + migration creates political stress"
    
  - target: sahel.water_stress
    magnitude: -10 points (improvement)
    delay: 5 years
    mechanism: "Changed Atlantic circulation may increase Sahel rainfall"
    uncertainty: high
    
  - target: global.food_stocks_grains
    magnitude: -30%
    delay: 1-2 years
    mechanism: "European production collapse tightens global supply"

# These cascade impacts change state variables that condition other events:
# - Higher europe.agricultural_climate_risk → higher P(European food crisis)
# - Lower europe.regime_stability → higher P(EU fragmentation)
# - Lower global.food_stocks → higher P(food price spike) → higher P(MENA instability)
```

### 5.4 Worked Example: Climate Agreement

```yaml
event: MAJOR_CLIMATE_AGREEMENT
type: 3

window:
  preconditions:
    - us_china_tension < 65
    - global_temp_anomaly > 1.5  # sufficient urgency
    - recent_climate_disaster: true  # salience
  window_probability: 0.06
  
resolutions:
  - id: strong_agreement
    probability: 0.30
    impact_vector:
      global:
        emissions_trajectory:
          magnitude: -25% by 2040
          delay: 0
          duration: maintenance_required
          maintenance:
            survival_probability: 0.90
            failure_mode: gradual_erosion
            
      by_entity:
        fossil_exporters:  # Saudi, Russia, Iran, Nigeria, Kazakhstan
          fiscal_stress:
            magnitude: +20 points
            delay: 3 years
            duration: permanent
          regime_stability:
            magnitude: -10 to -25 points
            delay: 5-10 years
            duration: until_adaptation
            
        developed_economies:
          gdp_growth:
            magnitude: -0.3% (transition) then +0.2% (avoided damages)
            crossover: 2035
            uncertainty: high
            
      cascades:
        - target: fossil_exporters.regime_stability
          mechanism: "Revenue collapse strains petrostate social contracts"
        - target: global.us_china_tension
          magnitude: -10
          mechanism: "Successful cooperation builds trust"
          condition: if burden_sharing_perceived_fair
          
  - id: weak_agreement
    probability: 0.40
    impact_vector:
      global:
        emissions_trajectory:
          magnitude: -10% by 2040
          duration: maintenance_required
          maintenance:
            survival_probability: 0.85
      # Reduced impacts across all categories
      
  - id: no_agreement
    probability: 0.30
    impact_vector:
      global:
        us_china_tension:
          magnitude: +5
          mechanism: "Failed coordination increases rivalry framing"
      # Window closes without deal
```

### 5.5 Worked Example: AI Capability Acceleration

```yaml
event: AI_CAPABILITY_THRESHOLD
type: 2
description: "AI systems achieve autonomous research capability, dramatically accelerating further AI development"

pressure_variables:
  - variable: global.ai_capability_index
    weight: 0.7
    threshold_type: level  # triggers when index exceeds threshold
  - variable: ai_investment_rate
    weight: 0.3
    transform: log  # diminishing returns

threshold:
  estimate: 250  # index level (2025 = 100)
  uncertainty: normal(std=50)
  timing_estimate: 2030-2040
  
probability_function: logistic
current_assessment:
  ai_capability_index: 100
  years_to_threshold_at_trend: 8-15
  
impact_vector:
  global:
    ai_capability_index:
      magnitude: "growth rate +20%/year" 
      duration: until saturation
      mechanism: "AI accelerates own development"
      
    labor_productivity_trend:
      magnitude: +1.5%/year
      delay: 3-5 years (deployment lag)
      duration: permanent
      uncertainty: very high
      
  by_entity:
    developed_economies:
      gdp_growth:
        magnitude: +0.8% to +2.5%/year
        delay: 3-5 years
        uncertainty: high
        
      unemployment_rate:
        magnitude: +3% to +8% (transition)
        delay: 2-5 years
        duration: 5-10 years (reabsorption)
        uncertainty: very high
        
      inequality_index:
        magnitude: +15 to +30 points
        delay: 5 years
        duration: until policy response
        
    developing_economies:
      labor_cost_advantage:
        magnitude: -30% to -50%
        mechanism: "Automation reduces value of low-cost labor"
        delay: 5-10 years
        
  conditional:
    - condition: "if ai_governance_effective"
      modifier: "reduce inequality impact by 50%"
    - condition: "if us_china_ai_race intensifies"
      modifier: "reduce safety investment, increase misalignment risk"
      
  cascades:
    - target: developed_economies.protest_activity
      magnitude: +20
      delay: 3-5 years
      mechanism: "Labor displacement creates political backlash"
    - target: developed_economies.regime_stability
      magnitude: -5 to -15
      condition: "if inequality increase exceeds +20"
```

Note: This event is not "positive" or "negative." It has a complex impact profile with significant upside (productivity), significant downside (displacement, inequality), and deep uncertainty.

---

## 6. Implementation Phases

### 6.1 v1.0: State-Conditioned Multipliers

**Scope**: Minimal changes to existing factor model architecture.

**Changes**:

1. **Classify all events by causal type** in the catalog

2. **For Type 2 events, add trigger conditions**:
   ```yaml
   trigger_conditions:
     - variable: [state variable]
       function: [linear | logistic | exponential]
       parameters: [function-specific]
       baseline_multiplier: 1.0  # at reference level
   ```

3. **Modify sampling loop**:
   ```python
   # After baseline dynamics
   for event in events:
       if event.type == 2:
           multiplier = compute_state_multiplier(event, state)
           p = event.base_probability * multiplier * factor_adjustment
       else:
           p = event.base_probability * factor_adjustment
       # ... sample as before
   ```

4. **For Type 3 events, implement two-stage sampling**:
   ```python
   if event.type == 3:
       if preconditions_met(event, state):
           if random() < event.window_probability:
               resolution = sample_multinomial(event.resolution_probabilities)
               apply_resolution_impacts(event, resolution, state)
   ```

5. **Move clear Type 4 events to baseline** (solar, batteries, general AI trend)

6. **Document cascade pathways** without implementing dynamic state feedback within year

**Limitations Accepted**:
- State updates still annual (no within-year cascades)
- Factor shocks go to event probability, not to pressure variables (cleaner coupling in v2.0)
- Type 4 baseline uncertainty simplified

### 6.2 v2.0: Full Hybrid Factor-State Model

**Scope**: Fundamental restructuring of factor interpretation and state coupling.

**Changes**:

1. **Redefine factors as pressure drivers**:
   - Each factor maps to one or more state variables
   - Factor realization = shock to those state variables
   - Event probability derived from state, not directly from factors

2. **Implement pressure accumulation**:
   - Track pressure variables explicitly
   - Baseline pressure trends (some things get worse over time)
   - Factor shocks add volatility around trend
   - Threshold surfaces defined in state space

3. **Sub-annual resolution for fast cascades**:
   - Monthly or quarterly time steps for financial/conflict dynamics
   - Annual aggregation for slow-moving variables (demographics, climate)

4. **Full cascade implementation**:
   - Events update state immediately
   - Updated state conditions subsequent event probabilities within same time step
   - Cascade chains can propagate (A → state change → B → state change → C)

5. **Validation infrastructure**:
   - Historical backtesting against known events
   - Sensitivity analysis for threshold estimates
   - Cross-validation of pressure functions

### 6.3 Migration Path

| Component | v1.0 State | v2.0 Target | Migration Effort |
|-----------|------------|-------------|------------------|
| Event catalog | Add type, trigger conditions | Pressure mappings | Moderate |
| Factor model | Unchanged interpretation | Pressure driver interpretation | Significant |
| Probability | Static + multipliers | Fully state-conditioned | Moderate |
| Type 3 | Two-stage sampling | Same, refined | Low |
| Type 4 | Removed to baseline | Same | Done in v1.0 |
| Cascades | Documented only | Implemented | Significant |
| Time step | Annual | Sub-annual option | Moderate |

---

## 7. Implications for Event Catalog

### 7.1 Required Changes to Event Template

**Current template** (per `event-template.md`) needs revision:

**Add:**
```yaml
# Causal classification
causal_type: 1 | 2 | 3  # No Type 4 in event catalog
causal_type_rationale: "Brief explanation of classification"

# For Type 2
pressure_specification:
  variables: [list of state variables]
  weights: [relative importance]
  threshold: [estimate with uncertainty]
  probability_function: [functional form]

# For Type 3  
window_specification:
  preconditions: [state conditions]
  window_probability: [annual, given preconditions]
  resolutions: [list with probabilities and separate impact vectors]

# Structured impact vector
impact_vector:
  global: [...]
  by_entity: [...]
  conditional: [...]
  cascades: [...]

# Durability specification
durability:
  type: permanent | recoverable | maintenance_required
  parameters: [type-specific]
```

**Remove:**
- Any implicit or explicit valence classification
- Simple scalar "impact" fields (replace with structured vectors)

### 7.2 Events to Reclassify or Remove

| Event | Current Status | Action |
|-------|----------------|--------|
| Solar breakthrough | In catalog | **Remove**: baseline trajectory |
| Battery breakthrough | In catalog | **Remove**: baseline trajectory |
| AI productivity gains | In catalog | **Reclassify**: Type 2 threshold if specific capability defined, else baseline |
| Accelerated decarbonization | In catalog | **Reclassify**: Type 3 (requires policy coordination) |
| Energy storage breakthrough | In catalog | **Type 2** if specific cost threshold, else baseline |
| AMOC collapse | Type unclear | **Confirm Type 2** with pressure specification |
| Pakistan failure | Type unclear | **Confirm Type 2** with pressure specification |
| Taiwan conflict | Type unclear | **Confirm Type 3** with window/resolution structure |
| Climate agreement | Possibly missing | **Add as Type 3** |

### 7.3 New Specification Requirements

Every event in the catalog must have:

1. **Causal type** with rationale
2. **Type-appropriate probability specification**:
   - Type 1: Base rate + adjustment factors
   - Type 2: Pressure variables + threshold + conditioning function
   - Type 3: Preconditions + window probability + resolution distribution
3. **Structured impact vector** with:
   - Multi-dimensional impacts (not single GDP number)
   - Actor-specific differentiation where relevant
   - Time profile (immediate, delayed, duration)
   - Durability specification
4. **Cascade documentation** (what state changes condition what other events)
5. **Uncertainty characterization** (where confidence is low, say so)

---

## 8. Deprecated Concepts

### 8.1 Opportunity Factors (Discarded)

**What was proposed**: Add factors F_COOP, F_INNOV, F_INST to enable "positive" events.

**Why discarded**:

1. **Conceptual incoherence**: "Opportunity" isn't a force like "climate stress." High F_CLIM causes drought; what does high F_COOP cause? The symmetry is superficial.

2. **Calibration impossible**: What is P(high cooperation window)? Stress factors can be grounded in observables; opportunity factors cannot.

3. **Wrong solution to real problem**: The real problem was Type 3 events need preconditions and coordination, not a magic factor that makes good things happen.

4. **Dissolves under valence reframing**: Once we abandon positive/negative classification, there's no category of events that needs special enabling factors.

**Replacement**: Type 3 window-resolution structure captures coordination requirements without inventing fictitious factors.

### 8.2 Positive/Negative Event Classification (Discarded)

**What was proposed**: Classify events as positive or negative, model asymmetries between them.

**Why discarded**:

1. **Valence is not an event property**: Events have impact vectors with effects on multiple dimensions for multiple actors. "Climate agreement" isn't positive—it has winners, losers, and tradeoffs.

2. **False symmetry**: Trying to balance "positive" and "negative" events implies they should be symmetric. They're not symmetric because they're not the same kind of thing—they're all just events with complex impacts.

3. **Masked the real structure**: The meaningful distinction is causal type (how probability works), not valence (summary judgment).

**Replacement**: Events have impact vectors. Evaluative judgments are external to the model.

### 8.3 Symmetric Duration Assumptions (Revised)

**What was assumed**: Events have characteristic durations based on event type.

**What was proposed**: Asymmetric duration—"positive" events need maintenance, "negative" events are permanent.

**Why revised**:

1. **Partially correct insight**: Agreements do require maintenance. But so do sanctions, alliances, and other non-agreement outcomes. "Positive" isn't the relevant category.

2. **Correct frame**: Durability depends on **impact type**, not event valence:
   - Deaths: permanent
   - Destruction: slow recovery
   - Agreements: maintenance required
   - Technology adoption: permanent
   - Policy regimes: until reversed

**Replacement**: Impact vectors specify durability by impact type. An event can have some permanent impacts and some fragile impacts simultaneously.

---

## Appendix A: Revised Event Template

```yaml
# ============================================
# EVENT SPECIFICATION TEMPLATE v2.0
# ============================================

# IDENTIFICATION
id: [UNIQUE_EVENT_ID]
name: "[Human-readable name]"
description: |
  [Multi-sentence description of what this event represents,
  what state transition it captures, and why it matters]

# CAUSAL CLASSIFICATION
causal_type: [1 | 2 | 3]
causal_type_rationale: |
  [Why this type? What makes it stochastic/threshold/contingent?]
  
# For hybrids:
secondary_type: [optional, if hybrid]
secondary_rationale: [optional]

# ============================================
# TYPE-SPECIFIC PROBABILITY SPECIFICATION
# ============================================

# FOR TYPE 1 (Stochastic)
type_1_specification:
  base_rate:
    annual_probability: [0.0 - 1.0]
    estimate_basis: "[Historical frequency, expert judgment, etc.]"
  adjustments:
    - factor: "[What could change the rate]"
      direction: [higher | lower]
      magnitude: [qualitative or quantitative]
  confidence: [low | medium | high]

# FOR TYPE 2 (Threshold)
type_2_specification:
  pressure_variables:
    - variable: [state_variable_id]
      weight: [0.0 - 1.0]
      transform: [linear | logistic | exponential | inverse]
      current_value: [assessed value]
      trend: [increasing | stable | decreasing]
  pressure_function: [weighted_sum | max | product | custom]
  threshold:
    estimate: [0.0 - 1.0 or natural units]
    uncertainty: [distribution or range]
    basis: "[Historical thresholds, structural analysis, etc.]"
  probability_function:
    form: [logistic | exponential | step | custom]
    parameters:
      [function-specific parameters]
  current_assessment:
    pressure_level: [current composite pressure]
    distance_to_threshold: [how far from threshold]
    implied_probability: [current annual probability]

# FOR TYPE 3 (Contingent)
type_3_specification:
  window:
    preconditions:
      - condition: "[State condition description]"
        variable: [state_variable_id]
        operator: [< | > | == | in_range]
        value: [threshold or range]
    precondition_logic: "[How conditions combine: AND, OR, etc.]"
    window_probability: [annual probability given preconditions met]
    window_duration: [years window stays open if not resolved]
  resolutions:
    - id: [resolution_id]
      name: "[Resolution name]"
      probability: [0.0 - 1.0, must sum to 1.0 across resolutions]
      description: "[What this resolution means]"
      # Impact vector specified below, keyed by resolution_id

# ============================================
# IMPACT VECTOR
# ============================================

impact_vector:
  # For Type 1 and Type 2, single impact vector
  # For Type 3, keyed by resolution_id
  
  [resolution_id or "default"]:
    global:
      [variable_id]:
        magnitude: [value, range, or distribution]
        delay: [years, 0 = immediate]
        duration: [years | permanent | maintenance_required]
        uncertainty: [low | medium | high | distribution]
        notes: "[optional clarification]"
    
    by_entity:
      [entity_id or entity_group]:
        [variable_id]:
          magnitude: [...]
          delay: [...]
          duration: [...]
          uncertainty: [...]
    
    conditional:
      - condition: "[State condition or concurrent event]"
        target: [which impact to modify]
        modifier:
          type: [multiplier | additive]
          value: [adjustment]
    
    cascades:
      - target_variable: [state_variable_id]
        target_entity: [entity_id, or "global"]
        magnitude: [change]
        delay: [years]
        mechanism: "[How this cascade works]"
        conditions: "[When this cascade applies]"

# ============================================
# DURABILITY SPECIFICATION
# ============================================

durability:
  # Specify for each major impact component
  [impact_component]:
    type: [permanent | recoverable | maintenance_required]
    
    # For recoverable:
    recovery_half_life: [years]
    full_recovery_possible: [true | false]
    permanent_scarring: [fraction that never recovers]
    recovery_conditions:
      - "[Condition for recovery to proceed]"
    
    # For maintenance_required:
    annual_survival_probability: [0.0 - 1.0]
    failure_triggers:
      - "[What could cause failure]"
    on_failure:
      - outcome: [partial_reversal | full_reversal | graceful_degradation]
        probability: [0.0 - 1.0]
        magnitude: [fraction of impact lost]

# ============================================
# FACTOR LOADINGS (for correlation structure)
# ============================================

factor_loadings:
  F_CLIM: [0.0 - 0.9]
  F_FIN: [0.0 - 0.9]
  F_HLTH: [0.0 - 0.9]
  F_GPT: [0.0 - 0.9]
  F_FOOD: [0.0 - 0.9]
  F_EUR: [0.0 - 0.9]
  F_MENA: [0.0 - 0.9]
  F_SAS: [0.0 - 0.9]
  F_EAS: [0.0 - 0.9]
  F_SSA: [0.0 - 0.9]
  F_LAM: [0.0 - 0.9]
  F_TECH: [0.0 - 0.9]

loading_rationale: |
  [Why these loadings? What factors drive this event or 
  create shared vulnerability?]

# ============================================
# METADATA
# ============================================

research_tier: [1 | 2 | 3]
confidence_assessment:
  probability: [low | medium | high]
  impact_magnitude: [low | medium | high]
  key_uncertainties:
    - "[Major uncertainty 1]"
    - "[Major uncertainty 2]"

sources:
  - "[Source 1]"
  - "[Source 2]"

related_events:
  - event_id: [related_event]
    relationship: [precursor | consequence | alternative | correlated]

created: [date]
last_updated: [date]
version: [version number]

notes: |
  [Additional context, caveats, or considerations]
```

---

## Appendix B: Impact Type Durability Reference

| Impact Type | Durability Model | Typical Parameters | Examples |
|-------------|------------------|-------------------|----------|
| **Mortality** | Permanent | N/A | Conflict deaths, pandemic deaths |
| **Displacement (forced)** | Mixed | 50% return within 5 years, 30% permanent | Refugees, conflict displacement |
| **Physical destruction** | Recoverable | Half-life 3-10 years, depends on resources | Infrastructure, capital stock |
| **Institutional collapse** | Recoverable | Half-life 10-20 years, requires coordination | State failure, institutional decay |
| **Institutional reform** | Maintenance | Survival 0.90-0.95/year | Democratic transitions, governance reform |
| **International agreement** | Maintenance | Survival 0.85-0.95/year | Treaties, trade deals, climate agreements |
| **Peace agreement** | Maintenance | Survival 0.92-0.97/year | Conflict resolution |
| **Policy regime** | Until reversed | Reversal probability varies | Sanctions, monetary policy, regulations |
| **Technology adoption** | Permanent | N/A once saturated | Infrastructure, capabilities |
| **Knowledge/capability** | Permanent | Can be lost if not maintained | Scientific knowledge, skills |
| **Resource depletion** | Permanent | N/A | Aquifer exhaustion, extinction |
| **Environmental threshold** | Permanent | N/A | Tipping points, ecosystem shifts |
| **Economic shock** | Recoverable | Half-life 2-5 years typically | Recessions, financial crises |
| **Political shock** | Variable | Depends on institutional resilience | Coups, regime changes |

---

## Appendix C: State Variable → Event Probability Mappings

**Type 2 events with documented pressure relationships:**

| Event | Primary Pressure Variables | Threshold Estimate | Probability Function |
|-------|---------------------------|-------------------|---------------------|
| AMOC_COLLAPSE | amoc_strength, global_temp_anomaly | amoc_strength < 40% of baseline | Logistic (steep) |
| PAKISTAN_STATE_FAILURE | pak.regime_stability, pak.water_stress, pak.debt_external | Composite > 0.70 | Logistic (moderate) |
| EGYPT_STATE_FAILURE | egy.regime_stability, nile_water_availability, egy.food_import_stress | Composite > 0.75 | Logistic (moderate) |
| AMAZON_TIPPING | amazon_forest_cover, global_temp_anomaly, deforestation_rate | forest_cover < 60% | Logistic (steep) |
| CHINA_ECONOMIC_CRISIS | chn.debt_public, chn.gdp_growth (lagged), chn.property_sector_stress | Composite > 0.65 | Exponential |
| HYPERINFLATION_[country] | [country].debt_monetization, [country].reserves_foreign, [country].inflation_rate | Inflation > 50%/year | Step function |

**Type 3 events with documented window conditions:**

| Event | Window Preconditions | Window P | Resolution Distribution |
|-------|---------------------|----------|------------------------|
| TAIWAN_CRISIS | us_china_tension > 70, china.regime_stability < 70 | 0.08 | Conflict 35%, Peaceful 20%, Status quo 45% |
| US_CHINA_ACCOMMODATION | us_china_tension < 60, leadership_alignment | 0.05 | Success 25%, Partial 35%, Failure 40% |
| MAJOR_CLIMATE_AGREEMENT | global_temp_anomaly > 1.5, recent_disaster, tension < 65 | 0.06 | Strong 30%, Weak 40%, None 30% |
| KOREA_UNIFICATION | nk.regime_stability < 30, us_china_tension < 50 | 0.03 | Peaceful 40%, Chaotic 35%, Absorbed 25% |
| MIDDLE_EAST_BREAKTHROUGH | israel_palestine_tension < threshold, us_engagement high | 0.04 | Durable 20%, Fragile 30%, Collapse 50% |

---

## Document Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial integrated framework |

---

**Next Steps:**

1. Review and approval of this framework
2. Revise existing event specifications to conform to new template
3. Update related methodology documents
4. Implement v1.0 state conditioning in simulation code
5. Deprecate superseded documents

---

*This framework supersedes prior treatments of positive/negative asymmetry and integrates the causal typology with the state specification. Events are state transitions with complex impact vectors; causal type determines modeling approach; durability depends on impact type.*
