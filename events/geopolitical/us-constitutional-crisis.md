---
title: us-constitutional-crisis
type: note
permalink: events/geopolitical/us-constitutional-crisis
tags:
- event
- geopolitical
- type-2
- type-3
- hybrid
- usa
- political-crisis
- level-1
---

# US Constitutional Crisis

**Type 2/3 Hybrid Event** — Threshold pressure (Type 2) with contingent resolution (Type 3); declared as Type 2 in YAML because the probability block implements a pressure function, threshold and floor.

## Specification

```yaml
id: US_CONSTITUTIONAL_CRISIS
domain: political
scale: global
causal_type: 2
onset: sudden
reversibility: irreversible
```

*Original classification: Causal Type "Type 2/3 Hybrid: Threshold + Contingent Resolution" (one causal type per event in YAML; see below). Onset speed: rapid (crisis unfolds over 6-24 months). Reversibility: irreversible (all resolutions produce fundamental regime change).*

## Description

Breakdown of US constitutional order: the federal system either transforms into a fundamentally different political structure or fragments entirely. This is not a political crisis that the system absorbs — it is the end of constitutional governance in its current form.

The event fires only when constitutional breakdown is underway. Severe crises that the system weathers through courts, Congress, or other constitutional mechanisms are sub-threshold — they represent the system functioning under extreme stress, not discontinuity. The 2000 election dispute, January 6 2021, and Watergate are canonical examples: extraordinary stress, but the same constitutional order continued operating afterward.

**Discontinuity requirement**: All resolutions produce a different regime governing the United States. "More polarized democracy" or "weakened institutions" is not a discontinuity.

---

## Causal Type Specification

### Type 2/3 Hybrid Structure

This event combines threshold dynamics (Type 2) with contingent resolution (Type 3):

**Type 2 Component**: Pressure accumulates through polarization, institutional erosion, legitimacy disputes, and economic stress. At critical pressure, constitutional breakdown becomes likely.

**Type 3 Component**: Once threshold is crossed, outcome depends on actor decisions (state governors, military commanders, judges, protest movements, political leaders). Resolution probabilities reflect structural factors but are not precisely calibrated.

```
Pressure accumulates → Threshold crossed → Constitutional breakdown inevitable →
Resolution sampled → Aftermath branches
```

**YAML declaration**: `causal_type: 2`. The probability block implements the Type 2 mechanism (pressure function, threshold, sharpness, floor); the Type 3 component is carried by the `resolutions:` block, which the engine samples at firing. The variance target stays at the hybrid's documented 0.55 per Task 4.2 validation rule 0 (see Factor Loadings for the loading correction this migration made to actually reach it).

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `usa.regime_stability` | 0.30 | inverse | Composite legitimacy/stability metric |
| `usa.institutional_quality` | 0.25 | inverse | Institutional decay signal; WGI-style composite |
| `usa.internal_conflict_intensity` | 0.20 | linear | Observable political violence, armed confrontation |
| `usa.protest_activity` | 0.15 | linear | Civil unrest; cross-partisan coordination multiplies impact |
| `usa.gdp_growth` | 0.10 | deviation from 2% baseline | Economic stress historically correlates with instability |

The two synthetic indices in this table (`regime_stability`, `institutional_quality`) and `protest_activity` are not state-catalog variables ([[methodology/concepts/synthetic-variable-problem]] §3; [[methodology/reference/state-variables-country]] §4). The YAML expression below realizes the table on observables, in the expression language's subset:

| Table term | Weight | Realization | Why |
|---|---|---|---|
| `usa.regime_stability` (inverse) | 0.30 | 0.15 × ramp of `usa.press_freedom_events` saturating at 50/yr + 0.15 × `1 / (1 + usa.years_since_irregular_transition / 5)` | The composite's two observable faces: norm erosion against the press (CPJ/RSF counts; a 2020-scale year of journalist arrests is full weight) and transition recency, the succession/legitimacy proxy the Pakistan, Chinese and EU events already use |
| `usa.institutional_quality` (inverse) | 0.25 | ramp of `(100 − usa.public_investment_efficiency) / 50` | Institutional quality → governance metrics, the same mapping the Chinese event uses for its impact rows (20 index points per WGI unit) |
| `usa.internal_conflict_intensity` (linear) | 0.20 | `/ 4` | Linear on the 0-4 scale |
| `usa.protest_activity` (linear) | 0.15 | `usa.protest_intensity_annual / 100` | The catalog's 0-100 unrest index |
| `usa.gdp_growth` (deviation from 2%) | 0.10 | ramp of `(2 − growth) / 6`, zero at 2% and saturating at −4% | Only shortfalls add pressure |

All six terms lie in [0, 1], so the weighted sum is wrapped `100 * (...)` to sit on `threshold`'s 0-100 scale. Polarization, elite cohesion and federal-state tension — three of the six components assessed below — have no observable in the catalog and are carried only through their downstream effects (unrest, political violence, press-freedom events).

*Note: Additional pressure from GLOBAL_FINANCIAL_CRISIS (+1.5% for 3 years) and cascades from contested elections.*

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 85 on 0-100 scale | Event fires only when constitutional breakdown is underway, not when crisis is severe |
| **Uncertainty** | ±10 (range 75-95) | Unprecedented event; threshold poorly calibrated |
| **Sharpness (k)** | 12 | Sharp transition — constitutional orders appear stable until they're not |
| **Historical calibration** | US 1860-61 (threshold breach → Civil War); Weimar 1932-33 (threshold breach → collapse); US 2020-21 (sub-threshold — system absorbed via courts/Congress) |

### Current Pressure Assessment (2025)

**Estimated pressure**: ~45-50 on 0-100 scale

| Component | Status | Contribution |
|-----------|--------|--------------|
| Polarization | Historically high; approaching 1850s levels | High |
| Institutional legitimacy | Supreme Court, elections questioned by large minorities | Moderate-High |
| Elite cohesion | Low; significant elite polarization | High |
| Political violence | Elevated but contained; January 6, political threats | Moderate |
| Economic performance | Moderate growth; high inequality but not crisis | Low-Moderate |
| Federal-state tension | Elevated; some states defying federal authority on specific issues | Moderate |

Distance to threshold (~35-40 points) is substantial but narrower than most other democracies.

*Expression check*: at plausible 2025 values (`usa.press_freedom_events` ≈ 15, `usa.years_since_irregular_transition` ≥ 160, `usa.public_investment_efficiency` ≈ 100, `usa.internal_conflict_intensity` = 1, `usa.protest_intensity_annual` ≈ 30, `usa.gdp_growth` ≈ 2.5) the YAML expression gives ~14/100. The "~45-50" above is a judgment estimate that includes the components the observable proxy cannot see (polarization, elite cohesion, federal-state tension); the compiler's baseline check is skipped for country-variable pressures, so the gap is recorded here rather than mechanically enforced. With sharpness 12 per point, the annual probability sits at the floor until pressure approaches the drawn threshold (sim/README.md §4 item 11).

### Minimum Probability

**Floor**: 0.15% annually even at low pressure

Black swan triggers: assassination of major political figure, military refusing civilian command, simultaneous contested elections at federal and state levels, foreign intervention in electoral system with disputed attribution.

---

## Probability

```yaml
probability:
  pressure: |
    100 * (
      0.15 * min(1.0, max(0.0, usa.press_freedom_events / 50.0)) +
      0.15 * (1.0 / (1.0 + usa.years_since_irregular_transition / 5.0)) +
      0.25 * min(1.0, max(0.0, (100.0 - usa.public_investment_efficiency) / 50.0)) +
      0.20 * (usa.internal_conflict_intensity / 4.0) +
      0.15 * (usa.protest_intensity_annual / 100.0) +
      0.10 * min(1.0, max(0.0, (2.0 - usa.gdp_growth) / 6.0))
    )
  threshold: 85
  threshold_std: 10
  sharpness: 12
  floor: 0.0015
  resolves_after: 10
  annual: 0.005
  range: [0.002, 0.010]
  confidence: low
```

