---
title: impact-estimation-v2
type: note
permalink: methodology/impact-estimation-v2
tags:
- methodology
- impacts
- estimation
- durability
- impact-vectors
---

# Impact Estimation v2

**Updated per [[methodology/integrated-event-state-framework]]**

## What Impact Estimates Mean

Impact estimates describe **how state variables change when an event occurs**. Events are state transitions—discrete changes in the trajectory of one or more variables.

Key principles from the integrated framework:

1. **Events have impact vectors, not valence** — Specify effects on multiple variables, not whether the event is "good" or "bad"
2. **Impacts are multi-dimensional** — Different actors affected differently
3. **Durability depends on impact type** — Deaths are permanent, agreements require maintenance
4. **Cascades flow through state** — Event impacts change state, which affects future event probabilities

---

## Impact Vector Structure

Every event specifies impacts using a structured format:

```yaml
impact_vector:
  global:
    [variable_id]:
      direction: increase | decrease
      magnitude: {mean, std}
      onset: immediate | delayed(N) | gradual(N)
      durability: {type, parameters}
      
  by_country:
    [country_or_group]:
      [variable_id]: {...}
      
  differential:
    exposure_variable: [state_variable_id]
    function: linear | threshold
    description: "How impact scales with exposure"
```

### Required Components

| Component | Description | Example |
|-----------|-------------|---------|
| **Variable** | Which state variable changes | `gdp_real`, `regime_stability`, `displacement` |
| **Direction** | Increase or decrease | ↑ or ↓ |
| **Magnitude** | Mean and uncertainty | -3% ± 1.5% |
| **Onset** | When does impact materialize | Immediate, delayed 3 years, gradual over 10 years |
| **Durability** | How long does it persist | Permanent, decaying (half-life 5yr), maintenance_required |

---

## Durability Types

**Critical update**: Durability depends on the *type of impact*, not the "valence" of the event.

### The Five Durability Types

| Type | Behavior | Parameters | Examples |
|------|----------|------------|----------|
| **permanent** | Never reverses | None | Deaths, knowledge gains, resource depletion, ecosystem transitions |
| **decaying** | Fades toward baseline | `half_life`, `floor` | Financial shocks, reputational damage, GDP deviations |
| **maintenance_required** | Fails without ongoing effort | `annual_failure_prob`, `failure_conditions` | Treaties, alliances, agreements, policy achievements |
| **shock_vulnerable** | Can be reversed by other events | `vulnerable_to`, `reversal_fraction` | Development gains, institutional improvements |
| **regime_dependent** | Persists only in certain system states | `persists_in_regimes` | Political achievements tied to regime type |

### Durability by Impact Category

| Impact Category | Typical Durability | Notes |
|-----------------|-------------------|-------|
| **Mortality** | permanent | Deaths don't reverse |
| **Physical destruction** | decaying | Recovery time depends on resources available |
| **Infrastructure damage** | decaying | Half-life varies by severity and resources |
| **Institutional collapse** | decaying (long) | 10-30 year recovery requiring coordination |
| **Treaties/agreements** | maintenance_required | Annual probability of defection/failure |
| **Alliance formation** | maintenance_required | Requires continued mutual benefit |
| **Technology adoption** | permanent | Deployed technology doesn't un-deploy |
| **Knowledge/capability** | permanent | Scientific discoveries, weapons programs |
| **GDP shocks** | decaying | Typical half-life 2-5 years |
| **Living standards gains** | shock_vulnerable | Can be reversed by crises |
| **Political achievements** | regime_dependent | May not survive regime change |
| **Ecosystem transitions** | permanent (hysteresis) | Forest→savanna doesn't easily reverse |
| **Resource depletion** | permanent | Exhausted reserves stay exhausted |

### Specifying Durability

```yaml
# Permanent impact (deaths)
durability:
  type: permanent

# Decaying impact (GDP shock)
durability:
  type: decaying
  half_life: 3  # years
  floor: -0.02  # persistent 2% below baseline

# Maintenance-required impact (treaty)
durability:
  type: maintenance_required
  annual_failure_prob: 0.05  # 5% per year
  failure_conditions:
    - regime_change_in_major_party
    - economic_crisis_in_major_party
  cascade_on_failure: true

# Shock-vulnerable impact (development gains)
durability:
  type: shock_vulnerable
  vulnerable_to: [FINANCIAL_CRISIS, STATE_FAILURE, CONFLICT]
  reversal_fraction: 0.5  # Lose half the gains

# Regime-dependent impact (policy)
durability:
  type: regime_dependent
  persists_in_regimes: [democracy, hybrid_democratic]
  transitions_with: regime_type
```

