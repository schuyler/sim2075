# sim2075 engine

Code for the Monte Carlo discontinuity model whose catalog and methodology
live in the rest of this repository. This is a scenario-exploration tool
under documented judgment, not a forecasting system: every number it consumes
is a reasoned, diffable field in an event file under `events/`, and the
engine's job is to sample the joint consequences of those judgments faithfully.

Normative design: [`methodology/reference/simulator-architecture.md`](../methodology/reference/simulator-architecture.md)
(ADRs), [`expression-language.md`](../methodology/reference/expression-language.md),
[`event-yaml-schema.md`](../methodology/reference/event-yaml-schema.md),
[`mvp-dynamics-scope.md`](../methodology/reference/MVP%20Dynamics%20Scope.md).
Execution plan: [`methodology/project/implementation-guide.md`](../methodology/project/implementation-guide.md).
This README adds nothing to those documents except the implementation
decisions they left open (§3) and what the build has found so far (§4).

## 1. Status

| Stage | Deliverable | Gate | State |
|---|---|---|---|
| E0 | `sim/` scaffolding, fixtures FIX-A/B/C, five broken-input variants | `pytest` collects and runs | done |
| E1 | scalar reference implementation `sim/reference/` | FIX-A reproduced exactly; FIX-B event log matches hand trace | done |
| E2 | catalog compiler `sim/catalog/` | compiles the completed migrations; rejects each broken variant naming the event | done |
| E3 | `sim/engine/factors.py`: Ω validation, Cholesky, correlated draws, propensity, copula uniforms | R=100k: factor correlation within ±0.02 of Ω; per-event Z variance within ±0.02 of 1 | done |
| E4 | `sim/engine/firing.py`: per-type `p_base` and gates, per-run Type 2 thresholds, fire mask | R=100k: Type 1 frequency within 3σ for every fixture event; Type 2 monotone in pressure; Type 3 never fires while gated off | done |
| E5 | `sim/engine/memory.py`: sustained counters, cascade slots, `EventState` updates, resolution/branch code draw | hand-built FIX-B factor path opens the sustained gate in exactly the specified year and resets on interruption; cascade delta present for exactly `years` years after firing; conditional cascade respects its `if`; 257th live cascade raises `LedgerOverflow` | done |
| E6 | `sim/engine/impacts.py`: active-shock ledger, impact-row selection and magnitudes, shock schedule, epsilon-cull, `until: resolved` flags | single decaying shock matches the closed-form half-life to rtol 1e-9 and its epsilon-cull year restores the no-shock value and frees the slot; `permanent` + `immediate` takes no slot, a ramped `permanent` frees its slot at onset end keeping its level; delayed/gradual onset per the §3 table; `until: resolved` holds `resolves_after` years and re-firing restarts it; multiplicative decay returns to the no-shock path, contribution ≤ −1 raises `ImpactOutOfRange`; `max_active + 1` live shocks raise `LedgerOverflow`, `max_active` do not; oracle diff on FIX-B passes | done |
| E7 | `sim/engine/dynamics.py`: step 7 — Tier 2 mean reversion, then `gdp_stock` compounding and Tier 1 drifts (growth-rate-first); oil/food → inflation transmission is E7b, after D4 (§4, item 19) | no-event FIX-A run compounds `gdp_per_capita` at 2%/yr and adds 0.2/0.1 yr of life expectancy per year, matching closed forms to rtol 1e-9; a σ = 0 mean-reverting variable displaced by initial condition or by an E6 shock sits at `μ + d · 0.5^(k/h)` after `k` years for h ∈ {1, 2, 3, 0.5}; stock compounds by post-reversion growth; noise from the entry's own `dyn_z` column; phase-2 declaration order; loud failures on unknown key/kind, `dyn_z` shape, state dtype/shape; every scenario cross-checked against the reference | done |
| — | §5.2 oracle diff, `sim/tests/test_oracle_diff.py`: FIX-A/FIX-B at R=64 under `SeededDraws` | F and U every year; every year from the reference's recorded state: `p_eff`, gate, fire mask, resolution/branch codes, cascade bitmask, sustained counters, impact magnitudes, `until: resolved` flags, live ledger; dynamics-free mode (both engines `DynamicsSpec([])`, own state from initial conditions, plus FIX-B's scripted draws with `x.stress` 2.0, and test-built ramped-onset, long-horizon, `until: resolved` re-firing and small-`max_active` variants): full state trajectory (rtol 1e-9), exact event log, `LedgerOverflow` runs and year, `ImpactOutOfRange` runs, year, row and contribution; full-dynamics own-state mode (both engines on the fixture's own `DynamicsSpec`, E3–E7 in step order; FIX-A and FIX-B, FIX-B also over 20 years, plus test-built FIX-A variants with distinct σ > 0 on every mean-reverting variable and with an additive drift on a `gdp_stock`'s growth variable declared before and after the stock): the same per-year diff — grows with each stage; through `simulate()` (the E8 gate, `test_e8_simulation.py` and the `test_oracle_diff_simulate*` cases): the engine's own loop, blocks and recording on FIX-A/FIX-B at one and four blocks, FIX-B over 20 years, noisy FIX-A, the drift on a growth key, with `n_full = R`, thin keys and mixed scenario flags — full trajectories, terminal state, factors and thin at rtol 1e-9, flags and `max_active_seen` exactly, the event log exactly with magnitudes row for row; the ramped overflow and out-of-range variants raise through `simulate()` naming the reference's runs, year, row and contribution | in suite |
| E8 | `sim/engine/state.py` (block state tensor, state-key binding) and `sim/engine/simulation.py`: `simulate(catalog, initial_conditions, dynamics, params, R, seed, recording)` → `RunOutputs`, the year loop wiring E3–E7 in step order over §4.6 blocks, recording per ADR-9 (terminal state, factors `[R, K, T]`, columnar event log with provenance, thin and full trajectories, scenario flags, `max_active_seen`) | oracle diff through `simulate()` (row above); hard failures name the reference's runs and year; step order pinned; flags equal a direct count over recorded trajectories; performance smoke R=10,000 × 50 years < 60 s (opt-in, below) | done; the smoke raises on the data (§4, items 25–26) |
| E9–E10 | analysis, end-to-end validation | per guide §3 | not started |

