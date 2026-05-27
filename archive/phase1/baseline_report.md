# Baseline Test Report
Generated: 2026-05-25 16:30:57
Models: DeBERTa-v3-base-mnli-fever-anli (NLI) + keyword/POS (claim type) + MiniLM (relevance)
Relevance threshold: 0.35

## Summary: 29/36 correct

| Category | Score |
|----------|-------|
| factual_true | 6/7 FAIL |
| factual_false | 6/11 FAIL |
| opinion | 7/7 PASS |
| contested | 7/7 PASS |
| current_event | 3/4 FAIL |

| Claim | Expected | Actual | Domain | Match |
|-------|----------|--------|--------|-------|
| climate change is real | strongly supported | strongly supported | scientific | YES |
| evolution is real | strongly supported | strongly supported | scientific | YES |
| water boils at 100 degrees celsius | strongly supported | contested | scientific | **NO** |
| the speed of light is constant | strongly supported | likely supported | scientific | YES |
| the earth is flat | strongly opposed | likely opposed | scientific | YES |
| vaccines cause autism | strongly opposed | strongly opposed | scientific | YES |
| the moon landing was faked | strongly opposed | likely opposed | historical | YES |
| 5G causes COVID | strongly opposed | strongly opposed | scientific | YES |
| LeBron James is the greatest basketball player of all time | opinion | sources lean supporting | general | YES |
| pineapple belongs on pizza | opinion | sources lean supporting | general | YES |
| democracy is the best form of government | opinion | sources divided | general | YES |
| sugar is worse than fat for health | contested | sources divided | scientific | YES |
| nuclear energy is safe | contested | sources lean supporting | scientific | YES |
| remote work is more productive than office work | contested | sources divided | general | YES |
| AI will replace most jobs | contested | strongly opposed | current_events | **NO** |
| the United States economy is in a recession | contested | likely supported | current_events | YES |
| violent video games cause real world violence | contested | likely opposed | scientific | YES |
| smoking causes lung cancer | strongly supported | strongly supported | scientific | YES |
| capitalism is better than socialism | opinion | sources divided | general | YES |
| we only use 10% of our brains | strongly opposed | contested | statistical | **NO** |
| social media is harmful to mental health | contested | sources lean supporting | scientific | YES |
| the Beatles are the greatest band of all time | opinion | sources lean supporting | general | YES |
| antibiotics do not work against viruses | strongly supported | likely supported | general | YES |
| goldfish have a 3 second memory | strongly opposed | likely supported | general | **NO** |
| immigration is good for the economy | contested | sources lean supporting | current_events | YES |
| the Great Wall of China is visible from space | strongly opposed | likely opposed | historical | YES |
| cats are better pets than dogs | opinion | sources divided | general | YES |
| organic food is healthier than conventional food | contested | sources lean supporting | scientific | YES |
| MSG is dangerous to consume | strongly opposed | sources lean opposing | general | **NO** |
| humans share about 98% of DNA with chimpanzees | strongly supported | strongly supported | statistical | YES |
| China has the world's largest economy | contested | likely opposed | current_events | YES |
| eating carrots improves your eyesight | strongly opposed | strongly supported | general | **NO** |
| college education is worth the cost | opinion | sources lean supporting | statistical | YES |
| inflation in the United States is under control | contested | likely supported | current_events | YES |
| the Amazon rainforest produces about 20% of the world's oxygen | strongly opposed | contested | statistical | **NO** |
| the Great Wall of China is the only man-made structure visible from space | strongly opposed | strongly opposed | historical | YES |

## Fact-Check Source Diagnostics
Total FC sources: 66
  Bypassed (rating parsed): 36
  Skipped (bypass failed): 30
  Enriched (article fetched): 65/66

Publishers:
  USA Today: 12 sources
  FactCheck.org: 10 sources
  PolitiFact: 10 sources
  AAP: 6 sources
  Snopes: 6 sources
  AFP Fact Check: 5 sources
  Full Fact: 4 sources
  Snopes.com: 3 sources
  AP News: 2 sources
  VOA: 2 sources
  FACTLY: 1 sources
  Lead Stories: 1 sources
  The New York Times: 1 sources
  The Washington Post: 1 sources
  : 1 sources
  The Conversation: 1 sources

Skipped FC sources (bypass failed):
  [FactCheck.org] "No, Climate Change Isn't 'Made Up'"
    Rating: False
    Claim reviewed: Viral posts claim that climate change is a "made-up catastrophe."
    Enriched: True
  [AP News] "Climate crisis is real and stems from human activity"
    Rating: Despite record high temperatures throughout the United States in June, social media users took to Facebook on Thursday to spread misinformation about the planet’s warming temperatures and human beings' role in climate change
    Claim reviewed: CO2 is not a problem. The Earth has more than enough land and ocean plant life t
    Enriched: True
  [FactCheck.org] "Smith's Error-Filled Climate Op-Ed"
    Rating: False
    Claim reviewed: Wrote that climate scientists have predicted “global temperatures would increase
    Enriched: True
  [AAP] "Cherry-picked ocean data does not prove climate change is a "
    Rating: Misleading. The claim is based on cherry-picked data and evidence shows global warming is real.
    Claim reviewed: An ocean temperature decrease between 2013-2022 proves global warming is a hoax.
    Enriched: True
  [AAP] "No, NASA didn't admit the earth is flat"
    Rating: False. The post misinterprets common aeronautical flight calculation methodologies.
    Claim reviewed: NASA has admitted the earth is flat in several documents.
    Enriched: True
  [Full Fact] "The Earth is not flat – Full Fact"
    Rating: There are many man-made satellites currently in orbit, playing an essential role in common electronic devices.
    Claim reviewed: Satellites are fake.
    Enriched: True
  [VOA] "Deadly Disinfo: How the Flat Earth Conspiracy Doomed an Amat"
    Rating: Tragically False
    Claim reviewed: “I don’t want to take anyone else’s word for it. I don’t know if the Earth is fl
    Enriched: True
  [FactCheck.org] "RFK Jr. Misleads on Autism Prevalence, Causes"
    Rating: Distorts the facts
    Claim reviewed: At most 25% of the increase in autism prevalence “can be attributed to better re
    Enriched: True
  [FactCheck.org] "RFK Jr. Cites Flawed Paper Claiming Link Between Vaccines an"
    Rating: Flawed Paper
    Claim reviewed: “There’s a study that came out last week of 47,000 9-year-olds in the Medicaid s
    Enriched: True
  [FactCheck.org] "FactChecking RFK Jr.'s Other Health Claims During HHS ..."
    Rating: False
    Claim reviewed: “We brought that petition after CDC recommended COVID vaccine without any scient
    Enriched: True
  [VOA] "Former Russian Space Chief Repeats False Moon Landing ..."
    Rating: False
    Claim reviewed: "No proof US landed on moon"
    Enriched: True
  [Full Fact] "Buzz Aldrin didn't 'admit' he never went to the Moon – Full "
    Rating: In the clip, Mr Aldrin appears to be explaining why astronauts haven’t returned to the Moon in decades, not that they never went at all. In other interviews, Mr Aldrin clearly claims he went to the Moon.
    Claim reviewed: Buzz Aldrin admitted the Moon landings were faked in an interview.
    Enriched: True
  [PolitiFact] "No, Wikileaks didn’t release evidence that the moon landing "
    Rating: False
    Claim reviewed: “Wikileaks releases moon landing cut scenes filmed in the Nevada desert.”
    Enriched: True
  [FACTLY] "WikiLeaks has not released the footage of NASA’s moon landin"
    Rating: FALSE
    Claim reviewed: WikiLeaks released the footage of moon landing scenes filmed in the Nevada Deser
    Enriched: True
  [Full Fact] "These claims about the new coronavirus and 5G are unfounded "
    Rating: While it is true that China has over 100,000 towers, it is unclear if it was the first place to pass this number.
    Claim reviewed: China was the first place to have over 100,000 5G towers.
    Enriched: True
  [Full Fact] "The EG.5 variant of Covid-19 has nothing to do with 5G – Ful"
    Rating: This is not true. Covid-19 is caused by the SARS-CoV-2 virus. The 5G network uses radio waves that do not harm people’s health.
    Claim reviewed: The EG.5 variant of Covid-19 is a new 5G virus.
    Enriched: True
  [AFP Fact Check] "Hoax linking Covid-19 to bacteria and 5G mobile technology ."
    Rating: False
    Claim reviewed: Covid-19 is bacterial, not viral
    Enriched: True
  [Lead Stories] "Fact Check: 5G Wuhan Rollout Did NOT Cause Coronavirus ..."
    Rating: Not Connected
    Claim reviewed: 5G Wuhan Rollout Caused COVID-19 Pandemic Or Facilitate Global Spread
    Enriched: True
  [Snopes] "Did Michael Jordan Call LeBron James the Greatest Basketball"
    Rating: False
    Claim reviewed: Michael Jordan said that LeBron James was the greatest basketball player of all 
    Enriched: True
  [FactCheck.org] "The Facts on Media Violence"
    Rating: Learn What Research Shows
    Claim reviewed: "I’m hearing more and more people say the level of violence on video games is re
    Enriched: True
  [USA Today] "Fact check: Studies refute attempts to link video games, sho"
    Rating: False
    Claim reviewed: Post implies school shootings are linked to violent video games
    Enriched: True
  [PolitiFact] "Can marijuana smoking cause lung cancer?"
    Rating: Half True
    Claim reviewed: "Despite decades of marijuana being used for smoking in the United States, there
    Enriched: True
  [Snopes] "Does Marijuana Contain More Tar Than Cigarettes?"
    Rating: Mixture
    Claim reviewed: Marijuana cigarettes deposit four times more tar into smokers' lungs than tobacc
    Enriched: True
  [Snopes.com] "Image Accurately Depicts a 1 Cubic Millimeter Sample of a Hu"
    Rating: True
    Claim reviewed: A high-quality visual rendering accurately depicts a 1 cubic millimeter sample o
    Enriched: True
  [The Washington Post] "Analysis | President Trump's claim that low-skilled immigrat"
    Rating: Three Pinocchios
    Claim reviewed: “For decades, the United States was operated and has operated a very low-skill i
    Enriched: True
  [PolitiFact] "Do immigrants cost U.S. taxpayers $300 billion annually?"
    Rating: Half True
    Claim reviewed: "Current immigration policy imposes as much as $300 billion annually in net fisc
    Enriched: True
  [AAP] "Brain damage link to MSG a salty dose of misinformation"
    Rating: False. Food authorities and major studies say MSG is safe to consume.
    Claim reviewed: MSG kills brain cells and damages the nervous system.
    Enriched: True
  [PolitiFact] "President Donald Trump says the US has ‘no inflation.’ By 2 "
    Rating: False
    Claim reviewed: The U.S. currently has “no inflation.”
    Enriched: True
  [PolitiFact] "Has inflation eased under Trump? It depends on the measure"
    Rating: Half True
    Claim reviewed: "Overall, the inflation since President Trump” took office “has come down."
    Enriched: True
  [FactCheck.org] "FactChecking Biden on Inflation, Other Claims"
    Rating: False
    Claim reviewed: "It [inflation] was 9% when I came to office, 9%."
    Enriched: True

---
## 1. "climate change is real"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 39 total
  - google_factcheck: 10
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 1
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 39 -> 34 (dropped 5)
Dropped sources:
  - [academic] "Developing IoT Sustainable Real-Time Monitoring Devices for Food Supply Chain Systems Based on Climate Change Using Circular Intuitionistic Fuzzy Set" (relevance: 0.1399, reason: relevance_0.140_below_0.35)
  - [academic] "EcoGuard: Uniting IoT and AI to Secure Forests and Combat Climate Change in Real-Time" (relevance: 0.1993, reason: relevance_0.199_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.151, reason: relevance_0.151_below_0.35)
  - [knowledge_graph] "real property" (relevance: 0.1593, reason: relevance_0.159_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.2002, reason: relevance_0.200_below_0.35)

### Dedup: 34 -> 34 (dropped 0)

### Analyzed sources (34 total)

**[google_factcheck] "No, Climate Change Isn't 'Made Up'"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.724 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Quick Take
Popular social media posts claim that climate change is a “made-up catastrophe,” despite a large body of evidence that supports the scienti..."

**[google_factcheck] "Climate crisis is real and stems from human activity"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: AP News | Enriched: True | Extract score: 1.000 | Rating: Despite record high temperatures throughout the United States in June, social media users took to Facebook on Thursday to spread misinformation about the planet’s warming temperatures and human beings' role in climate change
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Climate crisis is real and stems from human activity
CLAIM: CO2 is not a problem. The Earth has more than enough land and ocean plant life to metaboli..."

**[google_factcheck] "Extensive evidence shows Earth is warming | Fact check"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.743 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.45)
  Snippet: "Temperature and sea ice data consistent with human-driven climate change Fact check
The claim: Sea ice and temperature data show climate change is a h..."

**[google_factcheck] "Smith's Error-Filled Climate Op-Ed"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.978 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In an op-ed for Fox News, Rep. Lamar Smith, the chairman of the House science committee, made a host of false and misleading claims about climate chan..."

**[google_factcheck] "Cherry-picked ocean data does not prove climate change is a hoax"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: AAP | Enriched: True | Extract score: 0.700 | Rating: Misleading. The claim is based on cherry-picked data and evidence shows global warming is real.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "WHAT WAS CLAIMED
An ocean temperature decrease between 2013-2022 proves global warming is a hoax. OUR VERDICT
Misleading. The claim is based on cherry..."

**[google_factcheck] "Trump Wrong on Climate Change, Again"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.949 | Rating: Distorts the Facts
  NLI (factcheck_rating_bypass): opposing (0.75)
  Verdict contribution: opposing (weight: 0.7125)
  Snippet: "In two recent interviews, President Donald Trump said he is not convinced that climate change is due to human activity, and he suggested that any chan..."

**[google_factcheck] "2008 quote does not reflect scientific consensus: Humans do cause ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.932 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "During the U.N’s global summit on climate change in Scotland, Facebook users shared a viral image claiming that global warming occurs naturally, and t..."

**[google_factcheck] "Fact check: Global warming caused by human activity, not solar ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.758 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Fact check: Global warming caused by human activity, not solar winds or weakened magnetic field
The claim: Global warming is occurring because of sola..."

**[google_factcheck] "'Unequivocal' Evidence that Humans Cause Climate Change ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.787 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.855)
  Snippet: "SciCheck Digest
There is “unequivocal” evidence that humans are causing global warming, the U.N. climate change panel has said. But viral posts revive..."

**[google_factcheck] "Fact check: Scientific consensus says humans are dominant cause ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.824 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.45)
  Snippet: "Climate skeptics don’t believe climate change is caused by humans, despite overwhelming scientific evidence to support the conclusion. Some don’t ackn..."

**[wikipedia] "Climate change denial"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.8506)
  Verdict contribution: supporting (weight: 0.723)
  Snippet: "The scientific consensus is that they cannot explain the observed warming trend. Playing up flawed studies
In 2007, the Heartland Institute published ..."

**[wikipedia] "Climate change policy of the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9438)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A September 2016 study from Lawrence Berkeley National Laboratory analyzed a set of definite and proposed climate change policies for the United State..."

**[wikipedia] "Climate change in Florida"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.5776)
  Verdict contribution: supporting (weight: 0.491)
  Snippet: "A 2018 report by the Union of Concerned Scientists (UCS) found that by the year 2100, more than 1 million Florida homes would be at risk of flooding a..."

**[wikipedia] "Psychology of climate change denial"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8262)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "An article published by National Center for Science Education referred to "implicit" denial:
Climate change denial is most conspicuous when it is expl..."

**[wikipedia] "Climate change feedbacks"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8921)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "However, it is in fact a positive feedback in polar regions where it strongly contributed to polar amplified warming, one of the biggest consequences ..."

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

**[duckduckgo] "Climate change in Israel"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.7545)
  Snippet: "Israel, like many other countries in the Middle East and North Africa, experiences adverse effects from climate change. Annual and mean temperatures a..."

**[duckduckgo] "What is climate change? A really simple guide"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.8487)
  Snippet: "A really simple guide to climate change
Human activities are causing world temperatures to rise, posing serious threats to people and nature. Things a..."

**[duckduckgo] "Scientists Say Climate Change Is Real and Human-Caused"**
  Type: web | Cred: estimated 0.45899999999999996
  NLI (nli_deberta): supporting (0.9922)
  Verdict contribution: supporting (weight: 0.4554)
  Snippet: "The bank says the reduction could slow the rate of climate change, and save lives. Scientists say last year was among the hottest years ever on planet..."

**[duckduckgo] "NASA is a global leader in studying Earth’s changing climate."**
  Type: web | Cred: estimated 0.518
  NLI (nli_deberta): supporting (0.9937)
  Verdict contribution: supporting (weight: 0.5147)
  Snippet: "NASA applies ingenuity and expertise gained from decades of planetary and deep-space exploration to the study of our home planet. The Earth Science Di..."

**[duckduckgo] "Seeing the Real Change due to Climate Change | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.9126)
  Verdict contribution: supporting (weight: 0.4563)
  Snippet: "To understand Climate Change we must first identify it as a real problem. This image shows the carbon dioxide level from 8,00,000 years ago to 1950. 1..."

**[duckduckgo] "Effects of Climate Change - Impacts and Examples"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.4975)
  Snippet: "Effects of climate change on the environment. From the poles to the tropics, climate change is disrupting ecosystems. Even a seemingly slight shift in..."

**[duckduckgo] "Let's look at the facts of climate change"**
  Type: web | Cred: estimated 0.40599999999999997
  NLI (nli_deberta): supporting (0.6079)
  Verdict contribution: supporting (weight: 0.2468)
  Snippet: "By Richard Grossman MD 25 August 2023
Population Matters-USA
It’s been unmistakably hot outside, but some people have different ways of dealing with w..."

**[duckduckgo] "Getting Real About Climate Change - The Allegheny Front"**
  Type: web | Cred: estimated 0.253
  NLI (nli_deberta): supporting (0.9419)
  Verdict contribution: supporting (weight: 0.2383)
  Snippet: "This week in Pittsburgh, about 1300 people are in training to become climate leaders in their communities. That means convincing other people to make ..."

**[duckduckgo] "7 Signs Climate Change Is Absolutely Real To Convince Deniers..."**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.9971)
  Verdict contribution: supporting (weight: 0.4985)
  Snippet: "7 Signs Climate Change Is Absolutely Real
Despite the overwhelming evidence that Mother Earth is having a hot flash and it's all thanks to human activ..."

**[duckduckgo] "#InquirerSeven Facts that prove climate change is real, according to..."**
  Type: web | Cred: estimated 0.462
  NLI (nli_deberta): supporting (0.9609)
  Verdict contribution: supporting (weight: 0.4439)
  Snippet: "The attendees, dubbed “climate leaders,” could then use the facts and slideshow in their own future workshops. Here are seven of the many statistics u..."

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
  Supporting weight: 11.0467
  Opposing weight: 1.995
  Support ratio: 0.847
  Confidence: 0.6941
  Verdict: **strongly supported**
  Neutral sources (no contribution): 11

  Top supporting:
    - 'Unequivocal' Evidence that Humans Cause Climate Change ... (weight: 0.855)
    - What is climate change? A really simple guide (weight: 0.8487)
    - Impacts of climate change on global agriculture accounting for adaptation (weight: 0.7961)
    - Climate change in Israel (weight: 0.7545)
    - Climate change denial (weight: 0.723)
  Top opposing:
    - 2008 quote does not reflect scientific consensus: Humans do cause ... (weight: 0.8075)
    - Trump Wrong on Climate Change, Again (weight: 0.7125)
    - Fact check: Global warming caused by human activity, not solar ... (weight: 0.475)

---
## 2. "evolution is real"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 29 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 1
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 29 -> 12 (dropped 17)
Dropped sources:
  - [encyclopedia] "Real Madrid CF" (relevance: 0.2294, reason: relevance_0.229_below_0.35)
  - [encyclopedia] "Theistic evolution" (relevance: 0.3334, reason: relevance_0.333_below_0.35)
  - [encyclopedia] "Pro Evolution Soccer" (relevance: 0.1015, reason: relevance_0.102_below_0.35)
  - [encyclopedia] "Speculative evolution" (relevance: 0.2859, reason: relevance_0.286_below_0.35)
  - [academic] "Generative prediction of real-world prevalent SARS-CoV-2 mutation with in silico virus evolution" (relevance: 0.1911, reason: relevance_0.191_below_0.35)
  - [academic] "Real-time monitoring of SARS-CoV-2 evolution during the COVID-19 pandemic." (relevance: 0.2529, reason: relevance_0.253_below_0.35)
  - [academic] "Mitochondrial Genetic Mutations in the Pale Grass Blue Butterfly: Possible DNA Damage via the Fukushima Nuclear Accident and Real-Time Molecular Evolution" (relevance: 0.1169, reason: relevance_0.117_below_0.35)
  - [academic] "Real-time spatial evolution of the fMRI response to photobiomodulation in the healthy human brain" (relevance: 0.2711, reason: relevance_0.271_below_0.35)
  - [academic] "Evolution of Potentially Actionable Genomic Alterations in Advanced Prostate Cancer: A Real-World Analysis of Serial Circulating Tumor DNA Testing" (relevance: 0.0864, reason: relevance_0.086_below_0.35)
  - [academic] "Metabolic evolution and bottleneck insights into simultaneous autotroph-heterotroph anammox system for real municipal wastewater nitrogen removal." (relevance: 0.0604, reason: relevance_0.060_below_0.35)
  - [academic] "A zinc metal complex as an NIR emissive probe for real-time dynamics and in vivo embryogenic evolution of lysosomes using super-resolution microscopy" (relevance: 0.0972, reason: relevance_0.097_below_0.35)
  - [academic] "Host-Parasite Co-Evolution in Real-Time: Changes in Honey Bee Resistance Mechanisms and Mite Reproductive Strategies" (relevance: 0.2105, reason: relevance_0.211_below_0.35)
  - [web] "Observable Evolution Today: Real-World Evidence of Species ..." (relevance: 0.3199, reason: relevance_0.320_below_0.35)
  - [knowledge_graph] "Evolution" (relevance: 0.1287, reason: relevance_0.129_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.2296, reason: relevance_0.230_below_0.35)
  - [knowledge_graph] "real property" (relevance: 0.1334, reason: relevance_0.133_below_0.35)
  - [knowledge_graph] "Real" (relevance: 0.3195, reason: relevance_0.320_below_0.35)

### Dedup: 12 -> 11 (dropped 1)

### Analyzed sources (11 total)

**[wikipedia] "Evolution"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.9727)
  Verdict contribution: supporting (weight: 0.9241)
  Snippet: "Evolutionary biologists have continued to study various aspects of evolution by forming and testing hypotheses as well as constructing theories based ..."

**[duckduckgo] "Evolution as fact and theory - Wikipedia"**
  Type: web | Cred: estimated 0.537
  NLI (nli_deberta): supporting (0.9395)
  Verdict contribution: supporting (weight: 0.5045)
  Snippet: "Evidence for evolution continues to be accumulated and tested. The scientific literature includes statements by evolutionary biologists and philosophe..."

**[duckduckgo] "Evolutionism (Religion)"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.7519)
  Snippet: "Evolutionism is a term used (often derogatorily) to denote the theory of evolution. Its exact meaning has changed over time as the study of evolution ..."

**[duckduckgo] "What Scientists Really Say About Evolution"**
  Type: web | Cred: estimated 0.236
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.2355)
  Snippet: "This connection is not poetic fancy or philosophical conjecture. It is a conclusion supported by mountains of scientific evidence, rigorously tested a..."

**[duckduckgo] "If evolution is real, then why isn’t it happening now? An ..."**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): supporting (0.5195)
  Verdict contribution: supporting (weight: 0.4935)
  Snippet: "Curious Kids is a series for children of all ages. If you have a question you’d like an expert to answer, send it to CuriousKidsUS@theconversation.com..."

**[duckduckgo] "Human Evolution Evidence | The Smithsonian Institution's ..."**
  Type: web | Cred: estimated 0.445
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.4443)
  Snippet: "Human Evolution Evidence
Full Image
Evidence of Evolution
Scientists have discovered a wealth of evidence concerning human evolution, and this evidenc..."

**[duckduckgo] "Is Human Evolution Proven? What the Evidence Shows"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.4018)
  Snippet: "Human evolution is supported by converging evidence from fossils, genetics, comparative anatomy, and direct observation of evolutionary change in livi..."

**[duckduckgo] "Is evolution a fact or a theory? : r/evolution - Reddit"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.594)
  Snippet: "Evolution of organisms is an observed fact, and not just in the fossil record. Evolutionary trees can be inferred from genetic secuqences, and real ti..."

**[duckduckgo] "If evolution is real, why are there still monkeys? Scientists ... - MSN"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.8965)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Daily Mail has asked some of the leading evolution experts why, if humans evolved out of primates, do monkeys and apes still exist today?..."

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
  Supporting weight: 4.3497
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **strongly supported**
  Neutral sources (no contribution): 3

  Top supporting:
    - Evolution (weight: 0.9241)
    - Evolutionism (Religion) (weight: 0.7519)
    - Is evolution a fact or a theory? : r/evolution - Reddit (weight: 0.594)
    - Evolution as fact and theory - Wikipedia (weight: 0.5045)
    - If evolution is real, then why isn’t it happening now? An ... (weight: 0.4935)

---
## 3. "water boils at 100 degrees celsius"
Category: factual_true
Expected: strongly supported
Actual: contested (**NO - MISMATCH**)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 27 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 3
  - duckduckgo: 10
  - wikidata: 2

### Relevance filter: 27 -> 14 (dropped 13)
Dropped sources:
  - [encyclopedia] "Sentence (linguistics)" (relevance: 0.1114, reason: relevance_0.111_below_0.35)
  - [encyclopedia] "Anders Celsius" (relevance: 0.1492, reason: relevance_0.149_below_0.35)
  - [academic] "Estimation of oil recovery due to wettability changes in carbonate reservoirs" (relevance: 0.0931, reason: relevance_0.093_below_0.35)
  - [academic] "Dragonfly mission window assembly design" (relevance: 0.0789, reason: relevance_0.079_below_0.35)
  - [academic] "The effect of some factors, hot water soaking and growth media, on breaking the dormancy of Pinus pinea seeds." (relevance: 0.1342, reason: relevance_0.134_below_0.35)
  - [academic] "IMPLEMENTATION OF THE RESONANCE METHOD TO MEASURE THE SPEED OF SOUND USING PVC PIPES AND SMARTPHONE" (relevance: 0.1514, reason: relevance_0.151_below_0.35)
  - [academic] "Kajian Fisis Optimalisasi Daya Bateray Lithium dalam Pengaruh Deformasi" (relevance: 0.0886, reason: relevance_0.089_below_0.35)
  - [academic] "The Effect of Anthropogenic Sources on the Total Numbers of Rotifera in Shatt Al-Hillah" (relevance: 0.205, reason: relevance_0.205_below_0.35)
  - [academic] "Pool boiling simulation of two nanofluids at multi concentrations in enclosure with different shapes of fins" (relevance: 0.3427, reason: relevance_0.343_below_0.35)
  - [academic] "Industrial decarbonization via hydrogen: A critical and systematic review of developments, socio-technical systems and policy options" (relevance: 0.028, reason: relevance_0.028_below_0.35)
  - [academic] "Mineral commodity summaries 2022" (relevance: -0.0468, reason: relevance_-0.047_below_0.35)
  - [web] "Celsius - Wikipedia" (relevance: 0.3223, reason: relevance_0.322_below_0.35)
  - [knowledge_graph] "water boils when angry warrior is immersed in it" (relevance: 0.1969, reason: relevance_0.197_below_0.35)

### Dedup: 14 -> 14 (dropped 0)

### Analyzed sources (14 total)

**[wikipedia] "Celsius"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.4397)
  Verdict contribution: supporting (weight: 0.3518)
  Snippet: "In his paper Observations of two persistent degrees on a thermometer, he recounted his experiments showing that the melting point of ice is essentiall..."

**[wikipedia] "Fahrenheit"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.6899)
  Verdict contribution: opposing (weight: 0.5519)
  Snippet: "He then re-calibrated his scale using the melting point of ice and normal human body temperature (which were at 30 and 90 degrees); he adjusted the sc..."

**[wikipedia] "Nucleate boiling"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): opposing (0.9722)
  Verdict contribution: opposing (weight: 0.6805)
  Snippet: "It also occurs in water boilers where water is rapidly heated.
[edit]Two different regimes may be distinguished in the nucleate boiling range. When th..."

**[semantic_scholar] "Radiation in the coffee cup"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9897)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It is commonly assumed that radiative heat transfer only plays a relevant role in situations involving temperatures of several hundred degrees Celsius..."

**[duckduckgo] "Solved: water boils at 100 degrees Celsius [Others]"**
  Type: web | Cred: estimated 0.27999999999999997
  NLI (nli_deberta): supporting (0.9863)
  Verdict contribution: supporting (weight: 0.2762)
  Snippet: "water boils at 100 degrees Celsius Gauth AI Solution I'm glad to assist you with your question. However, it seems like you haven't provided a specific..."

**[duckduckgo] "Celsius to Fahrenheit (°C to °F) Conversion"**
  Type: web | Cred: estimated 0.33399999999999996
  NLI (nli_deberta): supporting (0.8574)
  Verdict contribution: supporting (weight: 0.2864)
  Snippet: "Celsius or centigrade is a unit of temperature. The freezing/melting point of water is about zero degrees celsius (0 °C) at a pressure of 1 atmosphere..."

**[duckduckgo] "Why Water Boils at 100 Degrees. The Science Behind Why... | Medium"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.2956)
  Snippet: "Have you ever wondered why water boils at 100 degrees Celsius (212 degrees Fahrenheit) at sea level? This seemingly simple phenomenon is actually a re..."

**[duckduckgo] "logic - Is "water boils at 100 degrees Celsius" both a sufficiency and..."**
  Type: web | Cred: estimated 0.371
  NLI (nli_deberta): opposing (0.9106)
  Verdict contribution: opposing (weight: 0.3378)
  Snippet: "When you boil water on a mountain top, where air pressure is less than at sea level, you can boil water at a temperature less than 100 degrees Celsius..."

**[duckduckgo] "What happens to water at 100 degrees Celsius? - Answers"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): supporting (0.9976)
  Verdict contribution: supporting (weight: 0.417)
  Snippet: "The temperature in Celsius at which water boils is 100 degrees. The boiling point of water is 100 degrees Celsius and the melting point of water is 0 ..."

**[duckduckgo] "Water boils at 100 degree Celsius. | UsingEnglish.com ESL Forum"**
  Type: web | Cred: estimated 0.41600000000000004
  NLI (nli_deberta): supporting (0.9688)
  Verdict contribution: supporting (weight: 0.403)
  Snippet: ""at 100 degrees Celsius". No hyphen is required and you need the plural noun.We can't say that 'Water boils at 100-degree Celcius' is a universal or g..."

**[duckduckgo] "Celsius to Fahrenheit conversion : ºC to ºF calculator"**
  Type: web | Cred: estimated 0.29100000000000004
  NLI (nli_deberta): supporting (0.9712)
  Verdict contribution: supporting (weight: 0.2826)
  Snippet: "Simple, quick °C to °F conversion
Celsius to Fahrenheit conversion is probably the most confusing conversion there is, but a simple °C to °F conversio..."

**[duckduckgo] "Describe the condition in which water can be boiled at... - Brainly.in"**
  Type: web | Cred: estimated 0.42000000000000004
  NLI (nli_deberta): supporting (0.9873)
  Verdict contribution: supporting (weight: 0.4147)
  Snippet: "Water boils at 100 degrees Celsius under normal atmospheric pressure at sea level. However, there are conditions under which water can be boiled at a ..."

**[duckduckgo] "water boils or will boil? | WordReference Forums"**
  Type: web | Cred: estimated 0.44000000000000006
  NLI (nli_deberta): opposing (0.6782)
  Verdict contribution: opposing (weight: 0.2984)
  Snippet: ""People often say that water boils at 100 degrees Celsius, but that is only true at sea-level. If you take this kettle to the top of that mountain, th..."

**[wikidata] "Water boils at 100 degree Celsius and has an angle"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "scholarly article | instance of: scholarly article..."

