---
title: open-questions
type: note
permalink: methodology/project/open-questions
tags:
- methodology
- planning
- open-questions
- todo
---

# Open Questions

Higher-level methodological and structural questions that warrant dedicated exploratory sessions. These are distinct from the task-oriented progress tracker—each item here represents an area of uncertainty or potential improvement in the simulation architecture itself.

---

## Active Questions

### 2. Type 3 Event Calibration

**Status:** Unresolved  
**Added:** December 2025  
**Source:** Methodology review  
**See also:** [[methodology/concepts/small-n-actor-problem]], [[methodology/concepts/entropy-maximization]]

Type 3 (Contingent) events—Taiwan, climate agreements, great power negotiations—depend on decisions by specific actors in ways that Type 1 base rates and Type 2 pressure accumulation don't capture well.

**Key issues:**
- The window-resolution structure is reasonable, but calibrating resolution probabilities ("35% military conflict, 25% negotiated accommodation") is essentially geopolitical forecasting
- Geopolitical forecasting has poor track records (see small-n-actor-problem)
- How should epistemic humility be reflected in Type 3 specifications?

**Candidate approaches:**
- Maximum entropy default (uniform over resolutions) per entropy-maximization principle
- Scenario-based sensitivity analysis for high-impact Type 3 events
- Explicit epistemic categorization (well-characterized / partially-understood / unprecedented)

**Session goal:** Develop guidance for Type 3 calibration that honestly reflects uncertainty about actor decisions while remaining operationally useful.

---

## Resolved Questions

### 1. Factor Correlation Structure

**Status:** Resolved  
**Added:** December 2025  
**Resolved:** December 2025  
**Source:** Methodology review

**Original question:** The correlation structure *between factors themselves* was underspecified. Should factors be independent, correlated via a matrix, or structured hierarchically via meta-factors?

**Resolution:** Adopted inter-factor correlation matrix (Ω). 

**Key decisions:**
- Independent factors underestimate clustering when multiple systemic factors are elevated
- Meta-factors don't fit our case—the correlations we need are pairwise with specific mechanisms, not manifestations of higher-order constructs
- Direct correlation matrix is transparent, mechanism-specific, and revisable

**Deliverables:**
- [[methodology/concepts/gaussian-copula]] — Conceptual foundation for correlated sampling
- [[methodology/concepts/factor-correlation-structure]] — Design rationale for choosing Ω over alternatives
- [[methodology/reference/factor-correlation-matrix]] — The 12×12 matrix with 19 non-zero correlations

**Remaining work:**
- Compute implied event correlations once more events are specified
- Verify double-counting doesn't inflate correlations unreasonably
- Sensitivity analysis on key correlations (F_CLIM↔F_FOOD, F_GPT↔F_EAS)

**Known limitations documented in factor-correlation-matrix:**
- Double-counting through direct loadings + factor correlation
- Symmetric correlation misrepresents causal direction
- No empirical calibration (structured judgment only)

---

### 2. Recovery Dynamics

**Status:** Resolved  
**Added:** December 2025  
**Resolved:** December 2025  
**Source:** Methodology review

**Original question:** The collapse-patterns document covers how things fall apart in detail, but recovery trajectories are thinner. If the simulation produces "Pakistan state failure in 2035," what happens next matters for cumulative outcomes. Does collapsed state remain collapsed, partially recover, or cascade further? Durability types handle impact persistence, but not state recovery trajectories.

**Resolution:** Recovery dynamics are modeled as **event aftermath branches**, not entity regime states or pure impact decay.

**Key decisions:**
- Aftermath branches are event-attached, not entity-attached—we don't pre-classify entities as "fragile" or "stable"
- When an event fires, we sample which aftermath branch obtains
- Each branch specifies ongoing factor modifications and duration/exit conditions
- This preserves narrative interpretability ("Pakistan state failure, persistent_failure branch") without requiring full entity state machines
- MVP uses single-branch aftermaths; multi-branch refinement follows sensitivity analysis

**Why not entity regime states:**
- Entity-attached states require pre-classifying which entities can fail—normatively problematic
- Event-attached states are more general: any event can have branches if warranted
- Complexity is local to events that need it, not spread across entity model

**Why not pure impact decay:**
- Decay captures magnitude attenuation but not qualitative trajectory differences
- "Pakistan recovered slowly" vs "Pakistan became a persistent failed state" have different ongoing dynamics
- These differences matter for cascade potential and tail outcomes

**Deliverables:**
- [[methodology/reference/aftermath-branches]] — Full specification of aftermath branch structure
- Updates to [[methodology/concepts/state-event-coupling]] — Section on aftermath branches
- Updates to [[methodology/concepts/implementation-roadmap]] — Aftermath branches in v1.0 scope

**Implementation approach:**
- v1.0: Single-branch aftermath for events with significant persistent effects
- Refinement trigger: Sensitivity analysis shows tail outcomes depend on aftermath type
- v2.0: Multi-branch specifications for high-impact events

