---
title: pakistan-state-failure
type: note
permalink: events/geopolitical/pakistan-state-failure
tags:
- event
- geopolitical
- state-failure
- pakistan
- south-asia
- nuclear
- type-2
- threshold
- level-1
---

# Pakistan State Failure

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | PAKISTAN_STATE_FAILURE |
| **Scale** | National |
| **Domain** | Political |
| **Causal Type** | **Type 2: Threshold/Accumulation** |
| **Onset Speed** | Rapid (1-3 years from trigger to acute phase) |
| **Reversibility** | Partial (recovery possible but incomplete) |

## Description

Collapse of effective Pakistani state authority, characterized by loss of territorial control over significant portions of the country, failure to provide basic services, potential military fragmentation, and mass displacement. 

This is a **state transition**: Pakistan crosses from "stressed but functional" to "failed state" regime, marked by `pak.internal_conflict_intensity` rising to 4 (major war/state collapse) and loss of effective territorial control.

**What marks occurrence**: Central government loses control over multiple provinces; military fragments or is unable to maintain order; mass displacement begins; basic services collapse outside major cities.

---

## Causal Type Specification (Type 2: Threshold)

### Why Type 2?

Pakistan exhibits classic pressure accumulation:
- Multiple stressors compound over time (water, debt, governance, conflict)
- State appears stable until threshold crossed, then rapid cascade
- No single actor decision determines outcome (unlike Type 3)
- Not random timing (unlike Type 1)—probability increases with stress

### Pressure Function

Uses observable state variables per [[methodology/reference/state-variables-country]]. Note that `regime_stability` has been replaced by observable indicators.

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `pak.water_stress` | 0.25 | linear | Indus water is binding constraint; civilizational risk |
| `pak.debt_external` | 0.20 | threshold(80) | Sharp increase above 80% debt/GDP; IMF dependency |
| `pak.internal_conflict_intensity` | 0.20 | exponential | Conflict accelerates pressure; currently ~2 |
| `pak.years_since_irregular_transition` | 0.15 | inverse_log | Recent coups/irregular transitions signal fragility |
| `pak.protest_intensity_annual` | 0.10 | linear | Mass unrest indicates stress |
| `pak.food_import_dependence` | 0.10 | linear | Fiscal vulnerability to food prices |

**Pressure calculation**:
```
pressure = 0.25 × pak.water_stress / 100
         + 0.20 × debt_threshold_function(pak.debt_external, 80)
         + 0.20 × exp_transform(pak.internal_conflict_intensity)
         + 0.15 × inverse_log(pak.years_since_irregular_transition)
         + 0.10 × pak.protest_intensity_annual / 100
         + 0.10 × pak.food_import_dependence / 100
```
*Normalized to 0-100 scale*

**Proxy note**: The original specification used `regime_stability` as a composite variable. Per [[methodology/concepts/synthetic-variable-problem]], this has been replaced with observable indicators. The pressure function now directly uses `years_since_irregular_transition`, `protest_intensity_annual`, and `internal_conflict_intensity` as the political stress measures.

### Threshold Specification

| Parameter | Value |
|-----------|-------|
| **Estimate** | 70 (on 0-100 pressure scale) |
| **Uncertainty** | ±10 |
| **Sharpness (k)** | 0.20 (moderate-sharp; compound crises cascade quickly) |
| **Historical calibration** | Syria (crossed ~2011), Venezuela (crossed ~2017), Yugoslavia (crossed ~1991) |

### Minimum Probability

**Floor**: 0.3%/year (military cohesion provides backstop, but not absolute)

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability (current pressure)** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 2.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~30% at point estimate |

### Current Pressure Estimate

Current pressure: ~55/100 (elevated but below threshold)
- `pak.water_stress`: ~70 (severe, worsening)
- `pak.debt_external`: ~75% (near threshold)
- `pak.internal_conflict_intensity`: 2 (intermediate conflict)
- `pak.years_since_irregular_transition`: ~2 (recent PTI crisis counts)
- `pak.protest_intensity_annual`: ~45 (elevated)
- `pak.food_import_dependence`: ~35%

### Derivation

1. **Base rate**: 15-25% over 25 years for high-vulnerability states (from historical collapse patterns)
2. **Annualization**: ~0.9%/year assuming constant hazard
3. **Adjustment for worsening baseline**: Water stress accelerating; IMF dependency chronic; Indus glacier melt accelerating
4. **Adjusted estimate**: 1.5%/year (range: 0.8-2.5%)

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4:

**1. Military has always intervened before failure**

Pakistan's military has a history of seizing power when civilian governance fails—1958, 1969, 1977, 1999. The military is more coherent than the civilian state. "State failure" in the Syria/Somalia sense may be impossible because the military would impose order first. The event as specified may not be reachable.

