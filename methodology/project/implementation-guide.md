---
title: implementation-guide
type: note
permalink: methodology/project/implementation-guide
tags:
- methodology
- project
- implementation
- orchestration
- v0.1
- guide
---

# v0.1 Implementation Guide

**Document Version:** 1.0
**Date:** July 2026
**Status:** Execution plan — written to be wielded by an orchestrating agent driving subagents

This document is a **plan, not a design**. The design lives in
[[methodology/reference/simulator-architecture]] (ADRs) and
[[methodology/reference/expression-language]] (expression contract); those are
the normative sources and this guide deliberately does not restate them. What
this guide adds is what an orchestrator needs and the ADRs don't provide:
**pinned decisions, build order, verification gates, frozen interface
contracts, and guardrails.**

**Relationship to the project plan.** This guide is the execution of
[[strategy/roadmap]] **Phase 1** (the engine track). Roadmap Phase 0 — war
absorption — proceeds in parallel as prose, methodology corrections, and new
event specs: war events that fit the current schema (the three Type 3 war-hub
events) join the Task 4.2 migration table and this guide's data track like any
other event. War lessons that would require new schema constructs (hybrid
causal types, multi-front resolution clocks, per-component hysteresis) are
**schema v0.2 backlog** items per roadmap Phase 0 item 5 and MUST NOT be built
into v0.1 — guardrail 3 applies. Phase 0 state-variable additions (roadmap
Phase 0 item 3 / Task 6.7) are likewise spec-side only: **for the duration of
the build**, the v0.1 engine's entity/variable axes stay pinned to
[[methodology/reference/mvp-dynamics-scope]], and widening them mid-build is a
frozen-seam change (stop and report), not something event authoring can
trigger. The sanctioned widening moments — a one-time pre-E0 revision of the
MVP scope, and post-E10 versioned catalog releases — are defined in
[[methodology/reference/catalog-versioning]], along with the variable
admission rule (dossier) and release gates. Guardrail 7 is what makes the
post-E10 moment a data change rather than an engine change.

**Rules of engagement for any agent using this guide:**
1. Where this guide and the ADRs conflict, **stop and report** — do not resolve
   the conflict yourself.
2. Every stage ends at its gate. A stage is not done until its gate passes
   mechanically (a test run, not a judgment).
3. Nothing outside your assigned stage's file scope may be modified.

---

## 0. Pinned decisions (discharges Task 5.0)

The open decisions from [[methodology/reference/simulator-architecture]] §5 are
resolved as follows. These are **constraints, not options**.

| # | Decision | Resolution |
|---|----------|------------|
| 1 | Type 2 `threshold_std` | **Per-run threshold offset**, drawn once at run initialization: `threshold_r = threshold + threshold_std · z_r`, `z_r ~ N(0,1)`. Not marginalized analytically. |
| 2 | Cascade / ledger storage | **One shared pattern**: fixed-width active-effect tensors on the run axis with per-slot age/expiry fields. Cascades and impact shocks use the same slot-recycling mechanics. |
| 3 | Ledger width | **`max_active = 256`** per run. Overflow is a **counted hard failure**: increment an overflow counter, raise at end of year with run indices; never silently drop a shock. Revisit width after fixture pilots. |
| 4 | Reference implementation location | **`sim/reference/`** inside the same package, importable in tests. Shares the compile layer (`catalog/`); shares **no** engine code. |
| 5 | Compound multipliers (framework §8.6) | **Retired.** Compounding is expressed through cascades + additive impacts only. No pairwise-between-events structure may be built (ADR-6). |

Further standing constraints, stated here because agents commonly violate
them silently:

- **dtype is float64 everywhere** in v0.1. No float32 "optimizations."
- **Draw shapes must be outcome-independent** (see §5.2). Never draw random
  numbers only for runs that "need" them.
- **One causal type per event in YAML.** Events whose prose describes a hybrid
  mechanism (e.g. GLOBAL_FINANCIAL_CRISIS "Type 1/2") declare their dominant
  mechanism as `causal_type`; the secondary pathway stays in prose until
  schema v0.2. Migrating agents pick the type the event's own probability
  model actually implements and note the choice in the changelog.
