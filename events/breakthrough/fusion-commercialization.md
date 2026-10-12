---
title: fusion-commercialization
type: note
permalink: events/breakthrough/fusion-commercialization
tags:
- event
- type-1
- stochastic
- technology
- energy
- fusion
- breakthrough
- global
- level-1
---

# Fusion Commercialization

**Type 1 (Stochastic) Event** — Technological breakthrough with timing unpredictable; base rate from analog reference class.

---

## Description

Commercial fusion power achieves grid-scale deployment, defined as: (1) net-positive energy reactors operating commercially, (2) levelized cost competitive with alternatives in major markets, and (3) clear pathway to scaled deployment. This represents a discrete technological discontinuity — the baseline assumption is that fusion remains "30 years away" indefinitely. Successful commercialization would fundamentally restructure global energy systems, with cascading effects on climate trajectories, petrostate economies, and industrial geography.

**What marks occurrence**: First commercial fusion plant achieves sustained operation AND credible cost projections demonstrate competitiveness AND multiple follow-on projects are funded/under construction. The event fires when commercialization is clearly underway, not at scientific demonstration.

---

## Specification

```yaml
id: FUSION_COMMERCIALIZATION
domain: technological
scale: global
causal_type: 1
onset: gradual
reversibility: irreversible
```

*Domain: technological / energy. Onset speed: gradual (5-15 years from first commercial operation to material system impact). Reversibility: irreversible (knowledge/capability gains permanent; deployment may vary).*

---

## Causal Type Specification (Type 1: Stochastic)

### Base Rate Derivation

**Reference class problem**: No prior fusion commercialization exists. Must use analog reference class.

**Analog reference class**: Major energy technology breakthroughs achieving commercial deployment

| Decade | Breakthrough | Time from feasibility to commercial scale |
|--------|--------------|-------------------------------------------|
| 1950s | Nuclear fission | ~15 years (1942 chain reaction → 1957 Shippingport) |
| 1970s | Combined-cycle gas turbines | ~20 years (concept → dominant new build) |
| 2010s | Shale oil/gas (horizontal drilling + fracking) | ~10 years (Mitchell experiments → US energy independence) |
| 2010s-20s | Utility-scale solar/wind | ~15 years (cost parity → dominant new capacity) |

**Observation**: Major energy technology breakthroughs occur roughly 2-4 times per century when the reference class is "technologies that fundamentally restructure energy systems."

**Current fusion state assessment**:
- Scientific feasibility: Demonstrated (NIF ignition 2022, JET records)
- Engineering feasibility: Partially demonstrated (ITER under construction, private ventures progressing)
- Economic feasibility: Undemonstrated (cost projections highly uncertain)
- Deployment pathway: Unclear (regulatory frameworks, supply chains not established)

**Base rate estimate**: Given 2-4 major energy breakthroughs per century and fusion being one of ~3-5 candidates for next breakthrough (alongside advanced geothermal, next-gen nuclear, breakthrough storage, direct air capture), assign fusion ~20-30% of the "energy breakthrough" probability mass.

Calculation: (3 breakthroughs/century) × (25% fusion share) = 0.75%/year

### Condition Adjustments

| Condition | Adjustment | Rationale |
|-----------|------------|-----------|
| Private investment surge (2020s) | +0.2% | Commonwealth, TAE, Helion, others attracted $6B+ in private capital; parallel development paths |
| ITER progress | +0.1% | First plasma expected late 2030s; validates tokamak path even if delayed |
| AI/ML acceleration | +0.1% | Machine learning optimizing plasma control, materials discovery |
| Supply chain constraints | -0.1% | Specialized materials (tritium, superconducting magnets) have limited supply |
| Regulatory uncertainty | -0.1% | No established licensing pathway in most jurisdictions |

**Net adjustment**: +0.2% → adjusted annual probability 0.8-1.0% (central estimate: 0.9%)

---

## Probability

```yaml
probability:
  annual: 0.009
  range: [0.004, 0.018]
  confidence: low
```

| Metric | Value |
|--------|-------|
| **Annual probability** | 0.9% |
| **Low bound** | 0.4% |
| **High bound** | 1.8% |
| **Confidence** | Low-Medium (recorded as `low` in YAML: the schema enum is `low|medium|high`) |
| **25-year cumulative** | ~20% at point estimate |
| **50-year cumulative** | ~36% at point estimate |

