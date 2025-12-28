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

Actionable development tasks, ordered by importance and dependency. This complements the high-level [[methodology/project/development-roadmap]] and the event-focused [[methodology/project/progress-tracker]].

---

## How to Use This Document

Tasks are grouped by category and roughly ordered by priority within each category. Dependencies are noted where they exist.

**Status markers:**
- 🔲 Not started
- 🟡 In progress
- ✅ Complete
- ⏸️ Blocked (dependency noted)

When completing a task, move it to the Completed section at the bottom with the completion date.

---

## 1. Foundational Methodology

Tasks that must be completed before event specification can proceed correctly. These define *how* to specify events.

| Priority | Task | Status | Dependencies | Notes |
|----------|------|--------|--------------|-------|
| **1.1** | Write Type 3 calibration guidance | ✅ | — | [[methodology/reference/type-3-calibration]] complete. Worked example: [[events/geopolitical/taiwan-conflict]]. |
| **1.2** | Update causal-types reference | ✅ | 1.1 | [[methodology/reference/causal-types]] updated. Tractability framing, epistemology links, common mistakes added. |
| **1.3** | Update probability-estimation reference | ✅ | — | Type-specific guidance added for Type 1, Type 2, Type 3. |
| **1.4** | Update calibration-anchors reference | ✅ | — | Historical reference events typed; new anchors added (Oil Shock, Volcanic, Breakthrough). |
| **1.5** | Update factor-loadings reference | ✅ | — | Complete (commit 359ec14). Revisions 1.5.1-1.5.5 addressed conceptual issues with factor-state relationships. |

#### Task 1.5 Sub-tasks (Revisions)

Self-critique identified that the initial implementation treats factors as if they "shock" state variables, but factors are latent constructs (dimensionality reduction for correlated event sampling), not causal agents. The relationship is: `Latent Factor → (unobserved mechanism) → Observable State Variables`. Revisions needed:

| Sub-task | Status | Description |
|----------|--------|-------------|
| **1.5.1** | ✅ | Added worked example tracing Pakistan State Failure through factor loadings to state variable impacts |
| **1.5.2** | ✅ | Added per-factor narrative paragraphs explaining causal pathways |
| **1.5.3** | ✅ | Separated "indicator variables" from "affected variables" for each factor |
| **1.5.4** | ✅ | Verified and updated cross-references to state-specification section numbers |
| **1.5.5** | ✅ | Included ~80 specific variable IDs replacing category-level descriptions |

| **1.6** | Establish research documentation standards | 🔲 | — | Define schemas for source documentation, synthesis structure, citation conventions. Events and entities become ongoing research projects; need norms for how research accumulates and traces to parameter choices. Includes templates for Level 1/2/3 deliverables. |
| **1.7** | Investigate Type 3 non-discontinuity resolutions | 🟡 | — | Current Type 3 methodology includes "status quo restoration" and similar resolutions that are explicitly *not* discontinuities. This creates structural inconsistency: the event catalog should enumerate discontinuities, but Type 3 events include non-discontinuity outcomes in their resolution sets. **India-Pakistan Military Conflict revised as worked example of correct approach**: event IS the discontinuity, probability is occurrence rate (0.9%), non-discontinuity outcomes are simply non-occurrence. Remaining work: apply same revision to Taiwan Conflict and update Type 3 methodology docs. |
| **1.8** | Refactor state-specification into modular documents | 🟡 | — | Current document is ~1,100 lines mixing entities, variables, dynamics, transmission, and outputs. Refactor into 7 focused documents per [[methodology/concepts/synthetic-variable-problem]] analysis. See §1.8 sub-tasks below. |
| **1.9** | Apply synthetic variable changes | ⏸️ | 1.8.2, 1.8.3 | Implement recommendations from [[methodology/concepts/synthetic-variable-problem]]: eliminate synthetic indices, decompose to observables, move assessments to outputs. Changes land in `state-variables-country` and `state-variables-global`. |

#### Task 1.8 Sub-tasks (State Specification Refactoring)

The current `state-specification` document (~1,100 lines) mixes several concerns and duplicates content between main body and appendices. Refactor into focused documents for maintainability and progressive disclosure.

**Analysis document:** [[methodology/concepts/synthetic-variable-problem]]

