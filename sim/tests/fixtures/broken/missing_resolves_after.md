# `until: resolved` without `resolves_after` (broken fixture: missing_resolves_after)

```yaml
id: BROKEN_MISSING_RESOLVES_AFTER
domain: political
scale: national
causal_type: 1
onset: sudden
reversibility: partial
```

```yaml
probability:
  annual: 0.02
  confidence: low
```

```yaml
factors:
  F_GPT: 0.5
variance: 0.25
```

```yaml
impacts:
  default:
    - {var: active_major_conflicts, mag: [1, 0], onset: immediate, until: resolved}
```