### Derivation

1. **Analog base rate**: ~0.75%/year from energy breakthrough reference class
2. **Condition adjustments**: Net +0.2% from accelerating investment and scientific progress
3. **Final estimate**: 0.9%/year (range 0.4%-1.8%)

The wide range reflects genuine uncertainty—fusion could remain perpetually "30 years away" (low bound) or private sector approaches could achieve breakthrough faster than historical analogs suggest (high bound).

### Comparative Ranking

Per [[methodology/reference/priority-event-ranking]] logic:
- **Less likely than**: Severe pandemic (2.0%), global financial crisis (3.0%)
- **Similar to**: AMOC weakening (1.0%), major state failures (0.8-1.5%)
- **More likely than**: Catastrophic asteroid impact (0.01%)

This ranking seems appropriate—fusion commercialization is a "once per lifetime" possibility, not a near-term expectation, but also not a fantasy.

### Key Uncertainties

- **Private sector wildcards**: Commonwealth Fusion, Helion, TAE pursuing different approaches; any could achieve breakthrough or all could stall
- **ITER outcome**: Success validates path; failure could chill investment for decades
- **Competitor technologies**: If solar+storage or advanced geothermal solve the same problems cheaper, fusion investment may decline
- **Tritium availability**: Breeding blanket technology unproven at scale; tritium scarcity could bottleneck deployment
- **"Faster than expected" scenario**: If compact tokamaks or alternative approaches work, timeline could compress dramatically

### Case Against

**Fusion has been "30 years away" for 70 years**: The history of fusion promises is one of repeated disappointment. Private investment surges have occurred before (1980s, 2000s) without breakthrough. The 0.9%/year estimate may be optimistic given this track record.

**Solar+storage may solve the same problem cheaper**: Grid-scale solar with battery storage is achieving cost reductions on a steeper curve than any fusion pathway. By the time fusion achieves commercialization, the market need may have disappeared. Fusion may be a solution in search of a problem.

**Engineering challenges are more severe than scientific ones**: NIF ignition demonstrated scientific feasibility, but commercial viability requires sustained operation (not single shots), materials that withstand neutron bombardment, tritium breeding that actually works, and costs competitive with alternatives. These engineering challenges may prove intractable even with scientific success.

**Regulatory timelines are prohibitive**: Nuclear licensing takes decades. Even if fusion technology works, regulatory approval for commercial plants may take 10-15 years in most jurisdictions. First commercial operation ≠ material grid impact.

**Reference class selection is questionable**: Comparing fusion to shale or solar may be inappropriate. Shale used existing drilling technology in new ways; solar scaled existing manufacturing. Fusion requires building entirely new industrial supply chains. The "energy breakthrough" reference class may be too optimistic.

*Counter*: The counterarguments are valid but incomplete. Private investment today differs qualitatively from past surges—multiple credible approaches with near-term milestones, not just government megaprojects. NIF ignition was a genuine scientific breakthrough, not hype. Fusion offers baseload power without intermittency, a different value proposition than solar+storage. The estimate acknowledges uncertainty with a 0.4-1.8% range and explicitly models the possibility that fusion remains "30 years away" indefinitely.

### Probability Evolution

As a Type 1 stochastic event, probability is relatively stable but influenced by R&D progress and competitor technologies:

| Period | Annual P | Rationale |
|--------|----------|-----------|
| 2025-2035 | 0.8-1.2% | Private venture milestones expected; ITER progress; but still early stage |
| 2035-2050 | 0.8-1.5% | If early milestones hit, acceleration likely; if not, probability declines |
| 2050-2075 | 0.5-1.5% | Highly path-dependent on 2025-2050 outcomes; solar+storage competition intensifies |

**Key inflection points**:
- Commonwealth/Helion/TAE milestones (2025-2030): Success accelerates; failure chills investment
- ITER first plasma and full operation: Validates tokamak path or exposes challenges
- Solar+storage cost trajectory: If battery costs fall 10× more, fusion market shrinks
- First commercial plant (if achieved): Validates deployment pathway and triggers acceleration

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve breakthrough target (ΛΩΛᵀ)ᵢᵢ = 0.55*