Data track (guide §2): D1 and D2 done — all 29 events compile and the
full-catalog gate (`strict_cascades` on) is green with no dropped edges
(2026-10-22, after `US_CONSTITUTIONAL_CRISIS` landed; §4 item 10). D3 and
D4 (initial conditions, dynamics defaults) are not started.

```
pip install -e ".[test]"
python -m pytest                     # the stage gates (`python -m`: a bare `pytest` may be another interpreter's)
python -m sim.catalog.cli events     # compile report for every migrated event
SIM2075_SMOKE=1 python -m pytest sim/tests/test_e8_simulation.py -k smoke -s   # E8 performance smoke (opt-in; prints time and profile)
```

The smoke is skipped unless `SIM2075_SMOKE=1`, so the default run stays
fast. It compiles every migrated event except those whose compile notes carry
the multiplicative "mean ≤ −1" warning (derived, not listed by hand; today
Taiwan), takes each global's `baseline_2025` as its initial condition and
builds smoke-only dynamics from MVP scope §2.2/§3 inside the test (§4, item
25). It currently fails on the data, not the loop: see §4, item 26.

## 2. Layout

```
sim/
├── catalog/      compile layer (ADR-7): extract.py · schema.py · expr.py · compile.py · cli.py
├── reference/    scalar reference engine (ADR-1): model.py (inputs) · engine.py (the year step)
├── rng.py        draw schedule contract (guide §4.6), shared by both engines
├── data/         state_catalog.yaml (generated from the markdown catalogs) · omega.yaml (Ω, transcribed)
├── engine/       vectorized runtime: factors.py (E3) · firing.py (E4) · memory.py (E5) · impacts.py (E6) · dynamics.py (E7) ·
│                 state.py (E8, block state tensor) · simulation.py (E8, `simulate` / `RunOutputs`)
├── analysis/     E9 (empty)
└── tests/        fixtures/ (fix_a, fix_b, fix_c, broken/) and one test module per gate
```

`data/state_catalog.yaml` is the compiler's name authority (schema validation
rule 3) and sizes the engine's axes (guardrail 7). It is generated from the
markdown state catalogs; regenerate it when they change rather than editing
it. Derived variables are included so expressions may read them, but they are
rejected as impact targets. The §9 "outputs only" assessments are excluded.

## 3. Pinned implementation semantics

Everything here is a choice the normative documents did not make. Each is
implemented in the reference engine, exercised by a fixture, and must be
reproduced exactly by the vectorized engine. Changing one is a versioned
decision, not a refactor.

**Year step.** Transcribes architecture §3 in order: factors → propensity →
threshold (+ cascade deltas) → fire → resolve → impacts → dynamics → memory →
record. Expressions and gates read start-of-year state and this year's factor
draw. The vectorized loop (`simulate`, E8) runs it per §4.6 block: one block
per `params.block_size` runs with `run_offset = start`, Type 2 thresholds once
per block from `stream.init["t2_offset"]`, state from `StateTensor` (the
initial conditions broadcast over the block), and per year `FactorModel.year`
(1–2) → `namespace_from_state` → `FiringModel.base`, `p_eff = p_base +
MemoryModel.deltas()` (3) → `FiringModel.fire` (4) → `MemoryModel.resolve`,
then `ImpactLedger.resolve` (5) → `ImpactLedger.apply` (6) →
`DynamicsModel.step(country, global_, dyn_z)` (7) →
`MemoryModel.end_of_year(sustained_now, year)`, then
`ImpactLedger.end_of_year(year)` (8) → record (9). The two step-8 calls touch
disjoint state; their order is pinned and tested all the same. Outputs are
assembled by global run index, so results depend on `(seed, block_size)` and
nothing else; `LedgerOverflow` and `ImpactOutOfRange` propagate with their
global run indices and are never caught. `SimParams.max_active` bounds the
shock ledger as it does in the reference; the cascade slots keep pinned
decision #3's width (`MAX_ACTIVE`, 256), which the reference's cascade list
does not bound at all — a run would need more than 256 live cascades for the
engines to differ, which no fixture or catalog approaches.

**Firing.** `fired = gate & (U < p_eff)` with `p_eff = p_base + Σ active
cascade deltas`. `p_eff` is not clamped: a value ≤ 0 never fires and ≥ 1
always fires, which is what unclamped arithmetic gives and is never silent.
Type 2 `p_base = floor + (1 − floor) · σ(k · (pressure − threshold_r))` with
`threshold_r = threshold + threshold_std · z_r` drawn once per run (pinned #1;
this is the probability-estimation logistic with ceiling 1). Pressure is on
`threshold`'s 0–100 scale (schema §Type 2, 2026-10-12); the compiler evaluates
each pressure expression at the state catalog's `baseline_2025` values and
rejects the event outside `threshold ± 4·threshold_std`, or records a skip in
`meta["notes"]` when a name it reads has no baseline (country variables do
not, yet). Note that `probability-estimation.md`'s worked numbers for this
logistic (p ≈ 1% at pressure 45 with threshold 65, k 0.15, floor 0.002) do
not follow from its own formula, which gives ≈ 4.9%; the formula is what is
implemented, the worked numbers are not. Type 3
`p_base = window · resolution`, `gate = all(preconditions) ∧ all(counter ≥ years)`.

**Sustained counters** are updated in step 8 from the same evaluation the
gate used in step 3, so a gate in year *t* sees counters reflecting years
≤ *t − 1*: "F_GPT > 1.0 for 2 years" means the two years *before* the firing
year. Counters reset to 0 the first year the condition fails.

**Cascades.** A cascade pushed by a firing in year *t* is active for exactly
`years` subsequent years, *t + 1 … t + years*, never the firing year itself
(step 3 precedes step 4). Its `if` is evaluated at firing time with the source
event's just-drawn `resolution`/`branch`. Overlapping cascades sum.
`triggered_by` lists are informational; only `triggers` produce edges.

