---
title: planned-events-round-2
type: note
permalink: events/planned-events-round-2
tags:
- events
- planning
- stubs
- round-2
- backlog
- ensemble
---

# Planned Events — Round 2 (Stub Catalog)

**Status: Stubs for ensemble authoring. None specified at Level 1 yet.**

This is the demand-signal-driven second batch, assembled per [[methodology/reference/catalog-versioning]] §5. Each entry is a **stub**: enough structure that an Opus agent can open [[methodology/02-event-template]] and fill it out in one ~40-minute Level 1 pass ([[methodology/01-level-1-workflow]]), without first having to decide *whether* the event belongs or *what shape* it takes.

Every stub commits to the four decisions that are hardest to make cold and easiest to get wrong late:

1. **Causal type** — 1 / 2 / 3 / hybrid, with the one-line reason. This fixes which probability machinery the author uses (base rate vs. `pressure_function` vs. `window`).
2. **Provisional factor loadings** — dominant + secondary factors from the 12-factor set, so the author starts from a variance-allocation target rather than a blank `factor_loadings` block. Numbers are placeholders to be scaled per [[methodology/reference/variance-allocation]].
3. **The discontinuity claim** — one sentence on what state break this is, so it doesn't collapse into "severe-but-recoverable stress" (the [[methodology/03-critical-review]] Q1 failure).
4. **Consumers and new variables** — which existing events cascade to/from it, and whether it needs a state variable that doesn't exist yet (those go to [[methodology/reference/state-variables-round-2]]).

Where a stub came from a dangling cascade reference, its origin is tagged `[registry]` and cross-listed in [[events/backlog-registry]]. Where it fills a coverage gap identified in the strategy layer or the existing planning docs, it's tagged accordingly.

**Priority key:** P1 = author first (registry-mandated or high tail-relevance); P2 = strong candidate; P3 = low-priority queue, author only if sensitivity analysis surfaces the region/factor.

**Author's contract for each stub:** fill every template section; run the critical review; if you conclude the event should be *folded* or *declined* instead of specified, say so in the changelog and update [[events/backlog-registry]] — a well-argued decline is a valid Level 1 outcome.

**Modeling scope.** This catalog — like everything under `events/` — estimates the *probabilities and impact vectors* of possible future events so the Monte Carlo engine can explore trajectory space. Specs describe consequences (mortality, GDP, displacement, system load) and cite public risk literature for base rates (per [[methodology/reference/research-documentation-standards]]). They do not analyze mechanisms for bringing any event about, and nothing here is guidance toward any outcome; the epistemic stance is [[methodology/concepts/epistemology]]. This applies with particular force to the conflict, nuclear, cyber, and health/bio stubs below: authors stay at the consequence-and-base-rate level throughout.

---

## A. Nuclear & Great-Power Conflict

The catalog's thinnest tail relative to impact. Several of these are registry-mandated by the Third Gulf War remediation ([[strategy/roadmap]] Phase 0).

### A1. `ISRAEL_IRAN_WAR` — P1 [registry, Phase 0]

- **Discontinuity:** Direct state-on-state war between Israel and Iran (as opposed to proxy exchange), with US entanglement risk. The 2026 episode is the reference case.
- **Type:** 3 (Contingent). Window = acute escalation trigger; resolution = the multi-clock structure the war exposed (US–Iran, Israel–Lebanon veto-through-non-compliance, Iran-internal). Compress to a single resolution set for v0.1 per Phase 0 item 1; note the multi-clock form as a schema-v0.2 backlog item.
- **Provisional loadings:** F_GPT ~0.45 (dominant), F_MENA ~0.55, F_FIN ~0.20 (oil→inflation), F_HLTH negligible.
- **Consumers:** triggered_by `IRAN_NUCLEAR_ACQUISITION`, `IRAN_REGIME_CHANGE`; triggers `STRAIT_OF_HORMUZ_CRISIS`, `OIL_SUPPLY_SHOCK`, `NPT_REGIME_COLLAPSE`. Absorbs `PROXY_NETWORK_COLLAPSE`.
- **New variables:** actor behavioral history (repeated-brinksmanship count) — see round-2 variables §1; a ceasefire-floor durability (`persistent/floor`) is schema-v0.2, approximate as `permanent` for now.
- **Note:** anchor probabilities and repeated-actor base rate on the wiki's ~8-cycle observation, per [[strategy/sim2075-third-gulf-war-interaction]] §3.2.

### A2. `STRAIT_OF_HORMUZ_CRISIS` — P1 [registry, Phase 0]

- **Discontinuity:** Physical closure or effective interdiction of Hormuz transit for weeks+, not a price wobble. ~20% of seaborne oil.
- **Type:** 3 (Contingent). Short window, sharp resolution.
- **Provisional loadings:** F_MENA ~0.50, F_GPT ~0.35, F_FIN ~0.30 (transmits hard to `oil_brent`).
- **Consumers:** triggered_by `ISRAEL_IRAN_WAR`, `IRAN_REGIME_CHANGE`; triggers `OIL_SUPPLY_SHOCK` (near-deterministic), `GLOBAL_FINANCIAL_CRISIS` (delta).
- **New variables:** chokepoint-transit-status could be a global observable; candidate in round-2 variables §4.

