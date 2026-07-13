---
title: backlog-registry
type: note
permalink: events/backlog-registry
tags:
- events
- backlog
- registry
- line-373-rule
- process
---

# Event Backlog Registry

**Status: Adopted — the machine-checkable side of the line-373 rule**

This file is the explicit backlog registry called for by [[strategy/emergent-ideas]] idea 2 and [[methodology/reference/catalog-versioning]] §5. The rule it mechanizes: **any event ID named in a cascade list, resolution note, or impact comment that is absent from the catalog must appear here with a disposition.** Once Phase 1 item 5 CI exists, a referenced ID that is neither in the catalog nor in this registry fails the build.

Every ID below was extracted from the 29 specified event files (July 2026 sweep). Dispositions:

- **promote** — becomes a first-class event; a stub exists in [[events/planned-events-round-2]]
- **fold** — absorbed into an existing or promoted event (as a resolution branch, impact row, or cascade magnitude); the referencing file should eventually be edited to point at the canonical ID
- **alias** — the ID is a naming drift for an event that already exists; referencing files should be normalized
- **decline** — too vague, too local, or baseline-trajectory material; recorded so the reference is consciously dangling rather than forgotten

---

## 1. Promotions (stub exists in round-2 catalog)

| Referenced ID | Referenced in | Canonical ID |
|---|---|---|
| `ISRAEL_IRAN_WAR` / `US_IRAN_WAR` | iran-nuclear-acquisition, iran-regime-change (line 373) | `ISRAEL_IRAN_WAR` |
| `STRAIT_OF_HORMUZ_CRISIS` | iran-nuclear-acquisition, iran-regime-change | `STRAIT_OF_HORMUZ_CRISIS` |
| `GULF_STATE_ATTACKS` | iran-regime-change | `GULF_STATE_ATTACKS` |
| `NPT_REGIME_EROSION` / `NPT_REGIME_COLLAPSE` | iran-nuclear-acquisition | `NPT_REGIME_COLLAPSE` |
| `GLOBAL_NUCLEAR_RECONFIGURATION` | india-pakistan-military-conflict, korean-peninsula-crisis | `NPT_REGIME_COLLAPSE` |
| `NUCLEAR_SECURITY_CRISIS` | iran-regime-change, russia-state-failure | `NUCLEAR_SECURITY_CRISIS` |
| `US_CHINA_DIRECT_CONFLICT` | korean-peninsula-crisis | `US_CHINA_DIRECT_CONFLICT` |
| `NATO_ARTICLE_5_CRISIS` / `NATO_CRISIS` | turkey-political-breakdown | `NATO_RUSSIA_DIRECT_CONFLICT` |
| `UKRAINE_CONFLICT_RESOLUTION` | russia-state-failure | `UKRAINE_CONFLICT_RESOLUTION` |
| `NIGERIA_NORTHERN_CRISIS` / `NIGERIA_NORTHERN_DESTABILIZATION` | sahel-catastrophe | `NIGERIA_STATE_FAILURE` |
| `WEST_AFRICA_REGIONAL_COLLAPSE` / `COASTAL_WEST_AFRICA_DESTABILIZATION` | sahel-catastrophe | `COASTAL_WEST_AFRICA_DESTABILIZATION` |
| `MASS_MIGRATION_CRISIS` / `EUROPEAN_REFUGEE_CRISIS` / `EUROPEAN_MIGRATION_CRISIS` / `EU_MIGRATION_CRISIS` / `REFUGEE_CRISIS_MENA` / `REFUGEE_CRISIS_MAJOR` / `GLOBAL_REFUGEE_CRISIS` | saudi-regime-instability, russia-state-failure, turkey-political-breakdown, sahel-catastrophe, iran-regime-change | `EUROPEAN_MIGRATION_CRISIS` |
| `GLOBAL_HUMANITARIAN_CAPACITY_CRISIS` | sahel-catastrophe | fold into `EUROPEAN_MIGRATION_CRISIS` resolution set for now; revisit if a second consumer appears |
| `GLOBAL_REINSURANCE_CRISIS` | turkey-political-breakdown | `CLIMATE_INSURANCE_CRISIS` |
| `KURDISH_AUTONOMY_EXPANSION` / `KURDISH_STATE_FORMATION` | iran-regime-change, turkey-political-breakdown | `KURDISH_STATE_FORMATION` (low-priority queue) |

