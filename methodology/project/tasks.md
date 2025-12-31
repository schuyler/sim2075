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

**Next: Phase 2 (Prototype Implementation)**

---

## Upcoming Priorities

### Methodology

| Task | Dependencies | Notes |
|------|--------------|-------|
| **1.6** Establish research documentation standards | — | Define schemas for source documentation, synthesis structure, citation conventions. Events and entities become ongoing research projects; need norms for how research accumulates and traces to parameter choices. Includes templates for Level 1/2/3 deliverables. |

### Validation

| Task | Dependencies | Notes |
|------|--------------|-------|
| **3.3** Historical proxy analysis | Phase 2 complete | 🟡 **Deferred** — Requires observable proxy data |
| **3.4** Sensitivity analysis: factor correlations | Phase 2 complete | ⏸️ Blocked on prototype |
| **3.5** Audit Type 3 resolution branch completeness | — | Ensure favorable branches exist per positive-discontinuity resolution |

### Cleanup Tasks

| Task | Description | Priority | Status |
|------|-------------|----------|--------|
| **3.15** | **Vestigial Type 4**: Evaluate whether Type 4 variance targets are needed—we classified Type 4 as "not events, move to baseline." If no Type 4 events exist, remove from framework. | Low | 🔲 Deferred |
| **3.16** | **Validation notes cleanup**: Delete stale validation working documents (validation-event-correlations, validation-findings-report, validation-correlation-matrix-data). Essential findings captured in [[methodology/reference/variance-allocation]]. | Low | 🔲 |

### Additional Events

Candidates for expanding beyond 29 current events:

| Event | Type | Source | Notes |
|-------|------|--------|-------|
| Coastal West Africa Destabilization | Type 2 | Cascade from Sahel | Ghana, Côte d'Ivoire, Benin vulnerability |
| Nigeria Northern Crisis | Type 2 | Regional coverage | Boko Haram, climate stress, demographic pressure |
| Turkey Nuclear Reconsideration | Type 3 | Cascade from Iran | NATO member response to regional proliferation |
| Egypt Nuclear Reconsideration | Type 3 | Cascade from Saudi | Regional proliferation response |

---

## Blocked / Future Work

### Implementation (Phase 2)

Build simulation prototype. See [[methodology/project/development-roadmap]] for detailed architecture.

| Task | Status | Dependencies |
|------|--------|--------------|
| **4.1** Set up prototype directory structure | ⏸️ | Phase 1 complete ✓ |
| **4.2** Implement state vector management | ⏸️ | 4.1 |
| **4.3** Implement factor sampling with correlations | ⏸️ | 4.1 |
| **4.4** Implement event firing logic | ⏸️ | 4.3 |
| **4.5** Implement impact transmission | ⏸️ | 4.2, 4.4 |
| **4.6** Implement aftermath tracking | ⏸️ | 4.5 |
| **4.7** Implement baseline dynamics | ⏸️ | 4.2 |
| **4.8** Implement main simulation loop | ⏸️ | 4.3-4.7 |
| **4.9** Implement output analysis | ⏸️ | 4.8 |
| **4.10** Create prototype run notebook | ⏸️ | 4.8, 4.9 |
| **4.11** Validate prototype produces sensible output | ⏸️ | 4.10 |

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

*Last updated: December 31, 2025 — Phase 1 complete*