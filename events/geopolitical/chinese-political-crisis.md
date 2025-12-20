---
title: chinese-political-crisis
type: note
permalink: events/geopolitical/chinese-political-crisis
tags:
- event
- geopolitical
- type-2
- type-3
- hybrid
- china
- political-crisis
- level-1
---

# Chinese Political Crisis

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | CHINESE_POLITICAL_CRISIS |
| **Scale** | Global |
| **Domain** | Political |
| **Causal Type** | Type 2/3 Hybrid: Threshold + Contingent Resolution |
| **Onset Speed** | Rapid (crisis unfolds over 6-18 months) |
| **Reversibility** | Irreversible (all resolutions produce permanent state changes) |

## Description

Acute political instability exceeding normal CCP political processes, characterized by visible elite factional conflict, mass unrest beyond quiet suppression, or security apparatus fragmentation. This represents a discrete transition from "managed authoritarian stability" to "contested regime survival" — a threshold crossing that forces extraordinary response.

The event fires only when accumulated stress overwhelms normal CCP mechanisms (elite bargaining, controlled succession, localized repression). Per [[methodology/reference/causal-types]], smooth succession or crisis management through normal channels is NOT a discontinuity — it's sub-threshold stress. All resolutions must represent genuine discontinuities with permanent effects.

---

## Causal Type Specification

### Type 2/3 Hybrid Structure

This event combines threshold dynamics (Type 2) with contingent resolution (Type 3):

**Type 2 Component**: Pressure accumulates through legitimacy erosion, economic underperformance, elite conflict, and social unrest. At critical pressure level, crisis becomes likely.

**Type 3 Component**: Once crisis threshold is crossed, outcome depends on actor decisions (elite factions, military commanders, protest movements). Resolution probabilities are intractable per [[methodology/concepts/small-n-actor-problem]].

```
Pressure accumulates → Threshold crossed → Crisis fires →
Resolution sampled → Aftermath branches
```

### Pressure Function

The pressure function combines **state-variable-driven components** (observable, tracked by the simulation) with **exogenous parameters** (unobservable, modified only by discrete events or time-based triggers).

#### State-Variable Components (60% of pressure)

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `chn.regime_stability` | 0.20 | inverse | Composite legitimacy metric; captures accumulated erosion |
| `chn.gdp_growth` | 0.15 | deviation from 5% baseline | Performance legitimacy; CCP has conditioned expectations to ~5% growth |
| `chn.protest_activity` | 0.12 | linear | Observable unrest; proxy for social mobilization |
| `chn.unemployment_rate` | 0.08 | linear | Economic stress; correlates with youth unemployment |
| `chn.inflation_rate` | 0.05 | threshold (>5%) | Price instability erodes living standards |

**State-driven pressure contribution:**
```
P_state = 0.20 × (100 - regime_stability) / 100
        + 0.15 × max(0, (5 - gdp_growth)) / 5
        + 0.12 × protest_activity / 100
        + 0.08 × unemployment_rate / 20
        + 0.05 × max(0, (inflation_rate - 5)) / 10
```

All terms normalized to 0-1 range; sum weighted by component weights.

#### Exogenous Parameters (40% of pressure)

These parameters cannot be observed or derived from state variables. They are initialized at simulation start and modified only by specific events or time-based triggers.

| Parameter | Initial Value | Range | Modifying Events/Triggers |
|-----------|---------------|-------|---------------------------|
| `elite_cohesion` | 75 | 0-100 | CHINESE_ECONOMIC_CRISIS: -15 for 3yr; TAIWAN_CONFLICT (defeat): -20 for 5yr |
| `succession_uncertainty` | 25 | 0-100 | Leader age >80: +20; Leader incapacitation: +50; Successful succession: reset to 15 |

**Exogenous pressure contribution:**
```
P_exogenous = 0.25 × (100 - elite_cohesion) / 100
            + 0.15 × succession_uncertainty / 100
```

#### Combined Pressure Function

```
P_total = P_state + P_exogenous
```

Both components are on 0-1 scale; total pressure is 0-100 when multiplied by 100.

#### Exogenous Parameter Dynamics

**Elite Cohesion (`elite_cohesion`)**

Represents internal CCP factional alignment. Unobservable from outside; inferred only through visible purges, defections, or policy paralysis.

| Trigger | Effect | Duration | Mechanism |
|---------|--------|----------|-----------|
| CHINESE_ECONOMIC_CRISIS fires | -15 points | 3 years (then recovers 5/yr) | Economic failure creates blame dynamics; factions form around response |
| TAIWAN_CONFLICT (defeat/stalemate) | -20 points | 5 years (then recovers 4/yr) | Military failure triggers recrimination; hardliners vs. reformists |
| Time since last crisis | +2 points/decade (max 85) | Ongoing | Gradual consolidation absent shocks |

**Succession Uncertainty (`succession_uncertainty`)**

Represents clarity of power transition. Increases with leader age; spikes on incapacitation; resets on successful transition.

