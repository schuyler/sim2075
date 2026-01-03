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

Key insight driving Section 4: **progress is continuous, catastrophe is discontinuous**. Without baseline dynamics capturing gradual improvement (GDP growth, life expectancy gains, technology cost declines), the simulation produces only decline. The "progress engine" is essential, not optional.

Start with **Task 4.1** to document MVP dynamics scope, then proceed with parallel work on 4.2 (event extraction) and 4.3 (initial conditions).
## Upcoming Priorities

### Pre-Implementation Preparation (Section 4)

Tasks required before Phase 2 implementation. Revised Dec 31, 2025 to reflect "minimum viable dynamics" approach.

**Tier structure:**
- **Tier 1 (Essential):** Parameters that carry the positive side of the ledger — baseline growth, life expectancy trends, technology costs
- **Tier 2 (Defaults):** Mean-reversion parameters using literature defaults — half-lives, volatilities
- **Tier 3 (Deferred):** Complex transmission, country-specific calibration — addressed post-sensitivity analysis

| Task | Description | Dependencies | Status |
|------|-------------|--------------|--------|
| **4.2** | **Event specification migration** (6/29): See detailed instructions below. | — | 🟡 |
| **4.3** | **Initial conditions + baseline trends**: The "progress engine." Gather 2025 baselines and trend rates for: GDP per capita (46 entities), life expectancy (46 entities), technology costs (global), climate trajectories (global). Single-source from IMF WEO, UN Population. ~200 parameters. | — | 🔲 |
| **4.4** | **Dynamics defaults**: Specify default parameters for mean-reverting variables. Equilibria from 4.3 baselines. Default half-lives (~2 years economic, ~1 year financial). Placeholder volatilities. Document simplifications explicitly. | 4.3 | 🔲 |

**Dependency graph:**
```
4.2 Event Catalog (ready to start)
4.3 Initial Conditions + Trends (ready to start)
 └── 4.4 Dynamics Defaults
```

#### Task 4.2 Detailed Instructions

**Objective**: Convert event specification **tables** to embedded **YAML blocks** while **preserving all prose**.

**Reference documents**:
- Schema: [[methodology/reference/event-yaml-schema]]
- Template: [[methodology/02-event-template]]
- Worked example: [[events/geopolitical/taiwan-conflict]]

**What to convert (tables → YAML)**:
- Classification table → `specification:` block
- Probability table → `probability:` block
- Pressure function table (Type 2) → `pressure:` expression in probability block
- Preconditions table (Type 3) → `preconditions:` in probability block
- Factor loadings table → `factors:` block
- Severity/resolution branches table → `branches:` or `resolutions:` block
- Impact tables → `impacts:` block (keyed by branch)
- Cascade tables → `cascades:` block
- Research status table → `research:` block

**What to preserve (all prose)**:
- Description and "what marks occurrence"
- Causal type rationale ("Why Type N?")
- Base rate derivation and calculation walkthrough
- Condition adjustments with rationales
- Probability evolution discussion
- Case Against section with counterarguments
- Key uncertainties
- Threshold specification rationale and historical calibration
- Branch probability rationale
- Impact derivation methodology
- Transmission channel explanations
- Cascade pathway diagrams and explanations
- Durability rationale
- Historical analogues
- Comparative ranking
- Sources
- Open questions

**Validation requirements**:
1. **Factors**: Every factor ID in `factors:` block must exist in [[factors/]] catalog (e.g., `F_GPT`, `F_SAS`)
2. **Events**: Every event ID in `cascades:` block must exist in [[events/]] catalog (e.g., `TAIWAN_CONFLICT`, `SEVERE_PANDEMIC`)
3. **State variables**: Every variable in `probability.pressure`, `probability.preconditions`, and `impacts:` must exist in [[methodology/reference/state-variables-global]] or [[methodology/reference/state-variables-country]] using correct entity.variable syntax
4. **Probabilities**: Resolution probabilities sum to 1.0; branch probabilities within each resolution sum to 1.0
5. **Variance**: Factor loadings should achieve type-appropriate variance target (Type 1: 0.75, Type 2: 0.65, Type 3: 0.45)

