---
title: sim2075-third-gulf-war-interaction
type: note
permalink: strategy/sim2075-third-gulf-war-interaction
tags:
- strategy
- validation
- third-gulf-war
- tractability
- causal-types
---

# Sim2075 × Third Gulf War: How the Model and the War Interact

Synthesis of [[strategy/inputs/war-validation-report]] and [[strategy/inputs/oil-taco-digest]] against [[methodology/concepts/tractability-boundaries]], [[methodology/concepts/epistemology]], and [[methodology/concepts/framework-overview]]. The war ran Feb 28–June 17 2026 (Islamabad MOU, Day 110); the sim2075 event specs under test were finalized ~60 days before onset.

---

## 1. Verdict

**The failure was curation, not architecture.** The US/Israel–Iran war was not a first-class event in the catalog. It existed only as appendages: a 10% branch of `IRAN_REGIME_CHANGE` (`external_intervention_trigger`), strike branches of `IRAN_NUCLEAR_ACQUISITION`, and a named trigger scenario inside `OIL_SUPPLY_SHOCK`. The composite path probability the catalog would have assigned the observed world is roughly **0.5–1%/yr** — thin for the single most precondition-laden interstate war on Earth as of December 2025.

The specs knew this. A single cascade comment in `events/geopolitical/iran-regime-change.md` (line 373) names all three missing war-hub events: *"STRAIT_OF_HORMUZ_CRISIS, GULF_STATE_ATTACKS, ISRAEL_IRAN_WAR not in catalog."* That is not an architectural gap; it's an unactioned backlog item the model wrote to itself.

Everything downstream of onset — regime survival, correlated hazard elevation, durability splits, and the war's actual hinge variable — the framework's existing machinery handled correctly once the war is admitted as a Type 3 event. Where the framework lacked vocabulary was around the mechanism that decided the war's *outcome*: the TACO Clock. That mechanism yields the **two boundary corrections** this document exists to record (§3.1–3.2), plus a proposed causal-types addition and a calibration lesson (§3.3–3.4).

Schuyler's own read matches the evidence: the Small-N Actor Problem dominated from day one, oil markets were the real surprise, military outcomes tracked expectations, and the war's outcome hinged entirely on one man's tolerance for continuing it.

---

## 2. What the war validated

### (a) Type 3 tractability doctrine, validated by the harshest possible test

[[methodology/concepts/tractability-boundaries]] claims resolution probabilities are low-tractability while aftermath consequences are moderate-to-high tractability. The Third Gulf War research wiki is the strongest available test of that claim, because it had far more information than any prior model — daily hidden-parameter tracking, ~40 dated assessments, direct sourcing to principals — and still split exactly along the predicted line:

- **Resolution missed.** The wiki held escalation (B2) as modal for 37 days; the war ended in the deal branch (B1) it had priced at 11–20%. Separately, it documented "The Third Option Pattern": seven instances of mispricing Iran's binary choices.
- **Aftermath repeatedly beat institutional sources.** Fertilizer lock-in, oil-price-fiction mechanics, infrastructure irreversibility, and the strait-reopening two-barrier model were confirmed weeks ahead of Goldman, IEA, and Rystad (Goldman needed 4 revisions and 81 days to reach the supply picture the wiki had on Day 6).

This is the tractability stratification working exactly as designed, in the wild, under maximal information: **the framework predicted its own failure mode correctly.** More research does not buy resolution predictability — see [[methodology/concepts/tractability-boundaries]] on "Effort Justification" as a failure mode. The wiki is a 1,000-hour demonstration of that exact point.

### (b) Discontinuity boundary rules

`causal-types.md`'s Common Mistakes section states explicitly: "Khamenei dying and being replaced by another Supreme Leader through normal processes ≠ Iran regime change," and "regime survives crisis = sub-threshold." Khamenei was assassinated; Mojtaba succeeded within ~8 days under IRGC coercion; the regime governs the same territory in the same institutional form. `IRAN_REGIME_CHANGE` correctly did not fire.

More pointedly: the spec's own *Case Against* argument — a strike "might trigger rally-around-flag rather than collapse" — was right, **against the actual operating belief of the people who launched the war** (the war's planners appear to have expected the strike to produce more instability than it did; the regime-change illusion the war's own NIC explicitly rejected). A model built from outside the decision got the boundary condition right where insiders' working assumption was wrong.

### (c) Correlated-factor signature