*`resolves_after: 10`*: the Prolonged Instability resolution's "sustained for the duration of instability" rows are written `until: resolved`, and the specification puts that duration at 5-15 years; 10 is the midpoint. The window applies to every firing (the engine keeps one per event), but only the Prolonged Instability rows read it.

| Metric | Value |
|--------|-------|
| **Annual probability** | 0.5% |
| **Low bound** | 0.2% |
| **High bound** | 1.0% |
| **Confidence** | Low |
| **25-year cumulative** | ~12% at point estimate |

### Derivation

**Step 1: Reference class — constitutional breakdowns in established democracies**

| Reference | Outcome | Annual Rate | Notes |
|-----------|---------|-------------|-------|
| United States 1789-1860 | Civil War | ~1.4% (1 in 71 years) | Slavery crisis unique |
| United States 1865-present | No breakdown | 0% realized (160 years) | Multiple crises absorbed |
| Weimar Germany 1919-1933 | Collapsed | ~7% (1 in 14 years) | Weak constitutional design |
| French Fourth Republic 1946-1958 | Collapsed | ~8% (1 in 12 years) | Structural instability |
| Established democracies (broad) | Variable | ~0.2-0.5% | Polity IV database |

US has strong constitutional design and history of absorbing crises. Base rate for comparable established democracies: ~0.3-0.5%.

**Step 2: Structural factors**

Factors increasing probability:
- Polarization at historical highs; epistemic fragmentation
- Legitimacy of elections questioned by significant minorities
- Federal-state tensions elevated; states defying federal authority on specific issues
- Electoral College vulnerable to contested outcomes
- Norm erosion (peaceful transfer questioned 2020-21)
- Armed population; militias with political orientation

Factors decreasing probability:
- Strong constitutional design with multiple veto points
- Military tradition of apolitical service; officer corps professionalized
- No recent history of successful political violence
- Economic performance adequate (not Depression conditions)
- Geographic integration (unlike 1860, no clear regional split)
- Institutional redundancy (courts, states, Congress)

**Step 3: Historical periods of extreme polarization**

| Period | Polarization Level | Outcome |
|--------|-------------------|---------|
| 1850s-1860s | Extreme (slavery) | Civil War |
| 1890s-1900s | High (populism, labor) | Absorbed; reforms |
| 1930s | High (Depression) | Absorbed; New Deal |
| 1960s-1970s | High (civil rights, Vietnam) | Absorbed; institutional reform |
| 2016-present | Very high | Ongoing |

Current polarization is arguably approaching 1850s levels in some dimensions (epistemic divergence, legitimacy disputes) but lacks the clear sectional/geographic division and the singular irresolvable issue (slavery) of that era.

**Step 4: Conditional probability from cascades**

- GLOBAL_FINANCIAL_CRISIS: +1.5% for 3 years (severe economic stress)
- Contested election (not separately modeled): +2.0% for 2 years

**Step 5: Final estimate**

**Point estimate: 0.5% annually** with range 0.2%-1.0%.

This is higher than Chinese Political Crisis (0.4%) because:
- Current pressure estimate is higher (~45-50 vs. ~35-40)
- Multiple visible precursor events (2020-21 contested transfer)
- Structural vulnerabilities in electoral system

This is lower than Russia State Failure (1.0%) because:
- US institutions are stronger and more redundant
- Military is apolitical by strong tradition
- Economic performance is adequate

### Comparative Ranking

- Less likely than: Russia State Failure (~1.0%), Turkey Political Crisis (~1.0%)
- Similar to: Saudi Regime Instability (~0.8%), Iran Regime Change (~0.6%)
- More likely than: Chinese Political Crisis (~0.4%), AMOC Weakening (~0.5%)

The comparative ranking reflects that US is experiencing visible stress but has stronger institutional resilience than most comparison cases.

---

## Resolution Specification (Type 3 Component)

Once the threshold is crossed, one of four resolutions occurs:

### Resolution Branches

```yaml
resolutions:
  - id: authoritarian
    p: 0.30
    branches:
      - {id: stable_autocracy,       p: 0.45, desc: "Authoritarian regime consolidates and stabilizes; possible economic stabilization"}
      - {id: unstable_autocracy,     p: 0.55, desc: "Authoritarian regime faces ongoing resistance; economic decline"}
  - id: fragmentation
    p: 0.25
    branches:
      - {id: peaceful_separation,    p: 0.25, desc: "Successor states establish sovereignty without major armed conflict"}
      - {id: violent_fragmentation,  p: 0.75, desc: "Armed conflict between successor entities"}
  - id: prolonged_instability
    p: 0.30
    branches:
      - {id: eventual_consolidation, p: 0.40, desc: "One faction eventually gains control (5-15 years)"}
      - {id: eventual_fragmentation, p: 0.35, desc: "Prolonged conflict leads to effective partition (5-15 years)"}
      - {id: eventual_settlement,    p: 0.25, desc: "Exhaustion leads to negotiated new order (10-20 years)"}
  - id: negotiated
    p: 0.15
    branches:
      - {id: successful_order,       p: 0.50, desc: "New constitutional arrangement proves durable"}
      - {id: failed_restructuring,   p: 0.50, desc: "New order fails; transitions to another resolution within 3-7 years"}
```

| Resolution | Probability | Description |
|------------|-------------|-------------|
| **Authoritarian Consolidation** | 30% | One faction gains control; constitutional order replaced |
| **Federal Fragmentation** | 25% | Federal authority not recognized; effective secession |
| **Prolonged Instability** | 30% | No faction gains control; extended period of conflict |
| **Negotiated Restructuring** | 15% | Constitutional convention produces new order |

The branches under each resolution are the aftermath branches specified below (their probabilities, durations, factor modifications and transition hazards are in the Aftermath Branches section); their IDs are unique across resolutions so that cascade conditions can name them with `branch == '...'`.

### Resolution Probability Rationale

**Entropy-maximized default**: 25% / 25% / 25% / 25%

**Structural deviation**:

| Resolution | Deviation | Rationale |
|------------|-----------|-----------|
| Authoritarian Consolidation | +5% (30%) | Historical pattern: breakdowns often produce authoritarian successor |
| Federal Fragmentation | 0% (25%) | Federalism creates plausible pathway; but geographic integration works against |
| Prolonged Instability | +5% (30%) | Modern civil conflicts tend toward prolonged stalemate |
| Negotiated Restructuring | -10% (15%) | Successful negotiated transitions from crisis are historically rare |

Maximum ratio is 2:1 (30:15), within guidelines.

### Resolution Descriptions

**Authoritarian Consolidation (30%)**

One faction gains control of federal apparatus and suppresses opposition:
- Executive consolidation with legislative/judicial acquiescence or marginalization
- Emergency powers invoked and normalized
- Opposition parties/movements suppressed or marginalized
- Elections continue but are not genuinely competitive

Historical models: Hungary post-2010 (softer), Venezuela post-1999 (harder). The key marker is that constitutional constraints no longer bind the ruling faction.

**Federal Fragmentation (25%)**

Federal authority not recognized by some states; effective secession or confederation:
- States refuse to recognize federal authority on major issues
- Federal enforcement capacity insufficient or unwilling
- Possible formal secession or de facto sovereignty
- Multiple governing authorities claim legitimacy

Historical models: Yugoslavia 1991 (violent fragmentation), Czechoslovakia 1993 (peaceful separation), USSR 1991 (mixed). US geography and economic integration make clean separation difficult.

**Prolonged Instability (30%)**

No faction gains decisive control; extended period of political violence and institutional dysfunction:
- Multiple factions compete for control
- Political violence becomes normalized
- Institutions function sporadically
- Economic activity severely disrupted

Historical models: Lebanon 1975-1990, Colombia 1948-1958 (La Violencia). This is arguably the worst resolution for human welfare.

