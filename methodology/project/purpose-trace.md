---
title: purpose-trace
type: note
permalink: methodology/project/purpose-trace
tags:
- methodology
- project
- purpose
- validation
- v0.1
---

# Purpose Trace

**Date:** 2026-10-23
**Status:** Standing check: re-run whenever scope is cut, and before E10

Every other check in this project runs *downward*: event file to compiled catalog, spec to reference engine,
reference engine to vectorized engine. Nothing ran *upward*, from what the project is for to the mechanisms
that would have to carry it. So when MVP Dynamics Scope §5.1's pseudocode omitted the population step, the
omission passed through the implementation guide and eight engine stages unnoticed. Demographic transition is
half of the founding thesis, and the project began with a question about Chinese demographic shifts
(sim/README.md §4 item 22).

This document is the upward check. For each claim the model exists to explore, it traces the chain a claim
needs in order to show up in output:

> **state variables** that represent it → **between events**, what moves them (dynamics) → **at events**,
> what moves them (impact rows) → **feedback**, what reads them back into the model (event probability
> expressions, cascade conditions, dynamics or transmission rules) → **outputs** that would display it

Each link is marked *specified* (a document states it), *parameterized* (numbers exist), *scheduled* (a build
stage or task carries it) and *built*. A claim is only as strong as its weakest link.

**Rules.**
1. A scope cut that breaks a link of P0 or of the core claims P1–P5 needs the project owner's explicit sign-off,
   recorded here (see [[methodology/00-start-here]]).
2. Re-run the trace when scope is cut and before E10. The mechanical part is the query under "Method".
3. E10 gate: every row below is either *carried* or carries an owner-signed entry saying why not.

## The claims

From [[methodology/00-start-here]] §"Purpose and Decision Context":

- **P0. The founding question.** "What will Chinese demographic shifts do to its geopolitical strategy?"
- **P1.** The 21st century is shaped by the *interaction* of demographic transition and climate change.
- **P2.** Below-replacement fertility will reshape economic and political capacity everywhere.
- **P3.** Emissions are unlikely to fall fast enough to avoid severe climate impacts in vulnerable regions.
- **P4.** Wealthy nations will largely enforce borders rather than absorb climate migration at scale.
- **P5.** The result is a century of divergence: some regions adapt and stay stable, others face compounding
  crises.
- **P6.** Financial fragility compounds political instability; regional crises cascade or remain contained.

## Trace (2026-10-23, at E8)

<!-- TRACE-TABLE -->

## Cross-cutting findings

<!-- FINDINGS -->

## Method

The mechanical part of the trace is a query over the compiled full catalog, run from the repository root.
It finds which names event expressions read, which variables impact rows move, and which read variables
nothing moves:

```python
import pathlib
from sim.catalog.cli import load_state_catalog, load_omega, extract_all, compile_event_records
sc = load_state_catalog(); _, om = load_omega(factors=sc.factors)
recs, known, _ = extract_all(pathlib.Path("events"))
cat = compile_event_records(recs, om, sc, known_event_ids=known, strict_cascades=True)
# names read: cat.type2[e].pressure.names; cat.type3[e].preconditions / .sustained; cascade_edges[i].cond.names
# variables moved at events: cat.impact_table (entity_idx, var_idx); between events: the DynamicsSpec (D4)
```

The rest is reading. For each claim, find the documents that specify each link and the stage that builds it.

## History

| Date | Change |
|------|--------|
| 2026-10-23 | First trace, at E8, after population dynamics were found to be specified for v0.1 but scheduled nowhere |
