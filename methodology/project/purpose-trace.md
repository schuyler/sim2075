---
title: purpose-trace
type: note
permalink: methodology/project/purpose-trace
tags:
- methodology
- project
- purpose
- validation
- v0.1
---

# Purpose Trace

**Date:** 2026-10-23
**Status:** Standing check: re-run whenever scope is cut, and before E10

Every other check in this project runs *downward*: event file to compiled catalog, spec to reference engine,
reference engine to vectorized engine. Nothing ran *upward*, from what the project is for to the mechanisms
that would have to carry it. So when MVP Dynamics Scope §5.1's pseudocode omitted the population step, the
omission passed through the implementation guide and eight engine stages unnoticed. Demographic transition is
half of the founding thesis, and the project began with a question about Chinese demographic shifts
(sim/README.md §4 item 22).

This document is the upward check. For each claim the model exists to explore, it traces the chain a claim
needs in order to show up in output:

> **state variables** that represent it → **between events**, what moves them (dynamics) → **at events**,
> what moves them (impact rows) → **feedback**, what reads them back into the model (event probability
> expressions, cascade conditions, dynamics or transmission rules) → **outputs** that would display it

Each link is marked *specified* (a document states it), *parameterized* (numbers exist), *scheduled* (a build
stage or task carries it) and *built*. A claim is only as strong as its weakest link.

**Rules.**
1. A scope cut that breaks a link of P0 or of the core claims P1–P5 needs the project owner's explicit sign-off,
   recorded here (see [[methodology/00-start-here]]).
2. Re-run the trace when scope is cut and before E10. The mechanical part is the query under "Method".
3. E10 gate: every row below is either *carried* or carries an owner-signed entry saying why not.

## The claims

From [[methodology/00-start-here]] §"Purpose and Decision Context":

- **P0. The founding question.** "What will Chinese demographic shifts do to its geopolitical strategy?"
- **P1.** The 21st century is shaped by the *interaction* of demographic transition and climate change.
- **P2.** Below-replacement fertility will reshape economic and political capacity everywhere.
- **P3.** Emissions are unlikely to fall fast enough to avoid severe climate impacts in vulnerable regions.
- **P4.** Wealthy nations will largely enforce borders rather than absorb climate migration at scale.
- **P5.** The result is a century of divergence: some regions adapt and stay stable, others face compounding
  crises.
- **P6.** Financial fragility compounds political instability; regional crises cascade or remain contained.

## Trace (2026-10-23, at E8)

Two traces were made independently and then reconciled: one by the implementing session, one by a separate
adversarial audit given the purpose, the documents and the code but not the first trace's conclusions. They
agreed on every finding the first trace had; the audit found more (findings 1, 5, 7 and 8 below are its).
Catalog facts are from the full compiled catalog: 29 events, 3,818 impact rows, 110 cascade edges.

Link key: **S** specified, **P** parameterized, **Sch** scheduled, **B** built; — absent.

