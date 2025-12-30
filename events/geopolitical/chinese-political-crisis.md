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
| **Reversibility** | Irreversible (all resolutions produce permanent regime change) |

## Description

CCP regime discontinuity: the party-state either transforms into a fundamentally different political system or collapses entirely. This is not a crisis that the regime survives — it is the end of CCP rule in its current form.

The event fires only when regime change becomes inevitable. Severe crises that the CCP weathers through repression, purges, or extraordinary measures are sub-threshold — they represent the regime functioning under stress, not discontinuity. Tiananmen 1989 is the canonical example: extraordinary measures, but the same regime continued governing the same territory with the same institutional form.

**Discontinuity requirement**: All resolutions produce a different regime governing China. "More repressive CCP" or "isolated CCP" is not a discontinuity.

---

## Causal Type Specification

### Type 2/3 Hybrid Structure

This event combines threshold dynamics (Type 2) with contingent resolution (Type 3):

**Type 2 Component**: Pressure accumulates through legitimacy erosion, economic underperformance, elite conflict, and social unrest. At critical pressure, regime change becomes likely.

**Type 3 Component**: Once threshold is crossed, outcome depends on actor decisions (elite factions, military commanders, protest movements). Resolution probabilities reflect structural factors but are not precisely calibrated.

```
Pressure accumulates → Threshold crossed → Regime change inevitable →
Resolution sampled → Aftermath branches
```

### Pressure Function

Per [[methodology/concepts/synthetic-variable-problem]], we use observable indicators rather than synthetic indices like `regime_stability` or `institutional_quality`. Chinese political crisis pressure is proxied through observable economic and political stress indicators:

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `chn.gdp_growth` | 0.30 | inverse (below 3% threshold) | Performance legitimacy; social contract requires growth; primary CCP legitimacy source |
| `chn.unemployment_rate` | 0.20 | linear | Economic stress indicator; youth unemployment particularly destabilizing |
| `chn.protest_intensity_annual` | 0.20 | linear | Observable unrest; cross-class coordination multiplies impact |
| `chn.years_since_irregular_transition` | 0.15 | inverse | Proxy for succession risk; longer tenure creates succession uncertainty |
| `chn.inflation_rate` | 0.10 | linear | Economic stress; affects popular grievance |
| `chn.fdi_net` | 0.05 | inverse | Elite confidence proxy; capital flight signals loss of confidence |

**Proxy limitations**: True regime stability depends on unobservable factors: elite cohesion, military loyalty, internal party dynamics. These cannot be directly measured. We proxy through their downstream effects: economic performance (legitimacy), protest activity (popular discontent), and FDI flows (elite/business confidence). The pressure function captures stress symptoms rather than underlying political dynamics. Probability calibration relies primarily on reference class reasoning from other authoritarian regime transitions.

*Note: CHINESE_ECONOMIC_CRISIS cascade adds +2.0% probability modifier for 5 years through its impact on multiple observable indicators.*

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 85 on 0-100 scale | Event fires only when regime change is inevitable, not when crisis is severe |
| **Uncertainty** | ±10 (range 75-95) | Regime opacity |
| **Sharpness (k)** | 15 | Very sharp transition — regimes appear stable until they're not |
| **Historical calibration** | USSR 1991 (threshold breach → collapse); Romania 1989 (rapid breach); China 1989 (sub-threshold — regime survived via extraordinary measures) |

### Current Pressure Assessment (2025)

**Estimated pressure**: ~35-40 on 0-100 scale

| Component | Status | Contribution |
|-----------|--------|--------------|
| Economic performance | Slowing but not crisis | Moderate |
| Elite cohesion | Consolidated under Xi | Low |
| Social unrest | Elevated but controlled | Moderate |
| Succession | Uncertainty deferred | Low |
| Regime stability | Stressed but functional | Moderate |

Distance to threshold (~45-50 points) is substantial.

### Minimum Probability

**Floor**: 0.15% annually even at low pressure

Black swan triggers: sudden leader incapacitation without succession plan, military incident producing elite fragmentation, or external shock (Taiwan conflict defeat) that catalyzes regime collapse.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 0.4% |
| **Low bound** | 0.2% |
| **High bound** | 0.8% |
| **Confidence** | Low |
| **25-year cumulative** | ~10% at point estimate |