```yaml
factors:
  F_TECH: 0.56  # R&D investment, scientific progress cluster together
  F_FIN: 0.28   # Capital availability for long-horizon development
  F_GPT: 0.16   # Great power competition affects collaboration and national programs
variance: 0.55  # Breakthrough target
```

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_TECH** | 0.56 | Primary driver: R&D investment, scientific progress, engineering breakthroughs cluster together; high F_TECH year means accelerated progress across frontier technologies |
| **F_FIN** | 0.28 | Capital availability for long-horizon, capital-intensive development; private fusion ventures require sustained investment through long development cycles |
| **F_GPT** | 0.16 | Great power tension affects technology sharing, international collaboration (ITER), and may accelerate national programs through competition |
| F_CLIM | 0.00 | Climate stress doesn't accelerate fusion timeline (unlike solar, which benefits from policy urgency) |
| F_EUR | 0.00 | Regional stress doesn't affect fusion probability |
| F_EAS | 0.00 | No pathway (China fusion program captured in F_TECH) |
| F_HLTH, F_FOOD, F_MENA, F_SAS, F_SSA, F_LAM | 0.00 | No pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.55 (breakthrough target); scale factor = 0.80 from original loadings.

### Loading Interpretation (Type 1)

For Type 1 events, factors modify annual probability through correlated conditions:
- High F_TECH → accelerated R&D across sectors → fusion more likely to achieve breakthrough in same period
- High F_FIN → capital availability → sustained investment in capital-intensive fusion development
- High F_GPT → great power competition → potential acceleration of national programs (US, China), but also reduced collaboration

---

## Branches

Once fusion commercialization occurs, deployment patterns vary:

```yaml
branches:
  - {id: gradual, p: 0.50, desc: "Diffusion over 15-25 years (nuclear fission pattern)"}
  - {id: rapid, p: 0.30, desc: "10-year transformation (solar/wind 2015-2025 pattern)"}
  - {id: concentrated, p: 0.20, desc: "One great power achieves decisive lead; technology hoarded"}
```

### Gradual Diffusion (50%)

Single nation or company achieves commercial deployment. Technology diffuses over 15-25 years through licensing, parallel development, and gradual cost reduction. Similar to nuclear fission deployment pattern (1957-1980s).

| Attribute | Value |
|-----------|-------|
| **Impact multiplier** | 1.0× |
| **Deployment timeline** | 20 years to material global impact |
| **First mover advantage** | Moderate |
| **Petrostate adjustment time** | 15-20 years |
| **Climate trajectory improvement** | Gradual |

### Rapid Transformation (30%)

Multiple approaches succeed in quick succession. Costs decline faster than expected (learning curve acceleration). Deployment resembles solar/wind 2015-2025 rather than nuclear 1960s.

| Attribute | Value |
|-----------|-------|
| **Impact multiplier** | 2.0× |
| **Deployment timeline** | 10 years to material global impact |
| **First mover advantage** | Limited (fast-follower viable) |
| **Petrostate adjustment time** | 8-12 years |
| **Climate trajectory improvement** | Rapid |

### Geopolitically Concentrated (20%)

One great power (US or China) achieves decisive lead. Technology treated as strategic asset with restricted transfer. Creates energy technology dependency analogous to current semiconductor concentration.

| Attribute | Value |
|-----------|-------|
| **Impact multiplier** | 1.5× |
| **Deployment timeline** | 15 years, but geographically uneven |
| **First mover advantage** | Extreme |
| **Petrostate adjustment time** | Varies by alignment |
| **Great power implications** | Significant |

### Branch Probability Rationale

- **Gradual diffusion (0.50)**: Historical pattern for major energy technologies. Nuclear fission, despite its revolutionary nature, took decades to deploy globally. Regulatory, supply chain, and workforce constraints apply.
- **Rapid transformation (0.30)**: Solar/wind demonstrated that energy technology deployment can accelerate dramatically with manufacturing scale-up and policy support. If fusion follows similar pattern, transformation could be faster than nuclear precedent suggests.
- **Geopolitically concentrated (0.20)**: Current great power competition and technology restriction trends (semiconductors, AI) suggest breakthrough technologies may be hoarded rather than shared. Probability lower because fusion requires large-scale deployment to be economically significant—hard to restrict entirely.

---

## Impacts

### Transmission Channels

**Energy Prices**: Fusion provides baseload electricity at lower marginal cost than fossil alternatives, collapsing electricity prices and reducing oil/gas demand for power generation. Affected regions: all, but especially energy importers (benefit) and exporters (harm). Affected variables: `oil_brent`, `gas_europe_ttf`, `gas_asia_lng`, `energy_import_dependence`, `current_account`. Differential exposure: energy intensity of economy, import/export status.

