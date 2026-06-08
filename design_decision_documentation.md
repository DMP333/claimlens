# Project A — Design Decisions Log
### Evidence Intelligence API (ClaimLens / FalseClaimDetector)

This document collects the design decisions made across the whole project where more than one option was genuinely on the table. For each one it records what the decision was about, the options weighed, why the chosen option won, and the **specific numbers** involved plus how each number was set. The point is interview readiness: being able to say "here is what I built, here is what I rejected, here is why, and here is the exact threshold and how I picked it" is what separates a real engineering story from a memorized one.

A note on the numbers: each value is tagged so the honesty is explicit.
- **[tested]** = chosen by running a comparison and reading the result.
- **[tunable]** = a knob set to a sensible starting value, meant to be retuned against real data.
- **[heuristic]** = a defensible judgment call, not optimized against a labeled dataset (often because no such dataset existed).
Being able to say which is which, especially admitting the heuristic ones, reads as honest engineering rather than false precision.

---

## 0. Cross-cutting principles

- **No LLM anywhere in the verification pipeline (non-negotiable).** The differentiator is independent, transparent evidence aggregation, not a model's opinion. An LLM in the stance or summarization path would make it a GPT wrapper and destroy the independence claim. The LLM appears only offline, as a labeling teacher for fine-tuning, never at inference.
- **Anti-overfitting is sacred.** Fixes are designed as general mechanisms and validated on claims outside the test set, never reverse-engineered from test-set errors. This was violated once, produced inflated accuracy, and cost real time, after which it was enforced strictly.
- **Test on real data, not synthetic.** The 71% Wikipedia artifact rate and the enrichment regression were only visible on the real pipeline.
- **Root cause over band-aid; principled over keyword hacks.** Keyword matching was repeatedly rejected as overfitting, except where a rule genuinely matches a production baseline.
- **Correctness over speed, even at build time.** fp32 over mixed precision, full files over diffs, explore wide before committing.

---

## 1. Project framing and scope

### Fact-checker vs evidence analyst
**About:** the core identity of the product.
**Options:** (a) a verdict machine returning true/false; (b) an evidence tool that always shows both sides and treats a verdict as an optional add-on.
**Chose:** (b). Contested claims have two defensible sides, so forcing a verdict is both wrong and less useful than showing the evidence. The verdict layers on only for high-confidence factual claims. This is also the differentiator versus Webcite, Factiverse, ClaimBuster, Full Fact: claim-type-aware adaptive output and evidence transparency.

### LLM in the pipeline, or not
**Options:** (a) use an LLM for pre-summarization or stance; (b) keep the pipeline LLM-free.
**Chose:** (b), to protect independence and avoid being a GPT wrapper. This forced every harder downstream decision (sentence-level NLI, fine-tuning).

### The Google Fact Check "derivative" concern
**Chose:** reframe Google Fact Check as one of six independent inputs feeding aggregation, credibility scoring, and synthesis, not the product itself.

---

## 2. Source retrieval

### Which source APIs
**Cut:** Serper (one-time 2,500-credit cap), NewsAPI (free tier restricted to development), GDELT (early set, later swapped out).
**Chose (final six):** Google Fact Check, Wikipedia, Semantic Scholar, OpenAlex, DuckDuckGo, Wikidata. All free, production-usable at roughly zero cost, spanning fact-checks, encyclopedic text, academic literature, open web, and structured facts.

### Concurrency: async vs threads vs processes
**Options:** serial; `asyncio.gather` on one thread; threads; processes.
**Chose:** `asyncio.gather` with `return_exceptions=True`. The work is network-bound idle waiting, which a single event loop overlaps for free. **[tested]** Measured later: the gather ran in about **3.8s** against a **13.6s** serial sum, confirming real parallelism. Per-source timeout wrapper set to **SOURCE_TIMEOUT_SECONDS = 10.0 [tunable]** so one hung API is dropped rather than stalling the request.

### Per-page enrichment concurrency (latency diagnosis)
**Chose:** read the code and measure before "fixing." The assumption that DuckDuckGo fetched serially was wrong; it already uses `asyncio.gather`. No cheap fix existed; the search stage is bounded by the single slowest connector. Lesson logged: confirm against the code first.

