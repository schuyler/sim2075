---
title: impact-estimation
type: note
permalink: methodology/impact-estimation
tags:
- methodology
- impacts
- estimation
- calibration
---

# Impact Estimation

**Updated per [[methodology/integrated-event-state-framework]]**

## What Impact Estimates Mean

Impact estimates describe **how state variables change when an event occurs**. Like probabilities, these are judgments, not measurements.

The key shift in the integrated framework: **Events have impact vectors, not valences.** An impact vector specifies:
- Which variables are affected
- Direction (increase/decrease)
- Magnitude (with uncertainty)
- Who is affected differently
- How long it lasts (durability)

Whether an impact is "good" or "bad" depends on whose welfare function you apply—that's external to the model.

---

## Impact Vector Structure

Every event specifies impacts using this structure:

```yaml
impact_vector:
  global:
    [variable_id]:
      magnitude: {mean, std, distribution}
      onset: immediate | delayed(N) | gradual(N)
      durability: {type, parameters}
      
  by_country:
    [country_id]:
      [variable_id]: {...}
      
  differential:
    exposure_variable: [state_variable_id]
    function: linear | threshold | custom
```

---

## Durability Types

**Critical insight from integrated framework:** Durability depends on **what kind of impact** it is, not whether the event is "good" or "bad."

### The Five Durability Types

| Type | Meaning | Example Impacts |
|------|---------|-----------------|
| **permanent** | Never reverses | Deaths, resource depletion, knowledge/capability gains, technology adoption (post-saturation) |
| **decaying** | Fades with half-life | Financial shocks, reputational damage, consumer confidence, market dislocations |
| **maintenance_required** | Fails without upkeep | Treaties, alliances, agreements, policy achievements, international institutions |
| **shock_vulnerable** | Can be reversed by events | Development gains, living standards, economic growth trajectories |
| **regime_dependent** | Persists only in certain states | Political achievements tied to specific regime, conditional agreements |

### Durability Specification

```yaml
durability:
  type: permanent | decaying | maintenance_required | shock_vulnerable | regime_dependent
  
  # For decaying:
  half_life: N years           # Time for 50% of impact to fade
  floor: X                     # Minimum persistent impact (0 = full decay)
  
  # For maintenance_required:
  annual_failure_prob: P       # Probability agreement/achievement fails each year
  failure_conditions: [...]    # State conditions that increase failure probability
  cascade_on_failure: bool     # Does failure trigger other events?
  
  # For shock_vulnerable:
  vulnerable_to: [event_ids]   # Which events can reverse this impact?
  reversal_fraction: X         # Fraction of gains lost if shock occurs
  
  # For regime_dependent:
  persists_in: [regime_ids]    # Which regime types preserve this impact?
  transitions_with: [...]      # State thresholds that end the regime
```

### Common Durability Patterns

| Impact Type | Typical Durability | Rationale |
|-------------|-------------------|-----------|
| Mortality | permanent | Deaths don't reverse |
| Physical destruction | decaying (recovery) | Infrastructure can be rebuilt; half-life = reconstruction time |
| Institutional collapse | maintenance_required | Requires coordination to maintain recovery |
| Treaties/agreements | maintenance_required | Defection possible each year |
| Technology adoption | permanent | Deployed technology doesn't un-deploy |
| Development gains | shock_vulnerable | Economic growth can be reversed by crises |
| Resource depletion | permanent | Exhausted reserves stay exhausted |
| Ecosystem transitions | regime_dependent (hysteresis) | Forest→savanna doesn't easily reverse |
| Scientific knowledge | permanent | Discoveries aren't forgotten |
| Market dislocations | decaying | Prices and confidence recover over time |

---

## Impact Categories

### Economic Impacts

| Variable | Units | Typical Durability |
|----------|-------|-------------------|
| GDP shock | % change | decaying (half-life varies) |
| GDP trajectory shift | % growth change | shock_vulnerable |
| Trade disruption | % reduction | decaying |
| Investment destruction | $ value | decaying (reconstruction) |
| Debt accumulation | % GDP | persistent until paid/defaulted |

### Humanitarian Impacts

| Variable | Units | Typical Durability |
|----------|-------|-------------------|
| Excess mortality | millions | **permanent** (definitionally) |
| Displacement | millions | decaying (return rate varies) |
| Acute food insecurity | millions | decaying (seasonal) |
| Chronic malnutrition | millions | shock_vulnerable |

### Political/Institutional Impacts

| Variable | Units | Typical Durability |
|----------|-------|-------------------|
| Regime stability shock | points (0-100) | decaying |
| Institutional quality change | -2.5 to +2.5 | shock_vulnerable |
| Alliance formation | categorical | maintenance_required |
| Treaty achievement | categorical | maintenance_required |
| State failure | categorical | regime_dependent (recovery hard) |

### Environmental Impacts

| Variable | Units | Typical Durability |
|----------|-------|-------------------|
| Emissions trajectory shift | % change | shock_vulnerable |
| Ecosystem transition | categorical | permanent or regime_dependent |
| Resource depletion | % remaining | permanent |
| Pollution damage | index | decaying (remediation) |

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
| Treaty success | Montreal Protocol, Antarctic Treaty, WTO formation |
| Technology adoption | Internet deployment, mobile phones, renewable energy |

**Adjust for:** Scale differences, structural changes, policy response capacity.

**Warning:** Single analogs are dangerous. 2008 is one data point, not a universal model.

