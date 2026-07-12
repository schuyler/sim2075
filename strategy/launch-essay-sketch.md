---
title: launch-essay-sketch
type: note
permalink: strategy/launch-essay-sketch
tags:
- strategy
- publication
- launch-essay
- third-gulf-war
- sketch
---

# Launch Essay Sketch

Sketch of the Phase 0 public launch essay, not the essay. Specified by [[strategy/roadmap]] Phase 0 item 6: adapt [[strategy/sim2075-third-gulf-war-interaction]] into "what the Third Gulf War taught a model built 60 days before it started," leading with the model's failure, matching the wiki's credibility-through-honesty tone, and introducing the project to the wiki's existing audience.

Relationship to [[strategy/methods-paper-sketch]]: same evidence, different genre. The essay is the public, narrative, zero-prerequisites version for the wiki's readership; the paper is the scholarly version for *Futures*-class reviewers. The essay ships first (Phase 0) and should not burn the paper's novelty claims — it can say everything the paper says, but as story, not as claims-and-evidence.

---

## 1. Working titles

1. **"What the Third Gulf War taught a model built 60 days before it started"** — the roadmap's own phrasing; direct, honest, dated.
2. **"The model knew what it was missing"** — leads with the self-flag; strongest hook, riskier as a standalone title without context.
3. **"A war we priced at 1%"** — leads with the number; clean, but undersells the parts that held.

Default to 1 with 2 as the section heading for the cold open.

## 2. Audience, tone, venue

- **Audience.** The Third Gulf War wiki's existing readers: international-geopolitics readers and energy-market dabblers ([[strategy/roadmap]] "Audience and evidence"). Assume zero knowledge of sim2075, Monte Carlo methods, or copulas. Assume deep familiarity with the war itself — do not re-narrate it; reference it.
- **Tone.** The wiki's own: dated claims, scored misses, no hedging after the fact. The essay's credibility *is* the willingness to lead with the failure. No academic hedging, no marketing.
- **Venue.** Open question (§7) — candidate homes: the wiki itself (as a linked essay), a project page in this repo rendered publicly, or a personal blog cross-linked from the wiki. Whatever is chosen, the essay must be somewhere the wiki audience already is.
- **Length.** Target 2,500–4,000 words. Long enough to carry the four validations and two corrections with receipts; short enough to be read in one sitting.

## 3. Thesis and lede

**Thesis.** A hobbyist-scale structural model, frozen ~60 days before the war, correctly predicted *which of its own predictions would fail* — and the failure that actually occurred was one the model had literally written down in a comment to itself. That combination (architecture held, curation failed, failure self-flagged in advance) is more informative about the method than a lucky hit would have been.

**Cold open.** The single cascade comment: `events/geopolitical/iran-regime-change.md:373` — *"STRAIT_OF_HORMUZ_CRISIS, GULF_STATE_ATTACKS, ISRAEL_IRAN_WAR not in catalog."* Written December 2025. Unactioned. The war began February 28, 2026. The essay opens here: the model's most consequential output was a note to itself that nobody read back.

## 4. Outline

### a. The note the model wrote to itself (cold open)

The line-373 comment, the December 2025 changelog dates, the February 28 onset. State the composite path probability the catalog would have assigned the observed world (~0.5–1%/yr) plainly — "we priced the most precondition-laden interstate war on Earth at about one percent" — before explaining anything about how the model works.

### b. What the thing is (one section, plain language)

