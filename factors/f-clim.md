---
title: f-clim
type: note
permalink: factors/f-clim
tags:
- factor
- climate
- correlation-structure
---

# F_CLIM: Climate Stress Factor

## Overview

The Climate Stress factor represents global climate pressure—the degree to which climate-related stresses are elevated in a given simulation year. When F_CLIM has a high realization, all climate-sensitive events become more likely simultaneously.

## What This Factor Captures

- Global temperature anomalies and acceleration
- Extreme weather frequency and intensity
- Ice sheet and glacier dynamics
- Drought and precipitation extremes
- Heat wave severity and duration
- Ecosystem stress signals

## Events That Load Heavily on F_CLIM

Events with loading ≥ 0.4:

| Event | Loading | Rationale |
|-------|---------|-----------|
| [[amoc-weakening]] | 0.85 | Direct climate system tipping point |
| Amazon Tipping Point | 0.80 | Climate + deforestation interaction |
| Permafrost Methane Release | 0.75 | Temperature-driven threshold |
| [[pakistan-state-failure]] | 0.38 | Indus glacier melt, agricultural stress |
| Egypt State Failure | 0.35 | Nile flows, agricultural climate |
| Sahel Catastrophe | 0.60 | Desertification, rainfall failure |

## Correlation Implications

High F_CLIM realizations tend to produce clusters of:
- Climate tipping point events
- Agricultural crises in climate-vulnerable regions
- Water stress events
- Climate-driven state fragility

## Relationship to Other Factors

- **F_FOOD**: Strong positive relationship. Climate stress drives food system stress.
- **F_SSA, F_SAS, F_MENA**: Climate stress amplifies regional instability in vulnerable areas.
- **F_FIN, F_GPT**: Weak relationship. Climate operates somewhat independently of financial and geopolitical dynamics.

## Calibration Notes

F_CLIM is modeled as a standard normal variable in each simulation year. The factor loading determines how much each event's probability responds to climate conditions.

A +2σ realization of F_CLIM represents a year of exceptional climate stress (extreme heat, drought, rapid ice loss). Events with 0.5+ loading on F_CLIM would see their probability roughly double in such a year.

## References

- [[methodology-factor-model]]
- IPCC AR6 on climate extremes and tipping points
- 21st_century_assessment.md climate sections
