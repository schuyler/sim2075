---
title: public-landscape-survey
type: research-input
permalink: strategy/inputs/public-landscape-survey
tags:
- strategy
- research
- landscape
---

# Public Landscape Survey: Long-Range Probabilistic Geopolitical Forecasting & Simulation (as of mid-2026)

*Research subagent report, July 10, 2026. Compiled to situate sim2075 (Monte Carlo simulation of geopolitical trajectories to 2075; ~30 correlated discontinuity events, 12-factor Gaussian-copula latent model, 4-type causal typology, bidirectional state-event coupling, explicit tractability boundaries).*

---

## 1. Academic / institutional world models

### International Futures (IFs) — Pardee Institute, Univ. of Denver
- **What**: Open-source integrated deterministic model, 186 countries to 2100; dynamically linked submodels (demographics, economy, energy, agriculture, health, education, governance, international politics). Powers UNDP SDG work and past NIC Global Trends editions. Active.
- **vs sim2075**: The strongest public analog for *scope* (country-level, multi-decade, cross-domain coupling), but it is a trend-extrapolation machine: no stochastic discontinuities, no Monte Carlo, no event correlation, no durability model. Scenarios are hand-built parameter variants. Its epistemology is "calibrated to data," not "documented judgment."

### IIASA / Integrated Assessment Models (MESSAGE, SSP framework)
- **What**: The SSP scenario database was updated in 2025 (new GDP/population projections), with updated IAM quantifications due in 2026. Horizon 2100.
- **vs sim2075**: Deterministic pathways; the literature itself (e.g., arXiv 2512.06026 on extending IAMs to 2150; arXiv 2511.00378 on IAM uncertainty) flags that IAMs assume continuous growth, treat tipping points poorly, and lack discontinuity mechanics. No geopolitical events at all. Active, heavily resourced, but structurally incapable of what sim2075 does.

### World3 descendants — Earth4All / recalibrations
- **What**: Earth4All (Club of Rome, ongoing; "Earth for All: Germany" published Oct 2024) adds regional resolution and a social-tension index to a World3-lineage system-dynamics model; two hand-authored scenarios ("Too Little Too Late," "Giant Leap"). Nebel et al. 2024 (*Journal of Industrial Ecology*) recalibrated World3 to 50 years of data. Active.
- **vs sim2075**: Continuous system dynamics, no discrete events, no probability, no countries. Collapse emerges from stock-flow feedback, not from a shock catalog.

### PRIO long-range conflict projections (Hegre et al.)
- **What**: The one academic lineage that does *probabilistic multi-decade* conflict simulation: Hegre et al. 2013 (*ISQ*) projected armed conflict to 2050 via dynamic multinomial simulation of country conflict-state transitions; Hegre et al. 2016 (*ERL*) extended this along the SSPs to 2100. Mostly dormant as a research line since ViEWS absorbed the effort into short horizons.
- **vs sim2075**: Closest academic precedent for country-level stochastic trajectory simulation, but single-domain (civil conflict only), covariate-driven (no event catalog, no cross-domain correlation), and impact-free (predicts incidence, not consequences).

## 2. Conflict forecasting (short-horizon, empirical)

### ViEWS (Uppsala + PRIO)
- **What**: ML-driven monthly forecasts of state-based violence 1–36 months ahead, country- and grid-month level; latest release covers May 2026–April 2029; 2026 headline forecasts published (Ukraine, Palestine/Israel, Sudan, Pakistan, Nigeria deadliest). Kluz Prize winner. Very active.
- **vs sim2075**: Empirical, validated, and short-horizon. No structural model of *why*, no cross-domain events (no financial crises, no climate tipping), no correlation structure beyond learned features, horizon two orders of magnitude shorter.

### ACLED CAST
- **What**: Hierarchical random-forest/XGBoost forecasts of political-violence event counts, six 4-week periods ahead, every country; public pipeline on GitHub (ACLED/cast-public). Active.
- **vs sim2075**: Same story as ViEWS, even shorter horizon.

### ICEWS → POLECAT (US government lineage)
- **What**: ICEWS discontinued April 11, 2023; successor POLECAT (PLOVER ontology) provides hourly-updated, weekly-posted global event data from 2018, hosted on Harvard Dataverse. It is a *data* program; the forecasting layer is now mostly academic papers built on top.
- **vs sim2075**: Event *detection*, not event *simulation*. No forward structural model.