- **Variance validation is against the declared `variance:` field.** The
  compiler checks achieved `(ΛΩΛᵀ)ᵢᵢ` against each event's declared target,
  never against a type-derived table — hybrid-type events legitimately declare
  off-table targets (Task 4.2 validation rule 0). The type-keyed targets in
  [[methodology/reference/variance-allocation]] are authoring guidance, not a
  compile gate.

---

## 1. Two tracks and their convergence

```
DATA TRACK                          ENGINE TRACK
4.2  event YAML migration  ┐        E0 scaffolding + fixtures
     (24 + 3 remediations) │        E1 scalar reference impl (the oracle)
4.3  initial conditions    │        E2 catalog compiler
4.4  dynamics defaults     │        E3 factor sampling
                           │        E4 firing (Types 1/2/3)
                           │        E5 per-run memory
                           │        E6 impact ledger
                           │        E7 dynamics
                           │        E8 year loop + recording
                           ▼        E9 analysis
                    ── E10 / 5.11 end-to-end validation ──
```

The engine track is **fixture-driven** and does not wait for the data track:
every stage through E9 builds and gates against hand-authored fixtures plus the
already-migrated events. Only 5.11 (full-catalog validation runs) requires the
data track complete.

**Parallelism guidance for an orchestrator:**
- The data track's Task 4.2 is the ideal fan-out: 24 migrations + 3
  remediations (counts per the [[methodology/project/tasks]] §4.2 subtask
  table, which is the single source of truth for migration status), each
  independent, each with a strict documented process
  ([[methodology/project/tasks]] §Task 4.2 Detailed Instructions) and
  mechanical validation. One agent per event; verify with a separate checker
  pass per event (schema validation + prose-preservation diff against git
  history).
