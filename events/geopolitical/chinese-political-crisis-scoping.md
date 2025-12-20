---
title: chinese-political-crisis-scoping
type: note
permalink: events/geopolitical/chinese-political-crisis-scoping
tags:
- event
- geopolitical
- type-2
- type-3
- hybrid
- china
- political-crisis
- scoping
- planning
---

# Chinese Political Crisis — Scoping Note

Pre-specification analysis for Task 2.1.13. Resolves definitional questions before drafting the full Level 1 specification.

---

## Event Definition

### Proposed Definition

**Chinese Political Crisis**: Acute political instability characterized by visible elite factional conflict, widespread social unrest beyond regime capacity to suppress quietly, or military/security apparatus fragmentation — representing a discrete transition from "managed authoritarian stability" to "contested regime survival."

This definition focuses on the *crisis state* rather than the *outcome*. The crisis is the Type 2 threshold event; how it resolves is the Type 3 component.

### What This Event IS

- Elite factional conflict that becomes publicly visible (purges, defections, competing power centers)
- Mass unrest exceeding the scale of 1989 Tiananmen (multiple cities, sustained duration, cross-class participation)
- Security apparatus fragmentation (PLA units refusing orders, regional military commands acting independently)
- Succession crisis with contested legitimacy
- Any combination creating genuine uncertainty about regime survival

### What This Event IS NOT

