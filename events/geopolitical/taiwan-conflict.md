---
title: taiwan-conflict
type: note
permalink: events/geopolitical/taiwan-conflict
tags:
- event
- type-3
- geopolitical
- east-asia
- taiwan
- china
- level-1
---

# Taiwan Conflict

**Type 3 (Contingent) Event** — Military conflict or great power settlement following acute cross-strait crisis.

---

## Event Classification

| Attribute | Value |
|-----------|-------|
| **ID** | `TAIWAN_CONFLICT` |
| **Scale** | Global |
| **Domain** | Geopolitical |
| **Causal Type** | Type 3: Contingent |
| **Onset Speed** | Sudden (<1yr) |
| **Reversibility** | Partial to Irreversible (aftermath-dependent) |

## Description

Military conflict between PRC and Taiwan, or US-brokered great power settlement fundamentally altering cross-strait relations. Distinguished from baseline tensions and sub-threshold crises by either (a) actual military operations or (b) binding agreements backed by great power guarantees that materially change Taiwan's status. This is the discontinuity; crises that de-escalate without combat or formal settlement are non-events.

Bilateral Taiwan-PRC negotiation is not modeled as a plausible path — the preference sets don't overlap. Settlement requires US involvement as broker and guarantor, fundamentally changing the negotiating dynamic.

---

## Causal Type Specification

### Type 3 (Contingent) Event

This event has Type 3 structure: preconditions create crisis windows, and actor decisions determine whether discontinuity occurs. The probability decomposition is:

- **P(crisis window)**: ~3% annually — acute crisis develops
- **P(discontinuity | window)**: ~65% — military conflict or great power settlement occurs
- **P(event)**: ~2% annually — the discontinuity probability

The ~35% of crisis windows that de-escalate without combat or formal agreement are *non-events* — they don't appear in the simulation as discontinuities.

**Window Preconditions**:

Observable conditions from state model that indicate elevated window probability:
- Elevated F_GPT (Great Power Tension factor) sustained for 2+ years
- Elevated F_EAS (East Asian factor) indicating regional instability
- `chn.military_spending_deviation` elevated (unusual buildup)
- `usa.external_conflict_involvement` < 3 (capacity available)

**Historical basis for window probability (~3%)**:

Acute crises reaching threshold where military action or major diplomatic shift became imminent:
- 1954-55 First Taiwan Strait Crisis (military engagement)
- 1958 Second Taiwan Strait Crisis (military engagement)
- 1995-96 Third Taiwan Strait Crisis (military mobilization, de-escalated)
- 2022 Pelosi visit tensions (did not reach acute phase)

Pattern: ~3-4 acute crises per century when baseline tensions elevated. Current period has elevated baseline due to PRC military modernization, US strategic competition, and semiconductor stakes.

**Historical basis for discontinuity probability given window (~65%)**:

Of the 3 acute crises since 1954, 2 involved actual military operations (1954-55, 1958). The 1995-96 crisis de-escalated without combat — a non-event in our framework. This suggests roughly two-thirds of acute crises produce discontinuous outcomes.

---

## Probability

| Metric | Value |
|--------|-------|
| **Annual probability** | ~2.0% |
| **Low bound** | 1.0% |
| **High bound** | 3.5% |
| **Confidence** | Medium |
| **25-year cumulative** | ~40% (at least one discontinuity) |

### Derivation

1. **Window probability**: 3% annually (2-5% range)
2. **Discontinuity given window**: 65% (50-80% range)
3. **Combined**: 3% × 65% = 1.95%, rounded to ~2%

### Comparative Ranking

| Event | Annual Probability | Comparison |
|-------|-------------------|------------|
| Taiwan Conflict | ~2.0% | — |
| India-Pakistan Military Conflict | ~0.9% | Lower — more frequent crises but lower conflict-given-crisis |
| Pakistan State Failure | ~1.5% | Similar magnitude |
| Chinese Economic Crisis | ~2.0% | Similar magnitude |
| Global Financial Crisis | ~3.0% | Higher — more frequent, less actor-dependent |

### Case Against This Specification

Per [[methodology/03-critical-review]] Q4:

**1. Probability may be too high**

Nuclear deterrence and economic interdependence make Taiwan conflict substantially less likely than historical crises suggest. The 1954-58 crises occurred before PRC had nuclear weapons and before deep economic integration. Modern conflict would be catastrophic for both sides in ways that didn't apply historically.

*Counter*: PRC has invested heavily in military capabilities specifically designed for Taiwan scenarios. This investment is not consistent with deterrence-only posture. Additionally, nationalist pressures and "century of humiliation" narrative create political incentives that may override economic rationality.