| Trigger | Effect | Duration | Mechanism |
|---------|--------|----------|-----------|
| Leader age 75-79 | Base +10 points | Ongoing | Actuarial risk increases |
| Leader age 80+ | Base +25 points | Ongoing | Mortality risk substantial |
| Leader incapacitation (hypothetical event) | +50 points | Until succession resolved | No clear successor; power vacuum |
| Successful succession | Reset to 15 | Permanent until next cycle | New leader consolidates |

**Implementation Note:** These parameters require event definitions for "leader incapacitation" and "successful succession" that don't currently exist in the event catalog. For Phase 2 implementation, they can be: (1) treated as fixed at initial values (simplified model), (2) implemented as time-varying functions of simulation year (leader age proxy), or (3) added as simple stochastic events (low priority).

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 80 on 0-100 scale | CCP has exceptional institutional capacity, surveillance technology, and financial resources; threshold substantially higher than typical authoritarian regime |
| **Uncertainty** | ±12 (range 68-92) | Regime opacity; apparent strength may mask fragility (or vice versa) |
| **Sharpness (k)** | 12 | Sharp transition once visible cracks appear — authoritarian regimes exhibit "sudden death" dynamics |
| **Historical calibration** | USSR 1989-91 (threshold breach → collapse); China 1989 (approached threshold, regime stabilized via extraordinary measures); Romania 1989 (rapid threshold breach) |

### Current Pressure Assessment (2025)

**Estimated pressure**: ~37 on 0-100 scale

| Component | Value | Contribution |
|-----------|-------|--------------|
| `chn.regime_stability` | ~70 | 0.20 × 0.30 = 0.06 |
| `chn.gdp_growth` | ~4.5% | 0.15 × 0.10 = 0.015 |
| `chn.protest_activity` | ~25 | 0.12 × 0.25 = 0.03 |
| `chn.unemployment_rate` | ~5% | 0.08 × 0.25 = 0.02 |
| `chn.inflation_rate` | ~2% | 0.05 × 0 = 0 |
| `elite_cohesion` (exogenous) | 75 | 0.25 × 0.25 = 0.0625 |
| `succession_uncertainty` (exogenous) | 25 | 0.15 × 0.25 = 0.0375 |
| **Total** | | **~0.37** (37 on 0-100 scale) |

Distance to threshold (~80) is substantial. Crisis is not imminent under current baseline conditions.

### Minimum Probability

**Floor**: 0.3% annually even at low pressure

Black swan triggers possible: failed assassination attempt, sudden leader incapacitation without succession plan, military incident producing civilian casualties and elite blame-shifting, or external shock (Taiwan conflict defeat) that catalyzes latent fissures.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 0.8% |
| **Low bound** | 0.4% |
| **High bound** | 1.5% |
| **Confidence** | Low |
| **25-year cumulative** | ~18% at point estimate |

### Derivation

**Step 1: Threshold distance analysis**

Current pressure (~37) is well below threshold (~80). Standard Type 2 logic suggests low annual probability at this distance. However, authoritarian regimes exhibit nonlinear threshold dynamics — pressure can accumulate rapidly during external shocks.

**Step 2: Pressure trajectory assessment**

Key pressure drivers:
- **Economic**: Property/LGFV stress increasing; growth deceleration structural (demographics)
- **Succession**: Xi aging (72 in 2025); no clear successor; concentration of power creates fragility
- **Elite dynamics**: Anti-corruption campaign has created enemies; succession will surface factional tensions
- **External**: US-China competition creating pressure; potential Taiwan flashpoint

Pressure likely increases ~1-2 points annually under baseline, reaching threshold zone (~70+) only in 2040s-2050s. But shocks (economic crisis, military defeat) could accelerate dramatically.

**Step 3: Reference class reasoning**

| Reference | Outcome | Annual Crisis Rate | Relevance |
|-----------|---------|-------------------|-----------|
| USSR 1922-1991 | Collapse | ~1.4% (1 in 69 years) | High institutional capacity; still collapsed |
| China 1949-present | Near-crisis 1989; no collapse | ~1.3% for near-crisis | Same regime; survived |
| Single-party states generally | Variable | ~2% for significant instability | Broad reference class |

CCP has survived 75+ years — longer than USSR. But regime age itself may be pressure factor (institutional sclerosis, accumulated grievances).

**Step 4: Conditional probability from Chinese Economic Crisis**

[[events/financial/chinese-economic-crisis]] specifies +2.0% probability modifier lasting 5 years. Given Chinese Economic Crisis has ~2.0% annual probability, the contribution is:
- P(econ crisis) × P(political crisis | econ crisis modifier) ≈ 2% × 2% = 0.04% additional

This is already captured in the pressure function through `chn.regime_stability` degradation.

**Step 5: Expert/structural reasoning**

Most China experts assess CCP as stable for foreseeable future, but acknowledge:
- Succession is the critical vulnerability
- Economic legitimacy is under strain
- Xi's power concentration creates single-point-of-failure risk
- Surveillance technology has shifted balance toward regime

