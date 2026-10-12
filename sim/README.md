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
| — | §5.2 oracle diff, `sim/tests/test_oracle_diff.py`: FIX-A/FIX-B at R=64 under `SeededDraws` | F and U every year; `p_base`, gate, fire mask in year 0 — grows with each stage | in suite |
| E5–E10 | memory, impacts, dynamics, year loop, analysis | per guide §3 | not started |

```
pip install -e ".[test]"
pytest                               # the stage gates
python -m sim.catalog.cli events     # compile report for every migrated event
```

## 2. Layout

```
sim/
├── catalog/      compile layer (ADR-7): extract.py · schema.py · expr.py · compile.py · cli.py
├── reference/    scalar reference engine (ADR-1): model.py (inputs) · engine.py (the year step)
├── rng.py        draw schedule contract (guide §4.6), shared by both engines
├── data/         state_catalog.yaml (generated from the markdown catalogs) · omega.yaml (Ω, transcribed)
├── engine/       vectorized runtime: factors.py (E3) · firing.py (E4) · E5+ pending
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
draw.

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

**Vectorized modules** (E3, E4) consume whole §4.6 blocks and reproduce
the reference's steps 1–4 for every run of the block: `FactorModel.year`
gives `F = z Lᵀ` and `U = Φ(F Λᵀ + σ_idio ε)`; `FiringModel.thresholds`
takes the init-time `t2_offset` block; `FiringModel.base` evaluates the §4.3
callables once over `(R,)` views (namespace from `namespace_from_state`
plus per-event `resolution`/`branch`/`years_since` columns of an
`EventState`) and returns `p_base`, the Type 3 gate and this year's sustained
evaluations for step 8; `FiringModel.fire` is `gate & (U < p_eff)`. Type 2
uses `scipy.special.expit`, which agrees with the reference's `1/(1+e^{−x})`
to rounding (the oracle diff's rtol 1e-9 covers it). Per-run memory
(`EventState`, sustained counters, cascade deltas) is read here and will be
owned by E5.

**Draws** (guide §4.6). One `SeedSequence(master_seed)`, one child per block
of `block_size` runs; within a block, `t2_offset` once, then per year
`factor, idio, res_u, branch_u, impact_z, dyn_z`. Resolution and branch
uniforms are drawn for every event (every event has at least the implicit
`default` outcome). Results depend on `(master_seed, block_size)` and nothing
else. The reference engine replays run *r* by generating block `r //
block_size` at full width and consuming row `r % block_size`.

**Dynamics** (reference engine, pending E7 for the vectorized engine):
mean-reverting variables update first (`x += θ(μ − x) + σ z`, `θ = ln 2 /
half_life`, one `dyn_z` column per mean-reverting variable in declaration
order, drawn even when σ = 0), then `gdp_stock` variables compound by the
updated growth rate (growth in % per year), then additive and multiplicative
drifts. The oil/food → inflation transmission of MVP scope §5.1 step 6 is not
yet implemented (E7).

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
   nuclear branch's GDP row out of `inherit`, or re-express it.

## 5. License

Code under `sim/`: BSD-2-Clause (`LICENSE`). Catalog, methodology and other
prose: CC BY 4.0.
