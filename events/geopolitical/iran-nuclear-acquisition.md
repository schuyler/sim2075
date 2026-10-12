---
title: iran-nuclear-acquisition
type: note
permalink: events/geopolitical/iran-nuclear-acquisition
tags:
- event
- type-2
- type-3
- hybrid
- geopolitical
- nuclear
- proliferation
- iran
- mena
- level-1
---

# Iran Nuclear Acquisition

**Type 2/3 Hybrid Event (declared Type 2 in YAML)** — Pressure accumulates from the regional security environment toward a weaponization threshold; crossing it is a small-N leadership decision.

---

## Event Classification

```yaml
id: IRAN_NUCLEAR_ACQUISITION
domain: political
scale: regional
causal_type: 2
onset: sudden
reversibility: irreversible
```

| Attribute | Value |
|-----------|-------|
| **ID** | IRAN_NUCLEAR_ACQUISITION |
| **Scale** | Regional (with global consequences) |
| **Domain** | Political / Strategic |
| **Causal Type** | **Type 2/3 Hybrid**: Threshold (pressure accumulation) + Contingent (weaponization decision) |
| **Onset Speed** | Rapid (6-18 months from decision to confirmed capability) |
| **Reversibility** | Irreversible (knowledge cannot be undone; weapons can be dismantled but capability persists) |

*The YAML declares `causal_type: 2` because the probability block below implements the Type 2 machinery (pressure function, threshold, sharpness, floor); the Type 3 weaponization decision — P(weaponize | threshold crossed) ≈ 50% — is folded into the annual estimate in prose and stays there until schema v0.2 (one causal type per event, [[methodology/project/implementation-guide]] §0). The variance target keeps the documented Type 2/3 hybrid value of 0.55 (Task 4.2 validation rule 0).*

## Description

Iran crosses the threshold from nuclear-capable state to confirmed nuclear weapons possessor. This represents a transition in `iran.nuclear_status` from `Threshold` to `Possessed`.

Iran is already a threshold state with substantial enrichment capability, stockpiles of enriched uranium, and the technical knowledge to construct a device. The discontinuity is the political decision to weaponize plus the time required for assembly and (likely) testing or confirmed intelligence of capability.

**What marks occurrence**: Confirmed nuclear test, credible intelligence of assembled weapon, or Iranian declaration of capability. The event is the crossing of the weaponization Rubicon, not the accumulation of technical prerequisites.

**Important distinction from IRAN_REGIME_CHANGE**: Nuclear acquisition can occur under the current Islamic Republic regime (indeed, this is the most likely pathway). Regime change could either accelerate (chaos scenario) or terminate (reformist scenario) the nuclear program. These events interact but are distinct.

---

## Causal Type Specification (Type 2/3 Hybrid)

### Why Type 2/3?

**Type 2 component (threshold dynamics):**
- Pressure accumulates from regional threats and security environment
- As pressure rises, the perceived benefits of nuclear deterrence increase relative to costs
- Historical pattern: Iran has accelerated enrichment during periods of maximum pressure
- The regime absorbs international pressure until a threshold where deterrence value exceeds isolation cost

**Type 3 component (decision point):**
- Once pressure crosses threshold, Iranian leadership faces explicit weaponization decision
- This is a small-N actor decision (Supreme Leader, IRGC, regime inner circle)
- Resolution probability (whether to weaponize given threshold crossed) has low tractability
- The mode of acquisition (covert vs. breakout vs. contested) also involves actor decisions

### Pressure Function

Per [[methodology/concepts/synthetic-variable-problem]], we use observable indicators. Iran nuclear decision is driven by security environment and regime calculus, proxied through:

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `irn.sanctions_level` | 0.30 | linear | Higher isolation reduces diplomatic alternatives; JCPOA collapse demonstrated |
| `isr.external_conflict_involvement` | 0.25 | exponential | Proxy for strike threat; accelerates as Israel engages regionally |
| `irn.protest_intensity_annual` | 0.15 | inverse | Lower protest = more stable regime with bandwidth for nuclear decision |
| `irn.years_since_irregular_transition` | 0.10 | inverse | Aging regime may seek nuclear guarantee |
| `sau.military_spending` | 0.10 | linear | Saudi military buildup increases Iranian threat perception |
| `global_credit_spread` | 0.10 | linear | Proxy for US-China distraction; higher stress = less crisis management capacity |

**Pressure calculation** (original specification):
```
pressure = 0.30 × (sanctions_level / 100)
         + 0.25 × exp(israel_conflict / 2) / exp(2)  # accelerating
         + 0.15 × (100 - protest_intensity_annual) / 100  # inverse: stability enables
         + 0.10 × (years_since_irregular_transition / 50)  # 46 years since 1979
         + 0.10 × (saudi_military / baseline_military)
         + 0.10 × (global_credit_spread / 300)
```
*Normalized to 0-100 scale*

