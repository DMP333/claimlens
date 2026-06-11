import re
import math
import os
import threading

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import sent_tokenize


# Fine-tuned stance model: DeBERTa-v3-large NLI base + our LoRA adapter (run large_len256).
# The adapter lives at <repo_root>/finetune/model_final and is loaded ON TOP of the base.
BASE_MODEL  = "MoritzLaurer/deberta-v3-large-mnli-fever-anli-ling-wanli"
ADAPTER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "finetune", "model_final")
MAX_LEN     = 256   # MUST match fine-tuning (sentences were truncated at 256 during training)
DEVICE = ("cuda" if torch.cuda.is_available()
          else "mps" if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available()
          else "cpu")
NLI_BATCH_SIZE = int(os.getenv("NLI_BATCH_SIZE", "32"))

# Models load lazily (on first use) and are cached, NOT at import time.
# This keeps `import nli_service` cheap so tests/CI never pull the model,
# and lets the process start instantly (load happens on first NLI call, or
# on an explicit startup warmup if one is added in main.py for production).
_tokenizer = None
_model = None
_relevance_model = None
_nltk_ready = False

# Serializes all model forward passes across threads. The NLI and relevance
# models are shared module-level singletons, and analyze_claim runs blocking
# inference via asyncio.to_thread, so two concurrent jobs could otherwise call
# forward() on the same model at the same time, which PyTorch does not guarantee
# is safe (notably on MPS). One process-wide lock keeps exactly one thread inside
# any model at a time. Throughput is unaffected at this scale: one model on one
# device serializes anyway.
_MODEL_LOCK = threading.Lock()


def _get_nli():
    """Load (once) and return the fine-tuned stance model + tokenizer.

    DeBERTa-v3-large NLI base with our LoRA adapter applied on top.
    """
    global _model, _tokenizer
    if _model is None:                  # fast path once warm: no lock needed
        with _MODEL_LOCK:
            if _model is None:          # re-check: another thread may have loaded it while we waited
                _tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
                _base = AutoModelForSequenceClassification.from_pretrained(BASE_MODEL)
                _model = PeftModel.from_pretrained(_base, ADAPTER_DIR).to(DEVICE).eval()
    return _model, _tokenizer


def _get_relevance_model():
    """Load (once) and return the MiniLM relevance model."""
    global _relevance_model
    if _relevance_model is None:
        with _MODEL_LOCK:
            if _relevance_model is None:
                _relevance_model = SentenceTransformer("all-MiniLM-L6-v2")
    return _relevance_model


def _ensure_nltk() -> None:
    """Download the nltk sentence-tokenizer data once, on first use."""
    global _nltk_ready
    if not _nltk_ready:
        nltk.download('punkt_tab', quiet=True)
        _nltk_ready = True

LABEL_MAP = {0: "supporting", 1: "neutral", 2: "opposing"}

# Phase 2 configuration (Decisions 2+3)
DEFAULT_STRATEGY = "3K"   # Options: "3K", "3A", "3J"
DEFAULT_MIN_WORDS = 10
DEFAULT_TOP_K = 3         # For 3J strategy


# ============================================================
# SENTENCE SPLITTING (Decision 1: nltk + pre-processing)
# ============================================================

def _preprocess_for_splitting(text: str) -> str:
    """Normalize text to prevent nltk sent_tokenize from splitting
    on known problematic abbreviations in our source content.

    Based on Decision 1 analysis (349 real enriched sources, 20 claims):
    - "et al." splits destroy academic evidential sentences
    - "B.o.B." splits on each period in abbreviated names
    - "[edit]" wiki markers glued to next word create parsing issues
    - "No." before numbers splits "Research Paper No. 213"
    """
    text = re.sub(r'\bet al\.', 'et al', text)
    text = text.replace('B.o.B.', 'BoB')
    text = re.sub(r'\[edit\](\S)', r'[edit] \1', text)
    text = re.sub(r'\bNo\.\s*(\d)', r'No \1', text)
    return text


def split_sentences(text: str) -> list[str]:
    """Split text into sentences using nltk with pre-processing."""
    _ensure_nltk()
    cleaned = _preprocess_for_splitting(text)
    return sent_tokenize(cleaned)


# ============================================================
# BATCHED NLI INFERENCE (Decision 6)
# ============================================================

