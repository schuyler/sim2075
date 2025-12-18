---
title: methodology-index
type: note
permalink: methodology/methodology-index
tags:
- methodology
- index
- overview
- standards
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

## Document Status
| Document | Purpose | Status |
|----------|---------|--------|
| [[methodology/integrated-event-state-framework]] | **Primary framework** | **Current** |
| [[methodology/epistemology]] | Intellectual honesty framing | Complete |
| [[methodology/level-1-workflow]] | Step-by-step event production | Complete |
| [[methodology/event-template]] | Canonical event template | Complete |
| [[methodology/probability-estimation]] | Probability methods | Complete |
| [[methodology/priority-event-ranking]] | Cross-check ranking | Complete |
| [[methodology/impact-estimation]] | Impact and durability methods | Complete |
| [[methodology/factor-loadings]] | Factor loading guidance | Complete |
| [[methodology/research-tiers]] | Level 1/2/3 definitions | Complete |
| [[methodology/quality-checklist]] | Final checklist with causal types | Complete |
| [[methodology/calibration-anchors]] | Reference events | Complete |
| [[methodology/validation]] | Validation approaches | Complete |
| [[methodology/progress-tracker]] | Project status | Complete |
## Future Extensions
- **v2.0 hybrid factor-state model** — Factors as pressure drivers with explicit threshold surfaces. See [[methodology/integrated-event-state-framework]] Section 6.2.
- **Sub-annual time steps** — For cascade-sensitive dynamics (financial, conflict).
- **Full cascade implementation** — Events update state immediately, conditioning subsequent events.

## Deprecated Documents

| Document | Status | Reason |
|----------|--------|--------|
| [[methodology/asymmetric-modeling-proposal]] | **DEPRECATED** | Opportunity factors discarded; superseded by integrated framework |
| [[methodology/discontinuity-causal-typology]] | **ABSORBED** | Content incorporated into integrated framework |