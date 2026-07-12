---
title: validation-notes-sketch
type: note
permalink: strategy/validation-notes-sketch
tags:
- strategy
- publication
- validation
- phase-2
- sketch
---

# Validation Notes Sketch

Sketches of the three Phase 2 published notes, not the notes. [[strategy/roadmap]] Phase 2 specifies three independent validation instruments, each ending in "a published note with method, results, and the catalog/parameter changes it produced." This document pins each note's question, method, skeleton, and success/failure framing now — before the engine exists — so that instrument design is settled when path ensembles arrive and the notes don't drift into post-hoc rationalization.

**What a sketch can and cannot contain.** Everything here is method and structure. No results, no numbers, no findings — those sections are marked `[RESULTS]` and stay empty until the Phase 1 engine produces ensembles. The sketches also invent no engine features: all three instruments are *consumers* of the v0.1 engine's outputs as specified by [[methodology/reference/simulator-architecture]] and [[methodology/project/implementation-guide]]; anything an instrument wants that the engine doesn't emit is a finding for the v0.2 backlog, not a requirement injected backward into Phase 1.

**Shared publication pattern.** Each note follows the same shape, so readers of one can navigate the others:

1. Question — what structural property of the model this instrument tests
2. Method — fully specified before results existed (this sketch is the timestamp)
3. `[RESULTS]`
4. Catalog diffs produced — every parameter change traced to a finding, reasoning attached
5. What this instrument cannot test — scope discipline

The notes share the engine but not each other: any order, stop after any of them, each stands alone ([[strategy/roadmap]] Phase 2).

---

## Note A — Sensitivity analysis: which parameters drive the tails?

**Working title:** "What moves the tails: sensitivity structure of a correlated-discontinuity model"

**Question.** Which events, parameters, and factors drive the output distribution — especially tail outcomes — and, critically, *how does that ranking partition across the model's declared tractability strata?* The note's thesis is not "here are the sensitive parameters" but "here is which conclusions rest on parameters we have documented we cannot know." This demonstrates the reporting discipline of [[methodology/concepts/tractability-boundaries]] in practice, which is the paper-relevant deliverable ([[strategy/methods-paper-sketch]] build-list item 4).

