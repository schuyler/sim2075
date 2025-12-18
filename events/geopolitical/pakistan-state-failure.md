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

This is a **state transition**: `pakistan.regime_stability` crosses below failure threshold (~25), triggering shift from "stressed but functional" regime to "failed state" regime.

---

## Causal Type Specification (Type 2: Threshold)

### Pressure Function

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `pakistan.regime_stability` | 0.35 | inverse | Lower stability → higher pressure |
| `pakistan.water_stress` | 0.25 | linear | Indus water is binding constraint |
| `pakistan.debt_external` | 0.15 | threshold(80) | Sharp increase above 80% debt/GDP |
| `pakistan.internal_conflict_intensity` | 0.15 | exponential | Conflict accelerates pressure |
| `pakistan.food_import_dependence` | 0.10 | linear | Fiscal vulnerability to food prices |

**Pressure calculation**:
```
pressure = 0.35 × (100 - regime_stability) / 100
         + 0.25 × water_stress / 100
         + 0.15 × debt_threshold_function(debt_external)
         + 0.15 × exp_transform(conflict_intensity)
         + 0.10 × food_import_dependence / 100
```
*Normalized to 0-100 scale*

### Threshold

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
- `regime_stability`: ~45 (chronically stressed)
- `water_stress`: ~70 (severe, worsening)
- `debt_external`: ~75% (near threshold)
- `internal_conflict_intensity`: ~2 (moderate ongoing)
- `food_import_dependence`: ~35%

### Derivation

1. **Base rate**: 15-25% over 25 years for Tier 1 vulnerability countries (from collapse-patterns)
2. **Annualization**: ~0.9%/year assuming constant hazard
3. **Adjustment for worsening baseline**: Water stress accelerating; IMF dependency chronic; Indus glacier melt accelerating
4. **Adjusted estimate**: 1.5%/year (range: 0.8-2.5%)

### Key Uncertainties

- **Indus water trajectory**: Faster glacial melt → pressure rises faster → probability increases
- **Military cohesion**: Military fracture vs. military intervention (the key swing variable)
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
| **F_SSA** | 0.00 | No link |
| **F_LAM** | 0.00 | No link |

**Sum of squared loadings**: 0.94 ✓

### Loading Interpretation (per Integrated Framework)

Factors shock state variables that feed into pressure function:
- High F_SAS → regional instability → `regime_stability` declines → pressure rises
- High F_FOOD → food prices → `food_import_dependence` stress → pressure rises
- High F_CLIM → water stress → `water_stress` increases → pressure rises
- High F_FIN → credit conditions → `debt_external` pressure → pressure rises

This is the Type 2 factor→state→pressure→probability pathway.

---

## Impact Vector

### Pakistan Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `pakistan.gdp_real` | ↓ | -40% ± 12% | rapid(2) | decaying (half_life: 15yr, floor: -20%) |
| `pakistan.regime_stability` | ↓ | to <20 | immediate | regime_dependent (recovery requires reconstitution) |
| `pakistan.internal_conflict_intensity` | ↑ | to 4 (civil war) | immediate | decaying (half_life: 8yr) |
| `pakistan.displacement` | ↑ | 30M ± 15M | rapid(3) | decaying (half_life: 20yr) |
| `pakistan.excess_mortality` | ↑ | 6M ± 4M | gradual(10) | permanent |

### Regional Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `india.gdp_real` | ↓ | -2% ± 1% | delayed(2) | decaying (half_life: 5yr) |
| `afghanistan.regime_stability` | ↓ | -15 ± 5 | immediate | persistent |
| `south_asia_aggregate.displacement` | ↑ | +35M ± 18M | rapid(3) | decaying |

### Global Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `global_gdp` | ↓ | -0.3% ± 0.15% | gradual(5) | decaying (half_life: 7yr) |
| `nuclear_stability` | ↓ | -15 ± 10 | immediate | maintenance_required (depends on resolution) |
| `active_major_conflicts` | ↑ | +1 | immediate | decaying |

### Durability Rationale