### Derivation

**Step 1: Reference class — actual regime changes in single-party states**

| Reference | Outcome | Annual Rate | Notes |
|-----------|---------|-------------|-------|
| USSR 1922-1991 | Collapsed | ~1.4% (1 in 69 years) | High capacity; still fell |
| PRC 1949-present | No regime change | 0% realized (76 years) | Same regime; survived 1989 |
| Single-party states (broad) | Variable | ~1-2% for regime change | Includes weaker regimes |

CCP has survived longer than USSR and has greater surveillance/financial resources. Base rate for comparable high-capacity regimes: ~0.5-1.0%.

**Step 2: Structural factors**

Factors increasing probability:
- Xi's power concentration creates succession fragility
- Economic model under strain (demographics, property, debt)
- No clear successor identified

Factors decreasing probability:
- Exceptional surveillance and control technology
- Large financial reserves and policy space
- No serious organized opposition
- Military thoroughly integrated with party

**Step 3: Conditional probability from cascades**

- CHINESE_ECONOMIC_CRISIS: +2.0% for 5 years
- TAIWAN_CONFLICT (defeat): +3.0% for 3 years

These represent scenarios where regime change becomes much more likely, but the baseline (absent these triggers) is low.

**Step 4: Final estimate**

**Point estimate: 0.4% annually** with range 0.2%-0.8%.

This is low because we're modeling actual regime discontinuity — the CCP ceasing to exist or transforming beyond recognition — not severe political crises.

### Comparative Ranking

- Less likely than: Russia State Failure (~1.0%), Turkey Political Crisis (~1.0%), Saudi Regime Instability (~0.8%)
- Similar to: AMOC Weakening (~0.5%)
- More likely than: Permafrost Methane Release (~0.3% for severe)

CCP is more stable than these other regimes. The comparison to climate tipping points reflects that we're modeling rare, high-consequence discontinuities.

### Case Against This Specification

**CCP has exceptional survival capacity**: The party has the most sophisticated surveillance apparatus in history, massive financial reserves, no organized opposition, and military thoroughly integrated with party leadership. Every prediction of CCP collapse since 1989 has been wrong. The 0.4%/year estimate may be too high for a regime with this much adaptive capacity.

**The discontinuity definition may be too narrow**: If the only event that counts is complete regime change, we're modeling a tail so extreme it approaches zero probability. Meaningful political crises that the CCP survives through extraordinary measures (another Tiananmen, Xi removal by elite faction, etc.) are excluded. This may undercount politically significant events.

**Reference class is weak**: Comparing CCP to USSR or single-party states generally conflates very different regimes. China has advantages the USSR lacked: market economy integration, national unity, no satellite empire to manage, and much greater surveillance technology. The reference class may not apply.

**Post-Xi succession may be managed**: The assumption that Xi's power concentration creates succession fragility may be wrong. The party may have internal succession mechanisms that are not visible externally. Authoritarian succession in China (Mao → Deng → Jiang → Hu → Xi) has been orderly compared to other systems.

**Counterargument**: The concerns are valid, which is why the estimate is low (0.4%, implying only ~10% cumulative probability over 25 years). The USSR also appeared impregnable in 1985. Regimes appear stable until they aren't—the threshold dynamics capture this discontinuity. We acknowledge low confidence and wide uncertainty range (0.2-0.8%).

### Probability Evolution

As a Type 2/3 hybrid, probability varies with pressure accumulation and succession dynamics:

| Period | Annual Probability | Rationale |
|--------|-------------------|-----------|
| 2025-2030 | ~0.3-0.4% | Current leadership stable; succession deferred |
| 2030-2040 | ~0.4-0.6% | Xi succession window; economic stress likely elevated |
| 2040-2050 | ~0.3-0.5% | Depends on succession outcome and economic trajectory |
| 2050-2075 | ~0.2-0.5% | Path-dependent on whether transition occurred or regime adapted |

**Key inflection points**:
- Xi succession: Major vulnerability window whenever it occurs
- Economic crisis: CHINESE_ECONOMIC_CRISIS would add +2% for 5 years
- Taiwan conflict outcome: Defeat would add +3%; victory would reduce probability
- Generational elite turnover: Creates potential for factional conflict