**Target structure:**
```
methodology/reference/
├── state-overview.md              # Entry point (~200 lines)
├── state-entities.md              # 40 countries + 12 aggregates (~250 lines)
├── state-variables-country.md     # Full country variable catalog (~400 lines)
├── state-variables-global.md      # Full global variable catalog (~250 lines)
├── state-dynamics.md              # Variable dynamics classification (~200 lines)
├── state-transmission.md          # Transmission mechanisms (~200 lines)
└── state-outputs.md               # Output specs + derived assessments (~300 lines)
```

| Sub-task | Status | Session | Deliverables |
|----------|--------|---------|--------------|
| **1.8.1** | ✅ | 1 | Create `state-overview`, `state-entities`; update index |
| **1.8.2** | ✅ | 2 | Create `state-variables-country` with synthetic variable changes applied |
| **1.8.3** | 🔲 | 3 | Create `state-variables-global` with synthetic variable changes applied |
| **1.8.4** | 🔲 | 4 | Create `state-dynamics`, `state-transmission`, `state-outputs`; archive old doc; final cleanup |

**Session 1 entry criteria:** This plan documented and committed.
**Session 1 exit criteria:** `state-overview` and `state-entities` created; index updated; git committed.

**Session 2 entry criteria:** Session 1 complete.
**Session 2 exit criteria:** `state-variables-country` created with synthetic variable changes (eliminate `regime_stability`, `institutional_quality`, `state_capacity`, `corruption_index`; decompose alliance variables; add observable replacements); git committed.

**Session 3 entry criteria:** Session 2 complete.
**Session 3 exit criteria:** `state-variables-global` created with synthetic variable changes (address geopolitical structure indices); git committed.

**Session 4 entry criteria:** Session 3 complete.
**Session 4 exit criteria:** Remaining documents created; derived assessment formulas in `state-outputs`; old `state-specification` archived or deleted; cross-references updated; git committed.

**Content migration map:**

| Current Section | Destination |
|-----------------|-------------|
| Executive Summary | `state-overview` |
| Entity Inventory (§2) | `state-entities` |
| Country Variables (§3) | `state-variables-country` |
| Global Variables (§4) | `state-variables-global` |
| Dynamics Classification (§5) | `state-dynamics` |
| Transmission Mechanisms (§6) | `state-transmission` |
| Outputs & Assessments (§7) | `state-outputs` |
| Open Questions (§8) | Distribute to relevant docs or retire |
| Appendix A (variable tables) | Merge into variable catalogs (eliminate duplication) |
| Appendix B (regional composition) | `state-entities` |
| Appendix C (data sources) | Distribute to variable catalogs |

**Rationale for ordering:**
- 1.1 blocks Type 3 event specification (Taiwan, climate agreements, etc.)
- 1.2 depends on 1.1 (incorporates its conclusions)
- 1.3-1.5 are independent and can proceed in parallel

---

## 2. Event Specification

The core intellectual work. Populate the event catalog with fully specified discontinuity events.

### 2.1 Priority Events (First 20)

| Priority | Event | Type | Status | Dependencies | Notes |
|----------|-------|------|--------|--------------|-------|
| **2.1.1** | Taiwan Conflict | Type 3 | ✅ | — | Level 1 complete; [[events/geopolitical/taiwan-conflict]] |
| **2.1.2** | Severe Pandemic | Type 1 | ✅ | 1.3 | Level 1 complete; [[events/health/severe-pandemic]] |
| **2.1.3** | Global Financial Crisis | Type 1/2 | ✅ | 1.3 | Level 1 complete; [[events/financial/global-financial-crisis]] |
| **2.1.4** | Amazon Tipping Point | Type 2 | ✅ | — | Level 1 complete; [[events/climate/amazon-tipping-point]] |
| **2.1.5** | Permafrost Methane Release | Type 2 | ✅ | — | Level 1 complete; [[events/climate/permafrost-methane-release]] |
| **2.1.6** | Egypt State Failure | Type 2 | ✅ | — | Level 1 complete; [[events/geopolitical/egypt-state-failure]] |
| **2.1.7** | Russia State Failure | Type 2 | ✅ | — | Level 1 complete; [[events/geopolitical/russia-state-failure]] |
| **2.1.8** | Saudi Regime Instability | Type 2 | ✅ | — | Level 1 complete; [[events/geopolitical/saudi-regime-instability]] |
| **2.1.9** | Iran Regime Change | Type 2 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/iran-regime-change]] |
| **2.1.10** | Turkey Political Crisis | Type 2 | ✅ | — | Level 1 complete; [[events/geopolitical/turkey-political-crisis]] |
| **2.1.11** | Dollar Reserve Crisis | Type 2 | ✅ | — | Level 1 complete; [[events/financial/dollar-reserve-crisis]] |
| **2.1.12** | Chinese Economic Crisis | Type 2 | 🟡 | — | Level 1 draft complete; [[events/financial/chinese-economic-crisis]]; awaiting review |
| **2.1.13** | Chinese Political Crisis | Type 2/3 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/chinese-political-crisis]] |
| **2.1.14** | EU Fragmentation | Type 2 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/eu-fragmentation]] |
| **2.1.15** | US Constitutional Crisis | Type 2/3 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/us-constitutional-crisis]] |
| **2.1.16** | India-Pakistan Military Conflict | Type 3 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/india-pakistan-military-conflict]] |
| **2.1.17** | Korean Peninsula Crisis | Type 3 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/korean-peninsula-crisis]] |
| **2.1.18** | US-China Economic Rupture | Type 3 | ✅ | 1.1 | Level 1 complete; [[events/geopolitical/us-china-economic-rupture]] |
| **2.1.19** | Oil Supply Shock | Type 1 | ✅ | 1.3 | Level 1 complete; [[events/energy/oil-supply-shock]] |
| **2.1.20** | Iran Nuclear Acquisition | Type 3 | ✅ | 1.1, 2.1.9 | Level 1 complete; [[events/geopolitical/iran-nuclear-acquisition]]; Type 2/3 hybrid. Pressure from regional threats + decision to weaponize. F_MENA/F_GPT primary drivers. Three acquisition modes (covert/breakout/contested) at uniform probability. Key cascade: Saudi Nuclear Acquisition (+5-8%/year for 10 years). |