---

## 3. Source quality, enrichment, and contamination

### Relevance filtering
**Chose:** all-MiniLM-L6-v2 cosine similarity, threshold **RELEVANCE_THRESHOLD = 0.35 [tested/heuristic]**. The cutoff was chosen by observing it removed clearly off-topic sources (Real Madrid, a video game) from unrelated queries while keeping on-topic ones; it was not optimized against a labeled relevance set, so it is a validated-by-eyeball threshold, not a tuned one. Keyword matching was rejected as overfitting.

### Content extraction (the scoring he asked about, part 1)
**About:** turning a full fetched article into the most evidence-rich snippet.
**Options:** positional truncation (first N words); BM25 relevance; evidence-density patterns; a blend.
**Chose:** a blend in `content_extractor.py`, **RELEVANCE_WEIGHT = 0.3** (BM25) and **EVIDENCE_WEIGHT = 0.7** (evidence density). **[tested]** On hard synthetic cases with known gold paragraphs: evidence-density alone hit 3/4 top-1, BM25 alone 1/4, and the 30/70 blend hit 3/4 while being robust to edge cases. The 70/30 split toward evidence reflects that a paragraph can be topically relevant while containing no actual evidence.
Other extractor constants: **MAX_EXTRACT_WORDS = 400** (a word budget that captured the gold paragraph in 4/4 test cases) **[tested]**; **MIN_PARAGRAPH_WORDS = 15** (below this is treated as a heading/artifact) **[heuristic]**; **MERGE_THRESHOLD_WORDS = 30** (segments shorter than this get merged with neighbors to avoid noisy micro-chunks) **[heuristic]**. BM25 parameters left at the standard **k1 = 1.5, b = 0.75 [heuristic, library-standard defaults]**.

### Wikipedia content: intro vs full article
**Chose:** full article text fetched in parallel, then run through `content_extractor`, because evidence often lives in body sections, not the intro.

### Trafilatura HTML artifacts
**Chose:** add `_clean_extracted_text()` regex pre-processing after real data showed **71%** of Wikipedia snippets carried artifacts (infobox pipes, reference brackets, sidebars). Result: **120/120** clean, accuracy **83% to 86%**. **[tested on real data]** Hardened the "test on real data" rule.

### Deduplication: one layer vs three
**Chose:** three-layer dedup (URL normalization, title normalization, content hash on the first 200 chars), validated against a labeled set showing title-based duplicates that URL-only dedup would miss (mostly Semantic Scholar and OpenAlex returning the same paper under different URLs). Dedup priority is encoded as a score: **fact_check +2000, encyclopedia +1500**, plus citation count capped at **1000**, plus a snippet-richness bonus **[heuristic, ordinal-only]** (the absolute values do not matter, only that fact-check outranks encyclopedia outranks raw academic). A bug was fixed where URL dedup used a first-in-wins set instead of a priority-aware dict.

### Source contamination
**About:** **89 of 1,178** sources (**7.6%**) were topically adjacent but wrong (wrong entity, adjacent subtopic, entertainment-title collisions like a novel or band whose name matches the claim). MiniLM plus the parenthetical-marker regex could not catch these.
**Six design axes tested:** when filtering happens, what text to filter on, which model scores relevance, query construction, source-type-specific pipelines, single vs multi-stage. **[tested]** via a labeled harness (89 contaminated, 1,089 clean) running 9 combinations of 3 models by 3 input types.
**Rule attached:** any fix must be a general mechanism validated on new claims, never reverse-engineered from the contaminated examples. Subsequently judged mostly addressed and parked so as not to block the finish.

### Temporal filtering (Step 6): skipped
**Chose:** skip. Analysis of all sources showed only about **4%** (7 of 175 temporal sources) were genuinely problematic, concentrated in a few current-events claims; 96% were valid study dates and context. False-positive risk outweighed the tiny gain.

### Query reformulation (Step 7): skipped
**Chose:** skip. The sources were already topically correct; the errors were NLI misclassification, so better queries would just return more debunking articles that would also be misread.

---

## 4. Credibility scoring (the scoring he asked about, part 2)

