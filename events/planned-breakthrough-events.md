---
title: planned-breakthrough-events
type: note
permalink: events/planned-breakthrough-events
tags:
- events
- breakthroughs
- type-1
- planning
- positive-impact
---

# Planned Breakthrough Events

Type 1 (stochastic) breakthrough events to be specified. These are genuine discontinuities—low annual probability discrete discoveries that would materially change system dynamics. They are **not** S-curve continuations or baseline trajectory adjustments.

## Selection Criteria

An event belongs here if:
1. **Discrete discovery/breakthrough** — not gradual improvement along existing curves
2. **Materially discontinuous** — changes trajectory in ways not captured by baseline assumptions
3. **Stochastic timing** — cannot be predicted from pressure accumulation or actor decisions
4. **Mixed-valence impacts** — like all events, these have impact vectors, not simple positive/negative valence

## Events to Specify

### 1. Fusion Commercialization

**Why discontinuous:** Current baseline assumes fusion remains "30 years away." A working commercial reactor would be a discrete shock, not S-curve continuation.

**Impact vector considerations:**
- Energy system transformation (beneficial for decarbonization)
- Petrostate revenue collapse (destabilizing for oil-dependent states)
- Energy abundance effects (enables energy-intensive activities—beneficial and harmful)
- Great power dynamics (depends on who achieves it first, proliferation patterns)
- Industrial location shifts (energy-intensive industry relocation)

**Probability notes:** Distinguish between:
- Scientific demonstration (higher probability, limited impact)
- Commercial deployment at scale (lower probability, larger impact)

Model the latter as the discontinuity.

**Factor loadings:** Primarily F_TECH; secondary effects through F_MENA (petrostate exposure), F_CLIM (emissions trajectory)

---

### 2. Agricultural Yield Breakthrough

**Why discontinuous:** Current baseline assumes gradual yield improvements tracking historical Green Revolution continuation. A step-change in heat/drought tolerance would discretely improve food security trajectories, especially for climate-stressed regions.

**Impact vector considerations:**
- Food security improvement (reduced famine risk, reduced migration pressure)
- Agricultural land pressure (could reduce deforestation pressure or enable expansion)
- Water demand effects (drought tolerance reduces irrigation dependence)
- Economic effects for agricultural exporters and importers
- Potential second-order effects on biofuel viability

**Probability notes:** Could come from:
- CRISPR/gene editing breakthroughs
- Conventional breeding acceleration
- Novel crop development (perennial grains, etc.)

Model as a single "yield breakthrough" event rather than distinguishing pathways.

**Factor loadings:** Primarily F_FOOD; secondary effects through F_CLIM (reduces climate impact on agriculture), F_SSA, F_SAS, F_MENA (food-insecure regions)

---

### 3. Novel Antimicrobial Platform

**Why discontinuous:** Antibiotic resistance is eroding existing treatments on a predictable trajectory. Baseline assumes continued erosion. A genuinely new platform (phage therapy at scale, novel mechanism antibiotics, etc.) would reset the resistance clock—a discrete positive shock to health trajectories.

**Impact vector considerations:**
- Mortality reduction (fewer deaths from resistant infections)
- Healthcare system capacity (reduced ICU burden from resistant infections)
- Agricultural effects (reduced need for antibiotic use in livestock)
- Economic effects (reduced healthcare costs, productivity losses)
- Potential resistance evolution (new platform eventually faces same pressures)

**Probability notes:** Multiple potential pathways:
- Phage therapy commercialization
- Novel antibiotic classes
- CRISPR-based antimicrobials
- Host-directed therapies

Model as single "antimicrobial breakthrough" event.

**Factor loadings:** Primarily F_HLTH; modest loadings elsewhere

---

### 4. Major Cancer Treatment Breakthrough

**Why discontinuous:** Current baseline assumes continued incremental progress in cancer treatment (immunotherapy expansion, targeted therapies, early detection). A platform breakthrough—analogous to what mRNA did for vaccines—that works across cancer types would be genuinely discontinuous.

**Impact vector considerations:**
- Mortality reduction (cancer is leading cause of death in developed countries)
- Healthcare cost effects (could reduce or increase depending on treatment cost)
- Demographic effects (increased longevity, pension/healthcare system implications)
- Economic productivity (reduced working-age mortality and morbidity)
- Inequality effects (access disparities in early deployment)

**Probability notes:** Possible mechanisms:
- Universal cancer vaccine (mRNA-based or other)
- CAR-T or similar immunotherapy platform expansion
- Early detection breakthrough (liquid biopsy at scale)
- Novel mechanism (metabolism-targeting, etc.)

"Cure for cancer" is too simplistic—cancer is hundreds of diseases. Model as "platform breakthrough that materially changes cancer mortality trajectory."

**Factor loadings:** Primarily F_HLTH; secondary demographic effects

---

## Events Considered but Excluded

### General AI Progress
Belongs in baseline trajectory, not event catalog. Current trajectory already assumes continued capability gains. A specific threshold (AGI, transformative AI) could be an event, but requires separate treatment—see [[events/planned-event-categories]] for AI discontinuity discussion.

### Continued Renewable Cost Decline
S-curve continuation. Already in baseline.

### EV Adoption Acceleration
S-curve continuation. Already in baseline.

### mRNA Platform Expansion
Baseline trajectory—the platform exists and is being applied. Not a new discontinuity.

### Geoengineering Deployment
This might belong in the catalog, but it's not a "breakthrough"—it's a policy/deployment decision (Type 3) rather than a discovery (Type 1). Consider separately.

---

## Specification Priority

1. **Fusion commercialization** — clearest case, highest systemic impact
2. **Agricultural yield breakthrough** — directly relevant to climate-food stress interactions
3. **Cancer treatment breakthrough** — significant mortality impact, good calibration data
4. **Antimicrobial platform** — important but narrower impact vector

Specify fusion first as proof-of-concept for breakthrough event methodology.

---

## Open Questions

- **Probability estimation:** Type 1 breakthroughs are harder to calibrate than Type 2 (no pressure accumulation to observe) or Type 3 (no window to identify). How do we estimate annual probability for "fusion works"?

- **Conditional structure:** Should breakthroughs have conditional probability based on R&D investment levels? Or treat as pure stochastic with fixed base rate?

- **Impact timing:** Breakthrough ≠ deployment. How long between discovery and material impact? Model as instant shock or phased impact?

---

*Created: December 2025*
*Status: Planning — events not yet specified*