**Already complete:**
- ✅ AMOC Weakening (Type 2)
- ✅ Pakistan State Failure (Type 2)

### 2.2 Breakthrough Events (Type 1 Positive)

| Priority | Event | Status | Notes |
|----------|-------|--------|-------|
| **2.2.1** | Fusion Commercialization | ✅ | [[events/breakthrough/fusion-commercialization]]; Level 1 complete |
| **2.2.2** | Agricultural Yield Breakthrough | ✅ | [[events/breakthrough/agricultural-yield-breakthrough]]; Level 1 complete |
| **2.2.3** | Cancer Treatment Breakthrough | ✅ | [[events/breakthrough/cancer-treatment-breakthrough]]; Level 1 complete; Platform technology achieving broad efficacy across solid tumor types. Annual probability 1.0% from medical breakthrough reference class. F_TECH primary driver (0.70), F_HLTH secondary (0.30). Three deployment branches: Gradual Diffusion (50%), Rapid Transformation (30%), Economically Concentrated (20%). Differential impact by population age structure and health system capacity—Japan/Germany highest benefit (+3.0-3.5 years life expectancy), young populations see minimal impact. Critical review flagged Gradual/Rapid branch distinction for Level 2 reconsideration. |
| **2.2.4** | Antimicrobial Platform | ✅ | [[events/breakthrough/antimicrobial-platform]]; Level 1 complete |
| **2.2.5** | Energy Storage Breakthrough | - | Commercialization of disruptive improvements in battery density; TODO |

### 2.3 Additional Events (to reach 40+)

To be identified after Priority Events are complete. Candidates will emerge from:
- Gaps identified during priority event specification
- Cascade triggers referenced by priority events
- Regional coverage gaps
- Sensitivity analysis (Phase 3)

**Identified candidates:**

| Event | Type | Source | Notes |
|-------|------|--------|-------|
| Saudi Nuclear Acquisition | Type 3 | Cascade from IRAN_NUCLEAR_ACQUISITION | Stated Saudi policy to match Iranian capability; Pakistan assistance pathway |
| Sahel Catastrophe | Type 2 | Regional coverage | Highest-risk humanitarian zone |

### 2.4 Critical Review of Existing Events

Apply [[methodology/03-critical-review]] to all completed Level 1 events. Adds "Probability Evolution" (for Type 2) and "Case Against" sections per rubric.