### Flat score vs tiered system
**Options:** one flat credibility score; a tiered system using different signals per source type.
**Chose:** three tiers, because different source types carry trust in different forms and a flat score discards that.
- **Tier 1, verified:** an exact match in the Media Bias/Fact Check CSV (idiap dataset, Apache 2.0). Uses the dataset's bias and factual-reporting ratings directly.
- **Tier 2, estimated:** OpenPageRank domain authority plus source-type-specific scoring.
- **Tier 3, unverified fallback:** **0.30 [heuristic]**. A round low-but-nonzero value: an unknown web source should count for little but not zero.

### The specific per-type scores, and how they were set
All of these are **[heuristic]**: they encode "more signal equals more credible" with round, defensible cutoffs. They were not optimized against a labeled credibility dataset, because none existed. The honest interview line is exactly that.

- **Academic (`_score_academic`), by citation count:** roughly **1000+ citations to 0.95**, **mid-range (around 50) to 0.65**, **few or none to 0.40**. Reasoning: a heavily cited paper is demonstrably authoritative; an uncited one is not yet vetted by the field, so it gets a floor rather than a high score.
- **Wikipedia (`_score_wikipedia`), by quality signals:** **Featured/Good Article to 0.95**, **long article (around 20,000 chars) to 0.80**, **short stub (around 100 chars) to 0.55**. Reasoning: Featured status is a vetted-by-editors signal; article length is a rough proxy for maturity and sourcing.
- **Unknown web:** the **0.30** Tier-3 floor.

The defensible framing for all of these: they are ordinal and conservative. The exact decimals do not carry meaning beyond "clearly authoritative" versus "plausible" versus "unverified," and they would be the first thing to calibrate if a labeled credibility set existed.

---

## 5. Claim classification and routing

### Classifier: model vs rules
**Options:** the original lighteternal fact-or-opinion XLM-RoBERTa model; zero-shot/embedding; keyword lexicon plus NLTK POS tagging.
**Chose:** keyword lexicon plus POS tagging in `claim_classifier.py`, with a scientific-context override so quantitative claims do not misfire as opinion. The XLM-R model was broken in practice. **[tested]** Reached **100% type accuracy** and **93% domain accuracy** on 42 test claims, with residual errors on genuinely ambiguous cases the field considers open. The POS-tag baseline matches what ClaimBuster uses.
**Confidence values are fixed bands [heuristic]:** phrase match **0.95**, keyword match **0.90**, comparative/superlative POS **0.85**, default factual **0.80**. These are tiers of "how strong is the signal," not probabilities.
**Honest caveat recorded:** this classifier is overfitting-by-design and is on the backlog to be replaced with zero-shot or embedding-based classification. Opinion keyword lists (OPINION_KEYWORDS, and testable-property words like "dangerous"/"safe") were explicitly removed as fragile hardcoding.

### Source routing by domain
**Chose:** `source_router.py` maps claim domain plus keyword-to-academic-field analysis into per-source config, so scientific claims send field filters to Semantic Scholar and post-filter OpenAlex by topic, with a cap of about **7 results** per academic source for filtered domains. Better per-type inputs beat a uniform pipeline.

---

## 6. NLI stance detection

### Base model: SNLI/MNLI vs FEVER-trained
**Chose:** swap cross-encoder/nli-deberta-v3-base for MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli (same architecture, plus FEVER fact-verification training). It flipped textbook cases like "climate change is real" from likely-opposed to strongly-supported. LABEL_MAP locked at **{0: supporting, 1: neutral, 2: opposing}** after an earlier label-ordering bug dropped accuracy to 3/22.

### Premise: title+snippet vs snippet only
**Chose:** snippet only. The title carries the topic name, which poisons the model into reading "about X" as "supports X."

### Is NLI even the right architecture
**Chose:** keep NLI, fix how it is applied. BART zero-shot with a custom "discusses" label was **[tested]** and rejected (fixed 2 cases, broke 1, never actually assigned "discusses"). An LLM was rejected on principle. The real fixes were sentence-level processing and fine-tuning.

### Sentence-level vs paragraph-level NLI
**Chose:** sentence-level, **[tested] 3.6x better** than paragraph-level on real enriched content. Concretely, per-source accuracy moved from **47.2% (paragraph)** to **70.7% (sentence-level 3K)** on the Set B validation. A long passage dilutes the one decisive sentence. This also explained the earlier **-6.8pp** enrichment regression.