**Known limitations:**
- Single-branch MVP doesn't capture trajectory diversity
- Multi-branch research is Level 2/3 effort (4-20+ hours per event)
- Branch probabilities are judgment-based, not empirically calibrated

---

### 3. Time Horizon Tractability

**Status:** Resolved (partial)  
**Added:** December 2025  
**Resolved:** December 2025  
**Source:** Methodology review

**Original question:** The 50-year horizon (to 2075) strains the methodology. Calibration anchors cover 5-15 year windows. Are 50-year distributions decision-relevant or just noise? Should 2050 be primary?

**Resolution:** Adopted dual-horizon interpretation. Simulation runs through 2075; interpretation distinguishes decision-relevant from exploratory horizons.

**Key decisions:**
- Truncating at 2050 would systematically underweight slow-burn discontinuities (climate tipping points, demographic crunches, institutional decay, climate migration) in favor of acute shocks
- 50-year distributions are not decision-relevant in the policy sense, but are useful for tail exploration—understanding which cascade patterns produce civilizational-scale disruption
- Report distributions at multiple horizons (2035, 2050, 2075) with explicit confidence degradation at longer horizons

**Interpretation framework:**
- **2050 (25 years):** Primary horizon for decision-relevant claims. Outer bound of meaningful action-consequence linkage.
- **2075 (50 years):** Horizon for tail exploration. "What fraction of trajectories lead to catastrophic outcomes?" Not forecasting—exploring possibility space.

**Deferred to implementation (Phase 2):**
- How confidence intervals widen mechanically with time horizon
- Whether Monte Carlo variance growth naturally produces appropriate uncertainty, or whether epistemic uncertainty needs separate modeling
- Validation that longer-horizon outputs aren't false precision

**Known limitations:**
- "Tail exploration" is interpretively useful but not rigorously defined
- No formal confidence degradation model yet
- Calibration anchors remain 5-15 year phenomena; extrapolation to 50 years is acknowledged weakness

---

### 4. Positive Discontinuity Coverage

**Status:** Resolved  
**Added:** December 2025  
**Resolved:** December 2025  
**Source:** Methodology review

**Original question:** The priority event list includes no breakthrough energy, no major de-escalation, no institutional innovation. Does this create asymmetric uncertainty that underweights positive tails?

**Resolution:** The framework is valence-neutral; no special treatment needed. The apparent gap dissolves into two tractable sub-problems.

**Key insight:** "Positive discontinuity" in the integrated framework just means "event with net-beneficial expected impact vector." An event like fusion breakthrough isn't intrinsically positive—it's a shock with mixed-valence downstream effects (reduced emissions pressure, petrostate destabilization, energy abundance effects, great power dynamics shifts). The model handles this correctly.

**What was actually missing:**

1. **Type 3 resolution branches:** Existing contingent events (Taiwan, climate negotiations) already accommodate favorable resolutions. The gap is specification completeness, not missing events. Audit existing Type 3 events for explicit positive resolution branches.

2. **Type 1 breakthroughs:** Genuine stochastic shocks outside baseline trajectory. These are not S-curve continuations—they're low-probability discrete discoveries that would materially change system dynamics.

**Type 1 breakthroughs to specify:**
- Fusion commercialization
- Agricultural yield breakthrough (heat/drought-tolerant crops)
- Novel antimicrobial platform (antibiotic alternative)
- Major cancer treatment breakthrough (immunotherapy platform or equivalent)

See [[events/planned-breakthrough-events]] for specification planning.

**Explicitly excluded from event catalog:**
- Continued solar/wind cost decline → baseline trajectory
- EV adoption acceleration → baseline trajectory
- General AI capability progress → baseline trajectory
- mRNA platform expansion → baseline trajectory

Technology S-curves belong in baseline assumptions, not the event catalog, unless modeling a specific discrete threshold crossing.

**Action items:**
- [ ] Audit Type 3 events for resolution branch completeness
- [ ] Specify 3-4 Type 1 breakthrough events per standard workflow

**Why this isn't a cop-out:** The original concern was that the model would systematically underweight positive tails. The resolution shows this concern was partially misframed (Type 3 events already include favorable branches) and partially valid (Type 1 breakthroughs were missing). Adding breakthroughs and auditing Type 3 completeness addresses the valid part without introducing artificial symmetry.

---

## How to Use This Document

Each open question should get a dedicated exploratory session when bandwidth permits. Sessions should:

1. Review the question and any relevant existing documentation
2. Explore options and tradeoffs
3. Make a decision or explicitly defer with rationale
4. Update relevant methodology documents
5. Move the question to "Resolved" with summary

Questions may spawn sub-questions or reveal new issues—add those as new entries rather than expanding existing items indefinitely.

---

*Last updated: December 2025*