---
permalink: methodology/project/development-roadmap
---

# Geopolitical Monte Carlo Simulation: Development Roadmap

**Document Version:** 1.0  
**Date:** December 2025  
**Status:** Planning document

---

## Overview

This roadmap outlines a phased approach to building a Monte Carlo simulation of geopolitical trajectories through 2075. The approach prioritizes working software over comprehensive specification, using iterative expansion guided by sensitivity analysis.

### Design Principles

1. **Start minimal, expand based on evidence.** Build a working prototype with a subset of entities and variables, then add complexity where it matters.

2. **Events before dynamics.** The discontinuity event catalog is the intellectual core. Get this right first; baseline dynamics can be refined later.

3. **Let sensitivity analysis guide investment.** Don't parameterize everything upfront. Run the prototype, see what drives outcomes, then invest in refining what matters.

4. **Working code beats perfect specification.** A simulation that runs and produces distributions you can examine is more valuable than a comprehensive specification you can't execute.

---

## Phase 1: Event Catalog

### Objective
Define 40-60 discontinuity events with probabilities, factor loadings, and impact vectors.

### Deliverables
- Complete event catalog document (JSON or YAML format)
- Events organized by category:
  - Climate/planetary tipping points (5-8 events)
  - Great power conflict scenarios (5-8 events)
  - Regional conflicts and state failures (10-15 events)
  - Economic/financial crises (5-8 events)
  - Pandemic and health events (3-5 events)
  - Technology discontinuities (3-5 events)
  - Political discontinuities in major powers (5-8 events)

### Per-Event Specification
For each event, define:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier |
| `name` | Human-readable name |
| `description` | What this event represents |
| `probability` | Annual probability (point estimate + range) |
| `factor_loadings` | Loadings on 12 latent factors (from methodology doc) |
| `impacts` | Which state variables are affected, by how much |
| `duration` | How long impacts persist |
| `reversibility` | Can the system recover? |
| `preconditions` | State conditions that increase/decrease probability |
| `cascade_triggers` | Other events this makes more likely |

### Priority Events (First 20)
1. AMOC significant weakening
2. Amazon tipping point
3. Taiwan Strait conflict
4. US-China trade war escalation
5. Global financial crisis (2008-level)
6. Severe pandemic (COVID-level or worse)
7. Russian state failure
8. Chinese economic crisis
9. Chinese political crisis
10. Pakistan state failure
11. Egypt state failure
12. Saudi regime instability
13. Iran regime change
14. Turkey political crisis
15. European Union fragmentation
16. US constitutional crisis
17. India-Pakistan military conflict
18. Korean peninsula crisis
19. Dollar reserve currency crisis
20. Oil supply shock

### Success Criteria
- 40+ events fully specified
- Factor loadings sum-of-squares validated (≤1 per event)
- Impact vectors map to state variables from specification doc
- Internal consistency reviewed (no contradictory assumptions)

### Estimated Effort
2-3 focused sessions

---

## Phase 2: Prototype Implementation

### Objective
Build a minimal working simulation that produces output distributions.

### Scope Constraints

#### Countries (15 core)
| Country | Rationale |
|---------|-----------|
| United States | Hegemon, reserve currency |
| China | Primary rival, demographic crisis |
| Russia | Nuclear power, energy, Ukraine |
| India | Demographic giant, rising power |
| Germany | EU anchor |
| United Kingdom | Nuclear, financial center |
| Japan | Demographic pioneer, US ally |
| Brazil | BRICS, regional power |
| Saudi Arabia | Energy, de-dollarization |
| Pakistan | Nuclear, fragile, climate-vulnerable |
| Nigeria | African demographic giant |
| Taiwan | Semiconductor chokepoint |
| Iran | Nuclear threshold, sanctions |
| Turkey | Regional power, NATO member |
| Indonesia | SE Asian anchor, BRICS |