**Negotiated Restructuring (15%)**

Crisis forces recognition that current constitutional order is untenable; new order negotiated:
- Constitutional convention or equivalent
- New institutional arrangements (parliamentary system? regional devolution?)
- Requires cross-partisan elite coalition recognizing mutual need for new framework

Historical models: South Africa 1990-1994 (successful transition), France 1958 (Fifth Republic). Rare but possible when all factions recognize deadlock.

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 2/3 Hybrid target (ΛΩΛᵀ)ᵢᵢ = 0.55*

```yaml
factors:
  F_FIN: 0.42   # Primary: Economic crises historically correlate with political instability
  F_GPT: 0.26   # Secondary: External pressure could unite or divide; historically unifying
  F_EAS: 0.15   # China tensions affect domestic politics; rally/polarize effects
  F_TECH: 0.10  # Technology platforms affect information environment; polarization channel
  F_EUR: 0.10   # European instability affects transatlantic alliance; modest feedback
  F_CLIM: 0.05  # Climate stress may exacerbate regional tensions; limited direct impact
  F_HLTH: 0.05  # Pandemic management became politically polarized; limited ongoing impact
  F_FOOD: 0.05  # Food security not a major US vulnerability
  F_MENA: 0.05  # Limited direct impact
  F_LAM: 0.05   # Migration politics create pressure; limited magnitude
variance: 0.55  # Type 2/3 Hybrid target (validation rule 0), not the Type 2 table value
```

F_SAS and F_SSA carry no loading (no direct linkage).

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.558 under the catalog Ω against the 0.55 target (compiler tolerance ±0.02); scale factor 1.03 from the original loadings.

**Correction (2026-10-22).** The 2025-12-21 specification documented loadings of F_FIN 0.36, F_GPT 0.22, F_EAS 0.13, F_TECH 0.09, F_EUR 0.09, F_CLIM/F_HLTH/F_FOOD/F_MENA/F_LAM 0.04, described as "scale factor = 0.89 from original loadings" to reach 0.55. Under Ω those loadings explain 0.409 of unit variance, and the original loadings they were scaled from (F_FIN 0.40, F_GPT 0.25, F_EAS 0.15, F_TECH 0.10, F_EUR 0.10, F_CLIM/F_HLTH/F_FOOD/F_MENA/F_LAM 0.045 — sum of squared loadings ≈ 0.28) explain 0.516 — or 0.523 if their minor loadings are read as 0.05 rather than 0.04/0.89, the reconstruction sim/README.md §4 item 10 first reported; the originals were never committed, so both are reconstructions from the documented set — and either way the originals were already *below* the target, so the 0.89 scaling moved them further from it. The scaling was applied in the wrong direction. The loadings above multiply the originals by √(0.55 / 0.516) ≈ 1.03 (equivalently the documented loadings by 1.16), which preserves the relative structure the rationale column argues for and reaches the documented target. The target itself is unchanged.

The lower loading sum reflects that US constitutional crisis is primarily domestically driven. External factors operate through domestic political channels rather than directly.

Lower loading sum reflects that US constitutional crisis is primarily domestically driven. External factors operate through domestic political channels rather than directly.

---

## Impact Vector

### Analog Basis

| Analog | Event Type | Key Observations | Relevance |
|--------|------------|------------------|-----------|
| **US Civil War (1861-1865)** | Constitutional breakdown → war | GDP -20% (South -40%); ~620K deaths; 4-year duration | Federal Fragmentation, Prolonged Instability |
| **Weimar Collapse (1933)** | Democratic breakdown → authoritarian | Rapid consolidation; opposition suppressed; economic recovery under authoritarianism | Authoritarian Consolidation |
| **USSR Collapse (1991)** | Federal fragmentation | GDP -40% over 5 years; nuclear security concerns; 15 successor states | Federal Fragmentation |
| **Yugoslavia (1991-95)** | Federal fragmentation → war | ~140K deaths; ~4M displaced; economic collapse | Federal Fragmentation, Prolonged Instability |
| **Venezuela (1999-present)** | Democratic erosion → authoritarian | GDP -65% cumulative; ~7M emigrants; prolonged decline | Authoritarian Consolidation |
| **South Africa (1990-94)** | Negotiated transition | Relatively successful; GDP initially flat then grew; limited violence | Negotiated Restructuring |

### Global Impacts (All Resolutions)

The US is the global hegemon, reserve currency issuer, and NATO anchor. All resolutions produce severe global consequences.

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usd_reserve_share` | ↓ | -15 ± 8 pp | delayed(1yr) | resolution_dependent | Dollar requires credible US governance |
| `nato_cohesion` | ↓ | -30 ± 12 points | immediate | resolution_dependent | US is NATO anchor |
| `nuclear_stability` | ↓ | -20 ± 10 points | immediate | resolution_dependent | ~5,500 warheads under uncertain command |
| `global_credit_spread` | ↑ | +150 ± 60 bps | immediate | decaying: half_life=2yr | Flight to safety reverses; Treasury haven status questioned |
| `us_10yr_yield` | ↑ | +200 ± 100 bps | immediate | resolution_dependent | Risk premium; possible Fed independence loss |
| `global_trade_volume` | ↓ | -8 ± 4% | delayed(6mo) | decaying: half_life=3yr | US is ~10% of world trade; supply chain disruption |
| `us_china_tension` | ↑/↓ | Resolution-dependent | immediate | resolution_dependent | See resolution-specific |
| `semiconductor_supply` | ↓ | -5 ± 3% | delayed(6mo) | decaying: half_life=2yr | US design capacity; supply chain routing |

### US Impacts (All Resolutions)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.regime_stability` | ↓ | Falls to <30 | immediate | resolution_dependent | Definitional |
| `usa.gdp_growth` | ↓ | -6 ± 3 pp | immediate | resolution_dependent | Crisis impact |
| `usa.institutional_quality` | ↓ | -1.5 ± 0.5 | immediate | resolution_dependent | Constitutional breakdown |
| `usa.state_capacity` | ↓ | -25 ± 12 points | immediate | resolution_dependent | Federal dysfunction |
| `usa.internal_conflict_intensity` | ↑ | +2 ± 1 levels | immediate | resolution_dependent | Political violence |
| `usa.reserves_foreign` | ↓ | -3 ± 2 months imports | gradual(1yr) | decaying: half_life=3yr | Capital flight |
| `usa.fdi_net` | ↓ | -2 ± 1 pp GDP | delayed(6mo) | resolution_dependent | Investment freeze |

### Resolution-Specific Impacts

#### Authoritarian Consolidation

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.regime_type` | — | Changes to Authoritarian | immediate | permanent | Definitional |
| `usa.civil_liberties` | ↓ | -40 ± 15 points | gradual(2yr) | permanent | Opposition suppression |
| `usa.regime_stability` | — | 50 ± 15 medium-term | gradual(3yr) | shock_vulnerable | Authoritarians can stabilize |
| `usa.gdp_per_capita` | ↓ | -10 ± 5% cumulative | gradual(5yr) | permanent | Institutional damage; Venezuela analog |
| `usd_reserve_share` | ↓ | -20 ± 10 pp | gradual(5yr) | permanent | Dollar credibility destroyed |
| `nato_cohesion` | ↓ | -40 ± 15 points | immediate | permanent | Alliance collapses or transforms |
| `us_china_tension` | — | Resolution-dependent | — | — | Authoritarian US may accommodate or confront |

#### Federal Fragmentation

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.gdp_real` | ↓ | -25 ± 10% cumulative | gradual(5yr) | permanent | USSR analog; supply chain disruption |
| `usa.regime_stability` | ↓ | Falls to <15 | immediate | N/A (state ceases to be unified) | Multiple successor entities |
| `nuclear_stability` (global) | ↓ | -35 ± 15 points | immediate | decaying: half_life=8yr | ~5,500 warheads; command fragmentation |
| `usd_reserve_share` | ↓ | -25 ± 10 pp | gradual(3yr) | permanent | Dollar regime ends |
| `nato_cohesion` | ↓ | Falls to <20 | immediate | permanent | Alliance collapses |
| `global_trade_volume` | ↓ | -15 ± 6% | delayed(1yr) | decaying: half_life=5yr | Major disruption |

