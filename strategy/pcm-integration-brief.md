---
title: pcm-integration-brief
type: note
permalink: strategy/pcm-integration-brief
tags:
- strategy
- integration
- pcm
- cascade-institute
- validation
- correlation
---

# PCM Integration Brief

How the Cascade Institute's Polycrisis Core Model (PCM v2.5, technical synopsis Aug 10, 2025; Homer-Dixon, Lawrence, Shipman, Janzwood, Kemp, Philpot, Schweizer, Bendall) could be integrated with sim2075. Context: [[strategy/inputs/public-landscape-survey]] identifies PCM as sim2075's closest public relative. PCM figures beyond the survey's precision are primary-sourced from the v2.5 synopsis PDF (accessed 2026-07-10) and recorded, with what could and could not be verified, in [[strategy/inputs/pcm-v25-synopsis-notes]].

**Core framing**: the two models share an epistemology — documented expert judgments as parameters, open matrices, honest uncertainty (their zeros explicitly encode "uncertainty made judgment impossible"; our tractability boundaries do the same work) — but occupy disjoint methodological niches. PCM is **static equilibrium analysis**: which 2040 world-states are internally consistent, and which attractors dominate the state space. sim2075 is **dynamic trajectory generation**: timing, probability mass, cascades, durability over 2025–2075. Neither does the other's job. That makes integration a complement, not a merger.

---

## 1. Architecture comparison