- **GDP**: Decaying with long half-life; recovery possible but slow (Syria analogy: 12+ years, still not recovered)
- **Deaths**: Permanent by definition
- **Displacement**: Decaying but slow; "trapped population" dynamics limit return rates
- **Nuclear stability impact**: Maintenance_required—depends on how arsenal is secured/controlled
- **Regional instability**: Persistent contagion effects

---

## Differential Impacts

**Exposure variable**: Border proximity and economic ties to Pakistan

| Country/Region | Impact Multiplier | Rationale |
|----------------|-------------------|-----------|
| Afghanistan | 2.0× regional stability impact | Shared border, Taliban ties |
| India | 1.5× security impact, 1.0× economic | Nuclear risk, refugee pressure, Kashmir |
| Iran | 0.8× | Baluchistan border, but more distant |
| Gulf States | 1.5× remittance disruption | Large Pakistani diaspora |
| China | 1.2× economic impact | CPEC investments at risk |

---

## Cascade Effects

### State → Probability Cascades

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Ungoverned space → terrorism | TERRORISM_MAJOR_ATTACK | +3%/year | 15 years | Safe haven formation |
| Regional destabilization → India-Pakistan | INDIA_PAKISTAN_CONFLICT | +2%/year | 10 years | Escalation risk from chaos |
| Afghan spillover | AFGHANISTAN_FURTHER_COLLAPSE | +4%/year | 10 years | Border pressure, militant flows |
| Nuclear uncertainty | NUCLEAR_INCIDENT | +0.5%/year | Until resolved | Command-and-control uncertainty |
| Remittance collapse → Gulf pressure | GULF_LABOR_CRISIS | +1%/year | 5 years | Mass worker returns |

### Impact Chains

**Pathway 1**: Pakistan failure → Afghan spillover → Central Asian pressure
```
Event → ungoverned Af-Pak border → militant flows → regional instability → P(Central Asia crisis) ↑
```

**Pathway 2**: Pakistan failure → nuclear uncertainty → international intervention
```
Event → command-and-control concerns → US/India intervention pressure → escalation risk
```

**Pathway 3**: Pakistan failure → Gulf remittance collapse → South Asian poverty
```
Event → Gulf states expel workers → remittances collapse → Bangladesh/India household income ↓
```

---

## Transmission Channels

### Migration Channel

**Direction**: Pakistan → (constrained in all directions)
- India: Militarized border; minimal acceptance
- Afghanistan: No capacity; already in crisis
- Iran: Limited willingness
- Gulf states: Would expel existing workers

**Implication**: "Trapped population" dynamic—displacement is internal or fatal

### Nuclear Security Channel

**Mechanism**: State failure raises arsenal security concerns
- Military cohesion is key variable
- External intervention likely if fragmentation
- India's response is critical unknown

### Regional Contagion Channel

- Afghanistan: Further destabilization
- India: Refugee pressure, terrorism, Kashmir opportunism
- China: CPEC investments at risk; potential intervention

### Remittance Channel

- ~$30B/year in remittances
- Gulf workers expelled during crisis
- Remittance collapse deepens economic crisis (feedback loop)
- Affects Bangladesh, India (Gulf labor market competition)

---

## Historical Analogues

| Case | Relevance | Key Difference |
|------|-----------|----------------|
| Syria (2011-) | Compound crisis → state failure | No nuclear weapons |
| Yugoslavia (1991-) | Multi-ethnic state fragmentation | International intervention earlier |
| Somalia (1991-) | Complete state collapse | Smaller population, no nuclear weapons |
| Venezuela (2013-) | Economic collapse → dysfunction | Didn't reach territorial fragmentation |

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-17 |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Nuclear dimension unprecedented; military cohesion is key swing variable requiring deeper analysis |

## Sources

- [[21st-century-assessment]] South Asia section
- collapse-patterns-predictive-framework.md
- IMF Article IV consultations
- IPCC Indus basin projections

## Open Questions

- **Military cohesion**: Will military fragment or intervene to prevent collapse?
- **Nuclear security**: How robust are command-and-control systems under stress?
- **External intervention**: Would US/China/India intervene? How?
- **Trapped population**: What are realistic mortality rates with closed borders?
- **Recovery pathway**: What does reconstitution look like? Somalia model or Yugoslavia model?
