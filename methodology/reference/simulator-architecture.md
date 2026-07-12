---
title: simulator-architecture
type: note
permalink: methodology/reference/simulator-architecture
tags:
- methodology
- reference
- simulator
- architecture
- implementation
- adr
- v0.1
---

# Simulator Architecture

**Document Version:** 0.1 (draft for discussion)
**Date:** July 2026
**Status:** Design specification — architecture overview + decision records

The engine that executes the v0.1 prototype (Tasks 5.1–5.11). This document
records the architecture at the level of **decisions and their rationale**, not
line-by-line module specs. Detailed module contracts follow once these decisions
are ratified.

**Related documents:**
- [[methodology/concepts/monte-carlo-framework]] — original methodology (§8–9 predate the current schema)
- [[methodology/concepts/gaussian-copula]] — how Ω enters sampling
- [[methodology/reference/factor-correlation-matrix]] — the 12×12 Ω matrix
- [[methodology/reference/event-yaml-schema]] — the input the compiler consumes
- [[methodology/reference/expression-language]] — **normative contract** for event-embedded expressions (companion to ADR-4)
- [[methodology/reference/mvp-dynamics-scope]] — Tier 1/2/3 dynamics the engine implements
- [[methodology/reference/state-dynamics]] — the six dynamics types
- [[methodology/reference/state-outputs]] — what the engine records

---

## 1. What changed since the original sketch

The implementation architecture in [[methodology/concepts/monte-carlo-framework]]
§8–9 assumed **independent factors and static per-event probabilities**. Under
that assumption every run, year, and event is an independent draw and the whole
simulation is one big vectorized `U < p` comparison.

The design has since outgrown that assumption in four places, and the engine must
absorb all four:

| Feature | Source | Consequence for the engine |
|---------|--------|----------------------------|
| **Correlated factors (Ω)** | [[methodology/reference/factor-correlation-matrix]] | Factors need a copula draw over Ω, not independent normals; idiosyncratic variance is `1 − (ΛΩΛᵀ)ᵢᵢ`, not `1 − Σλ²` |
| **Type 2 pressure functions** | [[methodology/reference/event-yaml-schema]] | Annual probability reads **per-run state** → path-dependent |
| **Type 3 preconditions + `sustained`** | [[events/geopolitical/taiwan-conflict]] | Firing is gated on **per-run multi-year memory** |
| **Cascades (`delta`, `years`, `if`)** | Taiwan event | A run's firing rewrites **that same run's** future probabilities |

Plus: impacts now carry `onset`/`decay`/`until: resolved` durability, events branch
through `resolutions → branches`, and a baseline "progress engine" runs every year.

**Net effect:** the simulator is no longer a static sampler. It is a **stateful,
path-dependent stepper**. The architecture below is organized around making that
stepper fast enough to hit the performance target (10k runs × 50 years < 60s)
without giving up the state↔probability↔state feedback.

---

## 2. Two layers

The system splits into a **compile layer** (slow, runs once) and a **runtime
layer** (fast, the hot loop). Everything the runtime touches is a pre-resolved
NumPy array or a pre-compiled callable — no string parsing, no dict lookups, no
markdown in the inner loop.

```
sim2075/sim/
├── catalog/                      # COMPILE LAYER (once, ~seconds)
│   ├── extract.py                #   pull ```yaml blocks out of events/**/*.md
│   ├── schema.py                 #   validate against event-yaml-schema
│   ├── expr.py                   #   compile Python-string exprs → vector callables
│   └── compile.py                #   → CompiledCatalog (all names → array indices)
├── engine/                       # RUNTIME LAYER (per run-block, the hot path)
│   ├── state.py                  #   StateTensor + entity/variable index maps
│   ├── factors.py                #   Ω Cholesky, correlated factor draws
│   ├── firing.py                 #   unified copula + type-specific thresholds
│   ├── memory.py                 #   sustained counters, cascade delta buffers
│   ├── impacts.py                #   active-shock ledger (onset/decay/durability)
│   ├── dynamics.py               #   drift + mean-reversion + transmission
│   └── simulation.py             #   the year loop
├── analysis/                     # distributions, scenarios, contribution
└── run.py
```

Directory sits under `sim/` at repo root so the wiki (`events/`, `methodology/`)
and the code stay cleanly separated.

---

## 3. The year step (data flow)

Every operation carries the run count `R` as the leading array axis. The Python
interpreter iterates **once per year (≈50)**, never once per run.

```
state: country[R, E, V]  ·  global[R, Vg]  ·  memory[R, …]  ·  ledger[R, …]

