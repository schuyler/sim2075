---
title: calibration-anchors
type: note
permalink: methodology/calibration-anchors
tags:
- methodology
- calibration
- anchors
- reference
---

# Calibration Anchor Events

**Updated per [[methodology/integrated-event-state-framework]]**

Reference events for calibrating new event specifications. When specifying a new event, find the most similar anchor and ask:
- Is the new event the same causal type?
- Is the new event more or less likely? By how much?
- Is the new event's impact larger or smaller? By how much?
- Should the loading pattern be similar or different?
- What durability types apply?

---

## Climate Anchor (Type 2: Threshold)

### AMOC Weakening

| Field | Value |
|-------|-------|
| **Causal Type** | Type 2 (Threshold) |
| **Annual probability** | ~1% (range 0.5-2%) at current pressure |
| **Key characteristics** | Climate tipping point, irreversible, high European economic impact, moderate humanitarian impact |
| **Primary factor** | F_CLIM (0.85) |
| **GDP impact** | Europe -8 to -15%, Global -2 to -5% |
| **Displacement** | 5-20M (European agricultural zones) |
| **Specification** | [[events/climate/amoc-weakening]] |

**Type 2 Parameters:**

| Field | Value |
|-------|-------|
| **Pressure variables** | amoc_strength, global_temp_anomaly, arctic_ice_extent |
| **Threshold** | ~40% of 2000 baseline AMOC strength |
| **Current pressure** | Moderate (amoc_strength ~95%) |
| **Sharpness** | High—once threshold approaches, collapse is rapid |

**Durability:** Impacts are **permanent** (ecosystem transition) or **regime_dependent** (recovery requires centuries if at all)

**Use as anchor for:** Other climate tipping points (Amazon, permafrost, ice sheets)—all Type 2

---

## State Failure Anchor (Type 2: Threshold)

### Pakistan State Failure

| Field | Value |
|-------|-------|
| **Causal Type** | Type 2 (Threshold) |
| **Annual probability** | ~1.5% (range 1-2.5%) at current pressure |
| **Key characteristics** | Nuclear state, multi-factor fragility, high humanitarian impact, regional spillover |
| **Primary factor** | F_SAS (0.7) with F_CLIM (0.4), F_FOOD (0.4) |
| **GDP impact** | Pakistan collapse, South Asia -3 to -8%, Global -1 to -2% |
| **Displacement** | 25-50M |
| **Specification** | [[events/geopolitical/pakistan-state-failure]] |

**Type 2 Parameters:**

| Field | Value |
|-------|-------|
| **Pressure variables** | regime_stability (-), water_stress (+), debt_external (+), internal_conflict_intensity (+) |
| **Threshold** | Composite pressure ~75 on 0-100 scale |
| **Current pressure** | Elevated (~55-60) |
| **Sharpness** | Moderate—instability can persist before collapse |

**Durability:** 
- Mortality: **permanent**
- Displacement: **decaying** (half-life ~10 years for refugee return)
- Regional GDP impact: **decaying** (half-life ~5 years)
- Nuclear security risk: **regime_dependent** (persists until new stable government)

**Use as anchor for:** Other state failures (Egypt, Nigeria, Ethiopia, Bangladesh)—all Type 2

---

## Financial Anchor (Type 1/2 Hybrid)

### Global Financial Crisis (2008-type)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1/2 Hybrid |
| **Annual probability** | ~3% (range 2-5%) |
| **Key characteristics** | Financial systemic, reversible within 2-3 years, global contagion |
| **Primary factor** | F_FIN (0.85) |
| **GDP impact** | Global -3 to -5%, Developed -4 to -6% |
| **Displacement** | Minimal direct |
| **Reference** | 2008 GFC, 1997 Asian crisis |

**Causal Structure:**
- Type 1 component: Trigger events (Lehman-type failures) have stochastic timing
- Type 2 component: Vulnerability accumulates (leverage, credit conditions, imbalances)

**Durability:**
- GDP shock: **decaying** (half-life ~1.5-2 years)
- Unemployment spike: **decaying** (half-life ~2-3 years)
- Debt accumulation: **persistent** (countries carry higher debt for decades)
- Institutional changes: **maintenance_required** (regulatory reforms can erode)

**Use as anchor for:** Regional financial crises, sovereign debt crises, currency crises

---

## Health Anchor (Type 1: Stochastic)

### Severe Pandemic (COVID-type or worse)

| Field | Value |
|-------|-------|
| **Causal Type** | Type 1 (Stochastic) |
| **Annual probability** | ~2% (range 1-3%) |
| **Key characteristics** | Health systemic, reversible, global reach, economic + mortality impacts |
| **Primary factor** | F_HLTH (0.85) |
| **GDP impact** | Global -2 to -5% |
| **Excess mortality** | 5-25M depending on severity |
| **Reference** | COVID-19, 1918 flu |

