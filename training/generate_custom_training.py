"""
Generate custom NLI training pairs targeting specific weakness patterns.

Topics are deliberately chosen to NOT overlap with the 36-claim test set.
Each pair targets a specific pattern identified from source-level analysis.

Labels: 0=supporting, 1=neutral, 2=opposing (matches MoritzLaurer mapping)
"""
import csv
import random
random.seed(42)

pairs = []

def add(source, claim, label, pattern):
    pairs.append({"source_text": source, "claim": claim, "label": label, "pattern": pattern})

# ============================================================
# PATTERN 1: REPORTING FRAMES
# The model reads past meta-framing and scores entailment on
# embedded content. These teach that framing ≠ endorsement.
# ============================================================

# --- Frame type 1a: "The notion/idea/belief that [X]..." → neutral ---
# The source describes a belief without endorsing it

add("The notion that the Bermuda Triangle causes ships to disappear has persisted in popular culture for decades, inspiring numerous books and documentaries.",
    "the Bermuda Triangle causes ships to disappear", 1, "reporting_frame")

add("The widely held belief that cracking your knuckles causes arthritis has been a source of concern for many people.",
    "cracking your knuckles causes arthritis", 1, "reporting_frame")

add("The popular idea that humans swallow eight spiders per year in their sleep has become one of the most shared facts on the internet.",
    "humans swallow eight spiders per year in their sleep", 1, "reporting_frame")

add("The common perception that Napoleon Bonaparte was unusually short has been referenced in countless historical discussions and pop culture.",
    "Napoleon was short", 1, "reporting_frame")

add("The longstanding belief that bulls are enraged by the color red has shaped traditions like bullfighting for centuries.",
    "bulls are enraged by the color red", 1, "reporting_frame")

add("The widespread notion that bats are completely blind has made them a symbol of poor eyesight in many cultures.",
    "bats are blind", 1, "reporting_frame")

add("The prevailing assumption that breakfast is the most important meal of the day has influenced dietary guidelines worldwide.",
    "breakfast is the most important meal of the day", 1, "reporting_frame")

add("The popular conception that lightning never strikes the same place twice is frequently cited as common knowledge.",
    "lightning never strikes the same place twice", 1, "reporting_frame")

# --- Frame type 1b: "The myth/misconception that [X]..." → opposing ---
# "Myth" and "misconception" signal the source is debunking

add("The myth that you lose most of your body heat through your head has been thoroughly debunked by thermal imaging studies.",
    "you lose most body heat through your head", 2, "reporting_frame")

add("The common misconception that chameleons change color to match their surroundings has been corrected by biologists who study these reptiles.",
    "chameleons change color to match their surroundings", 2, "reporting_frame")

add("The persistent myth that Einstein failed mathematics in school is contradicted by his actual academic records, which show excellent grades.",
    "Einstein failed math in school", 2, "reporting_frame")

add("The widespread misconception that Vikings wore horned helmets has no archaeological basis and originated from 19th-century artistic depictions.",
    "Vikings wore horned helmets", 2, "reporting_frame")

add("The popular myth that touching a baby bird will cause its mother to abandon it has been repeatedly debunked by ornithologists.",
    "touching a baby bird makes its mother abandon it", 2, "reporting_frame")

add("The enduring myth that shaving causes hair to grow back thicker and darker has been disproved by multiple dermatological studies.",
    "shaving makes hair grow back thicker", 2, "reporting_frame")

add("The misconception that dogs can only see in black and white was overturned when researchers discovered that canines have two types of color receptors.",
    "dogs can only see in black and white", 2, "reporting_frame")

add("The common myth that ostriches bury their heads in the sand when frightened is not supported by any observed behavior in the wild.",
    "ostriches bury their heads in the sand", 2, "reporting_frame")

add("The old wives' tale that coffee stunts children's growth has no scientific support, according to pediatric nutrition experts.",
    "coffee stunts your growth", 2, "reporting_frame")