**Step 6: Final estimate**

Given:
- Large threshold distance under current conditions
- Structural pressure increasing slowly
- Low but non-zero black swan risk
- Regime has exceptional resources but also exceptional opacity

**Point estimate: 0.8% annually** with range 0.4-1.5%.

This is deliberately conservative. The event fires only when normal CCP processes fail — a high bar. Lower than typical "regime change" estimates because we're modeling genuine discontinuity, not normal political stress.

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]]:
- Less likely than: Russia State Failure (~1.0%), Turkey Political Crisis (~1.0%)
- Similar to: Saudi Regime Instability (~0.8%)
- More likely than: AMOC Weakening (~0.5%)

Rationale: CCP has more resources than Saudi Arabia (hence similar probability despite greater apparent stability), but fewer than the already-stressed Russia/Turkey regimes.

### Key Uncertainties

**Factors that could push probability higher**:
- Chinese Economic Crisis occurs (cascade: +2.0% for 5 years)
- Taiwan conflict defeat/humiliation (cascade: +3.0% for 3 years)
- Xi incapacitation without succession plan
- Elite factional conflict becomes visible
- Mass unrest exceeds 1989 scale

**Factors that could push probability lower**:
- Successful economic transition to consumption model
- Smooth managed succession
- Continued surveillance/control effectiveness
- External threats unify elite (rally effect)

---

## Resolution Specification (Type 3 Component)

Once the crisis threshold is crossed, one of three resolutions occurs. Per [[methodology/reference/type-3-calibration]], resolution probabilities use entropy maximization with structural deviation.

### Resolution Branches

| Resolution | Probability | Description |
|------------|-------------|-------------|
| **Stabilization via Extraordinary Measures** | 50% | Crisis suppressed through means beyond normal CCP operations |
| **Regime Transformation** | 20% | Crisis forces genuine system change |
| **Regime Collapse** | 30% | CCP loses power entirely |

### Resolution Probability Rationale

**Entropy-maximized default**: 33% / 33% / 33%

**Structural deviation justification**:

| Factor | Direction | Strength |
|--------|-----------|----------|
| Activation energy: Transformation/collapse require sustained mobilization; stabilization requires only elite coordination + security loyalty | Favors stabilization | Moderate |
| Historical pattern: Tiananmen 1989, Belarus 2020, Myanmar 2021 — regimes double down more often than liberalize | Favors stabilization | Moderate |
| Institutional capacity: CCP has exceptional organizational resources | Favors stabilization | Moderate |
| Technology: Surveillance advantages incumbents | Favors stabilization | Moderate |
| Nuclear arsenal: Military unlikely to allow fragmentation | Disfavors collapse | Weak |
| Crisis severity: If threshold crossed, regime may lack resources for transformation | Disfavors transformation | Weak |

**Proposed deviation**: 50% / 20% / 30%

Maximum ratio is 2.5:1 (Stabilization:Transformation), slightly exceeding the 2:1 guideline. Justification: the historical pattern of authoritarian crisis response is strongly asymmetric — regimes that face genuine crisis almost always either crush it or fall; successful reform under pressure is rare.

### Resolution Descriptions

**Stabilization via Extraordinary Measures (50%)**

Crisis suppressed through means beyond normal CCP operations:
- Martial law declared; PLA deployed against civilians
- Mass purges exceeding Xi-era anti-corruption scope
- Permanent information lockdown (not temporary censorship)
- Potential elimination of remaining institutional constraints (NPC, courts)

This is a discontinuity because the regime survives but is fundamentally changed — "CCP" continues in name but governance mode shifts toward pure security state.

**Regime Transformation (20%)**

Crisis forces genuine system change:
- Liberalization under pressure (elite faction seeks legitimacy through reform)
- Power-sharing arrangement (factional federation, constitutional constraints)
- Fundamental restructuring of party-state relationship

This is rare but not unprecedented: Taiwan (1980s-90s), South Korea (1987), and to some extent USSR under Gorbachev attempted reform under pressure. Usually fails, but sometimes succeeds.

**Regime Collapse (30%)**

CCP loses power entirely:
- Revolutionary transition (mass movement overthrows regime)
- State fragmentation (regional power centers emerge; Tibet/Xinjiang/Taiwan implications)
- Military takeover (PLA assumes direct control; praetorian state)

Collapse doesn't mean the state disappears — successor regime(s) emerge with uncertain character.

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.10 | Climate stress affects rural stability, food security, regional inequality |
| F_FIN | 0.40 | **Primary**: Economic conditions are core legitimacy input; global financial stress amplifies domestic vulnerabilities |
| F_HLTH | 0.10 | Pandemic management affects governance perceptions; COVID legacy |
| F_GPT | 0.35 | **Secondary**: Great power tension affects nationalist legitimacy; foreign pressure can unify or fracture elite |
| F_FOOD | 0.15 | Food security affects rural stability; historical sensitivity (Great Leap Forward memory) |
| F_TECH | 0.10 | Technology competition affects development narrative; semiconductor restrictions |
| F_EUR | 0.05 | European economic/political stress has limited direct impact on China |
| F_MENA | 0.0 | No direct linkage |
| F_SAS | 0.05 | Border tensions (India) create external pressure; limited internal effect |
| F_EAS | 0.30 | Regional dynamics affect legitimacy; Taiwan/Korea/Japan situations (excluding China-caused component) |
| F_SSA | 0.0 | No direct linkage |
| F_LAM | 0.0 | No direct linkage |

