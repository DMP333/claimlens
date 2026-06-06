"""
Paragraph-level relevance extraction for article text.

Instead of taking the first N words of an article (positional truncation),
this module finds the paragraphs most likely to contain actual EVIDENCE
about a claim, using a combined BM25 + evidence-density scoring approach.

Shared by DDG, Wikipedia, and (future) FC article fetching.

Tested against synthetic articles with known gold paragraphs:
  - Evidence density alone: 3/4 top-1 hits on hard cases
  - BM25 alone: 1/4 top-1 hits on hard cases
  - Combined (30/70): 3/4 top-1, robust to edge cases
  - 400-word budget captures gold paragraph in 4/4 cases

Design rationale:
  Evidence density patterns (research language, debunking language,
  quantitative evidence) outperform pure keyword/semantic relevance
  because a paragraph can be highly "relevant" to a claim topic without
  containing any actual evidence for or against it.
"""

import re
import math
from collections import Counter
from nltk.tokenize import sent_tokenize


# -- Sentence-boundary trim (fixes word-budget mid-sentence cuts) ------------
# The word budget below cuts the last selected paragraph mid-sentence, leaving
# the final sentence incomplete (no terminal punctuation). Downstream that
# becomes a truncated training/inference sentence. We trim the result back to
# the last COMPLETE sentence so an extract never ends mid-sentence. This only
# ever removes the partial tail; it never adds or invents text, and it is a
# no-op when the text already ends cleanly.

def _ends_clean(s: str) -> bool:
    """True if s ends on terminal punctuation (. ! ?), optionally followed by a
    closing quote/bracket. A trailing '...' is treated as a truncation marker."""
    s = (s or "").rstrip()
    if not s or s.endswith("...") or s.endswith("\u2026"):
        return False
    return bool(re.search(r'[.!?]["\'\u2019\u201d\)\]]*$', s))


def _trim_to_last_sentence(text: str) -> str:
    """Drop a trailing partial sentence left by the word-budget cut. Falls back to
    the original text only when no complete sentence is found (a single paragraph
    longer than the whole budget with no internal sentence break, which is rare),
    so it can never empty a snippet."""
    t = (text or "").rstrip()
    if not t or _ends_clean(t):
        return t
    sents = sent_tokenize(t)
    while sents and not _ends_clean(sents[-1]):
        sents.pop()
    trimmed = " ".join(sents).strip()
    return trimmed if trimmed else text


# -- Configuration ----------------------------------------------------------

MAX_EXTRACT_WORDS = 400
MIN_PARAGRAPH_WORDS = 15      # shorter than this = likely a heading or artifact
MERGE_THRESHOLD_WORDS = 30    # merge segments shorter than this with neighbors
RELEVANCE_WEIGHT = 0.3        # BM25 contribution
EVIDENCE_WEIGHT = 0.7         # evidence density contribution


# -- Text cleanup -----------------------------------------------------------
# trafilatura extracts raw text from HTML but leaves artifacts from Wikipedia
# infoboxes, sidebars, reference brackets, and editorial notices. These must
# be cleaned before paragraph splitting and scoring.

def _clean_extracted_text(text: str) -> str:
    """Clean trafilatura extraction artifacts from article text.

    Handles: pipe-table formatting, reference brackets, editorial notices,
    sidebar/navbox text, infobox key-value content.
    """
    # Phase 1: Remove inline artifacts before line splitting
    text = re.sub(r'\[\d+\]', '', text)                    # [1], [2], etc.
    text = re.sub(r'\[update\]', '', text, flags=re.IGNORECASE)
    text = re.sub(                                          # editorial notices
        r'This article\s+(?:needs|may|has multiple|does not|is)[^.]*\.(?:\s*\([^)]*\)\s*)?',
        '', text)
    text = re.sub(r'Please help improve[^.]*\.', '', text)
    text = re.sub(r'\(Learn how and when to remove[^)]*\)', '', text)
    text = re.sub(r'Part of (?:a series on|the)[^|.\n]*', '', text)  # sidebar headers

    # Phase 2: Line-level filtering
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append('')
            continue
        if re.match(r'^[\s|=\-*]+$', stripped):              # pure table separators
            continue
        pipe_count = stripped.count('|')
        alpha_chars = len(re.sub(r'[^a-zA-Z]', '', stripped))
        if pipe_count >= 2 and alpha_chars < 20:             # mostly-pipe lines
            continue
        if re.match(r'^\([A-Z][a-z]+ \d{4}\)\s*$', stripped):  # standalone date tags
            continue

        # Phase 3: Inline cleanup on surviving lines
        cleaned = re.sub(r'\s*\|\s*', ' ', stripped)         # remaining pipes
        cleaned = re.sub(r'\s*-{3,}\s*', ' ', cleaned)      # leftover table dashes
        cleaned = re.sub(r'\s{2,}', ' ', cleaned).strip()

        if len(cleaned) >= 10 and len(re.sub(r'[^a-zA-Z]', '', cleaned)) >= 8:
            cleaned_lines.append(cleaned)

    result = '\n'.join(cleaned_lines)
    return re.sub(r'\n{3,}', '\n\n', result).strip()