**Shock schedule** (increment model: each year the state receives
`contribution(age) − contribution(age − 1)`, so decay is recovery and state is
additive in the variable's own units):

| onset | ramp(age) | onset complete at age |
|---|---|---|
| `immediate` | 1 | 0 |
| `{delayed: N}` | 0 for age < N, else 1 | N |
| `{gradual: N}` | min(age + 1, N) / N | N − 1 |

`contribution = M · ramp(age)` until onset completes; `decay: h` then
multiplies by `0.5^((age − onset_end) / h)`. Magnitude `M = mean + std · z`
is drawn at firing. Rows the compiler tags `multiplicative` (`gdp_real`:
fractions of the entity's current value, schema §Impact Fields "Units",
2026-10-12) move the state by the ratio `(1 + contribution) / (1 +
previous contribution)` instead of the difference: `state *= 1 +
contribution` at firing, and a contribution that decays to zero returns the
state to its no-shock path (a literal `state *= 1 + increment` would not).
A multiplicative contribution ≤ −1 is an `ImpactOutOfRange` hard failure
naming the run, year and row. Because multiplicativity is a property of the
variable, additive and multiplicative shocks never share a target, so the
order in which a year's shocks are applied is immaterial. `permanent` + `immediate` folds into state at firing and
takes no slot; `permanent` with a ramp holds a slot until the ramp completes,
then is freed. A decaying shock is epsilon-culled when `|contribution| <
1e-4 · |M|`: its remaining contribution is returned exactly to zero and the
slot freed. More than `max_active` slots is a `LedgerOverflow` naming the run
and year.

**`until: resolved`.** A firing sets the event active for
`CompiledCatalog.resolves_after[e]` years including the firing year (the
event's required `probability.resolves_after`, schema 2026-10-12); the flag
is cleared in step 8 of the last active year and the shock's contribution
drops to zero the year after. Re-firing while active restarts the window and
pushes additional shocks. Events with no `until: resolved` rows carry 0 and
are never active past the firing year's step 8. The array is a per-event
field of the catalog, beyond the guide's §4.1 table (§4, item 2).

**Expressions.** `years_since` is `year − last_fire_year`, a very large
number for an event that has never fired. `branch` names usable in
expressions must be unique across the event's resolutions. Multi-line YAML
block scalars are parsed as one parenthesized expression.

**Vectorized modules** (E3–E7) consume whole §4.6 blocks and reproduce
the reference's steps 1–8 for every run of the block: `FactorModel.year`
gives `F = z Lᵀ` and `U = Φ(F Λᵀ + σ_idio ε)`; `FiringModel.thresholds`
takes the init-time `t2_offset` block; `FiringModel.base` evaluates the §4.3
callables once over `(R,)` views (namespace from `namespace_from_state`
plus per-event `resolution`/`branch`/`years_since` columns of an
`EventState`) and returns `p_base`, the Type 3 gate and this year's sustained
evaluations for step 8; `FiringModel.fire` is `gate & (U < p_eff)`. Type 2
uses `scipy.special.expit`, which agrees with the reference's `1/(1+e^{−x})`
to rounding (the oracle diff's rtol 1e-9 covers it). Per-run memory
(`EventState`, sustained counters, cascade deltas) is read there and owned by
E5: `MemoryModel` holds the counters, the `EventState` it updates where an
event fires, and the cascade slots (`[R, max_active]` arrays `active`,
`dst_event`, `delta`, `years_remaining`, `src_event`, recycled lowest-free
first; overflow raises `LedgerOverflow` with the list of overflowing run
indices); `draw_codes` is the step-5 resolution/branch draw for every run and
event, which E6 reuses for impact rows. E6's `ImpactLedger` owns the shock
ledger and the per-event `until: resolved` flags (`event_active` bool and
`active_until` int64, `[R, E]`): `resolve` (step 5) selects the impact rows
matching each firing's codes, draws `M` from `impact_z` (drawn for every row
and run, used where selected; `ImpactDraw.for_firing` gives
`EventFiring.magnitudes`) and sets the flags; `apply` (step 6) ages, applies
and frees live shocks, then applies and slots this year's, mutating the
caller's `country`/`global_` in place; `end_of_year` (step 8, after
`MemoryModel.end_of_year`) clears the flags. Ledger slots are the guide's
§4.4 `[R, max_active]` arrays (`max_active` from `SimParams`), recycled
lowest-free-first, plus three fields the reference's schedule needs and the
§4.4 table omits: `row` (int32, the `impact_table` row: provenance and the
`ImpactOutOfRange` message), `prev` (float64, the contribution currently in
state) and `mult` (bool, the row's `multiplicative` tag) — beyond the guide's
§4.4 slot layout, as the `multiplicative` column is beyond §4.1 (§4, item 5).
`LedgerOverflow` and `ImpactOutOfRange` carry the list of offending global run
indices (the reference raises with its single run's index; both exception
types accept either); `ImpactOutOfRange`'s row and contribution are those the
reference reports for the lowest offending run: its first offending shock in
the reference's application order, live shocks by firing year, owner event and
row, then this year's by event and row. Shocks on the same variable are summed (or
multiplied) in slot order rather than the reference's list order, which
differs from it only by rounding. E7's `DynamicsModel` owns step 7: it
resolves every `DynamicsSpec` key once at construction (an unknown key is a
`KeyError`, an unknown kind a `ValueError`) and `step(country, global_,
dyn_z)` applies the two phases to the caller's state in place, after
`ImpactLedger.apply` and before `MemoryModel.end_of_year`, checking the state's
dtype and shape and `dyn_z`'s shape (`[R, len(noisy_keys)]`) loudly. It
iterates entries in declaration order, one `(R,)` operation per entry, so it
reproduces the reference's arithmetic element for element; it never regroups
entries by kind, since phase-2 order matters when a `gdp_stock`'s growth
variable is itself a drift target. E8's `simulate` owns nothing of the
semantics: it wires the modules above in the pinned order ("Year step"),
holds the block's state in a `StateTensor` (`state.py`, with `resolve_key`
for `"entity.var"` / `"global_var"` keys and `bind_names` for an expression
namespace over the current state), and records (`"Recording"`). It is the
year loop that `test_oracle_diff.py`'s `_step`/`_diff_own_state` ran in test
form, promoted, not re-derived.

