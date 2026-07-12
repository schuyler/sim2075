---
title: roadmap
type: note
permalink: strategy/roadmap
tags:
- strategy
- roadmap
- planning
- open-source
- llm-convergence
---

# Roadmap: sim2075 as Open Tooling and Convergence Practice

The plan for pursuing sim2075 as a set of free and open tools refined in public, and as feedstock for an "LLM + structural world model" convergence practice. Synthesizes [[strategy/sim2075-third-gulf-war-interaction]], [[strategy/methods-paper-sketch]], [[strategy/pcm-integration-brief]], and [[strategy/inputs/public-landscape-survey]].

---

## Governing constraint

This is a free and open project. It will never produce income and doesn't need to; there is no revenue requirement anywhere in this plan. The only existential risk is author attention moving elsewhere. The design consequence is absolute:

**Every phase ends in a complete, standalone artifact. No phase's value is contingent on the next phase happening.**

If the project stops after any phase, what exists at that point is finished, published, and useful on its own. Phases are ordered by dependency, but nothing below is a down payment on something later.

## What the product is

sim2075 is a narrative **generator**, not a set of narratives. Technically: a semi-Markov process on a rich state space. The process is memoryless conditional on state, and everything that would make history matter is pushed into state variables — pressure levels, window flags, decay clocks, actor behavioral histories, ratchet/lock-in variables, duration clocks for aftermath sojourns. Each Monte Carlo run samples a path through that space, and a sampled path is a narrative skeleton. Any narrative we publish is a regenerable demonstration of the machinery, never the product itself.

Three commitments follow:

1. **Import baselines, export narratives, compete in neither.** Type 4 / trend baselines are borrowed from SSP/IFs public data — they have industrial-scale calibration, and building our own would be a worse version of free data. Importing also confines our judgments to the discontinuity layer, which strengthens the epistemology: every number we own is a documented judgment about discontinuities, not a rival trend model. (Per [[strategy/inputs/public-landscape-survey]] Assessment (b): don't compete on trend depth, short-horizon prediction, marginal elicitation, or qualitative narratives.)

2. **The public interface split.** The engine plus the YAML schema are stable, small, boring infrastructure. The event catalog is the community-editable layer. A disputed probability is a diffable YAML field with documented reasoning attached — the architecture makes parameter disagreement productive rather than rhetorical.

3. **The LLM convergence practice.** The core loop is *path-level plausibility auditing*: LLMs audit sampled trajectories for structural incoherence ("financial crisis → EU fragmentation in the same year with no transmission step"); every complaint is routed back to the specific parameter that produced it; a human adjudicates. This inverts typical LLM forecasting — instead of asking the model to know the world, it asks it to notice when a story doesn't hang together, a better-matched task. It is also the validation method for an otherwise unvalidatable model: humans and LLMs can judge sequence coherence even when they can't judge marginal probabilities, and sampled paths expose joint-distribution errors (correlation structure, cascades, durability) that no marginal check reaches. Secondary LLM roles: parameter elicitation, narrative rendering of paths.

## Audience and evidence

The Third Gulf War wiki is already public and drew attention from international-geopolitics readers and energy-market dabblers. That audience is the seed community for the catalog layer.

The wiki is also a first-class methodological asset: a **timestamped public record** of real-time predictions with confirmation scoring, misses included — the Day-11 repricing call confirmed Day 12, the Day-25 Passover-window call within 48 hours of actual, the Day-84 OPG-predicts-cycle-9 bet won, the ground-campaign hypothesis scored as a failure. This upgrades the methods paper's evidence class from "author reports" to "check the record," and every phase below that touches the war treats it that way.

## Funding

Not needed. Noted for completeness: Open Philanthropy funds the forecasting/GCR-methods intersection, and a small grant could later buy compute for large-scale path auditing or catalog-maintenance help. Zero effort on this now; revisit only if Phase 4 materializes.

---

## Relationship to prior roadmaps

This document is now the project plan. Reconciliation with the two pre-war planning documents:

| Prior document | Disposition |
|---|---|
| [[methodology/project/development-roadmap]] | **Superseded as the plan.** Its Phase 1 (event catalog) is complete at Level 1 scope (~30 events; see [[index]]) — short of its own 40–60-event success criterion; the gap is Phase 0 and ongoing catalog-growth work, not a blocker. Its Phase 2 (prototype) becomes Phase 1 here, rebuilt around public-from-first-commit and imported baselines. Its Phase 3 (sensitivity analysis) is absorbed into Phase 2 here as one validation instrument among three. Its Phases 4–6 (iterative expansion, calibration, production use) are dropped as phases: expansion becomes continuous catalog-layer work driven by audit findings; "calibration" is reframed per [[methodology/concepts/epistemology]] — parameters are documented judgments checked by the Phase 2 instruments, not calibrated quantities; "production use" is replaced by the open-tool framing above. Its design principles (start minimal, events before dynamics, sensitivity guides investment, working code beats specification) are inherited intact. |
| [[methodology/concepts/implementation-roadmap]] | **Superseded as engine specification** by [[methodology/reference/simulator-architecture]] (the ADRs) and [[methodology/project/implementation-guide]] (pinned decisions, build order, gates), which postdate it and define v0.1 scope authoritatively. Its v2.0 feature list survives as the candidate backlog: unscheduled, promoted only if a Phase 2 instrument demonstrates an item matters. |
| [[methodology/reference/simulator-architecture]] + [[methodology/project/implementation-guide]] | **The engine specification and execution plan — normative.** Phase 1 below *is* these documents: the guide's data track (4.2–4.4) and engine track (E0–E10) are Phase 1's work breakdown. Where this roadmap's prose and those documents differ on engine matters, they win. |
| [[index]] "Next Steps" | Updated — now points here. |

---

## Phase overview

| Phase | Name | Standalone artifact | Depends on |
|---|---|---|---|
| 0 | Absorb the war | Remediated catalog + public launch essay | Nothing — all inputs exist |
| 1 | The engine, built in the open | Runnable engine + frozen schema + catalog | Phase 0 (content only) |
| 2 | Validation instruments | Three self-contained published notes | Phase 1 engine |
| 3 | The methods paper | Public preprint + journal submission | Phases 0–2 |
| 4 | Elicitation at scale *(optional)* | Judgment schema + pilot elicitation round | A community that has materialized |

---

## Phase 0 — Absorb the war

**Purpose.** Incorporate the Third Gulf War's lessons into the catalog and methodology before building anything on top of them, and convert the interaction analysis into the project's public launch. [[strategy/sim2075-third-gulf-war-interaction]] is the specification; this phase executes its §4 fixes and §3 corrections.

**Work items.**

1. **Promote the self-flagged missing events.** Add `ISRAEL_IRAN_WAR` / `US_IRAN_WAR` (one event — the final ID is settled at authoring), `STRAIT_OF_HORMUZ_CRISIS`, and `GULF_STATE_ATTACKS` as first-class Type 3 events — all three are named as "not in catalog" in a single cascade comment (`events/geopolitical/iran-regime-change.md:373`) and were left unactioned. They are textbook Type 3 window/resolution events (interaction doc §1) and **fit the current [[methodology/reference/event-yaml-schema]] as-is** — author them against it and add them to the Task 4.2 migration table, so they compile into the v0.1 engine like any other event. Each spec should note that its single-resolution shape deliberately compresses the multi-clock structure the war exposed (interaction doc §4 fix 3) — the uncompressed form is a v0.2 backlog item (item 5 below). Adopt the process rule permanently: any event named in a cascade list but absent from the catalog is a mandatory backlog item.
2. **Precursor-war hazard multipliers and `OIL_SUPPLY_SHOCK` reclassification.** Record the reclassification case (flat Type 1 → hybrid: base stochastic rate plus a state-conditioned geopolitical pathway — time-since-last-conflict-with-same-actor, arsenal reconstitution, negotiation-collapse risk) in the event's prose and probability-evolution discussion now. The YAML keeps `causal_type: 1` for v0.1 — the schema and the frozen `CompiledCatalog` contract ([[methodology/project/implementation-guide]] §4.1) represent a single generating mechanism per event — and the mechanical reclassification lands with schema v0.2 (see item 5).
3. **State-vector widening — prose now, schema v0.2 for the rest.** Document the variable classes the war showed are load-bearing: actor behavioral histories (the §3.2 repeated-actor base rates — OPG-style within-episode counts), ratchet/lock-in variables (insurance floors, alliance-credibility damage), and duration clocks for aftermath sojourns. Anything expressible as an ordinary engine-maintained state variable under the current schema (the `years_since_irregular_transition` pattern, per [[methodology/reference/expression-language]] §6) may be added now; anything requiring new schema constructs waits for v0.2. **Scope pin:** "added now" means added to the state catalog and event specs — the v0.1 engine's entity/variable axes stay pinned to [[methodology/reference/mvp-dynamics-scope]], and a new variable enters the engine only through an explicit revision of that scope, never as a side effect of event authoring (the implementation guide treats the axes as a frozen seam).
4. **Methodology updates from §3.** Write the two boundary corrections into [[methodology/concepts/tractability-boundaries]] (expectation-mediated transmission; repeated-actor partial tractability — the latter framed as a mechanism hypothesis with one supporting case, not a calibrated rule); record the depletion-stock proposal in [[methodology/reference/causal-types]] as a candidate Type 2 sub-pattern; widen demand-elasticity uncertainty bands per §3.4. Engine-neutral prose — no sequencing constraint.
5. **Open the schema v0.2 backlog.** The war lessons that require new schema constructs — hybrid causal types (item 2), multi-front events with actor-specific resolution clocks, per-component transmission thresholds/hysteresis (interaction doc §4, items 3–4), behavioral-history/ratchet/duration-clock constructs beyond plain state variables (item 3), and decay-to-floor ("persistent / floor") durability for impact rows — the war's "damage a ceasefire cannot fix" class (interaction doc §2d), which the current five durability types can only approximate as `permanent` — are recorded as a named **schema v0.2 backlog**, not built into v0.1. Promotion out of the backlog is gated the same way as the old plan's v2.0 features: a Phase 2 instrument has to show the omission matters. This applies the roadmap's own evidence discipline to its own wishlist.
6. **The public launch essay** (sketched: [[strategy/launch-essay-sketch]]). Adapt the interaction document into "what the Third Gulf War taught a model built 60 days before it started." It leads with the model's failure — the war wasn't a first-class catalog event despite the catalog's own self-flag — matching the wiki's credibility-through-honesty tone, and introduces the project to the wiki's existing audience. Before publication, re-verify every load-bearing wiki quote and date against the wiki itself: the strategy inputs are second-hand digests, and one day-anchor in them has already needed correcting.
7. Update [[index]] Next Steps to point at this roadmap.

**Standalone artifact.** The remediated catalog (a better set of documented judgments than existed before, useful as pure research prose even with no engine) plus the published essay.

**Dependencies.** None. Interaction doc, [[strategy/inputs/war-validation-report]], and [[strategy/inputs/oil-taco-digest]] all exist.

**Failure modes.** State-vector widening snowballs into a full schema redesign — mitigated by item 3's scope rule. The essay stalls on how much wiki material is quotable in public — resolvable by scoping to what's already public. If the phase stalls partway: each remediated event stands alone, and the essay is publishable before remediation completes (it describes the fixes; it doesn't require all of them landed).

---

## Phase 1 — The engine, built in the open

**Purpose.** Turn the specs into a runnable sampler and establish the engine/catalog interface split in public. The repo is already public — the refinement process is the point, not a threat to it.

**Work items.**

1. **The v0.1 engine, exactly as specified.** The design is [[methodology/reference/simulator-architecture]] (ADRs: vectorized stateful stepper, Gaussian copula over Ω, unified firing kernel, active-shock ledger, compiled expression language) and the execution plan is [[methodology/project/implementation-guide]] (data track 4.2–4.4; engine stages E0–E10, reference-implementation-first, fixture-gated). This roadmap adds nothing to those documents and does not restate them; the conceptual summary is that each Monte Carlo run samples a path through a rich state space — a semi-Markov process where everything history-dependent lives in state — and emits event sequences with timing and state snapshots.
2. **Imported baselines.** Type 4 trend dynamics come from SSP/IFs public data as exogenous inputs (v0.1 seeds trend rates from IMF WEO / UN WPP per the guide's data track). The engine does not contain a trend model.
3. **Schema freeze — the current schema, versioned.** [[methodology/reference/event-yaml-schema]] as it stands today is the v0.1 engine/catalog contract; the Phase 0 war events are authored against it (they fit — see Phase 0 items 1–2). The schema-breaking war lessons live in the Phase 0 item 5 **v0.2 backlog** and land, if the Phase 2 instruments justify them, as a versioned schema revision with a migration path. Schema changes after freeze are versioned, deliberate, and rare.
4. **The interface split, materialized.** Engine and schema in one small, stable layer; the catalog as the data layer with a documented contribution path. A catalog PR that changes a probability must change the attached reasoning — that's the whole review standard.
5. **Licensing and hygiene.** Apply the decided licenses: BSD (2- or 3-clause) for the engine — the 2-vs-3-clause choice is the only open question — and CC BY 4.0 for catalog and prose. CI that validates every catalog file against the schema. A README that states what the tool is and is not (scenario exploration under documented judgment, not forecasting).

**Standalone artifact.** A runnable engine + frozen schema + the 29-event (post-Phase 0, 32+) catalog. Anyone can clone it, run it, and get trajectory ensembles; anyone can fork the catalog and disagree with a parameter legibly.

**Dependencies.** Phase 0, softly — engine development can start against the pre-remediation catalog; the remediated catalog is what ships.

**Failure modes.** The classic one: dynamics scope creep — building baseline models instead of importing them, or reaching for deferred features (sub-annual steps, full cascade propagation, the v0.2 schema backlog) before any instrument shows they matter. The defenses are the implementation guide's guardrails ("no feature invention," frozen seams) and the evidence gate on the v0.2/v2.0 backlogs; cross either only on Phase 2 evidence. If the phase stalls: the frozen schema plus machine-readable catalog is itself a complete artifact — a citable, forkable corpus of documented judgments — and even a partial engine (copula sampling without state evolution) demonstrates the O(n×k) elicitation argument concretely.

---

## Phase 2 — Validation instruments

**Purpose.** The model is unvalidatable in the calibration sense; these are the instruments that test its structure anyway. Three independent instruments, each ending in its own self-contained published note (sketched: [[strategy/validation-notes-sketch]]). They share the engine but not each other — do them in any order, stop after any of them.

**Work items.**

| Instrument | What it does | Notes |
|---|---|---|
| **Sensitivity analysis** | Tornado-style: which outputs move under marginal/loading perturbation; correlated vs. independent sampling; which factors drive tail clustering. | Demonstrates the "conclusions depend on tractable vs. intractable parameters" reporting discipline in practice. Inherits the analysis menu from the old plan's Phase 3 (§3.1–3.5 of [[methodology/project/development-roadmap]]). |
| **PCM attractor consistency check** | Project simulated 2040 states onto the PCM descriptor space; compare cluster *geometry* against their three attractors; report probability mass per attractor as new information, never as a rescoring of their basin weights. | Direction (a) of [[strategy/pcm-integration-brief]] — cheap, self-contained, and the natural opener with Cascade regardless of outcome (convergence validates two independent judgment bases; divergence is a publishable puzzle). The brief's PCM figures are primary-sourced via [[strategy/inputs/pcm-v25-synopsis-notes]], with unverified items fenced there. Externally blocked on their matrix publication. |
| **LLM path-plausibility audit harness** | Render sampled paths in a fixed format; LLMs flag structural incoherence; each complaint routes to the parameter that produced it (a loading, a cascade magnitude, a missing transmission step); a human adjudicates and the catalog diff carries the reasoning. | The core convergence practice from the preamble, operationalized. This is the instrument that reaches joint-distribution errors — correlation structure, cascade timing, durability — that no marginal check touches. The landscape survey (§6) found this niche unoccupied. |

**Standalone artifact.** Each instrument is a published note with method, results, and the catalog/parameter changes it produced. Three notes, individually complete.

**Dependencies.** Phase 1 engine (all three consume path ensembles). The PCM check additionally waits on Cascade's published matrix.

**Failure modes.** The audit harness produces noise — complaints that can't be attributed to a parameter; the fixes are narrower path windows and a stricter rendering format, and even a negative result ("LLM audits at current capability can't localize incoherence") is a publishable note. The PCM check can be blocked indefinitely from outside; it's one instrument of three, not a gate. Sensitivity analysis finding "everything is sensitive" is itself the finding — it bounds what the model can claim. Any completed instrument stands alone.

---

## Phase 3 — The methods paper

**Purpose.** Assemble Phases 0–2 into the paper specified by [[strategy/methods-paper-sketch]]: catastrophe-modeling techniques for the polycrisis, the latent-factor copula as the fix for what killed probabilistic cross-impact, with the war as a documented out-of-sample stress test.

**Work items** — the sketch's pre-submission build list, reconciled against this roadmap:

| Build-list item | Status under this roadmap |
|---|---|
| 2. Working prototype | Phase 1 |
| 3. Catalog remediation | Phase 0 |
| 4. Sensitivity analysis | Phase 2 |
| 5. Worked PCM comparison | Phase 2 |
| 8. Licensing/openness decision | Phase 1 (and materially strengthens the paper at *Futures*/*Global Sustainability*) |
| 1. Formal copula/factor specification writeup | **This phase** |
| 6. Coherence/burden demonstration (pairwise conditionals going incoherent vs. factor elicitation) | **This phase** — the paper's central technical argument |
| 7. War-validation appendix | **This phase.** Treat the wiki's timestamped record as a first-class methodological point: dated changelogs establish the 60-day precedence claim, and the confirmation scoring — including the scored misses — makes the evidence "check the record," not "trust the author." Resolve how much of the wiki is citable. |

Plus the sketch's open questions for Schuyler before drafting: single paper vs. split, wiki citability, author list, Cascade pre-submission contact. Venue order per the sketch: *Futures*, then *Global Sustainability*, *TFSC*, *Risk Analysis*.

**Standalone artifact.** A public preprint, plus a journal submission. The preprint is the artifact; the submission is upside.

**Dependencies.** Phases 0–2. The paper's §vi claims the war corrections were incorporated, so they must be (Phase 0); it cannot ship on specs alone (Phase 1); its evidence sections consume the Phase 2 notes.

**Failure modes.** Review cycles outlasting author attention — which is why the preprint, not acceptance, is the completion criterion. Wiki-anonymization scope disputes stalling the appendix — decide the citability question *first*, before drafting. If the phase stalls entirely, Phases 0–2 already published everything the paper would assemble; the paper is a synthesis, not the sole carrier of any result.

---

## Phase 4 — Elicitation at scale *(optional, aspirational)*

**Purpose.** If — and only if — a community materializes around the catalog, the paper, or the audit practice, scale the elicitation substrate: model parameters as resolvable questions for crowds and LLM ensembles, and a shared judgment schema with the PCM. This phase is explicitly not planned for; it is described so that Phases 0–3 leave the door open.

**Work items** (sketched, not committed):

1. **Judgment schema** — claim, scale and semantics, rationale, sources, judge, date, confidence — shared with Cascade if the relationship from Phase 2 developed (direction (e) of [[strategy/pcm-integration-brief]]); useful solo regardless.
2. **Parameters as questions.** A generator that turns any catalog YAML field into a documented elicitation question, Metaculus-style but resolving *model parameters* rather than world events — the unoccupied niche flagged in [[strategy/inputs/public-landscape-survey]] (c)4.
3. **LLM ensemble elicitation runs** against the question set, reconciled with XPT/Metaculus-class marginals where they exist.
4. If scale ever demands it: the Open Philanthropy note in the preamble — a small grant for audit compute or catalog maintenance.

**Standalone artifact.** The judgment schema plus one published pilot elicitation round.

**Dependencies.** A community. Not a phase output — an external event this plan can't schedule.

**Failure modes.** The honest one: nobody shows up. By design, that costs nothing — Phases 0–3 are each complete without this, and the schema (item 1) is cheap enough to draft on its own merits if Cascade collaboration alone warrants it.

---

## Sources

- [[strategy/sim2075-third-gulf-war-interaction]] — Phase 0 specification
- [[strategy/launch-essay-sketch]] — Phase 0 item 6 (launch essay) sketch
- [[strategy/validation-notes-sketch]] — Phase 2 published-notes sketch
- [[strategy/methods-paper-sketch]] — Phase 3 specification
- [[strategy/pcm-integration-brief]] — Phase 2 (PCM check) and Phase 4 (shared schema); figures primary-sourced via [[strategy/inputs/pcm-v25-synopsis-notes]]
- [[strategy/inputs/public-landscape-survey]] — positioning and niches
- [[methodology/reference/simulator-architecture]] — engine design (ADRs; normative)
- [[methodology/project/implementation-guide]] — engine execution plan (normative)
- [[methodology/concepts/implementation-roadmap]] — superseded engine spec; v2.0 candidate backlog
- [[methodology/project/development-roadmap]] — superseded plan (design principles inherited)