---

## Impact Categories

### Economic Impacts

| Variable | Units | Durability | Notes |
|----------|-------|------------|-------|
| GDP (global/regional/country) | % change | decaying | Half-life typically 2-5 years |
| GDP growth rate | percentage points | shock_vulnerable | Can persist if structural |
| Inflation | percentage points | decaying | Mean-reverts to target |
| Debt/GDP | percentage points | decaying (slow) | Fiscal consolidation required |
| Reserves | months of imports | decaying | Rebuild rate depends on policy |

### Humanitarian Impacts

| Variable | Units | Durability | Notes |
|----------|-------|------------|-------|
| Displacement | Millions | decaying (variable) | Returns depend on conditions |
| Excess mortality | Millions | permanent | Deaths don't reverse |
| Food insecurity | Millions | decaying | Seasonal, shock-responsive |
| Health system damage | Index | decaying | Rebuild time 5-15 years |

### Political/Strategic Impacts

| Variable | Units | Durability | Notes |
|----------|-------|------------|-------|
| Regime stability | 0-100 scale | decaying | Recovery if stress removed |
| Institutional quality | Index | decaying (slow) | 10-30 year rebuild |
| Alliance cohesion | 0-100 scale | shock_vulnerable | Events can disrupt |
| Conflict intensity | 0-4 scale | decaying | Depends on resolution dynamics |

---

## Estimation Methods

### Method A: Historical Analog

Find comparable historical events. What were the observed impacts?

**This is the strongest method when good analogs exist.**

| Event Type | Potential Analogs |
|------------|-------------------|
| Financial crisis | 2008 GFC, 1997 Asian crisis, 1930s Depression |
| Pandemic | COVID-19, 1918 flu, 1957 flu |
| State failure | Syria, Yugoslavia, Somalia, USSR collapse |
| Climate disaster | Pakistan 2022 floods, European 2003 heat wave |
| Peace agreement | Camp David, Good Friday, Dayton |
| Technology adoption | Internet diffusion, mobile phone adoption |

**Adjust for:** Scale differences, structural changes, policy response capacity.

**Document:** Which analog(s) used, what adjustments made, why this analog is appropriate.

### Method B: Transmission Channel Analysis

Identify pathways from event to impact. Estimate each pathway.

**Example — Taiwan Conflict:**
- Channel 1: Semiconductor supply disruption → manufacturing → GDP
- Channel 2: Shipping disruption → trade costs → inflation
- Channel 3: Financial contagion → asset prices → wealth effect
- Channel 4: Direct military costs → government spending

**Useful when:** Analogs don't exist or channels are well-understood.

**Document:** Each channel, its estimated magnitude, total summed across channels.

### Method C: Comparative Scaling

If you have confidence in one event's impacts, scale others relative to it.

"Pakistan state failure displaces ~30M. Bangladesh affects a denser population with fewer exit routes—probably 40-60M."

**Document:** Reference event, scaling rationale, adjustment factors.

---

## Calibration Anchors

### Economic Impacts (Global GDP)

| Observed Event | GDP Impact | Duration | Recovery |
|----------------|------------|----------|----------|
| 2008-09 Financial Crisis | ~3-4% decline | 2-3 years | Full |
| COVID-19 (2020) | ~3% decline | 1-2 years | Full (aggregate) |
| Great Depression | ~15% US decline | 4 years down | 10+ years to prior trend |
| WWII (combatants) | 20-50% for losers | 5-15 years | Varied |

### Displacement

| Observed Event | Displaced | Duration | Return Rate |
|----------------|-----------|----------|-------------|
| Syrian civil war | ~12M | Ongoing (10+ years) | Low (<20%) |
| Ukrainian war (2022-) | ~8M external | Ongoing | Unknown |
| Partition of India (1947) | ~15M | Permanent | Near zero |
| Yugoslav wars | ~4M | 5-10 years | ~50% returned |