**2. Great power settlement may be implausible**

Even at 35%, the weight on settlement may be too high. The scenarios require US willingness to reduce its position, PRC trust in US commitments, and Taiwan acquiescence to constrained autonomy. Each of these faces severe barriers. The US has no domestic constituency for accommodation; PRC has no reason to trust US commitments given historical record; Taiwan's democracy would likely reject any framework imposed by great powers.

*Counter*: Crisis dynamics differ from peacetime analysis. Faced with imminent catastrophic conflict, preferences may shift in ways current politics don't reveal. Historical precedents (Austria 1955, Korea 1953) show great powers can impose settlements when the alternative is unacceptable.

**3. Non-event probability may be too low**

35% non-event probability may understate crisis management capacity. The 1995-96 crisis de-escalated despite military mobilization. International pressure, economic stakes, and nuclear risks all push toward de-escalation.

*Counter*: If this is true, it argues for lower window probability rather than higher non-event share. The window is meant to capture crises where discontinuity is genuinely imminent.

**4. Type 3 structure may impose false precision**

The decomposition into window probability × resolution probability may give false confidence. In reality, these are deeply entangled—the factors that make a window open also affect resolution probability. The structural separation may not carve nature at the joints.

*Counter*: The decomposition is a modeling choice, not a claim about underlying structure. It helps organize reasoning even if imperfect.

### Window Probability Evolution

For Type 3 events, the relevant evolution question is how window probability changes over time, not pressure accumulation.

| Period | Estimated Window Probability | Rationale |
|--------|------------------------------|-----------|
| 2025-2030 | ~3%/year | Current elevated baseline; PRC military modernization continuing |
| 2030-2035 | ~4%/year | PRC likely reaches peak military readiness relative to US |
| 2035-2045 | ~3-4%/year | Depends on resolution of current trajectory; could stabilize or escalate |
| 2045-2075 | Uncertain | If no prior resolution, either accommodation reached or permanent tension |

### Key Uncertainties

- **PRC military readiness trajectory**: Rapid capability improvements may shift window toward action
- **US commitment credibility**: Strategic ambiguity creates uncertainty about response
- **Semiconductor stakes**: TSMC's value may increase or decrease conflict likelihood
- **Domestic politics**: Nationalist pressures on both sides affect crisis behavior

---

## Factor Loadings

*Loadings scaled per [[methodology/reference/variance-allocation]] to achieve Type 3 target (ΛΩΛᵀ)ᵢᵢ = 0.45*

| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_EAS** | 0.38 | Regional instability directly relevant |
| **F_GPT** | 0.33 | Great power tension is primary driver |
| **F_FIN** | 0.09 | Economic stress may affect calculus but secondary |
| **F_TECH** | 0.07 | Semiconductor competition adds stakes |
| F_CLIM | 0.00 | No direct pathway |
| F_HLTH | 0.00 | No direct pathway |
| F_FOOD | 0.00 | No direct pathway |
| F_EUR | 0.00 | No direct pathway |
| F_MENA | 0.00 | No direct pathway |
| F_SAS | 0.00 | No direct pathway |
| F_SSA | 0.00 | No direct pathway |
| F_LAM | 0.00 | No direct pathway |

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.45 (Type 3 target); scale factor = 0.47 from original loadings

---

## Resolutions

Once a crisis window opens *and* a discontinuity occurs (65% of windows), one of two resolutions:

### Resolution 1: Military Conflict

**Probability given discontinuity**: 65%

PRC initiates military action against Taiwan. Ranges from blockade to limited strikes to full invasion.

### Resolution 2: Great Power Settlement

**Probability given discontinuity**: 35%

US brokers binding settlement between PRC and Taiwan. Agreement backed by great power guarantees, materially changing Taiwan's status, security arrangements, or governance framework.

**Resolution probability rationale**:

Military conflict faces barriers (nuclear risk, economic costs, military uncertainty) but requires only one actor (PRC) to decide to act.

Settlement requires three actors to agree on terms none would accept under normal circumstances—US willingness to reduce position, PRC trust in US commitments, Taiwan acquiescence. This structural asymmetry justifies weighting military conflict higher.

---

## Aftermath Branches

### Military Conflict Aftermath

**Branch 1: Limited Conflict (55%)**

Blockade or limited strikes without amphibious invasion. Semiconductor supply severely disrupted for 1-3 years. No direct US-China military engagement.

**Branch 2: Full Invasion (30%)**

Amphibious assault and occupation attempt. Catastrophic semiconductor disruption. High probability of US military involvement. Prolonged conflict likely.

**Branch 3: Nuclear Escalation (15%)**

Conflict escalates to nuclear weapons use. Civilizational-scale consequences.

