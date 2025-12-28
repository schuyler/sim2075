---
title: Synthetic Variable Problem
type: note
permalink: methodology/concepts/synthetic-variable-problem
tags:
- methodology
- concepts
- measurement
- validity
- synthetic-variables
- observables
- state-variables
---

# The Synthetic Variable Problem

## Why Some State Variables Undermine Simulation Validity

**Status:** Analysis and recommendations  
**Applies to:** [[methodology/reference/state-specification]]  
**Created:** December 2025

---

## 1. The Measurement Validity Problem

### What Makes a State Variable Useful?

For a state variable to be useful in simulation, it must satisfy three criteria:

1. **Definability**: We can specify what real-world phenomenon it measures
2. **Initializability**: We can establish a defensible starting value from data or structured estimation
3. **Updatability**: We can specify how events and dynamics change it in ways that correspond to real-world causation

Many variables in the current state specification fail one or more of these criteria.

### Measurement vs. Assessment

A crucial distinction:

**Measurement** observes a phenomenon and records a value. The value exists independently of the observer. Different competent observers would record the same (or very similar) values. Examples: population count, GDP in local currency, atmospheric CO2 concentration.

**Assessment** synthesizes observations into a judgment. The value depends on the observer's framework, weighting choices, and interpretation. Different competent observers might reach different values even with identical source data. Examples: "regime stability," "institutional quality," "state capacity."

Assessments are not useless—they compress complex realities into tractable summaries. But they create problems when used as causal intermediaries in simulation:

- The assessment methodology becomes a hidden model inside the simulation
- Shocks to assessments have unclear real-world referents
- Circular reasoning emerges when assessments condition probabilities of the phenomena they purport to measure

### The Circularity Problem

Consider `regime_stability` as a state variable conditioning P(state failure):

```
P(state_failure) = f(regime_stability, ...)
```

If `regime_stability` is defined as "likelihood the regime survives," this is tautological:

```
P(state_failure) = f(P(regime_survives), ...) 
```

We've restated the probability as a variable, gaining no information.

Even if `regime_stability` is defined differently—say, as "resilience to shocks"—the circularity persists in diluted form. The variable exists to capture regime survival likelihood. Using it to condition regime survival probability means the model's output is largely determined by an input that is itself a guess about the output.

### The Opacity Problem

When an event occurs, how does it update `institutional_quality`?

```
EVENT: severe_pandemic
IMPACT: institutional_quality -= ???
```

What number goes in the blank? The specification gives no guidance because there's no clear mapping between real-world pandemic effects and movements on an abstract institutional quality scale.

Contrast with an observable:

```
EVENT: severe_pandemic
IMPACT: gdp_growth -= 5 percentage points
```

This has a clear real-world referent. We can estimate it from historical pandemic data. We can defend the number.

---

## 2. Variable Taxonomy by Observability

We classify state variables into five categories based on their relationship to observable reality:

### Category A: Directly Measured

**Characteristics:**
- Official statistics or physical measurements
- Standard methodologies with documented procedures
- Different data collectors would produce same/similar values
- Clear units with physical or economic meaning

**Examples:**
- Population by cohort (census, demographic surveys)
- GDP in constant currency (national accounts)
- Public debt stock (treasury data)
- Atmospheric CO2 concentration (direct measurement)
- Oil price (market transactions)

**Treatment:** Keep as state variables. Initialize from authoritative sources. Update via explicit shock magnitudes with real-world referents.

### Category B: Algorithmically Derived from Observables

**Characteristics:**
- Computed from Category A variables via explicit formula
- Formula is documented and reproducible
- No subjective judgment in computation (though judgment may inform formula choice)

**Examples:**
- `dependency_ratio` = (pop_0_14 + pop_65+) / pop_15_64
- `export_concentration` = Herfindahl index of export categories
- `debt_service_ratio` = annual_debt_service / government_revenue
- `trade_openness` = (exports + imports) / GDP

