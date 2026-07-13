---
title: State Variables - Round 2 (Stubs)
type: note
permalink: methodology/reference/state-variables-round-2
tags:
- methodology
- reference
- state
- variables
- stubs
- round-2
- dossier
---

# State Variables — Round 2 (Stub Catalog)

**Status: Stubs for ensemble authoring. None admitted to the catalog yet.**

Candidate state variables for **catalog v1.1**, assembled alongside [[events/planned-events-round-2]]. A variable enters the real catalog ([[methodology/reference/state-variables-country]] / [[methodology/reference/state-variables-global]]) only when it carries a **complete dossier** per [[methodology/reference/catalog-versioning]] §3. This document holds each candidate at the stub stage — the modeling *reason* is decided, the dossier is not yet filled — so an Opus agent can complete the four dossier requirements against a known target rather than inventing the variable cold.

**The dossier each stub must complete before admission** ([[methodology/reference/catalog-versioning]] §3):

1. **Measurement procedure + data source** — observable, no synthetic indices ([[methodology/concepts/synthetic-variable-problem]]).
2. **Dynamics classification + parameters** — a class from [[methodology/reference/state-dynamics]] (drift / mean-reverting / event-driven / regime-dependent) with its parameters.
3. **Sourced 2025 initial conditions** for every entity that tracks it.
4. **≥1 consumer** — an event impact row, a `pressure:`/`preconditions:`/`if:` expression, or a transmission channel. **Every stub below names its consumer(s) in [[events/planned-events-round-2]]** — that requirement is pre-satisfied by construction; the author still confirms the consumer's spec actually reads/writes the variable.

**The hard cases are §1–§3.** These are the "war-mandated variable classes" from [[strategy/roadmap]] Phase 0 item 3 and [[strategy/sim2075-third-gulf-war-interaction]] §3 — behavioral histories, ratchets, and duration clocks. The roadmap's **scope pin** applies: anything expressible as an ordinary engine-maintained state variable under the current schema (the `years_since_irregular_transition` pattern, [[methodology/reference/expression-language]] §6) **may be added now**; anything needing a new schema construct is a **schema-v0.2 backlog** item, recorded here but not admitted. The scope-pin discipline: a variable enters the *engine* only through an explicit revision of [[methodology/reference/mvp-dynamics-scope]], never as a side effect of authoring.

**Anti-pattern warning.** Several stubs (§2 absorption capacity, §4 automation exposure) are one careless step from the synthetic-variable trap the whole state model was designed to avoid. The dossier's requirement #1 is the guardrail: if you cannot state the measurement procedure and data source in one line, the variable is synthetic and does not get admitted — decompose it or drop it.

---

## 1. Actor Behavioral Histories (war-mandated)

**Class rationale.** [[strategy/sim2075-third-gulf-war-interaction]] §3.2: a *repeated* small-N actor generates its own behavioral base rate that is tractable even when the underlying psychology is not — but only after enough within-episode repetitions accumulate (the wiki needed ~8 brinksmanship cycles). This is a within-episode count, cleanly expressible under the current schema as an integer state variable in the `years_since_irregular_transition` family. **Admit now.**

### 1.1 `brinksmanship_cycles_current_episode` — country-level

- **Measures:** count of distinct escalation-then-de-escalation cycles between a given actor pair within the current unresolved episode (resets when the episode resolves).
- **Data source (stub):** ACLED escalation event coding + episode segmentation rules — author must define the cycle-boundary criterion precisely (this is the load-bearing definitional choice).
- **Dynamics:** event-driven increment; reset on episode-resolution event. Class: event-driven, no decay within episode.
- **2025 initial conditions:** per active dyad (US–Iran, India–Pakistan, Israel–Hezbollah, DPRK–US, etc.); most start at the observed within-current-episode count.
- **Consumers:** `ISRAEL_IRAN_WAR`, `IRAN_REGIME_CHANGE`, `INDIA_PAKISTAN_MILITARY_CONFLICT`, `KOREAN_PENINSULA_CRISIS` — resolution-shape base rate per §3.2.
- **Open question:** is this per-dyad (needs a dyad index — possible schema pressure) or per-country-toward-primary-rival (fits current schema)? Author decides; if per-dyad needs new schema, split: admit the country-level scalar now, backlog the dyad matrix.

### 1.2 `time_since_last_conflict_same_actor` — country-level

- **Measures:** years since this actor last engaged the same adversary in armed conflict. Feeds the `OIL_SUPPLY_SHOCK` reclassification case ([[strategy/roadmap]] Phase 0 item 2 — arsenal reconstitution / repeated-actor pathway).
- **Data source:** UCDP/PRIO dyadic dataset.
- **Dynamics:** deterministic annual increment; reset on conflict-onset event. (Exact `years_since_irregular_transition` analogue.) **Admit now.**
- **Consumers:** `OIL_SUPPLY_SHOCK` (geopolitical-pathway rate), `ISRAEL_IRAN_WAR`.