*Counter*: Military intervention is a different outcome from state failure, but military fragmentation IS possible. The military's coherence depends on ethnic/provincial balance (Punjabi dominated), institutional discipline, and external support. Under severe enough stress (especially combined with India-Pakistan conflict), even the military could fragment. The 1971 breakup of Pakistan demonstrates this is possible.

**2. External support will always arrive**

Pakistan is "too nuclear to fail." China has $60B+ invested in CPEC. The US cares about nuclear security. Gulf states care about remittances. Saudi/UAE/IMF have repeatedly bailed out Pakistan. Someone will always provide enough support to prevent collapse.

*Counter*: External support has been sufficient for "muddle through" but not for structural resolution. Each bailout creates more debt; at some point, bailout fatigue sets in. China's appetite for throwing good money after bad is limited. And if collapse begins rapidly (e.g., triggered by severe climate event), external support may not arrive fast enough.

**3. 1.5%/year is too high for a nuclear state**

The international community's interest in preventing nuclear state failure creates enormous stabilization pressure. No nuclear-armed state has ever failed. The 1.5%/year estimate may be 2-3× too high compared to what the nuclear dimension justifies.

*Counter*: The nuclear dimension creates intervention incentive but doesn't guarantee intervention success. A rapid cascade could outrun international response. And internal dynamics—not external intervention—determine collapse. The Soviet Union was nuclear-armed and did fragment (though not into "failed state" conditions).

**4. Water stress timeline is longer than implied**

Indus water stress is severe but the crisis timeline is decades, not years. Glacier melt increases flow in the medium term before reducing it. The binding constraint may be 2040s-2050s, not 2025-2035. Current probability may be lower than estimated.

*Counter*: Fair point on timeline. But the 2022 floods showed acute shocks can accelerate stress. And water stress interacts with other pressures—it doesn't need to reach peak to contribute to failure. The probability estimate includes uncertainty about timeline.

### Probability Evolution

For Type 2 events, probability varies with pressure accumulation.

| Period | Estimated Pressure | Annual Probability | Rationale |
|--------|-------------------|-------------------|-----------|
| 2025-2035 | 55 → 62 | ~1.3% | Current trajectory; water stress worsening |
| 2035-2045 | 62 → 72 | ~2.0% | Entering threshold zone; glacier melt accelerating |
| 2045-2060 | 72 → 80+ | ~2.5-3.5% | Peak water stress period |
| 2060-2075 | 80+ | ~3.0%+ | If no prior failure, either very high pressure or adaptation |

### Key Uncertainties

- **Indus water trajectory**: Faster glacial melt → pressure rises faster
- **Military cohesion**: Military fracture vs. military intervention is the key swing variable
- **External support**: IMF, China, Gulf states willingness to provide bailouts
- **Climate shock timing**: 2022 floods were preview; worse shocks possible
- **India-Pakistan dynamics**: External conflict could trigger cascade

---

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_SAS** | 0.71 | This IS the South Asian anchor crisis; dominant regional loading |
| **F_FOOD** | 0.42 | Indus water-agriculture nexus is core vulnerability |
| **F_CLIM** | 0.38 | Glacial melt, monsoon variability, flood risk |
| **F_FIN** | 0.29 | Chronic fiscal crisis; IMF dependency |
| **F_GPT** | 0.21 | US-China competition affects aid flows |
| **F_MENA** | 0.17 | Afghan border, Gulf remittances |
| **F_HLTH** | 0.13 | Healthcare vulnerability, population density |
| **F_EAS** | 0.08 | Via China relationship |
| **F_TECH** | 0.04 | Marginal |
| **F_EUR** | 0.04 | Diaspora link |
| F_SSA | 0.00 | No link |
| F_LAM | 0.00 | No link |

**Sum of squared loadings**: 0.94 ✓

---

## Severity Branches

### Branch 1: Controlled Collapse

**Probability given event**: 40%

**Description**: Central government loses control of periphery but military maintains core territorial integrity. Baluchistan, parts of KPK effectively autonomous. Major humanitarian crisis but not complete state dissolution. International intervention helps stabilize.

**Impact modifiers**: 0.7× baseline

### Branch 2: Fragmentation

**Probability given event**: 45%

**Description**: State fragments along provincial/ethnic lines. Multiple power centers emerge. Sindh-Punjab core barely holds together. Mass displacement. Prolonged civil conflict. Nuclear security uncertain but probably maintained.

**Impact modifiers**: 1.0× baseline

### Branch 3: Complete Collapse

**Probability given event**: 15%

**Description**: Military fragments. No coherent central authority. Nuclear security becomes acute international concern. External intervention likely. Mortality and displacement at upper end of range.

**Impact modifiers**: 1.8× baseline

---

