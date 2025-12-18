---
title: durability-types
type: note
permalink: methodology/reference/durability-types
tags:
- methodology
- reference
- durability
- impacts
- permanent
- decaying
- maintenance
---

# Durability Types Reference

**Critical insight**: Durability depends on the **type of impact**, not the "valence" of the event. Deaths are permanent whether from a pandemic or a war. Agreements require maintenance whether they're peace treaties or climate deals.

---

## The Five Durability Types

| Type | Behavior | Key Parameters |
|------|----------|----------------|
| **permanent** | Never reverses | None |
| **decaying** | Fades toward baseline | `half_life`, `floor` |
| **maintenance_required** | Fails without ongoing effort | `annual_failure_prob`, `failure_conditions` |
| **shock_vulnerable** | Can be reversed by other events | `vulnerable_to`, `reversal_fraction` |
| **regime_dependent** | Persists only in certain system states | `persists_in_regimes` |

---

## Permanent

**What it means**: The impact never reverses. Once it happens, it's permanent.

**Examples**:
- Mortality (deaths don't reverse)
- Knowledge/capability gains (scientific discoveries, weapons programs)
- Resource depletion (exhausted reserves stay exhausted)
- Ecosystem transitions with hysteresis (forest → savanna)
- Technology adoption post-saturation (deployed infrastructure)

**Specification**:
```yaml
durability:
  type: permanent
```

---

## Decaying

**What it means**: Impact fades over time toward baseline, with half the effect gone after a characteristic half-life.

**Examples**:
- GDP shocks (economies recover)
- Financial market dislocations (confidence returns)
- Reputational damage (memories fade)
- Infrastructure damage (can be rebuilt)
- Displacement (some refugees return)
- Institutional damage (can be rebuilt, slowly)

**Parameters**:
- `half_life`: Years for 50% of impact to fade
- `floor`: Minimum persistent impact (0 = full recovery possible)

**Specification**:
```yaml
durability:
  type: decaying
  half_life: 5  # years
  floor: 0.1    # 10% of impact is permanent scarring
```

**Common Half-Lives**:
| Impact Type | Typical Half-Life |
|-------------|-------------------|
| Financial shock | 1-2 years |
| GDP deviation | 2-5 years |
| Consumer confidence | 1-3 years |
| Infrastructure damage | 3-10 years (depends on resources) |
| Institutional decay | 10-30 years |
| Displacement | 5-15 years (context-dependent) |

---

## Maintenance Required

**What it means**: The impact persists only with ongoing effort. Each year, there's a probability it fails.

**Examples**:
- Treaties and agreements (parties may defect)
- Alliances (require continued mutual benefit)
- Policy achievements (can be reversed by new government)
- International institutions (require buy-in)
- Peace agreements (require ongoing compliance)

**Parameters**:
- `annual_failure_prob`: Probability the arrangement fails each year
- `failure_conditions`: State conditions that increase failure probability
- `cascade_on_failure`: Whether failure triggers other events

**Specification**:
```yaml
durability:
  type: maintenance_required
  annual_failure_prob: 0.05  # 5% per year
  failure_conditions:
    - regime_change_in_major_party
    - economic_crisis_in_major_party
    - external_shock_exceeds: 0.7
  cascade_on_failure: true
```

**Historical Reference Points**:
| Agreement Type | Typical Annual Failure Rate |
|----------------|---------------------------|
| Montreal Protocol (strong) | ~1% |
| NPT (moderate) | ~2% |
| Bilateral peace agreements | ~3-5% |
| Climate agreements | ~5-10% |
| Arms control agreements | ~3-8% |
| Weak international agreements | ~10-15% |

---

## Shock Vulnerable

**What it means**: The impact can be reversed if certain other events occur.

**Examples**:
- Development gains (can be wiped out by crisis)
- Living standards improvements (vulnerable to economic collapse)
- Institutional improvements (vulnerable to state failure)
- Infrastructure investments (vulnerable to conflict)
- Economic growth trajectory (vulnerable to financial crisis)

**Parameters**:
- `vulnerable_to`: List of events that can reverse the impact
- `reversal_fraction`: Fraction of gains lost if shock occurs

**Specification**:
```yaml
durability:
  type: shock_vulnerable
  vulnerable_to: [FINANCIAL_CRISIS, STATE_FAILURE, MAJOR_CONFLICT]
  reversal_fraction: 0.5  # Lose half the gains if shocked
```

---

## Regime Dependent

**What it means**: The impact persists only in certain system states. A regime change can eliminate it entirely.

**Examples**:
- Political achievements tied to specific regime type
- Democratic reforms (vulnerable to authoritarian transition)
- Authoritarian control (vulnerable to democratization)
- Alliance commitments under specific leadership
- Economic arrangements dependent on regime ideology

**Parameters**:
- `persists_in_regimes`: Which regime types preserve this impact
- `transitions_with`: What variable determines regime type

**Specification**:
```yaml
durability:
  type: regime_dependent
  persists_in_regimes: [democracy, hybrid_democratic]
  transitions_with: regime_type
```

---

## Durability by Impact Category

Quick reference for common impact types:

| Impact Category | Typical Durability | Notes |
|-----------------|-------------------|-------|
| **Mortality** | permanent | Deaths don't reverse |
| **Physical destruction** | decaying | Recovery time depends on resources |
| **Infrastructure damage** | decaying | Half-life varies by severity |
| **Institutional collapse** | decaying (long) | 10-30 year recovery |
| **Treaties/agreements** | maintenance_required | Annual defection probability |
| **Alliance formation** | maintenance_required | Requires continued benefit |
| **Technology adoption** | permanent | Deployed tech doesn't un-deploy |
| **Knowledge/capability** | permanent | Discoveries aren't forgotten |
| **GDP shocks** | decaying | Typical half-life 2-5 years |
| **Living standards** | shock_vulnerable | Can be reversed by crises |
| **Political achievements** | regime_dependent | May not survive regime change |
| **Ecosystem transitions** | permanent | Hysteresis effects |
| **Resource depletion** | permanent | Exhausted reserves stay exhausted |
| **Market dislocations** | decaying | Prices/confidence recover |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Assigning durability by event "valence" | Assign by impact type—deaths are permanent whether good or bad |
| "Positive events are fragile" | Treaties require maintenance; but so do sanctions and alliances |
| Single durability for whole event | Different impacts within one event can have different durabilities |
| Ignoring recovery conditions | Decaying impacts may require conditions (state capacity, resources) |
| Permanent when clearly recoverable | Use decaying with appropriate half-life |

---

## Specifying Durability in Event Templates

In the impact vector section:

```yaml
impact_vector:
  global:
    gdp_real:
      magnitude: -0.03
      onset: immediate
      durability:
        type: decaying
        half_life: 3
        floor: -0.005  # small permanent scarring
        
    displaced_population:
      magnitude: 10  # millions
      onset: immediate
      durability:
        type: decaying
        half_life: 8
        recovery_conditions:
          - conflict_intensity < 2
          - origin_country.regime_stability > 40
          
    treaty_effect:
      magnitude: -0.25  # 25% emissions reduction
      onset: gradual(5)
      durability:
        type: maintenance_required
        annual_failure_prob: 0.08
        failure_conditions:
          - leadership_change_in_major_party
          - economic_crisis_severity > 0.6
```

---

*See [[methodology/00-start-here]] for navigation | [[methodology/reference/impact-estimation]] for magnitude estimation*