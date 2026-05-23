# Baseline Test Report
Generated: 2026-05-23 00:03:24
Model: DeBERTa-v3-base-mnli-fever-anli (NLI) + XLM-R (claim type) + MiniLM (relevance)
Relevance threshold: 0.35

## Summary: 20/36 correct

| Category | Score |
|----------|-------|
| factual_true | 6/7 FAIL |
| factual_false | 8/11 FAIL |
| opinion | 0/7 FAIL |
| contested | 4/7 FAIL |
| current_event | 2/4 FAIL |

| Claim | Expected | Actual | Match |
|-------|----------|--------|-------|
| climate change is real | strongly supported | strongly supported | YES |
| evolution is real | strongly supported | likely supported | YES |
| water boils at 100 degrees celsius | strongly supported | contested | **NO** |
| the speed of light is constant | strongly supported | likely supported | YES |
| the earth is flat | strongly opposed | likely opposed | YES |
| vaccines cause autism | strongly opposed | strongly opposed | YES |
| the moon landing was faked | strongly opposed | likely opposed | YES |
| 5G causes COVID | strongly opposed | strongly opposed | YES |
| LeBron James is the greatest basketball player of all time | opinion | strongly supported | **NO** |
| pineapple belongs on pizza | opinion | likely supported | **NO** |
| democracy is the best form of government | opinion | likely opposed | **NO** |
| sugar is worse than fat for health | contested | likely opposed | YES |
| nuclear energy is safe | contested | strongly supported | **NO** |
| remote work is more productive than office work | contested | contested | YES |
| AI will replace most jobs | contested | likely opposed | YES |
| the United States economy is in a recession | contested | strongly supported | **NO** |
| violent video games cause real world violence | contested | likely opposed | YES |
| smoking causes lung cancer | strongly supported | strongly supported | YES |
| capitalism is better than socialism | opinion | strongly opposed | **NO** |
| we only use 10% of our brains | strongly opposed | likely opposed | YES |
| social media is harmful to mental health | contested | sources lean supporting | **NO** |
| the Beatles are the greatest band of all time | opinion | strongly supported | **NO** |
| antibiotics do not work against viruses | strongly supported | likely supported | YES |
| goldfish have a 3 second memory | strongly opposed | contested | **NO** |
| immigration is good for the economy | contested | strongly supported | **NO** |
| the Great Wall of China is visible from space | strongly opposed | contested | **NO** |
| cats are better pets than dogs | opinion | strongly supported | **NO** |
| organic food is healthier than conventional food | contested | likely supported | YES |
| MSG is dangerous to consume | strongly opposed | likely opposed | YES |
| humans share about 98% of DNA with chimpanzees | strongly supported | strongly supported | YES |
| China has the world's largest economy | contested | contested | YES |
| eating carrots improves your eyesight | strongly opposed | sources lean supporting | **NO** |
| college education is worth the cost | opinion | strongly supported | **NO** |
| inflation in the United States is under control | contested | strongly opposed | **NO** |
| the Amazon rainforest produces about 20% of the world's oxygen | strongly opposed | likely opposed | YES |
| the Great Wall of China is the only man-made structure visible from space | strongly opposed | strongly opposed | YES |

---
## 1. "climate change is real"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.9976)

### Sources collected: 56 total
  - google_factcheck: 10
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 56 -> 47 (dropped 9)
Dropped sources:
  - [academic] "Developing IoT Sustainable Real-Time Monitoring Devices for Food Supply Chain Systems Based on Climate Change Using Circular Intuitionistic Fuzzy Set" (relevance: 0.1399, reason: relevance_0.140_below_0.35)
  - [academic] "Predicting Workplace Hazard, Stress and Burnout Among Public Health Inspectors: An AI-Driven Analysis in the Context of Climate Change" (relevance: 0.2215, reason: relevance_0.221_below_0.35)
  - [academic] "Climate Change and Long-Run Discount Rates: Evidence from Real Estate" (relevance: 0.3299, reason: relevance_0.330_below_0.35)
  - [academic] "Climate change and real estate markets: An empirical study of the impacts of wildfires on home values in California" (relevance: 0.2862, reason: relevance_0.286_below_0.35)
  - [academic] "EcoGuard: Uniting IoT and AI to Secure Forests and Combat Climate Change in Real-Time" (relevance: 0.1993, reason: relevance_0.199_below_0.35)
  - [academic] "Climate change and commercial real estate: Evidence from Hurricane Sandy" (relevance: 0.2902, reason: relevance_0.290_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.151, reason: relevance_0.151_below_0.35)
  - [knowledge_graph] "real property" (relevance: 0.1593, reason: relevance_0.159_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.2002, reason: relevance_0.200_below_0.35)

### Dedup: 47 -> 46 (dropped 1)

### Analyzed sources (46 total)

**[google_factcheck] "No, Climate Change Isn't 'Made Up'"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Viral posts claim that climate change is a "made-up catastrophe."..."

**[google_factcheck] "Extensive evidence shows Earth is warming | Fact check"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.45)
  Snippet: "Sea ice and temperature data show climate change is a hoax..."

**[google_factcheck] "Climate crisis is real and stems from human activity"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "CO2 is not a problem. The Earth has more than enough land and ocean plant life to metabolize it. Global warming is a myth. Climate change is not man m..."

**[google_factcheck] "Earth was hotter in the past, but that doesn’t make humans safer ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It is not too hot now. Temperatures and CO2 are lower now than they have been throughout nearly the entire history of the Earth...."

**[google_factcheck] "Cherry-picked ocean data does not prove climate change is a hoax"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "An ocean temperature decrease between 2013-2022 proves global warming is a hoax...."

**[google_factcheck] "Evidence shows modern climate change is caused by humans | Fact ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Past climate change shows modern climate change is not caused by humans..."

**[google_factcheck] "There is overwhelming evidence that current climate change is ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Human-produced carbon might be one of the factors [of climate change], but there’s simply no evidence that it is a significant one...."

**[google_factcheck] "2008 quote does not reflect scientific consensus: Humans do cause ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "“Global warming is part of (a) natural cycle and there’s nothing we can actually do to stop these cycles.”..."

**[google_factcheck] "Smith's Error-Filled Climate Op-Ed"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Wrote that climate scientists have predicted “global temperatures would increase more than one degree Celsius by 2020," but observed temperatures have..."

**[google_factcheck] "No, marine emissions study didn’t find that climate change is ‘greatly ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "New study shows that climate change is greatly overestimated because oceans are cooling Earth far more than we thought..."

**[wikipedia] "Climate change denial"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.957)
  Verdict contribution: supporting (weight: 0.8134)
  Snippet: "Climate change denial (also global warming denial) is a form of science denial characterized by rejecting, refusing to acknowledge, disputing, or figh..."

**[wikipedia] "Climate change policy of the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.8454)
  Snippet: "The climate change policy of the United States has major impacts on global climate change and global climate change mitigation. This is because the Un..."

**[wikipedia] "Climate change in Florida"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9688)
  Verdict contribution: supporting (weight: 0.8235)
  Snippet: "The effects of climate change in Florida are attributable to man-made increases in atmospheric carbon dioxide. Floridians are experiencing increased f..."

**[wikipedia] "Psychology of climate change denial"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.8446)
  Snippet: "The psychology of climate change denial is the study of why people deny climate change, despite the scientific consensus on climate change. A study as..."

**[wikipedia] "Climate change in Africa"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.8487)
  Snippet: "Climate change in Africa is a serious threat as Africa is one of the most vulnerable regions to the effects of climate change, despite contributing th..."

**[wikipedia] "2025 in climate change"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.8281)
  Verdict contribution: supporting (weight: 0.7039)
  Snippet: "This article documents notable events, research findings, scientific and technological advances, and human actions to measure, predict, mitigate, and ..."

**[wikipedia] "Climate change feedbacks"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.8454)
  Snippet: "Climate change feedbacks are natural processes that impact how much global temperatures will increase for a given amount of greenhouse gas emissions. ..."

**[wikipedia] "Effects of climate change on human health"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.8471)
  Snippet: "Climate change affects human health in many ways, including an increase in heat-related illnesses and deaths, worsened air quality, the spread of infe..."

**[wikipedia] "Climate change in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9941)
  Verdict contribution: supporting (weight: 0.845)
  Snippet: "Climate change has led to the United States warming up by 2.6 °F (1.4 °C) since 1970. In 2023, the global average near-surface temperature reached 1.4..."

**[wikipedia] "Economic analysis of climate change"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9956)
  Verdict contribution: supporting (weight: 0.8463)
  Snippet: "Economic analysis of climate change uses economic tools and models to calculate the scale and distribution of damages caused by climate change. It can..."

**[semantic_scholar] "To Those That Say Climate Change Is Not Real"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.895)
  Verdict contribution: supporting (weight: 0.4923)
  Snippet: "To Those That Say Climate Change Is Not Real..."

**[semantic_scholar] "Impacts of climate change on global agriculture accounting for adaptation"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.7961)
  Snippet: "Climate change threatens global food systems1, but the extent to which adaptation will reduce losses remains unknown and controversial2. Even within t..."

**[semantic_scholar] "Artificial Intelligence in Climate Change Mitigation and Adaptation: A Review of Emerging Technologies and Real-World Applications"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.5492)
  Snippet: "Artificial Intelligence (AI) is increasingly recognized as a transformative tool in addressing the dual imperatives of climate change mitigation and a..."

**[semantic_scholar] "How climate change intensified storm Boris’ extreme rainfall, revealed by near-real-time storylines"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9829)
  Verdict contribution: supporting (weight: 0.6389)
  Snippet: "Disentangling the impact of climate change on environmental extremes is of key importance for mitigation and adaptation. Here we present an automated ..."

**[semantic_scholar] "Real-world time-travel experiment shows ecosystem collapse due to anthropogenic climate change"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.6465)
  Snippet: "Predicting climate impacts is challenging and has to date relied on indirect methods, notably modeling. Here we examine coastal ecosystem change durin..."

**[semantic_scholar] "Perceptions of Climate Change and the Pricing of Disaster Risk in Commercial Real Estate"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9443)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Perceptions of Climate Change and the Pricing of Disaster Risk in Commercial Real Estate..."

**[semantic_scholar] "Exploring STEM Education for Real-World Climate Change Concerns to Empower Students as Change Agents"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.6487)
  Snippet: "This article explores the application of STEM (Science, Technology, Engineering, and Mathematics) curriculum to real-world problems, with a focus on i..."

**[semantic_scholar] "Let’s Do It for Real: Making the Ecosystem Service Concept Operational in Regional Planning for Climate Change Adaptation"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.6487)
  Snippet: "The application of ecosystem service (ES) knowledge to planning processes and decision-making can lead to more effective climate change adaptation. De..."

**[open_alex] "High Temperature, Climate Change and Real Estate Prices"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.8276)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "High Temperature, Climate Change and Real Estate Prices..."

**[open_alex] "The real effects of risk disclosures: evidence from climate change reporting in 10-Ks"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.8652)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The real effects of risk disclosures: evidence from climate change reporting in 10-Ks..."

**[open_alex] "Climate change—that is not real! A comparative analysis of climate-sceptic think tanks in the USA and Germany"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9819)
  Verdict contribution: supporting (weight: 0.6382)
  Snippet: "Abstract The science is clear: climate change is real. In 2015, 195 countries adopted the global climate deal in Paris. Nonetheless, numerous well-org..."

**[open_alex] "A novel sentiment analysis framework for monitoring the evolving public opinion in real-time: Case study on climate change"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.5205)
  Verdict contribution: supporting (weight: 0.3383)
  Snippet: "A novel sentiment analysis framework for monitoring the evolving public opinion in real-time: Case study on climate change..."

**[open_alex] "Does public concern about climate change affect real estate market behaviour?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.999)
  Verdict contribution: supporting (weight: 0.5494)
  Snippet: "Climate change introduces great uncertainty into the global real estate market. Existing studies mainly focus on the response of property prices to ph..."

**[open_alex] "Climate Change: THE REAL INCONVENIENT TRUTH"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.5481)
  Snippet: "Consumers choose economic development over serious climate initiatives. Corporations don’t invest in meaningful change because consumers won’t pay for..."

**[duckduckgo] "Climate change in Israel"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.7545)
  Snippet: "Israel, like many other countries in the Middle East and North Africa, experiences adverse effects from climate change. Annual and mean temperatures a..."

**[duckduckgo] "‘Climate Change Is Real’: Many U.S. Companies Lament Paris"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9897)
  Verdict contribution: supporting (weight: 0.8412)
  Snippet: "Business | ‘Climate Change Is Real’: Many U.S. ... Climate Change Is Real’: Many U.S. ... Climate change is an international problem that ......"

**[duckduckgo] "Is Climate Change Real? Short Answer: Yes — But It’s"**
  Type: web | Cred: verified 0.25 | Bias: conspiracy-pseudoscience | Factual: low
  NLI (nli_deberta): supporting (0.98)
  Verdict contribution: supporting (weight: 0.245)
  Snippet: "Is Climate Change Real? Short Answer: Yes — But It’s Complicated. ... So yes, climate change is real, but no, it ’ s not a crisis...."

**[duckduckgo] "Yes, climate change is real | A Skewed Perspective"**
  Type: web | Cred: estimated 0.23199999999999998
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.2305)
  Snippet: "Yes, climate change is real ... The first of these pernicious myths that crop up in our world is the notion that climate change is a hoax...."

**[duckduckgo] "Climate Change Is Real. So What? – SkyWaterEarth"**
  Type: web | Cred: estimated 0.22999999999999998
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.2266)
  Snippet: "Climate Change Is Real. ... Of course climate change is real. ... Why do Republicans support the absurd position that there is no climate change when ..."

**[duckduckgo] "» Climate Change Is A Real Problem To Honest Scientists"**
  Type: web | Cred: estimated 0.335
  NLI (nli_deberta): supporting (0.9541)
  Verdict contribution: supporting (weight: 0.3196)
  Snippet: "Climate Change Is A Real Problem To Honest Scientists And To … : The scientific evidence for climate change is … http://t.co/0aWom7mb..."

**[duckduckgo] "Legalectric » Blog Archive » Yes, climate change is"**
  Type: web | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8955)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... in Monticello, MN, it was up to 54 degrees! At each of the seven meetings, at least two people waxed histrionically that climate change was not re..."

**[duckduckgo] "Climate Change Is Real Ft E-State & BangCorrupt"**
  Type: web | Cred: estimated 0.28500000000000003
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.2825)
  Snippet: "Climate Change Is Real Ft E-State & BangCorrupt ... These MCs ” mix, this is a chill little mix of my “ Climage Change Is Real ......"

**[duckduckgo] "There is no real debate around 'is climate change"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9751)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... climate change debate while we await confirmation of whether climate ... Determining whether climate change is real or even human-induced is moot...."

**[wikidata] "climate change"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "human-caused changes to climate on Earth | instance of: global problem..."

**[wikidata] "climate change adaptation"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "process of adjustment to actual or expected climate change and its effects, seeking to moderate or avoid harm or exploit beneficial opportunities..."

**[wikidata] "climate change mitigation"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "actions to limit climate change in order to reduce the risks of global warming | instance of: field of work..."

### Verdict computation
  Supporting weight: 18.1078
  Opposing weight: 0.8075
  Support ratio: 0.9573
  Confidence: 0.9146
  Verdict: **strongly supported**
  Neutral sources (no contribution): 16

  Top supporting:
    - Climate change in Africa (weight: 0.8487)
    - Effects of climate change on human health (weight: 0.8471)
    - Economic analysis of climate change (weight: 0.8463)
    - Climate change policy of the United States (weight: 0.8454)
    - Climate change feedbacks (weight: 0.8454)
  Top opposing:
    - 2008 quote does not reflect scientific consensus: Humans do cause ... (weight: 0.8075)

---
## 2. "evolution is real"
Category: factual_true
Expected: strongly supported
Actual: likely supported (YES)
Claim type: factual (0.9979)

### Sources collected: 46 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 46 -> 16 (dropped 30)
Dropped sources:
  - [encyclopedia] "Real Madrid CF" (relevance: 0.2242, reason: relevance_0.224_below_0.35)
  - [encyclopedia] "Pro Evolution Soccer" (relevance: 0.2573, reason: relevance_0.257_below_0.35)
  - [encyclopedia] "Dove Campaign for Real Beauty" (relevance: 0.2142, reason: relevance_0.214_below_0.35)
  - [encyclopedia] "Evolution (2001 film)" (relevance: 0.4292, reason: non_content_pattern)
  - [encyclopedia] "Real Betis" (relevance: 0.1788, reason: relevance_0.179_below_0.35)
  - [encyclopedia] "Evolution (advertisement)" (relevance: 0.4835, reason: non_content_pattern)
  - [academic] "AI Agents: Evolution, Architecture, and Real-World Applications" (relevance: 0.1139, reason: relevance_0.114_below_0.35)
  - [academic] "Study on dynamic wear evolution of modified gear rack considering the real-time variation of contact characteristics" (relevance: 0.0799, reason: relevance_0.080_below_0.35)
  - [academic] "Real-time tracking of CoSe2@VSe2 anode evolution for stable sodium storage" (relevance: 0.1026, reason: relevance_0.103_below_0.35)
  - [academic] "In-situ and Real-time Monitoring the Chemical and Thermal Evolution of Lithium-ion Batteries with Single-crystalline Ni-rich Layered Oxide Cathode." (relevance: -0.0107, reason: relevance_-0.011_below_0.35)
  - [academic] "Real-Time Operator Evolution in Two and Three Dimensions via Sparse Pauli Dynamics" (relevance: 0.0194, reason: relevance_0.019_below_0.35)
  - [academic] "Structure Learning of Hamiltonians from Real-Time Evolution" (relevance: 0.1989, reason: relevance_0.199_below_0.35)
  - [academic] "Evolution of the real area of contact during laboratory earthquakes" (relevance: 0.0083, reason: relevance_0.008_below_0.35)
  - [academic] "Evolution of a real-time laser M2 measurement system" (relevance: -0.0564, reason: relevance_-0.056_below_0.35)
  - [academic] "Quantum real-time evolution of entanglement and hadronization in jet production: Lessons from the massive Schwinger model" (relevance: 0.1515, reason: relevance_0.152_below_0.35)
  - [academic] "Real-time control of urban drainage systems using neuro-evolution." (relevance: 0.2582, reason: relevance_0.258_below_0.35)
  - [academic] "Structural evolution of real estate industry in China: 2002-2017" (relevance: 0.1628, reason: relevance_0.163_below_0.35)
  - [academic] "ACE: Anchor-Free Corner Evolution for Real-Time Arbitrarily-Oriented Object Detection" (relevance: 0.1023, reason: relevance_0.102_below_0.35)
  - [academic] "Real- and Imaginary-Time Evolution with Compressed Quantum Circuits" (relevance: 0.1343, reason: relevance_0.134_below_0.35)
  - [academic] "Real- and Imaginary-Time Evolution with Compressed Quantum Circuits" (relevance: 0.1343, reason: relevance_0.134_below_0.35)
  - [academic] "Host-Parasite Co-Evolution in Real-Time: Changes in Honey Bee Resistance Mechanisms and Mite Reproductive Strategies" (relevance: 0.2105, reason: relevance_0.211_below_0.35)
  - [academic] "Public Opinion Analysis on Novel Coronavirus Pneumonia and Interaction With Event Evolution in Real World" (relevance: 0.1858, reason: relevance_0.186_below_0.35)
  - [academic] "From AI to AGI - The Evolution of Real-Time Systems with GPT Integration" (relevance: 0.047, reason: relevance_0.047_below_0.35)
  - [academic] "Towards Automatic Grammatical Evolution for Real-world Symbolic Regression" (relevance: 0.2886, reason: relevance_0.289_below_0.35)
  - [academic] "Quantum Algorithm for Simulating Real Time Evolution of Lattice Hamiltonians" (relevance: 0.1172, reason: relevance_0.117_below_0.35)
  - [academic] "Jumping a Moving Train: SARS-CoV-2 Evolution in Real Time" (relevance: 0.2053, reason: relevance_0.205_below_0.35)
  - [knowledge_graph] "Evolution" (relevance: 0.1287, reason: relevance_0.129_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.2296, reason: relevance_0.230_below_0.35)
  - [knowledge_graph] "real property" (relevance: 0.1334, reason: relevance_0.133_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.3195, reason: relevance_0.320_below_0.35)

### Dedup: 16 -> 16 (dropped 0)

### Analyzed sources (16 total)

**[wikipedia] "Evolution"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.9449)
  Snippet: "Evolution is the change in the heritable characteristics of biological populations over successive generations. It occurs when evolutionary processes ..."

**[wikipedia] "Theistic evolution"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9761)
  Verdict contribution: supporting (weight: 0.8297)
  Snippet: "Theistic evolution (also known as theistic evolutionism or God-guided evolution, or alternatively called evolutionary creationism) is a view that God ..."

**[wikipedia] "Speculative evolution"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.9771)
  Verdict contribution: opposing (weight: 0.8305)
  Snippet: "Speculative evolution is a subgenre of science fiction and an artistic movement focused on hypothetical scenarios in the evolution of life, and a sign..."

**[wikipedia] "Evolutionism"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.96)
  Verdict contribution: supporting (weight: 0.672)
  Snippet: "Evolutionism is a term used (often derogatorily) to denote the theory of evolution. Its exact meaning has changed over time as the study of evolution ..."

**[duckduckgo] "Evolutionism (Religion)"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.7519)
  Snippet: "Evolutionism is a term used (often derogatorily) to denote the theory of evolution. Its exact meaning has changed over time as the study of evolution ..."

**[duckduckgo] "Why Cultural Evolution Is Real (And What It Is) –"**
  Type: web | Cred: estimated 0.322
  NLI (nli_deberta): supporting (0.8755)
  Verdict contribution: supporting (weight: 0.2819)
  Snippet: "47 thoughts on “ Why Cultural Evolution Is Real (And What It Is) ” ... My point here is to establish the reality of cultural evolution ......"

**[duckduckgo] "If evolution is real, then why isn’t it happening now? An"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.9268)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "https://theconversation.com/if-evolution-is-real-then-why-isnt-it-happening-now-an-anthropologist-explains-that-humans-actually-are-still-evolving ......"

**[duckduckgo] "Evolution is not real"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.9497)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "I realize that this is a debate focused on biology, so will ... Con is arguing that Evolution is real, Pro is defending that Evolution is not real...."

**[duckduckgo] "Is evolution theory real? - Science Mathematics"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9663)
  Verdict contribution: supporting (weight: 0.1933)
  Snippet: "... and chemical forces or that some entity that nobody ever sees waved a magic wand and created everything? Yes of course evolution theory is real...."

**[duckduckgo] "Evolution Is Real | I, Dynamo"**
  Type: web | Cred: estimated 0.21400000000000002
  NLI (nli_deberta): supporting (0.9932)
  Verdict contribution: supporting (weight: 0.2125)
  Snippet: "Evolution Is Real ... C ’ mon, people, evolution is real. ... Evolution is real...."

**[duckduckgo] "Is evolution real? - Faith & Science Conversation - The"**
  Type: web | Cred: estimated 0.29500000000000004
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.2907)
  Snippet: "Yes evolution is real. ... is just a small example of what is established by many more lines of evidence leading to evolutionary thought, and if that ..."

**[duckduckgo] "Curious Kids: If evolution is real, then why isn’t it"**
  Type: web | Cred: estimated 0.42699999999999994
  NLI (nli_deberta): neutral (0.9404)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Curious Kids: If evolution is real, then why isn’t it ... If evolution is real, then why is it not happening now? – Dee, Memphis, Tennessee..."

**[duckduckgo] "Is Evolution Real?"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9224)
  Verdict contribution: opposing (weight: 0.2767)
  Snippet: "Is Evolution Real? I have stated in the past here on this site (and other places) that I believe that evolution is false...."

**[duckduckgo] "Evolution Is As Real As Gravity"**
  Type: web | Cred: estimated 0.25
  NLI (nli_deberta): supporting (0.98)
  Verdict contribution: supporting (weight: 0.245)
  Snippet: "Evolution Is As Real As Gravity ... So why would anyone claim that evolution is not real, or that Darwin was wrong?..."

**[wikidata] "Evolution"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "monthly scientific journal | instance of: scientific journal | inception: 1947-00-00..."

**[wikidata] "evolution"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "change in heritable characteristics of biological populations over successive generations | instance of: type of process..."

### Verdict computation
  Supporting weight: 4.4219
  Opposing weight: 1.1073
  Support ratio: 0.7997
  Confidence: 0.5995
  Verdict: **likely supported**
  Neutral sources (no contribution): 5

  Top supporting:
    - Evolution (weight: 0.9449)
    - Theistic evolution (weight: 0.8297)
    - Evolutionism (Religion) (weight: 0.7519)
    - Evolutionism (weight: 0.672)
    - Is evolution real? - Faith & Science Conversation - The (weight: 0.2907)
  Top opposing:
    - Speculative evolution (weight: 0.8305)
    - Is Evolution Real? (weight: 0.2767)

---
## 3. "water boils at 100 degrees celsius"
Category: factual_true
Expected: strongly supported
Actual: contested (**NO - MISMATCH**)
Claim type: factual (0.9943)

### Sources collected: 42 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 2

### Relevance filter: 42 -> 17 (dropped 25)
Dropped sources:
  - [encyclopedia] "Sentence (linguistics)" (relevance: -0.0097, reason: relevance_-0.010_below_0.35)
  - [encyclopedia] "Anders Celsius" (relevance: 0.2334, reason: relevance_0.233_below_0.35)
  - [encyclopedia] "Kelvin" (relevance: 0.2979, reason: relevance_0.298_below_0.35)
  - [encyclopedia] "Rankine scale" (relevance: 0.2679, reason: relevance_0.268_below_0.35)
  - [encyclopedia] "Boiling water reactor" (relevance: 0.3065, reason: relevance_0.307_below_0.35)
  - [academic] "Investigation of the impact of the physical and chemical factors during correction treatment of NPP unbalance water to ensure compliance of conditioned radioactive waste with regulatory requirements" (relevance: 0.2064, reason: relevance_0.206_below_0.35)
  - [academic] "Development of Zinc Oxide Nanoparticle–Infused Carrageenan Membranes with Enhanced Structural and Antimicrobial Properties for Guided Tissue Regeneration" (relevance: -0.0564, reason: relevance_-0.056_below_0.35)
  - [academic] "Estimation of oil recovery due to wettability changes in carbonate reservoirs" (relevance: 0.0931, reason: relevance_0.093_below_0.35)
  - [academic] "Effects of Valerian and ST36 Acupuncture on Kidney and Liver Function in Rats" (relevance: 0.0394, reason: relevance_0.039_below_0.35)
  - [academic] "B-075 A solution for peak migration in capillary electrophoresis hemoglobin A1c readings in patients with hyperleukocytosis" (relevance: 0.1198, reason: relevance_0.120_below_0.35)
  - [academic] "Climate Change and Its Impact on Groundwater Resources in Semi-Arid Regions: A Case Study of Libya" (relevance: 0.1023, reason: relevance_0.102_below_0.35)
  - [academic] "Using polyethylene terephthalate plastic to produce nano-activate carbon for use in industrial wastewater treatment" (relevance: 0.0942, reason: relevance_0.094_below_0.35)
  - [academic] "Design of a cyclone separator with circumfluent cyclone and convergent vortex finder for spray drying" (relevance: 0.1261, reason: relevance_0.126_below_0.35)
  - [academic] "Introducing sound speed variability in laboratory water tank" (relevance: 0.2224, reason: relevance_0.222_below_0.35)
  - [academic] "Pool boiling simulation of two nanofluids at multi concentrations in enclosure with different shapes of fins" (relevance: 0.3427, reason: relevance_0.343_below_0.35)
  - [academic] "Boerhavia diffusa Mediated Selenium Nanoparticles and their Antioxidant and Anti-Inflammatory Activity" (relevance: -0.0171, reason: relevance_-0.017_below_0.35)
  - [academic] "Evaluation of Anti-Inflammatory Property of Maranta Arundinacea using Protein Denaturation Assay - An In vitro Study" (relevance: -0.0258, reason: relevance_-0.026_below_0.35)
  - [academic] "Anti Microbial Activity of Musa sapientum Mediated Copper Nanoparticle against Oral Pathogens: An In-vitro Study" (relevance: 0.109, reason: relevance_0.109_below_0.35)
  - [academic] "Green Synthesis and Antioxidant Activity of Silver Nanoparticles Synthesized Using Ficus benghalensis" (relevance: 0.0504, reason: relevance_0.050_below_0.35)
  - [academic] "Mineral commodity summaries 2022" (relevance: -0.0468, reason: relevance_-0.047_below_0.35)
  - [academic] "Industrial decarbonization via hydrogen: A critical and systematic review of developments, socio-technical systems and policy options" (relevance: 0.028, reason: relevance_0.028_below_0.35)
  - [academic] "Measuring Reading Comprehension with the Lexile Framework" (relevance: 0.2316, reason: relevance_0.232_below_0.35)
  - [academic] "The potential of biofuels from first to fourth generation" (relevance: 0.0356, reason: relevance_0.036_below_0.35)
  - [academic] "Circular economy approach of enhanced bifunctional catalytic system of CaO/CeO2 for biodiesel production from waste loquat seed oil with life cycle assessment study" (relevance: -0.0454, reason: relevance_-0.045_below_0.35)
  - [knowledge_graph] "water boils when angry warrior is immersed in it" (relevance: 0.1969, reason: relevance_0.197_below_0.35)

### Dedup: 17 -> 17 (dropped 0)

### Analyzed sources (17 total)

**[wikipedia] "Celsius"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The degree Celsius is the unit of temperature on the Celsius temperature scale (originally known as the centigrade scale in English), one of two tempe..."

**[wikipedia] "Fahrenheit"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.9536)
  Verdict contribution: opposing (weight: 0.7629)
  Snippet: "The Fahrenheit scale () is a temperature scale based on one proposed in 1724 by the physicist Daniel Gabriel Fahrenheit (1686–1736). It uses the degre..."

**[wikipedia] "Nucleate boiling"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): opposing (0.9941)
  Verdict contribution: opposing (weight: 0.6959)
  Snippet: "In fluid thermodynamics, nucleate boiling is a type of boiling that takes place when the surface temperature is hotter than the saturated fluid temper..."

**[wikipedia] "Temperature"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In classical thermodynamics and kinetic theory, temperature reflects the average kinetic energy of the particles in a system, providing a quantitative..."

**[wikipedia] "Degree (temperature)"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.8853)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The term degree is used in several scales of temperature, with the notable exception of kelvin, primary unit of temperature for engineering and the ph..."

**[semantic_scholar] "Immaculate Water Tank"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.96)
  Verdict contribution: opposing (weight: 0.528)
  Snippet: "The water in overhead tanks heats up to a temperature of more than 40 degrees Celsius during the summer in Tamil Nadu, where temperatures range from 3..."

**[duckduckgo] "What does water change to above 100 degrees Celsius? - Answers"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.4143)
  Snippet: "Water boils at 100 degrees Celsius. ... At this temperature, water is above its freezing point (0 degrees Celsius) and below its boiling point (100 ....."

**[duckduckgo] "At what degree water starts to boil? - Answers"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): supporting (0.9839)
  Verdict contribution: supporting (weight: 0.4113)
  Snippet: "Water starts to boil at a temperature of 100 degrees Celsius, regardless of the microwave frequency used. ... make water 2 boil at 97 degree Celsius ...."

**[duckduckgo] "Why does water boil at 121 degrees? - Answers"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.4174)
  Snippet: "Water boils at 121 degrees Celsius under normal atmospheric pressure, which is approximately 1 atmosphere or 101.3 kilopascals (kPa)...."

**[duckduckgo] "boiling - Can I boil water to temperature lower than 100"**
  Type: web | Cred: estimated 0.40499999999999997
  NLI (nli_deberta): supporting (0.9834)
  Verdict contribution: supporting (weight: 0.3983)
  Snippet: "... to reach with boiling the water - or wait a bit on a somewhat lower temperature until every bacteria is dead, in this case 1 minute at 100 Celsius..."

**[duckduckgo] "Why Water has a Boiling Point of 100 Degrees Celcius |"**
  Type: web | Cred: estimated 0.217
  NLI (nli_deberta): supporting (0.9858)
  Verdict contribution: supporting (weight: 0.2139)
  Snippet: "The reason water boils at 100 degrees Celsius though is because we are the people that made the scale and if we wanted to we could have based the ......"

**[duckduckgo] "Why Water has a Boiling Point of 100 Degrees Celcius |"**
  Type: web | Cred: estimated 0.217
  NLI (nli_deberta): opposing (0.8335)
  Verdict contribution: opposing (weight: 0.1809)
  Snippet: "Guess which scale I just made up.) You could just as easily define your own temperature scale, on which water can boil at 0, 42, or 1000 degrees...."

**[duckduckgo] "90 Degrees Celsius To Fahrenheit Is It Truly Boiling Hot"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.9932)
  Verdict contribution: supporting (weight: 0.298)
  Snippet: "And speaking of temperatures, did you know that water boils at 100 degrees Celsius? This fact creates a clear picture of how close we get at 90 ......"

**[duckduckgo] "Why doesn't boiling water exceed 100 deg C? •"**
  Type: web | Cred: estimated 0.34700000000000003
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.3439)
  Snippet: "The discussion centers on the fundamental reasons why water boils at 100 degrees Celsius at standard atmospheric pressure (1 atm)...."

**[duckduckgo] "Boil Water - You can boil water."**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9849)
  Verdict contribution: supporting (weight: 0.197)
  Snippet: "Water will boil at 100 degrees Celsius or 212 degrees Fahrenheit. ... Question: When does water boil ? Answer: Water boils at 212 degrees F or 100 ......"

**[duckduckgo] "40 Lessons From 40 Years - by Jared A. Brock"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.9907)
  Verdict contribution: supporting (weight: 0.2972)
  Snippet: "Water boils at 100 degrees Celsius. ... Why do people desire the attention of strangers? Because we all need to love and be loved, to know and be ......"

**[wikidata] "Water boils at 100 degree Celsius and has an angle"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scholarly article | instance of: scholarly article..."

### Verdict computation
  Supporting weight: 2.5739
  Opposing weight: 2.585
  Support ratio: 0.4989
  Confidence: 0.0022
  Verdict: **contested**
  Neutral sources (no contribution): 4

  Top supporting:
    - What does water change to above 100 degrees Celsius? - Answers (weight: 0.4143)
    - At what degree water starts to boil? - Answers (weight: 0.4113)
    - boiling - Can I boil water to temperature lower than 100 (weight: 0.3983)
    - Why doesn't boiling water exceed 100 deg C? • (weight: 0.3439)
    - 90 Degrees Celsius To Fahrenheit Is It Truly Boiling Hot (weight: 0.298)
  Top opposing:
    - Fahrenheit (weight: 0.7629)
    - Nucleate boiling (weight: 0.6959)
    - Immaculate Water Tank (weight: 0.528)
    - Why does water boil at 121 degrees? - Answers (weight: 0.4174)
    - Why Water has a Boiling Point of 100 Degrees Celcius | (weight: 0.1809)

---
## 4. "the speed of light is constant"
Category: factual_true
Expected: strongly supported
Actual: likely supported (YES)
Claim type: factual (0.9964)

### Sources collected: 39 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 39 -> 27 (dropped 12)
Dropped sources:
  - [encyclopedia] "Formulations of special relativity" (relevance: 0.2693, reason: relevance_0.269_below_0.35)
  - [encyclopedia] "Quantum foam" (relevance: 0.0457, reason: relevance_0.046_below_0.35)
  - [encyclopedia] "Variable-pitch propeller (aeronautics)" (relevance: 0.2416, reason: relevance_0.242_below_0.35)
  - [academic] "Model-independent confirmation of a constant speed of light over cosmological distances" (relevance: 0.3152, reason: relevance_0.315_below_0.35)
  - [knowledge_graph] "Speed" (relevance: 0.2938, reason: relevance_0.294_below_0.35)
  - [knowledge_graph] "Speed" (relevance: 0.1062, reason: relevance_0.106_below_0.35)
  - [knowledge_graph] "visible spectrum" (relevance: 0.1425, reason: relevance_0.143_below_0.35)
  - [knowledge_graph] "lighthouse" (relevance: 0.1962, reason: relevance_0.196_below_0.35)
  - [knowledge_graph] "Light" (relevance: 0.2397, reason: relevance_0.240_below_0.35)
  - [knowledge_graph] "Constant" (relevance: 0.2768, reason: relevance_0.277_below_0.35)
  - [knowledge_graph] "Constant" (relevance: 0.2658, reason: relevance_0.266_below_0.35)
  - [knowledge_graph] "Constanța" (relevance: 0.3208, reason: relevance_0.321_below_0.35)

### Dedup: 27 -> 26 (dropped 1)

### Analyzed sources (26 total)

**[wikipedia] "Speed of light"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.9976)
  Verdict contribution: supporting (weight: 0.9477)
  Snippet: "The speed of light in vacuum, often called simply the speed of light and commonly denoted c, is a universal physical constant exactly equal to 2997924..."

**[wikipedia] "Variable speed of light"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9429)
  Verdict contribution: supporting (weight: 0.7543)
  Snippet: "A variable speed of light (VSL) is a feature of a family of hypotheses stating that the speed of light may in some way not be constant, for example, t..."

**[wikipedia] "Physical constant"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9873)
  Verdict contribution: supporting (weight: 0.7898)
  Snippet: "A physical constant, sometimes called a fundamental physical constant or universal constant, is a physical quantity that cannot be explained by a theo..."

**[wikipedia] "Special relativity"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9922)
  Verdict contribution: supporting (weight: 0.8434)
  Snippet: "In physics, the special theory of relativity, or simply special relativity, is a scientific theory of the relationship between space and time. In Albe..."

**[wikipedia] "Speed"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9912)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In kinematics, the speed (commonly referred to as v) of an object is the magnitude of the change of its position over time or the magnitude of the cha..."

**[wikipedia] "One-way speed of light"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.6284)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "When using the term "the speed of light" it is sometimes necessary to make the distinction between its one-way speed and its two-way speed. The "one-w..."

**[wikipedia] "Faster-than-light"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9595)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Faster-than-light (superluminal or supercausal) travel and communication are the conjectural propagation of matter or information faster than the spee..."

**[open_alex] "Constraints on variation in the speed of light based on gravitational constant constraints"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.6987)
  Verdict contribution: supporting (weight: 0.4542)
  Snippet: "ABSTRACT We consider the possibility of a varying speed of light based on a unit of length defined with a rigid rod or atomic standard. The reference ..."

**[open_alex] "The cosmological evolution condition of the Planck constant in the varying speed of light models through adiabatic expansion"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9907)
  Verdict contribution: opposing (weight: 0.644)
  Snippet: "The cosmological evolution condition of the Planck constant in the varying speed of light models through adiabatic expansion..."

**[open_alex] "Asymmetry theory derived from the principle of constant light speed"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.6465)
  Snippet: "“The principle of the constancy of the velocity of light” was well established, while the further assumption that the light velocity is independent of..."

**[open_alex] "Constraining a possible time-variation of the speed of light along with the fine-structure constant using strong gravitational lensing and Type Ia supernovae observations"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9561)
  Verdict contribution: opposing (weight: 0.6215)
  Snippet: "Abstract The possible time variation of the fundamental constants of nature has been an active subject of research since the large-number hypothesis w..."

**[open_alex] "The Speed of Light Is Not Constant in Basic Big Bang Theory"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9888)
  Verdict contribution: opposing (weight: 0.5438)
  Snippet: "Starting from the basic assumptions and equations of Big Bang theory, we present a simple mathematical proof that this theory implies a varying (decre..."

**[open_alex] "Dilaton-induced variations in Planck constant and speed of light: An alternative to dark energy"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9854)
  Verdict contribution: opposing (weight: 0.542)
  Snippet: "We reveal a novel aspect of scale-invariant actions that allow matter to couple with a dilaton field: The dynamics of the dilaton can induce variation..."

**[open_alex] "New Physical Meaning and Principle of Determining the Speed of Light Constant"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.7583)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The work applies to all areas of physics where the speed constant is used - the speed of light in a vacuum c, in particular - to quantum physics, soli..."

**[open_alex] "The cosmological evolution condition of the Planck constant in the varying speed of light models through adiabatic expansion"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.998)
  Verdict contribution: opposing (weight: 0.5489)
  Snippet: "There have been various varying speed of light (VSL) models with one free parameter, $b$, to characterize the time variation of the speed of light as ..."

**[open_alex] "Revelations from Historical Experiments on Constant Speed of Light"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9712)
  Verdict contribution: supporting (weight: 0.5342)
  Snippet: "The postulate of constant speed of light for all reference frames is the foundation of relativity theories. The resultant time dilation and length con..."

**[duckduckgo] "Is the speed of light constant? : r/AskPhysics - Reddit"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): supporting (0.9819)
  Verdict contribution: supporting (weight: 0.5852)
  Snippet: "May 5, 2023 · The speed of light is always locally (near to you) constant and 'c' in a vacuum regardless of acceleration or gravitational sources. You..."

**[duckduckgo] "Is The Speed of Light Everywhere the Same? - UCR Math"**
  Type: web | Cred: estimated 0.45999999999999996
  NLI (nli_deberta): supporting (0.9419)
  Verdict contribution: supporting (weight: 0.4333)
  Snippet: "In special relativity, the speed of light is constant when measured in any inertial frame. In general relativity, the appropriate generalisation is th..."

**[duckduckgo] "Why the Speed of Light (c) Keeps Constant? - SCIRP"**
  Type: web | Cred: estimated 0.369
  NLI (nli_deberta): neutral (0.9038)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "When Einstein setup the relativity theory, he supposed the speed of light is constant and furthermore, nobody in our universe can go faster than the l..."

**[duckduckgo] "Speed of Light May Not Be Constant, Physicists Say | Live Science"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.9961)
  Verdict contribution: opposing (weight: 0.8467)
  Snippet: "Apr 27, 2013 · The speed of light may not be constant, a possibility that could have broad implications for fields of cosmology and even astronomy, ....."

**[duckduckgo] "Why is the speed of light in vacuum constant? - Physics Stack Exchange"**
  Type: web | Cred: estimated 0.457
  NLI (nli_deberta): supporting (0.5986)
  Verdict contribution: supporting (weight: 0.2736)
  Snippet: "Jan 5, 2015 · All I hear is that light in vacuum travels at a constant speed because that's an observation and that it fits in a coherent theory with ..."

**[duckduckgo] "How "Fast" is the Speed of Light?"**
  Type: web | Cred: estimated 0.251
  NLI (nli_deberta): supporting (0.9868)
  Verdict contribution: supporting (weight: 0.2477)
  Snippet: "Light travels at a constant, finite speed of 186,000 mi/sec. A traveler, moving at the speed of light, would circum-navigate the equator approximately..."

**[duckduckgo] "The Speed of Light is NOT Constant | by Fermion Physics | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9272)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Nov 22, 2022 · It's often said that in the context of special relativity, the speed of light is constant in all frames of reference...."

**[duckduckgo] "Speed of light not constant proving Relativity wrong"**
  Type: web | Cred: estimated 0.281
  NLI (nli_deberta): opposing (0.999)
  Verdict contribution: opposing (weight: 0.2807)
  Snippet: "Jul 17, 2023 · The one-way speed of light depends on the observer's velocity relative to the cosmological reference frame, i.e. relative to space. Ein..."

**[duckduckgo] "DOE Explains...Relativity - Department of Energy"**
  Type: web | Cred: estimated 0.488
  NLI (nli_deberta): neutral (0.937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "May 14, 2026 · The speed of light is incredibly high. Because the speed of light is squared in Einstein's equation, tiny amounts of mass contain huge ..."

**[wikidata] "speed"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "magnitude of velocity of motion..."

### Verdict computation
  Supporting weight: 6.5098
  Opposing weight: 4.0275
  Support ratio: 0.6178
  Confidence: 0.2356
  Verdict: **likely supported**
  Neutral sources (no contribution): 8

  Top supporting:
    - Speed of light (weight: 0.9477)
    - Special relativity (weight: 0.8434)
    - Physical constant (weight: 0.7898)
    - Variable speed of light (weight: 0.7543)
    - Asymmetry theory derived from the principle of constant light speed (weight: 0.6465)
  Top opposing:
    - Speed of Light May Not Be Constant, Physicists Say | Live Science (weight: 0.8467)
    - The cosmological evolution condition of the Planck constant in the varying speed of light models through adiabatic expansion (weight: 0.644)
    - Constraining a possible time-variation of the speed of light along with the fine-structure constant using strong gravitational lensing and Type Ia supernovae observations (weight: 0.6215)
    - The cosmological evolution condition of the Planck constant in the varying speed of light models through adiabatic expansion (weight: 0.5489)
    - The Speed of Light Is Not Constant in Basic Big Bang Theory (weight: 0.5438)

---
## 5. "the earth is flat"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.998)

### Sources collected: 54 total
  - google_factcheck: 10
  - wikipedia: 10
  - semantic_scholar: 8
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 54 -> 30 (dropped 24)
Dropped sources:
  - [encyclopedia] "Flat Earth (disambiguation)" (relevance: 0.7941, reason: non_content_pattern)
  - [encyclopedia] "Tanith Lee bibliography" (relevance: 0.0792, reason: relevance_0.079_below_0.35)
  - [encyclopedia] "Flat Earth Society (disambiguation)" (relevance: 0.6382, reason: non_content_pattern)
  - [academic] "The Earth is Flat because...: Investigating LLMs' Belief towards Misinformation via Persuasive Conversation" (relevance: 0.1047, reason: relevance_0.105_below_0.35)
  - [academic] "Where the Earth is flat and 9/11 is an inside job: A comparative algorithm audit of conspiratorial information in web search results" (relevance: 0.1099, reason: relevance_0.110_below_0.35)
  - [academic] "The Earth Is Flat and the Sun Is Not a Star: The Susceptibility of GPT-2 to Universal Adversarial Triggers" (relevance: 0.0351, reason: relevance_0.035_below_0.35)
  - [academic] "The Earth Is Not Flat: Bilateral Elevation as a Component of Trade Costs" (relevance: 0.2543, reason: relevance_0.254_below_0.35)
  - [academic] "First detection of VHE gamma-ray signal from the FSRQ TON 0599" (relevance: 0.079, reason: relevance_0.079_below_0.35)
  - [academic] "Near-IR and optical radial velocities of the active M-dwarf star Gl 388 (AD Leo) with SPIRou at CFHT and SOPHIE at OHP: A 2.23 day rotation period and no evidence for a co-rotating planet" (relevance: 0.1083, reason: relevance_0.108_below_0.35)
  - [academic] "Cosmic Supernova Neutrino and Gamma-Ray Backgrounds in the MeV Regime" (relevance: 0.1031, reason: relevance_0.103_below_0.35)
  - [academic] "Where the earth is flat and 9/11 is an inside job: A comparative algorithm audit of conspiratorial information in web search results" (relevance: 0.1348, reason: relevance_0.135_below_0.35)
  - [academic] "Rapid, robust, and automated mapping of tidal flats in China using time series Sentinel-2 images and Google Earth Engine" (relevance: 0.3224, reason: relevance_0.322_below_0.35)
  - [academic] "The Earth Is Flat and the Sun Is Not a Star: The Susceptibility of GPT-2 to Universal Adversarial Triggers" (relevance: 0.0351, reason: relevance_0.035_below_0.35)
  - [academic] "A Classification of Tidal Flat Wetland Vegetation Combining Phenological Features with Google Earth Engine" (relevance: 0.2486, reason: relevance_0.249_below_0.35)
  - [academic] "The Earth is Flat because...: Investigating LLMs' Belief towards Misinformation via Persuasive Conversation" (relevance: 0.1047, reason: relevance_0.105_below_0.35)
  - [academic] "Conspiracy Theory as Individual and Group Behavior: Observations from the Flat Earth International Conference" (relevance: 0.2326, reason: relevance_0.233_below_0.35)
  - [academic] "Tracking dynamics characteristics of tidal flats using landsat time series and Google Earth Engine cloud platform" (relevance: 0.3381, reason: relevance_0.338_below_0.35)
  - [web] "The Earth Is Not Flat (book)" (relevance: 0.6897, reason: non_content_pattern)
  - [knowledge_graph] "Earth" (relevance: 0.2605, reason: relevance_0.261_below_0.35)
  - [knowledge_graph] "soil" (relevance: 0.2673, reason: relevance_0.267_below_0.35)
  - [knowledge_graph] "Earth, Wind & Fire" (relevance: 0.2054, reason: relevance_0.205_below_0.35)
  - [knowledge_graph] "apartment" (relevance: 0.0336, reason: relevance_0.034_below_0.35)
  - [knowledge_graph] "apartment building" (relevance: 0.0076, reason: relevance_0.008_below_0.35)
  - [knowledge_graph] "Flat" (relevance: 0.3034, reason: relevance_0.303_below_0.35)

### Dedup: 30 -> 27 (dropped 3)

### Analyzed sources (27 total)

**[google_factcheck] "No, NASA didn't admit the earth is flat"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "NASA has admitted the earth is flat in several documents...."

**[google_factcheck] "The Earth is not flat – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Satellites are fake...."

**[google_factcheck] "Flight paths are not evidence for a flat Earth"**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Flights from New Zealand to Argentina connect through the U.S., which only makes sense if the Earth is flat...."

**[google_factcheck] "Fact check: Gravity pulls objects toward the center of the Earth"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "The Earth is flat because cities cannot be upside-down..."

**[google_factcheck] "Earth isn't flat, and shooting stars fly every direction | Fact check"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Earth is flat because we never see shooting stars coming from the bottom up..."

**[google_factcheck] "Deadly Disinfo: How the Flat Earth Conspiracy Doomed an Amateur ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "“I don’t want to take anyone else’s word for it. I don’t know if the Earth is flat or round … I just couldn’t dismiss it (flat Earth theory) after fou..."

**[google_factcheck] "Fact check: False claim that timelapse photo from South Pole proves ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Photo of solar eclipse taken at the South Pole proves Earth is flat..."

**[google_factcheck] "Fact check: Earth curve, motion detectable, air pressure from gravity"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Earth not curved or moving; air pressure couldn't exist without a container..."

**[google_factcheck] "No, radar technology doesn't prove Earth is flat | Fact check"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Radar technology wouldn’t work if the Earth was a globe..."

**[wikipedia] "Flat Earth"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.937)
  Verdict contribution: opposing (weight: 0.7964)
  Snippet: "Flat Earth is an archaic and scientifically disproven conception of the Earth's shape as a plane or disk. Many ancient societies subscribed to a flat-..."

**[wikipedia] "Modern flat Earth beliefs"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.9004)
  Verdict contribution: opposing (weight: 0.7653)
  Snippet: "Anti-scientific beliefs in a flat Earth are promoted by a number of organizations and individuals. The claims of modern flat Earth proponents are not ..."

**[wikipedia] "Myth of the flat Earth"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.7041)
  Verdict contribution: opposing (weight: 0.5633)
  Snippet: "The myth of the flat Earth, or the flat-Earth error, is a modern historical misconception that European scholars and educated people during the Middle..."

**[wikipedia] "Inventing the Flat Earth"**
  Type: encyclopedia | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.4946)
  Verdict contribution: opposing (weight: 0.272)
  Snippet: "Inventing the Flat Earth (ISBN 978-0-275-95904-3) is a 1991 book by historian Jeffrey Burton Russell which debunks the notion that medieval Christians..."

**[wikipedia] "The Flat Earth"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.6216)
  Verdict contribution: supporting (weight: 0.4351)
  Snippet: "The Flat Earth is the second studio album by the English new wave and synth-pop musician Thomas Dolby, released on 6 February 1984 by EMI and Capitol ..."

**[wikipedia] "Tales from the Flat Earth"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.8564)
  Verdict contribution: supporting (weight: 0.5995)
  Snippet: "Tales from the Flat Earth is a fantasy series by British writer Tanith Lee.  The novels take inspiration from One Thousand and One Nights and are simi..."

**[wikipedia] "Mark Sargent (flat Earth proponent)"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9453)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Mark Kendall Sargent (born c. 1969) is an American conspiracy theorist, who is one of the leading proponents of, and recruiters for, the discredited f..."

**[semantic_scholar] "Did the New Testament Authors Believe the Earth Is Flat?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9888)
  Verdict contribution: opposing (weight: 0.5438)
  Snippet: "Certain scholars find evidence that the authors of the New Testament held to the cosmology of the ancient Near East, in which the sky is regarded as a..."

**[open_alex] "The Earth is Flat because...: Investigating LLMs’ Belief towards Misinformation via Persuasive Conversation"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9194)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Rongwu Xu, Brian Lin, Shujian Yang, Tianqi Zhang, Weiyan Shi, Tianwei Zhang, Zhixuan Fang, Wei Xu, Han Qiu. Proceedings of the 62nd Annual Meeting of ..."

**[open_alex] "Mapping Tidal Flats of the Bohai and Yellow Seas Using Time Series Sentinel-2 Images and Google Earth Engine"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.8716)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Tidal flats are one of the most productive ecosystems on Earth, providing essential ecological and economical services. Because of the increasing anth..."

**[open_alex] "The Flat Earth satire: using science theater to debunk absurd theories"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9888)
  Verdict contribution: supporting (weight: 0.6427)
  Snippet: "Abstract. Science needs everyone and everything; therefore, art must be used for its understanding. As the popularity of social media grows, absurd th..."

**[duckduckgo] "The earth is flat"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): opposing (0.8965)
  Verdict contribution: opposing (weight: 0.6778)
  Snippet: "Flat Earth is an archaic and scientifically disproven conception of the Earth's shape as a plane or disk. Many ancient societies subscribed to a flat-..."

**[duckduckgo] "Flat Earthers: What They Believe and Why | Scientific American"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.6782)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Two-dimensional maps show the earth as flat because it is impossible to show the entire surface with a photograph of a single globe...."

**[duckduckgo] "Is the Earth Flat? | Answers in Genesis"**
  Type: web | Cred: verified 0.25 | Bias: right-pseudoscience | Factual: low
  NLI (nli_deberta): neutral (0.9307)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Most people are aware that there is a Flat Earth Society, thinking that the Flat Earth Society is a serious group of people dedicated to promoting ......"

**[duckduckgo] "The earth is flat (p > 0.05): significance thresholds and"**
  Type: web | Cred: estimated 0.53
  NLI (nli_deberta): supporting (0.9888)
  Verdict contribution: supporting (weight: 0.5241)
  Snippet: "The earth is flat (p > 0.05): significance thresholds and the crisis of unreplicable research ... then describe how the switch in ......"

**[duckduckgo] "The Flat Earth Wiki"**
  Type: web | Cred: estimated 0.397
  NLI (nli_deberta): neutral (0.9434)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... is dedicated to unravelling the true mysteries of the ... The Flat Earth Society holds that there is a difference between believing and knowing ...."

**[duckduckgo] "Looking for Life on a Flat Earth | The New Yorker"**
  Type: web | Cred: verified 0.85 | Bias: left | Factual: high
  NLI (nli_deberta): supporting (0.9717)
  Verdict contribution: supporting (weight: 0.8259)
  Snippet: "The Earth is flat,” he said. ... The flat Earth is the post-truth landscape. ... Believing in a flat Earth is hard work; there is so much to ......"

**[duckduckgo] "Is Earth Actually Flat? - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.5615)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Support Vsauce, your brain, Alzheimer's research, and other YouTube educators by joining THE CURIOSITY BOX: a seasonal delivery of viral science ......"

### Verdict computation
  Supporting weight: 3.0273
  Opposing weight: 5.5187
  Support ratio: 0.3542
  Confidence: 0.2915
  Verdict: **likely opposed**
  Neutral sources (no contribution): 12

  Top supporting:
    - Looking for Life on a Flat Earth | The New Yorker (weight: 0.8259)
    - The Flat Earth satire: using science theater to debunk absurd theories (weight: 0.6427)
    - Tales from the Flat Earth (weight: 0.5995)
    - The earth is flat (p > 0.05): significance thresholds and (weight: 0.5241)
    - The Flat Earth (weight: 0.4351)
  Top opposing:
    - Flat Earth (weight: 0.7964)
    - Modern flat Earth beliefs (weight: 0.7653)
    - The earth is flat (weight: 0.6778)
    - Myth of the flat Earth (weight: 0.5633)
    - Did the New Testament Authors Believe the Earth Is Flat? (weight: 0.5438)

---
## 6. "vaccines cause autism"
Category: factual_false
Expected: strongly opposed
Actual: strongly opposed (YES)
Claim type: factual (0.9971)

### Sources collected: 50 total
  - google_factcheck: 10
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 50 -> 44 (dropped 6)
Dropped sources:
  - [fact_check] "FactChecking RFK Jr.'s Other Health Claims During HHS ..." (relevance: 0.0461, reason: relevance_0.046_below_0.35)
  - [fact_check] "FactChecking RFK Jr.'s Other Health Claims During HHS ..." (relevance: 0.1037, reason: relevance_0.104_below_0.35)
  - [fact_check] "FactChecking RFK Jr.'s Other Health Claims During HHS ..." (relevance: 0.2006, reason: relevance_0.201_below_0.35)
  - [encyclopedia] "Jenny McCarthy" (relevance: 0.1525, reason: relevance_0.153_below_0.35)
  - [academic] "Cross-platform spread: vaccine-related content, sources, and conspiracy theories in YouTube videos shared in early Twitter COVID-19 conversations" (relevance: 0.2834, reason: relevance_0.283_below_0.35)
  - [academic] "COVID-19 and vaccine hesitancy: A longitudinal study" (relevance: 0.3167, reason: relevance_0.317_below_0.35)

### Dedup: 47 -> 40 (dropped 7)

### Analyzed sources (40 total)

**[google_factcheck] "RFK Jr. Misleads on Autism Prevalence, Causes"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "As part of a 1970 autism prevalence study, “all the kids in Wisconsin were tested.”..."

**[google_factcheck] "RFK Jr. Cites Flawed Paper Claiming Link Between Vaccines and ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "“There’s a study that came out last week of 47,000 9-year-olds in the Medicaid system in Florida — I think a Louisiana scientist called Mawson — that ..."

**[google_factcheck] "FactChecking RFK Jr.'s Other Health Claims During HHS ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ""The Cochrane Collaboration has said that the "gold standard" approach for treating opioid addiction is 12 step programs."..."

**[wikipedia] "Vaccines and autism"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.9922)
  Verdict contribution: opposing (weight: 0.7938)
  Snippet: "Extensive investigation into vaccines and autism spectrum disorder has shown that there is no relationship between the two, causal or otherwise, and t..."

**[wikipedia] "MMR vaccine and autism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.7739)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Claims of a link between the measles, mumps, and rubella (MMR) vaccine and autism have been extensively investigated and have been found to be false. ..."

**[wikipedia] "Causes of autism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.9556)
  Verdict contribution: opposing (weight: 0.8123)
  Snippet: "The causes of autism are a subject of scientific research, but understanding of the etiology of autism is incomplete. It is influenced by a complex in..."

**[wikipedia] "Thiomersal and vaccines"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.689)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Concerns about thiomersal and vaccines are commonly expressed by anti-vaccine activists. Claims relating to the safety of thiomersal, a mercury-based ..."

**[wikipedia] "Brian Hooker (bioengineer)"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.5371)
  Verdict contribution: opposing (weight: 0.4297)
  Snippet: "Brian S. Hooker is a biologist and chemist who was department chair and Professor Emeritus of Biology at Simpson University. He is known for promoting..."

**[wikipedia] "Epidemiology of autism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The epidemiology of autism is the study of the incidence and distribution of autism spectrum disorders (ASD). A 2022 systematic review of global preva..."

**[wikipedia] "Autism Speaks"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Autism Speaks Inc. is an American non-profit autism awareness organization and the largest autism research organization in the United States. It spons..."

**[wikipedia] "Vaccine hesitancy"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Vaccine hesitancy is a delay in acceptance or refusal of vaccines despite availability and supporting evidence of effectivity. The term also includes ..."

**[wikipedia] "National Vaccine Injury Compensation Program"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Office of Special Masters of the U.S. Court of Federal Claims, popularly known as "vaccine court", administers a no-fault system for litigating va..."

**[semantic_scholar] "How Do Vaccines Cause Autism?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8232)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "How Do Vaccines Cause Autism?..."

**[semantic_scholar] "Vaccines work… and do not cause autism"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.98)
  Verdict contribution: opposing (weight: 0.392)
  Snippet: "Vaccines have saved millions of lives, yet their importance and safety is repeatedly in question. We cannot let disinformation campaigns get in the wa..."

**[semantic_scholar] "Time to remember: Vaccines don't cause autism"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9072)
  Verdict contribution: opposing (weight: 0.499)
  Snippet: "It was with great concern that the pediatric medicine community heard only 4 years ago of the recurring myth that that vaccines cause autism. So, gett..."

**[semantic_scholar] "Vaccine Induced Autoimmunity May Cause Autism and Neurological Disorders"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Much evidence has accumulated that vaccines not only cause inflammation but also induce autoimmunity. While the efficacy for many vaccines has been de..."

**[semantic_scholar] "Debunking Misinformation About a Causal Link Between Vaccines and Autism: Two Preregistered Tests of Dual-Process Versus Single-Process Predictions (With Conflicting Results)"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9561)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Dual-process and single-process theories lead to conflicting predictions about whether debunking messages negating a state of affairs should change re..."

**[semantic_scholar] "Evidence Showing Childhood Vaccinations Are Causing Autism and Other Intellectual Disabilities"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.6348)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The association between vaccines and neurodevelopmental disorders has been referred to by the recently re-elected US President Donald Trump and his ne..."

**[semantic_scholar] "Unadjusted Analysis of a Population-Based Study of Measles, Mumps, and Rubella Vaccination and Autism."**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8848)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Unadjusted Analysis of a Population-Based Study of Measles, Mumps, and Rubella Vaccination and Autism...."

**[semantic_scholar] "“I Thought It Was Better to Be Safe Than Sorry”: Factors Influencing Parental Decisions on HPV and Other Adolescent Vaccinations for Students with Intellectual Disability and/or Autism in New South Wales, Australia"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9233)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The uptake of human papilloma virus (HPV) and other adolescent vaccinations in special schools for young people with disability is significantly lower..."

**[semantic_scholar] "Misinformation About COVID-19 Vaccines on Social Media: Rapid Review"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9336)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background The development of COVID-19 vaccines has been crucial in fighting the pandemic. However, misinformation about the COVID-19 pandemic and vac..."

**[semantic_scholar] "Autism? COVID? Science?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9385)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Autism has been in the news — again and again. First, in September 2025 government officials warned that Tylenol (acetaminophen) use in pregnancy was ..."

**[open_alex] "Extension: Beliefs about causes of autism and vaccine hesitancy"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.6938)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Extension: Beliefs about causes of autism and vaccine hesitancy..."

**[open_alex] "Misinformation About COVID-19 Vaccines on Social Media: Rapid Review"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9473)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "BACKGROUND: The development of COVID-19 vaccines has been crucial in fighting the pandemic. However, misinformation about the COVID-19 pandemic and va..."

**[open_alex] "Time to remember: Vaccines don't cause autism"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9072)
  Verdict contribution: opposing (weight: 0.499)
  Snippet: "It was with great concern that the pediatric medicine community heard only 4 years ago of the recurring myth that that vaccines cause autism. So, gett..."

**[open_alex] "Republicans, Not Democrats, Are More Likely to Endorse Anti-Vaccine Misinformation"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9351)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Vaccine safety skeptics are often thought to be more likely to self-identify as Democrats (vs. Independents or Republicans). Recent studies, however, ..."

**[open_alex] "Medical Students and SARS-CoV-2 Vaccination: Attitude and Behaviors"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9756)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Since physicians play a key role in vaccination, the initial training of medical students (MS) should aim to help shape their attitude in this regard...."

**[open_alex] "The myth of vaccination and autism spectrum"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9062)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The myth of vaccination and autism spectrum..."

**[open_alex] "Vaccine Induced Autoimmunity May Cause Autism and Neurological Disorders"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Much evidence has accumulated that vaccines not only cause inflammation but also induce autoimmunity. While the efficacy for many vaccines has been de..."

**[open_alex] "Do vaccines cause autism?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.998)
  Verdict contribution: opposing (weight: 0.3992)
  Snippet: "Current research and expert consensus clarify that vaccines do not cause autism...."

**[duckduckgo] "Vaccines and autism - Wikipedia"**
  Type: web | Cred: estimated 0.537
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.5357)
  Snippet: "Extensive investigation into vaccines and autism spectrum disorder has shown that there is no relationship between the two, causal or otherwise, [1][2..."

**[duckduckgo] "Vaccines cause autism"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): opposing (0.98)
  Verdict contribution: opposing (weight: 0.7409)
  Snippet: "Extensive investigation into vaccines and autism spectrum disorder has shown that there is no relationship between the two, causal or otherwise, and t..."

**[duckduckgo] "Autism and Vaccines | Vaccine Safety | CDC"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): neutral (0.8809)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The claim "vaccines do not cause autism" is not an evidence-based claim because studies have not ruled out the possibility that infant vaccines cause ..."

**[duckduckgo] "Autism & Vaccines: Separating Fact from Fiction"**
  Type: web | Cred: estimated 0.29900000000000004
  NLI (nli_deberta): neutral (0.9536)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Autism is a lifelong condition that requires compassion, understanding, and scientific inquiry. Ensuring that families receive accurate information ab..."

**[duckduckgo] "Vaccines and autism: What Colorado families should know"**
  Type: web | Cred: estimated 0.471
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.4699)
  Snippet: "Recent national discussions have raised understandable questions about vaccines and autism. In Colorado, we rely on decades of rigorous, global scient..."

**[duckduckgo] "Vaccines Do Not Cause Autism | Johns Hopkins | Bloomberg School of ..."**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): opposing (0.9834)
  Verdict contribution: opposing (weight: 0.4484)
  Snippet: "Bloomberg School Why Experts Have Concluded That Vaccines Do Not Cause Autism How a retracted study from the 1990s undermined trust in vaccines and le..."

**[duckduckgo] "Experts: CDC Website Shift on Vaccines, Autism Sparks Confusion"**
  Type: web | Cred: estimated 0.471
  NLI (nli_deberta): opposing (0.9897)
  Verdict contribution: opposing (weight: 0.4661)
  Snippet: "The vaccines and autism page also is not clear in that its new bullet points are followed by a heading that maintains the previous CDC stance, “vaccin..."

**[duckduckgo] "Fact Checked: Vaccines: Safe and Effective, No Link to Autism"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): opposing (0.6777)
  Verdict contribution: opposing (weight: 0.6438)
  Snippet: "Autism is often first identified in children between 12 and 24 months. This corresponds to many developmental milestones and temporally corresponds to..."

**[duckduckgo] "Vaccines and autism: What does the evidence show? - Healio"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.7036)
  Verdict contribution: opposing (weight: 0.5981)
  Snippet: "For decades, debate has centered on whether vaccines — particularly the MMR vaccine — cause autism, a claim repeatedly discredited by scientific evide..."

**[duckduckgo] "Vaccines and autism"**
  Type: web | Cred: estimated 0.47800000000000004
  NLI (nli_deberta): neutral (0.9487)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The vaccines and autism controversy encompasses claims that childhood immunizations, particularly the measles-mumps-rubella (MMR) vaccine and those co..."

### Verdict computation
  Supporting weight: 0.0
  Opposing weight: 7.7277
  Support ratio: 0.0
  Confidence: 1.0
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 26

  Top opposing:
    - Causes of autism (weight: 0.8123)
    - Vaccines and autism (weight: 0.7938)
    - Vaccines cause autism (weight: 0.7409)
    - Fact Checked: Vaccines: Safe and Effective, No Link to Autism (weight: 0.6438)
    - Vaccines and autism: What does the evidence show? - Healio (weight: 0.5981)

---
## 7. "the moon landing was faked"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.997)

### Sources collected: 46 total
  - google_factcheck: 10
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 46 -> 30 (dropped 16)
Dropped sources:
  - [encyclopedia] "Man on the Moon (R.E.M. song)" (relevance: 0.3421, reason: relevance_0.342_below_0.35)
  - [encyclopedia] "Dark Side of the Moon (2002 film)" (relevance: 0.4795, reason: non_content_pattern)
  - [encyclopedia] "Copán La Leyenda" (relevance: 0.0517, reason: relevance_0.052_below_0.35)
  - [encyclopedia] "Moon theory" (relevance: 0.3173, reason: relevance_0.317_below_0.35)
  - [encyclopedia] "Operation Avalanche (film)" (relevance: 0.3792, reason: non_content_pattern)
  - [encyclopedia] "Tim Commerford" (relevance: -0.0236, reason: relevance_-0.024_below_0.35)
  - [encyclopedia] "United States UFO files" (relevance: 0.2179, reason: relevance_0.218_below_0.35)
  - [academic] "Of tinfoil hats and thinking caps: Reasoning is more strongly related to implausible than plausible conspiracy beliefs" (relevance: 0.3043, reason: relevance_0.304_below_0.35)
  - [academic] "Individual, intergroup and nation-level influences on belief in conspiracy theories" (relevance: 0.2616, reason: relevance_0.262_below_0.35)
  - [academic] "“If they believe, then so shall I”: Perceived beliefs of the in-group predict conspiracy theory belief" (relevance: 0.2255, reason: relevance_0.225_below_0.35)
  - [academic] "Misinformation of COVID-19 vaccines and vaccine hesitancy" (relevance: 0.1529, reason: relevance_0.153_below_0.35)
  - [academic] "The Relationship Between Social Media Use and Beliefs in Conspiracy Theories and Misinformation" (relevance: 0.3061, reason: relevance_0.306_below_0.35)
  - [academic] "Phytoestrogens (Resveratrol and Equol) for Estrogen-Deficient Skin—Controversies/Misinformation versus Anti-Aging In Vitro and Clinical Evidence via Nutraceutical-Cosmetics" (relevance: -0.0235, reason: relevance_-0.023_below_0.35)
  - [academic] "AI-generated characters for supporting personalized learning and well-being" (relevance: 0.1052, reason: relevance_0.105_below_0.35)
  - [knowledge_graph] "faked death" (relevance: 0.3295, reason: relevance_0.329_below_0.35)
  - [knowledge_graph] "false evidence" (relevance: 0.3352, reason: relevance_0.335_below_0.35)

### Dedup: 30 -> 29 (dropped 1)

### Analyzed sources (29 total)

**[google_factcheck] "Buzz Aldrin didn't 'admit' he never went to the Moon – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Buzz Aldrin admitted the Moon landings were faked in an interview...."

**[google_factcheck] "'Fake' moon landing claim orbits the simple facts"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Newspaper photos of the moon landing published on the same day could not have been transported and developed so quickly - proving the 1969 mission was..."

**[google_factcheck] "No, Wikileaks didn’t release evidence that the moon landing was faked"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "“Wikileaks releases moon landing cut scenes filmed in the Nevada desert.”..."

**[google_factcheck] "Media coverage post misleads about moon landing photos | Fact ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.65)
  Verdict contribution: opposing (weight: 0.325)
  Snippet: "Apollo 11 mission was faked because images appeared in newspapers day of..."

**[google_factcheck] "In 1969, the president called the astronauts on the moon. Here’s how"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "The phone President Richard Nixon used to talk to the first astronauts on the moon is evidence the 1969 moon landing was faked...."

**[google_factcheck] "Apollo 16 crew removed helmets at Kennedy Space Center | Fact ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Image shows NASA astronauts posing for picture on the moon without helmets..."

**[google_factcheck] "Fact check: Moon landing conspiracy theory misrepresents footprint"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Mismatch between a space boot and lunar footprint proves moon landing fake..."

**[google_factcheck] "AI-generated images falsely shared as 'proof the US faked Moon ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Photo proves US Moon landing is staged..."

**[google_factcheck] "Video clips don't show Buzz Aldrin admitting he never went to the ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Buzz Aldrin has admitted that he never went to the Moon...."

**[google_factcheck] "No. Buzz Aldrin didn't say the moon landing was a hoax."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Buzz Aldrin admitted that the moon landing “didn’t happen.”..."

**[wikipedia] "Moon landing conspiracy theories"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.8013)
  Verdict contribution: supporting (weight: 0.6811)
  Snippet: "Conspiracy theories claim that some or all elements of the Apollo program and the associated Moon landings were hoaxes staged by NASA, possibly with t..."

**[wikipedia] "Moon landing conspiracy theories in popular culture"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9697)
  Verdict contribution: supporting (weight: 0.7758)
  Snippet: "The notion that the Apollo Moon landings were hoaxes perpetrated by NASA and other agencies has appeared many times in popular culture. Not all refere..."

**[wikipedia] "Apollo 11"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): opposing (0.9731)
  Verdict contribution: opposing (weight: 0.9244)
  Snippet: "Apollo 11 (July 16–24, 1969) was the American spaceflight that first landed humans on the Moon, and the fifth crewed mission of NASA's Apollo program...."

**[open_alex] "Of Tinfoil Hats and Thinking Caps: Reasoning is More Strongly Related to Implausible than Plausible Conspiracy Beliefs"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.5489)
  Snippet: "People who strongly endorse conspiracy theories typically exhibit biases in domain-general reasoning. We describe an overfitting hypothesis, according..."

**[open_alex] "Conspiracy vs. Science: A Survey of U.S. Public Beliefs"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.5073)
  Verdict contribution: supporting (weight: 0.279)
  Snippet: "In this brief, author Lawrence Hamilton reports the results of a nationwide U.S. survey that asked respondents whether they agreed, disagreed, or were..."

**[open_alex] "Conspiracy Theories and Evidential Self-Insulation"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9272)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract What are conspiracy theories? And what, if anything, is epistemically wrong with them? This chapter offers an account on which conspiracy the..."

**[duckduckgo] "The moon landing was fake"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): neutral (0.8604)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Conspiracy theories claim that some or all elements of the Apollo program and the associated Moon landings were hoaxes staged by NASA, possibly with t..."

**[duckduckgo] "The Moon Landings Were Faked - Conspiracy Theories - TIME"**
  Type: web | Cred: estimated 0.47800000000000004
  NLI (nli_deberta): supporting (0.5254)
  Verdict contribution: supporting (weight: 0.2511)
  Snippet: "Doubters say the US government, desperate to beat the Russians in the space race, faked the lunar landings, with Armstrong and Buzz Aldrin acting out ..."

**[duckduckgo] "How do we know that we went to the Moon? - Institute of Physics"**
  Type: web | Cred: verified 0.95 | Factual: very high
  NLI (nli_deberta): opposing (0.8774)
  Verdict contribution: opposing (weight: 0.8335)
  Snippet: "With a powerful amateur telescope you can see the Apollo landing sites and, if you look at the photos from the Lunar Reconnaissance Orbiter, you can s..."

**[duckduckgo] "What's some irrefutable evidence of the moon landing? : r/space - Reddit"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.9453)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Apr 5, 2017 · I was recently in two discussion about the moon landing and if it happened or not. In both cases they were sure it didn't happen and one..."

**[duckduckgo] "News: Why do people believe the moon landing... (The Washington ..."**
  Type: web | Cred: estimated 0.44400000000000006
  NLI (nli_deberta): supporting (0.8721)
  Verdict contribution: supporting (weight: 0.3872)
  Snippet: "(The Washington Post) Why do people believe the moon landing hoax or other conspiracy theories?. Associated research findings from the National Librar..."

**[duckduckgo] "The Moon Landing Hoax - Digital Commons @ Butler University"**
  Type: web | Cred: estimated 0.43
  NLI (nli_deberta): neutral (0.8711)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Space Race was a highly contested period of the 20th century between the United States and Soviet Union. The overarching goal was to see which cou..."

**[duckduckgo] "Were the Moon Conspiracy Theories Faked? | Andy Borowitz | Episode 3"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9526)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Oct 14, 2019 · New Yorker magazine humorist Andy Borowitz looks at the evolution of the myth that the moon landing was faked, as well as other truth-a..."

**[duckduckgo] "Moon landing conspiracy theories | Communication and Mass Media"**
  Type: web | Cred: estimated 0.40700000000000003
  NLI (nli_deberta): opposing (0.8237)
  Verdict contribution: opposing (weight: 0.3352)
  Snippet: "Moon landing conspiracy theories emerged shortly after the Apollo 11 mission successfully landed astronauts on the lunar surface in 1969...."

**[duckduckgo] "Watch Conspiracy Theory: Did We Land On The Moon? | Netflix"**
  Type: web | Cred: estimated 0.493
  NLI (nli_deberta): supporting (0.6846)
  Verdict contribution: supporting (weight: 0.3375)
  Snippet: "Skeptics and experts discuss photographs and other evidence that suggest the United States government faked NASA's moon landings for political gain...."

**[wikidata] "Moon landing"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "arrival of a spacecraft on the surface of the Moon | instance of: occurrence..."

**[wikidata] "Moon Landing"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "album by James Blunt | instance of: album..."

**[wikidata] "Moon Landing"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "album by Sivert Høyem | instance of: album..."

**[wikidata] "faked death"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "case in which an individual leaves evidence to suggest that they are dead | instance of: Wikibase reason for deprecated rank..."

### Verdict computation
  Supporting weight: 3.2606
  Opposing weight: 6.1232
  Support ratio: 0.3475
  Confidence: 0.3051
  Verdict: **likely opposed**
  Neutral sources (no contribution): 13

  Top supporting:
    - Moon landing conspiracy theories in popular culture (weight: 0.7758)
    - Moon landing conspiracy theories (weight: 0.6811)
    - Of Tinfoil Hats and Thinking Caps: Reasoning is More Strongly Related to Implausible than Plausible Conspiracy Beliefs (weight: 0.5489)
    - News: Why do people believe the moon landing... (The Washington ... (weight: 0.3872)
    - Watch Conspiracy Theory: Did We Land On The Moon? | Netflix (weight: 0.3375)
  Top opposing:
    - Apollo 11 (weight: 0.9244)
    - How do we know that we went to the Moon? - Institute of Physics (weight: 0.8335)
    - 'Fake' moon landing claim orbits the simple facts (weight: 0.8075)
    - In 1969, the president called the astronauts on the moon. Here’s how (weight: 0.8075)
    - AI-generated images falsely shared as 'proof the US faked Moon ... (weight: 0.8075)

---
## 8. "5G causes COVID"
Category: factual_false
Expected: strongly opposed
Actual: strongly opposed (YES)
Claim type: factual (0.9962)

### Sources collected: 50 total
  - google_factcheck: 10
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 50 -> 30 (dropped 20)
Dropped sources:
  - [encyclopedia] "COVID-19 misinformation" (relevance: 0.2805, reason: relevance_0.280_below_0.35)
  - [encyclopedia] "Cristiano Amon" (relevance: 0.1532, reason: relevance_0.153_below_0.35)
  - [encyclopedia] "Thomas Cowan (alternative medicine practitioner)" (relevance: 0.0247, reason: relevance_0.025_below_0.35)
  - [encyclopedia] "Sacha Stone" (relevance: 0.0297, reason: relevance_0.030_below_0.35)
  - [encyclopedia] "Kate Shemirani" (relevance: 0.2225, reason: relevance_0.223_below_0.35)
  - [encyclopedia] "Mark Steele (conspiracy theorist)" (relevance: 0.2027, reason: relevance_0.203_below_0.35)
  - [encyclopedia] "COVID-19 pandemic in South Africa" (relevance: 0.3062, reason: relevance_0.306_below_0.35)
  - [academic] "Medical disinformation and the unviable nature of COVID-19 conspiracy theories" (relevance: 0.2981, reason: relevance_0.298_below_0.35)
  - [academic] "How to Improve the Management of Acute Ischemic Stroke by Modern Technologies, Artificial Intelligence, and New Treatment Methods" (relevance: 0.1005, reason: relevance_0.100_below_0.35)
  - [academic] "Pathophysiological involvement of host mitochondria in SARS-CoV-2 infection that causes COVID-19: a comprehensive evidential insight" (relevance: 0.1713, reason: relevance_0.171_below_0.35)
  - [academic] "SARS-CoV-2: The Monster Causes COVID-19" (relevance: 0.3049, reason: relevance_0.305_below_0.35)
  - [academic] "CANCOV- Canadian Prospective Cohort of 1-year Outcomes in Critically Ill Patients With COVID-19 and Their Family Caregivers - Preliminary Report on Causes of Death in the ICU Cohort" (relevance: 0.1468, reason: relevance_0.147_below_0.35)
  - [academic] "Medical disinformation and the unviable nature of COVID-19 conspiracy theories" (relevance: 0.2981, reason: relevance_0.298_below_0.35)
  - [academic] "Different Conspiracy Theories Have Different Psychological and Social Determinants: Comparison of Three Theories About the Origins of the COVID-19 Virus in a Representative Sample of the UK Population" (relevance: 0.2987, reason: relevance_0.299_below_0.35)
  - [academic] "Knowledge, Attitudes, Practices, and Misconceptions towards COVID-19 among Sub-Sahara Africans" (relevance: 0.2648, reason: relevance_0.265_below_0.35)
  - [academic] "Pandemic Management for Diseases Similar to COVID-19 Using Deep Learning and 5G Communications" (relevance: 0.2799, reason: relevance_0.280_below_0.35)
  - [academic] "The real economic costs of COVID-19: Insights from electricity consumption data in Hunan Province, China" (relevance: 0.3154, reason: relevance_0.315_below_0.35)
  - [academic] "Next-generation nanophotonic-enabled biosensors for intelligent diagnosis of SARS-CoV-2 variants" (relevance: 0.1099, reason: relevance_0.110_below_0.35)
  - [academic] "GNPy model of the physical layer for open and disaggregated optical networking [Invited]" (relevance: 0.1836, reason: relevance_0.184_below_0.35)
  - [academic] "Characterizing the roles of bots on Twitter during the COVID-19 infodemic" (relevance: 0.1874, reason: relevance_0.187_below_0.35)

### Dedup: 30 -> 25 (dropped 5)

### Analyzed sources (25 total)

**[google_factcheck] "These claims about the new coronavirus and 5G are unfounded ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Bill Gates created the new coronavirus and a vaccine for it...."

**[google_factcheck] "The EG.5 variant of Covid-19 has nothing to do with 5G – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The EG.5 variant of Covid-19 is a new 5G virus...."

**[google_factcheck] "Viral claim falsely asserts that COVID-19 is due to 5G technology ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The coronavirus outbreak is not actually caused by a virus, but by 5G technology..."

**[google_factcheck] "Social media clips revive false claims by David Icke linking 5G and ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "5G at 60 GHz “stops the human body and blood absorbing oxygen”; this is what doctors are describing in COVID-19 cases..."

**[google_factcheck] "Hoax linking Covid-19 to bacteria and 5G mobile technology ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Covid-19 is bacterial, not viral..."

**[google_factcheck] "Fresh false claims about COVID-19 vaccine and 5G technology ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "COVID-19 means 'certificate of vaccination identity', leading to a mass vaccination effort which, alongside the rollout of 5G, weakens the immune syst..."

**[wikipedia] "5G misinformation"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.9922)
  Verdict contribution: opposing (weight: 0.7938)
  Snippet: "Misinformation related to 5G telecommunications technology is widespread in many countries of the world. The spreading of false information and conspi..."

**[wikipedia] "5G"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8477)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "5G is the fifth generation of cellular network technology and the successor to 4G. In common commercial use, the term refers primarily to mobile netwo..."

**[wikipedia] "Concerns over Chinese involvement in 5G wireless networks"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8779)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Concerns over Chinese involvement in 5G wireless networks stem from allegations that cellular network equipment sourced from vendors from the People's..."

**[semantic_scholar] "Comparative Analysis of Max-Throughput and Proportional Fair Scheduling Algorithms in 5G Networks"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.3988)
  Snippet: "Mobile network service use is growing, especially after the Covid-19 pandemic. To improve the quality of mobile network services, 5G comes as a networ..."

**[semantic_scholar] "Progressive Use of IoT and 5G Network-Based Systems Post COVID-19 Pandemic"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.399)
  Snippet: "The outbreak of COVID-19 has led to a reduction in a number of services and activities, but it has also accelerated the development of communication a..."

**[semantic_scholar] "Covid-19 Conspiracy Theories: QAnon, 5G, the New World Order and Other Viral Ideas"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.979)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Covid-19 Conspiracy Theories: QAnon, 5G, the New World Order and Other Viral Ideas..."

**[semantic_scholar] "Review of 5G Wireless Cellular Network on Covid-19 Pandemic: Digital Healthcare & Challenges"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.5484)
  Snippet: "Since the coronavirus disease (COVID-19) began in 2020, it has changed the way people live such as social life and healthcare. One of the simplest way..."

**[semantic_scholar] "5G in Healthcare: From COVID-19 to Future Challenges"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.6484)
  Snippet: "Worldwide up to May 2022 there have been 515 million cases of COVID-19 infection and over 6 million deaths. The World Health Organization estimated th..."

**[open_alex] "Could 5G Technology Be the Cause of COVID-19?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9053)
  Verdict contribution: opposing (weight: 0.4979)
  Snippet: "The burning of 5G sites across the UK in April 2020 has shocked the scientific and industrial society in the UK. The UK's mobile networks have reporte..."

**[open_alex] "Covering Conspiracy: Approaches to Reporting the COVID/5G Conspiracy Theory"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9209)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Conspiracy theories about the ‘real’ origins of the coronavirus have co-evolved with media coverage of the COVID-19 crisis itself; the World Health Or..."

**[duckduckgo] "5G Doesn't Cause COVID-19, But the Rumor It Does Spread Like a Virus | SPH"**
  Type: web | Cred: estimated 0.41600000000000004
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.4154)
  Snippet: "A version of this article was originally published on the Boston University Hariri Institute News site. People's fear of 5G technology is rational. Su..."

**[duckduckgo] "Spreading Like a Virus: False Rumor That 5G Causes COVID-19"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.731)
  Verdict contribution: opposing (weight: 0.6213)
  Snippet: "Credit: Nsoesie et al., 2020 Why 5G Myths Persist Even though 5G technology isn't entirely new, there are a few reasons why people might have believed..."

**[duckduckgo] "Does 5g cause covid19 - factually.co"**
  Type: web | Cred: estimated 0.325
  NLI (nli_deberta): opposing (0.8296)
  Verdict contribution: opposing (weight: 0.2696)
  Snippet: "Treat claims that 5G causes COVID‑19 as a debunked conspiracy supported by social‑media circulation rather than by laboratory science; focus on establ..."

**[duckduckgo] "The people who think coronavirus is caused by 5G - BBC"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9443)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The people who think coronavirus is caused by 5G The idea that 5G could have health implications isn't new. But conspiracy theories linking 5G with Co..."

**[duckduckgo] "5G Conspiracy Theories Debunked: Separating Fact from Fiction"**
  Type: web | Cred: estimated 0.40199999999999997
  NLI (nli_deberta): neutral (0.7925)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "5G Conspiracy Theories during the Covid-19 Pandemic During the Covid-19 pandemic, a surge of conspiracy theories appeared linking 5G technology to the..."

**[duckduckgo] "Is 5G Safe? Here's What Experts Say - Forbes Health"**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9194)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Claims state 5G weakens the immune system, making it easier to contract COVID-19, or that it directly causes the virus. Simply put, research emphasize..."

**[duckduckgo] "5G and coronavirus: Debunking the fake news stories - BBC"**
  Type: web | Cred: estimated 0.47400000000000003
  NLI (nli_deberta): neutral (0.7739)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Looking at why fake news stories linking coronavirus to 5G have spread so fast, and why these stories are false...."

**[duckduckgo] "Why Inaccurate 5G Coronavirus Conspiracy Theories Spread - TIME"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): opposing (0.7378)
  Verdict contribution: opposing (weight: 0.6271)
  Snippet: "When the coronavirus spread around the world, conspiracy theorists started spreading inaccurate theories about 5G. Here's how platforms are cracking d..."

**[duckduckgo] "5G technology does not cause or spread coronavirus - UNICEF"**
  Type: web | Cred: estimated 0.43899999999999995
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.4377)
  Snippet: "5G technology does not cause or spread coronavirus This conspiracy theory is more often believed by those who do not use the internet (47%), which ind..."

### Verdict computation
  Supporting weight: 0.765
  Opposing weight: 5.6576
  Support ratio: 0.1191
  Confidence: 0.7618
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 13

  Top supporting:
    - Fresh false claims about COVID-19 vaccine and 5G technology ... (weight: 0.765)
  Top opposing:
    - 5G misinformation (weight: 0.7938)
    - 5G in Healthcare: From COVID-19 to Future Challenges (weight: 0.6484)
    - Why Inaccurate 5G Coronavirus Conspiracy Theories Spread - TIME (weight: 0.6271)
    - Spreading Like a Virus: False Rumor That 5G Causes COVID-19 (weight: 0.6213)
    - Review of 5G Wireless Cellular Network on Covid-19 Pandemic: Digital Healthcare & Challenges (weight: 0.5484)

---
## 9. "LeBron James is the greatest basketball player of all time"
Category: opinion
Expected: opinion
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.9979)

### Sources collected: 37 total
  - google_factcheck: 1
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 37 -> 22 (dropped 15)
Dropped sources:
  - [encyclopedia] "GOAT (sports culture)" (relevance: 0.3094, reason: relevance_0.309_below_0.35)
  - [encyclopedia] "2026 NBA playoffs" (relevance: 0.1921, reason: relevance_0.192_below_0.35)
  - [academic] "Sports Analytics: Data Mining to Uncover NBA Player Position, Age, and Injury Impact on Performance and Economics" (relevance: 0.2684, reason: relevance_0.268_below_0.35)
  - [academic] "Commercial aspects of personal branding of athletes on social networks" (relevance: 0.2042, reason: relevance_0.204_below_0.35)
  - [academic] "A <i>wen-wu</i> Approach to Male Teenage Chinese Sports Fans’ Heteronormative Interpretation of Masculinity" (relevance: 0.1826, reason: relevance_0.183_below_0.35)
  - [academic] "Competitive spirit as a form of behavioral addiction: the case study of Michael Jordan" (relevance: 0.3257, reason: relevance_0.326_below_0.35)
  - [academic] "The National Basketball Association’s (NBA) Digital Transformation: An Explanatory Case Study" (relevance: 0.3176, reason: relevance_0.318_below_0.35)
  - [academic] "Sustainability in Sport: Sport, Part of the Problem … and of the Solution" (relevance: 0.2122, reason: relevance_0.212_below_0.35)
  - [academic] "Inside the NBA Bubble: how Black players performed better without fans" (relevance: 0.2502, reason: relevance_0.250_below_0.35)
  - [academic] "Music in sport: From conceptual underpinnings to applications" (relevance: 0.1101, reason: relevance_0.110_below_0.35)
  - [academic] "Sports, Brand America and U.S. public diplomacy during the presidency of Donald Trump" (relevance: 0.1473, reason: relevance_0.147_below_0.35)
  - [academic] "Athlete Activists, Sports Diplomats and Human Rights: Action versus Agency" (relevance: 0.1911, reason: relevance_0.191_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.053, reason: relevance_0.053_below_0.35)
  - [knowledge_graph] "time" (relevance: 0.1677, reason: relevance_0.168_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.0644, reason: relevance_0.064_below_0.35)

### Dedup: 22 -> 21 (dropped 1)

### Analyzed sources (21 total)

**[google_factcheck] "Did Michael Jordan Call LeBron James the Greatest Basketball ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Michael Jordan said that LeBron James was the greatest basketball player of all time...."

**[wikipedia] "LeBron James"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "LeBron Raymone James ( lə-BRON; born December 30, 1984) is an American professional basketball player for the Los Angeles Lakers of the National Baske..."

**[wikipedia] "NBA 75th Anniversary Team"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The NBA 75th Anniversary Team, also referred to as the NBA 75, was chosen in 2021 to honor the 75th anniversary of the founding of the National Basket..."

**[wikipedia] "List of career achievements by LeBron James"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The American professional basketball player LeBron James began his career in the National Basketball Association (NBA) when he was selected by the Cle..."

**[wikipedia] "50 Greatest Players in NBA History"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The 50 Greatest Players in NBA History, also referred to as NBA's 50th Anniversary All-Time Team, were chosen in 1996 to honor the 50th anniversary of..."

**[wikipedia] "The Block (basketball)"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Block was a defensive basketball play that occurred in Game 7 of the 2016 NBA Finals, played between the Cleveland Cavaliers and Golden State Warr..."

**[wikipedia] "Kawhi Leonard"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Kawhi Anthony Leonard ( kə-WHY; born June 29, 1991) is an American professional basketball player for the Los Angeles Clippers of the National Basketb..."

**[wikipedia] "2016 NBA Finals"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The 2016 NBA Finals was the championship series of the National Basketball Association's (NBA) 2015–16 season and conclusion of the season's playoffs...."

**[wikipedia] "List of sports figures considered the greatest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In sports, spectators including sports fandom and sportswriters, as well as participants themselves have discussed players, coaches, teams, and relate..."

**[duckduckgo] "Let's end this debate. Is Lebron the greatest basketball player of all time."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.6323)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Mar 3, 2024 · My opinion after seeing all 3 play is that LBJ is the best and most complete basketball player of all time without a doubt.Lebron is arg..."

**[duckduckgo] "LeBron James is the greatest of all time - The Quinnipiac Chronicle"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): neutral (0.9756)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Oct 28, 2025 · 23 for the Los Angeles Lakers, forward LeBron James is one of two players in the modern-day debate of the greatest basketball player of..."

**[duckduckgo] "LeBron James has had 'the greatest career of any NBA player,' says JJ ..."**
  Type: web | Cred: estimated 0.5269999999999999
  NLI (nli_deberta): neutral (0.9844)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "May 1, 2026 · "To me he's had the greatest career of any NBA player. You can argue all you want, and I really don't care to postulate on who's the gre..."

**[duckduckgo] "Lebron is the greatest basketball player of all time - Facebook"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9346)
  Verdict contribution: supporting (weight: 0.4673)
  Snippet: "Nov 13, 2025 · He gave us unforgettable moments and six rings. But LeBron James is the most complete basketball player the game has ever seen. He has ..."

**[duckduckgo] "Sorry, Michael—LeBron James is the Greatest Basketball Player of All Time"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.9849)
  Verdict contribution: supporting (weight: 0.4924)
  Snippet: "Mar 11, 2019 · The debate is over. LeBron James is the greatest basketball player in history. His closest competitor, Michael Jordan, has been vanquis..."

**[duckduckgo] "LeBron James Is the Greatest of All Time - Sports Illustrated"**
  Type: web | Cred: estimated 0.421
  NLI (nli_deberta): neutral (0.9893)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Feb 8, 2023 · In 20 NBA seasons, though, James has done more. Four NBA championships. Four MVPs. More points in the playoffs than any player in NBA hi..."

**[duckduckgo] "Why is Lebron James the best player in the NBA, and one of the greatest ..."**
  Type: web | Cred: estimated 0.487
  NLI (nli_deberta): neutral (0.9712)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jul 31, 2018 · Lebron is universally regarded as a top-ten player of all time largely because he was clearly the best player in the league for several..."

**[duckduckgo] "NBA fans witness Lebron James, the greatest player in a generation"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9927)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "LeBron has the most complete game of any basketball player I've ever seen. He's so efficient and the stats back it up...."

**[duckduckgo] "The 10 Greatest Basketball Players of All Time | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9717)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "LeBron James overtook Kareem Abdul-Jabbar as the NBA's leading scorer in February 2023. (Read James Naismith's 1929 Britannica essay on his invention ..."

**[wikidata] "LeBron James"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "American basketball player (born 1984) | instance of: human | country of citizenship: United States | place of birth: Akron | date of birth: December ..."

**[wikidata] "LeBron James"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "fictional character in Teen Titans Go! The Simpsons, Trainwreck, The Cleveland Show, Entourage, SpongeBob SquarePants, Space Jam: A New Legacy, House ..."

**[wikidata] "lebron james"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "species of plant | instance of: taxon..."

### Verdict computation
  Supporting weight: 0.9597
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 19

  Top supporting:
    - Sorry, Michael—LeBron James is the Greatest Basketball Player of All Time (weight: 0.4924)
    - Lebron is the greatest basketball player of all time - Facebook (weight: 0.4673)

---
## 10. "pineapple belongs on pizza"
Category: opinion
Expected: opinion
Actual: likely supported (**NO - MISMATCH**)
Claim type: factual (0.9885)

### Sources collected: 33 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 33 -> 13 (dropped 20)
Dropped sources:
  - [encyclopedia] "Cheung Ka Long" (relevance: 0.0205, reason: relevance_0.021_below_0.35)
  - [encyclopedia] "Concerns and controversies at the 2024 Summer Olympics" (relevance: -0.0795, reason: relevance_-0.079_below_0.35)
  - [encyclopedia] "Vargskelethor Joel" (relevance: 0.0702, reason: relevance_0.070_below_0.35)
  - [encyclopedia] "Brazilian cuisine" (relevance: 0.1971, reason: relevance_0.197_below_0.35)
  - [encyclopedia] "MasterChef Australia series 17" (relevance: -0.094, reason: relevance_-0.094_below_0.35)
  - [encyclopedia] "Hell's Kitchen (American TV series) season 23" (relevance: 0.0956, reason: relevance_0.096_below_0.35)
  - [encyclopedia] "Agriculture in Taiwan" (relevance: 0.0222, reason: relevance_0.022_below_0.35)
  - [encyclopedia] "SpongeBob SquarePants season 1" (relevance: 0.1015, reason: relevance_0.102_below_0.35)
  - [encyclopedia] "Hell's Kitchen (American TV series) season 9" (relevance: 0.022, reason: relevance_0.022_below_0.35)
  - [encyclopedia] "The Great British Bake Off series 13" (relevance: 0.0212, reason: relevance_0.021_below_0.35)
  - [academic] "The cosmetic dentistry rush" (relevance: 0.0371, reason: relevance_0.037_below_0.35)
  - [academic] "Application of Artificial Intelligence in Food Industry—a Guideline" (relevance: 0.1746, reason: relevance_0.175_below_0.35)
  - [academic] "Americans misperceive the frequency and format of political debate" (relevance: -0.0036, reason: relevance_-0.004_below_0.35)
  - [academic] "Managing Bad News in Social Media: A Case Study on Domino’s Pizza Crisis" (relevance: 0.2491, reason: relevance_0.249_below_0.35)
  - [academic] "Nutritional Composition, Antinutritional Factors, and Utilization Trends of Ethiopian Chickpea (Cicer arietinum L.)" (relevance: 0.185, reason: relevance_0.185_below_0.35)
  - [academic] "Biodiesel Production From Lignocellulosic Biomass Using Oleaginous Microbes: Prospects for Integrated Biofuel Production" (relevance: 0.1238, reason: relevance_0.124_below_0.35)
  - [academic] "Migration of Chemical Compounds from Packaging Materials into Packaged Foods: Interaction, Mechanism, Assessment, and Regulations" (relevance: 0.1445, reason: relevance_0.144_below_0.35)
  - [academic] "The future of food tourism in a post-COVID-19 world: insights from New Zealand" (relevance: 0.1934, reason: relevance_0.193_below_0.35)
  - [academic] "Polyphenols: Natural Preservatives with Promising Applications in Food, Cosmetics and Pharma Industries; Problems and Toxicity Associated with Synthetic Preservatives; Impact of Misleading Advertisements; Recent Trends in Preservation and Legislation" (relevance: 0.1912, reason: relevance_0.191_below_0.35)
  - [academic] "Categorizing Social Media Screenshots for Identifying Author Misattribution" (relevance: 0.1241, reason: relevance_0.124_below_0.35)

### Dedup: 13 -> 13 (dropped 0)

### Analyzed sources (13 total)

**[duckduckgo] "We Asked 3 Chefs if Pineapple Belongs on Pizza, and They All Said the Same Thing"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): supporting (0.9839)
  Verdict contribution: supporting (weight: 0.4113)
  Snippet: "May 10, 2024 - The first two points are easily ... to personal preference. At the end of the day, you can love or hate it, but yes, pineapple belongs ..."

**[duckduckgo] "Does Pineapple Belong on Pizza | Made in New York Pizza"**
  Type: web | Cred: estimated 0.248
  NLI (nli_deberta): supporting (0.9639)
  Verdict contribution: supporting (weight: 0.239)
  Snippet: "April 10, 2025 - It all began in 1962 when Sam ... but people loved the contrast, and he eventually called it the Hawaiian Pizza. First, scientific ev..."

**[duckduckgo] "Does Pineapple Belong on Pizza?︱Salerno’s Pizza"**
  Type: web | Cred: estimated 0.251
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.2503)
  Snippet: "January 5, 2024 - It’s commonly baked and grilled, but apart from this dish, it’s rarely paired with cheese. Celebrity chef Gordon Ramsay once said, “..."

**[duckduckgo] "Pineapple doesn't belong on pizza - The Emery"**
  Type: web | Cred: estimated 0.399
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.3984)
  Snippet: "No, pineapple does not belong on pizza...."

**[duckduckgo] "Simply Souperlicious – Pineapple ON Pizza: The Final Argument"**
  Type: web | Cred: estimated 0.23700000000000002
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.2355)
  Snippet: "October 27, 2021 - If you have had any kind of online presence and are interested in food, you’ve probably noticed that the debate on pineapple and pi..."

**[duckduckgo] "Pineapple doesn't belong on pizza - Beaver Tales"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): opposing (0.998)
  Verdict contribution: opposing (weight: 0.1996)
  Snippet: "Pineapple is sweet and juicy; it’s not meant to be put on something that is warm and cheesy. Think about a strawberry. Would a sweet strawberry be goo..."

**[duckduckgo] "Does pineapple belong on pizza? The science behind food pairings | Sensory & Consumer Science |Science Meets Food"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.6543)
  Verdict contribution: supporting (weight: 0.2637)
  Snippet: "November 3, 2021 - By Aishwarya Badiger They say food ... pizza. The origins of using pineapple as a pizza topping began in 1962 Canada when Sam Panop..."

**[duckduckgo] "Ending the Debate: Why Pineapple Belongs on Pizza"**
  Type: web | Cred: estimated 0.446
  NLI (nli_deberta): supporting (0.8711)
  Verdict contribution: supporting (weight: 0.3885)
  Snippet: "August 7, 2023 - However, to some others the pizza ... Trudeau weighed in on the topic on twitter: First of all, it is scientifically proven that pine..."

**[duckduckgo] "Benefits of Pineapple on Pizza - Pineapple Pizza Recipe"**
  Type: web | Cred: estimated 0.337
  NLI (nli_deberta): neutral (0.7915)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Join our list → ⭐ free shipping all Steels in the contiguous usa ... Pineapple on pizza might be the most controversial topping in history. Some swear..."

**[duckduckgo] "Why pineapple belongs on pizza — Domino's Newsroom"**
  Type: web | Cred: estimated 0.34199999999999997
  NLI (nli_deberta): supporting (0.9829)
  Verdict contribution: supporting (weight: 0.3362)
  Snippet: "January 26, 2020 - I mean, if we can all accept a slimy anchovy why can’t we accept a humble slice of pineapple!? ... Understanding that the precursor..."

**[wikidata] "pizza"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Italian universal popular dish with a flat dough-based base and toppings | instance of: type of food or dish..."

**[wikidata] "Pizza"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "1981 album by Alain Bashung | instance of: album..."

**[wikidata] "Pizza"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "article in Otto's encyclopedia | instance of: encyclopedia article..."

### Verdict computation
  Supporting weight: 1.8742
  Opposing weight: 0.8483
  Support ratio: 0.6884
  Confidence: 0.3768
  Verdict: **likely supported**
  Neutral sources (no contribution): 4

  Top supporting:
    - We Asked 3 Chefs if Pineapple Belongs on Pizza, and They All Said the Same Thing (weight: 0.4113)
    - Ending the Debate: Why Pineapple Belongs on Pizza (weight: 0.3885)
    - Why pineapple belongs on pizza — Domino's Newsroom (weight: 0.3362)
    - Does pineapple belong on pizza? The science behind food pairings | Sensory & Consumer Science |Science Meets Food (weight: 0.2637)
    - Does Pineapple Belong on Pizza | Made in New York Pizza (weight: 0.239)
  Top opposing:
    - Pineapple doesn't belong on pizza - The Emery (weight: 0.3984)
    - Does Pineapple Belong on Pizza?︱Salerno’s Pizza (weight: 0.2503)
    - Pineapple doesn't belong on pizza - Beaver Tales (weight: 0.1996)

---
## 11. "democracy is the best form of government"
Category: opinion
Expected: opinion
Actual: likely opposed (**NO - MISMATCH**)
Claim type: factual (0.9978)

### Sources collected: 41 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 2
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 41 -> 31 (dropped 10)
Dropped sources:
  - [encyclopedia] "Hans-Adam II, Prince of Liechtenstein" (relevance: -0.0645, reason: relevance_-0.065_below_0.35)
  - [academic] "An Approach to Pediatric or Mentally Deficient Donors from a Bioethical Perspective: Considerations and Recommendations on Behalf of the Donor Research Team of the Turkish Society of Hematology (DART)" (relevance: 0.0524, reason: relevance_0.052_below_0.35)
  - [academic] "A global panel database of pandemic policies (Oxford COVID-19 Government Response Tracker)" (relevance: 0.1123, reason: relevance_0.112_below_0.35)
  - [academic] "How polarization, populist attitudes, and cultural backlash affect citizens’ support for democracy: Evidence from Spain" (relevance: 0.3393, reason: relevance_0.339_below_0.35)
  - [knowledge_graph] "Democracy Club" (relevance: 0.3225, reason: relevance_0.323_below_0.35)
  - [knowledge_graph] "Best forms of involvement for first-year student veterans for academic success" (relevance: 0.1212, reason: relevance_0.121_below_0.35)
  - [knowledge_graph] "BEST Form of CARDIO | Fastest | Fat Loss" (relevance: 0.1212, reason: relevance_0.121_below_0.35)
  - [knowledge_graph] "Q120472867" (relevance: -0.0351, reason: relevance_-0.035_below_0.35)
  - [knowledge_graph] "public school" (relevance: 0.2046, reason: relevance_0.205_below_0.35)
  - [knowledge_graph] "civil servant" (relevance: 0.1244, reason: relevance_0.124_below_0.35)

### Dedup: 31 -> 29 (dropped 2)

### Analyzed sources (29 total)

**[wikipedia] "Democracy"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Democracy is a form of government in which political power is vested in the people or the population of a state. Under a minimalist definition of demo..."

**[wikipedia] "Mixed government"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Mixed government, or mixed constitution, is a form of government that combines elements of democracy, aristocracy, and monarchy, ostensibly making imp..."

**[wikipedia] "List of forms of government"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This article lists forms of government and political systems, which are not mutually exclusive, and often have much in common. According to Yale profe..."

**[wikipedia] "Criticism of democracy"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.848)
  Snippet: "Democracy as a concept and as a practical form of government has been the subject of critique throughout history. Some critics consider that democrati..."

**[wikipedia] "Types of democracy"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Types of democracy refers to the various governance structures that embody the principles of democracy ("rule by the people") in some way. Democracy i..."

**[wikipedia] "Republic"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A republic, based on the Latin phrase res publica ('public thing' or 'people's thing'), is a state in which political power rests with the public (peo..."

**[wikipedia] "Participatory democracy"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Participatory democracy, participant democracy, participative democracy, or semi-direct democracy is a form of government in which citizens participat..."

**[wikipedia] "New Democracy (Greece)"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "New Democracy is a liberal-conservative political party in Greece. In contemporary Greek politics, New Democracy has been the main centre-right to rig..."

**[wikipedia] "Parliamentary system"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A parliamentary system is a form of government based on the fusion of powers. In this system the head of government (chief executive) derives their de..."

**[semantic_scholar] "Democracy and Development in Africa: Demystifying Democracy as the Best Form of Government"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9883)
  Verdict contribution: opposing (weight: 0.3953)
  Snippet: "The resurgence of coups d’etat in Africa has resuscitated discussions about the suitability of democracy as an agent of development on the Continent. ..."

**[open_alex] "Why Ukrainians Are Rallying Around Democracy"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.98)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In democratizing countries it seems to make sense that any prolonged crisis will turn citizens away from democracy, from its "rules of the game," and ..."

**[open_alex] "Democracy and Development in Africa: Demystifying Democracy as the Best Form of Government"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9883)
  Verdict contribution: opposing (weight: 0.3953)
  Snippet: "The resurgence of coups d’etat in Africa has resuscitated discussions about the suitability of democracy as an agent of development on the Continent. ..."

**[open_alex] "Generational and Ideological Gaps in Democratic Support: Seeds of Deconsolidation in Post-Crisis Southern Europe?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This article explores trends in overall levels of democratic support in Portugal, Spain, Italy, and Greece. Additionally, the article examines the ext..."

**[open_alex] "Democratic Design"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract The twenty-first century poses serious challenges to democratic ideals and institutions. Democratic Design argues that to respond effectively..."

**[open_alex] "Does crime breed authoritarianism? Crime exposure, democratic decoupling and political attitudes in Brazil"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9072)
  Verdict contribution: supporting (weight: 0.499)
  Snippet: "Abstract How does crime influence democratic attitudes and behaviors? Existing research offers conflicting answers: some argue that crime fosters anti..."

**[open_alex] "Politics, planning, and ruling: the art of taming public participation"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Public participation is still a democratic challenge to city and municipal governments. Numerous studies have suggested experiments on participative p..."

**[open_alex] "Trust made the difference for democracies in COVID-19"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Trust made the difference for democracies in COVID-19..."

**[open_alex] "Defending democracy: Militant and popular models of democratic self‐defense"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.7163)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With the electoral victories of authoritarian populists in a range of parliamentary democracies in recent years, there has been a growing unease with ..."

**[duckduckgo] "Why Democracy Is Best | Tulanian"**
  Type: web | Cred: estimated 0.399
  NLI (nli_deberta): neutral (0.9033)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The democratic recession raises important questions about the best form of government. The most consequential of these questions is also the most basi..."

**[duckduckgo] "Democracy Is The Best Form Of Government: Arguments For ... - WorldAtlas"**
  Type: web | Cred: estimated 0.413
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Here are some of the pros and cons of democracy, which is one of the most popular forms of government around the world. Countries that use democracy a..."

**[duckduckgo] "Why democracy is still the best form of government"**
  Type: web | Cred: estimated 0.48200000000000004
  NLI (nli_deberta): neutral (0.564)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With scandal, corruption and nationalism on the rise, it's easy to feel a sense of despair about the state of democracy. But is the alternative any be..."

**[duckduckgo] "Democracy - Equality, Representation, Participation | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9175)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Democracy - Equality, Representation, Participation: Why should "the people" rule? Is democracy really superior to any other form of government? Altho..."

**[duckduckgo] "The importance of democracy - Chatham House"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): supporting (0.6719)
  Verdict contribution: supporting (weight: 0.5711)
  Snippet: "Why democracy is the best form of government Liberal democracy, in theory at least, provides a mechanism for some form of rule by proportionate repres..."

**[duckduckgo] "Which Form of Government Is Best? - Kellogg Insight"**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): opposing (0.6445)
  Verdict contribution: opposing (weight: 0.2939)
  Snippet: "Is Democracy the Best Form of Government? "A common notion is that a democracy should be superior to dictatorships because they are able to select the..."

**[duckduckgo] "Why Democracy is the Best We've Got - Carnegie Council for Ethics in ..."**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Democracy is a system of government in which the citizens of a nation determine its policies through elected representatives, direct voting, or in mos..."

**[duckduckgo] "26 Democracy Pros and Cons (2026) - Helpful Professor"**
  Type: web | Cred: estimated 0.43
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Democracy is a form of government in which all eligible citizens have an equal vote in selecting its own leaders. It is often called "rule by the peop..."

**[wikidata] "democracy"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "form of government | instance of: form of government..."

**[wikidata] "Democracy"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "instance of: book..."

**[wikidata] "government"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "system or group of people governing an organized community, often a state | instance of: type of organization..."

### Verdict computation
  Supporting weight: 1.0701
  Opposing weight: 1.9325
  Support ratio: 0.3564
  Confidence: 0.2872
  Verdict: **likely opposed**
  Neutral sources (no contribution): 23

  Top supporting:
    - The importance of democracy - Chatham House (weight: 0.5711)
    - Does crime breed authoritarianism? Crime exposure, democratic decoupling and political attitudes in Brazil (weight: 0.499)
  Top opposing:
    - Criticism of democracy (weight: 0.848)
    - Democracy and Development in Africa: Demystifying Democracy as the Best Form of Government (weight: 0.3953)
    - Democracy and Development in Africa: Demystifying Democracy as the Best Form of Government (weight: 0.3953)
    - Which Form of Government Is Best? - Kellogg Insight (weight: 0.2939)

---
## 12. "sugar is worse than fat for health"
Category: contested
Expected: contested
Actual: likely opposed (YES)
Claim type: factual (0.9969)

### Sources collected: 49 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 49 -> 31 (dropped 18)
Dropped sources:
  - [encyclopedia] "Malnutrition" (relevance: 0.3045, reason: relevance_0.304_below_0.35)
  - [encyclopedia] "Polyendocrine metabolic ovarian syndrome" (relevance: 0.0426, reason: relevance_0.043_below_0.35)
  - [encyclopedia] "Metabolic dysfunction–associated steatotic liver disease" (relevance: 0.2558, reason: relevance_0.256_below_0.35)
  - [encyclopedia] "Barry Popkin" (relevance: 0.3431, reason: relevance_0.343_below_0.35)
  - [encyclopedia] "Starvation" (relevance: 0.2453, reason: relevance_0.245_below_0.35)
  - [academic] "Metabolic syndrome and psoriatic arthritis: the role of weight loss as a disease-modifying therapy" (relevance: 0.1892, reason: relevance_0.189_below_0.35)
  - [academic] "2021 ESC Guidelines on cardiovascular disease prevention in clinical practice" (relevance: 0.1442, reason: relevance_0.144_below_0.35)
  - [academic] "Microbiota in health and diseases" (relevance: 0.1699, reason: relevance_0.170_below_0.35)
  - [academic] "Dementia prevention, intervention, and care: 2024 report of the Lancet standing Commission" (relevance: 0.0916, reason: relevance_0.092_below_0.35)
  - [academic] "2023 AHA/ACC/ACCP/ASPC/NLA/PCNA Guideline for the Management of Patients With Chronic Coronary Disease: A Report of the American Heart Association/American College of Cardiology Joint Committee on Clinical Practice Guidelines" (relevance: 0.1376, reason: relevance_0.138_below_0.35)
  - [academic] "Breast Cancer—Epidemiology, Risk Factors, Classification, Prognostic Markers, and Current Treatment Strategies—An Updated Review" (relevance: 0.0057, reason: relevance_0.006_below_0.35)
  - [academic] "2023 ESC Guidelines for the management of cardiovascular disease in patients with diabetes" (relevance: 0.1781, reason: relevance_0.178_below_0.35)
  - [knowledge_graph] "Sugar" (relevance: 0.2274, reason: relevance_0.227_below_0.35)
  - [knowledge_graph] "unstable angina" (relevance: 0.0165, reason: relevance_0.017_below_0.35)
  - [knowledge_graph] "worse" (relevance: 0.3151, reason: relevance_0.315_below_0.35)
  - [knowledge_graph] "worse is better" (relevance: 0.2582, reason: relevance_0.258_below_0.35)
  - [knowledge_graph] "File Allocation Table" (relevance: -0.0306, reason: relevance_-0.031_below_0.35)
  - [knowledge_graph] "overweight" (relevance: 0.272, reason: relevance_0.272_below_0.35)

### Dedup: 31 -> 31 (dropped 0)

### Analyzed sources (31 total)

**[wikipedia] "Diet food"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9897)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Diet food (or dietetic food) refers to any food or beverage whose recipe is altered to reduce fat, carbohydrates, and/or sugar in order to make it par..."

**[wikipedia] "Trans fat"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Trans fat is a type of unsaturated fat that occurs in foods. Trans fats are fats (triglycerides, i.e. triple esters of glycerin) that contain chains d..."

**[wikipedia] "Aseem Malhotra"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Aseem Malhotra is a British cardiologist and author, whose COVID-19 vaccine and anti-statin views have been criticised as misinformation by experts. H..."

**[wikipedia] "Diabetes"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Diabetes mellitus, commonly known as diabetes, is a group of common endocrine diseases characterized by sustained high blood sugar levels. Diabetes te..."

**[wikipedia] "Childhood obesity"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Childhood obesity is a condition where excess body fat negatively affects a child's health or well-being. As methods to determine body fat directly ar..."

**[semantic_scholar] "Dietary Intake and Diet Quality of Adult Survivors of Childhood Cancer and the General Population: Results from the SCCSS-Nutrition Study"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9712)
  Verdict contribution: opposing (weight: 0.6313)
  Snippet: "Childhood cancer survivors (CCSs) are at increased risk of developing chronic health conditions. This may potentially be reduced by a balanced diet. W..."

**[semantic_scholar] "DIET AND COGNITION IN AGING: EFFECTS OF HIGH-FAT-SUGAR DIETS ON MEMORY AND EXECUTIVE FUNCTIONING"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9897)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract High-fat and high-sugar (HFS) diets may affect the hippocampus, and consequently the hippocampus-dependent memory. Previously, we found that ..."

**[semantic_scholar] "Ultra-processed food intake is associated with worse mental health in Southern Italian individuals"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9883)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract Background A growing body of literature suggests that inclusion of ultra-processed foods (UPFs) in the diet may be associated with various no..."

**[semantic_scholar] "Fat chance of escaping obesogens"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.6523)
  Verdict contribution: opposing (weight: 0.3588)
  Snippet: "Fat chance of escaping obesogens..."

**[semantic_scholar] "Fat acceptance as social justice"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.6182)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "CMAJ | SEPTEMBER 7, 2021 | VOLUME 193 | ISSUE 35 © 2021 CMA Joule Inc. or its licensors T he fat body has long been a site of medical surveillance, an..."

**[semantic_scholar] "Does co-consumption of Western diet and binge drinking result in more progressive liver disease?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9775)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Now the leading liver disease worldwide, metabolic dysfunction associated steatotic liver disease (MASLD) is a public health crisis. A major concern w..."

**[semantic_scholar] "Identifying the time course and contributors for Western diet-induced increase in glycocalyx barrier function"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9307)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The endothelial glycocalyx is a dynamic gel-like structure bound to the vascular endothelium composed of glycosaminoglycans, such as hyaluronan. The g..."

**[semantic_scholar] "983-P: Prediabetes A1C Is Associated with Metabolic Disease in Girls with PCOS and Obesity"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.4688)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Polycystic Ovary Syndrome (PCOS) is associated with metabolic diseases, including diabetes, and metformin is indicated if a1c is ≥5.7 demonstrating pr..."

**[semantic_scholar] "Chrono-nutrition and its Association with Chronotype and Blood Glucose Control Among People with Type 2 Diabetes"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.8252)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background: Recent studies have revealed conflicting results for low glycaemic index (GI) meals in the prevention and treatment of metabolic disorders..."

**[open_alex] "A 2022 update on the epidemiology of obesity and a call to action: as its twin COVID-19 pandemic appears to be receding, the obesity and dysmetabolism pandemic continues to rage on"**
  Type: academic | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.978)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The WHO just released in May 2022 a report on the state of the obesity pandemic in Europe, stating that 60% of citizens in the area of Europe are eith..."

**[open_alex] "Dietary Intake and Diet Quality of Adult Survivors of Childhood Cancer and the General Population: Results from the SCCSS-Nutrition Study"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9795)
  Verdict contribution: opposing (weight: 0.6367)
  Snippet: "Childhood cancer survivors (CCSs) are at increased risk of developing chronic health conditions. This may potentially be reduced by a balanced diet. W..."

**[open_alex] "Global Impacts of Western Diet and Its Effects on Metabolism and Health: A Narrative Review"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Western diet is a modern dietary pattern characterized by high intakes of pre-packaged foods, refined grains, red meat, processed meat, high-sugar..."

**[open_alex] "Socio-economic patterns of diet, obesity, and biomarkers for cardiovascular disease among Indian adolescents"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.5635)
  Verdict contribution: supporting (weight: 0.3099)
  Snippet: "ABSTRACT Background The impact of socioeconomic (SES) factors, maternal education and household wealth on diet and consequently on a host of cardiovas..."

**[duckduckgo] "Sugar vs fat: which is worse? - BHF - British Heart Foundation"**
  Type: web | Cred: estimated 0.341
  NLI (nli_deberta): neutral (0.9478)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Eat well Sugar vs fat: which is worse? Whether fat or sugar is worse for your health has become a dietary battleground. Senior Dietitian Victoria Tayl..."

**[duckduckgo] "Cut Added Sugars to Lose Weight and Improve Health"**
  Type: web | Cred: estimated 0.266
  NLI (nli_deberta): neutral (0.9546)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "As we learn that not all types of fats are created equal, the culprit now more often mentioned is added sugar. ... HealthCastle, founded in 1997, is ...."

**[duckduckgo] "Which Is Worse for You: Fat or Sugar? - Cleveland Clinic Health Essentials"**
  Type: web | Cred: estimated 0.488
  NLI (nli_deberta): neutral (0.9409)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Whether sugar or fat should be included in a heart-healthy diet depends on which fats and sugars you choose. Here's what you need to know about both...."

**[duckduckgo] "Sugar vs fat: which is actually worse? Here's what dietitians say"**
  Type: web | Cred: estimated 0.28900000000000003
  NLI (nli_deberta): opposing (0.9775)
  Verdict contribution: opposing (weight: 0.2825)
  Snippet: "Fat is slightly worse than sugar when it comes to calorie content. Sugar contains four calories per gram, whereas fats provide nine calories per gram...."

**[duckduckgo] "Fat vs Sugar: Which is Really Worse for Your Health? Expert Analysis ..."**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.9082)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Fat vs Sugar: Which is Really Worse for Your Health? Expert Analysis & Research EllieB The age-old debate between fat and sugar continues to spark hea..."

**[duckduckgo] "Sugar vs Fat - Which One Is Worse, Do We Need Fat and Sugar - Diabetes"**
  Type: web | Cred: estimated 0.371
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sugar and fat are two of the most widely talked about dietary topics, with one of the most commonly asked questions by people with (and without) diabe..."

**[duckduckgo] "Is sugar bad for you? Exploring the health debate"**
  Type: web | Cred: estimated 0.449
  NLI (nli_deberta): neutral (0.9849)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Breaking down the health risks of sugar Reducing added sugar is often something people think of when they want to lose weight — and for good reason. R..."

**[duckduckgo] "Is Sugar Worse Than Fat for the Heart? - iCliniq"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.9873)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Curbing more than 50 % of the current sugar intake and including an appropriate amount of healthy fat. Nevertheless, holding on to these restrictions ..."

**[duckduckgo] "Sugar vs. Fat: The Final Verdict on Which is Worse for Your"**
  Type: web | Cred: estimated 0.264
  NLI (nli_deberta): supporting (0.9736)
  Verdict contribution: supporting (weight: 0.257)
  Snippet: "... the field of functional medicine, Mark Hyman, MD, has just settled a 50-year debate proving that sugar is far more detrimental to our health than ..."

**[duckduckgo] "What's Worse, Fat or Sugar? - Food Blog Alliance"**
  Type: web | Cred: estimated 0.301
  NLI (nli_deberta): supporting (0.8638)
  Verdict contribution: supporting (weight: 0.26)
  Snippet: "Ultimately, sugar is generally considered worse than fat for overall health, due to its significant impact on metabolic processes, inflammation, and ...."

**[wikidata] "sugar"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "short-chain, water-soluble carbohydrate | instance of: excipient..."

**[wikidata] "diabetes"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "group of metabolic disorders characterized by high blood sugar levels over a prolonged period | instance of: class of disease..."

**[wikidata] "obesity"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "medical condition in which individuals have an excess of body fat | instance of: health risk..."

### Verdict computation
  Supporting weight: 0.827
  Opposing weight: 1.9092
  Support ratio: 0.3022
  Confidence: 0.3955
  Verdict: **likely opposed**
  Neutral sources (no contribution): 24

  Top supporting:
    - Socio-economic patterns of diet, obesity, and biomarkers for cardiovascular disease among Indian adolescents (weight: 0.3099)
    - What's Worse, Fat or Sugar? - Food Blog Alliance (weight: 0.26)
    - Sugar vs. Fat: The Final Verdict on Which is Worse for Your (weight: 0.257)
  Top opposing:
    - Dietary Intake and Diet Quality of Adult Survivors of Childhood Cancer and the General Population: Results from the SCCSS-Nutrition Study (weight: 0.6367)
    - Dietary Intake and Diet Quality of Adult Survivors of Childhood Cancer and the General Population: Results from the SCCSS-Nutrition Study (weight: 0.6313)
    - Fat chance of escaping obesogens (weight: 0.3588)
    - Sugar vs fat: which is actually worse? Here's what dietitians say (weight: 0.2825)

---
## 13. "nuclear energy is safe"
Category: contested
Expected: contested
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.9965)

### Sources collected: 46 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 46 -> 41 (dropped 5)
Dropped sources:
  - [academic] "Soft Self-Templating Approach-Derived Covalent Triazine Framework with Bimodal Nanoporosity for Efficient Radioactive Iodine Capture for Safe Nuclear Energy" (relevance: 0.2383, reason: relevance_0.238_below_0.35)
  - [knowledge_graph] "nuclear binding energy" (relevance: 0.3078, reason: relevance_0.308_below_0.35)
  - [knowledge_graph] "Safe" (relevance: 0.2713, reason: relevance_0.271_below_0.35)
  - [knowledge_graph] "personal protective equipment" (relevance: 0.1295, reason: relevance_0.129_below_0.35)
  - [knowledge_graph] "safe" (relevance: 0.302, reason: relevance_0.302_below_0.35)

### Dedup: 41 -> 41 (dropped 0)

### Analyzed sources (41 total)

**[wikipedia] "Nuclear power"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Nuclear power is the use of nuclear reactions to produce electricity. Nuclear power can be obtained from nuclear fission, nuclear decay and nuclear fu..."

**[wikipedia] "Pro-nuclear energy movement"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9092)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Proponents of nuclear energy contend that nuclear power is safe, and a sustainable energy source that reduces carbon emissions and increases energy se..."

**[wikipedia] "Nuclear Energy Agency"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Nuclear Energy Agency (NEA) is an intergovernmental agency that is organized under the Organisation for Economic Co-operation and Development (OEC..."

**[wikipedia] "Nuclear power in Pakistan"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In Pakistan, nuclear power is provided by six nuclear reactors in two commercial nuclear power plants with a net capacity of 3,545 MW from pressurized..."

**[wikipedia] "Nuclear power in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the United States, nuclear power is provided by 94 commercial reactors with a net capacity of 97 gigawatts (GW), with 63 pressurized water reactors..."

**[wikipedia] "National Nuclear Security Administration"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The National Nuclear Security Administration (NNSA) is a United States federal agency responsible for safeguarding national security through the milit..."

**[wikipedia] "Chernobyl Nuclear Power Plant"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9438)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Chernobyl Nuclear Power Plant (ChNPP) is a nuclear power plant undergoing decommissioning. ChNPP is located near the abandoned city of Pripyat in ..."

**[wikipedia] "Nuclear Energy Institute"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Nuclear Energy Institute (NEI) is a nuclear industry trade association in the United States, based in Washington, D.C...."

**[wikipedia] "Chernobyl New Safe Confinement"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9609)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The New Safe Confinement (NSC or New Shelter; Ukrainian: Новий безпечний конфайнмент, romanized: Novyy bezpechnyy konfaynment) is a structure put in p..."

**[wikipedia] "Energoatom"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Public JSC National nuclear energy generating company "Energoatom" (Ukrainian: ПАТ 'НАЕК "Енергоатом"', romanized: PAT NAEK 'Enerhoatom') is the p..."

**[semantic_scholar] "Stellarator–mirror fusion–fission hybrid – a fast route to clean and safe nuclear energy"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.7905)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The multiple-recycle fuel cycle for uranium-238 considered here, if practically realized, can bring revolutionary changes in nuclear energy. A full us..."

**[semantic_scholar] "Pakistan's safe nuclear energy generation: An essential source to target sustainable development"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9424)
  Verdict contribution: supporting (weight: 0.5183)
  Snippet: "Pakistan's safe nuclear energy generation: An essential source to target sustainable development..."

**[semantic_scholar] "NEW GLOBAL SAFE/ECONOMICAL NUCLEAR ENERGY INDUSTRY-THORIUM MOLTEN-SALT NUCLEAR ENERGY SYNERGETICS-"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.6826)
  Verdict contribution: supporting (weight: 0.273)
  Snippet: "NEW GLOBAL SAFE/ECONOMICAL NUCLEAR ENERGY INDUSTRY-THORIUM MOLTEN-SALT NUCLEAR ENERGY SYNERGETICS-..."

**[semantic_scholar] "Soft Self-Templating Approach-Derived Covalent Triazine Framework with Bimodal Nanoporosity for Efficient Radioactive Iodine Capture for Safe Nuclear Energy"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.627)
  Verdict contribution: supporting (weight: 0.4076)
  Snippet: "Soft Self-Templating Approach-Derived Covalent Triazine Framework with Bimodal Nanoporosity for Efficient Radioactive Iodine Capture for Safe Nuclear ..."

**[semantic_scholar] "The Q-NPT: Redefining Nuclear Energy Governance for Sustainability"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.8423)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Global peace, security, and sustainable energy development depend on effective nuclear energy governance. While the Nuclear Non-Proliferation Treaty (..."

**[semantic_scholar] "Artificial Intelligence in Nuclear Energy: Legal Challenges and International Cooperation in the Search of Approaches to Regulation"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9609)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The application of artificial intelligence (AI) holds the potential for revolutionary advancements in civil nuclear energy. However, this necessitates..."

**[semantic_scholar] "Nuclear Energy As a Reliable And Safe Source of Power Generation"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.9473)
  Verdict contribution: supporting (weight: 0.3789)
  Snippet: "Nuclear Energy As a Reliable And Safe Source of Power Generation..."

**[semantic_scholar] "Nuclear Energy"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9253)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "
 Nuclear Energy: Boom, Bust, and Emerging Renaissance explores the history and developing aspects of nuclear energy and examines its potential to mee..."

**[semantic_scholar] "International experience of legal regulation of nuclear energy use and its development in other countries"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.8311)
  Verdict contribution: supporting (weight: 0.3324)
  Snippet: "This article provides an overview of the global experience in legal regulation in the field of nuclear energy. Itfocuses on the evolution of legislati..."

**[semantic_scholar] "Research and practice of nuclear energy steam supply in the industrial field based on the background of comprehensive energy utilization"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Research and practice of nuclear energy steam supply in the industrial field based on the background of comprehensive energy utilization..."

**[open_alex] "Pakistan's safe nuclear energy generation: An essential source to target sustainable development"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9424)
  Verdict contribution: supporting (weight: 0.6126)
  Snippet: "Pakistan's safe nuclear energy generation: An essential source to target sustainable development..."

**[open_alex] "Nuclear energy: A pathway towards mitigation of global warming"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9902)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Nuclear energy: A pathway towards mitigation of global warming..."

**[open_alex] "Development and outlook of advanced nuclear energy technology"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.6084)
  Verdict contribution: supporting (weight: 0.4867)
  Snippet: "As the only clean, low-carbon, safe and efficient basic load energy, nuclear energy has been increasingly developed in major nuclear power nations aro..."

**[open_alex] "Sharing the “safe” atom?: the International Atomic Energy Agency and nuclear regulation through standardisation 1"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9893)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This chapter scrutinises the early efforts of the International Atomic Energy Agency (IAEA, founded in 1957) to both promote and monitor the developme..."

**[open_alex] "Stellarator–mirror fusion–fission hybrid – a fast route to clean and safe nuclear energy"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.7905)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The multiple-recycle fuel cycle for uranium-238 considered here, if practically realized, can bring revolutionary changes in nuclear energy. A full us..."

**[open_alex] "The roles of hydro, nuclear and biomass energy towards carbon neutrality target in China: A policy-based analysis"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The roles of hydro, nuclear and biomass energy towards carbon neutrality target in China: A policy-based analysis..."

**[open_alex] "Advanced nuclear energy: the safest and most renewable clean energy"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9141)
  Verdict contribution: supporting (weight: 0.7313)
  Snippet: "Advanced nuclear energy: the safest and most renewable clean energy..."

**[open_alex] "Technological solutions for long-term storage of partially used nuclear waste: A critical review"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9805)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Technological solutions for long-term storage of partially used nuclear waste: A critical review..."

**[open_alex] "Floating Nuclear Power Plants, a Safe Way Out of the Energy and Climate Conundrum"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.959)
  Verdict contribution: supporting (weight: 0.5274)
  Snippet: "Abstract Climate scientists are alarmed at the rate global temperatures are rising and its knock-on effect on biodiversity. Some believe we are in the..."

**[duckduckgo] "Nuclear energy in Israel"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "While Israel operates nuclear research reactors, it has no nuclear power plants. However, the possibility of constructing nuclear power plants in the ..."

**[duckduckgo] "Safety of Nuclear Power Reactors - World Nuclear Association"**
  Type: web | Cred: estimated 0.45199999999999996
  NLI (nli_deberta): neutral (0.5273)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "March 30, 2026 - It should be emphasized that a commercial-type power reactor simply cannot under any circumstances explode like a nuclear bomb – the ..."

**[duckduckgo] "Enhanced Safety of Advanced Reactors | Department of Energy"**
  Type: web | Cred: estimated 0.488
  NLI (nli_deberta): neutral (0.9414)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "1 week ago - Nuclear power plants are designed, built, and operated using a “defense-in-depth” approach in which multiple independent and redundant la..."

**[duckduckgo] "Is Nuclear Power Bad for the Environment? • Friends of the Earth"**
  Type: web | Cred: estimated 0.421
  NLI (nli_deberta): opposing (0.8359)
  Verdict contribution: opposing (weight: 0.3519)
  Snippet: "August 19, 2024 - Even if modern designs are safer, human error, natural disasters, cyber risks, and extreme weather will always introduce failure ris..."

**[duckduckgo] "Advanced nuclear energy: the safest and most renewable clean energy - ScienceDirect"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.8376)
  Snippet: "November 28, 2022 - Nuclear energy is much safer than solar and wind renewables and has a lower life cycle carbon footprint. The disadvantage of nucle..."

**[duckduckgo] "Ask an Expert: Nuclear’s World-Class Safety Standards | NEI"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.9253)
  Verdict contribution: supporting (weight: 0.3729)
  Snippet: "May 13, 2022 - Third, is the fact that nuclear can provide energy security that allows us to reduce our reliance on non-U.S. or non-allied sources of ..."

**[duckduckgo] "How Safe Are Nuclear Power Plants? -- ANS / Nuclear Newswire"**
  Type: web | Cred: estimated 0.348
  NLI (nli_deberta): supporting (0.9858)
  Verdict contribution: supporting (weight: 0.3431)
  Snippet: "Generating energy by nuclear fission has proven to be one of the safest industrial pursuits in the world. Nuclear accidents such as Chernobyl or Fukus..."

**[duckduckgo] "Nuclear power and the environment - U.S. Energy Information Administration (EIA)"**
  Type: web | Cred: estimated 0.40700000000000003
  NLI (nli_deberta): neutral (0.834)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "U.S. energy facts ... State and U.S. territory data ... U.S. nuclear industry ... An uncontrolled nuclear reaction could result in widespread contamin..."

**[duckduckgo] "Nuclear Power | Union of Concerned Scientists"**
  Type: web | Cred: estimated 0.308
  NLI (nli_deberta): neutral (0.8813)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "March 31, 2026 - Low-carbon electricity, with serious economic and safety issues. ... In the 1970s and 80s, more than a hundred nuclear reactors were ..."

**[duckduckgo] "Nuclear Energy - Our World in Data"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9624)
  Verdict contribution: supporting (weight: 0.818)
  Snippet: "July 10, 2020 - The key insight is that they are all much safer than fossil fuels. Nuclear energy, for example, results in 99.9% fewer deaths than bro..."

**[wikidata] "nuclear power"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "power generated from nuclear reactions | instance of: energy production..."

**[wikidata] "Nuclear Energy"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "sculpture by Henry Moore (LH 526, University of Chicago) | instance of: sculpture | country: United States | located in: Chicago | inception: January ..."

### Verdict computation
  Supporting weight: 6.6399
  Opposing weight: 0.3519
  Support ratio: 0.9497
  Confidence: 0.8993
  Verdict: **strongly supported**
  Neutral sources (no contribution): 27

  Top supporting:
    - Advanced nuclear energy: the safest and most renewable clean energy - ScienceDirect (weight: 0.8376)
    - Nuclear Energy - Our World in Data (weight: 0.818)
    - Advanced nuclear energy: the safest and most renewable clean energy (weight: 0.7313)
    - Pakistan's safe nuclear energy generation: An essential source to target sustainable development (weight: 0.6126)
    - Floating Nuclear Power Plants, a Safe Way Out of the Energy and Climate Conundrum (weight: 0.5274)
  Top opposing:
    - Is Nuclear Power Bad for the Environment? • Friends of the Earth (weight: 0.3519)

---
## 14. "remote work is more productive than office work"
Category: contested
Expected: contested
Actual: contested (YES)
Claim type: factual (0.969)

### Sources collected: 49 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 49 -> 33 (dropped 16)
Dropped sources:
  - [encyclopedia] "Computer-supported cooperative work" (relevance: 0.3452, reason: relevance_0.345_below_0.35)
  - [encyclopedia] "Work–life balance in the United States" (relevance: 0.2043, reason: relevance_0.204_below_0.35)
  - [encyclopedia] "Preference theory" (relevance: 0.0752, reason: relevance_0.075_below_0.35)
  - [encyclopedia] "Human resources" (relevance: 0.2323, reason: relevance_0.232_below_0.35)
  - [encyclopedia] "Bring your own device" (relevance: 0.2084, reason: relevance_0.208_below_0.35)
  - [academic] "Cooler, Quieter, and More Productive" (relevance: 0.3456, reason: relevance_0.346_below_0.35)
  - [academic] "Mismatch in Preferences for Working from Home – Evidence from Discrete Choice Experiments with Workers and Employers" (relevance: 0.2683, reason: relevance_0.268_below_0.35)
  - [academic] "Chatting and cheating: Ensuring academic integrity in the era of ChatGPT" (relevance: 0.1681, reason: relevance_0.168_below_0.35)
  - [academic] "Researching the Post‐Pandemic Professional Service Firm: Challenging our Assumptions" (relevance: 0.346, reason: relevance_0.346_below_0.35)
  - [academic] "Metallaphotoredox: The Merger of Photoredox and Transition Metal Catalysis" (relevance: 0.0361, reason: relevance_0.036_below_0.35)
  - [academic] "The role of artificial intelligence in healthcare: a structured literature review" (relevance: 0.1307, reason: relevance_0.131_below_0.35)
  - [academic] "Six Key Advantages and Disadvantages of Working from Home in Europe during COVID-19" (relevance: 0.3217, reason: relevance_0.322_below_0.35)
  - [knowledge_graph] "virtual assistant" (relevance: 0.3371, reason: relevance_0.337_below_0.35)
  - [knowledge_graph] "productive animal" (relevance: 0.3122, reason: relevance_0.312_below_0.35)
  - [knowledge_graph] "economic production" (relevance: 0.2096, reason: relevance_0.210_below_0.35)
  - [knowledge_graph] "productive forces" (relevance: 0.3162, reason: relevance_0.316_below_0.35)

### Dedup: 33 -> 33 (dropped 0)

### Analyzed sources (33 total)

**[wikipedia] "Work–life balance"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the intersection of work and personal life, the work–life balance is the equilibrium between the two. There are many aspects of one's personal life..."

**[wikipedia] "Remote work"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Remote work is the practice of working at or from one's home or another space rather than from an office or workplace.
The practice of working at home..."

**[wikipedia] "Work (human activity)"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Work or labor (labour in British English) refers to the intentional activities individuals engage in to meet their own needs and potentially wants, as..."

**[wikipedia] "Productivity theater"**
  Type: encyclopedia | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9912)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Productivity theater is a form of impression management where an employee acts productively in the workplace, typically by appearing busy or unavailab..."

**[wikipedia] "Four-day workweek"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A four-day workweek is an arrangement where a workplace or place of education has its employees or students work or attend school, college or universi..."

**[semantic_scholar] "Work-Life Balance in Home-Office Contexts Exploring Productivity, Stress, and Boundary Management in Remote Work"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9438)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract This study investigates the impact of home-office arrangement on work-life balance (WLB) with reference to productivity, stress, and boundary..."

**[semantic_scholar] "Working Remotely? Selection, Treatment, and the Market for Remote Work"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.649)
  Snippet: "How does remote work affect productivity and how productive are workers who choose remote jobs? We decompose these effects in a Fortune 500 firm. Befo..."

**[semantic_scholar] "Remote Work and Development – A Law-and-Economics Perspective"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Remote Work and Development – A Law-and-Economics Perspective..."

**[semantic_scholar] "Workplace Transformation in the Post-Pandemic Era: Impact of Remote Work on Productivity"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.398)
  Snippet: "In this study, an analysis of the effects of remote working on productivity is conducted through a well-structured questionnaire using a Likert scale ..."

**[semantic_scholar] "Tools and Technology for Effective Remote Work"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9414)
  Verdict contribution: opposing (weight: 0.6119)
  Snippet: "Office work refers to work that is generally done in an office building designated explicitly for administrative and professional duties. Remote work ..."

**[semantic_scholar] "Heuristics for Equitable Technical Communication in Remote & Hybrid Game Development"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Purpose: This article seeks to provide a set of heuristics for technical communication, addressing the newfound challenges to game developers as a res..."

**[semantic_scholar] "Talent attraction through flexible work anytime from anywhere"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "As a flexible working style, working anytime from anywhere can attract talented individuals due to flexibility and expanded talent pools. This literat..."

**[semantic_scholar] "Remote Approach for the Effective Task Execution and Data Accessing Tool"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.5703)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ": Work that is typically completed in an office building specifically intended for administrative and professional functions is referred to as office ..."

**[semantic_scholar] "Effects of Remote Working in Fortune 500 Global Companies"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.6797)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The 500 largest global companies are not just leaders economically, they are also seen as role models. Especially during Covid-19, they had to change ..."

**[open_alex] "Changes in perceived productivity of software engineers during COVID-19 pandemic: The voice of evidence"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9214)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The COVID-19 pandemic triggered a natural experiment of an unprecedented scale as companies closed their offices and sent employees to work from home...."

**[open_alex] "Covid‐19 and The Study of Professionals and Professional Work"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.811)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Covid-19 global pandemic changes how we study professional workers and their everyday lives. We normally think of professionals as leading stable,..."

**[open_alex] "COVID‐19, digitization and hybrid workspaces: A critical inflection point for public sector governance and workforce development"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Whereas the physical office setting has long been the bedrock of public sector operations, COVID-19 starkly disrupted this enduring reality with an un..."

**[open_alex] "Why Working from Home Will Stick"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9907)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "COVID-19 drove a mass social experiment in working from home (WFH). We survey more than 30,000 Americans over multiple waves to investigate whether WF..."

**[duckduckgo] "Remote Work vs Office Productivity: Which Work Model ... - CurrentWare"**
  Type: web | Cred: estimated 0.269
  NLI (nli_deberta): neutral (0.9888)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Compare remote work vs office productivity and learn which work model delivers better focus, collaboration, and performance. Explore key advantages, c..."

**[duckduckgo] "Remote Work Productivity Study: Surprising Findings From a 4-Year ..."**
  Type: web | Cred: estimated 0.354
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Explore key findings from a longitudinal remote work productivity study. Learn how working from home impacts performance and why productivity remains ..."

**[duckduckgo] "Comparing Productivity for Remote Work vs. In-Office Employees"**
  Type: web | Cred: estimated 0.376
  NLI (nli_deberta): neutral (0.9858)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Are employees more productive working from home or in the office? Here's what the latest research has to say about the pros and cons of working remote..."

**[duckduckgo] "Remote vs In Person Work: A Data-Backed Comparison Guide"**
  Type: web | Cred: estimated 0.40499999999999997
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Deciding between remote work vs office? Our complete guide compares the pros, cons, and costs of each model, using recent stats on productivity, emplo..."

**[duckduckgo] "The rise in remote work since the pandemic and its impact on ..."**
  Type: web | Cred: estimated 0.44000000000000006
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "We also compare 2019 data with 2022 data to see if the relationship between remote work and productivity changed as businesses and employees further a..."

**[duckduckgo] "Remote Work vs Office Work: Complete Comparison Guide 2026"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Comprehensive comparison of remote work and office work. Productivity, career advancement, work-life balance, compensation, and how to choose the righ..."

**[duckduckgo] "The Surprising Truth About Remote Work Productivity"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9849)
  Verdict contribution: supporting (weight: 0.8372)
  Snippet: "Key points Studies show that remote workers are 5 to 9 percent more productive than those working in a physical office. Remote work leads to improved ..."

**[duckduckgo] "Remote Work or Office Work: What's Better for Productivity?"**
  Type: web | Cred: estimated 0.479
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Case for Remote Work Flexibility and Autonomy: Remote work provides flexibility, allowing employees to set their own schedules and work from the c..."

**[duckduckgo] "Can Employees Be More Productive From Home? - business.com"**
  Type: web | Cred: estimated 0.40199999999999997
  NLI (nli_deberta): neutral (0.9014)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Are Employees More Productive Working From Home? While questions around remote vs. in-office work persist, recent data suggests that well-managed remo..."

**[duckduckgo] "Remote Or In-Office Work? The Future Lies In A Better Hybrid Model - Forbes"**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): neutral (0.6157)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A return to fully in-office work would be a real step backwards for the business world, in terms of both work-life balance and organizational producti..."

**[wikidata] "remote work"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "work arrangement..."

**[wikidata] "remote worker"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "worker working remotely..."

**[wikidata] "office work"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "productive activity using the mind and not requiring significant movement or bodily exertion | instance of: activity..."

**[wikidata] "office worker"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "person who works in an office | instance of: clerical occupation..."

**[wikidata] "Office Workstations Limited"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "instance of: business | inception: 1984-00-00..."

### Verdict computation
  Supporting weight: 1.2352
  Opposing weight: 1.2609
  Support ratio: 0.4948
  Confidence: 0.0103
  Verdict: **contested**
  Neutral sources (no contribution): 29

  Top supporting:
    - The Surprising Truth About Remote Work Productivity (weight: 0.8372)
    - Workplace Transformation in the Post-Pandemic Era: Impact of Remote Work on Productivity (weight: 0.398)
  Top opposing:
    - Working Remotely? Selection, Treatment, and the Market for Remote Work (weight: 0.649)
    - Tools and Technology for Effective Remote Work (weight: 0.6119)

---
## 15. "AI will replace most jobs"
Category: current_event
Expected: contested
Actual: likely opposed (YES)
Claim type: factual (0.9969)

### Sources collected: 49 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 49 -> 39 (dropped 10)
Dropped sources:
  - [encyclopedia] "SpaceXAI" (relevance: 0.2821, reason: relevance_0.282_below_0.35)
  - [academic] "Western Australian medical students’ attitudes towards artificial intelligence in healthcare" (relevance: 0.2872, reason: relevance_0.287_below_0.35)
  - [academic] "Multi-stakeholder preferences for the use of artificial intelligence in healthcare: A systematic review and thematic analysis" (relevance: 0.2775, reason: relevance_0.278_below_0.35)
  - [knowledge_graph] "Anguilla" (relevance: -0.0437, reason: relevance_-0.044_below_0.35)
  - [knowledge_graph] "Air India" (relevance: 0.0543, reason: relevance_0.054_below_0.35)
  - [knowledge_graph] "replacement" (relevance: 0.2092, reason: relevance_0.209_below_0.35)
  - [knowledge_graph] "replacement name" (relevance: 0.0437, reason: relevance_0.044_below_0.35)
  - [knowledge_graph] "electoral list" (relevance: 0.0174, reason: relevance_0.017_below_0.35)
  - [knowledge_graph] "Jobs" (relevance: 0.2197, reason: relevance_0.220_below_0.35)
  - [knowledge_graph] "Jobst" (relevance: 0.189, reason: relevance_0.189_below_0.35)

### Dedup: 39 -> 39 (dropped 0)

### Analyzed sources (39 total)

**[wikipedia] "AI agent"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the context of generative artificial intelligence, AI agents (also referred to as compound AI systems or agentic AI) are a class of intelligent age..."

**[wikipedia] "Artificial intelligence"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learnin..."

**[wikipedia] "AI boom"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "An AI boom is a period of rapid growth in the field of artificial intelligence (AI). The most recent boom happened in the early 2020s before seeing in..."

**[wikipedia] "Generative AI"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Generative artificial intelligence (GenAI) is a subfield of artificial intelligence (AI) that uses generative models to generate text, images, videos,..."

**[wikipedia] "Artificial general intelligence"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial general intelligence (AGI) is a hypothetical type of artificial intelligence that matches or surpasses human capabilities across virtually ..."

**[wikipedia] "Tilly Norwood"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Tilly Norwood is a character created using generative artificial intelligence in 2025 by Xicoia, the AI division of Particle6 Group, a production comp..."

**[wikipedia] "AI slop"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "AI slop (also known as slop content or simply as slop) is digital content made with generative artificial intelligence that is perceived as lacking in..."

**[wikipedia] "OpenAI"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "OpenAI is an American artificial intelligence (AI) research organization headquartered in San Francisco, consisting of a for-profit public benefit cor..."

**[wikipedia] "Dario Amodei"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Dario Amodei (born 1983) is an American artificial intelligence (AI) researcher and entrepreneur. In 2021, he and his sister Daniela Amodei co-founded..."

**[semantic_scholar] "Why can’t artificial intelligence replace most typing jobs?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.7534)
  Verdict contribution: opposing (weight: 0.3014)
  Snippet: "Artificial intelligence (AI) has spread across many jobs over the past years. By 2030, artificial intelligence may have replaced most of the jobs in t..."

**[semantic_scholar] "The Impact of AI On Jobs"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9849)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract - Artificial Intelligence (AI) has become one of the most powerful technologies of the 21st century, influencing industries, economies, and s..."

**[semantic_scholar] "Consequences of AI in the workforce: How AI is taking our Jobs"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Although artificial intelligence is helping solve many problems in today's world, it is also the reason many people around the world are losing their ..."

**[semantic_scholar] "AI disruption in chartering in Danish Shipping"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9893)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Our research highlights the current state and trends of artificial intelligence (AI) adoption in Denmark’s chartering, particularly in the dry bulk an..."

**[semantic_scholar] "Unveiling sora open AI’s impact: a review of transformative shifts in marketing and advertising employment"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract Marketing and advertising are two of the many industries that are significantly impacted by rapid advancements in artificial intelligence (AI..."

**[semantic_scholar] "Hierarchy and hope: Exploring AI’s role in medicine through a thematic analysis of online discourse"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9927)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The healthcare community remains divided on the benefits of artificial intelligence (AI) in medicine. In this qualitative study, we sought to better u..."

**[semantic_scholar] "AI in Employment: Threats or Opportunity? An Analysis of Global Trends, Sectoral Impacts, and Policy Responses"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9561)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial intelligence is one of the most discussed topics today. It is changing the way people work. This paper
examines whether AI is a threat to e..."

**[semantic_scholar] "A composite Literature review on Impact of Artificial Intelligence on Jobs Profiling"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The employment impact of advances in artificial intelligence has become a major concern in today's world in recent years. It is often discussed at con..."

**[semantic_scholar] "How companies can prepare for the coming “AI-first” world"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9712)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "
Purpose
The authors’ research identified seven best practices of leading companies with a particularly aggressive “All-in-on-AI” approach to Artifici..."

**[semantic_scholar] "A bleak outlook turns brighter"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9883)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "
 
 This paper aims to review the latest management developments across the globe and pinpoint practical implications from cutting-edge research and c..."

**[open_alex] "On the use of AI-based tools like ChatGPT to support management research"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.6875)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Purpose The article discusses the current relevance of artificial intelligence (AI) in research and how AI improves various research methods. This art..."

**[open_alex] "Understanding knowledge hiding under technological turbulence caused by artificial intelligence and robotics"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9883)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Purpose Artificial intelligence (AI) will be performing 52% of the tasks in companies by 2025. The increasing adoption of AI is generating technologic..."

**[open_alex] "Public understanding of artificial intelligence through entertainment media"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Public understanding of artificial intelligence through entertainment media..."

**[open_alex] "How Generative AI Can Augment Human Creativity"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9888)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "How Generative AI Can Augment Human Creativity..."

**[open_alex] "Artificial intelligence impact on banks clients and employees in an Asian developing country"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9502)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Purpose The purpose of this paper is to discuss the application of artificial intelligence (AI) in banking sector, its impact on banks employees and c..."

**[open_alex] "Art in an age of artificial intelligence"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9639)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial intelligence (AI) will affect almost every aspect of our lives and replace many of our jobs. On one view, machines are well suited to take ..."

**[open_alex] "Knowledge and perception of healthcare workers towards the adoption of artificial intelligence in healthcare service delivery in Nigeria"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background: Artificial Intelligence (AI) is seen as the machine that replaces human labour to work for men with a more effective and speedier result. ..."

**[open_alex] "What skills and abilities can automation technologies replicate and what does it mean for workers?"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This paper exploits novel data on the degree of automatability of approximately 100 skills and abilities collected through an original survey of exper..."

**[duckduckgo] "ChatGPT: the 10 Jobs Most at Risk of Being Replaced by AI -"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): opposing (0.7808)
  Verdict contribution: opposing (weight: 0.6637)
  Snippet: "Still, Oded Netzer, a Columbia Business School professor, said he thinks that AI will help coders rather than replace them...."

**[duckduckgo] "Will AI replace most jobs? -"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): opposing (0.9824)
  Verdict contribution: opposing (weight: 0.1965)
  Snippet: "Conclusion: Will AI Replace Most Jobs? Not Likely, but Change Is Inevitable AI is undoubtedly reshaping the job market, but the future doesn’t have ....."

**[duckduckgo] "70+ Stats On AI Replacing Jobs (2026)"**
  Type: web | Cred: estimated 0.502
  NLI (nli_deberta): neutral (0.6362)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "However, will AI really put most people’s jobs at risk, or is the reality more nuanced? ... school degree worked in the jobs most exposed to AI...."

**[duckduckgo] "What jobs will AI replace & which are safe in 2025 [+Data]"**
  Type: web | Cred: estimated 0.5820000000000001
  NLI (nli_deberta): opposing (0.8862)
  Verdict contribution: opposing (weight: 0.5158)
  Snippet: "The most common question is: “Will AI replace marketing jobs?” The short answer? It won’t. ... The jobs that will be replaced by AI are often ......"

**[duckduckgo] "AI to replace most jobs by 2045, only these 3 careers are safe,"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.7676)
  Verdict contribution: supporting (weight: 0.3838)
  Snippet: "Adam Dorr, Director of Research at think tank RethinkX, recently predicted that AI and robotics will replace the majority of human jobs...."

**[duckduckgo] "Why AI Won't Replace Most Jobs in 2026—but Will Reshape Work,"**
  Type: web | Cred: estimated 0.40499999999999997
  NLI (nli_deberta): opposing (0.998)
  Verdict contribution: opposing (weight: 0.4042)
  Snippet: "Why AI Won't Replace Most Jobs in 2026—but Will ... AI will not replace most jobs by 2026, but it will automate specific tasks within many roles...."

**[duckduckgo] ""AI will replace all the jobs!" Is Just Tech Execs"**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): neutral (0.9189)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The core assertion by the “ AI will replace 20-50% of all jobs ” crowd seems to be that the past 20 years of machine learning and ......"

**[duckduckgo] "AI Will Replace Jobs: But Most People Still Aren’t Using It"**
  Type: web | Cred: estimated 0.40599999999999997
  NLI (nli_deberta): supporting (0.7339)
  Verdict contribution: supporting (weight: 0.298)
  Snippet: "AI Will Replace Jobs: But Most People Still Aren’t Using It ... day work week is coming in just 10 years, thanks to AI replacing humans ‘for most ......"

**[duckduckgo] "Geoffrey Hinton Warns AI Will Replace Most Jobs Soon - Bizmart"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.6108)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Geoffrey Hinton Warns AI Will Replace Most Jobs Soon ... Although some optimists argue that AI will mostly assist rather than replace humans, Hinton ...."

**[duckduckgo] "Generative AI and the future of work in America | McKinsey"**
  Type: web | Cred: estimated 0.429
  NLI (nli_deberta): opposing (0.917)
  Verdict contribution: opposing (weight: 0.3934)
  Snippet: "In fact, the occupational categories most exposed to generative AI could continue to add jobs through 2030 (Exhibit 4), although its adoption may ......"

**[wikidata] "artificial intelligence"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "field of computer science that develops and studies software enabling machines to exhibit intelligent behavior | instance of: type of technology..."

**[wikidata] "Jobs"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "2013 film directed by Joshua Michael Stern | instance of: film..."

### Verdict computation
  Supporting weight: 0.6818
  Opposing weight: 2.4749
  Support ratio: 0.216
  Confidence: 0.568
  Verdict: **likely opposed**
  Neutral sources (no contribution): 31

  Top supporting:
    - AI to replace most jobs by 2045, only these 3 careers are safe, (weight: 0.3838)
    - AI Will Replace Jobs: But Most People Still Aren’t Using It (weight: 0.298)
  Top opposing:
    - ChatGPT: the 10 Jobs Most at Risk of Being Replaced by AI - (weight: 0.6637)
    - What jobs will AI replace & which are safe in 2025 [+Data] (weight: 0.5158)
    - Why AI Won't Replace Most Jobs in 2026—but Will Reshape Work, (weight: 0.4042)
    - Generative AI and the future of work in America | McKinsey (weight: 0.3934)
    - Why can’t artificial intelligence replace most typing jobs? (weight: 0.3014)

---
## 16. "the United States economy is in a recession"
Category: current_event
Expected: contested
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.9981)

### Sources collected: 36 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 36 -> 32 (dropped 4)
Dropped sources:
  - [academic] "Assessment of Economic Sustainability in the Construction Sector: Evidence from Three Developed Countries (the USA, China, and the UK)" (relevance: 0.3289, reason: relevance_0.329_below_0.35)
  - [academic] "Introduction. Changing Yet Persistent: Revolutions and Revolutionary Events" (relevance: 0.012, reason: relevance_0.012_below_0.35)
  - [academic] "The Political Economy of Public Pensions" (relevance: 0.2721, reason: relevance_0.272_below_0.35)
  - [academic] "Left to Our Own Devices" (relevance: 0.2911, reason: relevance_0.291_below_0.35)

### Dedup: 32 -> 31 (dropped 1)

### Analyzed sources (31 total)

**[wikipedia] "List of recessions in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.6084)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There have been as many as 48 recessions in the United States dating back to the Articles of Confederation, and although economists and historians dis..."

**[wikipedia] "Great Recession in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9717)
  Verdict contribution: supporting (weight: 0.8259)
  Snippet: "In the United States, the Great Recession was a severe financial crisis combined with a deep recession. While the recession officially lasted from Dec..."

**[wikipedia] "Economy of the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9771)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The United States has a highly developed and diversified market-oriented economy. It is the world's largest economy by nominal GDP, generating 26% of ..."

**[wikipedia] "Recession shapes"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Recession shapes or recovery shapes are used by economists to describe different types of recessions and their subsequent recoveries.  There is no spe..."

**[wikipedia] "Economy of Australia"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Australia has a highly developed mixed economy. As of 2026, Australia was the 12th-largest national economy by nominal GDP (gross domestic product), t..."

**[wikipedia] "Early 1990s recession in the United States"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.6548)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The United States entered a recession in 1990, which lasted 8 months through March 1991. Although the recession was mild relative to other post-war re..."

**[wikipedia] "List of recessions in Canada"**
  Type: encyclopedia | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9248)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Although Canada's economy is closely linked to the United States' economy, Canadian and American recessions do not always coincide.  A recession is ge..."

**[wikipedia] "Recession of 1920–1921"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Recession of 1920–1921 was a sharp deflationary economic contraction in the United States, United Kingdom and other countries, beginning 14 months..."

**[wikipedia] "List of recessions in the United Kingdom"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9858)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This is a list of recessions (and depressions) that have affected the economy of the United Kingdom and its predecessor states...."

**[wikipedia] "Early 1980s recession in the United States"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.8999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The United States entered recession in January 1980 and returned to growth six months later in July 1980. Although recovery took hold, the unemploymen..."

**[open_alex] "The Economic Impacts of COVID-19: Evidence from a New Public Database Built Using Private Sector Data"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9771)
  Verdict contribution: supporting (weight: 0.7817)
  Snippet: "We build a publicly available database that tracks economic activity in the United States at a granular level in real time using anonymized data from ..."

**[open_alex] "The Coronavirus Stimulus Package: How Large is the Transfer Multiplier"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.52)
  Verdict contribution: supporting (weight: 0.338)
  Snippet: "Abstract In response to the COVID-19 pandemic, large parts of the economy were locked down and, as a result, households’ income risk rose sharply. At ..."

**[open_alex] "Investigating the nexus between green economy, sustainability, bitcoin and oil prices: Contextual evidence from the United States"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Investigating the nexus between green economy, sustainability, bitcoin and oil prices: Contextual evidence from the United States..."

**[open_alex] "Time varying causal relationship between renewable energy consumption, oil prices and economic activity: New evidence from the United States"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Time varying causal relationship between renewable energy consumption, oil prices and economic activity: New evidence from the United States..."

**[open_alex] "Economic recovery forecasts under impacts of COVID-19"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.8774)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Economic recovery forecasts under impacts of COVID-19..."

**[open_alex] "Clusters and the Great Recession"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.8979)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Clusters and the Great Recession..."

**[duckduckgo] "Will There Be a Recession? Bloomberg Economics Says 38..."**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9048)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "US Recession Chances Surge to 38%, Bloomberg Economics Model Says.The odds of a US recession in the next year are now roughly one-in-three after consu..."

**[duckduckgo] "Is the US headed into a recession under Trump?"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.96)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the US, a recession is defined as a prolonged and widespread decline in economic activity typically characterised by a jump in unemployment and fal..."

**[duckduckgo] "The energy shock isn’t likely to trigger a US... - RBC Economics"**
  Type: web | Cred: estimated 0.40599999999999997
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.4054)
  Snippet: "1. The US economy in aggregate is not currently in a recession. The set of indicators used by the National Bureau of Economic Research (NBER)* to iden..."

**[duckduckgo] "Economy of the United States by GDP in 2024 - GeeksforGeeks"**
  Type: web | Cred: estimated 0.331
  NLI (nli_deberta): neutral (0.9731)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Over the years, United States economy has stood as global powerhouse. It has been contributing to and leading the world economic output. With the dive..."

**[duckduckgo] "The US economy is contracting faster than expected. Is it a recession?"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): neutral (0.5225)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "But the official definition of a recession in the United States (yes, other countries have different definitions, because economics is a squishy field..."

**[duckduckgo] "Why There's a 70% Chance of Recession... - Business Insider"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.8999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There's a 70% chance the US economy is either in a recession or headed toward one in the months ahead, according to Bloomberg Economics Chief US Econo..."

**[duckduckgo] "Recessionary Gap (Definition, Graph) | Top Causes of Recessionary..."**
  Type: web | Cred: estimated 0.288
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "When a recession happens when the economy is not reaching its full potential, there comes the recessionary gap. It measures the difference between whe..."

**[duckduckgo] "U.S. Economy Plunged Into Recession in February - The New York..."**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9424)
  Verdict contribution: supporting (weight: 0.801)
  Snippet: "Many economists believe the United States may already have exited the recession — or at least be on its way out.The global economy as a whole will exp..."

**[duckduckgo] "Gross Domestic Product (GDP) | FRED | St. Louis Fed"**
  Type: web | Cred: estimated 0.5
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "View economic output, reported as the nominal value of all new goods and services produced by labor and property located in the U.S.Inflation, consume..."

**[wikidata] "United States economy growth revised up to 0.4% in last quarter of 2012"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Wikinews article | instance of: Wikinews article..."

**[wikidata] "United States economy shrinks by 0.1% in last quarter of 2012"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Wikinews article | instance of: Wikinews article..."

**[wikidata] "United States Economy with Alan Greenspan: Prospects For a Sustained Growth - 1976 (NAID 51060)"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "item in the National Archives and Records Administration's holdings | instance of: item of collection or exhibition..."

**[wikidata] "recession"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "business cycle contraction..."

**[wikidata] "Recession"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "2017 early access video game | instance of: video game..."

**[wikidata] "Recession's Greetings"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "painting by Jack Davis | instance of: painting | inception: January 1, 1974..."

### Verdict computation
  Supporting weight: 2.7467
  Opposing weight: 0.4054
  Support ratio: 0.8714
  Confidence: 0.7428
  Verdict: **strongly supported**
  Neutral sources (no contribution): 26

  Top supporting:
    - Great Recession in the United States (weight: 0.8259)
    - U.S. Economy Plunged Into Recession in February - The New York... (weight: 0.801)
    - The Economic Impacts of COVID-19: Evidence from a New Public Database Built Using Private Sector Data (weight: 0.7817)
    - The Coronavirus Stimulus Package: How Large is the Transfer Multiplier (weight: 0.338)
  Top opposing:
    - The energy shock isn’t likely to trigger a US... - RBC Economics (weight: 0.4054)

---
## 17. "violent video games cause real world violence"
Category: contested
Expected: contested
Actual: likely opposed (YES)
Claim type: factual (0.9972)

### Sources collected: 43 total
  - google_factcheck: 3
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 43 -> 36 (dropped 7)
Dropped sources:
  - [encyclopedia] "Harvester (video game)" (relevance: 0.2057, reason: non_content_pattern)
  - [academic] "Deep Learning-Based Violence Detection: A YOLO V7 Approach for Real-World Security Applications" (relevance: 0.3443, reason: relevance_0.344_below_0.35)
  - [academic] "The Use of Social Media in Children and Adolescents: Scoping Review on the Potential Risks" (relevance: 0.3001, reason: relevance_0.300_below_0.35)
  - [academic] "The psychological drivers of misinformation belief and its resistance to correction" (relevance: 0.0695, reason: relevance_0.069_below_0.35)
  - [academic] "Misinformation: susceptibility, spread, and interventions to immunize the public" (relevance: 0.12, reason: relevance_0.120_below_0.35)
  - [academic] "Annual Research Review: Sex, gender, and internalizing conditions among adolescents in the 21st century – trends, causes, consequences" (relevance: 0.2759, reason: relevance_0.276_below_0.35)
  - [academic] "Role of media – social, electronic, and print media – in mental health and wellbeing" (relevance: 0.2306, reason: relevance_0.231_below_0.35)

### Dedup: 36 -> 35 (dropped 1)

### Analyzed sources (35 total)

**[google_factcheck] "The Facts on Media Violence"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ""I’m hearing more and more people say the level of violence on video games is really shaping young people’s thoughts."..."

**[google_factcheck] "Do Video Games Lead to Mass Shootings? Researchers Say No ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Video games and violent movies lead to mass shootings...."

**[google_factcheck] "Fact check: Studies refute attempts to link video games, shootings"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Post implies school shootings are linked to violent video games..."

**[wikipedia] "Violence and video games"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.6211)
  Verdict contribution: opposing (weight: 0.5279)
  Snippet: "Since their inception in the 1970s, video games have often been criticized by some for violent content. Politicians, parents, and other activists have..."

**[wikipedia] "Graphic violence"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.978)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Graphic violence is a depiction of explicit or detailed acts of violence in mass media. It may be real, simulated live action, or animated.
Intended f..."

**[wikipedia] "Nonviolent video game"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9492)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Nonviolent video games are video games characterized by little or no violence. As the term is vague, game designers, developers, and marketers that de..."

**[wikipedia] "Effects of violence in mass media"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9736)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The study of violence in mass media analyzes the degree of correlation between themes of violence in media sources (particularly violence in video gam..."

**[wikipedia] "List of banned video games by country"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This is a list of video games that have been censored or banned by governments of various states in the world. Governments that have banned video game..."

**[wikipedia] "List of controversial video games"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9932)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This is a list of video games considered controversial. The list includes games that have earned controversies for violence, sexual content, racism, a..."

**[wikipedia] "Video game"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A video game, computer game, or simply game is an electronic game that involves interaction with a user interface or input device (such as a joystick,..."

**[wikipedia] "Game studies"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Game studies, also known as ludology (from ludus, "game", and -logia, "study", "research") or gaming theory, is
an interdisciplinary academic field fo..."

**[wikipedia] "Video game controversies"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There have been many debates on the social effects of video games on players and broader society, as well as debates within the video game industry. S..."

**[semantic_scholar] "Adolescent Aggression: A Narrative Review on the Potential Impact of Violent Video Games"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.6982)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background: Exposure to violent content through video games can shape perceptions of aggression as normative or acceptable, potentially desensitizing ..."

**[semantic_scholar] "Violent Video Games, Recruitment and Extremism"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.6831)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Violent video games are not always or perhaps even typically used for recruitment by extremist groups, even when extremists produce their own games. N..."

**[semantic_scholar] "Habitual engagement with violent video games does not translate virtual aggression to real-world emotional processing: insights from gaze behaviour metrics"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9668)
  Verdict contribution: opposing (weight: 0.3867)
  Snippet: "Habitual engagement with violent video games does not translate virtual aggression to real-world emotional processing: insights from gaze behaviour me..."

**[semantic_scholar] "The Influence of Moral Choices in Video Games on Real-World Decision-Making and Empathy"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9551)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This paper explores the impact of moral choices in video games on players' real-world decision-making and ethical behavior. This study highlights the ..."

**[semantic_scholar] "Towards Real-world Violence Recognition via Efficient Deep Features and Sequential Patterns Analysis"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9639)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Towards Real-world Violence Recognition via Efficient Deep Features and Sequential Patterns Analysis..."

**[semantic_scholar] "DVD: A Comprehensive Dataset for Advancing Violence Detection in Real-World Scenarios"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Violence Detection (VD) has become an increasingly vital area of research. Existing automated VD efforts are hindered by the limited availability of d..."

**[semantic_scholar] "Neuroimaging and behavioral evidence that violent video games exert no negative effect on human empathy for pain and emotional reactivity to violence"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9009)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Influential accounts claim that violent video games (VVGs) decrease players’ emotional empathy by desensitizing them to both virtual and real-life vio..."

**[semantic_scholar] "Violent Video Games on Aggression and Self-control of Student Gamers"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.915)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The rise in popularity of violent video games has sparked debates on their influence, particularly on aggression and self-control. Concerns about adul..."

**[semantic_scholar] "Desensitization and Violent Video Games: Mechanisms and Evidence."**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.7261)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Desensitization, the reduction of cognitive, emotional, and/or behavioral responses to a stimulus, is an automatic and unconscious phenomenon often ex..."

**[open_alex] "Possible Effects of Playing Video Games With Explicit Violence on Player Aggression"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.8833)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Video games have become the most significant phenomenon of popular culture, and one of the most widespread forms of entertainment in society of the In..."

**[open_alex] "VIDEO GAMES AND VIOLENCE: THE ONSLAUGHT ON YOUNG MINDS"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.5264)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Video games have long been popular in people of all ages. The Covid-19 pandemic led to a significant surge in use of digital technology globally inclu..."

**[open_alex] "A Positive Side of Violent Video Game Play"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.8267)
  Verdict contribution: opposing (weight: 0.4547)
  Snippet: "The exploration of the potential link between aggression and violent video game play has been extended to violent video game play as a precursor to vi..."

**[open_alex] ""Screen-time" for children and adolescents in COVID-19 times"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.5142)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The lockdown following the COVID-19 has changed the way a large proportion of people around the world go about their lives. Among the continued school..."

**[open_alex] "Don’t You Know That You’re Toxic: Normalization of Toxicity in Online Gaming"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Video game toxicity, endemic to online play, represents a pervasive and complex problem. Antisocial behaviours in online play directly harm player wel..."

**[duckduckgo] "The evidence that video game violence leads to real-world ..."**
  Type: web | Cred: estimated 0.40700000000000003
  NLI (nli_deberta): supporting (0.8276)
  Verdict contribution: supporting (weight: 0.3368)
  Snippet: "Oct 1, 2018 · A 2018 meta-analysis found that there is a small increase in real-world physical aggression among adolescents and pre-teens who play vio..."

**[duckduckgo] "Blame Game: Violent Video Games Do Not Cause Violence"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9814)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Apr 10, 2026 · In each study, the participants assigned to play a violent game seemed more prone to acting or thinking aggressively than those who pla..."

**[duckduckgo] "Violent Video Games: Impact, Science, and Controversy"**
  Type: web | Cred: estimated 0.409
  NLI (nli_deberta): neutral (0.9878)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Aug 21, 2025 · Explore the complex relationship between violent video games and real-world behavior, examining research, psychology, and societal fact..."

**[duckduckgo] "Do Video Games Cause Violence? Myths vs. Reality"**
  Type: web | Cred: estimated 0.429
  NLI (nli_deberta): opposing (0.9951)
  Verdict contribution: opposing (weight: 0.4269)
  Snippet: "May 6, 2026 · The myth that video games cause violence has persisted for far too long. Research shows that while violent media can have short-term eff..."

**[duckduckgo] "Violent Video Games and Aggression - National Center for ..."**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): neutral (0.9692)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In 2017, the APA Task Force on Violent Media concluded that violent video game exposure was linked to increased aggressive behaviors, thoughts, and em..."

**[duckduckgo] "Violent video games and young people - Harvard Health"**
  Type: web | Cred: estimated 0.329
  NLI (nli_deberta): supporting (0.9414)
  Verdict contribution: supporting (weight: 0.3097)
  Snippet: "Oct 1, 2010 · The view endorsed by organizations such as the American Academy of Pediatrics (AAP) and the American Academy of Child & Adolescent Psych..."

**[duckduckgo] "The contagious impact of playing violent video games on aggression"**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): neutral (0.9761)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Meta‐analyses have shown that violent video game play increases aggression in the player. The present research suggests that violent video game play a..."

**[duckduckgo] "What are your opinions on the effect that violence in video games ..."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.9482)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Dec 7, 2022 ... Playing violent video games significantly increases aggressive thoughts, emotions, and behavior. Even researchers in the violent games..."

**[duckduckgo] "Are Video Games Really Making Us More Violent? - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): supporting (0.9878)
  Verdict contribution: supporting (weight: 0.732)
  Snippet: "Jan 8, 2020 ... ... violent video games leads to mass homicide or violence in real life. Instead the debate in the research field is about the role vi..."

### Verdict computation
  Supporting weight: 1.3785
  Opposing weight: 2.6037
  Support ratio: 0.3462
  Confidence: 0.3077
  Verdict: **likely opposed**
  Neutral sources (no contribution): 27

  Top supporting:
    - Are Video Games Really Making Us More Violent? - YouTube (weight: 0.732)
    - The evidence that video game violence leads to real-world ... (weight: 0.3368)
    - Violent video games and young people - Harvard Health (weight: 0.3097)
  Top opposing:
    - Do Video Games Lead to Mass Shootings? Researchers Say No ... (weight: 0.8075)
    - Violence and video games (weight: 0.5279)
    - A Positive Side of Violent Video Game Play (weight: 0.4547)
    - Do Video Games Cause Violence? Myths vs. Reality (weight: 0.4269)
    - Habitual engagement with violent video games does not translate virtual aggression to real-world emotional processing: insights from gaze behaviour metrics (weight: 0.3867)

---
## 18. "smoking causes lung cancer"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.9978)

### Sources collected: 46 total
  - google_factcheck: 6
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 46 -> 44 (dropped 2)
Dropped sources:
  - [encyclopedia] "Tobacco packaging warning messages" (relevance: 0.3044, reason: relevance_0.304_below_0.35)
  - [encyclopedia] "Joseph Berkson" (relevance: 0.0436, reason: relevance_0.044_below_0.35)

### Dedup: 44 -> 44 (dropped 0)

### Analyzed sources (44 total)

**[google_factcheck] "Smoking had been identified as a causative factor for lung cancer by ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "CDC said cigarette smoking doesn't cause cancer in 1958..."

**[google_factcheck] "Science stubs out claim smoking doesn't cause cancer"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Smoking doesn’t cause cancer...."

**[google_factcheck] "Overwhelming scientific evidence shows that smoking causes lung ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Smoking may protect lungs from cancer..."

**[google_factcheck] "Claim that not all smokers develop lung discoloration ignores severe ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The black lung lie: It’s the widespread belief that smokers’ lungs turn black...."

**[google_factcheck] "Can marijuana smoking cause lung cancer?"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ""Despite decades of marijuana being used for smoking in the United States, there have been no reported medical cases of lung cancer" attributed to mar..."

**[google_factcheck] "Does Marijuana Contain More Tar Than Cigarettes?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Marijuana cigarettes deposit four times more tar into smokers' lungs than tobacco-based cigarettes...."

**[wikipedia] "Smoking-related interstitial fibrosis (SRIF)"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.6729)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Smoking-related interstitial fibrosis (SRIF) is an abnormality in the lungs characterized by excessive collagen deposition within the walls of the air..."

**[wikipedia] "Lung cancer"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.9486)
  Snippet: "Lung cancer, also called lung carcinoma, is a malignant tumor that originates in the tissues of the lungs. Lung cancer is caused by genetic damage to ..."

**[wikipedia] "Health effects of smoking tobacco"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Smoking tobacco has serious negative effects on human health. Smoking tobacco is the greatest cause of preventable death globally. Half of tobacco smo..."

**[wikipedia] "Smoking in China"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Smoking in China is prevalent, as the People's Republic of China is the world's largest consumer and producer of tobacco. As of 2022, there are around..."

**[wikipedia] "Comprehensive Smoking Education Act"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.9917)
  Verdict contribution: supporting (weight: 0.6942)
  Snippet: "The Comprehensive Smoking Education Act of 1984 (also known as the Rotational Warning Act) is an act of the Congress of the United States. A national ..."

**[wikipedia] "Causes of cancer"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cancer is caused by genetic changes leading to uncontrolled cell growth and tumor formation. The basic cause of sporadic (non-familial) cancers is DNA..."

**[wikipedia] "Non-small-cell lung cancer"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Non-small-cell lung cancer (NSCLC), or non-small-cell lung carcinoma, is a type of epithelial lung cancer other than small-cell lung cancer (SCLC). No..."

**[wikipedia] "Smoking cessation"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.7935)
  Verdict contribution: supporting (weight: 0.6745)
  Snippet: "Smoking cessation, usually called quitting smoking or stopping smoking, is the process of discontinuing tobacco smoking. Tobacco smoke contains nicoti..."

**[semantic_scholar] "The impact of smoking on lung cancer patients"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.5489)
  Snippet: "Although smoking prevalence has shown a decreasing trend, the total number of smokers remains high due to population growth. Smoking causes several di..."

**[semantic_scholar] "Multidimensional bioinformatics perspective on smoking-linked driver genes and immune regulatory mechanisms in non-small cell lung cancer"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9941)
  Verdict contribution: supporting (weight: 0.5468)
  Snippet: "Lung cancer, one of the leading causes of cancer-related morbidity and mortality worldwide, is strongly associated with smoking as its primary carcino..."

**[semantic_scholar] "Four decades of lung cancer: Trends in comorbidities and causes of death in a nationwide Danish cohort."**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9941)
  Verdict contribution: supporting (weight: 0.5468)
  Snippet: "BACKGROUND
Lung cancer remains the leading cause of cancer-related deaths globally, with gradual improvements in patient survival attributed to early ..."

**[semantic_scholar] "Identification of prognostic biomarkers of smoking-related lung cancer"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.8301)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background The early diagnosis and effective prognostic treatment measures for lung cancer are still limited, leading to a 5-year survival rate of les..."

**[semantic_scholar] "Implications of the Immune Landscape in COPD and Lung Cancer: Smoking Versus Other Causes"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.7944)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cigarette smoking is reported in about one third of adults worldwide. A strong relationship between cigarette smoke exposure and chronic obstructive p..."

**[semantic_scholar] "CYP2A6 activity and cigarette consumption interact in smoking-related lung cancer susceptibility"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9858)
  Verdict contribution: supporting (weight: 0.6408)
  Snippet: "Cigarette smoke, containing both nicotine and carcinogens, causes lung cancer. However, not all smokers develop lung cancer, highlighting the importan..."

**[semantic_scholar] "Tumor Suppressor miR-584-5p Inhibits Migration and Invasion in Smoking Related Non-Small Cell Lung Cancer Cells by Targeting YKT6"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.6478)
  Snippet: "Simple Summary Cigarette smoke is a major carcinogen that causes lung cancer and induces DNA methylation. DNA methylation regulates the expression of ..."

**[semantic_scholar] "Advancements in lung cancer: molecular insights, innovative therapies, and future prospects"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9907)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Advancements in lung cancer: molecular insights, innovative therapies, and future prospects..."

**[semantic_scholar] "TP53 common variants and interaction with PPP1R13L and CD3EAP SNPs and lung cancer risk and smoking behavior in a Chinese population"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.814)
  Verdict contribution: supporting (weight: 0.4477)
  Snippet: "Background TP53 encodes a tumor suppressor protein containing cell cycle arrest, apoptosis, senescence, DNA repair, or changes in metabolism. The effe..."

**[semantic_scholar] "Broadening the Net: Overcoming Challenges and Embracing Novel Technologies in Lung Cancer Screening."**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.8882)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Lung cancer is one of the leading causes of cancer-related mortality worldwide, with most cases diagnosed at advanced stages where curative treatment ..."

**[open_alex] "Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries"**
  Type: academic | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.7856)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This article presents global cancer statistics by world region for the year 2022 based on updated estimates from the International Agency for Research..."

**[open_alex] "Screening for Lung Cancer"**
  Type: academic | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.4849)
  Verdict contribution: supporting (weight: 0.4607)
  Snippet: "IMPORTANCE: Lung cancer is the second most common cancer and the leading cause of cancer death in the US. In 2020, an estimated 228 820 persons were d..."

**[open_alex] "Implications of the Immune Landscape in COPD and Lung Cancer: Smoking Versus Other Causes"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.7944)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cigarette smoking is reported in about one third of adults worldwide. A strong relationship between cigarette smoke exposure and chronic obstructive p..."

**[open_alex] "The global burden of lung cancer: current status and future trends"**
  Type: academic | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.9619)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The global burden of lung cancer: current status and future trends..."

**[open_alex] "Epidemiology of lung cancer"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.7973)
  Snippet: "Lung cancer is the leading cause of global cancer incidence and mortality, accounting for an estimated 2 million diagnoses and 1.8 million deaths. Neo..."

**[open_alex] "Lung cancer statistics, 2023"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9868)
  Verdict contribution: supporting (weight: 0.7894)
  Snippet: "Despite decades of declining mortality rates, lung cancer remains the leading cause of cancer death in the United States. This article examines lung c..."

**[open_alex] "Lung cancer in patients who have never smoked — an emerging disease"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.7236)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Lung cancer in patients who have never smoked — an emerging disease..."

**[open_alex] "Appraising the causal role of smoking in multiple diseases: A systematic review and meta-analysis of Mendelian randomization studies"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.644)
  Verdict contribution: supporting (weight: 0.5152)
  Snippet: "BACKGROUND: The causal association between cigarette smoking and several diseases remains equivocal. The purpose of this study was to appraise the cau..."

**[open_alex] "Screening for lung cancer: 2023 guideline update from the American Cancer Society"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9312)
  Verdict contribution: supporting (weight: 0.745)
  Snippet: "Lung cancer is the leading cause of mortality and person-years of life lost from cancer among US men and women. Early detection has been shown to be a..."

**[open_alex] "Mapping of global, regional and national incidence, mortality and mortality-to-incidence ratio of lung cancer in 2020 and 2050"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.795)
  Snippet: "AIM: Lung cancer is the leading cause of cancer deaths worldwide. This study examines the current and future burden of lung cancer at global, regional..."

**[duckduckgo] "Lung Cancer Causes | Lung Cancer in Non-Smokers"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.9481)
  Snippet: "Learn about different causes of lung cancer including tobacco smoking.Smoking tobacco is by far the leading cause of lung cancer. About 85% of lung ca..."

**[duckduckgo] "How does smoking cause cancer? | Cancer Research UK"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9956)
  Verdict contribution: supporting (weight: 0.4022)
  Snippet: "What types of cancer does smoking cause? The link between smoking and cancer is very clear. It causes at least 16 different types of cancer, including..."

**[duckduckgo] "Lung cancer - Causes - NHS"**
  Type: web | Cred: estimated 0.41600000000000004
  NLI (nli_deberta): supporting (0.6562)
  Verdict contribution: supporting (weight: 0.273)
  Snippet: "It can sometimes be found in buildings. If radon is breathed in, it can damage your lungs, particularly if you smoke. Radon gas causes a small number ..."

**[duckduckgo] "Lung Cancer Causes & Risk Factors | American Lung Association"**
  Type: web | Cred: verified 0.85 | Bias: pro-science/left-center | Factual: high
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.8483)
  Snippet: "Smoking is the number one cause of lung cancer. It causes about 90 percent of lung cancer cases. Tobacco smoke contains many chemicals that are known ..."

**[duckduckgo] "How Smoking Causes Lung Cancer"**
  Type: web | Cred: estimated 0.477
  NLI (nli_deberta): supporting (0.543)
  Verdict contribution: supporting (weight: 0.259)
  Snippet: ""When smoking causes inflammation in the lungs – as it always does – the inflammatory response increases damage to our DNA, making cancer more likely...."

**[duckduckgo] "How Many Cigarettes Do You Need to Smoke to Get Cancer?"**
  Type: web | Cred: verified 0.5 | Bias: pro-science | Factual: mixed
  NLI (nli_deberta): supporting (0.9922)
  Verdict contribution: supporting (weight: 0.4961)
  Snippet: "The more cigarettes you smoke per day, the higher your chances of developing cancer. According to the Centers for Disease Control and Prevention (CDC)..."

**[duckduckgo] "Lung Cancer Causes and Risks Explained at kokilaben hospital"**
  Type: web | Cred: estimated 0.23399999999999999
  NLI (nli_deberta): supporting (0.9956)
  Verdict contribution: supporting (weight: 0.233)
  Snippet: "What causes lung cancer isn’t always straightforward. Smoking is the leading cause, responsible for about 85% of cases. But what about the remaining 1..."

**[duckduckgo] "What Causes Lung Cancer?"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9941)
  Verdict contribution: supporting (weight: 0.845)
  Snippet: "Smoking causes about 90% of lung cancer cases. It also has a link to more than a dozen other types of cancer. Cigarettes have about 250 harmful chemic..."

**[duckduckgo] "What Causes Lung Cancer? Scary Risks Found - Liv Hospital"**
  Type: web | Cred: estimated 0.327
  NLI (nli_deberta): supporting (0.9941)
  Verdict contribution: supporting (weight: 0.3251)
  Snippet: "Lung cancer is a big health worry, and knowing its risks is key. We know that smoking is the main cause of lung cancer. It’s behind up to 80-90% of ca..."

**[duckduckgo] "Not Enough Smoking Causes Lung Cancer - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.9839)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "L. Ron Hubbard Narconon Scientology pseudoscience quackery. Science fiction writer, Hubbard did have his way with words, and plenty of them, but much ..."

### Verdict computation
  Supporting weight: 16.7231
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 17

  Top supporting:
    - Lung cancer (weight: 0.9486)
    - Lung Cancer Causes | Lung Cancer in Non-Smokers (weight: 0.9481)
    - Lung Cancer Causes & Risk Factors | American Lung Association (weight: 0.8483)
    - What Causes Lung Cancer? (weight: 0.845)
    - Epidemiology of lung cancer (weight: 0.7973)

---
## 19. "capitalism is better than socialism"
Category: opinion
Expected: opinion
Actual: strongly opposed (**NO - MISMATCH**)
Claim type: factual (0.992)

### Sources collected: 50 total
  - google_factcheck: 1
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 50 -> 36 (dropped 14)
Dropped sources:
  - [encyclopedia] "Socialism in the United States" (relevance: 0.2918, reason: relevance_0.292_below_0.35)
  - [encyclopedia] "Nordic model" (relevance: 0.3421, reason: relevance_0.342_below_0.35)
  - [academic] "Liberating Enslaved Humanity: Decolonial Political Thought of Abul Hashim" (relevance: 0.1855, reason: relevance_0.186_below_0.35)
  - [academic] "Vietnam tourism at the crossroads of socialism and market economy" (relevance: 0.1747, reason: relevance_0.175_below_0.35)
  - [academic] "African solutions to African problems: a narrative of corruption in postcolonial Africa" (relevance: 0.161, reason: relevance_0.161_below_0.35)
  - [academic] "The internal fragility of representative democracy: was Schumpeter right?" (relevance: 0.2505, reason: relevance_0.251_below_0.35)
  - [academic] "Deliberative Democracy or Agonistic Pluralism?" (relevance: 0.2532, reason: relevance_0.253_below_0.35)
  - [academic] "Economic growth and income inequality" (relevance: 0.1935, reason: relevance_0.193_below_0.35)
  - [academic] "Sustainalism: An Integrated Socio-Economic-Environmental Model to Address Sustainable Development and Sustainability" (relevance: 0.3049, reason: relevance_0.305_below_0.35)
  - [academic] "Critiques of the circular economy" (relevance: 0.2445, reason: relevance_0.244_below_0.35)
  - [knowledge_graph] "Better" (relevance: 0.1345, reason: relevance_0.134_below_0.35)
  - [knowledge_graph] "Better" (relevance: 0.0358, reason: relevance_0.036_below_0.35)
  - [knowledge_graph] "better85 (Conrad Honey)" (relevance: 0.1184, reason: relevance_0.118_below_0.35)
  - [knowledge_graph] "Socialism and Freedom Party" (relevance: 0.2973, reason: relevance_0.297_below_0.35)

### Dedup: 36 -> 36 (dropped 0)

### Analyzed sources (36 total)

**[google_factcheck] "Quote Falsely Tied to Ocasio-Cortez"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Meme quotes Alexandria Ocasio-Cortez as saying, "Under capitalism, man oppresses man. Under socialism, it’s the other way around."..."

**[wikipedia] "Authoritarian socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Authoritarian socialism, or socialism from above, is an economic and political system supporting some form of socialist economics while rejecting poli..."

**[wikipedia] "Late capitalism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Late capitalism (or late-stage capitalism) is a concept in political economy, political science and sociology. It is used by social critics to describ..."

**[wikipedia] "Democratic socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8413)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Democratic socialism is a left-wing set of political philosophies that supports political democracy and some form of a socially owned economy, with a ..."

**[wikipedia] "Socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Socialism is an economic and political philosophy encompassing diverse economic and social systems characterised by social ownership of the means of p..."

**[wikipedia] "Scientific socialism"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Scientific socialism in Marxism is the application of historical materialism to the development of socialism, as not just a practical and achievable o..."

**[wikipedia] "Market socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Market socialism is a type of economic system involving social ownership of the means of production within the framework of a market economy. Various ..."

**[wikipedia] "Socialism with Chinese characteristics"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Socialism with Chinese characteristics (Chinese: 中国特色社会主义; pinyin: Zhōngguó tèsè shèhuìzhǔyì; Mandarin: [ʈʂʊ́ŋ.kwǒ tʰɤ̂.sɤ̂ ʂɤ̂.xwêɪ.ʈʂù.î] ) is a ter..."

**[wikipedia] "Anarchism and capitalism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9873)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The nature of capitalism is criticized by most anarchists, who reject hierarchy and advocate stateless societies based on non-hierarchical voluntary a..."

**[semantic_scholar] "Would Democratic Socialism Be Better?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.7964)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The case for a modern democratic humane socialism typically has two parts. The first is that capitalism is bad, at or least not very good. In reaching..."

**[semantic_scholar] "Is a capitalist steady-state economy possible? Is it better in socialism?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.5449)
  Verdict contribution: opposing (weight: 0.2997)
  Snippet: "Is a capitalist steady-state economy possible? Is it better in socialism?..."

**[semantic_scholar] "Rethinking Development"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Perhaps there has never been a better historical moment to interrogate development. The fog of market fundamentalism and the neoliberal consensus has ..."

**[semantic_scholar] "Cows, Moonshine, Pheasants … versus Soybeans"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9839)
  Verdict contribution: opposing (weight: 0.3936)
  Snippet: "
 Drawing on decades of participant observation, followed by ethnographic research in Novoalexeevka (the Russian Far East), this article reveals why a..."

**[semantic_scholar] "Would Democratic Socialism Be Better?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9204)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The relative merits of democratic socialism are becoming progressively more relevant in the United States. More Americans are beginning to see through..."

**[semantic_scholar] "Global Capitalism and Climate Change: The Need for an Alternative System by Hans A. Baer"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9824)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It is something of a cliché to quote Karl Marx’s (1845) observation in Eleven Theses on Feuerbach, where he wrote, “The philosophers have only interpr..."

**[open_alex] "Would Democratic Socialism Be Better?"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.791)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract The case for a modern democratic humane socialism typically has two parts. The first is that capitalism is bad, at or least not very good. In..."

**[open_alex] "Left Turn Ahead: Surveying Attitudes of Young People Towards Capitalism and Socialism"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Left Turn Ahead: Surveying Attitudes of Young People Towards Capitalism and Socialism..."

**[open_alex] "Would Democratic Socialism Be Better Than Social Democratic Capitalism?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.6328)
  Verdict contribution: opposing (weight: 0.2531)
  Snippet: "What kind of economic system do we want? Should democratic socialism be a prominent part of the conversation? The case for a modern, democratic, human..."

**[open_alex] "Would Democratic Socialism Be Better Than Social Democratic Capitalism?"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9375)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract Should you favor democratic socialism? If you believe strongly in workplace democracy and are willing to mandate it, or if you attach a high ..."

**[open_alex] "Introduction to Neoliberal Social Justice"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.8945)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "What sort of social institutions, in practice, represent Rawlsian commitments to free and equal citizenship and distributive justice? Many philosopher..."

**[open_alex] "Socialism"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.5484)
  Snippet: "Abstract This book provides an introduction to arguments for and against socialism. The approach is logical and analytic: arguments are broken down in..."

**[duckduckgo] "Why Capitalism is Better than Socialism | by Ebenezer... | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.5459)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "When the government has a heavy hand in the free market it can stifle what the businesses can do as well as undo the positive effects of a capitalist ..."

**[duckduckgo] "Is Capitalism Better Than Socialism? Bryan Caplan and Elizabeth..."**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Under capitalism, how people use their freedom is up to them. What’s so awesome about the capitalist ideal? It’s a system based on individual freedom ..."

**[duckduckgo] "5 Reasons Socialism Is Inferior To Capitalism"**
  Type: web | Cred: verified 0.5 | Bias: right | Factual: mixed
  NLI (nli_deberta): opposing (0.9263)
  Verdict contribution: opposing (weight: 0.4632)
  Snippet: "Saying that capitalism is better than socialism is like saying that winning a million dollars is better than being in a high impact car crash...."

**[duckduckgo] "20 Quotes That Explain Why Capitalism Is Better Than Socialism - AEI"**
  Type: web | Cred: verified 0.5 | Bias: right | Factual: mixed
  NLI (nli_deberta): neutral (0.6753)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Socialism is a plan of morally sanctioned theft. It is about dividing up what others have created. Consequently, socialist economies don’t work; they ..."

**[duckduckgo] "Why Capitalism is Better than Socialism | Free Essay Example"**
  Type: web | Cred: estimated 0.37
  NLI (nli_deberta): supporting (0.835)
  Verdict contribution: supporting (weight: 0.309)
  Snippet: "For instance, during President Obama’s term, the rate of growth of the economy reduced and only increased when the government implemented tax deregula..."

**[duckduckgo] "Comparing Socialism and Capitalism"**
  Type: web | Cred: estimated 0.42300000000000004
  NLI (nli_deberta): neutral (0.9565)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "(iii) When arguing that capitalism is better than socialism, Brennan often refers to the virtues of markets. But this neglects the varieties of social..."

**[duckduckgo] "(doc) this house believes that capitalism is better than socialism"**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): neutral (0.9199)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Capitalism can be seen as the better economic choice because capitalist countries are usually much more technologically advanced, and because individu..."

**[duckduckgo] "5 Key Reasons Capitalism Is Better Than Socialism"**
  Type: web | Cred: estimated 0.327
  NLI (nli_deberta): neutral (0.7871)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Capitalism describes the desirable version of life whereas socialism describes the depressing one. Why is hating capitalism the newest trend in the me..."

**[duckduckgo] "Capitalism is better than socialism for creating jobs"**
  Type: web | Cred: estimated 0.5429999999999999
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Capitalism is opposed particularly by socialists and defended mainly by conservatives.A social system based on the principle of individual rights. Pol..."

**[duckduckgo] "Capitalism is better than socialism | Forum"**
  Type: web | Cred: estimated 0.41600000000000004
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Capitalism is a bank. Socialism is a credit union. If you're claiming anything more condemning about either, you're projecting a bias upon it to push ..."

**[wikidata] "Capitalism"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "1995 video game | instance of: video game..."

**[wikidata] "capitalism"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "economic system based on private ownership of the means of production | instance of: social formation..."

**[wikidata] "Capitalism: A Journal of History and Economics"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "trans-disciplinary journal | instance of: scientific journal | country: United States | inception: January 2, 2020..."

**[wikidata] "socialism"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "socio-economic system based on social ownership of the means of production; also the ideology that aims to implement it | instance of: political ideol..."

**[wikidata] "socialist mode of production"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "marxian economy centered around use value, planning and contribution-based distribution | instance of: mode of production..."

### Verdict computation
  Supporting weight: 0.309
  Opposing weight: 1.9579
  Support ratio: 0.1363
  Confidence: 0.7274
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 30

  Top supporting:
    - Why Capitalism is Better than Socialism | Free Essay Example (weight: 0.309)
  Top opposing:
    - Socialism (weight: 0.5484)
    - 5 Reasons Socialism Is Inferior To Capitalism (weight: 0.4632)
    - Cows, Moonshine, Pheasants … versus Soybeans (weight: 0.3936)
    - Is a capitalist steady-state economy possible? Is it better in socialism? (weight: 0.2997)
    - Would Democratic Socialism Be Better Than Social Democratic Capitalism? (weight: 0.2531)

---
## 20. "we only use 10% of our brains"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.9943)

### Sources collected: 48 total
  - google_factcheck: 2
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 48 -> 16 (dropped 32)
Dropped sources:
  - [fact_check] "Image Accurately Depicts a 1 Cubic Millimeter Sample of a Human ..." (relevance: 0.31, reason: relevance_0.310_below_0.35)
  - [encyclopedia] "Boltzmann brain" (relevance: 0.3128, reason: relevance_0.313_below_0.35)
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: 0.1232, reason: relevance_0.123_below_0.35)
  - [encyclopedia] "Equipotentiality" (relevance: 0.297, reason: relevance_0.297_below_0.35)
  - [encyclopedia] "Bad Brains" (relevance: 0.2098, reason: relevance_0.210_below_0.35)
  - [encyclopedia] "Eat, Brains, Love" (relevance: 0.1981, reason: relevance_0.198_below_0.35)
  - [encyclopedia] "Barry Beyerstein" (relevance: 0.2028, reason: relevance_0.203_below_0.35)
  - [encyclopedia] "Brain in a vat" (relevance: 0.2964, reason: relevance_0.296_below_0.35)
  - [encyclopedia] "Dunbar's number" (relevance: 0.2357, reason: relevance_0.236_below_0.35)
  - [encyclopedia] "Tanzschein" (relevance: 0.1105, reason: relevance_0.110_below_0.35)
  - [academic] "WE ONLY USE 10% OF OUR BRAINS AND OTHER NEUROMYTHS – A SURVEY OF TEACHERS IN BOSNIA AND HERZEGOVINA" (relevance: 0.2946, reason: relevance_0.295_below_0.35)
  - [academic] "Sex-Specific Concordance of Striatal Transcriptional Signatures of Opioid Addiction in Human and Rodent Brains" (relevance: 0.1673, reason: relevance_0.167_below_0.35)
  - [academic] "The individualized neural tuning model: Precise and generalizable cartography of functional architecture in individual brains" (relevance: 0.2992, reason: relevance_0.299_below_0.35)
  - [academic] "Practice makes plasticity: 10-Hz rTMS enhances LTP-like plasticity in musicians and athletes" (relevance: 0.2708, reason: relevance_0.271_below_0.35)
  - [academic] "Interleukin-10 improves stroke outcome by controlling the detrimental Interleukin-17A response" (relevance: 0.1545, reason: relevance_0.154_below_0.35)
  - [academic] "Resting-State Functional Connectivity Predicts Attention Problems in Children: Evidence from the ABCD Study" (relevance: 0.219, reason: relevance_0.219_below_0.35)
  - [academic] "Stealing Brains: From English to Czech Language Model" (relevance: 0.1488, reason: relevance_0.149_below_0.35)
  - [academic] "Region-specific ups and downs in mitochondrial numerical densities during Alzheimer's disease progression: A pilot study in human brains" (relevance: 0.185, reason: relevance_0.185_below_0.35)
  - [academic] "Initiative, Immersive Human–Computer Interactions: Software-Defined Memristive Neural Networks for Nonlinear Heterogeneous Scheme in Internet of Brains" (relevance: 0.1979, reason: relevance_0.198_below_0.35)
  - [academic] "WE ONLY USE 10% OF OUR BRAINS AND OTHER NEUROMYTHS – A SURVEY OF TEACHERS IN BOSNIA AND HERZEGOVINA" (relevance: 0.2946, reason: relevance_0.295_below_0.35)
  - [academic] "High-Order Interdependencies in the Aging Brain" (relevance: 0.1292, reason: relevance_0.129_below_0.35)
  - [academic] "Systemic infection exacerbates cerebrovascular dysfunction in Alzheimer’s disease" (relevance: 0.0374, reason: relevance_0.037_below_0.35)
  - [academic] "Review of deep learning: concepts, CNN architectures, challenges, applications, future directions" (relevance: 0.2214, reason: relevance_0.221_below_0.35)
  - [academic] "The Elements of Intelligence" (relevance: 0.3004, reason: relevance_0.300_below_0.35)
  - [academic] "Classification of diseases with accumulation of Tau protein" (relevance: 0.1625, reason: relevance_0.162_below_0.35)
  - [academic] "Structural differences in adolescent brains can predict alcohol misuse" (relevance: 0.2631, reason: relevance_0.263_below_0.35)
  - [academic] "Practice makes plasticity: 10-Hz rTMS enhances LTP-like plasticity in musicians and athletes" (relevance: 0.2708, reason: relevance_0.271_below_0.35)
  - [academic] "Differential perivascular microglial activation in the deep white matter in vascular dementia developed post‐stroke" (relevance: 0.1532, reason: relevance_0.153_below_0.35)
  - [academic] "Reactive astrocyte nomenclature, definitions, and future directions" (relevance: 0.0101, reason: relevance_0.010_below_0.35)
  - [knowledge_graph] "Wednesday" (relevance: -0.0112, reason: relevance_-0.011_below_0.35)
  - [knowledge_graph] "Welsh" (relevance: -0.0272, reason: relevance_-0.027_below_0.35)
  - [knowledge_graph] "West Germany" (relevance: 0.0257, reason: relevance_0.026_below_0.35)

### Dedup: 16 -> 15 (dropped 1)

### Analyzed sources (15 total)

**[google_factcheck] "Do We Only Use 10% of our Brains?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Humans only use 10% of their brains...."

**[wikipedia] "Ten-percent-of-the-brain myth"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.8062)
  Verdict contribution: supporting (weight: 0.645)
  Snippet: "The ten-percent-of-the-brain myth or ninety-percent-of-the-brain myth states that humans generally use only one-tenth (or some other small fraction) o..."

**[semantic_scholar] "Organisation for Economic Co-operation and Development (OECD)"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.769)
  Verdict contribution: supporting (weight: 0.3076)
  Snippet: "One of the most persistent and widely spread brain myths states that we only use 10% of our brains. What a shock, if we think of the 90% of our brain ..."

**[duckduckgo] "Do we only use 10% of our brains?"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): opposing (0.9829)
  Verdict contribution: opposing (weight: 0.8355)
  Snippet: "Yet many people do cling on to the idea that we only use 10% of our brains.He was not only wrong about the 10%, but he was also wrong about the impact..."

**[duckduckgo] "Are We Really Only Using 10% of Our Brains? | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): opposing (0.8789)
  Verdict contribution: opposing (weight: 0.4395)
  Snippet: "The myth that we only utilise 10% of our brain’s capacity is one of my favourites.Our brain can be stimulated in several ways by learning a new skill,..."

**[duckduckgo] "It’s a myth that we only use 10% of our brains – here’s why"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): opposing (0.9731)
  Verdict contribution: opposing (weight: 0.9244)
  Snippet: "If we were only regularly using only 10% of our brains at any given time, we might all be prone to cerebral atrophy, resembling patients with neurodeg..."

**[duckduckgo] "Debunking the Myth: Do We Really Only Use 10% of Our Brains?"**
  Type: web | Cred: estimated 0.346
  NLI (nli_deberta): opposing (0.9556)
  Verdict contribution: opposing (weight: 0.3306)
  Snippet: "For instance, if we truly only used 10% of our brain, scans of inactive areas would be dark and empty, but that's not what scientists find. Instead, i..."

**[duckduckgo] "Is it true or false that we only use 10% of our brains? - Brainly.in"**
  Type: web | Cred: estimated 0.42000000000000004
  NLI (nli_deberta): neutral (0.5278)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Brain uses 20% of the total oxygen in the blood. It it doesn't get oxygen for 5 to 6 minutes it will die. There are 100 billion neurones present in ou..."

**[duckduckgo] "Do we really use only 10% of our brain? Think again."**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.645)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "..."

**[duckduckgo] "Ten-percent-of-the-brain myth"**
  Type: web | Cred: estimated 0.47800000000000004
  NLI (nli_deberta): opposing (0.9927)
  Verdict contribution: opposing (weight: 0.4745)
  Snippet: "The common myth that humans use only 10% of their brain capacity, which is debunked as we actually use virtually all of our brain. Explanation of the ..."

**[duckduckgo] "2 Popular Psychology Myths, Debunked | Psychology Today"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.9282)
  Verdict contribution: opposing (weight: 0.789)
  Snippet: "If we only use 10% of our brains, then traumatic brain injuries to the other 90% would have no effect on our functioning. In reality, however, there’s..."

**[duckduckgo] "7 myths about the human body that are often mistaken as facts"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.9917)
  Verdict contribution: supporting (weight: 0.3997)
  Snippet: "1. We only use 10% of our brains.This is probably why the factoid that we only use 10% of our brains has such traction. It’s a silly fact, though...."

**[wikidata] "Our brains are not us."**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scientific article published in July 2009 | instance of: scholarly article..."

**[wikidata] "Our Brains are Targets No. 1, Cleared for Firing - an Overview"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scientific article published in 2021 | instance of: scholarly article..."

**[wikidata] "Our brains electric"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scientific article published in 2020 | instance of: scholarly article..."

### Verdict computation
  Supporting weight: 1.3522
  Opposing weight: 4.2685
  Support ratio: 0.2406
  Confidence: 0.5188
  Verdict: **likely opposed**
  Neutral sources (no contribution): 5

  Top supporting:
    - Ten-percent-of-the-brain myth (weight: 0.645)
    - 7 myths about the human body that are often mistaken as facts (weight: 0.3997)
    - Organisation for Economic Co-operation and Development (OECD) (weight: 0.3076)
  Top opposing:
    - It’s a myth that we only use 10% of our brains – here’s why (weight: 0.9244)
    - Do we only use 10% of our brains? (weight: 0.8355)
    - 2 Popular Psychology Myths, Debunked | Psychology Today (weight: 0.789)
    - Do We Only Use 10% of our Brains? (weight: 0.475)
    - Ten-percent-of-the-brain myth (weight: 0.4745)

---
## 21. "social media is harmful to mental health"
Category: contested
Expected: contested
Actual: sources lean supporting (**NO - MISMATCH**)
Claim type: opinion (0.9832)

### Sources collected: 49 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 49 -> 40 (dropped 9)
Dropped sources:
  - [encyclopedia] "Mental disorder" (relevance: 0.3305, reason: relevance_0.331_below_0.35)
  - [encyclopedia] "List of mental disorders" (relevance: 0.325, reason: relevance_0.325_below_0.35)
  - [knowledge_graph] "social media" (relevance: 0.3389, reason: relevance_0.339_below_0.35)
  - [knowledge_graph] "influencer" (relevance: 0.2684, reason: relevance_0.268_below_0.35)
  - [knowledge_graph] "substance abuse" (relevance: 0.2207, reason: relevance_0.221_below_0.35)
  - [knowledge_graph] "alcohol abuse" (relevance: 0.2104, reason: relevance_0.210_below_0.35)
  - [knowledge_graph] "Harmful Algae" (relevance: 0.1955, reason: relevance_0.196_below_0.35)
  - [knowledge_graph] "mental health" (relevance: 0.3414, reason: relevance_0.341_below_0.35)
  - [knowledge_graph] "mental disorder" (relevance: 0.3476, reason: relevance_0.348_below_0.35)

### Dedup: 40 -> 40 (dropped 0)

### Analyzed sources (40 total)

**[wikipedia] "Digital media use and mental health"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9854)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Researchers in psychology, sociology, anthropology, and medicine have studied the relationship between digital media use and mental health since the m..."

**[wikipedia] "Mental illness in media"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9766)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Mental illnesses, also known as psychiatric disorders, are often inaccurately portrayed in the media. Films, television programs, books, magazines, an..."

**[wikipedia] "Social media"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Social media are new media technologies that facilitate the creation, sharing and aggregation of content (such as ideas, interests, and other forms of..."

**[wikipedia] "The Anxious Generation"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9858)
  Verdict contribution: supporting (weight: 0.7886)
  Snippet: "The Anxious Generation: How the Great Rewiring of Childhood Is Causing an Epidemic of Mental Illness is a 2024 book by Jonathan Haidt. It argues that ..."

**[wikipedia] "Problematic social media use"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9971)
  Verdict contribution: supporting (weight: 0.8475)
  Snippet: "Excessive use of social media can lead to problems including impaired functioning and a reduction in overall wellbeing, for both users and those aroun..."

**[wikipedia] "Artificial intelligence in mental health"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial intelligence in mental health refers to the application of artificial intelligence (AI), computational technologies and algorithms to suppo..."

**[wikipedia] "Social determinants of mental health"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The social determinants of mental health (SDOMH) are societal problems that disrupt mental health, increase risk of mental illness among certain group..."

**[wikipedia] "Mental health"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Mental health encompasses emotional, psychological, and social well-being, influencing cognition, perception, and behavior. Mental health plays a cruc..."

**[semantic_scholar] "The Harmful Effects of Social Media Addiction on Mental Health: A Qualitative Study"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.999)
  Verdict contribution: supporting (weight: 0.3996)
  Snippet: "Objective: The aim of this study was to examine the harmful effects of social media addiction on the mental health of students and to identify the fac..."

**[semantic_scholar] "There is no evidence that time spent on social media is correlated with adolescent mental health problems: Findings from a meta-analysis."**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9404)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The issue of whethersocial media use does or does not in ﬂ uence youth internalizingmental health disorders (e.g., anxiety, depression) remains a pres..."

**[semantic_scholar] "36. Adolescent Mental Health and Big Tech: Investigating Policy Avenues to Regulate Harmful Social Media Algorithms"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.5088)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Purpose: Adolescents are using social media now more than ever, especially given the ongoing COVID-19 pandemic. A growing body of research demonstrate..."

**[semantic_scholar] "Navigating the Digital Maze: A Review of AI Bias, Social Media, and Mental Health in Generation Z"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.5161)
  Verdict contribution: supporting (weight: 0.2839)
  Snippet: "The rapid adoption of artificial intelligence (AI) within social media platforms has fundamentally transformed the way Generation Z interacts with and..."

**[semantic_scholar] "Public and mental health professionals’ perspectives on social media and suicide exposure"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9795)
  Verdict contribution: supporting (weight: 0.5387)
  Snippet: "The rapid evolution of social media in recent years has increased public exposure to suicide. While research has highlighted concerns about the role o..."

**[semantic_scholar] "Debate: Social media in children and young people – time for a ban? From polarised debate to precautionary action – a population mental health perspective on social media and youth well‐being"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9761)
  Verdict contribution: supporting (weight: 0.5369)
  Snippet: "Adolescents spend much of their daily lives online, with social media a central part of their digital environment. While findings are complex, evidenc..."

**[semantic_scholar] "Broken Shields: Holding Social Media Giants Accountable for the Youth Mental Health Crisis"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9893)
  Verdict contribution: supporting (weight: 0.5441)
  Snippet: "The United States is experiencing a youth mental health crisis associated with the rise in social media pervasiveness. As a result, state attorneys ge..."

**[semantic_scholar] "An Analysis of Demand Characteristics: Uncovering the True Effects of Social Media on Mental Health"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9629)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "As social media use continues to rise, concerns about its effects on mental health remain debated. While some research links social media to adverse m..."

**[semantic_scholar] "MindSET: Advancing Mental Health Benchmarking through Large-Scale Social Media Data"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Social media data has become a vital resource for studying mental health, offering real-time insights into thoughts, emotions, and behaviors that trad..."

**[semantic_scholar] "Debate: Social media in children and young people – time for a ban? Beyond bans: addressing the digital determinants of youth mental health and well‐being in the European region"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9956)
  Verdict contribution: supporting (weight: 0.5476)
  Snippet: "The complex role that social media plays in shaping young people's mental health and well‐being requires a nuanced approach to regulation beyond simpl..."

**[open_alex] "Social Media Addiction and Mental Health Among University Students During the COVID-19 Pandemic in Indonesia"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9746)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Social Media Addiction and Mental Health Among University Students During the COVID-19 Pandemic in Indonesia..."

**[open_alex] "Exploring adolescents’ perspectives on social media and mental health and well-being – A qualitative literature review"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9248)
  Verdict contribution: supporting (weight: 0.7398)
  Snippet: "Many quantitative studies have supported the association between social media use and poorer mental health, with less known about adolescents' perspec..."

**[open_alex] "36. Adolescent Mental Health and Big Tech: Investigating Policy Avenues to Regulate Harmful Social Media Algorithms"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.7861)
  Verdict contribution: supporting (weight: 0.4324)
  Snippet: "36. Adolescent Mental Health and Big Tech: Investigating Policy Avenues to Regulate Harmful Social Media Algorithms..."

**[open_alex] "There Is No Evidence That Associations Between Adolescents’ Digital Technology Engagement and Mental Health Problems Have Increased"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9214)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Digital technology is ubiquitous in modern adolescence, and researchers are concerned that it has negative impacts on mental health that, furthermore,..."

**[open_alex] "“I See Me Here”: Mental Health Content, Community, and Algorithmic Curation on TikTok"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.7563)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Social media platforms are a place where people look for information and social support for mental health, resulting in both positive and negative eff..."

**[open_alex] "Problematic social media use in childhood and adolescence"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9731)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "At the time of writing, about 4.59 billion people use social media with many adolescents using their social media accounts across a myriad of applicat..."

**[open_alex] "Social Media–Driven Routes to Positive Mental Health Among Youth: Qualitative Enquiry and Concept Mapping Study"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.7793)
  Verdict contribution: opposing (weight: 0.5065)
  Snippet: "BACKGROUND: Social media influence almost every aspect of our lives by facilitating instant many-to-many communication and self-expression. Recent res..."

**[open_alex] "Reviewing the Impact of Social Media on the Mental Health of Adolescents and Young Adults"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.6478)
  Snippet: "Adolescents now cannot imagine their lives without social media. Practitioners want to be able to assess risk, and social media may be a new factor to..."

**[open_alex] "Social media use of adolescents who died by suicide: lessons from a psychological autopsy study"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9932)
  Verdict contribution: supporting (weight: 0.6456)
  Snippet: "BACKGROUND: while there are many benefits for young people to use social media, adverse effects such as cyberbullying, online challenges, social compa..."

**[open_alex] "Social media and mental health in students: a cross-sectional study during the Covid-19 pandemic"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.7061)
  Verdict contribution: supporting (weight: 0.459)
  Snippet: "BACKGROUND: Social media causes increased use and problems due to their attractions. Hence, it can affect mental health, especially in students. The p..."

**[duckduckgo] "Social Media and Mental Health: Benefits, Risks, and Opportunities ..."**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): supporting (0.6299)
  Verdict contribution: supporting (weight: 0.3641)
  Snippet: "Recent studies have reported negative effects of social media use on mental health of young people, including social comparison pressure with others a..."

**[duckduckgo] "Social media's impact on our mental health and tips to use it safely"**
  Type: web | Cred: estimated 0.465
  NLI (nli_deberta): supporting (0.9863)
  Verdict contribution: supporting (weight: 0.4586)
  Snippet: "May 10, 2024 · Social media can negatively impact our overall wellbeing by fueling anxiety, depression, loneliness and FOMO (fear or missing out)...."

**[duckduckgo] "Social Media and Mental Health - HelpGuide.org"**
  Type: web | Cred: estimated 0.40499999999999997
  NLI (nli_deberta): supporting (0.8892)
  Verdict contribution: supporting (weight: 0.3601)
  Snippet: "Excessive social media use can trigger feelings of inadequacy, dissatisfaction, and isolation, and worsen symptoms of depression, anxiety, and stress...."

**[duckduckgo] "Social Media and Mental Health in Children and Teens"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): neutral (0.9868)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sep 25, 2024 · Some experts believe that mental health concerns may be an unexpected side effect of increased social media use...."

**[duckduckgo] "Effects of Social Media on Mental Health"**
  Type: web | Cred: estimated 0.323
  NLI (nli_deberta): supporting (0.8301)
  Verdict contribution: supporting (weight: 0.2681)
  Snippet: "Dec 12, 2024 · Multiple studies have found a strong link between heavy social media and an increased risk of depression, anxiety, loneliness, self-har..."

**[duckduckgo] "Social Media Addiction and Mental Health: The Growing Concern for ..."**
  Type: web | Cred: estimated 0.49000000000000005
  NLI (nli_deberta): supporting (0.5278)
  Verdict contribution: supporting (weight: 0.2586)
  Snippet: "May 20, 2024 · A systematic review found that the use of social networking sites is associated with an increased risk of depression, anxiety, and psyc..."

**[duckduckgo] "[PDF] Social Media and Youth Mental Health - HHS.gov"**
  Type: web | Cred: estimated 0.41
  NLI (nli_deberta): neutral (0.9927)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Child and adolescent use of platforms designed for adults places them at high risk of “unsupervised, developmentally inappropriate, and potentially ha..."

**[duckduckgo] "Scrolling and Stress: The Impact of Social Media on Mental Health"**
  Type: web | Cred: estimated 0.322
  NLI (nli_deberta): supporting (0.9478)
  Verdict contribution: supporting (weight: 0.3052)
  Snippet: "Mar 30, 2026 · It's not just in your head—social media can fuel anxiety, disrupt sleep, and leave you feeling alone in a crowd · Keep Reading To Learn..."

**[duckduckgo] "Social Media Use and Impact on Mental Health - NAMI"**
  Type: web | Cred: estimated 0.563
  NLI (nli_deberta): supporting (0.9624)
  Verdict contribution: supporting (weight: 0.5418)
  Snippet: "Social media use also poses risks to mental health, including increased exposure to cyberbullying, disordered eating, harmful content, and discriminat..."

**[duckduckgo] "How Social Media Affects Your Teen's Mental Health: A Parent's Guide"**
  Type: web | Cred: estimated 0.33399999999999996
  NLI (nli_deberta): neutral (0.9839)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jun 17, 2024 · Social media use may be associated with distinct changes in the developing brain, potentially affecting such functions as emotional lea..."

**[wikidata] "social networking service"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "online platform that facilitates the building of social relations..."

**[wikidata] "Mental Health"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "medical journal | instance of: scientific journal..."

### Verdict computation
  Supporting weight: 9.968
  Opposing weight: 0.5065
  Support ratio: 0.9516
  Confidence: 0.9033
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 19

  Top supporting:
    - Problematic social media use (weight: 0.8475)
    - The Anxious Generation (weight: 0.7886)
    - Exploring adolescents’ perspectives on social media and mental health and well-being – A qualitative literature review (weight: 0.7398)
    - Reviewing the Impact of Social Media on the Mental Health of Adolescents and Young Adults (weight: 0.6478)
    - Social media use of adolescents who died by suicide: lessons from a psychological autopsy study (weight: 0.6456)
  Top opposing:
    - Social Media–Driven Routes to Positive Mental Health Among Youth: Qualitative Enquiry and Concept Mapping Study (weight: 0.5065)

---
## 22. "the Beatles are the greatest band of all time"
Category: opinion
Expected: opinion
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.9973)

### Sources collected: 36 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 36 -> 24 (dropped 12)
Dropped sources:
  - [encyclopedia] "Rolling Stone's 500 Greatest Songs of All Time" (relevance: 0.3443, reason: relevance_0.344_below_0.35)
  - [academic] "Neurophysiological Synchrony Between Children With Severe Physical Disabilities and Their Parents During Music Therapy" (relevance: 0.0766, reason: relevance_0.077_below_0.35)
  - [academic] "Vidding" (relevance: 0.0919, reason: relevance_0.092_below_0.35)
  - [academic] "Measuring Attribution in Natural Language Generation Models" (relevance: -0.049, reason: relevance_-0.049_below_0.35)
  - [academic] "ChoCo: a Chord Corpus and a Data Transformation Workflow for Musical Harmony Knowledge Graphs" (relevance: 0.1479, reason: relevance_0.148_below_0.35)
  - [academic] "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model" (relevance: -0.0221, reason: relevance_-0.022_below_0.35)
  - [academic] "The illusion of data validity: Why numbers about people are likely wrong" (relevance: -0.0541, reason: relevance_-0.054_below_0.35)
  - [academic] "Song Form and the Mainstreaming of Hip-Hop Music" (relevance: 0.122, reason: relevance_0.122_below_0.35)
  - [academic] "Beyond Tools and Function: The Selection of Materials and the Ontology of Hunter-Gatherers. Ethnographic Evidences and Implications for Palaeolithic Archaeology" (relevance: 0.0183, reason: relevance_0.018_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.1062, reason: relevance_0.106_below_0.35)
  - [knowledge_graph] "time" (relevance: 0.0729, reason: relevance_0.073_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.1418, reason: relevance_0.142_below_0.35)

### Dedup: 24 -> 23 (dropped 1)

### Analyzed sources (23 total)

**[wikipedia] "With the Beatles"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With the Beatles is the second studio album by the English rock band the Beatles. It was released in the United Kingdom on 22 November 1963 on Parloph..."

**[wikipedia] "The Beatles albums discography"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Worldwide, the English rock band the Beatles have released 12 studio albums (17 in the US), 5 live albums, 52 compilation albums, 36 extended plays (E..."

**[wikipedia] "A Collection of Beatles Oldies"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A Collection of Beatles Oldies (subtitled But Goldies!) is a compilation album by the English rock band the Beatles. Released in the United Kingdom on..."

**[wikipedia] "NME's The 500 Greatest Albums of All Time"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.7119)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ""The 500 Greatest Albums of All Time" is a 2013 special issue of the British magazine NME. The list presented was compiled based on votes from current..."

**[wikipedia] "The Beatles"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Beatles were an English rock band formed in Liverpool in 1960. The band comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr. Th..."

**[wikipedia] "Rolling Stone's 100 Greatest Artists of All Time"**
  Type: encyclopedia | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ""The 100 Greatest Artists of All Time" was a special issue published by Rolling Stone in two parts in 2004 and 2005, and later updated in 2011. The li..."

**[wikipedia] "Revolver (Beatles album)"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Revolver is the seventh studio album by the English rock band the Beatles. It was released on 5 August 1966, accompanied by the double A-side single "..."

**[wikipedia] "Outline of the Beatles"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The following outline is provided as an overview of and topical guide to the Wikipedia articles available about the Beatles from their formation throu..."

**[wikipedia] "Band on the Run"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Band on the Run is the third studio album by the British rock band Paul McCartney and Wings, released on 30 November 1973 in the United Kingdom and 5 ..."

**[open_alex] "<i>The Beatles: Get Back</i>, directed by Peter Jackson"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9282)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The first episode of The Beatles: Get Back debuted on November 25, 2021—which might be the only undeniable certainty of the endeavor. The three-episod..."

**[open_alex] "The original music  artists and their music I love - The Beatles            "**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8433)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The original music artists and their music I love - The BeatlesYiren Qin1,*1Black Family Stem Cell Institute, Department of Cell, Developmental and Re..."

**[duckduckgo] "The Beatles are the greatest band of all time. Here's why"**
  Type: web | Cred: estimated 0.277
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Aug 27, 2025 · In just ten years, The Beatles changed the face of Western popular culture. Their songs have never lost their relevance, speaking to yo..."

**[duckduckgo] "'60s Group Ranked #1 'Greatest Classic Rock Band of All Time ..."**
  Type: web | Cred: estimated 0.47400000000000003
  NLI (nli_deberta): supporting (0.7285)
  Verdict contribution: supporting (weight: 0.3453)
  Snippet: "Oct 19, 2025 · The Beatles top a new poll as the greatest classic rock band of all time, decades after redefining music and culture in the 1960s...."

**[duckduckgo] "Why The Beatles Are the Greatest Band of All Time (Lessons ..."**
  Type: web | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.9517)
  Verdict contribution: supporting (weight: 0.6662)
  Snippet: "Dec 17, 2025 · What I found affirmed what I long felt in my heart: The Beatles stand as the greatest band of all time, and their journey holds lessons..."

**[duckduckgo] "Top 7 reasons why the Beatles are the greatest band ever"**
  Type: web | Cred: estimated 0.21800000000000003
  NLI (nli_deberta): supporting (0.8633)
  Verdict contribution: supporting (weight: 0.1882)
  Snippet: "May 11, 2023 · Beatles are unquestionably the best and most important band in rock history. 7 amazing reasons why the Beatles and their songs are the ..."

**[duckduckgo] "What makes The Beatles the most influential band of all time?"**
  Type: web | Cred: verified 0.85 | Bias: right-center | Factual: high
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jul 3, 2019 · Over 50 years since The Beatles disbanded, the band and its music and image are still so familiar that a movie can imagine a world where..."

**[duckduckgo] "Does anyone here believe The Beatles are the greatest band of ..."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.9468)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Does anyone here believe The Beatles are the greatest band of all time and it’s not even particularly close? I’ve been listening for a little over a m..."

**[duckduckgo] "The Beatles: the Greatest Band of All Time? - PHDessay.com"**
  Type: web | Cred: estimated 0.433
  NLI (nli_deberta): neutral (0.918)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Harvard "The Beatles: the Greatest Band of All Time ... ASA "The Beatles: the Greatest Band of All Time?," Free Essays - PhDessay.com , 13-Apr-2017...."

**[duckduckgo] "The Beatlesfrom Greatest Rock Bands of All Time List 😉"**
  Type: web | Cred: estimated 0.28900000000000003
  NLI (nli_deberta): neutral (0.5508)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Ask a random stranger on the street, what's the greatest band of all times? There are big chances of replying "The Beatles", their influences not ......"

**[duckduckgo] "The Beatlesfrom Best Bands of All Time List 😉"**
  Type: web | Cred: estimated 0.28900000000000003
  NLI (nli_deberta): neutral (0.6885)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Whether or not the Beatles are the greatest band of all time will always be up for debate. ... the Beatles are objectively the greatest band of all ....."

**[wikidata] "The Beatles"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "English pop rock band (1960–1970) | instance of: musical group | inception: 1960-00-00 | dissolved: April 10, 1970..."

**[wikidata] "Beatles"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "vocal track by Flamingokvintetten; 1977 studio recording | instance of: music track with vocals..."

**[wikidata] "Beatles for Sale"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "1964 studio album by the Beatles | instance of: album..."

### Verdict computation
  Supporting weight: 1.1997
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 20

  Top supporting:
    - Why The Beatles Are the Greatest Band of All Time (Lessons ... (weight: 0.6662)
    - '60s Group Ranked #1 'Greatest Classic Rock Band of All Time ... (weight: 0.3453)
    - Top 7 reasons why the Beatles are the greatest band ever (weight: 0.1882)

---
## 23. "antibiotics do not work against viruses"
Category: factual_true
Expected: strongly supported
Actual: likely supported (YES)
Claim type: factual (0.9975)

### Sources collected: 45 total
  - google_factcheck: 2
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 45 -> 30 (dropped 15)
Dropped sources:
  - [encyclopedia] "Respiratory syncytial virus" (relevance: 0.3118, reason: relevance_0.312_below_0.35)
  - [encyclopedia] "Ebola" (relevance: 0.2585, reason: relevance_0.258_below_0.35)
  - [encyclopedia] "Travelers' diarrhea" (relevance: 0.1205, reason: relevance_0.120_below_0.35)
  - [encyclopedia] "Lyme disease" (relevance: 0.1064, reason: relevance_0.106_below_0.35)
  - [encyclopedia] "Bacteriophage" (relevance: 0.319, reason: relevance_0.319_below_0.35)
  - [encyclopedia] "Pneumonia" (relevance: 0.1044, reason: relevance_0.104_below_0.35)
  - [academic] "Identification and dynamics of novel scaffolds against Enterococcus faecium serine hydroxymethyltransferase enzyme: a potential target for antibiotics development" (relevance: 0.3433, reason: relevance_0.343_below_0.35)
  - [academic] "Surviving sepsis campaign: international guidelines for management of sepsis and septic shock 2021" (relevance: 0.0929, reason: relevance_0.093_below_0.35)
  - [academic] "Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050" (relevance: 0.3029, reason: relevance_0.303_below_0.35)
  - [academic] "Microbiota in health and diseases" (relevance: 0.2449, reason: relevance_0.245_below_0.35)
  - [academic] "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021" (relevance: 0.1313, reason: relevance_0.131_below_0.35)
  - [academic] "Antimicrobial Face Shield: Next Generation of Facial Protective Equipment against SARS-CoV-2 and Multidrug-Resistant Bacteria" (relevance: 0.3201, reason: relevance_0.320_below_0.35)
  - [academic] "Infectious disease in an era of global change" (relevance: 0.3208, reason: relevance_0.321_below_0.35)
  - [academic] "2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure" (relevance: 0.0334, reason: relevance_0.033_below_0.35)
  - [academic] "Emerging concepts in the science of vaccine adjuvants" (relevance: 0.2199, reason: relevance_0.220_below_0.35)

### Dedup: 30 -> 30 (dropped 0)

### Analyzed sources (30 total)

**[google_factcheck] "Consuming antibiotics cannot treat Covid-19 | Fact Check"**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Drinking amoxicillin diluted in water can help treat Covid-19..."

**[google_factcheck] "No, COVID-19 won’t respond to antibiotics, despite findings from ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "“Autopsies prove that COVID-19 is” a blood clot, not pneumonia, “and ought to be fought with antibiotics” and the whole world has been wrong in treati..."

**[wikipedia] "Antibiotic"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.8487)
  Snippet: "An antibiotic is a type of antimicrobial substance active against bacteria. It is the most important type of antibacterial agent for fighting bacteria..."

**[wikipedia] "Introduction to viruses"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.9902)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A virus is a tiny infectious agent that reproduces inside the cells of living hosts. When infected, the host cell is forced to rapidly produce thousan..."

**[wikipedia] "Antibiotic misuse"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9829)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Antibiotic misuse, sometimes called antibiotic abuse or antibiotic overuse, refers to the misuse or overuse of antibiotics, with potentially serious e..."

**[wikipedia] "Amoxicillin"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9858)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Amoxicillin is an antibiotic medication belonging to the aminopenicillin class of the penicillin family. The drug is used to treat bacterial infection..."

**[semantic_scholar] "Studies on Comparative Analysis of Antimicrobial Strength of Three Over the Counter Commonly Used Antibiotics: A Case Study in Owerri Municipal"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.3992)
  Snippet: "Antibiotics are drugs that either halt bacterial growth or kills the bacteria entirely. The comparative analysis of these three most common antibiotic..."

**[semantic_scholar] "Virucidal Activity of the Drug «Thymogen®», a Nasal Dosed Spray, Against Human Respiratory Viruses In Vitro"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8784)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background. Respiratory syncytial virus (RSV) and parainfluenza virus together account for up to 40% of the pathogens causing acute respiratory infect..."

**[semantic_scholar] "Repositioning of Antibiotics in the Treatment of Viral Infections"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9966)
  Verdict contribution: opposing (weight: 0.5481)
  Snippet: "Drug repurposing, also known as drug repositioning, is a currently tested approach by which new uses are being assigned for already tested drugs. In t..."

**[semantic_scholar] "Genome Features and In Vitro Activity against Influenza A and SARS-CoV-2 Viruses of Six Probiotic Strains"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.7349)
  Verdict contribution: opposing (weight: 0.4777)
  Snippet: "Purpose The aim of this work was to analyze the complete genome of probiotic bacteria Lactobacillus plantarum 8 RA 3, Lactobacillus fermentum 90 TC-4,..."

**[semantic_scholar] "An Instant Update on Viruses"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9976)
  Verdict contribution: supporting (weight: 0.5487)
  Snippet: "Abstract The current COVID-19 pandemic shows how little many people know about viruses. Yet apart from COVID-19, the world has observed epidemic sprea..."

**[semantic_scholar] "Targeting bacterial persistence with bacteriophages: a next-generation antimicrobial strategy."**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.5151)
  Verdict contribution: supporting (weight: 0.2833)
  Snippet: "Antibiotic resistance has become a problem of global concern. However, less focus has been placed on scenarios where antibiotics fail to work in the a..."

**[semantic_scholar] "Klebsiella pneumoniae Phage M198 and Its Therapeutic Potential"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.5742)
  Verdict contribution: opposing (weight: 0.3158)
  Snippet: "The rapid worldwide spread of antibiotic resistance is quickly becoming an increasingly concerning problem for human healthcare. Non-antibiotic antiba..."

**[semantic_scholar] "Infected burn wound healing using Hydroxy-propyl-methyl cellulose gel containing bacteriophages against Pseudomonas aeruginosa and Klebsiella pneumoniae"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8975)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background and Objectives: Pseudomonas aeruginosa (P. aeruginosa) and Klebsiella pneumoniae (K. pneumoniae) are the two leading bacterial strains invo..."

**[semantic_scholar] "Bacteriophage-antibiotic combination therapy against extensively drug-resistant Pseudomonas aeruginosa infection to allow liver transplantation in a toddler"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.9824)
  Verdict contribution: opposing (weight: 0.7859)
  Snippet: "Post-operative bacterial infections are a leading cause of mortality and morbidity after ongoing liver transplantation. Bacteria causing these infecti..."

**[open_alex] "The overlooked pandemic of antimicrobial resistance"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9741)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The overlooked pandemic of antimicrobial resistance..."

**[open_alex] "Genome Features and <i>In Vitro</i> Activity against Influenza A and SARS‐CoV‐2 Viruses of Six Probiotic Strains"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.8813)
  Verdict contribution: opposing (weight: 0.5728)
  Snippet: "Purpose . The aim of this work was to analyze the complete genome of probiotic bacteria Lactobacillus plantarum 8 RA 3, Lactobacillus fermentum 90 TC‐..."

**[duckduckgo] "Why are antibiotics ineffective against viruses? - The AMR Narrative"**
  Type: web | Cred: estimated 0.34199999999999997
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.3398)
  Snippet: "November 21, 2025 - So, antibiotics are ineffective against viruses, simply because viruses are not cells and do not have those “machineries” that ant..."

**[duckduckgo] "Why Don’t Antibiotics Work on Viruses | Dragonfly Medical and Behavioral Health"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.7275)
  Verdict contribution: supporting (weight: 0.1455)
  Snippet: "January 5, 2026 - Most antibiotics are designed to attack bacterial cell walls, protein synthesis, or metabolic processes. Viruses do not have these s..."

**[duckduckgo] "Antibiotics | Johns Hopkins Medicine"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.978)
  Verdict contribution: supporting (weight: 0.9291)
  Snippet: "However, treating viral infections with antibiotics in order to prevent bacterial infections is not recommended because of the risk of causing bacteri..."

**[duckduckgo] "Fighting viruses with antibiotics: an overlooked path - PMC - NIH"**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): neutral (0.9727)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Checking your browser before accessing pmc.ncbi.nlm.nih.gov · Click here if you are not automatically redirected after 5 seconds..."

**[duckduckgo] "Viral Infections - Why Don't Antibiotics Kill Viruses? - Drugs.com"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.9883)
  Verdict contribution: supporting (weight: 0.9389)
  Snippet: "June 2, 2025 - But why don’t antibiotics kill ... reasons are that: Antibiotics cannot kill viruses because viruses have different structures and repl..."

**[duckduckgo] "Antibiotics: Not always the answer - Mayo Clinic Health System"**
  Type: web | Cred: estimated 0.414
  NLI (nli_deberta): supporting (0.9897)
  Verdict contribution: supporting (weight: 0.4097)
  Snippet: "March 20, 2024 - Viruses are not cells — they are even smaller particles that require a host, such as your healthy sinus or lung cells, to survive and..."

**[duckduckgo] "Why antibiotics can’t be used to treat viruses, colds or the flu | Vaccination Matters"**
  Type: web | Cred: estimated 0.254
  NLI (nli_deberta): supporting (0.9961)
  Verdict contribution: supporting (weight: 0.253)
  Snippet: "March 29, 2023 - When you’re sick all you want is a medicine that will make everything better. It’s the same when someone you care for is sick. Unfort..."

**[duckduckgo] "Why are there so many drugs to kill bacteria, but so few to tackle viruses?"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.944)
  Snippet: "August 27, 2025 - https://theconversation.com/why-are-there-so-many-drugs-to-kill-bacteria-but-so-few-to-tackle-viruses-137480 ... As the end of the s..."

**[duckduckgo] "Why Don’t Doctors Give Antibiotics for Viral Infections?"**
  Type: web | Cred: estimated 0.24700000000000003
  NLI (nli_deberta): supporting (0.9512)
  Verdict contribution: supporting (weight: 0.2349)
  Snippet: "November 12, 2025 - Since viruses behave differently from bacteria, antibiotics simply do not affect them. Antibiotics work by targeting structures or..."

**[duckduckgo] "Antibiotics: Know When You Need Them | Atrium Health"**
  Type: web | Cred: estimated 0.458
  NLI (nli_deberta): supporting (0.9927)
  Verdict contribution: supporting (weight: 0.4547)
  Snippet: "Antibiotics work by killing bacteria, but they won’t help your symptoms of viruses like colds or the flu. Learn how to use antibiotics the right way...."

**[wikidata] "Antibiotics"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scientific journal published by MDPI | instance of: scientific journal | country: Switzerland..."

**[wikidata] "antibiotic"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "drug used in the treatment and prevention of bacterial infections | instance of: class of chemical entities with similar applications or functions..."

**[wikidata] "Antibiotics & Chemotherapy"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "US medical journal | instance of: scientific journal..."

### Verdict computation
  Supporting weight: 8.2596
  Opposing weight: 2.7004
  Support ratio: 0.7536
  Confidence: 0.5072
  Verdict: **likely supported**
  Neutral sources (no contribution): 10

  Top supporting:
    - Why are there so many drugs to kill bacteria, but so few to tackle viruses? (weight: 0.944)
    - Viral Infections - Why Don't Antibiotics Kill Viruses? - Drugs.com (weight: 0.9389)
    - Antibiotics | Johns Hopkins Medicine (weight: 0.9291)
    - Antibiotic (weight: 0.8487)
    - Consuming antibiotics cannot treat Covid-19 | Fact Check (weight: 0.765)
  Top opposing:
    - Bacteriophage-antibiotic combination therapy against extensively drug-resistant Pseudomonas aeruginosa infection to allow liver transplantation in a toddler (weight: 0.7859)
    - Genome Features and <i>In Vitro</i> Activity against Influenza A and SARS‐CoV‐2 Viruses of Six Probiotic Strains (weight: 0.5728)
    - Repositioning of Antibiotics in the Treatment of Viral Infections (weight: 0.5481)
    - Genome Features and In Vitro Activity against Influenza A and SARS-CoV-2 Viruses of Six Probiotic Strains (weight: 0.4777)
    - Klebsiella pneumoniae Phage M198 and Its Therapeutic Potential (weight: 0.3158)

---
## 24. "goldfish have a 3 second memory"
Category: factual_false
Expected: strongly opposed
Actual: contested (**NO - MISMATCH**)
Claim type: factual (0.998)

### Sources collected: 43 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 43 -> 14 (dropped 29)
Dropped sources:
  - [encyclopedia] "Goldfish (band)" (relevance: 0.4996, reason: non_content_pattern)
  - [encyclopedia] "Hippocampus" (relevance: 0.2468, reason: relevance_0.247_below_0.35)
  - [encyclopedia] "Goodbye Mr. Fish" (relevance: 0.2792, reason: relevance_0.279_below_0.35)
  - [encyclopedia] "Kowloon Generic Romance" (relevance: -0.0227, reason: relevance_-0.023_below_0.35)
  - [encyclopedia] "Panpanya" (relevance: 0.1242, reason: relevance_0.124_below_0.35)
  - [encyclopedia] "David Attenborough" (relevance: 0.0714, reason: relevance_0.071_below_0.35)
  - [encyclopedia] "The Walls" (relevance: 0.191, reason: relevance_0.191_below_0.35)
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: 0.0577, reason: relevance_0.058_below_0.35)
  - [encyclopedia] "Muscle memory" (relevance: 0.3015, reason: relevance_0.301_below_0.35)
  - [academic] "Effects of auditory processing, memory, and experience on early and later stages of second language speech learning" (relevance: 0.2768, reason: relevance_0.277_below_0.35)
  - [academic] "Working memory and second language writing: A systematic review" (relevance: 0.2485, reason: relevance_0.249_below_0.35)
  - [academic] "MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations" (relevance: 0.2567, reason: relevance_0.257_below_0.35)
  - [academic] "Meta's Second Generation AI Chip: Model-Chip Co-Design and Productionization Experiences" (relevance: 0.2536, reason: relevance_0.254_below_0.35)
  - [academic] "Term immune memory responses to human papillomavirus (HPV) vaccination following 2 versus 3 doses of HPV vaccine." (relevance: 0.1686, reason: relevance_0.169_below_0.35)
  - [academic] "The Infralimbic, but not the Prelimbic Cortex is needed for a Complex Olfactory Memory Task" (relevance: 0.3093, reason: relevance_0.309_below_0.35)
  - [academic] "Learning-dependent modulation of working memory" (relevance: 0.2893, reason: relevance_0.289_below_0.35)
  - [academic] "3DL-PIM: A Look-Up Table Oriented Programmable Processing in Memory Architecture Based on the 3-D Stacked Memory for Data-Intensive Applications" (relevance: 0.292, reason: relevance_0.292_below_0.35)
  - [academic] "Engineered T cells secreting anti-BCMA T cell engagers control multiple myeloma and promote immune memory in vivo" (relevance: 0.0498, reason: relevance_0.050_below_0.35)
  - [academic] "Repeated Omicron exposures redirect SARS-CoV-2–specific memory B cell evolution toward the latest variants" (relevance: 0.1963, reason: relevance_0.196_below_0.35)
  - [academic] "Improving the Domain Adaptation of Retrieval Augmented Generation (RAG) Models for Open Domain Question Answering" (relevance: 0.1547, reason: relevance_0.155_below_0.35)
  - [academic] "Additive manufacturing of structural materials" (relevance: 0.0095, reason: relevance_0.010_below_0.35)
  - [academic] "BASS: multi-scale and multi-sample analysis enables accurate cell type clustering and spatial domain detection in spatial transcriptomic studies" (relevance: 0.1061, reason: relevance_0.106_below_0.35)
  - [academic] "Apparatus design and behavioural testing protocol for the evaluation of spatial working memory in mice through the spontaneous alternation T-maze" (relevance: 0.2998, reason: relevance_0.300_below_0.35)
  - [academic] "ConceptFusion: Open-set multimodal 3D mapping" (relevance: 0.0874, reason: relevance_0.087_below_0.35)
  - [academic] "Parallel subgenome structure and divergent expression evolution of allo-tetraploid common carp and goldfish" (relevance: 0.2575, reason: relevance_0.258_below_0.35)
  - [academic] "The effect of environmental stressors on growth in fish and its endocrine control" (relevance: 0.2358, reason: relevance_0.236_below_0.35)
  - [academic] "Corporate Climate Risk: Measurements and Responses" (relevance: -0.017, reason: relevance_-0.017_below_0.35)
  - [academic] "AnchorWave: Sensitive alignment of genomes with high sequence diversity, extensive structural polymorphism, and whole-genome duplication" (relevance: 0.1687, reason: relevance_0.169_below_0.35)
  - [academic] "MemoryBank: Enhancing Large Language Models with Long-Term Memory" (relevance: 0.3169, reason: relevance_0.317_below_0.35)

### Dedup: 14 -> 14 (dropped 0)

### Analyzed sources (14 total)

**[wikipedia] "Goldfish"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The goldfish (Carassius auratus) is a freshwater fish in the family Cyprinidae of the order Cypriniformes. It is commonly kept as a pet in indoor aqua..."

**[duckduckgo] "Do Goldfish Really Have A 3-Second Memory? » ScienceABC"**
  Type: web | Cred: estimated 0.23199999999999998
  NLI (nli_deberta): opposing (0.8066)
  Verdict contribution: opposing (weight: 0.1871)
  Snippet: "We often compare this frustrating experience to the life of a goldfish, as though they are always forgetting what they were just doing. But do goldfis..."

**[duckduckgo] "Goldfish three-second memory myth busted - ABC News"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.8018)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is a popular belief that goldfish only have a three-second memory span and every lap of their fishbowl is like seeing the world for the first ti..."

**[duckduckgo] "Hi friend, which one is right? 1. Goldfish have a 3 second memory or..."**
  Type: web | Cred: estimated 0.33199999999999996
  NLI (nli_deberta): supporting (0.9922)
  Verdict contribution: supporting (weight: 0.3294)
  Snippet: "1. Goldfish have a 3 second memory = correct! goldfish have 3 second memories. Doesn’t work... but it so almost correct fee would notice.NOTE: "3-seco..."

**[duckduckgo] "Do goldfish have a 3-second memory? Learn how memory work in..."**
  Type: web | Cred: estimated 0.33799999999999997
  NLI (nli_deberta): opposing (0.8853)
  Verdict contribution: opposing (weight: 0.2992)
  Snippet: "You may have heard that goldfish only have a memory of 3 seconds. This is a common myth, but it is not true. Goldfish are far smarter than many people..."

**[duckduckgo] "MythBuster: Goldfish Have a 3-Second Memory — STEAM Ahead"**
  Type: web | Cred: estimated 0.303
  NLI (nli_deberta): neutral (0.7612)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "“I have the memory of a goldfish!” It’s a common phrase used to describe forgetfulness, and it’s based on the popular belief that goldfish can only re..."

**[duckduckgo] "Do fish really have a 3 second memory? | Interviews"**
  Type: web | Cred: estimated 0.252
  NLI (nli_deberta): opposing (0.8291)
  Verdict contribution: opposing (weight: 0.2089)
  Snippet: "And these memories last for months, not minutes. According to a study by animal psychologists at Plymouth University, goldfish can even tell the time...."

**[duckduckgo] "Myth #8: Goldfish have a 3-second memory."**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.2993)
  Snippet: "✍️ TL;DR❌ Goldfish do not have a 3-second memory.✅ They can remember tasks, routes, and associations for months...."

**[duckduckgo] "Is the popular notion that a goldfish only has a 3 second memory..."**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.5874)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Most people think goldfish only have a 3 second memory, but the truth is very different.The research into the behaviour of the goldfish regarding memo..."

**[duckduckgo] "Goldfish Have a 3-Second Memory (Myth Debunked) - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.9185)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In this series, Professor Raja Sharma presents videos that debunk common myths, providing fresh perspectives and deeper insights. The visuals used in ..."

**[duckduckgo] "Unraveling 10 Misconceptions You Didn’t Know Were Wrong | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.959)
  Verdict contribution: supporting (weight: 0.4795)
  Snippet: "3. **Goldfish Have a 3-Second Memory:** Contrary to the belief that goldfish have a memory span of only three seconds, studies have shown that they ca..."

**[wikidata] "goldfish"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "species of freshwater fish, common in aquariums | instance of: taxon..."

**[wikidata] "Goldfish"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "video game developed by Gabry Corti | instance of: video game..."

**[wikidata] "Goldfish"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "South African electronic music duo | instance of: musical duo..."

### Verdict computation
  Supporting weight: 0.8089
  Opposing weight: 0.9946
  Support ratio: 0.4485
  Confidence: 0.1029
  Verdict: **contested**
  Neutral sources (no contribution): 8

  Top supporting:
    - Unraveling 10 Misconceptions You Didn’t Know Were Wrong | Medium (weight: 0.4795)
    - Hi friend, which one is right? 1. Goldfish have a 3 second memory or... (weight: 0.3294)
  Top opposing:
    - Myth #8: Goldfish have a 3-second memory. (weight: 0.2993)
    - Do goldfish have a 3-second memory? Learn how memory work in... (weight: 0.2992)
    - Do fish really have a 3 second memory? | Interviews (weight: 0.2089)
    - Do Goldfish Really Have A 3-Second Memory? » ScienceABC (weight: 0.1871)

---
## 25. "immigration is good for the economy"
Category: contested
Expected: contested
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.9861)

### Sources collected: 43 total
  - google_factcheck: 4
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 43 -> 25 (dropped 18)
Dropped sources:
  - [encyclopedia] "Modern immigration to the United Kingdom" (relevance: 0.3267, reason: relevance_0.327_below_0.35)
  - [encyclopedia] "Chinese Exclusion Act" (relevance: 0.2899, reason: relevance_0.290_below_0.35)
  - [encyclopedia] "2024 Keir Starmer speech on migration" (relevance: 0.3257, reason: relevance_0.326_below_0.35)
  - [encyclopedia] "Operation Metro Surge" (relevance: 0.2379, reason: relevance_0.238_below_0.35)
  - [academic] "Understanding rural system with a social-ecological framework: Evaluating sustainability of rural evolution in Jiangsu province, South China" (relevance: 0.1085, reason: relevance_0.108_below_0.35)
  - [academic] "Pandemic Politics" (relevance: 0.1351, reason: relevance_0.135_below_0.35)
  - [academic] "Trump’s authoritarian neoliberal governance and the US-Mexican border" (relevance: 0.3431, reason: relevance_0.343_below_0.35)
  - [academic] "A theory of migration: the aspirations-capabilities framework" (relevance: 0.2615, reason: relevance_0.261_below_0.35)
  - [academic] "<scp>WHO</scp>'s global oral health status report 2022: Actions, discussion and implementation" (relevance: 0.0425, reason: relevance_0.043_below_0.35)
  - [academic] "International Journal of Design" (relevance: 0.0106, reason: relevance_0.011_below_0.35)
  - [academic] "Long-Term Care Workforce in Croatia: A Qualitative Study on the Potential Role of Immigration" (relevance: 0.3278, reason: relevance_0.328_below_0.35)
  - [knowledge_graph] "Immigration" (relevance: 0.2828, reason: relevance_0.283_below_0.35)
  - [knowledge_graph] "Good" (relevance: 0.1519, reason: relevance_0.152_below_0.35)
  - [knowledge_graph] "Goodreads" (relevance: 0.0144, reason: relevance_0.014_below_0.35)
  - [knowledge_graph] "goods" (relevance: 0.1454, reason: relevance_0.145_below_0.35)
  - [knowledge_graph] "economy" (relevance: 0.3274, reason: relevance_0.327_below_0.35)
  - [knowledge_graph] "Economy" (relevance: 0.1666, reason: relevance_0.167_below_0.35)
  - [knowledge_graph] "Economy" (relevance: 0.2794, reason: relevance_0.279_below_0.35)

### Dedup: 25 -> 24 (dropped 1)

### Analyzed sources (24 total)

**[google_factcheck] "What does immigration do to wages? – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is little evidence that falling wages are being caused by migration, aside from in construction...."

**[google_factcheck] "Analysis | President Trump's claim that low-skilled immigration ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "“For decades, the United States was operated and has operated a very low-skill immigration system. … This policy has placed substantial pressure on Am..."

**[google_factcheck] "Do immigrants cost U.S. taxpayers $300 billion annually?"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ""Current immigration policy imposes as much as $300 billion annually in net fiscal costs on U.S. taxpayers."..."

**[wikipedia] "Economic impact of immigration to Canada"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.7485)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The economic impact of immigration to Canada is dominated by two conflicting narratives: higher immigration levels increase GDP but decrease GDP per c..."

**[wikipedia] "Immigration to China"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Immigration to the People's Republic of China (PRC) is the international movement of non-Chinese nationals in order to reside permanently in the count..."

**[wikipedia] "List of immigration enforcement operations in the second Trump presidency"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "During Donald Trump's second presidency, United States immigration officials have engaged in mass deportation operations across the country. These ope..."

**[wikipedia] "History of immigration to the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Throughout United States history, the country experienced successive waves of immigration, particularly from Europe and later on from Asia and from La..."

**[wikipedia] "Opposition to immigration"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Opposition to immigration is a political position that seeks to restrict or ban legal and illegal immigration. In the modern sense, immigration refers..."

**[wikipedia] "Immigration to the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Immigration has been a major source of population growth and cultural change in the United States throughout much of its history. As of January 2025, ..."

**[open_alex] "Is tightening immigration policy good for workers in the receiving economy?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9546)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Is tightening immigration policy good for workers in the receiving economy?..."

**[open_alex] "U.S. Residents’ Current Attitudes toward Immigrants and Immigration"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.8555)
  Verdict contribution: supporting (weight: 0.4705)
  Snippet: "Abstract Immigration is a fiery topic in U.S. society, as it generally brings to a boil native-born citizens’ disparate attitudes toward immigrants an..."

**[open_alex] "Anti-immigrant Attitudes in the European Union: What Role for Values?"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This paper aims to analyse the connection between values individuals hold and perception whether immigration is bad or good for economy in the Europea..."

**[duckduckgo] "Explainer: Immigrants and the U.S. Economy | migrationpolicy.org"**
  Type: web | Cred: verified 0.85 | Factual: high
  NLI (nli_deberta): supporting (0.9893)
  Verdict contribution: supporting (weight: 0.8409)
  Snippet: "Immigrants boost overall economic growth by expanding the labor force and increasing consumer spending.The foreign born also start new businesses at h..."

**[duckduckgo] "Benefits of Immigration Outweigh the Costs"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.9878)
  Verdict contribution: supporting (weight: 0.3981)
  Snippet: "Immigration fuels the economy. When immigrants enter the labor force, they increase the productive capacity of the economy and raise GDP...."

**[duckduckgo] "The Effects of Immigration on the United States' Economy"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.9829)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jan 11, 2024 ... However, although immigrants increase the supply of labor, they also spend their wages on homes, food, TVs and other goods and servic..."

**[duckduckgo] "Does immigration boost the economy? : r/AskEconomics - Reddit"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): supporting (0.9634)
  Verdict contribution: supporting (weight: 0.5742)
  Snippet: "Nov 1, 2024 ... Economists generally agree that immigration has a net positive effect on the U.S. economy. 35. 9 ......"

**[duckduckgo] "The Importance of Immigrant Labor to the US Economy"**
  Type: web | Cred: estimated 0.41500000000000004
  NLI (nli_deberta): supporting (0.9385)
  Verdict contribution: supporting (weight: 0.3895)
  Snippet: "Sep 2, 2024 ... In an economic sense, immigrants and their labor contribute to the growth of the overall economy. The Congressional Budget Office rece..."

**[duckduckgo] "How Does Immigration Affect the U.S. Economy?"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): supporting (0.7803)
  Verdict contribution: supporting (weight: 0.6633)
  Snippet: "Dec 4, 2025 ... Most economists say that immigration is good for the U.S. economy because it helps grow the size of the labor force, boost tax revenue..."

**[duckduckgo] "Unlocking America's Potential: How Immigration Fuels Economic ..."**
  Type: web | Cred: verified 0.85 | Factual: high
  NLI (nli_deberta): neutral (0.7139)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sep 13, 2023 ... Immigrants increase the supply of labor, which increases the supply of goods and services that people need; their consumption, entrep..."

**[duckduckgo] "MIGRATION: The Economic Benefits of Immigration"**
  Type: web | Cred: estimated 0.31
  NLI (nli_deberta): supporting (0.9243)
  Verdict contribution: supporting (weight: 0.2865)
  Snippet: "Immigrants' willingness to move helps slow wage decline in stagnant regions and contributes to economic growth in booming ones. Combined with the ......"

**[duckduckgo] "Do Immigrants and Immigration Help the Economy?"**
  Type: web | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.8784)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Apr 12, 2024 ... And the education and skill level of migrants matters, too: more education equals a more positive economic effect. “The headline find..."

**[duckduckgo] "Immigration Facts: The Positive Economic Impact of ... - FWD.us"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): neutral (0.9517)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "All of this increases employment opportunities for native-born American workers, boosts wages and strengthens the middle class. As the U.S. economy be..."

**[wikidata] "immigration"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "movement of people into another country or region to which they are not native | instance of: activity..."

**[wikidata] "immigration to the United States"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "overview of immigration to the United States | country: United States..."

### Verdict computation
  Supporting weight: 3.623
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 17

  Top supporting:
    - Explainer: Immigrants and the U.S. Economy | migrationpolicy.org (weight: 0.8409)
    - How Does Immigration Affect the U.S. Economy? (weight: 0.6633)
    - Does immigration boost the economy? : r/AskEconomics - Reddit (weight: 0.5742)
    - U.S. Residents’ Current Attitudes toward Immigrants and Immigration (weight: 0.4705)
    - Benefits of Immigration Outweigh the Costs (weight: 0.3981)

---
## 26. "the Great Wall of China is visible from space"
Category: factual_false
Expected: strongly opposed
Actual: contested (**NO - MISMATCH**)
Claim type: factual (0.9979)

### Sources collected: 40 total
  - google_factcheck: 1
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 40 -> 21 (dropped 19)
Dropped sources:
  - [encyclopedia] "Factoid" (relevance: -0.0568, reason: relevance_-0.057_below_0.35)
  - [encyclopedia] "Queen Elizabeth II Great Court" (relevance: 0.2291, reason: relevance_0.229_below_0.35)
  - [encyclopedia] "Plan 9 from Outer Space" (relevance: 0.1276, reason: relevance_0.128_below_0.35)
  - [encyclopedia] "2026 in spaceflight" (relevance: 0.1878, reason: relevance_0.188_below_0.35)
  - [academic] "4 Research Methods: Quantitative and Qualitative Approaches" (relevance: -0.004, reason: relevance_-0.004_below_0.35)
  - [academic] "On the Road to 6G: Visions, Requirements, Key Technologies, and Testbeds" (relevance: 0.0826, reason: relevance_0.083_below_0.35)
  - [academic] "The Road Towards 6G: A Comprehensive Survey" (relevance: 0.0476, reason: relevance_0.048_below_0.35)
  - [academic] "Developing fibrillated cellulose as a sustainable technological material" (relevance: 0.0672, reason: relevance_0.067_below_0.35)
  - [academic] "GLC_FCS30: global land-cover product with fine classification system at 30 m using time-series Landsat imagery" (relevance: 0.1335, reason: relevance_0.133_below_0.35)
  - [academic] "Integrated photonics on thin-film lithium niobate" (relevance: -0.0061, reason: relevance_-0.006_below_0.35)
  - [academic] "Augmented reality and virtual reality displays: emerging technologies and future perspectives" (relevance: 0.1496, reason: relevance_0.150_below_0.35)
  - [academic] "Abiotic Stress and Reactive Oxygen Species: Generation, Signaling, and Defense Mechanisms" (relevance: -0.0491, reason: relevance_-0.049_below_0.35)
  - [knowledge_graph] "galaxy filament" (relevance: 0.2661, reason: relevance_0.266_below_0.35)
  - [knowledge_graph] "People's Republic of China" (relevance: 0.2591, reason: relevance_0.259_below_0.35)
  - [knowledge_graph] "Taiwan" (relevance: 0.1782, reason: relevance_0.178_below_0.35)
  - [knowledge_graph] "China" (relevance: 0.2904, reason: relevance_0.290_below_0.35)
  - [knowledge_graph] "visible spectrum" (relevance: 0.2301, reason: relevance_0.230_below_0.35)
  - [knowledge_graph] "Visible Noise" (relevance: 0.0699, reason: relevance_0.070_below_0.35)
  - [knowledge_graph] "Visible" (relevance: 0.1878, reason: relevance_0.188_below_0.35)

### Dedup: 21 -> 19 (dropped 2)

### Analyzed sources (19 total)

**[google_factcheck] "Is the Great Wall of China Visible from the Moon?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "The Great Wall of China is the only man-made object visible from the moon...."

**[wikipedia] "Artificial structures visible from space"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9907)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial structures visible from space without magnification include highways, dams, and cities. 
Whether an object is visible depends significantly..."

**[wikipedia] "Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Great Wall of China (traditional Chinese: 萬里長城; simplified Chinese: 万里长城; pinyin: Wànlǐ Chángchéng, literally "ten thousand li long wall") is a se..."

**[wikipedia] "History of the Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The history of the Great Wall of China began when fortifications built by various states during the Spring and Autumn (771–476 BC) and Warring States ..."

**[wikipedia] "Ming Great Wall"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Ming Great Wall (Chinese: 明長城; pinyin: Míng Chángchéng), built by the Ming dynasty (1368–1644), forms the most visible parts of the Great Wall of ..."

**[wikipedia] "Mexico–United States border wall"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A border wall has been built along portions of the Mexico–United States border in an attempt to reduce illegal immigration to the United States from M..."

**[wikipedia] "Defensive wall"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A defensive wall is a fortification usually used to protect a city, town or other settlement from potential aggressors. The walls can range from simpl..."

**[open_alex] "Claim Verification: "The Great Wall of China is the only man-made object visible from space with the naked eye." — Disproved"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9844)
  Verdict contribution: opposing (weight: 0.3938)
  Snippet: "Automated fact-verification of the claim: "The Great Wall of China is the only man-made object visible from space with the naked eye." Verdict: DISPRO..."

**[open_alex] "Claim Verification: "The Great Wall of China is the only man-made object visible from space with the naked eye." — Disproved"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9844)
  Verdict contribution: opposing (weight: 0.3938)
  Snippet: "Automated fact-verification of the claim: "The Great Wall of China is the only man-made object visible from space with the naked eye." Verdict: DISPRO..."

**[duckduckgo] "Great Wall - NASA"**
  Type: web | Cred: verified 0.95 | Factual: very high
  NLI (nli_deberta): opposing (0.9609)
  Verdict contribution: opposing (weight: 0.9129)
  Snippet: "The Great Wall of China and Inner Mongolia are featured in this image photographed by Expedition 10 Commander Leroy Chiao on the International Space S..."

**[duckduckgo] "Is China's Great Wall Visible from Space? | Scientific American"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9922)
  Verdict contribution: supporting (weight: 0.8434)
  Snippet: "Choose a legend: The Great Wall of China is the one of the few man-made structures visible from orbit.Although the Great Wall spans some 4,500 miles (..."

**[duckduckgo] "Can you see the Great Wall of China from space? - BBC Sky at Night Magazine"**
  Type: web | Cred: estimated 0.282
  NLI (nli_deberta): supporting (0.7026)
  Verdict contribution: supporting (weight: 0.1981)
  Snippet: "One of the biggest is the idea that the Great Wall of China is the only human-made structure that can be seen from space. Is this true?..."

**[duckduckgo] "Forget the Great Wall: the human landmark astronauts actually ... - Futura"**
  Type: web | Cred: estimated 0.281
  NLI (nli_deberta): neutral (0.854)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Great Wall myth: a 300-year-old guess The idea that the Great Wall of China is visible from the Moon didn't start with the space age; it likely tr..."

**[duckduckgo] "NASA Just Confirmed That The Largest Structure Visible From Space Isn't ..."**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9614)
  Verdict contribution: supporting (weight: 0.8172)
  Snippet: "For many years, experts believed that the magnificent Great Wall of China in Asia was the largest visible structure from space, whose oldest section w..."

**[duckduckgo] "Can you see the Great Wall of China from space? | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): supporting (0.4966)
  Verdict contribution: supporting (weight: 0.4221)
  Snippet: "You typically can't see the Great Wall of China from space. A popular myth, the claim was disproved when astronauts stated that the Great Wall of Chin..."

**[duckduckgo] "Can the Great Wall Be Seen from the Space? - TravelChinaGuide"**
  Type: web | Cred: estimated 0.29
  NLI (nli_deberta): opposing (0.9692)
  Verdict contribution: opposing (weight: 0.2811)
  Snippet: "Is the Great Wall truly visible from the moon? It is generally accepted that the Great Wall cannot be seen from the space which is proved from both th..."

**[duckduckgo] "Is the Great Wall of China really visible from space?"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9487)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Is the Great Wall of China really visible from space? Contrary to popular belief, the Great Wall of China is a thin structure that blends in well with..."

**[wikidata] "Great Wall Motor"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Chinese vehicle manufacturing company | instance of: automobile manufacturer | country: People's Republic of China | inception: 1984-00-00 | headquart..."

**[wikidata] "Great Wall of China"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "series of fortifications built along the historical border of China | instance of: tourist attraction | country: People's Republic of China | located ..."

### Verdict computation
  Supporting weight: 2.2808
  Opposing weight: 2.4564
  Support ratio: 0.4815
  Confidence: 0.0371
  Verdict: **contested**
  Neutral sources (no contribution): 10

  Top supporting:
    - Is China's Great Wall Visible from Space? | Scientific American (weight: 0.8434)
    - NASA Just Confirmed That The Largest Structure Visible From Space Isn't ... (weight: 0.8172)
    - Can you see the Great Wall of China from space? | Britannica (weight: 0.4221)
    - Can you see the Great Wall of China from space? - BBC Sky at Night Magazine (weight: 0.1981)
  Top opposing:
    - Great Wall - NASA (weight: 0.9129)
    - Is the Great Wall of China Visible from the Moon? (weight: 0.475)
    - Claim Verification: "The Great Wall of China is the only man-made object visible from space with the naked eye." — Disproved (weight: 0.3938)
    - Claim Verification: "The Great Wall of China is the only man-made object visible from space with the naked eye." — Disproved (weight: 0.3938)
    - Can the Great Wall Be Seen from the Space? - TravelChinaGuide (weight: 0.2811)

---
## 27. "cats are better pets than dogs"
Category: opinion
Expected: opinion
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.9922)

### Sources collected: 46 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 46 -> 28 (dropped 18)
Dropped sources:
  - [encyclopedia] "Dog" (relevance: 0.3384, reason: relevance_0.338_below_0.35)
  - [encyclopedia] "Springfield pet-eating hoax" (relevance: 0.2647, reason: relevance_0.265_below_0.35)
  - [encyclopedia] "The Sims 2: Pets" (relevance: 0.3015, reason: relevance_0.302_below_0.35)
  - [academic] "Nutrition and aging in dogs and cats: assessment and dietary strategies" (relevance: 0.2693, reason: relevance_0.269_below_0.35)
  - [academic] "Molecular detection and characterization of SARS-CoV-2 in cats and dogs of positive owners during the first COVID-19 wave in Brazil" (relevance: 0.3437, reason: relevance_0.344_below_0.35)
  - [academic] "How Italian practitioners manage dirofilariosis in dogs and cats? Data of a second national survey." (relevance: 0.3215, reason: relevance_0.322_below_0.35)
  - [academic] "A one-year extensive molecular survey on SARS-CoV-2 in companion animals of Turkey shows a lack of evidence for viral circulation in pet dogs and cats" (relevance: 0.337, reason: relevance_0.337_below_0.35)
  - [academic] "<scp>WSAVA</scp>guidelines for the control of reproduction in dogs and cats" (relevance: 0.3334, reason: relevance_0.333_below_0.35)
  - [academic] "<i>Dermacentor variabilis</i> is the Predominant <i>Dermacentor</i> spp. (Acari: Ixodidae) Feeding on Dogs and Cats Throughout the United States" (relevance: 0.2243, reason: relevance_0.224_below_0.35)
  - [academic] "Pet cats, the better sentinels for indoor organic pollutants" (relevance: 0.2975, reason: relevance_0.297_below_0.35)
  - [academic] "Dog Nose-Print Identification Using Deep Neural Networks" (relevance: 0.2706, reason: relevance_0.271_below_0.35)
  - [academic] "Awareness of parasitic zoonotic diseases among pet owners in Cairo, Egypt" (relevance: 0.3182, reason: relevance_0.318_below_0.35)
  - [academic] "Effects of extruded pet foods containing dried yeast (<i>Saccharomyces cerevisiae</i>) on palatability, nutrient digestibility, and fecal quality in dogs and cats" (relevance: 0.3194, reason: relevance_0.319_below_0.35)
  - [academic] "Establishment of a direct 2.5D organoid culture model using companion animal cancer tissues" (relevance: 0.2497, reason: relevance_0.250_below_0.35)
  - [knowledge_graph] "Cats" (relevance: 0.3328, reason: relevance_0.333_below_0.35)
  - [knowledge_graph] "dog" (relevance: 0.3317, reason: relevance_0.332_below_0.35)
  - [knowledge_graph] "Dogs" (relevance: 0.2481, reason: relevance_0.248_below_0.35)
  - [knowledge_graph] "sled dog racing" (relevance: 0.2422, reason: relevance_0.242_below_0.35)

### Dedup: 28 -> 28 (dropped 0)

### Analyzed sources (28 total)

**[wikipedia] "Pet"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A pet, or companion animal, is an animal kept primarily for a person's company or entertainment rather than as a working animal, livestock, or a labor..."

**[wikipedia] "Overpopulation of domestic pets"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In some countries, there is an overpopulation of pets such as cats, dogs, and exotic animals. In the United States, six to eight million animals are b..."

**[wikipedia] "Human interaction with cats"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Human interaction with cats relates to the hundreds of millions of cats that are kept as pets around the world. Cats were originally domesticated thou..."

**[wikipedia] "Cat"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The cat (Felis catus), also called domestic cat and house cat, is a small domesticated carnivorous mammal. It is an obligate carnivore, requiring a pr..."

**[wikipedia] "Cat food"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cat food is food specifically formulated for consumption by cats. In the 19th and early 20th centuries, cats in London were commonly fed horse meat so..."

**[wikipedia] "Pet food"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Pet food is animal feed intended for consumption by pets. Typically sold in pet stores and supermarkets, it is usually specific to the type of animal,..."

**[wikipedia] "United States presidential pets"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Most United States presidents have kept pets while in office, or pets have been part of their families. Only James K. Polk, Andrew Johnson, and Donald..."

**[semantic_scholar] "PETS AS THERAPY: THE ROLE OF CATS AND DOGS IN REDUCING STRESS AND BLOOD PRESSURE"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Pet ownership, particularly of cats and dogs, has been increasingly recognized as contributing to human health and well-being. Globally, cardiovascula..."

**[semantic_scholar] "An exploratory mixed methods study on shared decision-making and antibiotic prescribing for pet cats and dogs in Singapore veterinary clinics"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Veterinarians primarily engage pet owners in shared decision-making (SDM) to enhance treatment outcomes and owner satisfaction, but not specifically f..."

**[semantic_scholar] "Grain-Free Diets for Dogs and Cats: An Updated Review Focusing on Nutritional Effects and Health Considerations"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Simple Summary Currently, there is a significant amount of controversy surrounding the advantages and disadvantages of feeding pets grain-free foods. ..."

**[semantic_scholar] "Owner survey suggests cats may be undertreated for pain compared to dogs after an elective ovariohysterectomy or orchiectomy."**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "OBJECTIVE
To investigate differences in pain management between dogs and cats after surgical sterilization. We hypothesized that dogs would be more li..."

**[semantic_scholar] "Cats and dogs: The role of owner attachment and local cultural values in animal welfare"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This study aims to analyze the relationship between pet owner attachment and the welfare of pets (cats and dogs) through the lens of local cultural va..."

**[semantic_scholar] "Comparing Pears to Apples: Unlike Dogs, Cats Need Habituation before Lab Tests"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Simple Summary Comparative studies can help us better understand our family pets’ social and cognitive behaviours and gain more insights in the evolut..."

**[open_alex] "Pet–Human Relationships: Dogs versus Cats"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.7334)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The study of human-animal interactions has increased, focusing on the dog-owner relationship, leaving a lag in research on the cat-owner relationship ..."

**[open_alex] "Monitoring of Diabetes Mellitus Using the Flash Glucose Monitoring System: The Owners’ Point of View"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The flash glucose monitoring system (FGMS) has recently become one of the most common monitoring methods in dogs and cats with diabetes mellitus. The ..."

**[open_alex] "Adaptation and psychometric properties of Lexington Attachment to Pets Scale: Brazilian version (LAPS-B)"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Adaptation and psychometric properties of Lexington Attachment to Pets Scale: Brazilian version (LAPS-B)..."

**[duckduckgo] "32 reasons why cats are better pets than dogs | PetsRadar"**
  Type: web | Cred: estimated 0.23199999999999998
  NLI (nli_deberta): supporting (0.9717)
  Verdict contribution: supporting (weight: 0.2254)
  Snippet: "So, as you can see there are lots of perks to having a pussycat as a pet. And we’re only just getting started. To discover why cats are better pets th..."

**[duckduckgo] "Interesting Reasons why cats are better than dogs"**
  Type: web | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9707)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cats appear to be better companions than dogs for a variety of reasons, according to cat lovers. Here are some reasons why cats make better pets than ..."

**[duckduckgo] "5 Reasons Cats Make Better Pets Than Dogs - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube...."

**[duckduckgo] "Why Cats make better pets than Dogs for people living in... | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9609)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cats make great pets and are ideal companions for people who work full time or who live in an apartment. They are less expensive to keep and require l..."

**[duckduckgo] "24 Reasons Cats Are Better Than Dogs (From a Dog...) - A-Z Animals"**
  Type: web | Cred: estimated 0.441
  NLI (nli_deberta): neutral (0.9937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cats eat less than dogs, so they leave a smaller carbon footprint. Meat, which is the primary source of food for both species, isn’t great for the pla..."

**[duckduckgo] "Why Are Cats Better Pets Than Dogs? 11 Reasons – Cat Cave Co"**
  Type: web | Cred: estimated 0.281
  NLI (nli_deberta): supporting (0.9683)
  Verdict contribution: supporting (weight: 0.2721)
  Snippet: "I know that dog parents will be unsatisfied with this article, but I have numerous proofs why cats are better pets than dogs. Yes, dogs are more dedic..."

**[duckduckgo] "Top 10 Reasons Why Cats Are Better Than Dogs | Coops And Cages"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cats make great pets for all kinds of reasons, from their independent spirits to their playful demeanor. Here are the top ten reasons why cats are the..."

**[duckduckgo] "Here are three reasons why cats make better pets than dogs"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9941)
  Verdict contribution: supporting (weight: 0.1988)
  Snippet: "One reason why cats are better pets to have in the house is because they are cleaner. Dogs spend a lot of time outside and tend to bring the outside i..."

**[duckduckgo] "15 Reasons Why Cats Are Better Than Dogs"**
  Type: web | Cred: estimated 0.21000000000000002
  NLI (nli_deberta): supporting (0.5864)
  Verdict contribution: supporting (weight: 0.1231)
  Snippet: "Both cats and dogs have their advantages and we do not discriminate depending on the choice of your pet. However, we do love cats a bit more than dogs..."

**[duckduckgo] "13 Reasons Cats Will Always Be Better Pets Than Dogs"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.981)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sure, dogs are cool. They are man's best friend. But have you ever come home from a long day of work, thrown on your pajamas, laid on the couch with y..."

**[wikidata] "Cats"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "2019 film directed by Tom Hooper | instance of: film..."

**[wikidata] "Cats"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "family name | instance of: family name..."

### Verdict computation
  Supporting weight: 0.8195
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 24

  Top supporting:
    - Why Are Cats Better Pets Than Dogs? 11 Reasons – Cat Cave Co (weight: 0.2721)
    - 32 reasons why cats are better pets than dogs | PetsRadar (weight: 0.2254)
    - Here are three reasons why cats make better pets than dogs (weight: 0.1988)
    - 15 Reasons Why Cats Are Better Than Dogs (weight: 0.1231)

---
## 28. "organic food is healthier than conventional food"
Category: contested
Expected: contested
Actual: likely supported (YES)
Claim type: factual (0.9564)

### Sources collected: 48 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 8

### Relevance filter: 48 -> 40 (dropped 8)
Dropped sources:
  - [encyclopedia] "Food system" (relevance: 0.2641, reason: relevance_0.264_below_0.35)
  - [encyclopedia] "Cat food" (relevance: 0.2142, reason: relevance_0.214_below_0.35)
  - [encyclopedia] "Ultra-processed food" (relevance: 0.2943, reason: relevance_0.294_below_0.35)
  - [academic] "Determination of Regulated and Emerging Mycotoxins in Organic and Conventional Gluten-Free Flours by LC-MS/MS" (relevance: 0.2547, reason: relevance_0.255_below_0.35)
  - [academic] "Diet and food type affect urinary pesticide residue excretion profiles in healthy individuals: results of a randomized controlled dietary intervention trial" (relevance: 0.3417, reason: relevance_0.342_below_0.35)
  - [knowledge_graph] "Healthier Lives" (relevance: 0.184, reason: relevance_0.184_below_0.35)
  - [knowledge_graph] "Healthier lunchboxes : ideas for primary schools" (relevance: 0.2474, reason: relevance_0.247_below_0.35)
  - [knowledge_graph] "Healthier Hearts Foundation" (relevance: 0.2178, reason: relevance_0.218_below_0.35)

### Dedup: 40 -> 40 (dropped 0)

### Analyzed sources (40 total)

**[wikipedia] "Organic food"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic food, also known as ecological or biological food, refers to foods and beverages produced using methods that comply with the standards of orga..."

**[wikipedia] "Organic farming"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic farming, also known as organic agriculture or ecological farming, or biological farming, is an agricultural system that emphasizes the use of ..."

**[wikipedia] "Genetically modified food controversies"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Consumers, farmers, biotechnology companies, governmental regulators, non-governmental organizations, and scientists have been involved in controversi..."

**[wikipedia] "Health food store"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9268)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A health food store (or health food shop) is a type of grocery store that primarily sells healthful foods, organic foods, local produce, and often nut..."

**[wikipedia] "Organic certification"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic certification is a certification process for producers of organic food and other organic agricultural products. In general, any business direc..."

**[wikipedia] "Eggs as food"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Humans and other hominids have consumed eggs for millions of years. The most widely consumed eggs are those of fowl, especially chickens. People in So..."

**[wikipedia] "Human food"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Human food is food which is fit for human consumption, and which humans willingly eat. Food is a basic necessity of life, and humans typically seek fo..."

**[semantic_scholar] "Studies on Impact and Opinion of Organic Food Products of Human Life during Covid-19"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.9976)
  Verdict contribution: supporting (weight: 0.5487)
  Snippet: "Organic food has become useful nowadays and every person know the benefits and effect of the organic products. Organic food products Opinion of consum..."

**[semantic_scholar] "Consumer Attitudes and Determinants of Organic Food Purchasing Behavior: Evidence from Andhra Pradesh, India"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.7739)
  Verdict contribution: supporting (weight: 0.3096)
  Snippet: "The increasing awareness of the health and environmental benefits of organic food products has led to a growing demand for these products worldwide. T..."

**[semantic_scholar] "The production and processing of organic food"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.9961)
  Verdict contribution: supporting (weight: 0.3984)
  Snippet: "Food is not only failing to fulfill its purpose of nourishing and, therefore, of generating health, but also, from more and more broad scientific sect..."

**[semantic_scholar] "Fruit quality in organic and conventional farming: advantages and limitations."**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.5908)
  Verdict contribution: opposing (weight: 0.384)
  Snippet: "Fruit quality is essential for nutrition and human health and needs urgent attention in current agricultural practices. Organic farming is not as prod..."

**[semantic_scholar] "Organic food labels bias food healthiness perceptions: Estimating healthiness equivalence using a Discrete Choice Experiment."**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9199)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Individuals perceive organic food as being healthier and containing fewer calories than conventional foods. We provide an alternative way to investiga..."

**[semantic_scholar] "Comparison of Wheat Quality, Antioxidant Activity, and Mycotoxins Under Organic and Conventional Farming"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9365)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Wheat (Triticum aestivum L.) is a major global staple crop, widely consumed in processed forms such as bread and pasta. As consumer demand for healthi..."

**[semantic_scholar] "Potential Health Benefits of a Diet Rich in Organic Fruit and Vegetables versus a Diet Based on Conventional Produce: A Systematic Review"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9717)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract Context Over the past decade, the production and consumption of organic food (OF) have received increasing interest. Scientific studies have ..."

**[semantic_scholar] "Key Findings of the French BioNutriNet Project on Organic Food-Based Diets: Description, Determinants, and Relationships to Health and the Environment."**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.6465)
  Snippet: "Few studies have investigated the relationships between organic food consumption, dietary patterns, monetary diet cost, health, and the environment. T..."

**[semantic_scholar] "EFFECTS OF ORGANIC FOOD PERCEIVED VALUES ON CONSUMERS’ ATTITUDE AND BEHAVIOR IN DEVELOPING COUNTRY: MODERATING ROLE OF PRICE SENSITIVITY"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "EFFECTS OF ORGANIC FOOD PERCEIVED VALUES ON CONSUMERS’ ATTITUDE AND BEHAVIOR IN DEVELOPING COUNTRY: MODERATING ROLE OF PRICE SENSITIVITY..."

**[open_alex] "A Review of Organic Waste Treatment Using Black Soldier Fly (Hermetia illucens)"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The increase in solid waste generation is caused primarily by the global population growth that resulted in urban sprawl, economic development, and co..."

**[open_alex] "Customer Preferences for Organic Agriculture Produce in the Czech Republic: 2016 and 2019"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.6128)
  Verdict contribution: supporting (weight: 0.3983)
  Snippet: "The article analyses the customer attitude towards the qualities and benefits of organic agriculture production for farmers and customers in the Czech..."

**[open_alex] "Organic food labels bias food healthiness perceptions: Estimating healthiness equivalence using a Discrete Choice Experiment"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9546)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic food labels bias food healthiness perceptions: Estimating healthiness equivalence using a Discrete Choice Experiment..."

**[open_alex] "Europe’s Farm to Fork Strategy and Its Commitment to Biotechnology and Organic Farming: Conflicting or Complementary Goals?"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sustainable food systems will require profound changes in people’s consumption patterns and lifestyles, which is true regardless of the farming method..."

**[open_alex] "Key Findings of the French BioNutriNet Project on Organic Food–Based Diets: Description, Determinants, and Relationships to Health and the Environment"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Key Findings of the French BioNutriNet Project on Organic Food–Based Diets: Description, Determinants, and Relationships to Health and the Environment..."

**[open_alex] "Lipid characteristics, bioactive properties, and mineral content in hazelnut grown under different cultivation systems"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.8413)
  Verdict contribution: supporting (weight: 0.5468)
  Snippet: "The demand for organic food is increasing due to the view among consumers that organic food is healthier and more nutritious. However, very limited da..."

**[open_alex] "How Do Italian Consumers Value Sustainable Certifications on Fish?—An Explorative Analysis"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9717)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sustainable certifications communicate the environmental benefits of food products to consumers, and allow producers to differentiate their products f..."

**[open_alex] "Fruit quality in organic and conventional farming: advantages and limitations"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Fruit quality in organic and conventional farming: advantages and limitations..."

**[open_alex] "Differences in Processing Quality Traits, Protein Content and Composition between Spelt and Bread Wheat Genotypes Grown under Conventional and Organic Production"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.981)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The unique rheological properties of bread wheat dough and the breadmaking quality of its flour are the main factors responsible for the global distri..."

**[duckduckgo] "Organic foods: Are they safer? More nutritious? - Mayo Clinic"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9463)
  Verdict contribution: supporting (weight: 0.8044)
  Snippet: "People who buy organic food also ... healthier diet pattern than the average. These traits are linked to having a lower risk of disease and fewer dise..."

**[duckduckgo] "Organic food no more nutritious than conventionally grown food - Harvard Health"**
  Type: web | Cred: estimated 0.329
  NLI (nli_deberta): supporting (0.9663)
  Verdict contribution: supporting (weight: 0.3179)
  Snippet: "September 5, 2012 - They're healthier. A few studies have suggested organic foods might be higher in nutrients than their traditional counterparts...."

**[duckduckgo] "Are organic foods really healthier? Two pediatricians break it down | Good Food Is Good Medicine | UC Davis Health"**
  Type: web | Cred: estimated 0.465
  NLI (nli_deberta): opposing (0.9902)
  Verdict contribution: opposing (weight: 0.4604)
  Snippet: "April 5, 2019 - Organic foods are not healthier, per se, in terms of nutrients. You are still getting the same benefits in conventionally grown foods ..."

**[duckduckgo] "A Systematic Review of Organic Versus Conventional Food Consumption: Is There a Measurable Benefit on Human Health? - PMC"**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): neutral (0.5664)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic foods have been shown to have lower levels of toxic metabolites, including heavy metals such as cadmium, and synthetic fertilizer and pesticid..."

**[duckduckgo] "Is Organic Food Healthier Than Non-Organic Food? | Bayer Canada | Bayer Canada"**
  Type: web | Cred: estimated 0.413
  NLI (nli_deberta): opposing (0.9766)
  Verdict contribution: opposing (weight: 0.4033)
  Snippet: "There’s no evidence showing that organic produce is safer or more nutritious than non-organic produce. Several studies have revealed that there is no ..."

**[duckduckgo] "Is Organic Food Really Better for You?"**
  Type: web | Cred: estimated 0.267
  NLI (nli_deberta): opposing (0.9507)
  Verdict contribution: opposing (weight: 0.2538)
  Snippet: "And while organic foods have a reputation for being healthy and nutritious, studies show that there is actually very little difference in nutritional ..."

**[duckduckgo] "Is Organic Food Healthier Than Conventional? — Your Latina Nutrition"**
  Type: web | Cred: estimated 0.296
  NLI (nli_deberta): opposing (0.9028)
  Verdict contribution: opposing (weight: 0.2672)
  Snippet: "January 16, 2026 - Overall, there is no conclusive evidence that organic food is healthier than conventional food...."

**[duckduckgo] "Are organic foods healthier than conventional foods? - Genetic Literacy Project"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.9946)
  Verdict contribution: opposing (weight: 0.8454)
  Snippet: "March 14, 2022 - There are unique benefits and challenges associated with all approaches to agriculture. As a result, the scientific consensus remains..."

**[duckduckgo] "Are organics more nutritious than conventional foods? A comprehensive systematic review - ScienceDirect"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.7173)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "March 21, 2024 - Therefore, the results herein show no generalizable superiority of organic over conventional foods. Claims for nutritious advantages ..."

**[duckduckgo] "Is Organic Food Better? - US News Health"**
  Type: web | Cred: estimated 0.477
  NLI (nli_deberta): neutral (0.9731)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "August 6, 2024 - Some studies have compared organic vs. conventional produce and have found little nutritional differences, beyond potentially higher ..."

**[wikidata] "organic food"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "foods produced without synthetic pesticides and chemical fertilizers | instance of: protected term..."

**[wikidata] "Organic Food"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "episode of Penn & Teller: Bullshit! (S7 E6) | instance of: television series episode..."

**[wikidata] "organic food processing"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "processing without artificial ingredients or synthetic preservatives to maintain the integrity of the product that began with organic practices on the..."

**[wikidata] "Conventional foods, followed by dietary supplements and fortified foods, are the key sources of vitamin D, vitamin B6, and selenium intake in Dutch participants of the NU-AGE study"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scientific article published on 27 May 2016 | instance of: scholarly article..."

**[wikidata] "Conventional Food Plot Management in an Organic Coffee Cooperative: Explaining the Paradox"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scholarly article published 9 August 2013 | instance of: scholarly article..."

### Verdict computation
  Supporting weight: 3.9706
  Opposing weight: 2.6143
  Support ratio: 0.603
  Confidence: 0.206
  Verdict: **likely supported**
  Neutral sources (no contribution): 26

  Top supporting:
    - Organic foods: Are they safer? More nutritious? - Mayo Clinic (weight: 0.8044)
    - Key Findings of the French BioNutriNet Project on Organic Food-Based Diets: Description, Determinants, and Relationships to Health and the Environment. (weight: 0.6465)
    - Studies on Impact and Opinion of Organic Food Products of Human Life during Covid-19 (weight: 0.5487)
    - Lipid characteristics, bioactive properties, and mineral content in hazelnut grown under different cultivation systems (weight: 0.5468)
    - The production and processing of organic food (weight: 0.3984)
  Top opposing:
    - Are organic foods healthier than conventional foods? - Genetic Literacy Project (weight: 0.8454)
    - Are organic foods really healthier? Two pediatricians break it down | Good Food Is Good Medicine | UC Davis Health (weight: 0.4604)
    - Is Organic Food Healthier Than Non-Organic Food? | Bayer Canada | Bayer Canada (weight: 0.4033)
    - Fruit quality in organic and conventional farming: advantages and limitations. (weight: 0.384)
    - Is Organic Food Healthier Than Conventional? — Your Latina Nutrition (weight: 0.2672)

---
## 29. "MSG is dangerous to consume"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.9969)

### Sources collected: 42 total
  - google_factcheck: 3
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 42 -> 15 (dropped 27)
Dropped sources:
  - [encyclopedia] "Controversies of Nestlé" (relevance: 0.2289, reason: relevance_0.229_below_0.35)
  - [encyclopedia] "Text messaging" (relevance: 0.1232, reason: relevance_0.123_below_0.35)
  - [encyclopedia] "Anthony William" (relevance: 0.2182, reason: relevance_0.218_below_0.35)
  - [encyclopedia] "André the Giant" (relevance: -0.0137, reason: relevance_-0.014_below_0.35)
  - [encyclopedia] "Weather satellite" (relevance: -0.0425, reason: relevance_-0.043_below_0.35)
  - [encyclopedia] "Jon Jones" (relevance: 0.0544, reason: relevance_0.054_below_0.35)
  - [encyclopedia] "List of The Great North episodes" (relevance: -0.0687, reason: relevance_-0.069_below_0.35)
  - [encyclopedia] "Diego Garcia" (relevance: 0.0088, reason: relevance_0.009_below_0.35)
  - [encyclopedia] "Industrial microbiology" (relevance: 0.127, reason: relevance_0.127_below_0.35)
  - [academic] "Capabilities of GPT-4 on Medical Challenge Problems" (relevance: 0.0796, reason: relevance_0.080_below_0.35)
  - [academic] "Flood Risk Mapping by Remote Sensing Data and Random Forest Technique" (relevance: 0.0567, reason: relevance_0.057_below_0.35)
  - [academic] "Edukasi Zat Aditif Makanan Berbahaya dan Efeknya Bagi Tubuh di SMA PGRI 4 Cipayung Jakarta Timur" (relevance: 0.1831, reason: relevance_0.183_below_0.35)
  - [academic] "The cost of anti-Asian racism during the COVID-19 pandemic" (relevance: 0.0748, reason: relevance_0.075_below_0.35)
  - [academic] "Understanding the sustainability debate on forest biomass for energy in Europe: A discourse analysis" (relevance: 0.0286, reason: relevance_0.029_below_0.35)
  - [academic] "The State of Ethereum Smart Contracts Security: Vulnerabilities, Countermeasures, and Tool Support" (relevance: -0.0028, reason: relevance_-0.003_below_0.35)
  - [academic] "Waste to Sustainable Biohydrogen Production Via Photo-Fermentation and Biophotolysis − A Systematic Review" (relevance: 0.0443, reason: relevance_0.044_below_0.35)
  - [academic] "Tolerable Upper Intake Level for Individual Amino Acids in Humans: A Narrative Review of Recent Clinical Studies" (relevance: 0.206, reason: relevance_0.206_below_0.35)
  - [academic] "Astounding Health Benefits of Jamun (Syzygium cumini) toward Metabolic Syndrome" (relevance: 0.3, reason: relevance_0.300_below_0.35)
  - [academic] "Rare Earth Frontiers: From Terrestrial Subsoils to Lunar Landscapes" (relevance: 0.0148, reason: relevance_0.015_below_0.35)
  - [knowledge_graph] "Madison Square Garden" (relevance: -0.0104, reason: relevance_-0.010_below_0.35)
  - [knowledge_graph] "Mobile Suit Gundam" (relevance: -0.0466, reason: relevance_-0.047_below_0.35)
  - [knowledge_graph] "Dangerous" (relevance: 0.259, reason: relevance_0.259_below_0.35)
  - [knowledge_graph] "Dangerous" (relevance: 0.1925, reason: relevance_0.193_below_0.35)
  - [knowledge_graph] "Dangerous" (relevance: 0.2565, reason: relevance_0.257_below_0.35)
  - [knowledge_graph] "Consumer Electronics Show" (relevance: -0.0651, reason: relevance_-0.065_below_0.35)
  - [knowledge_graph] "consumer protection" (relevance: 0.0653, reason: relevance_0.065_below_0.35)
  - [knowledge_graph] "consumer electronics" (relevance: 0.0028, reason: relevance_0.003_below_0.35)

### Dedup: 15 -> 15 (dropped 0)

### Analyzed sources (15 total)

**[google_factcheck] "Fact check: MSG doesn't cause neurological disorders, is safe ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "MSG is a deadly brain toxin, causes neurological disorders and other health problems..."

**[google_factcheck] "Brain damage link to MSG a salty dose of misinformation"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "MSG kills brain cells and damages the nervous system...."

**[google_factcheck] "Viral online posts claiming MSG is unsafe for consumption omit ..."**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): opposing (0.65)
  Verdict contribution: opposing (weight: 0.5525)
  Snippet: "Philippine FDA confirms MSG food additive is 'a silent killer'..."

**[wikipedia] "Glutamate flavoring"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Glutamate flavoring is the generic name for flavor-enhancing compounds based on glutamic acid and its salts (glutamates). These compounds provide a sa..."

**[duckduckgo] "MSG is neither terribly dangerous nor perfectly fine"**
  Type: web | Cred: estimated 0.28900000000000003
  NLI (nli_deberta): opposing (0.9917)
  Verdict contribution: opposing (weight: 0.2866)
  Snippet: "MSG is neither terribly dangerous nor perfectly fine literallycaneven: This actually really bothered me that a scientific consensus can be bought by ...."

**[duckduckgo] "MSG – How Dangerous Is It? - CoreLife Healthcare"**
  Type: web | Cred: estimated 0.246
  NLI (nli_deberta): neutral (0.9434)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... MSG consumption to weight gain and obesity, but it’s unclear if such findings are a consequences of MSG consumption or that fact that the foods MS..."

**[duckduckgo] "MSG Is Perfectly Safe to Consume, but We All Spent Several"**
  Type: web | Cred: estimated 0.41100000000000003
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.41)
  Snippet: "MSG Is Perfectly Safe to Consume ... And all this despite the fact that—again— extensive studies have found MSG is perfectly safe to consume...."

**[duckduckgo] "MSG is safe in small amounts, or so you think - NaturalNews.com"**
  Type: web | Cred: verified 0.1 | Bias: far right conspiracy-pseusdoscience | Factual: very low
  NLI (nli_deberta): opposing (0.9922)
  Verdict contribution: opposing (weight: 0.0992)
  Snippet: "Conventionally considered to be safe for consumption, MSG has even been touted to be beneficial, as it can help reduce salt intake while keeping food ..."

**[duckduckgo] "(MSG), a Potentially Dangerous"**
  Type: web | Cred: estimated 0.279
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In summary, MSG’s history is deeply tied to Japan’s discovery of umami and the centuries-old use of glutamate-containing ingredients in Asian ......"

**[duckduckgo] "Fact-check: MSG is safe for human consumption - HealthLEADS"**
  Type: web | Cred: estimated 0.23399999999999999
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.2334)
  Snippet: "According to the report , MSG is categorized under the label GRAS (Generally recognized as safe) and does not pose any serious hazards to the body...."

**[duckduckgo] "Toxic at One Dose: MSG is Causing Headaches, Wrecking Your"**
  Type: web | Cred: verified 0.5 | Bias: left conspiracy-pseudoscience | Factual: mixed
  NLI (nli_deberta): supporting (0.8047)
  Verdict contribution: supporting (weight: 0.4023)
  Snippet: "Additionally, while steering clear of MSG is the best way to protect yourself from its damage, recent research indicates ginger may be able to ......"

**[duckduckgo] "Is MSG Bad For You? – Miracle Noodle"**
  Type: web | Cred: estimated 0.309
  NLI (nli_deberta): supporting (0.9746)
  Verdict contribution: supporting (weight: 0.3012)
  Snippet: "And the danger of consuming free glutamate sources like MSG is that it causes neurons to “fire wildly”, which can damage and even destroy neurons ......"

**[duckduckgo] "Is Msg Dangerous or Is It Safe? | Ideal Nutrition"**
  Type: web | Cred: estimated 0.236
  NLI (nli_deberta): neutral (0.9849)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... s acceptable daily intake (of 30mg/kg body weight/day) is deemed unattainable to reach when MSG is consumed at normal dietary levels...."

**[duckduckgo] "MSG in Food Being Dangerous, Bad for You Is a Myth - Business"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... and all came to the same conclusion: there is no scientific evidence linking MSG consumption to any of the symptoms it is popularly believed to ca..."

**[wikidata] "monosodium L-glutamate"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "chemical compound, flavor enhancer | instance of: type of chemical entity..."

### Verdict computation
  Supporting weight: 0.7035
  Opposing weight: 2.0568
  Support ratio: 0.2549
  Confidence: 0.4903
  Verdict: **likely opposed**
  Neutral sources (no contribution): 7

  Top supporting:
    - Toxic at One Dose: MSG is Causing Headaches, Wrecking Your (weight: 0.4023)
    - Is MSG Bad For You? – Miracle Noodle (weight: 0.3012)
  Top opposing:
    - Viral online posts claiming MSG is unsafe for consumption omit ... (weight: 0.5525)
    - Fact check: MSG doesn't cause neurological disorders, is safe ... (weight: 0.475)
    - MSG Is Perfectly Safe to Consume, but We All Spent Several (weight: 0.41)
    - MSG is neither terribly dangerous nor perfectly fine (weight: 0.2866)
    - Fact-check: MSG is safe for human consumption - HealthLEADS (weight: 0.2334)

---
## 30. "humans share about 98% of DNA with chimpanzees"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.9979)

### Sources collected: 39 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 39 -> 22 (dropped 17)
Dropped sources:
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: 0.0921, reason: relevance_0.092_below_0.35)
  - [academic] "The influence of evolutionary history on human health and disease" (relevance: 0.334, reason: relevance_0.334_below_0.35)
  - [academic] "Plasmodium—a brief introduction to the parasites causing human malaria and their basic biology" (relevance: 0.2066, reason: relevance_0.207_below_0.35)
  - [academic] "Perspectives in machine learning for wildlife conservation" (relevance: 0.063, reason: relevance_0.063_below_0.35)
  - [academic] "CADD v1.7: using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide variant predictions" (relevance: 0.0933, reason: relevance_0.093_below_0.35)
  - [academic] "Vaccine development for emerging infectious diseases" (relevance: 0.1244, reason: relevance_0.124_below_0.35)
  - [academic] "Evolution of the germline mutation rate across vertebrates" (relevance: 0.3126, reason: relevance_0.313_below_0.35)
  - [academic] "Therapeutic cancer vaccines: advancements, challenges and prospects" (relevance: 0.0449, reason: relevance_0.045_below_0.35)
  - [knowledge_graph] "Q136928448" (relevance: 0.1003, reason: relevance_0.100_below_0.35)
  - [knowledge_graph] "Humans Share More Preferences for Floral Phenotypes With Pollinators Than With Pests" (relevance: 0.1666, reason: relevance_0.167_below_0.35)
  - [knowledge_graph] "Humans share task load with a computer partner if (they believe that) it acts human-like" (relevance: 0.268, reason: relevance_0.268_below_0.35)
  - [knowledge_graph] "98% identical, 100% wrong: per cent nucleotide identity can lead plant virus epidemiology astray." (relevance: 0.3307, reason: relevance_0.331_below_0.35)
  - [knowledge_graph] "98% IGHV gene identity is the optimal cutoff to dichotomize the prognosis of Chinese patients with chronic lymphocytic leukemia" (relevance: 0.1954, reason: relevance_0.195_below_0.35)
  - [knowledge_graph] "98% of UK companies fail to implement security standard" (relevance: 0.1385, reason: relevance_0.139_below_0.35)
  - [knowledge_graph] "deoxyribonucleic acid" (relevance: 0.2597, reason: relevance_0.260_below_0.35)
  - [knowledge_graph] "DNA" (relevance: 0.2556, reason: relevance_0.256_below_0.35)
  - [knowledge_graph] "DNA binding" (relevance: 0.1292, reason: relevance_0.129_below_0.35)

### Dedup: 22 -> 22 (dropped 0)

### Analyzed sources (22 total)

**[wikipedia] "Human evolution"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Homo sapiens is a distinct species of the hominid family of primates, which also includes all the great apes. Over their evolutionary history, humans ..."

**[wikipedia] "Chimpanzee"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The chimpanzee (; Pan troglodytes), also simply known as the chimp, is an endangered species of great ape native to the forests and savannahs of tropi..."

**[wikipedia] "Bonobo"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The bonobo (; Pan paniscus), also historically called the pygmy chimpanzee (less often the dwarf chimpanzee or gracile chimpanzee), is an endangered g..."

**[wikipedia] "Timeline of human evolution"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The timeline of human evolution outlines the major events in the evolutionary lineage of the modern human species, Homo sapiens,
throughout the histor..."

**[wikipedia] "Human evolutionary genetics"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Human evolutionary genetics studies how one human genome differs from another human genome, the evolutionary past that gave rise to the human genome, ..."

**[wikipedia] "Human genome"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The human genome is a complete set of DNA sequences for each of the 22 autosomes and the two distinct sex chromosomes (X and Y). A small DNA molecule ..."

**[wikipedia] "Interbreeding between archaic and modern humans"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Interbreeding between archaic humans (such as Neanderthals and Denisovans) and anatomically modern humans (contemporaneous Homo sapiens) took place du..."

**[wikipedia] "Chimpanzee genome project"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9927)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Chimpanzee Genome Project was an effort to determine the DNA sequence of the chimpanzee genome. Sequencing began in 2005 and by 2013 twenty-four i..."

**[wikipedia] "Recent African origin of modern humans"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.979)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The recent African origin of modern humans or the "Out of Africa" theory (OOA) holds that present-day humans outside Africa descend mainly from a sing..."

**[open_alex] "The structure, function and evolution of a complete human chromosome 8"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9902)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: ". Here we use complementary long-read sequencing technologies to complete the linear assembly of human chromosome 8. Our assembly resolves the sequenc..."

**[open_alex] "Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9146)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract DNA transfer from cytoplasmic organelles to the cell nucleus is a legacy of the endosymbiotic event—the majority of nuclear-mitochondrial seg..."

**[open_alex] "The evolution and changing ecology of the African hominid oral microbiome"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Significance The microbiome plays key roles in human health, but little is known about its evolution. We investigate the evolutionary history of the A..."

**[duckduckgo] "Comparing Chimp, Bonobo and Human DNA | AMNH"**
  Type: web | Cred: estimated 0.363
  NLI (nli_deberta): supporting (0.9873)
  Verdict contribution: supporting (weight: 0.3584)
  Snippet: "The chimpanzee and another ape, bonobo, are humans' closest living relatives. These three species look alike in many ways, both in body and behavior.H..."

**[duckduckgo] "Do humans and chimps really share nearly 99% of their DNA?"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9653)
  Verdict contribution: supporting (weight: 0.8205)
  Snippet: "Chimpanzees, along with bonobos, are humans' closest living relatives. In fact, you may have heard that humans and chimps share 98.8% of their DNA. Bu..."

**[duckduckgo] "Do Humans and Chimps Share a Common... | Answers in Genesis"**
  Type: web | Cred: verified 0.25 | Bias: right-pseudoscience | Factual: low
  NLI (nli_deberta): neutral (0.6426)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Whenever you read that human and chimp DNA is 98–99% the same, it’s simply not true! The 98–99% refers only to substitutions in aligned regions where ..."

**[duckduckgo] "Humans share 98.8% of DNA with chimpanzees #facts... - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): supporting (0.9897)
  Verdict contribution: supporting (weight: 0.7334)
  Snippet: "Humans share 98.8% of chimpanzee DNA.Despite these similarities, though, we still have around 35 million differences between us. #animals #facts #wild..."

**[duckduckgo] "Chimpanzees and humans share 98.8% of their DNA — and just like..."**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9775)
  Verdict contribution: supporting (weight: 0.8309)
  Snippet: "Although chimpanzees and humans share a surprising 98.8 percent of their DNA, our differences are vast – or at least we like to think. Take a look at ..."

**[duckduckgo] "Chimpanzees, Listed Endangered | Chimps of Virunga National Park"**
  Type: web | Cred: estimated 0.429
  NLI (nli_deberta): supporting (0.9502)
  Verdict contribution: supporting (weight: 0.4076)
  Snippet: "The endangered chimpanzee, one of five species of great ape, inhabits the tropical savannas and forests of central and west Africa. It is threatened b..."

**[duckduckgo] "Animals That Share Human DNA Sequences"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Humans Share DNA with Cats and Mice. You have to go back about 25 million years to find the common ancestor of monkeys and apes and further still to f..."

**[duckduckgo] "Science fact: Chimpanzees and humans share 98.8% similar DNA...."**
  Type: web | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The reason why chimps and humans look so different is not because of genetic differences but because the ways in which the same gene can express itsel..."

**[duckduckgo] "genetics - Do apes and humans share 99% of DNA or 99% of genes?"**
  Type: web | Cred: estimated 0.45
  NLI (nli_deberta): opposing (0.876)
  Verdict contribution: opposing (weight: 0.3942)
  Snippet: "Humans and chimpanzees differ approximately every 100 nucleotides in their total DNA sequence. This is does not mean that 98.5% of the genes are share..."

**[duckduckgo] "“1% Difference” Now Overturned | Science and Culture Today"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.9341)
  Verdict contribution: supporting (weight: 0.3764)
  Snippet: "“Humans and chimps share a surprising 98.8 percent of their DNA.” (American Museum of Natural History). “[H]umans share about 99 percent of our DNA wi..."

### Verdict computation
  Supporting weight: 3.5272
  Opposing weight: 0.3942
  Support ratio: 0.8995
  Confidence: 0.799
  Verdict: **strongly supported**
  Neutral sources (no contribution): 15

  Top supporting:
    - Chimpanzees and humans share 98.8% of their DNA — and just like... (weight: 0.8309)
    - Do humans and chimps really share nearly 99% of their DNA? (weight: 0.8205)
    - Humans share 98.8% of DNA with chimpanzees #facts... - YouTube (weight: 0.7334)
    - Chimpanzees, Listed Endangered | Chimps of Virunga National Park (weight: 0.4076)
    - “1% Difference” Now Overturned | Science and Culture Today (weight: 0.3764)
  Top opposing:
    - genetics - Do apes and humans share 99% of DNA or 99% of genes? (weight: 0.3942)

---
## 31. "China has the world's largest economy"
Category: current_event
Expected: contested
Actual: contested (YES)
Claim type: factual (0.9982)

### Sources collected: 43 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 43 -> 36 (dropped 7)
Dropped sources:
  - [encyclopedia] "Economy of India" (relevance: 0.3398, reason: relevance_0.340_below_0.35)
  - [academic] "Can digital economy truly improve agricultural ecological transformation? New insights from China" (relevance: 0.3413, reason: relevance_0.341_below_0.35)
  - [academic] "Effects of digital economy on carbon emission intensity in Chinese cities: A life-cycle theory and the application of non-linear spatial panel smooth transition threshold model" (relevance: 0.305, reason: relevance_0.305_below_0.35)
  - [academic] "The perspective of meat and meat-alternative consumption in China" (relevance: 0.335, reason: relevance_0.335_below_0.35)
  - [academic] "Recent progress and emerging strategies for carbon peak and carbon neutrality in China" (relevance: 0.3177, reason: relevance_0.318_below_0.35)
  - [academic] "IDF Diabetes Atlas: Global, regional and country-level diabetes prevalence estimates for 2021 and projections for 2045" (relevance: 0.0259, reason: relevance_0.026_below_0.35)
  - [knowledge_graph] "Taiwan" (relevance: 0.3209, reason: relevance_0.321_below_0.35)

### Dedup: 36 -> 35 (dropped 1)

### Analyzed sources (35 total)

**[wikipedia] "Economy of China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.8475)
  Snippet: "The People's Republic of China (PRC) has a developing socialist market economy, incorporating industrial policies and strategic five-year plans. China..."

**[wikipedia] "Economy of the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9902)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The United States has a highly developed and diversified market-oriented economy. It is the world's largest economy by nominal GDP, generating 26% of ..."

**[wikipedia] "China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "China, officially the People's Republic of China (PRC), is a country in East Asia. It is the second-most populous country after India, with a populati..."

**[wikipedia] "List of countries by largest historical GDP"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.7969)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This list of countries by largest historical GDP shows how the membership and rankings of the world's ten largest economies as measured by their gross..."

**[wikipedia] "List of the largest trading partners of China"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This is a list of the largest trading partners of the People's Republic of China...."

**[wikipedia] "Economy of Russia"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Russia has a developing market-oriented mixed economy considered high-income and highly industrialized. It has the ninth-largest economy in the world ..."

**[wikipedia] "Economy of Japan"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Japan has a highly developed mixed economy. It is known as an East Asian model for its public investment into strategic sectors. Japan is the fourth-l..."

**[wikipedia] "Economy of the European Union"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.5967)
  Verdict contribution: supporting (weight: 0.5072)
  Snippet: "The European Union's economy combines the national economies of the supranational organization's member states. It makes up the majority of the Europe..."

**[wikipedia] "Economy of Germany"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Germany has a highly developed social market economy. As the largest economy in Europe, Germany maintains the third-largest by nominal GDP in the worl..."

**[semantic_scholar] "Vikshit Bharat: A Threat to the Global Order? - India’s Rise to the World’s Fourth-Largest Economy and the Growth Path for Startups & Unicorns"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.7446)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Recently, Sep – Oct 2025, India overtook Japan to become the world’s fourth-largest economy in terms of nominal GDP. This achievement has significant ..."

**[semantic_scholar] "Toward a new growth pole for the world: Rethinking the strategies for Huaihua International Inland Port in China"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.399)
  Snippet: "This article aims to analyze the existing Huaihua International Inland Port studies and regional economic development. On this basis, the strategic po..."

**[semantic_scholar] "FROM FACTORY OF THE WORLD TO ECONOMIC SUPERPOWER: CHINA'S INFLUENCE ON THE GLOBAL ARENA"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9775)
  Verdict contribution: opposing (weight: 0.391)
  Snippet: "China's profound transformation into a global economic power has changed the world order, challenging the traditional dominance of Western economies. ..."

**[semantic_scholar] "The role of green finance in supporting the transition to a green economy: China as a model"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.8511)
  Verdict contribution: opposing (weight: 0.4681)
  Snippet: "Amid escalating environmental challenges, this study aims to assess the pivotal role of green finance in supporting China’s transition toward a sustai..."

**[semantic_scholar] "Reducing the carbon intensity of China’s economy: the role of climate policy and carbon markets"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Since the early 2000s accelerated industrialization, urban population growth, and increased energy consumption have led the People’s Republic of China..."

**[semantic_scholar] "ANALYSIS OF THE CURRENT STATUS AND TRENDS OF CHINA'S DIGITAL ECONOMY DEVELOPMENT"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9268)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the era of rapid technological advancements, the digital economy has emerged as a powerful driver of global economic growth and transformation. It ..."

**[semantic_scholar] "The Impact of Regional Economic and Trade Conflicts on Participants and the Global Economy: A Case Study Based on the China-U.S. Trade War"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.7798)
  Verdict contribution: supporting (weight: 0.3119)
  Snippet: "Against the backdrop of globalization, China and the United States, as the world's two largest economies, exert profound influence on the global econo..."

**[semantic_scholar] "RETRACTED ARTICLE: Digital Economy and Carbon Neutrality: Exploring the Pathways and Implications for China’s Sustainable Development"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "RETRACTED ARTICLE: Digital Economy and Carbon Neutrality: Exploring the Pathways and Implications for China’s Sustainable Development..."

**[semantic_scholar] "From China to the world – Urban China studies for a global community"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): supporting (0.7407)
  Verdict contribution: supporting (weight: 0.4074)
  Snippet: "As the inaugural editors of Transactions in Planning and Urban Research, we would like to welcome you to this new journal, which we hope will become a..."

**[open_alex] "The Rise of China's Digital Economy: An Overview"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9912)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "ABSTRACT To stimulate a debate about the rise of China's digital economy, this essay compares China and the US in one key area of the digital economy ..."

**[open_alex] "Does digital finance promote the green innovation of China's listed companies?"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Does digital finance promote the green innovation of China's listed companies?..."

**[open_alex] "The impact of China's low-carbon transition on economy, society and energy in 2030 based on CO2 emissions drivers"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The impact of China's low-carbon transition on economy, society and energy in 2030 based on CO2 emissions drivers..."

**[open_alex] "Environmental regulation, market forces, and corporate environmental responsibility: Evidence from the implementation of cleaner production standards in China"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Environmental regulation, market forces, and corporate environmental responsibility: Evidence from the implementation of cleaner production standards ..."

**[open_alex] "Cotton cultivation technology with Chinese characteristics has driven the 70-year development of cotton production in China"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Since the founding of the People's Republic of China in 1949, significant achievements have been made in cotton production in China. China has maintai..."

**[open_alex] "China's roadmap to plastic waste management and associated economic costs"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "China's roadmap to plastic waste management and associated economic costs..."

**[duckduckgo] "Countries with the largest nominal GDP worldwide 2026 - Statista"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): supporting (0.895)
  Verdict contribution: supporting (weight: 0.7608)
  Snippet: "Apr 27, 2026 ... China tops the list based on PPP ... Although in nominal terms the United States is still the world's largest economy, when adjustmen..."

**[duckduckgo] "China Is Now the World's Largest Economy. We Shouldn't Be ..."**
  Type: web | Cred: verified 0.85 | Bias: right-center | Factual: high
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Oct 15, 2020 ... Converted to U.S. dollars at a market rate of 7 yuan to 1 dollar, China will have an MER GDP of $14.6 trillion versus the U.S. GDP of..."

**[duckduckgo] "The 25 Largest Economies in the World - Investopedia"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): opposing (0.9951)
  Verdict contribution: opposing (weight: 0.8458)
  Snippet: "China has the world's second-largest nominal GDP in current dollars and the largest in terms of PPP. Its economy has seen historic growth in the last ..."

**[duckduckgo] "ELI5: How is China's economy not already bigger than the USA's?"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): opposing (0.9844)
  Verdict contribution: opposing (weight: 0.5867)
  Snippet: "Jun 17, 2024 ... China will eventually overtake the US to become the world's largest economy but why haven't they already? They have 5 times the popul..."

**[duckduckgo] "Unpacking China's GDP - ChinaPower Project - CSIS"**
  Type: web | Cred: estimated 0.441
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Its economy is far larger than that of developing countries, and it has sustained decades of rapid economic growth. Yet China's economy also differs i..."

**[duckduckgo] "China as the World's “Largest Economy” | Congress.gov"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): supporting (0.7646)
  Verdict contribution: supporting (weight: 0.7264)
  Snippet: "Jan 29, 2015 ... While the PPP data purport to show that China is the world's largest economy, such data are not an indicator of the quality of that d..."

**[duckduckgo] "China | World Bank Group"**
  Type: web | Cred: estimated 0.449
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Since 1978, the beginning of China's reform and opening up period, GDP growth has averaged over 9 percent a year, lifting almost 800 million people ou..."

**[duckduckgo] "China has cemented its position as the world's second-largest ..."**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9897)
  Verdict contribution: supporting (weight: 0.4949)
  Snippet: "Mar 1, 2026 ... China is the world's largest economy, let's take a lot at China's top 10 important partners. 🛢️ For the third year in a row, China was..."

**[duckduckgo] "Analysis: China's Economy and Its Influence on Global Markets"**
  Type: web | Cred: estimated 0.45499999999999996
  NLI (nli_deberta): opposing (0.998)
  Verdict contribution: opposing (weight: 0.4541)
  Snippet: "4 days ago ... China is the world's second largest economy, trailing only the United States. Some forecasters expect China could eventually surpass th..."

**[wikidata] "People's Republic of China"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "country in East Asia | instance of: sovereign state | country: People's Republic of China | capital: Beijing | population: 1375198619 | head of govern..."

**[wikidata] "China"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "cultural region, ancient civilization, and nation in East Asia; mostly refers to the People's Republic of China in political situation and rarely refe..."

### Verdict computation
  Supporting weight: 3.2085
  Opposing weight: 3.9923
  Support ratio: 0.4456
  Confidence: 0.1089
  Verdict: **contested**
  Neutral sources (no contribution): 22

  Top supporting:
    - Countries with the largest nominal GDP worldwide 2026 - Statista (weight: 0.7608)
    - China as the World's “Largest Economy” | Congress.gov (weight: 0.7264)
    - Economy of the European Union (weight: 0.5072)
    - China has cemented its position as the world's second-largest ... (weight: 0.4949)
    - From China to the world – Urban China studies for a global community (weight: 0.4074)
  Top opposing:
    - Economy of China (weight: 0.8475)
    - The 25 Largest Economies in the World - Investopedia (weight: 0.8458)
    - ELI5: How is China's economy not already bigger than the USA's? (weight: 0.5867)
    - The role of green finance in supporting the transition to a green economy: China as a model (weight: 0.4681)
    - Analysis: China's Economy and Its Influence on Global Markets (weight: 0.4541)

---
## 32. "eating carrots improves your eyesight"
Category: factual_false
Expected: strongly opposed
Actual: sources lean supporting (**NO - MISMATCH**)
Claim type: opinion (0.9927)

### Sources collected: 33 total
  - google_factcheck: 2
  - wikipedia: 10
  - semantic_scholar: 1
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 33 -> 16 (dropped 17)
Dropped sources:
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: -0.0141, reason: relevance_-0.014_below_0.35)
  - [encyclopedia] "Creatures (video game series)" (relevance: 0.1014, reason: relevance_0.101_below_0.35)
  - [encyclopedia] "Falling Up (poetry collection)" (relevance: 0.0435, reason: relevance_0.044_below_0.35)
  - [encyclopedia] "List of The Transformers characters" (relevance: -0.0451, reason: relevance_-0.045_below_0.35)
  - [encyclopedia] "List of The Good Doctor episodes" (relevance: 0.0128, reason: relevance_0.013_below_0.35)
  - [encyclopedia] "List of The Return of Superman episodes" (relevance: 0.0638, reason: relevance_0.064_below_0.35)
  - [encyclopedia] "Discworld (world)" (relevance: 0.0701, reason: relevance_0.070_below_0.35)
  - [encyclopedia] "Fancy mouse" (relevance: -0.0134, reason: relevance_-0.013_below_0.35)
  - [encyclopedia] "List of Oggy and the Cockroaches episodes" (relevance: 0.0812, reason: relevance_0.081_below_0.35)
  - [academic] "This Year (2022) Top Stories About LoFi CBD Gummies! v1" (relevance: 0.1356, reason: relevance_0.136_below_0.35)
  - [academic] "Immune boosting functional components of natural foods and its health benefits" (relevance: 0.3252, reason: relevance_0.325_below_0.35)
  - [academic] "Exploring the Status of Preference, Utilization Practices, and Challenges to Consumption of Amaranth in Kenya and Tanzania" (relevance: 0.269, reason: relevance_0.269_below_0.35)
  - [academic] "A cluster randomized trial of a comprehensive intervention nesting family and clinic into school centered implementation to reduce myopia and obesity among children and adolescents in Beijing, China: study protocol" (relevance: 0.3126, reason: relevance_0.313_below_0.35)
  - [academic] "Fat-Soluble Vitamins and the Current Global Pandemic of COVID-19: Evidence-Based Efficacy from Literature Review" (relevance: 0.1041, reason: relevance_0.104_below_0.35)
  - [academic] "Food essentialism: Implications for expectations and perceptions of the properties of processed foods" (relevance: 0.1743, reason: relevance_0.174_below_0.35)
  - [academic] "“I Climbed a Fig Tree, on an Apple Bashing Spree, Only Pears Fell Free”: Economic, Symbolic and Intrinsic Values of Plants Occurring in Slovenian Folk Songs Collected by K. Štrekelj (1895–1912)" (relevance: 0.0922, reason: relevance_0.092_below_0.35)
  - [academic] "Exploring the factors influencing nutritional literacy based on the socioecological model among patients with age-related macular degeneration: a qualitative study from China" (relevance: 0.2537, reason: relevance_0.254_below_0.35)

### Dedup: 16 -> 16 (dropped 0)

### Analyzed sources (16 total)

**[google_factcheck] "Does Eating Carrots Improve Your Vision?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Eating carrots results in significantly improved vision...."

**[google_factcheck] "Carrots Alone Won't Improve Eyesight"**
  Type: fact_check | Cred: estimated 0.85
  NLI (factcheck_rating_bypass): opposing (0.75)
  Verdict contribution: opposing (weight: 0.6375)
  Snippet: "Carrots improve eyesight...."

**[wikipedia] "Carrot"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The carrot (Daucus carota subsp. sativus) is a root vegetable in the umbellifer family Apiaceae. Carrots are typically orange in colour due to their b..."

**[open_alex] "Exploring the knowledge, attitudes, and practice towards child eye health: A qualitative analysis of parent experience focus groups"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "BACKGROUND: The majority of childhood blindness causes in low-income countries are treatable or avoidable. Parents or guardians are responsible for ma..."

**[open_alex] "Unveiling the Spectrum of Ophthalmic Manifestations in Nutritional Deficiencies: A Comprehensive Review"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This comprehensive review explores the intricate relationship between nutrition and ocular health, focusing on the crucial roles of essential nutrient..."

**[open_alex] "HOW 6 BENEFITS OF CARROT JUICE YOU NEVER KNEW!"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.8276)
  Verdict contribution: supporting (weight: 0.331)
  Snippet: "Carrots are power foods, that is one of the major reasons why it is suggested by our elders. Of all of their health enhancing properties, the one rela..."

**[duckduckgo] "4 Ways Eating Carrots Regularly Can Improve Your Eyesight - Health"**
  Type: web | Cred: estimated 0.382
  NLI (nli_deberta): supporting (0.8867)
  Verdict contribution: supporting (weight: 0.3387)
  Snippet: "Carrots are rich in antioxidants that support night vision, reduce the risk of age-related vision loss, and protect against cataracts...."

**[duckduckgo] "Does Eating Carrots Help Improve Eyesight? 5 Proven Benefits You Should ..."**
  Type: web | Cred: estimated 0.254
  NLI (nli_deberta): neutral (0.7349)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Know the truth about carrots and eyesight. Learn 5 proven benefits of carrots for eye health, vision, skin, and overall wellness in this detailed guid..."

**[duckduckgo] "Carrots & Eye Health: Myth or Fact? - University of Utah Health"**
  Type: web | Cred: estimated 0.47800000000000004
  NLI (nli_deberta): neutral (0.752)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Your eyes rely on tiny arteries for oxygen and nutrients, just as your heart relies on much larger arteries. That means you get a two-for-one benefit ..."

**[duckduckgo] "Are Carrots Good for Your Eyes? - Healthline"**
  Type: web | Cred: verified 0.5 | Bias: pro-science | Factual: mixed
  NLI (nli_deberta): supporting (0.6172)
  Verdict contribution: supporting (weight: 0.3086)
  Snippet: "Carrots and eye health It has long been believed that eating carrots promotes eye health and improves your eyesight, especially at night...."

**[duckduckgo] "Carrots and Eyesight: The Truth Behind the Myth"**
  Type: web | Cred: estimated 0.229
  NLI (nli_deberta): supporting (0.9458)
  Verdict contribution: supporting (weight: 0.2166)
  Snippet: "The idea that eating carrots can significantly improve your eyesight, particularly night vision, was popularized during World War II. British Royal Ai..."

**[duckduckgo] "Yes, eating carrots can help your eyesight. But it's not a cure-all."**
  Type: web | Cred: verified 0.85 | Factual: high
  NLI (nli_deberta): supporting (0.9956)
  Verdict contribution: supporting (weight: 0.8463)
  Snippet: "Yes, eating carrots can help your eyesight. But it's not a cure-all. The World War II propaganda that touted the veggie wasn't totally wrong, but carr..."

**[duckduckgo] "Do carrots help you see at night? The truth behind popular food myths - BBC"**
  Type: web | Cred: estimated 0.47400000000000003
  NLI (nli_deberta): opposing (0.6587)
  Verdict contribution: opposing (weight: 0.3122)
  Snippet: "Whilst eating carrots can help keep the cells in your eyes healthy and functioning well, nutrition experts agree they won't give you superhuman night ..."

**[duckduckgo] "Myths about Your Eyes - WebMD"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9653)
  Verdict contribution: supporting (weight: 0.8205)
  Snippet: "Eating Carrots Will Improve Your Vision Fact: Carrots are high in vitamin A, a nutrient essential for good vision. Eating carrots will provide you wit..."

**[duckduckgo] "Do Carrots Improve Vision? Separating Fact from Fiction About Eye ..."**
  Type: web | Cred: estimated 0.22000000000000003
  NLI (nli_deberta): opposing (0.8682)
  Verdict contribution: opposing (weight: 0.191)
  Snippet: "Discover the truth behind the age-old claim that carrots improve your vision. While rich in vitamin A, essential for eye health and night vision, eati..."

**[duckduckgo] "Myth or Fact: Eating Carrots Improves Eyesight | Duke Health"**
  Type: web | Cred: estimated 0.302
  NLI (nli_deberta): neutral (0.6074)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The notion that eating carrots improves eyesight sounds like a story your mother made up to get you to eat your vegetables...."

### Verdict computation
  Supporting weight: 2.8617
  Opposing weight: 1.6157
  Support ratio: 0.6391
  Confidence: 0.2783
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 6

  Top supporting:
    - Yes, eating carrots can help your eyesight. But it's not a cure-all. (weight: 0.8463)
    - Myths about Your Eyes - WebMD (weight: 0.8205)
    - 4 Ways Eating Carrots Regularly Can Improve Your Eyesight - Health (weight: 0.3387)
    - HOW 6 BENEFITS OF CARROT JUICE YOU NEVER KNEW! (weight: 0.331)
    - Are Carrots Good for Your Eyes? - Healthline (weight: 0.3086)
  Top opposing:
    - Carrots Alone Won't Improve Eyesight (weight: 0.6375)
    - Does Eating Carrots Improve Your Vision? (weight: 0.475)
    - Do carrots help you see at night? The truth behind popular food myths - BBC (weight: 0.3122)
    - Do Carrots Improve Vision? Separating Fact from Fiction About Eye ... (weight: 0.191)

---
## 33. "college education is worth the cost"
Category: opinion
Expected: opinion
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.997)

### Sources collected: 49 total
  - google_factcheck: 0
  - wikipedia: 10
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 49 -> 24 (dropped 25)
Dropped sources:
  - [encyclopedia] "List of colleges and universities in Florida" (relevance: 0.3056, reason: relevance_0.306_below_0.35)
  - [encyclopedia] "Fort Worth, Texas" (relevance: 0.133, reason: relevance_0.133_below_0.35)
  - [encyclopedia] "Dallas Fort Worth International Airport" (relevance: 0.0933, reason: relevance_0.093_below_0.35)
  - [encyclopedia] "Technical College System of Georgia" (relevance: 0.2299, reason: relevance_0.230_below_0.35)
  - [encyclopedia] "History of African Americans in Dallas–Fort Worth" (relevance: 0.168, reason: relevance_0.168_below_0.35)
  - [encyclopedia] "Advanced Placement" (relevance: 0.2702, reason: relevance_0.270_below_0.35)
  - [academic] "Effects of examination malpractice on students’ academic performance: Evidence from Federal College of Education, Gidan-Madi" (relevance: 0.2306, reason: relevance_0.231_below_0.35)
  - [academic] "I am worth saving- A Qualitative Study of People with Alzheimers Disease Considering Lecanemab Treatment" (relevance: 0.2876, reason: relevance_0.288_below_0.35)
  - [academic] "EFFECTIVENESS OF THE USE OF TECHNOLOGY IN TEACHING FOR PROMOTING ECONOMIC GROWTH AMONG BUSINESS EDUCATION GRADUATES IN EKITI STATE" (relevance: 0.2853, reason: relevance_0.285_below_0.35)
  - [academic] "PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews" (relevance: -0.009, reason: relevance_-0.009_below_0.35)
  - [academic] "Chatting and cheating: Ensuring academic integrity in the era of ChatGPT" (relevance: 0.1889, reason: relevance_0.189_below_0.35)
  - [academic] "Dementia prevention, intervention, and care: 2024 report of the Lancet standing Commission" (relevance: 0.047, reason: relevance_0.047_below_0.35)
  - [academic] "The school and society" (relevance: 0.2071, reason: relevance_0.207_below_0.35)
  - [academic] "Why science education is more important than most scientists think" (relevance: 0.2984, reason: relevance_0.298_below_0.35)
  - [academic] "Application of Simulation Technology in Vocational Education Skills Competition" (relevance: 0.2511, reason: relevance_0.251_below_0.35)
  - [academic] "Educational collaboration can empower patients, support doctors in training and future‐proof medical education" (relevance: 0.2402, reason: relevance_0.240_below_0.35)
  - [academic] "Finite Element Modeling and Simulation of Torsion Experiment and Teaching Practice in Vocational Colleges" (relevance: 0.1806, reason: relevance_0.181_below_0.35)
  - [academic] "Why Working from Home Will Stick" (relevance: 0.118, reason: relevance_0.118_below_0.35)
  - [academic] "Impact of the COVID‐19 pandemic on the career of junior doctors" (relevance: 0.1635, reason: relevance_0.163_below_0.35)
  - [knowledge_graph] "Worth" (relevance: 0.0653, reason: relevance_0.065_below_0.35)
  - [knowledge_graph] "Worth" (relevance: 0.1172, reason: relevance_0.117_below_0.35)
  - [knowledge_graph] "Wörth" (relevance: 0.0904, reason: relevance_0.090_below_0.35)
  - [knowledge_graph] "Costco" (relevance: 0.0767, reason: relevance_0.077_below_0.35)
  - [knowledge_graph] "Costa" (relevance: -0.0332, reason: relevance_-0.033_below_0.35)
  - [knowledge_graph] "Costa Rica" (relevance: -0.046, reason: relevance_-0.046_below_0.35)

### Dedup: 24 -> 24 (dropped 0)

### Analyzed sources (24 total)

**[wikipedia] "Higher education in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the United States, higher education is an optional stage of formal learning following secondary education. It is also referred to as post-secondary..."

**[wikipedia] "Crimson Education"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Crimson Education is a multinational university admissions consultancy headquartered in Auckland, New Zealand.
The business specializes in providing c..."

**[wikipedia] "Higher education financing issues in the United States"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Financial issues facing students in the United States include the rising cost of tuition, as well as ancillaries, such as room and board, textbook and..."

**[wikipedia] "Higher education bubble in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is concern that the possible higher education bubble in the United States could have negative repercussions in the broader economy. Although col..."

**[semantic_scholar] "Researchable Questions in History and Economics of Higher Education"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Researchable Questions in History and Economics of Higher Education..."

**[semantic_scholar] "Aimless And Under Siege: Theorizing Change In American Higher Education"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.5776)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is a stark irony about the state of American higher education at present. American universities and colleges have never enjoyed greater signific..."

**[semantic_scholar] "The Proper Role of Higher Education in a Democratic Society"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.7847)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "American higher education has served to prepare students to be active participants in a democratic society. During a time of great civil upheaval foll..."

**[semantic_scholar] "Rising Colleges Fees: a Reflection of Offerings or Aspirations"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Rising Colleges Fees: a Reflection of Offerings or Aspirations..."

**[semantic_scholar] "Is the value worth the costs?: Examining the experiences of preservice teachers of color in predominantly White colleges of education"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "ABSTRACT Recruiting and retaining students of color in colleges of education in predominately White institutions (PWIs) is a source of concern. Effort..."

**[semantic_scholar] "Innovative Models of Higher Education Management and Student Training Mechanisms under Big Data Technology"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "By using a refined K-means algorithm that includes optimized initial centroid selection and lessened distance computations, this research clusters stu..."

**[semantic_scholar] "Cost-Benefit Analysis of Cloud Computing in Education Using the Base Cost Estimation Model"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cloud computing is one of technology's miracle workers that fulfill today's needs. Especially with the current economic crisis due to COVID-19 and the..."

**[duckduckgo] "Is a College Degree Worth It in 2024? | Pew Research Center"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.8721)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "May 7, 2025 - Some 47% say the cost is worth it only if someone doesn’t have to take out loans. And 29% say the cost is not worth it. These findings c..."

**[duckduckgo] "Is College Worth the Cost? Factors to Consider"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9844)
  Verdict contribution: supporting (weight: 0.8367)
  Snippet: "February 20, 2025 - For most students, experts say, it remains financially worthwhile to go to college, despite rising tuition. College graduates lear..."

**[duckduckgo] "Is a College Education Still Worth It? | UCLA has the Data | UCLA"**
  Type: web | Cred: estimated 0.47300000000000003
  NLI (nli_deberta): supporting (0.7373)
  Verdict contribution: supporting (weight: 0.3487)
  Snippet: "February 12, 2026 - Both in the video and almost four years later, Chang points out that college can be worth it for students who are interested in tr..."

**[duckduckgo] "Is College Worth the Cost? | Champlain College Online"**
  Type: web | Cred: estimated 0.353
  NLI (nli_deberta): supporting (0.9507)
  Verdict contribution: supporting (weight: 0.3356)
  Snippet: "April 20, 2026 - It's a valid question - but in short, the answer is yes. You might look at the list above and think that there's no way that spending..."

**[duckduckgo] "Is College Worth It? a Cost-Benefit Analysis of College in 2025"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.5327)
  Verdict contribution: supporting (weight: 0.4528)
  Snippet: "March 19, 2025 - The same survey uncovered that 47% of adults in the U.S. think college is worth it only as long as you don't have to take out loans. ..."

**[duckduckgo] "Is College Worth It? Pros and Cons of Going to College"**
  Type: web | Cred: estimated 0.272
  NLI (nli_deberta): neutral (0.9341)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "March 16, 2026 - So even if you go into college not quite sure what you want to do for a career yet, you can use the resources your school provides to..."

**[duckduckgo] "Is College Still Worth It? - Liberty Street Economics"**
  Type: web | Cred: estimated 0.462
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "April 16, 2025 - Thank you for your comment, Nick. To estimate the out-of-pocket cost of college, we use the best information available from National ..."

**[duckduckgo] "Is a College Education Worth the Cost? | Edvisors"**
  Type: web | Cred: estimated 0.27799999999999997
  NLI (nli_deberta): supporting (0.9858)
  Verdict contribution: supporting (weight: 0.2741)
  Snippet: "May 8, 2025 - Although some arguments might stem ... rates. The message is clear: pursuing a college degree is often a worthwhile investment, offering..."

**[duckduckgo] "Is College Worth It?"**
  Type: web | Cred: estimated 0.313
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "3 weeks ago - Earning a degree in a timely manner ... costs, run the risk of losing financial aid eligibility, and further delay their entry into the ..."

**[duckduckgo] "Is College Still Worth the High Price? Weighing Costs and Benefits of Investing in Human Capital | St. Louis Fed"**
  Type: web | Cred: estimated 0.40599999999999997
  NLI (nli_deberta): neutral (0.8149)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "November 18, 2025 - A March 2023 survey found that only 42% of Americans believe college is worth the cost because it leads to better job opportunitie..."

**[wikidata] "higher education"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "academic tertiary education, such as from colleges and universities | instance of: educational stage..."

**[wikidata] "college education in Quebec"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "college education system in Quebec, Canada | instance of: education in country or region | country: Canada | located in: Quebec..."

**[wikidata] "higher education in the Bahamas"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "national university and college education | instance of: higher education in country or region | country: The Bahamas..."

### Verdict computation
  Supporting weight: 2.2479
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 19

  Top supporting:
    - Is College Worth the Cost? Factors to Consider (weight: 0.8367)
    - Is College Worth It? a Cost-Benefit Analysis of College in 2025 (weight: 0.4528)
    - Is a College Education Still Worth It? | UCLA has the Data | UCLA (weight: 0.3487)
    - Is College Worth the Cost? | Champlain College Online (weight: 0.3356)
    - Is a College Education Worth the Cost? | Edvisors (weight: 0.2741)

---
## 34. "inflation in the United States is under control"
Category: current_event
Expected: contested
Actual: strongly opposed (**NO - MISMATCH**)
Claim type: factual (0.9981)

### Sources collected: 40 total
  - google_factcheck: 1
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 40 -> 21 (dropped 19)
Dropped sources:
  - [encyclopedia] "Rent control in the United States" (relevance: 0.2773, reason: relevance_0.277_below_0.35)
  - [encyclopedia] "Fuel taxes in the United States" (relevance: 0.2435, reason: relevance_0.244_below_0.35)
  - [encyclopedia] "2028 United States presidential election" (relevance: 0.1916, reason: relevance_0.192_below_0.35)
  - [encyclopedia] "2028 United States elections" (relevance: 0.1507, reason: relevance_0.151_below_0.35)
  - [encyclopedia] "2026 in the United States" (relevance: 0.186, reason: relevance_0.186_below_0.35)
  - [encyclopedia] "List of disasters in the United States by death toll" (relevance: 0.3351, reason: relevance_0.335_below_0.35)
  - [academic] "EU Strategic Autonomy after the Russian Invasion of Ukraine: Europe's Capacity to Act in Times of War" (relevance: 0.0366, reason: relevance_0.037_below_0.35)
  - [academic] "European Integration and the War in Ukraine: Just Another Crisis?" (relevance: 0.0955, reason: relevance_0.096_below_0.35)
  - [academic] "Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DALYs), and healthy life expectancy (HALE) for 371 diseases and injuries in 204 countries and territories and 811 subnational locations, 1990–2021: a systematic analysis for the Global Burden of Disease Study 2021" (relevance: 0.0649, reason: relevance_0.065_below_0.35)
  - [academic] "Foreign currency exchange rate prediction using non-linear Schrödinger equations with economic fundamental parameters" (relevance: 0.2037, reason: relevance_0.204_below_0.35)
  - [academic] "The impact of COVID‐19 on African economies: An introduction" (relevance: 0.2403, reason: relevance_0.240_below_0.35)
  - [academic] "Common Method Bias: It's Bad, It's Complex, It's Widespread, and It's Not Easy to Fix" (relevance: 0.0562, reason: relevance_0.056_below_0.35)
  - [academic] "A Focus on Contraception in the Wake of Dobbs" (relevance: 0.0834, reason: relevance_0.083_below_0.35)
  - [knowledge_graph] "United States" (relevance: 0.1273, reason: relevance_0.127_below_0.35)
  - [knowledge_graph] "United States Census Bureau" (relevance: 0.0756, reason: relevance_0.076_below_0.35)
  - [knowledge_graph] "Mexico" (relevance: 0.035, reason: relevance_0.035_below_0.35)
  - [knowledge_graph] "Under Control" (relevance: 0.1873, reason: relevance_0.187_below_0.35)
  - [knowledge_graph] "Under Control" (relevance: 0.1262, reason: relevance_0.126_below_0.35)
  - [knowledge_graph] "Under Control" (relevance: 0.1468, reason: relevance_0.147_below_0.35)

### Dedup: 21 -> 21 (dropped 0)

### Analyzed sources (21 total)

**[google_factcheck] "President Donald Trump says the US has ‘no inflation.’ By 2 ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The U.S. currently has “no inflation.”..."

**[wikipedia] "Inflation"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In economics, inflation is an increase in the average price of goods and services in terms of money.This increase is measured using a price index, typ..."

**[wikipedia] "2021–2023 inflation surge"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Following the start of the COVID-19 pandemic in 2020, a worldwide surge in inflation began in mid-2021 and lasted until mid-2022. Many countries saw t..."

**[wikipedia] "List of countries by inflation rate"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This is the list of countries by annual inflation rate. Inflation is defined as a positive annual percent change in consumer prices compared with the ..."

**[wikipedia] "Housing crisis in the United States"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.6543)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "For decades, the United States has faced a growing shortage of housing. The scope and effect of the housing crisis depends on the affected region or s..."

**[open_alex] "Inflation: The problems for aquaculture"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.959)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Inflation has been a popular news topic in 2022, with reports that inflation has reached its highest rates in 30–40 years in some countries (Davies, 2..."

**[open_alex] "Monetary Policy Performance under Control of exchange rate and consumer price index"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9219)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Central Reserve announced the Monetary Policy Rate and equally interested in the output of exchange rate and price stability. Besides having a stabili..."

**[open_alex] "Hyperinflation in Venezuela"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Venezuela entered hyperinflation at the end of 2017, preceded by several years of large budget deficits and declining oil revenues. Despite many polic..."

**[duckduckgo] "US inflation dynamics effect on US economy | Deloitte Insights"**
  Type: web | Cred: estimated 0.365
  NLI (nli_deberta): opposing (0.6445)
  Verdict contribution: opposing (weight: 0.2352)
  Snippet: "These price shocks will likely raise domestic inflation in the United States. This will likely make the Fed even more cautious when cutting interest r..."

**[duckduckgo] "Why Are Prices Rising? Understanding America's Inflation Problem"**
  Type: web | Cred: estimated 0.34700000000000003
  NLI (nli_deberta): supporting (0.751)
  Verdict contribution: supporting (weight: 0.2606)
  Snippet: "In the United States, responsibility for managing the economy and combating inflation is shared between the Federal Reserve, which conducts monetary p..."

**[duckduckgo] "How Governments Fight Inflation With Monetary Policies"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Explore how governments use monetary policy, interest rates, and other strategies to control inflation and sustain economic growth...."

**[duckduckgo] "Inflation in the U.S. Economy: Causes and Policy Options"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): opposing (0.915)
  Verdict contribution: opposing (weight: 0.8692)
  Snippet: "Introduction The COVID-19 pandemic has led to many unexpected and unprecedented economic developments. 1 One such development is higher price inflatio..."

**[duckduckgo] "Current U.S. Inflation Rates: 2000-2026 - US Inflation Calculator"**
  Type: web | Cred: estimated 0.292
  NLI (nli_deberta): neutral (0.9937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The annual inflation rate in the United States was 3.8% for the 12 months ending April, up from 3.3% previously, according to U.S. Labor Department da..."

**[duckduckgo] "Is the U.S. in an Above-Target Inflation Regime? | St. Louis Fed"**
  Type: web | Cred: estimated 0.40599999999999997
  NLI (nli_deberta): neutral (0.9414)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Just like during the inflation surge, the above-target inflation period is broad-based and not attributable to a few sectors or categories. These fact..."

**[duckduckgo] "Current US Inflation Rate at 3.8%: Latest CPI Report - Forbes"**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9658)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "According to the Labor Department's most recent report, CPI in March was 3.3% higher than one year prior and 0.9% higher than in February...."

**[duckduckgo] "US inflation may slow, but the affordability debate is likely to keep ..."**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Consumers - voters - focus far less on the macroeconomic generalities analyzed by economists, for whom inflation is a carefully weighted average rate ..."

**[duckduckgo] "PDF Inflation since the Pandemic: Lessons and Challenges"**
  Type: web | Cred: estimated 0.46900000000000003
  NLI (nli_deberta): neutral (0.9893)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The stability of longer-term inflation expectations, in turn, likely helped to contain the inflation surge, allowing inflation and short-term inflatio..."

**[duckduckgo] "CPI Home : U.S. Bureau of Labor Statistics"**
  Type: web | Cred: estimated 0.44000000000000006
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Consumer Price Index (CPI) is a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer good..."

**[wikidata] "inflation"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "rise in price level in an economy over time | instance of: economic concept..."

**[wikidata] "inflation"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "theory of rapid universe expansion | instance of: cosmological model..."

**[wikidata] "Inflation"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "short documentary | instance of: short film..."

### Verdict computation
  Supporting weight: 0.2606
  Opposing weight: 1.1045
  Support ratio: 0.1909
  Confidence: 0.6182
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 18

  Top supporting:
    - Why Are Prices Rising? Understanding America's Inflation Problem (weight: 0.2606)
  Top opposing:
    - Inflation in the U.S. Economy: Causes and Policy Options (weight: 0.8692)
    - US inflation dynamics effect on US economy | Deloitte Insights (weight: 0.2352)

---
## 35. "the Amazon rainforest produces about 20% of the world's oxygen"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.998)

### Sources collected: 36 total
  - google_factcheck: 3
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 36 -> 21 (dropped 15)
Dropped sources:
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: 0.0622, reason: relevance_0.062_below_0.35)
  - [encyclopedia] "Gold mining in Brazil" (relevance: 0.2935, reason: relevance_0.293_below_0.35)
  - [encyclopedia] "Cocoa bean" (relevance: 0.2811, reason: relevance_0.281_below_0.35)
  - [academic] "An Atlas of Phanerozoic Paleogeographic Maps: The Seas Come In and the Seas Go Out" (relevance: 0.0728, reason: relevance_0.073_below_0.35)
  - [academic] "The 2023 report of the Lancet Countdown on health and climate change: the imperative for a health-centred response in a world facing irreversible harms" (relevance: 0.0554, reason: relevance_0.055_below_0.35)
  - [academic] "Our future in the Anthropocene biosphere" (relevance: 0.1497, reason: relevance_0.150_below_0.35)
  - [academic] "COP26: more challenges than achievements" (relevance: -0.0059, reason: relevance_-0.006_below_0.35)
  - [academic] "Reviewing the Impact of Land Use and Land‐Use Change on Moisture Recycling and Precipitation Patterns" (relevance: 0.2939, reason: relevance_0.294_below_0.35)
  - [academic] "Actions to halt biodiversity loss generally benefit the climate" (relevance: 0.2218, reason: relevance_0.222_below_0.35)
  - [academic] "The Angiosperm Terrestrial Revolution and the origins of modern biodiversity" (relevance: 0.3398, reason: relevance_0.340_below_0.35)
  - [academic] "Anthropogenic Drought: Definition, Challenges, and Opportunities" (relevance: 0.1729, reason: relevance_0.173_below_0.35)
  - [academic] "Environment of Peace: Security in a New Era of Risk" (relevance: 0.1054, reason: relevance_0.105_below_0.35)
  - [knowledge_graph] "Percent Free time" (relevance: 0.0555, reason: relevance_0.055_below_0.35)
  - [knowledge_graph] "⅕" (relevance: 0.0725, reason: relevance_0.072_below_0.35)
  - [knowledge_graph] "20% d’amour en plus" (relevance: 0.0665, reason: relevance_0.067_below_0.35)

### Dedup: 21 -> 18 (dropped 3)

### Analyzed sources (18 total)

**[google_factcheck] "Amazon Doesn’t Produce 20% of Earth’s Oxygen"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.9025)
  Snippet: ""The Amazon creates over 20% of the world’s oxygen."..."

**[google_factcheck] "Take a breath: the Amazon does not produce 20% of the world's ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "The Amazon rainforest _ “the lungs of the Earth” _ produces 20% of the planet’s oxygen...."

**[google_factcheck] "Amazon fires are destructive, but they aren't depleting Earth's ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.9025)
  Snippet: "The Amazon rain forest produces 20% of our planet’s oxygen..."

**[wikipedia] "Deforestation of the Amazon rainforest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Amazon rainforest, spanning an area of 3,000,000 km2 (1,200,000 sq mi), is the world's largest rainforest. It encompasses the largest and most bio..."

**[wikipedia] "Amazon rainforest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Amazon rainforest, also called the Amazon jungle or Amazonia, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the..."

**[wikipedia] "Rainforest"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Rainforests are forests characterized by a closed and continuous tree canopy, moisture-dependent vegetation, the presence of epiphytes and lianas and ..."

**[wikipedia] "Tropical rainforest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Tropical rainforests are dense and warm rainforests with high rainfall typically found between 10° north and south of the Equator. They are a subset o..."

**[wikipedia] "2019 Amazon rainforest wildfires"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The 2019 Amazon rainforest wildfires season saw a year-to-year surge in fires occurring in the Amazon rainforest and Amazon biome within Brazil, Boliv..."

**[wikipedia] "Amazon basin"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Amazon basin is the part of South America drained by the Amazon River and its tributaries. The Amazon drainage basin covers  a large area spreadin..."

**[wikipedia] "Deforestation in Brazil"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Brazil once had the highest deforestation rate in the world, and recent data still shows high rates of deforestation. Between 2001 and 2023, Brazil lo..."

**[open_alex] "Ecosystem services provided by marine and freshwater phytoplankton"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Phytoplankton, the ecological group of microalgae adapted to live in apparent suspension in water masses, is much more than an ecosystem's engineer. I..."

**[duckduckgo] "Why the Amazon doesn’t really produce 20% of the world’s oxygenHow Much Oxygen Does the Rainforest Produce? - Biology InsightsAmazon Doesn’t Produce 20% of Earth’s Oxygen - FactCheck.orgDoes the amazon provide 20% of our oxygen? - oxfordecosystemsHow Much Oxygen Does the Amazon Forest Produce? Separating ...Amazon Rainforest Doesn’t Actually Produce 20% of the World’s ...Take a breath: the Amazon does not produce 20% of the world’s ..."**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.8892)
  Verdict contribution: supporting (weight: 0.7558)
  Snippet: "Aug 19, 2025 · Given that the atmosphere contains less than half a percent of carbon dioxide, but 21 percent oxygen, it’s not possible for the Amazon ..."

**[duckduckgo] "How Much Oxygen Does the Rainforest Produce? - Biology Insights"**
  Type: web | Cred: estimated 0.41
  NLI (nli_deberta): neutral (0.7402)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jan 9, 2026 · The popular belief that the Amazon rainforest produces 20% or more of the world’s atmospheric oxygen is a misconception. The scientifica..."

**[duckduckgo] "Does the amazon provide 20% of our oxygen? - oxfordecosystems"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.2995)
  Snippet: "Oct 7, 2019 · So, in all practical terms, the net contribution of the Amazon ECOSYSTEM (not just the plants alone) to the world's oxygen is effectivel..."

**[duckduckgo] "How Much Oxygen Does the Amazon Forest Produce? Separating ..."**
  Type: web | Cred: estimated 0.399
  NLI (nli_deberta): supporting (0.8354)
  Verdict contribution: supporting (weight: 0.3333)
  Snippet: "Dec 23, 2025 · The Amazon doesn’t produce 20% of the world’s oxygen – This widely shared claim is scientifically false. The forest produces and consum..."

**[duckduckgo] "Amazon Rainforest Doesn’t Actually Produce 20% of the World’s ..."**
  Type: web | Cred: estimated 0.40800000000000003
  NLI (nli_deberta): neutral (0.8066)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jul 19, 2023 · Amazon’s myriad microbes likely consume the remainder of the oxygen produced. Therefore, the Amazon rainforest’s net contribution to th..."

**[duckduckgo] "How the Amazon Rainforest Produces 20% of the World's Oxygen"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): supporting (0.9814)
  Verdict contribution: supporting (weight: 0.7272)
  Snippet: "The Amazon Rainforest is the largest rainforest in the world, and it plays a vital role in the Earth's ecosystem.In fact, the Amazon is estimated to p..."

**[duckduckgo] "Why is it said that Amazon creates 20% of the oxygen production of..."**
  Type: web | Cred: estimated 0.35
  NLI (nli_deberta): opposing (0.7119)
  Verdict contribution: opposing (weight: 0.2492)
  Snippet: "Clearly the Amazon does not create 20 percent of the worlds oxygen. Most of the oxygen in the atmosphere is fossil oxygen, produced by photosynthetic ..."

### Verdict computation
  Supporting weight: 1.8164
  Opposing weight: 3.1612
  Support ratio: 0.3649
  Confidence: 0.2702
  Verdict: **likely opposed**
  Neutral sources (no contribution): 10

  Top supporting:
    - Why the Amazon doesn’t really produce 20% of the world’s oxygenHow Much Oxygen Does the Rainforest Produce? - Biology InsightsAmazon Doesn’t Produce 20% of Earth’s Oxygen - FactCheck.orgDoes the amazon provide 20% of our oxygen? - oxfordecosystemsHow Much Oxygen Does the Amazon Forest Produce? Separating ...Amazon Rainforest Doesn’t Actually Produce 20% of the World’s ...Take a breath: the Amazon does not produce 20% of the world’s ... (weight: 0.7558)
    - How the Amazon Rainforest Produces 20% of the World's Oxygen (weight: 0.7272)
    - How Much Oxygen Does the Amazon Forest Produce? Separating ... (weight: 0.3333)
  Top opposing:
    - Amazon Doesn’t Produce 20% of Earth’s Oxygen (weight: 0.9025)
    - Amazon fires are destructive, but they aren't depleting Earth's ... (weight: 0.9025)
    - Take a breath: the Amazon does not produce 20% of the world's ... (weight: 0.8075)
    - Does the amazon provide 20% of our oxygen? - oxfordecosystems (weight: 0.2995)
    - Why is it said that Amazon creates 20% of the oxygen production of... (weight: 0.2492)

---
## 36. "the Great Wall of China is the only man-made structure visible from space"
Category: factual_false
Expected: strongly opposed
Actual: strongly opposed (YES)
Claim type: factual (0.9979)

### Sources collected: 37 total
  - google_factcheck: 1
  - wikipedia: 10
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 37 -> 18 (dropped 19)
Dropped sources:
  - [encyclopedia] "Plan 9 from Outer Space" (relevance: 0.0965, reason: relevance_0.096_below_0.35)
  - [encyclopedia] "Kowloon Walled City" (relevance: 0.2243, reason: relevance_0.224_below_0.35)
  - [encyclopedia] "Benin Moat" (relevance: 0.2911, reason: relevance_0.291_below_0.35)
  - [encyclopedia] "Ziad Fazah" (relevance: 0.0836, reason: relevance_0.084_below_0.35)
  - [encyclopedia] "People's Liberation Army" (relevance: 0.0562, reason: relevance_0.056_below_0.35)
  - [academic] "The Road Towards 6G: A Comprehensive Survey" (relevance: 0.0207, reason: relevance_0.021_below_0.35)
  - [academic] "Review on Ammonia as a Potential Fuel: From Synthesis to Economics" (relevance: -0.1011, reason: relevance_-0.101_below_0.35)
  - [academic] "Human-in-the-loop machine learning: a state of the art" (relevance: 0.0002, reason: relevance_0.000_below_0.35)
  - [academic] "State of the Art in Defect Detection Based on Machine Vision" (relevance: 0.142, reason: relevance_0.142_below_0.35)
  - [academic] "A Survey on Blockchain Technology: Evolution, Architecture and Security" (relevance: 0.048, reason: relevance_0.048_below_0.35)
  - [academic] "Exosomes as a new frontier of cancer liquid biopsy" (relevance: -0.0305, reason: relevance_-0.030_below_0.35)
  - [academic] "Structural Design Strategies of Polymer Matrix Composites for Electromagnetic Interference Shielding: A Review" (relevance: 0.1259, reason: relevance_0.126_below_0.35)
  - [academic] "The 2022 Plasma Roadmap: low temperature plasma science and technology" (relevance: 0.0802, reason: relevance_0.080_below_0.35)
  - [academic] "Metals to combat antimicrobial resistance" (relevance: 0.0091, reason: relevance_0.009_below_0.35)
  - [academic] "Layered double hydroxide-based nanomaterials for biomedical applications" (relevance: 0.0601, reason: relevance_0.060_below_0.35)
  - [knowledge_graph] "galaxy filament" (relevance: 0.3122, reason: relevance_0.312_below_0.35)
  - [knowledge_graph] "People's Republic of China" (relevance: 0.2424, reason: relevance_0.242_below_0.35)
  - [knowledge_graph] "Taiwan" (relevance: 0.137, reason: relevance_0.137_below_0.35)
  - [knowledge_graph] "China" (relevance: 0.2314, reason: relevance_0.231_below_0.35)

### Dedup: 18 -> 17 (dropped 1)

### Analyzed sources (17 total)

**[google_factcheck] "Is the Great Wall of China Visible from the Moon?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "The Great Wall of China is the only man-made object visible from the moon...."

**[wikipedia] "Artificial structures visible from space"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): opposing (0.999)
  Verdict contribution: opposing (weight: 0.6993)
  Snippet: "Artificial structures visible from space without magnification include highways, dams, and cities. 
Whether an object is visible depends significantly..."

**[wikipedia] "Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Great Wall of China (traditional Chinese: 萬里長城; simplified Chinese: 万里长城; pinyin: Wànlǐ Chángchéng, literally "ten thousand li long wall") is a se..."

**[wikipedia] "History of the Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The history of the Great Wall of China began when fortifications built by various states during the Spring and Autumn (771–476 BC) and Warring States ..."

**[wikipedia] "Ming Great Wall"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.998)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Ming Great Wall (Chinese: 明長城; pinyin: Míng Chángchéng), built by the Ming dynasty (1368–1644), forms the most visible parts of the Great Wall of ..."

**[wikipedia] "Mexico–United States border wall"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.978)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A border wall has been built along portions of the Mexico–United States border in an attempt to reduce illegal immigration to the United States from M..."

**[duckduckgo] "What makes the Great Wall of China the only man-made object visible from space? | Science Questions with Surprising Answers"**
  Type: web | Cred: estimated 0.42400000000000004
  NLI (nli_deberta): opposing (0.9927)
  Verdict contribution: opposing (weight: 0.4209)
  Snippet: "December 11, 2012 - The Great Wall of China is not visible to the naked eye from space, even in low-earth orbit, according to NASA. Even though the wa..."

**[duckduckgo] "Is China's Great Wall Visible from Space? | Scientific American"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9702)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "February 20, 2024 - Both are false, say astronauts and remote-sensing specialists. Although the Great Wall spans some 4,500 miles (7,200 kilometers), ..."

**[duckduckgo] "Fact or Fiction: The Great Wall of China Is Visible From Space"**
  Type: web | Cred: estimated 0.269
  NLI (nli_deberta): neutral (0.9492)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "January 24, 2023 - And thus, the presumption that the Great Wall of China is the only man-made creation that can be seen from space originated. ... Fi..."

**[duckduckgo] "Can you see the Great Wall of China from space? | BBC Sky at Night Magazine"**
  Type: web | Cred: estimated 0.282
  NLI (nli_deberta): opposing (0.7319)
  Verdict contribution: opposing (weight: 0.2064)
  Snippet: "October 1, 2024 - For example, there are plenty of strange things astronomers used to believe about the Moon. One space-based myth that we all have he..."

**[duckduckgo] "Is it true that The Great Wall of China is the only man-made structure visible from space, or is that a myth? - Quora"**
  Type: web | Cred: estimated 0.487
  NLI (nli_deberta): neutral (0.6284)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Answer (1 of 2): The Great Wall of China is itself NOT very visible from space; it’s certainly long enough, but it’s no wider on average than a fairly..."

**[duckduckgo] "Fact Check: Is The Great Wall Of China Visible From Space? | Times Now"**
  Type: web | Cred: estimated 0.307
  NLI (nli_deberta): opposing (0.998)
  Verdict contribution: opposing (weight: 0.3064)
  Snippet: "August 17, 2024 - While the Great Wall of China is not visible from space, plenty of other human-made structures can be seen from orbit. The Pyramids ..."

**[duckduckgo] "Is the Great Wall of China Really Visible from Space? | Live Science"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.9619)
  Verdict contribution: opposing (weight: 0.8176)
  Snippet: "September 12, 2012 - The Great Wall of China has been touted as the only manmade object visible from Space since 1932, yet the notion is easily debunk..."

**[duckduckgo] "Great Wall of China is visible from space: Fact or myth? | - The Times of India"**
  Type: web | Cred: estimated 0.554
  NLI (nli_deberta): neutral (0.8394)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "February 22, 2026 - The Great Wall is an impressive ... Wall is the only man-made structure visible from space,” you can coolly reply: “Actually, no.”..."

**[duckduckgo] "Can you see the Great Wall of China from Space?"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.1971)
  Snippet: "The Great Wall of China is the only man-made structure that can be visible from the space. Is this a rumor or a truth? Our spaceman will speak it..."

**[wikidata] "Great Wall Motor"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Chinese vehicle manufacturing company | instance of: automobile manufacturer | country: People's Republic of China | inception: 1984-00-00 | headquart..."

**[wikidata] "Great Wall of China"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "series of fortifications built along the historical border of China | instance of: tourist attraction | country: People's Republic of China | located ..."

### Verdict computation
  Supporting weight: 0.1971
  Opposing weight: 2.9256
  Support ratio: 0.0631
  Confidence: 0.8738
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 10

  Top supporting:
    - Can you see the Great Wall of China from Space? (weight: 0.1971)
  Top opposing:
    - Is the Great Wall of China Really Visible from Space? | Live Science (weight: 0.8176)
    - Artificial structures visible from space (weight: 0.6993)
    - Is the Great Wall of China Visible from the Moon? (weight: 0.475)
    - What makes the Great Wall of China the only man-made object visible from space? | Science Questions with Surprising Answers (weight: 0.4209)
    - Fact Check: Is The Great Wall Of China Visible From Space? | Times Now (weight: 0.3064)
