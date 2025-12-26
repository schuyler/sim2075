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
| **2.1.20** | Iran Nuclear Acquisition | Type 3 | 🔲 | 1.1, 2.1.9 | Likely Type 3 (decision-driven); interacts with Iran Regime Change; triggers regional proliferation cascade |

**Already complete:**
- ✅ AMOC Weakening (Type 2)
- ✅ Pakistan State Failure (Type 2)

### 2.2 Breakthrough Events (Type 1 Positive)

| Priority | Event | Status | Notes |
|----------|-------|--------|-------|
| **2.2.1** | Fusion Commercialization | 🔲 | Per positive-discontinuity resolution |
| **2.2.2** | Agricultural Yield Breakthrough | 🔲 | Heat/drought-tolerant crops |
| **2.2.3** | Cancer Treatment Breakthrough | 🔲 | Immunotherapy platform or equivalent |
| **2.2.4** | Antimicrobial Platform | 🔲 | Antibiotic alternative |

### 2.3 Additional Events (to reach 40+)

To be identified after Priority Events are complete. Candidates will emerge from:
- Gaps identified during priority event specification
- Cascade triggers referenced by priority events
- Regional coverage gaps
- Sensitivity analysis (Phase 3)

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

## Completed Tasks

Tasks moved here when done, with completion date.

