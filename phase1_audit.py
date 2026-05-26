"""
Phase 1 Final Audit

Two tests:
1. NLI accuracy on labeled test dataset (tests discusses-vs-endorses,
   keyword association, weak negation, genuine support/oppose patterns)
2. Pipeline metrics summary from baseline test results

Usage:
  python phase1_audit.py                    # run NLI test only
  python phase1_audit.py --with-pipeline    # also re-run pipeline metrics

Output: tests/phase1_audit_report.md
"""

import argparse
import csv
import os
from datetime import datetime
from collections import Counter, defaultdict

# -- NLI Test Dataset ----------------------------------------------------------
# Labels: 0 = supporting, 1 = neutral, 2 = opposing

NLI_TEST_DATA = [
    # reporting_frame: sources that discuss/report on a claim
    # Expected: neutral (label 1) - these REPORT ON the claim, don't endorse it
    {"source": "The notion that the Bermuda Triangle causes ships to disappear has persisted in popular culture for decades, inspiring numerous books and documentaries.", "claim": "the Bermuda Triangle causes ships to disappear", "label": 1, "pattern": "reporting_frame"},
    {"source": "The widely held belief that cracking your knuckles causes arthritis has been a source of concern for many people.", "claim": "cracking your knuckles causes arthritis", "label": 1, "pattern": "reporting_frame"},
    {"source": "The popular idea that humans swallow eight spiders per year in their sleep has become one of the most shared facts on the internet.", "claim": "humans swallow eight spiders per year in their sleep", "label": 1, "pattern": "reporting_frame"},
    {"source": "The common perception that Napoleon Bonaparte was unusually short has been referenced in countless historical discussions and pop culture.", "claim": "Napoleon was short", "label": 1, "pattern": "reporting_frame"},
    {"source": "The longstanding belief that bulls are enraged by the color red has shaped traditions like bullfighting for centuries.", "claim": "bulls are enraged by the color red", "label": 1, "pattern": "reporting_frame"},
    {"source": "The widespread notion that bats are completely blind has made them a symbol of poor eyesight in many cultures.", "claim": "bats are blind", "label": 1, "pattern": "reporting_frame"},
    {"source": "The prevailing assumption that breakfast is the most important meal of the day has influenced dietary guidelines worldwide.", "claim": "breakfast is the most important meal of the day", "label": 1, "pattern": "reporting_frame"},
    {"source": "The popular conception that lightning never strikes the same place twice is frequently cited as common knowledge.", "claim": "lightning never strikes the same place twice", "label": 1, "pattern": "reporting_frame"},

    # reporting_frame with debunking language - Expected: opposing (label 2)
    {"source": "The myth that you lose most of your body heat through your head has been thoroughly debunked by thermal imaging studies.", "claim": "you lose most body heat through your head", "label": 2, "pattern": "reporting_frame"},
    {"source": "The common misconception that chameleons change color to match their surroundings has been corrected by biologists who study these reptiles.", "claim": "chameleons change color to match their surroundings", "label": 2, "pattern": "reporting_frame"},
    {"source": "The persistent myth that Einstein failed mathematics in school is contradicted by his actual academic records, which show excellent grades.", "claim": "Einstein failed math in school", "label": 2, "pattern": "reporting_frame"},
    {"source": "The widespread misconception that Vikings wore horned helmets has no archaeological basis and originated from 19th-century artistic depictions.", "claim": "Vikings wore horned helmets", "label": 2, "pattern": "reporting_frame"},
    {"source": "The popular myth that touching a baby bird will cause its mother to abandon it has been repeatedly debunked by ornithologists.", "claim": "touching a baby bird makes its mother abandon it", "label": 2, "pattern": "reporting_frame"},
    {"source": "The enduring myth that shaving causes hair to grow back thicker and darker has been disproved by multiple dermatological studies.", "claim": "shaving makes hair grow back thicker", "label": 2, "pattern": "reporting_frame"},
    {"source": "The misconception that dogs can only see in black and white was overturned when researchers discovered that canines have two types of color receptors.", "claim": "dogs can only see in black and white", "label": 2, "pattern": "reporting_frame"},
    {"source": "The common myth that ostriches bury their heads in the sand when frightened is not supported by any observed behavior in the wild.", "claim": "ostriches bury their heads in the sand", "label": 2, "pattern": "reporting_frame"},
    {"source": "The old wives' tale that coffee stunts children's growth has no scientific support, according to pediatric nutrition experts.", "claim": "coffee stunts your growth", "label": 2, "pattern": "reporting_frame"},
    {"source": "The widely repeated myth that daddy longlegs are the most venomous spiders in the world is doubly wrong: they are neither particularly venomous nor technically spiders.", "claim": "daddy longlegs are the most venomous spiders", "label": 2, "pattern": "reporting_frame"},
    {"source": 'Lemmings throw themselves off cliffs in mass suicide events. This is one of the most persistent myths in popular zoology, originating from a staged Disney documentary in the 1950s.', "claim": "lemmings commit mass suicide", "label": 2, "pattern": "reporting_frame"},
    {"source": "You need to wait 24 hours before filing a missing person report. This widespread belief is actually false, and police departments across the country encourage immediate reporting.", "claim": "you need to wait 24 hours to report a missing person", "label": 2, "pattern": "reporting_frame"},
    {"source": "Blood is blue inside your body before it's exposed to oxygen. This common claim is incorrect. Blood is always red, though deoxygenated blood appears darker.", "claim": "blood is blue inside your body", "label": 2, "pattern": "reporting_frame"},
    {"source": "The tongue has specific taste zones: sweet at the tip, sour on the sides, bitter at the back. This model, taught in schools for decades, has been thoroughly refuted.", "claim": "the tongue has specific taste zones", "label": 2, "pattern": "reporting_frame"},
    {"source": "Sugar makes children hyperactive. Despite how firmly many parents believe this, controlled studies consistently find no causal link between sugar consumption and hyperactivity.", "claim": "sugar makes children hyperactive", "label": 2, "pattern": "reporting_frame"},
    {"source": "Conspiracy theories claim that the Illuminati secretly controls world governments through financial manipulation and media ownership.", "claim": "the Illuminati controls world governments", "label": 1, "pattern": "reporting_frame"},
    {"source": "Proponents of the theory argue that chemtrails, the white trails left by aircraft, are actually chemical agents sprayed for population control purposes.", "claim": "chemtrails are used for population control", "label": 1, "pattern": "reporting_frame"},
    {"source": "Believers in the conspiracy suggest that Area 51, a classified US Air Force facility in Nevada, houses recovered alien spacecraft and extraterrestrial technology.", "claim": "Area 51 houses alien technology", "label": 1, "pattern": "reporting_frame"},
    {"source": "Some theorists have claimed that the sinking of the Titanic was actually an elaborate insurance fraud involving the ship's sister vessel, the Olympic.", "claim": "the Titanic sinking was an insurance scam", "label": 1, "pattern": "reporting_frame"},
    {"source": "Adherents of this theory maintain that crop circles appearing in agricultural fields are created by extraterrestrial visitors attempting to communicate with humanity.", "claim": "crop circles are made by aliens", "label": 1, "pattern": "reporting_frame"},
    {"source": "Flat Earth advocates argue that all photographs of a spherical Earth taken from space have been fabricated by government agencies.", "claim": "all space photos of Earth are fabricated", "label": 1, "pattern": "reporting_frame"},
    {"source": "It's one of the most enduring pieces of pseudoscience in popular culture: the idea that we only use a fraction of our brain capacity.", "claim": "we only use a small fraction of our brain", "label": 2, "pattern": "reporting_frame"},
    {"source": "Perhaps the most widespread piece of nutritional misinformation is the claim that detox diets and cleanses can remove accumulated toxins from your body.", "claim": "detox diets remove toxins from your body", "label": 2, "pattern": "reporting_frame"},
    {"source": "One of the oldest and most debunked claims in alternative medicine is that natural remedies are inherently safer than pharmaceutical drugs.", "claim": "natural remedies are safer than pharmaceutical drugs", "label": 2, "pattern": "reporting_frame"},
    {"source": "A 2019 survey found that approximately 40% of respondents believed that crop circles were created by extraterrestrial beings, while 35% attributed them to natural phenomena.", "claim": "crop circles are made by aliens", "label": 1, "pattern": "reporting_frame"},
    {"source": "According to a poll conducted by Chapman University, roughly 20% of Americans believe that the government is concealing information about alien encounters.", "claim": "the government is hiding alien encounters", "label": 1, "pattern": "reporting_frame"},
    {"source": "Research published in the Journal of Consumer Psychology examined why the belief that sugar causes hyperactivity in children persists despite contradictory evidence.", "claim": "sugar makes children hyperactive", "label": 1, "pattern": "reporting_frame"},

    # keyword_assoc: keyword overlap but neutral content
    {"source": "Researchers who study Bermuda Triangle disappearances have identified several natural explanations, including methane gas eruptions and rogue waves.", "claim": "the Bermuda Triangle has supernatural powers", "label": 1, "pattern": "keyword_assoc"},
    {"source": "The psychology of people who believe in Bigfoot reveals interesting patterns in how humans process ambiguous sensory information in wilderness settings.", "claim": "Bigfoot exists", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Historians who specialize in the Napoleonic era have extensively documented the emperor's military campaigns across Europe and their lasting impact on international law.", "claim": "Napoleon was the greatest military leader of all time", "label": 1, "pattern": "keyword_assoc"},
    {"source": "The sociology of conspiracy theory adoption examines how social networks and cognitive biases contribute to the spread of alternative explanations for major events.", "claim": "conspiracy theories are usually true", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Economists studying universal basic income programs have modeled the potential effects on labor force participation using data from pilot programs in Finland and Kenya.", "claim": "universal basic income would reduce poverty", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Meteorologists who study lightning patterns have placed sensors on tall buildings and communication towers to understand strike frequency and distribution.", "claim": "lightning never strikes the same place twice", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Marine biologists studying deep-sea ecosystems in the Atlantic have catalogued over 300 previously unknown species in the region between Bermuda and Puerto Rico.", "claim": "the Bermuda Triangle causes ships to disappear", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Criminal justice researchers examining the relationship between surveillance technology and crime rates have published conflicting findings across different metropolitan areas.", "claim": "video surveillance reduces crime", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Educational psychologists have been studying how homework policies vary across countries and their correlation with standardized test performance.", "claim": "homework improves academic performance", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Nutritional scientists who research breakfast habits have tracked the dietary patterns of over 10,000 participants across a five-year longitudinal study.", "claim": "breakfast is the most important meal of the day", "label": 1, "pattern": "keyword_assoc"},
    {"source": "Climate researchers studying electric vehicle adoption patterns have modeled the infrastructure requirements for widespread EV charging networks.", "claim": "electric cars are better for the environment", "label": 1, "pattern": "keyword_assoc"},

    # weak_negation: negation without strong explicit opposing signal
    {"source": "Most rheumatologists don't think there is a meaningful connection between habitual knuckle cracking and the later development of arthritis.", "claim": "cracking your knuckles causes arthritis", "label": 2, "pattern": "weak_negation"},
    {"source": "Despite decades of research, scientists have failed to find any credible evidence supporting the existence of a large primate species in the Pacific Northwest.", "claim": "Bigfoot exists", "label": 2, "pattern": "weak_negation"},
    {"source": "The evidence linking moderate coffee consumption to stunted growth in children remains inconclusive at best, with most large-scale studies finding no significant effect.", "claim": "coffee stunts your growth", "label": 2, "pattern": "weak_negation"},
    {"source": "Researchers have been unable to replicate early findings that suggested reading in low-light conditions causes permanent damage to eyesight.", "claim": "reading in dim light damages your eyes", "label": 2, "pattern": "weak_negation"},
    {"source": "Marine investigators have found little to suggest that the rate of disappearances in the Bermuda Triangle region exceeds what would be expected for any comparably trafficked area of ocean.", "claim": "the Bermuda Triangle causes ships to disappear", "label": 2, "pattern": "weak_negation"},
    {"source": "Controlled trials have consistently failed to demonstrate that detox diets provide any measurable benefit beyond what the liver and kidneys already accomplish naturally.", "claim": "detox diets remove toxins from your body", "label": 2, "pattern": "weak_negation"},
    {"source": "Pediatric nutrition experts generally do not support the claim that eating breakfast has a unique or outsized impact on health compared to other meals.", "claim": "breakfast is the most important meal of the day", "label": 2, "pattern": "weak_negation"},
    {"source": "Attempts to verify reports of Loch Ness monster sightings using sonar mapping and underwater cameras have yielded no confirmed evidence of a large unknown creature.", "claim": "the Loch Ness monster is real", "label": 2, "pattern": "weak_negation"},
    {"source": "The data does not convincingly show that standardized tests measure innate intelligence rather than test-taking skills and socioeconomic background.", "claim": "standardized testing accurately measures intelligence", "label": 2, "pattern": "weak_negation"},
    {"source": "Sleep researchers have found no basis for the claim that humans regularly ingest spiders during sleep, noting that vibrations from breathing would deter any approaching arachnid.", "claim": "humans swallow eight spiders per year in their sleep", "label": 2, "pattern": "weak_negation"},
    {"source": "Meta-analyses of homework research have struggled to establish a clear causal relationship between homework quantity and academic achievement, particularly at the elementary school level.", "claim": "homework improves academic performance", "label": 2, "pattern": "weak_negation"},
    {"source": "While some early studies hinted at a connection, subsequent larger trials have not been able to confirm that moderate sugar intake directly causes behavioral changes in children.", "claim": "sugar makes children hyperactive", "label": 2, "pattern": "weak_negation"},

    # sentiment_stance: has sentiment but factual stance is supporting (label 0)
    {"source": "Automation will eliminate millions of manufacturing jobs in the coming decade, devastating communities that depend on factory employment and widening the inequality gap.", "claim": "automation will eliminate manufacturing jobs", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Rising sea levels will displace millions of coastal residents, creating unprecedented refugee crises and overwhelming existing immigration systems.", "claim": "rising sea levels will displace coastal residents", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Antibiotic resistance is spreading at an alarming rate, threatening to render many common medical procedures dangerous and potentially pushing humanity into a post-antibiotic era.", "claim": "antibiotic resistance is spreading", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Standardized testing does measure certain cognitive skills, but at the terrible cost of narrowing curricula, increasing student anxiety, and punishing creative thinking.", "claim": "standardized testing measures cognitive skills", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Surveillance cameras have been shown to reduce certain types of street crime, though critics rightly point out the chilling effect on civil liberties and the disproportionate targeting of minorities.", "claim": "surveillance cameras reduce street crime", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Factory farming does produce cheaper food, but the environmental destruction, animal suffering, and public health risks it creates make the true cost far higher than the price tag suggests.", "claim": "factory farming produces cheaper food", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Urban sprawl is accelerating across developing nations, swallowing agricultural land and straining infrastructure in ways that threaten long-term sustainability.", "claim": "urban sprawl is accelerating in developing nations", "label": 0, "pattern": "sentiment_stance"},
    {"source": "Cryptocurrency mining does secure blockchain networks, but the enormous energy consumption involved is an environmental catastrophe that undermines any claims of technological progress.", "claim": "cryptocurrency mining secures blockchain networks", "label": 0, "pattern": "sentiment_stance"},

    # genuine_support: clearly supporting (label 0)
    {"source": "Multiple peer-reviewed studies have confirmed that habitual exercise reduces the risk of cardiovascular disease, with even moderate activity providing significant protective benefits.", "claim": "exercise reduces the risk of heart disease", "label": 0, "pattern": "genuine_support"},
    {"source": "Photosynthesis is the process by which green plants convert sunlight, water, and carbon dioxide into glucose and oxygen, providing the foundation for nearly all food chains on Earth.", "claim": "photosynthesis converts sunlight into energy for plants", "label": 0, "pattern": "genuine_support"},
    {"source": "The Earth completes one full orbit around the Sun approximately every 365.25 days, which is why our calendar includes a leap year every four years.", "claim": "the Earth orbits the Sun", "label": 0, "pattern": "genuine_support"},
    {"source": "Deoxyribonucleic acid, commonly known as DNA, is the molecule that carries the genetic instructions for the development, functioning, and reproduction of all known living organisms.", "claim": "DNA contains genetic information", "label": 0, "pattern": "genuine_support"},
    {"source": "Gravity is the fundamental force that causes all objects with mass to attract one another, and is responsible for keeping planets in orbit around stars.", "claim": "gravity causes objects to attract each other", "label": 0, "pattern": "genuine_support"},
    {"source": "Archaeological evidence shows that the ancient Egyptians built the pyramids at Giza using organized labor forces, ramps, and copper tools over a period of approximately 20 years.", "claim": "the ancient Egyptians built the pyramids", "label": 0, "pattern": "genuine_support"},
    {"source": "The speed of sound in dry air at 20 degrees Celsius is approximately 343 meters per second, a figure that has been precisely measured using multiple independent methods.", "claim": "the speed of sound is approximately 343 meters per second", "label": 0, "pattern": "genuine_support"},
    {"source": "Antibodies are Y-shaped proteins produced by B cells in the immune system that bind to specific antigens on pathogens, marking them for destruction by other immune cells.", "claim": "antibodies are part of the immune system", "label": 0, "pattern": "genuine_support"},
    {"source": "Exposure to ultraviolet radiation from the sun is the primary cause of skin cancer, with cumulative UV damage to skin cell DNA leading to mutations over time.", "claim": "UV radiation causes skin cancer", "label": 0, "pattern": "genuine_support"},
    {"source": "The Antarctic ice sheet contains approximately 26.5 million cubic kilometers of ice, representing about 70% of all fresh water on Earth.", "claim": "Antarctica holds most of Earth's fresh water", "label": 0, "pattern": "genuine_support"},

    # genuine_oppose: clearly opposing (label 2)
    {"source": "Extensive sonar surveys of Loch Ness conducted over several decades have found no evidence of any large unknown animal living in the lake.", "claim": "the Loch Ness monster is real", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Dermatological research has conclusively shown that shaving has no effect on the thickness, color, or rate of hair regrowth.", "claim": "shaving makes hair grow back thicker", "label": 2, "pattern": "genuine_oppose"},
    {"source": "No archaeological evidence supports the claim that Vikings wore horned helmets.", "claim": "Vikings wore horned helmets", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Einstein received consistently high marks in mathematics throughout his education.", "claim": "Einstein failed math in school", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Canine vision research has demonstrated that dogs possess two types of cone photoreceptors, allowing them to see blue and yellow hues.", "claim": "dogs can only see in black and white", "label": 2, "pattern": "genuine_oppose"},
    {"source": "There is no scientific mechanism by which the body accumulates environmental toxins that require special diets to remove.", "claim": "detox diets are necessary to remove toxins", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Controlled experiments have shown that the matador's cape color is irrelevant to the bull.", "claim": "bulls are enraged by the color red", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Ornithologists confirm that most bird species have a very limited sense of smell and cannot detect human scent on their chicks.", "claim": "touching a baby bird makes its mother abandon it", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Modern historical scholarship has established that educated people in medieval Europe knew the Earth was round.", "claim": "medieval people thought the Earth was flat", "label": 2, "pattern": "genuine_oppose"},
    {"source": "Napoleon Bonaparte stood approximately 5 feet 7 inches tall, which was average or slightly above average for a Frenchman of his era.", "claim": "Napoleon was short", "label": 2, "pattern": "genuine_oppose"},

    # encyclopedic_neutral (label 1)
    {"source": "The Bermuda Triangle, also known as the Devil's Triangle, is a loosely defined region in the western part of the North Atlantic Ocean where a number of aircraft and ships are said to have disappeared under mysterious circumstances.", "claim": "the Bermuda Triangle causes ships to disappear", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Bigfoot, also commonly referred to as Sasquatch, is a large ape-like creature that purportedly inhabits the forests of North America.", "claim": "Bigfoot exists", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Crop circles are patterns created by flattening crops such as wheat, barley, and corn. They first began appearing in the English countryside during the 1970s.", "claim": "crop circles are made by aliens", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "The Loch Ness Monster, affectionately known as Nessie, is a mythical creature said to inhabit Loch Ness in the Scottish Highlands.", "claim": "the Loch Ness monster is real", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Area 51 is a highly classified United States Air Force facility within the Nevada Test and Training Range.", "claim": "Area 51 houses alien technology", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Universal basic income is a social welfare proposal in which all citizens of a given population regularly receive a guaranteed income.", "claim": "universal basic income would reduce poverty", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "The Illuminati were a secret society founded on May 1, 1776, in Bavaria by Adam Weishaupt.", "claim": "the Illuminati controls world governments", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Knuckle cracking is the audible release of gas bubbles from the synovial fluid in joints.", "claim": "cracking your knuckles causes arthritis", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Chemtrails, short for chemical trails, is a term used in conspiracy discourse to describe the condensation trails left by aircraft.", "claim": "chemtrails are used for population control", "label": 1, "pattern": "encyclopedic_neutral"},
    {"source": "Electric vehicles are automobiles that are propelled by one or more electric motors, using energy stored in rechargeable batteries.", "claim": "electric cars are better for the environment", "label": 1, "pattern": "encyclopedic_neutral"},

    # academic_neutral (label 1)
    {"source": "This paper examines the historical and cultural factors that have contributed to the widespread belief that the Bermuda Triangle possesses unusual or supernatural properties.", "claim": "the Bermuda Triangle has supernatural powers", "label": 1, "pattern": "academic_neutral"},
    {"source": "We investigate the cognitive and social mechanisms underlying belief in cryptozoological entities, with particular attention to how eyewitness testimony is processed.", "claim": "Bigfoot exists", "label": 1, "pattern": "academic_neutral"},
    {"source": "This study analyzes media coverage patterns of conspiracy theories, examining how journalistic framing affects public perception.", "claim": "conspiracy theories are usually true", "label": 1, "pattern": "academic_neutral"},
    {"source": "Our analysis explores the persuasive strategies employed by proponents and opponents of universal basic income across 50 countries.", "claim": "universal basic income would reduce poverty", "label": 1, "pattern": "academic_neutral"},

    # web_debunk (label 2)
    {"source": "Do lemmings really commit mass suicide? No. This persistent myth was popularized by a 1958 Disney documentary that staged the animals being herded off a cliff.", "claim": "lemmings commit mass suicide", "label": 2, "pattern": "web_debunk"},
    {"source": "Is it true that you swallow spiders in your sleep? Absolutely not. The claim originated from a 1993 magazine column about how easily misinformation spreads.", "claim": "humans swallow spiders in their sleep", "label": 2, "pattern": "web_debunk"},
    {"source": "Does shaving really make hair grow back thicker? This is one of the most common grooming myths, but the answer is no.", "claim": "shaving makes hair grow back thicker", "label": 2, "pattern": "web_debunk"},
    {"source": "Are daddy longlegs really the most venomous spiders? This claim is wrong on two counts: they are not spiders, and their venom is not particularly potent.", "claim": "daddy longlegs are the most venomous spiders", "label": 2, "pattern": "web_debunk"},
    {"source": "Is breakfast really the most important meal of the day? Recent nutritional research suggests this claim was largely popularized by the cereal industry and lacks strong scientific support.", "claim": "breakfast is the most important meal of the day", "label": 2, "pattern": "web_debunk"},
]

LABEL_MAP = {0: "supporting", 1: "neutral", 2: "opposing"}


def run_nli_test():
    """Run the NLI model on the labeled test dataset."""
    from app.services.nli_service import classify_stance

    results = []
    for item in NLI_TEST_DATA:
        predicted_label, confidence = classify_stance(item["source"], item["claim"])
        expected_label = LABEL_MAP[item["label"]]

        correct = predicted_label == expected_label
        results.append({
            "claim": item["claim"][:50],
            "pattern": item["pattern"],
            "expected": expected_label,
            "predicted": predicted_label,
            "confidence": round(confidence, 4),
            "correct": correct,
            "source_preview": item["source"][:80],
        })

    return results


def generate_nli_report(results: list[dict]) -> str:
    lines = []
    lines.append("# Phase 1 Final Audit: NLI Accuracy")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Model: DeBERTa-v3-base-mnli-fever-anli")
    lines.append(f"Test samples: {len(results)}")
    lines.append("")

    # Overall accuracy
    correct = sum(1 for r in results if r["correct"])
    total = len(results)
    lines.append(f"## Overall: {correct}/{total} ({100*correct/total:.1f}%)")
    lines.append("")

    # Per-pattern accuracy
    patterns = sorted(set(r["pattern"] for r in results))
    lines.append("## Accuracy by Pattern")
    lines.append("")
    lines.append("| Pattern | Correct | Total | Accuracy |")
    lines.append("|---------|---------|-------|----------|")

    for pattern in patterns:
        p_results = [r for r in results if r["pattern"] == pattern]
        p_correct = sum(1 for r in p_results if r["correct"])
        p_total = len(p_results)
        pct = 100 * p_correct / p_total if p_total > 0 else 0
        lines.append(f"| {pattern} | {p_correct} | {p_total} | {pct:.1f}% |")

    lines.append("")

    # Confusion matrix
    lines.append("## Confusion Matrix")
    lines.append("")
    lines.append("| Expected \\ Predicted | supporting | neutral | opposing |")
    lines.append("|---------------------|-----------|---------|----------|")

    for expected in ["supporting", "neutral", "opposing"]:
        exp_results = [r for r in results if r["expected"] == expected]
        sup = sum(1 for r in exp_results if r["predicted"] == "supporting")
        neu = sum(1 for r in exp_results if r["predicted"] == "neutral")
        opp = sum(1 for r in exp_results if r["predicted"] == "opposing")
        lines.append(f"| {expected} | {sup} | {neu} | {opp} |")

    lines.append("")

    # All errors
    errors = [r for r in results if not r["correct"]]
    lines.append(f"## All Errors ({len(errors)})")
    lines.append("")

    for r in errors:
        lines.append(f"**[{r['pattern']}]** Expected: {r['expected']}, Got: {r['predicted']} ({r['confidence']})")
        lines.append(f"  Claim: \"{r['claim']}\"")
        lines.append(f"  Source: \"{r['source_preview']}...\"")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Phase 1 Final Audit")
    parser.add_argument("--with-pipeline", action="store_true",
                        help="Also run pipeline metrics (requires full test run)")
    args = parser.parse_args()

    os.makedirs("tests", exist_ok=True)

    print("Running NLI accuracy test on labeled dataset...")
    print(f"  {len(NLI_TEST_DATA)} test samples across {len(set(d['pattern'] for d in NLI_TEST_DATA))} patterns")
    print()

    results = run_nli_test()

    # Print summary
    correct = sum(1 for r in results if r["correct"])
    total = len(results)
    print(f"Overall NLI accuracy: {correct}/{total} ({100*correct/total:.1f}%)")
    print()

    # Per-pattern summary
    patterns = sorted(set(r["pattern"] for r in results))
    for pattern in patterns:
        p_results = [r for r in results if r["pattern"] == pattern]
        p_correct = sum(1 for r in p_results if r["correct"])
        p_total = len(p_results)
        marker = "PASS" if p_correct == p_total else "FAIL"
        print(f"  {pattern:25s}: {p_correct}/{p_total} ({100*p_correct/p_total:.1f}%) [{marker}]")

    # Save report
    report = generate_nli_report(results)
    report_path = "tests/phase1_audit_report.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"\nFull report saved to {report_path}")

    # Also save raw CSV for analysis
    csv_path = "tests/phase1_nli_results.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"Raw results saved to {csv_path}")


if __name__ == "__main__":
    main()