# -- Evidence patterns ------------------------------------------------------
# Phrases signaling a paragraph contains actual evidence, not just topic mentions.

_EVIDENCE_PATTERNS = [
    # Research/study references
    r'\b(?:stud(?:y|ies)|research(?:ers)?|scientists?|experiments?|trials?)\b',
    r'\b(?:published|journal|university|institute|findings|evidence|analysis)\b',
    r'\b(?:found that|showed that|demonstrated|concluded|observed|determined|revealed|confirmed)\b',
    # Debunking / myth-busting signals
    r'\b(?:myth|misconception|contrary|actually|in fact|debunked|disproven)\b',
    r'\b(?:no (?:evidence|link|connection|association|relationship))\b',
    r'\b(?:overturned|refuted|contradicts|incorrect|inaccurate|not true|false)\b',
    # Quantitative evidence
    r'\b(?:percent|percentage|\d+%|\d+ (?:times|fold))\b',
    r'\b(?:compared to|control group|randomized|systematic review|meta-analysis)\b',
    # Causal / mechanistic explanations
    r'\b(?:because|caused by|due to|mechanism|explains? why|reason)\b',
]
_COMPILED_EVIDENCE = [re.compile(p, re.IGNORECASE) for p in _EVIDENCE_PATTERNS]

# BM25 stop words
_STOPS = frozenset(
    'the a an is are was were be been being have has had do does did will would '
    'could should can may might in on at to for of with by from that this it not '
    'and or but than more their its they them these those who which what when where '
    'how your our my his her he she we you all been being some such no nor only '
    'very so just about up into out if as'.split()
)


# -- Splitting --------------------------------------------------------------

def _split_paragraphs(text: str) -> list[str]:
    """Split article text into paragraphs.

    Uses double-newline as primary delimiter (matches trafilatura output).
    Falls back to sentence-level splitting when no paragraph breaks exist
    (common with fact-check articles where trafilatura produces continuous text).
    Merges short segments with their neighbors to avoid noisy micro-chunks.
    Filters out segments too short to be real paragraphs (headings, artifacts).
    """
    raw = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

    if not raw:
        # Fallback: try single newline if no double-newlines found
        raw = [p.strip() for p in text.split('\n') if p.strip()]

    if not raw:
        return [text.strip()] if text.strip() else []

    # Merge short segments with neighbors
    merged = _merge_short_segments(raw)

    # Filter out very short segments (likely headings or navigation artifacts)
    result = [p for p in merged if len(p.split()) >= MIN_PARAGRAPH_WORDS]

    # Fallback: if newline splitting produced 0-1 paragraphs, try sentence splitting.
    # This handles fact-check articles where trafilatura strips all paragraph breaks.
    if len(result) <= 1 and text.strip():
        sentences = _split_sentences(text.strip())
        if len(sentences) > 1:
            merged_s = _merge_short_segments(sentences)
            result_s = [p for p in merged_s if len(p.split()) >= MIN_PARAGRAPH_WORDS]
            if len(result_s) > 1:
                return result_s

    return result


def _merge_short_segments(segments: list[str]) -> list[str]:
    """Merge segments shorter than MERGE_THRESHOLD_WORDS with neighbors."""
    merged = []
    buffer = ""
    for p in segments:
        if buffer:
            buffer += " " + p
        else:
            buffer = p
        if len(buffer.split()) >= MERGE_THRESHOLD_WORDS:
            merged.append(buffer)
            buffer = ""
    if buffer:
        if merged:
            merged[-1] += " " + buffer
        else:
            merged.append(buffer)
    return merged


# Sentence boundary: punctuation followed by space and uppercase letter.
# Requires at least 2 lowercase letters before the punctuation to avoid
# splitting on abbreviations like "Dr.", "F.", "Jr.", "U.S.", etc.
# The merge step handles any remaining short segments.
_SENTENCE_SPLIT = re.compile(
    r'(?<=[a-z]{2}[.!?])\s+(?=[A-Z])'
)


def _split_sentences(text: str) -> list[str]:
    """Split text into sentences using punctuation + uppercase boundaries."""
    parts = _SENTENCE_SPLIT.split(text)
    return [p.strip() for p in parts if p.strip()]


# -- Scoring ----------------------------------------------------------------

