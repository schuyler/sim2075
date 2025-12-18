---
title: Simulation Project Overview
type: note
permalink: methodology/simulation-project-overview
tags:
- index
- overview
- project-management
---

# Simulation Project Overview

## Purpose

Monte Carlo simulation of geopolitical trajectories through 2075, producing probability distributions of outcomes for countries, regions, and the global system.

## Core Documents (Claude Project Files)

These methodology documents live in the Claude project and define the simulation architecture:

- **geopolitical-monte-carlo-methodology.md**: Discontinuity event modeling, factor structure, sampling approach
- **geopolitical-simulation-state-specification.md**: Entity inventory, state variables, outputs
- **geopolitical-simulation-development-roadmap.md**: Phased development plan
- **collapse-patterns-predictive-framework.md**: Historical collapse patterns, impact benchmarks
- **21st_century_assessment.md**: Regional trajectory assessments
- **brics-dedollarization-us-impact-research-2025.md**: Financial system analysis

## Memory Bank Structure

This knowledge base contains the working research that populates the simulation:

```
/factors/           # 12 latent factor definitions
/events/
  /climate/         # Climate tipping points, extreme weather
  /geopolitical/    # State failures, conflicts
  /financial/       # Economic crises, currency events
  /health/          # Pandemics
  /technology/      # Tech disruptions
/methodology/       # Reference docs, guidelines
/research/          # Source notes, decision logs
```

## Factor Model

12 latent factors capture event correlation:

### Global Systemic Factors
- [[F_CLIM - Climate Stress Factor]]
- [[F_FIN - Financial Fragility Factor]]
- [[F_HLTH - Pandemic Health Factor]]
- [[F_GPT - Great Power Tension Factor]]
- [[F_TECH - Technology Disruption Factor]]

### Cross-Cutting Factor
- [[F_FOOD - Food System Stress Factor]]

### Regional Factors
- [[F_EUR - European Stress Factor]]
- [[F_MENA - Middle East North Africa Instability Factor]]
- [[F_SAS - South Asian Stress Factor]]
- [[F_EAS - East Asian Tension Factor]]
- [[F_SSA - Sub-Saharan Africa Crisis Factor]]
- [[F_LAM - Latin American Stress Factor]]

## Event Catalog Status

### Completed (Level 1)
- [[AMOC Significant Weakening]] - Climate tipping point
- [[Pakistan State Failure]] - Geopolitical/state failure

### Priority Events (Remaining 18 of 20)
Climate:
- Amazon Tipping Point
- Permafrost Methane Release
- Multi-Breadbasket Failure

Great Power:
- Taiwan Conflict
- US-China Trade War Escalation
- Russia-NATO Direct Conflict

Regional/State Failure:
- Egypt State Failure
- Saudi Regime Instability
- Iran Regime Change
- Nigeria State Fragmentation
- South Africa Collapse

Financial:
- Global Financial Crisis
- Dollar Reserve Crisis
- EU Fiscal Crisis

Health:
- Severe Pandemic
- Antibiotic Resistance Crisis

Technology:
- Severe AI Disruption

Political:
- US Constitutional Crisis
- China Political Crisis

## Development Phase

Currently in **Phase 1: Event Catalog** per roadmap.

Next steps:
1. Complete Level 1 estimates for remaining 18 priority events
2. Move to Phase 2: Prototype Implementation
3. Phase 3 sensitivity analysis will identify which events need Level 2 research