**Sum of squared loadings**: 0.16 + 0.1225 + 0.01 + 0.01 + 0.0225 + 0.01 + 0.0025 + 0.0025 + 0.09 = **0.43** ✓

### Loading Rationale

Lower loading sum (~0.43) reflects that Chinese political crisis is more domestically-driven than externally-driven. International factors matter (F_FIN, F_GPT, F_EAS) but core dynamics are internal: elite cohesion, succession, social contract.

**F_FIN (0.40)**: Global financial stress is the primary external factor because CCP legitimacy rests heavily on economic performance. High F_FIN years create external demand shocks, capital flight pressure, and reduce policy space. The factor operates through `chn.gdp_growth` and `chn.unemployment` which feed the pressure function.

**F_GPT (0.35)**: Great power tension affects China through trade restrictions, technology access, and geopolitical pressure. Can have complex effects — external threat may unify elite (reduce pressure) or create scapegoats when policies fail (increase pressure). Net effect is pressure-increasing because it constrains economic options.

**F_EAS (0.30)**: Regional stress (Korea, Japan, Taiwan situations not caused by China) affects trade, investment, and creates external policy challenges. High F_EAS years may see regional instability that complicates Chinese foreign policy and creates opportunities for elite blame-shifting.

---

## Impact Vector

### Analog Basis for Magnitude Estimates

Impact magnitudes are derived from historical analogs and transmission analysis, not invention. Key reference cases:

| Analog | Event Type | Key Observations | Relevance |
|--------|------------|------------------|-----------|
| **USSR Collapse (1991)** | Regime collapse + fragmentation | GDP -40% over 5 years (Russia); ~25M displaced across former USSR; nuclear command fragmented then reconsolidated | Collapse branches |
| **Indonesia 1998** | Economic-political crisis | GDP -13% single year; Suharto fell; minimal territorial change; 2-3 year recovery | Transformation branch |
| **Tiananmen 1989** | Stabilization via repression | GDP growth dip ~2pp for 2 years; international sanctions ~3 years; no regime change | Stabilization branch |
| **Russia post-2022** | International isolation analog | Sanctions level ~70-80; GDP -2% to -5%; permanent growth penalty ~1-2pp | Isolation effects |
| **Yugoslavia 1991-95** | State fragmentation | Multiple successor states; ~140K deaths; ~4M displaced; 5+ year conflict | Fragmentation branch |
| **South Korea 1987** | Successful transformation | Democratic transition; GDP growth accelerated post-transition; international integration improved | Transformation success case |

### Global Impacts (All Resolutions)

Immediate effects of crisis onset, before resolution is determined.

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `us_china_tension` | ↑ | +25 ± 10 points (0-100 scale) | immediate | resolution_dependent | Chinese instability increases great power uncertainty; cf. Russia 1991 elevated tensions |
| `global_trade_volume` | ↓ | -6 ± 3% | delayed(6mo) | decaying: half_life=3yr | China is ~15% of world trade; supply chain disruption + demand collapse; USSR collapse saw ~10% FSU trade collapse |
| `nuclear_stability` | ↓ | -15 ± 8 points (0-100 scale) | immediate | resolution_dependent | Command uncertainty during political crisis; cf. USSR 1991 nuclear concerns |
| `global_credit_spread` | ↑ | +80 ± 40 bps | immediate | decaying: half_life=1yr | 2008 GFC saw +300bps; this is second-largest economy, expect ~25% of that magnitude |
| `semiconductor_supply` | ↓ | -8 ± 4% | delayed(3mo) | decaying: half_life=2yr | China is ~25% of semiconductor demand; supply chain uncertainty; less severe than Taiwan conflict |

### China Impacts (All Resolutions)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.gdp_growth` | ↓ | -4 ± 2 pp | immediate | resolution_dependent | Indonesia 1998: -13% GDP (but from financial crisis); Tiananmen: ~2pp dip; midpoint for political crisis |
| `chn.regime_stability` | ↓ | -35 ± 12 points (0-100) | immediate | resolution_dependent | By definition, crisis crossing means regime stability severely degraded |
| `chn.state_capacity` | ↓ | -20 ± 10 points (0-100) | immediate | resolution_dependent | State resources diverted to crisis management; institutional function degraded |
| `chn.reserves_foreign` | ↓ | -6 ± 3 months of imports | gradual(1yr) | decaying: half_life=3yr | Capital flight depletes reserves; China has ~15mo baseline; could lose 30-50% |
| `chn.current_account` | ↓ | -4 ± 2 pp GDP | delayed(6mo) | decaying: half_life=2yr | Trade disruption + capital flight; cf. Asian crisis countries |
| `chn.fdi_net` | ↓ | -3 ± 1.5 pp GDP | delayed(6mo) | resolution_dependent | Investment freeze during uncertainty; Indonesia 1998 saw FDI collapse |

