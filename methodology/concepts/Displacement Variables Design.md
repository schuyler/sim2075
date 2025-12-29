---
title: Displacement Variables Design
type: note
permalink: methodology/concepts/displacement-variables-design
tags:
- methodology
- concepts
- state-variables
- displacement
- refugees
- idp
- design
- pending
---

# Displacement Variables Design

**Status:** Design note — pending implementation in state variable catalog  
**Date:** December 2025  
**Triggered by:** Sahel Catastrophe event specification used displacement variables that don't exist in current state model

---

## Problem Statement

The [[events/geopolitical/sahel-catastrophe]] specification referenced `displaced_population` as a pressure function input and impact vector output. Review revealed this variable doesn't exist in [[methodology/reference/state-variables-country]].

Displacement is analytically important for:
- Type 2 pressure functions (rising displacement signals crisis severity)
- Impact vectors (crises generate displacement)
- Cascade effects (refugees burden host countries)
- Humanitarian catastrophe modeling generally

---

## Conceptual Analysis

"Displaced population" conflates three distinct concepts with different locations and policy implications:

| Concept | Description | Physical Location |
|---------|-------------|-------------------|
| **IDPs** | Internally displaced persons — fled their homes but remain in-country | IN origin country |
| **Refugees abroad** | Persons who fled this country and are now in other countries | NOT in origin country |
| **Refugees hosted** | Refugees from other countries hosted here | IN host country |

A naive single variable `displaced_population = IDPs + refugees abroad` mixes stocks in different locations, which creates confusion when modeling impacts.

---

## Proposed Solution: Three Variables

Add to [[methodology/reference/state-variables-country]] under Demographic Flows:

| Variable ID | Description | Units | Data Source |
|-------------|-------------|-------|-------------|
| `idp_population` | Internally displaced persons | Millions | IDMC |
| `refugees_abroad` | Refugees from this country living in other countries | Millions | UNHCR |
| `refugees_hosted` | Refugees from other countries hosted here | Millions | UNHCR |

### Derived Measures (Computed, Not Stored)

| Measure | Formula | Meaning |
|---------|---------|---------|
| `displaced_present` | `idp_population` + `refugees_hosted` | Total displaced persons physically IN this country (burden measure) |
| `displacement_caused` | `idp_population` + `refugees_abroad` | Total displacement originating FROM this country's crisis (severity measure) |

### Dynamics

| Variable | Dynamics | Parameters |
|----------|----------|------------|
| `idp_population` | Event-driven increase; slow decay | half-life ~10-15 years; conflict resolution enables return |
| `refugees_abroad` | Event-driven increase; very slow decay | half-life ~15-20 years; repatriation is slow |
| `refugees_hosted` | Driven by neighboring country crises; policy-dependent | responds to `refugees_abroad` in neighbors |

### Conservation Principle

When refugees flee Country A to Country B:
- Country A: `refugees_abroad` ↑
- Country B: `refugees_hosted` ↑

The simulation should model this as a transfer, maintaining global consistency.

---

## Application to Events

### Sahel Catastrophe

**Pressure function** should use `idp_population`:
- Rising IDPs indicate crisis severity before mass exodus
- More directly observable than cross-border flows

**Sahel impact vector** should increase:
- `sahel.idp_population` (immediate)
- `sahel.refugees_abroad` (as crisis deepens)

**Coastal state impact vector** should increase:
- `ghana.refugees_hosted`, `cote_divoire.refugees_hosted`, etc.

### Other Humanitarian Events

Similar logic applies to Pakistan State Failure, Egypt State Failure, and any conflict or collapse event. The three-variable structure enables:
- Tracking crisis severity via origin-country displacement
- Modeling host-country burden via refugees hosted
- Cascade effects as refugee burden destabilizes hosts

---

## Implementation Notes

1. **Category placement:** Demographic Flows in state-variables-country
2. **Tier 2 aggregates:** Should track at least `idp_population` for crisis monitoring
3. **Baseline values:** Initialize from UNHCR/IDMC 2025 data
4. **Regional aggregates:** Sum of component country values

---

## Pending Actions

- [ ] Add three variables to [[methodology/reference/state-variables-country]]
- [ ] Update [[events/geopolitical/sahel-catastrophe]] pressure function and impact vector
- [ ] Review other humanitarian events for displacement variable usage
- [ ] Define transmission mechanism for refugee flows between countries

---

*See [[methodology/concepts/synthetic-variable-problem]] for related discussion of observable vs. synthetic variables.*