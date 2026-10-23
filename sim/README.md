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
| — | §5.2 oracle diff, `sim/tests/test_oracle_diff.py`: FIX-A/FIX-B at R=64 under `SeededDraws` | F and U every year; every year from the reference's recorded state: `p_eff`, gate, fire mask, resolution/branch codes, cascade bitmask, sustained counters, impact magnitudes, `until: resolved` flags, live ledger; dynamics-free mode (both engines `DynamicsSpec([])`, own state from initial conditions, plus FIX-B's scripted draws with `x.stress` 2.0, and test-built ramped-onset, long-horizon, `until: resolved` re-firing and small-`max_active` variants): full state trajectory (rtol 1e-9), exact event log, `LedgerOverflow` runs and year, `ImpactOutOfRange` runs, year, row and contribution — grows with each stage | in suite |
| E7–E10 | dynamics, year loop, analysis | per guide §3 | not started |

Data track (guide §2): D1 and D2 done — all 29 events compile and the
full-catalog gate (`strict_cascades` on) is green with no dropped edges
(2026-10-22, after `US_CONSTITUTIONAL_CRISIS` landed; §4 item 10). D3 and
D4 (initial conditions, dynamics defaults) are not started.

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
├── engine/       vectorized runtime: factors.py (E3) · firing.py (E4) · memory.py (E5) · impacts.py (E6) · E7+ pending
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

**Vectorized modules** (E3–E6) consume whole §4.6 blocks and reproduce
the reference's steps 1–6 and 8 for every run of the block: `FactorModel.year`
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
differs from it only by rounding.

**Draws** (guide §4.6). One `SeedSequence(master_seed)`, one child per block
of `block_size` runs; within a block, `t2_offset` once, then per year
`factor, idio, res_u, branch_u, impact_z, dyn_z`. Resolution and branch
uniforms are drawn for every event (every event has at least the implicit
`default` outcome). Results depend on `(master_seed, block_size)` and nothing
else. The reference engine replays run *r* by generating block `r //
block_size` at full width and consuming row `r % block_size`.

**Dynamics** (reference engine, pending E7 for the vectorized engine):
mean-reverting variables update first (`x += θ(μ − x) + σ z`, `θ = 1 −
0.5^(1/half_life)`, one `dyn_z` column per mean-reverting variable in
declaration order, drawn even when σ = 0), then `gdp_stock` variables
compound by the updated growth rate (growth in % per year), then additive and
multiplicative drifts. θ is the exact one-year discretization of the OU
process, so a σ = 0 displacement `d` is exactly `d · 0.5^(k/h)` after `k`
years and "half-life" means what it means in the shock schedule's `decay:`
rows (§4, item 18). σ is the standard deviation of the one-year innovation,
not of the stationary distribution (which is `σ / sqrt(θ(2 − θ))`, ≈ 1.41σ at
h = 2). `VarDynamics` rejects a `mean_revert` `half_life` that is not finite
and > 0 and any `sigma < 0`, and `DynamicsSpec` rejects duplicate keys (entries
apply sequentially and a repeated mean-revert key would map to its last
`dyn_z` column), each with a `ValueError` naming the key. The oil/food →
inflation transmission of MVP scope §5.1 step 6 is not yet implemented (E7).

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

## 5. License

Code under `sim/`: BSD-2-Clause (`LICENSE`). Catalog, methodology and other
prose: CC BY 4.0.