#### Variables per Country (~18)
| Category | Variables |
|----------|-----------|
| Demographics (4) | `pop_total`, `pop_working_age`, `tfr`, `net_migration_rate` |
| Economics (6) | `gdp_real`, `gdp_per_capita`, `gdp_growth`, `debt_public`, `inflation_rate`, `reserves_foreign` |
| Political (4) | `regime_stability`, `institutional_quality`, `internal_conflict_intensity`, `regime_type` |
| Climate (2) | `water_stress`, `food_import_dependence` |
| Strategic (2) | `sanctions_level`, `external_conflict_involvement` |

#### Global Variables (~22)
| Category | Variables |
|----------|-----------|
| Climate (4) | `global_temp_anomaly`, `amoc_strength`, `amazon_forest_cover`, `sea_level_global` |
| Commodities (6) | `oil_brent`, `gold_price`, `wheat_price`, `food_stocks_grains`, `fertilizer_price_index`, `gas_europe_ttf` |
| Financial (6) | `usd_reserve_share`, `us_10yr_yield`, `global_credit_spread`, `fed_funds_rate`, `cny_reserve_share`, `gold_reserve_share` |
| Trade (2) | `global_trade_volume`, `semiconductor_supply` |
| Geopolitical (4) | `us_china_tension`, `active_major_conflicts`, `nuclear_stability`, `brics_integration` |

### Technical Architecture

```
prototype/
├── data/
│   ├── events.json           # Event catalog from Phase 1
│   ├── factor_loadings.csv   # Factor loading matrix
│   ├── initial_conditions.json # 2025 baseline values
│   └── parameters.json       # Dynamics parameters
│
├── core/
│   ├── state.py              # State vector management
│   ├── events.py             # Event sampling with factor copula
│   ├── dynamics.py           # Baseline evolution between events
│   ├── impacts.py            # Event → state variable transmission
│   └── simulation.py         # Main simulation loop
│
├── analysis/
│   ├── distributions.py      # Output distribution analysis
│   ├── scenarios.py          # Scenario frequency counts
│   └── sensitivity.py        # Sensitivity analysis
│
├── visualization/
│   └── plots.py              # Distribution and trajectory plots
│
└── notebooks/
    ├── prototype_run.ipynb   # Run and examine simulations
    └── sensitivity.ipynb     # Sensitivity analysis
```

### Dynamics (Simplified for Prototype)

| Variable Type | Dynamics Model |
|---------------|----------------|
| Population | Deterministic cohort aging + fertility/mortality rates |
| GDP | Trend growth + mean-reverting shocks |
| Debt | Accumulates based on deficit (GDP growth vs. spending) |
| Inflation | Mean-reverting to target + supply shocks |
| Stability indices | Slow decay when shocked, gradual recovery |
| Global climate | Deterministic trend + small noise |
| Commodities | Mean-reverting with event shocks |
| Reserve shares | Slow trend + event-driven shifts |

### Success Criteria
- Simulation runs 10,000 iterations in <60 seconds
- Produces sensible output distributions (no degenerate results)
- Events fire at approximately specified frequencies
- Correlation structure produces visible clustering
- Can examine terminal state for any country in any run

### Estimated Effort
2-3 implementation sessions + 1 debugging/validation session

---

## Phase 3: Sensitivity Analysis

### Objective
Discover which events, variables, and parameters drive outcomes—especially tail outcomes.

### Analyses to Run

#### 3.1 Event Contribution Analysis
For runs in the worst 5% of outcomes (by various metrics):
- Which events occurred most frequently?
- Which event combinations appeared?
- Which events are necessary vs. sufficient for tail outcomes?

#### 3.2 Parameter Sensitivity
- Run with probability bounds (low vs. high for each event)
- Run with impact magnitude bounds
- Run with/without correlation structure (independent vs. correlated sampling)
- Identify which parameters have largest effect on outcome distributions

#### 3.3 Factor Analysis
- Which latent factors (F_CLIM, F_FIN, F_GPT, etc.) drive worst outcomes?
- How much does factor correlation contribute to tail risk vs. independent sampling?

