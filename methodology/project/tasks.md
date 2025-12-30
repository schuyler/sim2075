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

### 1.7 Investigate Type 3 Non-Discontinuity Resolutions (🟡 In Progress)

**Issue:** Current Type 3 methodology includes "status quo restoration" and similar resolutions that are explicitly *not* discontinuities. This creates structural inconsistency—the event catalog should enumerate discontinuities, but Type 3 events include non-discontinuity outcomes.

**Solution identified:** India-Pakistan Military Conflict revised as worked example. Event IS the discontinuity, probability is occurrence rate (0.9%), non-discontinuity outcomes are simply non-occurrence.

**Remaining work:**
- Apply same revision to Taiwan Conflict
- Update Type 3 methodology documents ([[methodology/reference/type-3-calibration]], [[methodology/reference/causal-types]])

---

## Upcoming Priorities

### Methodology

| Task | Dependencies | Notes |
|------|--------------|-------|
| **1.6** Establish research documentation standards | — | Define schemas for source documentation, synthesis structure, citation conventions. Events and entities become ongoing research projects; need norms for how research accumulates and traces to parameter choices. Includes templates for Level 1/2/3 deliverables. |

### Critical Reviews

Apply [[methodology/03-critical-review]] to all Level 1 events (24 remaining). Adds "Probability Evolution" (Type 2) and "Case Against" sections.

**Completed:** AMOC Weakening, Chinese Political Crisis, Chinese Economic Crisis (3/27)

**Remaining:**

| Event | Type | Status |
|-------|------|--------|
| Taiwan Conflict | Type 3 | 🔲 |
| Severe Pandemic | Type 1 | 🔲 |
| Global Financial Crisis | Type 1/2 | 🔲 |
| Amazon Tipping Point | Type 2 | 🔲 |
| Permafrost Methane Release | Type 2 | 🔲 |
| Pakistan State Failure | Type 2 | 🔲 |
| Egypt State Failure | Type 2 | 🔲 |
| Russia State Failure | Type 2 | 🔲 |
| Saudi Regime Instability | Type 2 | 🔲 |
| Iran Regime Change | Type 2 | 🔲 |
| Turkey Political Crisis | Type 2 | 🔲 |
| Dollar Reserve Crisis | Type 2 | 🔲 |
| EU Fragmentation | Type 2 | 🔲 |
| US Constitutional Crisis | Type 2/3 | 🔲 |
| India-Pakistan Military Conflict | Type 3 | 🔲 |
| Korean Peninsula Crisis | Type 3 | 🔲 |
| US-China Economic Rupture | Type 3 | 🔲 |
| Oil Supply Shock | Type 1 | 🔲 |
| Iran Nuclear Acquisition | Type 2/3 | 🔲 |
| Fusion Commercialization | Type 1 | 🔲 |
| Agricultural Yield Breakthrough | Type 1 | 🔲 |
| Antimicrobial Platform | Type 1 | 🔲 |
| Sahel Catastrophe | Type 2 | 🔲 |
| Saudi Nuclear Acquisition | Type 3 | 🔲 |

### Validation

| Task | Dependencies | Notes |
|------|--------------|-------|
| **3.1** Compute implied event correlations | 10+ events specified ✓ | Use Σ = ΛΩΛ' + Ψ; verify correlations are sensible |
| **3.2** Check double-counting inflation | 3.1 | Events loading on correlated factors may have inflated correlations |
| **3.3** Historical proxy analysis | Phase 2 complete | Compare factor correlations to observable proxy correlations |
| **3.4** Sensitivity analysis: factor correlations | Phase 2 complete | Test F_CLIM↔F_FOOD, F_GPT↔F_EAS at low/baseline/high |
| **3.5** Audit Type 3 resolution branch completeness | Type 3 events specified ✓ | Ensure favorable branches exist per positive-discontinuity resolution |

### Additional Events

Candidates for expanding beyond 27 current events:

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
| **4.1** Set up prototype directory structure | ⏸️ | Phase 1 complete |
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

## Recently Completed (Last 5)

| Task | Completion Date | Notes |
|------|-----------------|-------|
| Energy Storage Breakthrough critical review | Dec 2025 | 0.8% annual probability; differential impacts on oil exporters |
| Cancer Treatment Breakthrough critical review | Dec 2025 | Platform technology; age-structure sensitive impacts |
| Saudi Nuclear Acquisition critical review | Dec 2025 | Cascade event; 70-85% conditional probability |
| Sahel Catastrophe critical review | Dec 2025 | Regional crisis; factor loadings rescaled |
| Chinese Economic Crisis critical review | Dec 29, 2025 | Pressure function revised to universal variables |

See [[methodology/project/tasks-completed]] for full completion history.

---

## Task Management Protocol

**When adding tasks:**
1. Add to appropriate section
2. Assign priority/dependencies
3. Reference source if from a session

**When completing tasks:**
1. Move to "Recently Completed" (keep last 5)
2. Archive older completions to tasks-completed.md
3. Update dependent tasks
4. Update [[methodology/project/progress-tracker]] if affects event counts
5. Commit changes to Git

---

*Last updated: December 30, 2025*