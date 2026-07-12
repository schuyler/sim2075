---
title: emergent-ideas
type: note
permalink: strategy/emergent-ideas
tags:
- strategy
- ideas
- process
- backlog
---

# Emergent Ideas: Standing Mechanisms

Seven ideas that emerged from a close read of the strategy layer (July 2026) and are recorded here so they aren't lost. None is scheduled; each names its natural home and its gate. The common thread: [[strategy/roadmap]] is strong on *artifacts* and thinner on *standing mechanisms* — practices that make the project's good accidents (the wiki running in parallel, the line-373 self-flag, the freeze timestamps) structural rather than lucky.

These follow the roadmap's own evidence discipline: recording an idea costs nothing and commits to nothing. Promotion into the plan goes through the same gates as everything else — Phase 2 evidence for model features, plain cheapness for process changes.

---

## 1. Manufacture the next out-of-sample test (live-window protocol)

**The idea.** The Third Gulf War's evidentiary value was accidental: specs happened to be frozen ~60 days before onset, and the wiki happened to run in parallel. [[strategy/sim2075-third-gulf-war-interaction]] §5 already observes that the wiki was a hand-run implementation of the sim2075 grammar. Make that repeatable: define a lightweight **live-window protocol** that activates when any Type 3 window looks like it's opening (Taiwan, Korea, India–Pakistan) — a wiki-style tracking page run against the *frozen* spec, with a living pressure-variable log, scored falsifiable hypotheses, and the dominant-variable discipline ([[strategy/inputs/oil-taco-digest]] §3).

**Why it matters.** Each activation turns N=1 into N=2, N=3. The project's strongest evidence class — a timestamped public record with confirmation scoring, misses included ([[strategy/roadmap]] "Audience and evidence") — becomes a renewable resource. It is also the only mechanism on offer that generates *future* validation data; every Phase 2 instrument tests structure against the past or against another model.