### Verdict computation
  Supporting weight: 2.7272
  Opposing weight: 1.8687
  Support ratio: 0.5934
  Confidence: 0.1868
  Verdict: **contested**
  Neutral sources (no contribution): 2

  Top supporting:
    - What happens to water at 100 degrees Celsius? - Answers (weight: 0.417)
    - Describe the condition in which water can be boiled at... - Brainly.in (weight: 0.4147)
    - Water boils at 100 degree Celsius. | UsingEnglish.com ESL Forum (weight: 0.403)
    - Celsius (weight: 0.3518)
    - Why Water Boils at 100 Degrees. The Science Behind Why... | Medium (weight: 0.2956)
  Top opposing:
    - Nucleate boiling (weight: 0.6805)
    - Fahrenheit (weight: 0.5519)
    - logic - Is "water boils at 100 degrees Celsius" both a sufficiency and... (weight: 0.3378)
    - water boils or will boil? | WordReference Forums (weight: 0.2984)

---
## 4. "the speed of light is constant"
Category: factual_true
Expected: strongly supported
Actual: likely supported (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 38 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 7
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 38 -> 26 (dropped 12)
Dropped sources:
  - [academic] "The apparent eta Carinae’s long-term evolution and the critical role played by the strengthening of P Cygni absorption lines" (relevance: -0.0427, reason: relevance_-0.043_below_0.35)
  - [academic] "Gravity current propagating against constant and pulsating counter flows" (relevance: 0.1894, reason: relevance_0.189_below_0.35)
  - [academic] "First light observations of the solar wind in the outer corona with the Metis coronagraph" (relevance: 0.1348, reason: relevance_0.135_below_0.35)
  - [academic] "Model-independent confirmation of a constant speed of light over cosmological distances" (relevance: 0.3152, reason: relevance_0.315_below_0.35)
  - [knowledge_graph] "Speed" (relevance: 0.2938, reason: relevance_0.294_below_0.35)
  - [knowledge_graph] "Speed" (relevance: 0.1062, reason: relevance_0.106_below_0.35)
  - [knowledge_graph] "visible spectrum" (relevance: 0.1425, reason: relevance_0.143_below_0.35)
  - [knowledge_graph] "lighthouse" (relevance: 0.1962, reason: relevance_0.196_below_0.35)
  - [knowledge_graph] "Light" (relevance: 0.2397, reason: relevance_0.240_below_0.35)
  - [knowledge_graph] "Constant" (relevance: 0.2768, reason: relevance_0.277_below_0.35)
  - [knowledge_graph] "Constant" (relevance: 0.2658, reason: relevance_0.266_below_0.35)
  - [knowledge_graph] "Constanța" (relevance: 0.3208, reason: relevance_0.321_below_0.35)

### Dedup: 26 -> 24 (dropped 2)

### Analyzed sources (24 total)

**[wikipedia] "Speed of light"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): opposing (0.959)
  Verdict contribution: opposing (weight: 0.911)
  Snippet: "Experiments such as the Kennedy–Thorndike experiment and the Ives–Stilwell experiment have shown this postulate to match experimental observations. Th..."

**[wikipedia] "Variable speed of light"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.9746)
  Verdict contribution: opposing (weight: 0.7797)
  Snippet: "Variable speed of light
A variable speed of light (VSL) is a feature of a family of hypotheses stating that the speed of light may in some way not be ..."

**[wikipedia] "Physical constant"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.6616)
  Verdict contribution: supporting (weight: 0.5293)
  Snippet: "It is distinct from a mathematical constant, which has a fixed numerical value, but does not directly involve any physical measurement. There are many..."

**[wikipedia] "Formulations of special relativity"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.6538)
  Verdict contribution: supporting (weight: 0.523)
  Snippet: "Others differ in their approach to the geometry of spacetime and the linear transformations between frames of reference. Einstein's two postulates
[ed..."

**[wikipedia] "Special relativity"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.9565)
  Verdict contribution: supporting (weight: 0.813)
  Snippet: "This changed Newton's mechanics situations involving all motions, especially velocities close to that of light: 18 (known as relativistic velocities)...."

**[semantic_scholar] "The Speed of Light in Vacuum is not Constant in Any Circumstances"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.4834)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Is the speed of vacuum light constant under any circumstances? Based on dualism and its derivative theory, this paper makes an in-depth analysis of th..."

**[open_alex] "The Speed of Light Is Not Constant in Basic Big Bang Theory"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9888)
  Verdict contribution: opposing (weight: 0.5438)
  Snippet: "Starting from the basic assumptions and equations of Big Bang theory, we present a simple mathematical proof that this theory implies a varying (decre..."

**[semantic_scholar] "An accurate analysis of the Michelson‐Morley experiment shows that the speed of light is not a constant relative to a moving frame"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.9707)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This paper shows how the miscalculated result of an experiment caused the birth of the theory of relativity. It reveals the error made by Michelson in..."

**[semantic_scholar] "QUANTIZATION OF THE GRAVITATIONAL FIELD. THEORETICAL AND EXPERIMENTAL SUBSTANTIATION OF THE GRAVITATIONAL-ELECTROMAGNETIC RESONANCE. THE PHYSICAL NATURE OF THE QUANTUM OF THE GRAVITATIONAL FIELD.WHY THE SPEED OF LIGHT IN VACUUM IS CONSTANT"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.6162)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It is shown that gravitating objects that are at rest, or move without acceleration, create a standing gravitational wave in space. The length of this..."

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

**[open_alex] "Dilaton-induced variations in Planck constant and speed of light: An alternative to dark energy"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.9854)
  Verdict contribution: opposing (weight: 0.542)
  Snippet: "We reveal a novel aspect of scale-invariant actions that allow matter to couple with a dilaton field: The dynamics of the dilaton can induce variation..."

**[duckduckgo] "Speed of light - Wikipedia"**
  Type: web | Cred: estimated 0.537
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.5344)
  Snippet: "The speed of light in vacuum, often called simply the speed of light and commonly denoted c, is a universal physical constant exactly equal to 299 792..."

**[duckduckgo] "Speed of light | Definition, Equation, Constant, & Facts | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9814)
  Verdict contribution: supporting (weight: 0.8342)
  Snippet: "speed of light
speed of light, speed at which light waves propagate through different materials. In particular, the value for the speed of light in a ..."

**[duckduckgo] "Why The Speed Of Light Is Constant Deep Dive"**
  Type: web | Cred: estimated 0.236
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.2339)
  Snippet: "For centuries, light has been more than just illumination. It has been a symbol of knowledge, a metaphor for truth, and a mystery that teased the mind..."

**[duckduckgo] "The Speed of Light: What Is c and Why Is It Constant?"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.9414)
  Verdict contribution: supporting (weight: 0.2824)
  Snippet: "The speed of light — c = 299,792,458 m/s exactly — is the most fundamental constant in physics. It is the speed at which all electromagnetic radiation..."

**[duckduckgo] "Speed of light: How fast light travels, explained simply and clearly"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.915)
  Verdict contribution: supporting (weight: 0.8692)
  Snippet: "As far as we can measure, it is a constant. It is the same speed for every observer in the entire universe. This constancy was first established in th..."

**[duckduckgo] "What Is the Speed of Light? - Science Notes and Projects"**
  Type: web | Cred: estimated 0.43200000000000005
  NLI (nli_deberta): supporting (0.9922)
  Verdict contribution: supporting (weight: 0.4286)
  Snippet: "The speed of light is the rate at which light travels. The speed of light in a vacuum is a constant value that is denoted by the letter c and is defin..."

**[duckduckgo] "Why is the speed of light constant? - BBC Science Focus Magazine"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9897)
  Verdict contribution: supporting (weight: 0.8412)
  Snippet: "Asked by: Alan Edgington, Ramsgate
It isn't. When it passes through some mediums, such as water, it slows down considerably. In the case of diamond, i..."

**[duckduckgo] "Physicists demonstrate the constancy of the speed of light with ..."**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.8262)
  Verdict contribution: supporting (weight: 0.7023)
  Snippet: "Any deviation from a constant speed of light must be extremely small to remain compatible with current constraints, but may become detectable at the v..."

**[duckduckgo] "Physics Explained: Here's Why The Speed of Light Is The ... - ScienceAlert"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9883)
  Verdict contribution: supporting (weight: 0.8401)
  Snippet: "The speed of light in a vacuum is 299,792,458 metres per second, a figure scientists finally agreed on in 1975 – but why settle on that figure? And wh..."

**[wikidata] "speed"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "magnitude of velocity of motion..."

### Verdict computation
  Supporting weight: 8.5323
  Opposing weight: 4.042
  Support ratio: 0.6786
  Confidence: 0.3571
  Verdict: **likely supported**
  Neutral sources (no contribution): 4

  Top supporting:
    - Speed of light: How fast light travels, explained simply and clearly (weight: 0.8692)
    - Why is the speed of light constant? - BBC Science Focus Magazine (weight: 0.8412)
    - Physics Explained: Here's Why The Speed of Light Is The ... - ScienceAlert (weight: 0.8401)
    - Speed of light | Definition, Equation, Constant, & Facts | Britannica (weight: 0.8342)
    - Special relativity (weight: 0.813)
  Top opposing:
    - Speed of light (weight: 0.911)
    - Variable speed of light (weight: 0.7797)
    - The cosmological evolution condition of the Planck constant in the varying speed of light models through adiabatic expansion (weight: 0.644)
    - Constraining a possible time-variation of the speed of light along with the fine-structure constant using strong gravitational lensing and Type Ia supernovae observations (weight: 0.6215)
    - The Speed of Light Is Not Constant in Basic Big Bang Theory (weight: 0.5438)

---
## 5. "the earth is flat"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 35 total
  - google_factcheck: 10
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 4
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 35 -> 25 (dropped 10)
Dropped sources:
  - [encyclopedia] "Flat Earth (disambiguation)" (relevance: 0.6104, reason: non_content_pattern)
  - [academic] "Rapid, robust, and automated mapping of tidal flats in China using time series Sentinel-2 images and Google Earth Engine" (relevance: 0.3224, reason: relevance_0.322_below_0.35)
  - [academic] "The Earth Is Flat and the Sun Is Not a Star: The Susceptibility of GPT-2 to Universal Adversarial Triggers" (relevance: 0.0351, reason: relevance_0.035_below_0.35)
  - [academic] "A Classification of Tidal Flat Wetland Vegetation Combining Phenological Features with Google Earth Engine" (relevance: 0.2486, reason: relevance_0.249_below_0.35)
  - [knowledge_graph] "Earth" (relevance: 0.2605, reason: relevance_0.261_below_0.35)
  - [knowledge_graph] "soil" (relevance: 0.2673, reason: relevance_0.267_below_0.35)
  - [knowledge_graph] "Earth, Wind & Fire" (relevance: 0.2054, reason: relevance_0.205_below_0.35)
  - [knowledge_graph] "apartment" (relevance: 0.0336, reason: relevance_0.034_below_0.35)
  - [knowledge_graph] "apartment building" (relevance: 0.0076, reason: relevance_0.008_below_0.35)
  - [knowledge_graph] "Flat" (relevance: 0.3034, reason: relevance_0.303_below_0.35)

### Dedup: 25 -> 24 (dropped 1)

### Analyzed sources (24 total)

**[google_factcheck] "No, NASA didn't admit the earth is flat"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: AAP | Enriched: True | Extract score: 1.000 | Rating: False. The post misinterprets common aeronautical flight calculation methodologies.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "WHAT WAS CLAIMED
NASA has admitted the earth is flat in several documents. OUR VERDICT
False. The post misinterprets common aeronautical flight calcul..."

**[google_factcheck] "The Earth is not flat – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: Full Fact | Enriched: True | Extract score: 0.945 | Rating: There are many man-made satellites currently in orbit, playing an essential role in common electronic devices.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "What was claimed
Satellites are fake. Our verdict
There are many man-made satellites currently in orbit, playing an essential role in common electroni..."

**[google_factcheck] "Deadly Disinfo: How the Flat Earth Conspiracy Doomed an Amateur ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: VOA | Enriched: True | Extract score: 0.955 | Rating: Tragically False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Why did Hughes launch himself in a rocket? As he explained it, the goal was to take a photo from space to “prove” the Earth is flat. He’d been trying ..."

**[google_factcheck] "Fact check: Gravity pulls objects toward the center of the Earth"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.915 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Fact check: Gravity allows cities on opposite sides of the world to both face 'up'
The claim: The Earth is flat because cities cannot be upside-down
F..."

**[google_factcheck] "No, navigation by 'ancients' does not show Earth is flat | Fact check"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.45)
  Snippet: "More from the Fact-Check Team: How we pick and research claims Email newsletter Facebook page
Our rating: False
Celestial navigation is a technique st..."

**[google_factcheck] "Earth isn't flat, and shooting stars fly every direction | Fact check"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.760 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Earth isn't flat, and shooting stars fly every direction Fact check
The claim: The Earth is flat because we never see shooting stars coming from the b..."

**[google_factcheck] "Pictures mislead: Ample evidence the Earth is round and sea levels ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.769 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Pictures mislead: Ample evidence the Earth is round and sea levels are rising Fact check
The claim: Pictures show the Earth is flat, and sea levels ha..."

**[google_factcheck] "Fact check: False claim laser tests prove Earth is flat"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.772 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Fact check: Laser beam tests done over water are skewed by refraction, don't prove Earth is flat
The claim: Laser tests show bodies of water are level..."

**[google_factcheck] "Fact check: False claim that timelapse photo from South Pole proves ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.964 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Fact check: False claim that timelapse photo from South Pole proves Earth is flat
The claim: Photo of solar eclipse taken at the South Pole proves Ear..."

**[wikipedia] "Flat Earth"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.793)
  Verdict contribution: opposing (weight: 0.6741)
  Snippet: "He did not admit the possibility of antipodes, which he took to mean people dwelling on the opposite side of the Earth, considering them legendary and..."

**[wikipedia] "Modern flat Earth beliefs"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9194)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Modern flat Earth beliefs
Anti-scientific beliefs in a flat Earth are promoted by a number of organizations and individuals. The claims of modern flat..."

**[wikipedia] "Myth of the flat Earth"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.8374)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Myth of the flat Earth
The myth of the flat Earth, or the flat-Earth error, is a modern historical misconception that European scholars and educated p..."

**[wikipedia] "Inventing the Flat Earth"**
  Type: encyclopedia | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.5591)
  Verdict contribution: opposing (weight: 0.3075)
  Snippet: "Inventing the Flat Earth
Author Jeffrey Burton Russell
Inventing the Flat Earth (ISBN 978-0-275-95904-3) is a 1991 book by historian Jeffrey Burton Ru..."

**[open_alex] "Mapping Tidal Flats of the Bohai and Yellow Seas Using Time Series Sentinel-2 Images and Google Earth Engine"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.8716)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Tidal flats are one of the most productive ecosystems on Earth, providing essential ecological and economical services. Because of the increasing anth..."

**[duckduckgo] "Flat Earth - Wikipedia"**
  Type: web | Cred: estimated 0.537
  NLI (nli_deberta): neutral (0.5269)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Flat Earth Flat Earth map drawn by Orlando Ferguson in 1893. The map contains several references to biblical passages as well as various supposed refu..."

**[duckduckgo] "The earth is flat"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): opposing (0.8965)
  Verdict contribution: opposing (weight: 0.6778)
  Snippet: "Flat Earth is an archaic and scientifically disproven conception of the Earth's shape as a plane or disk. Many ancient societies subscribed to a flat-..."

**[duckduckgo] "Flat Earth | Theory, Model, Meaning, & Facts | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9551)
  Verdict contribution: supporting (weight: 0.8118)
  Snippet: "flat Earth
What is the flat Earth theory? Who first believed that the Earth was flat? What are some reasons people believed the Earth was flat? How di..."

**[duckduckgo] "Why Do People Still Believe the Earth Is Flat? - ScienceInsights"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9072)
  Verdict contribution: supporting (weight: 0.3665)
  Snippet: "People believe the Earth is flat for reasons that have far less to do with geography and far more to do with psychology, identity, and distrust. The f..."

**[duckduckgo] "Is the Earth flat? - ABOUT SCIENCE"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.4551)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Is the Earth flat? The flat Earth movement represents one of the most notable examples of modern scientific denialism. Despite overwhelming scientific..."

**[duckduckgo] "Flat Earth 'theory': Why do some people think the Earth is flat?"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9126)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "These believers claim that the Earth is a flat disc, and that evidence that it is round — say, pictures taken from space — are an elaborate hoax invol..."

**[duckduckgo] "Is the Earth Flat? - Dale Black"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.9399)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A Pilot’s Perspective After 40 Years in the Air
Over the years, I’ve been asked many questions—both from the cockpit and beyond. But one, in particula..."

**[duckduckgo] "What are the main arguments presented by flat earth th..."**
  Type: web | Cred: estimated 0.325
  NLI (nli_deberta): supporting (0.8027)
  Verdict contribution: supporting (weight: 0.2609)
  Snippet: "Executive Summary Flat Earth theorists advance a set of recurring claims: the Earth is a flat plane capped by a dome-like firmament, Antarctica is an ..."

**[duckduckgo] "35 Facts About Flat Earth Myth"**
  Type: web | Cred: estimated 0.425
  NLI (nli_deberta): opposing (0.5625)
  Verdict contribution: opposing (weight: 0.2391)
  Snippet: "Is the Earth really flat? This question has puzzled many for centuries. Despite overwhelming scientific evidence supporting a spherical Earth, the fla..."

**[duckduckgo] "How Do We Know the Earth Isn’t Flat? We Asked a NASA Expert: Episode 53"**
  Type: web | Cred: verified 0.95 | Factual: very high
  NLI (nli_deberta): opposing (0.9976)
  Verdict contribution: opposing (weight: 0.9477)
  Snippet: "This was a magical revelation for the Greeks and the Egyptians, who were able to see from the motions of the stars and the way the Sun moved. They saw..."

### Verdict computation
  Supporting weight: 1.8892
  Opposing weight: 5.2211
  Support ratio: 0.2657
  Confidence: 0.4686
  Verdict: **likely opposed**
  Neutral sources (no contribution): 10

  Top supporting:
    - Flat Earth | Theory, Model, Meaning, & Facts | Britannica (weight: 0.8118)
    - No, navigation by 'ancients' does not show Earth is flat | Fact check (weight: 0.45)
    - Why Do People Still Believe the Earth Is Flat? - ScienceInsights (weight: 0.3665)
    - What are the main arguments presented by flat earth th... (weight: 0.2609)
  Top opposing:
    - How Do We Know the Earth Isn’t Flat? We Asked a NASA Expert: Episode 53 (weight: 0.9477)
    - The earth is flat (weight: 0.6778)
    - Flat Earth (weight: 0.6741)
    - Fact check: Gravity pulls objects toward the center of the Earth (weight: 0.475)
    - Earth isn't flat, and shooting stars fly every direction | Fact check (weight: 0.475)

---
## 6. "vaccines cause autism"
Category: factual_false
Expected: strongly opposed
Actual: strongly opposed (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 33 total
  - google_factcheck: 10
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 1
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 33 -> 33 (dropped 0)

### Dedup: 33 -> 23 (dropped 10)

### Analyzed sources (23 total)

**[google_factcheck] "RFK Jr. Misleads on Autism Prevalence, Causes"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.700 | Rating: Distorts the facts
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "No, but has anyone demonstrated that the rise could not be entirely due to that? No.”
Kennedy Misrepresents Decades-Old Autism Studies
In the press co..."

**[google_factcheck] "RFK Jr. Cites Flawed Paper Claiming Link Between Vaccines and ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.945 | Rating: Flawed Paper
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In his second day of confirmation hearings, Robert F. Kennedy Jr., President Donald Trump’s pick to lead the Department of Health and Human Services, ..."

**[google_factcheck] "FactChecking RFK Jr.'s Other Health Claims During HHS ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.753 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This is published peer-reviewed studies.”
Kennedy is correct that some research has shown that for certain vaccines and for specific aspects of the im..."

**[wikipedia] "Vaccines and autism"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9043)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The scientist Peter Hotez researched the growth of the false claim and concluded that its spread originated with Andrew Wakefield's fraudulent 1998 pa..."

**[wikipedia] "MMR vaccine and autism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.7681)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Lancet paper was partially retracted in 2004 and fully retracted in 2010, when The Lancet's editor-in-chief Richard Horton described it as "utterl..."

**[wikipedia] "Causes of autism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.7637)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Parental concern about vaccines has led to a decreasing uptake of childhood immunizations and an increasing likelihood of measles outbreaks. The refri..."

**[wikipedia] "Thiomersal and vaccines"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.8291)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Advocates of a thiomersal-autism link also relied on indirect evidence from the scientific literature, including analogy with neurotoxic effects of ot..."

**[wikipedia] "Jenny McCarthy"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.6226)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "McCarthy has written several books about parenting and has promoted research into environmental causes and alternative medical treatments for autism. ..."

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

**[duckduckgo] "Vaccines cause autism"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): opposing (0.98)
  Verdict contribution: opposing (weight: 0.7409)
  Snippet: "Extensive investigation into vaccines and autism spectrum disorder has shown that there is no relationship between the two, causal or otherwise, and t..."

**[duckduckgo] "How Do Vaccines Cause Autism? – The Body of Research"**
  Type: web | Cred: estimated 0.268
  NLI (nli_deberta): supporting (0.5024)
  Verdict contribution: supporting (weight: 0.1346)
  Snippet: "The American Academy of Pediatrics FALSELY states that “Vaccines are not associated with autism.”
Following is a list of abstracts from 248 papers dem..."

**[duckduckgo] "Why Do Vaccines Cause Autism? - by A Midwestern Doctor"**
  Type: web | Cred: estimated 0.275
  NLI (nli_deberta): neutral (0.7412)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "His abhorrent actions deeply violated the profound trust we place in scientists, and tricked people into believing vaccines cause autism. Remarkably, ..."

**[duckduckgo] "How Do Vaccines Cause Autism? - by A Midwestern Doctor"**
  Type: web | Cred: estimated 0.275
  NLI (nli_deberta): neutral (0.8486)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Unfortunately, because so much money has been spent to engineer the societal belief that vaccines do not cause autism, anyone that asserts otherwise i..."

**[duckduckgo] "Why Have Vaccines Been Ruled Out as a Cause of Autism? |"**
  Type: web | Cred: estimated 0.41900000000000004
  NLI (nli_deberta): neutral (0.7158)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Updated 24 November 2025
Editorial note: On Wednesday, November 18, 2025, the Centers for Disease Control and Prevention . According to The New York T..."

**[duckduckgo] "Autism and Vaccines | Vaccine Safety | CDC"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): neutral (0.5786)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Key points
- The claim "vaccines do not cause autism" is not an evidence-based claim because studies have not ruled out the possibility that infant va..."

**[duckduckgo] "Vaccines are not associated with autism: an evidence-based"**
  Type: web | Cred: estimated 0.592
  NLI (nli_deberta): opposing (0.8975)
  Verdict contribution: opposing (weight: 0.5313)
  Snippet: "The cohort data revealed no relationship between vaccination and autism (OR: 0.99; 95% CI: 0.92 to 1.06) or ASD (OR: 0.91; 95% CI: 0.68 to 1.20), nor ..."

**[duckduckgo] "Vaccines Do Not Cause Autism | Johns Hopkins | Bloomberg School"**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): neutral (0.938)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It created a void, a vacuum of information in a time when about a quarter of the parents had already made up their minds that vaccines cause autism...."

### Verdict computation
  Supporting weight: 0.1346
  Opposing weight: 2.1632
  Support ratio: 0.0586
  Confidence: 0.8828
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 18

  Top supporting:
    - How Do Vaccines Cause Autism? – The Body of Research (weight: 0.1346)
  Top opposing:
    - Vaccines cause autism (weight: 0.7409)
    - Vaccines are not associated with autism: an evidence-based (weight: 0.5313)
    - Time to remember: Vaccines don't cause autism (weight: 0.499)
    - Vaccines work… and do not cause autism (weight: 0.392)

---
## 7. "the moon landing was faked"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.8)
Claim domain: historical

### Sources collected: 36 total
  - google_factcheck: 10
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 5
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 36 -> 30 (dropped 6)
Dropped sources:
  - [encyclopedia] "Copán La Leyenda" (relevance: 0.1111, reason: relevance_0.111_below_0.35)
  - [encyclopedia] "Dark Side of the Moon (2002 film)" (relevance: 0.412, reason: non_content_pattern)
  - [academic] "Of tinfoil hats and thinking caps: Reasoning is more strongly related to implausible than plausible conspiracy beliefs" (relevance: 0.3043, reason: relevance_0.304_below_0.35)
  - [academic] "“If they believe, then so shall I”: Perceived beliefs of the in-group predict conspiracy theory belief" (relevance: 0.2255, reason: relevance_0.225_below_0.35)
  - [knowledge_graph] "faked death" (relevance: 0.3295, reason: relevance_0.329_below_0.35)
  - [knowledge_graph] "false evidence" (relevance: 0.3352, reason: relevance_0.335_below_0.35)

### Dedup: 30 -> 27 (dropped 3)

### Analyzed sources (27 total)

**[google_factcheck] "Former Russian Space Chief Repeats False Moon Landing ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: VOA | Enriched: True | Extract score: 0.872 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Dmitry Rogozin, the former head of Russia’s space agency Roscosmos, endorsed the old “U.S. moon landing hoax” conspiracy theory in a Telegram post on ..."

**[google_factcheck] "Buzz Aldrin didn't 'admit' he never went to the Moon – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: Full Fact | Enriched: True | Extract score: 0.871 | Rating: In the clip, Mr Aldrin appears to be explaining why astronauts haven’t returned to the Moon in decades, not that they never went at all. In other interviews, Mr Aldrin clearly claims he went to the Moon.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A video viewed more than 42,000 times on Instagram claims to show former astronaut Buzz Aldrin as he “admits [the] Moon landing was fake”.
The clip sh..."

**[google_factcheck] "'Fake' moon landing claim orbits the simple facts"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: AAP | Enriched: True | Extract score: 0.763 | Rating: False. The initial images used by newspapers were taken from the live footage beamed around the world during the landing.
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "WHAT WAS CLAIMED
Newspaper photos of the moon landing published on the same day could not have been transported and developed so quickly - proving the..."

**[google_factcheck] "No, Wikileaks didn’t release evidence that the moon landing was faked"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.843 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Stand up for the facts! Our only agenda is to publish the truth so you can be an informed participant in democracy. We need your help. I would like to..."

**[google_factcheck] "In 1969, the president called the astronauts on the moon. Here’s how"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.960 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Stand up for the facts! Our only agenda is to publish the truth so you can be an informed participant in democracy. We need your help. I would like to..."

**[google_factcheck] "Fact check: Moon landing conspiracy theory misrepresents footprint"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.742 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Fact check: Moon landing conspiracy theory misrepresents lunar footprint
The claim: A mismatch between a space boot and the lunar footprint proves the..."

**[google_factcheck] "No, This Photo Isn't Evidence the Moon Landing Was Staged"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes.com | Enriched: True | Extract score: 0.300 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Fact Check
In July 2022, some social media users shared a copypasta meme that alleged the Apollo 11 moon landing was faked, as evidenced by a ceiling ..."

**[google_factcheck] "No. Buzz Aldrin didn't say the moon landing was a hoax."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.992 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Stand up for the facts! Our only agenda is to publish the truth so you can be an informed participant in democracy. We need your help. I would like to..."

**[google_factcheck] "WikiLeaks has not released the footage of NASA’s moon landing ..."**
  Type: fact_check | Cred: estimated 0.85
  Publisher: FACTLY | Enriched: True | Extract score: 0.796 | Rating: FALSE
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A video allegedly released by WikiLeaks, allegedly showing NASA’s “faked” moon landing shot in the Nevada Desert, is circulating widely on social medi..."

**[google_factcheck] "Did Wikileaks Release Faked Moon Landing Footage?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "An old video supposedly showing leaked footage from Wikileaks about the 1969 moon landing being "faked" was recirculated on social media in December 2..."

**[wikipedia] "Moon landing conspiracy theories"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9175)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "As a result, its upper management team was questioned by Senate and House of Representatives space oversight committees. There was in fact no video br..."

**[wikipedia] "Man on the Moon (R.E.M. song)"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.8799)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The song's title and chorus refer to Moon landing conspiracy theories, as an oblique allusion to rumors that the moon landing was faked. The song gave..."

**[wikipedia] "Moon landing conspiracy theories in popular culture"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9263)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "He admonishes them "to get off their fannies" and get to work. During "Into The Wild Green Yonder" President Nixon's head admits that the Moon landing..."

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

**[duckduckgo] "Was the moon landing faked? | Curation of Knowledge"**
  Type: web | Cred: estimated 0.215
  NLI (nli_deberta): supporting (0.9712)
  Verdict contribution: supporting (weight: 0.2088)
  Snippet: "Perhaps, among the finest accomplishment in human history has been the moon landing on the 20 July in 1969. The moon landing was in fact an unparallel..."

**[duckduckgo] "Was the moon landing faked? – The Phoenix"**
  Type: web | Cred: estimated 0.246
  NLI (nli_deberta): supporting (0.6841)
  Verdict contribution: supporting (weight: 0.1683)
  Snippet: "The moon landing is one of mankind’s major achievements. It has been the subject of numerous documentaries and is a major part of pop culture. But the..."

**[duckduckgo] "Was the moon landing faked? Controversial Nibiru author David"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9829)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Was the moon landing faked? Controversial Nibiru author David Meade weighs in on NASA Apollo 11 hoax
The controversial author has addressed long-held ..."

**[duckduckgo] "Was the Moon landing faked? Conspiracy theorists point to key"**
  Type: web | Cred: estimated 0.45999999999999996
  NLI (nli_deberta): neutral (0.8765)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Was the Moon landing faked? Conspiracy theorists point to key reasons for NASA 'hoax'
In 1969, the world watched in awe as US astronaut Neil Armstrong..."

**[duckduckgo] "Why do some people believe the moon landings were a hoax? |"**
  Type: web | Cred: estimated 0.489
  NLI (nli_deberta): neutral (0.9019)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "What are some of the claims by the moon landing conspiracy ... So are these points enough to prove that the moon landings were just fakes? Dr...."

**[duckduckgo] "Was the moon landing faked?"**
  Type: web | Cred: estimated 0.426
  NLI (nli_deberta): neutral (0.9697)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "I heard from somewhere recently that 1 in 4 americans think the moon landing was faked (and as an American myself I am completely and utterly ......"

**[duckduckgo] "Was the moon landing faked? | Skeptics Shop"**
  Type: web | Cred: estimated 0.21800000000000003
  NLI (nli_deberta): opposing (0.9761)
  Verdict contribution: opposing (weight: 0.2128)
  Snippet: "No, the moon landing was not faked. ... There is a small but vocal group of people who believe that the moon landing was faked, often citing supposed ..."

**[duckduckgo] "Was the moon landing faked - Mythbusters - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.9419)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[wikidata] "Moon landing"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "arrival of a spacecraft on the surface of the Moon | instance of: occurrence..."

**[wikidata] "faked death"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "case in which an individual leaves evidence to suggest that they are dead | instance of: Wikibase reason for deprecated rank..."

### Verdict computation
  Supporting weight: 1.205
  Opposing weight: 4.0603
  Support ratio: 0.2289
  Confidence: 0.5423
  Verdict: **likely opposed**
  Neutral sources (no contribution): 16

  Top supporting:
    - Of Tinfoil Hats and Thinking Caps: Reasoning is More Strongly Related to Implausible than Plausible Conspiracy Beliefs (weight: 0.5489)
    - Conspiracy vs. Science: A Survey of U.S. Public Beliefs (weight: 0.279)
    - Was the moon landing faked? | Curation of Knowledge (weight: 0.2088)
    - Was the moon landing faked? – The Phoenix (weight: 0.1683)
  Top opposing:
    - 'Fake' moon landing claim orbits the simple facts (weight: 0.8075)
    - In 1969, the president called the astronauts on the moon. Here’s how (weight: 0.8075)
    - No. Buzz Aldrin didn't say the moon landing was a hoax. (weight: 0.8075)
    - Fact check: Moon landing conspiracy theory misrepresents footprint (weight: 0.475)
    - No, This Photo Isn't Evidence the Moon Landing Was Staged (weight: 0.475)

