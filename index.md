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
| [[methodology/03-critical-review]] | Five judgment questions before format checks |
| [[methodology/04-format-checklist]] | Format verification before saving |
| [[methodology/05-source-template]] | Template for source registry notes |

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
| [[methodology/reference/variance-allocation]] | Type-based variance targets for factor model |
| [[methodology/reference/factor-correlation-matrix]] | Inter-factor correlation matrix (Ω) |
| [[methodology/reference/event-yaml-schema]] | **YAML schema for machine-readable event specs** |
| [[methodology/reference/mvp-dynamics-scope]] | **v0.1 dynamics scope** — essential vs. default vs. deferred |
| [[methodology/reference/simulator-architecture]] | **Simulator engine architecture** — execution model + decision records (ADRs) |
| [[methodology/reference/expression-language]] | **Event expression language** — normative contract for `pressure:`/`preconditions:`/`if:` expressions |
| [[methodology/reference/calibration-anchors]] | Reference events for comparison |
| [[methodology/reference/priority-event-ranking]] | Cross-check probability estimates |
| [[methodology/reference/research-documentation-standards]] | Source registry and citation conventions |

### State Model Reference

| Document | Purpose |
|----------|---------|
| [[methodology/reference/state-overview]] | **State model orientation — start here** |
| [[methodology/reference/state-entities]] | The 40 countries and 12 regional aggregates |
| [[methodology/reference/state-variables-country]] | Country-level variable catalog |
| [[methodology/reference/state-variables-global]] | Global variable catalog |
| [[methodology/reference/state-dynamics]] | How variables evolve between events |
| [[methodology/reference/state-transmission]] | How variables affect each other |
| [[methodology/reference/state-outputs]] | What the simulation produces |

### Conceptual Foundations

| Document | Purpose |
|----------|---------|
| [[methodology/concepts/framework-overview]] | Why events are state transitions |
| [[methodology/concepts/state-event-coupling]] | Factor-state-event architecture |
| [[methodology/concepts/implementation-roadmap]] | v1.0 vs v2.0 phases |
| [[methodology/concepts/monte-carlo-framework]] | Original methodology — factor-model foundations (§§8–9 superseded by [[methodology/reference/simulator-architecture]]) |
| [[methodology/concepts/gaussian-copula]] | How correlated event sampling works |
| [[methodology/concepts/factor-correlation-structure]] | Why factors are correlated, not independent |
| [[methodology/concepts/epistemology]] | Intellectual honesty framing |
| [[methodology/concepts/tractability-boundaries]] | What we can vs. cannot reason about structurally |
| [[methodology/concepts/entropy-maximization]] | Default to maximum entropy for uncalibrated parameters |
| [[methodology/concepts/small-n-actor-problem]] | Why Type 3 resolution probabilities are intractable |
| [[methodology/concepts/causal-chain-decomposition]] | Events as multi-stage causal chains with different types per stage |
| [[methodology/concepts/synthetic-variable-problem]] | Why synthetic indices undermine validity; observable decomposition approach |
| [[methodology/concepts/displacement-variables-design]] | IDP/refugee variable design (pending implementation) |

### Computational Tools

| Document | Purpose |
|----------|---------|
| [[methodology/tools/compute-scaled-loadings]] | Python script to compute correctly scaled factor loadings |
| [[methodology/tools/variance-verification-script]] | Python script to verify variance allocation calculations |

### Project Management

| Document | Purpose |
|----------|---------|
| [[methodology/project/tasks]] | **Actionable development tasks** — start here for next work |
| [[methodology/project/implementation-guide]] | **v0.1 execution plan** — build order, gates, contracts; written for agent orchestration |
| [[methodology/project/tasks-completed]] | Completed task archive |
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
| [[events/climate/amazon-tipping-point]] | Type 2 | ~2.0% | Level 1 complete |
| [[events/climate/permafrost-methane-release]] | Type 2 | ~1.5% | Level 1 complete |

