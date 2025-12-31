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
| **4.1** | **MVP dynamics scope**: Document minimum viable dynamics framework. Define three tiers (Essential/Defaults/Deferred). List parameters per tier. Document simplifications. Create [[methodology/reference/mvp-dynamics-scope]]. | — | 🔲 |
| **4.2** | **Event catalog compilation**: Extract 29 event specifications to machine-readable format (YAML). Include probabilities, factor loadings (raw + scaled), resolution branches, impact vectors, cascade triggers. | — | 🔲 |
| **4.3** | **Initial conditions + baseline trends**: The "progress engine." Gather 2025 baselines and trend rates for: GDP per capita (40 countries), life expectancy (40 countries), technology costs (global), climate trajectories (global). Single-source from IMF WEO, UN Population. ~100 parameters. | 4.1 | 🔲 |
| **4.4** | **Dynamics defaults**: Specify default parameters for mean-reverting variables. Equilibria from 4.3 baselines. Default half-lives (~2 years economic, ~1 year financial). Placeholder volatilities. Document simplifications explicitly. | 4.1, 4.3 | 🔲 |
| **4.5** | **Transmission simplifications**: Document v0.1 transmission scope. Include: oil→inflation, food→inflation (single global passthrough scaled by import dependence). Defer: financial contagion, trade transmission, climate damage functions, policy reaction functions. | 4.1 | 🔲 |

**Dependency graph:**
```
4.1 MVP Dynamics Scope
 ├── 4.2 Event Catalog (parallel, no dependency)
 ├── 4.3 Initial Conditions + Trends
 │    └── 4.4 Dynamics Defaults
 └── 4.5 Transmission Simplifications
```

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

*Last updated: December 31, 2025 — Task 4 series revised to "minimum viable dynamics" approach; added Task 4.5 (transmission simplifications)*