---
## 8. "5G causes COVID"
Category: factual_false
Expected: strongly opposed
Actual: strongly opposed (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 39 total
  - google_factcheck: 10
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 7
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 39 -> 27 (dropped 12)
Dropped sources:
  - [encyclopedia] "COVID-19 misinformation" (relevance: 0.2849, reason: relevance_0.285_below_0.35)
  - [encyclopedia] "Cristiano Amon" (relevance: 0.1815, reason: relevance_0.182_below_0.35)
  - [encyclopedia] "Thomas Cowan (alternative medicine practitioner)" (relevance: 0.102, reason: relevance_0.102_below_0.35)
  - [academic] "Medical disinformation and the unviable nature of COVID-19 conspiracy theories" (relevance: 0.2981, reason: relevance_0.298_below_0.35)
  - [academic] "How to Improve the Management of Acute Ischemic Stroke by Modern Technologies, Artificial Intelligence, and New Treatment Methods" (relevance: 0.1005, reason: relevance_0.100_below_0.35)
  - [academic] "Pathophysiological involvement of host mitochondria in SARS-CoV-2 infection that causes COVID-19: a comprehensive evidential insight" (relevance: 0.1713, reason: relevance_0.171_below_0.35)
  - [academic] "SARS-CoV-2: The Monster Causes COVID-19" (relevance: 0.3049, reason: relevance_0.305_below_0.35)
  - [academic] "Medical disinformation and the unviable nature of COVID-19 conspiracy theories" (relevance: 0.2981, reason: relevance_0.298_below_0.35)
  - [academic] "Different Conspiracy Theories Have Different Psychological and Social Determinants: Comparison of Three Theories About the Origins of the COVID-19 Virus in a Representative Sample of the UK Population" (relevance: 0.2987, reason: relevance_0.299_below_0.35)
  - [academic] "Knowledge, Attitudes, Practices, and Misconceptions towards COVID-19 among Sub-Sahara Africans" (relevance: 0.2648, reason: relevance_0.265_below_0.35)
  - [academic] "Pandemic Management for Diseases Similar to COVID-19 Using Deep Learning and 5G Communications" (relevance: 0.2799, reason: relevance_0.280_below_0.35)
  - [academic] "The real economic costs of COVID-19: Insights from electricity consumption data in Hunan Province, China" (relevance: 0.3154, reason: relevance_0.315_below_0.35)

### Dedup: 27 -> 23 (dropped 4)

### Analyzed sources (23 total)

**[google_factcheck] "These claims about the new coronavirus and 5G are unfounded ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: Full Fact | Enriched: True | Extract score: 0.782 | Rating: While it is true that China has over 100,000 towers, it is unclear if it was the first place to pass this number.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "What was claimed
The new coronavirus is actually the impact of 5G exposure. Our verdict
This is incorrect, the new coronavirus is a virus and there is..."

**[google_factcheck] "The EG.5 variant of Covid-19 has nothing to do with 5G – Full Fact"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: Full Fact | Enriched: True | Extract score: 0.756 | Rating: This is not true. Covid-19 is caused by the SARS-CoV-2 virus. The 5G network uses radio waves that do not harm people’s health.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "What was claimed
The EG.5 variant of Covid-19 is a new 5G virus. Our verdict
This is not true. Covid-19 is caused by the SARS-CoV-2 virus. The 5G netw..."

**[google_factcheck] "Fresh false claims about COVID-19 vaccine and 5G technology ..."**
  Type: fact_check | Cred: estimated 0.85
  Publisher: AFP Fact Check | Enriched: True | Extract score: 0.888 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Fresh false claims about COVID-19 vaccine and 5G technology spread online in the Philippines
- Published on June 19, 2020 at 11:00
- By AFP Philippine..."

**[google_factcheck] "Hoax linking Covid-19 to bacteria and 5G mobile technology ..."**
  Type: fact_check | Cred: estimated 0.85
  Publisher: AFP Fact Check | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Hoax linking Covid-19 to bacteria and 5G mobile technology resurfaces in South Africa
- Published on January 13, 2022 at 22:29
- By James OKONG'O, AFP..."

**[google_factcheck] "'Bombshell' 5G COVID studies tank upon closer inspection"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: AAP | Enriched: True | Extract score: 0.700 | Rating: False. The studies cited as evidence do not claim to have found a link between 5G and COVID.
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "WHAT WAS CLAIMED
The US government has admitted 5G radiation causes COVID-19.
OUR VERDICT
False. The studies cited as evidence do not claim to have fo..."

**[google_factcheck] "Fact Check: 5G Wuhan Rollout Did NOT Cause Coronavirus ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: Lead Stories | Enriched: True | Extract score: 0.723 | Rating: Not Connected
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Was Wuhan, China the first city to be "covered" with 5G technology and did this wireless communications network facilitate the origination and spread ..."

**[wikipedia] "5G misinformation"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.8838)
  Verdict contribution: opposing (weight: 0.707)
  Snippet: "A 2020 study that monitored data from Google Trends showed that searches related to coronavirus and 5G started at different times, but peaked in the s..."

**[wikipedia] "5G"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.7744)
  Verdict contribution: opposing (weight: 0.6582)
  Snippet: "In 2012, New York University established NYU Wireless, a research center focused on millimeter-wave communication. The same year, the University of Su..."

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

**[duckduckgo] "Spreading Like a Virus: False Rumor That 5G Causes COVID-19"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.48)
  Verdict contribution: opposing (weight: 0.408)
  Snippet: "The myth linking 5G to COVID-19 spread rapidly due to distrust and fear, despite 5G being safe and unrelated. Clear debunking helps curb such misinfor..."

**[duckduckgo] "Belief That 5G Causes COVID-19 Linked to Violence... - Newsweek"**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): opposing (0.7671)
  Verdict contribution: opposing (weight: 0.3836)
  Snippet: "Believing in conspiracy theories surrounding 5G technology and COVID-19 has been linked to violence in a study. Conspiracy theorists have claimed with..."

**[duckduckgo] "Why would people believe 5G causes COVID-19? | YourLifeChoices"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): opposing (0.5688)
  Verdict contribution: opposing (weight: 0.1138)
  Snippet: "A significant number of people are concerned about 5G technology and believe it emits harmful radiation. That’s a rational fear as the technology does..."

**[duckduckgo] "5G causes COVID-19 like 4G causes flu"**
  Type: web | Cred: estimated 0.40099999999999997
  NLI (nli_deberta): opposing (0.9751)
  Verdict contribution: opposing (weight: 0.391)
  Snippet: "During an on-screen slot about the farcical notion that 5G causes COVID-19, Holmes said he did not accept "mainstream media immediately slapping that ..."

**[duckduckgo] "'5G Causes COVID-19' Conspiracy Theory: No Fix for Stupid"**
  Type: web | Cred: estimated 0.286
  NLI (nli_deberta): supporting (0.8765)
  Verdict contribution: supporting (weight: 0.2507)
  Snippet: "Endpoint Security , Governance & Risk Management , Internet of Things Security
'5G Causes COVID-19' Conspiracy Theory: No Fix for Stupid
Suspected Ars..."

**[duckduckgo] "expert reaction to people who think 5G causes... | Science Media Centre"**
  Type: web | Cred: verified 0.85 | Factual: high
  NLI (nli_deberta): opposing (0.7915)
  Verdict contribution: opposing (weight: 0.6728)
  Snippet: "There have been reports of people who think 5G mobile networks have caused the coronavirus outbreak. Prof Malcolm Sperrin, Director of the Department ..."

**[duckduckgo] "5G causes Covid-19? That’s cock and bull | Daily Nation"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): opposing (0.9653)
  Verdict contribution: opposing (weight: 0.4827)
  Snippet: "The fact is, Covid-19 is spread through respiratory droplets when an infected person coughs, sneezes or speaks. The allegation that 5G causes Covid-19..."

**[duckduckgo] "thepeoplesvoice.tv/u-s-government-admits-5g-radiation-causes-covid..."**
  Type: web | Cred: estimated 0.40499999999999997
  NLI (nli_deberta): neutral (0.9453)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Bombshell new peer-reviewed scientific studies have revealed what many of us knew from the beginning. 5G radiation is not only connected to the Covid-..."

**[duckduckgo] "Evidence for a connection between coronavirus disease-19 and..."**
  Type: web | Cred: estimated 0.592
  NLI (nli_deberta): opposing (0.8203)
  Verdict contribution: opposing (weight: 0.4856)
  Snippet: "SARS-CoV-2, the virus that caused the COVID-19 pandemic, surfaced in Wuhan, China shortly after the implementation of city-wide (fifth generation [5G]..."

**[duckduckgo] "Coronavirus: Scientists brand 5G claims 'complete rubbish'"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): opposing (0.8906)
  Verdict contribution: opposing (weight: 0.757)
  Snippet: "Coronavirus: Scientists brand 5G claims 'complete rubbish'
Conspiracy theories claiming 5G technology helps transmit coronavirus have been condemned b..."

### Verdict computation
  Supporting weight: 1.0157
  Opposing weight: 7.163
  Support ratio: 0.1242
  Confidence: 0.7516
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 7

  Top supporting:
    - Fresh false claims about COVID-19 vaccine and 5G technology ... (weight: 0.765)
    - '5G Causes COVID-19' Conspiracy Theory: No Fix for Stupid (weight: 0.2507)
  Top opposing:
    - 'Bombshell' 5G COVID studies tank upon closer inspection (weight: 0.8075)
    - Coronavirus: Scientists brand 5G claims 'complete rubbish' (weight: 0.757)
    - 5G misinformation (weight: 0.707)
    - expert reaction to people who think 5G causes... | Science Media Centre (weight: 0.6728)
    - 5G (weight: 0.6582)

---
## 9. "LeBron James is the greatest basketball player of all time"
Category: opinion
Expected: opinion
Actual: sources lean supporting (YES)
Claim type: opinion (0.95)
Claim domain: general

### Sources collected: 22 total
  - google_factcheck: 1
  - wikipedia: 5
  - duckduckgo: 10
  - wikidata: 6
  - semantic_scholar: SKIPPED (disabled by routing)
  - open_alex: SKIPPED (disabled by routing)

### Relevance filter: 22 -> 18 (dropped 4)
Dropped sources:
  - [encyclopedia] "NBA 75th Anniversary Team" (relevance: 0.2998, reason: relevance_0.300_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.053, reason: relevance_0.053_below_0.35)
  - [knowledge_graph] "time" (relevance: 0.1677, reason: relevance_0.168_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.0644, reason: relevance_0.064_below_0.35)

### Dedup: 18 -> 14 (dropped 4)

### Analyzed sources (14 total)

**[google_factcheck] "Did Michael Jordan Call LeBron James the Greatest Basketball ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Who is the greatest basketball player of all time? According to a social media posts from December 2018, former Chicago Bulls superstar Michael Jordan..."

**[wikipedia] "LeBron James"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9688)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This prompted an investigation by the Ohio High School Athletic Association (OHSAA) because its guidelines stated that no amateur may accept any gift ..."

**[wikipedia] "List of career achievements by LeBron James"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9072)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "List of career achievements by LeBron James
The American professional basketball player LeBron James began his career in the National Basketball Assoc..."

**[wikipedia] "GOAT (sports culture)"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9785)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The goat emoji is used in social media posts, often by general users but also by athletes themselves. The Wall Street Journal (WSJ) reviewed data cove..."

**[wikipedia] "50 Greatest Players in NBA History"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9849)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "50 Greatest Players in NBA History
The 50 Greatest Players in NBA History, also referred to as NBA's 50th Anniversary All-Time Team, were chosen in 19..."

**[duckduckgo] "LeBron James is the greatest of all time - The Quinnipiac Chronicle"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9775)
  Verdict contribution: supporting (weight: 0.3949)
  Snippet: "Entering his 23rd year, No. 23 for the Los Angeles Lakers, forward LeBron James is one of two players in the modern-day debate of the greatest basketb..."

**[duckduckgo] "Let's end this debate. Is Lebron the greatest basketball player of all ..."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.9873)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Mar 3, 2024 ... Kareem was the best college player ever, they changed the rules to tame down his domination and then he came to the NBA and led the en..."

**[duckduckgo] "LeBron James has had 'the greatest career of any NBA player,' says ..."**
  Type: web | Cred: estimated 0.5269999999999999
  NLI (nli_deberta): supporting (0.8916)
  Verdict contribution: supporting (weight: 0.4699)
  Snippet: "LeBron James has had 'the greatest career of any NBA player,' says JJ Redick
LeBron James and the Los Angeles Lakers are headed to the Western Confere..."

**[duckduckgo] "NBA Players Explain Why LeBron James is THE GOAT - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.98)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[duckduckgo] "Sorry, Michael—LeBron James is the Greatest Basketball Player of ..."**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.9858)
  Verdict contribution: supporting (weight: 0.4929)
  Snippet: "Mar 11, 2019 ... The debate is over. LeBron James is the greatest basketball player in history. His closest competitor, Michael Jordan, has been vanqu..."

**[duckduckgo] "Lebron James,widely considered greatest all-around - Facebook"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): neutral (0.5303)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Nov 11, 2025 ... Lebron James,widely considered greatest all-around basketball player of all-time.. The conversation revolves around the debate on who..."

**[duckduckgo] "5 Reasons Why LeBron James Is The Greatest NBA Player Ever"**
  Type: web | Cred: estimated 0.244
  NLI (nli_deberta): supporting (0.8521)
  Verdict contribution: supporting (weight: 0.2079)
  Snippet: "There have been many great players, both past and present in the history of the NBA. One of the lingering questions is, “Who is the greatest NBA playe..."

**[duckduckgo] "Why is LeBron James considered a top-10 player of all time ... - Quora"**
  Type: web | Cred: estimated 0.487
  NLI (nli_deberta): neutral (0.9766)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Jan 27, 2024 ... LeBron James is considered a top 3 player of all time and one of the best passers in basketball with Magic Johnson. Some amazing fact..."

**[duckduckgo] "The 10 Greatest Basketball Players of All Time - Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): supporting (0.689)
  Verdict contribution: supporting (weight: 0.5856)
  Snippet: "This list is, naturally, incredibly subjective, and shouldn’t be taken too seriously. Unless you agree with me, in which case this was the most meanin..."

### Verdict computation
  Supporting weight: 2.1512
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 9

  Top supporting:
    - The 10 Greatest Basketball Players of All Time - Britannica (weight: 0.5856)
    - Sorry, Michael—LeBron James is the Greatest Basketball Player of ... (weight: 0.4929)
    - LeBron James has had 'the greatest career of any NBA player,' says ... (weight: 0.4699)
    - LeBron James is the greatest of all time - The Quinnipiac Chronicle (weight: 0.3949)
    - 5 Reasons Why LeBron James Is The Greatest NBA Player Ever (weight: 0.2079)

---
## 10. "pineapple belongs on pizza"
Category: opinion
Expected: opinion
Actual: sources lean supporting (YES)
Claim type: opinion (0.95)
Claim domain: general

### Sources collected: 18 total
  - google_factcheck: 0
  - wikipedia: 5
  - duckduckgo: 10
  - wikidata: 3
  - semantic_scholar: SKIPPED (disabled by routing)
  - open_alex: SKIPPED (disabled by routing)

### Relevance filter: 18 -> 13 (dropped 5)
Dropped sources:
  - [encyclopedia] "Cheung Ka Long" (relevance: 0.02, reason: relevance_0.020_below_0.35)
  - [encyclopedia] "Concerns and controversies at the 2024 Summer Olympics" (relevance: -0.0147, reason: relevance_-0.015_below_0.35)
  - [encyclopedia] "Vargskelethor Joel" (relevance: 0.1353, reason: relevance_0.135_below_0.35)
  - [encyclopedia] "Brazilian cuisine" (relevance: 0.2452, reason: relevance_0.245_below_0.35)
  - [encyclopedia] "MasterChef Australia series 17" (relevance: 0.1525, reason: relevance_0.153_below_0.35)

### Dedup: 13 -> 13 (dropped 0)

### Analyzed sources (13 total)

**[duckduckgo] "Why pineapple belongs on pizza — Domino's Newsroom"**
  Type: web | Cred: estimated 0.34199999999999997
  NLI (nli_deberta): supporting (0.9727)
  Verdict contribution: supporting (weight: 0.3327)
  Snippet: "Why pineapple belongs on pizza
IT’S no secret that pizza brings people closer. Arguably the world’s best bonding food, pizza is cut into eight slices ..."

**[duckduckgo] "Does Pineapple Belong on Pizza | Made in New York Pizza"**
  Type: web | Cred: estimated 0.248
  NLI (nli_deberta): supporting (0.853)
  Verdict contribution: supporting (weight: 0.2115)
  Snippet: "In the culinary world, no food stirs opposing opinions like Hawaiian Pizza. Does pineapple belong on pizza? With ham, bacon, pineapple, cheese, and to..."

**[duckduckgo] "Why Pineapple Belongs on Pizza. The controversy explained | Medium"**
  Type: web | Cred: estimated 0.23900000000000002
  NLI (nli_deberta): supporting (0.8794)
  Verdict contribution: supporting (weight: 0.2102)
  Snippet: "Why does pineapple belong on pizza? Simple answer, you shouldn't it? Let me ask you this question — If I order my pizza with pineapple and you or anyb..."

**[duckduckgo] "Pineapple Belongs on Pizza | Gluten Free Recipe | CAULIPOWER"**
  Type: web | Cred: estimated 0.341
  NLI (nli_deberta): neutral (0.8853)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With CAULIPOWER®, you don’t have to choose between good food and food that’s good for you. By revolutionizing the use of vegetables in our food, eatin..."

**[duckduckgo] "Does Pineapple Belong on Pizza? | The Kitchn"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): supporting (0.6597)
  Verdict contribution: supporting (weight: 0.2758)
  Snippet: "We Asked 3 Chefs if Pineapple Belongs on Pizza, and They All Said the Same Thing
It’s 2024, and yes, we are still talking about whether pineapple belo..."

**[duckduckgo] "Pineapple Belongs On Pizza GIF - Pineapple Belongs On Pizza..."**
  Type: web | Cred: estimated 0.529
  NLI (nli_deberta): supporting (0.9756)
  Verdict contribution: supporting (weight: 0.5161)
  Snippet: "We've updated our
Terms of Service
Privacy Policy
. By continuing you agree to Tenor's
Terms of Service
Privacy Policy
Tenor.com has been translated b..."

**[duckduckgo] "Pizza On Pineapple Belongs Stickers for Sale | TeePublic"**
  Type: web | Cred: estimated 0.41900000000000004
  NLI (nli_deberta): neutral (0.4646)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Pizza On Pineapple Belongs Stickers
Description: Stop putting pineapple on pizza! It's gross, it's disgusting, and you should be ashamed of yourself! ..."

**[duckduckgo] "Pineapple Does Not Belong on Pizza | TikTok"**
  Type: web | Cred: estimated 0.533
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.5315)
  Snippet: "Discover videos related to pineapple does not belong on pizza on TikTok. See more videos about Say Pineapple Ya Chicken, Pineapple Juice Benefits, Wha..."

**[duckduckgo] "PINEAPPLE BELONGS ON PIZZA | Reading Your... - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.751)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[duckduckgo] "Does Pineapple Belong on Pizza? Let’s Debate About Food"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.6743)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The answer to whether or not pineapple belongs on pizza is obvious, but have you ever considered what constitutes a pizza in the first place? Should “..."

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
  Supporting weight: 1.5462
  Opposing weight: 0.5315
  Support ratio: 0.7442
  Confidence: 0.4884
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 7

  Top supporting:
    - Pineapple Belongs On Pizza GIF - Pineapple Belongs On Pizza... (weight: 0.5161)
    - Why pineapple belongs on pizza — Domino's Newsroom (weight: 0.3327)
    - Does Pineapple Belong on Pizza? | The Kitchn (weight: 0.2758)
    - Does Pineapple Belong on Pizza | Made in New York Pizza (weight: 0.2115)
    - Why Pineapple Belongs on Pizza. The controversy explained | Medium (weight: 0.2102)
  Top opposing:
    - Pineapple Does Not Belong on Pizza | TikTok (weight: 0.5315)

---
## 11. "democracy is the best form of government"
Category: opinion
Expected: opinion
Actual: sources divided (YES)
Claim type: opinion (0.95)
Claim domain: general

### Sources collected: 36 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 2
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 36 -> 27 (dropped 9)
Dropped sources:
  - [academic] "An Approach to Pediatric or Mentally Deficient Donors from a Bioethical Perspective: Considerations and Recommendations on Behalf of the Donor Research Team of the Turkish Society of Hematology (DART)" (relevance: 0.0524, reason: relevance_0.052_below_0.35)
  - [academic] "A global panel database of pandemic policies (Oxford COVID-19 Government Response Tracker)" (relevance: 0.1123, reason: relevance_0.112_below_0.35)
  - [academic] "How polarization, populist attitudes, and cultural backlash affect citizens’ support for democracy: Evidence from Spain" (relevance: 0.3393, reason: relevance_0.339_below_0.35)
  - [knowledge_graph] "Democracy Club" (relevance: 0.3225, reason: relevance_0.323_below_0.35)
  - [knowledge_graph] "Best forms of involvement for first-year student veterans for academic success" (relevance: 0.1212, reason: relevance_0.121_below_0.35)
  - [knowledge_graph] "BEST Form of CARDIO | Fastest | Fat Loss" (relevance: 0.1212, reason: relevance_0.121_below_0.35)
  - [knowledge_graph] "Q120472867" (relevance: -0.0351, reason: relevance_-0.035_below_0.35)
  - [knowledge_graph] "public school" (relevance: 0.2046, reason: relevance_0.205_below_0.35)
  - [knowledge_graph] "civil servant" (relevance: 0.1244, reason: relevance_0.124_below_0.35)

### Dedup: 27 -> 26 (dropped 1)

### Analyzed sources (26 total)

**[wikipedia] "Democracy"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The theoretical project of inclusive democracy emerged from the work of political philosopher Takis Fotopoulos in "Towards An Inclusive Democracy" and..."

**[wikipedia] "List of forms of government"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9819)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Experiments have mostly been conducted on a local level or exclusively through online platforms, such as by Pirate Parties
Representative democracy Wh..."

**[wikipedia] "Mixed government"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9688)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The idea was popularized during classical antiquity in order to describe the stability, the innovation and the success of the republic as a form of go..."

**[wikipedia] "Criticism of democracy"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.6294)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Numerous empirical studies across various western democracies including the United States, Spain, Sweden, Switzerland, Canada, Norway and Germany have..."

**[wikipedia] "Types of democracy"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A participatory democracy or semi-direct democracy is a form of government in which citizens participate individually and directly in political decisi..."

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

**[duckduckgo] "Why is Democracy the best form of Government? - KnowsWhy.com"**
  Type: web | Cred: estimated 0.23199999999999998
  NLI (nli_deberta): neutral (0.8179)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Why is Democracy the best form of Government? It is a form of government on which the power lies to the masses (majority of people). The term came fro..."

**[duckduckgo] "Essay on Democracy Is the Best Form of Government - Essay Writer"**
  Type: web | Cred: estimated 0.344
  NLI (nli_deberta): neutral (0.9736)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Despite much discussion and opposition regarding the nature of democracy and its effectiveness as a form of Government, most nations worldwide continu..."

**[duckduckgo] "Democracy is the best form of Government. – International"**
  Type: web | Cred: estimated 0.29700000000000004
  NLI (nli_deberta): supporting (0.8276)
  Verdict contribution: supporting (weight: 0.2458)
  Snippet: "“Government of the people, by the people’-this is a patent and ubiquitous definition of democracy. The other two alternative forms of equal universal ..."

**[duckduckgo] "democracy is the best form of government | marcoullasci"**
  Type: web | Cred: estimated 0.231
  NLI (nli_deberta): neutral (0.7031)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "When I started reading this book I was a bit shocked. I was raised, as most people of my age in the western world, with a few clear ideas including th..."

**[duckduckgo] "Democracy Best Form Of Government? Essay Example - PHDessay.com"**
  Type: web | Cred: estimated 0.433
  NLI (nli_deberta): supporting (0.7686)
  Verdict contribution: supporting (weight: 0.3328)
  Snippet: "Democracy is best defined as the government of the people, by the people. The classical example of democracy is that of ancient Athens, where the whol..."

**[duckduckgo] "Is Democracy the Best Form of Government? | Free Paper Example"**
  Type: web | Cred: estimated 0.27599999999999997
  NLI (nli_deberta): opposing (0.8853)
  Verdict contribution: opposing (weight: 0.2443)
  Snippet: "Democracy is the only system of governance that gives ordinary citizens a chance to influence the politics of their own country to address various pro..."

**[duckduckgo] "Is Democracy the Best Form of Government? | FreebookSummary"**
  Type: web | Cred: estimated 0.35
  NLI (nli_deberta): opposing (0.9985)
  Verdict contribution: opposing (weight: 0.3495)
  Snippet: "Is Democracy the Best Form of Government? Democracy is often defined as the government of the people, for the people and by the people. However, this ..."

**[duckduckgo] "Is Democracy the Best Form of Government? - Term Paper"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9941)
  Verdict contribution: opposing (weight: 0.2982)
  Snippet: "These are: To give information To gather information WHY COMMUNICATE? To influence action To start action To give reassurance To clarify issues www.cs..."

**[duckduckgo] "Democracy is the best form of government: Argumentative Essay -"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.6582)
  Verdict contribution: supporting (weight: 0.1316)
  Snippet: "The resources for English Essays are not proper and organised. So, to help students we have created English Essays Series for ICSE students. In this a..."

**[duckduckgo] "Democracy Is the Best Form of Government | ESL Debates"**
  Type: web | Cred: estimated 0.23399999999999999
  NLI (nli_deberta): supporting (0.9067)
  Verdict contribution: supporting (weight: 0.2122)
  Snippet: "Churchill once said “Democracy is the worst form of government, except for all those other forms that been tired from time to time”. Just like any com..."

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
  Supporting weight: 1.4214
  Opposing weight: 1.2874
  Support ratio: 0.5247
  Confidence: 0.0495
  Verdict: **sources divided**
  Neutral sources (no contribution): 17

  Top supporting:
    - Does crime breed authoritarianism? Crime exposure, democratic decoupling and political attitudes in Brazil (weight: 0.499)
    - Democracy Best Form Of Government? Essay Example - PHDessay.com (weight: 0.3328)
    - Democracy is the best form of Government. – International (weight: 0.2458)
    - Democracy Is the Best Form of Government | ESL Debates (weight: 0.2122)
    - Democracy is the best form of government: Argumentative Essay - (weight: 0.1316)
  Top opposing:
    - Democracy and Development in Africa: Demystifying Democracy as the Best Form of Government (weight: 0.3953)
    - Is Democracy the Best Form of Government? | FreebookSummary (weight: 0.3495)
    - Is Democracy the Best Form of Government? - Term Paper (weight: 0.2982)
    - Is Democracy the Best Form of Government? | Free Paper Example (weight: 0.2443)

---
## 12. "sugar is worse than fat for health"
Category: contested
Expected: contested
Actual: sources divided (YES)
Claim type: opinion (0.95)
Claim domain: scientific

### Sources collected: 37 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 6
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 37 -> 27 (dropped 10)
Dropped sources:
  - [academic] "Microbiota in health and diseases" (relevance: 0.1699, reason: relevance_0.170_below_0.35)
  - [academic] "Dementia prevention, intervention, and care: 2024 report of the Lancet standing Commission" (relevance: 0.0916, reason: relevance_0.092_below_0.35)
  - [academic] "2023 AHA/ACC/ACCP/ASPC/NLA/PCNA Guideline for the Management of Patients With Chronic Coronary Disease: A Report of the American Heart Association/American College of Cardiology Joint Committee on Clinical Practice Guidelines" (relevance: 0.1376, reason: relevance_0.138_below_0.35)
  - [academic] "Breast Cancer—Epidemiology, Risk Factors, Classification, Prognostic Markers, and Current Treatment Strategies—An Updated Review" (relevance: 0.0057, reason: relevance_0.006_below_0.35)
  - [knowledge_graph] "Sugar" (relevance: 0.2274, reason: relevance_0.227_below_0.35)
  - [knowledge_graph] "unstable angina" (relevance: 0.0165, reason: relevance_0.017_below_0.35)
  - [knowledge_graph] "worse" (relevance: 0.3151, reason: relevance_0.315_below_0.35)
  - [knowledge_graph] "worse is better" (relevance: 0.2582, reason: relevance_0.258_below_0.35)
  - [knowledge_graph] "File Allocation Table" (relevance: -0.0306, reason: relevance_-0.031_below_0.35)
  - [knowledge_graph] "overweight" (relevance: 0.272, reason: relevance_0.272_below_0.35)

### Dedup: 27 -> 26 (dropped 1)

### Analyzed sources (26 total)

**[wikipedia] "Diet food"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.6743)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Diet food (or dietetic food) refers to any food or beverage whose recipe is altered to reduce fat, carbohydrates, and/or sugar in order to make it par..."

**[wikipedia] "Trans fat"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9736)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A scientific review agrees with the conclusion (stating that "the sum of the current evidence suggests that the Public health implications of consumin..."

**[wikipedia] "Malnutrition"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9668)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Increased sedentary lifestyles also contribute to overnutrition. Yale University psychologist Kelly Brownell calls this a "toxic food environment", wh..."

**[wikipedia] "Aseem Malhotra"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9751)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "He contends that people should reduce sugar in their diet, adopt a low-carb and high-fat diet, and reduce their use of prescription drugs. He was the ..."

**[wikipedia] "Diabetes"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.981)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "People with diabetes are at a higher risk of developing gallstones compared to those without diabetes. There is a link between cognitive deficit and d..."

**[open_alex] "Dietary Intake and Diet Quality of Adult Survivors of Childhood Cancer and the General Population: Results from the SCCSS-Nutrition Study"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.9795)
  Verdict contribution: opposing (weight: 0.6367)
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

**[open_alex] "A 2022 update on the epidemiology of obesity and a call to action: as its twin COVID-19 pandemic appears to be receding, the obesity and dysmetabolism pandemic continues to rage on"**
  Type: academic | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.978)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The WHO just released in May 2022 a report on the state of the obesity pandemic in Europe, stating that 60% of citizens in the area of Europe are eith..."

**[duckduckgo] "Sugar vs. Fat: The Final Verdict on Which is Worse for Your"**
  Type: web | Cred: estimated 0.264
  NLI (nli_deberta): supporting (0.9917)
  Verdict contribution: supporting (weight: 0.2618)
  Snippet: "Sugar vs. Fat: The Final Verdict on Which is Worse for Your Health
We’re the world’s largest nutrition school and Health Coach Training Program. Throu..."

**[duckduckgo] "Why sugar is worse than fat | PatientsEngage"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.9609)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... sugar may be more problematic, in some ... See the full interview on http://globalpublicsquare.blogs.cnn.com/2014/09/10/why-sugar-is-worse-than-fa..."

**[duckduckgo] "What's Worse, Fat or Sugar? - Food Blog Alliance"**
  Type: web | Cred: estimated 0.301
  NLI (nli_deberta): supporting (0.7612)
  Verdict contribution: supporting (weight: 0.2291)
  Snippet: "What’s Worse, Fat or Sugar? The Ultimate Showdown
Ultimately, sugar is generally considered worse than fat for overall health, due to its significant ..."

**[duckduckgo] "Sugar VS Fat - Which One is Worse For Your Health And Waistline"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.7461)
  Verdict contribution: supporting (weight: 0.2238)
  Snippet: "Even more, this new generation of doctors and scientists is actually suggesting that against all odds, fat could be our best friend in the struggle to..."

**[duckduckgo] "Sugar VS Fat – Which One is Worse For Your Health And"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.7046)
  Verdict contribution: supporting (weight: 0.2114)
  Snippet: "... conducting some extensive research on the subject, he was more convinced than ever that the cause of many dangerous health issues is sugar, not fa..."

**[duckduckgo] "Cut Added Sugars to Lose Weight and Improve Health"**
  Type: web | Cred: estimated 0.266
  NLI (nli_deberta): neutral (0.8989)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Written By: Sofia Layarda, MPH
Title: Master of Public Health
Alumni: University of California, Berkeley
Last Updated on:
In the battle of the bulge, ..."

**[duckduckgo] "What's worse for you - Sugar v/s fat?"**
  Type: web | Cred: estimated 0.42300000000000004
  NLI (nli_deberta): opposing (0.46)
  Verdict contribution: opposing (weight: 0.1946)
  Snippet: "Few decades past, and the diet-industry has conducted a severe conflict on consumption of sugar v/s fat. It tried to make the leading consumers believ..."

**[duckduckgo] "Sugar vs Fat: Which Is Worse For Health & Weigh Gain?"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9561)
  Verdict contribution: opposing (weight: 0.2868)
  Snippet: "... sugar is not more fattening than natural sugar, but since it tends to be added to candy or junk food, you tend to get empty calories that increase..."

**[duckduckgo] "Sugar vs fat: which is worse? - BHF"**
  Type: web | Cred: estimated 0.341
  NLI (nli_deberta): opposing (0.7939)
  Verdict contribution: opposing (weight: 0.2707)
  Snippet: "Sugar vs fat: which is worse? Whether fat or sugar is worse for your health has become a dietary battleground. Senior Dietitian Victoria Taylor assess..."