The YAML expression below realizes these transforms in the expression language's subset: the Israeli-involvement exponential as `exp(x / 2) / exp(2)` (1.0 at the top of the 0-4 scale); the protest term as `(100 − protest) / 100`; the transition-recency term as the formula's `years / 50`, capped at 1.0 with `min()` so the term stays in [0, 1] once the regime passes 50 years (the table labels this transform "inverse" but the formula is direct in years — the formula is what the YAML implements); the Saudi term as the ratio to the ~6% of GDP 2025 baseline (`sau.military_spending / 6`, uncapped as in the formula, so a Saudi buildup above baseline keeps raising pressure); and the credit-spread term as `spread / 300`. The whole sum is wrapped `100 * (...)` per the schema's pressure-scale rule.

**Proxy limitations**: True "regime security perception" and "weaponization intent" are unobservable. We proxy through sanctions (isolation), Israeli activity (threat), Saudi spending (regional competition), and domestic stability indicators. The key unobservables—Supreme Leader calculus, IRGC faction preferences—cannot be directly captured. Probability calibration relies on reference class reasoning from other proliferation cases (North Korea, Pakistan, Libya).

### Threshold

| Parameter | Value |
|-----------|-------|
| **Estimate** | 70 (on 0-100 pressure scale) |
| **Uncertainty** | ±12 |
| **Sharpness (k)** | 0.15 (moderate; decision involves deliberation, not snap judgment) |
| **Historical calibration** | Post-JCPOA collapse acceleration (~pressure 55); 2003 suspension (~pressure 40, diplomatic alternative available); current 2025 (~pressure 50) |

### Key Context: Technical Readiness

Iran's technical position means the barrier is political, not technical:
- 60%+ enriched uranium stockpile sufficient for multiple devices
- Declared 18-day breakout timeline (per IAEA)
- Weaponization knowledge from historical program
- Delivery systems (ballistic missiles) already deployed

The pressure function reflects *political incentive* to weaponize, not technical capability.

### Minimum Probability

**Floor**: 0.5%/year (residual risk from sudden decision triggered by crisis, assassination of key figure, or intelligence of imminent Israeli strike)

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.30 * (irn.sanctions_level / 100) +
      0.25 * (exp(isr.external_conflict_involvement / 2) / exp(2)) +
      0.15 * ((100 - irn.protest_intensity_annual) / 100) +
      0.10 * min(1.0, irn.years_since_irregular_transition / 50) +
      0.10 * (sau.military_spending / 6) +
      0.10 * (global_credit_spread / 300)
    )
  threshold: 70
  threshold_std: 12
  sharpness: 0.15
  floor: 0.005
  annual: 0.015
  range: [0.008, 0.025]
  confidence: medium
