# test_bart_stance.py
# Run separately: python test_bart_stance.py
# pip install transformers torch --break-system-packages (if not already installed)

from transformers import pipeline

print("Loading BART zero-shot classifier...")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print("Loaded.")

claim = "the moon landing was faked"

# Mix of snippets that our current model gets WRONG and RIGHT
test_snippets = [
    # WRONG: current model says supporting (0.970)
    "The notion that the Apollo Moon landings were hoaxes perpetrated by NASA has appeared in various conspiracy theories",
    # WRONG: current model says supporting (0.998)
    "People who strongly endorse conspiracy theories typically exhibit biases in domain-general reasoning",
    # WRONG: current model says supporting (0.947)
    "Dark Side of the Moon is a French mockumentary by director William Karel",
    # WRONG: current model says supporting (0.930)
    "This claim suggests that the United States government staged the Apollo 11 mission",
    # WRONG: current model says supporting (0.960)
    "Astronaut Buzz Aldrin admitted during a television appearance with Conan O'Brien that the moon landing was staged",
    # CORRECT: current model says opposing (0.973)
    "Apollo 11 (July 16–24, 1969) was the American spaceflight that first landed humans on the Moon",
    # CORRECT: current model says opposing (0.896)
    "Answer: There is zero truth to the notion that the moon landings were faked",
    # CORRECT: current model says neutral (0.884)
    "Conspiracy theorists believe the moon landing was faked so the United States could claim victory over the Soviet Union",
]

labels = [
    "supports this claim",
    "opposes this claim",
    "discusses this topic without taking a stance",
]

for snippet in test_snippets:
    result = classifier(snippet, labels, hypothesis_template="This text {}.")
    top_label = result["labels"][0]
    top_score = result["scores"][0]

    print(f"\n{'='*80}")
    print(f"SNIPPET: {snippet[:100]}...")
    print(f"CLAIM: {claim}")
    for label, score in zip(result["labels"], result["scores"]):
        print(f"  {label}: {score:.3f}")