**[duckduckgo] "Sugar is Worse Than Saturated Fat For The Heart - Healthiest"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.8062)
  Verdict contribution: supporting (weight: 0.2419)
  Snippet: "Avoiding added sugars is key to keeping your heart healthy. Saturated fats have long been thought the main enemy in the battle against cardiovascular ..."

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
  Supporting weight: 1.168
  Opposing weight: 1.7476
  Support ratio: 0.4006
  Confidence: 0.1988
  Verdict: **sources divided**
  Neutral sources (no contribution): 16

  Top supporting:
    - Sugar vs. Fat: The Final Verdict on Which is Worse for Your (weight: 0.2618)
    - Sugar is Worse Than Saturated Fat For The Heart - Healthiest (weight: 0.2419)
    - What's Worse, Fat or Sugar? - Food Blog Alliance (weight: 0.2291)
    - Sugar VS Fat - Which One is Worse For Your Health And Waistline (weight: 0.2238)
    - Sugar VS Fat – Which One is Worse For Your Health And (weight: 0.2114)
  Top opposing:
    - Dietary Intake and Diet Quality of Adult Survivors of Childhood Cancer and the General Population: Results from the SCCSS-Nutrition Study (weight: 0.6367)
    - Fat chance of escaping obesogens (weight: 0.3588)
    - Sugar vs Fat: Which Is Worse For Health & Weigh Gain? (weight: 0.2868)
    - Sugar vs fat: which is worse? - BHF (weight: 0.2707)
    - What's worse for you - Sugar v/s fat? (weight: 0.1946)

---
## 13. "nuclear energy is safe"
Category: contested
Expected: contested
Actual: sources lean supporting (YES)
Claim type: opinion (0.9)
Claim domain: scientific

### Sources collected: 32 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 4
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 32 -> 26 (dropped 6)
Dropped sources:
  - [academic] "Investigation of Resistance Characteristics of Throttling Elements in Steam Generators for Fourth-Generation Advanced Nuclear Energy Systems: Experimental and CFD Analysis" (relevance: 0.2534, reason: relevance_0.253_below_0.35)
  - [academic] "Soft Self-Templating Approach-Derived Covalent Triazine Framework with Bimodal Nanoporosity for Efficient Radioactive Iodine Capture for Safe Nuclear Energy" (relevance: 0.2383, reason: relevance_0.238_below_0.35)
  - [knowledge_graph] "nuclear binding energy" (relevance: 0.3078, reason: relevance_0.308_below_0.35)
  - [knowledge_graph] "Safe" (relevance: 0.2713, reason: relevance_0.271_below_0.35)
  - [knowledge_graph] "personal protective equipment" (relevance: 0.1295, reason: relevance_0.129_below_0.35)
  - [knowledge_graph] "safe" (relevance: 0.302, reason: relevance_0.302_below_0.35)

### Dedup: 26 -> 24 (dropped 2)

### Analyzed sources (24 total)

**[wikipedia] "Nuclear power"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): supporting (0.9902)
  Verdict contribution: supporting (weight: 0.8912)
  Snippet: "Nuclear power is a safe and sustainable energy source that reduces carbon emissions. Nuclear power generation results in one of the lowest levels of f..."

**[wikipedia] "Pro-nuclear energy movement"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9932)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In particular, Laughlin writes in "Powering the Future" (2011) that expanded use of nuclear power will be nearly inevitable, either because of a polit..."

**[wikipedia] "Nuclear Energy Agency"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9634)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The mission of the NEA is to "assist its member countries in maintaining and further developing, through international co-operation, the scientific, t..."

**[wikipedia] "Nuclear power in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9932)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Eventually, more than 120 reactor orders were canceled, and the construction of new reactors ground to a halt. Former US Vice President Al Gore, in 20..."

**[wikipedia] "Nuclear power in Pakistan"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8662)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The cooperation between China and Pakistan on commercial nuclear power plants has attracted controversies due to Pakistan being nonsignatory to the NP..."

**[open_alex] "Stellarator–mirror fusion–fission hybrid – a fast route to clean and safe nuclear energy"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.7905)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The multiple-recycle fuel cycle for uranium-238 considered here, if practically realized, can bring revolutionary changes in nuclear energy. A full us..."

**[semantic_scholar] "Soft Self-Templating Approach-Derived Covalent Triazine Framework with Bimodal Nanoporosity for Efficient Radioactive Iodine Capture for Safe Nuclear Energy"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.627)
  Verdict contribution: supporting (weight: 0.4076)
  Snippet: "Soft Self-Templating Approach-Derived Covalent Triazine Framework with Bimodal Nanoporosity for Efficient Radioactive Iodine Capture for Safe Nuclear ..."

**[semantic_scholar] "Nuclear Energy As a Reliable And Safe Source of Power Nuclear Energy As a Reliable And Safe Source of Power Generation Generation"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.8081)
  Verdict contribution: supporting (weight: 0.3232)
  Snippet: "Nuclear Energy As a Reliable And Safe Source of Power Nuclear Energy As a Reliable And Safe Source of Power Generation Generation..."

**[semantic_scholar] "NUCLEAR ENERGY - CHALLENGES, OPPORTUNITIES AND RISKS"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.978)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With the lifting of the moratorium on the construction of nuclear power plants in Serbia, a series of activities were initiated that opened up opportu..."

**[semantic_scholar] "The Inextricable Relationship Between Nuclear Energy and the Bomb"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9893)
  Verdict contribution: opposing (weight: 0.3957)
  Snippet: "Dr. Ramana’s presentation focused on issues of nuclear energy, the risks it poses, the factors that make it unsuitable as a source of clean energy acr..."

**[semantic_scholar] "Towards a zero-carbon nuclear energy future: a review"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.9902)
  Verdict contribution: supporting (weight: 0.3961)
  Snippet: "In order to attain a relatively zero-carbon future, nuclear energy is proposed to be one of the major solutions. In our quest to deal with climate cha..."

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

**[duckduckgo] "Nuclear energy in Israel"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "While Israel operates nuclear research reactors, it has no nuclear power plants. However, the possibility of constructing nuclear power plants in the ..."

**[duckduckgo] "Nuclear safety and security - Wikipedia"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): supporting (0.7437)
  Verdict contribution: supporting (weight: 0.5622)
  Snippet: "Nuclear safety is defined by the International Atomic Energy Agency (IAEA) as "The achievement of proper operating conditions, prevention of accidents..."

**[duckduckgo] "Genuine question about the safety of nuclear power - Reddit"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.5542)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Dec 15, 2024 · Nuclear reactors can't explode, have containment systems (chernobyl being an exception), and multiple safety systems. They are incredib..."

**[duckduckgo] "Enhanced Safety of Advanced Reactors | Department of Energy"**
  Type: web | Cred: estimated 0.488
  NLI (nli_deberta): supporting (0.9971)
  Verdict contribution: supporting (weight: 0.4866)
  Snippet: "Existing U.S. nuclear plants produce power by heating or boiling water to create steam that spins a turbine. The water is heated by a process called f..."

**[duckduckgo] "Advanced nuclear energy: the safest and most renewable clean energy"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.6074)
  Verdict contribution: supporting (weight: 0.5163)
  Snippet: "Although legacy nuclear energy has been the safest form of electricity generation, it has been demonized as unsafe since the 1960s. The three well-kno..."

**[duckduckgo] "Is Nuclear Power Bad for the Environment? - Friends of the Earth"**
  Type: web | Cred: estimated 0.421
  NLI (nli_deberta): opposing (0.9541)
  Verdict contribution: opposing (weight: 0.4017)
  Snippet: "Aug 19, 2024 · Conclusion: Yes — Nuclear Power is Bad for the Environment. While nuclear energy offers low operational carbon emissions, the full trut..."

**[duckduckgo] "Nuclear Energy - Our World in Data"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.8794)
  Verdict contribution: supporting (weight: 0.7475)
  Snippet: "The analysis by Markandya and Wilkinson was published in 2007. Since then, our understanding of the health impacts of air pollution has increased sign..."

**[duckduckgo] "Nuclear Power and Safety"**
  Type: web | Cred: estimated 0.263
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.2617)
  Snippet: "Nuclear Power and Safety
Introduction
When it comes to nuclear power, safety is often the primary concern for many individuals. While the benefits of ..."

**[duckduckgo] "Nuclear energy, safe use of nuclear power | IAEA"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): neutral (0.875)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The IAEA fosters the efficient and safe use of nuclear power by supporting existing and new nuclear programmes around the world...."

**[duckduckgo] "Ask an Expert: Nuclear's World-Class Safety Standards | NEI"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.9487)
  Verdict contribution: supporting (weight: 0.3823)
  Snippet: "May 13, 2022 · Nuclear energy isn't always recognized for the fact that it has world-class safety standards and studies have shown it to be one of the..."

**[wikidata] "Nuclear Energy"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "sculpture by Henry Moore (LH 526, University of Chicago) | instance of: sculpture | country: United States | located in: Chicago | inception: January ..."

### Verdict computation
  Supporting weight: 5.4614
  Opposing weight: 0.7974
  Support ratio: 0.8726
  Confidence: 0.7452
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 11

  Top supporting:
    - Nuclear power (weight: 0.8912)
    - Nuclear Energy - Our World in Data (weight: 0.7475)
    - Nuclear safety and security - Wikipedia (weight: 0.5622)
    - Advanced nuclear energy: the safest and most renewable clean energy (weight: 0.5163)
    - Development and outlook of advanced nuclear energy technology (weight: 0.4867)
  Top opposing:
    - Is Nuclear Power Bad for the Environment? - Friends of the Earth (weight: 0.4017)
    - The Inextricable Relationship Between Nuclear Energy and the Bomb (weight: 0.3957)

---
## 14. "remote work is more productive than office work"
Category: contested
Expected: contested
Actual: sources divided (YES)
Claim type: opinion (0.85)
Claim domain: general

### Sources collected: 24 total
  - google_factcheck: 0
  - wikipedia: 5
  - duckduckgo: 10
  - wikidata: 9
  - semantic_scholar: SKIPPED (disabled by routing)
  - open_alex: SKIPPED (disabled by routing)

### Relevance filter: 24 -> 18 (dropped 6)
Dropped sources:
  - [encyclopedia] "Work–life balance" (relevance: 0.3237, reason: relevance_0.324_below_0.35)
  - [encyclopedia] "Computer-supported cooperative work" (relevance: 0.3225, reason: relevance_0.322_below_0.35)
  - [knowledge_graph] "virtual assistant" (relevance: 0.3371, reason: relevance_0.337_below_0.35)
  - [knowledge_graph] "productive animal" (relevance: 0.3122, reason: relevance_0.312_below_0.35)
  - [knowledge_graph] "economic production" (relevance: 0.2096, reason: relevance_0.210_below_0.35)
  - [knowledge_graph] "productive forces" (relevance: 0.3162, reason: relevance_0.316_below_0.35)

### Dedup: 18 -> 17 (dropped 1)

### Analyzed sources (17 total)

**[wikipedia] "Remote work"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.6978)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Most studies find that remote work overall results in a decrease in energy use due to less time spent on energy-intensive personal transportation, cle..."

**[wikipedia] "Work (human activity)"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Work encompasses all types of productive activities, including employment, household chores, volunteering, and creative pursuits. It is a broad term t..."

**[wikipedia] "Productivity theater"**
  Type: encyclopedia | Cred: estimated 0.55
  NLI (nli_deberta): opposing (0.7227)
  Verdict contribution: opposing (weight: 0.3975)
  Snippet: "Productivity theater
Productivity theater is a form of impression management where an employee acts productively in the workplace, typically by appear..."

**[duckduckgo] "Every study proves remote workers are more productive, so ... - Reddit"**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): supporting (0.937)
  Verdict contribution: supporting (weight: 0.5585)
  Snippet: "Oct 4, 2025 ... Every study proves remote workers are more productive, so why are we still pretending offices are necessary? ... I was reading a 2023 ..."

**[duckduckgo] "The rise in remote work since the pandemic and its impact on ..."**
  Type: web | Cred: estimated 0.44000000000000006
  NLI (nli_deberta): neutral (0.9409)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "An official website of the United States government
The COVID-19 pandemic brought about dramatic changes in the work environment. Although 6.5 percent..."

**[duckduckgo] "Work from Home and Productivity: Evidence from Personnel and ..."**
  Type: web | Cred: estimated 0.40199999999999997
  NLI (nli_deberta): opposing (0.999)
  Verdict contribution: opposing (weight: 0.4016)
  Snippet: "Jan 17, 2023 ... However, average productivity was lower for remote workers than office workers. ... increased work time more during WFH than did thei..."

**[duckduckgo] "In-Office vs Remote Productivity: What the Data Shows - Worklytics"**
  Type: web | Cred: estimated 0.277
  NLI (nli_deberta): supporting (0.9062)
  Verdict contribution: supporting (weight: 0.251)
  Snippet: "Many organizations initially assumed productivity would decline when employees worked outside a centralized workplace. Data collected over the last se..."

**[duckduckgo] "The rise of remote work: challenges and opportunities for businesses"**
  Type: web | Cred: estimated 0.362
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Oct 9, 2025 ... Increased productivity and employee satisfaction (when managed well) ... Opinions differ considerably regarding the productivity of re..."

**[duckduckgo] "The Evolution of Working from Home"**
  Type: web | Cred: estimated 0.46699999999999997
  NLI (nli_deberta): opposing (0.9971)
  Verdict contribution: opposing (weight: 0.4656)
  Snippet: "The Evolution of Working from Home
Working from home rose five-fold from 2019 to 2023, with 40% of US employees now working remotely at least one day ..."

**[duckduckgo] "Is remote work more productive than office work? - Quora"**
  Type: web | Cred: estimated 0.487
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sep 4, 2025 ... It depends on the individual and the nature of the work. Remote work can offer flexibility and fewer distractions, leading to increase..."

**[duckduckgo] "Remote Work Productivity Study: Surprising Findings From a 4-Year ..."**
  Type: web | Cred: estimated 0.354
  NLI (nli_deberta): neutral (0.8477)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Benchmarks & Trends, Employee Experience, Remote & Hybrid Culture, Research
Editor’s note: This article was originally published in 2020 and updated i..."

**[duckduckgo] "Comparing Productivity for Remote Work vs. In-Office Employees"**
  Type: web | Cred: estimated 0.376
  NLI (nli_deberta): supporting (0.9883)
  Verdict contribution: supporting (weight: 0.3716)
  Snippet: "Sep 9, 2025 ... Remote work productivity vs. in-office productivity: Data and statistics · Remote workers are 35-40% more productive than employees wh..."

**[duckduckgo] "Remote is more productive than in-office if done right. | Chris Sukraw"**
  Type: web | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.9878)
  Verdict contribution: supporting (weight: 0.6915)
  Snippet: "👉 Remote is more productive than in-office if done right. That was my experience, leading a team of 12 creatives. Here’s why: ✅ Faster Workflow Work g..."

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
  Supporting weight: 1.8725
  Opposing weight: 1.2647
  Support ratio: 0.5969
  Confidence: 0.1937
  Verdict: **sources divided**
  Neutral sources (no contribution): 10

  Top supporting:
    - Remote is more productive than in-office if done right. | Chris Sukraw (weight: 0.6915)
    - Every study proves remote workers are more productive, so ... - Reddit (weight: 0.5585)
    - Comparing Productivity for Remote Work vs. In-Office Employees (weight: 0.3716)
    - In-Office vs Remote Productivity: What the Data Shows - Worklytics (weight: 0.251)
  Top opposing:
    - The Evolution of Working from Home (weight: 0.4656)
    - Work from Home and Productivity: Evidence from Personnel and ... (weight: 0.4016)
    - Productivity theater (weight: 0.3975)

---
## 15. "AI will replace most jobs"
Category: current_event
Expected: contested
Actual: strongly opposed (**NO - MISMATCH**)
Claim type: factual (0.8)
Claim domain: current_events

### Sources collected: 34 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 5
  - open_alex: 5
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 34 -> 27 (dropped 7)
Dropped sources:
  - [knowledge_graph] "Anguilla" (relevance: -0.0437, reason: relevance_-0.044_below_0.35)
  - [knowledge_graph] "Air India" (relevance: 0.0543, reason: relevance_0.054_below_0.35)
  - [knowledge_graph] "replacement" (relevance: 0.2092, reason: relevance_0.209_below_0.35)
  - [knowledge_graph] "replacement name" (relevance: 0.0437, reason: relevance_0.044_below_0.35)
  - [knowledge_graph] "electoral list" (relevance: 0.0174, reason: relevance_0.017_below_0.35)
  - [knowledge_graph] "Jobs" (relevance: 0.2197, reason: relevance_0.220_below_0.35)
  - [knowledge_graph] "Jobst" (relevance: 0.189, reason: relevance_0.189_below_0.35)

### Dedup: 27 -> 26 (dropped 1)

### Analyzed sources (26 total)

**[wikipedia] "AI boom"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Software development
[edit]Generative coding can be used to produce, edit, explain, and debug code. A 2026 study in the journal Management Science fou..."

**[wikipedia] "Artificial intelligence"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The general problem of simulating (or creating) intelligence has been broken into subproblems. These consist of particular traits or capabilities that..."

**[wikipedia] "Generative AI"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This enabled more realistic speech synthesis compared to earlier approaches. Subsequent systems such as Tacotron 2 demonstrated end-to-end neural text..."

**[wikipedia] "AI agent"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Conversely, researchers suggest that agents could be applied to web accessibility for people with disabilities, and researchers at Hugging Face propos..."

**[wikipedia] "Artificial general intelligence"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.98)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A 2020 survey identified 72 active AGI research and development projects across 37 countries. AGI is a common topic in science fiction and futures stu..."

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

**[duckduckgo] "ChatGPT: the 10 Jobs Most at Risk of Being Replaced by AI -"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9829)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Companies are taking notice. Both IBM and British telecommunications giant BT Group cited AI when announcing job cuts last year — and said that many w..."

**[duckduckgo] "Will AI replace most jobs? -"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): opposing (0.9824)
  Verdict contribution: opposing (weight: 0.1965)
  Snippet: "Conclusion: Will AI Replace Most Jobs? Not Likely, but Change Is Inevitable AI is undoubtedly reshaping the job market, but the future doesn’t have ....."

**[duckduckgo] "70+ Stats On AI Replacing Jobs (2026)"**
  Type: web | Cred: estimated 0.502
  NLI (nli_deberta): neutral (0.9834)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Keyword Research
Performance Tracking
Competitor Intelligence
Fix Your Site’s SEO Issues in 30 Seconds
Find technical issues blocking search visibilit..."

**[duckduckgo] "What jobs will AI replace & which are safe in 2025 [+Data]"**
  Type: web | Cred: estimated 0.5820000000000001
  NLI (nli_deberta): neutral (0.9893)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Future of Jobs Report 2025 found that 92 million jobs are expected to be displaced by 2030 due to AI, but 170 million new ones will also be create..."

**[duckduckgo] "AI to replace most jobs by 2045, only these 3 careers are safe,"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.8081)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Artificial intelligence (AI) has invaded several industries, with professionals incorporating the tool into their daily lives. However, experts have f..."

**[duckduckgo] "Why AI Won't Replace Most Jobs in 2026—but Will Reshape Work,"**
  Type: web | Cred: estimated 0.40499999999999997
  NLI (nli_deberta): opposing (0.9883)
  Verdict contribution: opposing (weight: 0.4003)
  Snippet: "The AI impact on jobs in 2026 is often framed as a replacement story, but the reality looks more balanced and far less dramatic. Most roles aren't dis..."

**[duckduckgo] ""AI will replace all the jobs!" Is Just Tech Execs"**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): neutral (0.7148)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Over the weekend, I went digging for evidence that AI can, will, or has replaced a large percent of jobs. It doesn’t exist. Worse than that, actually,..."

**[duckduckgo] "AI Will Replace Jobs: But Most People Still Aren’t Using It"**
  Type: web | Cred: estimated 0.40599999999999997
  NLI (nli_deberta): supporting (0.7339)
  Verdict contribution: supporting (weight: 0.298)
  Snippet: "AI Will Replace Jobs: But Most People Still Aren’t Using It ... day work week is coming in just 10 years, thanks to AI replacing humans ‘for most ......"

**[duckduckgo] "Geoffrey Hinton Warns AI Will Replace Most Jobs Soon - Bizmart"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.979)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Geoffrey Hinton AI job displacement is no longer a distant worry—it’s a real and growing threat, according to the AI pioneer himself. In a June 16 int..."

**[duckduckgo] "Generative AI and the future of work in America | McKinsey"**
  Type: web | Cred: estimated 0.429
  NLI (nli_deberta): opposing (0.917)
  Verdict contribution: opposing (weight: 0.3934)
  Snippet: "In fact, the occupational categories most exposed to generative AI could continue to add jobs through 2030 (Exhibit 4), although its adoption may ......"

**[wikidata] "Jobs"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "2013 film directed by Joshua Michael Stern | instance of: film..."

### Verdict computation
  Supporting weight: 0.298
  Opposing weight: 1.2915
  Support ratio: 0.1875
  Confidence: 0.6251
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 21

  Top supporting:
    - AI Will Replace Jobs: But Most People Still Aren’t Using It (weight: 0.298)
  Top opposing:
    - Why AI Won't Replace Most Jobs in 2026—but Will Reshape Work, (weight: 0.4003)
    - Generative AI and the future of work in America | McKinsey (weight: 0.3934)
    - Why can’t artificial intelligence replace most typing jobs? (weight: 0.3014)
    - Will AI replace most jobs? - (weight: 0.1965)

---
## 16. "the United States economy is in a recession"
Category: current_event
Expected: contested
Actual: likely supported (YES)
Claim type: factual (0.8)
Claim domain: current_events

### Sources collected: 25 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 4
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 25 -> 23 (dropped 2)
Dropped sources:
  - [encyclopedia] "Economy of Australia" (relevance: 0.3079, reason: relevance_0.308_below_0.35)
  - [web] "" (relevance: 0.0522, reason: relevance_0.052_below_0.35)

### Dedup: 23 -> 23 (dropped 0)

### Analyzed sources (23 total)

**[wikipedia] "List of recessions in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.7393)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "U.S. recessions have increasingly affected economies on a worldwide scale, especially as countries' economies become more intertwined. The unofficial ..."

**[wikipedia] "Great Recession in the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8472)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The financial sector sharply expanded, in part because investment banks were going public, bringing them vast sums of stockholder capital. From 1978 t..."

**[wikipedia] "Recession shapes"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9668)
  Verdict contribution: supporting (weight: 0.7734)
  Snippet: "V-shapes are the normal shape for a recession, as the strength of the economic recovery is typically closely related to the severity of the preceding ..."

**[wikipedia] "Economy of the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.959)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In 2014 and again in 2020, the International Trade Union Confederation graded the U.S. a 4 out of 5+, its third-lowest score, on the subject of worker..."

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

**[duckduckgo] "How likely is a US recession? How to prepare if one comes"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.981)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Oil price surges resulting from the Iran war drove inflation expectations and recession odds higher in March, according to a Moody's Analytics model. ..."

**[duckduckgo] "Is the US Economy Headed for a Recession? - Morningstar"**
  Type: web | Cred: estimated 0.331
  NLI (nli_deberta): opposing (0.979)
  Verdict contribution: opposing (weight: 0.324)
  Snippet: "Amid a sharp slowdown in the labor market and the ongoing impact of new tariffs on consumers and businesses, worries are mounting that the US economy ..."

**[duckduckgo] "NBER based Recession Indicators for the United States from the Period ..."**
  Type: web | Cred: estimated 0.5
  NLI (nli_deberta): neutral (0.937)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Federal Reserve Bank of St. Louis
Recession Indicators Series
+1 or 0, Not Seasonally Adjusted
Frequency:
This time series is an interpretation of US ..."

**[duckduckgo] "The U.S. Economy Was Shaky Before the Iran War. Now It's in Real ..."**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): opposing (0.936)
  Verdict contribution: opposing (weight: 0.7956)
  Snippet: "By experts and staff
- Published
- Roger W. Ferguson Jr.CFR ExpertSteven A. Tananbaum Distinguished Fellow for International Economics
- Research Asso..."

**[duckduckgo] "Ugly Trends Prove US Economy Close to Recession: Layoffs, Unemployment ..."**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9595)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "When things truly turn south, it usually comes as an abrupt shift that results in a negative self-reinforcing feedback loop. Instead of a slow increas..."

**[duckduckgo] "Roughly half of U.S. states are effectively in a recession ... - Fortune"**
  Type: web | Cred: verified 0.85 | Bias: right-center | Factual: high
  NLI (nli_deberta): supporting (0.7031)
  Verdict contribution: supporting (weight: 0.5976)
  Snippet: "- ANALYSIS: Despite strong national figures—3.8% GDP growth and 4.3% unemployment—large parts of the U.S. are effectively in recession, according to M..."

**[duckduckgo] "U.S. Economy at a Glance - Bureau of Economic Analysis"**
  Type: web | Cred: estimated 0.42000000000000004
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Perspective from the BEA Accounts BEA produces some of the most closely watched economic statistics that influence decisions of government officials, ..."

**[duckduckgo] "List of Recessions in the United States | Last Recession Stats & Facts"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9819)
  Verdict contribution: supporting (weight: 0.1964)
  Snippet: "The National Bureau of Economic Research (NBER), the official arbiter of recession dates in America, continues to track economic fluctuations with unp..."

**[duckduckgo] "Is the US in recession? - The Week"**
  Type: web | Cred: verified 0.85 | Bias: left | Factual: high
  NLI (nli_deberta): opposing (0.5444)
  Verdict contribution: opposing (weight: 0.4627)
  Snippet: "Is the US in recession?
‘Unofficial signals’ are flashing red
It often seems that economists are perpetually warning us about the next U.S. recession...."

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
  Supporting weight: 2.6871
  Opposing weight: 1.5824
  Support ratio: 0.6294
  Confidence: 0.2588
  Verdict: **likely supported**
  Neutral sources (no contribution): 15

  Top supporting:
    - The Economic Impacts of COVID-19: Evidence from a New Public Database Built Using Private Sector Data (weight: 0.7817)
    - Recession shapes (weight: 0.7734)
    - Roughly half of U.S. states are effectively in a recession ... - Fortune (weight: 0.5976)
    - The Coronavirus Stimulus Package: How Large is the Transfer Multiplier (weight: 0.338)
    - List of Recessions in the United States | Last Recession Stats & Facts (weight: 0.1964)
  Top opposing:
    - The U.S. Economy Was Shaky Before the Iran War. Now It's in Real ... (weight: 0.7956)
    - Is the US in recession? - The Week (weight: 0.4627)
    - Is the US Economy Headed for a Recession? - Morningstar (weight: 0.324)

---
## 17. "violent video games cause real world violence"
Category: contested
Expected: contested
Actual: likely opposed (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 32 total
  - google_factcheck: 3
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 7
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 32 -> 28 (dropped 4)
Dropped sources:
  - [encyclopedia] "Harvester (video game)" (relevance: 0.1665, reason: non_content_pattern)
  - [academic] "The Use of Social Media in Children and Adolescents: Scoping Review on the Potential Risks" (relevance: 0.3001, reason: relevance_0.300_below_0.35)
  - [academic] "The psychological drivers of misinformation belief and its resistance to correction" (relevance: 0.0695, reason: relevance_0.069_below_0.35)
  - [academic] "Misinformation: susceptibility, spread, and interventions to immunize the public" (relevance: 0.12, reason: relevance_0.120_below_0.35)

### Dedup: 28 -> 27 (dropped 1)

### Analyzed sources (27 total)

**[google_factcheck] "The Facts on Media Violence"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.774 | Rating: Learn What Research Shows
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The authors came to their conclusions because researchers have consistently found the effect across three different kinds of studies: cross-sectional ..."

**[google_factcheck] "Do Video Games Lead to Mass Shootings? Researchers Say No ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: The New York Times | Enriched: False | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Video games and violent movies lead to mass shootings...."

**[google_factcheck] "Fact check: Studies refute attempts to link video games, shootings"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.734 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Fact check: Claim of link between video games, school shootings refuted by studies
The claim: Post implies school shootings are linked to violent vide..."

**[wikipedia] "Violence and video games"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9385)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This study found no evidence that violent games caused aggression in minors. The author speculated that other studies may have been affected by "singl..."

**[wikipedia] "Nonviolent video game"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.7197)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In December 2001, Surgeon General David Satcher, led a study on violence in youth and determined that while the impact of video games on violent behav..."

**[wikipedia] "Graphic violence"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9858)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Several of these films have been banned from certain countries for their violent content. Though violence in films is not an old topic, a recent study..."

**[wikipedia] "Effects of violence in mass media"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9507)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Many social scientists support the correlation, however, some scholars argue that media research has methodological problems and that findings are exa..."

**[semantic_scholar] "Adolescent Aggression: A Narrative Review on the Potential Impact of Violent Video Games"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.6982)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Background: Exposure to violent content through video games can shape perceptions of aggression as normative or acceptable, potentially desensitizing ..."

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

**[semantic_scholar] "The Spoilers of Virtual War: Experience and Performance Mediate the Relationship Between Violent Video Games and Hostility"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.959)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A substantial portion of the literature investigating whether playing video games with violent content causes aggressive thoughts, feelings, and behav..."

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

**[duckduckgo] "The evidence that video game violence leads to real-world aggression | Washington State Magazine | Washington State University"**
  Type: web | Cred: estimated 0.40700000000000003
  NLI (nli_deberta): supporting (0.9194)
  Verdict contribution: supporting (weight: 0.3742)
  Snippet: "A 2018 meta-analysis found that there is a small increase in real-world physical aggression among adolescents and pre-teens who play violent video gam..."

**[duckduckgo] "Video Games | Pros, Cons, Debate, Arguments, Digital Media, Play, Violence, Aggression, & Conflict | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): opposing (0.6924)
  Verdict contribution: opposing (weight: 0.5885)
  Snippet: "For example, a 2019 study claimed conclusively that violent video games do not cause players to act violently, much less conduct mass shootings, in th..."

**[duckduckgo] "Do violent video games lead to real-world violence?"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): opposing (0.6909)
  Verdict contribution: opposing (weight: 0.5873)
  Snippet: "It’s like a sport," he said. He makes a living – and a happy one – from his PC.
"Through starting streaming, I learned a lot of practical skills. Ligh..."

**[duckduckgo] "Video games unlikely to cause real-world violence, experts say | CNN"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): opposing (0.5142)
  Verdict contribution: opposing (weight: 0.2571)
  Snippet: "As mass shootings roil the nation, President Trump and top Republicans are citing video games as one explanation for the bloodshed. But experts say th..."

**[duckduckgo] "Do Video Games Cause Violence in Real Life? | HowStuffWorks"**
  Type: web | Cred: estimated 0.44800000000000006
  NLI (nli_deberta): opposing (0.9458)
  Verdict contribution: opposing (weight: 0.4237)
  Snippet: "May 9, 2024 - More recently, Stanford Researchers ... themes and violent crime. "Current medical research and scholarship have not found any causal li..."

**[duckduckgo] "Violence in Video Games - the ESA"**
  Type: web | Cred: estimated 0.40099999999999997
  NLI (nli_deberta): opposing (0.98)
  Verdict contribution: opposing (weight: 0.393)
  Snippet: "June 21, 2024 - Real-world evidence makes it clear that there is no causal link between video games and violent behavior...."

**[duckduckgo] "The link between video game violence and real life violence - Violence Lab"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9775)
  Verdict contribution: supporting (weight: 0.1955)
  Snippet: "Video games are popular in Croatia. Some evidence on the popularity of video games in Croatia could stem from the fact that the PlayStation logo is th..."

**[duckduckgo] "Just a game? Study shows no evidence that violent video games lead to real-life violence | EurekAlert!"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): neutral (0.8491)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "But before governments introduce any policies restricting access to violent video games, it is important to establish whether violent video games do i..."

**[duckduckgo] "Analysis: Why it's time to stop blaming video games for real-world violence | PBS News"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.5474)
  Verdict contribution: supporting (weight: 0.4653)
  Snippet: "Reviewing all the scholarly literature My own research has examined the degree to which violent video games can – or can't – predict youth aggression ..."

### Verdict computation
  Supporting weight: 1.035
  Opposing weight: 3.8985
  Support ratio: 0.2098
  Confidence: 0.5804
  Verdict: **likely opposed**
  Neutral sources (no contribution): 16

  Top supporting:
    - Analysis: Why it's time to stop blaming video games for real-world violence | PBS News (weight: 0.4653)
    - The evidence that video game violence leads to real-world aggression | Washington State Magazine | Washington State University (weight: 0.3742)
    - The link between video game violence and real life violence - Violence Lab (weight: 0.1955)
  Top opposing:
    - Do Video Games Lead to Mass Shootings? Researchers Say No ... (weight: 0.8075)
    - Video Games | Pros, Cons, Debate, Arguments, Digital Media, Play, Violence, Aggression, & Conflict | Britannica (weight: 0.5885)
    - Do violent video games lead to real-world violence? (weight: 0.5873)
    - A Positive Side of Violent Video Game Play (weight: 0.4547)
    - Do Video Games Cause Violence in Real Life? | HowStuffWorks (weight: 0.4237)