```

| Metric | Value |
|--------|-------|
| **Annual probability** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 2.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~31% at point estimate |

### Current Pressure Estimate

Current pressure: ~50/100 (elevated but below threshold)
- `irn.sanctions_level`: ~80 (comprehensive Western sanctions)
- `isr.external_conflict_involvement`: ~2.5 (active regional operations)
- `irn.protest_intensity_annual`: ~40 (elevated post-2022; suppressed but present)
- `irn.years_since_irregular_transition`: 46 years (since 1979 revolution)
- `sau.military_spending`: ~6% GDP (elevated but stable)
- `global_credit_spread`: ~120 bps (normal range)

*At these values the YAML expression gives 68.0, not ~50: the Saudi term sits at its full weight at baseline (ratio 1.0) and the 46-year transition term at 0.92, together contributing 19 points. The ~50 is the original judgment estimate; weights and transforms are kept as documented rather than re-tuned at migration (see changelog). The compiler's baseline check is skipped for this event because the expression reads country variables, which carry no recorded 2025 baseline.*

### Derivation

1. **Historical base rate**: No clear reference class. Pakistan and North Korea acquired despite pressure; Libya, South Africa, Ukraine gave up programs. Iran-specific factors dominate.

2. **Structural reasoning**:
   - *Toward acquisition*: Technical threshold already crossed; JCPOA collapse removed diplomatic alternative; regional threat environment (Israel, Saudi); North Korea demonstrates value of possession
   - *Against acquisition*: Supreme Leader fatwa (religious prohibition, though interpretable); acquisition triggers regional cascade and further isolation; current regime benefits from threshold ambiguity without possession costs

3. **Current position**: Iran benefits from threshold status—maximum leverage with reduced isolation costs. Acquisition decision requires either (a) perceived imminent threat justifying crossing Rubicon, or (b) regime instability making deterrence value paramount.

4. **Probability derivation**:
   - P(pressure crosses threshold in given year) ≈ 3%
   - P(weaponization | threshold crossed) ≈ 50% (entropy maximization; could be deterred even at high pressure)
   - Combined: ~1.5% annual probability

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- More likely than: AMOC collapse (~1.0%), Chinese Political Crisis (~0.4%)—technical prerequisites exist, political decision is limiting factor
- Similar to: Dollar Reserve Crisis (~1.5%), Egypt State Failure (~1.5%)—significant structural pressures with uncertain trigger
- Less likely than: Global Financial Crisis (~3.0%), Severe Pandemic (~2.0%)—latter have higher stochastic components

### Key Uncertainties

- **Israeli strike decision**: Would preemptive strike delay or accelerate?
- **US policy trajectory**: Maximum pressure vs. diplomatic engagement
- **Supreme Leader succession**: New leader may recalculate
- **Regional normalization**: Abraham Accords expansion reduces or increases pressure?
- **IRGC institutional interests**: Does IRGC benefit more from threshold or possession?

### Case Against This Specification

**Threshold status is optimal for Iran**: Iran currently enjoys the benefits of nuclear capability (leverage, deterrence perception) without the costs of possession (maximum isolation, regional cascade trigger). Rational actors should prefer this stable equilibrium. The 1.5%/year estimate may be too high for crossing a threshold that serves Iranian interests to preserve.

**The fatwa is more binding than outsiders assume**: Supreme Leader Khamenei has issued a fatwa declaring nuclear weapons un-Islamic. Western analysts tend to dismiss this as tactical, but religious rulings carry weight in the Islamic Republic's legitimacy structure. Crossing this line would require theological reinterpretation that may be genuinely difficult.

**International pressure has consistently delayed, not accelerated**: When pressure increases, Iran has accelerated enrichment but not weaponized. The pressure-to-weaponization link may be weaker than the pressure function assumes. Iran may absorb very high pressure while remaining at threshold.

**Regional cascade fears are overstated**: Pakistan's 1998 tests didn't trigger regional cascade despite predictions. Saudi nuclear acquisition faces enormous obstacles (technical, political, international). The cascade effects may not materialize even with Iranian acquisition.

**Counterargument**: North Korea demonstrates that threshold states do cross the Rubicon when incentives align. Iran's security environment has deteriorated since JCPOA collapse. The fatwa can be reinterpreted (defensive weapons, existential threat exception). The estimate acknowledges uncertainty in the 0.8-2.5% range.

### Probability Evolution

As a Type 2/3 hybrid, probability depends on pressure trajectory and decision windows:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | 1.5-2.0% | JCPOA dead; enrichment advancing; succession approaching |
| 2030-2040 | 1.2-2.0% | Post-succession period; depends on new leader's calculus |
| 2040-2050 | 1.0-1.8% | Path-dependent on whether acquisition occurred or regional dynamics shifted |
| 2050-2075 | 0.5-1.5% | If no acquisition by 2050, regional equilibrium may have stabilized |

**Key inflection points**:
- Supreme Leader succession (whenever it occurs): Window for policy recalculation
- Israeli strike decision: Would accelerate timeline if program survives
- Saudi nuclear pathway activation: Would increase pressure substantially
- US-Iran diplomatic breakthrough: Would decrease pressure substantially

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2/3 Hybrid target (ΛΩΛᵀ)ᵢᵢ = 0.55*

```yaml
factors:
  F_MENA: 0.48  # Regional threat environment; Saudi/Israel tensions drive pressure
  F_GPT: 0.37   # US-Iran confrontation; great power competition affects enforcement
  F_EAS: 0.14   # China relationship; alternative economic/diplomatic partner
  F_FIN: 0.10   # Sanctions effectiveness depends on global financial system
  F_EUR: 0.07   # European role in diplomacy and sanctions
  F_TECH: 0.03  # Marginal; technical capability already sufficient
variance: 0.55  # Type 2/3 Hybrid target (validation rule 0), not the Type 2 table value
```

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_MENA** | 0.48 | Regional threat environment; Saudi/Israel tensions drive pressure |
| **F_GPT** | 0.37 | US-Iran confrontation; great power competition affects enforcement |
| F_EAS | 0.14 | China relationship; alternative economic/diplomatic partner |
| F_FIN | 0.10 | Sanctions effectiveness depends on global financial system |
| F_EUR | 0.07 | European role in diplomacy and sanctions |
| F_TECH | 0.03 | Marginal; technical capability already sufficient |
| F_CLIM | 0.00 | No significant pathway |
| F_HLTH | 0.00 | No significant pathway |
| F_SAS | 0.00 | Limited direct linkage |
| F_SSA | 0.00 | No significant pathway |
| F_LAM | 0.00 | No significant pathway |
| F_FOOD | 0.00 | No significant pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.55 (Type 2/3 Hybrid target); scale factor = 0.68 from original loadings. The original (pre-Task 3.11) loadings were F_MENA 0.70, F_GPT 0.55, F_EAS 0.20, F_FIN 0.15, F_EUR 0.10, F_TECH 0.05, with the then-current check "Sum of squared loadings: 0.84 ✓"; under the correlated-factor Ω those loadings would have explained ~1.19 of unit variance, which is why they were scaled.

### Loading Interpretation (Type 2/3)

Factors shock state variables in pressure function:
- High F_MENA → Israeli military activity increases, Saudi buildup accelerates → `israel.external_conflict_involvement` and `saudi_arabia.military_spending` rise → pressure increases
- High F_GPT → US-Iran tension escalates, sanctions tighten → `iran.sanctions_level` rises; also US distraction increases → pressure increases
- High F_EAS → China provides more economic/diplomatic cover → may slightly reduce pressure or provide alternative pathway

---

## Resolution Branches

Once pressure crosses threshold and decision to weaponize is made, the mode of acquisition varies:

```yaml
resolutions:
  - id: covert_acquisition
    p: 0.34
    branches:
      - {id: fait_accompli_acceptance, p: 0.60, desc: "Containment/deterrence replaces prevention; India/Pakistan post-1998 trajectory"}
      - {id: delayed_military_response, p: 0.40, desc: "Israel/US strike the fait accompli; Iran retaliates; regional war risk"}
  - id: breakout_acquisition
    p: 0.33
    branches:
      - {id: isolation_consolidation, p: 0.55, desc: "North Korea pathway; regime survives under maximum sanctions"}
      - {id: preemptive_strike_during_breakout, p: 0.45, desc: "Strikes during the declared breakout; likely regional conflict"}
  - id: contested_acquisition
    p: 0.33
    branches:
      - {id: acquisition_despite_strikes, p: 0.70, desc: "Program completed under fire; strongest rally effect"}
      - {id: mutual_exhaustion, p: 0.30, desc: "Extended conflict; unstable deterrence from exhaustion"}
