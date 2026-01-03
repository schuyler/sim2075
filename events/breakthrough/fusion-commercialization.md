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

Commercial fusion power achieves grid-scale deployment: (1) net-positive energy reactors operating commercially, (2) levelized cost competitive with alternatives, (3) clear pathway to scaled deployment. This represents a discrete technological discontinuity — the baseline assumption is that fusion remains "30 years away" indefinitely.

**What marks occurrence**: First commercial fusion plant achieves sustained operation AND credible cost projections demonstrate competitiveness AND multiple follow-on projects are funded/under construction.

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

---

## Probability

```yaml
probability:
  annual: 0.009
  range: [0.004, 0.018]
  confidence: low-medium
```

### Base Rate Derivation

**Reference class**: Major energy technology breakthroughs achieving commercial deployment

| Decade | Breakthrough | Time to Commercial |
|--------|--------------|-------------------|
| 1950s | Nuclear fission | ~15 years |
| 1970s | Combined-cycle gas turbines | ~20 years |
| 2010s | Shale oil/gas | ~10 years |
| 2010s-20s | Utility-scale solar/wind | ~15 years |

**Calculation**: 2-4 major energy breakthroughs per century. Fusion is one of ~3-5 candidates for next breakthrough. Assign ~25% of "energy breakthrough" probability mass.

(3 breakthroughs/century) × (25% fusion share) = 0.75%/year base

### Condition Adjustments

| Condition | Adjustment | Rationale |
|-----------|------------|-----------|
| Private investment surge | +0.2% | Commonwealth, TAE, Helion: $6B+ in private capital |
| ITER progress | +0.1% | Validates tokamak path |
| AI/ML acceleration | +0.1% | Optimizing plasma control, materials discovery |
| Supply chain constraints | -0.1% | Tritium, superconducting magnets limited |
| Regulatory uncertainty | -0.1% | No established licensing pathway |

**Net adjustment**: +0.2% → 0.9%/year

### Probability Evolution

| Period | Annual P | Rationale |
|--------|----------|-----------|
| 2025-2035 | 0.8-1.2% | Private venture milestones; ITER progress |
| 2035-2050 | 0.8-1.5% | Path-dependent on early results |
| 2050-2075 | 0.5-1.5% | Solar+storage competition may shrink market need |

### Case Against

**Fusion has been "30 years away" for 70 years**: History of repeated disappointment. Private investment surges occurred before (1980s, 2000s) without breakthrough.

*Counter*: Private investment today differs qualitatively — multiple credible approaches with near-term milestones, not just government megaprojects.

**Solar+storage may solve the same problem cheaper**: By the time fusion achieves commercialization, the market need may have disappeared.

*Counter*: Fusion offers baseload power without intermittency; different value proposition than solar+storage.

**Engineering challenges are more severe than scientific ones**: NIF ignition demonstrated scientific feasibility, but commercial viability requires sustained operation, neutron-resistant materials, working tritium breeding.

*Counter*: Valid concern captured in wide probability range (0.4-1.8%).

---

## Factor Loadings

```yaml
factors:
  F_TECH: 0.56  # R&D investment, scientific progress cluster together
  F_FIN: 0.28   # Capital availability for long-horizon development
  F_GPT: 0.16   # Great power competition affects collaboration and national programs
variance: 0.55  # Breakthrough target
```

---

## Branches

```yaml
branches:
  - {id: gradual, p: 0.50, desc: "Diffusion over 15-25 years (nuclear fission pattern)"}
  - {id: rapid, p: 0.30, desc: "10-year transformation (solar/wind 2015-2025 pattern)"}
  - {id: concentrated, p: 0.20, desc: "One great power achieves decisive lead; technology hoarded"}
```

---

## Impacts

### Transmission Channels

**Energy Prices**: Fusion provides baseload electricity at lower marginal cost, reducing demand for fossil fuels. Oil and gas prices decline as substitution occurs.

**Industrial Competitiveness**: Energy-intensive industries gain cost advantage in fusion-powered regions. Captured via GDP effects.

**Petrostate Revenue**: Countries dependent on hydrocarbon exports face structural revenue decline.

**Climate Trajectory**: Reduced fossil fuel use lowers emissions growth. This affects `global_co2_ppm` drift rate via baseline dynamics, not direct shock — captured in cascade effects on climate tipping point probabilities.

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

### Climate Effects Note

Fusion's climate benefit operates through reduced fossil fuel consumption → lower emissions → slower `global_co2_ppm` accumulation → lower `global_temp_anomaly` trajectory. This is a *dynamics modification*, not a direct shock to a state variable. For v1.0, we capture this via cascade effects on climate tipping point probabilities. Full emissions-temperature coupling is Phase 2 work.

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

## Open Questions

1. Is tritium availability a binding constraint on deployment scale?
2. How quickly can licensing frameworks be established?
3. Does fusion's baseload characteristic create grid integration challenges?
4. Should we model separate US vs. China vs. private sector breakthrough branches?
5. How to model fossil fuel stranded assets and financial system effects?

---

## Changelog

| Date | Change |
|------|--------|
| 2025-12-25 | Initial Level 1 specification |
| 2025-12-30 | Critical review complete |
| 2025-01-01 | Migrated to YAML-embedded schema |
| 2025-01-02 | Revised impacts to use only observable state variables; climate effects via cascades |

---

*See [[events/planned-breakthrough-events]] for context | [[methodology/reference/probability-estimation]] for Type 1 methodology*