**Treatment:** Keep as state variables OR compute on demand from components. Either approach is valid; choice depends on computational convenience.

### Category C: Proxy-Based Indices with Observable Components

**Characteristics:**
- Composite index aggregating multiple observable indicators
- Components are individually measurable
- Aggregation involves weighting choices, but components are transparent
- Examples: many Fragile States Index sub-components, some World Governance Indicators

**Examples:**
- `water_stress` = withdrawals / renewable_supply (observable ratio)
- Fragile States "Economic Decline" = f(GDP trend, inflation, unemployment, inequality, ...)
- Some corruption measures based on observable audit findings, prosecution rates

**Treatment:** Decompose into observable components. Track components as state variables. Compute composite at analysis time if desired for interpretation, but don't use composite as causal intermediary.

### Category D: Expert Assessment Indices

**Characteristics:**
- Scores assigned by expert coders or survey respondents
- Methodology exists but involves irreducible subjective judgment
- Different expert panels might produce different scores
- Often perception-based rather than behavior-based

**Examples:**
- V-Dem "liberal democracy index"
- Freedom House civil liberties scores  
- Corruption Perceptions Index (explicitly perception-based)
- Most "regime stability" operationalizations

**Treatment:** Do not use as state variables. Either:
1. Replace with observable proxies that the index attempts to capture
2. Use as initialization heuristic but track underlying observables
3. Compute as derived output for human interpretation

### Category E: Simulation Artifacts

**Characteristics:**
- Variables that exist only because the simulation needs a number
- No clear real-world measurement procedure
- Created to fill a modeling need rather than to represent an observable phenomenon

**Examples:**
- `alliance_west` (0-100): What real-world measurement yields 65 vs 72?
- `regime_stability` (0-100): What procedure produces this number?
- `state_capacity` (0-100): What observable distinguishes 50 from 60?

**Treatment:** Eliminate or radically redesign. Replace with:
1. Categorical variables with clear criteria (alliance: NATO member / SCO member / non-aligned / multi-aligned)
2. Observable indicators that the artifact was meant to proxy
3. Nothing, if the variable served no clear purpose

---

## 3. Analysis of Problematic Variables

### 3.1 `regime_stability` (0-100)

**What it purports to measure:** Likelihood or capacity of current regime to maintain power.

**Initialization problem:** No standard data source. Would require subjective scoring or adopting someone else's subjective scoring.

**Update problem:** How does a financial crisis change the number? By how much? No principled answer.

**Circularity problem:** Severe. If used to condition P(regime_change) or P(state_failure), we're using our guess about regime survival to predict regime survival.

**Recommendation:** ELIMINATE as state variable.

**Replacement approach:** Track observable correlates of regime instability:
- `years_since_irregular_transition`: Observable from historical record
- `coup_attempts_10yr`: Count from ACLED or similar
- `mass_protest_intensity`: Event count or participant estimates from ACLED
- `elite_cohesion_proxy`: Cabinet turnover rate, defection events
- `economic_stress_index`: Derived from GDP growth, inflation, unemployment
- `security_force_loyalty_proxy`: Military spending trajectory, purge events

Event probability conditioning references these observables directly:
```
P(regime_change) = f(years_since_transition, coup_attempts, protest_intensity, 
                     economic_stress, military_factors, ...)
```

For human interpretation, we can compute a "stability assessment" from these observables at analysis time—but this is an output, not a causal intermediary.

### 3.2 `institutional_quality` (-2.5 to +2.5, WGI-style)

**What it purports to measure:** Aggregate quality of governance institutions.

**Initialization problem:** Would adopt WGI or similar. Inherits their methodology.

**Update problem:** How does an event shock "institutional quality"? The concept is too abstract to have clear shock semantics.

**Circularity problem:** Moderate. Institutional quality plausibly affects many outcomes, but if it conditions P(state_failure) and state failure is partly defined by institutional collapse, circularity emerges.