---

## Resolution Specification (Type 3 Component)

Once the threshold is crossed, one of two resolutions occurs:

### Resolution Branches

| Resolution | Probability | Description |
|------------|-------------|-------------|
| **Regime Transformation** | 40% | Crisis forces genuine system change; CCP rule ends but state continuity preserved |
| **Regime Collapse** | 60% | CCP loses power entirely; state continuity uncertain |

### Resolution Probability Rationale

**Entropy-maximized default**: 50% / 50%

**Structural deviation**: Slight tilt toward Collapse (60/40) because:
- Regimes under existential pressure rarely successfully reform
- Reform attempts often accelerate collapse (Gorbachev precedent)
- CCP's rigid structure makes controlled transformation difficult

Maximum ratio is 1.5:1, well within guidelines.

### Resolution Descriptions

**Regime Transformation (40%)**

CCP rule ends but is replaced by a successor regime with state continuity:
- Liberalization under pressure (elite faction seeks legitimacy through reform)
- Power-sharing arrangement (factional federation, constitutional constraints)
- Negotiated transition to different political system

Historical models: Taiwan (1980s-90s), South Korea (1987). These succeeded. USSR under Gorbachev attempted transformation but collapsed — that outcome is captured in the Collapse resolution.

**Regime Collapse (60%)**

CCP loses power without controlled transition:
- Revolutionary transition (mass movement overthrows regime)
- State fragmentation (regional power centers emerge)
- Military takeover (PLA assumes direct control)

Collapse doesn't mean China disappears — successor regime(s) emerge with uncertain character and territorial scope.

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.10 | Climate stress affects rural stability, food security |
| F_FIN | 0.40 | **Primary**: Economic conditions are core legitimacy input |
| F_HLTH | 0.10 | Pandemic management affects governance perceptions |
| F_GPT | 0.35 | **Secondary**: Great power tension affects legitimacy and elite cohesion |
| F_FOOD | 0.15 | Food security affects rural stability |
| F_TECH | 0.10 | Technology competition affects development narrative |
| F_EUR | 0.05 | Limited direct impact |
| F_MENA | 0.0 | No direct linkage |
| F_SAS | 0.05 | Border tensions create external pressure |
| F_EAS | 0.30 | Regional dynamics affect legitimacy |
| F_SSA | 0.0 | No direct linkage |
| F_LAM | 0.0 | No direct linkage |

**Sum of squared loadings**: 0.43 ✓

Lower loading sum reflects that Chinese regime change is primarily domestically-driven.

---

## Impact Vector

### Analog Basis

| Analog | Event Type | Key Observations | Relevance |
|--------|------------|------------------|-----------|
| **USSR Collapse (1991)** | Regime collapse + fragmentation | GDP -40% over 5 years; ~25M displaced; nuclear command fragmented | Collapse branches |
| **Indonesia 1998** | Regime change (Suharto fell) | GDP -13% single year; minimal territorial change; 2-3 year recovery | Transformation analog |
| **Yugoslavia 1991-95** | State fragmentation | Multiple successor states; ~140K deaths; ~4M displaced | Fragmentation branch |
| **South Korea 1987** | Successful transformation | Democratic transition; GDP growth accelerated; international integration improved | Transformation success |

### Global Impacts (All Resolutions)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `us_china_tension` | ↑ | +25 ± 10 points | immediate | resolution_dependent | Instability increases uncertainty |
| `global_trade_volume` | ↓ | -6 ± 3% | delayed(6mo) | decaying: half_life=3yr | China is ~15% of world trade |
| `nuclear_stability` | ↓ | -15 ± 8 points | immediate | resolution_dependent | Command uncertainty |
| `global_credit_spread` | ↑ | +80 ± 40 bps | immediate | decaying: half_life=1yr | Second-largest economy |
| `semiconductor_supply` | ↓ | -8 ± 4% | delayed(3mo) | decaying: half_life=2yr | Supply chain uncertainty |