### Resolution-Specific Impacts

#### Stabilization via Extraordinary Measures

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.regime_stability` | — | Recovers to 55 ± 10 (from crisis low ~30) | gradual(2yr) | permanent | Security state achieves stability but at lower baseline; cf. Belarus post-2020 |
| `chn.state_capacity` | ↓ | -15 ± 8 (permanent, from pre-crisis) | gradual(1yr) | permanent | Security focus crowds out developmental capacity; North Korea model |
| `chn.civil_liberties` | ↓ | -25 ± 10 points (0-100) | immediate | permanent | Martial law, information lockdown, political repression |
| `chn.sanctions_level` | ↑ | +40 ± 15 points (0-100) | delayed(6mo) | permanent | International response to repression; cf. Russia post-2022 (~70-80), Myanmar post-2021 |
| `chn.gdp_growth` | ↓ | -1.5 ± 0.5 pp (permanent trajectory) | gradual(2yr) | permanent | Security overhead + isolation penalty; Russia post-2022 ~1-2pp permanent loss |
| `chn.fdi_net` | ↓ | -2 ± 1 pp GDP (permanent) | gradual(1yr) | permanent | International isolation deters investment; sanctions effect |

Regime survives but at cost: reduced economic dynamism, international isolation, permanent security state overhead.

#### Regime Transformation

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.regime_stability` | — | 40 ± 15 short-term; trajectory uncertain | gradual(3yr) | shock_vulnerable | Transition creates instability; South Korea 1987-92 was rocky |
| `chn.state_capacity` | ↓ | -10 ± 8 short-term | gradual(2yr) | shock_vulnerable | Institutional restructuring reduces near-term effectiveness |
| `chn.civil_liberties` | ↑ | +25 ± 15 points (0-100) | gradual(5yr) | maintenance_required: annual_failure_prob=0.05 | Liberalization gains; Taiwan/Korea path; reversible |
| `chn.sanctions_level` | ↓ | -15 ± 8 points (0-100) | delayed(1yr) | maintenance_required | International engagement improves; contingent on continued reform |
| `chn.gdp_growth` | — | High uncertainty: -1 to +2 pp vs. baseline | gradual(3yr) | shock_vulnerable | Reform could unlock growth (Taiwan) or create chaos (USSR); wide range |

High variance outcome. Could be Taiwan/South Korea path (successful democratization, economic growth) or could be unstable transition that fails.

#### Regime Collapse

Collapse impacts depend on aftermath branch (Revolutionary Transition, State Fragmentation, Military Takeover). Common immediate effects:

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.regime_stability` | ↓ | Falls to <20 (regime ceases to exist in prior form) | immediate | N/A | Definitional |
| `chn.gdp_real` | ↓ | -20 ± 8% (cumulative over transition) | gradual(3yr) | permanent | USSR: -40% over 5 years; Yugoslavia: -25%; China larger/more integrated |
| `chn.state_capacity` | ↓ | -40 ± 15 points (0-100) | immediate | decaying: half_life=10yr | State institutions collapse; rebuilding takes decade+ |
| `chn.institutional_quality` | ↓ | -1.5 ± 0.5 (on -2.5 to +2.5 scale) | immediate | decaying: half_life=15yr | Institutional destruction; Russia took 15+ years to partial recovery |

**State Fragmentation branch additional impacts:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `nuclear_stability` (global) | ↓ | -35 ± 15 points | immediate | decaying: half_life=5yr | Multiple actors may control arsenal portions; USSR precedent but more warheads |
| `active_major_conflicts` (global) | ↑ | +2 ± 1 | delayed(1yr) | decaying: half_life=10yr | Internal conflicts in fragmenting state; cf. Yugoslavia |

### Regional Impacts

#### East Asia (Japan, South Korea)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `jpn.gdp_growth` | ↓ | -1.5 ± 0.8 pp | delayed(3mo) | decaying: half_life=2yr | China is Japan's largest trade partner (~25% exports); demand shock |
| `kor.gdp_growth` | ↓ | -2.0 ± 1.0 pp | delayed(3mo) | decaying: half_life=2yr | Korea more China-dependent than Japan (~30% exports) |
| `jpn.military_spending` | ↑ | +0.4 ± 0.2 pp GDP | gradual(2yr) | permanent | Security reassessment; already trending up |
| `kor.military_spending` | ↑ | +0.5 ± 0.3 pp GDP | gradual(2yr) | permanent | Peninsula uncertainty; North Korea opportunism risk |

#### Taiwan

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `twn.gdp_growth` | ↓ | -3.0 ± 1.5 pp | immediate | decaying: half_life=2yr | Cross-strait trade disruption; uncertainty premium |
| `twn.regime_stability` | — | Resolution-dependent; see Cascade Effects | — | — | Stabilization increases threat; Collapse (Fragmentation) reduces it |
| `twn.alliance_west` | ↑ | +10 ± 5 points (0-100) | gradual(1yr) | permanent | Accelerated US/Western engagement regardless of resolution |

#### United States

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.gdp_growth` | ↓ | -0.6 ± 0.3 pp | delayed(6mo) | decaying: half_life=2yr | Trade disruption, financial contagion; US less China-exposed than East Asia |
| `usa.military_spending` | ↑ | +0.3 ± 0.2 pp GDP | gradual(2yr) | permanent | Strategic reassessment regardless of resolution |