### Mortality

| Observed Event | Deaths | Timeframe | Notes |
|----------------|--------|-----------|-------|
| Syrian civil war | ~500K-600K | 10+ years | Direct + indirect |
| COVID-19 (global) | ~15-25M actual | 3 years | Official ~7M |
| 1918 flu | ~50M | 2 years | Pre-modern medicine |
| WWII | ~70-85M | 6 years | Military + civilian |

### Agreements/Treaties

| Agreement | Duration Before Failure/Revision | Notes |
|-----------|----------------------------------|-------|
| Bretton Woods | 27 years (1944-1971) | Structural pressures |
| Paris Climate | Ongoing, weak compliance | Maintenance challenges |
| Iran Nuclear Deal (JCPOA) | 3 years before US withdrawal | Political change vulnerability |
| Camp David | 45+ years, ongoing | High durability |

---

## Differential Impacts

Many events affect countries differently based on their characteristics. Document this with differential impact specifications:

```yaml
differential:
  exposure_variable: food_import_dependence
  function: linear
  description: "Countries with higher food import dependence experience larger inflation shock"
  
  # Or more complex:
  exposure_variables: [debt_external, reserves_foreign]
  function: threshold
  parameters:
    high_risk: "debt > 60% AND reserves < 3 months"
    medium_risk: "debt > 40% OR reserves < 6 months"
  description: "Countries meeting high_risk criteria experience 2x GDP impact"
```

---

## Cascade Effects

Events change state variables. Changed state affects probability of other events. Document expected cascade pathways:

```yaml
cascade_effects:
  - pathway: "Financial crisis → fiscal stress → reduced state capacity → higher P(instability)"
    target_event: STATE_FAILURE_VULNERABLE
    probability_modifier: "+0.02 annual probability"
    duration: 5 years
    mechanism: >
      Financial crisis depletes fiscal resources, reducing government 
      capacity to maintain services and security, increasing fragility.
      
  - pathway: "Climate agreement → reduced fossil demand → petrostates fiscal stress"
    target_event: PETROSTATE_INSTABILITY
    probability_modifier: "×1.5 multiplier"
    duration: 15 years
    mechanism: >
      Successful climate action reduces oil demand trajectory, 
      undermining revenue base for oil-dependent economies.
```

---

## Type-Specific Considerations

### Type 2 Events (Threshold)

Impacts include effect on **pressure variables** that condition future event probabilities:

```yaml
# Example: Financial crisis affects fragility pressure
impact_vector:
  by_country:
    emerging_markets:
      debt_pressure:  # Feeds into state failure pressure function
        direction: increase
        magnitude: {mean: 15, std: 5}  # Points on 0-100 pressure scale
        onset: immediate
        durability: {type: decaying, half_life: 3}
```

### Type 3 Events (Contingent)

Specify **separate impact vectors for each resolution**:

```yaml
event: TAIWAN_STRAIT_RESOLUTION

resolutions:
  - id: military_conflict
    impact_vector:
      global:
        semiconductor_supply: {direction: decrease, magnitude: {mean: -60, std: 15}}
        # ... severe impacts
        
  - id: negotiated_accommodation
    impact_vector:
      global:
        us_china_tension: {direction: decrease, magnitude: {mean: -20, std: 5}}
        # ... moderate positive impacts
        
  - id: status_quo_preserved
    impact_vector: null  # No change
```

---

## Documentation Requirements

| Field | Description | Required? |
|-------|-------------|-----------|
| **Variables affected** | Which state variables change | Yes |
| **Direction and magnitude** | ↑/↓ and mean ± std | Yes |
| **Onset timing** | Immediate / delayed / gradual | Yes |
| **Durability type** | Which of the 5 types | Yes |
| **Durability parameters** | Type-specific parameters | If applicable |
| **Estimation method** | Analog / Transmission / Scaling | Yes |
| **Reference cases** | Historical events used | If analog method |
| **Differential impacts** | How impacts vary by country | If significant variation |
| **Cascade effects** | Which event probabilities affected | If applicable |
| **Key uncertainties** | What could make impacts larger/smaller | Yes |