#### 3.4 Factor Correlation Matrix Validation
- **Proxy variable analysis**: Compute historical correlations between observable proxies for each factor (e.g., temperature anomaly for F_CLIM, FAO Food Price Index for F_FOOD, VIX for F_FIN). Compare to specified factor correlations—are we in the right ballpark?
- **Historical cluster analysis**: Examine historical "bad years" (2008-2009, 2010-2011, 2020) and check whether our correlation structure would predict observed factor clustering.
- **Implied event correlation review**: With the full event catalog, compute Σ_events = ΛΩΛ' + Ψ and verify implied event correlations are sensible. Check for double-counting inflation from events that load on correlated factors.

See [[methodology/reference/factor-correlation-matrix]] for the current matrix and known limitations.

#### 3.5 Country/Variable Importance
- Which country trajectories are most predictive of global outcomes?
- Which variables explain most variance in outcomes?
- Where is model under-specified (outcomes depend on unmodeled dynamics)?

### Outputs
- Ranked list of events by tail risk contribution
- Ranked list of parameters by sensitivity
- Recommendations for Phase 4 expansion priorities
- Identified gaps in model structure

### Success Criteria
- Clear understanding of what drives tail outcomes
- Prioritized list for refinement
- Confidence in what model can/cannot tell us

### Estimated Effort
1-2 analysis sessions

---

## Phase 4: Iterative Expansion

### Objective
Expand model based on Phase 3 findings.

### Potential Expansions (Priority TBD by Phase 3)

#### Additional Countries
Based on which regional dynamics matter:
- If MENA dynamics drive outcomes → add Egypt, Israel, UAE
- If European dynamics drive outcomes → add France, Italy, Poland
- If African dynamics drive outcomes → add Ethiopia, South Africa, Kenya
- If Asian dynamics drive outcomes → add South Korea, Vietnam, Bangladesh

#### Additional Variables
Based on which mechanisms matter:
- If remittances matter → add bilateral remittance flows
- If trade matters → add trade exposure matrix
- If migration matters → add displacement tracking
- If financial contagion matters → add cross-border exposures

#### Refined Dynamics
Based on which parameters are sensitive:
- If GDP growth rates matter → improve growth model
- If stability transitions matter → add regime-switching dynamics
- If commodity prices matter → improve mean-reversion parameters
- If climate-economy link matters → improve transmission functions

#### Additional Events
Based on which scenarios are missing:
- If regional conflicts matter → expand regional event coverage
- If compounding events matter → add cascade triggers
- If slow-burn crises matter → add gradual deterioration events

### Process
1. Review Phase 3 findings
2. Prioritize expansions by expected impact on output quality
3. Implement incrementally, validating after each addition
4. Re-run sensitivity analysis to confirm improvements

### Success Criteria
- Model complexity increased only where it improves output quality
- No "gold plating" of insensitive components
- Documented rationale for each expansion decision

### Estimated Effort
3-5 sessions (iterative)

---

## Phase 5: Calibration and Validation

### Objective
Ground the model in empirical data and validate against historical patterns.

### 5.1 Initial Conditions
- Gather 2025 baseline values for all state variables from authoritative sources
- Document sources and data quality for each variable
- Identify gaps requiring estimation

### 5.2 Parameter Calibration
- Estimate dynamics parameters from historical data where possible
- GDP growth trends from IMF projections
- Demographic rates from UN Population Division
- Commodity price parameters from historical volatility
- Stability indices from historical variation

### 5.3 Historical Backtesting
Limited backtesting possible for:
- Frequency of events (do historical base rates match our estimates?)
- Correlation patterns (do crises cluster as modeled?)
- Impact magnitudes (do historical shocks match our impact vectors?)

#### Factor Correlation Validation
If Phase 3 proxy analysis reveals significant discrepancies between specified factor correlations and historical proxy correlations:
- Revise correlation estimates for high-sensitivity correlations
- Document rationale for any estimates that deliberately diverge from historical patterns (e.g., if climate-food linkage is expected to strengthen)
- Re-validate positive semi-definiteness after revisions