---

## 2. Absorption / Tolerance Thresholds

**Class rationale.** The migration and humanitarian events (round-2 §C) need a *capacity* against which displacement stocks are compared. The displacement stocks already exist ([[methodology/reference/state-variables-country]] §2.2); the threshold does not. **Highest synthetic-trap risk in this document** — must be grounded in an observable, not "political will."

### 2.1 `migrant_absorption_capacity` — country-level (candidate: decompose)

- **Measures:** the level of refugee/migrant inflow a host can absorb before a political-response discontinuity. **Do not admit as a single synthetic score.** Decompose per the synthetic-variable discipline into observables the author can source:
  - refugees_hosted as % of population (derivable from existing variables — may need *no* new variable),
  - a policy-response observable (border-closure events, asylum-law changes — ACLED / news-coded), and/or
  - fiscal transfer capacity (already partially in economic variables).
- **Likely resolution:** the "threshold" is a `pressure_function` on **existing** variables inside `EUROPEAN_MIGRATION_CRISIS`, not a new state variable. Author's first task: prove a new variable is needed at all (dossier requirement #4 inverted — is there a consumer that *cannot* be written against existing variables?).
- **If admitted:** class regime-dependent (threshold shifts with `regime_type` / governing-coalition stance).

---

## 3. Ratchet / Lock-in Variables (war-mandated)

**Class rationale.** [[strategy/sim2075-third-gulf-war-interaction]] §3 (insurance floors, alliance-credibility damage) and [[strategy/emergent-ideas]] idea 6: some damage is asymmetric — easy to incur, slow or impossible to reverse ("damage a ceasefire cannot fix," interaction doc §2d). The *variable* (a level that moves one way easily) is expressible now; the **decay-to-floor durability** (`persistent/floor`) for impact rows that write to it is a schema-v0.2 construct. **Admit the variables now; approximate their durability as `permanent` until v0.2.**

### 3.1 `insurance_availability` — country-level (or region)

- **Measures:** share of climate/catastrophe-exposed property with available primary insurance (inverse of the uninsurable gap).
- **Data source (stub):** national insurance regulators, Swiss Re / Munich Re protection-gap reports, admitted-market withdrawal filings (e.g., state insurer-of-last-resort enrollment).
- **Dynamics:** ratchet — declines on catastrophe-loss events, recovers slowly or not at all (floor). Class: event-driven with asymmetric recovery; the asymmetry is the point.
- **2025 initial conditions:** by country, elevated protection gaps already observable (FL, CA, parts of Mediterranean/Australia).
- **Consumers:** `CLIMATE_INSURANCE_CRISIS` (round-2 D3) reads and shocks it; climate-tipping events write to it.
- **Schema note:** the floor behavior wants `persistent/floor` durability — **schema-v0.2 backlog**. For v1.1, model the shock as `permanent` and document the approximation.

### 3.2 `alliance_credibility_damage` — country-level or dyad

- **Measures:** accumulated, slow-to-repair damage to an alliance guarantee's credibility (a defection, an unmet commitment, a public abandonment). Feeds `NPT_REGIME_COLLAPSE` (why threshold states hedge toward weapons) and NATO/US-alliance events.
- **Data source (stub):** hard to observe directly — **synthetic-trap risk**. Candidate observables: unmet treaty-commitment events, allied defense-spending divergence, public alliance-exit rhetoric coded from statements. Author must find the observable or backlog it.
- **Dynamics:** ratchet (accumulates on defection events, decays very slowly).
- **Consumers:** `NPT_REGIME_COLLAPSE`, `NATO_RUSSIA_DIRECT_CONFLICT`, `SAUDI_NUCLEAR_ACQUISITION`.
- **Disposition:** if no clean observable emerges, this is **schema-v0.2 / decline** — do not admit a synthetic proxy.

---

## 4. Infrastructure & Systemic Reliability

**Class rationale.** Several round-2 events (cyber, South Africa, AI labor) shock or read infrastructure function that the current state vector doesn't represent. Mostly observable and schema-compatible.

### 4.1 `grid_reliability` — country-level

- **Measures:** electricity-supply reliability (e.g., SAIDI — average interruption duration, or % of demand met).
- **Data source:** national grid operators, World Bank Enterprise Surveys (outage frequency), ENTSO-E.
- **Dynamics:** slow drift + event shocks (cyber, state collapse). Class: mean-reverting around country equilibrium with event shocks. **Admit now.**
- **Consumers:** `MAJOR_CYBER_INFRASTRUCTURE_ATTACK`, `SOUTH_AFRICA_INSTITUTIONAL_COLLAPSE`.