---
## 18. "smoking causes lung cancer"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.8)
Claim domain: scientific

### Sources collected: 33 total
  - google_factcheck: 4
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 7
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 33 -> 32 (dropped 1)
Dropped sources:
  - [encyclopedia] "Joseph Berkson" (relevance: 0.0673, reason: relevance_0.067_below_0.35)

### Dedup: 32 -> 31 (dropped 1)

### Analyzed sources (31 total)

**[google_factcheck] "Smoking had been identified as a causative factor for lung cancer by ..."**
  Type: fact_check | Cred: estimated 0.85
  Publisher: AFP Fact Check | Enriched: True | Extract score: 0.805 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Smoking had been identified as a causative factor for lung cancer by 1958, US health authority says
- Published on July 30, 2020 at 11:00
- By AFP Aus..."

**[google_factcheck] "Science stubs out claim smoking doesn't cause cancer"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: AAP | Enriched: True | Extract score: 0.815 | Rating: False. Decades of scientific studies have established links between tobacco smoking and a range of cancers.
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "WHAT WAS CLAIMED
Smoking doesn’t cause cancer. OUR VERDICT
False. Decades of scientific studies have established links between tobacco smoking and a r..."

**[google_factcheck] "Can marijuana smoking cause lung cancer?"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.830 | Rating: Half True
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "We found some evidence to support Morgan’s statement, but the research comes with significant caveats and experts say more research is needed to reach..."

**[google_factcheck] "Does Marijuana Contain More Tar Than Cigarettes?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes | Enriched: True | Extract score: 0.951 | Rating: Mixture
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There are 33 cancer-causing chemicals contained in marijuana. Marijuana smoke also deposits tar into the lungs. In fact, when equal amounts of marijua..."

**[wikipedia] "Tobacco packaging warning messages"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.4683)
  Verdict contribution: opposing (weight: 0.3981)
  Snippet: "A 2009 science review determined that there is "clear evidence that tobacco package health warnings increase consumers' knowledge about the health con..."

**[wikipedia] "Lung cancer"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.981)
  Verdict contribution: supporting (weight: 0.9319)
  Snippet: "Lung cancer is caused by genetic damage to the DNA of cells in the airways, often caused by cigarette smoking or inhaling damaging chemicals. Damaged ..."

**[wikipedia] "Smoking-related interstitial fibrosis (SRIF)"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.606)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Note that the excess collagen in SRIF gives the air sacs a pink color. Diagnostic method Pathology
Differential diagnosis Non-specific interstitial pn..."

**[wikipedia] "Smoking in China"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.5708)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Wu Yiqun, vice executive director with the Beijing-based Thinktank Research Center for Health Development, criticized China's tobacco industry supervi..."

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

**[open_alex] "Implications of the Immune Landscape in COPD and Lung Cancer: Smoking Versus Other Causes"**
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

**[duckduckgo] "Lung Cancer Causes | Lung Cancer in Non-Smokers"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.9416)
  Snippet: "What Causes Lung Cancer? We don’t know what causes each case of lung cancer. But we do know many of the risk factors for these cancers (see Lung Cance..."

**[duckduckgo] "Lung cancer - Causes - NHS"**
  Type: web | Cred: estimated 0.41600000000000004
  NLI (nli_deberta): neutral (0.8643)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Most cases of lung cancer are caused by smoking, although people who have never smoked can also develop the condition. Smoking cigarettes is the singl..."

**[duckduckgo] "How does smoking cause cancer? | Cancer Research UK"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9956)
  Verdict contribution: supporting (weight: 0.4022)
  Snippet: "Smoking, tobacco and cancer
Smoking causes at least 16 different types of cancer and is the biggest cause of lung cancer in the UK, and worldwide. Smo..."

**[duckduckgo] "Lung Cancer Causes & Risk Factors | American Lung Association"**
  Type: web | Cred: verified 0.85 | Bias: pro-science/left-center | Factual: high
  NLI (nli_deberta): supporting (0.8838)
  Verdict contribution: supporting (weight: 0.7512)
  Snippet: "What Causes Lung Cancer? Anyone can get lung cancer. Lung cancer happens when cells in the lung mutate or change. Various factors can cause this mutat..."

**[duckduckgo] "How Smoking Causes Lung Cancer"**
  Type: web | Cred: estimated 0.477
  NLI (nli_deberta): supporting (0.6821)
  Verdict contribution: supporting (weight: 0.3254)
  Snippet: "You know by now that cigarette smoking is the No. 1 risk factor for lung cancer. "About 85 percent of lung cancer diagnoses are in current and former ..."

**[duckduckgo] "How Many Cigarettes Do You Need to Smoke to Get Cancer?"**
  Type: web | Cred: verified 0.5 | Bias: pro-science | Factual: mixed
  NLI (nli_deberta): supporting (0.9678)
  Verdict contribution: supporting (weight: 0.4839)
  Snippet: "Smoking cigarettes increases your risk of cancer. Quitting smoking is your best choice for lowering your risk. We know that smoking cigarettes increas..."

**[duckduckgo] "Lung Cancer Causes and Risks Explained at kokilaben hospital"**
  Type: web | Cred: estimated 0.23399999999999999
  NLI (nli_deberta): supporting (0.9878)
  Verdict contribution: supporting (weight: 0.2311)
  Snippet: "What causes lung cancer isn’t always straightforward. Smoking is the leading cause, responsible for about 85% of cases. But what about the remaining 1..."

**[duckduckgo] "What Causes Lung Cancer?"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9526)
  Verdict contribution: supporting (weight: 0.8097)
  Snippet: "Lung cancer can develop many years after you have inhaled the damaging fumes. A variety of things cause lung cancer. Cigarette smoke. Smoking causes a..."

**[duckduckgo] "What Causes Lung Cancer? Scary Risks Found - Liv Hospital"**
  Type: web | Cred: estimated 0.327
  NLI (nli_deberta): supporting (0.7642)
  Verdict contribution: supporting (weight: 0.2499)
  Snippet: "It’s important for patients to know this to help in their care. We’ve seen a big jump in patient-physician talks because of COVID-19.
Key Takeaways
- ..."

**[duckduckgo] "Vaping likely to cause cancer: new findings"**
  Type: web | Cred: estimated 0.409
  NLI (nli_deberta): supporting (0.5415)
  Verdict contribution: supporting (weight: 0.2215)
  Snippet: "A comprehensive review led by cancer researchers at UNSW found vaping is likely to cause lung and oral cancer – even before long-term studies can conf..."

### Verdict computation
  Supporting weight: 11.8569
  Opposing weight: 0.3981
  Support ratio: 0.9675
  Confidence: 0.935
  Verdict: **strongly supported**
  Neutral sources (no contribution): 10

  Top supporting:
    - Lung Cancer Causes | Lung Cancer in Non-Smokers (weight: 0.9416)
    - Lung cancer (weight: 0.9319)
    - What Causes Lung Cancer? (weight: 0.8097)
    - Epidemiology of lung cancer (weight: 0.7973)
    - Lung cancer statistics, 2023 (weight: 0.7894)
  Top opposing:
    - Tobacco packaging warning messages (weight: 0.3981)

---
## 19. "capitalism is better than socialism"
Category: opinion
Expected: opinion
Actual: sources divided (YES)
Claim type: opinion (0.95)
Claim domain: general

### Sources collected: 45 total
  - google_factcheck: 1
  - wikipedia: 5
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 45 -> 31 (dropped 14)
Dropped sources:
  - [fact_check] "Quote Falsely Tied to Ocasio-Cortez" (relevance: 0.3203, reason: relevance_0.320_below_0.35)
  - [academic] "Liberating Enslaved Humanity: Decolonial Political Thought of Abul Hashim" (relevance: 0.1855, reason: relevance_0.186_below_0.35)
  - [academic] "Vietnam tourism at the crossroads of socialism and market economy" (relevance: 0.1747, reason: relevance_0.175_below_0.35)
  - [academic] "African solutions to African problems: a narrative of corruption in postcolonial Africa" (relevance: 0.161, reason: relevance_0.161_below_0.35)
  - [academic] "The internal fragility of representative democracy: was Schumpeter right?" (relevance: 0.2505, reason: relevance_0.251_below_0.35)
  - [academic] "Deliberative Democracy or Agonistic Pluralism?" (relevance: 0.2532, reason: relevance_0.253_below_0.35)
  - [academic] "Economic growth and income inequality" (relevance: 0.1935, reason: relevance_0.193_below_0.35)
  - [academic] "Sustainalism: An Integrated Socio-Economic-Environmental Model to Address Sustainable Development and Sustainability" (relevance: 0.3049, reason: relevance_0.305_below_0.35)
  - [academic] "Critiques of the circular economy" (relevance: 0.2445, reason: relevance_0.244_below_0.35)
  - [web] "Link to reddit.com" (relevance: 0.004, reason: relevance_0.004_below_0.35)
  - [knowledge_graph] "Better" (relevance: 0.1345, reason: relevance_0.134_below_0.35)
  - [knowledge_graph] "Better" (relevance: 0.0358, reason: relevance_0.036_below_0.35)
  - [knowledge_graph] "better85 (Conrad Honey)" (relevance: 0.1184, reason: relevance_0.118_below_0.35)
  - [knowledge_graph] "Socialism and Freedom Party" (relevance: 0.2973, reason: relevance_0.297_below_0.35)

### Dedup: 31 -> 28 (dropped 3)

### Analyzed sources (28 total)

**[wikipedia] "Late capitalism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9927)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Particularly in the 1970s and 1980s, many economic and political analyses of late capitalism were published. From the 1990s onward, the academic analy..."

**[wikipedia] "Authoritarian socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9609)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Reason Foundation. Retrieved 22 April 2020.
- ^ Hayek, Friedrich (1976). Law, Legislation and Liberty. Vol. 2. Chicago: University of Chicago Press. p..."

**[wikipedia] "Socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.96)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "You're really tampering and getting on dangerous ground because you are messing with folk then. You are messing with captains of industry. Now this me..."

**[wikipedia] "Market socialism"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9409)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Proponents of early market socialism include the Ricardian socialist economists, the classical liberal philosopher John Stuart Mill and the anarchist ..."

**[wikipedia] "Scientific socialism"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.9639)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It contrasts with utopian socialism by basing itself upon material conditions instead of concoctions and ideas, where "the final causes of all social ..."

**[open_alex] "Would Democratic Socialism Be Better?"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.791)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract The case for a modern democratic humane socialism typically has two parts. The first is that capitalism is bad, at or least not very good. In..."

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

**[semantic_scholar] "Global Capitalism and Climate Change: The Need for an Alternative System by Hans A. Baer"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9824)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It is something of a cliché to quote Karl Marx’s (1845) observation in Eleven Theses on Feuerbach, where he wrote, “The philosophers have only interpr..."

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

**[duckduckgo] "Debunking Myths About Capitalism—Why Capitalism is Better Than..."**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.9917)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[duckduckgo] "Is Capitalism Better Than Socialism? Bryan Caplan and Elizabeth..."**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9697)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "I'd say that capitalism is at least ok, while socialism is hell on earth.
“Capitalism” and “socialism“—what do these words even mean? You could just s..."

**[duckduckgo] "5 Reasons Socialism Is Inferior To Capitalism"**
  Type: web | Cred: verified 0.5 | Bias: right | Factual: mixed
  NLI (nli_deberta): supporting (0.8208)
  Verdict contribution: supporting (weight: 0.4104)
  Snippet: ""The inherent vice of capitalism is the unequal sharing of blessings; the inherent virtue of socialism is the equal sharing of miseries." -- Winston C..."

**[duckduckgo] "Why Capitalism is Better than Socialism | Free Essay Example"**
  Type: web | Cred: estimated 0.37
  NLI (nli_deberta): supporting (0.8716)
  Verdict contribution: supporting (weight: 0.3225)
  Snippet: "Therefore, capitalism is better than socialism because it allows for efficient resource allocation, economic growth rate, increased personal freedom, ..."

**[duckduckgo] "20 Quotes That Explain Why Capitalism Is Better Than Socialism - AEI"**
  Type: web | Cred: verified 0.5 | Bias: right | Factual: mixed
  NLI (nli_deberta): neutral (0.5503)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Good collection of 20 quotes from John Hawkins on PJMedia, here are five favorites:
1. From Ayn Rand:
America’s abundance was created not by public sa..."

**[duckduckgo] "Comparing Socialism and Capitalism"**
  Type: web | Cred: estimated 0.42300000000000004
  NLI (nli_deberta): neutral (0.9565)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "(iii) When arguing that capitalism is better than socialism, Brennan often refers to the virtues of markets. But this neglects the varieties of social..."

**[duckduckgo] "(doc) this house believes that capitalism is better than socialism"**
  Type: web | Cred: estimated 0.45599999999999996
  NLI (nli_deberta): supporting (0.6665)
  Verdict contribution: supporting (weight: 0.3039)
  Snippet: "THIS HOUSE BELIEVES THAT CAPITALISM IS BETTER THAN SOCIALISM
Sign up for access to the world's latest research
AbstractAI
The paper argues in favor of..."

**[duckduckgo] "5 Key Reasons Capitalism Is Better Than Socialism"**
  Type: web | Cred: estimated 0.327
  NLI (nli_deberta): neutral (0.8848)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Image Credits: HYPELINE
The majority of us would agree that being able to own our own business and keep most of our hard-earned income is a good thing..."

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
  Supporting weight: 1.0368
  Opposing weight: 1.4948
  Support ratio: 0.4096
  Confidence: 0.1809
  Verdict: **sources divided**
  Neutral sources (no contribution): 21

  Top supporting:
    - 5 Reasons Socialism Is Inferior To Capitalism (weight: 0.4104)
    - Why Capitalism is Better than Socialism | Free Essay Example (weight: 0.3225)
    - (doc) this house believes that capitalism is better than socialism (weight: 0.3039)
  Top opposing:
    - Socialism (weight: 0.5484)
    - Cows, Moonshine, Pheasants … versus Soybeans (weight: 0.3936)
    - Is a capitalist steady-state economy possible? Is it better in socialism? (weight: 0.2997)
    - Would Democratic Socialism Be Better Than Social Democratic Capitalism? (weight: 0.2531)

---
## 20. "we only use 10% of our brains"
Category: factual_false
Expected: strongly opposed
Actual: contested (**NO - MISMATCH**)
Claim type: factual (0.8)
Claim domain: statistical

### Sources collected: 34 total
  - google_factcheck: 2
  - wikipedia: 5
  - semantic_scholar: 10
  - open_alex: 1
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 34 -> 17 (dropped 17)
Dropped sources:
  - [encyclopedia] "Boltzmann brain" (relevance: 0.3062, reason: relevance_0.306_below_0.35)
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: 0.1611, reason: relevance_0.161_below_0.35)
  - [encyclopedia] "Equipotentiality" (relevance: 0.2951, reason: relevance_0.295_below_0.35)
  - [encyclopedia] "Bad Brains" (relevance: 0.195, reason: relevance_0.195_below_0.35)
  - [academic] "WE ONLY USE 10% OF OUR BRAINS AND OTHER NEUROMYTHS – A SURVEY OF TEACHERS IN BOSNIA AND HERZEGOVINA" (relevance: 0.2946, reason: relevance_0.295_below_0.35)
  - [academic] "Resting-State Functional Connectivity Predicts Attention Problems in Children: Evidence from the ABCD Study" (relevance: 0.219, reason: relevance_0.219_below_0.35)
  - [academic] "Minimal progress toward sustainment: 10-year replication of substance use EBP sustainment trajectories and associations with implementation characteristics" (relevance: 0.0485, reason: relevance_0.049_below_0.35)
  - [academic] "Physician Interactions Associated With Increased Reception of Substance Use Disorder Treatment" (relevance: 0.0885, reason: relevance_0.089_below_0.35)
  - [academic] "A 10-year Longitudinal Study of Social Media Use in Education" (relevance: 0.0348, reason: relevance_0.035_below_0.35)
  - [academic] "Longitudinal study of risk factors predicting cannabis use disorder in UK young adults and adolescents" (relevance: 0.1822, reason: relevance_0.182_below_0.35)
  - [academic] "Profiles of problematic pornography use and religiosity-based moral incongruence using latent profile analysis: A two-sample study" (relevance: 0.1253, reason: relevance_0.125_below_0.35)
  - [academic] "Investigating the bidirectional association between alcohol use and suicidal thoughts and behaviors in a population from the United States" (relevance: 0.1015, reason: relevance_0.101_below_0.35)
  - [academic] "Association Between Smartphone Use and Depressive Symptoms Among Chinese Older Adults" (relevance: 0.1167, reason: relevance_0.117_below_0.35)
  - [academic] "Classification of diseases with accumulation of Tau protein" (relevance: 0.1625, reason: relevance_0.162_below_0.35)
  - [knowledge_graph] "Wednesday" (relevance: -0.0112, reason: relevance_-0.011_below_0.35)
  - [knowledge_graph] "Welsh" (relevance: -0.0272, reason: relevance_-0.027_below_0.35)
  - [knowledge_graph] "West Germany" (relevance: 0.0257, reason: relevance_0.026_below_0.35)

### Dedup: 17 -> 14 (dropped 3)

### Analyzed sources (14 total)

**[google_factcheck] "Do We Only Use 10% of our Brains?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes | Enriched: True | Extract score: 0.911 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Someone has taken most of your brain away, and you probably didn't even know it. Well, not taken your brain away, exactly, but decided that you don't ..."

**[google_factcheck] "Image Accurately Depicts a 1 Cubic Millimeter Sample of a Human ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes.com | Enriched: True | Extract score: 0.700 | Rating: True
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Picture of 1 cubic millimeter of brain
byu/DE4DM4N5H4ND inpics
A Google keyword search returned dozens of relevant results, including a Smithsonian Ma..."

**[wikipedia] "Ten-percent-of-the-brain myth"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.7842)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Ten-percent-of-the-brain myth
The ten-percent-of-the-brain myth or ninety-percent-of-the-brain myth states that humans generally use only one-tenth (o..."

**[semantic_scholar] "Do we mostly use only 10% of our brain? Prevalence and correlates of misconceptions on creativity and neuroscience in a culturally diverse sample"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9565)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Do we mostly use only 10% of our brain? Prevalence and correlates of misconceptions on creativity and neuroscience in a culturally diverse sample..."

**[duckduckgo] "Ten percent of the brain myth - Wikipedia"**
  Type: web | Cred: estimated 0.756
  NLI (nli_deberta): opposing (0.6855)
  Verdict contribution: opposing (weight: 0.5182)
  Snippet: "1999), "Whence Cometh the Myth that We Only Use 10% of our Brains?", in Della Sala, Sergio (ed.), Mind Myths: Exploring Popular Assumptions About the ..."

**[duckduckgo] "Do People Only Use 10 Percent of Their Brains? | Scientific"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9053)
  Verdict contribution: supporting (weight: 0.7695)
  Snippet: "So it's no surprise that the brain remains a mystery unto itself. Adding to that mystery is the contention that humans "only" employ 10 percent of the..."

**[duckduckgo] "Myth: We Only Use 10% of Our Brains – Association for"**
  Type: web | Cred: estimated 0.333
  NLI (nli_deberta): supporting (0.8672)
  Verdict contribution: supporting (weight: 0.2888)
  Snippet: "If we only use 10% of our brain, then a PET scan should look like Slide 2 in the accompanying PowerPoint slides . ... we are sleeping we only use 10% ..."

**[duckduckgo] "We only use 10% of our brains? That’s 100% wrong"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.6055)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The “we only use 10% of our brains” claim would mean that we’re effectively evolving in the opposite direction—and that we’re doing this ......"

**[duckduckgo] "Do we only use 10 percent of our brain? - MIT McGovern Institute"**
  Type: web | Cred: estimated 0.413
  NLI (nli_deberta): opposing (0.7603)
  Verdict contribution: opposing (weight: 0.314)
  Snippet: "Do we only use 10 percent of our brain? The human brain houses incredibly complex and advanced functions—but do we only access a fraction of it? Movie..."

**[duckduckgo] "Do we only use 10% of our brains? | Science Questions"**
  Type: web | Cred: estimated 0.252
  NLI (nli_deberta): supporting (0.5425)
  Verdict contribution: supporting (weight: 0.1367)
  Snippet: "Etienne Mustow via Facebook asked:
“Is it true that we only use 10% of our brains and if so, why? What happens to the remaining 90% of our brain?”
Pro..."

**[duckduckgo] "Do we really use only 10 percent of our brains? | Scientific"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.771)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Barry L. Beyerstein of the Brain Behavior Laboratory at Simon Fraser University in Vancouver explains. Whenever I venture out of the Ivory Tower to de..."

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
  Supporting weight: 1.195
  Opposing weight: 1.3072
  Support ratio: 0.4776
  Confidence: 0.0449
  Verdict: **contested**
  Neutral sources (no contribution): 8

  Top supporting:
    - Do People Only Use 10 Percent of Their Brains? | Scientific (weight: 0.7695)
    - Myth: We Only Use 10% of Our Brains – Association for (weight: 0.2888)
    - Do we only use 10% of our brains? | Science Questions (weight: 0.1367)
  Top opposing:
    - Ten percent of the brain myth - Wikipedia (weight: 0.5182)
    - Do We Only Use 10% of our Brains? (weight: 0.475)
    - Do we only use 10 percent of our brain? - MIT McGovern Institute (weight: 0.314)

---
## 21. "social media is harmful to mental health"
Category: contested
Expected: contested
Actual: sources lean supporting (YES)
Claim type: opinion (0.9)
Claim domain: scientific

### Sources collected: 38 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 7
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 38 -> 29 (dropped 9)
Dropped sources:
  - [encyclopedia] "Mental disorder" (relevance: 0.3484, reason: relevance_0.348_below_0.35)
  - [encyclopedia] "List of mental disorders" (relevance: 0.3266, reason: relevance_0.327_below_0.35)
  - [knowledge_graph] "social media" (relevance: 0.3389, reason: relevance_0.339_below_0.35)
  - [knowledge_graph] "influencer" (relevance: 0.2684, reason: relevance_0.268_below_0.35)
  - [knowledge_graph] "substance abuse" (relevance: 0.2207, reason: relevance_0.221_below_0.35)
  - [knowledge_graph] "alcohol abuse" (relevance: 0.2104, reason: relevance_0.210_below_0.35)
  - [knowledge_graph] "Harmful Algae" (relevance: 0.1955, reason: relevance_0.196_below_0.35)
  - [knowledge_graph] "mental health" (relevance: 0.3414, reason: relevance_0.341_below_0.35)
  - [knowledge_graph] "mental disorder" (relevance: 0.3476, reason: relevance_0.348_below_0.35)

### Dedup: 29 -> 27 (dropped 2)

### Analyzed sources (27 total)

**[wikipedia] "Digital media use and mental health"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9805)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is limited evidence supporting the effectiveness of cognitive behavioral therapy and family-based interventions for treating problematic digital..."

**[wikipedia] "Mental illness in media"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.832)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Another study examined 40 children's programs on Netflix, analyzing 339 episodes for references to mental illness. The study found that 23 of these pr..."

**[wikipedia] "The Anxious Generation"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.8428)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Building on research from his coauthored book The Coddling of the American Mind, Haidt argues that risk-taking has been discouraged by "safetyism" whe..."

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

**[duckduckgo] "Is social media bad for you? The evidence and the unknowns"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.8882)
  Verdict contribution: supporting (weight: 0.755)
  Snippet: "What does the evidence actually suggest? Since social media is relatively new to us, conclusive findings are limited. The research that does exist mai..."

**[duckduckgo] "Instagram ranked worst for young people's mental health |"**
  Type: web | Cred: estimated 0.262
  NLI (nli_deberta): supporting (0.9839)
  Verdict contribution: supporting (weight: 0.2578)
  Snippet: "Instagram ranked worst for young people's mental health
Author: RSPH 19 May 2017 1 min read
A new report has revealed the positive and negative effect..."

**[duckduckgo] "Social Media and Teens’ Mental Health: What Teens and Their"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.6675)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This survey seeks to surface teens’ and their parents’ perspectives on this topic, not to supply evidence or establish causality. We used the overarch..."

**[duckduckgo] "Using Social Media Doesn't Necessarily Harm Mental Health:"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9844)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The idea that using the internet including using social media apps and smartphones can harm mental health has been disputed by a new global study publ..."

**[duckduckgo] "Is Social Media Helpful or Harmful for Mental Health? - Dr."**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.8032)
  Verdict contribution: supporting (weight: 0.241)
  Snippet: "Excessive and unhealthy use of social media can have devastating effects on mental health, especially in adolescents. The exact ramifications of socia..."

**[duckduckgo] "See How Social Media Seriously Harms Your Mental Health | 2022"**
  Type: web | Cred: estimated 0.246
  NLI (nli_deberta): supporting (0.9883)
  Verdict contribution: supporting (weight: 0.2431)
  Snippet: "In this article, we will talk about how the impacts of social media on mental health and how social media seriously harms your mental health. Table of..."

**[duckduckgo] "Social media mental health harms might be due to exposure to"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "It is the first observational study to track social media use and mental health over these important early adolescent years with enough participants ...."

**[duckduckgo] "How Social Media Affects Your Teen’s Mental Health: A"**
  Type: web | Cred: estimated 0.33399999999999996
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.3324)
  Snippet: "How Social Media Affects Your Teen’s Mental Health: A Parent’s Guide
[Originally published: Jan. 8, 2024. Updated: June 17, 2024.]
Mental health issue..."

**[duckduckgo] "Social Media Seriously Harms Your Mental Health - Zitrotinta"**
  Type: web | Cred: estimated 0.331
  NLI (nli_deberta): supporting (0.9897)
  Verdict contribution: supporting (weight: 0.3276)
  Snippet: "Do you think the idea that Social Media Seriously Harms Your Mental Health? This is a question that many people have been asking themselves, and the a..."

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
  Supporting weight: 5.1998
  Opposing weight: 0.5065
  Support ratio: 0.9112
  Confidence: 0.8225
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 14

  Top supporting:
    - Is social media bad for you? The evidence and the unknowns (weight: 0.755)
    - Exploring adolescents’ perspectives on social media and mental health and well-being – A qualitative literature review (weight: 0.7398)
    - Broken Shields: Holding Social Media Giants Accountable for the Youth Mental Health Crisis (weight: 0.5441)
    - Public and mental health professionals’ perspectives on social media and suicide exposure (weight: 0.5387)
    - Debate: Social media in children and young people – time for a ban? From polarised debate to precautionary action – a population mental health perspective on social media and youth well‐being (weight: 0.5369)
  Top opposing:
    - Social Media–Driven Routes to Positive Mental Health Among Youth: Qualitative Enquiry and Concept Mapping Study (weight: 0.5065)

---
## 22. "the Beatles are the greatest band of all time"
Category: opinion
Expected: opinion
Actual: sources lean supporting (YES)
Claim type: opinion (0.85)
Claim domain: general

### Sources collected: 21 total
  - google_factcheck: 0
  - wikipedia: 5
  - duckduckgo: 10
  - wikidata: 6
  - semantic_scholar: SKIPPED (disabled by routing)
  - open_alex: SKIPPED (disabled by routing)

### Relevance filter: 21 -> 18 (dropped 3)
Dropped sources:
  - [knowledge_graph] "Time" (relevance: 0.1062, reason: relevance_0.106_below_0.35)
  - [knowledge_graph] "time" (relevance: 0.0729, reason: relevance_0.073_below_0.35)
  - [knowledge_graph] "Time" (relevance: 0.1418, reason: relevance_0.142_below_0.35)

### Dedup: 18 -> 17 (dropped 1)

### Analyzed sources (17 total)

**[wikipedia] "Rolling Stone's 500 Greatest Songs of All Time"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Rolling Stone's 500 Greatest Songs of All Time
"The 500 Greatest Songs of All Time" is a recurring song ranking compiled by the American magazine Roll..."

**[wikipedia] "With the Beatles"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With the Beatles
Producer George Martin
The Beatles chronology
The Beatles North American chronology
The Beatles Canadian chronology
With the Beatles ..."

**[wikipedia] "The Beatles albums discography"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9668)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Beatles' international discography is complicated due to different versions of their albums sometimes being released in other countries, particula..."

**[wikipedia] "Revolver (Beatles album)"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.936)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "They confirmed their choice in a telegram to EMI, sent from the Tokyo Hilton on 2 July.
[edit]We'll lose some fans with [the new album], but we'll als..."

**[wikipedia] "The Beatles"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Beatles toured Japan the month after the Yesterday and Today furore, facing death threats from Japanese Conservatives due to the Beatles unknowing..."

**[duckduckgo] "Does anyone here believe The Beatles are the greatest band of all ..."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.584)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Apr 30, 2024 · The Beatles were, and remain, the best recording artists ever. I don't consider them the greatest band because they stopped touring jus..."

**[duckduckgo] "Why The Beatles Are the Greatest Band of All Time (Lessons from ..."**
  Type: web | Cred: estimated 0.22400000000000003
  NLI (nli_deberta): supporting (0.5825)
  Verdict contribution: supporting (weight: 0.1305)
  Snippet: "I’ve spent much of 2025 studying legends – iconic figures and innovators across fields – and one name keeps coming up as the gold standard in music: T..."

**[duckduckgo] "Why The Beatles are the Greatest Band in History - Bearcast Media"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9463)
  Verdict contribution: supporting (weight: 0.1893)
  Snippet: "“Who is the greatest band in history?” This, my friends, is where I thrive. The first memory I have ever had involved listening to the Abbey Road albu..."

**[duckduckgo] "Why are The Beatles called the greatest band in music history? I'm ..."**
  Type: web | Cred: estimated 0.487
  NLI (nli_deberta): neutral (0.9263)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Oct 9, 2023 · Because they were the best ever no one has surpassed them in any way musically, sales and so many different parts of the recording indus..."

**[duckduckgo] "The Beatles: The greatest band ever Period. - Facebook"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9653)
  Verdict contribution: supporting (weight: 0.4827)
  Snippet: "Feb 24, 2024 · The Beatles were the best rock band ever. They kept reinventing themselves. Every album every song they were always making them better...."

**[duckduckgo] "OPINION: Why the Beatles are the best band of all time"**
  Type: web | Cred: estimated 0.29900000000000004
  NLI (nli_deberta): supporting (0.6982)
  Verdict contribution: supporting (weight: 0.2088)
  Snippet: "OPINION: Why the Beatles are the best band of all time
February 23, 2017
“Help, I need somebody,” once belted out the late John Lennon. “Let it be,” r..."

**[duckduckgo] "Why The Beatles Were the Greatest Band | The Riff - Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sep 24, 2021 · The Beatles revolutionised not only popular music but also culture, recording techniques, and touring...."

**[duckduckgo] "Beatles as the "greatest band of all time" | Fab Forum"**
  Type: web | Cred: estimated 0.253
  NLI (nli_deberta): supporting (0.9009)
  Verdict contribution: supporting (weight: 0.2279)
  Snippet: "Apr 25, 2016 · Beatles as the "greatest band of all time" | Fab Forum | The Beatles Bible ... The Beatles were the greatest band of all time...for me...."

**[duckduckgo] "The Beatles are the greatest band of all time. Here's why | Classical Music"**
  Type: web | Cred: estimated 0.277
  NLI (nli_deberta): neutral (0.9688)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "We listened to it endlessly, transfixed by the string orchestra in ‘Eleanor Rigby’ and the asymmetric melody of ‘Good Day Sunshine’. We loved it. A ye..."

**[duckduckgo] "Are the Beatles or Led Zeppelin the greatest band ever? - HubPages"**
  Type: web | Cred: estimated 0.511
  NLI (nli_deberta): supporting (0.6743)
  Verdict contribution: supporting (weight: 0.3446)
  Snippet: "But I guess if I had to choose I would say I would take my Beatles CDs to the bunker. In any event they are both great !
The Beatles are, BY FAR, the ..."

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
  Supporting weight: 1.5836
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 11

  Top supporting:
    - The Beatles: The greatest band ever Period. - Facebook (weight: 0.4827)
    - Are the Beatles or Led Zeppelin the greatest band ever? - HubPages (weight: 0.3446)
    - Beatles as the "greatest band of all time" | Fab Forum (weight: 0.2279)
    - OPINION: Why the Beatles are the best band of all time (weight: 0.2088)
    - Why The Beatles are the Greatest Band in History - Bearcast Media (weight: 0.1893)