| Dimension | PCM v2.5 | sim2075 |
|---|---|---|
| Object of analysis | Internal consistency of global system configurations in 2040 | Probabilistic trajectories of correlated discontinuities through 2075 |
| Resolution | 11 global-aggregate descriptors (Economy, Polity Type, World Order, Inequality, Conflict & Security, Energy, Climate, Health, Food, Transportation, Information Technology), 45 discrete states, ~4.05M combinations | 40 countries and 12 regional aggregates, plus global commons; ~3,100 state variables ([[methodology/reference/state-outputs]]: 3,072); 29 typed events; 12 latent factors ([[methodology/concepts/framework-overview]]) |
| Time treatment | Static: single-year (2040) equilibrium snapshot; no dynamics, no paths | Annual dynamic simulation with state-event feedback, cascades, aftermath branches, impact durability ([[methodology/concepts/state-event-coupling]]) |
| Probability treatment | Deliberately none (CIB doctrine): consistency + basin width ("weight" from succession analysis) and depth ("total impact score") | Explicit: annual event probabilities, joint distribution via Gaussian copula over correlated factors, Monte Carlo over full trajectories |
| Judgment base | 1,800+ documented cross-impact judgments on a −3..+3 Likert scale: sign = promoting/inhibitory influence of one descriptor state on another; magnitude = judgment confidence; row-balance constraint (judgments across a target descriptor's states sum to zero) | Documented per-parameter judgments: event probabilities, factor loadings, factor correlation matrix Ω ([[methodology/reference/factor-correlation-matrix]]), thresholds, cascade magnitudes |
| Output | 11 fully consistent 2040 scenarios collapsing to 3 attractors: "Illiberal Decline" (9 scenarios, basin "over three million"), "Mad Max" (their Scenario 4; basin weight 539,844), "Hope" (their Scenario 11; basin ~10K, but deep/high impact score) | Distribution over 50-year world trajectories: event timing, clustering, conditional aftermaths, recovery/durability structure |

Sourcing: the headline PCM figures (45 states, ~4.05M combinations, 1,800+ judgments, ~3M / ~500K / ~10K basin ordering) appear in [[strategy/inputs/public-landscape-survey]]. The finer-grained figures — the 9-scenario Illiberal Decline cluster, Mad Max = Scenario 4 with weight 539,844, the descriptor/state list, and the judgment-scale semantics — are primary-sourced; see [[strategy/inputs/pcm-v25-synopsis-notes]] for verification details, page references, and unverified items.

---

## 2. Integration directions

### a. PCM attractors as validation targets

**Question**: do sim2075's simulated 2040 world-states cluster near PCM's three attractors? Two independent judgment bases arriving at the same geometry would be meaningful mutual validation; divergence would be diagnostic for both.

**Mechanics**:
1. Define a projection map from sim2075's state variables to the 45 PCM descriptor states (e.g., `global_temp_anomaly` trajectory → Climate state; aggregate `regime_stability` distribution → Polity Type state; conflict event history → Conflict & Security state). Descriptors with no sim2075 analog (Transportation) get dropped or held fixed.
2. Run N simulations, snapshot each at 2040, project onto descriptor space.
3. Measure: cluster membership and geometry — which attractor basin (if any) each projected run falls in (using their published matrix and succession analysis for basin assignment), and distance of the modal simulated state from each fully consistent scenario. Per §3 risk 4, the comparison is *geometric* — do simulated states sit where their attractors sit? — never a scoring of our run fractions against their basin weights, which are not probabilities.
4. Bonus output PCM cannot produce: the fraction of runs per attractor is a genuine *probability mass* estimate — decision-relevant new information, reported alongside (not compared against) their combinatorial basin widths (§3, risk 4).

**Effort**: **S–M**. The projection map is the only new artifact (~11 classification rules); the rest is post-processing of runs we need anyway. Blocked on having a runnable simulation and their published matrix.

### b. PCM cross-impact matrix as a prior for Ω

**Question**: can their 1,800 judgments serve as independent evidence for the signs and rough magnitudes of our factor correlation matrix?

**Mechanics**:
1. Map descriptors onto factors where analogs exist: Climate→F_CLIM, Health→F_HLTH, Food→F_FOOD, World Order + Conflict & Security→F_GPT, Economy→F_FIN (partial), Information Technology→F_TECH, Energy→F_CLIM/F_TECH (split). Polity Type, Inequality, Transportation have no factor analog (they map to state variables, if anything); our six regional factors have no descriptor analog.
2. For each mappable descriptor pair, aggregate the state-by-state judgment block into a scalar coupling: e.g., a signed monotonicity statistic (do "worse" states of A promote "worse" states of B?), symmetrized across both directions.
3. Compare against Ω's entries. Concretely testable: does the Climate→Food block support Corr(F_CLIM, F_FOOD) = 0.50? Does Economy↔Health support F_HLTH↔F_FIN = 0.30? Do near-zero blocks corroborate our sparse-by-default entries?
4. Where PCM shows strong coupling and Ω has zero (or vice versa), document and either revise Ω or record the disagreement with rationale.

**Value**: [[methodology/reference/factor-correlation-matrix]] lists "No Empirical Calibration" as an open limitation — every Ω entry is our judgment alone. This is the only available external, documented, independently produced evidence base for those entries.

**Effort**: **M**. The mapping and aggregation statistic need design care (see §3); the comparison itself is small. Blocked on matrix publication.

### c. PCM descriptor states as boundary conditions

**Question**: what happens *after* 2040, from inside a basin? "Simulate forward from inside the Illiberal Decline basin" — is it durable to 2075? What are annual escape probabilities, and which events (or event absences) drive escape?

**Mechanics**: invert the projection map from (a). Take a fully consistent scenario (e.g., Mad Max — their Scenario 4: nonocracy, international fragmentation, widespread non-state violence, unmanaged economic failure, failed global industrial food production, high burden of disease; full state list in [[strategy/inputs/pcm-v25-synopsis-notes]]), set sim2075 initial state variables and factor means consistent with those descriptor states, run forward. Output: basin durability, escape routes, and conditional trajectory distributions — the dynamic questions their static method explicitly cannot ask.

**Effort**: **M**. Reuses the (a) projection map inverted; the hard part is choosing defensible initializations for the ~3,100 state variables a coarse descriptor state underdetermines. Natural second joint experiment after (a).

### d. sim2075 events as PCM "triggers" (contribution flowing the other way)

Their companion "Global Systemic Stresses" report (Nov 2025) proposes a Stress–Trigger–Crisis model — 14 slow stresses, fast triggers, 9 vital systems — but it is conceptual, not operationalized. sim2075's machinery operationalizes exactly this distinction:

| Their concept | sim2075 mechanism |
|---|---|
| Slow stresses | Pressure variables + factor-driven accumulation ([[methodology/concepts/state-event-coupling]]) |
| Fast triggers | Type 1 (stochastic) and Type 3 (contingent window-resolution) events |
| Stress→crisis threshold | Type 2 state-conditioned threshold events |
| Crisis propagation across vital systems | Cascades + aftermath branches + durability types |

**Mechanics**: a crosswalk document mapping their 14 stresses and 9 vital systems onto our factors, pressure variables, and event catalog, showing where each of their conceptual arrows becomes an explicit equation. This is a gift, not an ask — it demonstrates that sim2075 is the operational layer their framework paper (Gambhir et al. 2025, *Nature Communications*) calls for.

**Effort**: **S**. Pure documentation against material we already have.

### e. Shared elicitation infrastructure

Both models live or die on documented judgments: theirs are cross-impact scores with written justifications; ours are event probabilities, loadings, and Ω entries with mechanisms. A common judgment schema — claim, scale + semantics, rationale, sources, judge, date, confidence — would let judgments be reused across models: their Climate→Food block informs our Ω; our conditional event judgments inform their next matrix revision. Longer-term, this is the substrate for the crowd/LLM elicitation niche the landscape survey flags as unoccupied.

**Effort**: **S** for the schema; **M** for shared tooling. Only worth building past the schema stage if collaboration materializes.

---

## 3. Mismatch risks

1. **Descriptor-to-factor mapping is lossy.** PCM descriptors are global aggregates; sim2075 resolves 40 countries and 12 regional aggregates plus regional factors. Three descriptors (Polity Type, Inequality, Transportation) have no factor analog, and six of our twelve factors (the regional ones) have no descriptor analog. Any mapping covers perhaps half of each model's structure; conclusions must be scoped to the overlap.

2. **CIB judgments are not correlations.** Their −3..+3 scores are *directed influences between discrete descriptor states*, where magnitude encodes judgment *confidence* (not effect size), zeros are triply ambiguous (no influence / counterbalance / irreducible uncertainty), and a row-balance constraint forces judgments about one target descriptor to sum to zero. Ω entries are symmetric co-occurrence correlations of continuous latent factors. Direction is lost, discreteness must be aggregated, and confidence must not be silently reinterpreted as strength. Direction (b) is evidence *about signs and rough orderings*, never a mechanical transform. Treating it as more is the main way this integration could go wrong.

3. **Horizon mismatch: 2040 vs 2075.** PCM attractors are equilibria *in 2040*. sim2075 trajectories at 2075 may legitimately sit outside every 2040 basin — that is a finding (direction c), not a validation failure. The consistency check (a) must snapshot at 2040, not at end-of-run.

4. **Basin weight is not probability.** Succession-analysis "weight" counts inconsistent scenarios migrating to an attractor over an unweighted combinatorial space. Reading ~3M/4.05M as P(Illiberal Decline) ≈ 0.75 is a category error — Cascade explicitly assigns no probabilities. Direction (a) should compare *geometry* (where simulated mass clusters relative to attractors), and report our probability masses as new information, not as numbers their weights should have matched.

---

## 4. Engagement strategy

Cascade has committed to an open model: the v2.5 matrix with documented justifications for every judgment, published online, ScenarioWizard-reproducible, with an explicit invitation to enter alternative judgments and run sensitivity tests. That makes every direction above mechanically feasible without their participation — but participation is the prize; per the landscape survey, their team is the audience most likely to engage seriously with sim2075.

Sequence:

1. **Lead with (a), the consistency check.** Cheap, self-contained, flattering to both models regardless of outcome: convergence validates two independent judgment bases; divergence is a publishable puzzle. It also hands them the one number their method cannot produce — probability mass per attractor, framed per §3 risk 4 as new information rather than a rescoring of their basin weights — which is the clearest possible demonstration of complementarity.
2. **Include (d), the Stress–Trigger–Crisis crosswalk, in the first contact.** It costs little, flows value toward them, and frames sim2075 as operationalizing their published framework rather than competing with it.
3. **Propose (b), the Ω prior work, as the first joint project.** It requires their matrix at full depth (justification text, not just scores) and benefits from their read on the aggregation statistic — a natural co-authored methods piece.
4. **Hold (c) and (e) for an established relationship.** (c) is the flagship joint experiment ("what happens inside your basins after 2040"); (e) only pays off with sustained collaboration.

Audience: Homer-Dixon (framing/polycrisis theory), Kemp (existential-risk methods), Schweizer (CIB methodology — the right reviewer for the translation problems in §3).

---

## 5. Recommendation

Do regardless of engagement:

- **(a) Attractor consistency check** — external validation from an independent judgment base is worth having for its own sake, and the projection map is reusable for (c). Framed per §3 risk 4: compare attractor geometry and cluster membership of simulated 2040 states; report probability masses as sim2075's own contribution, never as numbers their basin weights should have matched. Do once simulation runs exist and their matrix is published.
- **(b) Ω comparison** — directly addresses the documented "no empirical calibration" limitation of [[methodology/reference/factor-correlation-matrix]]. Even a signs-only comparison is more external evidence than Ω currently has.
- **(d) Crosswalk** — small effort, doubles as sim2075 positioning material for any audience, not just Cascade.

Contingent on engagement: **(c)** (worth a solo pilot after (a), but its value is mostly as a joint experiment) and **(e)** (schema is cheap to draft; tooling only with a committed second user).

---

*Sources: PCM v2.5 technical synopsis (Aug 10, 2025, cascadeinstitute.org), verified figures in [[strategy/inputs/pcm-v25-synopsis-notes]]; [[strategy/inputs/public-landscape-survey]]; [[methodology/concepts/framework-overview]]; [[methodology/concepts/factor-correlation-structure]]; [[methodology/reference/factor-correlation-matrix]]; [[methodology/concepts/state-event-coupling]]*