### Sentence splitter: nltk vs spaCy
**Chose:** nltk `sent_tokenize` plus preprocessing (et al., B.o.B., edit markers, "No." patterns), after a comparison showed a **58.5%** disagreement rate between nltk and spaCy on 349 real sources, proving the choice mattered enough to test. **[tested]**

### Aggregation strategy
**Options:** 3A strongest single signal; 3K Bayesian log-likelihood ratio; 3J top-K comparison.
**Chose:** keep all three swappable, default **3K**. **[tested]** Source-level accuracy: **3K 86.3%, 3A 82.4%, 3J 79.4%**. Later fresh-baseline analysis found a different ranking at verdict level (**3A 68.5%, 3K 57.4%** on non-opinion claims), which is exactly why keeping them swappable paid off. Skepticism about 3K's independence assumption was recorded; the call was made empirically, not theoretically. Current DEFAULT_STRATEGY is **3K**, noted that the comparison predates fine-tuning and is worth re-running.

### Sentence-level relevance filtering (D5): rejected
**Chose:** keep all sentences. **[tested]** Both pattern-based and MiniLM filtering hurt every strategy, and hurt 3K specifically, because the neutral-looking sentences still carry weak directional signal the Bayesian aggregation uses.

### Min sentence length and batching
**Chose:** **10-word minimum [tested]** to drop fragment noise, **batch size 32 [tunable]** for inference speed.

---

## 7. Fine-tuning the NLI model

### Whether to fine-tune
**Chose:** fine-tune. Rules were overfitting, the LLM was off-limits, and the failures were systematic (the pre-fine-tune model showed catastrophic gaps: **weak_negation 8.3%, genuine_oppose 50%**, with a strong neutral bias misclassifying **53%** of genuinely opposing content as neutral).

### Dataset: FNC-1 vs custom
**Chose:** custom. **[tested]** FNC-1 was tried and rejected (domain mismatch, polarized predictions to 0.0/1.0, overcalled "discuss"). Built a custom dataset, expanded from **62 to 150 claims (100 train / 50 test)** with a stratified split, same-entity pairs kept entirely on the train side, zero cross-split entity collision. Full silver-label pass produced **24,597 labels** (roughly **80% neutral / 10% opposing / 8% supporting**, 0.17% refusals).

### Labeling method
**Chose:** an LLM teacher (claude-sonnet) under a locked strict prompt, after hybrid and manual approaches were explored. The teacher was validated first (about **84% beneficial** on a graded poison-pile audit) before being trusted. This is an offline labeler, which does not violate the no-LLM-at-inference rule.

### LoRA vs full fine-tuning
**Chose:** LoRA (freeze base, train adapters). Full fine-tuning repeatedly collapsed: mixed-precision instability, dtype bugs, NaN divergence, majority-class collapse. LoRA was the stable path and is cheaper to ship.

### fp32 vs mixed precision
**Chose:** fp32. Mixed precision was identified as the root cause of the collapse. Correctness over training speed.

### Size, sequence length, result
**Chose:** DeBERTa-v3-large, **max_len 256**, trained on a RunPod RTX 4090 (**$0.69/hr**). Sealed-test result: **macro-F1 0.66 to 0.80, accuracy 84% to 89%**, stable across **3 seeds**. This is the headline resume metric.

### Headline metric: source-level vs verdict-level
**Chose:** source/sentence-level as the headline (hundreds of data points, tight CI), verdict-level as a supporting stat, because verdict-level conflates aggregation, contamination, and mislabeled-expectation errors and has too few data points to defend.

---

## 8. Source-type-specific handling

### One pipeline vs per-type
**Chose:** route by source type. One NLI path for fact-check ratings, structured Wikidata facts, and web paragraphs was judged architecturally wrong.

### Fact-check: rating bypass vs NLI
**Chose:** rating bypass only, drop if unparseable, no NLI fallback (fact-check articles quote the claim they debunk, so NLI reads refutation as endorsement). **[tested] +23.6pp** over raw NLI on fact-check sources.