**Type 1 Basis:**
- Novel pathogen emergence is approximately Poisson
- Timing unpredictable; base rate estimable from historical frequency
- Limited leading indicators before emergence

**Durability:**
- Mortality: **permanent**
- GDP shock: **decaying** (half-life ~0.5-1 year for acute phase)
- Behavioral changes: **decaying** (half-life ~2-3 years)
- Health system strain: **decaying** (half-life ~1-2 years)
- Long-term health effects (long COVID equivalent): **decaying** (half-life ~5+ years)

**Use as anchor for:** Novel pandemics, antibiotic resistance crisis—Type 1

---

## Strategic Anchor (Type 3: Contingent)

### Taiwan Conflict

| Field | Value |
|-------|-------|
| **Causal Type** | Type 3 (Contingent) |
| **Annual probability** | ~1% overall (range 0.5-2%) |
| **Key characteristics** | Great power flashpoint, potentially irreversible geopolitical shift, semiconductor disruption |
| **Primary factors** | F_GPT (0.7), F_EAS (0.7) |
| **GDP impact** | Global -5 to -15% depending on escalation |
| **Reference** | No direct analog; Korean War, Cold War crises |

**Type 3 Parameters:**

| Field | Value |
|-------|-------|
| **Window preconditions** | us_china_tension > 75, taiwan.alliance_pressure > 60, trigger incident |
| **P(window opens \| preconditions)** | ~10% per year when conditions met |
| **Resolutions** | Military conflict (35%), Negotiated accommodation (25%), Economic coercion only (25%), Status quo preserved (15%) |

**Durability:**
- If military conflict: 
  - Casualties: **permanent**
  - Semiconductor disruption: **decaying** (half-life 3-5 years for rebuilding)
  - Geopolitical alignment: **regime_dependent**
- If negotiated accommodation:
  - Tension reduction: **maintenance_required** (annual_failure_prob ~5%)
  - Economic impacts: **decaying** (rapid recovery)

**Use as anchor for:** Other great power conflicts, Korean peninsula, negotiations—Type 3

---

## Agreement/Coordination Anchor (Type 3: Contingent)

### Major Climate Agreement

| Field | Value |
|-------|-------|
| **Causal Type** | Type 3 (Contingent) |
| **Annual probability** | Variable based on preconditions |
| **Key characteristics** | Coordination-dependent, requires maintenance, differential impacts by country |
| **Primary factors** | F_CLIM (0.3), F_GPT (0.2) |
| **GDP impact** | Mixed—benefits for some, costs for fossil exporters |
| **Reference** | Paris Agreement, Montreal Protocol, Copenhagen failure |

**Type 3 Parameters:**

| Field | Value |
|-------|-------|
| **Window preconditions** | Climate salience high, US + China + EU aligned on process, leadership transition windows |
| **P(window opens)** | ~15% per year when preconditions partially met |
| **Resolutions** | Binding ambitious agreement (20%), Weak agreement (40%), Collapse/no agreement (40%) |

**Durability:**
- Emissions trajectory shift: **maintenance_required** (annual_failure_prob 5-10% depending on strength)
- Technology deployment acceleration: **permanent** (learning curves don't reverse)
- Fossil exporter revenue decline: **permanent** (demand destruction)

**Use as anchor for:** Other international agreements, coordination achievements—Type 3

---

## Using Anchors with Causal Types

### Step 1: Match Causal Type

First ask: What causal type is my new event?
- If Type 1 → Use pandemic anchor for probability estimation method
- If Type 2 → Use state failure or climate anchor for pressure function structure
- If Type 3 → Use Taiwan or agreement anchor for window-resolution structure

### Step 2: Probability Comparison

"Egypt state failure: More or less likely than Pakistan?"
- Both are Type 2 → Compare pressure functions
- Egypt has higher food import dependence (higher F_FOOD weight)
- Egypt has stronger external support (higher threshold before failure)
- Egypt has different regional factor (F_MENA vs F_SAS)
- Judgment: Similar probability ~1-2%, but different pressure drivers

### Step 3: Impact Comparison with Durability

"Bangladesh state failure: What durability types?"
- Mortality: **permanent** (same as all state failures)
- Displacement: **decaying** but slower than Pakistan (fewer exit routes → longer half-life)
- Regional impact: **decaying** (similar to Pakistan)
- Sea level interaction: **permanent** (land lost to sea doesn't return)

### Step 4: Loading Comparison

"Egypt state failure: Similar pattern to Pakistan?"
- Both are Type 2 state failures → similar regional factor dominance
- Egypt loads on F_MENA instead of F_SAS
- Egypt has higher F_FOOD loading (more import dependent)
- Similar F_FIN exposure

### Step 5: Type-Specific Comparison

**For Type 2:** Compare pressure functions
- Same variables? Different weights?
- Similar threshold? Different sharpness?

**For Type 3:** Compare window-resolution structure
- Similar preconditions?
- Similar resolution distribution?
- Different resolution outcomes?
