---
title: Pakistan State Failure
type: note
permalink: events/geopolitical/pakistan-state-failure
tags:
- event
- geopolitical
- state-failure
- pakistan
- south-asia
- nuclear
- level-1
---

---
title: Pakistan State Failure
type: note
permalink: events/geopolitical/pakistan-state-failure
tags:
- event
- geopolitical
- deprecated
---

# ⚠️ SUPERSEDED

**This event specification has been superseded by [[events/geopolitical/pakistan-state-failure-v2]].**

The v2 specification adds:
- Causal type classification (Type 2: Threshold)
- Pressure function specification
- Impact vectors with durability types
- Cascade effects documentation

---

# Pakistan State Failure

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | PAKISTAN_STATE_FAILURE |
| **Scale** | National |
| **Domain** | Political |
| **Onset Speed** | Rapid (1-3 years from trigger to acute phase) |
| **Reversibility** | Partial (recovery possible but incomplete) |

## Description

Collapse of effective Pakistani state authority, characterized by loss of territorial control over significant portions of the country, failure to provide basic services, potential military fragmentation, and mass displacement. Triggered by compound water, food, economic, and political crises overwhelming institutional capacity.

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | 1.5% |
| **Low bound** | 0.8% |
| **High bound** | 2.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~30% (at point estimate) |

### Derivation

1. **Base rate from collapse-patterns**: 15-25% over 25 years for state failure in Tier 1 vulnerability countries
2. **Annualization**: ~0.9%/year assuming constant hazard
3. **Adjustment for worsening baseline**: Pakistan's water stress, climate exposure, and fiscal fragility are deteriorating. IMF dependency is chronic. Indus glacier melt is accelerating.
4. **Adjusted estimate**: 1.5%/year (range: 0.8-2.5%)

### Key Uncertainties

- **Indus water trajectory**: Faster glacial melt → higher probability
- **Military cohesion**: Military fracture vs. military takeover under stress
- **External support**: IMF, China, Gulf states willingness to bail out
- **India-Pakistan dynamics**: Crisis could be triggered or accelerated by external conflict
- **Climate shock timing**: 2022 floods were preview; worse is possible

## Factor Loadings

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_SAS** | 0.71 | This IS the South Asian crisis event; dominant regional loading |
| **F_FOOD** | 0.42 | Water-agriculture nexus is core vulnerability; Indus feeds 90% of agriculture |
| **F_CLIM** | 0.38 | Glacial melt, monsoon variability, 2022 floods as preview |
| **F_FIN** | 0.29 | Chronic IMF dependency, debt distress, currency pressure |
| **F_GPT** | 0.21 | US-China competition affects aid flows, India relations |
| **F_MENA** | 0.17 | Afghan border, Iran neighbor, Gulf remittances |
| **F_HLTH** | 0.13 | Healthcare system vulnerability, population density |
| **F_EAS** | 0.08 | Weak link via China relationship |
| **F_TECH** | 0.04 | Marginal |
| **F_EUR** | 0.04 | Marginal (diaspora, but limited direct link) |
| **F_SSA** | 0.00 | No link |
| **F_LAM** | 0.00 | No link |

**Sum of squared loadings**: 0.94 ✓ (within constraint)

### Loading Rationale

Multi-factor structure reflects compound vulnerability:
- F_SAS dominant because this is THE South Asian anchor crisis
- F_FOOD and F_CLIM high because water-agriculture nexus is primary structural vulnerability
- F_FIN significant because fiscal crisis is chronic and constrains adaptation
- Other factors are secondary contributors, not primary drivers

## Impacts

### Economic Impacts

| Variable | Mean | Std Dev | Distribution |
|----------|------|---------|--------------|
| Pakistan GDP | -40% | 12% | Normal |
| Global GDP | -0.3% | 0.15% | Normal |
| South Asia GDP | -5% | 2% | Normal |
| India GDP | -2% | 1% | Normal (spillover) |

### Humanitarian Impacts

| Variable | Mean | Std Dev | Distribution |
|----------|------|---------|--------------|
| Displacement | 30M | 15M | Log-normal |
| Excess mortality | 6M | 4M | Log-normal |

### Duration

| Metric | Value |
|--------|-------|
| Acute phase | 5-10 years |
| Recovery to baseline | 15-25 years |
| Model duration | 15 years |

### Impact Derivation

