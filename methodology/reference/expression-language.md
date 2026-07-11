---
title: expression-language
type: note
permalink: methodology/reference/expression-language
tags:
- methodology
- reference
- expressions
- schema
- events
- contract
- v0.1
---

# Event Expression Language

**Document Version:** 0.1 (draft for discussion)
**Date:** January 2026
**Status:** Normative specification — the contract for expressions embedded in event YAML

This document pins down exactly what "Python expressions for logic" means in
[[methodology/reference/event-yaml-schema]]. It exists because the simulator's
execution model ([[methodology/reference/simulator-architecture]] ADR-1, ADR-4)
evaluates every expression **once per year over vectors of all simulation runs
simultaneously**, and under that evaluation model some Python constructs change
meaning and others break outright. The safe subset must therefore be defined as
a contract, enforced at catalog compile time — not discovered at run time.

**Audiences:**
- **Event authors** — what you may write in `pressure:`, `preconditions:`, and
  cascade `if:` fields, and what to do when you need something outside the subset.
- **Compiler implementers** — what `catalog/expr.py` must accept, reject, and rewrite.

---

## 1. Where expressions appear

| Location | Expected result | Example |
|----------|-----------------|---------|
| `probability.pressure` (Type 2) | numeric | `0.50 * (global_temp_anomaly / 2.0) + …` |
| `probability.preconditions.all[]` (Type 3) | boolean | `"chn.military_spending_deviation > 0.15"` |
| `probability.preconditions.sustained[].expr` (Type 3) | boolean | `"F_GPT > 1.0"` |
| `cascades.triggers[].if` | boolean | `"resolution == 'military_conflict'"` |

---

## 2. Evaluation model

An expression is **compiled once** when the event catalog is built, and
**evaluated once per simulated year** against a namespace in which every name is
bound to a vector holding that quantity's value in *every* run (shape `(R,)`,
where `R` is the number of runs, e.g. 10,000). NumPy broadcasting then resolves
the expression for all runs in a single evaluation: `F_GPT > 1.0` yields a
vector of 10,000 booleans, one per run.

Consequences authors must internalize:

1. **Expressions are pure and total.** Every sub-expression is evaluated for
   every run, every year. There is no short-circuiting, no guarded evaluation,
   no side effects.
2. **Expressions see the present only.** The namespace contains the *current*
   year's factor draws and state. There is no history and no lookahead (see §6
   for the escape hatch).
3. **Expressions must be deterministic.** No randomness, no I/O, no calls
   outside the whitelist. This is what preserves seed reproducibility
   (architecture ADR-8).

---

## 3. Namespace

| Names | Binds to | Example |
|-------|----------|---------|
| `F_CLIM`, `F_FIN`, … (12 factor IDs) | This year's correlated factor draw | `F_GPT > 1.0` |
| Global variables | Current global state | `global_temp_anomaly / 2.0` |
| `entity.variable` (dotted) | Current country/aggregate state | `chn.gdp_growth < 0` |
| `resolution`, `branch`, `years_since` | Owning event's own state (categorical/int) | `resolution == 'military_conflict'` |

All names are resolved against the state catalogs
([[methodology/reference/state-variables-global]],
[[methodology/reference/state-variables-country]]) at compile time. An unknown
name **fails the catalog build** — this is schema validation rule #3, enforced
mechanically.

**Categorical comparisons.** Event-state names like `resolution` are categorical.
The *only* permitted operation is equality/inequality against a string literal
naming a resolution or branch declared by the owning event
(`resolution == 'military_conflict'`). The compiler resolves the string to an
integer code at build time; an undeclared name fails the build. String literals
are not permitted anywhere else.

---

## 4. The permitted subset

### Allowed

| Construct | Notes |
|-----------|-------|
| Numeric literals | `1.0`, `0.15` |
| Names per §3 | including dotted `entity.variable` |
| Arithmetic | `+  -  *  /  **`, unary `-`, parentheses |
| Comparisons | `<  <=  >  >=  ==  !=`, including chained (`0 < x < 1`) |
| Boolean logic | `and  or  not` — **rewritten** by the compiler, see below |
| Whitelisted functions | `min(a, b)`, `max(a, b)` (elementwise, two-argument), `abs`, `clip(x, lo, hi)`, `exp`, `log`, `sqrt`, `where(cond, a, b)` |
| String literals | only in categorical equality per §3 |

**Boolean rewriting.** Authors write natural Python (`and`, `or`, `not`); the
compiler rewrites these to elementwise vector operations (`&`, `|`, `~`) with
correct precedence. This is safe *because* expressions are pure and total (§2):
since both operands are always evaluable, the loss of short-circuit semantics
cannot change the result. The corollary is that **guarding idioms are invalid**
— `x > 0 and log(x) > 1` does not protect the `log`; it will be evaluated for
all runs, including those where `x ≤ 0`. Write `log(max(x, eps))` or restructure.