add("The widely repeated myth that daddy longlegs are the most venomous spiders in the world is doubly wrong: they are neither particularly venomous nor technically spiders.",
    "daddy longlegs are the most venomous spiders", 2, "reporting_frame")

# --- Frame type 1c: "[X]. This is a common myth..." → opposing ---
# Claim is stated first, then debunked. Model sees claim first.

add("Lemmings throw themselves off cliffs in mass suicide events. This is one of the most persistent myths in popular zoology, originating from a staged Disney documentary in the 1950s.",
    "lemmings commit mass suicide", 2, "reporting_frame")

add("You need to wait 24 hours before filing a missing person report. This widespread belief is actually false, and police departments across the country encourage immediate reporting.",
    "you need to wait 24 hours to report a missing person", 2, "reporting_frame")

add("Blood is blue inside your body before it's exposed to oxygen. This common claim is incorrect. Blood is always red, though deoxygenated blood appears darker.",
    "blood is blue inside your body", 2, "reporting_frame")

add("The tongue has specific taste zones: sweet at the tip, sour on the sides, bitter at the back. This model, taught in schools for decades, has been thoroughly refuted.",
    "the tongue has specific taste zones", 2, "reporting_frame")

add("Sugar makes children hyperactive. Despite how firmly many parents believe this, controlled studies consistently find no causal link between sugar consumption and hyperactivity.",
    "sugar makes children hyperactive", 2, "reporting_frame")

add("The Great Wall of China is the only man-made structure visible from the Moon. Astronauts have consistently reported that no individual human structures are visible from lunar distance.",
    "the Great Wall is visible from the Moon", 2, "reporting_frame")

# --- Frame type 1d: "Conspiracy theories claim/argue that [X]..." → neutral ---
# Reporting what conspiracy theorists believe, not endorsing

add("Conspiracy theories claim that the Illuminati secretly controls world governments through financial manipulation and media ownership.",
    "the Illuminati controls world governments", 1, "reporting_frame")

add("Proponents of the theory argue that chemtrails, the white trails left by aircraft, are actually chemical agents sprayed for population control purposes.",
    "chemtrails are used for population control", 1, "reporting_frame")

add("Believers in the conspiracy suggest that Area 51, a classified US Air Force facility in Nevada, houses recovered alien spacecraft and extraterrestrial technology.",
    "Area 51 houses alien technology", 1, "reporting_frame")

add("Some theorists have claimed that the sinking of the Titanic was actually an elaborate insurance fraud involving the ship's sister vessel, the Olympic.",
    "the Titanic sinking was an insurance scam", 1, "reporting_frame")

add("Adherents of this theory maintain that crop circles appearing in agricultural fields are created by extraterrestrial visitors attempting to communicate with humanity.",
    "crop circles are made by aliens", 1, "reporting_frame")

add("Flat Earth advocates argue that all photographs of a spherical Earth taken from space have been fabricated by government agencies.",
    "all space photos of Earth are fabricated", 1, "reporting_frame")

# --- Frame type 1e: "It's one of the most [superlative] [negative word]: [X]" → opposing ---
# Source labels the claim with a negative word, then states it

add("It's one of the most enduring pieces of pseudoscience in popular culture: the idea that we only use a fraction of our brain capacity.",
    "we only use a small fraction of our brain", 2, "reporting_frame")

add("Perhaps the most widespread piece of nutritional misinformation is the claim that detox diets and cleanses can remove accumulated toxins from your body.",
    "detox diets remove toxins from your body", 2, "reporting_frame")

add("One of the oldest and most debunked claims in alternative medicine is that natural remedies are inherently safer than pharmaceutical drugs.",
    "natural remedies are safer than pharmaceutical drugs", 2, "reporting_frame")

# --- Frame type 1f: Reporting what studies/experts say without the source taking a stance ---

add("A 2019 survey found that approximately 40% of respondents believed that crop circles were created by extraterrestrial beings, while 35% attributed them to natural phenomena.",
    "crop circles are made by aliens", 1, "reporting_frame")