## 3. Judgmental forecasting

### Metaculus
- **What**: Active; runs long-range question series (including extinction/catastrophe questions to 2100), quarterly AI Forecasting Benchmark tournaments, and FutureEval (AI-agent prediction benchmark spanning geopolitics). Pro human forecasters still beat bots each quarter as of 2025–26, but by shrinking margins.
- **vs sim2075**: Produces *marginal* probabilities on individually resolvable questions. No joint distribution, no correlation structure, no state variables, no impact/durability modeling. Long-range questions are unresolvable and known to be poorly incentivized.

### Good Judgment Inc / Superforecasters
- **What**: Active (Economist "World Ahead 2026" forecasts; FutureFirst subscription product; ~180 superforecasters). Horizons mostly ≤ 2 years.
- **vs sim2075**: Same marginal-probability limitation; commercial, closed.

### Forecasting Research Institute (Tetlock)
- **What**: The Existential Risk Persuasion Tournament (XPT, 2022; results in *International Journal of Forecasting* 41(2), 2025) elicited catastrophe/extinction probabilities to 2100: median expert 20% catastrophe / 6% extinction; median superforecaster 9% / 1%. Follow-ups: "Assessing Near-Term Accuracy in the XPT" (Sep 2025), "Can Humanity Achieve a Century of Nuclear Peace?" (Oct 2024). Also runs ForecastBench for LLMs. Very active.
- **vs sim2075**: This is the best public source of *calibratable priors for sim2075's event probabilities* — but it produces isolated numbers with documented irreducible expert/generalist disagreement, not a generative model. Notably, XPT's finding that four months of incentivized debate moved nobody is empirical support for sim2075's "tractability boundary" stance.

### Samotsvety
- **What**: Small elite group publishing ad hoc estimates (nuclear risk in the Ukraine war, AGI timelines: 32% by 2042, 73% by 2100; AI x-risk ≥5–10% by 2070). Sporadically active.
- **vs sim2075**: Same category: point marginals, no structure.

## 4. Scenario planning

### NIC Global Trends
- **What**: Global Trends 2040 (2021): structural forces → dynamics → five qualitative scenarios. Quadrennial; **no eighth edition surfaced in public searches as of mid-2026** — status of the next edition is unclear.
- **vs sim2075**: Qualitative narratives; the "Tragedy and Mobilization" scenario is the only one built on discontinuities. No probabilities, no simulation. Used IFs for its quantitative backbone historically.

### RAND — Robust Decision Making (RDM) / exploratory modeling
- **What**: RAND's RDM generates thousands of model runs across plausible futures and uses scenario discovery to find policy vulnerabilities. Active, mostly applied to climate/infrastructure/defense planning.
- **vs sim2075**: Methodologically the closest *philosophy* in the policy world ("many runs, structural discovery, not point prediction" — the same output framing as sim2075). But RDM is deliberately **non-probabilistic** (deep uncertainty doctrine rejects assigning probabilities), decision-centric rather than world-generative, and no RAND product stochastically generates correlated geopolitical discontinuities. RAND's wargaming shop is separate and non-quantitative.

### Shell scenarios
- **What**: Active (Energy Security Scenarios, Sky 2050). Qualitative narratives quantified through energy-system models.
- **vs sim2075**: Two-to-three hand-authored futures; no probability, no events.