One F_MENA/F_GPT shock elevated hazard simultaneously across `TAIWAN_CONFLICT`, `US_CHINA_ECONOMIC_RUPTURE`, dollar/financial stress, `SAUDI_NUCLEAR_ACQUISITION`, and `US_CONSTITUTIONAL_CRISIS` — none of which fired. That is precisely what a high-factor draw is supposed to do: correlated probability elevation, not deterministic cascade. The one *negative* cascade specified — external threat consolidates Gulf regimes (`SAUDI_REGIME_INSTABILITY` ×0.7) — also played out: GCC states absorbed strikes without regime stress.

### (d) Durability typing

[[methodology/concepts/framework-overview]]'s durability table (permanent / decaying / maintenance-required) maps cleanly onto the war's central economic lesson — "damage a ceasefire cannot fix":

| Impact | Durability | Evidence |
|---|---|---|
| Oil spot price | Decaying, short half-life | Round-tripped to ~$80 within days of the MOU |
| Ras Laffan LNG capacity | Decaying, long half-life | 3–5 year repair, force majeure |
| Shipping-insurance regime | Persistent / floor | Actuarial closure; war risk premiums did not reset |
| Alliance credibility (US security guarantees) | Persistent / floor | Feeds `SAUDI_NUCLEAR_ACQUISITION` window logic directly |
| Khamenei, ~40 officials, Lebanon casualties | Permanent | Deaths — never decay by definition |

The framework's insistence that durability is a property of the *impact type*, not the event's valence, is exactly what separates "gas fell 7 straight weeks post-MOU" (real but borrowed relief) from "SPR at a 42-year low" (a floor that a handshake does not restore).

---

## 3. What the war teaches the methodology

This is the substantive addition to the framework: two boundary corrections that revise [[methodology/concepts/tractability-boundaries]] (§3.1–3.2), one proposed addition to [[methodology/reference/causal-types]] (§3.3), and one calibration lesson (§3.4).

### 3.1 Boundary correction: expectation-mediated transmission

The tractability-boundaries doctrine currently stratifies by *domain* (physical dynamics vs. small-N decisions). The war shows the same event can have transmission channels that sit on opposite sides of the boundary depending on **whether the channel runs through a forecast of the intractable variable**.

Physical channels tracked as modeled: barrels stranded, mines laid, refineries destroyed, displacement flows, crack spreads. The wiki's Day-6 supply-side numbers matched Goldman's Day-87 numbers. But market *price formation* was not a physical channel — it was systematically contaminated by the Small-N actor:

> "The market is pricing Trump's psychology, not barrels." — [[strategy/inputs/oil-taco-digest]]

Seven-plus "Oil Price Fiction" cycles were episodes where price decoupled from physical supply because futures are, definitionally, "a bet on what oil will cost later, filtered through sentiment, hedging flows, and political signals." Blas's calibration: a ~$125 "real" price against an $83.85 WTI print during the same window, a mispricing driven by an institutionalized leak channel (Trump → Axios → market), sovereign FX-defensive shorting (Japan), and possible front-running of presidential posts — mechanisms with no representation in either the physical-transmission model or the small-N-actor model alone.

**Rule to add to [[methodology/concepts/tractability-boundaries]]:** *Transmission channels that run through expectations of a low-tractability variable inherit that variable's intractability, regardless of how tractable the underlying physical process is.* A channel's tractability is not fixed by its subject matter (oil, in this case) but by whether it is a direct physical linkage or a forecasting market sitting on top of a Small-N actor. Practically: price-based impact vectors for events with a dominant Type-3 resolution variable should be flagged low-tractability even when the physical impact vector for the same event is high-tractability. The oil digest states the generalizable form directly: *"structural consequences conditional on decisions" holds for physical transmission much better than for market transmission, because markets are themselves forecasting the intractable actor.*

### 3.2 Boundary correction: repeated-actor partial tractability

[[methodology/concepts/small-n-actor-problem]] treats Type 3 resolution as uniformly intractable. The war shows a real gradient within that category: a *repeated* small-N actor generates its own behavioral base rate that is tractable even though the underlying psychology is not.