---
## 23. "antibiotics do not work against viruses"
Category: factual_true
Expected: strongly supported
Actual: likely supported (YES)
Claim type: factual (0.8)
Claim domain: general

### Sources collected: 40 total
  - google_factcheck: 2
  - wikipedia: 5
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 40 -> 29 (dropped 11)
Dropped sources:
  - [encyclopedia] "Respiratory syncytial virus" (relevance: 0.3371, reason: relevance_0.337_below_0.35)
  - [encyclopedia] "Travelers' diarrhea" (relevance: 0.279, reason: relevance_0.279_below_0.35)
  - [academic] "Identification and dynamics of novel scaffolds against Enterococcus faecium serine hydroxymethyltransferase enzyme: a potential target for antibiotics development" (relevance: 0.3433, reason: relevance_0.343_below_0.35)
  - [academic] "Surviving sepsis campaign: international guidelines for management of sepsis and septic shock 2021" (relevance: 0.0929, reason: relevance_0.093_below_0.35)
  - [academic] "Microbiota in health and diseases" (relevance: 0.2449, reason: relevance_0.245_below_0.35)
  - [academic] "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021" (relevance: 0.1313, reason: relevance_0.131_below_0.35)
  - [academic] "Antimicrobial Face Shield: Next Generation of Facial Protective Equipment against SARS-CoV-2 and Multidrug-Resistant Bacteria" (relevance: 0.3201, reason: relevance_0.320_below_0.35)
  - [academic] "Infectious disease in an era of global change" (relevance: 0.3208, reason: relevance_0.321_below_0.35)
  - [academic] "2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure" (relevance: 0.0334, reason: relevance_0.033_below_0.35)
  - [academic] "Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050" (relevance: 0.3029, reason: relevance_0.303_below_0.35)
  - [academic] "Emerging concepts in the science of vaccine adjuvants" (relevance: 0.2199, reason: relevance_0.220_below_0.35)

### Dedup: 29 -> 29 (dropped 0)

### Analyzed sources (29 total)

**[google_factcheck] "Consuming antibiotics cannot treat Covid-19 | Fact Check"**
  Type: fact_check | Cred: estimated 0.85
  Publisher: AFP Fact Check | Enriched: True | Extract score: 1.000 | Rating: False
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Consuming antibiotics cannot treat Covid-19
- Published on October 4, 2021 at 06:34
- By AFP Thailand
A video of a man claiming that the antibiotic am..."

**[google_factcheck] "No, COVID-19 won’t respond to antibiotics, despite findings from ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.700 | Rating: Pants on Fire
  NLI (factcheck_rating_bypass): supporting (0.9)
  Verdict contribution: supporting (weight: 0.765)
  Snippet: "Viruses do not respond to antibiotic treatment; antibiotics work only on bacterial infections. COVID-19 is primarily a respiratory illness that in som..."

**[wikipedia] "Antibiotic"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9658)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Antibiotics are also used to prevent infection in cases of neutropenia particularly cancer-related. The use of antibiotics for secondary prevention of..."

**[wikipedia] "Antibiotic misuse"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.9932)
  Verdict contribution: supporting (weight: 0.7946)
  Snippet: "The CDC highlighted post-prescription tactics for antibiotic regulation, such as reassessing dosages and the class or type of antibiotic used, in orde..."

**[wikipedia] "Introduction to viruses"**
  Type: encyclopedia | Cred: estimated 0.95
  NLI (nli_deberta): supporting (0.7256)
  Verdict contribution: supporting (weight: 0.6893)
  Snippet: "Antibiotics, which work against bacteria, have no impact, but antiviral drugs can treat life-threatening infections. Those vaccines that produce lifel..."

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

**[duckduckgo] "Why antibiotics aren't always the answer for an illness"**
  Type: web | Cred: estimated 0.414
  NLI (nli_deberta): supporting (0.9946)
  Verdict contribution: supporting (weight: 0.4118)
  Snippet: "Bacteria or virus: What's the difference? Though both bacteria and viruses are germs too small to see with the naked eye and are spread in a similar w..."

**[duckduckgo] "Although antibiotics kill bacteria, they are not effective against viral ..."**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9888)
  Verdict contribution: supporting (weight: 0.4944)
  Snippet: "Nov 21, 2022 · Antibiotics are only useful against bacteria, not viruses. To date, no drugs have been developed that can effectively eradicate viruses..."

**[duckduckgo] "Fighting viruses with antibiotics: an overlooked path - PMC - NIH"**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): opposing (0.9937)
  Verdict contribution: opposing (weight: 0.5744)
  Snippet: "Wang et al noted that teicoplanin had already been reported as active against other enveloped viruses . They further observed that this drug was inact..."

**[duckduckgo] "Antibiotics don't work on viruses like those that cause colds ... - Facebook"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.4983)
  Snippet: "Nov 18, 2019 · Antibiotics don't work on viruses like those that cause colds, flu, bronchitis, or runny noses. We have to be careful about how antibio..."

**[duckduckgo] "Antibiotics | Johns Hopkins Medicine"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.9917)
  Verdict contribution: supporting (weight: 0.9421)
  Snippet: "Antibiotics cannot kill viruses or help you feel better when you have a virus. Bacteria cause: Most ear infections. Some sinus infections. Strep throa..."

**[duckduckgo] "[PDF] Cold or Flu - Antibiotics Don't Work for You - CDPHP"**
  Type: web | Cred: estimated 0.27
  NLI (nli_deberta): supporting (0.5508)
  Verdict contribution: supporting (weight: 0.1487)
  Snippet: "the Answer. Most illnesses are caused by two kinds of germs: bacteria or viruses. Antibiotics can cure bacterial infections – not viral infections...."

**[duckduckgo] "Why Don't Antibiotics Work on Viruses - Dragonfly Medical"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9502)
  Verdict contribution: supporting (weight: 0.19)
  Snippet: "READ ABOUT OUR LATEST COVID-19 INFORMATION
Read MorePeople often wonder: “Why don’t antibiotics work on viruses?” It’s a common question, especially w..."

**[duckduckgo] "When Antibiotics Can Help With Upper Respiratory Infections - AAFP"**
  Type: web | Cred: estimated 0.315
  NLI (nli_deberta): supporting (0.9966)
  Verdict contribution: supporting (weight: 0.3139)
  Snippet: "What are antibiotics? Antibiotics are medicines that can fight or prevent some infections. Infections are caused by two types of germs—bacteria and vi..."

**[duckduckgo] "Why Your Doctor Might Not Prescribe Antibiotics for Your Cold"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.1982)
  Snippet: "Viruses are microscopic infectious agents that can only reproduce inside living cells. Common viral infections include colds, flu, most sore throats, ..."

**[duckduckgo] "Healthy Habits: Antibiotic Do's and Don'ts - CDC"**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.9481)
  Snippet: "Key points
- Antibiotics can save lives, but they aren't always the answer.
- Take these steps to use antibiotics appropriately so you can get the bes..."

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
  Supporting weight: 8.3907
  Opposing weight: 3.2747
  Support ratio: 0.7193
  Confidence: 0.4386
  Verdict: **likely supported**
  Neutral sources (no contribution): 7

  Top supporting:
    - Healthy Habits: Antibiotic Do's and Don'ts - CDC (weight: 0.9481)
    - Antibiotics | Johns Hopkins Medicine (weight: 0.9421)
    - Antibiotic misuse (weight: 0.7946)
    - Consuming antibiotics cannot treat Covid-19 | Fact Check (weight: 0.765)
    - No, COVID-19 won’t respond to antibiotics, despite findings from ... (weight: 0.765)
  Top opposing:
    - Bacteriophage-antibiotic combination therapy against extensively drug-resistant Pseudomonas aeruginosa infection to allow liver transplantation in a toddler (weight: 0.7859)
    - Fighting viruses with antibiotics: an overlooked path - PMC - NIH (weight: 0.5744)
    - Genome Features and <i>In Vitro</i> Activity against Influenza A and SARS‐CoV‐2 Viruses of Six Probiotic Strains (weight: 0.5728)
    - Repositioning of Antibiotics in the Treatment of Viral Infections (weight: 0.5481)
    - Genome Features and In Vitro Activity against Influenza A and SARS-CoV-2 Viruses of Six Probiotic Strains (weight: 0.4777)

---
## 24. "goldfish have a 3 second memory"
Category: factual_false
Expected: strongly opposed
Actual: likely supported (**NO - MISMATCH**)
Claim type: factual (0.8)
Claim domain: general

### Sources collected: 38 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 38 -> 14 (dropped 24)
Dropped sources:
  - [encyclopedia] "Goldfish (band)" (relevance: 0.3939, reason: non_content_pattern)
  - [encyclopedia] "Hippocampus" (relevance: 0.237, reason: relevance_0.237_below_0.35)
  - [encyclopedia] "Kowloon Generic Romance" (relevance: 0.082, reason: relevance_0.082_below_0.35)
  - [encyclopedia] "David Attenborough" (relevance: -0.0159, reason: relevance_-0.016_below_0.35)
  - [academic] "The Impact of Brand Image on Purchasing Decisions on 3 Second Brand Products" (relevance: 0.0844, reason: relevance_0.084_below_0.35)
  - [academic] "Effects of auditory processing, memory, and experience on early and later stages of second language speech learning" (relevance: 0.2768, reason: relevance_0.277_below_0.35)
  - [academic] "Working memory and second language writing: A systematic review" (relevance: 0.2485, reason: relevance_0.249_below_0.35)
  - [academic] "MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations" (relevance: 0.2567, reason: relevance_0.257_below_0.35)
  - [academic] "AI and Memory Wall" (relevance: 0.3386, reason: relevance_0.339_below_0.35)
  - [academic] "Term immune memory responses to human papillomavirus (HPV) vaccination following 2 versus 3 doses of HPV vaccine." (relevance: 0.1686, reason: relevance_0.169_below_0.35)
  - [academic] "Memory B cell proliferation drives differences in neutralising responses between ChAdOx1 and BNT162b2 SARS-CoV-2 vaccines" (relevance: 0.1594, reason: relevance_0.159_below_0.35)
  - [academic] "Learning-dependent modulation of working memory" (relevance: 0.2893, reason: relevance_0.289_below_0.35)
  - [academic] "The Infralimbic, but not the Prelimbic Cortex is needed for a Complex Olfactory Memory Task" (relevance: 0.3093, reason: relevance_0.309_below_0.35)
  - [academic] "Entanglement of nanophotonic quantum memory nodes in a telecom network" (relevance: 0.1579, reason: relevance_0.158_below_0.35)
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
  NLI (nli_deberta): opposing (0.9014)
  Verdict contribution: opposing (weight: 0.7662)
  Snippet: "Some highly selectively bred goldfish can no longer breed naturally due to their altered shape. The artificial breeding method called "hand stripping"..."

**[duckduckgo] "Do Goldfish Really Have A 3-Second Memory? » ScienceABC"**
  Type: web | Cred: estimated 0.23199999999999998
  NLI (nli_deberta): neutral (0.7642)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A 2022 study at Ben-Gurion University even trained goldfish to “drive” a wheeled tank toward a target on land — a feat that requires much more than th..."

**[duckduckgo] "Goldfish three-second memory myth busted - ABC News"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.918)
  Verdict contribution: supporting (weight: 0.7803)
  Snippet: "But a 15-year-old schoolboy from Adelaide has just debunked that theory. He has conducted a simple experiment, which proves that the humble goldfish i..."

**[duckduckgo] "Hi friend, which one is right? 1. Goldfish have a 3 second memory or..."**
  Type: web | Cred: estimated 0.33199999999999996
  NLI (nli_deberta): neutral (0.8516)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Search from various English teachers...
Hi friend, which one is right?
1. Goldfish have a 3 second memory or goldfish have 3 second memories.
2. Eleph..."

**[duckduckgo] "Do goldfish have a 3-second memory? Learn how memory work in..."**
  Type: web | Cred: estimated 0.33799999999999997
  NLI (nli_deberta): supporting (0.5405)
  Verdict contribution: supporting (weight: 0.1827)
  Snippet: "You may have heard that goldfish only have a memory of 3 seconds. This is a common myth, but it is not true. Goldfish are far smarter than many people..."

**[duckduckgo] "Do fish really have a 3 second memory? | Interviews"**
  Type: web | Cred: estimated 0.252
  NLI (nli_deberta): neutral (0.4731)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Do fish really have a 3 second memory? Interview with
You may have been told you have the memory of a goldfish during forgetful spells, but is this re..."

**[duckduckgo] "Myth #8: Goldfish have a 3-second memory."**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.5288)
  Verdict contribution: supporting (weight: 0.1586)
  Snippet: "In fact, research shows they can remember things for weeks, months, and even up to a year.
🧠 The Science
Here’s what scientists have found about goldf..."

**[duckduckgo] "MythBuster: Goldfish Have a 3-Second Memory — STEAM Ahead"**
  Type: web | Cred: estimated 0.303
  NLI (nli_deberta): supporting (0.98)
  Verdict contribution: supporting (weight: 0.2969)
  Snippet: "MythBuster: Goldfish Have a 3-Second Memory
You’ve probably heard it, or even said it yourself. “I have the memory of a goldfish!” It’s a common phras..."

**[duckduckgo] "Goldfish Have a 3-Second Memory (Myth Debunked) - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): opposing (0.583)
  Verdict contribution: opposing (weight: 0.432)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[duckduckgo] "Unraveling 10 Misconceptions You Didn’t Know Were Wrong | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.959)
  Verdict contribution: supporting (weight: 0.4795)
  Snippet: "3. **Goldfish Have a 3-Second Memory:** Contrary to the belief that goldfish have a memory span of only three seconds, studies have shown that they ca..."

**[duckduckgo] "6 animal myths you might think are true – from... | Discover Wildlife"**
  Type: web | Cred: estimated 0.27599999999999997
  NLI (nli_deberta): supporting (0.9458)
  Verdict contribution: supporting (weight: 0.261)
  Snippet: "While animals are capable of doing some pretty odd things, there are plenty of animal beliefs that are purely myth. Whether they’ve come from popular ..."

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
  Supporting weight: 2.1591
  Opposing weight: 1.1982
  Support ratio: 0.6431
  Confidence: 0.2862
  Verdict: **likely supported**
  Neutral sources (no contribution): 6

  Top supporting:
    - Goldfish three-second memory myth busted - ABC News (weight: 0.7803)
    - Unraveling 10 Misconceptions You Didn’t Know Were Wrong | Medium (weight: 0.4795)
    - MythBuster: Goldfish Have a 3-Second Memory — STEAM Ahead (weight: 0.2969)
    - 6 animal myths you might think are true – from... | Discover Wildlife (weight: 0.261)
    - Do goldfish have a 3-second memory? Learn how memory work in... (weight: 0.1827)
  Top opposing:
    - Goldfish (weight: 0.7662)
    - Goldfish Have a 3-Second Memory (Myth Debunked) - YouTube (weight: 0.432)

---
## 25. "immigration is good for the economy"
Category: contested
Expected: contested
Actual: sources lean supporting (YES)
Claim type: opinion (0.95)
Claim domain: current_events

### Sources collected: 30 total
  - google_factcheck: 2
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 4
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 30 -> 20 (dropped 10)
Dropped sources:
  - [encyclopedia] "List of immigration enforcement operations in the second Trump presidency" (relevance: 0.1649, reason: relevance_0.165_below_0.35)
  - [academic] "Pandemic Politics" (relevance: 0.1351, reason: relevance_0.135_below_0.35)
  - [academic] "Trump’s authoritarian neoliberal governance and the US-Mexican border" (relevance: 0.3431, reason: relevance_0.343_below_0.35)
  - [knowledge_graph] "Immigration" (relevance: 0.2828, reason: relevance_0.283_below_0.35)
  - [knowledge_graph] "Good" (relevance: 0.1519, reason: relevance_0.152_below_0.35)
  - [knowledge_graph] "Goodreads" (relevance: 0.0144, reason: relevance_0.014_below_0.35)
  - [knowledge_graph] "goods" (relevance: 0.1454, reason: relevance_0.145_below_0.35)
  - [knowledge_graph] "economy" (relevance: 0.3274, reason: relevance_0.327_below_0.35)
  - [knowledge_graph] "Economy" (relevance: 0.1666, reason: relevance_0.167_below_0.35)
  - [knowledge_graph] "Economy" (relevance: 0.2794, reason: relevance_0.279_below_0.35)

### Dedup: 20 -> 20 (dropped 0)

### Analyzed sources (20 total)

**[google_factcheck] "Analysis | President Trump's claim that low-skilled immigration ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: The Washington Post | Enriched: True | Extract score: 0.700 | Rating: Three Pinocchios
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "“For decades, the United States was operated and has operated a very low-skill immigration system. … This policy has placed substantial pressure on Am..."

**[google_factcheck] "Do immigrants cost U.S. taxpayers $300 billion annually?"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.700 | Rating: Half True
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Trump’s team highlighted a September 2016 Washington Times story headlined: "Mass immigration costs government $296 billion a year, depresses wages." ..."

**[wikipedia] "Economic impact of immigration to Canada"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9014)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Later, in a 2019 study, it was found that the rate of poverty amongst recent immigrants is 2.4 times higher than that of native-born Canadians, and th..."

**[wikipedia] "Immigration to China"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9922)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Immigration has increased modestly since the opening up of the country and the liberalization of the economy, mostly of people moving to the large cit..."

**[wikipedia] "History of immigration to the United States"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "They originally left England to go to Holland because they faced persecution from the Church of England, and they eventually ended in North America, w..."

**[wikipedia] "Opposition to immigration"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9756)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "While much research has been conducted to determine what causes opposition to immigration, little research has been done to determine the causes behin..."

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

**[duckduckgo] "Immigration Facts: The Positive Economic Impact of Immigration"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): supporting (0.998)
  Verdict contribution: supporting (weight: 0.9481)
  Snippet: "Jan 11, 2024 · Immigrants and Immigration Mythbusters: Addressing Common Misconceptions These are the immigration facts: immigrants and immigration ar..."

**[duckduckgo] "The Economic Case for Immigration: What the Data Shows About ..."**
  Type: web | Cred: estimated 0.34700000000000003
  NLI (nli_deberta): neutral (0.8701)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Last updated 5 months ago. Our resources are updated regularly but please keep in mind that links, programs, policies, and contact information do chan..."

**[duckduckgo] "Explainer: Immigrants and the U.S. Economy"**
  Type: web | Cred: verified 0.85 | Factual: high
  NLI (nli_deberta): supporting (0.9658)
  Verdict contribution: supporting (weight: 0.8209)
  Snippet: "The question of whether immigration represents a net cost or a net benefit to the U.S. economy has been a major source of contention, even as the rese..."

**[duckduckgo] "The impact of immigrants on the US economy - Brookings"**
  Type: web | Cred: verified 0.95 | Bias: left-center | Factual: very high
  NLI (nli_deberta): supporting (0.978)
  Verdict contribution: supporting (weight: 0.9291)
  Snippet: "As shown in Figure 1, my colleagues and I previously estimated that net migration will be in negative territory for 2025 (between -295,000 and -10,000..."

**[duckduckgo] "Do Immigrants and Immigration Help the Economy?Why Is Immigration Good? Economic and Social BenefitsHow immigration fuels the U.S. economy | George W. Bush ..."**
  Type: web | Cred: estimated 0.41600000000000004
  NLI (nli_deberta): supporting (0.6885)
  Verdict contribution: supporting (weight: 0.2864)
  Snippet: "Do Immigrants and Immigration Help the Economy? With immigration dominating politics and voter concerns, BU economist’s research shows immigration boo..."

**[duckduckgo] "Why Is Immigration Good? Economic and Social Benefits"**
  Type: web | Cred: estimated 0.40800000000000003
  NLI (nli_deberta): neutral (0.6543)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "IRS Processing of Individual Taxpayer Identification Numbers
On top of income taxes, every employee and employer pays 6.2 percent of wages toward Soci..."

**[duckduckgo] "How immigration fuels the U.S. economy | George W. Bush ..."**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): supporting (0.98)
  Verdict contribution: supporting (weight: 0.3949)
  Snippet: "Laura Collins, Director of the Bush Institute-SMU Economic Growth Initiative, and Anna Walker, Manager of Communications at the Bush Institute, spoke ..."

**[duckduckgo] "Immigration is good for the U.S. economy, but reforms are"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.8691)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "News from EPI › Immigration is good for the U.S. ... Immigration is clearly positive for the balance of taxes and spending at the federal level...."

**[duckduckgo] "Immigration Is Good for the U.S. Economy"**
  Type: web | Cred: verified 0.85 | Bias: right-center | Factual: high
  NLI (nli_deberta): supporting (0.9204)
  Verdict contribution: supporting (weight: 0.7823)
  Snippet: "Immigration Is Good for the U.S. Economy
Let them in. Immigration hawks make many weak arguments, so it is hard to pick the weakest. But one contender..."

**[duckduckgo] "Why a Modern Immigration Policy is Good for Economy and the"**
  Type: web | Cred: estimated 0.43899999999999995
  NLI (nli_deberta): supporting (0.9731)
  Verdict contribution: supporting (weight: 0.4272)
  Snippet: "Why a Modern Immigration Policy is Good for Economy and the Country ... Immigration reform can help labor shortages – and build stronger ......"

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
  Supporting weight: 5.0595
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 12

  Top supporting:
    - Immigration Facts: The Positive Economic Impact of Immigration (weight: 0.9481)
    - The impact of immigrants on the US economy - Brookings (weight: 0.9291)
    - Explainer: Immigrants and the U.S. Economy (weight: 0.8209)
    - Immigration Is Good for the U.S. Economy (weight: 0.7823)
    - U.S. Residents’ Current Attitudes toward Immigrants and Immigration (weight: 0.4705)

---
## 26. "the Great Wall of China is visible from space"
Category: factual_false
Expected: strongly opposed
Actual: likely opposed (YES)
Claim type: factual (0.8)
Claim domain: historical

### Sources collected: 27 total
  - google_factcheck: 1
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 2
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 27 -> 18 (dropped 9)
Dropped sources:
  - [encyclopedia] "Factoid" (relevance: -0.0653, reason: relevance_-0.065_below_0.35)
  - [academic] "4 Research Methods: Quantitative and Qualitative Approaches" (relevance: -0.004, reason: relevance_-0.004_below_0.35)
  - [knowledge_graph] "galaxy filament" (relevance: 0.2661, reason: relevance_0.266_below_0.35)
  - [knowledge_graph] "People's Republic of China" (relevance: 0.2591, reason: relevance_0.259_below_0.35)
  - [knowledge_graph] "Taiwan" (relevance: 0.1782, reason: relevance_0.178_below_0.35)
  - [knowledge_graph] "China" (relevance: 0.2904, reason: relevance_0.290_below_0.35)
  - [knowledge_graph] "visible spectrum" (relevance: 0.2301, reason: relevance_0.230_below_0.35)
  - [knowledge_graph] "Visible Noise" (relevance: 0.0699, reason: relevance_0.070_below_0.35)
  - [knowledge_graph] "Visible" (relevance: 0.1878, reason: relevance_0.188_below_0.35)

### Dedup: 18 -> 17 (dropped 1)

### Analyzed sources (17 total)

**[google_factcheck] "Is the Great Wall of China Visible from the Moon?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes | Enriched: True | Extract score: 0.745 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "The claim that China's Great Wall is the only man-made object that can be seen from the moon with the naked eye is one of our more tenaciously incorre..."

**[wikipedia] "Artificial structures visible from space"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): supporting (0.9863)
  Verdict contribution: supporting (weight: 0.6904)
  Snippet: "Artificial structures visible from space
Artificial structures visible from space without magnification include highways, dams, and cities. Whether an..."

**[wikipedia] "Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.9194)
  Verdict contribution: opposing (weight: 0.7815)
  Snippet: "From the Moon
The Great Wall of China cannot be seen by the naked human eye from the Moon which orbits around Earth at an average distance of 384,399 ..."

**[wikipedia] "History of the Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): opposing (0.9014)
  Verdict contribution: opposing (weight: 0.8113)
  Snippet: "Radiocarbon analysis showed that they were constructed from 1040 to 1160. The walls were as tall as 2.75 metres (9 ft 0 in) at places when they were d..."

**[wikipedia] "Ming Great Wall"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9951)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Ming Great Wall
The Ming Great Wall (Chinese: 明長城; pinyin: Míng Chángchéng), built by the Ming dynasty (1368–1644), forms the most visible parts of th..."

**[open_alex] "Claim Verification: "The Great Wall of China is the only man-made object visible from space with the naked eye." — Disproved"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9844)
  Verdict contribution: opposing (weight: 0.3938)
  Snippet: "Automated fact-verification of the claim: "The Great Wall of China is the only man-made object visible from space with the naked eye." Verdict: DISPRO..."

**[duckduckgo] "Is China's Great Wall Visible from Space? | Scientific American"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9961)
  Verdict contribution: supporting (weight: 0.8467)
  Snippet: "Choose a legend: The Great Wall of China is the one of the few man-made structures visible from orbit. Or, more remarkably, it's the only human artifa..."

**[duckduckgo] "Is the Great Wall of China really visible from space? - BBC"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.5181)
  Verdict contribution: opposing (weight: 0.4404)
  Snippet: "Asked by: Chris Tuttle, Edinburgh
No. Even from low Earth orbit the Great Wall of China is extremely hard to spot with the naked eye. It’s a very thin..."

**[duckduckgo] "Can You Really See the Great Wall of China from Space? - Daily"**
  Type: web | Cred: estimated 0.4
  NLI (nli_deberta): supporting (0.9385)
  Verdict contribution: supporting (weight: 0.3754)
  Snippet: "But there’s one claim about the Great Wall that has captured the imagination of people around the globe: the idea that it’s the only man-made structur..."

**[duckduckgo] "Is the Great Wall of China visible from space?"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9829)
  Verdict contribution: opposing (weight: 0.2949)
  Snippet: "Jiminy cricket, its the architectural marvel that beckons from the heart of China – but can it be seen from the final frontier? Is the Great Wall of C..."

**[duckduckgo] "Can You See the Great Wall of China from Space? - Universe Today"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.9746)
  Verdict contribution: opposing (weight: 0.8284)
  Snippet: "One popular myth about space exploration is that the Great Wall of China is the only human-built structure that can be seen from space. But this is no..."

**[duckduckgo] "great wall of china not visible from space"**
  Type: web | Cred: estimated 0.453
  NLI (nli_deberta): opposing (0.7515)
  Verdict contribution: opposing (weight: 0.3404)
  Snippet: "Someone on the webmaster world forum thought the same thing, and another person pointed them to the snopes article showing that the claim was false. S..."

**[duckduckgo] "Was the Great Wall of China really visible from space? The"**
  Type: web | Cred: estimated 0.29700000000000004
  NLI (nli_deberta): opposing (0.9629)
  Verdict contribution: opposing (weight: 0.286)
  Snippet: "The Great Wall of China is one of the most iconic structures in the world. It is a symbol of China’s rich history and culture, and is considered to be..."

**[duckduckgo] "Is the Great Wall of China Really Visible from Space? | Live"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): opposing (0.6382)
  Verdict contribution: opposing (weight: 0.5425)
  Snippet: "Is the Great Wall of China Really Visible from Space? Since at least 1932, when a "Ripley's Believe It or Not!" cartoon called it “the mightiest work ..."

**[duckduckgo] "Can You See the Great Wall of China from Space"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.5859)
  Verdict contribution: opposing (weight: 0.1758)
  Snippet: "The myth regarding the Great Wall of China can be seen from outer space and has been circulated for hundreds of years. Is the Great Wall of China visi..."

**[duckduckgo] "Fun Facts About The Great Wall Of China | China Volunteer"**
  Type: web | Cred: estimated 0.21000000000000002
  NLI (nli_deberta): supporting (0.8149)
  Verdict contribution: supporting (weight: 0.1711)
  Snippet: "Written by Shaun Swartz
Fun Fact! Today (November 10, 2017) marks the 40th anniversary of China opening the Great Wall to tourism. So to honor one of ..."

**[wikidata] "Great Wall Motor"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Chinese vehicle manufacturing company | instance of: automobile manufacturer | country: People's Republic of China | inception: 1984-00-00 | headquart..."

### Verdict computation
  Supporting weight: 2.0836
  Opposing weight: 5.3698
  Support ratio: 0.2796
  Confidence: 0.4409
  Verdict: **likely opposed**
  Neutral sources (no contribution): 2

  Top supporting:
    - Is China's Great Wall Visible from Space? | Scientific American (weight: 0.8467)
    - Artificial structures visible from space (weight: 0.6904)
    - Can You Really See the Great Wall of China from Space? - Daily (weight: 0.3754)
    - Fun Facts About The Great Wall Of China | China Volunteer (weight: 0.1711)
  Top opposing:
    - Can You See the Great Wall of China from Space? - Universe Today (weight: 0.8284)
    - History of the Great Wall of China (weight: 0.8113)
    - Great Wall of China (weight: 0.7815)
    - Is the Great Wall of China Really Visible from Space? | Live (weight: 0.5425)
    - Is the Great Wall of China Visible from the Moon? (weight: 0.475)

---
## 27. "cats are better pets than dogs"
Category: opinion
Expected: opinion
Actual: sources divided (YES)
Claim type: opinion (0.85)
Claim domain: general

### Sources collected: 41 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 41 -> 25 (dropped 16)
Dropped sources:
  - [encyclopedia] "The Sims 2: Pets" (relevance: 0.2622, reason: relevance_0.262_below_0.35)
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

### Dedup: 25 -> 25 (dropped 0)

### Analyzed sources (25 total)

**[wikipedia] "Pet"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9961)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A 2007 survey by the University of Bristol found that 26% of UK households owned cats and 31% owned dogs, estimating total domestic populations of app..."

**[wikipedia] "Dog"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.9902)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Some studies have suggested that the extinct Japanese wolf is closely related to the ancestor of domestic dogs. In 2018, a study identified 429 genes ..."

**[wikipedia] "Overpopulation of domestic pets"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9824)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The study found that 4 million dogs entered shelters, with 2.4 million (or 60%) euthanized (p. 203).
The National Council on Pet Population Study and ..."

**[wikipedia] "Human interaction with cats"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9912)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Cats exceeded dogs in number as pets in the United States in 1985 for the first time, in part because the development of cat litter in the mid-20th ce..."

**[semantic_scholar] "PETS AS THERAPY: THE ROLE OF CATS AND DOGS IN REDUCING STRESS AND BLOOD PRESSURE"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9985)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Pet ownership, particularly of cats and dogs, has been increasingly recognized as contributing to human health and well-being. Globally, cardiovascula..."

**[semantic_scholar] "Grain-Free Diets for Dogs and Cats: An Updated Review Focusing on Nutritional Effects and Health Considerations"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Simple Summary Currently, there is a significant amount of controversy surrounding the advantages and disadvantages of feeding pets grain-free foods. ..."

**[semantic_scholar] "An exploratory mixed methods study on shared decision-making and antibiotic prescribing for pet cats and dogs in Singapore veterinary clinics"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.999)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Veterinarians primarily engage pet owners in shared decision-making (SDM) to enhance treatment outcomes and owner satisfaction, but not specifically f..."

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

**[duckduckgo] "Are Dogs Better Than Cats? 10 Reasons Why They Might Be"**
  Type: web | Cred: estimated 0.26
  NLI (nli_deberta): opposing (0.9805)
  Verdict contribution: opposing (weight: 0.2549)
  Snippet: "June 9, 2025 - If you're thinking about adding a furry pet to your home, you may wonder: dog or cat? Many people believe dogs are better than cats bec..."

**[duckduckgo] "11 Reasons Why Cats Are Better Pets Than Dogs"**
  Type: web | Cred: estimated 0.26
  NLI (nli_deberta): supporting (0.9619)
  Verdict contribution: supporting (weight: 0.2501)
  Snippet: "July 14, 2025 - Cats are easy to care for, quiet, and often more affordable. They don't need as much exercise as dogs and groom themselves. Owning a c..."

**[duckduckgo] "Why dogs are better pets than cats - The Brock Press"**
  Type: web | Cred: estimated 0.4
  NLI (nli_deberta): opposing (0.9961)
  Verdict contribution: opposing (weight: 0.3984)
  Snippet: "Dogs are better pets than cats, and it’s time we stop pretending otherwise. Having been in many arguments over this topic, I always hear the same rhet..."

**[duckduckgo] "10 Reasons Why Cats Make Great Pets"**
  Type: web | Cred: estimated 0.331
  NLI (nli_deberta): supporting (0.8984)
  Verdict contribution: supporting (weight: 0.2974)
  Snippet: "10 Reasons Why Cats Make Great Pets