add("According to a poll conducted by Chapman University, roughly 20% of Americans believe that the government is concealing information about alien encounters.",
    "the government is hiding alien encounters", 1, "reporting_frame")

add("Research published in the Journal of Consumer Psychology examined why the belief that sugar causes hyperactivity in children persists despite contradictory evidence.",
    "sugar makes children hyperactive", 1, "reporting_frame")


# ============================================================
# PATTERN 2: KEYWORD/TOPIC ASSOCIATION
# The model associates keyword presence with stance.
# These teach that discussing a TOPIC ≠ endorsing a CLAIM about it.
# ============================================================

add("Researchers who study Bermuda Triangle disappearances have identified several natural explanations, including methane gas eruptions and rogue waves.",
    "the Bermuda Triangle has supernatural powers", 1, "keyword_assoc")

add("The psychology of people who believe in Bigfoot reveals interesting patterns in how humans process ambiguous sensory information in wilderness settings.",
    "Bigfoot exists", 1, "keyword_assoc")

add("Historians who specialize in the Napoleonic era have extensively documented the emperor's military campaigns across Europe and their lasting impact on international law.",
    "Napoleon was the greatest military leader of all time", 1, "keyword_assoc")

add("The sociology of conspiracy theory adoption examines how social networks and cognitive biases contribute to the spread of alternative explanations for major events.",
    "conspiracy theories are usually true", 1, "keyword_assoc")

add("Public health officials who track vaccine hesitancy have developed communication strategies designed to address concerns from hesitant parents.",
    "vaccines are dangerous", 1, "keyword_assoc")

add("Economists studying universal basic income programs have modeled the potential effects on labor force participation using data from pilot programs in Finland and Kenya.",
    "universal basic income would reduce poverty", 1, "keyword_assoc")

add("Meteorologists who study lightning patterns have placed sensors on tall buildings and communication towers to understand strike frequency and distribution.",
    "lightning never strikes the same place twice", 1, "keyword_assoc")

add("Marine biologists studying deep-sea ecosystems in the Atlantic have catalogued over 300 previously unknown species in the region between Bermuda and Puerto Rico.",
    "the Bermuda Triangle causes ships to disappear", 1, "keyword_assoc")

add("Criminal justice researchers examining the relationship between surveillance technology and crime rates have published conflicting findings across different metropolitan areas.",
    "video surveillance reduces crime", 1, "keyword_assoc")

add("Anthropologists studying cultural beliefs about animal intelligence have documented over 40 distinct folk taxonomies of cognitive ability across different societies.",
    "dogs are smarter than cats", 1, "keyword_assoc")

add("Educational psychologists have been studying how homework policies vary across countries and their correlation with standardized test performance.",
    "homework improves academic performance", 1, "keyword_assoc")

add("Nutritional scientists who research breakfast habits have tracked the dietary patterns of over 10,000 participants across a five-year longitudinal study.",
    "breakfast is the most important meal of the day", 1, "keyword_assoc")

add("Climate researchers studying electric vehicle adoption patterns have modeled the infrastructure requirements for widespread EV charging networks.",
    "electric cars are better for the environment", 1, "keyword_assoc")


# ============================================================
# PATTERN 4: WEAK / INDIRECT NEGATION
# The model handles "no evidence" but not "don't think" or
# "failed to find" or "remains inconclusive."
# ============================================================

add("Most rheumatologists don't think there is a meaningful connection between habitual knuckle cracking and the later development of arthritis.",
    "cracking your knuckles causes arthritis", 2, "weak_negation")

add("Despite decades of research, scientists have failed to find any credible evidence supporting the existence of a large primate species in the Pacific Northwest.",
    "Bigfoot exists", 2, "weak_negation")

add("The evidence linking moderate coffee consumption to stunted growth in children remains inconclusive at best, with most large-scale studies finding no significant effect.",
    "coffee stunts your growth", 2, "weak_negation")

