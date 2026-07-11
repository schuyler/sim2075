---
title: pcm-v25-synopsis-notes
type: research-input
permalink: strategy/inputs/pcm-v25-synopsis-notes
tags:
- strategy
- research
- pcm
- cascade-institute
- sources
---

# Source Notes: PCM v2.5 Technical Synopsis

Primary-source figures verified directly from the Cascade Institute's PCM v2.5 technical synopsis PDF, for citation in [[strategy/pcm-integration-brief]]. Everything below was read from the document itself, page by page.

- **Source**: "Polycrisis Core Model: Technical synopsis of results of PCM v2.5"
- **URL**: https://cascadeinstitute.org/wp-content/uploads/2025/08/Cascade-Institute-Polycrisis-Core-Model-v2.5-technical-synopsis-of-results-Aug-11-2025.pdf
- **Accessed**: 2026-07-10 (fetched and read pp. 1–12, including Appendices 1–3)
- **Document date**: August 10, 2025
- **Authors**: Thomas Homer-Dixon, Mike Lawrence, Megan Shipman, Scott Janzwood, Luke Kemp, Simone Philpot, Vanessa Schweizer, Jordan Bendall
- Project page: https://cascadeinstitute.org/polycrisis-core-model/ (also accessed 2026-07-10; confirms 2040 horizon and open-model aim; adds team members not on the synopsis byline, e.g., Michael Lawrence's and Scott Janzwood's roles)

## Model structure (verified)

- 11 descriptors, each with 3–5 discrete states; **45 states total**; combinations yield **4.05 million scenarios** (p. 4).
- **Over 1,800 judgments** in the v2.5 matrix, generated spring 2025 after 18 months' preliminary work; grounded in "empirical data, scientific studies, and other forms of expert knowledge" (p. 3).

### Descriptors and states (Appendix 1, p. 9)

| Group | Descriptor | States |
|---|---|---|
| Social | Economy | Laissez-faire growth; Guided growth; Low growth; Managed economic contraction; Unmanaged economic failure |
| Social | Polity Type | Strong democracy; Illiberal democracy; Strong autocracy; Weak autocracy; Nonocracy |
| Social | World Order | International fragmentation; Multipolarity; Consolidated blocs; Multilateral rules-based order; Thick global governance |
| Social | Inequality | Low intl/low domestic; High intl/low domestic; Low intl/high domestic; High intl/high domestic |
| Social | Conflict & Security | Low violence; Widespread non-state violence; Civil/proxy war; International war; Great power war |
| Material | Energy | Fossil-fuel dependence; Peak oil and gas; Green-tech breakthrough; Low-carbon energy contraction |
| Material | Climate | <2.5°C in 2100; 2.5–4°C; >4°C |
| Material | Health | High / Medium / Low burden of disease (global DALYs) |
| Material | Food | Status-quo global industrial production; Agri-tech industrial breakthrough; Agro-ecological production; Variable regional production; Failed global industrial production |
| Material | Transportation | Fit for the future; Fit for now; Fragmented and failing |
| Material | Information Technology | Limited rollout; Managed rollout; Unmanaged rollout |

Note: Appendix 3's ScenarioWizard output labels the Climate descriptor "Earth."

## Judgment scale semantics (pp. 3–4, verified)

- 7-point Likert scale, −3 to +3, one judgment per (cause descriptor state → effect descriptor state) pair, assessed for the year 2040.
- Positive = "promoting" influence; negative = "inhibitory" influence.
- **Greater magnitude represents greater judgment confidence** (3 vs 2, −3 vs −2) — not effect size.
- **Balance constraint**: a descriptor state's judged impacts on another descriptor's states must sum to zero ("balance of confidence").
- **Zero** means any of: little/no influence; promoting and inhibitory influences largely counter-balance; or "uncertainty made an accurate judgment about the state's likely degree and direction of influence impossible."

## Method (p. 4, verified)

- Cross-impact balance (CIB) analysis run in **ScenarioWizard**.
- A scenario is **fully consistent** if, for every descriptor, the state the scenario most promotes (output) equals the scenario's input state.
- **Succession analysis** migrates each inconsistent scenario stepwise to its nearest fully consistent scenario; the count of migrating scenarios is the attractor's basin width (ScenarioWizard "weight"); "total impact score" measures basin depth / self-reinforcing stability.

## Results (pp. 5–7 and Appendix 3, verified)

- **11 fully consistent scenarios** out of 4.05M (p. 5).
- Figure (p. 5) labels: Illiberal Decline attractors = scenarios **1, 2, 3, 5, 6, 7, 8, 9, 10**; Mad Max attractor = scenario **4**; Hope attractor = scenario **11**. Prose (p. 6): "Nine are similar enough that we call them collectively 'Illiberal Decline.'"
- Basin sizes (p. 7 prose): Illiberal Decline absorbs "**over three million** of the model's 4 million inconsistent scenarios"; Mad Max "**about half a million**"; Hope "**only about ten thousand**" but with "a high total impact score, indicating that its basin is deep, with strong self-reinforcing stability."
- Appendix 3 excerpt (p. 12), **Scenario No. 4 (Mad Max)**: Weight **539,844**; Consistency value 1; Total impact score **116**. States: Polity Type = Nonocracy; World Order = International fragmentation; Conflict & Security = Widespread non-state violence; IT = Limited rollout; Economy = Unmanaged economic failure; Health = High burden of disease; Food = Failed global industrial production; Energy = Low-carbon energy contraction; Transportation = Fragmented and failing; Earth (Climate) = 2.5–4°C; Inequality = High intl/high domestic.
- Also visible on p. 12: Scenario No. 5 weight 189,685 (total impact score 62); Scenario No. 6 weight 102,994 (total impact score 60) — both Illiberal Decline members.

## Openness and caveats (pp. 7–8, verified)

- No probabilities assigned; coarse-grained by design ("crude look at the whole"); 2040 endpoint.
- Team is writing a codebook and per-descriptor papers; "the matrix itself, when released, will include documented justifications of all influence judgments."
- "The PCM will therefore be an 'open' model: anyone will be able to access the matrix online, enter their own judgments, and use ScenarioWizard to see how their results differ from ours, and to perform sensitivity testing."

## Not verified / not in the pages read

- **Scenario 11 (Hope) exact weight and total impact score** — its Appendix 3 entry was not on the pages read; only the p. 7 prose ("about ten thousand," "high total impact score") is verified.
- **Exact combined Illiberal Decline basin weight** — only the "over three million" prose figure.
- Appendix 2 (full matrix, p. 10) is rendered too small to read cell values; individual judgment scores other than the p. 3 example block (Polity Type ↔ World Order) are unverified.
