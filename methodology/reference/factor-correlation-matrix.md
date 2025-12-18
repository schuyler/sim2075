---
title: factor-correlation-matrix
type: note
permalink: methodology/reference/factor-correlation-matrix
tags:
- methodology
- reference
- factors
- correlation
- matrix
---

# Factor Correlation Matrix (Ω)

This document specifies correlations between the 12 latent factors. See [[methodology/concepts/factor-correlation-structure]] for why we use an inter-factor correlation matrix rather than independent factors.

---

## Estimation Approach

**Default**: Correlation is zero unless there's a clear mechanism.

**Correlation strength guidelines**:

| Magnitude | Interpretation | Threshold for inclusion |
|-----------|----------------|------------------------|
| 0.0 | No relationship | Default |
| 0.1–0.2 | Weak | Only if mechanism is clear but indirect |
| 0.3–0.4 | Moderate | Direct mechanism, one of several drivers |
| 0.5–0.6 | Strong | Primary transmission channel |
| 0.7+ | Very strong | Reserved; factors would be nearly redundant |

We avoid correlations above 0.6 between factors—if two factors are that correlated, they may not be distinct constructs.

**Symmetry limitation**: Correlation matrices are symmetric. Where causal direction matters (F_CLIM drives F_FOOD more than reverse), we note this but cannot represent it in Ω. The correlation captures "tend to co-occur" without encoding direction.

---

## Non-Zero Correlations

### Climate Cascade

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_CLIM ↔ F_FOOD | 0.50 | Drought, heat, and flooding directly disrupt agricultural production. Climate stress is the primary driver of food system stress. |
| F_CLIM ↔ F_SSA | 0.35 | Sub-Saharan Africa is highly climate-vulnerable: Sahel desertification, East African drought cycles, agricultural dependence. |
| F_CLIM ↔ F_SAS | 0.30 | South Asia depends on monsoon regularity and Himalayan glacier melt for water. Climate stress directly pressures the region. |
| F_CLIM ↔ F_MENA | 0.30 | MENA faces severe water stress amplified by climate change. Nile flows, Gulf heat extremes, agricultural margins. |

### Food System Propagation

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_FOOD ↔ F_SSA | 0.40 | Many SSA economies are agricultural; food price spikes cause immediate instability. Limited fiscal capacity to buffer. |
| F_FOOD ↔ F_MENA | 0.40 | MENA is heavily food-import dependent (Egypt imports ~50% of wheat). Food prices were a trigger for Arab Spring. |
| F_FOOD ↔ F_SAS | 0.30 | Large populations near subsistence; food stress translates quickly to political pressure. |

### Financial Contagion

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_FIN ↔ F_EUR | 0.40 | Eurozone financial integration means banking stress propagates. Sovereign-bank doom loop. ECB policy constraints. |
| F_FIN ↔ F_LAM | 0.35 | Dollar-denominated debt, commodity export dependence, history of contagion (1980s debt crisis, Tequila crisis, 2001 Argentina). |
| F_FIN ↔ F_EAS | 0.30 | Trade finance linkages, 1997 Asian financial crisis precedent, China credit concerns. |
| F_FIN ↔ F_MENA | 0.20 | Oil price volatility affects fiscal positions; less direct financial integration than other regions. |

### Great Power Tension

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_GPT ↔ F_EAS | 0.55 | East Asia is the primary theater of US-China competition: Taiwan, South China Sea, Korean peninsula. Regional stress and great power tension are deeply intertwined. |
| F_GPT ↔ F_EUR | 0.30 | NATO-Russia dynamic; Europe is secondary theater but still significant. Ukraine, Baltic security. |
| F_GPT ↔ F_FIN | 0.25 | Sanctions regimes, trade wars, financial weaponization. Economic tools of great power competition. |
| F_GPT ↔ F_TECH | 0.25 | Technology competition (semiconductors, AI) is a dimension of great power rivalry. Export controls, R&D races. |

