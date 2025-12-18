---
title: calibration-anchors
type: note
permalink: methodology/reference/calibration-anchors
tags:
- methodology
- calibration
- anchors
- reference
- probability
- causal-types
---

# Calibration Anchor Events

Reference events for calibrating new event specifications. When specifying a new event, find the most similar anchor and ask:
- Is the new event the same causal type?
- Is the new event more or less likely? By how much?
- Is the new event's impact larger or smaller? By how much?
- Should the loading pattern be similar or different?
- What durability types apply?

**Key reference:** [[methodology/reference/causal-types]] for full Type 1/2/3 definitions and decision tree.

---

## Anchor Index by Causal Type

| Type | Anchor Event | Domain | Annual Prob |
|------|--------------|--------|-------------|
| **Type 1** | Severe Pandemic | Health | ~2% |
| **Type 1** | Oil Supply Shock | Energy/Geopolitical | ~2-3% |
| **Type 1** | Major Volcanic Eruption | Climate/Natural | ~0.5% |
| **Type 1** | Technology Breakthrough | Technology | Variable |
| **Type 2** | AMOC Weakening | Climate | ~1% |
| **Type 2** | Pakistan State Failure | Geopolitical | ~1.5% |
| **Type 1/2** | Global Financial Crisis | Financial | ~3% |
| **Type 3** | Taiwan Conflict | Geopolitical | ~1% |
| **Type 3** | Major Climate Agreement | Coordination | Variable |

---

## Type 1 Anchors (Stochastic)

Type 1 events have stable base rates estimable from historical frequency. Timing is unpredictable; limited leading indicators. See [[methodology/reference/causal-types]] for full definition.

### Severe Pandemic (COVID-type or worse)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1 (Stochastic) |
| **Annual probability** | ~2% (range 1-3%) |
| **Key characteristics** | Health systemic, reversible, global reach, economic + mortality impacts |
| **Primary factor** | F_HLTH (0.85) |
| **GDP impact** | Global -2 to -5% |
| **Excess mortality** | 5-25M depending on severity |

**Type 1 Basis:**
- Novel pathogen emergence is approximately Poisson
- Timing unpredictable; base rate estimable from historical frequency
- Limited leading indicators before emergence

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| COVID-19 | 2020 | Type 1 | Novel coronavirus; no meaningful leading indicators before Wuhan cluster |
| 1918 Influenza | 1918 | Type 1 | H1N1 reassortment; wartime conditions amplified spread but didn't cause emergence |
| HIV/AIDS | 1980s | Type 1 | Zoonotic spillover decades earlier; discovery timing stochastic |
| 2009 H1N1 | 2009 | Type 1 | Swine flu reassortment; lower severity than feared |

**Durability:**
- Mortality: **permanent**
- GDP shock: **decaying** (half-life ~0.5-1 year for acute phase)
- Behavioral changes: **decaying** (half-life ~2-3 years)
- Health system strain: **decaying** (half-life ~1-2 years)
- Long-term health effects: **decaying** (half-life ~5+ years)

**Use as anchor for:** Novel pandemics, antibiotic resistance crisis, bioterrorism events—all Type 1

**Specification:** [[events/health/severe-pandemic]] (not yet created)

---

### Oil Supply Shock

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1 (Stochastic) |
| **Annual probability** | ~2-3% (range 1.5-4%) |
| **Key characteristics** | Energy systemic, recoverable, inflationary, differential regional impact |
| **Primary factors** | F_MENA (0.5), F_FIN (0.4), F_GPT (0.3) |
| **GDP impact** | Global -1 to -3%, Oil importers -2 to -5% |
| **Displacement** | Minimal direct |

**Type 1 Basis:**
- Trigger events (wars, accidents, political decisions) have stochastic timing
- Supply infrastructure is geographically concentrated → single points of failure
- Historical frequency provides reasonable base rate
- Some leading indicators (geopolitical tension) but timing remains unpredictable

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| 1973 Oil Embargo | 1973 | Type 1 | OPEC response to Yom Kippur War; war timing was stochastic trigger |
| 1979 Iranian Revolution | 1979 | Type 1 | Revolution timing unpredictable; supply disruption followed |
| 1990 Gulf War | 1990 | Type 1 | Iraqi invasion timing stochastic; supply impact immediate |
| 2022 Russia-Ukraine | 2022 | Type 1/3 hybrid | War had Type 3 elements but energy disruption was Type 1 consequence |

