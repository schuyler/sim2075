---
title: research-documentation-standards
type: note
permalink: methodology/reference/research-documentation-standards
tags:
- methodology
- reference
- research
- documentation
- sources
- citations
---

# Research Documentation Standards

Standards for documenting sources, managing citations, and producing research artifacts across Level 1/2/3 tiers.

---

## Overview

As events and entities become ongoing research projects, evidence accumulates over time. These standards ensure:

- **Provenance** — Parameter choices trace to specific sources
- **Durability** — Sources remain accessible despite link rot
- **Accumulation** — Research builds incrementally across sessions
- **Quality tracking** — Source reliability and staleness are visible

---

## Source Registry

All significant sources are registered as notes in the `sources/` directory. This creates a searchable, cross-referenced library of evidence supporting the simulation's parameters.

### Directory Structure

```
sources/
  index.md              # Lookup guidance and organization
  articles/             # News, magazine, opinion pieces
  papers/               # Academic/peer-reviewed
  reports/              # Think tanks, IGOs, NGOs, government
  data/                 # Datasets, statistical releases
  books/                # Book chapters, excerpts
```

### When to Create a Source Note

Create a source note when:
- A source directly informs a parameter choice (probability, loading, impact magnitude)
- A source provides calibration evidence (historical analogs, base rates)
- A source shapes understanding of mechanisms or pathways
- You read it and it informed your thinking, even if not directly cited

Do not create source notes for:
- Claude's training knowledge (Level 1 work has no sources)
- Casual background reading that didn't influence specifications
- Sources fully superseded by newer work already in registry

### Source Note Template

Use [[methodology/05-source-template]] for creating new source notes.

### Naming Convention

**Format:** `lowercase-descriptive-name.md`

**Pattern:** `[publication]-[topic]-[year].md`

**Examples:**
- `foreign-affairs-taiwan-semiconductor-leverage-2024.md`
- `nature-amoc-tipping-point-assessment-2023.md`
- `rand-pakistan-nuclear-security-2022.md`
- `imf-lebanon-article-iv-2023.md`

Keep names descriptive enough to identify without opening, but concise.

---

## Archival Requirements

Online sources may be moved, removed, or placed behind paywalls. Archive key sources at time of research to ensure long-term accessibility.

### Archival Workflow

1. **Find source** via web search
2. **Check archive.ph** for existing snapshot: `archive.ph/[original-url]`
3. **If no snapshot exists**, create one: submit URL to archive.ph
4. **Record both URLs** in source note (Original URL and Archive URL)
5. **Note access date** — establishes when content was captured

### What to Archive

| Source Type | Archive? | Notes |
|-------------|----------|-------|
| News articles | Yes | High link rot risk |
| Magazine/opinion pieces | Yes | Often reorganized |
| Blog posts | Yes | Frequently disappear |
| Think tank reports | Yes | PDFs may move |
| Government pages | Yes | Change frequently |
| Academic papers with DOI | No | DOIs are stable |
| Books | No | ISBN sufficient |
| Paywalled content | Yes | archive.ph may capture |

### Archive URL Format

archive.ph URLs are stable and follow the pattern:
- `https://archive.ph/AbC12` (short hash)
- `https://archive.ph/2024.03.15-123456/https://example.com/article` (timestamped)

Either format is acceptable in source notes.

---

## Citation Conventions

### In Event Specifications

Event specs include a **Sources** section listing all sources that informed the specification:

```markdown
## Sources

| Source | Relevance |
|--------|-----------|
| [[sources/papers/nature-amoc-tipping-point-assessment-2023]] | Threshold probability range |
| [[sources/reports/rand-taiwan-conflict-scenarios-2024]] | Resolution branch calibration |
| [[sources/articles/economist-pakistan-water-crisis-2024]] | Pressure function variables |
```

For specific claims within the spec, use inline references:

```markdown
Historical basis for window probability (~3%): Acute crises reaching threshold 
where military action became imminent occurred 3-4 times since 1954 
([[sources/papers/mit-taiwan-strait-crises-history-2021]]).
```

### In Synthesis Documents

Synthesis documents (like [[research/21st-century-assessment]]) use inline wiki links:

```markdown
Recent modeling suggests AMOC collapse probability may be higher than 
IPCC AR6 estimates ([[sources/papers/nature-amoc-tipping-point-assessment-2023]]), 
with some researchers arguing the risk has been systematically underestimated.
```