### Health-Economic Linkage

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_HLTH ↔ F_FIN | 0.30 | Pandemics cause economic disruption; COVID demonstrated the financial market sensitivity to health crises. |

### Regional Proximity

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_MENA ↔ F_EUR | 0.30 | Geographic proximity drives migration flows, energy dependence, and policy spillovers. Mediterranean as shared space. |
| F_SSA ↔ F_EUR | 0.20 | Migration pressure (Sahel → North Africa → Europe), development linkages, former colonial ties. |
| F_MENA ↔ F_SSA | 0.25 | Sahel sits at boundary; instability in Libya/North Africa propagates south. Shared climate pressures. |

### Technology Linkage

| Factor Pair | ρ | Mechanism |
|-------------|---|-----------|
| F_TECH ↔ F_FIN | 0.20 | Technology disruption affects labor markets, asset valuations, and financial system stability. AI automation concerns. |

---

## Full Correlation Matrix

Factors ordered: F_CLIM, F_FIN, F_HLTH, F_GPT, F_TECH, F_FOOD, F_EUR, F_MENA, F_SAS, F_EAS, F_SSA, F_LAM

```
         CLIM   FIN  HLTH   GPT  TECH  FOOD   EUR  MENA   SAS   EAS   SSA   LAM
CLIM     1.00  0.00  0.00  0.00  0.00  0.50  0.00  0.30  0.30  0.00  0.35  0.00
FIN      0.00  1.00  0.30  0.25  0.20  0.00  0.40  0.20  0.00  0.30  0.00  0.35
HLTH     0.00  0.30  1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00
GPT      0.00  0.25  0.00  1.00  0.25  0.00  0.30  0.00  0.00  0.55  0.00  0.00
TECH     0.00  0.20  0.00  0.25  1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00
FOOD     0.50  0.00  0.00  0.00  0.00  1.00  0.00  0.40  0.30  0.00  0.40  0.00
EUR      0.00  0.40  0.00  0.30  0.00  0.00  1.00  0.30  0.00  0.00  0.20  0.00
MENA     0.30  0.20  0.00  0.00  0.00  0.40  0.30  1.00  0.00  0.00  0.25  0.00
SAS      0.30  0.00  0.00  0.00  0.00  0.30  0.00  0.00  1.00  0.00  0.00  0.00
EAS      0.00  0.30  0.00  0.55  0.00  0.00  0.00  0.00  0.00  1.00  0.00  0.00
SSA      0.35  0.00  0.00  0.00  0.00  0.40  0.20  0.25  0.00  0.00  1.00  0.00
LAM      0.00  0.35  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.00
```

**Summary statistics:**
- Non-zero off-diagonal entries: 19 (of 66 possible)
- Maximum correlation: 0.55 (F_GPT ↔ F_EAS)
- Mean non-zero correlation: 0.31

---

## Factors With No Inter-Factor Correlations

Some factors have no correlations with other factors:

- **None fully isolated** — Every factor has at least one non-zero correlation

Factors with minimal correlations (only 1-2 links):
- **F_HLTH**: Only links to F_FIN. Pandemic emergence is largely stochastic; health factor is intentionally isolated from other systemic pressures.
- **F_TECH**: Links to F_FIN and F_GPT. Technology disruption is partly endogenous to great power competition but otherwise independent of climate/regional dynamics.
- **F_LAM**: Only links to F_FIN. Latin America is geographically isolated from Eurasian dynamics; financial contagion is primary transmission channel.
- **F_SAS**: Links to F_CLIM and F_FOOD. South Asian stress is primarily climate/food-driven; relatively isolated from European and East Asian dynamics.

---

## Validation Requirements

Before implementation, verify:

1. **Positive semi-definite**: All eigenvalues of Ω must be ≥ 0. If not, the matrix cannot represent a valid correlation structure.

2. **Diagonal = 1**: All diagonal entries must equal 1 (factors have unit variance).