**Draws** (guide §4.6). One `SeedSequence(master_seed)`, one child per block
of `block_size` runs; within a block, `t2_offset` once, then per year
`factor, idio, res_u, branch_u, impact_z, dyn_z`. Resolution and branch
uniforms are drawn for every event (every event has at least the implicit
`default` outcome). Results depend on `(master_seed, block_size)` and nothing
else. The reference engine replays run *r* by generating block `r //
block_size` at full width and consuming row `r % block_size`.

**Dynamics** (both engines; step 7): mean-reverting variables update first (`x += θ(μ − x) + σ z`, `θ = 1 −
0.5^(1/half_life)`, one `dyn_z` column per mean-reverting variable in
declaration order, drawn even when σ = 0); then, in declaration order,
`gdp_stock` variables compound by their growth rate as updated so far (growth
in % per year) and additive and multiplicative drifts apply. θ is the exact one-year discretization of the OU
process, so a σ = 0 displacement `d` is exactly `d · 0.5^(k/h)` after `k`
years and "half-life" means what it means in the shock schedule's `decay:`
rows (§4, item 18). σ is the standard deviation of the one-year innovation,
not of the stationary distribution (which is `σ / sqrt(θ(2 − θ))`, ≈ 1.41σ at
h = 2). `VarDynamics` rejects a `mean_revert` `half_life` that is not finite
and > 0 and any `sigma < 0`, and `DynamicsSpec` rejects duplicate keys (entries
apply sequentially and a repeated mean-revert key would map to its last
`dyn_z` column), each with a `ValueError` naming the key. Phase 1 (every
mean-reverting entry) completes before phase 2, which applies `gdp_stock`,
`additive` and `multiplicative` entries in declaration order, so a stock
reads its growth variable after a drift on it declared earlier and before
one declared later. Keys resolve as for expressions (`"global_var"` or
`"entity.var"`). Nothing is clamped: a stock compounded by growth ≤ −100 goes
to zero or changes sign. The oil/food → inflation transmission of MVP scope
§5.1 step 6 is deferred to stage E7b (§4, item 19).

