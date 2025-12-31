---
title: compute-scaled-loadings
type: note
permalink: methodology/tools/compute-scaled-loadings
tags:
- methodology
- tools
- python
- variance
- factor-model
- loadings
---

# Compute Scaled Loadings Script

Python script to compute correct scaled loadings for Sim2075 events given original loadings and variance targets.

## Usage

```bash
python3 compute-scaled-loadings.py
```

Add events to the `events` list, then run to get correctly scaled loadings.

## Script

```python
#!/usr/bin/env python3
"""
Compute correct scaled loadings for Sim2075 events.

Given original loadings and a target variance, computes:
1. Current factor-explained variance using full Ω matrix
2. Required scale factor
3. Scaled loadings that achieve target variance
"""

import numpy as np

# Factor order (must match Ω matrix)
FACTORS = ['F_CLIM', 'F_FIN', 'F_HLTH', 'F_GPT', 'F_TECH', 'F_FOOD', 
           'F_EUR', 'F_MENA', 'F_SAS', 'F_EAS', 'F_SSA', 'F_LAM']

# Factor correlation matrix Ω from methodology/reference/factor-correlation-matrix
# Order: CLIM, FIN, HLTH, GPT, TECH, FOOD, EUR, MENA, SAS, EAS, SSA, LAM
OMEGA = np.array([
    [1.00, 0.00, 0.00, 0.00, 0.00, 0.50, 0.00, 0.30, 0.30, 0.00, 0.35, 0.00],  # CLIM
    [0.00, 1.00, 0.30, 0.25, 0.20, 0.00, 0.40, 0.20, 0.00, 0.30, 0.00, 0.35],  # FIN
    [0.00, 0.30, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  # HLTH
    [0.00, 0.25, 0.00, 1.00, 0.25, 0.00, 0.30, 0.00, 0.00, 0.55, 0.00, 0.00],  # GPT
    [0.00, 0.20, 0.00, 0.25, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],  # TECH
    [0.50, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.40, 0.30, 0.00, 0.40, 0.00],  # FOOD
    [0.00, 0.40, 0.00, 0.30, 0.00, 0.00, 1.00, 0.30, 0.00, 0.00, 0.20, 0.00],  # EUR
    [0.30, 0.20, 0.00, 0.00, 0.00, 0.40, 0.30, 1.00, 0.00, 0.00, 0.25, 0.00],  # MENA
    [0.30, 0.00, 0.00, 0.00, 0.00, 0.30, 0.00, 0.00, 1.00, 0.00, 0.00, 0.00],  # SAS
    [0.00, 0.30, 0.00, 0.55, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00],  # EAS
    [0.35, 0.00, 0.00, 0.00, 0.00, 0.40, 0.20, 0.25, 0.00, 0.00, 1.00, 0.00],  # SSA
    [0.00, 0.35, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00],  # LAM
])

def compute_factor_variance(loadings_dict):
    """Compute (ΛΩΛᵀ)ᵢᵢ for a single event."""
    lambda_vec = np.array([loadings_dict.get(f, 0.0) for f in FACTORS])
    return lambda_vec @ OMEGA @ lambda_vec

def scale_loadings(loadings_dict, target):
    """Scale loadings to achieve target variance."""
    current = compute_factor_variance(loadings_dict)
    scale = np.sqrt(target / current)
    scaled = {k: round(v * scale, 2) for k, v in loadings_dict.items()}
    return scaled, scale, current


# ============================================================================
# EVENT DATA - Add events here to compute scaled loadings
# ============================================================================

events = [
    # Example:
    # {
    #     'name': 'AMOC Weakening',
    #     'file': 'events/climate/amoc-weakening.md',
    #     'type': 'Type 2',
    #     'target': 0.65,
    #     'original': {
    #         'F_CLIM': 0.85, 'F_FOOD': 0.20, 'F_EUR': 0.15, 
    #         'F_SSA': 0.10, 'F_LAM': 0.05
    #     }
    # },
]


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("=" * 80)
    print("COMPUTE SCALED LOADINGS")
    print("=" * 80)
    
    if not events:
        print("\nNo events defined. Add events to the 'events' list.")
        print("\nExample event structure:")
        print("""
    {
        'name': 'Event Name',
        'file': 'events/domain/event-file.md',
        'type': 'Type 2',  # or Type 1, Type 3
        'target': 0.65,    # Type 2 = 0.65, Type 3 = 0.45, Type 1 = 0.75
        'original': {
            'F_CLIM': 0.70, 'F_FOOD': 0.45, ...  # non-zero loadings only
        }
    }
        """)
    else:
        for event in events:
            scaled, scale, orig_var = scale_loadings(event['original'], event['target'])
            
            # Verify
            final_var = compute_factor_variance(scaled)
            
            print(f"\n{'='*80}")
            print(f"EVENT: {event['name']}")
            print(f"File: {event['file']}")
            print(f"Type: {event['type']} | Target: {event['target']}")
            print(f"Original variance: {orig_var:.4f}")
            print(f"Scale factor: {scale:.4f}")
            print(f"Final variance: {final_var:.4f} (error: {final_var - event['target']:+.4f})")
            print(f"{'='*80}")
            
            print("\nSCALED LOADINGS (copy to event file):")
            print("| Factor | Loading | Rationale |")
            print("|--------|---------|-----------|")
            
            # Print non-zero loadings first
            for f in FACTORS:
                orig = event['original'].get(f, 0.0)
                new = scaled.get(f, 0.0)
                if orig > 0:
                    # Bold for primary factors (loading >= 0.20)
                    if new >= 0.20:
                        print(f"| **{f}** | {new:.2f} | [rationale] |")
                    else:
                        print(f"| {f} | {new:.2f} | [rationale] |")
            
            # Print zero loadings
            for f in FACTORS:
                if event['original'].get(f, 0.0) == 0:
                    print(f"| {f} | 0.00 | [No pathway / No linkage] |")
            
            print(f"\n**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = {event['target']:.2f} ({event['type']} target); scale factor = {scale:.2f} from original loadings")
        
        # Summary table
        print("\n" + "=" * 80)
        print("SUMMARY: ALL SCALE FACTORS")
        print("=" * 80)
        print(f"{'Event':<35} {'Type':<8} {'Target':>7} {'Orig Var':>10} {'Scale':>8}")
        print("-" * 75)
        for event in events:
            scaled, scale, orig_var = scale_loadings(event['original'], event['target'])
            print(f"{event['name']:<35} {event['type']:<8} {event['target']:>7.2f} {orig_var:>10.4f} {scale:>8.4f}")
```