for year t in 2025..2075:
    1. FACTORS      F[R,K]  ~  N(0, Ω)          via cached Cholesky L (Ω = LLᵀ)
    2. PROPENSITY   Z = F @ Λᵀ + ε ;  U = Φ(Z)   correlated uniforms, one per event
    3. THRESHOLD    p_eff[R,E]  per causal type (see ADR-3):
                      T1: constant
                      T2: pressure(state) → sigmoid
                      T3: precondition gate × window × resolution
                    p_eff += cascade_delta[R,E]      (ADR-5)
    4. FIRE         fired = gate & (U < p_eff)
    5. RESOLVE      for fired events with resolutions: draw resolution+branch
    6. IMPACTS      push (event.branch) shocks into ledger; apply active shocks
    7. DYNAMICS     baseline drift → mean reversion → oil/food→inflation
    8. MEMORY       update sustained counters; decay/expire cascade buffers
    9. RECORD       append trajectory slice (subset of runs) + event log (all runs)
```

Path-dependence lives entirely in arrays that persist **across** the year loop
(`state`, `memory`, `ledger`), so it survives without a per-run Python loop.

---

## 4. Architecture Decision Records

Each ADR states the **context**, the **decision**, the **alternatives rejected**,
and the **consequences**. These are the ratifiable units of this document.

### ADR-1 — Execution model: vectorize across runs, loop over years

**Context.** 10k runs × 50 years × ~30 events × per-run state reads = ~15M
state-conditioned firing decisions, plus impact application and dynamics. A scalar
per-run Python loop with `eval` inside cannot hit <60s. But full flattening
(all runs × years × events at once) is impossible because year `t` depends on the
state produced by year `t−1`.

**Decision.** Carry `R` as the leading NumPy axis; loop in Python over the 50
years only. All 10k runs advance together as vectorized array operations. Within
a year, all events are evaluated as array ops across the run axis.

**Alternatives rejected.**
- *Scalar per-run loop + multiprocessing.* Simpler code and trivial expression
  eval, but needs heavy parallelism to approach the target and still burns the
  interpreter on 15M iterations. Kept as the **reference implementation** for
  cross-checking the vectorized engine, not as the production path.
- *Full flatten across years.* Impossible given inter-year state dependence.
- *JAX/Numba JIT (CPU or GPU).* Deferred. Revisit only if pure NumPy misses the
  target after profiling; adds a dependency and debugging friction not warranted
  for v0.1. Note the option stays cheap to exercise later — see consequences.

**Consequences.** The batch axis is load-bearing everywhere: state is a tensor,
memory is a tensor, the impact ledger is a tensor. Every design below is shaped by
"can this be expressed as an op over the `R` axis?" Runs remain independent, so the
`R` axis is also the natural chunking axis for multiprocessing (ADR-8).

The reference implementation has **two jobs**, not one: it is the correctness
oracle (diff against the vectorized engine at small `R` under shared seeds), and
it is the **narrator** — because runs are deterministic given the master seed
(ADR-8), any individual run that analysis flags as interesting can be *replayed*
through the scalar implementation with verbose instrumentation, recovering an
arbitrarily detailed per-run narrative without having stored it. Thin logging for
all runs, deep reconstruction on demand for the few that matter.

The constraints this ADR imposes (fixed-width tensors, no per-run control flow,
pure whitelisted expressions, explicit keyed RNG) are **exactly the constraints
GPU/JIT compilation requires** — so the design is GPU-ready as a side effect. At
v0.1 scale (10⁴ runs × ~30 events) per-year arrays are far too small to benefit
from a GPU; the option becomes attractive when the batch axis grows — tail
analysis at 10⁵–10⁶ runs, or sensitivity sweeps run as an additional batch
dimension (many parameter settings × many runs simultaneously). Caveat if
exercised: bit-exact CPU/GPU reproducibility will not hold, so the oracle
cross-check becomes tolerance-based rather than exact.

---

### ADR-2 — Factor sampling: Gaussian copula over Ω

**Context.** Factors are correlated ([[methodology/reference/factor-correlation-matrix]]:
19 non-zero off-diagonals, max ρ=0.55, PSD with min eigenvalue 0.20). The original
§8 pseudocode drew independent factors — no longer correct.

**Decision.** Precompute the Cholesky factor `L` of Ω once (`Ω = LLᵀ`). Each year
draw `F[R,K] = randn(R,K) @ Lᵀ`, giving correlated standard-normal factors. Event
propensity is `Zᵢ = Λᵢ·F + εᵢ` with idiosyncratic standard deviation

```
σ_idio,i = sqrt( 1 − (Λ Ω Λᵀ)ᵢᵢ )
```

— i.e. idiosyncratic variance is `1 − (factor-explained variance)`, using **Ω**,
matching the `variance:` target in each event's `factors:` block. (The old
`1 − Σλ²` form is only valid for independent factors and must not be used.)
Transform to correlated uniforms `U = Φ(Z)`.

**Alternatives rejected.**
- *Independent factors (original §8).* Understates clustering — the entire reason
  Ω exists.
- *Direct event-level correlation matrix + Cholesky.* O(n²) and re-introduces the
  PSD fragility the factor model was adopted to avoid.

**Consequences.** `L` and the per-event `σ_idio` vector are compile-time constants.
Validate Ω (symmetric, unit diagonal, PSD) at compile time and hard-fail on
violation, per the check in [[methodology/reference/factor-correlation-matrix]].

---

### ADR-3 — Unified firing: copula supplies the uniform, causal type supplies the threshold

**Context.** Events are simultaneously (a) correlated through factor loadings —
Taiwan loads on F_EAS/F_GPT — and (b) governed by a Type 1/2/3 probability model.
These two things must compose, not compete.

**Decision.** Separate the two cleanly:
- The **copula** (ADR-2) produces one correlated uniform `Uᵢ ∈ [0,1]` per event per
  run per year. This carries *all* cross-event correlation.
- The **causal type** produces a per-run firing threshold `p_eff,i[R]`:

  | Type | Threshold |
  |------|-----------|
  | **1 Stochastic** | constant `annual` |
  | **2 Threshold** | `floor + (1−floor)·σ( sharpness·(pressure(state) − threshold) )`, pressure evaluated per-run (ADR-4) |
  | **3 Contingent** | `gate(preconditions, sustained) × window × resolution` — `gate ∈ {0,1}` per run |

- An event **fires** when `gate & (Uᵢ < p_eff,i)`. Cascade deltas (ADR-5) add to
  `p_eff` before the comparison.

For Type 3, `window × resolution` is the annual discontinuity probability; the
`resolutions[].p` distribution (which sums to 1.0) then selects **which**
discontinuity, drawn only for runs that fired.

**Alternatives rejected.**
- *Bake state-dependence into the copula draw itself* (e.g. shift `Z` by pressure).
  Conflates correlation with probability and makes the marginal firing rate
  intractable to reason about. Keeping `U` (correlation) and `p_eff` (rate)
  orthogonal is what makes the model auditable.

**Consequences.** One firing kernel handles all three types; the type only changes
how `p_eff` and `gate` are computed. `threshold_std` (uncertainty in the Type 2
threshold location) is an **open detail** — resolve by either marginalizing the
logistic analytically or drawing a per-run threshold offset at init. Flagged in §5.

---

### ADR-4 — Vectorized expression evaluation

**Context.** Pressure functions and preconditions are **Python-string expressions**
in the YAML (`"F_GPT > 1.0"`, `"chn.military_spending_deviation > 0.15"`, the AMOC
pressure formula). They read factors and state variables and must be evaluated for
all 10k runs each year.

**Decision.** Compile each expression **once** at catalog-compile time into a
callable. At runtime, evaluate it against a namespace where every name binds to its
`(R,)`-shaped run-vector. Because the expressions use only arithmetic and
comparison, NumPy broadcasting resolves all 10k runs in a single evaluation —
`"F_GPT > 1.0"` becomes a `(R,)` boolean array for free.

- `expr.py` parses each string with `ast`, **rejects** any node type outside a
  vectorizable whitelist (names, numeric literals, arithmetic, comparison, boolean
  ops, whitelisted funcs like `min`/`max`/`abs`), and compiles the survivors.
- Names resolve through the state index map: `chn.military_spending_deviation` →
  a view into `country[:, idx(chn), idx(that_var)]`.

The permitted subset, its semantics under broadcasting, and the authoring rules
are specified normatively in [[methodology/reference/expression-language]] —
that document is the contract between event authors and this compiler.

**Alternatives rejected.**
- *`eval` per run.* 15M interpreter calls — defeats ADR-1.
- *A bespoke mini-DSL instead of Python.* The schema already commits to "Python
  expressions for logic"; re-inventing it is churn. Compiling the Python subset to
  vector ops honors the schema and stays fast.

**Consequences.** The AST whitelist is a hard validation gate — an expression that
references a non-vectorizable construct fails at compile time, not mid-run. This
also becomes a natural home for validation rule #3 in the schema (every referenced
variable must exist in the state catalog).

Vectorized evaluation **changes the language**, not just its speed: broadcasting
breaks `and`/`or` (the compiler rewrites them elementwise — safe because
expressions are pure and total, but guarding idioms like `x > 0 and log(x) > 1`
no longer guard), forbids ternary conditionals (use `where()`), and evaluates
every sub-expression for every run. The schema's "Python expressions for logic"
is thereby amended to *the broadcastable subset of Python* — a schema-level
contract, not an implementation detail.

It also forces an **expressiveness boundary** that feeds back into event
authoring: expressions read the *current* state only. Anything requiring memory
("GDP declined 5 consecutive years"), aggregation with logic, or iteration must
be promoted to an engine-maintained state variable that the expression merely
reads — the `years_since_irregular_transition` pattern, and the
[[methodology/concepts/synthetic-variable-problem]] discipline applied to
formulas. Details and the escape-hatch process:
[[methodology/reference/expression-language]] §6.

---

### ADR-5 — Per-run memory: sustained counters and cascade buffers

**Context.** Two features require memory that persists across years within a run:
`sustained` preconditions ("F_GPT > 1.0 for 2 years") and cascades (a firing raises
another event's probability by `delta` for `years`).

**Decision.** Represent both as tensors on the run axis, updated in step 8 each
year:
- **Sustained counters** `counter[R, C]` for each (event, sustained-condition):
  increment where the condition holds this year, reset to 0 where it doesn't; the
  gate is `counter ≥ years`.
- **Cascade deltas** as an accumulator `cascade_delta[R, E]` plus expiry tracking.
  When an event fires, add its outgoing `delta` to target events (subject to the
  optional `if:` predicate, itself an ADR-4 expression) with a remaining-years
  countdown; decrement and expire each year. Overlapping cascades sum.

**Alternatives rejected.**
- *Recompute history from an event log each year.* O(years²) and awkward to
  vectorize.

**Consequences.** Memory tensors are part of the run state and must be
seed-reproducible and chunkable exactly like `state` (ADR-8). Exact storage for
overlapping/expiring cascades (fixed-width active-effect tensor vs. accumulator +
schedule) is an **impl detail** shared with ADR-6's ledger — same pattern.

---

### ADR-6 — Impact durability: an active-shock ledger

**Context.** A fired `(event.branch)` injects a set of impacts, each with an
`onset` (`immediate` / `{delayed:N}` / `{gradual:N}`) and a durability
(`decay:N` half-life / `permanent` / `until: resolved`). A single run can have many
overlapping active shocks whose current magnitude depends on years-elapsed.

**Decision.** Maintain a fixed-width **active-shock ledger** on the run axis,
`ledger[R, max_active, fields]`, where each slot records target variable index,
signed magnitude draw, onset schedule, durability model, and age. Each year (step 6)
the engine recomputes every active shock's current contribution from its schedule
and scatter-adds into the target state variables; expired shocks free their slot.
`until: resolved` ties a shock's lifetime to a per-run event-status flag that the
resolution machinery clears.

- Magnitudes are drawn from `[mean, std]` at firing time (sign encodes direction,
  per schema).
- `inherit` + `scale` branches (e.g. `full_invasion` inherits `limited` ×1.5) are
  expanded at compile time into concrete impact lists — the runtime never resolves
  inheritance.
- Wildcard `*.gdp_real` impacts are expanded to the 40 country indices at compile
  time.

**Alternatives rejected.**
- *Per-run Python list of shock objects.* Clean but breaks the vectorized hot path.
- *Collapse all durability to permanent level shifts.* Loses the decay dynamics
  that distinguish a financial shock from a climate tipping point — central to the
  model's thesis.

**Consequences.** `max_active` must be sized against the worst plausible run
(estimate from event count × impacts-per-branch × overlap); a hard cap with an
overflow counter guards against silent truncation. This is the single trickiest
component to vectorize and the first candidate for the reference-implementation
cross-check (ADR-1).

Two rules keep the ledger scaling with the **shock intensity of the modeled
world rather than catalog size** (important if the catalog grows toward
hundreds of events):
1. **`permanent` shocks never occupy a ledger slot.** A permanent impact is a
   one-time level shift; apply it to state at firing time and forget it. This
   removes the longest-lived slot occupants entirely.
2. **Epsilon-cull decayed shocks.** Expire a decaying shock once its
   contribution falls below a threshold (a `decay: 2` shock is at ~3% of
   magnitude after 10 years) rather than carrying it forever. This bounds
   effective lifetime, which bounds peak concurrency.

More generally, catalog size `E` enters every core structure **linearly**
(`U[R,E]`, `p_eff[R,E]`, `Λ[E,K]`, sparse cascade edges) — there is no
combinatorial growth, *provided nothing pairwise between events is ever built*.
This is a standing design rule and the structural argument against the legacy
compound multipliers (open decision §5.5), which are inherently `E²`.

---

### ADR-7 — Catalog compilation: markdown YAML → resolved arrays

**Context.** Events are authored as embedded ```yaml blocks inside prose markdown
(29 files, one per event). The runtime must not see markdown, YAML, or string names.

