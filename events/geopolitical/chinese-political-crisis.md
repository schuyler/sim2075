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

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `chn.regime_stability` | 0.25 | inverse | Composite legitimacy metric; captures accumulated erosion |
| *economic_performance_gap* | 0.25 | linear | Gap between actual and expected growth; CCP legitimacy is performance-based |
| *elite_cohesion_index* | 0.20 | inverse | Factional conflict indicators; visible purge intensity beyond normal |
| *social_unrest_index* | 0.15 | threshold(high) | Protest frequency, scale, cross-class participation |
| `chn.youth_unemployment` | 0.10 | linear | Youth alienation; historical pattern of student-led movements |
| *succession_uncertainty* | 0.05 | linear | Unclear succession; contested legitimacy claims |

*Note: Variables in italics require definition or derivation from observable proxies. `chn.regime_stability` is affected by CHINESE_ECONOMIC_CRISIS through cascade.*

### Threshold Specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 80 on 0-100 scale | CCP has exceptional institutional capacity, surveillance technology, and financial resources; threshold substantially higher than typical authoritarian regime |
| **Uncertainty** | ±12 (range 68-92) | Regime opacity; apparent strength may mask fragility (or vice versa) |
| **Sharpness (k)** | 12 | Sharp transition once visible cracks appear — authoritarian regimes exhibit "sudden death" dynamics |
| **Historical calibration** | USSR 1989-91 (threshold breach → collapse); China 1989 (approached threshold, regime stabilized via extraordinary measures); Romania 1989 (rapid threshold breach) |

### Current Pressure Assessment (2025)

**Estimated pressure**: ~35-40 on 0-100 scale

| Component | Status | Contribution |
|-----------|--------|--------------|
| Economic performance | Slowing but not crisis; property stress managed | Moderate |
| Elite cohesion | Consolidated under Xi; no visible factional challenge | Low |
| Social unrest | Elevated (COVID protests, youth unemployment) but controlled | Moderate |
| Succession | Xi removed term limits; uncertainty deferred but not eliminated | Low |
| Regime stability | Stressed but functional | Moderate |

Distance to threshold (~40 points) is substantial. Crisis is not imminent under current baseline conditions.

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

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `global_geopolitical_uncertainty` | ↑ | +40 ± 20 (index) | immediate | resolution_dependent |
| `global_trade_volume` | ↓ | -8 ± 4% | delayed(6mo) | decaying: half_life=3yr |
| *nuclear_security_risk* | ↑ | +25 ± 15 (index) | immediate | resolution_dependent |
| `global_financial_volatility` | ↑ | +60 ± 25% (VIX equivalent) | immediate | decaying: half_life=1yr |

### China Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.gdp_growth` | ↓ | -4 ± 2 pp | immediate | resolution_dependent |
| `chn.regime_stability` | ↓ | -40 ± 15 | immediate | resolution_dependent |
| `chn.governance_effectiveness` | ↓ | -30 ± 15 | immediate | resolution_dependent |
| *chn.capital_flight* | ↑ | +$500B ± 200B | immediate | decaying: half_life=2yr |
| *chn.territorial_integrity* | ↓ | Variable by resolution | delayed(1yr) | resolution_dependent |

### Resolution-Specific Impacts

**Stabilization via Extraordinary Measures:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.regime_stability` | — | Returns to 60 ± 10 (from crisis low) | gradual(2yr) | permanent |
| `chn.governance_effectiveness` | ↓ | -20 ± 10 (security focus crowds out governance) | gradual(1yr) | permanent |
| *chn.international_isolation* | ↑ | +35 ± 15 | delayed(6mo) | permanent |
| *chn.economic_dynamism* | ↓ | -25 ± 10 | gradual(2yr) | permanent |
| `chn.gdp_growth` | ↓ | -2 ± 1 pp (permanent growth penalty) | gradual(2yr) | permanent |

Regime survives but at cost: reduced economic dynamism, international isolation, permanent security state overhead.

**Regime Transformation:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.regime_stability` | — | Highly uncertain; initial instability then potential improvement | gradual(5yr) | shock_vulnerable |
| `chn.governance_effectiveness` | — | -15 ± 20 short-term; uncertain long-term | gradual(3yr) | shock_vulnerable |
| *chn.political_freedom* | ↑ | +30 ± 20 | gradual(5yr) | maintenance_required |
| *chn.international_integration* | ↑ | +20 ± 15 | gradual(3yr) | maintenance_required |
| `chn.gdp_growth` | — | High uncertainty; reform could unlock growth or create chaos | gradual(3yr) | shock_vulnerable |

High variance outcome. Could be Taiwan/South Korea path (successful democratization, economic growth) or could be unstable transition that fails.

**Regime Collapse:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.regime_stability` | ↓ | Undefined (regime ceases to exist) | immediate | N/A |
| `chn.gdp_real` | ↓ | -15 ± 8% (cumulative during transition) | gradual(3yr) | permanent |
| *chn.territorial_integrity* | ↓ | See aftermath branches | delayed(1yr) | permanent |
| *nuclear_security_risk* | ↑ | +50 ± 25 | immediate | decaying: half_life=5yr |
| *global_refugee_flows* | ↑ | +5M ± 3M | delayed(1yr) | decaying: half_life=10yr |

Collapse implies successor state(s) with uncertain properties. Territorial integrity particularly vulnerable — Tibet, Xinjiang, and Taiwan situations fundamentally altered.

### Regional Impacts

**Hong Kong:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `hkg.governance` | — | Determined by China resolution | immediate | resolution_dependent |
| `hkg.gdp_growth` | ↓ | -8 ± 4 pp | immediate | decaying: half_life=3yr |
| *hkg.autonomy* | — | Collapse branch could restore; Stabilization eliminates | delayed(1yr) | permanent |

**Taiwan:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `twn.invasion_risk` | — | Resolution-dependent; see cascade section | immediate | resolution_dependent |
| `twn.international_status` | — | Collapse could enable independence; Stabilization increases pressure | delayed(1yr) | permanent |

**East Asia (Japan, Korea):**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `[country].gdp_growth` | ↓ | -2.0 ± 1.0 pp | delayed(3mo) | decaying: half_life=2yr |
| `[country].defense_spending` | ↑ | +0.5 ± 0.3 pp GDP | gradual(2yr) | permanent |
| *[country].china_trade_share* | ↓ | -10 ± 5 pp | gradual(3yr) | permanent |

**United States:**

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `usa.gdp_growth` | ↓ | -0.8 ± 0.4 pp | delayed(6mo) | decaying: half_life=2yr |
| `usa.defense_posture` | ↑ | Significant reassessment | delayed(1yr) | permanent |
| *usa.china_policy* | — | Fundamentally restructured; resolution-dependent direction | immediate | permanent |

### Durability Specifications

| Impact Category | Durability Type | Parameters | Rationale |
|-----------------|-----------------|------------|-----------|
| Regime stability (Stabilization) | permanent | — | Security state is a new equilibrium |
| International isolation (Stabilization) | permanent | — | Relationships fundamentally damaged |
| Growth penalty (Stabilization) | permanent | — | Security overhead is structural |
| Political reforms (Transformation) | maintenance_required | annual_failure_prob: 5% | Reforms can be reversed |
| Economic disruption | decaying | half_life=3yr | Markets adjust |
| Nuclear security risk | decaying | half_life=5yr | New command structures establish |
| Territorial changes (Collapse) | permanent | — | Borders don't easily revert |

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