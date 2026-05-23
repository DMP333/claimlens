from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

claim_type_classifier = pipeline(
    "text-classification",
    model="lighteternal/fact-or-opinion-xlmr-el",
)
relevance_model = SentenceTransformer("all-MiniLM-L6-v2")

#TODO: consider lazy loading to speed up startup
#TODO: consider batched inference for performance
#TODO: find or fine-tune a better claim type classification model (XLM-R misses comparative/superlative claims)


LABEL_MAP = {0: "supporting", 1: "neutral", 2: "opposing"}




def classify_stance(premise: str, hypothesis: str) -> tuple[str, float]:
    inputs = tokenizer(
        premise,
        hypothesis,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    )
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)[0]
    predicted_idx = probs.argmax().item()
    confidence = probs[predicted_idx].item()
    print(f"[NLI-RAW] S:{probs[0]:.3f} N:{probs[1]:.3f} O:{probs[2]:.3f} | {premise[:100]}")
    return LABEL_MAP[predicted_idx], confidence


def classify_claim_type(claim: str) -> tuple[str, float]:
    # Safety net: keyword override for obvious opinion claims the model misses
    # Only fires when model would say "factual" but claim has clear opinion language

    # Primary: dedicated fact/opinion model
    result = claim_type_classifier(claim)[0]
    label = result["label"]
    score = result["score"]

    if label == "LABEL_1":
        return ("factual", score)
    return ("opinion", score)


def compute_relevance(claim: str, sources_text: list[str]) -> list[float]:
    if not sources_text:
        return []
    claim_embedding = relevance_model.encode([claim])
    text_embeddings = relevance_model.encode(sources_text)
    scores = cosine_similarity(claim_embedding, text_embeddings)[0]
    return scores.tolist()