### 4.2 `chokepoint_transit_status` — global (per chokepoint)

- **Measures:** operational status / throughput of a maritime chokepoint (Hormuz, Suez, Bosphorus, Malacca, Panama) vs. baseline.
- **Data source:** AIS traffic data (e.g., IMF PortWatch), transit-authority reports.
- **Dynamics:** normally 100; event-driven collapse and recovery. Class: event-driven.
- **Consumers:** `STRAIT_OF_HORMUZ_CRISIS`, `BOSPHORUS_TRANSIT_DISRUPTION` (folded), `EGYPT_STATE_FAILURE` (Suez). Transmits to `oil_brent`, `container_freight_index`, `global_trade_volume`.
- **Schema note:** a per-chokepoint global variable may want a small indexed set — confirm the global-variable schema handles a keyed family, else enumerate the 4–5 named chokepoints as separate scalars.

### 4.3 `automation_exposure` — country-level (candidate: decline/backlog)

- **Measures:** share of employment in tasks exposed to near-term AI automation.
- **Data source (stub):** occupational task databases (O*NET) × employment structure — exists in the literature but is *projection-heavy*.
- **Disposition:** **high synthetic-trap risk and depends on `AI_LABOR_MARKET_DISRUPTION` (round-2 E1) surviving its own fold-or-specify decision.** Hold as **backlog** until E1 is specified rather than declined. If E1 declines to baseline, this declines with it.

---

## 5. Global Norm / Regime Counters

**Class rationale.** `NPT_REGIME_COLLAPSE` (round-2 A6) needs to read the *systemic* proliferation state, not just one country's `nuclear_status`. This is an aggregate over an existing variable — likely a derived output, not a new stored variable.

### 5.1 `nuclear_weapons_states_count` — global (likely derived)

- **Measures:** count of entities with `nuclear_status = POSSESSED`; and count at `THRESHOLD`.
- **Data source:** derived from existing country `nuclear_status` — **compute, don't store** (per the derived-indicator pattern). No dossier needed if derived; listed here so the author of A6 knows to add the derivation to [[methodology/reference/state-outputs]] rather than the state catalog.
- **Consumers:** `NPT_REGIME_COLLAPSE` pressure function.
- **Disposition:** derived output, not a state variable. Included for completeness of the A6 consumer chain.

---

## Summary & dispositions

| # | Candidate | Class | Schema fit | Disposition |
|---|---|---|---|---|
| 1.1 | `brinksmanship_cycles_current_episode` | event-driven counter | current (scalar) / v0.2 (dyad matrix) | admit scalar now |
| 1.2 | `time_since_last_conflict_same_actor` | deterministic clock | current | **admit now** |
| 2.1 | `migrant_absorption_capacity` | regime-dependent | prove-a-variable-is-needed first | likely no new variable |
| 3.1 | `insurance_availability` | ratchet | current variable; v0.2 durability | admit now, `permanent` approx |
| 3.2 | `alliance_credibility_damage` | ratchet | needs observable | admit or v0.2/decline |
| 4.1 | `grid_reliability` | drift + shock | current | **admit now** |
| 4.2 | `chokepoint_transit_status` | event-driven | current (confirm keyed family) | admit now |
| 4.3 | `automation_exposure` | projection | current but synthetic-risk | backlog with E1 |
| 5.1 | `nuclear_weapons_states_count` | derived | n/a | derived output, not stored |

**Clean admits now (schema-compatible, observable, consumed):** 1.1 (scalar), 1.2, 3.1, 4.1, 4.2. These five are the war-mandated + round-2-event-mandated core.

**Prove-then-admit / decompose:** 2.1, 3.2.

**Schema-v0.2 backlog:** dyad-indexed behavioral matrices (1.1 extended), `persistent/floor` durability (3.1's true form), per-component transmission thresholds — all already in the Phase 0 item 5 v0.2 backlog.

**Not stored:** 5.1 (derive), 4.3 (backlog with its event).

## Ensemble authoring notes

- Complete the dossier **in the same release** as the consuming event — the consumer requirement is only checkable at release granularity ([[methodology/reference/catalog-versioning]] §4).
- When admitting, update the real catalogs ([[methodology/reference/state-variables-country]] or `-global`), the total state-space counts, and — critically — the [[methodology/reference/mvp-dynamics-scope]] axes via explicit revision (the scope pin). Do not let a variable slip into the engine as an authoring side effect.
- Every admit adds `40 × 1` (country) or `52 × 1` (all entities) to the state space — the batching pressure is real; admit only variables with live consumers.

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-07-13 | Initial variable stub catalog (9 candidates, 5 clean admits) | War-mandated variable classes (Phase 0 item 3) + round-2 event consumers |