def _score_evidence_density(paragraphs: list[str]) -> list[float]:
    """Score paragraphs by density of evidential language.

    Returns a list of scores (higher = more evidence patterns per 100 words).
    """
    scores = []
    for p in paragraphs:
        p_lower = p.lower()
        count = sum(len(pat.findall(p_lower)) for pat in _COMPILED_EVIDENCE)
        word_count = max(len(p.split()), 1)
        scores.append(count / (word_count / 100))
    return scores


def _score_bm25(claim: str, paragraphs: list[str]) -> list[float]:
    """BM25 relevance scoring of paragraphs against the claim."""
    claim_terms = [t for t in re.sub(r'[^a-z0-9\s]', '', claim.lower()).split()
                   if t not in _STOPS]

    if not claim_terms or not paragraphs:
        return [0.0] * len(paragraphs)

    n = len(paragraphs)
    avgdl = sum(len(p.split()) for p in paragraphs) / n
    k1, b = 1.5, 0.75

    # Document frequencies
    df: Counter = Counter()
    for p in paragraphs:
        p_words = set(re.sub(r'[^a-z0-9\s]', '', p.lower()).split())
        for t in claim_terms:
            if t in p_words:
                df[t] += 1

    scores = []
    for p in paragraphs:
        p_words = re.sub(r'[^a-z0-9\s]', '', p.lower()).split()
        dl = len(p_words)
        tf = Counter(p_words)
        score = 0.0
        for t in claim_terms:
            if t not in tf:
                continue
            idf = math.log((n - df.get(t, 0) + 0.5) / (df.get(t, 0) + 0.5) + 1)
            tf_norm = (tf[t] * (k1 + 1)) / (tf[t] + k1 * (1 - b + b * dl / avgdl))
            score += idf * tf_norm
        scores.append(score)
    return scores


def _normalize(scores: list[float]) -> list[float]:
    """Min-max normalize scores to [0, 1]."""
    max_s = max(scores) if scores else 0
    if max_s <= 0:
        return [0.0] * len(scores)
    return [s / max_s for s in scores]


# -- Main API ---------------------------------------------------------------

def extract_relevant_paragraphs(
    article_text: str,
    claim: str,
    max_words: int = MAX_EXTRACT_WORDS,
    relevance_weight: float = RELEVANCE_WEIGHT,
    evidence_weight: float = EVIDENCE_WEIGHT,
) -> tuple[str, float]:
    """Extract the most evidence-rich paragraphs from an article.

    Args:
        article_text: Full article text (from trafilatura or similar).
        claim: The claim being verified.
        max_words: Maximum word budget for the extracted text.
        relevance_weight: Weight for BM25 topical relevance (default 0.3).
        evidence_weight: Weight for evidence density patterns (default 0.7).

    Returns:
        Tuple of (extracted_text, max_combined_score).
        - extracted_text: concatenated paragraphs in original document order.
        - max_combined_score: highest paragraph score (0-1). Low scores
          indicate the article likely doesn't contain claim-relevant evidence.
    """
    if not article_text or not article_text.strip():
        return "", 0.0

    # Clean trafilatura artifacts (pipes, refs, sidebars, editorial notices)
    article_text = _clean_extracted_text(article_text)
    if not article_text:
        return "", 0.0

    paragraphs = _split_paragraphs(article_text)

    if not paragraphs:
        words = article_text.split()
        return _trim_to_last_sentence(' '.join(words[:max_words])), 0.0

    if len(paragraphs) == 1:
        words = paragraphs[0].split()
        return _trim_to_last_sentence(' '.join(words[:max_words])), 0.0

    # Score each paragraph
    bm25_scores = _normalize(_score_bm25(claim, paragraphs))
    evidence_scores = _normalize(_score_evidence_density(paragraphs))

    combined = [
        relevance_weight * bm25_scores[i] + evidence_weight * evidence_scores[i]
        for i in range(len(paragraphs))
    ]

    max_score = max(combined) if combined else 0.0

    # Rank by combined score, select within word budget
    ranked_indices = sorted(range(len(paragraphs)), key=lambda i: -combined[i])

    selected_indices = []
    word_count = 0
    for idx in ranked_indices:
        p_words = len(paragraphs[idx].split())
        if word_count + p_words <= max_words:
            selected_indices.append(idx)
            word_count += p_words
        elif not selected_indices:
            selected_indices.append(idx)
            break

    # Return paragraphs in ORIGINAL document order (preserves reading flow)
    selected_indices.sort()
    result = '\n\n'.join(paragraphs[i] for i in selected_indices)

    words = result.split()
    if len(words) > max_words:
        result = _trim_to_last_sentence(' '.join(words[:max_words]))

    return result, max_score