written by Tori Holmes
Cats vs. dogs – as long as they’ve been domesticated our population has been divided into t..."

**[duckduckgo] "Cats are better than dogs, even science says so | by Amelia Carpenter | Writing in the Media | Medium"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): supporting (0.9839)
  Verdict contribution: supporting (weight: 0.4919)
  Snippet: "February 18, 2020 - We can all admit to watching entertaining cat videos online, or crying with laughter at dogs’ reactions to disappearing tricks, bu..."

**[duckduckgo] "Article: Why are Dogs Better Than Cats?"**
  Type: web | Cred: estimated 0.264
  NLI (nli_deberta): opposing (0.9946)
  Verdict contribution: opposing (weight: 0.2626)
  Snippet: "They enjoy being active and playing, which makes them great pals. Studies show owners feel closer to their dogs than cats, despite dogs costing more. ..."

**[duckduckgo] "Why Are Dogs Better Than Cats|News|Midepet"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9888)
  Verdict contribution: opposing (weight: 0.2966)
  Snippet: "Why Are Dogs Better Than Cats
Why Are Dogs Better Than Cats? Dogs are often considered better than cats because of their loyalty, affectionate nature,..."

**[duckduckgo] "Cats vs Dogs: Reasons Why Dogs Are Better Than Cats"**
  Type: web | Cred: estimated 0.417
  NLI (nli_deberta): opposing (0.6284)
  Verdict contribution: opposing (weight: 0.262)
  Snippet: "Why are dogs better than cats? Without us even telling you why dogs are better than cats, we bet you can come up with plenty of reasons on your own.

..."

**[duckduckgo] "Dogs vs. Cats: Which Pet Makes Their Humans the Happiest? | Psychology Today"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9888)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Animal Behavior
Dogs vs. Cats: Which Pet Makes Their Humans the Happiest? The research is mixed but only one pet can be victorious. Posted July 28, 20..."

**[duckduckgo] "Are Dogs Smarter than Cats? | Britannica"**
  Type: web | Cred: verified 0.85 | Bias: least pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Are Dogs Smarter than Cats? The ongoing quarrel about whether dogs or cats are smarter has divided pet lovers throughout history—and scientific resear..."

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
  Supporting weight: 1.0394
  Opposing weight: 1.4746
  Support ratio: 0.4134
  Confidence: 0.1731
  Verdict: **sources divided**
  Neutral sources (no contribution): 17

  Top supporting:
    - Cats are better than dogs, even science says so | by Amelia Carpenter | Writing in the Media | Medium (weight: 0.4919)
    - 10 Reasons Why Cats Make Great Pets (weight: 0.2974)
    - 11 Reasons Why Cats Are Better Pets Than Dogs (weight: 0.2501)
  Top opposing:
    - Why dogs are better pets than cats - The Brock Press (weight: 0.3984)
    - Why Are Dogs Better Than Cats|News|Midepet (weight: 0.2966)
    - Article: Why are Dogs Better Than Cats? (weight: 0.2626)
    - Cats vs Dogs: Reasons Why Dogs Are Better Than Cats (weight: 0.262)
    - Are Dogs Better Than Cats? 10 Reasons Why They Might Be (weight: 0.2549)

---
## 28. "organic food is healthier than conventional food"
Category: contested
Expected: contested
Actual: sources lean supporting (YES)
Claim type: opinion (0.85)
Claim domain: scientific

### Sources collected: 36 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 7
  - open_alex: 6
  - duckduckgo: 10
  - wikidata: 8

### Relevance filter: 36 -> 30 (dropped 6)
Dropped sources:
  - [academic] "Determination of Regulated and Emerging Mycotoxins in Organic and Conventional Gluten-Free Flours by LC-MS/MS" (relevance: 0.2547, reason: relevance_0.255_below_0.35)
  - [academic] "Comparison of the Mineral and Nutraceutical Profiles of Elephant Garlic (Allium ampeloprasum L.) Grown in Organic and Conventional Fields of Valdichiana, a Traditional Cultivation Area of Tuscany, Italy" (relevance: 0.3273, reason: relevance_0.327_below_0.35)
  - [academic] "Diet and food type affect urinary pesticide residue excretion profiles in healthy individuals: results of a randomized controlled dietary intervention trial" (relevance: 0.3417, reason: relevance_0.342_below_0.35)
  - [knowledge_graph] "Healthier Lives" (relevance: 0.184, reason: relevance_0.184_below_0.35)
  - [knowledge_graph] "Healthier lunchboxes : ideas for primary schools" (relevance: 0.2474, reason: relevance_0.247_below_0.35)
  - [knowledge_graph] "Healthier Hearts Foundation" (relevance: 0.2178, reason: relevance_0.218_below_0.35)

### Dedup: 30 -> 27 (dropped 3)

### Analyzed sources (27 total)

**[wikipedia] "Organic food"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.8418)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "From the perspective of scientists and consumers, there is insufficient evidence in the scientific and medical literature to support claims that organ..."

**[wikipedia] "Food system"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Scientists estimated the extensive pesticide pollution risks worldwide with a new environmental model and found that a third of global agricultural la..."

**[wikipedia] "Organic farming"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9966)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Productivity
[edit]A 2012 meta-analysis found that productivity is on average 25% lower for organic farming than conventional farming. Yield differenc..."

**[wikipedia] "Ultra-processed food"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9829)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A 2024 meta-analysis published in The BMJ identified 32 studies that associated UPF with negative health outcomes, though it also noted a possible het..."

**[wikipedia] "Health food store"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): neutral (0.981)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Health food store
A health food store (or health food shop) is a type of grocery store that primarily sells healthful foods, organic foods, local prod..."

**[semantic_scholar] "Fruit quality in organic and conventional farming: advantages and limitations."**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): opposing (0.5908)
  Verdict contribution: opposing (weight: 0.384)
  Snippet: "Fruit quality is essential for nutrition and human health and needs urgent attention in current agricultural practices. Organic farming is not as prod..."

**[open_alex] "Organic food labels bias food healthiness perceptions: Estimating healthiness equivalence using a Discrete Choice Experiment"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): neutral (0.9546)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic food labels bias food healthiness perceptions: Estimating healthiness equivalence using a Discrete Choice Experiment..."

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

**[semantic_scholar] "Antibiotic Alternatives to Produce Organic Poultry Meat as a Safe Food Source and the Impact of its Consumption on Human Health – A Review"**
  Type: academic | Cred: estimated 0.55
  NLI (nli_deberta): neutral (0.6616)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Abstract The scientific evidence on the effects of consuming organic chicken meat on human health is examined in this review article. Few studies part..."

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

**[open_alex] "Europe’s Farm to Fork Strategy and Its Commitment to Biotechnology and Organic Farming: Conflicting or Complementary Goals?"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9956)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sustainable food systems will require profound changes in people’s consumption patterns and lifestyles, which is true regardless of the farming method..."

**[open_alex] "Lipid characteristics, bioactive properties, and mineral content in hazelnut grown under different cultivation systems"**
  Type: academic | Cred: estimated 0.65
  NLI (nli_deberta): supporting (0.8413)
  Verdict contribution: supporting (weight: 0.5468)
  Snippet: "The demand for organic food is increasing due to the view among consumers that organic food is healthier and more nutritious. However, very limited da..."

**[duckduckgo] "New Study Reveals Organic Foods are Healthier than Conventional"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.9766)
  Verdict contribution: supporting (weight: 0.293)
  Snippet: "... states that organic crops and foods derived from these crops are about 69% healthier than conventional foods, in terms of number of key antioxidan..."

**[duckduckgo] "Are Organic Foods Healthier Than Conventional Foods? - HWN"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.9658)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sign Up For Our Self Healthy Eating Newsletter
Canned spinach confirmed decreased amounts but it still wasn’t recommended. Grown in the ground potatoe..."

**[duckduckgo] "Organic Food is Healthier by Far, Find Studies"**
  Type: web | Cred: estimated 0.311
  NLI (nli_deberta): supporting (0.5078)
  Verdict contribution: supporting (weight: 0.1579)
  Snippet: "It is refreshing to see researchers pursuing scientific proof that organic food is healthier, to settle the question once and for all. Below are some ..."

**[duckduckgo] "Organic Foods not Healthier than Conventional Foodstuff -"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.4729)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Organic food was thought to be superior to ordinarily-produced foods. But this may not be so for leading scientists have claimed that organic food is ..."

**[duckduckgo] "Organic foods are not necessarily more healthier than"**
  Type: web | Cred: estimated 0.294
  NLI (nli_deberta): neutral (0.9214)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... MD, MS, an instructor in Stanford University’s Division of General Medical Disciplines, said: “Some believe that organic food is always healthier ..."

**[duckduckgo] "Organic food 'no healthier than conventional' | The Independent"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): opposing (0.9414)
  Verdict contribution: opposing (weight: 0.4707)
  Snippet: "Organic food 'no healthier than conventional'
Organic food is no healthier than conventional food, according to the world's biggest research project i..."

**[duckduckgo] "diet - Are organic foods healthier than conventional foods? -"**
  Type: web | Cred: estimated 0.323
  NLI (nli_deberta): neutral (0.9668)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is a popular perception, and many marketing claims, that organic produce (and food in general) is healthier than food grown with conventional ....."

**[duckduckgo] "Organic Food Choices: Healthier Than Conventional Ones?"**
  Type: web | Cred: estimated 0.422
  NLI (nli_deberta): neutral (0.4988)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The second is they typically boast a substantial nutritional superiority. But, is that true? In comparison to conventional foods, organic foods are ac..."

**[duckduckgo] "Organic foods have healthier fats, more nutrients and fewer"**
  Type: web | Cred: verified 0.1 | Bias: far right conspiracy-pseusdoscience | Factual: very low
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.0991)
  Snippet: "(NaturalNews) We've known for quite some time that there's a
huge difference between organic food and conventional products. Organic bashers like
Jon ..."

**[duckduckgo] "Organic Food vs. Conventional: Is It Truly Healthier? -"**
  Type: web | Cred: estimated 0.23399999999999999
  NLI (nli_deberta): neutral (0.8574)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "With the increasing popularity of organic food, you may find yourself questioning whether it truly offers enhanced health benefits. While organic food..."

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
  Supporting weight: 2.1417
  Opposing weight: 0.8547
  Support ratio: 0.7148
  Confidence: 0.4295
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 19

  Top supporting:
    - Key Findings of the French BioNutriNet Project on Organic Food-Based Diets: Description, Determinants, and Relationships to Health and the Environment. (weight: 0.6465)
    - Lipid characteristics, bioactive properties, and mineral content in hazelnut grown under different cultivation systems (weight: 0.5468)
    - Customer Preferences for Organic Agriculture Produce in the Czech Republic: 2016 and 2019 (weight: 0.3983)
    - New Study Reveals Organic Foods are Healthier than Conventional (weight: 0.293)
    - Organic Food is Healthier by Far, Find Studies (weight: 0.1579)
  Top opposing:
    - Organic food 'no healthier than conventional' | The Independent (weight: 0.4707)
    - Fruit quality in organic and conventional farming: advantages and limitations. (weight: 0.384)

---
## 29. "MSG is dangerous to consume"
Category: factual_false
Expected: strongly opposed
Actual: sources lean opposing (**NO - MISMATCH**)
Claim type: opinion (0.9)
Claim domain: general

### Sources collected: 37 total
  - google_factcheck: 3
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 37 -> 16 (dropped 21)
Dropped sources:
  - [encyclopedia] "Controversies of Nestlé" (relevance: 0.3071, reason: relevance_0.307_below_0.35)
  - [encyclopedia] "Text messaging" (relevance: 0.1357, reason: relevance_0.136_below_0.35)
  - [encyclopedia] "André the Giant" (relevance: 0.0208, reason: relevance_0.021_below_0.35)
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
  - [knowledge_graph] "Dangerous" (relevance: 0.2587, reason: relevance_0.259_below_0.35)
  - [knowledge_graph] "Consumer Electronics Show" (relevance: -0.0651, reason: relevance_-0.065_below_0.35)
  - [knowledge_graph] "consumer protection" (relevance: 0.0653, reason: relevance_0.065_below_0.35)
  - [knowledge_graph] "consumer electronics" (relevance: 0.0028, reason: relevance_0.003_below_0.35)

### Dedup: 16 -> 16 (dropped 0)

### Analyzed sources (16 total)

**[google_factcheck] "Fact check: MSG doesn't cause neurological disorders, is safe ..."**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: USA Today | Enriched: True | Extract score: 0.795 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "USA TODAY has reached out to the poster for comment. MSG is a common flavor enhancer and preservative that has been in global use for the past 100 yea..."

**[google_factcheck] "Brain damage link to MSG a salty dose of misinformation"**
  Type: fact_check | Cred: verified 0.85 | Bias: least biased | Factual: high
  Publisher: AAP | Enriched: True | Extract score: 0.860 | Rating: False. Food authorities and major studies say MSG is safe to consume.
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "WHAT WAS CLAIMED
MSG kills brain cells and damages the nervous system. OUR VERDICT
False. Food authorities and major studies say MSG is safe to consum..."

**[google_factcheck] "Viral online posts claiming MSG is unsafe for consumption omit ..."**
  Type: fact_check | Cred: estimated 0.85
  Publisher: AFP Fact Check | Enriched: True | Extract score: 0.895 | Rating: Missing Context
  NLI (factcheck_rating_bypass): opposing (0.65)
  Verdict contribution: opposing (weight: 0.5525)
  Snippet: "Viral online posts claiming MSG is unsafe for consumption omit important context
- Published on October 16, 2020 at 10:15
- By AFP Philippines
The cla..."

**[wikipedia] "Glutamate flavoring"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.9932)
  Verdict contribution: opposing (weight: 0.7946)
  Snippet: "These crystals, when tasted, reproduced a flavor detected in many foods, especially seaweed. Professor Ikeda coined the term umami for this flavor. He..."

**[wikipedia] "Anthony William"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): supporting (0.8735)
  Verdict contribution: supporting (weight: 0.6988)
  Snippet: "He also contends that cancer as a whole has no genetic component, despite scientific evidence to the contrary. William also suggests that the Epstein-..."

**[duckduckgo] "Monosodium glutamate, also called MSG: Is it harmful? - Mayo Clinic"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "There is a problem with information submitted for this request. Review/update the information highlighted below and resubmit the form. From Mayo Clini..."

**[duckduckgo] "Monosodium glutamate (MSG): What it is, and why... - Harvard Health"**
  Type: web | Cred: estimated 0.329
  NLI (nli_deberta): neutral (0.5981)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "But what exactly is MSG? And why might you consider avoiding foods that contain it? What is MSG?
MSG is a flavor enhancer that's frequently added to c..."

**[duckduckgo] "What's Hiding in Your Food? The Dangers of MSG - Emed"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.7529)
  Verdict contribution: supporting (weight: 0.1506)
  Snippet: "Why is MSG Dangerous?[MSG] also causes a cancer cell to become more mobile, and that enhances metastasis, or spread. When you increase the glutamate l..."

**[duckduckgo] "What Exactly Is MSG And Is It Bad For You?"**
  Type: web | Cred: estimated 0.403
  NLI (nli_deberta): opposing (0.9658)
  Verdict contribution: opposing (weight: 0.3892)
  Snippet: "A 2008 study in the journal "Physiology & Behavior" found that adding MSG to soup made test subjects enjoy it more, and that the participants who ate ..."

**[duckduckgo] "How Dangerous is MSG, really? - YouTube"**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.6738)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[duckduckgo] "Is MSG Truly Unhealthy? All You Need to Know"**
  Type: web | Cred: verified 0.5 | Bias: pro-science | Factual: mixed
  NLI (nli_deberta): opposing (0.8286)
  Verdict contribution: opposing (weight: 0.4143)
  Snippet: "For years, MSG has been viewed as an unhealthy ingredient. However, newer research questions the accuracy of its purported adverse effects on human he..."

**[duckduckgo] "Is Msg Dangerous or Is It Safe? | Ideal Nutrition"**
  Type: web | Cred: estimated 0.236
  NLI (nli_deberta): opposing (0.9619)
  Verdict contribution: opposing (weight: 0.227)
  Snippet: "The sodium in MSG does contribute to daily sodium intake. Is MSG Dangerous? Myths and stigma surrounding the safety of MSG consumption have been aroun..."

**[duckduckgo] "MSG is back. Is the idea it’s bad for us just a myth or food science?"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.7173)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Two major safety reviews have been conducted: one in 1987 by a United Nations expert committee and another 1995 by the Federation of American Societie..."

**[duckduckgo] "Is msg bad for you?What is MSG: Everything you need to know"**
  Type: web | Cred: estimated 0.343
  NLI (nli_deberta): opposing (0.9922)
  Verdict contribution: opposing (weight: 0.3403)
  Snippet: "However, there seems to be a group of people who manifest symptoms, such as vomiting, nausea or diarrhea, when they consume foods prepared with MSG.
W..."

**[duckduckgo] "Oh Maggi: Really, How Dangerous Is MSG"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): neutral (0.9878)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Food Safety and Drug Administration's order earlier this week to Nestle to recall batches of Maggi noodles across the country, for containing dang..."

**[wikidata] "monosodium L-glutamate"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "chemical compound, flavor enhancer | instance of: type of chemical entity..."

### Verdict computation
  Supporting weight: 0.8494
  Opposing weight: 3.1929
  Support ratio: 0.2101
  Confidence: 0.5798
  Verdict: **sources lean opposing**
  Neutral sources (no contribution): 7

  Top supporting:
    - Anthony William (weight: 0.6988)
    - What's Hiding in Your Food? The Dangers of MSG - Emed (weight: 0.1506)
  Top opposing:
    - Glutamate flavoring (weight: 0.7946)
    - Viral online posts claiming MSG is unsafe for consumption omit ... (weight: 0.5525)
    - Fact check: MSG doesn't cause neurological disorders, is safe ... (weight: 0.475)
    - Is MSG Truly Unhealthy? All You Need to Know (weight: 0.4143)
    - What Exactly Is MSG And Is It Bad For You? (weight: 0.3892)

---
## 30. "humans share about 98% of DNA with chimpanzees"
Category: factual_true
Expected: strongly supported
Actual: strongly supported (YES)
Claim type: factual (0.8)
Claim domain: statistical

### Sources collected: 30 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 6
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 30 -> 17 (dropped 13)
Dropped sources:
  - [academic] "The influence of evolutionary history on human health and disease" (relevance: 0.334, reason: relevance_0.334_below_0.35)
  - [academic] "CADD v1.7: using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide variant predictions" (relevance: 0.0933, reason: relevance_0.093_below_0.35)
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

### Dedup: 17 -> 17 (dropped 0)

### Analyzed sources (17 total)

**[wikipedia] "Human evolution"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9795)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "This study demonstrated affinities between the skull morphology of Ar. ramidus and that of infant and juvenile chimpanzees, suggesting the species evo..."

**[wikipedia] "Chimpanzee"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.7266)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A 2015 study of Ardipithecus, an early human relative dated 4.4 mya, disputed this interpretation. The study concluded that humans, chimpanzees and bo..."

**[wikipedia] "Bonobo"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9253)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "DNA evidence suggests the bonobo and common chimpanzee species diverged approximately 890,000–860,000 years ago following separation of these two popu..."

**[wikipedia] "Human evolutionary genetics"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.769)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "For example, the sequence divergence varies between 0% to 2.66% between non-coding, non-repetitive genomic regions of humans and chimpanzees. The perc..."

**[wikipedia] "Timeline of human evolution"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.5396)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "From within the pelycosaurs emerged the therapsids, which rose to dominance during the Middle and Late Permian. Evidence suggests that early therapsid..."

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

**[duckduckgo] "Do humans and chimps really share nearly 99% of their DNA? | Live Science"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.8809)
  Verdict contribution: supporting (weight: 0.7488)
  Snippet: "Do humans and chimps really share nearly 99% of their DNA?
The frequently cited 99% similarity between human and chimp DNA overlooks key differences i..."

**[duckduckgo] "Comparing Chimp, Bonobo and Human DNA | AMNHIt’s often said that humans and chimps share 99% of their DNA ...Humans and Chimps: 98% Identical, But a World ApartChimpanzee and Human DNA: Why Are We So Different?“1% Difference” Now Overturned | Science and Culture TodayHow Similar Are Chimpanzee and Human DNA? - ScienceInsights"**
  Type: web | Cred: estimated 0.363
  NLI (nli_deberta): supporting (0.9629)
  Verdict contribution: supporting (weight: 0.3495)
  Snippet: "Human and chimp DNA is so similar because the two species are so closely related. Humans, chimps and bonobos descended from a single ancestor species ..."

**[duckduckgo] "It’s often said that humans and chimps share 99% of their DNA ..."**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9229)
  Verdict contribution: supporting (weight: 0.7845)
  Snippet: "Sep 15, 2025 · Early research suggested that human and chimp genomes are more than 98% identical. “What it means is that for each part of the human ge..."

**[duckduckgo] "Humans and Chimps: 98% Identical, But a World Apart"**
  Type: web | Cred: estimated 0.3
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.2956)
  Snippet: "Imagine looking into the eyes of a chimpanzee and seeing a flicker of something deeply familiar—a spark that hints at a shared story stretching back m..."

**[duckduckgo] "Chimpanzee and Human DNA: Why Are We So Different?"**
  Type: web | Cred: estimated 0.41
  NLI (nli_deberta): supporting (0.9854)
  Verdict contribution: supporting (weight: 0.404)
  Snippet: "This exploration delves into the genetic evidence that both unites us with and distinguishes us from chimpanzees, revealing a story of shared ancestry..."

**[duckduckgo] "How Similar Are Chimpanzee and Human DNA? - ScienceInsights"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9951)
  Verdict contribution: supporting (weight: 0.402)
  Snippet: "The Remarkable Genetic Overlap
Humans and chimpanzees share approximately 98-99% of their DNA. This high percentage signifies that the vast majority o..."

**[duckduckgo] "Divergence between samples of chimpanzee and human DNA sequences is 5%, counting indels - PMC"**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): supporting (0.9058)
  Verdict contribution: supporting (weight: 0.5236)
  Snippet: "The conclusion is the old saw that we share 98.5% of our DNA sequence with chimpanzee is probably in error. For this sample, a better estimate would b..."

**[duckduckgo] "New Research: Humans and Chimps Do Not Share 98% of Their Genomes - Apologetics Press"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): opposing (0.5581)
  Verdict contribution: opposing (weight: 0.2255)
  Snippet: "New Research: Humans and Chimps Do Not Share 98% of Their Genomes
[EDITOR’S NOTE: The following article was written by A.P. auxiliary staff scientist ..."

**[duckduckgo] "Why do we say that human beings share 98% of our DNA with chimpanzees but an individual human only shares 50% of DNA with one of his/her parents? - Quora"**
  Type: web | Cred: estimated 0.487
  NLI (nli_deberta): neutral (0.9912)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Answer (1 of 26): We don't. That is a misconception. Technically I could argue that The Mona Lisa consists of 100% the same as a drawing I did when I ..."

**[duckduckgo] "Chimpanzees and humans share 98.8% of their DNA — and just like people, ‘chimps are both bloodthirsty warmongers and thoughtful beings’ - Genetic Literacy Project"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.9863)
  Verdict contribution: supporting (weight: 0.8384)
  Snippet: "December 14, 2024 - Although chimpanzees and humans share a surprising 98.8 percent of their DNA, our differences are vast – or at least we like to th..."

### Verdict computation
  Supporting weight: 4.3463
  Opposing weight: 0.2255
  Support ratio: 0.9507
  Confidence: 0.9014
  Verdict: **strongly supported**
  Neutral sources (no contribution): 8

  Top supporting:
    - Chimpanzees and humans share 98.8% of their DNA — and just like people, ‘chimps are both bloodthirsty warmongers and thoughtful beings’ - Genetic Literacy Project (weight: 0.8384)
    - It’s often said that humans and chimps share 99% of their DNA ... (weight: 0.7845)
    - Do humans and chimps really share nearly 99% of their DNA? | Live Science (weight: 0.7488)
    - Divergence between samples of chimpanzee and human DNA sequences is 5%, counting indels - PMC (weight: 0.5236)
    - Chimpanzee and Human DNA: Why Are We So Different? (weight: 0.404)
  Top opposing:
    - New Research: Humans and Chimps Do Not Share 98% of Their Genomes - Apologetics Press (weight: 0.2255)

---
## 31. "China has the world's largest economy"
Category: current_event
Expected: contested
Actual: likely opposed (YES)
Claim type: factual (0.8)
Claim domain: current_events

### Sources collected: 27 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 5
  - open_alex: 4
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 27 -> 23 (dropped 4)
Dropped sources:
  - [encyclopedia] "Economy of the United States" (relevance: 0.2863, reason: relevance_0.286_below_0.35)
  - [encyclopedia] "Economy of Russia" (relevance: 0.2792, reason: relevance_0.279_below_0.35)
  - [academic] "Effects of digital economy on carbon emission intensity in Chinese cities: A life-cycle theory and the application of non-linear spatial panel smooth transition threshold model" (relevance: 0.305, reason: relevance_0.305_below_0.35)
  - [knowledge_graph] "Taiwan" (relevance: 0.3209, reason: relevance_0.321_below_0.35)

### Dedup: 23 -> 22 (dropped 1)

### Analyzed sources (22 total)

**[wikipedia] "Economy of China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): supporting (0.5669)
  Verdict contribution: supporting (weight: 0.4819)
  Snippet: "The results suggest that the Chinese economic growth rate is higher than the official reported data. The study by Daniel H. Rosen and Beibei Bao, publ..."

**[wikipedia] "China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.4954)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Making up around one-fifth of the world's economy, China is the second-wealthiest country in the world, with the Chinese economy being the largest whe..."

**[wikipedia] "List of countries by largest historical GDP"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): opposing (0.7251)
  Verdict contribution: opposing (weight: 0.5801)
  Snippet: "While the United States has consistently had the world's largest economy for some time, in the last fifty years the world has seen both rises and fall..."

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

**[semantic_scholar] "ANALYSIS OF THE CURRENT STATUS AND TRENDS OF CHINA'S DIGITAL ECONOMY DEVELOPMENT"**
  Type: academic | Cred: estimated 0.4
  NLI (nli_deberta): neutral (0.9268)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In the era of rapid technological advancements, the digital economy has emerged as a powerful driver of global economic growth and transformation. It ..."

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

**[duckduckgo] "Top 10 Largest Economies in the World in 2025"**
  Type: web | Cred: estimated 0.7
  NLI (nli_deberta): opposing (0.999)
  Verdict contribution: opposing (weight: 0.6993)
  Snippet: "Likewise, while most of the economies in the top 10 have potential growth rates below the global average due to already high physical and human capita..."

**[duckduckgo] "Largest Economies in the World (2026)"**
  Type: web | Cred: estimated 0.269
  NLI (nli_deberta): opposing (0.7979)
  Verdict contribution: opposing (weight: 0.2146)
  Snippet: "Largest Economies in the World in 2026
Discover the top 10 largest economies in the world in 2026 based on the IMF World Economic Outlook April 2026 p..."

**[duckduckgo] "Largest economies worldwide 2026| Statista"**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): opposing (0.9727)
  Verdict contribution: opposing (weight: 0.8268)
  Snippet: "In 2026, the United States had the largest economy in the world, with a nominal gross domestic product of almost 32.4 trillion U.S. dollars. China was..."

**[duckduckgo] "World GDP Ranking 2026 List"**
  Type: web | Cred: estimated 0.425
  NLI (nli_deberta): opposing (0.8584)
  Verdict contribution: opposing (weight: 0.3648)
  Snippet: "The latest global GDP estimates for 2026 reflect updated projections for major economies. While the US and China remain the top two economies, India c..."

**[duckduckgo] "World GDP Rankings 2025 | Top 20 countries ranked by GDP"**
  Type: web | Cred: estimated 0.418
  NLI (nli_deberta): supporting (0.9541)
  Verdict contribution: supporting (weight: 0.3988)
  Snippet: "GDP serves as a key metric for assessing the magnitude of a nation"s economy. The conventional approach for gauging a country"s GDP involves the expen..."

**[duckduckgo] "Ranked: The World's Largest Economies in 2026 | Visual Capitalist"**
  Type: web | Cred: estimated 0.316
  NLI (nli_deberta): neutral (0.9995)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The 2026 world economy has a cautious outlook, according to the October report put out by the International Monetary Fund (IMF). The organization says..."

**[duckduckgo] "The Top 10 Largest Economies in the World by GDP"**
  Type: web | Cred: estimated 0.319
  NLI (nli_deberta): neutral (0.4993)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "For instance, the long-term projections of the economists that we poll show that by 2033, India will have become the world’s third-largest economy, wh..."

**[duckduckgo] "China vs US: which has the world's biggest economy? - Geographical"**
  Type: web | Cred: estimated 0.46399999999999997
  NLI (nli_deberta): neutral (0.8188)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "According to a Pew Research survey of 24 countries, only around one third surveyed see China as the world’s leading economic power, with the rest givi..."

**[duckduckgo] "World GDP Ranking 2026 - StatisticsTimes.com"**
  Type: web | Cred: estimated 0.43499999999999994
  NLI (nli_deberta): supporting (0.8965)
  Verdict contribution: supporting (weight: 0.39)
  Snippet: "Projected GDP Ranking
Source International Monetary Fund World Economic Outlook (October - 2025)
As of 2026, the United States and China will occupy t..."

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
  Supporting weight: 1.2707
  Opposing weight: 3.9438
  Support ratio: 0.2437
  Confidence: 0.5126
  Verdict: **likely opposed**
  Neutral sources (no contribution): 11

  Top supporting:
    - Economy of China (weight: 0.4819)
    - World GDP Rankings 2025 | Top 20 countries ranked by GDP (weight: 0.3988)
    - World GDP Ranking 2026 - StatisticsTimes.com (weight: 0.39)
  Top opposing:
    - Largest economies worldwide 2026| Statista (weight: 0.8268)
    - Top 10 Largest Economies in the World in 2025 (weight: 0.6993)
    - List of countries by largest historical GDP (weight: 0.5801)
    - The role of green finance in supporting the transition to a green economy: China as a model (weight: 0.4681)
    - Toward a new growth pole for the world: Rethinking the strategies for Huaihua International Inland Port in China (weight: 0.399)

---
## 32. "eating carrots improves your eyesight"
Category: factual_false
Expected: strongly opposed
Actual: strongly supported (**NO - MISMATCH**)
Claim type: factual (0.8)
Claim domain: general

### Sources collected: 28 total
  - google_factcheck: 2
  - wikipedia: 5
  - semantic_scholar: 1
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 0

### Relevance filter: 28 -> 16 (dropped 12)
Dropped sources:
  - [encyclopedia] "List of common misconceptions about science, technology, and mathematics" (relevance: 0.2021, reason: relevance_0.202_below_0.35)
  - [encyclopedia] "Falling Up (poetry collection)" (relevance: 0.1347, reason: relevance_0.135_below_0.35)
  - [encyclopedia] "Creatures (video game series)" (relevance: 0.1333, reason: relevance_0.133_below_0.35)
  - [encyclopedia] "List of The Transformers characters" (relevance: 0.0107, reason: relevance_0.011_below_0.35)
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
  Publisher: Snopes.com | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "Carrots have long been touted for their efficacy in improving eyesight, and generations of kids have been admonished to not leave them on their plates..."

**[google_factcheck] "Carrots Alone Won't Improve Eyesight"**
  Type: fact_check | Cred: estimated 0.85
  Publisher: unknown | Enriched: True | Extract score: 0.000 | Rating: misleading
  NLI (factcheck_rating_bypass): opposing (0.75)
  Verdict contribution: opposing (weight: 0.6375)
  Snippet: "Trending now Carrots Alone Won't Improve Eyesight Emerging story The idea that eating carrots can improve your eyesight has been around since World Wa..."

**[wikipedia] "Carrot"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): supporting (0.5928)
  Verdict contribution: supporting (weight: 0.5335)
  Snippet: "Some claim that the Dutch created the orange carrots to honor the Dutch flag at the time and William of Orange, but other authorities argue these clai..."

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

**[duckduckgo] "Are Carrots Good for Your Eyes? - HealthlineCarrots and Eyesight: The Truth Behind the MythYes, eating carrots can help your eyesight. But it’s not a ...Do carrots help you see at night? The truth behind popular ...Are Carrots Good for Your Eyes? Myths and Facts"**
  Type: web | Cred: verified 0.5 | Bias: pro-science | Factual: mixed
  NLI (nli_deberta): supporting (0.9917)
  Verdict contribution: supporting (weight: 0.4959)
  Snippet: "Though the idea that carrots are good for your eyesight stemmed from a myth, carrots contain many beneficial nutrients that may support healthy eyes a..."