**Conditionals.** Python's `x if cond else y` is data-dependent control flow
and does not vectorize; it is rejected. Use `where(cond, x, y)`, which evaluates
both arms for all runs and selects per-run.

### Rejected (compile-time error)

| Construct | Why |
|-----------|-----|
| `x if cond else y` | Per-run control flow; use `where()` |
| `lambda`, function definitions | Expressions are formulas, not programs |
| Loops, comprehensions | Unbounded cost in the hot path; use a state variable (§6) |
| Subscripts, slicing | Nothing in the namespace is indexable by design |
| Attribute access beyond `entity.variable` | Closes the sandbox |
| Function calls outside the whitelist | Purity, determinism, cost |
| `import`, assignment, walrus, f-strings | Not formulas |
| String literals outside categorical equality | No string data in the state model |

The compiler enforces this as an **AST allow-list**: each parsed node type must
be on the permitted list or the catalog build fails with the event ID, the
offending expression, and the disallowed construct. Nothing is discovered at
simulation time.

### Type checking

- `pressure` expressions must evaluate to numeric vectors.
- `preconditions` and `if` expressions must evaluate to boolean vectors
  (their top-level operation must be a comparison or boolean combination).

---

## 5. Worked examples from the current catalog

Every expression in the catalog as of January 2026 falls inside the subset:

**AMOC pressure function** (Type 2, arithmetic only):

```python
0.50 * (global_temp_anomaly / 2.0) +
0.25 * (1.0 - arctic_ice_extent / 6.0) +
0.25 * (1.0 - amoc_strength / 18.0)
```
→ numeric `(R,)` vector; three global-variable names, arithmetic. Valid.

**Taiwan preconditions** (Type 3, comparisons):

```python
"F_GPT > 1.0"
"chn.military_spending_deviation > 0.15"
"usa.external_conflict_involvement < 3"
```
→ boolean `(R,)` vectors; the `all:` list is combined by the engine (an AND of
masks), so no boolean operators appear in the expressions themselves. Valid.

**Taiwan conditional cascade**:

```python
"resolution == 'military_conflict'"
```
→ categorical equality against a resolution declared by TAIWAN_CONFLICT,
compiled to an integer-code comparison. Valid.

---

## 6. The expressiveness boundary — and the escape hatch

The subset deliberately cannot express everything an author might want. The
rule for what lives where:

> **Expressions read the current state and do arithmetic on it. Anything that
> requires *memory*, *aggregation with logic*, or *iteration* becomes a state
> variable that the engine maintains — and the expression just reads it.**

| You want to say | Don't write | Instead |
|-----------------|-------------|---------|
| "GDP declined 5 consecutive years" | (impossible — no history in namespace) | Add a counter state variable (e.g. `gdp_decline_years`), maintained by the engine; write `usa.gdp_decline_years >= 5` |
| "F_GPT elevated for 2 years" | (impossible for the same reason) | Already solved: the `sustained:` block — the engine keeps the counter ([[methodology/reference/simulator-architecture]] ADR-5) |
| "≥3 SSA states in conflict" | a 9-term hand-written sum | Propose a derived state variable (e.g. `ssa_states_in_conflict`); keep specs readable |
| "worst drawdown in past decade" | (impossible) | Derived state variable with engine-maintained running extremum |

This boundary is not an implementation accident to route around — it is the
[[methodology/concepts/synthetic-variable-problem]] discipline applied to
expressions: complex constructs get **named, tracked, and auditable** as state
variables rather than hidden inside formula strings. The precedent already
exists in the catalog: `years_since_irregular_transition` is exactly such an
engine-maintained memory variable, created so that specifications can reference
duration without expressions needing history.

**Process:** when an event needs a variable that doesn't exist, the author
proposes it for the state catalog (or asks for help) — per the existing Task 4.2
rule: *"if a reference doesn't exist, find a justifiable alternative in the
catalog, or stop and ask."* Extending the function whitelist is a change to this
document and to the compiler, not something an individual event spec can do.

---

## 7. Compile-time validation summary

The catalog build rejects an event when any expression:

1. fails to parse as a Python expression;
2. contains an AST node outside the §4 allow-list;
3. references a name absent from the factor list, state catalogs, or the owning
   event's declared resolutions/branches;
4. uses a string literal outside categorical equality;
5. has the wrong result type for its slot (§4 type checking);
6. (`sustained` only) omits or malforms the `years` parameter.

All failures are build failures with actionable messages. A catalog that
compiles cannot raise from expression evaluation at simulation time.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-01 | Initial specification, extracted from simulator-architecture ADR-4 discussion |

---

*This document is the normative contract for event-embedded expressions. For
why the subset exists see [[methodology/reference/simulator-architecture]]
ADR-4; for the schema this amends see
[[methodology/reference/event-yaml-schema]] §Python Expression Context.*
