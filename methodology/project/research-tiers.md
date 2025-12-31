---
title: research-tiers
type: note
permalink: methodology/research-tiers
tags:
- methodology
- research
- tiers
- process
---

# Research Tiers

## Overview

Not all events deserve equal research investment. Use tiered approach: start shallow, deepen where it matters.

**Documentation standards:** [[methodology/reference/research-documentation-standards]]

---

## Level 1: Prior Knowledge Skeleton

**Method:** Claude Opus generates specification from prior knowledge and project documents

**Time:** ~30 minutes per event

**When:** All priority events initially

**What you get:**
- Rough probability estimate with range
- Factor loadings based on event type patterns
- Impact estimates scaled from similar events
- Key uncertainties flagged

**Quality standard:** Internally consistent, honestly uncertain, documents reasoning. Not deeply researched—acceptable to be wrong by 2x on probability or impacts.

**Output:** Complete event specification following template, marked as "Level 1"

---

## Level 2: Targeted Web Research

**Method:** Dedicated chat session with targeted web searches

**Time:** 2-4 hours per event

**When:** Events flagged by sensitivity analysis as high-impact on tail outcomes

**What you get:**
- Probability grounded in literature (expert estimates, historical base rates)
- Impacts calibrated to specific historical analogs
- Transmission channels documented
- Uncertainty ranges narrowed where evidence exists

**Quality standard:** Key claims have sources. Probability and impact estimates are defensible against informed critique.

**Output:** Revised event specification with source citations, marked as "Level 2"

---

## Level 3: Full Research Project

**Method:** Claude.ai research project with autonomous subagents

**Time:** 8-20 hours equivalent

**When:** 3-5 events that drive tail outcomes and merit deep investigation

**What you get:**
- Comprehensive literature review
- Multiple estimation methods applied and compared
- Expert disagreements documented
- Conditional probability structures (if applicable)
- High-confidence estimates where achievable, honest uncertainty elsewhere

**Quality standard:** Would survive peer review. Represents best available understanding.

**Output:** Detailed research document plus revised specification, marked as "Level 3"

---

## Progression Criteria

### When to Upgrade from Level 1 to Level 2

After prototype simulation runs sensitivity analysis:

- Event appears in >30% of worst-5% outcomes
- Small changes to event probability substantially shift outcome distribution
- Event is a "gateway" that triggers cascades

### When to Upgrade from Level 2 to Level 3

After Level 2 research:

- Event remains high-sensitivity
- Level 2 research revealed substantial disagreement or uncertainty
- Event is among top 5 drivers of tail risk
- Better estimates would materially change planning conclusions

---

## Research Tier Documentation

Every event specification must note:

```
## Research Status
- **Tier:** Level 1 / Level 2 / Level 3
- **Last updated:** [date]
- **Upgrade candidate:** Yes / No
- **Upgrade rationale:** [if yes, why]
```