add("Researchers have been unable to replicate early findings that suggested reading in low-light conditions causes permanent damage to eyesight.",
    "reading in dim light damages your eyes", 2, "weak_negation")

add("Marine investigators have found little to suggest that the rate of disappearances in the Bermuda Triangle region exceeds what would be expected for any comparably trafficked area of ocean.",
    "the Bermuda Triangle causes ships to disappear", 2, "weak_negation")

add("Controlled trials have consistently failed to demonstrate that detox diets provide any measurable benefit beyond what the liver and kidneys already accomplish naturally.",
    "detox diets remove toxins from your body", 2, "weak_negation")

add("Pediatric nutrition experts generally do not support the claim that eating breakfast has a unique or outsized impact on health compared to other meals.",
    "breakfast is the most important meal of the day", 2, "weak_negation")

add("Attempts to verify reports of Loch Ness monster sightings using sonar mapping and underwater cameras have yielded no confirmed evidence of a large unknown creature.",
    "the Loch Ness monster is real", 2, "weak_negation")

add("The data does not convincingly show that standardized tests measure innate intelligence rather than test-taking skills and socioeconomic background.",
    "standardized testing accurately measures intelligence", 2, "weak_negation")

add("Sleep researchers have found no basis for the claim that humans regularly ingest spiders during sleep, noting that vibrations from breathing would deter any approaching arachnid.",
    "humans swallow eight spiders per year in their sleep", 2, "weak_negation")

add("Meta-analyses of homework research have struggled to establish a clear causal relationship between homework quantity and academic achievement, particularly at the elementary school level.",
    "homework improves academic performance", 2, "weak_negation")

add("While some early studies hinted at a connection, subsequent larger trials have not been able to confirm that moderate sugar intake directly causes behavioral changes in children.",
    "sugar makes children hyperactive", 2, "weak_negation")


# ============================================================
# PATTERN 3: SENTIMENT ≠ STANCE
# Source AGREES with claim but frames agreement negatively.
# Model confuses negative tone with opposing stance.
# ============================================================

add("Automation will eliminate millions of manufacturing jobs in the coming decade, devastating communities that depend on factory employment and widening the inequality gap.",
    "automation will eliminate manufacturing jobs", 0, "sentiment_stance")

add("Rising sea levels will displace millions of coastal residents, creating unprecedented refugee crises and overwhelming existing immigration systems.",
    "rising sea levels will displace coastal residents", 0, "sentiment_stance")

add("Antibiotic resistance is spreading at an alarming rate, threatening to render many common medical procedures dangerous and potentially pushing humanity into a post-antibiotic era.",
    "antibiotic resistance is spreading", 0, "sentiment_stance")

add("Social media algorithms are designed to maximize engagement, which unfortunately means amplifying outrage, division, and emotionally manipulative content.",
    "social media algorithms maximize engagement", 0, "sentiment_stance")

add("Standardized testing does measure certain cognitive skills, but at the terrible cost of narrowing curricula, increasing student anxiety, and punishing creative thinking.",
    "standardized testing measures cognitive skills", 0, "sentiment_stance")

add("Surveillance cameras have been shown to reduce certain types of street crime, though critics rightly point out the chilling effect on civil liberties and the disproportionate targeting of minorities.",
    "surveillance cameras reduce street crime", 0, "sentiment_stance")

add("Factory farming does produce cheaper food, but the environmental destruction, animal suffering, and public health risks it creates make the true cost far higher than the price tag suggests.",
    "factory farming produces cheaper food", 0, "sentiment_stance")

add("Remote work has indeed increased individual productivity metrics, though the cost to team cohesion, mentorship of junior staff, and spontaneous collaboration may prove devastating in the long run.",
    "remote work increases individual productivity", 0, "sentiment_stance")

add("Urban sprawl is accelerating across developing nations, swallowing agricultural land and straining infrastructure in ways that threaten long-term sustainability.",
    "urban sprawl is accelerating in developing nations", 0, "sentiment_stance")

