---
title: State Entities
type: note
permalink: methodology/reference/state-entities
tags:
- methodology
- reference
- state
- entities
- countries
- aggregates
---

# State Entities

## The 40 Countries and 12 Regional Aggregates

**Document Version:** 2.0  
**Date:** December 2025  
**Status:** Design specification (pre-implementation)

**Parent document:** [[methodology/reference/state-overview]]

---

## Overview

The simulation models 40 individual countries plus 12 regional aggregates, capturing 92% of world population and GDP. This document specifies which entities are modeled and why.

**Selection criteria:**
- Capture 85%+ of world GDP
- Capture 74%+ of world population
- Include all nuclear states (9 of 9)
- Include all major regional powers
- Include key strategic chokepoints and nodes

---

## The 40 Countries

### North America (3)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **United States** | 340 | 28.0 | Global hegemon, reserve currency issuer, NATO anchor |
| **Canada** | 40 | 2.1 | G7, climate refuge potential, US economic integration |
| **Mexico** | 130 | 1.8 | US migration pressure, nearshoring destination, G20 |

### Europe (8)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Germany** | 84 | 4.5 | EU anchor, industrial economy, energy transition leader |
| **United Kingdom** | 68 | 3.5 | Nuclear state, financial center, post-Brexit trajectory |
| **France** | 68 | 3.0 | Nuclear state, EU co-leader, African ties |
| **Italy** | 59 | 2.3 | G7, EU fiscal stress case, Mediterranean migration |
| **Spain** | 48 | 1.6 | Mediterranean economy, Latin American ties |
| **Netherlands** | 18 | 1.1 | Trade hub, below sea level (climate), EU core |
| **Poland** | 38 | 0.8 | Largest Eastern EU member, NATO frontline, demographic stress |
| **Ukraine** | 37 | 0.2 | Active conflict zone, European security pivot, grain exporter |

### East Asia (5)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **China** | 1,425 | 18.0 | Primary US rival, demographic crisis, BRICS anchor |
| **Japan** | 124 | 4.2 | G7, demographic pioneer, US ally, China neighbor |
| **South Korea** | 52 | 1.7 | Extreme low fertility, semiconductor producer, divided peninsula |
| **Taiwan** | 24 | 0.8 | Semiconductor chokepoint (TSMC), most likely great power flashpoint |
| **North Korea** | 26 | 0.03 | Nuclear state, Korean peninsula wildcard, potential collapse |

### South Asia (3)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **India** | 1,440 | 3.9 | Largest population, demographic dividend, BRICS, non-aligned rising power |
| **Pakistan** | 240 | 0.4 | Nuclear state, climate-fragile, India rival, Afghan border |
| **Bangladesh** | 175 | 0.5 | Climate existential risk (sea level), garment economy, density extreme |

### Southeast Asia (5)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Indonesia** | 280 | 1.4 | Largest SE Asian economy, archipelagic, BRICS, G20 |
| **Vietnam** | 100 | 0.4 | Manufacturing growth, China alternative, BRICS partner |
| **Thailand** | 72 | 0.5 | Regional hub, aging demographics, BRICS partner |
| **Philippines** | 117 | 0.5 | US ally, South China Sea claimant, remittance dependent |
| **Singapore** | 6 | 0.5 | Financial hub, Malacca Strait chokepoint, ASEAN anchor |

### Central Asia (1)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Kazakhstan** | 20 | 0.3 | Central Asian anchor, Russia-China buffer, energy exporter, BRICS partner |

### West/Central Asia (2)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Iran** | 90 | 0.4 | Nuclear threshold state, BRICS, sanctions case, regional power |
| **Turkey** | 85 | 1.1 | NATO member, regional power, migration gateway, BRICS aspirant |

### Middle East (4)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Saudi Arabia** | 36 | 1.1 | OPEC leader, petrodollar anchor, BRICS, de-dollarization actor |
| **Egypt** | 105 | 0.4 | Largest Arab state, Suez Canal, Nile dependent, BRICS |
| **Israel** | 9 | 0.5 | Nuclear state, regional flashpoint, US ally |
| **UAE** | 10 | 0.5 | Financial hub, logistics center, remittance source, BRICS |

### Sub-Saharan Africa (5)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Nigeria** | 230 | 0.5 | Largest African population, oil producer, demographic giant |
| **Ethiopia** | 126 | 0.15 | BRICS, Nile upstream, East African anchor, high fragility |
| **DR Congo** | 100 | 0.07 | Critical minerals, chronic instability, population giant |
| **South Africa** | 60 | 0.4 | BRICS, only industrialized African economy, regional anchor |
| **Kenya** | 55 | 0.1 | East African economic hub, regional stabilizer |