**Successor entity note**: Fragmentation produces multiple successor states. Detailed modeling of successor entity trajectories is beyond Level 1; would require Level 2 scenario analysis.

#### Prolonged Instability

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.gdp_growth` | ↓ | -4 ± 2 pp sustained | immediate | duration of instability | Ongoing disruption |
| `usa.internal_conflict_intensity` | ↑ | Reaches 3-4 | immediate | duration of instability | Political violence normalized |
| `usa.regime_stability` | — | 15-30 range | — | fluctuating | No stable equilibrium |
| `nuclear_stability` (global) | ↓ | -25 ± 12 points | immediate | duration of instability | Command uncertainty |
| `global_credit_spread` | ↑ | +200 ± 80 bps sustained | immediate | duration of instability | Persistent uncertainty |

**Duration**: Prolonged Instability may last 5-15 years before transitioning to another resolution (Authoritarian Consolidation, Fragmentation, or Negotiated Restructuring). Model as: 10% annual probability of resolution, with resolution type sampled from remaining options.

#### Negotiated Restructuring

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.regime_type` | — | Changes (new constitutional order) | gradual(3yr) | permanent | By definition |
| `usa.regime_stability` | — | 45 ± 15 short-term | gradual(3yr) | shock_vulnerable | Transition instability |
| `usa.institutional_quality` | — | -0.5 ± 0.3 short-term | immediate | decaying: half_life=5yr | Institutional adjustment |
| `usa.civil_liberties` | — | ±10 points (uncertain direction) | gradual(5yr) | maintenance_required | Depends on new order |
| `usa.gdp_growth` | ↓ | -2 ± 1 pp short-term | immediate | decaying: half_life=3yr | Transition costs |
| `usd_reserve_share` | ↓ | -8 ± 5 pp | gradual(5yr) | shock_vulnerable | Credibility damaged but recoverable |
| `nato_cohesion` | ↓ | -15 ± 8 points | immediate | decaying: half_life=5yr | Alliance strains but may survive |

This is the least damaging resolution but also the least likely historically.

### Regional Impacts

#### NATO Allies (Europe, Canada, Australia, Japan, South Korea)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| All: `military_spending` | ↑ | +0.8 ± 0.4 pp GDP | gradual(3yr) | permanent | Security reassessment |
| All: `alliance_west` | ↓ | -20 ± 10 points | immediate | resolution_dependent | Anchor gone |
| `deu.gdp_growth` | ↓ | -1.0 ± 0.5 pp | delayed(6mo) | decaying: half_life=2yr | Trade/financial contagion |
| `jpn.gdp_growth` | ↓ | -1.5 ± 0.7 pp | delayed(6mo) | decaying: half_life=2yr | Higher exposure |
| `twn.regime_stability` | ↓ | -15 ± 8 points | immediate | resolution_dependent | Security guarantee questioned |