### 5.4 Expert Review
- Review output distributions with domain experts
- Are tail scenarios plausible? Are we missing important scenarios?
- Do country trajectories match expert intuition?
- Calibrate where expert judgment diverges from model output

### 5.5 Documentation
- Complete parameter documentation with sources
- Uncertainty quantification for each parameter
- Model limitations and appropriate use cases
- User guide for running and interpreting simulations

### Success Criteria
- All initial conditions sourced and documented
- Parameters calibrated or justified
- Expert review completed with revisions incorporated
- Model limitations clearly documented

### Estimated Effort
2-3 sessions

---

## Phase 6: Production and Application

### Objective
Use the model for actual planning purposes.

### Applications

#### 6.1 Scenario Analysis
- Generate probability distributions for planning-relevant questions
- "What is the distribution of US living standards in 2050?"
- "How often do we see dollar displacement below 40% reserve share?"
- "What is the probability of >100M displaced persons by 2060?"

#### 6.2 Stress Testing
- Examine model behavior under specific scenarios
- "What happens if AMOC collapses in the 2030s?"
- "What happens if Taiwan conflict occurs?"
- "What if oil demand collapses by 2035?"

#### 6.3 Sensitivity to Assumptions
- How much do outcomes depend on our probability estimates?
- Which uncertainties matter most for planning decisions?
- Where should we invest in better forecasting?

#### 6.4 Regular Updates
- Annual review of event catalog (probabilities, new events)
- Update initial conditions as time passes
- Incorporate new information (climate science, geopolitical developments)

### Deliverables
- Summary reports for key questions
- Interactive exploration capability
- Documentation for decision-makers

---

## Timeline Summary

| Phase | Focus | Sessions | Dependencies |
|-------|-------|----------|--------------|
| **Phase 1** | Event Catalog | 2-3 | Methodology doc, state spec |
| **Phase 2** | Prototype Implementation | 3-4 | Phase 1 |
| **Phase 3** | Sensitivity Analysis | 1-2 | Phase 2 |
| **Phase 4** | Iterative Expansion | 3-5 | Phase 3 |
| **Phase 5** | Calibration & Validation | 2-3 | Phase 4 |
| **Phase 6** | Production Use | Ongoing | Phase 5 |

**Total estimated effort: 12-18 sessions to production-ready model**

---

## Key Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| **Scope creep** | Strict Phase 2 constraints; expand only based on Phase 3 evidence |
| **Parameter uncertainty overwhelming signal** | Sensitivity analysis identifies what matters; accept uncertainty elsewhere |
| **Correlation structure invalid** | Factor model guarantees valid matrix; validate implied correlations |
| **Historical data insufficient** | Acknowledge this is judgment under uncertainty, not actuarial science |
| **Model misuse** | Clear documentation of limitations; outputs are distributions, not predictions |

---

## Next Session: Phase 1

### Preparation
The project files contain:
- `geopolitical-monte-carlo-methodology.md` — Factor structure and event sampling approach
- `geopolitical-simulation-state-specification.md` — State variables and entity list
- `collapse-patterns-predictive-framework.md` — Historical collapse patterns
- `21st_century_assessment.md` — Regional trajectory assessments
- `brics-dedollarization-us-impact-research-2025.md` — Financial system analysis

### Session Goal
Draft the first 20-25 events with complete specifications:
- Probabilities grounded in historical base rates and structural reasoning
- Factor loadings consistent with methodology doc's 12-factor structure
- Impact vectors mapping to state variables
- Internal consistency across events

### Starting Point
Begin with highest-confidence events:
1. Climate tipping points (AMOC, Amazon) — scientific literature provides probability ranges
2. Pandemic recurrence — historical base rates exist
3. Financial crisis — historical frequency known
4. State failures in highest-risk countries — framework document provides estimates

Then move to more speculative events (great power conflict, dollar crisis, technology disruptions).

---

## Document Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial roadmap |

---

*This roadmap prioritizes working software over comprehensive specification. The goal is to produce useful output distributions within a reasonable effort budget, then refine iteratively based on what we learn from running the model.*