### Latin America (2)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Brazil** | 215 | 2.2 | BRICS founder, Amazon custodian, regional anchor, G20 |
| **Argentina** | 46 | 0.6 | G20, chronic crisis case, Southern Cone anchor |

### Oceania (1)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Australia** | 26 | 1.7 | G20, US ally, Pacific anchor, climate refuge potential |

### Eurasia (1)

| Country | Pop (M) | GDP ($T) | Strategic Role |
|---------|---------|----------|----------------|
| **Russia** | 144 | 2.0 | Nuclear superpower, energy exporter, BRICS, Ukraine conflict |

---

## Regional Aggregates

For areas not covered by the 40 individual countries, regional aggregates track population, economic activity, and humanitarian outcomes.

### Tier 1 Aggregates (Full Variable Treatment)

These aggregates are populous enough or strategically important enough to require demographic structure and economic detail comparable to individual countries. They track the same ~55-60 variables as individual countries.

| Aggregate | Member Countries | Pop (M) | GDP ($B) | Rationale |
|-----------|------------------|---------|----------|-----------|
| **Gulf States** | Kuwait, Qatar, Bahrain, Oman | 15 | 500 | Remittance source, energy, UAE spillover |
| **Central America** | Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica, Panama | 55 | 400 | US migration pressure, humanitarian outcomes |
| **Sahel** | Mali, Niger, Burkina Faso, Chad, Mauritania, Senegal | 100 | 150 | Highest-risk humanitarian zone |
| **East Africa** | Tanzania, Uganda, Somalia, Sudan, South Sudan, Rwanda, Burundi, Eritrea | 200 | 300 | Climate displacement, fragility cluster |
| **Rest of EU** | Belgium, Austria, Sweden, Denmark, Finland, Ireland, Portugal, Greece, Czechia, Romania, Hungary, Slovakia, Bulgaria, Croatia, Slovenia, Lithuania, Latvia, Estonia, Luxembourg, Malta, Cyprus | 130 | 3,000 | EU fiscal/political dynamics |
| **Levant/Iraq** | Iraq, Syria, Jordan, Lebanon | 75 | 300 | Ongoing instability, refugee dynamics |

**Tier 1 total: 6 aggregates, ~575M population, ~$4.65T GDP**

### Tier 2 Aggregates (Simplified Treatment)

These aggregates track population, GDP, and key stress indicators but not full demographic structure. They track approximately 20 core variables.

| Aggregate | Member Countries | Pop (M) | GDP ($B) | Primary Purpose |
|-----------|------------------|---------|----------|-----------------|
| **Central Asia (other)** | Uzbekistan, Tajikistan, Kyrgyzstan, Turkmenistan | 60 | 150 | Water crisis, spillover from Kazakhstan |
| **Southeast Asia (other)** | Myanmar, Malaysia, Cambodia, Laos | 100 | 700 | Regional contagion, ASEAN dynamics |
| **Andean/Caribbean** | Colombia, Peru, Chile, Venezuela, Ecuador, Bolivia, Caribbean states | 180 | 1,200 | Venezuela spillover, regional economics |
| **Maghreb** | Morocco, Algeria, Tunisia, Libya | 110 | 500 | EU migration transit, gas supply |
| **Southern Africa (other)** | Zimbabwe, Zambia, Mozambique, Angola, Botswana, Namibia, Malawi, others | 150 | 400 | South Africa spillover, climate |
| **West/Central Africa (other)** | Ghana, Côte d'Ivoire, Cameroon, others (ex-Nigeria, Ethiopia, DRC) | 300 | 600 | Demographics, climate, fragility |

**Tier 2 total: 6 aggregates, ~900M population, ~$3.55T GDP**

---

## Coverage Summary

| Category | Count | Population (M) | % World | GDP ($T) | % World |
|----------|-------|----------------|---------|----------|---------|
| Individual Countries | 40 | 5,900 | 74% | 89 | 85% |
| Tier 1 Aggregates | 6 | 575 | 7% | 4.7 | 4% |
| Tier 2 Aggregates | 6 | 900 | 11% | 3.5 | 3% |
| **Model Total** | **52** | **7,375** | **92%** | **97.2** | **92%** |
| Unmodeled Remainder | — | 625 | 8% | 8 | 8% |

