Deliberately-broken event files, one per failure mode the E2 rejection gate requires
(implementation guide §5.1). Each is a minimal otherwise-valid Type 1/3 event with exactly one defect.
The compiler must reject each with the event ID in the error message.

`pressure_scale.md` (added with the 2026-10-12 schema change) is the sixth: a Type 2 pressure expression
off the threshold's 0-100 scale, rejected with the value computed at the 2025 baselines.
`missing_resolves_after.md` (same date) is the seventh: an `until: resolved` row on an event whose
probability block has no `resolves_after`.
