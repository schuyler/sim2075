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

**Variance allocation framework complete** (Tasks 3.6-3.10).

**Next**: Task 3.11 — Implement variance allocation across all 28 events.

This involves:
1. Determine causal type for each event
2. Compute current (ΛΩΛᵀ)ᵢᵢ
3. Compute scale factor: √(target / current)
4. Update event files with scaled loadings
5. Re-run validation
6. Document in changelogs

---

## Recently Completed

| Task | Completion Date | Notes |
|------|-----------------|-------|
| **1.7** Type 3 non-discontinuity resolutions | Dec 30, 2025 | Resolved structural inconsistency: resolutions are discontinuity types, not all possible outcomes. Updated type-3-calibration.md and causal-types.md. India-Pakistan is primary example. |
| Energy Storage Breakthrough critical review | Dec 2025 | 0.8% annual probability; differential impacts on oil exporters |
| Cancer Treatment Breakthrough critical review | Dec 2025 | Platform technology; age-structure sensitive impacts |
| Saudi Nuclear Acquisition critical review | Dec 2025 | Cascade event; 70-85% conditional probability |
| Sahel Catastrophe critical review | Dec 2025 | Regional crisis; factor loadings rescaled |

See [[methodology/project/tasks-completed]] for full completion history.

---

## Upcoming Priorities

### Methodology

| Task | Dependencies | Notes |
|------|--------------|-------|
| **1.6** Establish research documentation standards | — | Define schemas for source documentation, synthesis structure, citation conventions. Events and entities become ongoing research projects; need norms for how research accumulates and traces to parameter choices. Includes templates for Level 1/2/3 deliverables. |

### Critical Reviews

Apply [[methodology/03-critical-review]] to all Level 1 events (24 remaining). Adds "Probability Evolution" (Type 2) and "Case Against" sections.

**Completed:** 2.4.1 (AMOC), 2.4.2 (Chinese Political), 2.4.15 (Chinese Economic) — 3/27

**Remaining:**

| Task | Event | Type | Status |
|------|-------|------|--------|
| **2.4.3** | Taiwan Conflict | Type 3 | 🔲 |
| **2.4.4** | Severe Pandemic | Type 1 | 🔲 |
| **2.4.5** | Global Financial Crisis | Type 1/2 | 🔲 |
| **2.4.6** | Amazon Tipping Point | Type 2 | 🔲 |
| **2.4.7** | Permafrost Methane Release | Type 2 | 🔲 |
| **2.4.8** | Pakistan State Failure | Type 2 | 🔲 |
| **2.4.9** | Egypt State Failure | Type 2 | 🔲 |
| **2.4.10** | Russia State Failure | Type 2 | 🔲 |
| **2.4.11** | Saudi Regime Instability | Type 2 | 🔲 |
| **2.4.12** | Iran Regime Change | Type 2 | 🔲 |
| **2.4.13** | Turkey Political Crisis | Type 2 | 🔲 |
| **2.4.14** | Dollar Reserve Crisis | Type 2 | 🔲 |
| **2.4.16** | EU Fragmentation | Type 2 | 🔲 |
| **2.4.17** | US Constitutional Crisis | Type 2/3 | 🔲 |
| **2.4.18** | India-Pakistan Military Conflict | Type 3 | 🔲 |
| **2.4.19** | Korean Peninsula Crisis | Type 3 | 🔲 |
| **2.4.20** | US-China Economic Rupture | Type 3 | 🔲 |
| **2.4.21** | Oil Supply Shock | Type 1 | 🔲 |
| **2.4.22** | Iran Nuclear Acquisition | Type 2/3 | 🔲 |
| **2.4.23** | Fusion Commercialization | Type 1 | 🔲 |
| **2.4.24** | Agricultural Yield Breakthrough | Type 1 | 🔲 |
| **2.4.25** | Antimicrobial Platform | Type 1 | 🔲 |
| **2.4.26** | Sahel Catastrophe | Type 2 | 🔲 |
| **2.4.27** | Saudi Nuclear Acquisition | Type 3 | 🔲 |

### Validation

| Task | Dependencies | Notes |
|------|--------------|-------|
| **3.1** Compute implied event correlations | 10+ events specified ✓ | ✅ **COMPLETE** — See [[methodology/project/validation-event-correlations]]. Found significant issues: correlations up to 0.98 between event pairs. |
| **3.2** Check double-counting inflation | 3.1 | ✅ **COMPLETE** — Confirmed double-counting through shared factors + correlated factor paths. Climate events (ρ=0.93-0.98), financial events (ρ=0.96-0.98) form near-redundant clusters. |
| **3.3** Historical proxy analysis | Phase 2 complete | 🟡 **Deferred** — Requires observable proxy data; partially addressed in validation |
| **3.4** Sensitivity analysis: factor correlations | Phase 2 complete | ⏸️ Blocked on resolution of 3.1/3.2 findings |
| **3.5** Audit Type 3 resolution branch completeness | Type 3 events specified ✓ | Ensure favorable branches exist per positive-discontinuity resolution |

