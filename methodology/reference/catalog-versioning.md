---
title: Catalog Versioning
type: note
permalink: methodology/reference/catalog-versioning
tags:
- methodology
- reference
- catalog
- versioning
- growth
- process
---

# Catalog Versioning & Growth

## How the Catalog Develops Over Time Without Destabilizing the Engine

**Document Version:** 1.0
**Date:** July 2026
**Status:** Adopted policy

**Related documents:**
- [[strategy/roadmap]] — names continuous catalog growth as the post-Phase-1 mode of work
- [[methodology/reference/mvp-dynamics-scope]] — the v0.1 entity/variable axes this policy governs revisions to
- [[methodology/project/implementation-guide]] — the frozen-seam discipline this policy scopes
- [[methodology/concepts/synthetic-variable-problem]] — the admission standard for variables
- [[strategy/emergent-ideas]] — ideas 2, 4, and 7 (CI lint, audit-driven backlog, diff conventions) are mechanized here as release gates and conventions

---

## 1. Purpose

The catalog is designed to grow: richer simulations require more events, more
state variables, and eventually new schema constructs. The engine build, by
contrast, requires stable interfaces. The prior formulation resolved this
tension bluntly — the entity/variable axes were declared a frozen seam,
full stop. That protected the build but left no sanctioned path for the
growth the project plan itself calls for.

This document replaces the blunt freeze with a policy: **three axes of
growth with different costs and different gates, and a release discipline
that makes growth routine rather than exceptional.**

The architectural fact making this possible: `compile_catalog(event_paths,
omega, state_catalog)` already takes the state catalog as an input, and all
tensor shapes derive from compiled index maps. The variable list is data.
Widening it need never touch engine code — provided the engine is built
without hardcoded axis sizes (implementation guide guardrail 7).

---

## 2. The Three Axes of Growth

| Axis | Cost | Gate | Cadence |
|------|------|------|---------|
| **Events** | Low — pure data-layer work under the existing schema | Compiles clean; reasoning documented per the review standard | Continuous authoring; ships in the next catalog release |
| **State variables** | Medium — the cost is the dossier (§3), not code | Dossier complete (mechanical check) | Batched into catalog releases (§4) |
| **Schema constructs** | High — changes the compiler, both engines, and what every future event may express | A Phase 2 instrument shows the omission matters (the v0.2 backlog rule, unchanged) | Rare, versioned schema revisions with migration paths |

The prior formulation bundled axis two with axis three. Unbundled, variable
growth is a data change with a data gate; only axis three retains the full
evidence-gated freeze.

---

## 3. Variable Admission: The Dossier Rule

A variable enters the state catalog when — and mechanically, whenever — it
carries a complete dossier:

1. **Measurement procedure and data source.** Observable, per
   [[methodology/concepts/synthetic-variable-problem]]. No synthetic indices.
2. **Dynamics classification with parameters.** Which class from
   [[methodology/reference/state-dynamics]] (drift, mean-reverting,
   event-driven, regime-dependent) and the parameters that class requires.
3. **Sourced initial conditions** for every entity that tracks it (2025
   baseline with source tag, per the Task 4.3 standard).
4. **At least one consumer:** an event impact row, an expression
   (`pressure:`/`preconditions:`/`if:`), or a transmission channel that
   reads or shocks it. A variable nothing consumes is dead weight — false
   verisimilitude at real elicitation cost.

The dossier replaces stop-and-report governance for variables: admission is
a completeness check, not an escalation. What remains a human decision is
*prioritization* — which dossiers are worth assembling (§5).

---

## 4. Release Discipline

The catalog — event set, variable catalog, initial conditions, dynamics
defaults — is versioned as a unit. **Catalog v1.0 is whatever ships with
engine v0.1.** Growth lands in batched releases (v1.1, v1.2, …), never by
continuous drip into the contract. Three reasons:

1. **Comparability.** Monte Carlo results are only comparable within a
   catalog version. Every `RunOutputs` carries the catalog version stamp;
   cross-version comparisons are themselves informative ("the 2050 tail
   fattened because the v1.2 Sahel batch, not noise") but must be labeled.
2. **Coherence.** Variables land in the same release as the events that
   consume them — the dossier's consumer requirement is checkable only at
   release granularity.
3. **Elicitation budget.** Every event costs O(k) documented judgments.
   Batching forces the question "which additions does this release buy, and
   why these" instead of growth by recency of interest.

### Release gates (mechanical, CI-enforced once Phase 1 item 5 lands)

- Every event compiles; schema-validates; reasoning attached to every
  parameter change (the standing review standard).
- **No dangling references, either direction:** every impact row and
  expression targets an existing variable; every cascade-list event ID
  exists in the catalog or in the backlog registry
  ([[strategy/emergent-ideas]] idea 2); every variable has a consumer.
- Every new variable's dossier is complete (§3).
- A release changelog states what was added and why, with commit
  conventions per [[strategy/emergent-ideas]] idea 7 (audit-driven /
  world-event-driven / elicitation-driven).
- The release is git-tagged (pre-registration, per
  [[strategy/emergent-ideas]] idea 3).

---

## 5. What Drives Growth: The Demand Signal

Growth is prioritized by demonstrated model deficiency, not encyclopedic
completeness:

- **Backlog registry.** Event IDs named in cascade lists but absent from
  the catalog (the line-373 rule), plus unattributable complaints from the
  Phase 2 audit harness ("this path needed an event the model doesn't
  have" — [[strategy/emergent-ideas]] idea 4).
- **Sensitivity analysis.** An addition loading only on factors that drive
  no tail outcomes is wasted elicitation; the tornado results rank where
  new structure could matter.
- **World events.** The Third Gulf War is the precedent: a live event that
  exposes missing structure feeds the next release directly (the Phase 0
  war events and variable classes are exactly this).

The pre-instrument seed batch — the Phase 0 war events, the deduplicated
cascade-audit set, and the war-mandated variable classes — needs no
instrument evidence: the war already served as the instrument.

---

## 6. Relationship to the Frozen Seams

This policy scopes, rather than repeals, the implementation guide's freeze:

- **During the v0.1 engine build** (E0 through E10), the entity/variable
  axes stay pinned to [[methodology/reference/mvp-dynamics-scope]] exactly
  as the guide states. Agents building engine stages still stop and report
  rather than widen anything mid-build. Parallel construction against
  moving interfaces is the failure mode the freeze exists to prevent, and
  it remains in force there.
- **The sanctioned widening moments are two:** (a) a one-time revision of
  the MVP scope *before E0 starts* — the cheapest moment such a revision
  will ever have, absorbing the variables that current-plus-Phase-0 events
  already need (roadmap Phase 0 item 3 / Task 6.7); and (b) versioned
  catalog releases *after E10*, which under guardrail 7 are data changes,
  not engine changes.
- **Schema constructs keep the unmodified v0.2 evidence gate.** Nothing
  here loosens it.

"Frozen" continues to mean what it has always meant here: not immutable,
but *changed only as a versioned, deliberate event with an owner* — never
as a side effect of authoring.

---

*This policy governs how the catalog grows. For what the catalog currently
contains, see [[index]]. For the v0.1 axes it versions, see
[[methodology/reference/mvp-dynamics-scope]].*