- Normal political turnover (smooth succession is baseline, not discontinuity)
- Localized protests (routine; thousands occur annually)
- Elite purges that consolidate power (Xi's anti-corruption campaign was *stabilizing*, not crisis)
- Economic stress without political manifestation (covered by [[events/financial/chinese-economic-crisis]])
- Gradual liberalization or reform (belongs in baseline trajectory)

### Threshold Distinction

The key modeling question: where is the line between "stressed but stable" and "crisis"?

| Indicator | Below Threshold | Above Threshold |
|-----------|-----------------|-----------------|
| Elite conflict | Internal; rumors only | Public statements; defections; competing claims |
| Social unrest | Localized; single-issue; suppressed | Multi-city; cross-issue; sustained >2 weeks |
| Security forces | Unified command; effective suppression | Hesitation; selective non-compliance; visible splits |
| Information control | Effective; narrative managed | Breakdown; competing narratives; international attention |
| Succession | Clear line; no challengers | Contested; multiple claimants; legitimacy disputed |

---

## Causal Type Analysis

### Type 2/3 Hybrid Structure

This event exhibits hybrid dynamics similar to [[events/geopolitical/taiwan-conflict]]:

**Type 2 Component (Threshold)**:
- Pressure accumulates through multiple channels
- At critical pressure level, crisis becomes likely
- Threshold represents regime capacity to manage accumulated stress

**Type 3 Component (Resolution)**:
- Once crisis occurs, outcome depends on actor decisions
- Elite faction choices, military loyalty decisions, protest movement strategies
- Resolution probabilities are intractable per [[methodology/concepts/small-n-actor-problem]]

### Modeling Approach

```
Pressure accumulates (Type 2) → Crisis threshold crossed → 
Resolution sampled (Type 3) → Aftermath branches
```

This follows the established pattern from Taiwan Conflict specification.

---

## Pressure Function (Type 2 Component)

### Candidate State Variables

| State Variable | Weight | Transform | Rationale |
|----------------|--------|-----------|-----------|
| `chn.regime_stability` | 0.25 | inverse | Composite legitimacy/stability metric |
| *economic_performance_gap* | 0.25 | linear | Gap between actual and expected growth; performance legitimacy |
| *elite_cohesion_index* | 0.20 | inverse | Factional conflict indicators; purge intensity |
| *social_unrest_index* | 0.15 | threshold(high) | Protest frequency/scale; labor actions |
| `chn.youth_unemployment` | 0.10 | linear | Youth alienation; protest recruitment pool |
| *succession_uncertainty* | 0.05 | linear | Time since last succession; age of leadership |

*Note: Variables in italics require definition or derivation. `chn.regime_stability` exists in state-specification but may need refinement for this use case.*

### Threshold Estimate

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Threshold estimate** | 80 on 0-100 scale | CCP has exceptional institutional capacity; higher threshold than typical authoritarian regime |
| **Uncertainty** | ±12 (range 68-92) | Regime opacity makes true fragility difficult to assess |
| **Sharpness (k)** | 12 | Sharp transition once threshold breached — authoritarian regimes tend to collapse rapidly once visible cracks appear |

### Current Pressure Assessment

Current pressure (2025): ~35-40 on 0-100 scale

- Economic performance: Slowing but not crisis; legitimacy strain manageable
- Elite cohesion: Appears consolidated under Xi; no visible factional challenge
- Social unrest: Elevated (COVID protests, youth unemployment) but controlled
- Succession: Xi has removed term limits; uncertainty deferred but not eliminated

Distance to threshold is substantial. Crisis is not imminent under current conditions.

---

## Resolution Branches (Type 3 Component)

Per [[methodology/reference/type-3-calibration]], resolution probabilities start with entropy maximization (uniform distribution) unless structural asymmetries justify deviation.

### Critical Framing: What Counts as a Discontinuity

Per [[methodology/reference/causal-types]] (Common Mistakes section):

> **Leadership succession as discontinuity**: Smooth succession that maintains system continuity is NOT a discontinuity—it's normal political turnover. Only model succession as an event if the succession mechanism *fails* (factional conflict, institutional breakdown) or produces permanent/irreversible downstream effects.

This principle applies directly here. If a political crisis is resolved through normal elite bargaining that maintains CCP system continuity, **that's not a discontinuity** — it means the threshold wasn't actually crossed, or the event shouldn't have fired.

The event fires only when stress exceeds what normal CCP political processes can absorb. All resolutions must represent genuine discontinuities with permanent/irreversible effects.

### Proposed Resolutions (Revised)

| Resolution | Description | Why It's a Discontinuity |
|------------|-------------|--------------------------|
| **Regime Stabilization via Extraordinary Measures** | Crisis suppressed through means beyond normal CCP operations: martial law, mass purges exceeding Xi-era norms, permanent information lockdown, military deployment against civilians | Permanent shift in governance mode; regime survives but is fundamentally changed |
| **Regime Transformation** | Crisis forces genuine system change: liberalization, power-sharing, factional federation, or constitutional restructuring that alters CCP's monopoly on power | Irreversible system change even if non-violent; CCP continues but is no longer the same entity |
| **Regime Collapse** | CCP loses power entirely: state fragmentation, revolution, military takeover, or successor state(s) emerge | Obvious discontinuity |

### What Is NOT a Resolution (Threshold Not Crossed)

If the crisis is managed through:
- Elite bargaining that preserves existing power structures
- Leadership rotation through established succession mechanisms
- Concessions that don't fundamentally alter the system
- Temporary emergency measures that are later rescinded

...then **the event did not occur**. The pressure function should be calibrated such that these outcomes represent sub-threshold stress, not crisis resolution.

### Default Probabilities

**Entropy-maximized default**: 33% / 33% / 33%

### Structural Asymmetry Analysis

Is there justification for deviating from uniform?

| Factor | Direction | Strength |
|--------|-----------|----------|
| Activation energy: Transformation/collapse require sustained mobilization or elite defection; extraordinary stabilization requires only elite coordination + security force loyalty | Favors stabilization | Moderate |
| Historical pattern: Authoritarian regimes facing acute crisis more often double down than liberalize (Tiananmen 1989, Myanmar 2021) | Favors stabilization over transformation | Moderate |
| Institutional capacity: CCP has exceptional organizational resources; alternatives are weak | Favors stabilization | Moderate |
| Information environment: Modern surveillance/control technology advantages incumbents | Favors stabilization | Moderate |
| Nuclear arsenal: Military unlikely to allow state fragmentation with nuclear weapons at stake | Disfavors collapse | Weak |
| Legitimacy exhaustion: If crisis is severe enough to fire, regime may lack resources for transformation | Disfavors transformation | Weak |

**Assessment**: Structural factors favor regime stabilization (via extraordinary measures) over both transformation and collapse. Transformation is the least likely — it requires elite coordination toward reform under crisis conditions, which historically rarely succeeds (most regimes either crush dissent or fall).

**Proposed deviation**: 50% / 20% / 30%

| Resolution | Uniform | Proposed | Justification |
|------------|---------|----------|---------------|
| Stabilization (Extraordinary) | 33% | 50% | Structural advantages for repression; historical pattern (Tiananmen, Belarus 2020, etc.) |
| Regime Transformation | 33% | 20% | Requires elite coordination toward reform under pressure; historically rare |
| Regime Collapse | 33% | 30% | High uncertainty; structural disadvantages but cannot rule out |

This represents a weak-to-moderate deviation (~1.7:1 maximum ratio) within the 2:1 cap specified in Type 3 calibration guidance. The key ordering (Stabilization > Collapse > Transformation) is more defensible than the specific values.

---

## Cascade Relationships

### Triggered By

| Source Event | Probability Modifier | Duration | Mechanism |
|--------------|---------------------|----------|-----------|
| CHINESE_ECONOMIC_CRISIS | +2.0% | 5 years | Performance legitimacy failure; elite blame-shifting; mass unemployment |
| TAIWAN_CONFLICT (defeat) | +3.0% | 3 years | Nationalist legitimacy failure; military humiliation; elite recrimination |
| TAIWAN_CONFLICT (stalemate) | +1.0% | 3 years | Costly non-victory; economic damage; blame dynamics |
| SEVERE_PANDEMIC (China origin) | +1.0% | 2 years | Governance failure narrative; COVID precedent |

The Chinese Economic Crisis relationship is already specified in that event file. The Taiwan Conflict relationship requires careful calibration — defeat vs. stalemate vs. victory produce very different political dynamics.

### Triggers (Cascade Effects)

| Target Event | Effect | Duration | Mechanism |
|--------------|--------|----------|-----------|
| TAIWAN_CONFLICT | Complex; see below | — | Regime instability affects conflict calculus |
| GLOBAL_FINANCIAL_CRISIS | +1.5% | 2 years | Chinese political uncertainty triggers capital flight, market panic |
| DOLLAR_RESERVE_CRISIS | -0.5% | 3 years | Yuan alternative less viable; flight to dollar safety |
| NORTH_KOREA_CRISIS | +1.0% | 3 years | DPRK may see opportunity in Chinese distraction |
| PAKISTAN_STATE_FAILURE | +0.5% | 3 years | Reduced Chinese support capacity |

### Taiwan Conflict Interaction — Special Case

The relationship between Chinese political crisis and Taiwan conflict is bidirectional and complex:

**Crisis → Taiwan Conflict**:
- *Stabilization (Extraordinary) resolution*: May increase Taiwan risk (+0.8%) — regime uses nationalism to consolidate; hardened authoritarianism more likely to act
- *Regime Transformation resolution*: May decrease Taiwan risk (-0.5%) — liberalizing leadership less likely to pursue military adventurism
- *Regime Collapse resolution*: Highly uncertain — fragmented state unlikely to mount coordinated invasion; but transition chaos could produce accidental conflict or rogue military action

**Taiwan Conflict → Political Crisis**:
- Victory: Stabilizing (-1.0% to political crisis)
- Defeat/Humiliation: Highly destabilizing (+3.0%)
- Stalemate: Moderately destabilizing (+1.0%)

This requires careful specification to avoid circular logic.

---

## Factor Loadings (Preliminary)

| Factor | Loading | Rationale |
|--------|---------|-----------|
| F_CLIM | 0.10 | Climate stress affects rural stability, food security, regional development |
| F_FIN | 0.40 | Economic conditions are primary legitimacy input for performance-based regime |
| F_HLTH | 0.10 | Pandemic management affects governance perceptions |
| F_GPT | 0.35 | Great power tension affects nationalist legitimacy; foreign pressure dynamics |
| F_FOOD | 0.15 | Food security affects rural stability; historical sensitivity |
| F_TECH | 0.10 | Technology competition affects development narrative |
| F_EUR | 0.05 | Minimal direct impact |
| F_MENA | 0.0 | No direct linkage |
| F_SAS | 0.05 | Border tensions (India) affect stability |
| F_EAS | 0.30 | Regional dynamics affect legitimacy; Taiwan/Korea/Japan situations |
| F_SSA | 0.0 | No direct linkage |
| F_LAM | 0.0 | No direct linkage |

**Sum of squared loadings**: 0.16 + 0.1225 + 0.01 + 0.01 + 0.0225 + 0.01 + 0.0025 + 0.09 + 0.0025 = **0.43** 

Lower loading sum reflects that Chinese political crisis is more domestically-driven than externally-driven. International factors matter (F_FIN, F_GPT, F_EAS) but the core dynamics are internal elite politics and social cohesion.

---

## Relationship to Chinese Economic Crisis

### Avoiding Double-Counting

Both events affect China. The key distinction:

| Event | Primary Domain | Threshold | Resolution |
|-------|---------------|-----------|------------|
| Chinese Economic Crisis | Economic | Banking/property/growth collapse | Economic trajectory (hard landing vs. stagnation vs. reform) |
| Chinese Political Crisis | Political | Regime stability challenged beyond normal processes | Political trajectory (extraordinary stabilization vs. transformation vs. collapse) |

**Economic crisis does not automatically produce political crisis**. The economic event affects the `chn.regime_stability` variable, which feeds the political crisis pressure function. But:

- Regime may survive economic crisis through repression, nationalism, blame-shifting
- Political crisis may occur without economic crisis (succession dispute, military coup, mass movement)

### Impact Separation

**Economic Crisis impacts**: GDP, unemployment, trade, commodity prices, financial contagion
**Political Crisis impacts**: Governance, international alignment, territorial integrity, nuclear security

Some impacts are unique to political crisis:
- `chn.governance_effectiveness` — state capacity for policy implementation
- `chn.territorial_integrity` — risk of regional fragmentation
- `nuclear_security_risk` — command and control during instability
- `international_alignment` — regime change could fundamentally alter China's geopolitical posture

---

## Key Uncertainties

1. **Threshold calibration**: How much stress can CCP actually absorb? The apparent strength may mask fragility (or vice versa). Authoritarian regimes often appear stable until they suddenly aren't.

2. **Elite dynamics opacity**: We cannot observe factional alignments, military loyalty commitments, or succession planning. These are the core determinants of crisis resolution.

3. **Triggering event specification**: What specific events cross the threshold? Economic crisis is one pathway, but military defeat, succession dispute, or mass movement could also trigger. The pressure function may need multiple pathways.

4. **Resolution probability calibration**: Even with structural asymmetry analysis, we're operating in deep uncertainty. The 50/20/30 split is weakly justified; the ordering is more defensible than the specific values.

5. **Aftermath specification difficulty**: The "regime collapse" branch has enormous uncertainty — does China fragment? Is there civil war? What happens to nuclear weapons? This is genuinely uncharted territory.

6. **Time horizon effects**: Political crisis probability likely increases over time as Xi ages and succession questions intensify. The 2040-2050 period may have elevated risk regardless of economic conditions.

---

## Specification Approach

### Recommended Structure

1. **Event Classification**: Type 2/3 Hybrid (following Taiwan Conflict pattern)
2. **Pressure Function**: Type 2 threshold mechanics
3. **Resolution Sampling**: Type 3 with entropy-maximized probabilities (weak deviation)
4. **Aftermath Branches**: Three primary resolutions, each with 2-3 aftermath sub-branches

### Aftermath Branch Sketch

**Resolution: Stabilization via Extraordinary Measures (50%)**
- Branch: Consolidated hard authoritarianism (60%) — Permanent security state; North Korea-lite governance model; severe international isolation
- Branch: Unstable repression (40%) — Regime survives but faces ongoing resistance; periodic crackdowns; economic stagnation from control costs

**Resolution: Regime Transformation (20%)**
- Branch: Successful liberalization (40%) — Genuine power-sharing emerges; possible democratic transition over 10-20 years
- Branch: Unstable transition (60%) — Reform opens space for further instability; potential second crisis within 5 years

**Resolution: Regime Collapse (30%)**
- Branch: Revolutionary transition (35%) — New unified regime emerges; character uncertain (democratic, nationalist, military)
- Branch: State fragmentation (35%) — Regional power centers; Tibet/Xinjiang/Taiwan implications; civil conflict risk; nuclear security concerns
- Branch: Military takeover (30%) — PLA assumes direct control; praetorian state; uncertain civilian-military dynamics

### Estimated Effort

Full Level 1 specification: 1.5-2 hours following this scoping document

---

## Decision Points for Review

Before proceeding to full specification, please confirm:

1. **~~Resolution structure~~** ✅ RESOLVED: Three resolutions that are all genuine discontinuities: Stabilization via Extraordinary Measures / Regime Transformation / Regime Collapse. "Managed transition" that maintains system continuity is sub-threshold, not a resolution.

2. **Event definition**: Is "acute political instability that exceeds normal CCP political processes" the right threshold? The key is that the threshold must be high enough that crossing it necessarily produces permanent change.

3. **Probability deviation**: Is the 50/20/30 deviation from uniform justified? The ordering (Stabilization > Collapse > Transformation) seems defensible; the specific values are less certain.

4. **Scope of collapse/transformation aftermath**: How much detail should we invest in these branches given their speculative nature? State fragmentation and nuclear security concerns warrant serious treatment despite uncertainty.

5. **Taiwan Conflict interaction**: Should we specify the bidirectional relationship now, or defer to a separate cross-event relationship document?

---

*Related documents*: [[events/financial/chinese-economic-crisis]], [[events/geopolitical/taiwan-conflict]], [[methodology/reference/type-3-calibration]], [[methodology/reference/causal-types]]

*Task reference*: 2.1.13 in [[methodology/project/tasks]]