**Industrial Competitiveness**: Energy-intensive industries (aluminum, steel, chemicals, computing) gain cost advantage in fusion-powered regions. Affected regions: developed economies with fusion deployment; energy-intensive manufacturing centers. Captured via GDP effects. Differential exposure: industrial structure, proximity to fusion deployment.

**Petrostate Revenue**: Countries dependent on hydrocarbon exports face structural revenue decline. Captured as GDP and current-account rows on the exposed economies.

**Climate Trajectory**: Fusion enables deep decarbonization of electricity and potentially transport/heating, reducing cumulative emissions. This affects `global_co2_ppm` drift rate via baseline dynamics, not direct shock — captured in cascade effects on climate tipping point probabilities (see Climate Effects Note).

**Geopolitical Alignment**: Reduced dependence on energy imports shifts alliance calculations; petrostates lose leverage. Affected regions: energy importers, petrostates, great powers. Not carried as impact rows at Level 1.

```yaml
impacts:
  gradual:
    # Energy prices
    - {var: oil_brent,                  mag: [-25, 10],     onset: {gradual: 15}, permanent: true}
    - {var: gas_europe_ttf,             mag: [-15, 8],      onset: {gradual: 12}, permanent: true}
    - {var: gas_asia_lng,               mag: [-4, 2],       onset: {gradual: 12}, permanent: true}
    - {var: renewable_cost_index,       mag: [-20, 10],     onset: {gradual: 10}, permanent: true}
    
    # Petrostate impacts (GDP decline from revenue loss)
    - {var: sau.gdp_real,               mag: [-0.15, 0.08], onset: {gradual: 15}, permanent: true}
    - {var: sau.current_account,        mag: [-0.12, 0.05], onset: {gradual: 12}, permanent: true}
    - {var: rus.gdp_real,               mag: [-0.12, 0.06], onset: {gradual: 15}, permanent: true}
    - {var: rus.current_account,        mag: [-0.08, 0.04], onset: {gradual: 12}, permanent: true}
    - {var: irn.gdp_real,               mag: [-0.18, 0.08], onset: {gradual: 15}, permanent: true}
    - {var: are.gdp_real,               mag: [-0.10, 0.05], onset: {gradual: 15}, permanent: true}
    - {var: nga.gdp_real,               mag: [-0.08, 0.05], onset: {gradual: 15}, permanent: true}
    - {var: kaz.gdp_real,               mag: [-0.10, 0.05], onset: {gradual: 15}, permanent: true}
    
    # Energy importer benefits
    - {var: jpn.gdp_real,               mag: [0.03, 0.02],  onset: {gradual: 15}, permanent: true}
    - {var: jpn.current_account,        mag: [0.04, 0.02],  onset: {gradual: 12}, permanent: true}
    - {var: jpn.energy_import_dependence, mag: [-0.25, 0.10], onset: {gradual: 15}, permanent: true}
    - {var: kor.gdp_real,               mag: [0.02, 0.01],  onset: {gradual: 15}, permanent: true}
    - {var: ind.gdp_real,               mag: [0.04, 0.02],  onset: {gradual: 20}, permanent: true}
    - {var: chn.gdp_real,               mag: [0.02, 0.02],  onset: {gradual: 15}, permanent: true}
    - {var: deu.gdp_real,               mag: [0.015, 0.01], onset: {gradual: 15}, permanent: true}

  rapid:
    inherit: gradual
    scale: 2.0

  concentrated:
    inherit: gradual
    scale: 1.5
```

*Units: `gdp_real` rows are fractions of the entity's current value (Saudi Arabia −15% ± 8%); the energy-price rows are additive in the variable's units ([[methodology/reference/event-yaml-schema]] §Impact Fields).*

### Petrostate and Importer Exposure

**Petrostate losers** (negative economic impact):