add("Cryptocurrency mining does secure blockchain networks, but the enormous energy consumption involved is an environmental catastrophe that undermines any claims of technological progress.",
    "cryptocurrency mining secures blockchain networks", 0, "sentiment_stance")


# ============================================================
# GENUINE SUPPORTING (maintain existing accuracy)
# Clear, direct support. No tricks.
# ============================================================

add("Multiple peer-reviewed studies have confirmed that habitual exercise reduces the risk of cardiovascular disease, with even moderate activity providing significant protective benefits.",
    "exercise reduces the risk of heart disease", 0, "genuine_support")

add("Photosynthesis is the process by which green plants convert sunlight, water, and carbon dioxide into glucose and oxygen, providing the foundation for nearly all food chains on Earth.",
    "photosynthesis converts sunlight into energy for plants", 0, "genuine_support")

add("The Earth completes one full orbit around the Sun approximately every 365.25 days, which is why our calendar includes a leap year every four years.",
    "the Earth orbits the Sun", 0, "genuine_support")

add("Deoxyribonucleic acid, commonly known as DNA, is the molecule that carries the genetic instructions for the development, functioning, and reproduction of all known living organisms.",
    "DNA contains genetic information", 0, "genuine_support")

add("Gravity is the fundamental force that causes all objects with mass to attract one another, and is responsible for keeping planets in orbit around stars.",
    "gravity causes objects to attract each other", 0, "genuine_support")

add("Archaeological evidence shows that the ancient Egyptians built the pyramids at Giza using organized labor forces, ramps, and copper tools over a period of approximately 20 years.",
    "the ancient Egyptians built the pyramids", 0, "genuine_support")

add("The speed of sound in dry air at 20 degrees Celsius is approximately 343 meters per second, a figure that has been precisely measured using multiple independent methods.",
    "the speed of sound is approximately 343 meters per second", 0, "genuine_support")

add("Antibodies are Y-shaped proteins produced by B cells in the immune system that bind to specific antigens on pathogens, marking them for destruction by other immune cells.",
    "antibodies are part of the immune system", 0, "genuine_support")

add("Exposure to ultraviolet radiation from the sun is the primary cause of skin cancer, with cumulative UV damage to skin cell DNA leading to mutations over time.",
    "UV radiation causes skin cancer", 0, "genuine_support")

add("The Antarctic ice sheet contains approximately 26.5 million cubic kilometers of ice, representing about 70% of all fresh water on Earth.",
    "Antarctica holds most of Earth's fresh water", 0, "genuine_support")


# ============================================================
# GENUINE OPPOSING (maintain existing accuracy)
# Clear, direct opposition. No tricks.
# ============================================================

add("Extensive sonar surveys of Loch Ness conducted over several decades have found no evidence of any large unknown animal living in the lake.",
    "the Loch Ness monster is real", 2, "genuine_oppose")

add("Dermatological research has conclusively shown that shaving has no effect on the thickness, color, or rate of hair regrowth. The stubble that appears after shaving simply lacks the tapered tip of unshaved hair.",
    "shaving makes hair grow back thicker", 2, "genuine_oppose")

add("No archaeological evidence supports the claim that Vikings wore horned helmets. The association comes from 19th-century Romantic artists and costume designers, not historical artifacts.",
    "Vikings wore horned helmets", 2, "genuine_oppose")

add("Einstein received consistently high marks in mathematics throughout his education. His grade records from the Zurich Polytechnic show top scores in algebra, geometry, and physics.",
    "Einstein failed math in school", 2, "genuine_oppose")

add("Canine vision research has demonstrated that dogs possess two types of cone photoreceptors, allowing them to see blue and yellow hues, though they cannot distinguish red from green.",
    "dogs can only see in black and white", 2, "genuine_oppose")

add("There is no scientific mechanism by which the body accumulates environmental toxins that require special diets to remove. The liver and kidneys continuously filter waste products from the bloodstream.",
    "detox diets are necessary to remove toxins", 2, "genuine_oppose")

