---
title: war-validation-report
type: research-input
permalink: strategy/inputs/war-validation-report
tags:
- strategy
- research
- validation
- third-gulf-war
---

# Sim2075 Event Catalog vs. the Third Gulf War: Retrospective Assessment

*Research subagent report, July 10, 2026. Sources: Third Gulf War research wiki (Home, War Onset, Pre-War Decision, Mousavi Warhead Announcement, Trends/Iranian State Instability, monthly updates through 30 June 2026) and sim2075 repo event specs (`events/...`, `methodology/reference/causal-types.md`, `methodology/concepts/tractability-boundaries.md`). The sim2075 specs under review carry changelogs dated 2025-12-19/30 — roughly 60 days before the war began.*

---

## (a) What actually happened

- **Onset (28 Feb 2026):** Coordinated US ("Epic Fury") and Israeli ("Roaring Lion") strikes on Iran killed Supreme Leader Khamenei and ~40 senior officials in Tehran. Timing was set by a perishable CIA intelligence window on Khamenei's location — while negotiations were actively underway (Iran's FM had called a "historic" agreement "within reach" three days earlier). Stated objective: preventing an Iranian nuclear weapon; a continuation of the June 2025 Twelve-Day War.
- **Preconditions (per wiki's "Five Shifts"):** Iran rebuilt missiles ~1,000→~2,500 and ~80,000 Shaheds post-June-2025; the decapitation destroyed the face-saving ceasefire model; Trump shifted from restrainer to co-belligerent; the Dec 2025–Jan 2026 protests (thousands killed by security forces) created a regime-change illusion the NIC explicitly rejected; military planning outpaced economic contingency planning.
- **Course:** Iran closed the Strait of Hormuz (2 Mar) with mines and later a formal toll/"selective access" regime; the US imposed a reverse blockade. Iranian retaliation struck Gulf energy infrastructure across UAE (Ruwais, Fujairah), Qatar (Ras Laffan LNG — 3–5 year repair, force majeure, a global helium cascade), and bases in Kuwait/Bahrain. Israel invaded Lebanon (16 Mar): 3,400+ killed and 800K+ displaced by late spring, an occupation that outlasted the US-Iran war. Houthis re-entered at Bab el-Mandeb.
- **Consequences:** Brent breached $119 by day 10 (Dubai touched $170 physical); SPR drawn to a 42-year low; gasoline >$4; fertilizer/food crisis (US winter wheat smallest since 1965, farm bankruptcies +130% y/y); Moody's ~$1,000/household realized cost. Great-power dimension: China supplied MANPADs (downed an F-15E) and possibly early-warning radar, banned refined-product exports, normalized PLA median-line sorties at Taiwan; Russia ran a Caspian resupply corridor and Western sanctions architecture unraveled. Wiki's macro thesis: "End of the American Century" — systemic primacy damaged, not capability.
- **Nuclear dimension:** Strikes did *not* eliminate the program. 440kg of 60% HEU intact; weaponization timeline unchanged (9–12 months); IAEA assessed nuclear risk *higher* than before the strikes; Iran floated HEU transfer to China.
- **Regime dimension:** Iran's regime did **not** fall. Mojtaba Khamenei succeeded within ~8 days (constitutionally, under IRGC coercion). Rally-around-flag held; but post-war instability preconditions worsened severely (rial at 1.9M/$, food inflation +300%, Iraqi militias patrolling Tehran, civilian-IRGC fracture).
- **End:** Day 110 (17 June 2026) "Islamabad MOU" — $300B fund, blockade lift + demining, HEU down-blended in-country, enrichment/missiles deferred. Implementation immediately oscillated (renewed US-Iran kinetic exchanges late June). The wiki recorded its own forecasting miss: it held escalation (B2) as modal for ~37 days; the war ended in the deal branch it priced at 11–20%.

---

## (b) Event-by-event comparison

| Catalog event | Spec (type, p/yr) | Did it occur? | Match quality |
|---|---|---|---|
| **OIL_SUPPLY_SHOCK** | Type 1, 2.5% (1.5–4.0%) | **Yes** | **Strong.** The spec's "Strait of Hormuz Closure" pathway names the exact trigger ("Iran-US conflict"), the exact exposure (~20% oil, ~25% LNG), mine-clearing as the duration driver (3–12 months — actual: ~3.5 months full closure, functional normalization projected into 2027), and insufficient bypass pipelines. Its "what would change estimate 2x+" table lists "US-Iran military conflict: +150%." The discontinuity definition (structural adaptation, not price spike) matched reality: selective-access regime, bypass capex, SPR depletion, petrodollar erosion. Notably, its *Case Against* arguments (shale insulation, demand elasticity, SPR buffer) are precisely why US damage ran shallower than the wiki's own wartime modeling ("The Shallower Curve"). |
| **IRAN_NUCLEAR_ACQUISITION** | Type 2/3 hybrid, 1.5% | Not resolved — but **the war is this event's `preemptive_strike_during_breakout` / `contested_acquisition` pathway** | **Strong on shape.** The aftermath branch reads like a synopsis: "Israel/US strikes... may delay but not prevent... likely escalation to regional conflict," cascading to OIL_SUPPLY_SHOCK at p=0.70 ("Hormuz disruption during conflict") and IRAN_REGIME_CHANGE ×1.5. The `acquisition_despite_strikes` logic (Osirak precedent: strikes delay, don't prevent; rally effect) is what the IAEA and analysts ("Twice Bombed, Still Nuclear") concluded. Whether Iran ultimately acquires remains open — HEU intact, monitoring blocked in late June. |
| **IRAN_REGIME_CHANGE** | Type 2, 1.2% | **No** — decapitation + managed succession, regime held | **Right for the right reasons.** The spec's own Case Against: a strike "might trigger rally-around-flag rather than collapse... The 10% [external-intervention branch] may overstate how reliably intervention produces regime change." That is exactly what happened, and exactly what the NIC told the White House. The pressure function's inputs (protest intensity, inflation/rial, succession positioning, Khamenei health) were precisely the pre-war warning signals that spiked Dec 2025–Feb 2026. The Dec 2025 protests (larger than 2022, thousands killed) look like the `popular_uprising_suppressed` branch hovering just under threshold. |
| **SAUDI_REGIME_INSTABILITY** | Type 2, ~0.8% | No | Cascade design validated: iran-regime-change specified a *negative* modifier (×0.7, "external threat consolidates Gulf regimes"). GCC states absorbed missile strikes and infrastructure damage without regime stress; consolidation is what occurred. |
| **SAUDI_NUCLEAR_ACQUISITION** | Type 3 window | No | Window preconditions moved in the specified direction: F_GPT logic ("US security commitment less credible → rapid acquisition more likely") maps onto the war's alliance-credibility damage. Nothing observable yet. |
| **US_CHINA_ECONOMIC_RUPTURE** | Type 3, 1.75% | No | Tension elevated exactly along F_GPT: first confirmed Chinese-weapons→US-aircraft-loss causality chain, refined-products export ban, HEU-transfer non-denial. No rupture — consistent with elevated-hazard-without-occurrence. |
| **TAIWAN_CONFLICT** | Type 3 | No | Preconditions shifted materially: US interceptor stockpile depletion (3+ years to replenish per CSIS), PLA median-line sortie normalization, Hegseth omitting Taiwan from ally roll call, wiki tracks "Finlandization drift." This is what a correlated F_GPT shock propagating into another event's window looks like. |
| **GLOBAL_FINANCIAL_CRISIS / DOLLAR_RESERVE_CRISIS** | — | No | Stagflation pressure, Fed "Central Bank Trap," petrodollar-replacement trend tracked — elevated but sub-threshold. |
| **US_CONSTITUTIONAL_CRISIS** | Type 2 | No | Strains tracked (War Powers fights, MOU withheld from Congress, electoral-manipulation trend) — sub-threshold. |
| **The war itself: US/Israel–Iran interstate war** | **Not in catalog** | **Yes — this is the event that happened** | **The central gap.** See (c). |