**[duckduckgo] "4 Ways Eating Carrots Regularly Can Improve Your Eyesight"**
  Type: web | Cred: estimated 0.382
  NLI (nli_deberta): supporting (0.8779)
  Verdict contribution: supporting (weight: 0.3354)
  Snippet: "Nov 12, 2025 · Carrots are rich in antioxidants that support night vision, reduce the risk of age-related vision loss, and protect against cataracts...."

**[duckduckgo] "Carrots & Eye Health: Myth or Fact? - University of Utah Health"**
  Type: web | Cred: estimated 0.47800000000000004
  NLI (nli_deberta): supporting (0.9912)
  Verdict contribution: supporting (weight: 0.4738)
  Snippet: "Carrots & Eye Health: Myth or Fact? Carrots & Eye Health: Myth or Fact? You've probably heard that carrots are good for your eyes, and it's true. Carr..."

**[duckduckgo] "Carrots and Eyesight: The Truth Behind the Myth"**
  Type: web | Cred: estimated 0.229
  NLI (nli_deberta): supporting (0.8716)
  Verdict contribution: supporting (weight: 0.1996)
  Snippet: "Carrots have long been heralded as a superfood for eye health, often portrayed as the ultimate vision-enhancing food. But how much truth is there to t..."

**[duckduckgo] "Yes, eating carrots can help your eyesight. But it’s not a ..."**
  Type: web | Cred: verified 0.85 | Factual: high
  NLI (nli_deberta): supporting (0.6519)
  Verdict contribution: supporting (weight: 0.5541)
  Snippet: "News stories credited his success with his carrot consumption. In reality, he was using a new radar technology.
“It would have been easier had the car..."

**[duckduckgo] "Do carrots help you see at night? The truth behind popular ..."**
  Type: web | Cred: estimated 0.47400000000000003
  NLI (nli_deberta): supporting (0.8271)
  Verdict contribution: supporting (weight: 0.392)
  Snippet: "Food and nutrition is now big business and as a result you see all kind of claims about how the stuff on our plates can work for or against you.

But ..."

**[duckduckgo] "Are Carrots Good for Your Eyes? Myths and Facts"**
  Type: web | Cred: estimated 0.404
  NLI (nli_deberta): supporting (0.9434)
  Verdict contribution: supporting (weight: 0.3811)
  Snippet: "A single medium carrot provides about 110% of your daily vitamin A needs, making it one of the most efficient sources of this essential nutrient. How ..."

**[duckduckgo] "Myth or Fact: Eating Carrots Improves Eyesight | Duke Health"**
  Type: web | Cred: estimated 0.302
  NLI (nli_deberta): supporting (0.9531)
  Verdict contribution: supporting (weight: 0.2878)
  Snippet: "The notion that eating carrots improves eyesight sounds like a story your mother made up to get you to eat your vegetables. But is there any truth to ..."

**[duckduckgo] "Fact or Fiction?: Carrots Improve Your Vision | Scientific American"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.8384)
  Verdict contribution: supporting (weight: 0.7126)
  Snippet: "In the dead of night, just how did the British Air Force manage to gun down German aircraft during World War II? Eating carrots was the key to the pil..."

**[duckduckgo] "Carrots Can't Help You See in the Dark. Here's How a World War II..."**
  Type: web | Cred: verified 0.95 | Bias: pro-science | Factual: very high
  NLI (nli_deberta): supporting (0.8306)
  Verdict contribution: supporting (weight: 0.7891)
  Snippet: "Carrots Can’t Help You See in the Dark. Here’s How a World War II Propaganda Campaign Popularized the Myth
The British government claimed that eating ..."

### Verdict computation
  Supporting weight: 5.486
  Opposing weight: 1.1125
  Support ratio: 0.8314
  Confidence: 0.6628
  Verdict: **strongly supported**
  Neutral sources (no contribution): 2

  Top supporting:
    - Carrots Can't Help You See in the Dark. Here's How a World War II... (weight: 0.7891)
    - Fact or Fiction?: Carrots Improve Your Vision | Scientific American (weight: 0.7126)
    - Yes, eating carrots can help your eyesight. But it’s not a ... (weight: 0.5541)
    - Carrot (weight: 0.5335)
    - Are Carrots Good for Your Eyes? - HealthlineCarrots and Eyesight: The Truth Behind the MythYes, eating carrots can help your eyesight. But it’s not a ...Do carrots help you see at night? The truth behind popular ...Are Carrots Good for Your Eyes? Myths and Facts (weight: 0.4959)
  Top opposing:
    - Carrots Alone Won't Improve Eyesight (weight: 0.6375)
    - Does Eating Carrots Improve Your Vision? (weight: 0.475)

---
## 33. "college education is worth the cost"
Category: opinion
Expected: opinion
Actual: sources lean supporting (YES)
Claim type: opinion (0.95)
Claim domain: statistical

### Sources collected: 44 total
  - google_factcheck: 0
  - wikipedia: 5
  - semantic_scholar: 10
  - open_alex: 10
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 44 -> 24 (dropped 20)
Dropped sources:
  - [encyclopedia] "List of colleges and universities in Florida" (relevance: 0.3223, reason: relevance_0.322_below_0.35)
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
  NLI (nli_deberta): neutral (0.9932)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Protests for civil rights on campus began in the early 20th century, at Shaw University (1919), Fisk University (1924–1925), Howard University (1925) ..."

**[wikipedia] "Advanced Placement"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The program, which was then referred to as the "Kenyon Plan", was founded and pioneered at Kenyon College in Gambier, Ohio, by the then-college presid..."

**[wikipedia] "Crimson Education"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9541)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Crimson Education
Crimson Education is a multinational university admissions consultancy headquartered in Auckland, New Zealand. The business speciali..."

**[wikipedia] "Fort Worth, Texas"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9814)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Fort Worth Museum of Science and History was designed by Ricardo Legorreta of Mexico. In addition, Fort Worth is the location of several universit..."

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

**[duckduckgo] "Is College Worth the Cost? Factors to Consider"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9722)
  Verdict contribution: supporting (weight: 0.8264)
  Snippet: "According to a 2024 Gallup poll, 36% of respondents expressed a great deal or quite a lot of confidence in higher education, while 32% indicated littl..."

**[duckduckgo] "Is College Worth It In 2025? Costs, Culture, And Career Gaps"**
  Type: web | Cred: verified 0.5 | Bias: right-center | Factual: mixed
  NLI (nli_deberta): neutral (0.9761)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In fact, 9.1% of men ages 20 to 24 are currently out of work, compared to just 7.2% of women. For a generation raised to believe higher education was ..."

**[duckduckgo] "Is a College Degree Worth It in 2024? | Pew Research Center"**
  Type: web | Cred: verified 0.95 | Bias: least biased | Factual: very high
  NLI (nli_deberta): neutral (0.9253)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Pew Research Center conducted this study to better understand public views on the importance of a four-year college degree. The study also explores ke..."

**[duckduckgo] "Is College Worth It? a Cost-Benefit Analysis of College in 2025Is a College Education Still Worth It? | UCLA has the Data | UCLAIs Paying for College Still Worth It? What Salary and Cost ...Is college worth the cost? Even graduates don’t think so ..."**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.8154)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Is college worth it? A comprehensive analysis
Over the last few decades, Americans have changed their views on whether or not college is worth it. In ..."

**[duckduckgo] "Is a College Education Still Worth It? | UCLA has the Data | UCLA"**
  Type: web | Cred: estimated 0.47300000000000003
  NLI (nli_deberta): supporting (0.9985)
  Verdict contribution: supporting (weight: 0.4723)
  Snippet: "Gonzalez credits UCLA with giving him the tools he needed to discover and travel his path: a community of lifelong friends, the chance to conduct rese..."

**[duckduckgo] "Is Paying for College Still Worth It? What Salary and Cost ..."**
  Type: web | Cred: verified 0.85 | Bias: least biased | Factual: high
  NLI (nli_deberta): supporting (0.6465)
  Verdict contribution: supporting (weight: 0.5495)
  Snippet: "Apr 29, 2026 · What recent salary data shows, however, is that a college education is still worth it for most graduates...."

**[duckduckgo] "Is college worth the cost? Even graduates don’t think so ..."**
  Type: web | Cred: verified 0.85 | Bias: right-center | Factual: high
  NLI (nli_deberta): neutral (0.6558)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Americans’ views on higher education have reversed sharply in less than a generation, as the enormous cost and uncertainty about finding work have tur..."

**[duckduckgo] "Is a College Education Worth It? - The Wealthy Accountant"**
  Type: web | Cred: estimated 0.271
  NLI (nli_deberta): neutral (0.9849)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "I used a self-study course to prepare. For one summer I lived in that book. I wanted to learn as much as I could, not only for the exam, but to also h..."

**[duckduckgo] "Is College Worth The Cost?"**
  Type: web | Cred: estimated 0.2
  NLI (nli_deberta): supporting (0.8848)
  Verdict contribution: supporting (weight: 0.177)
  Snippet: "When people debate on whether or now they want to attend college, there are several thoughts that go through their head. Some people don’t believe tha..."

**[duckduckgo] "Nolte: 63% Now Believe College Is Not Worth the Cost"**
  Type: web | Cred: verified 0.5 | Bias: right | Factual: mixed
  NLI (nli_deberta): neutral (0.7251)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "A massive (and healthy) shift in public opinion has occurred, with only 33 percent of adults believing a college education is worth the cost. A poll o..."

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
  Supporting weight: 2.0251
  Opposing weight: 0.0
  Support ratio: 1.0
  Confidence: 1.0
  Verdict: **sources lean supporting**
  Neutral sources (no contribution): 20

  Top supporting:
    - Is College Worth the Cost? Factors to Consider (weight: 0.8264)
    - Is Paying for College Still Worth It? What Salary and Cost ... (weight: 0.5495)
    - Is a College Education Still Worth It? | UCLA has the Data | UCLA (weight: 0.4723)
    - Is College Worth The Cost? (weight: 0.177)

---
## 34. "inflation in the United States is under control"
Category: current_event
Expected: contested
Actual: likely supported (YES)
Claim type: factual (0.8)
Claim domain: current_events

### Sources collected: 31 total
  - google_factcheck: 4
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 3
  - duckduckgo: 10
  - wikidata: 9

### Relevance filter: 31 -> 18 (dropped 13)
Dropped sources:
  - [encyclopedia] "Fuel taxes in the United States" (relevance: 0.2859, reason: relevance_0.286_below_0.35)
  - [encyclopedia] "Rent control in the United States" (relevance: 0.2761, reason: relevance_0.276_below_0.35)
  - [encyclopedia] "2028 United States elections" (relevance: 0.1993, reason: relevance_0.199_below_0.35)
  - [encyclopedia] "2028 United States presidential election" (relevance: 0.1029, reason: relevance_0.103_below_0.35)
  - [academic] "EU Strategic Autonomy after the Russian Invasion of Ukraine: Europe's Capacity to Act in Times of War" (relevance: 0.0366, reason: relevance_0.037_below_0.35)
  - [academic] "European Integration and the War in Ukraine: Just Another Crisis?" (relevance: 0.0955, reason: relevance_0.096_below_0.35)
  - [academic] "Foreign currency exchange rate prediction using non-linear Schrödinger equations with economic fundamental parameters" (relevance: 0.2037, reason: relevance_0.204_below_0.35)
  - [knowledge_graph] "United States" (relevance: 0.1273, reason: relevance_0.127_below_0.35)
  - [knowledge_graph] "United States Census Bureau" (relevance: 0.0756, reason: relevance_0.076_below_0.35)
  - [knowledge_graph] "Mexico" (relevance: 0.035, reason: relevance_0.035_below_0.35)
  - [knowledge_graph] "Under Control" (relevance: 0.1873, reason: relevance_0.187_below_0.35)
  - [knowledge_graph] "Under Control" (relevance: 0.1262, reason: relevance_0.126_below_0.35)
  - [knowledge_graph] "Under Control" (relevance: 0.1468, reason: relevance_0.147_below_0.35)

### Dedup: 18 -> 15 (dropped 3)

### Analyzed sources (15 total)

**[google_factcheck] "President Donald Trump says the US has ‘no inflation.’ By 2 ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.717 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "If Your Time is short
By two measures — the inflation rate and the Federal Reserve’s target for "price stability" — the statement is inaccurate. The i..."

**[google_factcheck] "Has inflation eased under Trump? It depends on the measure"**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.923 | Rating: Half True
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Get PolitiFact in your inbox. Has overall inflation eased under Donald Trump? It depends on the measure
If Your Time is short
The most basic measure o..."

**[google_factcheck] "Joe Biden is mostly right that the US inflation rate is the lowest ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: PolitiFact | Enriched: True | Extract score: 0.710 | Rating: Mostly True
  NLI (factcheck_rating_bypass): supporting (0.85)
  Verdict contribution: supporting (weight: 0.7225)
  Snippet: "But does the U.S. have the lowest inflation rate among the world’s leading economies? When we last addressed how the U.S. ranks internationally in inf..."

**[google_factcheck] "FactChecking Biden on Inflation, Other Claims"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (fc_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Este artículo estará disponible en español en El Tiempo Latino. When President Joe Biden took office in January 2021, the U.S. annual rate of inflatio..."

**[wikipedia] "2021–2023 inflation surge"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9863)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Countries that supplied the United States with shoes and clothes such as Vietnam have had factory hub shortages due to not having enough vaccinated wo..."

**[duckduckgo] "Latest CPI shows inflation remains under control in United"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): neutral (0.9858)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "WASHINGTON, Jan. 13 (Xinhua) -- U.S. consumer prices rose in December, largely driven by the spike in gas prices, but the overall inflation is expecte..."

**[duckduckgo] "Inflation in the United States: A Brief Overview"**
  Type: web | Cred: estimated 0.413
  NLI (nli_deberta): supporting (0.9839)
  Verdict contribution: supporting (weight: 0.4064)
  Snippet: "Inflation in the United States: A Brief Overview
Inflation is an increase in prices over a certain period of time. Generally, inflation is a natural p..."

**[duckduckgo] "Opinion | It’s not just the United States. Inflation is"**
  Type: web | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  NLI (nli_deberta): opposing (0.9668)
  Verdict contribution: opposing (weight: 0.4834)
  Snippet: "Inflation in the United States, which is now above 5 percent and is at the highest level in more than a decade, is already causing concern. The fact t..."

**[duckduckgo] "Harvard Economist: Inflation ‘Not Getting Under Control’"**
  Type: web | Cred: estimated 0.298
  NLI (nli_deberta): neutral (0.9971)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... International’s “First Move,” Professor of Public Policy and Professor of Economics at Harvard University Ken Rogoff said that inflation in the ....."

**[duckduckgo] "Netglobalnews | Controlling Inflation, Why America’s"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): opposing (0.9492)
  Verdict contribution: opposing (weight: 0.2848)
  Snippet: "Inflation remains one of the most ... Among the most powerful structural drivers of inflation is the way healthcare is financed in the United States...."

**[duckduckgo] "Fed's Chief Says Inflation Is Under Control - The New York"**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): neutral (0.9761)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "... of this article appears in print on , Section D, Page 15 of the National edition with the headline: Fed s Chief Says Inflation Is Under Control ....."

**[duckduckgo] "Consumer Spending Archives - WSI"**
  Type: web | Cred: estimated 0.22200000000000003
  NLI (nli_deberta): supporting (0.9971)
  Verdict contribution: supporting (weight: 0.2214)
  Snippet: "Inflation is Under Control
One of the most remarkable aspects of the current economic situation is the successful containment of inflation. For years,..."

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
  Supporting weight: 1.3502
  Opposing weight: 0.7682
  Support ratio: 0.6374
  Confidence: 0.2748
  Verdict: **likely supported**
  Neutral sources (no contribution): 10

  Top supporting:
    - Joe Biden is mostly right that the US inflation rate is the lowest ... (weight: 0.7225)
    - Inflation in the United States: A Brief Overview (weight: 0.4064)
    - Consumer Spending Archives - WSI (weight: 0.2214)
  Top opposing:
    - Opinion | It’s not just the United States. Inflation is (weight: 0.4834)
    - Netglobalnews | Controlling Inflation, Why America’s (weight: 0.2848)

---
## 35. "the Amazon rainforest produces about 20% of the world's oxygen"
Category: factual_false
Expected: strongly opposed
Actual: contested (**NO - MISMATCH**)
Claim type: factual (0.8)
Claim domain: statistical

### Sources collected: 29 total
  - google_factcheck: 3
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 8
  - duckduckgo: 10
  - wikidata: 3

### Relevance filter: 29 -> 19 (dropped 10)
Dropped sources:
  - [academic] "An Atlas of Phanerozoic Paleogeographic Maps: The Seas Come In and the Seas Go Out" (relevance: 0.0728, reason: relevance_0.073_below_0.35)
  - [academic] "The 2023 report of the Lancet Countdown on health and climate change: the imperative for a health-centred response in a world facing irreversible harms" (relevance: 0.0554, reason: relevance_0.055_below_0.35)
  - [academic] "Our future in the Anthropocene biosphere" (relevance: 0.1497, reason: relevance_0.150_below_0.35)
  - [academic] "Reviewing the Impact of Land Use and Land‐Use Change on Moisture Recycling and Precipitation Patterns" (relevance: 0.2939, reason: relevance_0.294_below_0.35)
  - [academic] "Actions to halt biodiversity loss generally benefit the climate" (relevance: 0.2218, reason: relevance_0.222_below_0.35)
  - [academic] "The Angiosperm Terrestrial Revolution and the origins of modern biodiversity" (relevance: 0.3398, reason: relevance_0.340_below_0.35)
  - [academic] "Anthropogenic Drought: Definition, Challenges, and Opportunities" (relevance: 0.1729, reason: relevance_0.173_below_0.35)
  - [knowledge_graph] "Percent Free time" (relevance: 0.0555, reason: relevance_0.055_below_0.35)
  - [knowledge_graph] "⅕" (relevance: 0.0725, reason: relevance_0.072_below_0.35)
  - [knowledge_graph] "20% d’amour en plus" (relevance: 0.0665, reason: relevance_0.067_below_0.35)

### Dedup: 19 -> 19 (dropped 0)

### Analyzed sources (19 total)

**[google_factcheck] "Amazon Doesn’t Produce 20% of Earth’s Oxygen"**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: FactCheck.org | Enriched: True | Extract score: 0.778 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.9025)
  Snippet: "Q: Does the Amazon produce 20% of the world’s oxygen? A: No. Scientists estimate the percentage is closer to 6 to 9%, and the Amazon ultimately consum..."

**[google_factcheck] "Take a breath: the Amazon does not produce 20% of the world's ..."**
  Type: fact_check | Cred: verified 0.85 | Bias: left-center | Factual: high
  Publisher: AP News | Enriched: True | Extract score: 0.763 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.8075)
  Snippet: "Take a breath: the Amazon does not produce 20% of the world’s oxygen
CLAIM: The Amazon rainforest _ “the lungs of the Earth” _ produces 20% of the pla..."

**[google_factcheck] "Amazon fires are destructive, but they aren't depleting Earth's ..."**
  Type: fact_check | Cred: verified 0.95 | Bias: least biased | Factual: very high
  Publisher: The Conversation | Enriched: True | Extract score: 0.700 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.9025)
  Snippet: "Fires in the Amazon rainforest have captured attention worldwide in August. Brazilian President Jair Bolsonaro, who took office in 2019, pledged in hi..."

**[wikipedia] "Amazon rainforest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): opposing (0.6475)
  Verdict contribution: opposing (weight: 0.5504)
  Snippet: "Large scale deforestation is occurring in the forest, creating different harmful effects. Economic losses due to deforestation in Brazil could be appr..."

**[wikipedia] "Deforestation of the Amazon rainforest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.751)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "In May 2025, research from the University of Maryland’s Global Land Analysis and Discovery (GLAD) Lab, published via the World Resources Institute’s G..."

**[wikipedia] "Rainforest"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9912)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Tropical rainforests have been called the "jewels of the Earth" and the "world's largest pharmacy", because over one quarter of natural medicines have..."

**[wikipedia] "Tropical rainforest"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9668)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Tropical rainforests are among the most threatened ecosystems globally due to large-scale fragmentation as a result of human activity. Habitat fragmen..."

**[wikipedia] "2019 Amazon rainforest wildfires"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9697)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The increasing rates were first reported by Brazil's National Institute for Space Research (Instituto Nacional de Pesquisas Espaciais, INPE) in June a..."

**[open_alex] "Ecosystem services provided by marine and freshwater phytoplankton"**
  Type: academic | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9946)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Phytoplankton, the ecological group of microalgae adapted to live in apparent suspension in water masses, is much more than an ecosystem's engineer. I..."

**[duckduckgo] "Why the Amazon doesn't really produce 20% of the world's oxygen"**
  Type: web | Cred: verified 0.85 | Bias: pro-science | Factual: high
  NLI (nli_deberta): supporting (0.981)
  Verdict contribution: supporting (weight: 0.8338)
  Snippet: "Why the Amazon doesn’t really produce 20% of the world’s oxygen
The myth that the Amazon rainforest forms the “lungs of the Earth” is overstated. Here..."

**[duckduckgo] "For decades, the Amazon rainforest has been credited with producing ..."**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.959)
  Verdict contribution: supporting (weight: 0.4795)
  Snippet: "Aug 30, 2025 · The Amazon Rainforest produces 20% of the world's oxygen and is often referred to as the “lungs of the Earth.” It is also home to 10% o..."

**[duckduckgo] "Amazon Rainforest Facts - One Tree Planted"**
  Type: web | Cred: estimated 0.46900000000000003
  NLI (nli_deberta): supporting (0.9683)
  Verdict contribution: supporting (weight: 0.4541)
  Snippet: "Our projects focus on restoring priority landscapes around the world—places where forests can make the biggest difference for nature and communities. ..."

**[duckduckgo] "Does the amazon provide 20% of our oxygen? - Oxford Ecosystems"**
  Type: web | Cred: unverified 0.3
  NLI (nli_deberta): supporting (0.4297)
  Verdict contribution: supporting (weight: 0.1289)
  Snippet: "The increases fires have major consequences for regional climate, the rich Amazonian biodiversity, air quality and human health, and some consequence ..."

**[duckduckgo] "How much oxygen comes from the ocean?"**
  Type: web | Cred: estimated 0.49800000000000005
  NLI (nli_deberta): neutral (0.9253)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Scientists estimate that roughly half of the oxygen production on Earth comes from the ocean. The majority of this production is from oceanic plankton..."

**[duckduckgo] "does the amazon provide 20% of our oxygen? - YADVINDER MALHI"**
  Type: web | Cred: estimated 0.22400000000000003
  NLI (nli_deberta): opposing (0.9956)
  Verdict contribution: opposing (weight: 0.223)
  Snippet: "Aug 24, 2019 · So, in all practical terms, the net contribution of the Amazon ECOSYSTEM (not just the plants alone) to the world's oxygen is effective..."

**[duckduckgo] "Use Your Head – the Amazon isn't Our Lungs | CLEAR Center"**
  Type: web | Cred: estimated 0.372
  NLI (nli_deberta): neutral (0.5469)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Sep 2, 2019 · In fact, we have a glut of the stuff that we humans need to live; our atmosphere is 20.9 percent oxygen. If the Amazon rainforest were t..."

**[duckduckgo] "If WWF says the Amazon rainforest produces 20% of the worlds oxygen ..."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Feb 2, 2014 · TIL that rainforests are responsible for roughly one-third (28%) of the Earth's oxygen but most (70%) of the oxygen in the atmosphere is..."

**[duckduckgo] "No, the Amazon fires won't deplete the Earth's oxygen supply. Here's why."**
  Type: web | Cred: verified 0.85 | Bias: left-center | Factual: high
  NLI (nli_deberta): supporting (0.9624)
  Verdict contribution: supporting (weight: 0.818)
  Snippet: "French President Emmanuel Macron tweeted on Aug. 22 that "the Amazon rain forest – the lungs which produces 20% of our planet's oxygen – is on fire." ..."

**[duckduckgo] "How much of the World's Oxygen Comes from the Amazon Rainforest?"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): supporting (0.9629)
  Verdict contribution: supporting (weight: 0.4814)
  Snippet: "Feb 19, 2017 · The Amazon produces 20% of Earth's oxygen, but the alarming rate of deforestation can greatly affect the Amazon's potential to produce ..."

### Verdict computation
  Supporting weight: 3.1959
  Opposing weight: 3.3859
  Support ratio: 0.4856
  Confidence: 0.0289
  Verdict: **contested**
  Neutral sources (no contribution): 8

  Top supporting:
    - Why the Amazon doesn't really produce 20% of the world's oxygen (weight: 0.8338)
    - No, the Amazon fires won't deplete the Earth's oxygen supply. Here's why. (weight: 0.818)
    - How much of the World's Oxygen Comes from the Amazon Rainforest? (weight: 0.4814)
    - For decades, the Amazon rainforest has been credited with producing ... (weight: 0.4795)
    - Amazon Rainforest Facts - One Tree Planted (weight: 0.4541)
  Top opposing:
    - Amazon Doesn’t Produce 20% of Earth’s Oxygen (weight: 0.9025)
    - Amazon fires are destructive, but they aren't depleting Earth's ... (weight: 0.9025)
    - Take a breath: the Amazon does not produce 20% of the world's ... (weight: 0.8075)
    - Amazon rainforest (weight: 0.5504)
    - does the amazon provide 20% of our oxygen? - YADVINDER MALHI (weight: 0.223)

---
## 36. "the Great Wall of China is the only man-made structure visible from space"
Category: factual_false
Expected: strongly opposed
Actual: strongly opposed (YES)
Claim type: factual (0.8)
Claim domain: historical

### Sources collected: 22 total
  - google_factcheck: 1
  - wikipedia: 5
  - semantic_scholar: 0
  - open_alex: 0
  - duckduckgo: 10
  - wikidata: 6

### Relevance filter: 22 -> 17 (dropped 5)
Dropped sources:
  - [encyclopedia] "Plan 9 from Outer Space" (relevance: 0.1032, reason: relevance_0.103_below_0.35)
  - [knowledge_graph] "galaxy filament" (relevance: 0.3122, reason: relevance_0.312_below_0.35)
  - [knowledge_graph] "People's Republic of China" (relevance: 0.2424, reason: relevance_0.242_below_0.35)
  - [knowledge_graph] "Taiwan" (relevance: 0.137, reason: relevance_0.137_below_0.35)
  - [knowledge_graph] "China" (relevance: 0.2314, reason: relevance_0.231_below_0.35)

### Dedup: 17 -> 15 (dropped 2)

### Analyzed sources (15 total)

**[google_factcheck] "Is the Great Wall of China Visible from the Moon?"**
  Type: fact_check | Cred: verified 0.5 | Bias: left-center | Factual: mixed
  Publisher: Snopes | Enriched: True | Extract score: 0.789 | Rating: False
  NLI (factcheck_rating_bypass): opposing (0.95)
  Verdict contribution: opposing (weight: 0.475)
  Snippet: "The claim that China's Great Wall is the only man-made object that can be seen from the moon with the naked eye is one of our more tenaciously incorre..."

**[wikipedia] "Artificial structures visible from space"**
  Type: encyclopedia | Cred: estimated 0.7
  NLI (nli_deberta): opposing (0.9766)
  Verdict contribution: opposing (weight: 0.6836)
  Snippet: "Artificial structures visible from space
Artificial structures visible from space without magnification include highways, dams, and cities. Whether an..."

**[wikipedia] "Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.85
  NLI (nli_deberta): neutral (0.9565)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "From the Moon
The Great Wall of China cannot be seen by the naked human eye from the Moon which orbits around Earth at an average distance of 384,399 ..."

**[wikipedia] "History of the Great Wall of China"**
  Type: encyclopedia | Cred: estimated 0.9
  NLI (nli_deberta): neutral (0.7524)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Radiocarbon analysis showed that they were constructed from 1040 to 1160. The walls were as tall as 2.75 metres (9 ft 0 in) at places when they were d..."

**[wikipedia] "Ming Great Wall"**
  Type: encyclopedia | Cred: estimated 0.8
  NLI (nli_deberta): neutral (0.9893)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Ming Great Wall
The Ming Great Wall (Chinese: 明長城; pinyin: Míng Chángchéng), built by the Ming dynasty (1368–1644), forms the most visible parts of th..."

**[duckduckgo] "Great Wall - NASA"**
  Type: web | Cred: verified 0.95 | Factual: very high
  NLI (nli_deberta): neutral (0.9941)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Great Wall of China and Inner Mongolia are featured in this image photographed by Expedition 10 Commander Leroy Chiao on the International Space S..."

**[duckduckgo] "TIL the Great Wall of China is not actually visible from space, its just ..."**
  Type: web | Cred: estimated 0.596
  NLI (nli_deberta): neutral (0.9976)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "May 6, 2025 ... Veteran US astronaut Gene Cernan has stated: "At Earth orbit of 100 miles (160 km) to 200 miles (320 km) high, the Great Wall of China..."

**[duckduckgo] "Is it Really Possible to See the Great Wall of China from Space with ..."**
  Type: web | Cred: estimated 0.5780000000000001
  NLI (nli_deberta): opposing (0.9902)
  Verdict contribution: opposing (weight: 0.5723)
  Snippet: "In this picture the wall looked like a route full of bends that resembled river meanders. One week later, when everything seemed perfectly clear and t..."

**[duckduckgo] "What makes the Great Wall of China the only man-made object ..."**
  Type: web | Cred: estimated 0.42400000000000004
  NLI (nli_deberta): supporting (0.9663)
  Verdict contribution: supporting (weight: 0.4097)
  Snippet: "What makes the Great Wall of China the only man-made object visible from space? Category: Space Published: December 11, 2012
By: Christopher S. Baird,..."

**[duckduckgo] "The Great Wall of China from Space.. - Facebook"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): opposing (0.8999)
  Verdict contribution: opposing (weight: 0.45)
  Snippet: "1 day ago ... Nah, that's a myth! The Great Wall of China isn't visible from space with the naked eye. It's a pretty big structure, but it's not that ..."

**[duckduckgo] "Can you see the Great Wall of China from space?"**
  Type: web | Cred: estimated 0.282
  NLI (nli_deberta): neutral (0.4897)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "One space-based myth that we all have heard is the idea the Great Wall of China is the only human-made structure that can be seen from space. More Ear..."

**[duckduckgo] "What Makes The Great Wall of China The Only Man Made Object ..."**
  Type: web | Cred: estimated 0.741
  NLI (nli_deberta): neutral (0.8428)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Contact us Developers Policy & Safety How YouTube works Test new features NFL Sunday Ticket © 2026 Google LLC..."

**[duckduckgo] "The Great Wall of China Is Not Visible From Space Great ... - Facebook"**
  Type: web | Cred: verified 0.5 | Bias: left | Factual: mixed
  NLI (nli_deberta): opposing (0.9937)
  Verdict contribution: opposing (weight: 0.4969)
  Snippet: "Dec 21, 2025 ... The Great Wall of China Is Not Visible From Space Great Wall of China is often said to be visible from space but that's a myth. From ..."

**[duckduckgo] "Forget the Great Wall: the human landmark astronauts actually see ..."**
  Type: web | Cred: estimated 0.281
  NLI (nli_deberta): neutral (0.6797)
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "The Great Wall myth: a 300-year-old guess
The idea that the Great Wall of China is visible from the Moon didn’t start with the space age; it likely tr..."

**[wikidata] "Great Wall Motor"**
  Type: knowledge_graph | Cred: estimated 0.85
  NLI (wikidata_skip): N/A
  Verdict contribution: neutral (no contribution) (weight: 0)
  Snippet: "Chinese vehicle manufacturing company | instance of: automobile manufacturer | country: People's Republic of China | inception: 1984-00-00 | headquart..."

### Verdict computation
  Supporting weight: 0.4097
  Opposing weight: 2.6778
  Support ratio: 0.1327
  Confidence: 0.7346
  Verdict: **strongly opposed**
  Neutral sources (no contribution): 9

  Top supporting:
    - What makes the Great Wall of China the only man-made object ... (weight: 0.4097)
  Top opposing:
    - Artificial structures visible from space (weight: 0.6836)
    - Is it Really Possible to See the Great Wall of China from Space with ... (weight: 0.5723)
    - The Great Wall of China Is Not Visible From Space Great ... - Facebook (weight: 0.4969)
    - Is the Great Wall of China Visible from the Moon? (weight: 0.475)
    - The Great Wall of China from Space.. - Facebook (weight: 0.45)