### China Impacts (All Resolutions)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.gdp_growth` | ↓ | -4 ± 2 pp | immediate | resolution_dependent | Indonesia 1998 reference |
| `chn.regime_stability` | ↓ | -35 ± 12 points | immediate | resolution_dependent | By definition |
| `chn.state_capacity` | ↓ | -20 ± 10 points | immediate | resolution_dependent | Institutional disruption |
| `chn.reserves_foreign` | ↓ | -6 ± 3 months imports | gradual(1yr) | decaying: half_life=3yr | Capital flight |
| `chn.current_account` | ↓ | -4 ± 2 pp GDP | delayed(6mo) | decaying: half_life=2yr | Trade disruption |
| `chn.fdi_net` | ↓ | -3 ± 1.5 pp GDP | delayed(6mo) | resolution_dependent | Investment freeze |

### Resolution-Specific Impacts

#### Regime Transformation

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.regime_stability` | — | 40 ± 15 short-term | gradual(3yr) | shock_vulnerable | Transition instability |
| `chn.state_capacity` | ↓ | -10 ± 8 short-term | gradual(2yr) | shock_vulnerable | Institutional restructuring |
| `chn.civil_liberties` | ↑ | +25 ± 15 points | gradual(5yr) | maintenance_required: annual_failure_prob=0.05 | Liberalization gains |
| `chn.sanctions_level` | ↓ | -15 ± 8 points | delayed(1yr) | maintenance_required | International engagement improves |
| `chn.gdp_growth` | — | -1 to +2 pp vs. baseline | gradual(3yr) | shock_vulnerable | High variance; Taiwan/Korea vs. USSR paths |

#### Regime Collapse

Common immediate effects across all collapse branches:

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `chn.regime_stability` | ↓ | Falls to <20 | immediate | N/A | Definitional |
| `chn.gdp_real` | ↓ | -20 ± 8% cumulative | gradual(3yr) | permanent | USSR: -40%; Yugoslavia: -25% |
| `chn.state_capacity` | ↓ | -40 ± 15 points | immediate | decaying: half_life=10yr | Institutional collapse |
| `chn.institutional_quality` | ↓ | -1.5 ± 0.5 | immediate | decaying: half_life=15yr | Russia took 15+ years |

**State Fragmentation branch additional impacts:**

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `nuclear_stability` (global) | ↓ | -35 ± 15 points | immediate | decaying: half_life=5yr | Multiple actors may control arsenal |
| `active_major_conflicts` (global) | ↑ | +2 ± 1 | delayed(1yr) | decaying: half_life=10yr | Internal conflicts |

### Regional Impacts

#### East Asia (Japan, South Korea)

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `jpn.gdp_growth` | ↓ | -1.5 ± 0.8 pp | delayed(3mo) | decaying: half_life=2yr | China is ~25% of exports |
| `kor.gdp_growth` | ↓ | -2.0 ± 1.0 pp | delayed(3mo) | decaying: half_life=2yr | Korea more China-dependent |
| `jpn.military_spending` | ↑ | +0.4 ± 0.2 pp GDP | gradual(2yr) | permanent | Security reassessment |
| `kor.military_spending` | ↑ | +0.5 ± 0.3 pp GDP | gradual(2yr) | permanent | Peninsula uncertainty |

#### Taiwan

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `twn.gdp_growth` | ↓ | -3.0 ± 1.5 pp | immediate | decaying: half_life=2yr | Cross-strait disruption |
| `twn.regime_stability` | — | Resolution-dependent | — | — | Transformation reduces threat; Fragmentation eliminates it |
| `twn.alliance_west` | ↑ | +10 ± 5 points | gradual(1yr) | permanent | Accelerated engagement |

#### United States

| Variable | Direction | Magnitude | Onset | Durability | Derivation |
|----------|-----------|-----------|-------|------------|------------|
| `usa.gdp_growth` | ↓ | -0.6 ± 0.3 pp | delayed(6mo) | decaying: half_life=2yr | Trade/financial contagion |
| `usa.military_spending` | ↑ | +0.3 ± 0.2 pp GDP | gradual(2yr) | permanent | Strategic reassessment |

### Hong Kong Note

Hong Kong is not separately modeled. Its fate:
- **Transformation**: Possible restoration of some autonomy
- **Collapse (Fragmentation)**: Status contested; possible de facto independence

### Cascade Effects on Territorial Outcomes

State Fragmentation branch triggers:

| Cascade Target | Effect | Mechanism |
|----------------|--------|-----------|
| TAIWAN_CONFLICT | -1.5% for 5 years | No unified state to mount invasion |
| PAKISTAN_STATE_FAILURE | +1.0% for 5 years | CPEC collapses; Chinese support eliminated |

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| Civil liberties gains (Transformation) | maintenance_required | annual_failure_prob: 5% | Reforms reversible |
| GDP disruption | decaying | half_life=2-3yr | Markets adjust |
| Nuclear stability (Collapse) | decaying | half_life=5yr | New structures establish |
| Institutional quality (Collapse) | decaying | half_life=15yr | Slow rebuild |
| State capacity (Collapse) | decaying | half_life=10yr | Gradual recovery |

---

## Aftermath Branches

### Regime Transformation — Aftermath

**Branch 1: Successful Liberalization (40%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Genuine democratization; possible 10-20 year transition |
| **Duration** | Transition period 10-20 years |
| **Factor modifications** | F_GPT: -0.1 for 10 years; F_EAS: -0.15 for 10 years |

- Taiwan situation potentially resolved peacefully
- Economic liberalization may accelerate growth
- International integration improves
- Model: Taiwan 1980s-90s, South Korea post-1987

**Branch 2: Unstable Transition (60%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Reform opens space for further instability; potential collapse within 5 years |
| **Duration** | 3-7 years until collapse or stabilization |
| **Factor modifications** | F_GPT: +0.15 for 5 years; F_EAS: +0.2 for 5 years |
| **Collapse probability** | 8% annually for 5 years |

- Reform faction loses control
- May accelerate to Collapse resolution
- Model: USSR 1989-91

### Regime Collapse — Aftermath

**Branch 1: Revolutionary Transition (35%)**

| Attribute | Value |
|-----------|-------|
| **Description** | New unified regime emerges; character uncertain |
| **Duration** | Transition 2-5 years; new regime permanent |
| **Factor modifications** | F_GPT: +0.4 for 5 years; F_EAS: +0.35 for 5 years |

- Successor regime could be: democratic, nationalist authoritarian, military, or hybrid
- Territorial integrity likely maintained
- Nuclear weapons: chain of command preserved

**Branch 2: State Fragmentation (35%)**

| Attribute | Value |
|-----------|-------|
| **Description** | Regional power centers emerge; civil conflict |
| **Duration** | 5-15 years of instability |
| **Factor modifications** | F_GPT: +0.6 for 10 years; F_EAS: +0.5 for 10 years; F_FIN: +0.3 for 5 years |

- Tibet, Xinjiang separatism
- Taiwan: de facto independence
- Nuclear weapons: critical security concern
- Massive refugee flows (10M+)
- Model: USSR collapse but more violent

**Branch 3: Military Takeover (30%)**

| Attribute | Value |
|-----------|-------|
| **Description** | PLA assumes direct control |
| **Duration** | Permanent regime change |
| **Factor modifications** | F_GPT: +0.45 for 10 years; F_EAS: +0.4 for 10 years |

- Military government; praetorian state
- Taiwan: risk may increase
- Nuclear weapons: command preserved
- Economic policy: likely nationalist/autarkic

---

## Cascade Effects

### Triggered By

| Source Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| CHINESE_ECONOMIC_CRISIS | +2.0% | 5 years | Performance legitimacy failure |
| TAIWAN_CONFLICT (defeat) | +3.0% | 3 years | Nationalist legitimacy failure |
| TAIWAN_CONFLICT (stalemate) | +1.0% | 3 years | Costly non-victory |
| SEVERE_PANDEMIC (China origin) | +1.0% | 2 years | Governance failure narrative |
| GLOBAL_FINANCIAL_CRISIS | +0.5% | 2 years | External shock amplifies stress |

### Triggers

| Target Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 2 years | Capital flight, market panic |
| DOLLAR_RESERVE_CRISIS | -0.5% | 3 years | Yuan alternative less viable |
| KOREAN_PENINSULA_CRISIS | +1.0% | 3 years | DPRK opportunism |
| PAKISTAN_STATE_FAILURE | +0.5% | 3 years | Chinese support capacity eliminated |
| TAIWAN_CONFLICT | Resolution-dependent | — | See below |

### Taiwan Conflict Interaction

**Chinese Political Crisis → Taiwan Conflict:**

| Resolution | Effect | Mechanism |
|------------|--------|-----------|
| Transformation | -0.5% for 5 years | Liberalizing leadership less likely to use force |
| Collapse (Revolutionary) | +0.3% for 3 years | Nationalist successor may seek legitimacy |
| Collapse (Fragmentation) | -1.5% for 5 years | No unified state; Taiwan effectively independent |
| Collapse (Military) | +1.0% for 5 years | Military more likely to use force |

**Taiwan Conflict → Chinese Political Crisis:**

| Taiwan Outcome | Effect | Duration |
|----------------|--------|----------|
| Victory (reunification) | -1.0% | 5 years |
| Defeat/Humiliation | +3.0% | 3 years |
| Stalemate | +1.0% | 3 years |

---

## Transmission Channels

### 1. Elite Cohesion Channel (Primary)

Crisis stress exposes elite divisions. Military/security loyalty becomes contested. Resolution depends on which faction controls security forces.

### 2. Social Mobilization Channel

Mass unrest exceeds suppression capacity. Cross-class, cross-regional coordination multiplies impact.

### 3. Economic Disruption Channel

Political crisis creates capital flight, supply chain disruption. Economic damage feeds back into pressure.

### 4. Information Control Channel

Crisis challenges information monopoly. Loss of domestic information control accelerates dynamics.

### 5. Nuclear Security Channel

Collapse scenarios create command uncertainty. State fragmentation: who controls ~350 warheads?

---

## Relationship to Chinese Economic Crisis

| Dimension | Chinese Economic Crisis | Chinese Political Crisis |
|-----------|------------------------|-------------------------|
| **Domain** | Economic | Political |
| **Threshold** | Banking/property/growth collapse | Regime change inevitable |
| **Resolutions** | Hard landing / Stagnation / Reform | Transformation / Collapse |
| **Key impacts** | GDP, trade, financial contagion | Governance, territory, nuclear |

Economic crisis does NOT automatically produce political crisis — regime may survive through repression. Political crisis may occur WITHOUT economic crisis — succession dispute, military coup.

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete |
| **Revision note** | Replaced synthetic variables (regime_stability, institutional_quality) with observables in pressure function. Added Case Against and Probability Evolution sections. |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | High-impact event; Level 2 could model succession scenarios and military loyalty. Impact vector synthetic variables (state_capacity, civil_liberties) need replacement in Level 2. |

## Sources

- Minxin Pei — China's Crony Capitalism
- Susan Shirk — Overreach: How China Derailed Its Peaceful Rise
- Victor Shih — Coalitions of the Weak
- Andrew Nathan — Authoritarian resilience literature
- Comparative politics literature on authoritarian breakdown
- [[events/financial/chinese-economic-crisis]]
- [[events/geopolitical/taiwan-conflict]]
- [[research/21st-century-assessment]]

## Open Questions

1. **Threshold calibration**: Is CCP at 35/85 or 55/85? Authoritarian regimes appear stable until they're not.

2. **Military loyalty**: Would PLA fragment or remain unified? 1989 suggests unity, but circumstances may differ.

3. **Nuclear security in fragmentation**: What happens to ~350 warheads if China fragments?

4. **Taiwan interaction timing**: Does crisis follow conflict (defeat triggers crisis) or occur independently?

5. **Time-varying probability**: Probability likely increases as Xi ages. Current 0.4% is an average; true distribution may be U-shaped over succession cycle.

---

*Cross-references*: [[events/financial/chinese-economic-crisis]], [[events/geopolitical/taiwan-conflict]], [[methodology/reference/causal-types]], [[methodology/reference/type-3-calibration]], [[research/21st-century-assessment]]

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-30 | Critical review: replaced synthetic variables in pressure function with observables; added Case Against and Probability Evolution sections; noted impact vector synthetic variables for Level 2 | Task 2.4 systematic review |
| 2025-12-20 | Removed Stabilization resolution; tightened discontinuity requirement; lowered probability to 0.4% | Consistency with "discontinuity means discontinuity" principle |
| 2025-12-18 | Initial Level 1 specification | Task 2.1 geopolitical events |