**Recommendation:** DECOMPOSE into observable components.

**Replacement approach:** WGI itself is composed of sub-indicators. Track the observable components:
- `government_effectiveness_proxy`: Budget execution rates, service delivery metrics
- `regulatory_quality_proxy`: Business registration time, contract enforcement speed
- `rule_of_law_proxy`: Court case clearance rates, property rights security
- `control_of_corruption_proxy`: Audit findings, prosecution rates (not perceptions)

For variables without clean observables, accept that we cannot track them as state variables. The simulation models what we can measure; institutional nuance beyond our measurement capacity is treated as unmodeled uncertainty.

### 3.3 `state_capacity` (0-100)

**What it purports to measure:** Ability of the state to implement policy and provide services.

**Initialization problem:** No standard measure. Would require constructing an index.

**Update problem:** Same opacity as institutional_quality.

**Circularity problem:** Moderate. State capacity affects resilience to shocks, which affects probability of state failure, which is defined partly by capacity collapse.

**Recommendation:** ELIMINATE as separate variable. Overlaps with institutional_quality components.

**Replacement approach:** Merge into observable governance indicators:
- Tax revenue / GDP (fiscal extraction capacity)
- Budget execution rate (implementation capacity)  
- Infrastructure quality indices (outcome of capacity)
- Public sector wage / private sector wage ratio (bureaucratic competence proxy)

### 3.4 `civil_liberties` (0-100)

**What it purports to measure:** Extent of individual rights and freedoms.

**Initialization problem:** Would adopt Freedom House or V-Dem. Inherits their expert coding.

**Update problem:** How does a coup change civil liberties score? Expert judgment would be needed—but then we're running expert judgment inside the simulation.

**Circularity problem:** Low for most events, but present if civil liberties decline conditions P(democratic_breakdown).

**Recommendation:** MOVE TO OUTPUT or accept as slowly-changing background parameter.

**Replacement approach:** Civil liberties matter for the simulation primarily as:
1. A background condition affecting other dynamics (authoritarian states respond differently to crises)
2. An outcome we want to track (how do civil liberties fare across scenarios?)

For (1): Use `regime_type` categorical (Democracy / Hybrid / Authoritarian) as the relevant conditioning variable. This is coarser but more defensible.

For (2): Compute a civil liberties estimate at analysis time from observable proxies (press freedom events, political prisoner counts, protest permission rates).

### 3.5 `corruption_index` (0-100)

**What it purports to measure:** Level of corruption in public sector.

**Initialization problem:** CPI is perception-based. Actual corruption is hard to measure.

**Update problem:** Does a financial crisis increase corruption? The causal story is unclear, and quantification is arbitrary.

**Circularity problem:** Low, unless corruption conditions P(state_failure) and corruption is itself defined by institutional failure.

**Recommendation:** ELIMINATE as state variable. Use observable proxies where corruption matters.

**Replacement approach:** Where corruption affects the simulation:
- Investment climate → use FDI flows (observable outcome)
- Government effectiveness → use budget execution, service delivery metrics
- Elite extraction → use inequality measures, capital flight estimates

We don't need a corruption number if we track its consequences.

### 3.6 `fragility_score` (derived composite)

**What it purports to measure:** Overall fragility/vulnerability of a state.

**Initialization problem:** Derived from other state variables—but if those are synthetic, this compounds the problem.

**Update problem:** Inherits opacity from components.

**Circularity problem:** Severe if used to condition P(state_failure). Fragility score is essentially P(state_failure) restated as a variable.

**Recommendation:** ELIMINATE as state variable. Compute as output only.

**Replacement approach:** Fragility becomes a derived assessment computed from observable state at analysis time:

```python
def compute_fragility_assessment(state, country):
    """Compute fragility assessment from observable state variables."""
    economic_stress = compute_economic_stress(state, country)
    political_stress = compute_political_stress(state, country)
    climate_stress = compute_climate_stress(state, country)
    demographic_stress = compute_demographic_stress(state, country)
    
    # Weighted composite for human interpretation
    fragility = (0.30 * economic_stress + 
                 0.30 * political_stress + 
                 0.25 * climate_stress + 
                 0.15 * demographic_stress)
    
    return fragility
```

This is an output for understanding scenarios, not an input for conditioning probabilities.

### 3.7 `alliance_west`, `alliance_china`, `alliance_nonaligned` (0-100 each)

**What they purport to measure:** Degree of alignment with major power blocs.

**Initialization problem:** No standard measure. What observable yields "alliance_west = 67"?

**Update problem:** How does an event shift alignment by some number of points? Arbitrary.

**Circularity problem:** Low for most uses.

**Recommendation:** REDESIGN as categorical + observable indicators.

**Replacement approach:**

Categorical alliance status:
```
alliance_status: enum
  - NATO_MEMBER
  - NATO_PARTNER  
  - SCO_MEMBER
  - CHINA_SECURITY_PARTNER
  - US_BILATERAL_ALLY
  - NON_ALIGNED
  - MULTI_ALIGNED
```

Observable alignment indicators:
- `un_voting_alignment_us`: Correlation of UN General Assembly votes with US (measurable)
- `un_voting_alignment_china`: Same for China
- `military_exercise_partners`: Count/categorization of joint exercises
- `arms_import_source`: Share from US/NATO vs Russia/China
- `trade_share_west`: Trade with US+EU+allies as share of total
- `trade_share_china`: Trade with China as share of total
- `bri_participation`: Belt and Road project count/value

These are observable. Events can shock them with clear semantics:
```
EVENT: us_china_rupture
IMPACT: 
  - Countries must choose: alliance_status may shift
  - trade_share splits forced toward one bloc
```

### 3.8 `regime_type` (categorical: Democracy/Hybrid/Authoritarian)

**What it purports to measure:** Basic character of political system.

**Initialization problem:** Manageable. Polity, V-Dem, and Freedom House largely agree on broad categorization.

**Update problem:** Regime type changes are discrete events, not continuous shocks. This is actually appropriate for a categorical variable.

**Circularity problem:** Low. Regime type is a background condition, not a probability estimate.

**Recommendation:** KEEP, but clarify transition rules.

**Refinement:** Define explicit criteria for each category:
- **Democracy**: Competitive elections, peaceful transfers, basic civil liberties
- **Hybrid**: Elections occur but flawed; contested legitimacy; partial civil liberties
- **Authoritarian**: No competitive elections; single party/leader/military rule; limited civil liberties

Transitions occur via discrete events (democratic_breakdown, democratic_transition, etc.), not gradual drift.

---

## 4. The Observable Decomposition Approach

### Core Principle

Replace synthetic indices with bundles of observable indicators. The simulation tracks observables. Human-interpretable assessments are computed from observables at analysis time.

```
BEFORE:
  State Variable: regime_stability (synthetic)
  → Conditions P(state_failure)
  → Updated by ??? when events occur

AFTER:
  State Variables: years_since_transition, coup_attempts_10yr, 
                   protest_intensity, economic_stress, ...
  → Each observable conditions P(state_failure) via explicit function
  → Each observable updated by events with clear semantics
  
  Derived Output: stability_assessment = f(observables)
  → Computed for human interpretation
  → Not used as causal intermediary
```

### Benefits

1. **Auditability**: Can trace why P(state_failure) is high in a given run—which observables are elevated?

2. **Defensible initialization**: Each observable has a data source and measurement procedure.

3. **Clear update semantics**: Events shock observables with magnitudes that have real-world referents.

4. **No circularity**: Probability conditioning references causes (economic stress, protest activity), not restated probability estimates.

5. **Falsifiability**: Observable predictions can be checked against reality.

### Implementation Pattern

For each synthetic variable being replaced:

1. **Identify the construct**: What is the synthetic variable trying to capture?

2. **List observable correlates**: What measurable phenomena indicate this construct?

3. **Select tractable indicators**: Which correlates can we actually initialize and update?

4. **Specify data sources**: Where does initialization data come from?

5. **Define update rules**: How do events shock each indicator?

6. **Define derived output**: How do we compute human-readable assessment from indicators?

---

## 5. Implications for Probability Conditioning

### Current Approach (Problematic)

```yaml
event: pakistan_state_failure
type: 2
pressure_variables:
  - variable: pakistan.regime_stability  # SYNTHETIC
    weight: 0.35
  - variable: pakistan.water_stress
    weight: 0.25
  - variable: pakistan.debt_external
    weight: 0.20
  - variable: pakistan.institutional_quality  # SYNTHETIC
    weight: 0.20
```

Problems:
- `regime_stability` and `institutional_quality` are synthetic
- Weights on synthetics propagate arbitrary initialization choices
- No clear update path when events occur

### Revised Approach (Observable)

```yaml
event: pakistan_state_failure
type: 2
pressure_variables:
  # Political stress observables
  - variable: pakistan.years_since_irregular_transition
    weight: 0.10
    transform: inverse_log  # Longer = lower pressure
  - variable: pakistan.coup_attempts_10yr
    weight: 0.10
    transform: linear
  - variable: pakistan.protest_intensity_annual
    weight: 0.10
    transform: linear
  
  # Economic stress observables  
  - variable: pakistan.gdp_growth_3yr_avg
    weight: 0.10
    transform: inverse  # Lower growth = higher pressure
  - variable: pakistan.inflation_rate
    weight: 0.08
    transform: logistic(center=15, steepness=0.2)
  - variable: pakistan.debt_external
    weight: 0.10
    transform: logistic(center=60, steepness=0.1)
  - variable: pakistan.reserves_foreign
    weight: 0.07
    transform: inverse  # Fewer reserves = higher pressure
  
  # Resource stress observables
  - variable: pakistan.water_stress
    weight: 0.15
    transform: linear
  - variable: pakistan.food_import_dependence
    weight: 0.05
    transform: linear
  
  # Security observables
  - variable: pakistan.internal_conflict_intensity
    weight: 0.10
    transform: linear
  - variable: pakistan.military_spending_gdp_deviation
    weight: 0.05
    transform: absolute  # Large deviation either direction = stress
```

Benefits:
- Every variable is observable/measurable
- Weights can be calibrated against historical data
- Event impacts have clear targets
- No circular reasoning

### Calibration Approach

With observable pressure variables, we can attempt calibration:

1. **Historical cases**: For countries that experienced state failure, what were observable values beforehand?

2. **Near-misses**: For countries that approached failure but recovered, what were observable values?

3. **Stable cases**: For countries with prolonged stability, what observable ranges do they occupy?

4. **Weight estimation**: Statistical analysis of historical data can inform weights (with appropriate humility about out-of-sample performance).

This calibration is impossible with synthetic variables because we don't have ground-truth synthetic scores for historical cases—only post-hoc assessments.

---

## 6. Implications for State Specification

### Summary of Required Changes

| Current Variable | Category | Recommendation | Replacement |
|------------------|----------|----------------|-------------|
| `regime_stability` | E | ELIMINATE | Observable political stress indicators |
| `institutional_quality` | D | DECOMPOSE | Observable governance indicators |
| `state_capacity` | E | ELIMINATE | Merge with governance indicators |
| `civil_liberties` | D | OUTPUT ONLY | Derive from observables at analysis time |
| `corruption_index` | D | ELIMINATE | Track consequences, not corruption itself |
| `fragility_score` | Derived | OUTPUT ONLY | Compute from observables at analysis time |
| `alliance_west/china/nonaligned` | E | REDESIGN | Categorical status + observable indicators |
| `regime_type` | Categorical | KEEP | Clarify transition criteria |
| `protest_activity` | C | KEEP/RENAME | Rename to `protest_intensity_annual`, specify data source |
| `internal_conflict_intensity` | C | KEEP | Specify coding rules (UCDP/PRIO scale) |