**Method** — inherits the analysis menu from [[methodology/project/development-roadmap]] §3.1–3.5 (the superseded plan's Phase 3, explicitly carried forward by [[strategy/roadmap]]):

| Analysis | Design |
|---|---|
| Event contribution (§3.1) | For runs in the worst 5% by selected output metrics: event frequency, event combinations, necessity/sufficiency screens for tail membership |
| Parameter perturbation (§3.2) | Tornado-style: re-run at each event's documented probability bounds and impact-magnitude bounds; rank by output movement |
| Correlation structure (§3.2–3.3) | Correlated vs. independent sampling (Ω and Λ on/off); which factors drive tail clustering; how much of tail mass is correlation-induced |
| Ω validation (§3.4) | Historical-proxy correlations vs. specified Ω entries; historical bad-year clustering (2008–09, 2010–11, 2020) vs. model-implied clustering; implied event correlations Σ = ΛΩΛᵀ + Ψ reviewed for double-counting |
| Country/variable importance (§3.5) | Which entity trajectories predict global outcomes; where outcomes depend on unmodeled dynamics (under-specification map) |

**The distinctive cut.** Every ranked parameter carries its tractability class from the specs. The headline exhibit is the tornado chart *partitioned by stratum*: results driven by high-tractability parameters are reported as model claims; results driven by declared-intractable parameters (Type 3 resolutions above all) are reported as conditional structure only. If a maximum-entropy default turns out to dominate an output, the honest statement is "the model cannot make this claim," and the note says so.

**Skeleton.** Question → tractability-stratified reporting rule (stated before results) → method per table above → `[RESULTS]` → catalog diffs (loading refinements, probability-band tightening where evidence supports it, v0.2 backlog promotions where an omission demonstrably matters) → what this cannot test (marginal correctness — sensitivity says what matters *within* the model, not whether the model is right).

**Failure framing.** "Everything is sensitive" is itself the finding — it bounds what the model can claim, and gets published as exactly that ([[strategy/roadmap]] Phase 2 failure modes). "Nothing is sensitive" would indicate degenerate dynamics and is a Phase 1 bug report, not a note.

**Dependencies.** Phase 1 engine only. First note to attempt: no external blockers, and its outputs (the under-specification map, the backlog promotions) feed the other two.

---

## Note B — PCM attractor consistency check

**Working title:** "Two judgment bases, one geometry? Projecting simulated 2040 states onto the Polycrisis Core Model's attractor space"

**Question.** Do sim2075's simulated 2040 world-states cluster where the PCM's three attractors (Illiberal Decline, Mad Max, Hope) sit in descriptor space? Two independently produced judgment bases — their 1,800+ cross-impact scores, our marginals/loadings/Ω — arriving at the same geometry would be meaningful mutual validation; divergence is a publishable puzzle. Direction (a) of [[strategy/pcm-integration-brief]], which is this note's full specification; this sketch fixes the publication shape.

**Method** (brief §2a, condensed):

1. **Projection map** — ~11 classification rules from sim2075 state variables to the 45 PCM descriptor states (per [[strategy/inputs/pcm-v25-synopsis-notes]], Appendix 1). Descriptors with no analog (Transportation) are dropped and the coverage loss stated. The map is the note's one new artifact and is publishable in the note as a table — it should be independently criticizable.
2. **Snapshot at 2040**, not end-of-run (brief §3 risk 3): N runs, project each 2040 state onto descriptor space.
3. **Geometry comparison**: basin membership per projected run (using their published matrix and succession analysis), and distance of the modal simulated state from each fully consistent scenario.
4. **The bonus number**: fraction of runs per attractor is a genuine probability-mass estimate — reported as *new information alongside* their basin widths, never as a rescoring of them.

**Guardrails written into the note** (brief §3, restated as commitments): the mapping is lossy and conclusions are scoped to the overlap; CIB judgments are not correlations and no mechanical transform is implied; 2075 trajectories legitimately exit 2040 basins (that is direction (c) material, not a failure); basin weight is not probability, and the note never reads ~3M/4.05M as P ≈ 0.75.

**Skeleton.** Question → the complementarity framing (their static consistency, our dynamic trajectories; from the brief's core framing) → projection map (full table) → method → `[RESULTS]` (cluster geometry; mass per attractor; divergences itemized) → catalog diffs (a divergence that traces to a specific loading or Ω entry becomes a documented revision or a documented disagreement) → what this cannot test (their basin weights, our marginals — only joint geometry).

**Both outcomes publish.** Convergence: independent judgment bases agree on where 2040 mass sits. Divergence: localize it — which descriptor, which projection rule, which parameter family — and publish the puzzle. The note fails only if the projection map itself can't be made defensible, which is a finding about descriptor-level commensurability and worth a shorter note in its own right.

**Dependencies.** Phase 1 engine + Cascade's published matrix (external; can block indefinitely — it's one instrument of three, not a gate). The projection map can be drafted and even published *before* their matrix lands; only basin assignment waits.

**Sidecar deliverable.** The Stress–Trigger–Crisis crosswalk (brief direction (d)) — their 14 stresses / triggers / 9 vital systems mapped onto our factors, pressure variables, and causal types — is small, engine-independent, and per the brief's engagement strategy travels *with* this note as the first-contact package for Cascade. Draft it alongside; it needs no sketch of its own.

---

## Note C — LLM path-plausibility audit harness

**Working title:** "Auditing sampled futures: can LLMs localize structural incoherence to model parameters?"

**Question.** Rendered as narrative skeletons, do sampled trajectories contain structural incoherence that LLM auditors can (a) detect and (b) *localize to the specific parameter that produced it*? This is the core convergence practice of [[strategy/roadmap]] ("What the product is," commitment 3), operationalized — and the only instrument of the three that reaches joint-distribution errors (correlation structure, cascade timing, durability interactions) that no marginal check touches. Per [[strategy/inputs/public-landscape-survey]] §6, the niche — LLMs coupled to a structured Monte Carlo world model — is publicly unoccupied.

**Method.**

1. **Fixed rendering format.** Paths render into a stable, versioned textual format: annual timeline of fired events with timing, the state deltas that preceded them (pressure variables, window flags), active-shock decay status, and transmission steps between coupled events. Design variables to settle in a pilot: window length (full 50-year path vs. 5–10-year slices — the roadmap's failure-mode note already anticipates narrower windows), state verbosity, and whether renders include the *reasons* (factor draws) or withhold them so auditors judge the surface story only. Format versions are pinned per audit round; complaints are only comparable within a version.
2. **Incoherence taxonomy** (the audit prompt's vocabulary — auditors must classify every complaint):
   - *Missing transmission step* — consequence fires with no represented mechanism ("financial crisis → EU fragmentation in the same year with no transmission step")
   - *Timing implausibility* — sequence compresses or stretches beyond mechanism speed
   - *Durability violation* — an impact decays or persists contrary to its type
   - *Correlation implausibility* — co-occurrence with no shared driver, or conspicuous non-co-occurrence
   - *State–event contradiction* — event fires from a state that should have gated it
3. **Routing schema.** Every complaint either attributes to a parameter address — a marginal, a loading, an Ω entry, a cascade magnitude, an impact row/durability type, a missing event or transmission step (catalog gap) — or is logged `unattributable`. The unattributable rate is a headline metric, not discarded noise — and the unattributable stream is a *discovery channel*: a complaint that can't route to any existing parameter is the audit-time signature of the line-373 failure class (a missing event or state variable), so adjudicated-real unattributable complaints feed the catalog backlog under the same mandatory rule as cascade-list flags ([[strategy/emergent-ideas]] idea 4).
4. **Human adjudication.** Each attributed complaint is adjudicated (valid / invalid / valid-but-out-of-scope-for-v0.1 → v0.2 backlog). Valid complaints become catalog diffs whose commit reasoning carries the complaint — the audit trail *is* the contribution process working ([[strategy/roadmap]] "public interface split").
5. **Ensemble design.** Multiple models audit the same rendered paths; inter-model agreement per taxonomy class measures whether complaints are properties of the paths or of the auditors.

**Metrics.** Complaint rate per rendered path-year; attribution rate; adjudicated-valid rate; inter-model agreement; catalog diffs produced per audit round; and complaint-class distribution (which joint-distribution errors dominate — this is the number that tells us where the model's structure is weakest).

**Skeleton.** Question → why path-level auditing inverts LLM forecasting (judging story coherence, not knowing the world — roadmap commitment 3) → rendering format (versioned spec) → taxonomy and routing schema → adjudication protocol → `[RESULTS]` → catalog diffs → what this cannot test (marginal correctness; anything the render doesn't expose).

**Failure framing.** If complaints won't localize: narrow the windows, tighten the format, re-run. If it still fails, "LLM audits at current capability cannot localize incoherence" is a publishable negative result in an unoccupied niche ([[strategy/roadmap]] Phase 2 failure modes) — the note ships either way.

**Dependencies.** Phase 1 engine. The rendering format and taxonomy can be pilot-tested on *hand-authored* paths (including a hand-rendered Third Gulf War path, which doubles as a calibration case with a known-true structure) before any engine output exists.

---

## Publications described in the strategy documents but deliberately not sketched

For completeness — the full publication inventory across the strategy layer, and why the rest stays unsketched:

| Publication | Described in | Why not sketched now |
|---|---|---|
| Methods paper | [[strategy/methods-paper-sketch]] | Already sketched — the Phase 3 specification |
| Launch essay | [[strategy/launch-essay-sketch]] | Sketched alongside this document |
| Three validation notes | this document | — |
| Shorter war-validation companion note (the "split" option) | methods-paper-sketch §6 open questions | Blocked on Schuyler's single-vs-split decision and the wiki-citability question; its content already exists in [[strategy/inputs/war-validation-report]], and a sketch would duplicate the methods paper's §vi until the split is decided |
| Narrower technical companion for *Risk Analysis* | methods-paper-sketch §2 | A fallback contingent on venue outcomes; sketching it now is premature by the roadmap's own evidence discipline |
| Co-authored Ω-prior methods piece with Cascade | [[strategy/pcm-integration-brief]] §2b, §4 | Contingent on engagement materializing and on their matrix publishing at full depth; the brief already specifies the method |
| Phase 4 pilot elicitation round note | [[strategy/roadmap]] Phase 4 | Contingent on a community existing; Phase 4 is explicitly not planned for |

The rule applied: sketch what has a standing specification and no external gate; leave contingent publications to their gates.

## Sources

- [[strategy/roadmap]] — Phase 2 specification; failure modes; the evidence gate discipline
- [[methodology/project/development-roadmap]] §3 — inherited sensitivity-analysis menu (Note A)
- [[strategy/pcm-integration-brief]] — Note B's full specification; mismatch risks; engagement sequence
- [[strategy/inputs/pcm-v25-synopsis-notes]] — primary-sourced PCM figures for Note B
- [[strategy/inputs/public-landscape-survey]] §6 — the unoccupied LLM-audit niche (Note C)
- [[strategy/methods-paper-sketch]] — build-list items 4–5 consume Notes A–B
- [[methodology/concepts/tractability-boundaries]] — Note A's reporting discipline
- [[methodology/reference/simulator-architecture]], [[methodology/project/implementation-guide]] — the frozen engine contract all three notes consume