### Hong Kong Note

Hong Kong is not a separately modeled entity in the 40-country framework. Its fate is analytically important but tracked narratively rather than through state variables:

- **Stabilization**: Hong Kong autonomy eliminated; full mainland integration
- **Transformation**: Possible restoration of some autonomy under reformist leadership
- **Collapse (Fragmentation)**: Status contested; possible de facto independence or contested control

Economic effects on Hong Kong are partially captured through `chn.gdp_real` (Hong Kong is ~2% of China's GDP) and through global financial variables (Hong Kong as financial hub).

### Cascade Effects on Territorial Outcomes

Territorial integrity is not a continuous state variable but a discrete outcome. The State Fragmentation aftermath branch triggers cascade effects on other events:

| Cascade Target | Effect | Mechanism |
|----------------|--------|-----------|
| TAIWAN_CONFLICT | -1.5% for 5 years | No unified state to mount invasion; de facto independence |
| (Future) TIBETAN_INDEPENDENCE | Would trigger if event existed | Power vacuum enables separatism |
| (Future) XINJIANG_CONFLICT | Would trigger if event existed | Similar dynamics |
| PAKISTAN_STATE_FAILURE | +1.0% for 5 years | CPEC collapses; Chinese support capacity eliminated |

These cascade targets represent gaps in the current event catalog. For Phase 2.3 (Additional Events), consider adding events for regional separatism contingent on Chinese state weakness.

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| Regime stability (Stabilization) | permanent | — | Security state is a new equilibrium |
| Sanctions/isolation (Stabilization) | permanent | — | Relationships fundamentally damaged; cf. Russia post-2022 |
| Growth trajectory (Stabilization) | permanent | — | Security overhead and isolation are structural |
| Civil liberties gains (Transformation) | maintenance_required | annual_failure_prob: 5% | Reforms can be reversed under stress |
| GDP disruption (all branches) | decaying | half_life=2-3yr | Markets adjust; investment returns |
| Nuclear stability (Collapse) | decaying | half_life=5yr | New command structures eventually establish |
| Institutional quality (Collapse) | decaying | half_life=15yr | Institutions rebuild slowly; Russia reference |
| State capacity (Collapse) | decaying | half_life=10yr | Government effectiveness recovers gradually |

---

## Aftermath Branches

Each resolution triggers one of several post-event trajectories.

### Stabilization via Extraordinary Measures — Aftermath

**Branch 1: Consolidated Hard Authoritarianism (60%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Permanent security state; North Korea-lite governance model; severe international isolation |
| **Duration** | Permanent regime change |
| **Factor modifications** | F_GPT: +0.2 for 10 years; F_EAS: +0.2 for 10 years |

Aftermath impacts:
- CCP survives but is fundamentally transformed
- Economic dynamism permanently reduced
- International isolation comparable to Russia post-2022
- Taiwan pressure likely increases (nationalism as legitimacy substitute)
- Human rights situation severely deteriorated

**Branch 2: Unstable Repression (40%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Regime survives but faces ongoing resistance; periodic crackdowns; economic stagnation |
| **Duration** | 10-20 years until second crisis |
| **Factor modifications** | F_GPT: +0.3 for 5 years; F_EAS: +0.25 for 5 years |
| **Second crisis probability** | 3% annually for 15 years |

Aftermath impacts:
- Pyrrhic victory: regime survives but weakened
- Cycle of unrest and crackdown
- Economic stagnation from control costs
- Elite may eventually fracture under sustained pressure

### Regime Transformation — Aftermath

**Branch 1: Successful Liberalization (40%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Genuine power-sharing emerges; possible democratic transition over 10-20 years |
| **Duration** | Transition period 10-20 years |
| **Factor modifications** | F_GPT: -0.1 for 10 years; F_EAS: -0.15 for 10 years |

Aftermath impacts:
- Taiwan situation potentially resolved peacefully
- Economic liberalization may accelerate growth
- International integration improves
- Uncertain domestic stability during transition
- Model: Taiwan 1980s-90s, South Korea post-1987

**Branch 2: Unstable Transition (60%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Reform opens space for further instability; potential second crisis within 5 years |
| **Duration** | 3-7 years until second crisis or stabilization |
| **Factor modifications** | F_GPT: +0.15 for 5 years; F_EAS: +0.2 for 5 years |
| **Second crisis probability** | 8% annually for 5 years |

Aftermath impacts:
- Reform faction loses control
- Possible reversion to authoritarianism or acceleration to collapse
- Economic uncertainty depresses investment
- Model: USSR 1989-91 (reform → collapse)

### Regime Collapse — Aftermath

**Branch 1: Revolutionary Transition (35%)**

| Attribute | Value |
|-----------|-------|
| **Description** | New unified regime emerges; character uncertain |
| **Duration** | Transition 2-5 years; new regime permanent |
| **Factor modifications** | F_GPT: +0.4 for 5 years; F_EAS: +0.35 for 5 years |

Aftermath impacts:
- Successor regime could be: democratic, nationalist authoritarian, military, or hybrid
- Territorial integrity likely maintained (strong state persists)
- Taiwan: depends on successor regime orientation
- Nuclear weapons: chain of command preserved

**Branch 2: State Fragmentation (35%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Regional power centers emerge; civil conflict risk |
| **Duration** | 5-15 years of instability |
| **Factor modifications** | F_GPT: +0.6 for 10 years; F_EAS: +0.5 for 10 years; F_FIN: +0.3 for 5 years |

Aftermath impacts:
- Tibet, Xinjiang likely declare independence or face intervention
- Taiwan: de facto independence; question of formal recognition
- Nuclear weapons: **critical security concern** — multiple actors may control portions of arsenal
- Massive refugee flows (10M+)
- Civil conflict in contested regions
- Global trade severely disrupted
- Model: USSR collapse but more violent; Yugoslavia but larger

**Branch 3: Military Takeover (30%)**

| Attribute | Value |
|-----------|-------|
| **Description** | PLA assumes direct control; praetorian state |
| **Duration** | Permanent regime change |
| **Factor modifications** | F_GPT: +0.45 for 10 years; F_EAS: +0.4 for 10 years |

Aftermath impacts:
- Military government with uncertain civilian interface
- Taiwan: risk may increase (military more likely to view force as solution)
- Nuclear weapons: chain of command preserved under military
- Economic policy uncertain; likely nationalist/autarkic
- International relations severely strained

---

## Cascade Effects

### Triggered By (Probability Increases)

| Source Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| CHINESE_ECONOMIC_CRISIS | +2.0% | 5 years | Performance legitimacy failure; elite blame-shifting; mass unemployment |
| TAIWAN_CONFLICT (defeat) | +3.0% | 3 years | Nationalist legitimacy failure; military humiliation; elite recrimination |
| TAIWAN_CONFLICT (stalemate) | +1.0% | 3 years | Costly non-victory; economic damage; blame dynamics |
| SEVERE_PANDEMIC (China origin) | +1.0% | 2 years | Governance failure narrative; COVID precedent |
| GLOBAL_FINANCIAL_CRISIS | +0.5% | 2 years | External shock reduces policy space; amplifies domestic stress |

### Triggers (Cascade Effects on Other Events)

| Target Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 2 years | Chinese political uncertainty triggers capital flight, market panic |
| DOLLAR_RESERVE_CRISIS | -0.5% | 3 years | Yuan alternative less viable; flight to dollar safety |
| KOREAN_PENINSULA_CRISIS | +1.0% | 3 years | DPRK may see opportunity in Chinese distraction; ROK uncertainty |
| PAKISTAN_STATE_FAILURE | +0.5% | 3 years | Reduced Chinese support capacity; CPEC jeopardized |
| TAIWAN_CONFLICT | Complex; see below | — | Resolution-dependent effects |

### Taiwan Conflict Interaction

The relationship is bidirectional and resolution-dependent:

**Chinese Political Crisis → Taiwan Conflict:**

| Resolution | Effect on Taiwan Conflict | Mechanism |
|------------|--------------------------|-----------|
| Stabilization (Extraordinary) | +0.8% for 5 years | Hardened regime uses nationalism; diversionary incentive |
| Regime Transformation | -0.5% for 5 years | Liberalizing leadership less likely to use force |
| Regime Collapse (Revolutionary) | +0.3% for 3 years | New nationalist regime may seek legitimacy through Taiwan |
| Regime Collapse (Fragmentation) | -1.5% for 5 years | No unified state to mount invasion; Taiwan effectively independent |
| Regime Collapse (Military) | +1.0% for 5 years | Military regime more likely to view force as solution |

**Taiwan Conflict → Chinese Political Crisis:**

| Taiwan Outcome | Effect on Political Crisis | Duration |
|----------------|---------------------------|----------|
| Victory (reunification) | -1.0% | 5 years | Regime legitimacy reinforced |
| Defeat/Humiliation | +3.0% | 3 years | Nationalist legitimacy shattered; elite blame |
| Stalemate | +1.0% | 3 years | Costly non-victory; blame dynamics |

---

## Transmission Channels

### 1. Elite Cohesion Channel (Primary)

**Mechanism**: Crisis stress exposes and amplifies elite factional divisions. Normal bargaining mechanisms fail when stakes are existential. Military/security loyalty becomes contested.

**Key variables affected**: `chn.regime_stability`, elite cohesion, military loyalty

**Resolution depends on**: Which elite faction controls security forces; whether military remains unified; external intervention posture

### 2. Social Mobilization Channel

**Mechanism**: Mass unrest (urban protests, rural grievances, ethnic mobilization) creates pressure that exceeds suppression capacity. Cross-class, cross-regional coordination multiplies impact.

**Key variables affected**: Social unrest index, regime capacity, economic activity

**Historical precedent**: 1989 protests; COVID protests 2022 (limited but notable)

### 3. Economic Disruption Channel

**Mechanism**: Political crisis creates capital flight, business uncertainty, supply chain disruption. Economic damage feeds back into legitimacy pressure.

**Transmission**: Crisis → capital flight → currency pressure → inflation → economic disruption → legitimacy erosion

**Global transmission**: China supply chains affect global manufacturing; commodity demand collapse affects exporters

### 4. Information Control Channel

**Mechanism**: Crisis challenges information monopoly. Competing narratives emerge; international attention increases. Loss of information control accelerates crisis dynamics.

**Key threshold**: When regime loses ability to control domestic information environment, crisis accelerates rapidly

### 5. Nuclear Security Channel

**Mechanism**: Political crisis, especially collapse scenarios, creates uncertainty about nuclear command and control. Multiple actors may gain access to nuclear weapons or materials.

**Critical concern**: State fragmentation branch — who controls the ~350 warheads?

**Transmission**: Crisis → command uncertainty → proliferation risk / accident risk / international intervention incentive

---

## Relationship to Chinese Economic Crisis

Both events affect China but are distinct:

| Dimension | Chinese Economic Crisis | Chinese Political Crisis |
|-----------|------------------------|-------------------------|
| **Domain** | Economic | Political |
| **Threshold** | Banking/property/growth collapse | Regime stability challenged beyond normal processes |
| **Resolutions** | Hard landing / Stagnation / Reform | Extraordinary Stabilization / Transformation / Collapse |
| **Key impacts** | GDP, trade, commodities, financial contagion | Governance, alignment, territory, nuclear security |

**Cascade relationship**: Economic crisis → +2.0% political crisis probability (via regime_stability degradation)

**Economic crisis does NOT automatically produce political crisis**:
- Regime may survive economic crisis through repression, nationalism, blame-shifting
- Japan 1990s: severe economic crisis, no political regime change

**Political crisis may occur WITHOUT economic crisis**:
- Succession dispute
- Military coup
- Mass movement (non-economic grievance)

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-20 |
| **Revision note** | Pressure function and impact vector rewritten to use only state-specification-compliant variables and entities. Exogenous parameters (elite_cohesion, succession_uncertainty) now explicit with event-driven modification rules. Hong Kong removed as modeled entity; territorial outcomes moved to cascade effects. |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | High-impact event with complex resolution dynamics; Level 2 could model elite faction dynamics, succession scenarios, and military loyalty with greater specificity |

## Sources

- Minxin Pei — China's Crony Capitalism; regime fragility analysis
- Susan Shirk — Overreach: How China Derailed Its Peaceful Rise
- Victor Shih — Coalitions of the Weak; elite politics research
- Andrew Nathan — Authoritarian resilience literature
- Comparative politics literature on authoritarian breakdown
- [[events/financial/chinese-economic-crisis]] — Related event specification
- [[events/geopolitical/taiwan-conflict]] — Cascade interaction
- [[research/21st-century-assessment]] — Demographic and trajectory analysis

## Open Questions

1. **Elite faction dynamics**: What are the actual factional alignments within CCP? Who would control what in a succession crisis? This is fundamentally unobservable.

2. **Military loyalty**: Would PLA remain unified in regime crisis? Historical precedent (1989) suggests yes, but circumstances may differ.

3. **Threshold calibration**: The 80/100 threshold is speculative. Authoritarian regimes appear stable until they're not — is CCP at 35/80 or 55/80?

4. **Nuclear security in collapse**: What actually happens to nuclear weapons if China fragments? This is unprecedented and catastrophic if mishandled.

5. **Taiwan interaction timing**: Do crisis and conflict occur together (regime uses Taiwan to distract) or does crisis follow conflict (defeat triggers crisis)?

6. **Transformation probability**: Is 20% too high or too low? Successful reform under pressure is rare but not unknown.

7. **Time-varying probability**: Probability likely increases as Xi ages and succession approaches. Current flat 0.8% is an average; true distribution may be U-shaped (higher early in succession uncertainty, lower mid-reign, higher again as age increases).

---

*Cross-references*: [[events/financial/chinese-economic-crisis]], [[events/geopolitical/taiwan-conflict]], [[methodology/reference/causal-types]], [[methodology/reference/type-3-calibration]], [[research/21st-century-assessment]]

*Scoping document*: [[events/geopolitical/chinese-political-crisis-scoping]]