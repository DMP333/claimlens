# ClaimLens

An evidence intelligence API for factual claims. It shows what sources say on
both sides, and gives a verdict only when the evidence earns one.

Status: portfolio project, built solo. The pipeline is complete and deployed.

Live instance: http://44.240.204.197:8000
The box is usually off to save cost, so the link responds only while it is
running. To use ClaimLens any time, run it locally (see Quickstart).

---

## Why I built it

People increasingly treat contested questions as black and white, when plenty
of claims have real evidence on both sides. Most automated fact-checking tools
lean into that: they lead with a verdict, true or false, rather than the
evidence behind it.

ClaimLens was built to push the other way, to put the evidence on both sides in
front of people and let them reach their own conclusion. It works as a research
analyst, not a judge. Its main output is always the supporting and opposing
evidence, not a label. A verdict is layered on top, but only when the evidence
is one-sided enough to earn one, and for genuinely split claims it says they are
split instead of picking a side.

---

## Demo

Demo video and screenshots: Planned.. Hopefully coming soon!

A live instance is available at the address listed at the top of this README. It
is usually kept off to control cost, so it responds only while the box is
running. To try ClaimLens any time, run it locally. See Quickstart.

---

## How it works

A claim goes in, travels through the pipeline below, and comes back with a verdict and the evidence on both sides. This is the path a request takes; the reasoning behind each choice is in Design decisions.

1. **Classify the domain.** A lightweight rule-based classifier, keyword matching with a little part-of-speech tagging and no model, tags the claim as scientific, historical, current events, statistical, or general. This is used only to steer the search, and it is not part of the output.

2. **Route the search.** The domain decides how each source is queried. A scientific claim, for example, sends a field-of-study filter to the academic sources so they come back with relevant literature instead of noise.

3. **Search the sources.** Five sources, Google Fact Check, Wikipedia, Semantic Scholar, OpenAlex, and DuckDuckGo, are queried at the same time, each under a short timeout so one slow source cannot stall the request. Longer pages are reduced to their most relevant passage as they come back.

4. **Filter for relevance.** A small model scores how close each source is to the claim and drops the off-topic ones, so the heavier model later only reads material worth its time.

5. **Deduplicate.** The same source often arrives from more than one place, so duplicates are collapsed and the richer copy is kept.

6. **Score credibility.** Each source gets a credibility score: outlets in a known ratings dataset rank highest, others are estimated from signals like citation count or domain authority, and unknown sources get a low floor.

7. **Detect stance.** For web, encyclopedia, and academic sources, the fine-tuned model reads the source one sentence at a time and scores how each sentence leans. Those per-sentence scores are then aggregated into one stance for the source, supporting, opposing, or neutral, so the result rests on the whole body of sentences rather than any single line. Fact-check sources skip this and use their published rating instead.

8. **Weigh the evidence.** Each source's stance is weighted by how confident the model is and how credible the source is. The balance becomes a graded verdict, from strongly supported through contested to strongly opposed, with a confidence score that reflects how one-sided and how substantial the evidence is.

9. **Return the result.** The response is the verdict and its confidence, plus the supporting and opposing sources, each with its credibility and the evidence sentence behind its stance, so the reader can weigh both sides.

## Using the API

The website is just one client of the API; you can call the same endpoints directly from a script.

Set a base URL once and reuse it. Use the live address from the top of this README, or `http://localhost:8000` if you are running ClaimLens locally:

```bash
export BASE_URL=http://localhost:8000   # or the live address from the top of this README
```

Verifying a claim takes two steps: submit it, then poll for the result. Submitting hands back a job id immediately while the work runs in the background, so you poll that id until the job finishes.

### 1. Submit a claim

```bash
curl -s -X POST $BASE_URL/verify \
  -H 'Content-Type: application/json' \
  -d '{"claim": "The Great Wall of China is visible from space with the naked eye."}'
```

You get back a job id and a starting status:

```json
{ "id": "<job id, a UUID>", "status": "pending" }
```

| Status | Meaning |
| - | - |
| 202 Accepted | Claim accepted; the body carries the job id |
| 422 Unprocessable Entity | The claim is missing or not 3 to 1000 characters |
| 429 Too Many Requests | The server is at capacity; a `Retry-After` header says when to retry |
| 503 Service Unavailable | The verification store is unreachable |

### 2. Poll for the result

```bash
curl -s $BASE_URL/verify/<job id>
```