### A3. `GULF_STATE_ATTACKS` — P1 [registry, Phase 0]

- **Discontinuity:** Direct kinetic strikes on Gulf state infrastructure (Abqaiq-class), distinct from regime instability. Tests the one specified *negative* cascade (external threat consolidates Gulf regimes, ×0.7 on `SAUDI_REGIME_INSTABILITY`) — see [[strategy/emergent-ideas]] idea 6.
- **Type:** 3 (Contingent).
- **Provisional loadings:** F_MENA ~0.55, F_GPT ~0.30, F_FIN ~0.25.
- **Consumers:** triggered_by `ISRAEL_IRAN_WAR`; triggers `OIL_SUPPLY_SHOCK`; **negative** cascade to `SAUDI_REGIME_INSTABILITY` (preserve and stress-test the consolidation coupling).

### A4. `NATO_RUSSIA_DIRECT_CONFLICT` — P1 [registry]

- **Discontinuity:** Article-5-triggering direct NATO–Russia military engagement. Absent from the catalog despite being in the original planned categories (§2) at 0.5–2%/yr; referenced as `NATO_ARTICLE_5_CRISIS` / `NATO_CRISIS`.
- **Type:** 3 (Contingent) with a nuclear-escalation sub-branch.
- **Provisional loadings:** F_GPT ~0.60 (dominant), F_EUR ~0.45, F_FIN ~0.25.
- **Consumers:** triggered_by `RUSSIA_STATE_FAILURE`, `UKRAINE_CONFLICT_RESOLUTION` (collapse branch); triggers `EU_FRAGMENTATION` (cohesion stress or rally), `GLOBAL_FINANCIAL_CRISIS`.
- **New variables:** nuclear-use-threshold / escalation-ladder-rung — likely schema-v0.2; for v0.1 use a resolution branch.

### A5. `US_CHINA_DIRECT_CONFLICT` — P2 [registry]

- **Discontinuity:** Direct US–China kinetic conflict *outside* the Taiwan scenario (e.g., South China Sea, Korea-entangled). Distinct from `TAIWAN_CONFLICT` and `US_CHINA_ECONOMIC_RUPTURE`.
- **Type:** 3 (Contingent).
- **Provisional loadings:** F_GPT ~0.65, F_EAS ~0.50, F_FIN ~0.30.
- **Consumers:** triggered_by `KOREAN_PENINSULA_CRISIS`, `TAIWAN_CONFLICT` (spillover); overlaps Taiwan — author must justify non-duplication or fold.

### A6. `NPT_REGIME_COLLAPSE` — P1 [registry]

- **Discontinuity:** Cascade proliferation — the NPT's near-universal-restraint norm breaks and 3+ threshold states weaponize in a decade. Not any single acquisition (those are separate events) but the *systemic* norm collapse. Referenced as `NPT_REGIME_EROSION`, `NPT_REGIME_COLLAPSE`, `GLOBAL_NUCLEAR_RECONFIGURATION`; absorbs `TURKEY_NUCLEAR_RECONSIDERATION`, `EGYPT_NUCLEAR_PROGRAM`.
- **Type:** 2 (Threshold) — pressure = count of recent acquisitions + threshold-state count + alliance-credibility damage.
- **Provisional loadings:** F_GPT ~0.50, F_MENA ~0.35, F_EAS ~0.25, F_TECH ~0.15.
- **Consumers:** triggered_by `IRAN_NUCLEAR_ACQUISITION`, `SAUDI_NUCLEAR_ACQUISITION`; triggers every regional-conflict event (delta to conflict lethality).
- **New variables:** `nuclear_status` already exists (NONE/THRESHOLD/POSSESSED) — this event reads the global count. Alliance-credibility-damage ratchet is a round-2 variable candidate.

### A7. `NUCLEAR_SECURITY_CRISIS` — P2 [registry]

- **Discontinuity:** Loss of positive control over nuclear weapons/materials during state collapse (Pakistan or Russia the reference cases) — not use, but custody failure.
- **Type:** 2/3 hybrid — conditional on a state-failure event firing, then a custody-outcome resolution.
- **Provisional loadings:** F_GPT ~0.40, F_SAS ~0.30 (Pakistan), F_EUR ~0.20 (Russia).
- **Consumers:** triggered_by `PAKISTAN_STATE_FAILURE`, `RUSSIA_STATE_FAILURE`.

### A8. `NUCLEAR_FIRST_USE` — P1 [standout omission]