**⚠️ Validation Issue Summary (Updated Dec 30)**: Tasks 3.1-3.2 revealed a fundamental misspecification:

**Problem**: When factors are correlated, the true factor-explained variance is (ΛΩΛᵀ)ᵢᵢ, not simple Σⱼλᵢⱼ². The cross-terms from factor correlations inflate variance. Result: **8 of 11 analyzed events exceed unit variance**:

| Event | True (ΛΩΛᵀ)ᵢᵢ | Status |
|-------|--------------|--------|
| Taiwan Conflict | 2.04 | Severe |
| Pakistan State Failure | 1.74 | Severe |
| Global Financial Crisis | 1.48 | Severe |
| Dollar Reserve Crisis | 1.39 | Severe |
| Chinese Economic Crisis | 1.20 | Violation |
| Amazon Tipping Point | 1.11 | Violation |
| Oil Supply Shock | 1.07 | Violation |
| AMOC Weakening | 1.05 | Violation |

**Solution**: Variance allocation framework based on causal type epistemology. Key insight: idiosyncratic variance should reflect what factors *can* explain for each event type:

- **Type 1** (Stochastic): Large-N averaging → factors explain most variance (target ~0.70-0.80)
- **Type 2** (Threshold): Observable pressure, uncertain threshold → moderate-high (target ~0.60-0.70)
- **Type 3** (Contingent): Factors explain windows, resolution intractable → moderate-low (target ~0.40-0.50)
- **Type 4** (Breakthrough): Partly structural, partly serendipitous → moderate (target ~0.50-0.60)

This means Type 3 events (Taiwan, India-Pakistan) get scaled down more than Type 2 events (AMOC, Pakistan)—which is epistemically correct.

**Implementation**: Tasks 3.6–3.11 below.

### Variance Allocation Framework

Implements type-based variance allocation to resolve factor model misspecification. See [[methodology/project/validation-event-correlations]] for problem identification.

| Task | Description | Status |
|------|-------------|--------|
| **3.6** Create `methodology/reference/variance-allocation` | Core framework document: theoretical foundation, type-specific targets (0.70-0.80 for Type 1, 0.60-0.70 for Type 2, 0.40-0.50 for Type 3, 0.50-0.60 for Type 4), computation method for scale factors, worked examples | ✅ |
| **3.7** Update `methodology/reference/causal-types` | Add variance implications section linking each causal type to its factor-explained variance target and epistemological rationale | ✅ |
| **3.8** Update `methodology/reference/factor-loadings` | Add variance constraint requirement: (ΛΩΛᵀ)ᵢᵢ must equal target for event's causal type; add workflow for specifying relative loadings then scaling to target | ✅ |
| **3.9** Update `methodology/reference/type-3-calibration` | Add cross-reference connecting "resolution intractability" discussion to variance allocation operationalization; explain why Type 3 gets lowest factor-explained variance | ✅ |
| **3.10** Revise validation notes | Update `validation-event-correlations` and `validation-findings-report` with correct framing (type-based targets, not uniform); remove outdated recommendations | ✅ |
| **3.11** Implement variance allocation across all events | Compute scale factors for all 28 events by causal type; update event specifications with scaled loadings; re-run validation to confirm (ΛΩΛᵀ)ᵢᵢ ≤ target; document changes in event changelogs | 🔲 |

**Dependencies**: 3.6 → 3.7, 3.8, 3.9, 3.10 → 3.11

### Cleanup Tasks (Post-Variance Framework)

Documentation cleanup identified during Task 3.6-3.10 implementation.

| Task | Description | Priority | Status |
|------|-------------|----------|--------|
| **3.12** | **DRY violation**: Remove redundant variance target tables from causal-types, factor-loadings, type-3-calibration. Replace with single-line cross-references to variance-allocation. | Medium | 🔲 |
| **3.13** | **Stale guidance**: Update or remove "Common Patterns by Causal Type" and "Loading Scale" sections in factor-loadings—values (0.60-0.85) are inconsistent with post-scaling reality (~0.30-0.50 for Type 3). | Medium | 🔲 |
| **3.14** | **Index update**: Add variance-allocation to methodology index for discoverability. | Low | 🔲 |
| **3.15** | **Vestigial Type 4**: Evaluate whether Type 4 variance targets are needed—we classified Type 4 as "not events, move to baseline." If no Type 4 events exist, remove from framework. | Low | 🔲 |
| **3.16** | **Validation notes cleanup**: Either (a) rewrite validation-event-correlations and validation-findings-report as clean documents, or (b) archive/delete them since essential findings are captured in variance-allocation. Currently archaeological mess. | Low | 🔲 |
| **3.17** | **Verify math**: Run actual computation to verify worked examples—confirm scaled loadings produce target variance after all cross-terms. | Medium | 🔲 |

**Note**: Task 3.16 may be moot if validation notes are treated as scratch/working documents to discard after Task 3.11 implementation validates the framework.

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