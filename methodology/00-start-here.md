---
title: 00-start-here
type: note
permalink: methodology/00-start-here
tags:
- methodology
- index
- quickstart
- orientation
- purpose
---

# Start Here: Methodology Quick Reference

## Purpose and Decision Context

This simulation exists to explore how the world might transform over the next half-century.

The 21st century will be shaped by the interaction of demographic transition and climate change—two slow-moving forces already locked in and irreversible on human timescales. These forces challenge assumptions that have anchored geopolitical thinking for generations: American hegemony as permanent backdrop, economic growth as default condition, climate as stable context for human activity. The news is full of signals pointing toward futures not yet visible, and a wealth of interacting variables too complex to hold in any single mind.

### What the Simulation Enables

**Structured exploration of narrative futures.** The simulation helps trace complex causes and effects—how demographic decline interacts with climate stress, how financial fragility compounds political instability, how regional crises cascade or remain contained. It is a tool for thinking, not a crystal ball.

**Scenario generation and storytelling.** By running thousands of trajectories, the simulation can surface unexpected patterns, generate compelling "future histories," and identify which discontinuities drive the most dramatic divergences in outcomes.

**Education about systemic risk.** The process of building the simulation—specifying events, estimating probabilities, tracing transmission channels—forces rigorous thinking about how the world actually works. The model makes assumptions explicit and auditable.

**Interactive exploration.** The simulation can power games, visualizations, and other tools for exploring geopolitical trajectories, making complex dynamics accessible to broader audiences.

### The Core Intellectual Project

The simulation operationalizes a particular worldview about how demographic and climate forces will interact:

- Below-replacement fertility is now near-universal outside Sub-Saharan Africa and will reshape economic and political capacity everywhere
- Emissions are unlikely to decline fast enough to avoid severe climate impacts in vulnerable regions
- Wealthy nations will largely enforce borders rather than absorb climate migration at scale
- The result is a century of divergence—some regions adapting and maintaining stability, others facing compounding crises

This worldview may be wrong in important ways. The simulation makes it explicit so it can be examined, challenged, and revised as understanding improves.

### What Success Looks Like

The simulation succeeds if it enables clearer thinking about how discontinuity events interact, generates compelling narratives grounded in plausible mechanisms, reveals patterns that intuition alone would miss, and supports updating mental models when assumptions prove inconsistent.

The simulation fails if it produces false confidence in specific predictions, becomes an end in itself rather than a thinking tool, or obscures genuine uncertainty behind pseudo-precise numbers.

---

## What This Project Is

A Monte Carlo simulation of geopolitical trajectories through 2075. The simulation models **discontinuity events** (climate tipping points, state failures, conflicts, crises) that shock the system, tracks how they cluster through a **factor model**, and produces probability distributions of outcomes.

The goal is calibrated uncertainty—distributions that honestly reflect what we don't know while incorporating what we do.

---

## The Four Causal Types

Every event is classified by how its probability works:

| Type | Name | How Probability Works | Examples |
|------|------|----------------------|----------|
| **Type 1** | Stochastic | Stable base rate, unpredictable timing | Pandemic emergence, earthquakes |
| **Type 2** | Threshold | Probability rises as pressure accumulates | State failure, AMOC collapse, currency crisis |
| **Type 3** | Contingent | Window opens → resolution depends on decisions | Taiwan crisis, climate agreement |
| **Type 4** | S-Curve | **Not an event**—model as baseline trajectory | Technology adoption, cost curves |

**If unsure**: State failures and tipping points are usually Type 2. Great power conflicts and agreements are usually Type 3.

---

## Quick Constraints

- **Factor loadings**: Sum of squares must be ≤ 1.0
- **Probability ranges**: Use ranges, not false precision (1-3%, not 1.5-2.5%)
- **Type 4 events**: Move to baseline trajectory—they're not discontinuities
- **Durability**: Assigned by impact type (deaths=permanent, agreements=maintenance_required), not event "valence"

---

## Getting Things Done

| Task | Document | Time |
|------|----------|------|
| **Produce a new event spec** | [[methodology/01-level-1-workflow]] | ~40 min |
| **Get the blank template** | [[methodology/02-event-template]] | — |
| **Final checks before saving** | [[methodology/03-quality-checklist]] | 2 min |

## Looking Things Up

| Question | Document |
|----------|----------|
| What are the causal types? | [[methodology/reference/causal-types]] |
| How do I estimate probability? | [[methodology/reference/probability-estimation]] |
| How do impacts and durability work? | [[methodology/reference/impact-estimation]] |
| What are the durability types? | [[methodology/reference/durability-types]] |
| How do I assign factor loadings? | [[methodology/reference/factor-loadings]] |
| What are similar events for comparison? | [[methodology/reference/calibration-anchors]] |
| What's the probability ranking? | [[methodology/reference/priority-event-ranking]] |

## Understanding the Framework

| Topic | Document | Read When |
|-------|----------|-----------|
| Why events are state transitions, not "good/bad" | [[methodology/concepts/framework-overview]] | Once, to understand the approach |
| How factors, state, and events couple | [[methodology/concepts/state-event-coupling]] | When building the simulation |
| Epistemological honesty | [[methodology/concepts/epistemology]] | Once, to calibrate expectations |
| Implementation roadmap (v1.0 → v2.0) | [[methodology/concepts/implementation-roadmap]] | When planning development |
| Monte Carlo architecture | [[methodology/concepts/monte-carlo-framework]] | When building the simulation |
| State variables and entities | [[methodology/reference/state-specification]] | When building the simulation |

## Project Status

| Document | Purpose |
|----------|---------|
| [[methodology/project/progress-tracker]] | What's done, what's next |
| [[methodology/project/open-questions]] | Methodological issues to explore |
| [[methodology/project/research-tiers]] | Level 1/2/3 definitions |
| [[methodology/project/development-roadmap]] | Development phases |
| [[methodology/project/validation]] | How we test the model |

---

*Last updated: December 2025*