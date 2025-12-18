---
title: validation
type: note
permalink: methodology/validation
tags:
- methodology
- validation
- testing
---

# Validation Approaches

## The Validation Problem

We cannot validate this model in the traditional sense:
- We can't wait 50 years to check probability estimates
- We have no ground truth for factor loadings
- Historical data is too sparse for rigorous backtesting

However, we can apply **partial validation** approaches that increase confidence without providing definitive proof.

---

## Internal Consistency Checks

### Cross-Event Consistency

- Do similar events have similar probabilities?
- Do similar events have similar loading patterns?
- Are relative rankings stable under different estimation methods?

### Structural Validity

- Does the correlation matrix produced by loadings make sense?
- Do events that should cluster actually cluster in simulation?
- Are compound scenarios occurring at sensible frequencies?

### Sanity Bounds

- Is the "nothing happens" scenario appropriately rare/common?
- Are cumulative impacts over 50 years in plausible ranges?
- Do terminal states look like possible worlds?

---

## Historical Backtesting (Limited)

### What We Can Test

- Do historical event frequencies roughly match our estimates?
- Did events cluster historically as our correlation structure implies?
- Do historical impact magnitudes match our calibration?

### How To Do It

- Run simulation for historical period (e.g., 1970-2020)
- Compare event frequencies and clustering to actual history
- Identify where model diverges and investigate why

### Limitations

- 50 years is one sample path—can't distinguish model error from randomness
- Historical conditions differ from future conditions
- Risk of circular calibration to history

---

## Expert Review

### Process

1. Present output distributions to domain experts
2. Ask: "Are these distributions plausible?"
3. Identify specific objections
4. Revise and repeat

### What Experts Can Assess

- Are tail scenarios realistic?
- Are we missing important events?
- Do country trajectories match expert intuition?
- Are transmission mechanisms reasonable?

### Limitations

- Experts may share blind spots
- Intuition is not calibration
- Experts disagree with each other

---

## Sensitivity Analysis as Validation

If results are highly sensitive to uncertain parameters, that itself is information:

| Finding | Implication |
|---------|-------------|
| **Sensitive parameters** | Need more research, or accept high uncertainty |
| **Insensitive parameters** | Can use rough estimates with confidence |
| **Robust conclusions** | Hold across parameter ranges—trustworthy |

Sensitivity analysis identifies where model output is trustworthy vs. where it depends on assumptions.

---

## Prediction Market Comparison

Where prediction markets exist for relevant questions:
- Compare our estimates to market prices
- Investigate divergences
- Use market prices as sanity check, not ground truth

**Available markets:** Metaculus, Polymarket for some geopolitical questions. Limited coverage of our full event space.

---

## Documentation of Validation Efforts

For each validation approach applied, document:
- What was tested
- What was found
- What revisions were made (if any)
- What limitations remain

Validation is ongoing, not one-time.