#### China

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.gdp_growth` | ↓ | -1.0 ± 0.5 pp | delayed(6mo) | decaying: half_life=2yr | Trade disruption |
| `chn.alliance_china` | — | Regional states reassess | gradual(2yr) | permanent | Multipolarity accelerates |
| TAIWAN_CONFLICT | ↑ | See cascade effects | — | — | Window may open |

#### Global South

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| Commodity exporters | ↓ | -5 to -15% export revenue | delayed(6mo) | decaying | US demand collapse |
| Dollar-indebted countries | ↑/↓ | Depends on dollar trajectory | — | — | Mixed effects |
| Remittance-dependent | ↓ | -15 ± 8% remittance flows | delayed(3mo) | decaying: half_life=3yr | US employment disruption |

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| Dollar reserve share loss | resolution_dependent | Authoritarian/Fragmentation: permanent; Negotiated: shock_vulnerable (vulnerable_to: GLOBAL_FINANCIAL_CRISIS, renewed political crisis; reversal_fraction: 0.5) | Credibility varies by resolution |
| GDP disruption | decaying | half_life=2-3yr | Markets adjust |
| Nuclear stability (Fragmentation) | decaying | half_life=8yr | New command structures establish |
| Institutional quality | resolution_dependent | Varies | Depends on successor regime |
| Alliance structures | permanent | — | Don't recover to status quo ante |
| Regime stability (Negotiated) | shock_vulnerable | vulnerable_to: economic crisis, renewed polarization, external conflict; reversal_fraction: 0.6 | New constitutional orders are fragile |
| Civil liberties (Negotiated) | maintenance_required | annual_failure_prob: 0.08; failure_conditions: authoritarian resurgence, security crisis | Reforms require ongoing defense |

### Differential Impact Specifications

**Exposure Variables:**

| Impact Category | Exposure Variable | Function | Effect |
|-----------------|-------------------|----------|--------|
| GDP contagion | `trade_openness` | Linear | Higher trade openness → larger GDP impact |
| Financial contagion | `debt_external` | Threshold (>50% GDP) | High external debt → amplified financial stress |
| Security reassessment | `alliance_west` | Linear | Higher Western alignment → larger security impact |
| Remittance disruption | `remittance_dependence` (derived) | Linear | Higher US remittance share → larger income shock |
| Dollar exposure | `reserves_foreign` composition | Linear | Higher USD reserve share → larger reserve value impact |

### Impacts (YAML)

The tables above are the original specification; the YAML re-expresses them against the state catalog. Each resolution's list carries the global, US and regional "all resolutions" rows plus its resolution-specific rows (they stack, as in CHINESE_POLITICAL_CRISIS — the resolution-specific tables add to, not replace, the all-resolutions tables). The first aftermath branch under each resolution carries the explicit list and the other branches inherit it at scale 1.0, because the specification distinguishes aftermath branches by factor modifications, duration and transition hazards (prose below), not by impact rows.

```yaml
impacts:
  authoritarian.stable_autocracy:
    # Global (all resolutions)
    - {var: usd_reserve_share,                   mag: [-15, 8],      onset: {delayed: 1}, permanent: true}
    - {var: global_credit_spread,                mag: [150, 60],     onset: immediate,    decay: 2}
    - {var: us_10yr_yield,                       mag: [2.0, 1.0],    onset: immediate,    permanent: true}
    - {var: global_trade_volume,                 mag: [-8, 4],       onset: immediate,    decay: 3}
    - {var: semiconductor_supply,                mag: [-5, 3],       onset: immediate,    decay: 2}
    # United States (all resolutions)
    - {var: usa.gdp_growth,                      mag: [-6, 3],       onset: immediate,    decay: 2}
    - {var: usa.public_investment_efficiency,    mag: [-30, 10],     onset: immediate,    permanent: true}
    - {var: usa.tax_revenue_gdp,                 mag: [-6, 3],       onset: immediate,    decay: 5}
    - {var: usa.internal_conflict_intensity,     mag: [2, 1],        onset: immediate,    decay: 5}
    - {var: usa.reserves_foreign,                mag: [-3, 2],       onset: {gradual: 1}, decay: 3}
    - {var: usa.fdi_net,                         mag: [-2, 1],       onset: immediate,    decay: 2}
    # US treaty allies (all resolutions)
    - {var: can.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: deu.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: gbr.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: fra.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: ita.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: esp.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: nld.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: pol.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: eu_other.military_spending,          mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: tur.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: aus.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: jpn.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: kor.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: can.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: deu.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: gbr.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: fra.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: ita.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: esp.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: nld.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: pol.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: eu_other.un_voting_alignment_us,     mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: tur.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: aus.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: jpn.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: kor.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    # Trade/financial contagion (all resolutions)
    - {var: deu.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    - {var: jpn.gdp_growth,                      mag: [-1.5, 0.7],   onset: immediate,    decay: 2}
    - {var: chn.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    # Authoritarian Consolidation
    - {var: usa.gdp_real,                        mag: [-0.10, 0.05], onset: {gradual: 5}, permanent: true}
    - {var: usd_reserve_share,                   mag: [-20, 10],     onset: {gradual: 5}, permanent: true}

  authoritarian.unstable_autocracy:
    inherit: authoritarian.stable_autocracy
    scale: 1.0

  fragmentation.peaceful_separation:
    # Global (all resolutions)
    - {var: usd_reserve_share,                   mag: [-15, 8],      onset: {delayed: 1}, permanent: true}
    - {var: global_credit_spread,                mag: [150, 60],     onset: immediate,    decay: 2}
    - {var: us_10yr_yield,                       mag: [2.0, 1.0],    onset: immediate,    permanent: true}
    - {var: global_trade_volume,                 mag: [-8, 4],       onset: immediate,    decay: 3}
    - {var: semiconductor_supply,                mag: [-5, 3],       onset: immediate,    decay: 2}
    # United States (all resolutions)
    - {var: usa.gdp_growth,                      mag: [-6, 3],       onset: immediate,    decay: 3}
    - {var: usa.public_investment_efficiency,    mag: [-30, 10],     onset: immediate,    permanent: true}
    - {var: usa.tax_revenue_gdp,                 mag: [-6, 3],       onset: immediate,    decay: 10}
    - {var: usa.internal_conflict_intensity,     mag: [2, 1],        onset: immediate,    decay: 10}
    - {var: usa.reserves_foreign,                mag: [-3, 2],       onset: {gradual: 1}, decay: 3}
    - {var: usa.fdi_net,                         mag: [-2, 1],       onset: immediate,    decay: 3}
    # US treaty allies (all resolutions)
    - {var: can.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: deu.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: gbr.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: fra.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: ita.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: esp.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: nld.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: pol.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: eu_other.military_spending,          mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: tur.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: aus.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: jpn.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: kor.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: can.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: deu.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: gbr.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: fra.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: ita.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: esp.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: nld.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: pol.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: eu_other.un_voting_alignment_us,     mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: tur.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: aus.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: jpn.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    - {var: kor.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    permanent: true}
    # Trade/financial contagion (all resolutions)
    - {var: deu.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    - {var: jpn.gdp_growth,                      mag: [-1.5, 0.7],   onset: immediate,    decay: 2}
    - {var: chn.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    # Federal Fragmentation
    - {var: usa.gdp_real,                        mag: [-0.25, 0.10], onset: {gradual: 5}, permanent: true}
    - {var: usd_reserve_share,                   mag: [-25, 10],     onset: {gradual: 3}, permanent: true}
    - {var: global_trade_volume,                 mag: [-15, 6],      onset: {delayed: 1}, decay: 5}

  fragmentation.violent_fragmentation:
    inherit: fragmentation.peaceful_separation
    scale: 1.0

  prolonged_instability.eventual_consolidation:
    # Global (all resolutions)
    - {var: usd_reserve_share,                   mag: [-15, 8],      onset: {delayed: 1}, decay: 10}
    - {var: global_credit_spread,                mag: [150, 60],     onset: immediate,    decay: 2}
    - {var: us_10yr_yield,                       mag: [2.0, 1.0],    onset: immediate,    decay: 10}
    - {var: global_trade_volume,                 mag: [-8, 4],       onset: immediate,    decay: 3}
    - {var: semiconductor_supply,                mag: [-5, 3],       onset: immediate,    decay: 2}
    # United States (all resolutions)
    - {var: usa.gdp_growth,                      mag: [-6, 3],       onset: immediate,    decay: 3}
    - {var: usa.public_investment_efficiency,    mag: [-30, 10],     onset: immediate,    decay: 10}
    - {var: usa.tax_revenue_gdp,                 mag: [-6, 3],       onset: immediate,    decay: 10}
    - {var: usa.internal_conflict_intensity,     mag: [2, 1],        onset: immediate,    decay: 10}
    - {var: usa.reserves_foreign,                mag: [-3, 2],       onset: {gradual: 1}, decay: 3}
    - {var: usa.fdi_net,                         mag: [-2, 1],       onset: immediate,    decay: 3}
    # US treaty allies (all resolutions)
    - {var: can.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: deu.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: gbr.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: fra.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: ita.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: esp.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: nld.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: pol.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: eu_other.military_spending,          mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: tur.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: aus.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: jpn.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: kor.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: can.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: deu.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: gbr.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: fra.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: ita.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: esp.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: nld.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: pol.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: eu_other.un_voting_alignment_us,     mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: tur.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: aus.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: jpn.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    - {var: kor.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 10}
    # Trade/financial contagion (all resolutions)
    - {var: deu.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    - {var: jpn.gdp_growth,                      mag: [-1.5, 0.7],   onset: immediate,    decay: 2}
    - {var: chn.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    # Prolonged Instability (sustained for the duration; resolves_after: 10)
    - {var: usa.gdp_growth,                      mag: [-4, 2],       onset: immediate,    until: resolved}
    - {var: global_credit_spread,                mag: [200, 80],     onset: immediate,    until: resolved}

  prolonged_instability.eventual_fragmentation:
    inherit: prolonged_instability.eventual_consolidation
    scale: 1.0

  prolonged_instability.eventual_settlement:
    inherit: prolonged_instability.eventual_consolidation
    scale: 1.0

  negotiated.successful_order:
    # Global (all resolutions)
    - {var: usd_reserve_share,                   mag: [-15, 8],      onset: {delayed: 1}, decay: 10}
    - {var: global_credit_spread,                mag: [150, 60],     onset: immediate,    decay: 2}
    - {var: us_10yr_yield,                       mag: [2.0, 1.0],    onset: immediate,    decay: 5}
    - {var: global_trade_volume,                 mag: [-8, 4],       onset: immediate,    decay: 3}
    - {var: semiconductor_supply,                mag: [-5, 3],       onset: immediate,    decay: 2}
    # United States (all resolutions)
    - {var: usa.gdp_growth,                      mag: [-6, 3],       onset: immediate,    decay: 2}
    - {var: usa.public_investment_efficiency,    mag: [-30, 10],     onset: immediate,    decay: 5}
    - {var: usa.tax_revenue_gdp,                 mag: [-6, 3],       onset: immediate,    decay: 3}
    - {var: usa.internal_conflict_intensity,     mag: [2, 1],        onset: immediate,    decay: 3}
    - {var: usa.reserves_foreign,                mag: [-3, 2],       onset: {gradual: 1}, decay: 3}
    - {var: usa.fdi_net,                         mag: [-2, 1],       onset: immediate,    decay: 2}
    # US treaty allies (all resolutions)
    - {var: can.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: deu.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: gbr.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: fra.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: ita.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: esp.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: nld.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: pol.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: eu_other.military_spending,          mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: tur.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: aus.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: jpn.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: kor.military_spending,               mag: [0.8, 0.4],    onset: {gradual: 3}, permanent: true}
    - {var: can.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: deu.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: gbr.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: fra.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: ita.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: esp.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: nld.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: pol.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: eu_other.un_voting_alignment_us,     mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: tur.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: aus.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: jpn.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    - {var: kor.un_voting_alignment_us,          mag: [-0.2, 0.1],   onset: immediate,    decay: 5}
    # Trade/financial contagion (all resolutions)
    - {var: deu.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    - {var: jpn.gdp_growth,                      mag: [-1.5, 0.7],   onset: immediate,    decay: 2}
    - {var: chn.gdp_growth,                      mag: [-1.0, 0.5],   onset: immediate,    decay: 2}
    # Negotiated Restructuring
    - {var: usa.public_investment_efficiency,    mag: [-10, 6],      onset: immediate,    decay: 5}
    - {var: usa.gdp_growth,                      mag: [-2, 1],       onset: immediate,    decay: 3}
    - {var: usd_reserve_share,                   mag: [-8, 5],       onset: {gradual: 5}, permanent: true}

  negotiated.failed_restructuring:
    inherit: negotiated.successful_order
    scale: 1.0
```

*Units: `gdp_real` rows are fractions of the entity's current value (−10% ± 5% under authoritarian consolidation, −25% ± 10% under fragmentation); all other rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields). `global_trade_volume` and `semiconductor_supply` are indices (2025 = 100), so the original −8% / −15% / −5% are −8 / −15 / −5 index points. `us_10yr_yield` is in percent, so +200 ± 100 bps is +2.0 ± 1.0. Sub-year onsets (delayed 3mo / 6mo) are `immediate` in the annual-step engine.*

#### Variable Substitutions and Dropped Rows

The state catalog eliminated the synthetic indices the original tables used ([[methodology/reference/state-variables-country]] §4, [[methodology/reference/state-variables-global]] §9). The YAML maps them as follows:

| Original row | YAML row | Mapping |
|--------------|----------|---------|
| `usa.institutional_quality` −1.5 ± 0.5 (all) and −0.5 ± 0.3 (negotiated) | `usa.public_investment_efficiency` −30 ± 10 and −10 ± 6 index points | Institutional quality → governance metrics, at 20 index points per WGI unit (the CHINESE_POLITICAL_CRISIS mapping) |
| `usa.state_capacity` −25 ± 12 points | `usa.tax_revenue_gdp` −6 ± 3 pp of GDP | State capacity → fiscal extraction capacity ([[methodology/concepts/synthetic-variable-problem]] §3.3). Conversion: 1 index point ≈ 0.25 pp of GDP, the 0-100 index spanning roughly the US general-government ~27%-of-GDP tax take (the Chinese event uses 0.2 for China's ~20%) |
| `usa.gdp_per_capita` −10 ± 5% cumulative (authoritarian) | `usa.gdp_real` −0.10 ± 0.05 | Per-capita and aggregate real GDP coincide absent a population change; only `gdp_real` carries the fraction-of-current-value convention, and `gdp_per_capita` is in $K with no stated baseline |
| ally `alliance_west` −20 ± 10 points | ally `un_voting_alignment_us` −0.2 ± 0.1 | Alignment scores → observable alignment indicators (the IRAN_NUCLEAR_ACQUISITION mapping); −20 on a 0-100 score is −0.2 on the −1 to +1 scale |
| "All NATO allies" rows | `can`, `deu`, `gbr`, `fra`, `ita`, `esp`, `nld`, `pol`, `eu_other`, `tur`, `aus`, `jpn`, `kor` | The specification's list (Europe, Canada, Australia, Japan, South Korea) realized on the catalog's entities; Turkey is included as a NATO member under "Europe" |
| `usd_reserve_share` −15 ± 8 (all, resolution_dependent) | kept, durability per resolution | Permanent under authoritarian and fragmentation per the durability table; `decay: 10` under prolonged instability (duration of instability) and under negotiated restructuring ("damaged but recoverable"), where the negotiated-specific −8 ± 5 row is the permanent structural loss. Stacked totals: −35 pp (authoritarian), −40 (fragmentation), −15 then recovering (prolonged), −23 of which −8 permanent (negotiated), against the catalog's 58% baseline |
| `nato_cohesion` −30 ± 12 (all), −40 ± 15, "falls to <20", −15 ± 8 | *dropped* | No catalog variable (the EU_FRAGMENTATION migration drops it the same way); the alliance channel is carried by the ally `military_spending` and `un_voting_alignment_us` rows |
| `nuclear_stability` −20 ± 10 (all), −35 ± 15 (fragmentation), −25 ± 12 (prolonged) | *dropped* | Derived output, not a state variable; the nuclear security channel stays in prose (Transmission Channel 3, Nuclear Security Cascade, Open Question 4) |
| `us_china_tension` | *dropped* | Derived output, not a state variable; resolution-dependent sign stays in prose |
| `usa.regime_stability` "falls to <30", 50 ± 15, "falls to <15", 15-30 range, 45 ± 15 | *dropped* | Level statements, not deltas (the Chinese event's "falls to <20" is dropped the same way). The engine should also reset `usa.years_since_irregular_transition` on firing — a reset is not expressible as an additive impact row in v0.1 |
| `usa.regime_type` changes (authoritarian, negotiated) and `usa.civil_liberties` −40 ± 15 / ±10 | *dropped* | `regime_type` is categorical and cannot take an additive magnitude; the catalog has no civil-liberties variable. Suppression and liberalization stay in prose |
| `usa.internal_conflict_intensity` "reaches 3-4" (prolonged) | *dropped* | Level statement; the all-resolutions +2 ± 1 row (held with a 10-year half-life under prolonged instability) carries it |
| `twn.regime_stability` −15 ± 8 | *dropped* | No observable in the catalog carries "security guarantee questioned"; the Taiwan effect is carried by the TAIWAN_CONFLICT cascade conditions |
| `chn.alliance_china` "regional states reassess" | *dropped* | No magnitude in the original |
| Global South rows (commodity exporters, dollar-indebted, remittance-dependent) | *dropped* | Differential-exposure classes, not entities; the exposure functions below stay in prose |

*Durability realization (v0.1)*: `maintenance_required` and `shock_vulnerable` are schema v0.2 backlog; the shock-vulnerable dollar row under negotiated restructuring is `permanent: true` (the CHINESE_POLITICAL_CRISIS realization). Rows the tables mark `resolution_dependent` take a durability per resolution: growth and FDI flows decay with the durability table's 2-3 year GDP half-life (2 under authoritarian and negotiated, 3 under fragmentation and prolonged instability); stock variables (yield, alignment, investment efficiency) are permanent under authoritarian consolidation and fragmentation, `decay: 10` under prolonged instability (the 5-15 year duration) and `decay: 5` under negotiated restructuring (the half-life the negotiated-specific rows use); tax revenue and conflict intensity take 5 / 10 / 10 / 3 years (authoritarian / fragmentation / prolonged / negotiated), the Chinese event's 3-year transformation and 10-year collapse half-lives bracketing them. The prolonged-instability "duration of instability" rows are `until: resolved` with `resolves_after: 10`. The original forms stay in the tables above.

---

## Aftermath Branches

*Factor modifications, the 10%-per-year transition hazard out of Prolonged Instability, the Unstable Autocracy and Failed Restructuring breakdown hazards, and the transition probabilities between resolutions are not expressible in the v0.1 schema; they stay here as the specification of record.*

### Authoritarian Consolidation — Aftermath

**Branch 1: Stable Autocracy (45%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Authoritarian regime consolidates and stabilizes; possible economic stabilization |
| **Duration** | Permanent regime change |
| **Factor modifications** | F_GPT: +0.3 for 10 years; F_FIN: +0.2 for 5 years |

- Opposition suppressed or co-opted
- Economic policy may stabilize (authoritarian efficiency)
- International isolation moderate (authoritarian US is still powerful)
- Model: Hungary, Turkey trajectories

**Branch 2: Unstable Autocracy (55%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Authoritarian regime faces ongoing resistance; economic decline |
| **Duration** | Potentially transitional (10% annual probability of further breakdown) |
| **Factor modifications** | F_GPT: +0.5 for 10 years; F_FIN: +0.4 for 10 years |

- Ongoing resistance; emigration
- Economic decline (Venezuela pattern)
- May transition to Prolonged Instability or Fragmentation
- Model: Venezuela trajectory

### Federal Fragmentation — Aftermath

**Branch 1: Peaceful Separation (25%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Successor states establish sovereignty without major armed conflict |
| **Duration** | Permanent restructuring |
| **Factor modifications** | F_GPT: +0.4 for 10 years; F_FIN: +0.3 for 5 years |

- Czechoslovakia model (but US is more integrated)
- Relatively orderly nuclear asset division
- Economic disruption severe but manageable
- Requires: elite consensus on separation terms

**Branch 2: Violent Fragmentation (75%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Armed conflict between successor entities |
| **Duration** | 5-15 years of conflict |
| **Factor modifications** | F_GPT: +0.8 for 15 years; F_FIN: +0.6 for 10 years |

- Yugoslavia model
- Nuclear security critical concern
- Humanitarian catastrophe (internal displacement, casualties)
- International intervention likely
- Model: Yugoslavia but larger scale

### Prolonged Instability — Aftermath

**Branch 1: Eventual Consolidation (40%)**

| Attribute | Value |
|-----------|-------|
| **Description** | One faction eventually gains control |
| **Duration** | 5-15 years until transition to Authoritarian Consolidation |
| **Factor modifications** | F_GPT: +0.6 for duration; F_FIN: +0.5 for duration |

**Branch 2: Eventual Fragmentation (35%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Prolonged conflict leads to effective partition |
| **Duration** | 5-15 years until transition to Fragmentation |
| **Factor modifications** | F_GPT: +0.7 for duration; F_FIN: +0.5 for duration |

**Branch 3: Eventual Negotiated Settlement (25%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Exhaustion leads to negotiated new order |
| **Duration** | 10-20 years until transition to Negotiated Restructuring |
| **Factor modifications** | F_GPT: +0.4 declining; F_FIN: +0.3 declining |

### Negotiated Restructuring — Aftermath

**Branch 1: Successful New Order (50%)**

| Attribute | Value |
|-----------|-------|
| **Description** | New constitutional arrangement proves durable |
| **Duration** | Permanent |
| **Factor modifications** | F_GPT: +0.1 for 5 years; F_FIN: +0.1 for 3 years |

- South Africa model (though different context)
- US GDP eventually recovers
- International role diminished but US remains major power
- Nuclear command stabilized

**Branch 2: Failed Restructuring (50%)**

| Attribute | Value |
|-----------|-------|
| **Description** | New order fails; transitions to another resolution |
| **Duration** | 3-7 years until failure |
| **Factor modifications** | F_GPT: +0.3 for duration; F_FIN: +0.2 for duration |
| **Transition probabilities** | Authoritarian: 40%, Fragmentation: 30%, Prolonged Instability: 30% |

- Weimar → Hitler pattern
- Post-USSR Russian democracy → Putin pattern
- Attempted reform creates opening for consolidation

---

## Cascade Effects

```yaml
cascades:
  triggers:
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.020,  years: 2}
    - {event: DOLLAR_RESERVE_CRISIS,     delta: 0.030,  years: 3}
    - {event: TAIWAN_CONFLICT,           delta: 0.015,  years: 3, if: "(resolution == 'fragmentation') or (resolution == 'prolonged_instability')"}
    - {event: TAIWAN_CONFLICT,           delta: -0.010, years: 3, if: "resolution == 'authoritarian'"}
    - {event: EU_FRAGMENTATION,          delta: 0.010,  years: 3}
    - {event: CHINESE_POLITICAL_CRISIS,  delta: -0.005, years: 5}
    - {event: KOREAN_PENINSULA_CRISIS,   delta: 0.015,  years: 3}
  triggered_by:
    - {event: GLOBAL_FINANCIAL_CRISIS,   delta: 0.015}
    - {event: SEVERE_PANDEMIC,           delta: 0.008}   # US origin or mishandled
    - {event: TAIWAN_CONFLICT,           delta: 0.010}   # US involvement; taiwan-conflict's own triggers list writes 0.005
```

The TAIWAN_CONFLICT edge is written as two mutually exclusive resolution-conditional rows; negotiated restructuring carries no edge, per the table below. `triggered_by` is informational (the source events' `triggers` lists are what the compiler reads): DOLLAR_RESERVE_CRISIS declares a +1.5% edge into this event that the table below does not list, and TAIWAN_CONFLICT declares +0.5% against the +1.0% here — a cross-file reconciliation item (sim/README.md §4 item 15).

### Triggered By

| Source Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 3 years | Economic stress; 1930s parallel |
| SEVERE_PANDEMIC (US origin or mishandled) | +0.8% | 2 years | Governance failure; polarization |
| TAIWAN_CONFLICT (US involvement) | +1.0% | 3 years | War losses; domestic backlash |

### Triggers

| Target Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +2.0% | 2 years | Reserve currency disruption; market panic |
| DOLLAR_RESERVE_CRISIS | +3.0% | 3 years | Dollar hegemony requires credible US governance |
| TAIWAN_CONFLICT | +1.5% (Fragmentation/Instability) OR -1.0% (Authoritarian) | 3 years | Depends on resolution; security guarantee collapses or authoritarian US confronts |
| EU_FRAGMENTATION | +1.0% | 3 years | NATO anchor gone; European security crisis |
| CHINESE_POLITICAL_CRISIS | -0.5% | 5 years | External pressure on China reduces |
| KOREAN_PENINSULA_CRISIS | +1.5% | 3 years | DPRK may see opportunity |

### Nuclear Security Cascade

All resolutions except Negotiated Restructuring (Successful) create nuclear security concerns:

| Resolution | Nuclear Risk | Mechanism |
|------------|--------------|-----------|
| Authoritarian Consolidation | Moderate | Command preserved but international norms may erode |
| Federal Fragmentation | **Severe** | ~5,500 warheads; who controls? Multiple successor states? |
| Prolonged Instability | **High** | Command uncertain during conflict |
| Negotiated Restructuring | Low-Moderate | Command likely preserved if transition orderly |

---

## Transmission Channels

### 1. Financial System Channel (Primary)

Dollar reserve currency status requires credible US governance. Constitutional breakdown destroys this credibility across most resolutions.

**Mechanism**: Treasury safe haven status questioned → reserve diversification accelerates → dollar depreciation → imported inflation globally → financial system restructuring

**Affected variables**: `usd_reserve_share`, `global_credit_spread`, `us_10yr_yield`, all country `reserves_foreign`

### 2. Alliance System Channel

US is anchor of NATO, hub of hub-and-spoke Asian alliances (Japan, South Korea, Australia, Philippines).

**Mechanism**: US commitment credibility collapses → allies reassess security posture → military spending increases → regional power vacuums → potential conflict

**Affected variables**: `nato_cohesion`, all ally `military_spending`, `alliance_west` for all aligned countries

### 3. Nuclear Security Channel

US has ~5,500 nuclear warheads. Constitutional breakdown creates command uncertainty.

**Mechanism**: Command authority disputed → adversary calculation changes → nuclear taboo potentially weakened → proliferation incentives change

**Affected variables**: `nuclear_stability`, all nuclear-capable country security postures

### 4. Trade and Supply Chain Channel

US is ~10% of world trade and hub for many supply chains.

**Mechanism**: Political disruption → trade disruption → supply chain rerouting → short-term shortages → long-term restructuring away from US

**Affected variables**: `global_trade_volume`, `semiconductor_supply`, all country `gdp_growth`

### 5. Demonstration Effect Channel

US has been model for democratic governance. Failure affects global democratic legitimacy.

**Mechanism**: US democracy fails → authoritarian narratives strengthened → democratic movements weakened → global democracy index declines

**Affected variables**: Global average `civil_liberties`, `institutional_quality`

---

## Probability Evolution (Type 2 Documentation)

### How Probability Changes Over Time

| Condition | Probability Modifier | Duration |
|-----------|---------------------|----------|
| Contested election (either party) | +1.5% | 2 years |
| Major political assassination | +2.0% | 3 years |
| Economic recession (GDP growth < -2%) | +1.0% | Duration + 2 years |
| Successful prosecution of major political figure | +0.5% | 2 years |
| Major political violence event (>50 casualties) | +1.5% | 3 years |
| Military refusing civilian command | +3.0% | 1 year (crisis window) |
| State formally defying Supreme Court | +2.0% | 2 years |

### Scenario: High-Pressure Path

If US experiences:
- Contested 2028 election (+1.5%)
- Economic recession (+1.0%)
- Major political violence (+1.5%)

Probability could temporarily reach 4-5% annually during crisis window.

---

## Case Against This Specification

Per critical review methodology, explicitly stating the strongest counterarguments:

### 1. American Exceptionalism (Institutional Resilience)

**Argument**: US institutions have absorbed extraordinary shocks — Civil War aftermath, Depression, Watergate, January 6. The system is more resilient than this specification credits.

**Response**: Valid concern. The threshold is set high (85) specifically to require actual breakdown, not just severe stress. However, past performance may not predict future resilience if underlying conditions have fundamentally changed (polarization, epistemic fragmentation, norm erosion).

### 2. Geographic Integration

**Argument**: Unlike 1860, there's no clear regional division. Blue and red America are geographically intermixed. This makes fragmentation much less plausible.

**Response**: Valid. Fragmentation probability (25%) may be too high. However, state-level governance creates natural units; federalism could enable regional coalitions. Fragmentation might not follow 1860 lines but could follow state boundaries.

### 3. Military Apolitical Tradition

**Argument**: US military has strong tradition of apolitical service. Officer corps is professionalized. Military intervention in politics is extremely unlikely.

**Response**: Valid. This is a major protective factor. However, constitutional crisis might not require military to act politically — it might require military to choose which civilian authority to obey. 2020-21 showed some stress on this norm.

### 4. Economic Performance

**Argument**: Depression-level economic stress historically precedes democratic breakdown. US economic performance is adequate. Without severe economic crisis, political crisis is unlikely.

**Response**: Partially valid. This is why GLOBAL_FINANCIAL_CRISIS is a major cascade trigger. However, high inequality, regional divergence, and declining social mobility create distributed stress even without headline crisis.

### 5. Elite Self-Interest

**Argument**: US elites benefit enormously from current system. They have strong incentives to prevent breakdown regardless of partisan affiliation.

**Response**: Valid. However, elite coordination failures are possible. Elites may believe they can win under breakdown conditions, or be captured by base pressures. Game-theoretic stability is not guaranteed.

### What Would Make Me Revise by 2x or More

- Evidence that 2020-21 stress was aberration rather than new normal → lower
- Military or major law enforcement institution openly defying civilian command → higher
- Successful violent attack on government with significant casualties → higher
- Clear evidence of foreign state successfully manipulating elections → higher
- Economic crisis with unemployment >15% → higher
- Cross-partisan elite coalition publicly committing to constitutional order → lower

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-12-21
  review: complete
  upgrade: true
```

**Revision note (2025-12-21)**: Initial specification. The critical review ("Case Against This Specification") was written into the initial specification rather than as a separate pass.

### Upgrade Rationale

Highest-stakes event in catalog; Level 2 could model specific scenarios (contested election, secession, military crisis).

## Sources

- Levitsky & Ziblatt — How Democracies Die
- Snyder — On Tyranny
- Walter — How Civil Wars Start
- Balkin — Constitutional Crises and Constitutional Rot
- Polity IV database — democratic breakdown patterns
- V-Dem — democratic backsliding indicators
- Historical analysis: 1850s-1860s, Weimar Republic, Venezuela
- [[methodology/reference/causal-types]]
- [[methodology/reference/type-3-calibration]]
- [[events/geopolitical/chinese-political-crisis]] (analogous structure)

## Open Questions

1. **Threshold calibration**: Is 85 the right threshold? US may be more or less resilient than China. The lack of historical precedent (post-1865) makes calibration difficult.

2. **Geographic vs. institutional fragmentation**: Would fragmentation follow state lines, or could institutions fragment within states? The specification assumes state-level fragmentation but this may not be the actual pattern.

3. **Military behavior**: In a scenario where civilian authorities dispute legitimacy, what does the military do? The specification assumes uncertainty; specific scenario modeling would help.

4. **Nuclear command in fragmentation**: What happens to nuclear weapons if federal authority fragments? This has never happened to a major nuclear power. USSR fragmentation provides partial precedent but was relatively orderly.

5. **International intervention**: Would foreign powers intervene in US constitutional crisis? The specification assumes limited intervention but major powers (China, Russia, EU) would have strong interests.

6. **Time-varying probability**: Probability likely increases during election cycles and decreases during periods of unified government. Current 0.5% is an average; true distribution may be cyclical.

7. **Interaction with Chinese Political Crisis**: If both US and China experience political crisis simultaneously, what happens? The specification treats these as negatively correlated (US crisis reduces pressure on China) but mutual crisis scenario is underspecified.

---

*Cross-references*: [[events/financial/global-financial-crisis]], [[events/financial/dollar-reserve-crisis]], [[events/geopolitical/taiwan-conflict]], [[events/geopolitical/eu-fragmentation]], [[methodology/reference/causal-types]], [[methodology/reference/type-3-calibration]]

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2026-10-22 | Migrated to YAML-embedded schema; factor loadings corrected | Task 4.2.19. **Loadings**: the documented loadings achieved 0.409 against the declared hybrid target 0.55 because the 2025-12-21 "scale factor 0.89" was applied in the wrong direction (the originals already explained 0.516, below the target); loadings are now the originals × 1.03 (achieved 0.558), the target is unchanged, and both prior sets are recorded under Factor Loadings (sim/README.md §4 item 10). **Causal type**: `causal_type: 2` for the Type 2/3 hybrid (the probability block implements pressure/threshold/sharpness/floor; the Type 3 component is the `resolutions:` block). **Pressure**: the synthetic `regime_stability` (0.30) realized as 0.15 × `press_freedom_events` ramp (saturating at 50/yr) + 0.15 × transition recency `1/(1+years/5)`; `institutional_quality` → `public_investment_efficiency` ramp (zero at 100, saturating at 50); `protest_activity` → `protest_intensity_annual`; growth as a shortfall ramp below 2%; wrapped `100 * (...)`; gives ~14 at plausible 2025 values against the prose's ~45-50 (gap recorded); sharpness 12, threshold 85 ± 10 and floor 0.15% written as documented. **Resolutions**: four resolutions carry their aftermath branches as `branches:` (45/55, 25/75, 40/35/25, 50/50); the first branch of each carries the explicit impact list, the others inherit at scale 1.0. **Impacts**: all-resolutions and resolution-specific rows stack; `resolution_dependent` durabilities realized per resolution (table under Impacts (YAML)); the prolonged-instability "duration of instability" rows are `until: resolved` with `resolves_after: 10` (midpoint of 5-15 years). **Substitutions**: `institutional_quality` → `public_investment_efficiency` (20 points per WGI unit); `state_capacity` → `tax_revenue_gdp` (0.25 pp per point); `gdp_per_capita` −10% → `gdp_real` −0.10; ally `alliance_west` → `un_voting_alignment_us`; the ally list realized as can/deu/gbr/fra/ita/esp/nld/pol/eu_other/tur/aus/jpn/kor. **Dropped rows** (channels kept in prose): `nato_cohesion`, `nuclear_stability`, `us_china_tension`, all `regime_stability` level statements, `regime_type` and `civil_liberties` (categorical / no variable), the prolonged "reaches 3-4" conflict level, `twn.regime_stability`, `chn.alliance_china`, the Global South exposure classes. **Units**: `global_trade_volume` −8% / −15% and `semiconductor_supply` −5% → index points; `us_10yr_yield` +200 bps → +2.0. **Onsets**: delayed 3mo/6mo → `immediate`. **Cascades**: all seven targets exist as files; TAIWAN_CONFLICT written as two resolution-conditional rows; cross-file `triggered_by` deltas (Dollar Reserve Crisis +1.5%, Taiwan +0.5%) noted, not reconciled. Research review recorded `complete` (the Case Against section is the critical review). No prose removed; git history holds a single prior commit (the initial specification), so nothing needed restoring |
| 2025-12-21 | Initial Level 1 specification | Task 2.1 geopolitical events (Additional Events round) |