- **Discontinuity:** First combat use of a nuclear weapon since 1945 — the taboo break. This is **distinct from every nuclear event already in the catalog**: acquisition (`IRAN_/SAUDI_NUCLEAR_ACQUISITION`), systemic proliferation (`NPT_REGIME_COLLAPSE`, A6), and custody failure (`NUCLEAR_SECURITY_CRISIS`, A7) all leave the 80-year non-use norm intact. Detonation-in-anger is its own civilizational discontinuity and the single largest gap in the catalog. The July 2026 sweep found no `NUCLEAR_USE`/`NUCLEAR_TABOO` event of any kind.
- **Type:** 3 (Contingent) — conditional on a nuclear-armed dyad already in active conflict; resolution = use vs. non-use, then a second clock for the post-taboo world (limited exchange, escalation, or one-off).
- **Provisional loadings:** F_GPT ~0.55 (dominant), plus the regional factor of whichever dyad fires (F_SAS for India–Pakistan, F_EAS for Korea/Taiwan, F_MENA for Israel–Iran).
- **Consumers:** triggered_by `INDIA_PAKISTAN_MILITARY_CONFLICT`, `KOREAN_PENINSULA_CRISIS`, `NATO_RUSSIA_DIRECT_CONFLICT`, `TAIWAN_CONFLICT`; triggers a broad delta to `NPT_REGIME_COLLAPSE` (norm shattered → cascade proliferation) and a global risk-off shock. The aftermath branch is a *permanent* change to the whole model's nuclear-conflict priors — a strong candidate for the ratchet treatment in [[methodology/reference/state-variables-round-2]] §3.
- **Note:** the hardest Type 3 in the catalog to calibrate honestly (n=1 reference, 1945). Lean hard on the [[methodology/concepts/entropy-maximization]] default and invest in the *aftermath* branch (tractable) over the resolution probability (intractable), per [[methodology/project/open-questions]] Q2.

---

## B. State Failure & Regional Collapse

Fills the biggest *named-but-absent* cluster (Sahel cascade sub-events) and the original planned list's gaps (Nigeria, Ethiopia, South Africa, Venezuela).

### B1. `NIGERIA_STATE_FAILURE` — P1 [planned-categories gap + registry]

- **Discontinuity:** Loss of central-government control across multiple regions of Africa's demographic giant (~400M by 2050). In the original planned list at 2–4%/yr but never specified; referenced from Sahel as `NIGERIA_NORTHERN_CRISIS` / `..._DESTABILIZATION`.
- **Type:** 2 (Threshold).
- **Provisional loadings:** F_SSA ~0.60 (dominant), F_FOOD ~0.30, F_FIN ~0.20 (oil exporter), F_CLIM ~0.20.
- **Consumers:** triggered_by `SAHEL_CATASTROPHE`; triggers `OIL_SUPPLY_SHOCK` (Niger Delta), `EUROPEAN_MIGRATION_CRISIS`, `COASTAL_WEST_AFRICA_DESTABILIZATION`.
- **Pairwise:** compare to Pakistan/Egypt state-failure specs for probability coherence.

### B2. `ETHIOPIA_STATE_FRAGMENTATION` — P2 [planned-categories gap]

- **Discontinuity:** Fragmentation of the East African anchor along ethno-regional lines; Nile-water implications for Egypt/Sudan (GERD).
- **Type:** 2 (Threshold).
- **Provisional loadings:** F_SSA ~0.60, F_FOOD ~0.30, F_MENA ~0.15 (Nile linkage to Egypt).
- **Consumers:** triggers `EGYPT_STATE_FAILURE` (water-stress delta), `GLOBAL_HUMANITARIAN_CAPACITY_CRISIS`.

### B3. `SOUTH_AFRICA_INSTITUTIONAL_COLLAPSE` — P2 [planned-categories gap]

- **Discontinuity:** Grid/state-capacity collapse in the regional economic anchor; distinct from slow decline (the discontinuity is a step-change in state function — sustained grid failure, fiscal breakdown).
- **Type:** 2 (Threshold).
- **Provisional loadings:** F_SSA ~0.65, F_FIN ~0.25.
- **New variables:** grid/electricity-reliability is a candidate infrastructure variable — round-2 variables §4.

### B4. `VENEZUELA_COMPLETE_COLLAPSE` — P3 [planned-categories gap]

- **Discontinuity:** Terminal collapse from the ongoing baseline; the modeling value is as a *regional-spillover reference case* (Colombia, Brazil migration) more than a low-probability shock.
- **Type:** 2 (Threshold), pressure already near-max.
- **Provisional loadings:** F_LAM ~0.70, F_FIN ~0.20.

### B5. `COASTAL_WEST_AFRICA_DESTABILIZATION` — P2 [registry]

