---
title: 05-source-template
type: note
permalink: methodology/05-source-template
tags:
- methodology
- template
- sources
- research
---

# Source Note Template

Copy this template when creating a new source note.

**Save to:** `sources/[type]/[lowercase-descriptive-name].md`

**Types:** `articles/`, `papers/`, `reports/`, `data/`, `books/`

---

```markdown
# [Descriptive Title]

## Metadata

| Field | Value |
|-------|-------|
| **Type** | article / paper / report / data / book |
| **Author(s)** | |
| **Publication** | |
| **Date** | |
| **Original URL** | |
| **Archive URL** | |
| **DOI** | |
| **Accessed** | |
| **Superseded by** | |

## Summary

[2-5 sentences: What does this source contribute? Why is it relevant to the simulation?]

## Key Claims

- [Specific factual claim or data point we rely on]
- [Quote or paraphrase, with page/section reference if applicable]
- [Another key claim]

## Relevance

- [[events/path/to/event]] — how it informs this event
- [[research/document-name]] — how it informs this synthesis

## Quality Notes

**Reliability:** [Peer-reviewed? Reputable publication? Author credentials? Known biases?]

**Methodology:** [How were claims derived? Sample sizes? Model assumptions?]

**Limitations:** [What doesn't this source tell us? Gaps? Caveats?]

---

*Added: [date]*
```

---

## Field Guidance

### Metadata Fields

| Field | Guidance |
|-------|----------|
| **Type** | One of: article, paper, report, data, book |
| **Author(s)** | Last, First or Organization name |
| **Publication** | Journal, newspaper, publisher, or organization |
| **Date** | Publication date (YYYY-MM-DD or YYYY-MM or YYYY) |
| **Original URL** | Direct link to source (may break over time) |
| **Archive URL** | archive.ph link (stable, created at research time) |
| **DOI** | Digital Object Identifier if available (stable for papers) |
| **Accessed** | Date you accessed/archived the source |
| **Superseded by** | Wiki link to newer source if this one is outdated |

### Summary

Write for future-you who needs to quickly assess whether this source is relevant to a question. Focus on:
- What question does this source help answer?
- What's the main finding or argument?
- Why did we consider this worth archiving?

### Key Claims

Extract specific claims we rely on for parameter estimation:
- Quantitative data (base rates, frequencies, magnitudes)
- Expert probability estimates
- Historical precedents and analogies
- Mechanism descriptions

Use direct quotes sparingly; paraphrase with page/section references.

### Relevance

List all events and documents this source informs. This creates bidirectional links enabling:
- "Show me all sources for Taiwan Conflict"
- "Show me everything this paper influences"

Update this section if the source becomes relevant to additional events.

### Quality Notes

Be honest about limitations. A source can be useful while having significant caveats. Consider:
- Is this peer-reviewed or editorial?
- Does the author have relevant expertise?
- What assumptions underlie the analysis?
- What does this source *not* cover that we might assume it does?

---

## Examples

### Academic Paper

```markdown
# AMOC Tipping Point Assessment

## Metadata

| Field | Value |
|-------|-------|
| **Type** | paper |
| **Author(s)** | Ditlevsen, P. and Ditlevsen, S. |
| **Publication** | Nature Communications |
| **Date** | 2023-07-25 |
| **Original URL** | https://nature.com/articles/s41467-023-39810-w |
| **Archive URL** | — |
| **DOI** | 10.1038/s41467-023-39810-w |
| **Accessed** | 2025-03-15 |
| **Superseded by** | |

## Summary

Statistical analysis of AMOC proxy data suggesting tipping point could occur 
mid-century (2025-2095, 95% CI) under current trajectory. Argues IPCC AR6 
underestimates collapse risk. Key input for AMOC event probability estimation.

## Key Claims

- AMOC collapse could occur as early as 2025, most likely around 2050 (±30 years)
- Statistical significance of declining trend: p < 0.05
- Fingerprint analysis supports acceleration of weakening since 2000

## Relevance

- [[events/climate/amoc-weakening]] — primary source for probability estimation
- [[research/21st-century-assessment]] — informs Europe climate risk section

## Quality Notes

**Reliability:** Peer-reviewed in Nature Communications. Authors are established 
climate scientists. Some controversy — other researchers argue uncertainty is higher.

**Methodology:** Statistical extrapolation from proxy data. Assumes past trends 
continue. Does not model underlying physics directly.

**Limitations:** Wide confidence intervals. Other researchers (e.g., IPCC authors) 
argue statistical approach overstates confidence. Proxy data has known limitations.

---

*Added: 2025-03-15*
```

### News Article

```markdown
# Pakistan Water Crisis Deepens

## Metadata

| Field | Value |
|-------|-------|
| **Type** | article |
| **Author(s)** | Khan, Ayesha |
| **Publication** | The Economist |
| **Date** | 2024-08-15 |
| **Original URL** | https://economist.com/asia/pakistan-water-crisis-2024 |
| **Archive URL** | https://archive.ph/Xk9Lm |
| **DOI** | — |
| **Accessed** | 2025-01-10 |
| **Superseded by** | |

## Summary

Overview of Pakistan's accelerating water crisis: groundwater depletion, 
Indus flow reduction, agricultural impacts. Useful for current conditions 
assessment and pressure function calibration.

## Key Claims

- Groundwater tables falling 1-2 meters/year in Punjab agricultural zone
- Indus River flow down ~25% since 1990s due to upstream factors
- 2024 wheat harvest down 15% from 5-year average
- Government estimates 30% of irrigation infrastructure non-functional

## Relevance

- [[events/geopolitical/pakistan-state-failure]] — pressure function variables
- [[research/21st-century-assessment]] — South Asia water stress section

## Quality Notes

**Reliability:** The Economist is reputable but this is journalism, not research. 
Statistics likely from government sources (may understate problems).

**Methodology:** Reportage with expert quotes. No original analysis.

**Limitations:** Single snapshot in time. May not capture seasonal variation or 
long-term trends accurately.

---

*Added: 2025-01-10*
```

---

## See Also

- [[methodology/reference/research-documentation-standards]] — Full standards document
- [[sources/index]] — Source registry index