Using collapse-patterns benchmarks for compound collapse (economic + political + resource):
- GDP decline: 75% ± 10% range, adjusted down to 40% because Pakistan isn't starting from middle-income baseline
- Displacement: 12.5% of 240M population = 30M (civil war benchmark: 45% ± 15%)
- Mortality: 2.5% of population = 6M (compound collapse benchmark: 5% ± 3%, adjusted down for some international response)

## Transmission Channels

### Migration Channel

**Direction**: Pakistan → Afghanistan, Iran, India (all constrained), Gulf states (labor return)

**Mechanism**: Mass displacement with hostile or closed borders in all directions
- India: Highly unlikely to accept refugees; border militarized
- Afghanistan: Already in crisis; no capacity to absorb
- Iran: Limited willingness; economic stress
- Gulf states: Would expel Pakistani workers, compounding crisis

**Implication**: "Trapped population" dynamic—displacement is internal or fatal, not international resettlement

### Nuclear Security Channel

**Mechanism**: State failure raises concerns about command-and-control of nuclear arsenal

**Affected actors**: India (immediate threat), US/international community (proliferation risk)

**Scenario variants**:
- Military maintains cohesion → arsenal secured but military government
- Military fragments → arsenal security uncertain
- External intervention to secure weapons → escalation risk

### Regional Contagion Channel

**Afghanistan**: Further destabilization, ungoverned space expansion
**India**: Refugee pressure, terrorism risk, potential opportunistic action in Kashmir
**China**: Belt and Road investments at risk, CPEC corridor

### Remittance Channel

**Mechanism**: Pakistani diaspora (Gulf, UK, US) sends ~$30B/year in remittances
- Crisis disrupts receiving infrastructure
- Gulf states may expel workers during crisis
- Remittance collapse deepens economic crisis (feedback loop)

### Terrorism/Ungoverned Space Channel

**Mechanism**: State failure creates safe havens for militant groups
**Affected regions**: Afghanistan, India, potentially global

## Causal Relationships

### Caused By (increases probability)

| Event | Mechanism |
|-------|-----------|
| Indus Water Crisis | Core driver—water stress is binding constraint |
| Global Food Price Spike | Food import dependency, fiscal strain |
| India-Pakistan Military Conflict | External shock overwhelming weakened state |
| Global Financial Crisis | IMF/external financing dries up |
| Severe Drought (regional) | Agricultural collapse |

### Causes (makes more likely)

| Event | Mechanism |
|-------|-----------|
| India-Pakistan Nuclear Exchange | Escalation risk during state collapse |
| Afghanistan Further Collapse | Regional destabilization |
| South Asian Refugee Crisis | Mass displacement with closed borders |
| Terrorism Resurgence | Ungoverned space |

## Historical Analogues

| Case | Relevance | Key Difference |
|------|-----------|----------------|
| Syria | Compound crisis → state failure | Syria had active external intervention; Pakistan has nuclear weapons |
| Venezuela | Economic collapse → state dysfunction | Venezuela didn't experience state territorial fragmentation |
| Soviet Collapse | Nuclear state dissolution | Soviet collapse was negotiated; Pakistan failure would be chaotic |
| Yemen | State failure + external intervention | Yemen is smaller, non-nuclear |

## Source Documentation

- collapse-patterns-predictive-framework.md: Regional vulnerability assessment (Section 7.2.1), impact benchmarks
- 21st_century_assessment.md: Pakistan trajectory assessment (South Asia section)
- IPCC reports: Indus basin water stress projections
- IMF Article IV consultations: Fiscal sustainability analysis

## Confidence Assessment

| Dimension | Confidence | Notes |
|-----------|------------|-------|
| Probability estimate | Medium | Historical patterns exist; structural vulnerabilities clear |
| Factor loadings | Medium-High | Drivers are well-understood |
| Impact magnitude | Medium | Benchmarks from historical cases; Pakistan-specific adjustment uncertain |
| Transmission channels | Medium | Nuclear dimension is unprecedented |

## Notes

Pakistan represents one of the highest-consequence potential state failures due to nuclear weapons, population size (240M), and regional position. The compound nature of its vulnerabilities (water + food + fiscal + political) means that multiple pathways can lead to the same outcome.

The "trapped population" dynamic is crucial: unlike Syrian refugees who could reach Europe, Pakistani displacement would be largely contained by hostile borders, increasing mortality and internal displacement while limiting international visibility.

Military cohesion is the key swing variable—Pakistani military has historically intervened to prevent complete state failure, but may itself fragment under sufficient stress.