**Home and gate.** A short protocol note under `methodology/project/` (activation criteria, the tracking-page template, deactivation and retrospective-scoring rules — §5's wiki-practice table is most of the content already). Standing practice alongside the phases, not a phase. Gate: none — draft when a window first looks live, or earlier if cheap.

## 2. Mechanize the line-373 rule (CI lint for uncataloged references)

**The idea.** Phase 0 adopts the process rule "any event named in a cascade list but absent from the catalog is a mandatory backlog item." But the war's central lesson is that self-flags get ignored — the model wrote itself a note (`events/geopolitical/iran-regime-change.md:373`) and nobody read it back, one of a dozen-plus such comments. Phase 1 already plans CI that validates catalog files against the schema ([[strategy/roadmap]] Phase 1 item 5); extend it to parse cascade lists and event references and **fail** on any event ID that is neither in the catalog nor in an explicit backlog registry file.

**Why it matters.** The rule stops depending on authors noticing. The registry file also becomes the machine-readable backlog the roadmap's Phase 0 item 1 gestures at.

**Home and gate.** Phase 1 work item 5 (hygiene/CI) and [[methodology/project/implementation-guide]]'s data track. Gate: none — it's a few dozen lines of CI when the validation harness exists.

## 3. Continuous pre-registration (timestamps that don't need trusting)

**The idea.** The 60-day precedence claim rests on changelog dates inside the repo. Upgrade: git tags at every freeze point (schema versions, catalog releases, spec freezes), plus publishing the tagged commit hash somewhere third-party-timestamped. Every future "specified before X" claim becomes checkable against infrastructure the author doesn't control, rather than trust-the-changelog.

**Why it matters.** [[strategy/methods-paper-sketch]] §vi's evidence class is "check the record." This makes the record itself tamper-evident at ~zero cost, permanently, for every future stress test (see idea 1, which multiplies the occasions).

**Home and gate.** One line in Phase 1's licensing-and-hygiene item; a sentence in [[methodology/reference/research-documentation-standards]]. Gate: none.

## 4. Unattributable audit complaints are a discovery channel

**The idea.** The LLM audit harness ([[strategy/validation-notes-sketch]] Note C) routes every complaint to a parameter address or logs it `unattributable`. The line-373 failure class — a *missing event* — is precisely what surfaces as an unattributable complaint: "this path needed a war here and the model has no such event." Treat the unattributable stream as a standing pipeline into the catalog backlog (idea 2's registry), symmetric with the cascade-list rule: *flagged-by-audit* joins *flagged-in-cascade-list* as a mandatory backlog trigger.

**Why it matters.** The harness then fixes not just wrong parameters but absent ones — the failure mode the war actually exposed. (Recorded in Note C's routing schema as of this note's date.)

**Home and gate.** Already folded into [[strategy/validation-notes-sketch]] Note C. Gate: Phase 2 (the harness itself).

## 5. A cheap fourth instrument: blind re-elicitation consistency

**The idea.** Phase 4 gates elicitation-at-scale on a community materializing. But a solo version needs neither community nor engine: have LLM ensembles **blindly re-elicit a sample of documented parameters** — marginals, loadings — from the same public sources the specs cite, without seeing the specs, then compare against the catalog's values. Disagreements are review flags with reasoning attached; agreements are weak external corroboration for parameters that currently have none.

**Why it matters.** It is the only instrument on the table that tests the *judgments themselves* rather than their joint structure, and it doubles as empirical material for the methods paper's coherence/burden demonstration ([[strategy/methods-paper-sketch]] build-list item 6) — real elicitation transcripts instead of a constructed example. It also pilots the Phase 4 machinery (parameters as questions) at zero community cost.

**Home and gate.** A candidate fourth row in [[strategy/roadmap]] Phase 2's instrument table, or a standalone note. Gate: a frozen catalog (Phase 1 item 3) — nothing else. Deliberately *not* added to the Phase 2 table here; that's a plan change for Schuyler to make.

## 6. Audit the catalog's negative structure

**The idea.** The one specified *negative* cascade — external threat consolidates Gulf regimes, ×0.7 on `SAUDI_REGIME_INSTABILITY` — held ([[strategy/inputs/war-validation-report]] (b)), and it appears to be nearly alone in the catalog. Crisis modeling biases toward amplification, but stabilizing couplings are exactly what kept a dozen elevated hazards from firing in 2026. Run a systematic pass: where should negative cascades, negative loadings, or consolidation effects exist that don't?

**Why it matters.** A catalog with only positive couplings overstates tail clustering by construction — which corrupts the headline outputs (tail-driver identification) the project claims as its contribution.

**Home and gate.** A sub-question in [[strategy/validation-notes-sketch]] Note A (does removing negative structure visibly fatten the tails?) plus an authoring-checklist line in [[methodology/03-critical-review]] ("what does this event *suppress*?"). Gate: the sensitivity instrument for the quantitative half; none for the checklist line.

## 7. Treat the parameter diff history as a future dataset

**The idea.** Once the catalog is public and community-edited, the git history of parameter changes *is* a time series of documented judgment revisions. Adopt commit conventions now: tag every catalog-parameter change as audit-driven, world-event-driven, or elicitation-driven; never squash catalog history.

**Why it matters.** Years out, this answers questions no one else can: how documented judgments actually move — in response to world events versus audits versus argument — across a public, versioned corpus. It is also the natural longitudinal companion to the judgment schema ([[strategy/roadmap]] Phase 4 item 1). Cost today: a commit-message convention.

**Home and gate.** Phase 1 item 4 (the interface split — the convention belongs in the catalog contribution path) and [[methodology/reference/research-documentation-standards]]. Gate: none.

---

## Disposition summary

| # | Idea | Home | Gate |
|---|---|---|---|
| 1 | Live-window protocol | new `methodology/project/` note | none (draft at first live window) |
| 2 | CI lint for uncataloged references | Phase 1 item 5 / implementation guide | none |
| 3 | Continuous pre-registration | Phase 1 item 5; documentation standards | none |
| 4 | Unattributable complaints → backlog | validation-notes-sketch Note C (done) | Phase 2 |
| 5 | Blind re-elicitation instrument | candidate Phase 2 instrument | frozen catalog; plan change is Schuyler's call |
| 6 | Negative-structure audit | Note A sub-question; critical-review checklist | sensitivity instrument / none |
| 7 | Parameter-diff conventions | Phase 1 item 4; documentation standards | none |

## Sources

- [[strategy/roadmap]] — the plan these candidates would amend
- [[strategy/sim2075-third-gulf-war-interaction]] — §5 (wiki as manual runtime), line-373 lesson
- [[strategy/inputs/war-validation-report]] — negative-cascade validation; the curation failure
- [[strategy/inputs/oil-taco-digest]] — dominant-variable discipline (idea 1)
- [[strategy/methods-paper-sketch]] — evidence-class and build-list touchpoints (ideas 3, 5)
- [[strategy/validation-notes-sketch]] — Notes A and C touchpoints (ideas 4, 6)
