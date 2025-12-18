---
title: f-fin
type: note
permalink: factors/f-fin
tags:
- factor
- financial
- correlation-structure
---

# F_FIN: Financial Fragility Factor

## Overview

The Financial Fragility factor represents global financial system stress—credit conditions, liquidity, risk appetite, and systemic vulnerability. When F_FIN has a high realization, financial crises, sovereign defaults, and currency crises become more likely across multiple countries simultaneously.

## What This Factor Captures

- Global credit conditions and spreads
- Banking system stress indicators
- Sovereign debt sustainability concerns
- Currency market volatility
- Capital flow reversals
- Risk appetite (VIX-like dynamics)
- Contagion potential

## Events That Load Heavily on F_FIN

Events with loading ≥ 0.3:

| Event | Loading | Rationale |
|-------|---------|-----------|
| Global Financial Crisis | 0.90 | This IS the factor manifesting |
| Dollar Reserve Crisis | 0.70 | Financial system restructuring |
| Eurozone Sovereign Crisis | 0.65 | Debt sustainability, contagion |
| Emerging Market Contagion | 0.75 | Correlated capital flight |
| Turkey Political Crisis | 0.40 | Currency/debt vulnerability |
| [[pakistan-state-failure]] | 0.29 | IMF dependency, fiscal fragility |
| Chinese Economic Crisis | 0.50 | Property, debt overhang |

## Correlation Implications

High F_FIN realizations produce clusters of:
- Sovereign defaults across vulnerable countries
- Currency crises in weak-reserves countries
- Banking sector stress
- Risk-off capital flows from EM to safe havens

## Relationship to Other Factors

- **F_EUR, F_LAM**: Strong relationship. European and Latin American crises often have financial triggers.
- **F_CLIM**: Weak relationship. Financial dynamics largely independent of climate.
- **F_GPT**: Moderate relationship. Great power tensions can trigger sanctions and financial fragmentation.

## Calibration Notes

Financial stress is highly correlated across countries during crisis periods. The factor model captures this through shared F_FIN loading—when F_FIN spikes, all financially vulnerable countries see elevated crisis probability simultaneously.

This is why independent sampling dramatically underestimates tail risk: financial crises cluster.

## References

- [[methodology-factor-model]]
- brics-dedollarization-us-impact-research-2025.md
- collapse-patterns-predictive-framework.md Section 3 (Economic Collapse Pathway)