The TACO Clock's "OPG" (Operational Pause-and-Go) pattern — eight stand-down cycles, zero conversions to sustained kinetic action, by the time a ninth cycle was bet on and confirmed (Day 84) — is a base rate built from the actor's *own repeated behavior*, not from psychological modeling or external analogues. It predicted the **class** of outcome (exit via face-saving declaration, threats that don't convert, ceasefire ≠ Hormuz reopening) and the **shape** of the endgame, without ever making individual-day timing tractable. Individual stand-downs were rated ~50/50 in real time; the aggregate pattern across cycles was a reliable predictive tool.

**Correction:** a Small-N actor with a *high observation count within the same episode* (repeated brinksmanship, not a one-shot decision) supports a bounded, mechanism-lite forecast of resolution class/shape, distinct from and more tractable than the resolution timing/branch probability, which stays intractable. This sits between "Low Tractability" and "Moderate Tractability" in the existing stratification table — a within-episode behavioral base rate for a Type 3 resolution variable, applicable only after enough repetitions accumulate (the wiki needed ~8 cycles before treating the pattern as load-bearing).

The wiki's own operating discipline is the manual for using this correctly, and is worth adopting as guidance text:

> "identify which variable is dominant, hold that identification against noisier subordinate evidence, and expect the dominant variable to reach the structurally predicted endpoint 'through a wildly nonlinear path' — while refusing to call the path's individual steps." — [[strategy/inputs/oil-taco-digest]]

Their one significant miss (a Day-36 downgrade) came from violating this discipline — overweighting subordinate-variable noise against their own dominant-variable read.

### 3.3 Proposed causal-types addition: depletion-stock mechanism class

Four ostensibly unrelated variables — signal credibility, SPR, allied interceptor stocks, floating storage — obeyed identical finite-buffer logic across the war: a resource that absorbs shocks, has a knowable (if uncertain) capacity, depletes monotonically under sustained draw, and cannot be replenished on the relevant timescale. The wiki used exhaustion of one buffer to predict exhaustion of the others.

> "Buffer exhaustion is a calendar event, not a sentiment event." — [[strategy/inputs/oil-taco-digest]]

This is a somewhat different causal shape from Type 2 (threshold/accumulation toward a *trigger*) — it's accumulation toward *exhaustion* of a resource that was buying time, not toward a discontinuity. It may generalize beyond this war (ammunition stockpiles, foreign reserves, credibility of any repeated signal, evacuation capacity) and is currently unmodeled as a class. Worth evaluating as a possible sub-pattern under Type 2 in [[methodology/reference/causal-types]] — "Depletion/Buffer-Exhaustion" — with its own specification fields (buffer capacity, draw rate, replenishment rate, and whether the buffer's *signaling value* depletes independently of its *physical* stock, per the credibility mechanism in §3.1). This is a proposal for evaluation, not a settled revision.

### 3.4 Calibration lesson: demand elasticity over-modeled, symmetrically

Both the wiki and establishment forecasters made the same category of error in opposite directions on the same parameter. The wiki's own Day-91 self-assessment: "the demand side of the severity curve was over-modeled (substitution and elasticity repeatedly beating forecasts)... both have so far resolved toward 'less acute than modeled, later than modeled.'" IEA's "~6 weeks of jet fuel left" warning was effectively falsified. Establishment forecasters (Goldman) needed 4 revisions and 81 days converging from the *opposite* side — underestimating the physical supply shock the wiki had priced correctly from Day 6.

This is a moderate-tractability parameter (mechanism is right — elasticity dampens shocks — magnitude is not) where **both directions of error were made by sophisticated analysts simultaneously**, which argues for wider uncertainty bands on demand-side elasticity assumptions in `OIL_SUPPLY_SHOCK`-type events specifically, not a directional correction.

---

## 4. Structural fixes to the model

In priority order, directly actionable against the event catalog:

1. **Promote flagged-but-uncataloged cascade targets to mandatory backlog.** `ISRAEL_IRAN_WAR`, `STRAIT_OF_HORMUZ_CRISIS`, and `GULF_STATE_ATTACKS` were all named as "not in catalog" in one cascade comment (`iran-regime-change.md` line 373) — a self-flag that went unactioned, one of a dozen-plus such comments across the geopolitical specs. Adopt a rule: any event name appearing inside another spec's cascade list but absent from the catalog is a mandatory backlog item, not an optional one. This is a process fix as much as a content fix — the model already knew what it was missing.

2. **Precursor-war hazard multipliers; reclassify `OIL_SUPPLY_SHOCK`.** A flat Type 1 stochastic rate (2.5%/yr) cannot respond to a recently-concluded prior war between the same belligerents (June 2025 Twelve-Day War), an active protest wave, or a rebuilt missile arsenal (~1,000→~2,500 + ~80,000 Shaheds) — yet the event fired ~60 days after the spec was finalized, under exactly those precursor conditions. Reclassify as hybrid Type 1/Type 2-3: base stochastic rate, with a state-conditioned geopolitical pathway (pressure variables: time-since-last-conflict-with-same-actor, arsenal reconstitution, active-negotiation-collapse risk) that the Type 2/3 machinery already knows how to build.