**Durability:**
- Price spike: **decaying** (half-life ~1-2 years as markets adjust)
- Inflation pass-through: **decaying** (half-life ~1 year)
- Demand destruction: **permanent** (accelerates efficiency/substitution)
- Geopolitical realignment: **regime_dependent** (alliance shifts can persist)

**Use as anchor for:** Natural gas supply shocks, critical mineral disruptions, energy infrastructure attacks—Type 1

**Specification:** [[events/energy/oil-supply-shock]] (not yet created)

---

### Major Volcanic Eruption (VEI 6+)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1 (Stochastic) |
| **Annual probability** | ~0.5% for VEI 6+, ~0.1% for VEI 7 |
| **Key characteristics** | Climate forcing, agricultural disruption, regional devastation, global cooling |
| **Primary factors** | F_CLIM (0.4), F_FOOD (0.5) |
| **GDP impact** | Global -0.5 to -2%, Regional up to -10% |
| **Excess mortality** | 10K-1M depending on location and magnitude |

**Type 1 Basis:**
- Volcanic eruptions follow Poisson-like occurrence
- Geological processes are effectively stochastic at human timescales
- Historical frequency well-documented over centuries
- Monitoring provides days-to-weeks warning, not years

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| Pinatubo | 1991 | Type 1 | VEI 6; 0.5°C global cooling for ~2 years |
| Tambora | 1815 | Type 1 | VEI 7; "Year Without a Summer"; widespread famine |
| Krakatoa | 1883 | Type 1 | VEI 6; tsunamis, climate effects |
| Eyjafjallajökull | 2010 | Type 1 | VEI 4; aviation disruption example (lower magnitude) |

**Durability:**
- Mortality: **permanent**
- Climate forcing: **decaying** (half-life ~1-2 years for aerosols)
- Agricultural disruption: **decaying** (half-life ~1 year post-aerosol clearing)
- Regional infrastructure: **decaying** (half-life ~3-5 years for rebuilding)
- Aviation/trade disruption: **decaying** (half-life ~weeks to months)

**Use as anchor for:** Other natural disasters with stochastic timing (major earthquakes, asteroid impacts)—Type 1

**Specification:** [[events/climate/major-volcanic-eruption]] (not yet created)

---

### Technology Breakthrough (Positive Type 1)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1 (Stochastic) |
| **Annual probability** | Variable by domain; ~1-3% for major breakthroughs in active research areas |
| **Key characteristics** | Positive discontinuity, timing unpredictable, diffusion follows S-curve |
| **Primary factors** | F_TECH (0.7), domain-specific factors |
| **GDP impact** | Positive; +0.5 to +2% global over diffusion period |
| **Reference** | [[research/positive-discontinuities-historical]] |

**Type 1 Basis:**
- Scientific breakthroughs have stochastic "eureka" timing
- Research investment creates conditions but doesn't determine timing
- Historical frequency by domain provides rough base rates
- Limited leading indicators for when breakthrough occurs (vs. that research is active)

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| mRNA Vaccines | 2020 | Type 1 | Decades of research; COVID accelerated deployment but breakthrough timing was stochastic |
| Green Revolution | 1960s | Type 1 | Borlaug's dwarf wheat; research program existed but breakthrough timing unpredictable |
| Semiconductor Scaling | 1965+ | Type 1 series | Moore's Law as sequence of stochastic breakthroughs |
| Fracking | 2000s | Type 1 | Horizontal drilling + hydraulic fracturing combination |
| CRISPR | 2012 | Type 1 | Gene editing breakthrough; research was active but timing stochastic |

**Durability:**
- Knowledge gain: **permanent** (cannot be unlearned)
- Productivity improvement: **permanent** (but may be offset by new challenges)
- Deployment/diffusion: **shock_vulnerable** (economic crises can slow adoption)
- Regulatory approval: **maintenance_required** (can be reversed)

**Use as anchor for:** Fusion commercialization, agricultural yield breakthroughs, cancer treatment breakthroughs, AI capability jumps—Type 1 positive

**Specification:** [[events/planned-breakthrough-events]] for category planning

---

## Type 2 Anchors (Threshold)

Type 2 events have probability that rises as pressure accumulates toward a threshold. Collapse/transition becomes increasingly likely as pressure mounts. See [[methodology/reference/causal-types]] for full definition.

### AMOC Weakening