## Impact Vector

### Pakistan Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `pak.gdp_real` | ↓ | -40% ± 12% | rapid(2yr) | decaying: half_life=15yr, floor=-20% |
| `pak.internal_conflict_intensity` | ↑ | to 4 (civil war) | immediate | decaying: half_life=8yr |
| `pak.idp_population` | ↑ | +25M ± 10M | rapid(2yr) | decaying: half_life=15yr |
| `pak.refugees_abroad` | ↑ | +5M ± 3M | rapid(3yr) | decaying: half_life=20yr |
| `pak.unemployment_rate` | ↑ | +20 ± 8 pp | immediate | decaying: half_life=10yr |

*Mortality impact: Not a tracked state variable, but estimated at 2-10M excess deaths over 10 years depending on severity branch*

### Regional Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `ind.gdp_growth` | ↓ | -1.0 ± 0.5 pp | delayed(1yr) | decaying: half_life=3yr |
| `ind.refugees_hosted` | ↑ | +2M ± 1.5M | rapid(2yr) | decaying: half_life=15yr |
| `active_major_conflicts` (global) | ↑ | +1 | immediate | until resolution |

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `active_major_conflicts` | ↑ | +1 | immediate | until resolution |

### Durability Rationale

- **GDP**: Decaying with long half-life; recovery possible but slow (Syria analogy: 12+ years, still not recovered)
- **Displacement**: Decaying but slow; "trapped population" dynamics limit return rates; closed borders
- **Conflict intensity**: Decaying as civil war eventually exhausts or resolves

---

## Cascade Effects

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| INDIA_PAKISTAN_MILITARY_CONFLICT | +1.5%/year | 10 years | Chaos creates escalation risk; potential preemptive action |
| CHINESE_ECONOMIC_CRISIS | +0.2%/year | 5 years | CPEC losses; regional instability |

### Triggered By

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| INDIA_PAKISTAN_MILITARY_CONFLICT | +3%/year | Military engagement diverts resources; defeat could trigger fragmentation |
| SEVERE_PANDEMIC | +0.5%/year | Healthcare collapse; economic stress |
| GLOBAL_FINANCIAL_CRISIS | +0.8%/year | Capital flight; IMF unable to help |
| CHINESE_ECONOMIC_CRISIS | +0.5%/year | CPEC support collapses; regional contagion |

---

## Transmission Channels

### Migration Channel

**Direction**: Pakistan → (constrained in all directions)
- India: Militarized border; minimal acceptance expected
- Afghanistan: No capacity; already in crisis
- Iran: Limited willingness
- Gulf states: Would likely expel existing workers

**Implication**: "Trapped population" dynamic—displacement is internal or results in mortality

### Nuclear Security Channel

**Mechanism**: State failure raises arsenal security concerns
- Military cohesion is key variable
- External intervention likely if fragmentation occurs
- India's response is critical unknown
- US and international community would prioritize arsenal security

### Regional Contagion Channel

- Afghanistan: Further destabilization from border pressure
- India: Refugee pressure, terrorism risk, Kashmir opportunism
- China: CPEC investments at risk ($60B+); potential intervention to protect assets

### Remittance Channel

- ~$30B/year in remittances
- Gulf workers expelled during crisis
- Remittance collapse deepens economic crisis (feedback loop)

---

## Historical Analogues

| Case | Relevance | Key Difference |
|------|-----------|----------------|
| Syria (2011-) | Compound crisis → state failure | No nuclear weapons |
| Yugoslavia (1991-) | Multi-ethnic state fragmentation | International intervention earlier |
| Somalia (1991-) | Complete state collapse | Smaller population, no nuclear weapons |
| Pakistan 1971 | Actual fragmentation of Pakistan | External war catalyst; Bangladesh was geographically separate |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete (2025-12-30) |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Nuclear dimension unprecedented; military cohesion is key swing variable requiring deeper analysis |

## Sources

- IMF Article IV consultations
- IPCC Indus basin projections
- World Bank Pakistan Climate Assessment
- Historical state failure case studies

## Open Questions

1. **Military cohesion**: Will military fragment or intervene to prevent collapse?
2. **Nuclear security**: How robust are command-and-control systems under stress?
3. **External intervention**: Would US/China/India intervene? How?
4. **Trapped population**: What are realistic mortality rates with closed borders?
5. **Recovery pathway**: What does reconstitution look like? Somalia model or Yugoslavia model?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-17 | Initial Level 1 specification | Type 2 state failure template |
| 2025-12-30 | Critical review complete | Task 2.4.8 - Added Case Against, Probability Evolution; replaced regime_stability with observable indicators; fixed event references |

---

*See [[methodology/reference/state-variables-country]] for variable definitions | [[methodology/03-critical-review]] for review methodology*