| Claim | State variables | Between events | At events | Feedback into the model | Outputs | Status (weakest link) |
|---|---|---|---|---|---|---|
| **P0** Chinese demography → geopolitical strategy | 12 cohorts, `tfr`; derived `pop_working_age` (S) | cohort mechanics: S (one row of State Dynamics §3), P —, Sch (D5/E7c, 2026-10-23), B —; `gdp_growth` μ is one constant, so no demographic drag (MVP §7 "Linear trends") | no row targets `tfr` or a Chinese cohort | one term: `0.05 · clip((980 − chn.pop_working_age)/180, 0, 1)` in Chinese Economic Crisis pressure, at most 5 of 100 points; nothing computes the derived variable. Chinese Political Crisis reads no demographic name. Taiwan's gate reads `chn.military_spending_deviation`, which nothing moves | 5 countries' population as thin trajectories (State Outputs §4.1); no assessment reads a demographic variable | **broken**: feedback. Strategy itself is not represented (finding 5) |
| **P1** demography × climate interaction | both sides exist | climate globals drift (B); country exposure static | — | no expression or rule reads a demographic and a climate variable together | — | **unspecified**: no coupling anywhere |
| **P2** below-replacement fertility reshapes capacity | `tfr` (S; "slow-moving", Country catalog §2, vs "mean-reverting", State Dynamics §9) | Sch (D5), P —, B — | no row targets `tfr` | nothing reads `tfr`, cohorts or `dependency_ratio`; no rule links age structure to growth, tax or military capacity | `population_change` (E9) | **broken**: feedback empty |
| **P3** emissions → severe impacts in vulnerable regions | `global_temp_anomaly`, `sea_level_global`; country `water_stress`, `agricultural_climate_risk`, `heat_exposure`, `sea_level_exposure` | temperature +0.03/yr (S, P, B); country exposure "driven by global climate vars" in the Country catalog but deferred (MVP §4.1), no coefficients | exposure moved only by Amazon tipping on `bra` (6 rows); `heat_exposure`, `sea_level_exposure` by nothing | temperature read by the three tipping pressures (carried); Egypt, Pakistan, Iran and Sahel read exposure that never moves; `sea_level_global` and `wheat_price` are read by nothing | temperature and sea level as thin trajectories | **partial**: warming → tipping is carried; warming → vulnerable regions is broken |
| **P4** wealthy nations enforce borders | no border or absorption variable (a pre-dossier stub in `state-variables-round-2.md`) | — | 16 `refugees_hosted` and 18 `net_migration_rate` rows: event authors embed the assumption row by row | nothing reads `refugees_*` or `net_migration_rate`; the migration-crisis event is unauthored (`events/backlog-registry.md`); displacement originates only in state-failure events, plus one AMOC IDP row | `cumulative_displacement` (E9) | **unspecified**: authoring judgment only |
| **P5** century of divergence | `gdp_real`, `life_expectancy` per entity | compounding and LE drift (S, P, Sch, B); constant per-entity trends | 893 `gdp_real` rows | — | percentiles and classification (State Outputs §6–7; E9) | **partial**: divergence comes only from constant trends and event shocks; the slow drags the thesis names (aging, climate) are absent |
| **P6** financial fragility → political instability; cascades | debt, spreads, rates | `global_credit_spread`, `gdp_growth` mean-revert (B) | spreads, public and external debt shocked widely | the financial-crisis pressure reads spreads and rates; EU fragmentation reads Italian debt and spreads; Egypt and Pakistan read external debt; 110 cascade edges (B) | event log; scenario flags (none defined, README §4 item 23) | **carried**, the only claim that is. Caveat: sharpness 8–15 makes five Type 2 events step functions (README §4 item 11), so compounding is all-or-nothing |

**P0 in one paragraph.** A v0.1 run as planned can say almost nothing about the founding question. The only
path from a Chinese demographic quantity to anything geopolitical runs from the cohorts (E7c, unbuilt) to
`chn.pop_working_age` to one term in the Chinese economic crisis's pressure. That term is worth at most 5
points against a threshold of 75 ± 10 at sharpness 10. If that event fires, cascades add 0.02 a year for 5
years to the Chinese political crisis and 0.004 a year for 3 years to the Taiwan conflict. The Chinese political crisis reads no
demographic variable. Taiwan's gate reads `chn.military_spending_deviation`, a "Computed" variable (Country
catalog) that nothing computes, no event moves and no task supplies. At the engine's default of 0, Taiwan
can never fire; at any 2025 value above 0.15 its gate is open for 50 years. The effect of Chinese
demographic shifts on geopolitical outcomes in v0.1, as planned, is indistinguishable from zero.

## Cross-cutting findings

Ranked by damage to the purpose. Each is a finding, not a decision: what closes it, and whether it fits
v0.1, is for the requirements review that follows this trace.

1. **No 2025 values for the state that event probabilities read.** Expressions read 80 country-level names,
   73 of them outside D3's scope (GDP and life expectancy). Nothing schedules starting values for
   `debt_public`, `protest_intensity_annual`, `sanctions_level`, `water_stress`, `food_import_dependence`,
   `nuclear_status`, `un_voting_alignment_us` and the rest. The compiler skips its baseline check for country
   variables, and E8's smoke ran them all at 0 (README §4 item 25), which was reported as a cost
   measurement, not as a missing data task. Every Type 2 and Type 3 event is affected; E10 means nothing
   without this. *Closes with* a data task sourcing them per the Country catalog.
2. **Demography → capacity is empty.** No rule links workforce, age structure or `tfr` to growth, fiscal or
   military capacity, or to event probabilities beyond the one 5-point term. *Closes with* a specified
   channel: for example a per-entity μ(t) schedule for `gdp_growth` from UN WPP working-age trajectories,
   which `DynamicsSpec` cannot yet express (μ is one number), plus pressure terms reading `pop_working_age` or
   `dependency_ratio` in the Chinese political crisis and Taiwan conflict.
3. **33 variables that expressions read are never moved by anything**, so they act as constants set by their
   2025 values. The query is under "Method". Among them:
   - `chn.military_spending_deviation`, which decides alone whether the Taiwan conflict can ever fire;
   - `rus.military_spending_deviation`;
   - every `years_since_irregular_transition` and `leadership_tenure_years`;
   - `water_stress` in Egypt, Pakistan and Iran, and `food_import_dependence` in Egypt and Pakistan;
   - the Sahel's climate and governance inputs;
   - `fed_funds_rate`, `us_real_rate`, `cips_share`;
   - `irn.nuclear_status`.

   *Closes with* one of three things per variable: computation (the "Computed" ones), dynamics, or rewriting
   the expression to read something that moves.
