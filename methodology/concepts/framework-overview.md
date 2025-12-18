---
title: framework-overview
type: note
permalink: methodology/concepts/framework-overview
tags:
- methodology
- concepts
- framework
- overview
- valence
- state-transitions
---

# Framework Overview

This document explains the conceptual foundations of the discontinuity modeling approach. Read this once to understand *why* we model events this way.

---

## The Core Reframing: Events as State Transitions

### Why "Positive" and "Negative" Are Not Event Properties

Prior thinking framed events as intrinsically "positive" or "negative," then struggled to model asymmetries between them. This framing is flawed.

Consider "Major International Climate Agreement":

| Dimension | Impact | For Whom? |
|-----------|--------|-----------|
| Emissions trajectory | Reduced | Global benefit |
| Climate damages avoided | Substantial | Vulnerable populations |
| Fossil exporter revenues | Collapsed | Saudi, Russia, Iran |
| Stranded asset losses | $Trillions | Asset holders |
| Energy transition costs | High | Near-term |
| Energy security (renewables) | Improved | Long-term |
| Great power relations | Ambiguous | Depends on burden-sharing |

This event cannot be assigned a valence. It has a complex **impact vector** with winners, losers, tradeoffs, and deep uncertainty. Whether it is "good" depends on whose welfare function you apply.

The same applies to supposedly "obvious" cases:

**AMOC Collapse** (seemingly negative):
- Northwestern Europe: severe cooling
- Southern Europe: possibly less severe than greenhouse warming alone
- Global politics: might catalyze action (or fatalism)

**AI Productivity Breakthrough** (seemingly positive):
- Aggregate GDP: increases
- Labor displacement: millions of jobs lost
- Inequality: widens (capital vs. labor)
- Geopolitical: advantage to technology leaders

### The Solution: Events Have Impact Vectors

An event is a **discrete change in the trajectory of one or more state variables**.

Events are characterized by:
1. What state transition they represent
2. What conditions make them more/less likely
3. What impact vector results from the transition
4. How durable each impact component is

Evaluative judgments ("good"/"bad") are external to the model. Users apply their own welfare functions to the impact vectors.

---

## Why Causal Type Matters

Events differ fundamentally in how their probability works:

**Type 1 (Stochastic)**: Pandemic emergence doesn't accumulate—there's a base rate, and timing is unpredictable.

**Type 2 (Threshold)**: State failure does accumulate—pressure builds until a threshold is crossed. The probability depends on current state.

**Type 3 (Contingent)**: Taiwan conflict depends on decisions—preconditions create windows, but resolution depends on specific actors.

**Type 4 (S-Curve)**: Solar cost decline follows a learning curve—it's not a discrete event at all.

Mixing these up produces bad models:
- Treating Type 2 as Type 1 misses how pressure accumulation changes probability
- Treating Type 3 as Type 2 misses the role of agency and negotiation
- Treating Type 4 as discrete events invents discontinuities that don't exist

---

## The Factor Model: Why Events Cluster

Events don't occur independently. Financial crises, political instability, and climate disasters tend to cluster because:

- **Common causes**: Climate stress drives both drought and instability
- **Causal chains**: Drought → food prices → instability
- **Contagion**: Financial crisis spreads across borders
- **Feedback loops**: Instability → capital flight → economic crisis → more instability

The factor model captures clustering through 12 latent factors:

**Global Systemic**: Climate Stress (F_CLIM), Financial Fragility (F_FIN), Health (F_HLTH), Great Power Tension (F_GPT), Technology (F_TECH), Food Systems (F_FOOD)

**Regional**: European (F_EUR), MENA (F_MENA), South Asian (F_SAS), East Asian (F_EAS), Sub-Saharan (F_SSA), Latin American (F_LAM)

Events load on factors based on what drives them. When F_CLIM is high, all climate-sensitive events become more likely together.

---

## Durability: Why Impact Type Matters

Prior thinking assumed "positive events are fragile, negative events are permanent." This is wrong.

Durability depends on **what kind of impact** it is:

| Impact Type | Durability |
|-------------|------------|
| Deaths | Permanent (always) |
| Infrastructure damage | Decaying (rebuilding possible) |
| Agreements | Maintenance required (can defect) |
| Technology adoption | Permanent (once deployed) |
| Development gains | Shock vulnerable |
| Resource depletion | Permanent |

A climate agreement has some permanent impacts (technology deployment accelerates, learning curves advance) and some maintenance-required impacts (emissions commitments require ongoing compliance).

A war has some permanent impacts (deaths, knowledge gained) and some decaying impacts (GDP recovers, infrastructure rebuilds).

The same event can have impacts with different durabilities.

---

## State-Event Coupling

The simulation architecture connects events and state bidirectionally:

1. **Factors drive state**: Factor realizations shock pressure variables (climate stress → water scarcity increases)

2. **State conditions events**: State variables condition event probability (higher water scarcity → higher probability of state failure)

3. **Events shock state**: When events occur, they change state variables (state failure → displaced population increases)

4. **State affects future events**: Changed state conditions future event probability (displaced population → regional instability increases)

This creates proper feedback loops where crises can cascade.

---

## What This Framework Replaced

This integrated framework supersedes earlier proposals:

**Discarded: Opportunity Factors**
Proposal to add factors (F_COOP, F_INNOV) to enable "positive" events. Discarded because:
- "Opportunity" isn't a coherent force like "climate stress"
- Calibration impossible (what is P(high cooperation)?)
- Wrong solution—Type 3 window-resolution structure captures coordination without inventing fictitious factors

**Discarded: Positive/Negative Classification**
Proposal to classify events by valence and model asymmetries. Discarded because:
- Valence is not an event property—events have impact vectors
- "Positive" and "negative" aren't symmetric opposites
- The meaningful distinction is causal type, not valence

**Absorbed: Causal Typology**
The causal type framework (Types 1-4) was developed separately, then integrated as the core organizing principle for probability modeling.

---

## Implications for Event Specification

When specifying an event:

1. **Classify causal type first** — This determines how to model probability
2. **Define the state transition** — What changes when this happens?
3. **Specify type-appropriate probability** — Base rate, pressure function, or window-resolution
4. **Build impact vector** — Multi-dimensional, actor-specific, with durability types
5. **Document cascades** — How does this change probability of other events?

The template and workflow documents implement this framework operationally.

---

## Further Reading

- **[[methodology/reference/causal-types]]** — Detailed type definitions and decision tree
- **[[methodology/reference/durability-types]]** — Complete durability type specifications
- **[[methodology/concepts/state-event-coupling]]** — Technical architecture details
- **[[methodology/concepts/monte-carlo-framework]]** — Full simulation methodology

---

*See [[methodology/00-start-here]] for navigation*