| Field | Value |
|-------|-------|
| **Causal Type** | Type 2 (Threshold) |
| **Annual probability** | ~1% (range 0.5-2%) at current pressure |
| **Key characteristics** | Climate tipping point, irreversible, high European economic impact, moderate humanitarian impact |
| **Primary factor** | F_CLIM (0.85) |
| **GDP impact** | Europe -8 to -15%, Global -2 to -5% |
| **Displacement** | 5-20M (European agricultural zones) |

**Type 2 Parameters:**

| Field | Value |
|-------|-------|
| **Pressure variables** | amoc_strength, global_temp_anomaly, arctic_ice_extent |
| **Threshold** | ~40% of 2000 baseline AMOC strength |
| **Current pressure** | Moderate (amoc_strength ~95%) |
| **Sharpness** | High—once threshold approaches, collapse is rapid |

**Historical Reference Events:**

| Event | Period | Type Classification | Notes |
|-------|--------|---------------------|-------|
| Younger Dryas | ~12,800 BP | Type 2 | AMOC shutdown from meltwater pulse; pressure accumulated then rapid transition |
| 8.2 kiloyear event | ~8,200 BP | Type 2 | Smaller AMOC disruption; same threshold dynamics |
| No modern analog | — | — | Current weakening is unprecedented in instrumental record |

**Durability:** 
- Climate regime shift: **permanent** (centuries to millennia for recovery)
- Agricultural zone displacement: **permanent** (on human timescales)
- Economic restructuring: **regime_dependent** (adaptation investment determines outcomes)

**Use as anchor for:** Other climate tipping points (Amazon dieback, permafrost methane, ice sheet collapse)—all Type 2

**Specification:** [[events/climate/amoc-weakening]]

---

### Pakistan State Failure

| Field | Value |
|-------|-------|
| **Causal Type** | Type 2 (Threshold) |
| **Annual probability** | ~1.5% (range 1-2.5%) at current pressure |
| **Key characteristics** | Nuclear state, multi-factor fragility, high humanitarian impact, regional spillover |
| **Primary factor** | F_SAS (0.7) with F_CLIM (0.4), F_FOOD (0.4) |
| **GDP impact** | Pakistan collapse, South Asia -3 to -8%, Global -1 to -2% |
| **Displacement** | 25-50M |

**Type 2 Parameters:**

| Field | Value |
|-------|-------|
| **Pressure variables** | regime_stability (-), water_stress (+), debt_external (+), internal_conflict_intensity (+) |
| **Threshold** | Composite pressure ~75 on 0-100 scale |
| **Current pressure** | Elevated (~55-60) |
| **Sharpness** | Moderate—instability can persist before collapse |

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| Soviet Collapse | 1991 | Type 2 | Economic/political pressure accumulated over decades; threshold crossed rapidly |
| Yugoslav Collapse | 1991 | Type 2 | Multi-ethnic state under economic pressure; ethnic threshold dynamics |
| Syrian State Failure | 2011+ | Type 2 | Drought + economic pressure + political rigidity → threshold crossed |
| Venezuelan Collapse | 2010s | Type 2 | Oil dependence + political dysfunction; slow-motion threshold crossing |

**Durability:** 
- Mortality: **permanent**
- Displacement: **decaying** (half-life ~10 years for refugee return)
- Regional GDP impact: **decaying** (half-life ~5 years)
- Nuclear security risk: **regime_dependent** (persists until new stable government)

**Use as anchor for:** Other state failures (Egypt, Nigeria, Ethiopia, Bangladesh, Venezuela)—all Type 2

**Specification:** [[events/geopolitical/pakistan-state-failure]]

---

## Type 1/2 Hybrid Anchor

### Global Financial Crisis (2008-type)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1/2 Hybrid |
| **Annual probability** | ~3% (range 2-5%) |
| **Key characteristics** | Financial systemic, reversible within 2-3 years, global contagion |
| **Primary factor** | F_FIN (0.85) |
| **GDP impact** | Global -3 to -5%, Developed -4 to -6% |
| **Displacement** | Minimal direct |

**Causal Structure:**
- **Type 1 component:** Trigger events (Lehman-type failures) have stochastic timing
- **Type 2 component:** Vulnerability accumulates (leverage, credit conditions, imbalances)