---

## Entity Classification by Membership

### Nuclear States (9)

All nuclear-armed states are individually modeled:

| Country | Nuclear Status |
|---------|----------------|
| United States | Possessed |
| Russia | Possessed |
| China | Possessed |
| United Kingdom | Possessed |
| France | Possessed |
| India | Possessed |
| Pakistan | Possessed |
| Israel | Possessed (undeclared) |
| North Korea | Possessed |

**Threshold states** (may acquire during simulation):
- Iran (individually modeled)
- Saudi Arabia (individually modeled)

### G7 Members (7)

All G7 members are individually modeled:
- United States, Canada, United Kingdom, France, Germany, Italy, Japan

### G20 Members (19 countries)

All G20 country members are individually modeled:
- G7 (7) + Argentina, Australia, Brazil, China, India, Indonesia, Mexico, Russia, Saudi Arabia, South Africa, South Korea, Turkey

(EU is a G20 member but not a country; represented via individual European countries + Rest of EU aggregate)

### BRICS+ Members (10)

All BRICS+ members (2024 expansion) are individually modeled:
- Original BRICS: Brazil, Russia, India, China, South Africa
- 2024 additions: Egypt, Ethiopia, Iran, Saudi Arabia, UAE

### UN Security Council Permanent Members (5)

All P5 members are individually modeled:
- United States, Russia, China, United Kingdom, France

---

## Regional Groupings for Analysis

For output aggregation and regional analysis, entities group as follows:

| Region | Individual Countries | Aggregates |
|--------|---------------------|------------|
| **North America** | US, Canada, Mexico | — |
| **Europe** | Germany, UK, France, Italy, Spain, Netherlands, Poland, Ukraine | Rest of EU |
| **East Asia** | China, Japan, South Korea, Taiwan, North Korea | — |
| **South Asia** | India, Pakistan, Bangladesh | — |
| **Southeast Asia** | Indonesia, Vietnam, Thailand, Philippines, Singapore | Southeast Asia (other) |
| **Central Asia** | Kazakhstan | Central Asia (other) |
| **Middle East** | Iran, Turkey, Saudi Arabia, Egypt, Israel, UAE | Gulf States, Levant/Iraq |
| **North Africa** | Egypt | Maghreb |
| **Sub-Saharan Africa** | Nigeria, Ethiopia, DRC, South Africa, Kenya | Sahel, East Africa, Southern Africa (other), West/Central Africa (other) |
| **Latin America** | Brazil, Argentina | Central America, Andean/Caribbean |
| **Oceania** | Australia | — |
| **Eurasia** | Russia | — |

---

## Variable Treatment by Entity Type

| Entity Type | Count | Variables | Notes |
|-------------|-------|-----------|-------|
| Individual Country | 40 | ~55-60 | Full demographic, economic, political, climate, strategic |
| Tier 1 Aggregate | 6 | ~55-60 | Same as countries; aggregated from member states |
| Tier 2 Aggregate | 6 | ~20 | Core demographics (4 cohorts), GDP, growth, key stress indicators |

See [[methodology/reference/state-variables-country]] for the full variable catalog and Tier 1/Tier 2 differentiation.

---

## Notes on Entity Selection

### Why These 40 Countries?

The selection balances several criteria:

1. **Economic weight**: Top economies by GDP
2. **Population**: Major demographic centers
3. **Strategic importance**: Nuclear states, chokepoints, regional anchors
4. **Crisis potential**: Fragile states with global spillover risk
5. **Geopolitical alignment**: Representatives of major blocs and non-aligned states

### Why Regional Aggregates?

Some regions matter for the simulation but don't warrant individual country modeling:

- **Humanitarian outcomes**: Sahel, East Africa experience crises affecting millions but individual countries are too small to model separately
- **Spillover dynamics**: Central America migration affects US; Maghreb affects Europe
- **Completeness**: Rest of EU captures remaining European dynamics

### What's Not Modeled?

The unmodeled 8% of world population/GDP includes:
- Small island states
- Remaining small European states (non-EU)
- Remaining small African states
- Remaining small Asian states

These are assumed to follow regional trends without individual dynamics. If sensitivity analysis reveals gaps, entities can be added.

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 2025 | Initial specification (within state-specification) |
| 2.0 | December 2025 | Extracted to standalone document; added membership tables |

---

*For variable specifications, see [[methodology/reference/state-variables-country]] and [[methodology/reference/state-variables-global]].*