Call this with the id until `status` becomes `done` or `failed`. While the job is still `pending`, the response includes a `queue_position` so you can see how far back you are.

| Status | Meaning |
| - | - |
| 200 OK | The job exists; read its `status` from the body |
| 404 Not Found | No job has that id |
| 422 Unprocessable Entity | The id is not a valid UUID |
| 503 Service Unavailable | The verification store is unreachable |

A failed job is not an HTTP error. It still returns 200, with `status: "failed"` and an `error` message in the body.

### The response shape

This is the full shape of a poll response, with each field described. `result` is filled in only once `status` is `done`.

```json
{
  "id": "<job id, a UUID>",
  "status": "pending | done | failed",
  "queue_position": "<while pending: jobs ahead of you, 0 means next; null otherwise>",
  "created_at": "<when the job was submitted>",
  "completed_at": "<when it finished, or null while pending>",
  "error": "<message, only when status is failed; null otherwise>",
  "result": {
    "claim": "<the claim you submitted>",
    "verdict": "strongly supported | likely supported | contested | likely opposed | strongly opposed | insufficient evidence",
    "confidence_in_verdict": "<0.0 to 1.0>",
    "sources": [
      {
        "url": "<link to the source>",
        "title": "<source title>",
        "stance": "supporting | opposing",
        "stance_confidence": "<0.0 to 1.0, how sure the model is of the stance>",
        "credibility_tier": "verified | estimated | unverified",
        "credibility_score": "<0.0 to 1.0>",
        "bias_rating": "<bias label, only for verified sources; null otherwise>",
        "factual_reporting": "<factual-reporting label, only for verified sources; null otherwise>",
        "method": "sentence_nli | fact_check",
        "sentence_count": "<sentences read, for NLI sources; null otherwise>",
        "evidence": "<the sentence behind the stance, for NLI sources; null otherwise>",
        "snippet": "<the passage the evidence came from>",
        "rating": "<the publisher's rating, for fact-check sources; null otherwise>"
      }
    ]
  }
}
```

Sources come back supporting first, then opposing, with the strongest evidence at the top of each group. Sources the system reads as neutral are left out.

### Health check

```bash
curl -s $BASE_URL/health   # {"status": "ok"}
```

---

## Using the website

Open ClaimLens in a browser at the live address listed at the top of this README, or at `http://localhost:8000` if you are running it locally.

Type or paste a claim and submit it. After a few seconds you get a verdict with a confidence bar, then the sources for and against the claim shown side by side, each with its credibility score and the line of evidence behind its stance. A dark-mode toggle sits in the corner.

The live instance is usually kept off to control cost, so running it locally is the most reliable way to try the site. See Quickstart.

## Quickstart (local)

The reliable way to run ClaimLens yourself.

**Prerequisites:** Docker and Docker Compose. A CUDA GPU is optional; the model runs on CPU but is much slower.

**1. Get the code.** Clone the repo and move into it:

```bash
git clone https://github.com/DMP333/claimlens.git
cd claimlens
```

**2. API keys.** Create a `.env` file in the repo root:

```dotenv
GOOGLE_FACTCHECK_API_KEY=your_key_here
OPEN_PAGE_RANK_KEY=your_key_here
SEMANTIC_SCHOLAR_API_KEY=          # optional, raises rate limits
```

`DATABASE_URL` is set by Compose for the app container, so you do not need it here.

**3. Build and run.** The committed `docker-compose.yml` pulls a prebuilt image from a private registry, which a fresh clone cannot access. Use the local override, which builds the image from the Dockerfile instead of pulling it:

```bash
docker compose -f docker-compose.yml -f docker-compose.local.yml up --build
```

This builds the app image, starts PostgreSQL next to it, and serves on port 8000 once the database is ready. The first build is large and slow because it bundles the models into the image so the running app never has to download them; builds after that are cached and quick.