The hybrid nature means: probability rises with financial vulnerability (Type 2), but exact trigger timing remains stochastic (Type 1). Model as Type 2 with higher baseline variance.

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| 2008 GFC | 2008 | Type 1/2 | Leverage accumulated (Type 2); Lehman timing stochastic (Type 1) |
| 1997 Asian Crisis | 1997 | Type 2 dominant | Current account imbalances accumulated; Thailand devaluation was threshold |
| 1929 Crash | 1929 | Type 1/2 | Leverage accumulated; exact crash timing had stochastic elements |
| 2000 Dot-com | 2000 | Type 2 dominant | Valuation pressure accumulated; correction was threshold-like |
| 1987 Black Monday | 1987 | Type 1 dominant | More stochastic; less obvious pressure accumulation |

**Durability:**
- GDP shock: **decaying** (half-life ~1.5-2 years)
- Unemployment spike: **decaying** (half-life ~2-3 years)
- Debt accumulation: **persistent** (countries carry higher debt for decades)
- Institutional changes: **maintenance_required** (regulatory reforms can erode)

**Use as anchor for:** Regional financial crises, sovereign debt crises, currency crises, crypto contagion

**Specification:** [[events/financial/global-financial-crisis]] (not yet created)

---

## Type 3 Anchors (Contingent)

Type 3 events require a window to open, then resolution is determined by small-N actor decisions that are epistemically intractable. See [[methodology/reference/causal-types]] and [[methodology/reference/type-3-calibration]] for full treatment.

### Taiwan Conflict

| Field | Value |
|-------|-------|
| **Causal Type** | Type 3 (Contingent) |
| **Annual probability** | ~1% overall (range 0.5-2%) |
| **Key characteristics** | Great power flashpoint, potentially irreversible geopolitical shift, semiconductor disruption |
| **Primary factors** | F_GPT (0.7), F_EAS (0.7) |
| **GDP impact** | Global -5 to -15% depending on escalation |

**Type 3 Parameters:**

| Field | Value |
|-------|-------|
| **Window preconditions** | us_china_tension > 75, taiwan.alliance_pressure > 60, trigger incident |
| **P(window opens \| preconditions)** | ~10% per year when conditions met |
| **Resolutions** | Military conflict (35%), Negotiated accommodation (25%), Economic coercion only (25%), Status quo preserved (15%) |

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| Cuban Missile Crisis | 1962 | Type 3 | Window opened (missiles discovered); resolution depended on Kennedy-Khrushchev decisions |
| Korean War | 1950 | Type 3 | Window opened (North invasion); US response was contingent decision |
| 1995-96 Taiwan Strait | 1995-96 | Type 3 | Window opened (Lee Teng-hui visit); PRC response was missile tests, not invasion |
| Ukraine 2022 | 2022 | Type 3 | Window existed for years; Putin's decision timing was contingent |

**Durability:**
- If military conflict: 
  - Casualties: **permanent**
  - Semiconductor disruption: **decaying** (half-life 3-5 years for rebuilding)
  - Geopolitical alignment: **regime_dependent**
- If negotiated accommodation:
  - Tension reduction: **maintenance_required** (annual_failure_prob ~5%)
  - Economic impacts: **decaying** (rapid recovery)

**Use as anchor for:** Other great power conflicts (Korea, South China Sea), major bilateral crises—Type 3

**Specification:** [[events/geopolitical/taiwan-conflict]]

---

### Major Climate Agreement (Coordination Type 3)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 3 (Contingent) |
| **Annual probability** | Variable based on preconditions |
| **Key characteristics** | Coordination-dependent, requires maintenance, differential impacts by country |
| **Primary factors** | F_CLIM (0.3), F_GPT (0.2) |
| **GDP impact** | Mixed—benefits for some, costs for fossil exporters |

**Type 3 Parameters:**

| Field | Value |
|-------|-------|
| **Window preconditions** | Climate salience high, US + China + EU aligned on process, leadership transition windows |
| **P(window opens)** | ~15% per year when preconditions partially met |
| **Resolutions** | Binding ambitious agreement (20%), Weak agreement (40%), Collapse/no agreement (40%) |

**Historical Reference Events:**

| Event | Year | Type Classification | Notes |
|-------|------|---------------------|-------|
| Montreal Protocol | 1987 | Type 3 (success) | Window opened (ozone science consensus); negotiation succeeded |
| Paris Agreement | 2015 | Type 3 (partial) | Window opened (US-China bilateral); weak but universal agreement |
| Copenhagen | 2009 | Type 3 (failure) | Window opened; negotiation collapsed |
| Kyoto Protocol | 1997 | Type 3 (partial) | Agreement reached but US non-ratification limited effect |