**Process per event**:
1. Read current specification
2. **Review git history** for this event file to understand all changes made since creation; ensure no important prose has been lost in prior edits
3. Identify all tables to convert
4. Convert tables to YAML per schema
5. Verify all prose sections remain intact (compare against git history if uncertain)
6. Validate factor/event/variable references against catalogs
7. Add changelog entry
8. Commit atomically

#### Task 4.2 Event Subtasks

**Climate Events**:
| Subtask | Event | Status |
|---------|-------|--------|
| 4.2.1 | [[events/climate/amoc-weakening]] | ⚠️ Needs remediation |
| 4.2.2 | [[events/climate/amazon-tipping-point]] | 🔲 |
| 4.2.3 | [[events/climate/permafrost-methane-release]] | 🔲 |

**Geopolitical Events**:
| Subtask | Event | Status |
|---------|-------|--------|
| 4.2.4 | [[events/geopolitical/taiwan-conflict]] | ✅ |
| 4.2.5 | [[events/geopolitical/pakistan-state-failure]] | ⚠️ Needs remediation |
| 4.2.6 | [[events/geopolitical/egypt-state-failure]] | 🔲 |
| 4.2.7 | [[events/geopolitical/russia-state-failure]] | 🔲 |
| 4.2.8 | [[events/geopolitical/saudi-regime-instability]] | 🔲 |
| 4.2.9 | [[events/geopolitical/iran-regime-change]] | 🔲 |
| 4.2.10 | [[events/geopolitical/turkey-political-breakdown]] | 🔲 |
| 4.2.11 | [[events/geopolitical/chinese-political-crisis]] | 🔲 |
| 4.2.12 | [[events/geopolitical/eu-fragmentation]] | 🔲 |
| 4.2.13 | [[events/geopolitical/india-pakistan-military-conflict]] | 🔲 |
| 4.2.14 | [[events/geopolitical/korean-peninsula-crisis]] | 🔲 |
| 4.2.15 | [[events/geopolitical/us-china-economic-rupture]] | 🔲 |
| 4.2.16 | [[events/geopolitical/iran-nuclear-acquisition]] | 🔲 |
| 4.2.17 | [[events/geopolitical/sahel-catastrophe]] | 🔲 |
| 4.2.18 | [[events/geopolitical/saudi-nuclear-acquisition]] | 🔲 |
| 4.2.19 | [[events/geopolitical/us-constitutional-crisis]] | 🔲 |

**Financial Events**:
| Subtask | Event | Status |
|---------|-------|--------|
| 4.2.20 | [[events/financial/global-financial-crisis]] | 🔲 |
| 4.2.21 | [[events/financial/dollar-reserve-crisis]] | 🔲 |
| 4.2.22 | [[events/financial/chinese-economic-crisis]] | 🔲 |

**Health Events**:
| Subtask | Event | Status |
|---------|-------|--------|
| 4.2.23 | [[events/health/severe-pandemic]] | ⚠️ Needs remediation |

**Energy Events**:
| Subtask | Event | Status |
|---------|-------|--------|
| 4.2.24 | [[events/energy/oil-supply-shock]] | 🔲 |

**Breakthrough Events**:
| Subtask | Event | Status |
|---------|-------|--------|
| 4.2.25 | [[events/breakthrough/fusion-commercialization]] | ⚠️ Needs remediation |
| 4.2.26 | [[events/breakthrough/agricultural-yield-breakthrough]] | 🔲 |
| 4.2.27 | [[events/breakthrough/cancer-treatment-breakthrough]] | 🔲 |
| 4.2.28 | [[events/breakthrough/antimicrobial-platform]] | 🔲 |
| 4.2.29 | [[events/breakthrough/energy-storage-breakthrough]] | 🔲 |

**Status key**: ✅ Complete | ⚠️ Needs remediation (prose lost) | 🟡 In progress | 🔲 Not started

**Progress**: 1/29 complete, 4/29 need remediation, 24/29 not started

**Completed:** Tasks 4.1, 4.5 — see [[methodology/project/tasks-completed]]

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

Candidates for expanding beyond 29 current events:

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

**Note:** Section 4 uses "minimum viable dynamics" approach — baseline drift (progress engine) is essential; mean-reversion uses defaults; complex transmission is deferred. All Section 5 tasks proceed with this scope.

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

*Last updated: January 3, 2026 — Task 4.2 detailed instructions added; noted early migrations require prose remediation*