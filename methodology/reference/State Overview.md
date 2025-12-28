---
title: State Overview
type: note
permalink: methodology/reference/state-overview
tags:
- methodology
- reference
- state
- overview
- simulation
---

# State Model Overview

## Entry Point for State Space Documentation

**Document Version:** 2.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

---

## Purpose

This document provides orientation to the simulation's state model — the variables that define the world at any point in time. For detailed specifications, see the linked reference documents.

**Related documents:**
- [[methodology/reference/state-entities]] — The 40 countries and 12 regional aggregates
- [[methodology/reference/state-variables-country]] — Country-level variable catalog
- [[methodology/reference/state-variables-global]] — Global variable catalog
- [[methodology/reference/state-dynamics]] — How variables evolve between events
- [[methodology/reference/state-transmission]] — How variables affect each other
- [[methodology/reference/state-outputs]] — What the simulation produces

**Conceptual foundations:**
- [[methodology/concepts/state-event-coupling]] — How events and state interact
- [[methodology/concepts/synthetic-variable-problem]] — Measurement validity and observable decomposition

---

## What the State Model Does

The simulation generates probability distributions of outcomes for countries, regions, and the global system by:

1. Tracking **state variables** that evolve over time for 40 individually-modeled countries, regional aggregates, and the global commons
2. Sampling **discontinuity events** that shock the system (per event methodology)
3. Modeling **transmission mechanisms** through which shocks propagate
4. Producing **distributional outputs** across thousands of simulation runs

The state model defines:
- What entities we track (countries, aggregates, global commons)
- What variables characterize each entity
- How variables evolve between discontinuity events
- How variables transmit effects to each other
- What outputs we produce for analysis

---

## Scope

| Dimension | Coverage |
|-----------|----------|
| **Time horizon** | 2025-2075 (50 years) |
| **Time step** | Annual |
| **Individual countries** | 40 |
| **Regional aggregates** | 12 (6 Tier 1, 6 Tier 2) |
| **Country-level variables** | ~50-60 per entity |
| **Global variables** | ~48 |
| **Simulation runs** | 10,000-50,000 for stable distributions |

---

## Coverage Statistics

The 40-country model captures:

| Metric | Coverage |
|--------|----------|
| World GDP | ~85% |
| World Population | ~74% |
| Nuclear States | 9 of 9 (100%) |
| G7 | 7 of 7 (100%) |
| G20 | 19 of 19 country members (100%) |
| BRICS (2024 expansion) | 10 of 10 (100%) |
| UN Security Council Permanent Members | 5 of 5 (100%) |

**Entity breakdown:**

| Category | Population (M) | % World | GDP ($T) | % World |
|----------|---------------|---------|----------|---------|
| 40 Individual Countries | 5,900 | 74% | 89 | 85% |
| Tier 1 Aggregates | 575 | 7% | 4.7 | 4% |
| Tier 2 Aggregates | 900 | 11% | 3.5 | 3% |
| **Model Total** | **7,375** | **92%** | **97.2** | **92%** |
| Unmodeled Remainder | 625 | 8% | 8 | 8% |

For detailed entity listings, see [[methodology/reference/state-entities]].

---

## Design Philosophy

### Granularity Where It Matters

Demographics are tracked at cohort level because they drive fiscal capacity, labor supply, instability risk, and military potential. Economic variables are tracked at sufficient detail to model debt dynamics and external vulnerability.

### Global Commons Explicitly Modeled

Climate, commodity prices, and financial system variables are tracked globally because they affect countries differentially and cannot be attributed to any single nation.

### Events as Shocks to State

The discontinuity event model generates discrete shocks; this state specification defines what gets shocked and how the system evolves between shocks.

### Outputs Support Both Terminal Assessment and Distributional Analysis

The simulation produces full state vectors at any time point, enabling both "what does 2050 look like in this run?" and "what is the distribution of outcomes across runs?"

### Observable Variables Over Synthetic Indices

