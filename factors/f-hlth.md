---
title: f-hlth
type: note
permalink: factors/f-hlth
tags:
- factor
- health
- pandemic
- correlation-structure
---

# F_HLTH: Health/Pandemic Factor

## Overview

The Health/Pandemic factor represents global health system stress and pandemic risk. When F_HLTH has a high realization, pandemic events and health system failures become more likely.

## What This Factor Captures

- Novel pathogen emergence risk
- Health system capacity and strain
- Pandemic preparedness gaps
- Antibiotic resistance pressure
- Zoonotic spillover conditions
- Global health governance effectiveness

## Events That Load Heavily on F_HLTH

| Event | Loading | Rationale |
|-------|---------|-----------|
| Severe Pandemic | 0.90 | This IS the factor manifesting |
| Catastrophic Pandemic | 0.85 | Extreme health system event |
| Antibiotic Resistance Crisis | 0.70 | Health system structural failure |
| Regional Healthcare Collapse | 0.60 | System capacity failure |

## Correlation Implications

F_HLTH is somewhat more independent than other factors. Pandemics are partially random (novel pathogen emergence) but preparedness and response capacity are correlated across countries.

High F_HLTH realizations increase probability of:
- Pandemic emergence and spread
- Health system failures in weak states
- Compound crises where health shocks interact with other stresses

## Relationship to Other Factors

- **F_SSA, F_SAS**: Health system weakness correlates with development level
- **Regional factors**: Pandemics affect all regions, but capacity to respond varies
- **F_FIN**: Pandemics cause economic disruption; relationship is causal not correlational

## Calibration Notes

Pandemic risk is harder to estimate than financial or geopolitical risk because base rates are low and variable. COVID provided a recent calibration point, but pandemic severity varies enormously.

## References

- [[methodology-factor-model]]
- Historical pandemic analysis
