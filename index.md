---
title: index
type: note
permalink: index
tags:
- index
- overview
- simulation
- methodology
---

# Discontinuity Effects Model - Index

## Overview

Monte Carlo simulation modeling geopolitical trajectories through 2075. We sample correlated discontinuity events and track their cumulative impacts across 40 countries and 12 regional aggregates.

**Start here**: [[methodology/00-start-here]]

---

## Methodology

### Working Documents

| Document | Purpose |
|----------|---------|
| [[methodology/00-start-here]] | **Orientation — start here** |
| [[methodology/01-level-1-workflow]] | Step-by-step event production (~40 min) |
| [[methodology/02-event-template]] | Template to copy for new events |
| [[methodology/03-quality-checklist]] | Final checks before saving |

### Reference Material

| Document | Purpose |
|----------|---------|
| [[methodology/reference/causal-types]] | Type 1/2/3 definitions and decision tree |
| [[methodology/reference/type-3-calibration]] | Type 3 specification guidance |
| [[methodology/reference/probability-estimation]] | How to estimate probabilities |
| [[methodology/reference/impact-estimation]] | Impact vectors and durability |
| [[methodology/reference/durability-types]] | The five durability models |
| [[methodology/reference/aftermath-branches]] | Post-event trajectory modeling |
| [[methodology/reference/factor-loadings]] | Factor loading guidance |
| [[methodology/reference/factor-correlation-matrix]] | Inter-factor correlation matrix (Ω) |
| [[methodology/reference/calibration-anchors]] | Reference events for comparison |
| [[methodology/reference/priority-event-ranking]] | Cross-check probability estimates |
| [[methodology/reference/state-specification]] | State variable definitions |

### Conceptual Foundations

| Document | Purpose |
|----------|---------|
| [[methodology/concepts/framework-overview]] | Why events are state transitions |
| [[methodology/concepts/state-event-coupling]] | Factor-state-event architecture |
| [[methodology/concepts/implementation-roadmap]] | v1.0 vs v2.0 phases |
| [[methodology/concepts/monte-carlo-framework]] | Simulation architecture |
| [[methodology/concepts/gaussian-copula]] | How correlated event sampling works |
| [[methodology/concepts/factor-correlation-structure]] | Why factors are correlated, not independent |
| [[methodology/concepts/epistemology]] | Intellectual honesty framing |
| [[methodology/concepts/tractability-boundaries]] | What we can vs. cannot reason about structurally |
| [[methodology/concepts/entropy-maximization]] | Default to maximum entropy for uncalibrated parameters |
| [[methodology/concepts/small-n-actor-problem]] | Why Type 3 resolution probabilities are intractable |

### Project Management

| Document | Purpose |
|----------|---------|
| [[methodology/project/tasks]] | **Actionable development tasks** — start here for next work |
| [[methodology/project/progress-tracker]] | Event specification status |
| [[methodology/project/open-questions]] | Methodological issues to explore |
| [[methodology/project/research-tiers]] | Level 1/2/3 research definitions |
| [[methodology/project/development-roadmap]] | Overall development plan |
| [[methodology/project/simulation-project-overview]] | Project context |
| [[methodology/project/validation]] | Validation approaches |

---

## Factor Model

12 latent factors capture event correlation. Events load on factors; correlated factor draws produce correlated event occurrences.

### Global Systemic Factors

| Factor | Name | Domain |
|--------|------|--------|
| [[factors/f-clim]] | Climate Stress | Environmental |
| [[factors/f-fin]] | Financial Fragility | Economic |
| [[factors/f-hlth]] | Pandemic/Health | Health |
| [[factors/f-gpt]] | Great Power Tension | Geopolitical |
| [[factors/f-tech]] | Technology Disruption | Technology |
| [[factors/f-food]] | Food System Stress | Cross-cutting |

### Regional Factors

| Factor | Name | Region |
|--------|------|--------|
| [[factors/f-eur]] | European Stress | Europe |
| [[factors/f-mena]] | MENA Instability | Middle East & North Africa |
| [[factors/f-sas]] | South Asian Stress | South Asia |
| [[factors/f-eas]] | East Asian Tension | East Asia |
| [[factors/f-ssa]] | Sub-Saharan Crisis | Sub-Saharan Africa |
| [[factors/f-lam]] | Latin American Stress | Latin America |

---

## Event Catalog

Events organized by domain. Each specifies causal type, probability, factor loadings, and impact vectors.

**Planning document**: [[events/planned-event-categories]]

### Climate Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/climate/amoc-weakening]] | Type 2 | ~1.0% | Level 1 complete |
| Amazon Tipping Point | Type 2 | TBD | Not started |
| Permafrost Methane Release | Type 2 | TBD | Not started |

### Geopolitical Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/geopolitical/pakistan-state-failure]] | Type 2 | ~1.5% | Level 1 complete |
| [[events/geopolitical/taiwan-conflict]] | Type 3 | ~3% window | Level 1 complete |
| Egypt State Failure | Type 2 | TBD | Not started |
| Sahel Catastrophe | Type 2 | TBD | Not started |

### Financial Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| Global Financial Crisis | Type 1/2 | TBD | Not started |
| Dollar Reserve Crisis | Type 2 | TBD | Not started |

### Health Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| Severe Pandemic | Type 1 | TBD | Not started |

### Breakthrough Events (Type 1)

**Planning document**: [[events/planned-breakthrough-events]]

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| Fusion Commercialization | Type 1 | TBD | Not started |
| Agricultural Yield Breakthrough | Type 1 | TBD | Not started |
| Cancer Treatment Breakthrough | Type 1 | TBD | Not started |
| Antimicrobial Platform | Type 1 | TBD | Not started |

---

## Research Documents

Foundational analysis informing the simulation's worldview and parameters.

| Document | Purpose |
|----------|---------|
| [[research/21st-century-assessment]] | Regional trajectories through 2075 — demographic and climate |
| [[research/collapse-patterns-framework]] | Historical collapse cases, pathways, quantified effects |
| [[research/brics-de-dollarization]] | Financial system analysis — reserve currency dynamics |
| [[research/positive-discontinuities-historical]] | Historical positive discontinuities for calibration |
| [[research/positive-negative-asymmetry-analysis]] | Analysis of asymmetries between positive and negative events |

---

## Quick Reference

### Causal Types

| Type | Name | Key Idea |
|------|------|----------|
| **1** | Stochastic | Stable base rate, timing unpredictable |
| **2** | Threshold | Probability rises as pressure accumulates |
| **3** | Contingent | Window opens → resolution uncertain |
| **4** | S-Curve | **Not an event** — baseline trajectory |

### Probability Anchors (Annual)

| Probability | Meaning | Example |
|-------------|---------|---------|
| ~0.5% | Very rare | AMOC collapse |
| ~1.5% | Uncommon | Pakistan state failure |
| ~3% | Occasional | Global financial crisis |

### Durability Types

| Type | Meaning |
|------|---------|
| **permanent** | Deaths, resource depletion |
| **decaying** | Financial shocks (half-life) |
| **maintenance_required** | Treaties, agreements |
| **shock_vulnerable** | Development gains |
| **regime_dependent** | Political achievements |

---

## Next Steps

1. Complete Level 1 for remaining 18 priority events
2. Build prototype simulation (Phase 2)
3. Sensitivity analysis (Phase 3)
4. Level 2 upgrades for high-impact events

---

*Last updated: December 2025*