**Did the catalog contain the event?** Not as a first-class object. The war exists in the catalog only as *appendages of other events*: a 10% severity branch of IRAN_REGIME_CHANGE (`external_intervention_trigger`), the strike branches of IRAN_NUCLEAR_ACQUISITION, and a named trigger scenario inside OIL_SUPPLY_SHOCK. The specs even flag it themselves — `iran-regime-change.md` line 373: *"STRAIT_OF_HORMUZ_CRISIS, GULF_STATE_ATTACKS, ISRAEL_IRAN_WAR not in catalog."* And `planned-event-categories.md`'s Great Power Conflict section (Taiwan, US-China trade, NATO-Russia, Korea, India-Pakistan) contains **no Middle East interstate war** — despite the catalog being finalized six months *after* the June 2025 Twelve-Day War.

---

## (c) What the model got structurally right and wrong

### Right

1. **The gap is event-selection, not structural.** The framework could represent this war natively: it is a textbook Type 3 window/resolution event. Window preconditions were all observable state (unfinished Twelve-Day War, rebuilt Iranian arsenal, offensive-posture declaration Jan 2026, active negotiations); resolution turned on a small-N decision (Trump + Netanyahu, against IC advice, triggered by a perishable intelligence break). Nothing about the war violates the ontology — it just wasn't specified.

2. **The Type 3 tractability claim is strongly validated — by the author's own wiki.** `causal-types.md`: "resolution probabilities are low-tractability... the value comes from specifying *what follows* each resolution." The wiki, doing daily expert-level tracking with vastly more information than any prior model, still missed the resolution: B2-modal for 37 days while the war ended in a branch priced 11–20%, and separately documented "The Third Option Pattern" — seven instances of the US mispricing Iranian binary choices. Meanwhile the wiki's *consequence* analysis (fertilizer lock-in, oil price fiction, infrastructure irreversibility, strait-reopening two-barrier model) was repeatedly confirmed, sometimes weeks ahead of institutional sources. That is the tractability stratification (`tractability-boundaries.md`) observed in the wild: resolutions intractable, aftermaths tractable, impact magnitudes in between ("Shallower Curve": direction right, magnitude too aggressive).