Per [[methodology/concepts/synthetic-variable-problem]], we prefer directly observable or algorithmically derived variables over expert assessment indices. Synthetic assessments (fragility, stability, alignment) are computed as outputs for human interpretation, not used as causal intermediaries in probability conditioning.

---

## Variable Categories

### Country-Level Variables

| Category | Variables | Description |
|----------|-----------|-------------|
| **Demographic stocks** | 12 | Population by age/sex cohort |
| **Demographic flows** | 5 | Fertility, mortality, migration |
| **Economic stocks** | 6 | GDP, debt, reserves, current account |
| **Economic flows** | 4 | Growth, inflation, unemployment, FDI |
| **Economic structure** | 5 | Sectoral composition, trade openness |
| **Political/institutional** | ~10 | Observable governance and stability indicators |
| **Climate/resource** | 6 | Water, heat, agriculture, energy, food exposure |
| **Strategic position** | ~8 | Alliance status, sanctions, conflict involvement |

Total: ~55-60 variables per country. See [[methodology/reference/state-variables-country]] for full catalog.

### Global Variables

| Category | Variables | Description |
|----------|-----------|-------------|
| **Climate/Planetary** | 8 | Temperature, sea level, ice, AMOC, Amazon, CO2 |
| **Commodity Prices** | 12 | Oil, gas, food, metals |
| **Financial System** | 10 | Reserve shares, yields, policy rates |
| **Trade/Economic Structure** | 5 | Trade volume, shipping, semiconductors, payments |
| **Technology** | 3 | AI, renewables, batteries |
| **Health/Pandemic** | 3 | Pandemic status, severity, antibiotic resistance |
| **Geopolitical Structure** | 7 | Tension indices, alliance cohesion, conflict count |

Total: 48 global variables. See [[methodology/reference/state-variables-global]] for full catalog.

---

## Variable Dynamics

Variables evolve differently based on their nature:

| Dynamics Type | Characteristics | Examples |
|---------------|-----------------|----------|
| **Slow drift** | Deterministic trend + small noise | Temperature, CO2, demographics |
| **Mean-reverting** | Fluctuates around equilibrium | Oil prices, credit spreads |
| **Regime-dependent** | Different behavior in different states | AMOC (stable/collapsed), currencies |
| **Policy-driven** | Determined by decisions | Interest rates, sanctions |
| **Event-driven** | Dominated by discrete shocks | Conflict intensity, pandemic status |
| **Derived** | Computed from other variables | Dependency ratio, debt service |

See [[methodology/reference/state-dynamics]] for modeling approaches.

---

## Transmission Mechanisms

Variables affect each other through defined channels:

| Direction | Examples |
|-----------|----------|
| **Global → Country** | Oil prices → inflation; Temperature → agricultural risk |
| **Country → Country** | Trade linkages; Financial contagion; Migration flows |
| **Country → Global** | US policy → Treasury yields; China demand → commodities |

See [[methodology/reference/state-transmission]] for transmission specifications.

---

## Outputs

The simulation produces:

| Output Type | Description |
|-------------|-------------|
| **Terminal state** | Full state vector at simulation end |
| **Trajectories** | Time series for key variables |
| **Distributions** | Percentiles across simulation runs |
| **Scenario frequencies** | How often defined scenarios occur |
| **Contribution analysis** | Which events drive tail outcomes |
| **Derived assessments** | Human-interpretable stability/fragility/alignment scores |

See [[methodology/reference/state-outputs]] for output specifications.

---

## Integration with Event Model

The state model and event model interact bidirectionally:

**Events → State:** Discontinuity events shock state variables via impact vectors. Each event specifies which variables it affects and by how much.

**State → Events:** State variables condition event probabilities. Type 2 events have probability functions that depend on observable pressure variables. Type 3 event windows depend on preconditions defined in terms of state.

See [[methodology/concepts/state-event-coupling]] for the full architecture.

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial comprehensive specification (single document) |
| 2.0 | December 2025 | Refactored into modular documents; this overview extracted |

---

*This overview provides orientation. For implementation details, consult the linked reference documents.*