### Geopolitical Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/geopolitical/pakistan-state-failure]] | Type 2 | ~1.5% | Level 1 complete |
| [[events/geopolitical/taiwan-conflict]] | Type 3 | ~2.0% | Level 1 complete |
| [[events/geopolitical/egypt-state-failure]] | Type 2 | ~1.5% | Level 1 complete |
| [[events/geopolitical/russia-state-failure]] | Type 2 | ~1.0% | Level 1 complete |
| [[events/geopolitical/saudi-regime-instability]] | Type 2 | ~0.8% | Level 1 complete |
| [[events/geopolitical/iran-regime-change]] | Type 2 | ~1.2% | Level 1 complete |
| [[events/geopolitical/turkey-political-breakdown]] | Type 2 | ~0.55% | Level 1 complete |
| [[events/geopolitical/chinese-political-crisis]] | Type 2/3 | ~0.4% | Level 1 complete |
| [[events/geopolitical/eu-fragmentation]] | Type 2 | ~0.4% | Level 1 complete |
| [[events/geopolitical/india-pakistan-military-conflict]] | Type 3 | ~0.9% | Level 1 complete |
| [[events/geopolitical/korean-peninsula-crisis]] | Type 3 | ~0.75% | Level 1 complete |
| [[events/geopolitical/us-china-economic-rupture]] | Type 3 | ~1.75% | Level 1 complete |
| [[events/geopolitical/iran-nuclear-acquisition]] | Type 2/3 | ~1.5% | Level 1 complete |
| [[events/geopolitical/sahel-catastrophe]] | Type 2 | ~1.8% | Level 1 complete |
| [[events/geopolitical/saudi-nuclear-acquisition]] | Type 3 | ~0.5% | Level 1 complete |
| [[events/geopolitical/us-constitutional-crisis]] | Type 2/3 | ~0.5% | Level 1 complete |

### Financial Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/financial/global-financial-crisis]] | Type 1/2 | ~3.0% | Level 1 complete |
| [[events/financial/dollar-reserve-crisis]] | Type 2 | ~1.5% | Level 1 complete |
| [[events/financial/chinese-economic-crisis]] | Type 2 | ~2.0% | Level 1 complete |

### Health Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/health/severe-pandemic]] | Type 1 | ~2.0% | Level 1 complete |

### Energy Events

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/energy/oil-supply-shock]] | Type 1 | ~2.5% | Level 1 complete |

### Breakthrough Events (Type 1)

**Planning document**: [[events/planned-breakthrough-events]]

| Event | Type | Annual Prob | Status |
|-------|------|-------------|--------|
| [[events/breakthrough/fusion-commercialization]] | Type 1 | ~0.9% | Level 1 complete |
| [[events/breakthrough/agricultural-yield-breakthrough]] | Type 1 | ~1.3% | Level 1 complete |
| [[events/breakthrough/cancer-treatment-breakthrough]] | Type 1 | ~1.0% | Level 1 complete |
| [[events/breakthrough/antimicrobial-platform]] | Type 1 | ~1.2% | Level 1 complete |
| [[events/breakthrough/energy-storage-breakthrough]] | Type 1 | ~0.8% | Level 1 complete |

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

## Sources

Evidence library supporting parameter choices. Sources are archived and cross-referenced to events.

**Index:** [[sources/index]]

**Standards:** [[methodology/reference/research-documentation-standards]]

**Template:** [[methodology/05-source-template]]

| Directory | Contents |
|-----------|----------|
| `sources/articles/` | News, magazine, opinion pieces |
| `sources/papers/` | Academic/peer-reviewed |
| `sources/reports/` | Think tanks, IGOs, NGOs, government |
| `sources/data/` | Datasets, statistical releases |
| `sources/books/` | Book chapters, excerpts |

---

## Journal

[[journal/index]] — Conceptual exploration sessions and emerging patterns

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

**The project plan is [[strategy/roadmap]].** Current phases:

1. ~~Complete Level 1 for all priority events~~ ✓ (event catalog at Level 1 scope)
2. **Phase 0 — Absorb the war**: catalog remediation + methodology corrections per [[strategy/sim2075-third-gulf-war-interaction]]
3. **Phase 1 — The engine**: v0.1 per [[methodology/reference/simulator-architecture]], executed per [[methodology/project/implementation-guide]] (runs in parallel with Phase 0)
4. **Phase 2 — Validation instruments**: sensitivity analysis, PCM attractor check, LLM path-plausibility audits

---

*Last updated: July 12, 2026*