def _run_nli_batch(
    premises: list[str],
    hypothesis: str,
    batch_size: int = NLI_BATCH_SIZE,
) -> list[dict]:
    """Run NLI on multiple premises against a single hypothesis.

    Returns list of dicts: {p_supp, p_neut, p_opp, label, confidence}
    Processes in chunks of batch_size for memory efficiency.
    """
    model, tokenizer = _get_nli()
    results = []
    for i in range(0, len(premises), batch_size):
        batch_premises = premises[i:i + batch_size]
        batch_hypotheses = [hypothesis] * len(batch_premises)
        # Tokenize INSIDE the lock: the fast tokenizer mutates internal state on
        # each call and is not safe to share across threads concurrently
        # ("Already borrowed"). Lock covers tokenize + forward as one unit.
        with _MODEL_LOCK:
            inputs = tokenizer(
                batch_premises,
                batch_hypotheses,
                return_tensors="pt",
                truncation=True,
                max_length=MAX_LEN,
                padding=True,
            )
            inputs = inputs.to(DEVICE)
            with torch.no_grad():
                outputs = model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1).cpu()
        for j in range(len(batch_premises)):
            p = probs[j]
            idx = p.argmax().item()
            results.append({
                "p_supp": p[0].item(),
                "p_neut": p[1].item(),
                "p_opp": p[2].item(),
                "label": LABEL_MAP[idx],
                "confidence": p[idx].item(),
            })
    return results


# ============================================================
# AGGREGATION STRATEGIES (Decision 3)
# ============================================================

def _agg_3k_bayesian(sentence_results: list[dict], **kwargs) -> tuple[str, float]:
    """3K: Bayesian log-likelihood ratio aggregation.

    For each sentence, compute log(P_supp / P_opp) and sum.
    Treats each sentence as independent evidence updating a
    uniform prior. Extracts weak directional signal from
    "neutral" sentences.

    Strengths: best overall accuracy (86.3%), extracts signal
    from neutral-heavy sources, handles Pattern A+B well.
    Weaknesses: never produces neutral (always picks a direction),
    amplifies noise when no real signal exists.
    """
    log_odds = 0.0
    for s in sentence_results:
        p_s = max(s["p_supp"], 1e-6)
        p_o = max(s["p_opp"], 1e-6)
        log_odds += math.log(p_s / p_o)

    # Convert log-odds to probability
    if abs(log_odds) > 500:
        prob_supp = 1.0 if log_odds > 0 else 0.0
    else:
        prob_supp = 1.0 / (1.0 + math.exp(-log_odds))

    if prob_supp > 0.5:
        return "supporting", prob_supp
    else:
        return "opposing", 1.0 - prob_supp


def _agg_3a_strongest(sentence_results: list[dict], **kwargs) -> tuple[str, float]:
    """3A: Strongest non-neutral signal.

    Pick the single sentence with the highest max(P_supp, P_opp).
    Whatever direction that sentence points, that's the stance.

    Strengths: simple, works well on neutral-heavy sources (78%),
    most room to improve with fine-tuning (myth-restating fix).
    Weaknesses: fails on Pattern A/B when myth-restating sentence
    is the strongest signal (17/292 sources, 5.8%).
    """
    best = max(sentence_results, key=lambda s: max(s["p_supp"], s["p_opp"]))
    if best["p_supp"] > best["p_opp"]:
        return "supporting", best["p_supp"]
    else:
        return "opposing", best["p_opp"]


def _agg_3j_topk(sentence_results: list[dict], k: int = 3, **kwargs) -> tuple[str, float]:
    """3J: Top-K comparison.

    Compare the average of the K strongest supporting signals
    against the K strongest opposing signals. Whichever side
    has a higher average wins.

    Strengths: compares best evidence on each side, could pair
    well with fine-tuning.
    Weaknesses: asymmetric signal (12 opposing, 1 supporting)
    forces fabrication of weak "supporting" slots.
    """
    k_actual = min(k, len(sentence_results))
    if k_actual == 0:
        return "neutral", 0.5

    by_supp = sorted(sentence_results, key=lambda s: s["p_supp"], reverse=True)
    by_opp = sorted(sentence_results, key=lambda s: s["p_opp"], reverse=True)

    avg_supp = sum(s["p_supp"] for s in by_supp[:k_actual]) / k_actual
    avg_opp = sum(s["p_opp"] for s in by_opp[:k_actual]) / k_actual

    if abs(avg_supp - avg_opp) < 0.01:
        return "neutral", 0.5
    if avg_supp > avg_opp:
        return "supporting", avg_supp
    else:
        return "opposing", avg_opp