3. **The discontinuity boundary rules gave the right answers.** `causal-types.md` Common Mistakes says explicitly: "Khamenei dying and being replaced by another Supreme Leader through normal processes ≠ Iran regime change," and "regime survives crisis = sub-threshold." Khamenei was *assassinated* and Mojtaba succeeded within days; the regime governs the same territory in the same institutional form. Under the model's rules, IRAN_REGIME_CHANGE correctly did not fire — and the strike-produces-rally-not-collapse skepticism in the spec's Case Against was the correct call, against the actual belief of the people who launched the war.

4. **Correlated-factor architecture matches the war's signature.** One MENA/GPT shock simultaneously elevated the hazard of nearly every cataloged event — Taiwan window, US-China rupture, dollar/financial stress, Saudi proliferation, US constitutional strain, food crisis — while (so far) none of them fired. That is exactly what a high F_MENA/F_GPT factor draw does in the model: correlated probability elevation, not deterministic cascade. The one negative cascade specified (external threat *consolidates* Gulf regimes) was also validated.

5. **Durability types are the right vocabulary.** The war's core economic lesson — "damage a ceasefire cannot fix" — is the persistent/decaying-with-floor distinction: oil *price* round-tripped to $80 within days of the MOU (decaying, short half-life), while Ras Laffan (3–5 yr), shipping-insurance actuarial closure, the institutionalized toll regime, and alliance-credibility damage persist regardless of the deal (persistent / floor > 0).

### Wrong or weak

1. **Hub-and-spoke inversion.** The catalog made regime change and nuclear acquisition the hubs, with war as a branch. Reality inverted this: the war happened *first* and is itself the hub now driving regime-instability and proliferation hazard. Because war-shaped outcomes were reachable only through other events' branches, the simulation would assign the observed world a composite path probability of very roughly 0.5–1%/yr — thin for something whose preconditions were flashing in the state variables the model itself defined.

2. **OIL_SUPPLY_SHOCK's Type 1 classification undercuts the model's own state-conditioning insight.** A flat stochastic rate can't respond to the Twelve-Day War, the protest wave, or a rebuilt missile arsenal. The spec's Probability Evolution nudges 2025–2035 to 2.0–3.0%, but the event fired ~60 days after specification under precursor conditions the framework's Type 2/3 machinery could have priced. Post-precursor hazard multipliers (a recent war between the same parties is the strongest known predictor of the next one) are missing.

3. **Single-resolution-per-event compresses multi-front, multi-clock wars.** The actual war had at least three semi-independent resolution clocks — US-Iran (TACO clock), Israel-Lebanon (Israel's veto; outlasted the main war), Iran-internal (succession/IRGC). The wiki's key structural finding, "Israel holds a veto that operates through non-compliance," has no representation in a one-window-one-resolution event.

4. **Transmission channels have their own thresholds and hysteresis.** The fertilizer→food→political chain, helium cascade, and insurance non-reset behaved like sub-events with lock-in dates and irreversibilities, not like smoothly decaying impact vectors on state variables. The impact-vector formalism understates this.

5. **Refugee/humanitarian magnitudes were regionally misallocated.** The specs' refugee flows attach to Iranian collapse (which didn't happen); the actual displacement crisis was Lebanese (800K+ within two weeks). Minor, but symptomatic of the missing-war hub: Lebanon appears in the catalog only as an impact row.

---

## (d) Does the project have predictive-framework value?

**As an event oracle: no, and it never claimed to be one.** The composite probability it would have assigned this specific war in 2026 was ~1%. But this is largely the low-tractability region the framework itself fenced off — and the wiki's real-time forecasting miss (B1 at 11–20% at signing) demonstrates that even maximal information doesn't buy resolution predictability. The framework predicted its own failure mode correctly.

**As a structural grammar: substantially validated.** Four design choices were tested by reality and held: (1) the Type 3 window/resolution decomposition with entropy-maximized resolutions — the war was a small-N decision on an observable window; (2) invest-in-aftermaths — aftermath reasoning is where both the specs and the wiki generated durable, confirmed insight; (3) durability typing — decaying vs. persistent-with-floor is precisely the ceasefire-can't-fix-it distinction; (4) discontinuity boundary rules — managed succession and survived crises correctly excluded. The correlated-factor design also matches the observed pattern of one shock elevating many hazards without firing them.

**The failure was curation, not architecture.** The catalog omitted the single most precondition-laden interstate war on Earth as of December 2025 — while its own specs referenced it three times as an uncataloged cascade target. Concrete fixes if the project resumes: (1) add first-class Type 3 events for US/Israel–Iran war, Hormuz crisis, and Gulf infrastructure attack (the cascade targets already named in comments); (2) add recent-precursor-war hazard multipliers and reclassify OIL_SUPPLY_SHOCK to a hybrid with a state-conditioned geopolitical pathway; (3) allow multi-front events with actor-specific resolution clocks; (4) treat "flagged as not-in-catalog inside another spec's cascade list" as a mandatory backlog item — the model knew what it was missing and said so in its own comments.