### Cascade Institute — Polycrisis Core Model (the closest public relative)
- **What**: PCM v2.5 (technical synopsis, Aug 10–11, 2025; Homer-Dixon, Lawrence, Kemp, Schweizer et al.). Cross-impact balance (CIB) analysis over 11 global "descriptors" with 45 states (~4.05M combinations), driven by 1,800+ documented expert judgments on a −3..+3 scale; finds 11 fully consistent 2040 scenarios collapsing into three attractors: "Illiberal Decline" (~3M scenarios' basin), "Mad Max" (~500K), "Hope" (~10K). Plans an open model: published matrix, documented justification for every judgment, ScenarioWizard-reproducible. Companion work: "Global Systemic Stresses" report (Nov 2025) with a **Stress–Trigger–Crisis** model (14 slow stresses, fast triggers, 9 vital systems); Gambhir et al., "A systemic risk assessment methodological framework for the global polycrisis," *Nature Communications* (2025). Very active and well-funded.
- **vs sim2075**: Deep kinship in epistemology — parameters as documented, publicly criticizable judgments; explicit rejection of falsely precise IAM/system-dynamics parameterization. But the methods are almost perfectly complementary rather than overlapping: CIB is **static equilibrium analysis** (which world-states are self-consistent in 2040), with *no time dynamics, no probabilities, no event catalog, no durability, no Monte Carlo, no country resolution* (global-aggregate descriptors only). Their Stress–Trigger–Crisis distinction is a 2-category cousin of sim2075's 4-type causal typology, but is conceptual, not operationalized in the model.

## 5. Catastrophe modeling industry

### Verisk (AIR/Extreme Event Solutions + Maplecroft)
- **What**: April 2025: first-of-its-kind **SRCC (Strikes, Riots, Civil Commotion) catastrophe model for the US** — a 500,000-year stochastic event catalog of civil unrest at ZIP-code level, driven by social/economic/political factors. This is the first public transplant of cat-model machinery (stochastic catalogs, frequency-severity) into political violence. Active, commercial.
- **vs sim2075**: One peril, one country, insurance-loss impact metric only, ~1-year effective horizon. No cross-domain correlation, no state feedback. But it validates the core sim2075 move: geopolitical events *can* be treated with event-catalog mechanics.

### Lloyd's / Cambridge Centre for Risk Studies systemic risk scenarios
- **What**: Nine hypothetical systemic scenarios (geopolitical conflict, pandemic, cyber, extreme weather, economic stagnation…) each at three severities across 107 countries; the 2024 geopolitical-conflict scenario priced at $14.5T global GDP loss over 5 years ($7.8T–$50T range). Cambridge also maintains the Global Risk Index (expected GDP@Risk by city/threat). Active.
- **vs sim2075**: Deterministic scenario suites with severity tiers — no Monte Carlo over correlated events, no dynamics, no recovery/durability modeling beyond a 5-year loss window. Impact metric is GDP only.
- **General industry note**: Copula-based tail-dependence modeling is standard in reinsurance loss aggregation (e.g., copula-POT cat-bond pricing, arXiv 2302.00462), but is applied to *perils and portfolios*, never to a multi-decade world model. Swiss Re's SONAR is a qualitative emerging-risk radar. **Nobody in the public cat-model space runs a correlated, multi-domain, 50-year geopolitical event catalog.**

## 6. LLM-based geopolitical simulation/forecasting (2024–2026)

- **Wargaming/agent sims**: Lamparth et al., "Human vs. Machine: Behavioral Differences Between Expert Humans and LLMs in Wargame Simulations" (arXiv 2403.03407, 2024); "Open-Ended Wargames with LLMs" (arXiv 2404.11446, 2024); Fable Studio/OpenAI "SIM-1" multi-agent conflict sims; "LLMs as Strategic Actors" (arXiv 2603.02128, 2026); "Red Lines and Grey Zones in the Fog of War" (arXiv 2510.03514, 2025). These study LLM *behavior as actors* in single scenarios — role-play, not probabilistic trajectory generation.
- **Forecasting bots**: Metaculus quarterly AI Benchmark tournaments (bots still trail Pros as of Q2 2025 results but close fast); FutureSearch (commercial, #1 of 163 on Metaculus FutureEval, competitive with superforecasters on ForecastBench); "LLM4Geopolitics" (*Expert Systems*, 2026) — RAG + knowledge-graph event prediction. All short-horizon question-answering.
- **Hobbyist multi-actor pipelines**: e.g., danielrosehill/Geopol-Modeller and Geopol-Forecaster on GitHub (~40 LLM actors, 4 timesteps, "LLM council" producing calibrated probabilistic forecasts). Small scale, weeks-to-months horizon.
- **vs sim2075**: An entire field has appeared since 2024, but it splits into (a) actors-in-a-scenario and (b) question-level forecasters. Nobody publicly combines LLMs with a *structured Monte Carlo world model*. The obvious near-future convergence — LLMs eliciting/updating parameters for a structural simulation — appears unoccupied.

## 7. Cross-impact analysis / probabilistic scenario generation literature

- **CIB** (Weimer-Jehle 2006, *TFSC*; Springer monograph *Cross-Impact Balances (CIB) for Scenario Analysis*, 2023; ScenarioWizard software): the dominant modern method; deliberately **non-probabilistic** (consistency, not likelihood). Cascade's PCM is its flagship application.
- **Classic probabilistic cross-impact** (Gordon & Helmer 1966; Turoff 1971): did use conditional event probabilities and Monte Carlo, but the lineage largely died out due to elicitation burden and incoherence problems — sim2075's latent-factor copula is arguably the modern fix for exactly the problem that killed this literature.
- **Bayesian networks for geopolitical/country risk**: scattered papers (country-risk BNs, dynamic BNs for conflict), no sustained global-scale program found.
- **Undheim & Ahmad, "Quantitative scenarios for cascading risks in AI, climate, synthetic bio, and financial markets by 2075"** (*Frontiers in Complex Systems*, Mar 2024) — the single nearest neighbor by title and horizon: 19 indicators, CAGR extrapolation, five hand-built scenarios, cascade "multipliers" of 1.1–1.3x for co-occurring catastrophes. **No Monte Carlo, no probabilities, no correlation model, no durability structure.** Its headline finding (co-occurring catastrophes prevent the ~25-year single-catastrophe recovery pattern) is essentially a low-resolution version of what sim2075's copula + durability machinery is built to explore rigorously. Authors themselves call the field "methodological chaos" and say a serious version needs 10–1000x more indicators.
- Also relevant: "Systemic contributions to global catastrophic risk" (*Global Sustainability*, Cambridge) — the "synchronous failure" archetypes (long-fuse-big-bang / simultaneous stresses / ramifying cascade) are a qualitative taxonomy that sim2075's Type 1–4 typology operationalizes.

---

## Assessment

### (a) Genuinely novel or rare in the public space
1. **The combination itself**: no public project unites (event catalog × correlated sampling × state feedback × multi-decade horizon × country resolution). Every component exists somewhere; the assembly exists nowhere found.
2. **Copula/latent-factor correlation of heterogeneous geopolitical discontinuities**: cat modelers use copulas for perils; Verisk (2025) proved event catalogs work for political violence; nobody applies the technique across state failure + climate tipping + finance + pandemics + tech over 50 years. This is the clearest "cat model for geopolitics" gap.
3. **The 4-type causal typology, operationalized**: Cascade's Stress–Trigger–Crisis and the "synchronous failure" archetypes are conceptual cousins, but no public model assigns events different *generating mechanisms* (base-rate vs threshold vs small-N-contingent vs S-curve) with distinct math.
4. **Impact durability modeling**: essentially absent everywhere. Lloyd's prices 5-year GDP windows; Undheim & Ahmad note the 25-year recovery pattern but model it crudely; no one carries per-event recovery structure through a simulation.
5. **Declared intractability boundaries**: sim2075's explicit "Small-N Actor Problem → shift effort to conditional aftermaths" stance is rare. The XPT's finding of immovable expert disagreement is empirical evidence *for* it, and RAND's deep-uncertainty doctrine gestures at it, but no simulation project found writes its epistemic limits into the model architecture. Cascade's documented-judgment transparency is the closest kin (their zeros even encode "uncertainty made judgment impossible").

### (b) Well-covered elsewhere — don't compete here
- **Trend projection depth**: IFs and the IAM ecosystem have hundreds of person-years of empirical calibration on demographics/economy/energy. sim2075's Type-4 S-curves should borrow from, not rival, them.
- **Short-horizon conflict prediction**: ViEWS/CAST own the 1–36-month space with validated ML. Nothing sim2075 does should claim near-term predictive skill.
- **Single-event probability elicitation**: Metaculus/FRI/GJ/Samotsvety are better sources of marginals than any solo judgment; sim2075's annual probabilities should cite and reconcile with XPT-class numbers where they exist.
- **Qualitative narrative scenarios**: NIC/Shell/Cambridge-Lloyd's saturate this.
- **Static consistency/attractor analysis of global futures**: Cascade's PCM now owns this publicly, with a large team and open-model plans.

### (c) Plausible niches for an independent project
1. **The dynamic complement to Cascade's PCM**: PCM finds *where the attractors are* in 2040; sim2075 generates *trajectories, timing, and probability mass* to 2075. Same epistemology (documented judgments, open matrix/parameters), disjoint methods. This is the most natural publication frame and a concrete collaboration/critique target — their team (Homer-Dixon, Kemp, Schweizer) is the audience most likely to engage seriously.
2. **Methodology contribution**: "Catastrophe-modeling techniques for the polycrisis" — reviving probabilistic cross-impact (the dead Gordon–Helmer lineage) with latent-factor copulas as the coherence fix is a publishable methods paper (*Futures*, *Global Sustainability*, *Risk Analysis*, *Technological Forecasting & Social Change*; Gambhir et al.'s 2025 *Nature Communications* framework paper shows appetite).
3. **Open tooling**: no open-source correlated-discontinuity scenario generator exists (GitHub searches confirm: finance Monte Carlo and LLM role-play, nothing structural). A documented, forkable engine where users edit the event catalog and factor loadings would be a genuine public good — the "ScenarioWizard for dynamic probabilistic futures."
4. **Elicitation substrate**: parameters-as-documented-judgments makes the model a natural target for crowd/superforecaster/LLM elicitation (Metaculus-style questions resolving *model parameters* rather than world events), and separately a testbed for the unoccupied "LLM + structural world model" convergence.
5. **Honest caveat**: classified and proprietary analogs (IC internal work post-ICEWS, hedge-fund world models, reinsurer internal scenario engines) plausibly exist unpublished; novelty claims should be scoped to "public space."

**Bottom line**: sim2075's individual ingredients each have public precedent, but its architecture — correlated discontinuities with durability and feedback over a 50-year horizon, wrapped in an explicit intractability-aware epistemology — has no public equivalent as of mid-2026. Its nearest relatives are Cascade's PCM (shared epistemology, static method), Verisk's SRCC model (shared technique, tiny scope), and Undheim & Ahmad 2024 (shared question and horizon, far cruder machinery). The gap between those three points is exactly where sim2075 sits.

## Sources

[Pardee/IFs](https://korbel.du.edu/pardee/international-futures-platform/) · [IIASA SSP](https://iiasa.ac.at/models-tools-data/ssp) · [Earth4All](https://earth4all.life/the-science/) · [Nebel et al. 2024](https://onlinelibrary.wiley.com/doi/10.1111/jiec.13442) · [ViEWS](https://viewsforecasting.org/) · [ViEWS 2026 forecasts](https://viewsforecasting.org/news/new-forecasts-of-the-deadliest-conflict-zones-in-2026/) · [ACLED CAST](https://acleddata.com/methodology/cast-methodology) · [POLECAT](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/AJGVIT) · [FRI XPT](https://forecastingresearch.org/research/existential-risk-persuasion-tournament) · [XPT in IJF 2025](https://www.sciencedirect.com/science/article/abs/pii/S0169207024001250) · [Samotsvety](https://samotsvety.org/blog/) · [Good Judgment](https://goodjudgment.com/) · [NIC GT2040](https://www.dni.gov/index.php/gt2040-home) · [RAND RDM](https://www.rand.org/pubs/research_briefs/RB9701.html) · [Cascade PCM](https://cascadeinstitute.org/polycrisis-core-model/) · [PCM v2.5 synopsis](https://cascadeinstitute.org/wp-content/uploads/2025/08/Cascade-Institute-Polycrisis-Core-Model-v2.5-technical-synopsis-of-results-Aug-11-2025.pdf) · [Global Systemic Stresses](https://cascadeinstitute.org/global-systemic-stresses/) · [Verisk SRCC](https://www.verisk.com/company/newsroom/verisk-unveils-first-of-its-kind-srcc-catastrophe-model-for-the-u.s.-to-quantify-political-violence-risks/) · [Lloyd's geopolitical scenario](https://www.lloyds.com/insights/media-centre/press-releases/geopolitical-conflict-scenario) · [Cambridge CRS](https://www.jbs.cam.ac.uk/centres/risk/) · [Metaculus FutureEval](https://www.metaculus.com/futureeval/) · [FutureSearch](https://futuresearch.ai/) · [Lamparth et al.](https://arxiv.org/pdf/2403.03407) · [SIM-1](https://fablestudio.github.io/openai-wargames/) · [LLM4Geopolitics](https://onlinelibrary.wiley.com/doi/10.1111/exsy.70258) · [CIB book](https://link.springer.com/book/10.1007/978-3-031-27230-1) · [Weimer-Jehle 2006](https://cross-impact.de/ressourcen/cib_weimer-jehle_2006.pdf) · [Undheim & Ahmad 2024](https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2024.1323321/full) · [Systemic contributions to GCR](https://www.cambridge.org/core/journals/global-sustainability/article/systemic-contributions-to-global-catastrophic-risk/C9DCBFE8C24F8CA1505F61DC61E9822B)