**4. Open it.** The web client is at [http://localhost:8000](http://localhost:8000), and the API is on the same origin (see below).

> If you would rather not build the full image, run only the `db` service and run the app on the host inside a virtualenv: `pip install -r requirements-dev.txt`, then `uvicorn app.main:app`. You still need the models available locally for that path.

---

## Architecture and stack

ClaimLens is a single FastAPI service, organized in layers so each concern sits in one place. From the outside in:

**API layer** (`app/main.py`, `app/api/routes/claims.py`). `main.py` builds the FastAPI app, mounts the claims router, serves the single-page web client at `/` and a `/health` check, and on startup creates the database table if it is missing. The router defines the two real endpoints, `POST /verify` and `GET /verify/{id}`, depends on a per-request database session, and hands the actual work to the service layer.

**Schema layer** (`app/models/schemas.py`). Pydantic models that define the request and response shapes plus the internal source objects the pipeline passes around. They validate input at the edge: a claim must be 3 to 1000 characters, an id must be a UUID. The same models serialize the pipeline output back to JSON.

**Service layer** (`app/services/`). Plain async functions, not classes. Two responsibilities live here. `verification_service.py` owns the job lifecycle: insert the row, run the pipeline in the background, poll it, and the admission control that bounds load. `claim_service.py` is the pipeline orchestrator that calls the rest in order: the classifier and router, the five source connectors, the content extractor, the NLI and relevance models in `nli_service.py`, and `credibility_service.py`. Each module does one job and is independently testable.

**Data layer** (`app/db/`). `session.py` sets up the async SQLAlchemy engine, the per-request session factory, and the declarative base. `models.py` defines the one table. See Database below.

**Config** (`app/core/config.py`). pydantic-settings loads the API keys and the database URL from a `.env` file into a typed settings object, so nothing reads raw environment variables ad hoc.

**Frontend** (`app/static/index.html`). One self-contained HTML and JavaScript file served at the root. It calls the same `/verify` endpoints, so the page and the API share one origin with no separate server and no CORS setup.

The stack, with the load-bearing versions:

- Web and API: FastAPI 0.136, uvicorn, httpx for outbound calls, Pydantic 2 for validation.
- Models: PyTorch 2.12, Transformers 5.8, PEFT 0.19 to apply the LoRA adapter, sentence-transformers for the MiniLM relevance model, NLTK for sentence splitting, scikit-learn for the cosine-similarity step in relevance scoring.
- Data: SQLAlchemy 2.0 async on the asyncpg driver, against PostgreSQL 16.
- Retrieval: trafilatura for article extraction, ddgs for DuckDuckGo search.

The NLI and relevance models are loaded once on first use, behind a lock, and reused for every request after that, so the load cost is paid once rather than per claim.

---

## Database

The database is the one piece of shared state in the system. Verification is a submit-then-poll job, so the submit request and the later poll request are two separate HTTP calls that share nothing in memory. The database is where the in-flight job and its result live in between.

It is one PostgreSQL 16 table, `verifications`, one row per submission, reached through SQLAlchemy 2.0 async on the asyncpg driver. The columns:

- `id`: a UUID primary key, defaulted to a random value, so a result URL cannot be guessed or enumerated.
- `claim`: the submitted text.
- `status`: `pending`, then `done` or `failed`. Only the service writes it.
- `result`: the full pipeline output stored as JSONB, null until the job finishes successfully.
- `error`: the failure message, null unless the pipeline raised.
- `created_at`: when the row was inserted.
- `started_at`: when the job actually began running, null while it is still waiting in the admission queue. The stale-job check measures from this, not from `created_at`, so a job legitimately waiting for a slot is never mistaken for a hung one.
- `completed_at`: when it reached done or failed.

The table is created on startup by a lifespan hook that runs `create_all`, which is idempotent and leaves an existing table untouched, so a restart never drops data. There is no migration tool, because one stable table does not need one.

---

## Deployment and CI/CD

ClaimLens is packaged and shipped with Docker and GitHub Actions. Each piece below maps to a file in the repo.

**The image (`Dockerfile`).** The whole app is packaged as one Docker image that already contains the code and the models it uses, so a running copy never has to download anything to work.

**Running it (`docker-compose.yml`).** A Compose file runs the app container alongside a PostgreSQL container. On the server it pulls a prebuilt image; from a fresh clone you build that image yourself with the `docker-compose.local.yml` override (see Quickstart).

**Testing (the `CI` workflow in `.github/workflows/`).** On every push to GitHub, this Actions workflow installs the project and runs the test suite automatically.

**Build and deploy (the `Build and Publish to ECR` workflow).** On a push to the main branch, this second Actions workflow builds the image, uploads it to Amazon's container registry (ECR), and then tells the server to pull that new image and restart on it. It signs in to AWS without storing any keys, and it reaches the server through an agent already running on the box rather than by opening a remote login. Each image is tagged with the exact commit it came from, so the running version is always traceable to one point in the code.

**Where it runs.** A single GPU server on AWS (EC2) runs the app and its database together. The server keeps a fixed address, an Elastic IP, that stays the same when it restarts, which is the live link shown at the top.

## Fine-tuning

The stance model is the part that reads a source and decides whether it supports, opposes, or stays neutral on the claim. Out of the box it was not good enough, so it was fine-tuned. This section is the result the rest of the project is judged on.

### Why fine-tune: the diagnosis

The decision came out of chasing real failures, not a hunch. While digging into why some verdicts came out wrong, I traced the errors down to individual sentences, and the same patterns kept appearing. The base model misread sentences that restate a myth in order to knock it down, the kind that often literally contain the word "myth," as if they supported the myth. It also misread sentences that contradict the claim through negation or an indirect construction, reading clear opposition as neutral or even support.

To make sure this was a real pattern and not a few cherry-picked cases, I pulled a set of exactly these hard sentences, labeled them with an LLM, and checked those labels against my own hand labels to confirm the test set itself was trustworthy (around 86% agreement). Then I measured the base model on it, and its sentence-level accuracy on these patterns was poor. These are not edge cases: debunking articles quote the myth they are debunking, and real sources qualify and negate constantly, so these sentences reappear all the time in a system that runs on live web text. Better inputs cannot fix a model that reads the inputs wrong, so the model itself had to change.

### The training data

I built a custom dataset rather than using an off-the-shelf one. The public option I tried, FNC-1, came from a different domain and pushed the model toward over-polarized predictions and an over-eager "discuss" label, so it hurt more than it helped. The custom set grew to 150 claims, split into 100 for training and 50 for testing, with the split arranged so that sentences about the same entity never land on both sides. That last part matters: it means the test score measures whether the model generalizes, not whether it memorized an entity it had already seen in training.

Labeling every sentence in that set produced roughly 24,597 labeled examples, heavily skewed toward neutral (about 80% neutral, 10% opposing, 8% supporting). That imbalance mirrors real sources, and it is the reason the headline metric is macro-F1 rather than raw accuracy: on data that is 80% one class, accuracy can look high while the model is quietly failing on the rare classes that actually carry the verdict.

### How it was labeled

Hand-labeling tens of thousands of sentences was not realistic, so I used an LLM as an offline labeling teacher, under a fixed strict prompt. This does not break the project's no-LLM-at-inference rule, because the LLM never runs when a user submits a claim. It only produced training labels ahead of time, and the trained model it taught is fully independent of it at runtime. Before trusting those labels, I audited the teacher against my own hand labels, where it agreed about 86% of the time, enough to train on rather than take on faith.

### LoRA instead of full fine-tuning

Full fine-tuning means retraining all of the model's weights, and on a small, heavily imbalanced dataset it kept collapsing: the model would give up and just predict the majority class, neutral, on almost everything. LoRA was the stable path. Instead of retraining the whole model, it freezes the original and trains a small set of add-on weights, the adapter, that nudge its behavior. Because the original model stays intact and only a small adjustment is learned on top, the model cannot throw away what it already knows and collapse that way, and the adapter is tiny next to the full model, far cheaper to train and to ship.

### The result

On a sealed test set the model had never seen, macro-F1 rose from 0.66 to 0.80 and accuracy from 84% to 89%, and the gain held across three random seeds rather than being one lucky run. The base model was DeBERTa-v3-large, trained at a 256-token limit on a rented RTX 4090. This is the number the project leads with.

### Which number is the headline, and why

I report the sentence-level score as the headline, not an end-to-end verdict-level one. The sentence-level metric has hundreds of data points and isolates the single thing fine-tuning changed: how the model reads stance. A verdict-level number folds in source retrieval, contamination, and aggregation, and on top of that, a real share of claims are contested or subjective enough that there is no objective correct verdict to grade against, so whether the model is right on them is not even a well-defined question. That makes it a noisier figure on far fewer data points, and it says less about the model than the clean sentence-level score. Leading with the well-supported number and treating the verdict-level result as a supporting stat is the honest way to report it.

## Concurrency

Each pipeline stage runs under a different concurrency model. The third column is the actual primitive in the code, not a paraphrase.

| Stage | Concurrency model | Mechanism in code |
|---|---|---|
| Search + enrich | Async fan-out, I/O-bound | `asyncio.gather` over the connectors; `asyncio.to_thread` for sync clients and HTML parsing |
| Relevance filter | Thread offload, small | `asyncio.to_thread` around the MiniLM pass |
| Split + aggregate | GIL-bound pure Python | runs inside `asyncio.to_thread`, but the GIL serializes the Python work to one core |
| NLI forward pass | Lock-serialized, single GPU | `threading.Lock` (`_MODEL_LOCK`) around the batched `torch.no_grad()` forward |
| Verdict + result | Trivial Python | inline on the event loop |

Each claim runs as a detached background job (`asyncio.create_task`), so the request returns a job id immediately and the client polls. A single event loop drives the service, and every blocking step, model calls, sync HTTP clients, and HTML parsing, is pushed off the loop with `asyncio.to_thread` so the loop stays responsive. One process-wide lock guards every GPU forward pass, relevance and NLI alike, so the single T4 is never entered by two threads at once. The load-shedding layer in front of all this is admission control, covered in the next section because its justification is a performance argument.

---

## Performance and scaling

| Stage | Light load (single run) | Heavy load (9 concurrent) | Growth |
|---|---|---|---|
| Search + enrich | 4.6s | 6.9s | ~1.5x |
| Relevance filter | 0.2s | 0.5s | small |
| Split + aggregate | 1.0s | 4.9s | ~5x |
| NLI forward (GPU) | 1.0s | 1.2s | flat |
| Lock wait | 0.4s | 1.2s | small |
| End to end | ~7s | ~15s | |

*Measured under 9 concurrent claims on a g4dn.xlarge (1x T4).*

**The bottleneck.** Under load the heaviest stage is the pure-Python split and aggregate, and because it is GIL-bound it cannot use more than one core no matter how much hardware is added. The GPU stays flat and search grows only mildly, so the real ceiling is the interpreter and the external APIs, not GPU compute.

**Handling it now.** The service caps how many pipelines run at once with admission control. A semaphore holds concurrency where latency is still good, extra requests wait in line for free, and once a hard ceiling is reached it returns a 429 instead of letting every request degrade together.

**Scaling further.** True horizontal scale means several worker processes behind a job queue. Each process gets its own GIL, so the stage stuck on one core today would finally run in parallel, with one GPU per worker. That is a larger rebuild, so at single-GPU scale the bounded single-process version shipped instead.

---

## Honest limitations

- The **in-process job model loses an in-flight job on restart** (over-stale pending rows are marked failed). The durable answer is an external queue, intentionally deferred as unjustified infrastructure at this scale.
- A few **low-credibility sources can still surface boilerplate** as their evidence sentence in the raw JSON. Display-only, does not affect stance or verdict, backlogged.
- The **aggregation strategy comparison predates fine-tuning** and is worth re-running; the three strategies are kept swappable for exactly this reason.

---

## Design decisions

This is the heart of the project. Each entry lists the options that were on the table, then the call that was made with its reasoning. A few decisions had no real alternative and are just explained.

### Product

**1. Evidence analyst, not a verdict machine**
- Option A: a verdict machine that returns true or false
- Option B: an evidence tool that always shows both sides, verdict optional

Chose B. Contested claims have defensible sides, so a verdict is layered on only when the evidence is one-sided enough to earn it, and genuinely split evidence is labeled contested rather than forced to a side.

**2. No LLM in the verification pipeline**
- Option A: use an LLM for stance or for summarizing sources
- Option B: keep inference free of any LLM

Chose B, for three reasons. Independence, so the product is not a wrapper around one model's opinion. Cost, since there is no per-request API bill and it runs on owned compute for nothing per call. Traceability, since every decision traces to a source, a model score, or a documented threshold. An LLM is used only offline, as a labeling teacher for fine-tuning.

### Sources

**3. The source set**
- Option A: include paid or limited APIs such as Serper, NewsAPI, GDELT
- Option B: a free set that still spans different kinds of evidence

Chose B. Google Fact Check, Wikipedia, Semantic Scholar, OpenAlex, DuckDuckGo. All free, near-zero cost, and covering fact-checks, encyclopedic text, academic literature, and the open web.

**4. Handling sources by type**
- Option A: one uniform pipeline for every source
- Option B: handle each source type differently

Chose B. The text handed to the model is gathered differently per source, because the sources are shaped differently. An open-web page is long and noisy, so the full article is fetched and the most evidence-dense passage is pulled out. A Wikipedia article is fetched as full body text rather than just the lead, because the evidence usually lives in the body sections. Academic results lean on the title and abstract, since full text is often paywalled. Fact-check sources are the exception: their stance comes from the published rating rather than from running the model on the article text, because the article quotes the very claim it is debunking, which the model would read as endorsement. The model is still used on them, but only to confirm the fact-check is reviewing the same claim the user asked about.

### Stance detection

**5. The stance model**
- Option A: a plain NLI model
- Option B: a DeBERTa NLI model also trained on fact verification
- Option C: a zero-shot classifier
- Option D: an LLM

Chose B, then fine-tuned it. The plain model failed on real content. The zero-shot approach with a custom "discusses" label was tested and rejected for barely helping while breaking other cases. An LLM was off the table by decision 2. The fine-tuning targeted specific failure patterns, for example a sentence that restates the myth it is debunking, which the base model read as agreement, and a claim phrased as a negation, which it sometimes read backwards.

**6. Sentence-level, not whole-source, not sliding window**
- Option A: feed the whole source text to the model at once
- Option B: split into sentences, classify each, aggregate
- Option C: a sliding window of about three sentences

Chose B. An NLI model is built to judge one short premise against one hypothesis, not a whole document, and my own informal testing showed it doing badly on full passages in several cases. The sliding window was rejected because the runtime blows up, since every source becomes many overlapping windows.

**7. Minimum sentence length**

Set at ten words, to drop fragment noise while keeping real sentences. No real alternative here, just a threshold.

**8. Aggregation method**
- Option A: trust the single most confident sentence
- Option B: combine all sentences probabilistically so many mild signals can add up
- Option C: compare the strongest few on each side

Chose B as the default, with all three kept swappable. A real source usually has several mildly leaning sentences that together are steadier than any single loud one. Kept swappable because which one wins changes depending on whether you score at the source level or the final-verdict level.

### The model

**9. Fine-tuning**

The base model was not good enough, so it was fine-tuned with LoRA. The full story, why the base failed, the silver-labeling, LoRA versus full fine-tuning, and the result, is in [Fine-tuning](#fine-tuning) below.

### Scoring and verdict

**10. Credibility scoring**
- Option A: one flat credibility score
- Option B: tiered by source type

Chose B, in three tiers, each scored from whatever signal is actually available. Verified sources are an exact match in the Media Bias/Fact Check dataset and use its bias and factual-reporting ratings, with the score coming from the factual-reporting rating, since those are vetted external assessments. Estimated sources are not in that dataset, so they are scored per type: an academic paper by its citation count, since a heavily cited paper is vetted by its field; a Wikipedia article by its quality signals, like featured status and article length; a general web page by its domain authority; and a fact-checker by a fixed high value, since fact-checking outlets are credible by role. Unverified sources are unknown pages with no usable signal, given a low but nonzero floor, because they should count for little but not nothing. The tier boundaries and per-type scores are my own categorization, not values tuned against a labeled credibility dataset.

**11. Confidence formula**
- Option A: pure one-sidedness
- Option B: one-sidedness scaled by how much evidence there is

Chose B:

```
confidence = one_sidedness * evidence_factor
  one_sidedness   = |support_ratio - 0.5| * 2          # 0 when evenly split, 1 when unanimous
  evidence_factor = total_weight / (total_weight + K)  # K = 2.0
```

One-sidedness alone would give a thin, unanimous, weak set of sources full confidence, which is wrong. The evidence factor holds a small pool back, so confidence rises only when the evidence is both one-sided and substantial. The verdict itself is a credibility-weighted combination of the source stances mapped to a graded label, with a deliberately wide contested band so split evidence is not forced to a side.

### Backend

**12. Serving model**
- Option A: a synchronous request that blocks until the answer is ready
- Option B: an async job the client polls

Chose B. Warm latency is too long to hold a request open. The client posts a claim, gets an id immediately, and polls for the result, which keeps the server stateless per request.

**13. Storage engine**
- Option A: a transient store like Redis
- Option B: a durable store like Postgres

Chose B. The results are durable, revisitable records, not throwaway cache. If the database is down on submit, the API fails loudly with a 503 rather than pretending to accept work.

**14. Job id**
- Option A: an auto-incrementing integer
- Option B: a UUID

Chose B. The id sits in a shareable poll URL, so a sequential integer would be guessable and enumerable, letting anyone read other people's results or infer how many were run. A UUID is random, unique without any central counter, and not enumerable.

**15. Caching results**
- Option A: cache results with a TTL
- Option B: no cache

Chose B. Web evidence changes over time, so a cached result goes stale, and even a small change in how a claim is worded produces a different search, so cache hits would be rare. The caching machinery would solve a non-problem.

### Concurrency

**16. Source retrieval concurrency**
- Option A: serial requests
- Option B: a single async event loop
- Option C: threads
- Option D: processes

Chose B. The work is almost entirely waiting on external servers, which one event loop overlaps for free. Threads and processes are the tools for CPU-bound parallelism, not for waiting on the network, and both add overhead and complexity that buy nothing when the work is just sitting idle waiting for a response.

**17. Serializing the GPU**
- Option A: let concurrent calls hit the single GPU and collide
- Option B: serialize them behind a lock

Chose B. The model runs in worker threads, so without a lock two calls could hit the single GPU at the same time and collide. The lock serializes GPU access, one forward pass at a time. The cost is small because the GPU work itself is small.

**18. Batching**

Per-source calls were collapsed from about twenty-two tiny calls per claim to about two, by sending every sentence from every source through the GPU together. Fewer, fuller calls mean less lock contention and better GPU use.

**19. Concurrency under load**
- Option A: buy more GPU
- Option B: bound the load with admission control
- Option C: accept everything and let all requests degrade together

Chose B. The GPU is the smallest slice of the time, so more of it would fix the wrong thing. Instead the system caps how many claims run at once, queues the rest with a visible position, and refuses work past a bounded depth with a 429. The measured runtime detail behind this is in the Performance and scaling section above.

### Deployment

**20. CPU versus GPU**
- Option A: a CPU instance
- Option B: a GPU instance with a T4

Chose B. The model is unusable on CPU, on the order of three minutes per claim, and drops to seconds on the GPU. The single biggest latency win in the project.

**21. CI credentials**
- Option A: long-lived AWS keys stored as secrets
- Option B: short-lived federated credentials through OIDC

Chose B. No standing AWS keys to leak.

**22. Box access**
- Option A: open an SSH port
- Option B: SSM Session Manager

Chose B. No inbound SSH port open to the internet.

### Testing

**23. Test coverage**
- Option A: test everything
- Option B: unit-test the logic worth attacking, plus one real-chain integration test

Chose B, on a "would a sharp interviewer attack this" bar. Unit tests cover verdict math, rating parsing, dedup, the classifier, aggregation, routing, and credibility tiering. One integration test runs the real pipeline with the outer edges faked, the searches and the models mocked, so it catches seam bugs between functions while still exercising the real chain. Validation was done on real claims rather than synthetic ones, because the real bugs only showed up on live data.

### Cut or deferred

Planned, then left for later as scope and time ran out:
- Claim decomposition into sub-claims
- Confidence calibration against a fact-checking dataset
- Query diversification
- User source injection with before-and-after confidence
- Claim specificity flags

---

## Repository layout

```
app/
  main.py                 FastAPI app, lifespan, frontend + health routes
  api/routes/claims.py    POST /verify, GET /verify/{id}
  models/schemas.py       Pydantic request/response + job envelope models
  db/                     async engine, session, Verification ORM model
  core/config.py          settings loaded from the environment
  services/
    claim_service.py        pipeline orchestrator + verdict math
    claim_classifier.py     claim type + domain (no model)
    source_router.py        per-domain source routing config
    nli_service.py          fine-tuned NLI, sentence-level stance, aggregation
    credibility_service.py  three-tier credibility scoring
    content_extractor.py    evidence-density passage extraction
    verification_service.py async job lifecycle + admission control
    google_factcheck.py / wikipedia.py / semantic_scholar.py /
    open_alex.py / duckduckgo.py   source connectors
  static/index.html       single-file web client
  data/mbfc_raw.csv        Media Bias/Fact Check credibility data
finetune/
  model_final/            the LoRA adapter loaded at runtime
  ...                     training scripts, datasets, and eval artifacts
Dockerfile, docker-compose.yml, requirements*.txt
CREDITS.md
```

---

## Credits

Models, datasets, source APIs, and libraries are attributed in [`CREDITS.md`](./CREDITS.md).

## License

MIT License. See [`LICENSE`](./LICENSE). This covers the code in this repository; the third-party models and datasets keep their own licenses, attributed in [`CREDITS.md`](./CREDITS.md).