```

*Resolution probabilities are uniform in intent (33/33/33); the schema requires them to sum to exactly 1.0, so the rounding residual is carried by `covert_acquisition`, the North Korea-precedent pathway.*

**Covert acquisition** (33%): Iran develops weapons capability secretly at undisclosed facilities. Eventually detected through intelligence or inadvertent disclosure. Fait accompli when revealed. International community faces established nuclear state rather than preventable program. North Korea pathway.

**Breakout acquisition** (33%): Iran openly withdraws from NPT and races to weapon capability. Declared nuclear state. Maximum international isolation but also maximum domestic legitimacy ("standing up to pressure"). Fastest pathway but most visible.

**Contested acquisition** (33%): Israeli and/or US preemptive strike fails to prevent weaponization. Iran completes program despite military action, possibly accelerated by rally-around-flag effect. Acquires weapons while engaged in active or recent conflict. Most destabilizing pathway.

### Resolution Probability Rationale

| Field | Value |
|-------|-------|
| Default | uniform (33/33/33) |
| Specified | 33/33/33 |
| Confidence | n/a (using default) |

No clear structural asymmetry among acquisition modes.

Arguments for covert: North Korea precedent; Iran has undisclosed facilities history; maximizes strategic ambiguity.

Arguments for breakout: Faster timeline; domestic legitimacy gains; NPT withdrawal is reversible until late stage.

Arguments for contested: If Israel/US strikes, rally effect may accelerate rather than prevent; Osirak/Syria precedents show strikes delay but don't prevent determined programs.

Defaulting to uniform per entropy maximization. Mode of acquisition is small-N actor decision (Iranian leadership response to circumstances) with low tractability.

---

## Aftermath Branches (by Resolution)

The aftermath branches are the `branches:` of each resolution in the YAML above. Their factor modifications and decaying-to-floor durations are not representable in schema v0.1 (factor shocks from events and decay-to-floor are v0.2 backlog), so they are kept here as the original specification; the state-variable impacts in the `impacts:` block apply to all six branches at the same magnitude, as the original impact tables did not differentiate by branch. The per-branch cascade triggers are carried into the `cascades:` block where the target exists in the catalog and the form is an annual delta; the rest stay in the tables here (see Cascade Effects).

### Covert Acquisition Aftermath

**Fait accompli acceptance** (60%): International community accepts nuclear Iran as fait accompli. Containment/deterrence posture replaces prevention. Similar to India/Pakistan post-1998 trajectory. Maximum sanctions but no military response. Iran gains deterrent; regional dynamics shift toward accommodation.

| Field | Value |
|-------|-------|
| Factor modifications | F_MENA +0.30; F_GPT +0.25 |
| Duration | permanent |
| Cascade triggers | SAUDI_NUCLEAR_ACQUISITION +5%/year for 10 years — "Stated Saudi policy to match Iranian capability"; NPT_REGIME_EROSION +3%/year permanent — "Successful proliferation weakens nonproliferation norm" |

**Delayed military response** (40%): Israel and/or US conducts military strikes despite fait accompli. Limited effectiveness against dispersed, hardened capability. Escalation risk. Iran retaliates against Gulf states/Israel. Worst-case scenario: strikes trigger regional war without eliminating capability.

| Field | Value |
|-------|-------|
| Factor modifications | F_MENA +0.70; F_GPT +0.50; F_FIN +0.25 |
| Duration | decaying, half_life 5 years, floor 0.15 |
| Cascade triggers | STRAIT_OF_HORMUZ_CRISIS probability 0.50 — "Iran retaliates against shipping"; OIL_SUPPLY_SHOCK probability 0.60 — "Regional conflict disrupts supply"; ISRAEL_IRAN_WAR probability 0.70 — "Strikes escalate to broader conflict" |

### Breakout Acquisition Aftermath

**Isolation consolidation** (55%): Iran weathers maximum pressure, consolidates nuclear deterrent. North Korea pathway. Comprehensive sanctions; diplomatic isolation; but regime survives with nuclear security guarantee. Domestic rally effect may temporarily stabilize regime.

| Field | Value |
|-------|-------|
| Factor modifications | F_MENA +0.35; F_GPT +0.30 |
| Duration | permanent |
| Cascade triggers | SAUDI_NUCLEAR_ACQUISITION +6%/year for 10 years — "Declared Iranian capability maximizes Saudi response pressure"; TURKEY_NUCLEAR_RECONSIDERATION +2%/year for 10 years — "NATO member may reassess given regional dynamics" |

**Preemptive strike during breakout** (45%): Israel/US strikes during declared breakout attempt. Window is narrow (weeks to months). Success uncertain—may delay but not prevent. If strikes occur during breakout, likely escalation to regional conflict.

| Field | Value |
|-------|-------|
| Factor modifications | F_MENA +0.75; F_GPT +0.55; F_FIN +0.30 |
| Duration | decaying, half_life 6 years, floor 0.20 |
| Cascade triggers | OIL_SUPPLY_SHOCK probability 0.70 — "Hormuz disruption during conflict"; IRAN_REGIME_CHANGE ×1.5 — "Military conflict may destabilize regime" |

### Contested Acquisition Aftermath

**Acquisition despite strikes** (70%): Iran completes program despite Israeli/US military action. Strongest rally effect. Regime legitimacy enhanced by "resisting aggression." Nuclear capability achieved under fire. Most destabilizing outcome—demonstrates strikes cannot prevent determined proliferators.

| Field | Value |
|-------|-------|
| Factor modifications | F_MENA +0.80; F_GPT +0.60; F_FIN +0.35 |
| Duration | decaying, half_life 8 years, floor 0.25 |
| Cascade triggers | SAUDI_NUCLEAR_ACQUISITION +8%/year for 10 years — "Demonstrated failure of prevention accelerates Saudi timeline"; NPT_REGIME_COLLAPSE +5%/year permanent — "Prevention failure + retaliation severely damages regime"; STRAIT_OF_HORMUZ_CRISIS probability 0.80 — "Active conflict includes shipping disruption" |

**Mutual exhaustion** (30%): Extended conflict leads to exhaustion on all sides. Iran possesses weapons but faces severe damage. Israel/US have expended military options without prevention. Unstable deterrence emerges from mutual exhaustion rather than deliberate architecture.

| Field | Value |
|-------|-------|
| Factor modifications | F_MENA +0.50; F_GPT +0.40; F_FIN +0.25 |
| Duration | decaying, half_life 10 years, floor 0.15 |

**Aftermath probability rationale**: Contested acquisition branch probabilities reflect that if strikes fail to prevent (which is the definition of this resolution), Iran is highly likely to complete the program. The 70/30 split reflects whether the outcome is decisive Iranian success vs. mutual exhaustion.

Historical precedent: Osirak (1981) delayed but didn't prevent Iraqi program; Syrian reactor strike (2007) was more successful but Syria was earlier in development. Iran's dispersed, hardened infrastructure and technical readiness make prevention harder.

---

## Impact Vector

```yaml
impacts:
  covert_acquisition.fait_accompli_acceptance:
    # Iran
    - {var: irn.sanctions_level,               mag: [15, 10],     onset: immediate,    permanent: true}
    - {var: irn.protest_intensity_annual,      mag: [-10, 8],     onset: {gradual: 1}, decay: 5}
    - {var: irn.un_voting_alignment_us,        mag: [-0.2, 0.1],  onset: immediate,    permanent: true}
    - {var: irn.trade_share_china,             mag: [10, 8],      onset: {gradual: 1}, permanent: true}

    # Regional
    - {var: sau.military_spending,             mag: [2, 1],       onset: {gradual: 2}, permanent: true}
    - {var: isr.external_conflict_involvement, mag: [0.5, 0.3],   onset: immediate,    decay: 3}
    - {var: gulf_states.protest_intensity_annual, mag: [5, 3],    onset: {gradual: 1}, decay: 3}

    # Global
    - {var: oil_brent,                         mag: [15, 11.25],  onset: immediate,    decay: 1}

  covert_acquisition.delayed_military_response:
    inherit: covert_acquisition.fait_accompli_acceptance
    scale: 1.0

  breakout_acquisition.isolation_consolidation:
    inherit: covert_acquisition.fait_accompli_acceptance
    scale: 1.0

  breakout_acquisition.preemptive_strike_during_breakout:
    inherit: covert_acquisition.fait_accompli_acceptance
    scale: 1.0

  contested_acquisition.acquisition_despite_strikes:
    inherit: covert_acquisition.fait_accompli_acceptance
    scale: 1.0

  contested_acquisition.mutual_exhaustion:
    inherit: covert_acquisition.fait_accompli_acceptance
    scale: 1.0