### Great Power Settlement Aftermath

**Branch 1: Stable Framework (40%)**

Durable settlement backed by credible guarantees. Genuine tension reduction.

**Branch 2: Unstable Framework (60%)**

Agreement reached under crisis pressure but with structural weaknesses. Creates period of formal framework with elevated collapse risk.

---

## Impact Vector

### Global Impacts (Limited Conflict Branch)

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `semiconductor_supply` | ↓ | -70% ± 15% | immediate | decaying: half_life=2yr |
| `global_trade_volume` | ↓ | -15% ± 5% | immediate | decaying: half_life=3yr |
| `global_credit_spread` | ↑ | +200 ± 80 bps | immediate | decaying: half_life=1yr |
| `active_major_conflicts` | ↑ | +1 | immediate | until resolution |

### Taiwan Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `twn.gdp_real` | ↓ | -40% ± 15% | immediate | decaying: half_life=5yr |
| `twn.external_conflict_involvement` | ↑ | to 4 (major war) | immediate | until resolution |

### China Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `chn.gdp_real` | ↓ | -15% ± 8% | immediate | decaying: half_life=3yr |
| `chn.sanctions_level` | ↑ | +50 ± 20 | immediate | permanent until policy change |
| `chn.external_conflict_involvement` | ↑ | to 3-4 | immediate | until resolution |

### United States Impacts

| Variable | Direction | Magnitude | Onset | Durability |
|----------|-----------|-----------|-------|------------|
| `usa.gdp_real` | ↓ | -8% ± 4% | immediate | decaying: half_life=2yr |

*Full Invasion multiplies impacts by ~1.5×; Nuclear Escalation multiplies by ~3×*

---

## Cascade Effects

### State → Probability Cascades

| Target Event | Probability Change | Duration | Mechanism |
|--------------|-------------------|----------|-----------|
| KOREAN_PENINSULA_CRISIS | +1.5%/year | 3 years | North Korea may see opportunity |
| CHINESE_ECONOMIC_CRISIS | +2.0%/year | 5 years | Sanctions, trade disruption, confidence |
| CHINESE_POLITICAL_CRISIS | +1.0%/year | 5 years | If military failure, regime stress |

### Triggered By

| Source Event | Effect on This Event | Mechanism |
|--------------|---------------------|-----------|
| CHINESE_ECONOMIC_CRISIS | +0.5%/year | Nationalist distraction; domestic pressure |
| CHINESE_POLITICAL_CRISIS | +1.0%/year | Leadership instability may trigger action |
| US_CONSTITUTIONAL_CRISIS | +0.5%/year | US distraction may create perceived window |

---

## Transmission Channels

### Semiconductor Channel

Taiwan produces ~90% of advanced semiconductors. Any conflict scenario severely disrupts global technology supply chains. `semiconductor_supply` drops dramatically, affecting every technology-dependent economy.

### Trade Channel

Cross-strait conflict disrupts major shipping lanes. `global_trade_volume` impacts depend on conflict intensity and duration.

### Financial Channel

Conflict triggers capital flight, currency volatility, and risk repricing. `global_credit_spread` widens sharply.

---

## Research Status

| Field | Value |
|-------|-------|
| **Tier** | Level 1 |
| **Last updated** | 2025-12-30 |
| **Critical review** | Complete (2025-12-30) |
| **Upgrade candidate** | Yes |
| **Upgrade rationale** | Semiconductor impact modeling; great power settlement plausibility; nuclear escalation pathways |

## Open Questions

1. **Great power settlement precedent**: How do Austria 1955, Korea 1953, Camp David 1978 inform plausibility?
2. **US domestic constraints**: What are realistic limits on accommodation given domestic politics?
3. **PRC military readiness**: What is realistic timeline for peak capability relative to US?
4. **TSMC destruction calculus**: Would PRC destroy or try to capture facilities?
5. **Nuclear escalation pathways**: Under what scenarios does nuclear use become plausible?

---

## Changelog

| Date | Change | Rationale |
|------|--------|-----------|
| 2025-12-22 | Initial Level 1 specification | Type 3 worked example |
| 2025-12-22 | Revised resolution structure | Removed status quo as resolution; added great power settlement frame |
| 2025-12-30 | Variance allocation: scaled loadings | Task 3.11 - Factor-explained variance reduced to Type 3 target (0.45) per variance allocation framework |
| 2025-12-30 | Critical review complete | Task 2.4.3 - Fixed event/variable references; added formal Case Against and Window Evolution sections |

---

*See [[methodology/reference/type-3-calibration]] for methodology | [[events/geopolitical/india-pakistan-military-conflict]] for comparable Type 3 specification*