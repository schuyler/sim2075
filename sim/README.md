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
| E3–E10 | vectorized engine, dynamics, analysis | per guide §3 | not started |

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
├── engine/       vectorized runtime — E3+ (empty)
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
this is the probability-estimation logistic with ceiling 1). Type 3
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
is drawn at firing. `permanent` + `immediate` folds into state at firing and
takes no slot; `permanent` with a ramp holds a slot until the ramp completes,
then is freed. A decaying shock is epsilon-culled when `|contribution| <
1e-4 · |M|`: its remaining contribution is returned exactly to zero and the
slot freed. More than `max_active` slots is a `LedgerOverflow` naming the run
and year.

**`until: resolved`** (open question, §4): a firing sets the event active for
`SimParams.until_resolved_years` years including the firing year; the flag
is cleared in step 8 of the last active year and the shock's contribution
drops to zero the year after. Re-firing while active extends the window and
pushes additional shocks. `until_resolved_years` has no default on purpose.

**Expressions.** `years_since` is `year − last_fire_year`, a very large
number for an event that has never fired. `branch` names usable in
expressions must be unique across the event's resolutions. Multi-line YAML
block scalars are parsed as one parenthesized expression.

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

1. **Type 2 pressure scale mismatch.** AMOC's and Pakistan's pressure
   expressions are weighted sums of terms in [0, 1] (prose: "~45/100"), but
   `threshold` is on a 0–100 scale (65 and 70). Evaluated at the 2025
   baselines AMOC's pressure is 0.325, so `σ(0.15 · (0.325 − 65))` pins the
   event at its floor forever (implied annual p = 0.00206, not the documented
   1.0%). Either the expressions gain a `100 *` or the schema states the
   expression scale; the compiler cannot tell which is intended.
   Separately, `probability-estimation.md`'s own worked numbers for the
   logistic (p ≈ 1% at pressure 45) do not follow from its formula (≈ 4.9%).
2. **`until: resolved` has no defined end.** No field in the schema and no
   sentence in the ADRs says when an event "resolves". The engine takes a
   required `until_resolved_years` parameter until the spec decides
   (candidates: a per-event field, a per-resolution duration, or a drawn
   duration, which would add a draw category to §4.6).
3. **Pakistan references names outside the state catalog**:
   `pak.refugee_outflow`, `ind.refugee_inflow` (the catalog has
   `refugees_abroad` / `refugees_hosted`) and entity `afg`, which is not one of
   the 40 countries. Task 4.2 remediation item.
4. **`confidence` enum.** `severe-pandemic` (`medium-high`) and
   `fusion-commercialization` (`low-medium`) use values outside
   `low|medium|high`. Either the events or the enum should change; the
   compiler enforces the schema as written.
5. **Impact units are implicit.** `twn.gdp_real mag [-0.40, 0.15]` reads as
   −40%, `global_credit_spread mag [200, 80]` as +200 bps, both applied
   additively in the variable's units by every document that describes shock
   application. The data track should confirm that `gdp_real` impacts are
   meant as fractions and, if so, whether the catalog's `gdp_real` unit ($T)
   or the schema should change.
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

## 5. License

Code under `sim/`: BSD-2-Clause (`LICENSE`). Catalog, methodology and other
prose: CC BY 4.0.