| Country | GDP Impact | Onset | Mechanism |
|---------|------------|-------|-----------|
| Saudi Arabia | -15% ± 8% | gradual(15yr) | Oil revenue collapse; Vision 2030 insufficient diversification |
| UAE | -10% ± 5% | gradual(15yr) | More diversified; financial hub role partially protects |
| Russia | -12% ± 6% | gradual(15yr) | Gas exports to Europe collapse; limited diversification |
| Iran | -18% ± 8% | gradual(15yr) | Oil/gas dominant; sanctions limit adaptation |
| Nigeria | -8% ± 5% | gradual(15yr) | Oil-dependent but lower per-capita exposure |
| Kazakhstan | -10% ± 5% | gradual(15yr) | Energy exports to China decline |

**Energy importer beneficiaries** (positive economic impact):

| Country/Region | GDP Impact | Onset | Mechanism |
|----------------|------------|-------|-----------|
| Japan | +3% ± 2% | gradual(15yr) | Eliminates energy import dependence vulnerability |
| South Korea | +2% ± 1% | gradual(15yr) | Energy cost reduction; industrial competitiveness |
| India | +4% ± 2% | gradual(20yr) | Energy abundance enables industrialization |
| EU (aggregate) | +2% ± 1% | gradual(15yr) | Energy security; industrial reshoring potential (carried as Germany in the YAML) |
| China | +2% ± 2% | gradual(15yr) | Reduced import dependence; but disrupts domestic coal |

**Exposure variables for differential impact**:
- `energy_import_dependence`: Higher → larger benefit from cheap energy
- `export_concentration` (in hydrocarbons): Higher → larger loss from demand collapse
- `gdp_share_industry`: Higher → larger benefit from energy cost reduction

### Impact Derivation

**Primary method**: Structural reasoning + historical analogs

- **Energy price impacts**: Scaled from historical energy technology shocks (oil crises in reverse). The original specification expressed these as percentages (`oil_brent` −35% ± 15%, `gas_europe_ttf` −45% ± 20%, `renewable_cost_index` −40% ± 15%); the migration re-expressed them in the variables' own units against the 2025 baselines.
- **Petrostate GDP impacts**: Based on hydrocarbon share of GDP and export revenue
- **Climate impacts**: IPCC scenario differentials between high/low energy transition pathways (not direct rows; see Climate Effects Note)
- **Beneficiary impacts**: Energy cost as share of GDP × assumed cost reduction

### Durability Specifications

| Impact Type | Durability | Parameters | Rationale |
|-------------|------------|------------|-----------|
| Energy cost reduction | permanent | N/A | Technology doesn't un-invent; cost floor established |
| Emissions trajectory | permanent | N/A | Cumulative emissions permanently lower |
| Petrostate GDP impact | shock_vulnerable (original); permanent in YAML | vulnerable_to: [oil price recovery, alternative uses] | Could partially reverse if energy transition slows; the shock-vulnerable form is schema v0.2 backlog |
| Industrial location shifts | maintenance_required (original); not a row | annual_failure: 5% | Requires sustained cost advantage |
| Climate trajectory improvement | permanent | N/A | Lower cumulative emissions = lower peak warming |

### Climate Effects Note

Fusion's climate benefit operates through reduced fossil fuel consumption → lower emissions → slower `global_co2_ppm` accumulation → lower `global_temp_anomaly` trajectory. This is a *dynamics modification*, not a direct shock to a state variable. For v1.0, we capture this via cascade effects on climate tipping point probabilities. Full emissions-temperature coupling is Phase 2 work. The original specification's direct rows (`global_co2_ppm` −50 ± 30 ppm by 2075, `global_temp_anomaly` −0.3°C ± 0.2°C by 2075) record the intended magnitude of that coupling.

---

## Cascades

```yaml
cascades:
  triggers:
    # Petrostate destabilization (revenue loss → regime stress)
    - {event: SAUDI_REGIME_INSTABILITY, delta: 0.008, years: 15}
    - {event: IRAN_REGIME_CHANGE,       delta: 0.006, years: 15}
    - {event: RUSSIA_STATE_FAILURE,     delta: 0.004, years: 15}
    
    # Climate risk reduction (fewer emissions → lower tipping risk)
    - {event: AMOC_WEAKENING,           delta: -0.003, years: 30}
    - {event: AMAZON_TIPPING_POINT,     delta: -0.002, years: 30}
    - {event: PERMAFROST_METHANE_RELEASE, delta: -0.002, years: 30}
    
    # Energy market stabilization
    - {event: OIL_SUPPLY_SHOCK,         delta: -0.005, years: 20}
  triggered_by: []  # Breakthrough timing is fundamentally stochastic
```