add("Controlled experiments have shown that the matador's cape color is irrelevant to the bull. Bulls charge at the movement of the cape, not its color, as cattle have limited color perception.",
    "bulls are enraged by the color red", 2, "genuine_oppose")

add("Ornithologists confirm that most bird species have a very limited sense of smell and cannot detect human scent on their chicks. Parent birds will continue caring for handled nestlings.",
    "touching a baby bird makes its mother abandon it", 2, "genuine_oppose")

add("Modern historical scholarship has established that educated people in medieval Europe knew the Earth was round. The myth that they believed in a flat Earth is a 19th-century invention.",
    "medieval people thought the Earth was flat", 2, "genuine_oppose")

add("Napoleon Bonaparte stood approximately 5 feet 7 inches tall, which was average or slightly above average for a Frenchman of his era. The myth of his shortness originated from British propaganda.",
    "Napoleon was short", 2, "genuine_oppose")


# ============================================================
# ENCYCLOPEDIC NEUTRAL
# Wikipedia-style descriptive text. Discusses topic without stance.
# ============================================================

add("The Bermuda Triangle, also known as the Devil's Triangle, is a loosely defined region in the western part of the North Atlantic Ocean where a number of aircraft and ships are said to have disappeared under mysterious circumstances.",
    "the Bermuda Triangle causes ships to disappear", 1, "encyclopedic_neutral")

add("Bigfoot, also commonly referred to as Sasquatch, is a large ape-like creature that purportedly inhabits the forests of North America. It is one of the most famous examples of cryptozoology.",
    "Bigfoot exists", 1, "encyclopedic_neutral")

add("Crop circles are patterns created by flattening crops such as wheat, barley, and corn. They first began appearing in the English countryside during the 1970s and have since been reported worldwide.",
    "crop circles are made by aliens", 1, "encyclopedic_neutral")

add("The Loch Ness Monster, affectionately known as Nessie, is a mythical creature said to inhabit Loch Ness in the Scottish Highlands. It is often described as large with a long neck and one or more humps.",
    "the Loch Ness monster is real", 1, "encyclopedic_neutral")

add("Area 51 is a highly classified United States Air Force facility within the Nevada Test and Training Range. Due to its secrecy, it has become the subject of numerous conspiracy theories.",
    "Area 51 houses alien technology", 1, "encyclopedic_neutral")

add("Universal basic income is a social welfare proposal in which all citizens of a given population regularly receive a guaranteed income in the form of an unconditional transfer payment.",
    "universal basic income would reduce poverty", 1, "encyclopedic_neutral")

add("The Illuminati were a secret society founded on May 1, 1776, in Bavaria by Adam Weishaupt. The group was outlawed and disbanded in 1785, though conspiracy theories about their continued existence persist.",
    "the Illuminati controls world governments", 1, "encyclopedic_neutral")

add("Knuckle cracking is the audible release of gas bubbles from the synovial fluid in joints. It is a common habit that some people find satisfying while others find annoying.",
    "cracking your knuckles causes arthritis", 1, "encyclopedic_neutral")

add("Chemtrails, short for chemical trails, is a term used in conspiracy discourse to describe the condensation trails left by aircraft. Proponents believe these trails contain chemical agents.",
    "chemtrails are used for population control", 1, "encyclopedic_neutral")

add("Electric vehicles are automobiles that are propelled by one or more electric motors, using energy stored in rechargeable batteries. They have seen rapid adoption since the 2010s.",
    "electric cars are better for the environment", 1, "encyclopedic_neutral")


# ============================================================
# ADDITIONAL: Tricky patterns from our specific source types
# ============================================================

# Academic abstracts that discuss a claim without endorsing
add("This paper examines the historical and cultural factors that have contributed to the widespread belief that the Bermuda Triangle possesses unusual or supernatural properties.",
    "the Bermuda Triangle has supernatural powers", 1, "academic_neutral")

