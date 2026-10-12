# Branch p-sum (broken fixture: branch_psum)

```yaml
id: BROKEN_BRANCH_PSUM
domain: political
scale: national
causal_type: 3
onset: sudden
reversibility: partial
```

```yaml
probability:
  window: 0.05
  preconditions:
    all:
      - "F_GPT > 1.0"
  resolution: 0.5
  annual: 0.025
  confidence: low
```

```yaml
factors:
  F_GPT: 0.5
variance: 0.25
```

```yaml
branches:
  - {id: a, p: 0.5}
  - {id: b, p: 0.4}
```

```yaml
impacts:
  a:
    - {var: chn.gdp_real, mag: [-0.1, 0.05], onset: immediate, decay: 2}
  b:
    inherit: a
    scale: 2.0
```

```yaml
cascades:
  triggers:
    - {event: TAIWAN_CONFLICT, delta: 0.01, years: 2}
```
