---
title: methodology-index-v2
type: note
permalink: methodology/methodology-index-v2
tags:
- methodology
- index
- overview
- standards
- framework
---

# Methodology Index

## Primary Framework

**[[methodology/integrated-event-state-framework]]** — The core methodology document specifying:
- Events as state transitions (not valenced outcomes)
- Causal type classification (Type 1/2/3)
- Factor-state coupling architecture
- Impact vector structure and durability models
- Implementation phases (v1.0 → v2.0)

**Read this first if you're new to the project.**

## Purpose

This folder contains standards for specifying discontinuity events in the geopolitical Monte Carlo simulation. The goal is **durable research artifacts**—observations, mechanisms, and calibrated estimates that survive model changes.

## When to Read What

| When you're... | Read this | Length |
|----------------|-----------|--------|
| Understanding the framework | [[methodology/integrated-event-state-framework]] | 20 min |
| Starting the project (read once) | [[methodology/epistemology]] | 3 min |
| Producing a new event spec | [[methodology/level-1-workflow]] | 5 min |
| Need the blank template | [[methodology/event-template]] | — |
| Estimating probability | [[methodology/probability-estimation]] | 8 min |
| Cross-checking probability | [[methodology/priority-event-ranking]] | 2 min |
| Estimating impacts | [[methodology/impact-estimation]] | 5 min |
| Assigning factor loadings | [[methodology/factor-loadings]] | 4 min |
| Deciding research depth | [[methodology/research-tiers]] | 2 min |
| Finalizing an event | [[methodology/quality-checklist]] | 1 min |
| Comparing to reference events | [[methodology/calibration-anchors]] | 2 min |
| Understanding validation | [[methodology/validation]] | 5 min |
| Checking project status | [[methodology/progress-tracker]] | 1 min |

## Quick Reference

### Causal Types (from Integrated Framework)

| Type | Name | Probability Model | Examples |
|------|------|-------------------|----------|
| **Type 1** | Stochastic | Base rate × factor contribution | Pandemic emergence, earthquakes |
| **Type 2** | Threshold | State-conditioned via pressure function | State failure, AMOC collapse |
| **Type 3** | Contingent | P(window) × P(resolution\|window) | Taiwan crisis, climate agreement |
| **Type 4** | S-Curve | **Not an event** — baseline trajectory | Solar costs, AI capability |

### Research Tiers

| Tier | Method | When |
|------|--------|------|
| **Level 1** | Claude Opus from prior knowledge | All priority events initially |
| **Level 2** | Chat session with targeted web searches | Events flagged by sensitivity analysis |
| **Level 3** | Full research project with subagents | 3-5 events driving tail outcomes |

### Probability Calibration (rough anchors)

| Annual Prob | Meaning | Example |
|-------------|---------|---------|
| ~0.5% | Very rare, once in 200 years | AMOC collapse |
| ~1% | Rare, once per century | Major climate tipping point |
| ~2% | Uncommon, several per century | Severe pandemic |
| ~3% | Occasional, once per generation | Global financial crisis |
| ~5%+ | Regular occurrence | Consider if this is really a "discontinuity" |

### Factor Loading Scale

| Loading | Meaning |
|---------|---------|
| 0.0 | No relationship |
| 0.1-0.3 | Weak/marginal |
| 0.4-0.6 | Moderate, one of several drivers |
| 0.7-0.8 | Strong, primary driver |
| 0.85+ | Dominant, event expresses this factor |

### Impact Durability Types (from Integrated Framework)

| Type | Behavior | Examples |
|------|----------|----------|
| **permanent** | Never reverses | Deaths, knowledge gains, resource depletion |
| **decaying** | Fades over time | Financial shocks, reputational damage |
| **maintenance_required** | Fails without upkeep | Treaties, alliances, agreements |
| **shock_vulnerable** | Can be reversed by events | Development gains, living standards |
| **regime_dependent** | Persists only in certain states | Policy achievements |

## Document Status
| Document | Purpose | Status |
|----------|---------|--------|
| [[methodology/integrated-event-state-framework]] | **Primary framework** | **Current** |
| [[methodology/epistemology]] | Intellectual honesty framing | Complete |
| [[methodology/level-1-workflow]] | Step-by-step event production | Complete |
| [[methodology/event-template-v2]] | Canonical event template | **Current** |
| [[methodology/probability-estimation]] | Probability methods | Complete |
| [[methodology/priority-event-ranking]] | Cross-check ranking | Complete |
| [[methodology/impact-estimation-v2]] | Impact and durability methods | **Current** |
| [[methodology/factor-loadings]] | Factor loading guidance | Complete |
| [[methodology/research-tiers]] | Level 1/2/3 definitions | Complete |
| [[methodology/quality-checklist-v2]] | Final checklist with causal types | **Current** |
| [[methodology/calibration-anchors]] | Reference events | Complete |
| [[methodology/validation]] | Validation approaches | Complete |
| [[methodology/progress-tracker]] | Project status | Complete |
## Deprecated Documents

| Document | Status | Notes |
|----------|--------|-------|
| [[methodology/asymmetric-modeling-proposal]] | **DEPRECATED** | Opportunity factors discarded |
| [[methodology/discontinuity-causal-typology]] | **ABSORBED** | Content in integrated framework |

## Implementation Roadmap

**v1.0 (Current Target):**
- State-conditioned multipliers for Type 2 events
- Two-stage window-resolution for Type 3 events
- Type 4 dynamics moved to baseline
- Impact vectors with durability specifications

**v2.0 (Future):**
- Full hybrid factor-state model
- Explicit threshold monitoring
- Sub-annual cascade resolution