**Decision.** A compile pass (`catalog/`) that:
1. **Extracts** every ```yaml block from `events/**/*.md` and merges the blocks per
   file into one event record (`specification` / `probability` / `factors` /
   `resolutions` / `impacts` / `cascades` / `research`).
2. **Validates** against [[methodology/reference/event-yaml-schema]]: enum values,
   resolution/branch probabilities sum to 1.0, factor IDs exist in [[factors/]],
   cascade target events exist, referenced state variables exist, factor variance
   within tolerance of target.
3. **Compiles** to a `CompiledCatalog`: the `Λ` loading matrix `[E, K]`, per-event
   `σ_idio`, compiled probability callables (ADR-4), resolution/branch probability
   trees, compiled+expanded impact lists (ADR-6), and cascade edges — all with
   names already resolved to integer indices.

**Alternatives rejected.**
- *Hand-maintain a separate `events.json`.* Duplicates the source of truth; the
  prose files already are the catalog. A one-way compile keeps them authoritative.

**Consequences.** The compiler is where every schema validation rule is enforced;
a bad event fails the build, never the simulation. Compile output can be cached
(pickle/npz) so iterating on the engine doesn't re-parse 29 files each run.

---

### ADR-8 — State representation and reproducibility

**Context.** ~46 entities × ~18 v0.1 variables + ~22 globals, per run, evolving
over 50 years, must be reproducible and chunkable across cores.

**Decision.**
- **State** is dense tensors: `country[R, E, V]`, `global[R, Vg]`, `factors[R, K]`,
  with compile-time index maps (`entity_id → row`, `var_name → col`) shared with
  ADR-4's name resolution. v0.1 uses the 46-entity (40 countries + 6 Tier 1
  aggregates) × ~18-variable scope from [[methodology/reference/mvp-dynamics-scope]];
  the entity/variable **axes are configurable** so post-v0.1 expansion can widen
  toward the full state catalog (52 entities incl. Tier 2 aggregates / 63
  variables) without code changes.
- **RNG** is one `numpy.random.SeedSequence`; each run-block gets an independent
  child via `.spawn()`, so results are deterministic given the master seed and
  invariant to how runs are chunked across processes.

**Alternatives rejected.**
- *Per-entity Python objects.* Readable, un-vectorizable.
- *Global mutable `np.random` state.* Not reproducible under multiprocessing.

**Consequences.** Runs are embarrassingly parallel (per [[methodology/reference/state-outputs]]
§8.2): split the `R` axis across processes, each with its spawned seed, concatenate
outputs. No inter-run communication.

---

### ADR-9 — Output capture: log everything thin, trajectories for a subset

**Context.** Full 50-year trajectories for 3,072 variables × 10k runs ≈ 15 GB
([[methodology/reference/state-outputs]] §8.1) — too much to keep for every run.

**Decision.** Follow the state-outputs recommendation, extended:
- **All runs:** terminal state vector + full event log + per-run summary
  statistics and scenario flags, computed during the run.
- **Event log carries provenance.** Each firing records not just
  (event_id, year, resolution, branch, magnitude draws) but also `p_base`,
  `p_eff`, and which cascade deltas were active at firing time. Firing is
  probabilistic, so no causal claim is possible — but "Egypt's firing
  probability was elevated 2.5× by the Sahel cascade when it fired" is an
  auditable, quantified narrative link, and it costs two floats and a bitmask
  per fire.
- **Factor trajectories `F[R, K, T]` for all runs.** At 10⁴ runs × 12 factors ×
  50 years this is ~50 MB — trivial — and it supplies the "weather" of each run
  ("2031 was a +2.1σ climate/food year") for narrative reconstruction and for
  factor-contribution analysis (the sensitivity instrument of
  [[strategy/roadmap]] Phase 2).
- **Scenario flags are config, not code.** Predicates like "multi-year famine in
  SSA" are defined declaratively (an [[methodology/reference/expression-language]]
  condition + a minimum duration) and computed for **all** runs during
  simulation using the same counter machinery as ADR-5's sustained
  preconditions. Cross-run frequencies ("in 56% of runs…") are then a mean over
  a boolean run-axis array.
- **Subset (≈1,000 runs):** full annual trajectories for the key variables in
  [[methodology/reference/state-outputs]] §4.1. Prefer widening the set of
  *thin* trajectories kept for all runs (a dozen variables × 50 years × 10⁴
  runs ≈ 50 MB) over deepening the subset — post-hoc scenario queries want
  breadth of runs, not breadth of variables.
- **Derived assessments** (stability, fragility, alignment, …) are computed
  **post-run from observables** — never during simulation, never as state variables
  ([[methodology/reference/state-outputs]] §1, [[methodology/concepts/synthetic-variable-problem]]).
- Storage format: Parquet for tensors, JSON for logs.

**Consequences.** The event log is the primary substrate for contribution
analysis ("in the worst 5% of runs, which events fired?" — [[strategy/roadmap]]
Phase 2), so it must be complete even where trajectories are dropped. Anything *not* recorded remains recoverable:
determinism by seed (ADR-8) means any single run can be replayed with verbose
instrumentation through the reference implementation (ADR-1) — narrative depth is
reconstructed on demand, not stored speculatively.

---

## 5. Open decisions — RESOLVED

These were open at first draft; all five are now pinned in
[[methodology/project/implementation-guide]] §0, which is the normative record.
Summary:

1. **Type 2 `threshold_std` handling** (ADR-3) → **per-run threshold offset**
   drawn once at run initialization (simpler than analytic marginalization;
   adds realistic cross-run dispersion).
2. **Cascade / ledger storage shape** (ADR-5, ADR-6) → **fixed-width
   active-effect tensors** with slot recycling; one shared pattern for both.
3. **`max_active` ledger width** (ADR-6) → **256** per run, overflow as a
   counted hard failure; revisit after fixture pilots.
4. **Reference (scalar) implementation location** (ADR-1) → **`sim/reference/`**
   in the same package; shares the compile layer, none of the engine.
5. **Compound multipliers** (framework §8.6) → **retired**; compounding is
   expressed through cascades + additive impacts only (they were the design's
   only `E²` pairwise structure — see ADR-6 consequences).

---

## 6. Mapping to implementation tasks

| Task ([[methodology/project/tasks]] §5) | Delivered by |
|------|--------------|
| 5.1 Prototype directory structure | §2 layout |
| 5.2 State vector management | ADR-7, ADR-8 (`engine/state.py`) |
| 5.3 Factor sampling with correlations | ADR-2 (`engine/factors.py`) |
| 5.4 Event firing logic | ADR-3, ADR-4 (`engine/firing.py`) + `catalog/` |
| 5.5 Impact transmission | ADR-6 (`engine/impacts.py`) |
| 5.6 Aftermath tracking | ADR-6 resolution/branch + `until: resolved` |
| 5.7 Baseline dynamics | `engine/dynamics.py` per [[methodology/reference/mvp-dynamics-scope]] §5.1 |
| 5.8 Main simulation loop | §3 (`engine/simulation.py`) |
| 5.9 Output analysis | ADR-9 (`analysis/`) |
| 5.10 Prototype run notebook | `run.py` / notebook |
| 5.11 Validate sensible output | [[methodology/reference/mvp-dynamics-scope]] §8 success criteria |

The cascade/memory machinery (ADR-5) spans 5.4 and 5.6 and is not called out as its
own task — recommend adding **Task 5.4b: per-run memory (sustained counters +
cascade buffers)** to the backlog.

---

## 7. Risks

| Risk | Mitigation |
|------|------------|
| Vectorized ledger (ADR-6) is subtly wrong | Cross-check against the scalar reference impl (ADR-1) on small `R` |
| Expression whitelist too strict / too loose | Compile-time AST validation with explicit allow-list; fail loud |
| `max_active` overflow silently truncates impacts | Hard cap + overflow counter surfaced in validation output |
| Path-dependence makes runs non-reproducible under parallelism | `SeedSequence.spawn()` per run-block (ADR-8) |
| Performance target missed in pure NumPy | Profile first; JAX/Numba is a held-in-reserve escape hatch, not a v0.1 commitment |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07 | Initial architecture overview + ADRs (draft for discussion) |
| 2026-07 | Design-review refinements: reference impl as narrator + replay-by-seed (ADR-1); GPU/JIT readiness note (ADR-1); expression language extracted to normative spec (ADR-4 → [[methodology/reference/expression-language]]); ledger scaling rules — permanent shocks fold into state, epsilon-culling, no pairwise structures (ADR-6); event-log provenance, factor trajectories for all runs, declarative scenario flags (ADR-9); recommendation to retire compound multipliers (§5.5) |
| 2026-07 | §5 open decisions resolved and pinned in [[methodology/project/implementation-guide]] §0 |
| 2026-07-11 | Reconciled with [[strategy/roadmap]]: superseded-plan phase numbers removed (ADR-8 expansion no longer keyed to "Phase 4"; ADR-9 contribution analysis keyed to roadmap Phase 2); ADR-8 v0.1 scope corrected to the 46-entity MVP dynamics scope (was a stale 15-country figure from the superseded development roadmap) |

---

*Ratify the ADRs and resolve §5 before detailed module contracts. For the dynamics
this engine runs see [[methodology/reference/mvp-dynamics-scope]]; for what it
records see [[methodology/reference/state-outputs]].*