sim2075 in ~400 words, no math: a catalog of ~30 discontinuity events, each with a documented probability and a *generating mechanism* (steady background rate / pressure building to a threshold / a window that opens and a leader who decides / trends that aren't events at all); correlations carried by a small set of shared stress factors rather than event-by-event guesses; every impact typed by what recovers and what doesn't; and — the distinctive move — the model's own limits written into its architecture: parameters we believe are unknowable are *declared* unknowable and defaulted to maximum uncertainty, with effort shifted to "if X happens, then what." A narrative generator, not a set of predictions. Link the repo and [[strategy/roadmap]].

### c. What held (the four validations, with receipts)

From [[strategy/sim2075-third-gulf-war-interaction]] §2 / [[strategy/inputs/war-validation-report]] (c):

1. **The model predicted its own failure mode.** The framework says war-start decisions are unknowable and aftermaths are analyzable. The wiki — with daily tracking and vastly more information than any model — missed the resolution (held escalation as modal for 37 days; the war ended in a branch it priced at 11–20%) while its aftermath calls repeatedly beat institutional sources (the Day-6 supply picture Goldman took 4 revisions and 81 days to reach; the Day-11 repricing call confirmed Day 12; the Day-25 Passover-window call within 48 hours of the actual ceasefire; the Day-84 "OPG predicts cycle 9" bet, won). Scored misses included — the ground-campaign hypothesis was downgraded as a failure and stays in the record.
2. **The boundary rules got the non-event right, against the war's own planners.** Khamenei assassinated, Mojtaba succeeded within ~8 days, regime held — and `IRAN_REGIME_CHANGE` correctly did not fire, because the spec's rules say managed succession and survived crises are sub-threshold. The spec's Case Against ("rally-around-flag rather than collapse") was right where the people who launched the war were wrong.
3. **One shock, many elevated hazards, none fired.** Taiwan preconditions, US–China rupture pressure, dollar stress, Saudi proliferation logic, US constitutional strain — all moved together, none resolved. That is exactly the signature the correlated-factor design produces: correlated probability elevation, not deterministic cascade. The one specified *negative* cascade (external threat consolidates Gulf regimes) also held.
4. **"Damage a ceasefire cannot fix."** Oil price round-tripped to ~$80 within days of the MOU; Ras Laffan (3–5 year repair), the institutionalized Hormuz toll regime, insurance floors, and alliance-credibility damage persisted regardless. The model's insistence that durability belongs to the *impact type*, not the event, is precisely this distinction.

### d. What broke (as prominently as what held)

1. **The curation failure.** The hub-and-spoke inversion: the catalog made regime change and nuclear acquisition the hubs with war as a branch; reality made the war the hub. The event was representable natively (a textbook window/resolution event) — it just wasn't specified, despite the self-flag.
2. **The flat rate that should have been listening.** `OIL_SUPPLY_SHOCK` carried a flat 2.5%/yr that couldn't respond to a just-concluded war between the same belligerents, a rebuilt missile arsenal, or collapsing negotiations. It fired ~60 days after specification, under exactly those conditions.
3. **Two lessons the framework didn't have** (plain-language versions of the boundary corrections): (a) *markets were pricing Trump's psychology, not barrels* — a price channel sitting on top of an unknowable actor inherits that unknowability, no matter how tractable the physical logistics are; (b) *eight stand-downs, zero conversions* — a leader who repeats the same brinksmanship enough times generates his own base rate, and that base rate beat the strongest kinetic signals of the war. The unknowability boundary is softer for repeated actors than the framework assumed.

### e. What we're changing

The Phase 0 fix list, in plain terms: the three missing war-hub events become first-class catalog entries; a standing rule that any event named in a cascade list but absent from the catalog is a mandatory backlog item ("the model already knew what it was missing — the fix is to make it impossible to ignore itself"); precursor-war hazard conditioning recorded for `OIL_SUPPLY_SHOCK`; the two boundary corrections written into the methodology; the bigger structural lessons (multi-clock wars, threshold-carrying transmission channels) held in a named backlog gated on evidence, not enthusiasm.

### f. The invitation

The project is free, open, and public from the first commit. The engine and schema are small and boring; the event catalog is the layer where disagreement lives — a disputed probability is a diffable YAML field with documented reasoning attached. If you think 1.2%/yr for Iranian regime change is wrong, the correct response is a pull request with your reasoning, and the review standard is that changed numbers come with changed arguments. Close by pointing at the repo, the roadmap, and (if timing works) the first engine milestone.

## 5. Evidence discipline

Per [[strategy/roadmap]] Phase 0 item 6: **re-verify every load-bearing wiki quote and date against the wiki itself before publication.** The strategy inputs are second-hand digests, and one day-anchor has already needed correcting (the Day-40 ceasefire: announced 8pm April 7, wiki-dated Day 40 / April 8 — and it fractured within 18 hours; it did *not* end the war, which ran to the Day-110 Islamabad MOU, June 17).

Verification checklist (each item checked against the wiki, not the digests):

| Claim | Currently sourced from |
|---|---|
| Onset Feb 28, 2026; MOU Day 110 / June 17 | [[strategy/inputs/war-validation-report]] (a) |
| Spec changelogs 2025-12-19/30 (the "60 days" claim) | war-validation-report header |
| `iran-regime-change.md:373` comment text | verifiable in-repo (primary) |
| B2 modal 37 days; B1 priced 11–20% at signing | war-validation-report (a), (c) |
| Day-6 supply picture vs. Goldman 4 revisions / 81 days | [[strategy/inputs/oil-taco-digest]] §1(b) |
| Day-11 repricing call confirmed Day 12 | oil-taco-digest §1(a) |
| Day-25 Passover-window call within 48 hours | oil-taco-digest §2 |
| 8 stand-down cycles, 0 conversions; Day-84 cycle-9 bet | oil-taco-digest §2 |
| Ground-campaign hypothesis scored as failure | oil-taco-digest §2 |
| "The market is pricing Trump's psychology, not barrels" (verbatim) | oil-taco-digest §3 |
| "When I feel it in my bones" (verbatim, Day 14) | oil-taco-digest §2 |
| Oil price round-trip ~$80 within days of MOU; Ras Laffan 3–5 yr | interaction doc §2(d) |
| Mojtaba succession ~8 days | war-validation-report (a) |

Rule: anything the wiki can't confirm gets cut or attributed to the digest explicitly. The essay must survive its own audience checking the record — that audience *is* the wiki's readership.

## 6. What the essay is not

- Not a validation claim. N=1, and the framework partially failed; the essay says both, in that order of prominence where honesty demands it.
- Not a forecast. The project's output claim is scenario exploration under documented judgment; the essay must not drift into "we called it" — the whole point is that the model *didn't* call it and the interesting part is what that reveals.
- Not the methods paper. No lineage-revival claims, no venue positioning, no formal machinery. Where the essay gestures at machinery, it links rather than derives.

## 7. Decisions needed before drafting

1. **Venue/home** for the essay (wiki-adjacent page, repo page, blog) — determines link structure and how much project-introduction is needed.
2. **Wiki citability scope** — the same question the methods paper has ([[strategy/methods-paper-sketch]] §6); the essay is the first artifact to hit it. Deciding it here settles it for the paper's appendix too.
3. **Timing vs. Phase 0 remediation** — the essay describes the fixes and is publishable before all of them land ([[strategy/roadmap]] Phase 0 failure modes), but it reads better with at least the three war-hub events merged. Decide the minimum landed-work bar.

## Sources

- [[strategy/roadmap]] — Phase 0 item 6 (the specification for this essay)
- [[strategy/sim2075-third-gulf-war-interaction]] — primary content source
- [[strategy/inputs/war-validation-report]] — receipts for §4c–d
- [[strategy/inputs/oil-taco-digest]] — receipts for §4c–d; day-anchor caution
- [[strategy/methods-paper-sketch]] — the scholarly sibling; shared citability question