### Bidirectional Linking

Every source note includes a **Relevance** section listing where the source is used:

```markdown
## Relevance

- [[events/climate/amoc-weakening]] — informs threshold probability
- [[research/21st-century-assessment]] — informs Europe section
- [[events/geopolitical/eu-fragmentation]] — informs cascade effects
```

This enables:
- Finding all sources for a given event
- Finding all events informed by a given source
- Auditing provenance chains

---

## Research Tier Deliverables

### Level 1: Prior Knowledge

**Method:** Claude generates from training knowledge and project documents

**Sources:** None — this is the baseline

**Output:**
- Complete event specification following template
- Research Status: "Level 1"
- Open Questions section identifying gaps for future research

**Quality standard:** Internally consistent, honestly uncertain. Acceptable to be wrong by 2x on key parameters.

### Level 2: Targeted Research

**Method:** Dedicated session with web searches, 2-4 hours

**Sources:** 3-10 source notes created, archived, and linked

**Output:**
- Revised event specification with Sources section
- Source notes for each significant source
- Updated probability/impact estimates with citation support
- Narrowed uncertainty ranges where evidence exists

**Quality standard:** Key claims have sources. Estimates defensible against informed critique.

### Level 3: Full Research Project

**Method:** Extended research with autonomous subagents, 8-20 hours

**Sources:** 10-30+ source notes, comprehensive coverage

**Output:**
- Detailed research document (`research/[topic].md`) synthesizing findings
- Revised event specification with comprehensive Sources section
- Multiple estimation methods compared
- Expert disagreements documented
- Source quality systematically assessed

**Quality standard:** Would survive peer review. Represents best available understanding.

---

## Quality and Staleness Tracking

### Source Quality Assessment

Each source note includes a **Quality Notes** section assessing:

- **Reliability:** Peer-reviewed? Reputable publication? Known biases?
- **Methodology:** How were claims derived? Sample sizes? Model assumptions?
- **Relevance:** How directly applicable to our questions?
- **Limitations:** What doesn't this source tell us?

### Staleness Tracking

Sources can become outdated as events unfold or new research emerges.

**Superseded by field:** When a source is superseded by newer work:

```markdown
## Metadata
...
| **Superseded by** | [[sources/papers/nature-amoc-updated-assessment-2025]] |
```

**Staleness indicators:**
- Source >3 years old on fast-moving topic — review for updates
- Major events since publication — may need supplementation
- Contradicted by newer sources — note in Quality Notes

**Handling stale sources:**
1. Keep the original source note (historical record)
2. Add "Superseded by" reference to newer source
3. Update event specs to cite current source
4. Note in Quality Notes what changed

---

## Index Maintenance

The `sources/index.md` file provides lookup guidance. As the registry grows:

**Organize by:**
- Topic clusters (climate, geopolitical, financial, etc.)
- Key events they inform
- Recency (recent sources for rapidly evolving topics)

**Update index when:**
- Adding sources to a new topic area
- Accumulating >10 sources on a single topic
- Sources become important cross-references

---

## Workflow Summary

### Level 2 Research Workflow

1. **Identify research questions** from event's Open Questions
2. **Web search** for relevant sources
3. **For each significant source:**
   - Archive via archive.ph
   - Create source note using template
   - Extract key claims and quality assessment
4. **Update event specification:**
   - Revise estimates based on evidence
   - Add Sources section with links
   - Update Research Status to Level 2
   - Revise Open Questions
5. **Update source index** if needed
6. **Commit atomic set** of changes to git

### Source Note Creation Workflow

1. **Copy template** from [[methodology/05-source-template]]
2. **Fill metadata** (author, publication, date, URLs)
3. **Write summary** (2-5 sentences on contribution)
4. **Extract key claims** (specific facts/data we rely on)
5. **Assess quality** (reliability, limitations)
6. **Add relevance links** (which events/documents this informs)
7. **Save** to appropriate `sources/[type]/` directory

---

## Related Documents

- [[methodology/05-source-template]] — Template for source notes
- [[methodology/project/research-tiers]] — Tier definitions and progression criteria
- [[methodology/01-level-1-workflow]] — Level 1 production process
- [[sources/index]] — Source registry index

---

*Version 1.0 — December 2025*