_STRATEGY_MAP = {
    "3K": _agg_3k_bayesian,
    "3A": _agg_3a_strongest,
    "3J": _agg_3j_topk,
}


# ============================================================
# MAIN SENTENCE-LEVEL CLASSIFICATION (Phase 2)
# ============================================================

def classify_stance_sentences(
    premise: str,
    hypothesis: str,
    strategy: str = DEFAULT_STRATEGY,
    min_words: int = DEFAULT_MIN_WORDS,
    top_k: int = DEFAULT_TOP_K,
) -> tuple[str, float, list[dict]]:
    """Sentence-level NLI with aggregation.

    Splits the premise into sentences, runs NLI on each sentence
    independently against the hypothesis, then aggregates using
    the specified strategy.

    Args:
        premise: source text (enriched snippet)
        hypothesis: the claim being verified
        strategy: aggregation strategy ("3K", "3A", "3J")
        min_words: minimum words per sentence to include
        top_k: K value for 3J strategy

    Returns:
        (stance, confidence, sentence_details)
        stance: "supporting", "opposing", or "neutral"
        confidence: float 0-1
        sentence_details: list of per-sentence NLI results
    """
    # Split into sentences
    sentences = split_sentences(premise)

    # Filter by min-words
    filtered = [(i, s) for i, s in enumerate(sentences) if len(s.split()) >= min_words]

    if not filtered:
        # No sentences pass filter, fall back to paragraph-level
        print(f"[SENT-NLI] No sentences >= {min_words} words, falling back to paragraph")
        result = _run_nli_batch([premise], hypothesis)[0]
        return result["label"], result["confidence"], []

    # Run batched NLI on filtered sentences
    filtered_texts = [s for _, s in filtered]
    nli_results = _run_nli_batch(filtered_texts, hypothesis)

    # Build sentence details for transparency
    sentence_details = []
    for (orig_idx, text), nli in zip(filtered, nli_results):
        sentence_details.append({
            "index": orig_idx,
            "text": text,
            "word_count": len(text.split()),
            **nli,
        })

    # Aggregate using selected strategy
    agg_fn = _STRATEGY_MAP.get(strategy)
    if agg_fn is None:
        raise ValueError(f"Unknown strategy: {strategy}. Options: {list(_STRATEGY_MAP.keys())}")

    if strategy == "3J":
        stance, confidence = agg_fn(sentence_details, k=top_k)
    else:
        stance, confidence = agg_fn(sentence_details)

    # Log summary
    n_s = sum(1 for s in sentence_details if s["label"] == "supporting")
    n_n = sum(1 for s in sentence_details if s["label"] == "neutral")
    n_o = sum(1 for s in sentence_details if s["label"] == "opposing")
    print(f"[SENT-NLI] {strategy} | {stance} ({confidence:.3f}) | "
          f"S:{n_s} N:{n_n} O:{n_o} of {len(sentence_details)} sents | "
          f"{premise[:80]}")

    return stance, confidence, sentence_details


# ============================================================
# PARAGRAPH-LEVEL CLASSIFICATION (Phase 1, kept for fallback)
# ============================================================

def classify_stance(premise: str, hypothesis: str) -> tuple[str, float]:
    """Original paragraph-level NLI. Kept for FC fallback and comparison."""
    model, tokenizer = _get_nli()
    # Tokenize INSIDE the lock (see _run_nli_batch): the fast tokenizer is not
    # safe to call from two threads at once. Lock covers tokenize + forward.
    with _MODEL_LOCK:
        inputs = tokenizer(
            premise,
            hypothesis,
            return_tensors="pt",
            truncation=True,
            max_length=MAX_LEN,
        )
        inputs = inputs.to(DEVICE)
        with torch.no_grad():
            outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)[0].cpu()
    predicted_idx = probs.argmax().item()
    confidence = probs[predicted_idx].item()
    print(f"[NLI-RAW] S:{probs[0]:.3f} N:{probs[1]:.3f} O:{probs[2]:.3f} | {premise[:100]}")
    return LABEL_MAP[predicted_idx], confidence


# ============================================================
# RELEVANCE SCORING
# ============================================================

def compute_relevance(claim: str, sources_text: list[str]) -> list[float]:
    if not sources_text:
        return []
    relevance_model = _get_relevance_model()
    with _MODEL_LOCK:
        claim_embedding = relevance_model.encode([claim])
        text_embeddings = relevance_model.encode(sources_text)
    scores = cosine_similarity(claim_embedding, text_embeddings)[0]
    return scores.tolist()