```

*Units: every row is additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields); there are no `gdp_real` rows. The original tables below are the source magnitudes; where the YAML had to re-express a row (synthetic variable replaced by an observable, percentage converted to $/bbl, categorical transition not representable) the mapping is recorded under each table and in the changelog.*

### Iran Impacts (All Resolutions)

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `iran.nuclear_status` | → Possessed | Categorical transition | immediate | permanent |
| `iran.sanctions_level` | ↑ | +15 ± 10 | immediate | maintenance_required (depends on int'l consensus) |
| `iran.regime_stability` | ↑ | +10 ± 8 | rapid(1yr) | decaying (half_life: 5yr); rally effect fades |
| `iran.alliance_west` | ↓ | -20 ± 10 | immediate | persistent |
| `iran.alliance_china` | ↑ | +10 ± 8 | rapid(1yr) | maintenance_required |

*Mapping to YAML*: `nuclear_status` is a categorical variable (NONE/THRESHOLD/POSSESSED) with no numeric encoding in the state catalog, so the THRESHOLD → POSSESSED transition — the event's defining state change — has no impact row in v0.1 and is carried here in prose. `regime_stability` is a synthetic variable (replaced by observables at the 2025-12-30 review but left in this table); the rally effect is re-expressed as a −10 ± 8 drop in `irn.protest_intensity_annual` with the same onset and 5-year half-life. `alliance_west` and `alliance_china` are not catalog variables; the −20 on a 0-100 alignment scale becomes −0.2 ± 0.1 on `irn.un_voting_alignment_us` (−1 to +1, the same fifth of the scale's half-range) and the +10 becomes +10 ± 8 percentage points of `irn.trade_share_china`.

### Regional Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `saudi_arabia.military_spending` | ↑ | +2% GDP ± 1% | rapid(2yr) | persistent |
| `israel.external_conflict_involvement` | ↑ | +0.5 ± 0.3 | immediate | decaying (half_life: 3yr) |
| `global.us_china_tension` | ↑ | +8 ± 5 | immediate | decaying (half_life: 2yr) |
| Gulf States aggregate: `regime_stability` | ↓ | -5 ± 3 | rapid(1yr) | decaying |

*Mapping to YAML*: `us_china_tension` is a synthetic variable with no observable proxy in the catalog; the row (listed here and again under Global Impacts) is dropped and the channel kept in prose. The Gulf States `regime_stability` row becomes +5 ± 3 on `gulf_states.protest_intensity_annual`; the table gives no half-life for its "decaying" durability, so the YAML uses 3 years, matching the Israeli-involvement spike.

### Global Impacts

| Variable | Direction | Magnitude (mean ± std) | Onset | Durability |
|----------|-----------|------------------------|-------|------------|
| `global.nuclear_stability` | ↓ | -15 ± 8 | immediate | permanent (until new equilibrium) |
| `global.oil_brent` | ↑ | +20% ± 15% | immediate | decaying (half_life: 1yr) |
| `global.us_china_tension` | ↑ | +8 ± 5 | immediate | decaying (half_life: 2yr) |

*Mapping to YAML*: `nuclear_stability` has no catalog variable (NPT_REGIME_COLLAPSE in [[events/planned-events-round-2]] is the planned carrier of systemic proliferation risk); the row is dropped and the channel kept in prose. The oil row is converted against the `oil_brent` 2025 baseline of $75/bbl: +20% ± 15% → +$15 ± $11.25.

### Durability Specifications

| Durability Type | Parameters | Used For |
|-----------------|------------|----------|
| **permanent** | N/A | `nuclear_status` change; knowledge/capability |
| **decaying** | half_life: varies, floor: 0.1-0.2 | Oil price spike; rally effect; tension spikes |
| **maintenance_required** | annual_failure_prob: 5-10% | Sanctions consensus; isolation |

*v0.1 compiles only `decay`, `permanent` and `until: resolved`: the decay-to-floor rows are written as plain decays (floor dropped), and the maintenance_required rows (sanctions, China alignment) and the "persistent" rows (Saudi spending, Western alignment) as `permanent: true`. Maintenance and decay-to-floor durability are schema v0.2 backlog.*

---

## Cascade Effects

```yaml
cascades:
  triggers:
    # Proliferation precedent: +5/+6/+8%/year by acquisition mode (aftermath tables above)
    - {event: SAUDI_NUCLEAR_ACQUISITION, delta: 0.05, years: 10, if: "resolution == 'covert_acquisition'"}
    - {event: SAUDI_NUCLEAR_ACQUISITION, delta: 0.06, years: 10, if: "resolution == 'breakout_acquisition'"}
    - {event: SAUDI_NUCLEAR_ACQUISITION, delta: 0.08, years: 10, if: "resolution == 'contested_acquisition'"}
    # Oil risk premium
    - {event: OIL_SUPPLY_SHOCK,          delta: 0.02,  years: 3}
    # Regime legitimacy: rally effect, nuclear security guarantee
    - {event: IRAN_REGIME_CHANGE,        delta: -0.01, years: 5}
  triggered_by:
    - {event: IRAN_REGIME_CHANGE}  # direction depends on the successor regime; see Interaction section