| Date | Task | Notes |
|------|------|-------|
| Dec 2025 | Task 2.1.19: Oil Supply Shock | Level 1 complete; [[events/energy/oil-supply-shock]]; Type 1 stochastic event. Annual probability 2.5% based on historical base rate (2 discontinuities in 55 years) with condition adjustments. Discontinuity defined as sustained major disruption (>15% supply, 6+ months) forcing structural adaptation — excludes routine volatility. Three resolutions: Accelerated Transition (40%), Producer Restructuring (35%), Extended Crisis (25%). F_MENA primary driver (0.55), F_GPT secondary (0.40). Strait of Hormuz and Saudi stability as key vulnerability pathways. |
| Dec 2025 | Task 2.1.18: US-China Economic Rupture | Level 1 complete; [[events/geopolitical/us-china-economic-rupture]]; Type 3 contingent event. Annual probability 1.75% (= 2.5% crisis window × 70% discontinuity). Two resolutions: Full Rupture (50%), Managed Separation (50%). F_GPT primary driver (0.75), F_EAS secondary (0.40). Comprehensive supply chain impact modeling including pharmaceutical APIs, rare earths, consumer electronics. Distinguished from Taiwan Conflict by non-military trigger. |
| Dec 2025 | Task 2.1.17: Korean Peninsula Crisis | Level 1 complete; [[events/geopolitical/korean-peninsula-crisis]]; Type 3 contingent event. Annual probability 0.75% (= 2.5% crisis window × 30% conflict). Three aftermath branches: Limited Conflict (55%), Major War (30%), Nuclear Escalation (15%). F_EAS primary driver (0.85), F_GPT secondary (0.40). US tripwire forces mean automatic US involvement. Seoul vulnerability critical for impact estimates. |
| Dec 2025 | Task 2.1.16: India-Pakistan Military Conflict | Level 1 complete; [[events/geopolitical/india-pakistan-military-conflict]]; Type 3 contingent event. Revised framing: event IS the discontinuity (military conflict), not a crisis window. Annual probability 0.9% (= 2.5% crisis window × 35% escalation). Three aftermath branches: Limited Conflict (55%), Major War (35%), Nuclear Escalation (10%). F_SAS primary driver (0.80). Removed non-discontinuity resolutions per Task 1.7 investigation. |
| Dec 2025 | Task 2.1.15: US Constitutional Crisis | Level 1 complete; [[events/geopolitical/us-constitutional-crisis]]; Type 2/3 hybrid modeling constitutional breakdown. Four resolutions (Authoritarian Consolidation 30%, Federal Fragmentation 25%, Prolonged Instability 30%, Negotiated Restructuring 15%). Probability 0.5% annually. F_FIN/F_GPT primary drivers. Highest global-impact event due to dollar/NATO/nuclear implications. |
| Dec 2025 | Task 2.1.14: EU Fragmentation | Level 1 complete; [[events/geopolitical/eu-fragmentation]]; Critical review identified "Orderly Fragmentation" fails discontinuity test — converted to pure Type 2 threshold event modeling disorderly collapse only. Probability 0.4%, F_EUR/F_FIN drivers, Brexit:EU::Tiananmen:CCP calibration insight. Commits 60218a0, 4e73181. |
| Dec 2025 | Task 2.1.13: Chinese Political Crisis | Level 1 complete; [[events/geopolitical/chinese-political-crisis]]; Removed Stabilization resolution (not a discontinuity), new split Transformation 40%/Collapse 60%, probability 0.4%. Added [[methodology/discontinuity-test]] to methodology. Commits 4931001, 94ad28c, d73b526. |
| Dec 2025 | Task 2.1.11: Dollar Reserve Crisis | Level 1 complete; [[events/financial/dollar-reserve-crisis]]; Type 2 threshold, F_FIN/F_GPT drivers, three aftermath branches (disorderly/managed/Bretton Woods III) |
| Dec 2025 | Task 2.1.10: Turkey Political Crisis | Level 1 complete; [[events/geopolitical/turkey-political-crisis]]; Type 2 threshold, F_MENA/F_FIN/F_EUR/F_GPT drivers, currency vulnerability and Kurdish dimension |
| Dec 2025 | Task 2.1.9: Iran Regime Change | Level 1 complete; [[events/geopolitical/iran-regime-change]]; Type 2 threshold, F_MENA/F_GPT/F_CLIM drivers, water crisis emphasis |
| Dec 2025 | Task 2.1.8: Saudi Regime Instability | Level 1 complete; [[events/geopolitical/saudi-regime-instability]]; Type 2 threshold, F_MENA/F_FIN/F_CLIM drivers, lower probability due to financial cushion |
| Dec 2025 | Task 2.1.7: Russia State Failure | Level 1 complete; [[events/geopolitical/russia-state-failure]]; Type 2 threshold, F_GPT/F_EUR drivers, nuclear security considerations |
| Dec 2025 | Task 2.1.6: Egypt State Failure | Level 1 complete; [[events/geopolitical/egypt-state-failure]]; Type 2 threshold, F_MENA/F_FOOD/F_CLIM drivers, Nile vulnerability |
| Dec 2025 | Task 2.1.5: Permafrost Methane Release | Level 1 complete; [[events/climate/permafrost-methane-release]]; Type 2 threshold, F_CLIM dominant |
| Dec 2025 | Task 2.1.4: Amazon Tipping Point | Level 1 complete; [[events/climate/amazon-tipping-point]]; Type 2 threshold, F_CLIM/F_FOOD drivers |
| Dec 2025 | Task 2.1.3: Global Financial Crisis | Level 1 complete; [[events/financial/global-financial-crisis]]; Type 2 hybrid with Type 1 floor |
| Dec 2025 | Task 2.1.2: Severe Pandemic | Level 1 complete; [[events/health/severe-pandemic]]; First Type 1 event; established base-rate methodology |
| Dec 2025 | Task 1.5: Update factor-loadings reference | Complete. Sub-tasks 1.5.1-1.5.5 addressed conceptual issues: added worked example (Pakistan), per-factor paragraphs, indicator/affected variable separation, cross-reference verification, specific variable IDs. Commit 359ec14. |
| Dec 2025 | Task 1.4: Update calibration-anchors reference | Historical events typed; Oil Shock, Volcanic, Breakthrough anchors added |
| Dec 2025 | Task 1.3: Update probability-estimation reference | Type-specific guidance for Type 1/2/3; archived v1 event specs |
| Dec 2025 | Task 1.2: Update causal-types reference | [[methodology/reference/causal-types]] updated with tractability framing, epistemology links |
| Dec 2025 | Task 1.1: Type 3 calibration guidance | [[methodology/reference/type-3-calibration]]; worked example [[events/geopolitical/taiwan-conflict]] |
| Dec 2025 | Taiwan Conflict specification | Level 1 complete; [[events/geopolitical/taiwan-conflict]] |
| Dec 2025 | AMOC Weakening specification | Level 1 complete |
| Dec 2025 | Pakistan State Failure specification | Level 1 complete |
| Dec 2025 | Factor correlation matrix (Ω) | 12×12 matrix specified |
| Dec 2025 | Aftermath branches framework | Reference doc complete |
| Dec 2025 | Gaussian copula concept note | Conceptual foundation |
| Dec 2025 | Factor correlation structure rationale | Design doc complete |
| Dec 2025 | Entropy maximization concept note | Epistemic principle |
| Dec 2025 | Small-N actor problem concept note | Type 3 intractability |
| Dec 2025 | Tractability boundaries concept note | What is/isn't tractable |
| Dec 2025 | Resolve: Factor correlation structure | Open question closed |
| Dec 2025 | Resolve: Recovery dynamics | Open question closed |
| Dec 2025 | Resolve: Time horizon tractability | Open question closed (partial) |
| Dec 2025 | Resolve: Positive discontinuity coverage | Open question closed |

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

*Last updated: December 21, 2025*