---
title: progress-tracker
type: note
permalink: methodology/progress-tracker
tags:
- methodology
- progress
- tracking
- status
- placeholder
---

# Progress Tracker

**Status: PLACEHOLDER - To be filled in**

Tracks event specification progress and next actions.

## Summary Statistics

[TO BE ADDED]

## Event Status

[TO BE ADDED]

## Next Actions

[TO BE ADDED]

## Blockers

[TO BE ADDED]


## Progress Tracker
# Progress Tracker

Tracks event specification progress and next actions.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Priority events | 20 |
| Level 1 complete (old template) | 2 |
| Level 1 complete (new template) | 0 |
| Level 2 complete | 0 |
| Level 3 complete | 0 |
| **Remaining** | **20** (including 2 needing revision) |

**Completion: 0%** (per new template)

---

## Framework Status

### Methodology Documents

| Document | Status | Notes |
|----------|--------|-------|
| [[methodology/integrated-event-state-framework]] | **COMPLETE** | Primary framework document |
| [[methodology/event-template-v2]] | **COMPLETE** | Updated with causal types, impact vectors |
| [[methodology/level-1-workflow]] | **COMPLETE** | Updated workflow |
| [[methodology/impact-estimation]] | **COMPLETE** | Added durability types |
| [[methodology/quality-checklist]] | **COMPLETE** | Added type-specific checks |
| [[methodology/calibration-anchors]] | **COMPLETE** | Added causal type info |

### Deprecated Documents

| Document | Status |
|----------|--------|
| [[methodology/asymmetric-modeling-proposal]] | DEPRECATED (notice added) |
| [[methodology/discontinuity-causal-typology]] | ABSORBED (notice added) |
| [[research/positive-negative-asymmetry-analysis]] | FINDINGS VALID, FRAMING REVISED |

---

## Event Status

### ⚠️ Needs Revision to New Template

| Event | File | Issue |
|-------|------|-------|
| AMOC Weakening | [[events/climate/amoc-weakening]] | Add causal type, pressure function, impact vector with durability |
| Pakistan State Failure | [[events/geopolitical/pakistan-state-failure]] | Add causal type, pressure function, impact vector with durability |

### 🔲 Not Started

#### Climate Events (Type 2)
| Event | Causal Type | Priority |
|-------|-------------|----------|
| Amazon Tipping Point | Type 2 | High |
| Permafrost Methane Release | Type 2 | Medium |

#### Great Power / Strategic (Type 3)
| Event | Causal Type | Priority |
|-------|-------------|----------|
| Taiwan Conflict | Type 3 | High |
| US-China Trade War Escalation | Type 2/3 | High |
| India-Pakistan Conflict | Type 3 | Medium |
| Korean Peninsula Crisis | Type 3 | Medium |

#### State Failures (Type 2)
| Event | Causal Type | Priority |
|-------|-------------|----------|
| Egypt State Failure | Type 2 | High |
| Russian State Failure | Type 2 | Medium |
| Saudi Regime Instability | Type 2 | Medium |
| Iran Regime Change | Type 2/3 | Medium |
| Turkey Political Crisis | Type 2 | Medium |

#### Economic / Financial (Type 1/2)
| Event | Causal Type | Priority |
|-------|-------------|----------|
| Global Financial Crisis | Type 1/2 | High |
| Dollar Reserve Crisis | Type 2 | High |
| Chinese Economic Crisis | Type 2 | High |
| Oil Supply Shock | Type 1/2 | Medium |

#### Political (Type 2/3)
| Event | Causal Type | Priority |
|-------|-------------|----------|
| EU Fragmentation | Type 2 | Medium |
| US Constitutional Crisis | Type 2/3 | Medium |
| Chinese Political Crisis | Type 2 | Medium |

#### Health (Type 1)
| Event | Causal Type | Priority |
|-------|-------------|----------|
| Severe Pandemic | Type 1 | High |

---

## Next Actions

### Immediate Priority

1. **Revise AMOC specification** to new template (add Type 2 pressure function, impact vector with durability)
2. **Revise Pakistan specification** to new template (add Type 2 pressure function, impact vector with durability)
3. **Complete one new event** using [[methodology/level-1-workflow]] to validate process

### High Priority Events (Next)

| Event | Why High Priority |
|-------|-------------------|
| Taiwan Conflict | Type 3 anchor event; tests window-resolution structure |
| Global Financial Crisis | Type 1/2 anchor; tests hybrid modeling |
| Severe Pandemic | Type 1 anchor; tests stochastic modeling |
| Chinese Economic Crisis | High global impact; tests Type 2 for major economy |

### After Level 1 Complete

4. Build prototype simulation (Phase 2 per roadmap)
5. Run sensitivity analysis to identify upgrade candidates
6. Upgrade high-sensitivity events to Level 2

---

## Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| Existing event specs need revision | Can't validate prototype until specs conform to new template | Revise AMOC, Pakistan first |

---

## Session Log

| Date | Work Completed | Notes |
|------|----------------|-------|
| Dec 2025 | AMOC, Pakistan | Initial specifications (old template) |
| Dec 2025 | Methodology restructure | Level-1 workflow, templates |
| Dec 2025 | **Framework integration** | integrated-event-state-framework created; asymmetry approach discarded; all methodology docs updated |

---

## Milestone Targets

| Milestone | Target | Status |
|-----------|--------|--------|
| Framework documentation complete | Before event specs | ✅ COMPLETE |
| Existing specs revised to new template | Before new events | ⏳ Pending |
| All 20 priority events at Level 1 | Before Phase 2 | 0% complete |
| Prototype simulation running | After Level 1 complete | Not started |
| Sensitivity analysis complete | After prototype | Not started |
| Level 2 upgrades (5-8 events) | After sensitivity | Not started |