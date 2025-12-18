---
title: f-food
type: note
permalink: factors/f-food
tags:
- factor
- food
- agriculture
- correlation-structure
---

# F_FOOD: Food System Stress Factor

## Overview

The Food System Stress factor represents pressure on global food production and distribution—supply shocks, price spikes, stock drawdowns, and distribution failures. When F_FOOD has a high realization, food crises and downstream instability events become more likely.

## What This Factor Captures

- Global grain production shortfalls
- Stocks-to-use ratio drawdowns
- Fertilizer and input availability
- Trade disruptions (export bans, shipping)
- Food price spikes
- Distribution system failures

## Events That Load Heavily on F_FOOD

| Event | Loading | Rationale |
|-------|---------|-----------|
| Global Food Price Spike | 0.85 | This IS the factor manifesting |
| Sahel Catastrophe | 0.60 | Food insecurity is primary driver |
| Egypt State Failure | 0.50 | Heavy import dependence (50%+ wheat) |
| [[pakistan-state-failure]] | 0.42 | Agricultural disruption, import needs |
| North Korea Famine | 0.55 | Food system collapse |
| [[amoc-weakening]] | 0.20 | Affects European agriculture, global supply |

## Correlation Implications

Food system stress amplifies instability in import-dependent regions:
- MENA (Egypt, Gulf states, North Africa)
- South Asia (Bangladesh, Pakistan)
- Sub-Saharan Africa (Sahel, East Africa)

High F_FOOD often coincides with high F_CLIM (climate drives crop failures) but can also occur independently (war, trade disruption, policy failure).

## Relationship to Other Factors

- **F_CLIM**: Strong positive relationship. Climate stress drives crop failures.
- **F_SSA, F_SAS, F_MENA**: Food stress amplifies regional instability.
- **F_FIN**: Moderate relationship. Food prices affect inflation, stability.
- **F_GPT**: Moderate relationship. Conflicts disrupt production (Ukraine) and trade.

## Cross-Cutting Nature

F_FOOD is listed as a "cross-cutting factor" because it loads on climate events (as effect) and amplifies regional instability events (as cause). It transmits climate stress to political instability.

## Calibration Notes

The 2022-2023 period (Ukraine war, fertilizer disruption) provided recent calibration of food system stress dynamics.

## References

- [[methodology-factor-model]]
- [[f-clim]] (climate-food nexus)
- collapse-patterns-predictive-framework.md (famine case studies)