```

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism | In YAML? |
|---------|--------------|-------------------|----------|-----------|----------|
| Proliferation precedent | SAUDI_NUCLEAR_ACQUISITION | +5-8%/year | 10 years | Stated Saudi policy; Pakistan assistance pathway | Yes, by resolution |
| NPT erosion | TURKEY_NUCLEAR_RECONSIDERATION | +2%/year | 10 years | NATO member reassesses; regional dynamics | No — folds into NPT_REGIME_COLLAPSE (round-2 promotion, no file yet; [[events/backlog-registry]] §2) |
| Regional tension | ISRAEL_IRAN_WAR | +3%/year | 5 years | Israel may strike even after acquisition | No — round-2 promotion, no file yet ([[events/backlog-registry]] §1) |
| Oil risk premium | OIL_SUPPLY_SHOCK | +2%/year | 3 years | Hormuz vulnerability; regional instability | Yes |
| Regime legitimacy | IRAN_REGIME_CHANGE | -1%/year | 5 years | Rally effect; nuclear security guarantee | Yes |

The aftermath-branch cascade forms that are not annual deltas — STRAIT_OF_HORMUZ_CRISIS (conditional probability 0.50-0.80; round-2 promotion), OIL_SUPPLY_SHOCK (conditional probability 0.60-0.70 in the strike branches), NPT_REGIME_EROSION / NPT_REGIME_COLLAPSE (+3-5%/year permanent; round-2 promotion) and the IRAN_REGIME_CHANGE ×1.5 multiplier — stay in the aftermath tables above; the YAML carries the main-table deltas.

### Impact Chains

**Pathway 1**: Iran nuclear → Saudi response → Regional arms race
```
Iran acquires nuclear weapons →
Saudi Arabia accelerates nuclear program (Pakistan pathway) →
Turkey reconsiders nuclear status →
Regional nuclear arms race; NPT regime collapses
```

**Pathway 2**: Iran nuclear → Israeli response → Regional war
```
Iran acquires nuclear weapons →
Israel conducts strikes (prevention or punishment) →
Iran retaliates (Hormuz, Gulf states, direct strikes) →
Regional war; oil supply disruption
```

**Pathway 3**: Iran nuclear → Deterrence stability
```
Iran acquires nuclear weapons →
Regional powers adjust to nuclear-armed Iran →
Unstable but functioning deterrence emerges →
Reduced conventional conflict risk (nuclear shadow)
```

---

## Transmission Channels

### Proliferation Cascade Channel

**Mechanism**: Iranian acquisition demonstrates successful proliferation pathway; reduces perceived costs for other aspirants; triggers stated Saudi policy
**Affected regions**: Gulf, Turkey, Egypt (potential), East Asia (precedent effects)
**Affected variables**: `[country].nuclear_status`, `global.nuclear_stability`
**Notes**: Saudi Arabia has explicitly stated it would match Iranian capability. Pakistan has provided nuclear assistance historically.

### Oil Market Channel

**Mechanism**: Nuclear crisis raises Hormuz closure risk; general regional instability premium
**Affected regions**: Global (price effects); Asia and Europe (import dependence)
**Affected variables**: `global.oil_brent`, `global.container_freight_index`, importer inflation
**Notes**: Even without Hormuz closure, risk premium affects prices

### Regional Security Channel

**Mechanism**: Nuclear Iran changes regional power balance; affects alliance calculations
**Affected regions**: Gulf states, Israel, Turkey
**Affected variables**: `[country].alliance_west`, `[country].military_spending`, `[country].external_conflict_involvement`
**Notes**: Gulf states may seek closer US alignment or accommodation with Iran

---

## Interaction with IRAN_REGIME_CHANGE

These events have complex bidirectional effects:

### If IRAN_NUCLEAR_ACQUISITION occurs first:
- Regime gains nuclear security guarantee → P(IRAN_REGIME_CHANGE) decreases modestly (-1%/year for 5 years)
- But increased isolation may accelerate economic pressure → effect uncertain
- Net effect: slight stabilization of regime

### If IRAN_REGIME_CHANGE occurs first:
- **Revolutionary transition**: Depends on successor regime
  - Reformist successor: May abandon program (Libya pathway) → P(acquisition) drops substantially
  - Chaotic transition: May accelerate program (secure deterrent amid instability) → P(acquisition) increases
  - Military takeover: Likely continues program → P(acquisition) unchanged
- **Failed succession crisis**: Uncertain control of program → P(acquisition) may increase (use it or lose it dynamics)
- Net effect: Uncertain; model as conditional probability adjustment

---

## Historical Analogues

| Case | Relevance | Key Lesson |
|------|-----------|------------|
| North Korea 2006 | Threshold → acquisition under maximum pressure | Determined state can acquire despite sanctions; fait accompli acceptance likely |
| Pakistan 1998 | Regional rival nuclear acquisition | Tests followed by sanctions, then normalization; proliferation cascade didn't materialize fully |
| India 1974/1998 | Declared nuclear status | International adjustment to new nuclear state; regional stability concerns |
| Iraq 1981-2003 | Failed prevention through strikes and sanctions | Osirak delayed but didn't prevent; regime change ultimately ended program |
| Libya 2003 | Abandonment under pressure | Diplomatic alternative can work—but required regime security guarantee |
| South Africa 1990s | Voluntary denuclearization | Regime transition led to abandonment; unusual case |

---

## Early Warning Indicators

| Indicator | Current Status | Warning Level |
|-----------|---------------|---------------|
| Enrichment level | 60%+ (weapons-grade is 90%+) | Already elevated |
| IAEA access | Limited; disputes ongoing | Denial of access is warning |
| Fordow activity | Active | Expansion/hardening is warning |
| Declared stockpile | Sufficient for multiple devices | Already sufficient |
| NPT status | Member (with disputes) | Withdrawal announcement is critical warning |
| Regional tension | Elevated | Israeli strike preparation is warning |
| Diplomatic track | Stalled | Abandonment of diplomacy is warning |

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-30
  review: complete
  upgrade: true
```