| Priority | Event | Type | Status | Notes |
|----------|-------|------|--------|-------|
| **2.4.1** | AMOC Weakening | Type 2 | ✅ | Completed Dec 2025 (commit ea16a2e) |
| **2.4.2** | Chinese Political Crisis | Type 2/3 | ✅ | Completed Dec 2025 |
| **2.4.3** | Taiwan Conflict | Type 3 | 🔲 | |
| **2.4.4** | Severe Pandemic | Type 1 | 🔲 | |
| **2.4.5** | Global Financial Crisis | Type 1/2 | 🔲 | |
| **2.4.6** | Amazon Tipping Point | Type 2 | 🔲 | |
| **2.4.7** | Permafrost Methane Release | Type 2 | 🔲 | |
| **2.4.8** | Pakistan State Failure | Type 2 | 🔲 | |
| **2.4.9** | Egypt State Failure | Type 2 | 🔲 | |
| **2.4.10** | Russia State Failure | Type 2 | 🔲 | |
| **2.4.11** | Saudi Regime Instability | Type 2 | 🔲 | |
| **2.4.12** | Iran Regime Change | Type 2 | 🔲 | |
| **2.4.13** | Turkey Political Crisis | Type 2 | 🔲 | |
| **2.4.14** | Dollar Reserve Crisis | Type 2 | 🔲 | |
| **2.4.15** | Chinese Economic Crisis | Type 2 | 🔲 | After 2.1.12 review complete |

---

## 3. Validation & Refinement

Tasks that validate the model structure and refine parameters based on evidence.

| Priority | Task | Status | Dependencies | Notes |
|----------|------|--------|--------------|-------|
| **3.1** | Compute implied event correlations | 🔲 | 10+ events specified | Use Σ = ΛΩΛ' + Ψ; verify correlations are sensible |
| **3.2** | Check double-counting inflation | 🔲 | 3.1 | Events loading on correlated factors may have inflated correlations |
| **3.3** | Historical proxy analysis | 🔲 | Phase 2 complete | Compare factor correlations to observable proxy correlations |
| **3.4** | Sensitivity analysis: factor correlations | 🔲 | Phase 2 complete | Test F_CLIM↔F_FOOD, F_GPT↔F_EAS at low/baseline/high |
| **3.5** | Audit Type 3 resolution branch completeness | 🔲 | Type 3 events specified | Per positive-discontinuity resolution: ensure favorable branches exist |

---

## 4. Implementation (Phase 2)

Build the simulation prototype. See [[methodology/project/development-roadmap]] for detailed architecture.

| Priority | Task | Status | Dependencies | Notes |
|----------|------|--------|--------------|-------|
| **4.1** | Set up prototype directory structure | 🔲 | — | data/, core/, analysis/, visualization/ |
| **4.2** | Implement state vector management | 🔲 | 4.1 | state.py — country and global variables |
| **4.3** | Implement factor sampling with correlations | 🔲 | 4.1 | events.py — Gaussian copula approach |
| **4.4** | Implement event firing logic | 🔲 | 4.3 | events.py — factor draws → event occurrence |
| **4.5** | Implement impact transmission | 🔲 | 4.2, 4.4 | impacts.py — event → state variable effects |
| **4.6** | Implement aftermath tracking | 🔲 | 4.5 | Track active aftermaths, apply factor modifications |
| **4.7** | Implement baseline dynamics | 🔲 | 4.2 | dynamics.py — between-event state evolution |
| **4.8** | Implement main simulation loop | 🔲 | 4.3-4.7 | simulation.py — orchestrate annual steps |
| **4.9** | Implement output analysis | 🔲 | 4.8 | distributions.py — terminal state analysis |
| **4.10** | Create prototype run notebook | 🔲 | 4.8, 4.9 | Jupyter notebook for running and examining |
| **4.11** | Validate prototype produces sensible output | 🔲 | 4.10 | Events fire at ~specified rates; no degenerate results |

---

## 5. Future Work (Phase 3+)

Tasks to be prioritized after sensitivity analysis reveals what matters.

| Task | Status | Trigger |
|------|--------|---------|
| Multi-branch aftermath refinement | ⏸️ | Sensitivity shows aftermath type affects tail outcomes |
| Entity expansion (additional countries) | ⏸️ | Sensitivity shows regional dynamics matter |
| Variable expansion | ⏸️ | Sensitivity shows unmodeled mechanisms matter |
| Dynamics refinement | ⏸️ | Sensitivity shows dynamics parameters are important |
| Level 2/3 research for high-impact events | ⏸️ | Sensitivity identifies events driving tail outcomes |


---

## Task Addition Protocol

When new tasks emerge:
1. Add to appropriate section
2. Assign priority relative to existing tasks
3. Note dependencies
4. If task came from a session, reference the source

When completing tasks:
1. Move to Completed section with date
2. Update any dependent tasks (unblock them)
3. Update progress-tracker if it affects event counts
4. Commit changes

---

*Last updated: December 28, 2025*