### New Observable Variables to Add

**Political Stress Indicators:**
- `years_since_irregular_transition`: Integer, from historical record
- `coup_attempts_10yr`: Count, from ACLED/Powell-Thyne
- `leadership_tenure_years`: Integer, current leader
- `cabinet_turnover_annual`: Proportion replaced per year
- `political_prisoner_estimate`: Count, from human rights organizations
- `press_freedom_events`: Journalist arrests, outlet closures

**Governance Indicators:**
- `tax_revenue_gdp`: Percentage, from IMF
- `budget_execution_rate`: Percentage of approved budget spent
- `public_investment_efficiency`: Output per dollar of public investment

**Alignment Indicators:**
- `un_voting_alignment_us`: Correlation coefficient, from UN data
- `un_voting_alignment_china`: Correlation coefficient
- `arms_import_share_west`: Percentage from NATO countries
- `arms_import_share_east`: Percentage from Russia/China
- `trade_share_west`: Trade with US+EU+allies / total trade
- `trade_share_china`: Trade with China / total trade

**Security Indicators:**
- `military_spending_gdp`: Percentage, from SIPRI
- `military_spending_deviation`: Deviation from 10-year average
- `armed_forces_per_capita`: Soldiers per 1000 population

### Variables to Remove

- `regime_stability`
- `institutional_quality`
- `state_capacity`
- `corruption_index`
- `fragility_score`
- `alliance_west`
- `alliance_china`
- `alliance_nonaligned`

### Net Effect on State Space

Current: 53 country-level variables
Remove: 9 variables
Add: ~15 observable variables
Revised: ~59 country-level variables

Modest increase in variable count, substantial increase in measurement validity.

---

## 7. Implementation Sequencing

### Phase 1: Document Observable Decomposition (This Document)

- Analyze each problematic variable
- Specify replacement observables
- Define derived output computations
- Document reasoning for future reference

**Status:** This document

### Phase 2: Update State Specification

- Revise variable list per recommendations
- Add data source specifications for new observables
- Update variable count summaries
- Flag variables requiring further data source research

**Dependency:** This document approved

### Phase 3: Revise Event Specifications

- Update pressure_variables in Type 2 event specs
- Replace synthetic references with observable references
- Recalibrate weights where needed
- Document conditioning logic

**Dependency:** State specification updated

### Phase 4: Update Initialization Methodology

- Create initialization methodology document
- Specify data sources for each observable variable
- Define missing data handling
- Define validation checks

**Dependency:** State specification updated

### Phase 5: Define Derived Output Computations

- Specify formulas for human-interpretable assessments
- Fragility assessment from observables
- Stability assessment from observables
- Alignment assessment from observables
- Document computation procedures

**Dependency:** State specification updated

---

## 8. Derived Output Specifications

For human interpretation, we compute synthetic assessments from observables. These are OUTPUTS, not state variables—they don't condition probabilities or get updated by events.

### Stability Assessment

```python
def compute_stability_assessment(state, country) -> float:
    """
    Compute stability assessment from observable state variables.
    Returns value 0-100 where higher = more stable.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    # Political factors (40% weight)
    political = (
        0.15 * tenure_score(state[country].years_since_irregular_transition) +
        0.10 * inverse_score(state[country].coup_attempts_10yr, max=5) +
        0.10 * inverse_score(state[country].protest_intensity_annual, max=100) +
        0.05 * inverse_score(state[country].cabinet_turnover_annual, max=0.8)
    )
    
    # Economic factors (35% weight)
    economic = (
        0.15 * growth_score(state[country].gdp_growth_3yr_avg) +
        0.10 * inverse_score(state[country].inflation_rate, max=50) +
        0.05 * inverse_score(state[country].unemployment_rate, max=30) +
        0.05 * reserves_score(state[country].reserves_foreign)
    )
    
    # Security factors (25% weight)
    security = (
        0.15 * inverse_score(state[country].internal_conflict_intensity, max=4) +
        0.10 * inverse_score(state[country].external_conflict_involvement, max=4)
    )
    
    return 100 * (political + economic + security)
```