4. **Climate never reaches vulnerable regions.** Country exposure has no dynamics and no coefficients (MVP
   §4.1 defers damage functions; its inclusion trigger, "climate events have implausibly uniform impacts",
   can only fire after a run the deferral makes uninformative). *Closes with* exposure drifts tied to warming,
   e.g. E7's existing `additive` kind with a country coefficient (State Transmission §3.2's stylized form).
5. **Strategy is not represented.** The observable-over-synthetic refactor moved capacity and alignment
   indices to outputs; `alliance_status` is categorical and nothing shocks it. "Geopolitical strategy" survives
   only as cascade deltas and a handful of sanctions, trade and military-spending rows. Even fully wired, P0
   needs a decision on what in the state stands for a state's strategy.
6. **Political clocks are specified but unbuilt.** State Dynamics §7: `years_since_irregular_transition`
   +1 a year, reset to 0 by a transition event. Seven pressures read one. `DynamicsSpec` has no counter kind,
   and the schema has no "set" row, so the reset is inexpressible.
7. **Population mechanics are less specified than MVP §2.4 says.** "Specified in State Dynamics §3" is one
   table row. The cohort-width rule, life table, fertility band and migration split are all unwritten (Task 4.6
   now carries them), and `tfr` is classed both "slow-moving" and "mean-reverting".
8. **Sharpness makes the founding question's actors step functions.** Both Chinese events sit among the Type 2
   events with sharpness 8–15 (README §4 item 11), so pressure does not accumulate for them. The Taiwan
   conflict, the other actor, is Type 3; its inputs are the most static of all.
9. **The migration and border thesis (P4) is authoring judgment only.** There is no absorption mechanism and no
   climate-driven origin of migration, and the migration-crisis event is unauthored.
10. **Outputs.** No State Outputs §5 assessment reads a demographic variable; no scenario flag exists.

**How the purpose was lost in translation** (both traces agree):
- MVP scope framed Tier 1 as a "progress engine" to offset a catalog of negative events. The slow-burn
  *negative* forces of the thesis, aging and climate drag, got no tier at all.
- One sentence (§2.4, "not parameterized trend rates") removed demography from the parameter count, the
  §5.1 pseudocode and so the implementation guide.
- Every verification ran downward (event to catalog, spec to reference, reference to engine). Each stage
  passed its gate. None asked whether the gates measured the purpose.

## Method

The mechanical part of the trace is a query over the compiled full catalog, run from the repository root.
It finds which names event expressions read, which variables impact rows move, and which read variables
nothing moves:

```python
import pathlib
from sim.catalog.cli import load_state_catalog, load_omega, extract_all, compile_event_records
sc = load_state_catalog(); _, om = load_omega(factors=sc.factors)
recs, known, _ = extract_all(pathlib.Path("events"))
cat = compile_event_records(recs, om, sc, known_event_ids=known, strict_cascades=True)
# names read: cat.type2[e].pressure.names; cat.type3[e].preconditions / .sustained; cascade_edges[i].cond.names
# variables moved at events: cat.impact_table (entity_idx, var_idx); between events: the DynamicsSpec (D4)

# frozen inputs: names expressions read that no impact row moves and no dynamics entry will move
inv = {v: k for k, v in cat.index.country_var.items()}
ginv = {v: k for k, v in cat.index.global_var.items()}
ent = {v: k for k, v in cat.index.entity.items()}
moved = {ginv[r["var_idx"]] if r["entity_idx"] < 0 else f'{ent[r["entity_idx"]]}.{inv[r["var_idx"]]}'
         for r in cat.impact_table}
dynamic = set()   # fill from the DynamicsSpec in force (until D4: MVP §2.2–§3's variables)
frozen = sorted(n for n in cat.expression_names()
                if not n.startswith("F_") and n not in ("resolution", "branch", "years_since")
                and n not in moved and n.split(".", 1)[-1] not in dynamic)
```

On 2026-10-23, with `dynamic` set to MVP §2.2–§3's variables (`gdp_growth`, `inflation_rate`,
`unemployment_rate`, `fdi_net`, `life_expectancy`, `gdp_real`; the §2.2 global trends; commodity prices;
`global_credit_spread`), this gave 33 names.

The rest is reading. For each claim, find the documents that specify each link and the stage that builds it.

## History

| Date | Change |
|------|--------|
| 2026-10-23 | First trace, at E8, after population dynamics were found to be specified for v0.1 but scheduled nowhere |