**Key insight:** Same Type 3 structure can yield very different outcomes. Montreal succeeded where Copenhagen failed despite similar window conditions—small-N actor decisions (Reagan administration buy-in vs. China-US standoff) determined resolution.

**Durability:**
- Emissions trajectory shift: **maintenance_required** (annual_failure_prob 5-10% depending on strength)
- Technology deployment acceleration: **permanent** (learning curves don't reverse)
- Fossil exporter revenue decline: **permanent** (demand destruction)

**Use as anchor for:** Other international agreements, coordination achievements, treaty negotiations—Type 3

**Specification:** [[events/coordination/major-climate-agreement]] (not yet created)

---

## Using Anchors: Step-by-Step

### Step 1: Identify Causal Type

Before comparing to anchors, determine your event's causal type using [[methodology/reference/causal-types]]:

| If the event... | Then it's... | Primary anchor |
|-----------------|--------------|----------------|
| Has stable historical base rate, stochastic timing | Type 1 | Pandemic, Oil Shock, Volcanic |
| Has pressure accumulation toward threshold | Type 2 | State Failure, AMOC, Financial Crisis |
| Requires window + small-N actor decision | Type 3 | Taiwan, Climate Agreement |
| Combines stochastic trigger with accumulated vulnerability | Type 1/2 | Financial Crisis |

### Step 2: Select Matching Anchor

Choose the anchor most similar in domain and mechanism:

| Domain | Type 1 Anchor | Type 2 Anchor | Type 3 Anchor |
|--------|---------------|---------------|---------------|
| **Climate** | Volcanic Eruption | AMOC Weakening | Climate Agreement |
| **Geopolitical** | — | State Failure | Taiwan Conflict |
| **Financial** | — | Financial Crisis | — |
| **Health** | Pandemic | — | — |
| **Energy** | Oil Shock | — | — |
| **Technology** | Breakthrough | — | — |

### Step 3: Probability Comparison

Compare your event to the anchor:

**For Type 1:** "Is my event's base rate higher or lower than the anchor?"
- Pandemic anchor: ~2% annual
- If your health event is less severe → lower base rate
- If more transmissible pathogen class → possibly higher

**For Type 2:** "Is my event's pressure higher or lower? Threshold higher or lower?"
- Pakistan anchor: ~1.5% at current ~55-60 pressure
- If your state has higher current pressure → higher probability
- If your state has stronger institutions (higher threshold) → lower probability

**For Type 3:** "Are window conditions more or less likely? Resolution distribution similar?"
- Taiwan anchor: ~10% window opening when preconditions met
- If your crisis has more frequent trigger opportunities → higher window probability
- If fewer actors involved → resolution distribution may differ

### Step 4: Impact Comparison

**Scale impacts relative to anchor:**
- Pakistan displacement: 25-50M
- Smaller state with similar failure mode → proportionally smaller displacement
- Nuclear state like Pakistan → similar nuclear security concerns

**Match durability types:**
- All state failures: mortality is **permanent**, displacement is **decaying**
- Financial crises: GDP shock is **decaying**, debt is **persistent**
- Agreements: benefits are **maintenance_required**

### Step 5: Factor Loading Comparison

**Match regional factors:**
- Pakistan → F_SAS; Egypt → F_MENA; Nigeria → F_SSA
- Same failure mode, different regional factor dominance

**Match cross-cutting factors:**
- Pakistan has F_CLIM and F_FOOD loadings (water stress, food imports)
- Egypt has higher F_FOOD (more import dependent)
- Bangladesh has higher F_CLIM (sea level exposure)

### Step 6: Document Comparison

In your event specification, explicitly note:
- Which anchor you compared against
- Why probability is higher/lower
- Why impacts are larger/smaller
- What durability types you adopted and why

---

## Cross-Reference

- [[methodology/reference/causal-types]] — Full Type 1/2/3 definitions and decision tree
- [[methodology/reference/type-3-calibration]] — Detailed Type 3 specification guidance
- [[methodology/reference/probability-estimation]] — Probability estimation methods by type
- [[methodology/reference/impact-estimation]] — Impact vector specification
- [[methodology/reference/durability-types]] — The five durability models
- [[methodology/reference/priority-event-ranking]] — Cross-check probability rankings

---

*Last updated: December 2025*