### Fragility Assessment

```python
def compute_fragility_assessment(state, country) -> float:
    """
    Compute fragility assessment from observable state variables.
    Returns value 0-100 where higher = more fragile.
    
    FOR HUMAN INTERPRETATION ONLY - NOT A STATE VARIABLE
    """
    # Simply invert stability
    return 100 - compute_stability_assessment(state, country)
```

### Alignment Assessment

```python
def compute_alignment_profile(state, country) -> dict:
    """
    Compute alignment profile from observable indicators.
    Returns dict with west/china/nonaligned scores (0-100 each).
    
    FOR HUMAN INTERPRETATION ONLY - NOT STATE VARIABLES
    """
    # West alignment
    west = (
        0.25 * un_voting_to_score(state[country].un_voting_alignment_us) +
        0.25 * state[country].arms_import_share_west +
        0.25 * state[country].trade_share_west +
        0.25 * alliance_status_west_score(state[country].alliance_status)
    )
    
    # China alignment
    china = (
        0.25 * un_voting_to_score(state[country].un_voting_alignment_china) +
        0.25 * state[country].arms_import_share_east +
        0.25 * state[country].trade_share_china +
        0.25 * alliance_status_china_score(state[country].alliance_status)
    )
    
    # Non-aligned is residual
    nonaligned = 100 - max(west, china)
    
    return {'west': west, 'china': china, 'nonaligned': nonaligned}
```

---

## 9. Open Questions

### Data Availability

Some proposed observable variables may have limited data availability:
- `budget_execution_rate`: Not uniformly reported
- `political_prisoner_estimate`: Contested methodology
- `cabinet_turnover_annual`: Requires systematic tracking

For variables with poor data availability, we must choose:
1. Accept coarser proxy (e.g., use Freedom House category instead of continuous measure)
2. Omit from pressure functions (accept that we can't model this factor)
3. Use regional/peer imputation (risky but sometimes necessary)

### Calibration Feasibility

Observable decomposition enables calibration against historical data—but do we have sufficient historical cases of state failure, regime change, etc. to estimate weights reliably?

If historical data is sparse, weights remain expert judgment. Observable decomposition is still valuable (transparency, auditability) but calibration benefits are limited.

### Complexity vs. Parsimony

Adding ~15 observable variables while removing 9 synthetic variables increases complexity. Is this justified?

Argument for: The synthetic variables were false parsimony—they hid complexity behind arbitrary numbers. Observable decomposition makes the actual complexity explicit.

Argument against: More variables means more initialization burden, more update rules, more parameters to specify. Some simplification might be acceptable if acknowledged.

This tradeoff should be evaluated during implementation.

---

## 10. Conclusion

The current state specification includes several synthetic variables that undermine simulation validity through circular reasoning, opaque update semantics, and arbitrary initialization.

The recommended approach:
1. **Eliminate** pure simulation artifacts (`regime_stability`, `state_capacity`, `corruption_index`, continuous alignment scores)
2. **Decompose** expert assessment indices into observable components
3. **Compute** human-interpretable assessments from observables at analysis time, not as state variables

This approach increases transparency, enables calibration, eliminates circularity, and makes the simulation auditable.

The tradeoff is increased variable count and data assembly burden. This is acceptable because the synthetic variables were providing false parsimony—they hid real complexity behind arbitrary numbers rather than eliminating it.

---

*Next step: Update [[methodology/reference/state-specification]] to implement these recommendations.*