### Cascade Mechanisms

| Pathway | Target Event | Probability Change | Duration | Mechanism |
|---------|--------------|-------------------|----------|-----------|
| Petrostate revenue collapse → regime instability | SAUDI_REGIME_INSTABILITY | +0.8%/year | 15 years | Fiscal crisis undermines social contract; youth unemployment |
| Petrostate revenue collapse → regime instability | IRAN_REGIME_CHANGE | +0.6%/year | 15 years | Reduced resources for regime maintenance |
| Petrostate revenue collapse → state failure | RUSSIA_STATE_FAILURE | +0.4%/year | 15 years | Resource curse unwinding; regional power loss |
| Energy abundance → reduced conflict | OIL_SUPPLY_SHOCK | -0.5%/year | 20 years | Lower strategic value of oil reserves/shipping lanes |
| Climate trajectory improvement | AMOC_WEAKENING | -0.3%/year | 30 years | Lower peak warming reduces tipping point risk |
| Climate trajectory improvement | AMAZON_TIPPING_POINT | -0.2%/year | 30 years | Lower temperature stress on ecosystem |
| Climate trajectory improvement | PERMAFROST_METHANE_RELEASE | -0.2%/year | 30 years | Lower temperature stress on permafrost |

### Impact Chains

**Pathway 1**: Fusion → Petrostate crisis → Regional instability
```
Fusion commercialization → oil demand collapse → petrostate fiscal crisis →
social spending cuts → legitimacy crisis → P(regime instability) ↑
```

**Pathway 2**: Fusion → Climate improvement → Reduced tipping point risk
```
Fusion commercialization → accelerated decarbonization → lower cumulative emissions →
lower peak warming → P(climate tipping points) ↓
```

**Pathway 3**: Fusion → Energy abundance → Industrial transformation
```
Fusion commercialization → cheap energy → energy-intensive industry viable →
industrial location shifts → developed economy re-industrialization
```

---

## Research Status

```yaml
research:
  tier: 1
  updated: 2025-01-02
  review: complete
  upgrade: true
```

### Upgrade Rationale

- Private fusion venture progress (Commonwealth, Helion, TAE milestones)
- ITER timeline updates
- Petrostate impact calibration

## Sources

*Level 1 specification based on general knowledge. Key references for future documentation:*

- NIF ignition results (December 2022)
- ITER project status and timeline
- Private fusion venture announcements (Commonwealth, Helion, TAE)
- Historical energy technology deployment patterns
- IPCC scenarios for energy transition impacts

## Open Questions

1. **Tritium supply**: Is tritium availability a binding constraint on deployment scale?
2. **Regulatory pathway**: How quickly can licensing frameworks be established?
3. **Grid integration**: Does fusion's baseload characteristic create integration challenges in renewable-heavy grids?
4. **First mover dynamics**: Should we model separate branches for US vs. China vs. private sector achieving breakthrough?
5. **Technology pathway**: Does the specific approach (tokamak, stellarator, inertial, other) matter for impact?
6. **Stranded assets**: How to model fossil fuel infrastructure write-downs and associated financial system effects?
7. **Complementary technologies**: Does fusion require breakthrough storage or transmission to achieve full impact?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-25 | Initial Level 1 specification | Task 2.2.1 - first Type 1 breakthrough event |
| 2025-12-30 | Critical review complete | Task 2.4 systematic review - added Case Against and Probability Evolution sections |
| 2025-01-01 | Migrated to YAML-embedded schema | Task 4.2 format migration |
| 2025-01-02 | Revised impacts to use only observable state variables; climate effects via cascades | Observable-variable discipline |
| 2026-10-12 | **Remediated**: restored lost prose; `confidence: low` | Task 4.2.25 / data-track D1 — Restored full description and classification notes, current fusion state assessment, derivation, comparative ranking, key uncertainties, full Case Against, key inflection points, loading rationale table and interpretation, deployment branch tables and probability rationale, exposure tables and variables, impact derivation, durability specifications, cascade mechanisms, impact chains, transmission channel detail, sources, open questions 5-7, changelog rationale. The `low-medium` confidence wording stays in prose; the YAML enum is `low|medium|high` |

---

*See [[events/planned-breakthrough-events]] for context | [[methodology/reference/probability-estimation]] for Type 1 base rate methodology | [[methodology/reference/calibration-anchors]] for reference events*