- The engine track is **sequential through E2**, then E3–E7 can proceed with
  limited parallelism against the frozen contracts in §4 (each stage builds
  against the others' interfaces, converging in E8).
- Task 4.3 (initial conditions) and 4.4 (dynamics defaults) are single-agent
  research/data tasks, parallel to everything.

---

## 2. Data track

| Step | Work | Gate |
|------|------|------|
| D1 | Remediate 3 flagged events (Pakistan, severe pandemic, fusion) restoring lost prose per git history — AMOC already remediated | Checker agent confirms: YAML validates; all prose sections from history present |
| D2 | Migrate remaining 24 events per Task 4.2 process | Same per-event gate; progress table in [[methodology/project/tasks]] updated |
| D3 | Task 4.3: 2025 baselines + trend rates (~196 params) per [[methodology/reference/mvp-dynamics-scope]] §2, single-sourced (IMF WEO, UN WPP) into `sim/data/initial_conditions.yaml` | All 46 Tier-1 entities (40 countries + 6 Tier 1 aggregates per [[methodology/reference/state-entities]]) covered; every value carries a source tag |
| D4 | Task 4.4: mean-reversion defaults per [[methodology/reference/mvp-dynamics-scope]] §3 into `sim/data/dynamics_defaults.yaml` | All Tier 2 variable classes covered; outlier overrides (Argentina, Turkey) present |

The final gate for the whole track: **the catalog compiler (E2) compiles every
event in `events/` with zero errors** (29 at time of writing; roadmap Phase 0
adds the three war-hub events, which gate identically).

---

## 3. Engine track build order

Directory layout per [[methodology/reference/simulator-architecture]] §2.
Stages map to tasks 5.1–5.11; each row lists the deliverable and its
**mechanical gate**.

| Stage | Task | Deliverable | Gate |
|-------|------|-------------|------|
| **E0** | 5.1 | `sim/` scaffolding; pytest wiring; **fixtures** (§5.1) committed as hand-built `CompiledCatalog` instances + expected outputs | `pytest` collects and runs; fixture expectations documented in the fixture files themselves |
| **E1** | 5.8b (moved first) | Scalar reference implementation in `sim/reference/`: plain per-run, per-year stepper consuming a `CompiledCatalog`, implementing the full year step (architecture §3) with readable imperative code | Reproduces FIX-A expected outputs exactly (hand-computed); FIX-B runs without error and its event log matches hand-traced expectations |
| **E2** | 5.4 (compiler half) | `catalog/`: extract → schema-validate → expression-compile → `CompiledCatalog` | Compiles all currently-migrated events; **rejects** each of the deliberately-broken fixture variants (unknown variable, bad enum, branch p-sum ≠ 1, banned AST node, undeclared resolution name) with the event ID in the error |
| **E3** | 5.3 | `engine/factors.py`: Ω validation, Cholesky, correlated draws, `σ_idio` from `1 − (ΛΩΛᵀ)ᵢᵢ` | At R=100k: empirical factor correlation within ±0.02 of Ω entrywise; per-event Z variance within ±0.02 of 1.0 |
| **E4** | 5.4 (engine half) | `engine/firing.py`: unified copula + per-type thresholds + gates (ADR-3), per-run threshold offsets (pinned #1) | At R=100k, 1 year: Type 1 firing frequency within 3σ (binomial) of spec for every fixture event; Type 2 probability monotone in pressure across a pressure sweep; Type 3 never fires while gate is false |
| **E5** | 5.4b | `engine/memory.py`: sustained counters + cascade delta buffers (pinned #2) | Sustained: hand-built factor path in FIX-B opens the gate in exactly the specified year, resets on interruption. Cascades: delta present for exactly `years` years post-firing; conditional cascade respects its `if` |
| **E6** | 5.5, 5.6 | `engine/impacts.py`: active-shock ledger (pinned #2, #3); permanent shocks fold into state at firing; epsilon-cull at contribution < 1e-4 of drawn magnitude; `until: resolved` linkage; resolution/branch draws | Single-shock decay curve matches closed-form half-life to rtol 1e-9; `permanent` occupies no slot; overflow raises with run indices; **oracle diff vs E1 on FIX-B passes** (§5.2) |
| **E7** | 5.7 | `engine/dynamics.py`: Tier 1 drift, Tier 2 mean reversion, oil/food→inflation transmission per [[methodology/reference/mvp-dynamics-scope]] §5.1 (growth-rate-first ordering) | No-event run from FIX-A initial conditions shows compounding GDP growth and linear LE gains matching hand-computed trajectories to rtol 1e-9; shocked mean-reverting variable recovers with specified half-life |
| **E8** | 5.2, 5.8 | `engine/state.py` + `engine/simulation.py`: the year loop, wiring E3–E7 in the architecture §3 order; recording per ADR-9 (event log w/ provenance, factor trajectories, scenario flags, thin trajectories) | **Oracle diff vs E1 on FIX-A and FIX-B passes** (§5.2; FIX-C is compiler-only — no run semantics, not oracle-diffed); performance smoke: R=10,000 × 50 years < 60 s |
| **E9** | 5.9, 5.10 | `analysis/`: percentiles, scenario frequencies, conditional distributions, contribution analysis; run notebook / `run.py` | Analysis of a fixture batch reproduces hand-computable statistics (e.g. scenario flag frequency equals direct count from event logs) |
| **E10** | 5.11 | Full-catalog validation runs (requires data track complete) | The five success criteria of [[methodology/reference/mvp-dynamics-scope]] §8, each expressed as an executable check, all pass; validation outputs of [[methodology/reference/state-outputs]] §8.4 produced |

**Why E1 comes first.** For agent-driven development the scalar reference
implementation is not a late cross-check but the **primary verification
instrument**: it is small, directly transcribes the spec, and is easy to get
right; every subsequent vectorized module is then diffed against it under
shared draws (§5.2), converting "is this correct?" from judgment into
mechanics.

---

## 4. Frozen interface contracts

These seams are **normative**. An agent that needs to change one stops and
reports; it does not adapt the seam.

### 4.1 CompiledCatalog (compile layer → both engines)

Produced by `catalog/compile.py::compile_catalog(event_paths, omega, state_catalog) -> CompiledCatalog`.
All names resolved to integer indices; no strings in the hot path.

| Field | Type / shape | Notes |
|-------|--------------|-------|
| `event_ids` | `list[str]`, length E | position = event index everywhere |
| `lam` | `float64 [E, K]` | factor loadings |
| `sigma_idio` | `float64 [E]` | from `1 − (ΛΩΛᵀ)ᵢᵢ`, validated ≥ 0 |
| `causal_type` | `int8 [E]` | 1, 2, or 3 |
| `p_annual` | `float64 [E]` | Type 1 threshold; NaN for Types 2/3 |
| `type2` | per-event: pressure callable, `threshold`, `threshold_std`, `sharpness`, `floor` | callables per §4.3 |
| `type3` | per-event: precondition callables (`all`), sustained specs `(callable, years)`, `window`, `resolution` | |
| `resolution_tree` | per-event resolution probs + branch probs, plus `name → int` code maps | probs validated to sum to 1.0 |
| `impact_table` | flat rows: `(event, res_code, branch_code, entity_idx | −1, var_idx, mean, std, onset_kind, onset_years, dur_kind, dur_param)` | `inherit`/`scale` and wildcards already expanded |
| `cascade_edges` | rows: `(src_event, dst_event, delta, years, cond_callable | None)` | |
| `index` | `entity_id → int`, `var_name → int` (country and global), `factor_id → int` | shared with expression namespace |

### 4.2 StateTensor (engine-internal, shared with reference impl conceptually)

`country: float64 [R, N_ent, N_cvar]`, `global_: float64 [R, N_gvar]`, plus the
`index` maps from the catalog. The reference implementation uses the same
layout with `R = 1` semantics (see §5.2).

### 4.3 Expression callables

`fn(ns) -> np.ndarray` where `ns` maps every §3-namespace name
([[methodology/reference/expression-language]]) to an `(R,)` view. Returns
`(R,)` float64 (pressure) or bool (preconditions / `if`). Compiled and
validated per the expression spec; **the same callables serve both engines**
(the reference impl calls them with `(1,)` vectors).

### 4.4 Ledger slot layout (pinned decision #2, #3)

Parallel arrays of shape `[R, 256]`: `active (bool)`, `entity_idx (int16, −1 =
global)`, `var_idx (int16)`, `magnitude (float64, drawn)`, `onset_kind (int8)`,
`onset_years (int8)`, `dur_kind (int8)`, `dur_param (float64)`, `age (int16)`,
`owner_event (int16)` (for `until: resolved`). Cascade buffers use the same
slot pattern with `(dst_event, delta, years_remaining)` fields.

### 4.5 Simulation entry point and outputs

```python
simulate(catalog, initial_conditions, params, R, seed, years=50) -> RunOutputs
```

`RunOutputs`: terminal state (Parquet), event log with provenance
(`p_base`, `p_eff`, active-cascade bitmask; JSON/Parquet), factor trajectories
`float64 [R, K, T]`, scenario flags `bool [R, n_flags]`, thin trajectories for
the ADR-9 variable list, validation statistics per
[[methodology/reference/state-outputs]] §8.4.

### 4.6 RNG discipline (ADR-8)

One `np.random.SeedSequence(master_seed)`; `.spawn()` per run-block. Draws
occur in this **fixed order with fixed shapes** (all per-year except item 3,
which is consumed once at run initialization):

1. factor draws `[R, K]`
2. idiosyncratic draws `[R, E]`
3. Type 2 per-run threshold offsets — drawn **once at init**, `[R, E_type2]`
4. resolution uniforms `[R, E_resolving]`, branch uniforms `[R, E_resolving]`
5. impact magnitude normals `[R, n_impact_rows]`
6. dynamics noise `[R, n_noisy_vars]`

Shapes never depend on outcomes (draw for all runs, use where fired). This is
what makes replay and oracle diffing possible.

---

## 5. Verification protocol

### 5.1 Fixtures (committed under `sim/tests/fixtures/`)

| Fixture | Contents | Purpose |
|---------|----------|---------|
| **FIX-A** | 1 Type-1 event, 2 entities, 3 variables, dynamics noise off, 5 years | Hand-computable end-to-end expectations |
| **FIX-B** | One event of each type; one cascade edge (with `if`); one `until: resolved` impact; one `sustained` precondition; one permanent + one decaying impact | Exercises every mechanism once; hand-traced event log committed alongside |
| **FIX-C** | Taiwan + AMOC compiled from the real repo markdown | Compiler ground truth: output must equal the hand-built equivalent structure |

Fixtures are hand-built `CompiledCatalog` instances (not YAML) except FIX-C,
which exists precisely to test the compiler against a hand-built target.

E0 also commits the **deliberately-broken input variants** the E2 rejection
gate consumes — one minimal broken event file per failure mode: unknown
variable, bad enum, branch p-sum ≠ 1, banned AST node, undeclared resolution
name.

### 5.2 Oracle diff (the central check)

To compare engines, the reference implementation **replays a specific run of a
specific batch**: given `(master_seed, R, run_index r)`, it generates the same
full-width `[R, …]` draw arrays in the §4.6 order and consumes row `r` of each.
(A naive `R=1` run would consume different draws — this replay convention is
mandatory.)

Diff rule: for FIX-A/FIX-B at `R = 64`, every run's full state trajectory and
event log must match between engines — state to `rtol 1e-9`, event logs
(firings, resolutions, branches, years) **exactly**. Run in CI on every engine
change.

### 5.3 Statistical gates

Where behavior is distributional (E3, E4), gates use large-R empirical checks
with explicit tolerances (given in the stage table). Use fixed seeds; a gate
that flakes under seed change indicates a real problem, not test noise —
report it.

---

## 6. Guardrails

Standing prohibitions for all agents on this work:

1. **No new dependencies** beyond: numpy, scipy, pandas, pyarrow, pyyaml,
   pytest. Anything else requires explicit human approval.
2. **No spec edits from the engine track.** Engine agents do not modify
   `methodology/` or `events/`. If the spec seems wrong or ambiguous: stop,
   report, cite the documents.
3. **No feature invention.** If it isn't in the ADRs, the expression spec, the
   MVP dynamics scope, or this guide, don't build it — including "obvious"
   improvements (caching layers, config systems, CLI frameworks, plugins).
4. **No silent anything**: no silent caps, no silent dtype changes, no silent
   clamping, no swallowed exceptions. Every bound that can bind has a counter
   and a loud failure mode (pinned decision #3 is the model).
5. **Determinism is sacred.** No wall-clock, no unkeyed randomness, no
   iteration over unordered containers where order reaches results.
6. **Data track agents follow the Task 4.2 process exactly** — including the
   full-git-history prose-restoration step; validation failures are reported,
   not patched around.
7. **No hardcoded axis sizes.** Entity, variable, event, and factor counts
   (`E`, `K`, `N_ent`, `N_cvar`, `N_gvar`) derive at runtime from the
   `CompiledCatalog` and state-catalog index maps; no such count appears as a
   literal in engine code (fixture files excepted). This is what makes
   post-v0.1 catalog releases data changes rather than engine changes — see
   [[methodology/reference/catalog-versioning]].

---

## 7. Reporting and escalation

- Each stage completion report states: gate command(s) run, their output,
  deviations from contract (should be none), and open questions.
- Escalate (stop work, report to human) on: contract-vs-ADR conflict, gate
  that cannot be made to pass without changing a frozen seam, spec ambiguity
  with material implementation consequences, or any need to touch files
  outside scope.
- Do not escalate for: choices this guide already pins, naming/style within a
  module, test organization.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07 | Initial guide. Pins §5 open decisions from simulator-architecture (discharges Task 5.0); establishes fixture-driven build order with reference-impl-first sequencing |
| 2026-07-11 | Reconciled with [[strategy/roadmap]]: guide identified as Phase 1's execution plan; war events join the data track when authored; schema-breaking war lessons deferred to v0.2 backlog; one-causal-type-per-YAML rule stated; migration counts corrected against git history; compiler gate made dynamic over `events/` |
| 2026-07-12 | Review fixes: variance validation pinned to the declared `variance:` field (protects hybrid-type events at the E2/D-track gates); Phase 0 state-variable additions pinned spec-side (v0.1 axes frozen to MVP scope); broken-input fixture variants assigned to E0; §1 diagram shows E10 |
| 2026-07-12 | Catalog growth policy adopted: the axes pin scoped to build duration, with sanctioned widening moments (pre-E0 scope revision; post-E10 catalog releases) delegated to [[methodology/reference/catalog-versioning]]; guardrail 7 added (no hardcoded axis sizes) |

---

*Normative design sources: [[methodology/reference/simulator-architecture]],
[[methodology/reference/expression-language]],
[[methodology/reference/mvp-dynamics-scope]],
[[methodology/reference/event-yaml-schema]]. This guide adds order, gates,
contracts, and guardrails only.*