**Recording** (ADR-9; `RecordingSpec` in `sim/reference/model.py`, beside
`SimParams` and `DynamicsSpec`, §4 item 21). A `ScenarioFlag(name, condition,
min_years)` is an expression compiled by the catalog's expression compiler
with `allow_event_state=False`, so its names are validated against the state
catalog and it may read factors and state variables only: `resolution`,
`branch` and `years_since` are rejected at compile time and again by
`ScenarioFlag` itself, because a flag describes an outcome, not firing
mechanics (a flag about firings is an event-log query at E9). Both engines
evaluate every flag in step 9 on **end-of-year** state (after step 8) with
that year's factor draw, keep a per-run consecutive counter (+1 while the
condition holds, reset to 0 the year it fails, ADR-5's machinery) and set the
flag, which then stays set, in the first year the counter reaches `min_years`.
Recorded state is end-of-year state, so a flag's cross-run frequency equals a
direct count over recorded trajectories (E9's gate). `RecordingSpec` also
names the `thin_keys` (state keys `"entity.var"` / `"global_var"` kept
annually for every run) and `n_full` (the runs with the lowest global indices
that keep full trajectories); it defaults to nothing, so fixtures run without
it, and rejects a duplicate flag name or thin key, `min_years < 1` or `n_full
< 0` with a `ValueError` naming the offender. The reference's `RunRecord`
carries `scenario_flags` (bool `[n_flags]`); its full `country`/`global_`
trajectories already contain every thin key. No real flag definitions exist
yet: an owner/data-track item (§4, item 23). `simulate` returns `RunOutputs`,
in-memory arrays only (§4, item 21): terminal `country [R, N_ent, N_cvar]`
and `global_ [R, N_gvar]`; `factors float64 [R, K, T]`; `thin float64 [R,
n_thin, T+1]` and `full_country [n_full, T+1, N_ent, N_cvar]` /
`full_global [n_full, T+1, N_gvar]` for runs `0 … n_full − 1`, index 0 the
initial conditions and `t + 1` the end of `years[t]`; `scenario_flags bool
[R, n_flags]` in `RecordingSpec` order; `max_active_seen int64 [R]` (peak
live shocks, as the reference counts it); `years int64 [T]`; and an
`EventLog` of columns `run, year, event, resolution, branch, p_base, p_eff,
cascade_mask`, one row per firing ordered by `(run, year, event)`, with a
magnitudes table `(mag_firing, mag_row, mag_M)` in log order and
`impact_table` row order within a firing — the reference's `EventFiring`
list, columnar. Flags are evaluated per block on a namespace `bind_names`
builds afresh from end-of-year state (step 2's namespace holds views that
have been mutated by then, and only the catalog's names). `n_full > R`,
`R < 1` and initial conditions off the catalog's axes are `ValueError`s;
an unknown thin key or flag name is a `KeyError` before any year runs.
Serialization and the State Outputs §8.4 statistics are E9/E10.

**Partial catalogs.** A cascade edge whose target exists in `events/` but is
not yet migrated is dropped with a recorded warning when `strict_cascades` is
off (fixture and per-event compiles) and is an error when it is on (the
full-catalog gate). A target that exists nowhere is always an error.

**Durability forms.** `decay: N`, `permanent: true`, `until: resolved`, and
`durability: {type: decaying, half_life: N}` compile. `until:
policy_change`, decay-to-floor, maintenance and the other full forms are
schema v0.2 backlog and are rejected with a message saying so.

## 4. Findings from the build (for the data track and the spec owners)

Found by compiling the five migrated events. None is patched here
(guardrail 2): each is either a data-track item or a decision for the spec.

1. **Type 2 pressure scale mismatch** — *resolved 2026-10-12.* AMOC's and
   Pakistan's pressure expressions were weighted sums of terms in [0, 1]
   while `threshold` is on a 0–100 scale, so AMOC's pressure at the 2025
   baselines (0.325) pinned the event at its floor. The schema now states
   that pressure shares `threshold`'s scale, both expressions are wrapped in
   `100 * (...)`, and the compiler checks the value at the baselines (§3,
   "Firing"). The probability-estimation doc's worked numbers remain
   inconsistent with its formula (§3); the formula is unchanged.
2. **`until: resolved` has no defined end** — *resolved 2026-10-12.* The
   schema now requires `probability.resolves_after: N` on any event with an
   `until: resolved` row (Taiwan 3, severe pandemic 3, Pakistan 5, each with
   a one-line rationale in the event), the compiler rejects such an event
   without it, and `CompiledCatalog.resolves_after` (`int64 [E]`) replaces
   the engine parameter. Spec owners: the guide's §4.1 contract table should
   list this field; it is not changed from here (guardrail 2).
3. **Pakistan references names outside the state catalog** — *resolved
   2026-10-12 (D1).* Renamed to `pak.refugees_abroad` / `ind.refugees_hosted`;
   the `afg` row is dropped (Afghanistan is in no aggregate) and the gap is
   recorded in `events/backlog-registry.md` §5.
4. **`confidence` enum** — *resolved 2026-10-12 (D1).* The YAML uses `medium`
   (severe pandemic) and `low` (fusion); the original wording stays in prose.
5. **Impact units are implicit** — *resolved 2026-10-12 (D1).* The schema now
   states that `gdp_real` impacts are fractions of the entity's current value
   and everything else is additive; the compiler tags such rows
   `multiplicative` (a twelfth `impact_table` column, beyond the guide's §4.1
   row layout — spec owners, see item 2) and both engines apply them by ratio
   (§3, "Shock schedule").
6. **Variance tolerance** is unspecified; the compiler uses ±0.02 against the
   declared `variance:` field (Taiwan achieves 0.4537 vs 0.45, AMOC 0.6557
   vs 0.65).
7. **Entity/variable axes.** The compiler validates against the full state
   catalogs (66 country × 52 entity, 42 global), which is what rule 3 says and
   what Taiwan needs (`chn.sanctions_level` is outside the MVP ~18-variable
   list). Which variables carry *dynamics* in v0.1 is the MVP scope's
   business (E7); which exist in the tensor is the catalog's. The guide's
   "~18 variables" should be read as the former.
8. **Re-firing** of an event that is already active is allowed and additive;
   no document says otherwise.
9. **A fractional impact below −100%.** Taiwan's `military_conflict.nuclear`
   branch scales `twn.gdp_real [-0.40, 0.15]` by 3.0 to a mean of −1.2, which
   a multiplicative row cannot apply (the state would go negative). The
   compiler records a `WARNING` note for any multiplicative row with mean ≤
   −1 and the engines fail the run loudly when a drawn contribution is ≤ −1;
   with std 0.45 the draw lands at or below −1 about two-thirds of the time
   this branch fires. Data-track item: cap the scaled fraction, split the
   nuclear branch's GDP row out of `inherit`, or re-express it. The same
   shape recurs in the fan-out: Egypt's catastrophic branch was capped at
   −0.70 at migration, Sahel's branches were written explicitly instead of
   the 2.5×/5× multipliers, both recorded in the files' changelogs.

Surfaced by the 24-event migration fan-out (2026-10-12), each also recorded
in the file's changelog row:

10. **`US_CONSTITUTIONAL_CRISIS` fails the variance gate** — *resolved
    2026-10-22.* Its documented loadings achieved 0.409 against the declared
    hybrid target 0.55 because the file's "scale factor 0.89 from original
    loadings" had been applied in the wrong direction: the originals already
    explained 0.516, below the target. The migration multiplies the originals
    by 1.03 (achieved 0.558), keeps the target, and records both prior
    loading sets in the event's Factor Loadings section. With it landed the
    full-catalog strict compile passes with no dropped edges.
11. **Sharpness convention is mixed.** `sharpness` is applied per point of
    the 0–100 pressure scale (§3). AMOC and Pakistan use 0.15–0.20; the EU,
    Chinese political, Chinese economic, dollar-reserve and US-constitutional
    events document 8–15, which on this scale is a step at the drawn
    threshold: with pressure below threshold their annual probability is
    exactly the floor. Values were written as documented; one migration had
    rescaled 8 to 0.08 and was reverted before commit so the convention is
    decided once, here, not per file.
12. **Unit convention for `unemployment_rate` and the index variables.** The
    catalog gives `unemployment_rate` as "% of labor force" and
    `global_trade_volume`, `semiconductor_supply` as indices (2025 = 100).
    The January migrations (Taiwan, pandemic, Pakistan) wrote these as
    fractions (−0.15, 0.04); the October migrations wrote points (−15, +4),
    following the catalog. The three early files should be re-expressed, or
    the schema should list which variables are fractional (today only
    `gdp_real`).
13. **`nuclear_status` is categorical with no encoding.** Saudi nuclear
    acquisition's preconditions read `irn.nuclear_status` as an ordinal
    (NONE 0, THRESHOLD 1, POSSESSED 2); the catalog records "Categorical"
    and nothing else. The encoding needs to be stated in the state catalog
    or the variable made numeric.
14. **Rows exceeding their variable's range.** Permafrost's catastrophic
    `permafrost_integrity` −100 on a 0–100 variable at 90; Amazon's
    `bra.agricultural_climate_risk` +120 and `bra.water_stress` +80; Egypt
    and Pakistan's scaled `internal_conflict_intensity` (0–4) and
    `unemployment_rate` branches. The engine does not clip (guardrail 4), so
    these produce out-of-range state. Data-track review item.
15. **Cross-file `triggered_by` deltas disagree with the source's
    `triggers`** (Pakistan lists India–Pakistan at +0.030, the source writes
    +0.012; several events' `triggered_by` lists omit edges other files
    declare). `triggered_by` is informational (§3), so nothing is wrong in
    the engine, but the tables should be reconciled once.
16. **Pressure expressions versus prose estimates.** Where a prose "current
    pressure ~N" exists, the realized expression gives: AMOC 32.5 vs 45,
    Amazon ~43 vs 58, Permafrost 28 vs 50, Chinese political ~17 vs 35–40,
    Saudi regime ~12 vs 25, Russia ~66 vs 55, Iran nuclear 68 vs 50; the
    rest agree within a few points. Each file notes its own gap. Combined
    with item 11, several Type 2 events sit at their floor at the 2025
    baselines.
17. **`EU_COHESION_STRESS`** (Sahel cascade table) is in no registry
    section; registry §5 asks for a disposition.

Found at E7 (spec-owner review delegated by the project owner, 2026-10-23):

18. **Mean-reversion half-life convention** — *resolved 2026-10-23.* MVP
    scope §3.1 and §5.1 and State Dynamics §4 gave θ = ln 2/τ, the relation
    for the continuous OU process `dX = θ(μ − X)dt + σ dW`. Applied as an
    annual Euler step it shrinks a displacement by (1 − θ) per year, so the
    realized half-life is ln 0.5 / ln(1 − θ): 0.587 y at h = 1 (41% short),
    1.629 y at h = 2, 2.638 y at h = 3; and for h < ln 2 θ exceeds 1 and the
    step overshoots. The guide's E7 gate ("recovers with specified
    half-life") could not pass as worded. Both engines now use the exact
    one-year discretization θ = 1 − 0.5^(1/h) (h = 1 → 0.5; h = 2 →
    0.2928932…; h = 3 → 0.2062995…), which lies in (0, 1) for every h > 0
    and matches the shock schedule's `0.5^(age/h)`. σ is unchanged in
    meaning: the one-year innovation sd, which is how D4 must read MVP §3.3's
    "Default σ (annual)". The change was cheap only now: D4 has not started
    and no data uses dynamics half-lives. Amended: `sim/reference/engine.py`
    step 7, `sim/reference/model.py` (docstring and validation, §3
    "Dynamics"), FIX-A's hand trace, MVP Dynamics Scope §3.1, §3.3, §5.1 and
    its Document History (1.1), State Dynamics §4.
19. **Oil/food → inflation transmission** — *deferred to E7b, 2026-10-23.*
    MVP scope §5.1 step 6 (`inflation = f(oil, food, import_dependence)`) is
    not built at E7, for four reasons. (1) *The formula does not exist.*
    State Transmission §3.1 gives only `Δinflation = passthrough × Δsource`
    with passthrough left unspecified; §7.1 says the coefficients need
    empirical estimation and §8.2 recommends lagged values without pinning
    them. Task 4.5 was closed because those documents described the channel,
    but they do not parameterize it, and engine-side coefficients would be
    invented numbers that become de facto defaults (guardrail 3). (2) *It
    would double count today.* `events/energy/Oil Supply Shock.md` shocks
    both `oil_brent` and `*.inflation_rate` in the same branches, and its
    migration table says that once the passthrough exists "these rows and
    the passthrough overlap and one must give way"; other events also shock
    `inflation_rate` directly. State Transmission §8.1 forbids shocking both
    a source and its dependent, and fixing that means editing `events/`,
    which the engine track may not do. (3) *Exporters are unspecified.*
    Import dependence is "% of consumption", negative for net exporters
    (State Variables – Country §3), so a linear rule would give exporters
    deflation from an oil spike, which §3.1's exporter table does not say.
    (4) *Nothing gates on it.* Neither the E7 gate nor the five success
    criteria of MVP §8 need it, and MVP §5.3 already says v0.1 cannot
    validate transmission realism.
    **Seam:** architecture §3 puts transmission last in step 7, so E7b is a
    phase 3 appended to step 7, added to the reference first and then
    transcribed.
    **Proposal handed to D4 (a proposal, not a pin; not implemented):**
    `inflation_rate_i += κ_oil · max(dep_energy_i, 0)/100 · (oil_{t−1} −
    oil_{t−2}) / 75 + κ_food · max(dep_food_i, 0)/100 · (wheat_{t−1} −
    wheat_{t−2}) / 6`, using fully lagged recorded state and giving
    exporters zero; the increment then decays through `inflation_rate`'s own
    reversion. calibration-anchors gives that pass-through a half-life of ~1
    year while MVP §3.1 gives `inflation_rate` 2 years; D4 picks one. D4 also
    supplies κ_oil, κ_food, the exporter rule and the list of direct
    `inflation_rate` event rows to retire (Task 4.4, which absorbs reopened
    4.5).
20. **GDP is carried by `gdp_real`; `gdp_per_capita` is derived post-run** —
    *decided 2026-10-23 (spec-owner review delegated by the project owner).*
    The finding: 893 impact rows from 24 events shock `gdp_real` (fractions
    of current value), none shock `gdp_per_capita`, and MVP scope's progress
    engine compounds only `gdp_per_capita` (520 `gdp_growth` rows from 14
    events reach it through growth). No rule links the two stocks, so a
    level shock such as Taiwan's −40% landed on a variable with no dynamics
    and was invisible to the progress engine. No expression in `events/`
    reads either variable, so the choice has no firing-side effect.
    **Decision.** In v0.1 the GDP stock is `gdp_real`: D4 declares it as the
    `gdp_stock` entry with `growth_key: gdp_growth` for every dynamics
    entity, so level shocks (step 6) and compounding (step 7) act on one
    variable, in the order the engines already use. `gdp_per_capita` gets no
    dynamics entry and no event rows; it is a D3 2025 baseline, and its
    trajectory is derived in `analysis/` (E9) as `gdp_per_capita(0) ·
    [gdp_real(t) / gdp_real(0)] · [pop_total(0) / pop_total(t)]`, i.e. by
    relative change, which keeps D3's own per-capita definition and reduces
    to the plain GDP ratio while population is static. MVP §2.1's per-capita trend growth is read
    as `gdp_growth`'s equilibrium μ, as E7 already reads it. State Outputs
    §4.1's "GDP" thin trajectories record `gdp_real`.
    **Why.** (a) The multiplicative machinery is defined on `gdp_real`
    (event-yaml-schema §Impact Fields "Units"; `test_e2_compiler.py`
    asserts multiplicative ⇔ `gdp_real`), and State Outputs §3.2 defines
    `gdp_change` on it: moving 893 rows the other way is maximal churn for
    nothing. (b) The data track already reads it this way:
    `us-constitutional-crisis.md`'s migration table converted
    `usa.gdp_per_capita −10%` to `usa.gdp_real −0.10` because "per-capita
    and aggregate real GDP coincide absent a population change". Per capita
    is aggregate over population, so carrying the aggregate and deriving the
    ratio loses nothing. (Correction, same day: the review first said
    population dynamics are out of MVP scope; MVP §2.4 says cohorts evolve
    in v0.1, but no engine stage builds that. See item 22. The decision
    stands on (a), (c)–(e); the derivation above is exact either way.) (c) It is the only option that puts GDP shocks
    and growth on one variable, which MVP §8's criteria need; the ratio
    shock schedule (§3) returns the state to its no-shock path as the
    contribution decays, so it composes with compounding by design.
    (d) Guardrail 3: it removes a process (per-capita as state) rather than
    inventing one. (e) Cost: one D4 dynamics choice plus spec sentences,
    versus 893 event rows or a new engine coupling rule.
    **Follow-up.** Spec: MVP Dynamics Scope §2.1 (baseline and trend rows
    name `gdp_real`; `gdp_per_capita` stays a 2025 baseline), §5.1 step 4
    and its implementation note (`gdp_real(t) = gdp_real(t−1) · (1 +
    gdp_growth(t)/100)`), Document History; State Outputs §3.2 defining the
    derived per-capita series (both made 2026-10-23:
    MVP scope 1.2, State Outputs 1.1, with the D3 count in the guide and
    `tasks.md` 4.3 updated from ~196 to ~242). D3: 2025 baselines for
    both. D4: `gdp_stock` on `gdp_real` only. E9: the per-capita
    derivation, used by State Outputs §6 assessments that read
    `gdp_per_capita`. While no stage computes `pop_total` (item 22), E9
    must treat population as static and say so in its output.
    FIX-A's `gdp_per_capita` stock is fixture-internal and stays. Does not
    block E8 (fixtures plus a thin-key choice); it bites at D4 and E10.
21. **`simulate()` takes dynamics and recording config; `years` lives in
    `SimParams`** — *decided 2026-10-23 (same review; frozen seam, guide
    §4.5, edit authorized by the owner, to be made at E8).* Guide §4.5's
    `simulate(catalog, initial_conditions, params, R, seed, years=50)` has no
    `DynamicsSpec`, which every run needs, and repeats the horizon
    `SimParams` already carries. E8 implements `simulate(catalog,
    initial_conditions, dynamics, params, R, seed, recording=RecordingSpec())
    -> RunOutputs`. `dynamics` is the third positional, mirroring
    `simulate_reference`. `years=` is dropped, because two sources for the
    horizon invite silent disagreement (guardrail 4), and `SimParams` stays
    the single source for `years`, `start_year`, `max_active`,
    `epsilon_cull` and `block_size`. `RecordingSpec` lives in
    `sim/reference/model.py` beside the other shared contract types:
    `scenario_flags` (`ScenarioFlag(name, condition, min_years)`, ADR-9's
    "config, not code" on ADR-5's counter machinery), `thin_keys` (state
    keys) and `n_full` (runs with full trajectories, ADR-9's subset). It
    defaults to empty and 0, so fixtures run without it. The production list
    is data, loaded by `run.py` at E9: State Outputs §4.1 with GDP =
    `gdp_real` (item 20). No scenario-flag definitions exist yet: that is an
    owner/data-track item. `R` and `seed` stay separate arguments; the
    reference takes `draws, run_indices` because the oracle diff drives it,
    and that asymmetry is intended. §4.5's `RunOutputs` becomes in-memory
    arrays:
    - terminal state;
    - columnar event log with provenance;
    - `factors [R, K, T]`;
    - `scenario_flags bool [R, n_flags]`;
    - `thin [R, n_thin, T+1]`;
    - full trajectories for the first `n_full` runs;
    - `max_active_seen`;
    - the year axis.

    Two parts of §4.5 move to E9/E10, because neither is a semantics seam
    and keeping them out keeps E8 oracle-diffable: Parquet/JSON
    serialization moves to `run.py` (E9), and the State Outputs §8.4
    validation statistics, which are cross-run analyses of what E8 records,
    move to E9/E10. ADR-9 and architecture §3 need no edit.
22. **Population dynamics are specified for v0.1 but built by no stage** —
    *open, owner decision (found 2026-10-23).* MVP Dynamics Scope §2.4 says
    that in v0.1 the 12 population cohorts per country evolve by aging,
    mortality (from `life_expectancy`), fertility (`tfr`) and migration, per
    State Dynamics §3, and MVP §8's success criteria check for "no negative
    populations". But no row of guide §3 (E7 is drift and mean reversion),
    no task in `tasks.md`, the architecture and this README mention cohort
    mechanics. The state catalog's `pop_total` and `pop_working_age` are
    `derived: true`, and nothing computes derived variables. Until this is
    decided, population is static in both engines, which is what the
    per-capita derivation of item 20 falls back to. The choice is between
    a stage for cohort mechanics (with derived-variable computation)
    before E10, and an MVP scope amendment deferring population dynamics
    from v0.1.

Found at E8 (2026-10-23):

23. **No scenario-flag definitions exist.** `ScenarioFlag` (§3 "Recording")
    is the mechanism; nothing in the repository declares a flag. State
    Outputs §7.2's scenario table is prose, and most of its rows are not
    expressible as a flag over factors and state variables: "US severe
    decline" reads a per-capita change against a baseline (a derived
    quantity, item 20), "Great power war" and "Multi-state collapse" count
    firings (event-log queries at E9), "Chinese political crisis" and
    "European fragmentation" read §5 assessments, which are computed post-run
    and never during simulation (ADR-9). The rows that are expressible
    ("Dollar displacement": `usd_reserve_share < 40`; "Climate tipping point"
    partly, via `amoc_strength` / `amazon_forest_cover` thresholds) need a
    `min_years` each. Owner/data-track item: author the flag list as data
    (expression + `min_years`), loaded by `run.py` at E9 with the thin-key
    list; the engine takes whatever it is given.
24. **`n_full` memory at the real axis sizes.** The state catalog is 52
    entities × 77 country variables + 42 globals = 4,046 floats per year, so
    `n_full = 1000` over 50 years is 1000 × 51 × 4,046 × 8 B ≈ 1.65 GB of
    full trajectories in memory (the 1.42 GB figure in the E8 brief assumed
    66 country variables). E8 enforces nothing about it; E9's production
    default must take it into account (ADR-9 prefers widening the thin list
    over deepening the subset).
25. **The smoke's inputs** (`test_e8_simulation.py`, opt-in via
    `SIM2075_SMOKE=1`). The catalog is every migrated event compiled with
    `strict_cascades=False` minus the events whose compile notes carry the
    multiplicative "mean ≤ −1" WARNING, derived from the notes and asserted
    to be exactly `TAIWAN_CONFLICT` (item 9); dropping it drops 8 cascade
    edges into it (from `CHINESE_ECONOMIC_CRISIS` 1, `CHINESE_POLITICAL_CRISIS`
    4, `KOREAN_PENINSULA_CRISIS` 1, `US_CONSTITUTIONAL_CRISIS` 2), leaving 28
    events, 3,818 impact rows and 110 edges. Initial conditions are each
    global's `baseline_2025` (every global has one) and 0 for every country
    variable (none has one), so `gdp_real` starts at 0 and the smoke measures
    cost, not realism. The dynamics are built inside the test and never
    written under `sim/data/`: for every country, MVP §3 class defaults
    (`gdp_growth` h 2 σ 2, `inflation_rate` h 2 σ 2 μ 2, `unemployment_rate`
    h 3 σ 1 μ 5), a `gdp_stock` on `gdp_real` with `growth_key: gdp_growth`
    (item 20) and `life_expectancy` +0.2/yr; and the six §2.2 global trends,
    additive or multiplicative as §2.2 states them. §3.2 gives `gdp_growth`
    no tier value (its equilibrium is the country's Tier 1 trend, D3's), so
    the smoke uses 2 %/yr; D4 supplies the real one.
26. **The smoke raises on the data, twice, before the loop's cost can be
    measured** (E8-D5: a data finding, reported, not patched; nothing was
    clamped, caught, reseeded or edited).
    - *`LedgerOverflow` in 2025, the first year, at the pinned width.* Block
      0 (runs 0–1023, seed 20261023) raises `LedgerOverflow` for runs
      `[59, 77, 115, 137, 148, 182, 232, 375, 377, 413, 460, 464, 476, 621,
      728, 742, 751, 760, 804, 837, 869, 874, 949, 954, 962, 1005]`, year
      2025, 529 live shocks > `max_active = 256`. Cause: wildcard impact rows
      expand to one row per country (40), so one branch of
      `GLOBAL_FINANCIAL_CRISIS` pushes 202 slot-taking shocks,
      `OIL_SUPPLY_SHOCK` 163, `SEVERE_PANDEMIC` 163, `US_CHINA_ECONOMIC_RUPTURE`
      107; two or three of these in one year exceed 256, and they are
      Type 1/2 events with non-trivial annual probabilities. Pinned decision
      #3 said "revisit width after fixture pilots"; this is that pilot. The
      width is a `SimParams` field (the slot arrays cost ≈ 50 B per slot per
      run: 1024 slots × 1024 runs ≈ 50 MB per block), so widening is cheap;
      alternatively the data track can author the wide rows differently. A
      spec-owner decision.
    - *`ImpactOutOfRange` in 2026 with the ledger widened to 1024* (a
      diagnostic run, not the gate): runs `[232, 625]`, year 2026,
      `impact_table` row 2772 = `RUSSIA_STATE_FAILURE` branch
      `catastrophic_collapse`, `rus.gdp_real` mean −0.70 std 0.35, gradual
      onset 2, decay 8: the drawn M = −1.21875 (z ≈ −1.48) reaches the state
      at age 1 when the ramp completes. That row draws M ≤ −1 whenever
      z ≤ −0.857, about 20% of its firings; 11 multiplicative rows across
      `EGYPT_STATE_FAILURE`, `IRAN_REGIME_CHANGE`, `KOREAN_PENINSULA_CRISIS`,
      `PAKISTAN_STATE_FAILURE`, `RUSSIA_STATE_FAILURE`, `SAHEL_CATASTROPHE` and
      `TURKEY_POLITICAL_BREAKDOWN` can reach −1 within 3σ. Same shape as item
      9 (there the mean itself is below −1); data-track item: cap, truncate
      or re-express the fractional rows' spread.
    - *Cost, from what did run* (4 CPUs, x86_64, Python 3.13, NumPy 2.5;
      not the gate's number, which does not exist until the data runs). Even
      one year does not complete over all ten blocks (block 4, run 4157,
      2025: row 2899 = `TURKEY_POLITICAL_BREAKDOWN` / `earthquake_cascade`,
      `tur.gdp_real` mean −0.6 std 0.3, M = −1.22), so the sample is blocks
      0–3 (R = 4,096, whose draws are the smoke's: a `SeedSequence` child
      does not depend on the number of blocks) over 2025 at `max_active`
      1024: 3.09 s, 0.77 s per block-year, of which the §4.6 draws 0.23 s
      (`impact_z` is `[1024, 3,782]` normals every year), `ImpactLedger.resolve`
      0.23 s (the `[R, n_rows]` selection and magnitudes), `ImpactLedger.apply`
      0.15 s (587 firings per block in 2025 push ~60,000 shocks, wildcard
      rows again), state initialisation 0.12 s per block, everything else
      under 0.03 s. Projected over 500 block-years that is ≈ 310–390 s, five
      to six times the 60 s requirement, and a lower bound (the ledger is
      empty in year 0). Where the time goes is the outcome-independent
      `[R, n_impact_rows]` draw and selection the §4.6 contract mandates, and
      a ledger carrying hundreds of live shocks per run. Nothing was
      optimized at E8; the reading is that the data (wildcard fan-out), not
      the loop's structure, sets the cost, and the spec owners should see
      these numbers before any optimization beyond plain NumPy is considered.


## 5. License

Code under `sim/`: BSD-2-Clause (`LICENSE`). Catalog, methodology and other
prose: CC BY 4.0.