- **Discontinuity:** Jihadist/insurgency spread from the Sahel to the coastal states (Ghana, Côte d'Ivoire, Benin, Togo) — a qualitative regional break, not the Sahel event itself. Absorbs `GHANA_POLITICAL_CRISIS`, `COTE_DIVOIRE_INSTABILITY` as internal texture.
- **Type:** 2 (Threshold).
- **Provisional loadings:** F_SSA ~0.60, F_FOOD ~0.25, F_MENA ~0.10.
- **Consumers:** triggered_by `SAHEL_CATASTROPHE`, `NIGERIA_STATE_FAILURE`.

---

## C. Migration, Displacement & Humanitarian

A seven-ID cascade-reference cluster collapses to essentially one missing event class. The displacement *variables* exist ([[methodology/reference/state-variables-country]] §2.2); the *system-capacity* discontinuity does not.

### C1. `EUROPEAN_MIGRATION_CRISIS` — P1 [registry]

- **Discontinuity:** A migration surge that overwhelms EU absorption/political capacity — the 2015-scale-or-worse political discontinuity, measured by political response (border closures, EU-cohesion damage), not headcount alone. Canonical target for the seven-ID cascade-reference cluster (`MASS_MIGRATION_CRISIS`, `EUROPEAN_REFUGEE_CRISIS`, `EU_MIGRATION_CRISIS`, `REFUGEE_CRISIS_MENA`, `REFUGEE_CRISIS_MAJOR`, `GLOBAL_REFUGEE_CRISIS`, plus itself — full mapping in [[events/backlog-registry]]).
- **Type:** 2/3 hybrid — pressure from upstream displacement stocks; resolution = political response class.
- **Provisional loadings:** F_EUR ~0.55 (dominant), F_MENA ~0.30, F_SSA ~0.20.
- **Consumers:** triggered_by nearly every MENA/SSA state-failure and conflict event (displacement→hosting transmission per [[methodology/reference/state-transmission]]); triggers `EU_FRAGMENTATION`.
- **New variables:** host-country absorption-capacity / political-tolerance threshold — round-2 variables §2. Reads existing `refugees_hosted`, `idp_population`, `refugees_abroad`.

### C2. `GLOBAL_HUMANITARIAN_CAPACITY_CRISIS` — P3 [registry]

- **Discontinuity:** Simultaneous humanitarian emergencies exceed global response capacity (funding, agencies, logistics) — a *systemic* aid-system break. Currently only one consumer (Sahel); hold as P3 until a second consumer appears (per registry note). If specified, it's the mechanism by which multiple regional collapses compound super-linearly.
- **Type:** 2 (Threshold), pressure = concurrent active displacement crises.
- **Provisional loadings:** F_SSA ~0.35, F_MENA ~0.25, F_FOOD ~0.25, F_FIN ~0.15.

---

## D. Climate, Food & Infrastructure

The physical-tipping tail is well covered; the *transmission/adaptation-failure* tail is not.

### D1. `WEST_ANTARCTIC_ICE_SHEET_DESTABILIZATION` — P2 [planned-categories gap]

- **Discontinuity:** Commitment to multi-meter sea-level rise via WAIS marine-ice-sheet instability. In the original climate list (0.5–1%/yr) but never specified. Slow-onset but effectively irreversible commitment — the discontinuity is crossing the commitment threshold, distinct from the gradual `sea_level_global` drift.
- **Type:** 2 (Threshold).
- **Provisional loadings:** F_CLIM ~0.75 (dominant), F_FOOD ~0.10.
- **Consumers:** shocks `sea_level_global` trajectory (delayed, multi-decade); triggers `CLIMATE_INSURANCE_CRISIS`, coastal-exposure impacts across low-lying entities.

### D2. `ARCTIC_SEA_ICE_COLLAPSE` — P2 [planned-categories gap]

- **Discontinuity:** First reliably ice-free September Arctic; albedo feedback + shipping-route opening. In the original list (2–4%/yr).
- **Type:** 2 (Threshold), reads `arctic_sea_ice_sept`.
- **Provisional loadings:** F_CLIM ~0.70, F_GPT ~0.15 (Arctic access competition).

### D3. `CLIMATE_INSURANCE_CRISIS` — P1 [registry + strategy]

- **Discontinuity:** Insurance/reinsurance withdrawal from climate-exposed regions makes property uninsurable at scale — a financial-system transmission of climate risk. Referenced as `GLOBAL_REINSURANCE_CRISIS`; the war-validation work flagged reinsurance floors as a load-bearing ratchet variable ([[strategy/sim2075-third-gulf-war-interaction]] §3, insurance-floor lock-in).
- **Type:** 2 (Threshold), pressure = `climate_variability` + accumulated catastrophe losses.
- **Provisional loadings:** F_CLIM ~0.45, F_FIN ~0.45, F_EUR ~0.15.
- **New variables:** insurance-availability / reinsurance-floor is the canonical **ratchet** variable (asymmetric: easy to lose, hard to restore) — round-2 variables §3.

### D4. `MAJOR_BREADBASKET_FAILURE` — P2 [coverage gap]

- **Discontinuity:** Simultaneous multi-breadbasket harvest failure (correlated climate extremes hitting 2+ of US/EU/Black Sea/India/China grain belts in one year). Distinct from the agricultural *breakthrough* event and from gradual yield stress — the discontinuity is the correlated simultaneity.
- **Type:** 1/2 hybrid — stochastic weather with climate-rising base rate.
- **Provisional loadings:** F_FOOD ~0.60 (dominant), F_CLIM ~0.40.
- **Consumers:** shocks `wheat_price`, `rice_price`, `corn_price`, `food_stocks_grains`; triggers `SAHEL_CATASTROPHE`, `EGYPT_STATE_FAILURE`, `EUROPEAN_MIGRATION_CRISIS` (food-price→instability transmission).
- **Note:** high tail-relevance — correlated food shock is a classic cascade amplifier; likely a sensitivity-analysis driver.

### D5. `WATER_CRISIS_TRANSBOUNDARY` — P3 [coverage gap]

- **Discontinuity:** Transboundary water-sharing breakdown (Nile/GERD, Indus, Mekong, Tigris-Euphrates) escalating to interstate coercion. Water-stress is currently a slow variable with no discrete-conflict event consuming it.
- **Type:** 3 (Contingent).
- **Provisional loadings:** F_MENA ~0.35, F_SAS ~0.30, F_FOOD ~0.20, F_SSA ~0.15. (Author should consider splitting by basin.)

---

## E. Technology & Systemic Infrastructure

The highest-uncertainty domain; the original list named four, only breakthroughs were specified. These are the *disruption* (non-breakthrough) side.

### E1. `AI_LABOR_MARKET_DISRUPTION` — P2 [planned-categories gap]

- **Discontinuity:** The hard case. Baseline already assumes rising `ai_capability_index`; the *event* is a specific threshold crossing that restructures employment fast enough to outpace absorption (a discrete labor-market break, not the capability curve). Author must define the threshold crisply or fold to baseline — see [[methodology/project/open-questions]] and the exclusion note in [[events/planned-breakthrough-events]].
- **Type:** 2 (Threshold) on `ai_capability_index`, or decline as baseline. Genuine open question.
- **Provisional loadings:** F_TECH ~0.65 (dominant), F_FIN ~0.25.
- **New variables:** possibly a labor-displacement / automation-exposure variable — round-2 variables §4. High risk of synthetic-variable trap; hold to the dossier standard.

### E2. `MAJOR_CYBER_INFRASTRUCTURE_ATTACK` — P1 [planned-categories gap]

- **Discontinuity:** Cyber attack causing sustained physical-infrastructure failure (grid, financial rails, comms) across a major economy — days-to-weeks, not hours. In the original list (2–5%/yr), never specified.
- **Type:** 1/2 hybrid — stochastic with F_GPT-conditioned rate.
- **Provisional loadings:** F_TECH ~0.45, F_GPT ~0.40, F_FIN ~0.25.
- **Consumers:** triggered_by `TAIWAN_CONFLICT`, `NATO_RUSSIA_DIRECT_CONFLICT`, `US_CHINA_DIRECT_CONFLICT`; triggers `GLOBAL_FINANCIAL_CRISIS`.
- **New variables:** grid/critical-infrastructure-reliability — round-2 variables §4.

### E3. `SEMICONDUCTOR_SUPPLY_COLLAPSE` — P2 [planned-categories gap]

- **Discontinuity:** Non-conflict TSMC/Taiwan-concentration disruption (earthquake, industrial accident, non-military crisis) collapsing `semiconductor_supply`. Distinct from `TAIWAN_CONFLICT` (which also shocks this) — captures the concentration risk independent of war.
- **Type:** 1 (Stochastic).
- **Provisional loadings:** F_TECH ~0.55, F_EAS ~0.30, F_FIN ~0.20.
- **Consumers:** shocks `semiconductor_supply`; author must justify non-duplication with Taiwan (this is the peacetime tail).

### E4. `GNSS_SPACE_INFRASTRUCTURE_LOSS` — P3 [coverage gap]

- **Discontinuity:** Loss of GPS/GNSS or major satellite-constellation function (Kessler cascade, ASAT exchange, severe space weather / Carrington-class event). Underpins logistics, finance timing, precision agriculture.
- **Type:** 1/3 hybrid — natural (space weather) is Type 1; ASAT is Type 3.
- **Provisional loadings:** F_TECH ~0.50, F_GPT ~0.30.
- **Note:** consider splitting natural vs. adversarial into two events.

---

## F. Positive / De-escalation Discontinuities

Per [[methodology/project/open-questions]] resolved-Q4: the framework is valence-neutral, but the catalog under-populates favorable *contingent* resolutions and non-breakthrough positive shocks. [[strategy/emergent-ideas]] idea 6 (negative-structure audit) is the sibling concern; these are its positive-shock counterpart.

### F1. `UKRAINE_CONFLICT_RESOLUTION` — P1 [registry]

- **Discontinuity:** Durable settlement of the Russia–Ukraine war (either direction — negotiated peace *or* frozen-conflict lock-in). Referenced from `RUSSIA_STATE_FAILURE`. Note: a *negative* resolution (Russian collapse-driven) feeds `NATO_RUSSIA_DIRECT_CONFLICT` — mixed valence, as the framework expects.
- **Type:** 3 (Contingent).
- **Provisional loadings:** F_EUR ~0.45, F_GPT ~0.40, F_FIN ~0.20 (reconstruction, energy, sanctions unwind).
- **Consumers:** triggered_by `RUSSIA_STATE_FAILURE`; resolution branches feed `EU_FRAGMENTATION` (relief) and reserve/energy variables.

### F2. `US_CHINA_DETENTE` — P3 [asymmetry gap]

- **Discontinuity:** Durable managed-competition settlement lowering F_GPT structurally — the favorable long-run resolution the tension events (`TAIWAN_CONFLICT`, `US_CHINA_ECONOMIC_RUPTURE`) currently under-branch.
- **Type:** 3 (Contingent).
- **Provisional loadings:** F_GPT ~-0.55 (note: *negative* loading — this event fires when F_GPT is low), F_EAS ~-0.30, F_FIN ~0.20.
- **Note:** negative-loading events are the mechanism for positive tails; verify the variance-allocation math handles sign correctly. Good stress test of [[strategy/emergent-ideas]] idea 6 tooling.

### F3. `MAJOR_CLIMATE_COOPERATION_BREAKTHROUGH` — P3 [asymmetry gap]

- **Discontinuity:** A binding, enforced emissions/finance agreement that discretely bends the `global_co2_ppm` trajectory — distinct from the S-curve of renewable cost decline (baseline). Type 3 example used in [[methodology/reference/priority-event-ranking]] "using this ranking."
- **Type:** 3 (Contingent), ~30–40% resolution success when window opens.
- **Provisional loadings:** F_CLIM ~-0.50, F_GPT ~-0.20, F_FOOD ~-0.15.

---

## H. Health & Bio

Only one health event exists (`SEVERE_PANDEMIC`, natural) plus the antimicrobial *breakthrough*. The deliberate/engineered and slow-burn-resistance tails are unrepresented.

### H1. `ENGINEERED_PANDEMIC` — P1 [coverage gap]

- **Discontinuity:** A pandemic whose *origin* differs from `SEVERE_PANDEMIC` (Type 1 natural spillover) — an engineered or laboratory-origin pathogen. The modeling distinction is purely the generating mechanism and its resulting probability structure and severity distribution; the spec describes *outcomes and base rates*, never how such a pathogen would be produced. Whether its tail differs enough from the pandemic event's `catastrophic` branch to warrant a separate event is the author's first question — fold if not.
- **Type:** 2/3 hybrid — an intent-conditioned pathway (Type 3) and a lab-accident stochastic rate that scales with biotech diffusion (Type 2). Base rates come from published biosecurity/GCR risk assessments ([[methodology/reference/research-documentation-standards]]); consider splitting the two pathways.
- **Provisional loadings:** F_HLTH ~0.55 (dominant), F_TECH ~0.35, F_GPT ~0.20.
- **Consumers:** shocks `pandemic_status`/`pandemic_severity`; triggers `GLOBAL_FINANCIAL_CRISIS`, mortality shocks to population cohorts. A biotech-diffusion *proxy* variable (an observable index of capability spread drawn from the literature, not a how-to) could serve as the Type 2 pressure term — hold it to the synthetic-variable dossier standard.

### H2. `ANTIMICROBIAL_RESISTANCE_CRISIS` — P2 [asymmetry gap]

- **Discontinuity:** AMR crosses a threshold where routine infections/surgery become high-mortality — the *negative* counterpart to the `ANTIMICROBIAL_PLATFORM` breakthrough (which currently shocks `antibiotic_resistance` downward with no upward-crisis event to balance it). Reads the existing `antibiotic_resistance` slow-rising variable.
- **Type:** 2 (Threshold) on `antibiotic_resistance`.
- **Provisional loadings:** F_HLTH ~0.60, F_FOOD ~0.15 (livestock antibiotic use).

### H3. `VACCINE_CONFIDENCE_COLLAPSE` — P3 [coverage gap]

- **Discontinuity:** Sustained collapse in vaccination coverage returns controlled diseases (measles, polio) to endemic circulation in high-income populations — a public-health discontinuity driven by institutional-trust erosion.
- **Type:** 2 (Threshold). **Synthetic-trap risk** on the "trust" driver — ground in observable coverage rates (WHO/UNICEF WUENIC), not sentiment.
- **Provisional loadings:** F_HLTH ~0.45, plus regional factors.

---

## I. Frontier Technology (disruption tail)

The original list named "AI disruption" as highest-uncertainty; E1 covers the labor case. These are the other frontier-AI discontinuities the [[methodology/project/open-questions]] AI discussion flags as needing separate treatment.

### I1. `TRANSFORMATIVE_AI_THRESHOLD` — P2 [open-questions gap]

- **Discontinuity:** A specific capability threshold crossing (broadly capable autonomous systems) that discretely restructures economic/strategic dynamics — *not* the `ai_capability_index` S-curve (baseline), but a named threshold with step-change downstream effects. The hardest specification in the catalog; the exclusion note in [[events/planned-breakthrough-events]] and [[methodology/project/open-questions]] both defer it. Author must define the threshold operationally or decline. Genuinely may not be specifiable at Level 1.
- **Type:** 2 (Threshold) on `ai_capability_index`, or decline as baseline. Mixed valence — this is not intrinsically positive or negative.
- **Provisional loadings:** F_TECH ~0.70 (dominant), F_GPT ~0.30, F_FIN ~0.25.

### I2. `AUTONOMOUS_SYSTEMS_ACCIDENT` — P2 [coverage gap]

- **Discontinuity:** A high-consequence failure of a deployed autonomous/AI system — financial (flash-crash-scale), military (unintended-escalation), or infrastructure — distinct from a deliberate cyber attack (E2) and from labor disruption (E1). Captures the AI-reliability tail.
- **Type:** 1 (Stochastic), rate rising with autonomous-system deployment.
- **Provisional loadings:** F_TECH ~0.50, F_FIN ~0.25, F_GPT ~0.20.

---

## J. Climate Policy & Adaptation Failure

The physical-tipping tail is covered (round-1 + D1/D2); the *human-response* tail — unilateral intervention and adaptation-threshold crossing — is not.

### J1. `UNILATERAL_GEOENGINEERING` — P2 [deferred-in-breakthrough-doc]

- **Discontinuity:** Unilateral solar-radiation-management deployment by a state or coalition — a Type 3 *policy/deployment decision* (explicitly parked in [[events/planned-breakthrough-events]] "Considered but Excluded" as not-a-breakthrough). Carries a distinctive **termination-shock** risk: if deployment stops abruptly, suppressed warming returns fast. Mixed valence and a geopolitical flashpoint (who controls the thermostat).
- **Type:** 3 (Contingent) — window = a climate-desperation trigger; resolution = deploy/cooperate/conflict.
- **Provisional loadings:** F_CLIM ~0.45, F_GPT ~0.40, F_FOOD ~0.15.
- **New variables:** an SRM-deployment-status global variable; termination-shock is a natural `persistent`/ratchet interaction — see [[methodology/reference/state-variables-round-2]] §3.

### J2. `LETHAL_HEAT_THRESHOLD` — P2 [unconsumed-variable gap]

- **Discontinuity:** Wet-bulb temperatures cross survivability limits for sustained periods across populous regions (Gulf, South Asia, Sahel), forcing abandonment/mass seasonal displacement. The `heat_exposure` country variable exists but no event consumes it as a threshold crossing.
- **Type:** 2 (Threshold) on `heat_exposure` × `global_temp_anomaly`.
- **Provisional loadings:** F_CLIM ~0.50, F_SAS ~0.25, F_MENA ~0.20, F_FOOD ~0.15.
- **Consumers:** triggers `EUROPEAN_MIGRATION_CRISIS`, `EGYPT_/PAKISTAN_STATE_FAILURE` (habitability→displacement).

---

## K. Economic-Demographic & Resource

### K1. `AGING_SOCIETY_FISCAL_CRISIS` — P2 [coverage gap]

- **Discontinuity:** Pension/healthcare-obligation load in a rapidly-aging economy (Japan, Italy, Korea, China) forces a fiscal discontinuity — sovereign stress or forced entitlement restructuring — distinct from a market-driven `GLOBAL_FINANCIAL_CRISIS`. The state model tracks rich age-cohort demographics that currently feed no fiscal-crisis event. Check overlap with `DOLLAR_RESERVE_CRISIS`/`EUROZONE_SOVEREIGN_CRISIS` (queue) before specifying.
- **Type:** 2 (Threshold) on `dependency_ratio` × `debt_public`.
- **Provisional loadings:** F_FIN ~0.55, plus regional factor (F_EAS or F_EUR).

### K2. `CRITICAL_MINERALS_WEAPONIZATION` — P2 [unconsumed-variable gap]

- **Discontinuity:** Weaponized restriction of rare-earth / critical-mineral supply (China concentration) as economic coercion — collapses `rare_earths_index` availability, which no current event consumes. The materials-side counterpart to `SEMICONDUCTOR_SUPPLY_COLLAPSE` (E3).
- **Type:** 2/3 hybrid — F_GPT-conditioned policy decision.
- **Provisional loadings:** F_GPT ~0.45, F_TECH ~0.35, F_EAS ~0.25.
- **Consumers:** shocks `rare_earths_index`; transmits to energy-transition and defense-industrial variables; triggered_by `US_CHINA_ECONOMIC_RUPTURE`.

### K3. `INDIA_POLITICAL_CRISIS` — P2 [major-power gap]

- **Discontinuity:** Democratic backsliding to breakdown, or a governance crisis, in the world's largest democracy and soon-largest economy — absent from the catalog despite majors like the US, China, Russia, Turkey, EU all having political-crisis events.
- **Type:** 2 (Threshold).
- **Provisional loadings:** F_SAS ~0.60 (dominant), F_GPT ~0.15.
- **Consumers:** interacts with `INDIA_PAKISTAN_MILITARY_CONFLICT` (a nationalist-crisis→conflict delta).

---

## G. Low-Priority Queue (author only if sensitivity analysis surfaces them)

Registry declines and Tier-2-region references, held explicitly so they are consciously deferred, not forgotten. All cross-listed in [[events/backlog-registry]].

| Candidate ID | Region/domain | Gate to promote |
|---|---|---|
| `KURDISH_STATE_FORMATION` | MENA cross-border | Turkey/Iran/Iraq event shows Kurdish branch drives tails |
| `CAUCASUS_CONFLICT` | Post-Soviet | Russia-failure aftermath shown tail-relevant |
| `CENTRAL_ASIA_INSTABILITY` | Post-Soviet / Tier 2 | Same |
| `MAGHREB_INSTABILITY` | North Africa / Tier 2 | Sahel/migration spillover shown tail-relevant |
| `JAPANESE_POLITICAL_TRANSFORMATION` | East Asia | Original planned list §7; defense/immigration regime shift |
| `EMERGING_MARKET_CONTAGION` | Financial | Original planned list §4; may already be captured by GFC correlation structure — check before specifying |
| `EUROZONE_SOVEREIGN_CRISIS` | Financial/Europe | Original list §4; check overlap with `EU_FRAGMENTATION` + `GLOBAL_FINANCIAL_CRISIS` |

---

## Summary

| Section | Stubs | P1 | P2 | P3 |
|---|---|---|---|---|
| A. Nuclear & Great-Power | 8 | 6 | 2 | 0 |
| B. State Failure & Regional | 5 | 1 | 3 | 1 |
| C. Migration & Humanitarian | 2 | 1 | 0 | 1 |
| D. Climate, Food & Infrastructure | 5 | 1 | 3 | 1 |
| E. Technology & Infrastructure | 4 | 1 | 2 | 1 |
| F. Positive / De-escalation | 3 | 1 | 0 | 2 |
| H. Health & Bio | 3 | 1 | 1 | 1 |
| I. Frontier Technology | 2 | 0 | 2 | 0 |
| J. Climate Policy & Adaptation | 2 | 0 | 2 | 0 |
| K. Economic-Demographic & Resource | 3 | 0 | 3 | 0 |
| G. Low-priority queue | 7 | — | — | 7 |
| **Total** | **44** | **12** | **18** | **14** |

If the twelve P1 stubs are authored, the catalog grows from 29 to ~41 events — landing in the original 40–60 target band ([[events/planned-event-categories]]), clearing every registry-mandated dangling reference, and closing the two largest civilizational-scale omissions (nuclear first use, engineered pandemic). That set is the natural **catalog v1.1** release ([[methodology/reference/catalog-versioning]] §4). **The P2/P3 stubs are backlog, not a work order** — see the drawback note below; they should be promoted to full specs only on a demand signal (registry, world event, or Phase 2 sensitivity analysis), not for completeness.

## Why stubs but not specs: the cost of premature catalog growth

Recording a stub costs ~nothing and commits to nothing — the same evidence discipline [[strategy/emergent-ideas]] applies to process ideas. **Authoring a stub to Level 1 is where the cost lands**, and [[methodology/reference/catalog-versioning]] is explicit that growth is "prioritized by demonstrated model deficiency, not encyclopedic completeness." Concretely, each full spec:

1. **Spends elicitation budget** — O(k) documented judgments that must each survive review and be kept coherent (§5, "which additions does this release buy, and why these").
2. **Adds coherence debt** — every new event enlarges the pairwise-ranking cross-check ([[methodology/reference/priority-event-ranking]]) and the implied-correlation re-derivation, and creates new chances for dangling references and double-counting in Ω.
3. **Can make the model *worse*, not just costlier** — a catalog that keeps adding *amplifying* couplings without the negative-structure audit ([[strategy/emergent-ideas]] idea 6) overstates tail clustering by construction, corrupting the headline tail-driver output.
4. **Is spent blind before Phase 2** — the sensitivity instrument that tells you *which* events actually move tail outcomes doesn't exist until the engine does. Authoring a large batch now risks investing in events that load only on factors that drive nothing.
5. **Trades against the binding constraint** — the project's critical path is the Phase 1 engine, not more specs. 29 events you can run beats 44 you can't; Monte Carlo results are only comparable within a catalog version anyway.

**The discipline is at the promotion gate, not the capture gate.** Keep this list rich; promote in small, signal-driven releases.

## Ensemble authoring notes

- **Parallelizable:** stubs are independent except where a cascade target is itself a stub (author the target's ID first, or use a placeholder and reconcile at release). The eleven sections can go to separate agents.
- **Coherence pass required after authoring:** run every new probability through [[methodology/reference/priority-event-ranking]] pairwise, and re-derive implied event correlations per [[methodology/project/open-questions]] resolved-Q1 remaining work.
- **Variables gate the release, not the authoring:** a stub that needs a new variable can be drafted against the [[methodology/reference/state-variables-round-2]] stub, but the variable's dossier (§3 of [[methodology/reference/catalog-versioning]]) must complete before v1.1 ships.
- **Decline is a valid outcome:** E1 (AI labor), A5 (US-China direct), E3 (semiconductor) each have a real fold/duplication risk flagged inline. A reasoned decline that updates [[events/backlog-registry]] counts as done.

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-07-13 | Initial stub catalog (33 stubs across 7 sections) | Demand-signal batch: registry sweep + planned-category gaps + asymmetry gaps |
| 2026-07-13 | Second expansion: +11 stubs (nuclear first use; §§H–K health/bio, frontier tech, climate policy, economic-demographic); added premature-growth cost note | Fill remaining domain gaps at zero commitment; make the stub-vs-spec cost distinction explicit so the list stays backlog, not a work order |