### Fact-check rating parser (more scoring numbers)
**Chose:** a per-rating confidence lookup map (`RATING_LOOKUP`) instead of flat sets, **[heuristic, definitiveness-weighted]**. The confidence reflects how definitive each rating is:
- Strong negative: **"pants on fire" 0.99, "false" / "incorrect" / "fabricated" / "not true" 0.95, "mostly false" / "three pinocchios" / "altered" 0.85, "barely true" / "partly false" / "no evidence" 0.80**.
- Soft negative: **"misleading" / "flawed" 0.75, "unproven" / "outdated" 0.70, "missing context" / "lacks context" 0.65, "half true" / "mixture" 0.55** (these barely count).
- Positive: **"true" / "accurate" / "confirmed" 0.95, "mostly true" 0.85, "one pinocchio" 0.75**.
A substring fallback (when the exact label is not matched) is capped at **0.75** so an inferred match never scores as high as an exact one. The alignment confidence threshold was lowered from **0.70 to 0.55 [tested]** to recover bypass cases.

### Fact-check multi-review and bypass direction
**Chose:** expand across all `claimReview` entries (the API was only using the first), and restrict the bypass so only a supporting alignment triggers a flip while opposing-alignment cases drop, removing a class of wrong-direction errors. The double-inversion case (opposing alignment plus strong rating) requires alignment confidence **>= 0.85** before flipping, a deliberately high guard.

### Wikidata: include in NLI or not
**Chose:** exclude. Tagged `knowledge_graph`, marked neutral, kept as a structured reference only, because running NLI on structured facts is meaningless.

---

## 9. Verdict computation

### Opinion claims: verdict or not
**Chose:** soft verdicts ("sources lean supporting / divided / opposing"), because transparency about what sources say beats suppressing the signal.

### Verdict thresholds
The weighted support ratio maps to labels at **[heuristic, symmetric] >= 0.80 strongly supported, >= 0.60 likely supported, > 0.40 contested, >= 0.20 likely opposed, else strongly opposed**. Round symmetric cutoffs; the 0.40 to 0.60 contested band is deliberately wide so genuinely split evidence is not forced to a side.

### Confidence formula: lopsidedness vs evidence-weighted
**Chose:** direction times evidence mass, not lopsidedness alone. Confidence = `(abs(ratio - 0.5) * 2) * (total / (total + K))` with **EVIDENCE_SATURATION_K = 2.0 [tunable]**. The old formula gave a thin, unanimous-but-weak set a full 1.0; the K factor means a source pool with total weight 2.0 only reaches a 0.5 evidence factor, so thin or weak evidence can no longer score maximum confidence by being one-sided. K = 2.0 is a starting value explicitly meant to be tuned against real runs.

---

## 10. Testing strategy

### What to unit test, what to skip
**Bar used:** "would a sharp interviewer attack this gap." **Tested:** verdict computation, rating parsing, dedup, the classifier, NLI aggregation, routing, credibility tiering, plus one integration test (42 tests passing). **Skipped on purpose:** per-connector parsing (thin I/O adapters, integration-covered) and NLI model accuracy (covered by the fine-tuning eval).

### Unit vs integration, why both
**Chose:** both. Unit tests catch wrong logic inside a function; the integration test catches seam bugs between functions that every unit test would individually pass. The integration test mocks only the outer edges and lets the real chain run.

### Asserting confidence numbers
**Chose:** assert ranges and relationships (a richer set scores higher than a thin one), never magic constants, so retuning K does not break tests. Verdict labels, being a stable contract, are asserted exactly.

---

## 11. Backend design: async jobs and the database

### Caching: cache results, or not
**Chose:** do not cache. Web evidence is volatile, history is meaningless without auth, and an NLI-result cache has a low hit rate. All cache-key and TTL machinery was rejected as solving a non-problem.

### Synchronous vs async job
**Chose:** async job. Warm latency is about **10s** locally and higher on a budget cloud box, too long to block on. **[measured before committing]** The database exists as the shared place where the in-flight job and its result live between the separate submit and poll requests.

### Polling vs push
**Chose:** polling. The server stays purely reactive and stateless per request, no persistent connection. The client submits once, then sends repeated GETs by id until status flips to done.