3. **Multi-front events with actor-specific resolution clocks.** The war had at least three semi-independent resolution clocks: US-Iran (the TACO Clock), Israel-Lebanon (a veto that "operates through non-compliance" — Israel's Lebanon occupation outlasted the main war), and Iran-internal (succession/IRGC fracture). The single-resolution-per-event template compresses these into one branch set and loses the wiki's key structural finding about the Israel veto. Event template needs to support N independent resolution clocks per window, each with its own dominant variable and behavioral base rate (per §3.2).

4. **Transmission channels with their own thresholds and hysteresis.** Fertilizer→food→political-instability lock-in, the helium cascade (from Ras Laffan), and insurance non-reset behaved like sub-events with lock-in dates and irreversibilities, not smoothly decaying impact-vector components. The impact-vector formalism in [[methodology/concepts/framework-overview]] should allow individual vector components to carry their own threshold/hysteresis parameters rather than a single decay function per event.

5. **Refugee/humanitarian magnitude allocation.** Minor but symptomatic: specs attached displacement flows to Iranian regime collapse (which didn't happen); the actual crisis (800K+ displaced) was Lebanese, a theater the catalog only carries as an impact row on another event. Fixed by #3 (Lebanon needs its own resolution clock, not a footnote).

---

## 5. Method interaction: the wiki as a manual runtime for the sim2075 grammar

The war wiki was not just a data source to validate against — its operating method is, in practice, a hand-run implementation of the sim2075 grammar under real-time conditions the simulation is designed to approximate offline. Each side has practices worth the other absorbing.

| Wiki practice | Sim2075 equivalent | Who should absorb what |
|---|---|---|
| Daily hidden-parameter tracking (P1 TACO Clock, P2 interceptor stocks) with dated, falsifiable entries | Pressure variables in Type 2/3 specs | Sim2075 specs are static once written; the wiki treats pressure variables as *living* tracked quantities. Adopt a lightweight pressure-variable log for high-salience events during an active window. |
| Hypothesis pages with explicit confirmation scoring | Resolution probability estimates | Sim2075 states a probability once; the wiki scores falsifiable hypotheses against real-time evidence and records the misses (e.g. Ground Campaign Launch, downgraded). Adopt for post-hoc calibration review of Type 3 specs. |
| Dominant-variable discipline ("hold the dominant variable against subordinate noise") | Effort Allocation Principle in tractability-boundaries | The operational form of "shift effort to conditional consequences." Sim2075 states the principle; the wiki demonstrates the failure mode (Day-36 downgrade) and recovery. |
| Base-rate-from-repetition for a single actor (OPG pattern) | — (no current equivalent) | New: sim2075 absorbs this as §3.2 — partial-tractability treatment for repeated Small-N actors. |
| Explicit two-branch conditional predictions ("ceasefire won't reopen Hormuz unless X") | Type 3 "aftermath conditional on resolution" structure | Direct match — the wiki independently arrived at the "shift from probabilities to conditionals" structure, and it was its best-performing mode. Validates the doctrine; nothing to change. |
| Self-documented misses as first-class content (Phase 7 convergence, Third Option Pattern, pessimistic anchor bias) | — (no current equivalent) | Event specs for resolved Type 3 events should carry a retrospective field once the outcome is known. |

The wiki's single clearest transferable sentence, worth quoting into the framework's own guidance rather than paraphrasing:

> "identify which variable is dominant, hold that identification against noisier subordinate evidence, and expect the dominant variable to reach the structurally predicted endpoint through a wildly nonlinear path — while refusing to call the path's individual steps."

That is [[methodology/concepts/tractability-boundaries]]'s "shift from probabilities to conditionals" principle, independently rediscovered under fire.

---

## Sources

- [[strategy/inputs/war-validation-report]] — event-by-event comparison, structural verdicts
- [[strategy/inputs/oil-taco-digest]] — Oil Price Fiction and TACO Clock mechanism analysis
- [[methodology/concepts/tractability-boundaries]]
- [[methodology/concepts/epistemology]]
- [[methodology/concepts/framework-overview]]
- [[methodology/reference/causal-types]]
- [[methodology/concepts/small-n-actor-problem]] (referenced, not modified)
- [[methodology/concepts/entropy-maximization]] (referenced, not modified)