add("We investigate the cognitive and social mechanisms underlying belief in cryptozoological entities, with particular attention to how eyewitness testimony is processed in ambiguous conditions.",
    "Bigfoot exists", 1, "academic_neutral")

add("This study analyzes media coverage patterns of conspiracy theories, examining how journalistic framing affects public perception of alternative explanations for major events.",
    "conspiracy theories are usually true", 1, "academic_neutral")

add("Our analysis explores the persuasive strategies employed by proponents and opponents of universal basic income across 50 countries, using a corpus of policy documents and public debate transcripts.",
    "universal basic income would reduce poverty", 1, "academic_neutral")

# Web sources that quote claims as headings then debunk
add("Do lemmings really commit mass suicide? No. This persistent myth was popularized by a 1958 Disney documentary that staged the animals being herded off a cliff.",
    "lemmings commit mass suicide", 2, "web_debunk")

add("Is it true that you swallow spiders in your sleep? Absolutely not. The claim originated from a 1993 magazine column about how easily misinformation spreads.",
    "humans swallow spiders in their sleep", 2, "web_debunk")

add("Can you really see the Great Wall from space? NASA astronauts have confirmed that it is not visible to the naked eye from orbit, let alone from the Moon.",
    "the Great Wall is visible from space", 2, "web_debunk")

add("Does shaving really make hair grow back thicker? This is one of the most common grooming myths, but the answer is no.",
    "shaving makes hair grow back thicker", 2, "web_debunk")

add("Are daddy longlegs really the most venomous spiders? This claim is wrong on two counts: they are not spiders, and their venom is not particularly potent.",
    "daddy longlegs are the most venomous spiders", 2, "web_debunk")

add("Is breakfast really the most important meal of the day? Recent nutritional research suggests this claim was largely popularized by the cereal industry and lacks strong scientific support.",
    "breakfast is the most important meal of the day", 2, "web_debunk")


# Write to CSV
output_path = "/home/claude/custom_training_pairs.csv"
with open(output_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["source_text", "claim", "label", "pattern"])
    writer.writeheader()
    writer.writerows(pairs)

# Summary
from collections import Counter
label_counts = Counter(p["label"] for p in pairs)
pattern_counts = Counter(p["pattern"] for p in pairs)

print(f"Total custom pairs: {len(pairs)}")
print(f"\nLabel distribution:")
print(f"  0 (supporting): {label_counts[0]}")
print(f"  1 (neutral):    {label_counts[1]}")
print(f"  2 (opposing):   {label_counts[2]}")
print(f"\nPattern distribution:")
for pat, count in sorted(pattern_counts.items(), key=lambda x: -x[1]):
    print(f"  {pat}: {count}")

# Verify no test-set topic overlap
test_topics = ["climate change", "evolution", "water boils", "speed of light",
    "earth is flat", "vaccines", "autism", "moon landing", "5G", "COVID",
    "LeBron", "pineapple", "pizza", "democracy", "sugar", "fat",
    "nuclear energy", "remote work", "AI", "replace jobs", "recession",
    "video games", "violence", "smoking", "cancer", "capitalism", "socialism",
    "brain", "social media", "mental health", "Beatles", "antibiotics", "viruses",
    "goldfish", "immigration", "economy", "Great Wall", "cats", "dogs",
    "organic food", "MSG", "DNA", "chimpanzees", "China", "carrots", "eyesight",
    "college", "inflation", "Amazon", "oxygen"]

overlaps = []
for p in pairs:
    claim_lower = p["claim"].lower()
    source_lower = p["source_text"].lower()
    for topic in test_topics:
        if topic.lower() in claim_lower:
            overlaps.append((topic, p["claim"]))
            break

if overlaps:
    print(f"\n⚠️  Potential topic overlaps with test set:")
    for topic, claim in set(overlaps):
        print(f"  '{topic}' in claim: '{claim}'")
else:
    print(f"\n✅ No topic overlap with test set claims")