### Method B: Transmission Channel Analysis

Identify pathways from event to impact. Estimate each pathway.

**Example — Taiwan Conflict:**
- Channel 1: Semiconductor supply disruption → manufacturing (decaying, 2-5yr half-life)
- Channel 2: Shipping disruption → trade costs (decaying, 1-2yr half-life)
- Channel 3: Financial contagion → asset prices (decaying, 0.5-1yr half-life)
- Channel 4: Direct casualties → mortality (permanent)
- Channel 5: Infrastructure destruction → capacity loss (decaying, 5-10yr recovery)

**Useful when:** Analogs don't exist or channels are well-understood.

**Warning:** Easy to miss channels or double-count.

### Method C: Comparative Scaling

If you have confidence in one event's impacts, scale others relative to it.

"Pakistan state failure displaces ~30M. Bangladesh affects a denser population with fewer exit routes—probably 40-60M."

---

## Calibration Anchors

### Economic Impacts (Global GDP)

| Observed Event | GDP Impact | Recovery | Durability Pattern |
|----------------|------------|----------|-------------------|
| 2008-09 Financial Crisis | ~3-4% decline | 2-3 years | decaying (half-life ~1.5yr) |
| COVID-19 (2020) | ~3% decline | 1 year | decaying (half-life ~0.5yr) |
| Great Depression | ~15% US decline | 10+ years | shock_vulnerable (WW2 ended it) |
| WWII (combatants) | 20-50% | Varied | decaying for winners; regime_dependent for losers |

### Displacement

| Observed Event | Displaced | Return Rate | Durability Pattern |
|----------------|-----------|-------------|-------------------|
| Syrian civil war | ~12M | Low (<20% as of 2025) | regime_dependent (conflict ongoing) |
| Ukrainian war (2022-) | ~8M refugees | TBD | regime_dependent (conflict ongoing) |
| Partition of India (1947) | ~15M | Permanent | permanent (political settlement) |
| Post-WWII Europe | ~60M | High (5-10yr) | decaying (half-life ~3yr) |

### Mortality

| Observed Event | Deaths | Notes |
|----------------|--------|-------|
| Syrian civil war (10+ years) | ~500K-600K | Direct and indirect |
| COVID-19 (global) | ~15-25M actual | Official ~7M |
| 1918 flu | ~50M | Pre-modern medicine |
| WWII | ~70-85M | Military + civilian + Holocaust |

**All mortality is permanent by definition.**

### Agreements and Treaties

| Agreement | Duration Achieved | Failure Mode | Durability Observed |
|-----------|-------------------|--------------|---------------------|
| Montreal Protocol | 35+ years | Low defection | maintenance_required (annual_failure ~1%) |
| Paris Agreement | Ongoing | High defection | maintenance_required (annual_failure ~10%) |
| NPT | 55+ years | Occasional defection | maintenance_required (annual_failure ~2%) |
| Cold War arms agreements | Varied | US/Russia withdrawal | maintenance_required (eventual failure) |

---

## Onset Timing

Impacts don't always occur immediately:

| Onset Type | Specification | When to Use |
|------------|---------------|-------------|
| **immediate** | Impact occurs same year as event | Financial shocks, mortality from acute events |
| **delayed(N)** | Impact begins N years after event | Infrastructure effects, demographic shifts |
| **gradual(N)** | Impact ramps up over N years | Climate effects, technology diffusion, behavioral changes |

Example:
```yaml
# Climate agreement impact on emissions
global_emissions_trajectory:
  magnitude: {mean: -0.25, std: 0.10}
  onset: gradual(10)  # Takes 10 years to fully materialize
  durability:
    type: maintenance_required
    annual_failure_prob: 0.08
```

---

## Differential Impacts

Many events affect countries differently based on their characteristics:

```yaml
differential:
  exposure_variable: energy_import_dependence
  function: linear
  effect: "Higher import dependence → larger GDP impact from oil shock"
  
  # Or more complex:
  function: threshold
  threshold: 50  # % import dependence
  below_threshold_multiplier: 0.5
  above_threshold_multiplier: 2.0
```

Common exposure variables:
- `energy_import_dependence` — for commodity shocks
- `food_import_dependence` — for food system events
- `debt_external` — for financial contagion
- `sea_level_exposure` — for sea level events
- `heat_exposure` — for climate/heat events
- `trade_openness` — for trade disruption events
- `ai_readiness_index` — for technology disruption

---

## Documentation Requirements

| Field | Description |
|-------|-------------|
| **Impact vector** | Full specification per variable |
| **Magnitude ranges** | Mean ± std for each impact |
| **Onset** | Immediate / delayed / gradual |
| **Durability** | Type + parameters for each impact |
| **Differential effects** | How impacts vary by country characteristics |
| **Method** | Analog / Transmission / Scaling |
| **Reference cases** | Historical events used for calibration |
| **Key uncertainties** | What could make impacts much larger/smaller? |

---

## Checklist for Impact Estimation

- [ ] All significant state variables affected are identified
- [ ] Direction and magnitude specified for each
- [ ] Durability type assigned based on impact type (not event valence)
- [ ] Durability parameters specified where required
- [ ] Onset timing specified (immediate/delayed/gradual)
- [ ] Differential impacts documented if relevant
- [ ] Estimation method cited (analog/transmission/scaling)
- [ ] Reference cases provided for calibration
- [ ] Key uncertainties listed
