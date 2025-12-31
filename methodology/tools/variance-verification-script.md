---
title: variance-verification-script
type: note
permalink: methodology/tools/variance-verification-script
tags:
- methodology
- tools
- python
- variance
- verification
- factor-model
---

# Variance Verification Script

Python script to verify variance allocation calculations for Sim2075 events.

For each event, computes (ΛΩΛᵀ)ᵢᵢ using the full factor correlation matrix and verifies that scaled loadings produce the target variance.

## Usage

```bash
python3 variance-verification-script.py
```

## Script

```python
#!/usr/bin/env python3
"""
Verify variance allocation calculations for Sim2075 events.

For each event, computes (ΛΩΛᵀ)ᵢᵢ using the full factor correlation matrix
and verifies that scaled loadings produce the target variance.
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
    """
    Compute (ΛΩΛᵀ)ᵢᵢ for a single event.
    
    loadings_dict: dict mapping factor names to loading values
    Returns: factor-explained variance (scalar)
    """
    # Convert to vector in correct order
    lambda_vec = np.array([loadings_dict.get(f, 0.0) for f in FACTORS])
    
    # (ΛΩΛᵀ)ᵢᵢ = λᵢᵀ Ω λᵢ for a single event
    variance = lambda_vec @ OMEGA @ lambda_vec
    return variance

def compute_simple_sum_squares(loadings_dict):
    """Compute simple Σλ² (incorrect when factors correlated)."""
    return sum(v**2 for v in loadings_dict.values())

def verify_event(name, causal_type, target, original_loadings, scaled_loadings, claimed_scale):
    """Verify variance allocation for a single event."""
    print(f"\n{'='*60}")
    print(f"EVENT: {name}")
    print(f"Type: {causal_type} | Target variance: {target}")
    print(f"{'='*60}")
    
    # Compute variances
    orig_simple = compute_simple_sum_squares(original_loadings)
    orig_full = compute_factor_variance(original_loadings)
    
    scaled_simple = compute_simple_sum_squares(scaled_loadings)
    scaled_full = compute_factor_variance(scaled_loadings)
    
    # Compute what scale factor should be
    correct_scale = np.sqrt(target / orig_full)
    
    print(f"\nORIGINAL LOADINGS:")
    print(f"  Simple Σλ²:        {orig_simple:.4f}")
    print(f"  Full (ΛΩΛᵀ)ᵢᵢ:     {orig_full:.4f}")
    print(f"  Cross-term effect: {orig_full - orig_simple:+.4f} ({(orig_full/orig_simple - 1)*100:+.1f}%)")
    
    print(f"\nSCALE FACTOR:")
    print(f"  Claimed:           {claimed_scale:.2f}")
    print(f"  Correct:           {correct_scale:.4f}")
    print(f"  Error:             {abs(claimed_scale - correct_scale):.4f}")
    
    print(f"\nSCALED LOADINGS:")
    print(f"  Simple Σλ²:        {scaled_simple:.4f}")
    print(f"  Full (ΛΩΛᵀ)ᵢᵢ:     {scaled_full:.4f}")
    print(f"  Target:            {target:.2f}")
    print(f"  Error from target: {scaled_full - target:+.4f}")
    
    # Verdict
    scale_ok = abs(claimed_scale - correct_scale) < 0.02
    variance_ok = abs(scaled_full - target) < 0.02
    
    if scale_ok and variance_ok:
        verdict = "✓ PASS"
    elif variance_ok:
        verdict = "⚠ PASS (scale factor rounded but result correct)"
    else:
        verdict = "✗ FAIL"
    
    print(f"\nVERDICT: {verdict}")
    
    return {
        'name': name,
        'orig_simple': orig_simple,
        'orig_full': orig_full,
        'correct_scale': correct_scale,
        'claimed_scale': claimed_scale,
        'scaled_full': scaled_full,
        'target': target,
        'pass': variance_ok
    }


# ============================================================================
# EVENT DATA - Add events here for verification
# ============================================================================

events = [
    # Example event structure:
    # {
    #     'name': 'Event Name',
    #     'type': 'Type 2',
    #     'target': 0.65,
    #     'claimed_scale': 0.77,
    #     'original': {
    #         'F_CLIM': 0.70, 'F_FOOD': 0.45, ...
    #     },
    #     'scaled': {
    #         'F_CLIM': 0.54, 'F_FOOD': 0.34, ...
    #     }
    # },
]

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("VARIANCE ALLOCATION VERIFICATION")
    print("=" * 60)
    print(f"Factor correlation matrix Ω: {OMEGA.shape}")
    print(f"Events to verify: {len(events)}")
    
    # Verify Ω is valid
    eigenvalues = np.linalg.eigvalsh(OMEGA)
    print(f"Ω eigenvalues: min={eigenvalues.min():.4f}, max={eigenvalues.max():.4f}")
    assert eigenvalues.min() > -1e-10, "Ω is not positive semi-definite!"
    print("✓ Ω is valid (positive semi-definite)")
    
    if not events:
        print("\nNo events defined. Add events to the 'events' list to verify.")
    else:
        results = []
        for event in events:
            result = verify_event(
                event['name'],
                event['type'],
                event['target'],
                event['original'],
                event['scaled'],
                event['claimed_scale']
            )
            results.append(result)
        
        # Summary
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for r in results if r['pass'])
        print(f"\nResults: {passed}/{len(results)} events pass")
        
        print("\nDetailed results:")
        print(f"{'Event':<30} {'Orig Var':>10} {'Target':>8} {'Actual':>8} {'Status':>8}")
        print("-" * 70)
        for r in results:
            status = "✓" if r['pass'] else "✗"
            print(f"{r['name']:<30} {r['orig_full']:>10.4f} {r['target']:>8.2f} {r['scaled_full']:>8.4f} {status:>8}")
        
        # Flag any failures
        failures = [r for r in results if not r['pass']]
        if failures:
            print(f"\n⚠️  {len(failures)} EVENT(S) FAILED VERIFICATION:")
            for r in failures:
                print(f"  - {r['name']}: target={r['target']:.2f}, actual={r['scaled_full']:.4f}")
                print(f"    Correct scale factor: {r['correct_scale']:.4f} (claimed: {r['claimed_scale']:.2f})")
```

## Key Functions

### `compute_factor_variance(loadings_dict)`
Computes the true factor-explained variance (ΛΩΛᵀ)ᵢᵢ accounting for factor correlations.

### `compute_simple_sum_squares(loadings_dict)`
Computes the naive Σλ² (only correct when Ω = I).

### `verify_event(...)`
Full verification of a single event including:
- Original variance computation
- Scale factor verification
- Scaled variance verification
- Pass/fail determination

## Notes

- Cross-term effects typically inflate variance by 45-86% beyond simple Σλ²
- Pass threshold: actual variance within ±0.02 of target
- The OMEGA matrix must match [[methodology/reference/factor-correlation-matrix]]

## Related

- [[methodology/reference/variance-allocation]]
- [[methodology/reference/factor-correlation-matrix]]
- [[methodology/tools/compute-scaled-loadings]]