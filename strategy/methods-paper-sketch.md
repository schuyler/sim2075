---
title: methods-paper-sketch
type: note
permalink: strategy/methods-paper-sketch
tags:
- strategy
- publication
- methods-paper
- sketch
---

# Methods Paper Sketch

Sketch of a publishable methods paper, not the paper. Core thesis: **catastrophe-modeling techniques for the polycrisis** — reviving the dead probabilistic cross-impact lineage (Gordon & Helmer 1966; Turoff 1971) with a latent-factor Gaussian copula as the coherence fix, a causal typology, per-impact durability, and tractability boundaries built into the architecture — strengthened by a documented out-of-sample stress test (framework specified ~60 days before the Third Gulf War).

Inputs: [[strategy/inputs/public-landscape-survey]], [[strategy/inputs/war-validation-report]], [[strategy/inputs/oil-taco-digest]].

---

## 1. Working title and abstract

### Title options

1. **"Catastrophe modeling for the polycrisis: a latent-factor revival of probabilistic cross-impact analysis"**
2. **"Correlated discontinuities: an event-catalog method for long-range geopolitical scenario generation"**
3. **"Knowing what you can't estimate: tractability-stratified Monte Carlo simulation of global discontinuities to 2075"**

Option 1 leads with the lineage-revival claim and the cat-model transplant — probably strongest for *Futures*/*TFSC*. Option 3 leads with the epistemology, which may travel better at *Global Sustainability*.

### Abstract draft

> Probabilistic cross-impact analysis (Gordon & Helmer 1966; Turoff 1971) promised Monte Carlo generation of interdependent future events, but the lineage died: eliciting O(n²) conditional probabilities was burdensome, and elicited conditionals routinely implied no coherent joint distribution. Its non-probabilistic successor, cross-impact balance analysis, deliberately abandoned likelihood. We describe a method that restores probability to cross-impact scenario generation by borrowing the machinery of catastrophe modeling: a curated catalog of discontinuity events with documented marginal probabilities, correlated through a latent-factor Gaussian copula that reduces elicitation from O(n²) conditionals to O(n×k) factor loadings and guarantees a coherent (positive semi-definite) dependence structure by construction. Three further components address failure modes of judgmental long-range modeling: a four-type causal typology that assigns each event a generating mechanism (stochastic arrival, threshold accumulation, window/resolution contingency, S-curve reclassified as trajectory); per-impact durability typing (permanent, decaying, maintenance-required); and explicit tractability boundaries that route intractable parameters — notably small-N actor decisions — to maximum-entropy defaults while concentrating analytical effort on conditional aftermaths. The framework was fully specified roughly sixty days before the Third Gulf War (February–June 2026), providing an unplanned out-of-sample stress test — a single case, offered as structurally informative rather than validating. The war's course was consistent with the structural grammar — tractability stratification, discontinuity boundary rules, the correlated-hazard signature, durability typing — while exposing correctable failures in catalog curation, expectation-mediated transmission channels, and repeated-actor base rates, each of which we report and incorporate. We frame the method as scenario exploration under documented judgment, not forecasting, and scope novelty claims to the public literature.

---

## 2. Venues and audience

### Venues, ranked

Ranking is the authors' judgment of fit, not established fact — sanity-check against recent tables of contents before committing.

| Rank | Venue | Rationale |
|---|---|---|
| 1 | ***Futures*** | Home journal of the cross-impact/scenario-methods lineage being revived; methods papers with epistemological framing are in-scope; the Gordon–Helmer/Turoff resurrection narrative lands best with this readership. |
| 2 | ***Global Sustainability*** (Cambridge) | Published the "synchronous failure" / systemic-GCR taxonomy the Type 1–4 typology operationalizes; polycrisis framing is native; Cascade-adjacent readership. |
| 3 | ***Technological Forecasting & Social Change*** | Where CIB was introduced (Weimer-Jehle 2006) — the natural venue for "the probabilistic complement to CIB"; higher methods bar, longer review. |
| 4 | ***Risk Analysis*** | Best fit for the copula/cat-model machinery per se; but geopolitical scenario generation is peripheral to its core readership — fallback, or target for a narrower technical companion paper. |

Appetite signal: Gambhir et al. 2025 (*Nature Communications*) — a polycrisis systemic-risk *methodological framework* paper at a top general venue (see [[strategy/inputs/public-landscape-survey]] §4) — shows editors currently accept methods-forward polycrisis work.

### Audience

- **Primary: the Cascade Institute team** (Homer-Dixon, Kemp, Schweizer). Shared epistemology (parameters as documented, criticizable judgments), perfectly complementary method: their PCM finds *where the 2040 attractors are* (static CIB consistency); this method generates *trajectories, timing, and probability mass* to 2075. The paper should explicitly position itself as the dynamic complement to the PCM and their Stress–Trigger–Crisis model. Most likely serious engagers and critics.
- **Secondary: forecasting/GCR community** (FRI/XPT, Metaculus, superforecasting) — the XPT's immovable expert disagreement is empirical support for the tractability-boundary stance; XPT-class marginals are calibration inputs.
- **Tertiary: catastrophe-modeling crossover** — Verisk's 2025 SRCC model proved event-catalog mechanics work for political violence; this paper extends the transplant to multi-domain, multi-decade scope.

---

## 3. Section-by-section outline

### i. Problem: the polycrisis needs correlated-discontinuity machinery

The defining feature of polycrisis reasoning is that discontinuities cluster — common causes, causal chains, contagion, feedback — yet no public method generates correlated discontinuities over decadal horizons. Each existing approach lacks a piece: IAMs/IFs extrapolate trends and structurally cannot represent discontinuities; CIB finds consistent world-states but deliberately abandons probability, time, and events; judgmental forecasting (Metaculus, XPT, superforecasters) produces isolated marginals with no joint distribution; cat models have exactly the right machinery (stochastic catalogs, copula aggregation, frequency-severity) but apply it to single perils on ~1-year horizons. Key claim: the assembly — event catalog × correlated sampling × state feedback × durability × 50-year horizon — exists nowhere in public (landscape survey, Assessment (a)).

### ii. Why probabilistic cross-impact died, and the copula fix

Gordon–Helmer/Turoff cross-impact required experts to supply pairwise conditional probabilities: O(n²) elicitations that (a) exhaust expert patience and (b) routinely violate coherence — elicited conditionals often imply no valid joint distribution. The latent-factor Gaussian copula fixes both: experts supply one marginal per event plus loadings on k interpretable latent factors (climate stress, financial fragility, great-power tension, regional factors...), so elicitation is O(n×k) — at the repo's illustrative design target of 75 events × 12 factors, 900 loadings versus 2,775 pairwise conditionals; the current catalog is ~30 events, and the scaling argument holds at either size — and the implied correlation matrix Σ = ΛΛᵀ + Ψ is positive semi-definite by construction, so incoherence is impossible rather than merely checked for. Loadings are also individually meaningful and auditable ("this event loads 0.5 on MENA regional stress") in a way pairwise conditionals never were. Technical content from [[methodology/concepts/gaussian-copula]]; note the factor-independence assumption and its Ω-correlated alternative as an honest design choice.

### iii. The causal typology: generating mechanism must differ per event

A single probability formalism applied to heterogeneous events is a category error. The typology ([[methodology/reference/causal-types]]): **Type 1** stochastic arrivals (base rate, Poisson-like — pandemics); **Type 2** threshold/accumulation (probability conditioned on observable pressure state — state failure, AMOC); **Type 3** contingent window/resolution (preconditions open a window; resolution is a small-N actor decision — Taiwan, invasion decisions); **Type 4** S-curves, which are *not events* and get reclassified as baseline trajectory uncertainty. Each type gets distinct math (flat hazard; P(event|pressure); two-stage window/resolution sampling; parameterized learning curves) and a distinct factor-explained variance target. Position against the conceptual cousins it operationalizes: Cascade's Stress–Trigger–Crisis and the *Global Sustainability* synchronous-failure archetypes.

### iv. Durability vectors

Events are valence-free state transitions carrying multi-dimensional impact vectors, and each impact component gets its own durability type: deaths permanent, infrastructure decaying, agreements maintenance-required, technology deployment permanent ([[methodology/concepts/framework-overview]]). This is the machinery for the recovery-dynamics question the polycrisis literature keeps gesturing at (Undheim & Ahmad's 25-year single-catastrophe recovery pattern) and that no public model carries through a simulation — Lloyd's prices 5-year GDP windows and stops. The war supplied a vivid instance: oil *price* round-tripped within days of the MOU (decaying, short half-life) while Ras Laffan repair, the institutionalized Hormuz toll regime, and alliance-credibility damage persisted regardless of the deal (persistent / floor > 0) — "damage a ceasefire cannot fix."

### v. Tractability boundaries as architecture

The distinctive epistemological move: parameter knowability is stratified (high / moderate / low) and the stratification is written into the model, not the caveats section ([[methodology/concepts/tractability-boundaries]], [[methodology/concepts/epistemology]]). Low-tractability parameters — above all Type 3 resolution probabilities, the Small-N Actor Problem — get maximum-entropy defaults (uniform over plausible resolutions), and analytical effort shifts to conditional aftermaths, which are moderate-to-high tractability. "If X, then Y" replaces "P(X)" wherever P(X) has no structural purchase. Cite XPT's finding that four months of incentivized debate moved no one, and RAND's deep-uncertainty doctrine, as independent support; distinguish from RDM, which responds to the same problem by abandoning probability entirely rather than stratifying it.

### vi. The Third Gulf War as out-of-sample stress test

Documented natural experiment: specs frozen (changelogs 2025-12-19/30) ~60 days before onset (2026-02-28); a parallel real-time research wiki tracked the war daily, independently of the model. **What held** ([[strategy/inputs/war-validation-report]]): (1) tractability stratification observed in the wild — the wiki, with maximal information, missed the resolution (held escalation modal for 37 days; the war ended in a branch priced 11–20%) while its *conditional aftermath* analysis was repeatedly confirmed weeks ahead of institutional sources; (2) discontinuity boundary rules gave the right answers — Khamenei assassinated, Mojtaba succeeded within 8 days, regime held: IRAN_REGIME_CHANGE correctly did not fire, against the belief of the people who launched the war; (3) the correlated-hazard signature — one MENA/GPT shock elevated Taiwan, US-China rupture, dollar-stress, and proliferation hazards simultaneously without firing any of them, which is exactly what a high factor draw does, and the one specified *negative* cascade (external threat consolidates Gulf regimes) also held; (4) durability typing (see §iv). **What broke**: the war itself was not a first-class catalog event — it existed only as branches of other events (composite path probability ~0.5–1%/yr), even though a single cascade comment in one spec names all three missing war-hub events (`iran-regime-change.md:373`: "STRAIT_OF_HORMUZ_CRISIS, GULF_STATE_ATTACKS, ISRAEL_IRAN_WAR not in catalog"): a curation failure, not an ontology failure (the war is a textbook Type 3 window/resolution event). **Two boundary corrections** ([[strategy/inputs/oil-taco-digest]]): (a) *expectation-mediated transmission* — "structural consequences conditional on decisions" held for physical transmission (barrels, mines, refineries, displacement) but failed for market transmission, because prices were themselves forecasting the intractable actor ("the market is pricing Trump's psychology, not barrels"); market channels need to be modeled as partially contaminated by the Small-N variable; (b) *repeated-actor partial tractability* — an accumulated base rate of one actor's own behavior (eight stand-down cycles, zero conversions) became genuinely predictive, so the Small-N boundary is softer for repeated observed actors than the framework assumed. Plus: recent-precursor-war hazard multipliers (a war between the same parties is the strongest predictor of the next one) and multi-front events with actor-specific resolution clocks.

### vii. Limitations and honest-uncertainty framing

This is scenario exploration, not forecasting: parameters are documented judgments, unvalidatable on relevant timescales ([[methodology/concepts/epistemology]]); the output claim is "futures worth thinking about," structural dependencies, and tail-driver identification — not integrated probability forecasts. N=1 stress test, and one that the framework partially failed. Novelty is scoped to the public space — classified, hedge-fund, and reinsurer analogs plausibly exist unpublished. Known unfixed weaknesses go here too: single-resolution-per-event compression of multi-clock wars; transmission channels with their own thresholds and hysteresis that the impact-vector formalism understates; the Gaussian copula's thin tail dependence (t-copula as future work).

---

## 4. Claims-and-evidence table

| # | Headline claim | Evidence source |
|---|---|---|
| 1 | No public method combines event catalog × correlated sampling × state feedback × durability × multi-decade horizon | [[strategy/inputs/public-landscape-survey]] Assessment (a); scoped "public space" per (c)5 |
| 2 | Probabilistic cross-impact died from elicitation burden + incoherence; CIB survived by dropping probability | Landscape survey §7 (Gordon & Helmer 1966; Turoff 1971; Weimer-Jehle 2006) |
| 3 | Latent-factor copula cuts elicitation O(n²)→O(n×k) and is coherent (PSD) by construction | [[methodology/concepts/gaussian-copula]] (at the 75-event design target: 900 loadings vs 2,775 correlations; current catalog is ~30 events — scaling argument holds either way) |
| 4 | Event-catalog mechanics transplant to geopolitical perils | Verisk SRCC model (2025), landscape survey §5 |
| 5 | Generating mechanism must differ per causal type; conflation produces bad models | [[methodology/reference/causal-types]]; operationalizes Cascade Stress–Trigger–Crisis and synchronous-failure archetypes |
| 6 | Type 3 resolutions are intractable; aftermaths are tractable — invest there | [[methodology/concepts/tractability-boundaries]]; war wiki missed resolution (B1 at 11–20% at signing) while aftermath calls beat Goldman/IEA by 40–80 days ([[strategy/inputs/war-validation-report]] c.2, [[strategy/inputs/oil-taco-digest]] §3) |
| 7 | Expert deliberation cannot close intractable disagreement | XPT (FRI; *IJF* 41(2) 2025): four months of incentivized debate moved nobody |
| 8 | Discontinuity boundary rules exclude the right non-events | War report c.3: Khamenei assassination + managed succession correctly sub-threshold; spec's Case Against called rally-around-flag |
| 9 | Correlated-factor architecture matches observed crisis signature | War report c.4: one shock elevated many hazards, fired none; negative Gulf-consolidation cascade also held |
| 10 | Per-impact durability is the right vocabulary for what recovers vs. what doesn't | War report c.5 / d: price round-trip vs. Ras Laffan, toll regime, credibility damage |
| 11 | The catalog gap was curation, not architecture | War report b/c.1: war representable as textbook Type 3; a cascade comment in one spec names all three missing war-hub events (`iran-regime-change.md:373`) |
| 12 | Physical transmission tractable; market transmission contaminated by the Small-N actor | [[strategy/inputs/oil-taco-digest]] §3 cross-cutting finding (Oil Price Fiction ≈ TACO Clock projected into prices) |
| 13 | Repeated-actor behavioral base rates give partial tractability inside the Small-N domain | Oil/TACO digest: OPG pattern, 8–9 cycles → correct bet against strongest kinetic signals of the war |
| 14 | Durability/recovery structure is absent from existing quantitative futures work | Landscape survey §7 (Undheim & Ahmad 2024) and §5 (Lloyd's 5-year windows) |

---

## 5. Anticipated objections and responses

1. **"The war event wasn't even in your catalog."** Lead with this — it is the strongest objection and hiding it would cost all credibility. Response: the curation-vs-architecture distinction. The war is a textbook Type 3 event the ontology represents natively; the failure was omitting it from the catalog even though one spec's cascade comment (`iran-regime-change.md:373`) names all three missing war-hub events as not in the catalog. The corrective is procedural and reported in the paper (flagged-in-cascade-list → mandatory backlog item), and the miss itself generated the paper's two most useful boundary corrections. A method that specifies its own failure modes in advance and then fails in exactly those modes is giving evidence about itself.
2. **"Unvalidatable parameters — this is numerology."** Response: the epistemology concedes non-calibratability up front and substitutes a different standard — transparency, internal consistency, auditability, revisability ([[methodology/concepts/epistemology]]) — identical to Cascade's documented-judgment stance (1,800+ published judgments) already accepted in the literature. The tractability architecture is precisely the mechanism that prevents unvalidatable numbers from silently driving conclusions: intractable parameters get entropy-maximized, and results are reported as conditional on them.
3. **"N=1 stress test."** Response: correct, and claimed as such. The war is not offered as validation of any probability estimate; it is a structural stress test of the *grammar* (typology, boundary rules, correlation signature, durability), where one severe out-of-sample event is informative the way one crash is informative about an airframe. The paper reports what broke as prominently as what held; the falsifiable-in-principle posture is the contribution.
4. **"Gaussian copulas failed in 2008."** Response: the 2008 failure was calibrating tail dependence to short benign histories and treating outputs as pricing-grade truth. Here the copula is an elicitation and coherence device for documented judgments, outputs are scenario ensembles not prices, factor loadings are auditable, and tail-dependence limits are declared with the t-copula flagged as an alternative.
5. **"Why probabilities at all? RAND's deep-uncertainty doctrine says don't."** Response: without likelihood there is no probability *mass* across futures, no correlation structure, and no way to say which structural dependencies matter most. Stratified tractability is the middle path between RDM's abstention and IAM false precision: probability where structure supports it, entropy where it doesn't.
6. **"Judgmental marginals are worse than superforecasters'."** Response: agreed — the method is a consumer of XPT/Metaculus-class marginals, not a competitor; its contribution is the joint structure those sources cannot produce. Reconciliation with published marginals is part of the elicitation protocol.
7. **"This is just cat modeling / just cross-impact / just a factor model."** Response: each ingredient has precedent (and the paper cites it); the contribution is the assembly plus the typology, durability, and tractability layers — none of which exists in the cat-model transplant (Verisk: one peril, one country, one year) or the cross-impact lineage.

---

## 6. Pre-submission build list

Roughly in dependency order:

1. **Formal copula/factor specification writeup** — the math in [[methodology/concepts/gaussian-copula]] and [[methodology/reference/variance-allocation]] as a self-contained methods section: sampling procedure, loading→correlation algebra, variance-allocation targets by type, factor-independence assumption and Ω alternative.
2. **Working prototype simulation** — the paper cannot ship on specs alone. Minimum: the existing catalog (post-remediation), 12 factors, state-event coupling, producing trajectory ensembles with at least one headline structural finding (e.g., which factor loadings drive tail clustering).
3. **Catalog remediation from the war report** — add the first-class Type 3 events (US/Israel–Iran war, Hormuz crisis, Gulf infrastructure attack), recent-precursor hazard multipliers, OIL_SUPPLY_SHOCK reclassified to hybrid; the paper's §vi claims the corrections were incorporated, so they must be.
4. **Sensitivity analysis** — tornado-style: which outputs move under loading/marginal perturbation; demonstrates the "conclusions depend on tractable vs. intractable parameters" reporting discipline in practice.
5. **A worked comparison against the PCM** — even qualitative: same 2040 question, attractors vs. trajectory mass, to make the "dynamic complement" claim concrete for the Cascade audience.
6. **Coherence/burden demonstration** — small worked example showing elicited pairwise conditionals going incoherent vs. the factor elicitation for the same events; this is the paper's central technical argument and needs more than assertion.
7. **War-validation appendix** — condensed, citable form of [[strategy/inputs/war-validation-report]] with the wiki as documented evidence trail (timestamped changelogs establish the 60-day precedence claim; decide how much of the wiki is publishable/anonymizable).
8. **Decide licensing/openness** — the "open tooling / ScenarioWizard for dynamic probabilistic futures" positioning (landscape survey (c)3) materially strengthens the paper; releasing the engine and catalog alongside submission is worth the cost if the venue is *Futures* or *Global Sustainability*.

Open questions for Schuyler: single paper or split (methods paper + shorter war-validation note)? How much of the Third Gulf War wiki can be cited publicly? Author list / Cascade pre-submission contact?