## 2. Folds (absorbed into existing or promoted events)

| Referenced ID | Referenced in | Folds into | How |
|---|---|---|---|
| `DPRK_REGIME_COLLAPSE` | korean-peninsula-crisis | `KOREAN_PENINSULA_CRISIS` | Already a resolution branch of the existing event; normalize the self-reference |
| `TURKEY_NUCLEAR_RECONSIDERATION` | iran-nuclear-acquisition, saudi-nuclear-acquisition | `NPT_REGIME_COLLAPSE` | Proliferation-cascade branch (which states go next) |
| `EGYPT_NUCLEAR_PROGRAM` | saudi-nuclear-acquisition | `NPT_REGIME_COLLAPSE` | Same cascade branch |
| `GULF_STATE_CONTAGION` / `GULF_STATE_CASCADE` / `GULF_COOPERATION_STRESS` / `GUEST_WORKER_CRISIS` | saudi-regime-instability | `SAUDI_REGIME_INSTABILITY` + `GULF_STATE_ATTACKS` | Contagion belongs in the existing event's aftermath branches; attack pathways in the promoted war event |
| `PROXY_NETWORK_WEAKENING` / `PROXY_NETWORK_COLLAPSE` | iran-regime-change | `IRAN_REGIME_CHANGE`, `ISRAEL_IRAN_WAR` | Resolution-branch content, not standalone events |
| `CHINA_FAR_EAST_ASSERTION` | russia-state-failure | `RUSSIA_STATE_FAILURE` | Aftermath branch (who fills the vacuum) |
| `BOSPHORUS_TRANSIT_DISRUPTION` | turkey-political-breakdown | `TURKEY_POLITICAL_BREAKDOWN` | Impact row (trade/shipping variables), not an event |

## 3. Aliases (naming drift for specified events)

| Referenced ID | Referenced in | Canonical existing ID |
|---|---|---|
| `TURKEY_POLITICAL_CRISIS` | dollar-reserve-crisis, eu-fragmentation | `TURKEY_POLITICAL_BREAKDOWN` |
| `US_CHINA_TRADE_WAR` | chinese-economic-crisis | `US_CHINA_ECONOMIC_RUPTURE` |

## 4. Declines (consciously not events)

| Referenced ID | Referenced in | Why declined |
|---|---|---|
| `SANCTIONS_INTENSIFICATION` | iran-regime-change | Policy action, not a discontinuity; expressible as a `sanctions_level` impact row |
| `GREAT_POWER_INTERVENTION` | russia-state-failure | Too generic; specific interventions live in the relevant events' branches |
| `CENTRAL_ASIA_INSTABILITY` | russia-state-failure | Tier 2 aggregate region; revisit only if sensitivity analysis shows the region drives tails (low-priority queue) |
| `CAUCASUS_CONFLICT` | russia-state-failure | Same treatment as Central Asia (low-priority queue) |
| `MAGHREB_INSTABILITY` | sahel-catastrophe | Same treatment (low-priority queue) |
| `GHANA_POLITICAL_CRISIS` / `COTE_DIVOIRE_INSTABILITY` | sahel-catastrophe | Country-level texture inside `COASTAL_WEST_AFRICA_DESTABILIZATION`; not separate events |

---

## Maintenance

- New cascade references to uncataloged IDs are added here **in the same commit** that introduces them.
- When a promotion is specified at Level 1, move its row from this registry into the catalog proper and normalize the referencing files' IDs.
- The Phase 2 audit harness's unattributable-complaint stream ([[strategy/emergent-ideas]] idea 4) feeds new rows into this table.

*Created: July 13, 2026 — full-catalog reference sweep*
