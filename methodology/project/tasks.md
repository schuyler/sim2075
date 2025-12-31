---
title: tasks
type: note
permalink: methodology/project/tasks
tags:
- methodology
- project
- tasks
- backlog
- development
- tracking
---

# Development Tasks

Actionable development tasks for Sim2075. Completed tasks archived in [[methodology/project/tasks-completed]].

**Status markers:**
- 🔲 Not started
- 🟡 In progress
- ⏸️ Blocked

---

## Active Work

**Phase 1 Complete** — All Level 1 event specifications, critical reviews, and variance allocation finished (Dec 31, 2025).

**Next: Pre-Implementation Preparation (Section 4)**

Start with **Task 4.1** (prototype scope decision) to determine sequencing of remaining preparation tasks. Key decision: dynamics-free v0.1 vs. parameterization sprint.

---

## Upcoming Priorities

### Pre-Implementation Preparation (Section 4)

Tasks required before or alongside Phase 2 implementation. See analysis in session 2025-12-31.

| Task | Description | Dependencies | Status |
|------|-------------|--------------|--------|
| **4.1** | **Prototype scope decision**: Decide between (A) dynamics-free v0.1 that validates factor sampling and event firing, or (B) parameterization sprint before implementation. Document decision and rationale. | — | 🔲 |
| **4.2** | **Event catalog compilation**: Extract 28 event specifications from markdown to machine-readable format (JSON/YAML). Include probabilities, factor loadings, impact vectors, cascade effects. | — | 🔲 |
| **4.3** | **Initial conditions document**: Gather 2025 baseline values for prototype scope (15 countries × ~18 variables + ~22 global = ~300 values). Document sources. Placeholder values acceptable for v0.1. | 4.1 | 🔲 |
| **4.4** | **Dynamics parameterization**: Specify parameters from [[methodology/reference/state-dynamics]] §10: country-specific equilibria, reversion speeds, tipping thresholds, policy reaction coefficients. Can use simplified defaults for v0.1. | 4.1, 4.3 | 🔲 |

### Methodology

| Task | Dependencies | Notes |
|------|--------------|-------|
| **1.6** Establish research documentation standards | — | Define schemas for source documentation, synthesis structure, citation conventions. Events and entities become ongoing research projects; need norms for how research accumulates and traces to parameter choices. Includes templates for Level 1/2/3 deliverables. |

### Validation

| Task | Dependencies | Notes |
|------|--------------|-------|
| **3.5** Audit Type 3 resolution branch completeness | — | 🔲 Ensure favorable branches exist per positive-discontinuity resolution. **Elevated priority** — affects specification quality before implementation. |
| **3.3** Historical proxy analysis | Phase 2 complete | 🟡 **Deferred** — Requires observable proxy data |
| **3.4** Sensitivity analysis: factor correlations | Phase 2 complete | ⏸️ Blocked on prototype |

### Cleanup Tasks

| Task | Description | Priority | Status |
|------|-------------|----------|--------|
| **3.15** | **Vestigial Type 4**: Evaluate whether Type 4 variance targets are needed—we classified Type 4 as "not events, move to baseline." If no Type 4 events exist, remove from framework. | Low | 🔲 Deferred |
| **3.16** | **Validation notes cleanup**: Deleted stale validation working documents. Essential findings captured in [[methodology/reference/variance-allocation]]. | Low | ✅ |

### Additional Events

Candidates for expanding beyond 28 current events:

| Event | Type | Source | Notes |
|-------|------|--------|-------|
| Coastal West Africa Destabilization | Type 2 | Cascade from Sahel | Ghana, Côte d'Ivoire, Benin vulnerability |
| Nigeria Northern Crisis | Type 2 | Regional coverage | Boko Haram, climate stress, demographic pressure |
| Turkey Nuclear Reconsideration | Type 3 | Cascade from Iran | NATO member response to regional proliferation |
| Egypt Nuclear Reconsideration | Type 3 | Cascade from Saudi | Regional proliferation response |

---

## Blocked / Future Work

### Implementation (Phase 2 — Section 5)

Build simulation prototype. See [[methodology/project/development-roadmap]] for detailed architecture.

| Task | Description | Status | Dependencies |
|------|-------------|--------|--------------|
| **5.1** | Set up prototype directory structure | ⏸️ | 4.1 decision |
| **5.2** | Implement state vector management | ⏸️ | 5.1, 4.3 |
| **5.3** | Implement factor sampling with correlations | ⏸️ | 5.1 |
| **5.4** | Implement event firing logic | ⏸️ | 5.3, 4.2 |
| **5.5** | Implement impact transmission | ⏸️ | 5.2, 5.4 |
| **5.6** | Implement aftermath tracking | ⏸️ | 5.5 |
| **5.7** | Implement baseline dynamics | ⏸️ | 5.2, 4.4 |
| **5.8** | Implement main simulation loop | ⏸️ | 5.3–5.7 |
| **5.9** | Implement output analysis | ⏸️ | 5.8 |
| **5.10** | Create prototype run notebook | ⏸️ | 5.8, 5.9 |
| **5.11** | Validate prototype produces sensible output | ⏸️ | 5.10 |

**Note:** If Task 4.1 chooses dynamics-free v0.1 (Option A), tasks 5.7 and 4.4 are deferred. Core loop (5.3–5.6, 5.8) can proceed with 4.2 and 4.3 only.

### Phase 3+ (Sensitivity-Driven)

Tasks prioritized after sensitivity analysis reveals what matters:

| Task | Trigger |
|------|---------|
| Multi-branch aftermath refinement | Sensitivity shows aftermath type affects tail outcomes |
| Entity expansion (additional countries) | Sensitivity shows regional dynamics matter |
| Variable expansion | Sensitivity shows unmodeled mechanisms matter |
| Dynamics refinement | Sensitivity shows dynamics parameters are important |
| Level 2/3 research for high-impact events | Sensitivity identifies events driving tail outcomes |

---

## Task Management Protocol

**When adding tasks:**
1. Add to appropriate section
2. Assign priority/dependencies
3. Reference source if from a session

**When completing tasks:**
1. Archive to [[methodology/project/tasks-completed]]
2. Update dependent tasks
3. Update [[methodology/project/progress-tracker]] if affects event counts
4. Commit changes to Git

---

*Last updated: December 31, 2025 — Pre-implementation preparation tasks added (Section 4); Implementation renumbered to Section 5*