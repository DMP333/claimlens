# Phase 1 Final Audit: NLI Accuracy
Generated: 2026-05-25 17:15:57
Model: DeBERTa-v3-base-mnli-fever-anli
Test samples: 105

## Overall: 75/105 (71.4%)

## Accuracy by Pattern

| Pattern | Correct | Total | Accuracy |
|---------|---------|-------|----------|
| academic_neutral | 4 | 4 | 100.0% |
| encyclopedic_neutral | 7 | 10 | 70.0% |
| genuine_oppose | 5 | 10 | 50.0% |
| genuine_support | 10 | 10 | 100.0% |
| keyword_assoc | 10 | 11 | 90.9% |
| reporting_frame | 26 | 35 | 74.3% |
| sentiment_stance | 8 | 8 | 100.0% |
| weak_negation | 1 | 12 | 8.3% |
| web_debunk | 4 | 5 | 80.0% |

## Confusion Matrix

| Expected \ Predicted | supporting | neutral | opposing |
|---------------------|-----------|---------|----------|
| supporting | 18 | 0 | 0 |
| neutral | 5 | 33 | 4 |
| opposing | 4 | 17 | 24 |

## All Errors (30)

**[reporting_frame]** Expected: neutral, Got: supporting (0.5503)
  Claim: "humans swallow eight spiders per year in their sle"
  Source: "The popular idea that humans swallow eight spiders per year in their sleep has b..."

**[reporting_frame]** Expected: neutral, Got: supporting (0.6221)
  Claim: "lightning never strikes the same place twice"
  Source: "The popular conception that lightning never strikes the same place twice is freq..."

**[reporting_frame]** Expected: opposing, Got: supporting (0.6421)
  Claim: "lemmings commit mass suicide"
  Source: "Lemmings throw themselves off cliffs in mass suicide events. This is one of the ..."

**[reporting_frame]** Expected: opposing, Got: supporting (0.9893)
  Claim: "the tongue has specific taste zones"
  Source: "The tongue has specific taste zones: sweet at the tip, sour on the sides, bitter..."

**[reporting_frame]** Expected: neutral, Got: supporting (0.6489)
  Claim: "chemtrails are used for population control"
  Source: "Proponents of the theory argue that chemtrails, the white trails left by aircraf..."

**[reporting_frame]** Expected: neutral, Got: supporting (0.6416)
  Claim: "Area 51 houses alien technology"
  Source: "Believers in the conspiracy suggest that Area 51, a classified US Air Force faci..."

**[reporting_frame]** Expected: neutral, Got: supporting (0.9561)
  Claim: "crop circles are made by aliens"
  Source: "Adherents of this theory maintain that crop circles appearing in agricultural fi..."

**[reporting_frame]** Expected: opposing, Got: neutral (0.7563)
  Claim: "we only use a small fraction of our brain"
  Source: "It's one of the most enduring pieces of pseudoscience in popular culture: the id..."

**[reporting_frame]** Expected: opposing, Got: neutral (0.8857)
  Claim: "natural remedies are safer than pharmaceutical dru"
  Source: "One of the oldest and most debunked claims in alternative medicine is that natur..."

**[keyword_assoc]** Expected: neutral, Got: opposing (0.8896)
  Claim: "the Bermuda Triangle has supernatural powers"
  Source: "Researchers who study Bermuda Triangle disappearances have identified several na..."

**[weak_negation]** Expected: opposing, Got: neutral (0.772)
  Claim: "cracking your knuckles causes arthritis"
  Source: "Most rheumatologists don't think there is a meaningful connection between habitu..."

**[weak_negation]** Expected: opposing, Got: neutral (0.5811)
  Claim: "Bigfoot exists"
  Source: "Despite decades of research, scientists have failed to find any credible evidenc..."

**[weak_negation]** Expected: opposing, Got: neutral (0.7227)
  Claim: "coffee stunts your growth"
  Source: "The evidence linking moderate coffee consumption to stunted growth in children r..."

**[weak_negation]** Expected: opposing, Got: supporting (0.8828)
  Claim: "reading in dim light damages your eyes"
  Source: "Researchers have been unable to replicate early findings that suggested reading ..."

**[weak_negation]** Expected: opposing, Got: neutral (0.9497)
  Claim: "the Bermuda Triangle causes ships to disappear"
  Source: "Marine investigators have found little to suggest that the rate of disappearance..."

**[weak_negation]** Expected: opposing, Got: neutral (0.6621)
  Claim: "detox diets remove toxins from your body"
  Source: "Controlled trials have consistently failed to demonstrate that detox diets provi..."

**[weak_negation]** Expected: opposing, Got: neutral (0.9824)
  Claim: "breakfast is the most important meal of the day"
  Source: "Pediatric nutrition experts generally do not support the claim that eating break..."

**[weak_negation]** Expected: opposing, Got: neutral (0.9268)
  Claim: "the Loch Ness monster is real"
  Source: "Attempts to verify reports of Loch Ness monster sightings using sonar mapping an..."

**[weak_negation]** Expected: opposing, Got: neutral (0.9355)
  Claim: "humans swallow eight spiders per year in their sle"
  Source: "Sleep researchers have found no basis for the claim that humans regularly ingest..."

**[weak_negation]** Expected: opposing, Got: neutral (0.9609)
  Claim: "homework improves academic performance"
  Source: "Meta-analyses of homework research have struggled to establish a clear causal re..."

**[weak_negation]** Expected: opposing, Got: neutral (0.9922)
  Claim: "sugar makes children hyperactive"
  Source: "While some early studies hinted at a connection, subsequent larger trials have n..."

**[genuine_oppose]** Expected: opposing, Got: neutral (0.8237)
  Claim: "the Loch Ness monster is real"
  Source: "Extensive sonar surveys of Loch Ness conducted over several decades have found n..."

**[genuine_oppose]** Expected: opposing, Got: neutral (0.5474)
  Claim: "Vikings wore horned helmets"
  Source: "No archaeological evidence supports the claim that Vikings wore horned helmets...."

**[genuine_oppose]** Expected: opposing, Got: neutral (0.7612)
  Claim: "detox diets are necessary to remove toxins"
  Source: "There is no scientific mechanism by which the body accumulates environmental tox..."

**[genuine_oppose]** Expected: opposing, Got: neutral (0.9268)
  Claim: "touching a baby bird makes its mother abandon it"
  Source: "Ornithologists confirm that most bird species have a very limited sense of smell..."

**[genuine_oppose]** Expected: opposing, Got: supporting (0.6831)
  Claim: "Napoleon was short"
  Source: "Napoleon Bonaparte stood approximately 5 feet 7 inches tall, which was average o..."

**[encyclopedic_neutral]** Expected: neutral, Got: opposing (0.9946)
  Claim: "crop circles are made by aliens"
  Source: "Crop circles are patterns created by flattening crops such as wheat, barley, and..."

**[encyclopedic_neutral]** Expected: neutral, Got: opposing (0.9951)
  Claim: "the Loch Ness monster is real"
  Source: "The Loch Ness Monster, affectionately known as Nessie, is a mythical creature sa..."

**[encyclopedic_neutral]** Expected: neutral, Got: opposing (0.8804)
  Claim: "chemtrails are used for population control"
  Source: "Chemtrails, short for chemical trails, is a term used in conspiracy discourse to..."

**[web_debunk]** Expected: opposing, Got: neutral (0.7554)
  Claim: "breakfast is the most important meal of the day"
  Source: "Is breakfast really the most important meal of the day? Recent nutritional resea..."