### Job status states
**Chose:** three: pending, done, failed. Two would leave a crashed job pending forever; more would be empty ceremony with in-process execution.

### Background execution: in-process vs queue
**Chose:** in-process (FastAPI/asyncio), with two acknowledged caveats: a restart loses an in-flight job (over-stale pending rows get marked failed), and the blocking NLI runs in a thread so it does not freeze the event loop. An external queue (Celery/arq + Redis + worker) is the durable answer but is unjustified infrastructure at this scale.

### DB down at submit: degrade or fail
**Chose:** clean **503**. Once the database is core rather than an optional cache, the honest behavior is to fail loudly. This is a deliberate flip from the earlier cache-era "degrade gracefully" reasoning.

### API status codes
**Chose:** POST returns **202** (work started). GET returns **200** for any existing job including a failed one (failure described in the body), and **404** only for an unknown id. HTTP code answers "did the lookup work," the body answers "what happened to the job." A crashed pipeline is an expected outcome, not a server error, so it is not a 500.

### ID type: UUID vs auto-increment
**Chose:** UUID (122 random bits). The id goes in a shareable poll URL; sequential integers are guessable, enumerable, and leak volume. UUIDs are unique with overwhelming probability and need no central counter or cache.

### Storage: Postgres vs Redis
**Chose:** Postgres. Redis could hold in-flight state (and commonly does), but the results here are durable, revisitable records, and Redis is built for fast transient expiring data. Using both would be the real over-engineering at this scale; one durable store covers tracking plus the kept result.

### ORM: SQLAlchemy vs alternatives
**Chose:** SQLAlchemy async on asyncpg. Usage is three trivial statements (insert one row, update it, select by id), so the ORM is pure upside (Python objects, type safety, no injection-prone SQL strings). Raw SQL only for a hot/awkward query; a different ORM only for framework or model-integration reasons.

### Schema management
**Chose:** create-on-startup via a lifespan hook, not Alembic. Alembic is for a schema that evolves across releases; overkill for one stable table.

### No deduplication of submissions
**Chose:** each submission is its own timestamped row, because evidence changes over time and "same claim" matching is effort for little payoff.

---

## 12. Latency (diagnosis and resulting calls)

### Where the time goes
**Finding [measured]:** warm latency about **10s** locally; search stage roughly **4 to 7s** (bounded by the slowest connector, DuckDuckGo); the rest including NLI about **3s**. The assumption that NLI dominated was wrong.

### Fetch timeout as a tradeoff
**Chose:** **FETCH_TIMEOUT = 3.0s** per page, **MIN_ENRICHED_WORDS = 25** to fall back to the search snippet. **[tunable, latency-vs-coverage]** Lower would drop slow-but-valid pages and lose evidence; higher would let one slow page drag the request. Since fetches are parallel, the stage is bounded by the slowest of about ten open-web pages.

### Cutting latency further: parked
**Options:** lower the timeout, fetch fewer pages, swap DuckDuckGo's scraper for a paid search API, deploy on a GPU.
**Chose:** none for now; all trade quality, scope, or cost, and async hides the latency. Deployment latency is a money-versus-speed knob (a bigger instance or a GPU runs NLI faster but costs more); the realistic portfolio choice is a small cheap instance plus async.

---

## 13. Methodology and process decisions

### Phase 1 steps 6 and 7: skipped
Temporal filtering and query reformulation were designed and then deliberately skipped after the data showed low impact and high risk (see Source quality).

### Dataset size: 62 vs 150 claims
**Chose:** expand to 150 (100 train / 50 test). 62 was fine for the source-level headline (many data points) but too thin for the verdict-level supporting stat; budget went to a clean held-out test set over more training data.

### Evaluation architecture: end-to-end vs layered
**Chose:** evaluate layer by layer (sentence-level NLI, source relevance, aggregation) instead of one verdict number that conflates four error sources. This also surfaced that some test-set labels were themselves wrong, which an end-to-end number had hidden.

---

*Living document. Append new decisions from the remaining work (database build, Docker, CI/CD, AWS deploy, frontend) in the same format, with the same [tested]/[tunable]/[heuristic] tagging on every number.*