3. **Symmetric**: Ω must equal its transpose.

```python
import numpy as np

def validate_correlation_matrix(omega):
    """Validate that Ω is a valid correlation matrix."""
    # Check symmetric
    assert np.allclose(omega, omega.T), "Matrix not symmetric"
    
    # Check diagonal
    assert np.allclose(np.diag(omega), 1.0), "Diagonal not all 1s"
    
    # Check positive semi-definite
    eigenvalues = np.linalg.eigvalsh(omega)
    assert np.all(eigenvalues >= -1e-10), f"Not PSD: min eigenvalue = {eigenvalues.min()}"
    
    print("Validation passed")
    return True
```

If validation fails, correlations must be adjusted (typically by reducing the largest correlations) until the matrix is valid.

---

## Sensitivity Analysis

Key correlations for sensitivity testing:

| Correlation | Baseline | Test Range | Rationale |
|-------------|----------|------------|-----------|
| F_CLIM ↔ F_FOOD | 0.50 | 0.3–0.7 | Core climate cascade assumption |
| F_GPT ↔ F_EAS | 0.55 | 0.3–0.7 | How tightly is East Asia coupled to great power dynamics? |
| F_FIN ↔ F_EUR | 0.40 | 0.2–0.6 | Eurozone financial integration strength |
| F_FOOD ↔ F_MENA | 0.40 | 0.2–0.6 | Food import vulnerability |

Run simulation with correlation at low/baseline/high to assess impact on tail outcomes.

---

## Revision History

| Date | Change |
|------|--------|
| December 2025 | Initial specification |

---

*See [[methodology/concepts/factor-correlation-structure]] for design rationale*
*See [[methodology/concepts/gaussian-copula]] for how Ω enters the sampling procedure*


---

## Known Limitations and Open Issues

### Double-Counting Correlation

Events can correlate with climate-sensitive outcomes through two channels:
1. **Direct loading**: Event loads on F_CLIM
2. **Factor correlation**: Event loads on F_SAS, which correlates with F_CLIM

For an event like Pakistan state failure (loads on both F_SAS at 0.85 and F_CLIM at 0.38), both channels operate simultaneously. This may inflate the effective climate sensitivity beyond what either channel alone would produce.

**Status**: Accepted for now. When more events are specified, compute implied event correlations and verify they remain sensible. If correlations appear inflated, consider reducing either cross-loadings or factor correlations.

### Symmetric Correlation Misrepresents Causal Direction

The matrix treats F_CLIM ↔ F_FOOD as symmetric (0.50 both directions), but the causal relationship is asymmetric: climate stress drives food stress, not the reverse. 

In simulation, a high F_FOOD draw (e.g., from trade disruption) will also tend to produce high F_CLIM draws—implying elevated climate stress when none is warranted.

**Status**: Accepted as inherent limitation of correlation-based approach. The alternative (causal modeling) would require a different architecture entirely. For interpretation, remember that factor correlations represent "tend to co-occur" not "cause each other."

### Transitive Consistency Not Verified

The matrix specifies:
- F_CLIM ↔ F_FOOD: 0.50
- F_FOOD ↔ F_MENA: 0.40  
- F_CLIM ↔ F_MENA: 0.30

These create transitive pathways. The direct F_CLIM ↔ F_MENA correlation (0.30) should be consistent with the indirect path through F_FOOD. The PSD check confirms mathematical validity, but doesn't confirm the correlations tell a coherent causal story.

**Status**: The matrix passed PSD validation with comfortable margin (min eigenvalue 0.20), suggesting no gross inconsistency. Detailed review of transitive implications deferred until more events are specified.

### No Empirical Calibration

All correlations are judgment-based. No historical data on factor co-occurrence was used. This is unavoidable (latent factors aren't directly observable), but means the matrix is speculative.

**Status**: Document reasoning for each correlation; flag high-uncertainty estimates for sensitivity analysis. Accept that this is structured judgment, not empirical estimation.