## Variance Targets by Type

| Causal Type | Target (ΛΩΛᵀ)ᵢᵢ | Rationale |
|-------------|-----------------|-----------|
| Type 1 (Stochastic) | 0.75 | Large-N averaging; factors explain most variance |
| Type 2 (Threshold) | 0.65 | Observable pressure; threshold uncertain |
| Type 3 (Contingent) | 0.45 | Factors explain windows; resolution intractable |

## Output Format

The script outputs markdown-formatted loading tables ready to copy into event files:

```markdown
| Factor | Loading | Rationale |
|--------|---------|-----------|
| **F_CLIM** | 0.67 | [rationale] |
| F_FOOD | 0.16 | [rationale] |
...

**Variance allocation**: (ΛΩΛᵀ)ᵢᵢ = 0.65 (Type 2 target); scale factor = 0.79 from original loadings
```

## Mathematical Notes

The scale factor is computed as:

```
s = √(target / current)
```

Where `current = λᵀΩλ` for the original loadings vector λ.

All loadings are then scaled uniformly: `λ' = s × λ`

This preserves relative factor importance while achieving the target variance.

## Related

- [[methodology/reference/variance-allocation]]
- [[methodology/reference/factor-correlation-matrix]]
- [[methodology/tools/variance-verification-script]]