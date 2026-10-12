# Type 2 pressure off the threshold's 0-100 scale (broken fixture: pressure_scale)

The pressure expression is a weighted sum of [0, 1] terms without the `100 *`
wrapper; at the 2025 baselines it evaluates to 0.325 against a threshold of
65 ± 15, far outside threshold ± 4·std.

```yaml
id: BROKEN_PRESSURE_SCALE
domain: environmental
scale: global
causal_type: 2
onset: gradual
reversibility: irreversible
```

```yaml
probability:
  pressure: |
    0.50 * (global_temp_anomaly / 2.0) +
    0.25 * (1.0 - arctic_sea_ice_sept / 4.5) +
    0.25 * (1.0 - amoc_strength / 95)
  threshold: 65
  threshold_std: 15
  sharpness: 0.15
  floor: 0.002
  annual: 0.010
  confidence: low
```

```yaml
factors:
  F_CLIM: 0.5
variance: 0.25
```

```yaml
impacts:
  default:
    - {var: amoc_strength, mag: [-45, 10], onset: {gradual: 5}, permanent: true}
```