### Upgrade Rationale

IAEA technical assessments; Israeli strike capability analysis; Saudi nuclear pathway investigation; Pakistan assistance history

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- IAEA Iran reports (enrichment levels, stockpiles, access disputes)
- Iranian nuclear program technical assessments
- Saudi statements on nuclear matching
- Israeli military capability assessments
- NPT regime analysis
- Historical proliferation cases (North Korea, Pakistan, India, Iraq, Libya)

## Open Questions

- **Strike effectiveness**: Can Israeli/US strikes actually prevent acquisition given dispersal and hardening?
- **Saudi pathway**: How quickly could Saudi Arabia acquire weapons with Pakistani assistance?
- **Chinese role**: Would China provide diplomatic cover or actively facilitate?
- **Fatwa interpretation**: Is Supreme Leader fatwa against nuclear weapons a binding constraint or interpretable?
- **Deterrence stability**: Would nuclear Iran be more or less aggressive regionally?
- **Successor regime**: What would different post-regime-change governments do with program?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-10-12 | Migrated to YAML-embedded schema | Task 4.2.16. **Causal type**: Type 2/3 hybrid declared `causal_type: 2` (the probability block implements pressure/threshold/sharpness/floor; the 50% weaponization-decision factor stays in prose), `variance: 0.55` kept as the documented hybrid target (rule 0), loadings unchanged (achieved 0.554). **Pressure**: wrapped `100 * (...)`; transforms realized as documented under the pressure table; expression gives 68.0 at the prose's current values vs. the prose's "~50" — left as specified, flagged for review. **Resolutions**: 33/33/33 written 0.34/0.33/0.33 to sum to 1.0; aftermath branches became resolution `branches:` with their factor modifications and decay-to-floor durations kept in prose (v0.2 backlog); all six branches inherit the same impacts at scale 1.0 since the source tables did not differentiate. **Variables**: `regime_stability` (Iran) → `irn.protest_intensity_annual` −10 ± 8; Gulf `regime_stability` → `gulf_states.protest_intensity_annual` +5 ± 3 with a 3-year half-life supplied; `alliance_west` → `irn.un_voting_alignment_us` −0.2 ± 0.1; `alliance_china` → `irn.trade_share_china` +10 ± 8. **Dropped rows** (kept in prose): `irn.nuclear_status` (categorical, no numeric encoding), `global.us_china_tension` (synthetic, listed twice), `global.nuclear_stability` (no catalog variable). **Units**: oil +20% ± 15% → +$15 ± $11.25 against the $75/bbl baseline. **Durability**: maintenance_required and "persistent" → `permanent: true`; decay-to-floor → plain `decay`; "rapid(1yr/2yr)" → `{gradual: N}`. **Cascades**: SAUDI_NUCLEAR_ACQUISITION carried per resolution (0.05/0.06/0.08); OIL_SUPPLY_SHOCK and IRAN_REGIME_CHANGE from the main table; TURKEY_NUCLEAR_RECONSIDERATION (fold → NPT_REGIME_COLLAPSE), ISRAEL_IRAN_WAR, STRAIT_OF_HORMUZ_CRISIS and NPT_REGIME_EROSION/COLLAPSE are round-2 promotions without files and stay in prose; non-delta forms (conditional probabilities, ×1.5) stay in prose. No `until: resolved` rows, so no `resolves_after`. Legacy `resolutions`/`aftermath_branches` YAML blocks merged into the schema blocks. **Restored from history**: the pre-Task 3.11 loadings (F_MENA 0.70, F_GPT 0.55, F_EAS 0.20, F_FIN 0.15, F_EUR 0.10, F_TECH 0.05; "Sum of squared loadings: 0.84 ✓") under Factor Loadings |
| 2025-12-30 | Critical review: replaced synthetic variables (regime_stability, us_china_tension) with observables; added Case Against and Probability Evolution sections | Task 2.4 systematic review |
| 2025-12-25 | Initial Level 1 specification | Task 2.1.20 |

---

*See [[methodology/reference/type-3-calibration]] for Type 2/3 hybrid methodology | [[events/geopolitical/iran-regime-change]] for related event | [[factors/f-mena]] for regional factor*
