# ClaimLens latency reference (interview back-pocket)

Scenario: 9 claims submitted simultaneously to one g4dn.2xlarge (8 vCPU, 1x T4 GPU).
All numbers are measured. Light load = 1-3 concurrent, heavy load = 7-9 concurrent.

| phase            | light | heavy | grows? | GPU helps? | bottleneck type |
|------------------|-------|-------|--------|------------|-----------------|
| search+enrich    | 4.6s  | 6.9s  | 1.5x   | no         | external API wait + C parsing |
| relevance (MiniLM)| 0.2s | 0.5s  | small  | marginal   | small model compute |
| GPU forward      | 1.0s  | 1.2s  | flat   | YES (only) | single-GPU serial |
| CPU gap (python) | 1.0s  | 4.9s  | 5x     | no         | GIL-bound pure Python |
| lock wait        | 0.4s  | 1.2s  | small  | indirect   | consequence of single GPU |
| TOTAL            | ~7s   | ~15s  |        |            | |

## The one-sentence thesis
Under load the GIL-bound pure-Python work (sentence splitting + aggregation) grows 5x,
search grows 1.5x, and the GPU stays flat. The bottleneck is the interpreter and external
APIs, NOT the GPU. The expensive specialized hardware is the smallest slice.

## Per stage

### 1. Search + enrichment (biggest phase)
Six connectors fire concurrently (asyncio.gather); trafilatura parses returned HTML.
Mix of network WAITING (CPU idle) and C-level parsing (lxml releases GIL, so cores help).
Capped by: third-party server response times (not ours) + their throttling of bursts.
GPU: irrelevant, never touches GPU.
Done: already fully parallel. Optional future: result cache for repeat claims.

### 2. Relevance filter (small)
MiniLM embeds claim + snippets, cosine cutoff 0.35. Threaded. Small.
GPU: marginal benefit, not worth it at 0.5s.

### 3. GPU forward pass (THE PUNCHLINE: small + flat)
All sentence pairs + FC alignment through fine-tuned DeBERTa on T4.
After 3 batching rounds: exactly TWO batched calls per claim (was ~22 tiny calls).
C/CUDA, releases GIL, serialized across claims by _MODEL_LOCK (one GPU).
Capped by: single T4 executes serially. But work is only ~1.2s and FLAT under load.
GPU: this is the ONLY stage more GPUs would help. But it's the smallest slice, so
buying GPU = optimizing the wrong constraint. THIS is why we declined more GPU.
Done: GPU deploy (10-15x over CPU) + 3 batching rounds (22 lock visits -> 2).

### 4. CPU gap = sentence splitting + aggregation (THE THING THAT BLOWS UP)
nltk sent_tokenize + per-sentence dict building + 3K Bayesian aggregation. PURE PYTHON.
Capped by: the GIL. Pure-Python bytecode holds the GIL, so even though each claim's
splitting is on its own thread, threads can't run Python simultaneously - they time-share
one core's throughput regardless of 8 cores. Hence 5x growth under load while C-level
work grows little.
GPU: no effect (CPU-side Python).
Options surveyed and why declined:
  - Cap sentences/source: REJECTED, source-utility study proved breadth is load-bearing
    (cutting it flips verdicts = accuracy loss).
  - Free-threaded Python (3.13 exp / 3.14 supported, opt-in no-GIL build): risky - our
    C-extension stack (torch, asyncpg, trafilatura) isn't fully free-threading certified;
    importing one uncertified extension silently RE-ENABLES the GIL for the whole process.
    Likely zero gain on an experimental runtime. Declined.
  - Process pool for splitting: separate processes = separate GILs = real parallelism, but
    IPC overhead (serialize text to workers + back) for ~couple seconds on one stage.
    Disproportionate for a single-process app.
  - Queue + stateless worker processes: the CORRECT fix (each worker own process/GIL =
    true parallelism, also enables multi-GPU). It's a rearchitecture, out of wrap-up scope,
    DOCUMENTED as the horizontal scale path.

### 5. Lock wait (small, a consequence)
Each claim's 2 model calls acquire _MODEL_LOCK; sometimes wait behind another's forward pass.
Capped by: how long the holder is inside (~1.2s GPU). Small because GPU work is small.
Was the dominant cost BEFORE batching (22 queuing visits); now a footnote (2 visits).

## Why latency still climbs to ~20s at 9 concurrent
Not because any stage is broken. Because the system currently accepts UNLIMITED concurrent
work, so everyone degrades together. The fix is NOT speed - it's ADMISSION CONTROL
(backpressure): cap concurrency at ~3 (where latency is good), queue the rest with a
visible position via the existing poll mechanism, 429 past a bounded queue depth. Converts
"everyone degrades to 20s+" into "admitted requests stay fast, excess handled honestly."
Plus documented horizontal path: queue + workers + one GPU per worker.

## Optimization journey (the arc)
184s (CPU inference) -> GPU deploy -> 3 batching rounds (24.3 -> 21.2 -> 16.7 -> 15.9 at 5c)
-> 150-claim source-utility study (REJECTED cutting sources, breadth is load-bearing)
-> 8-vCPU right-size (confirmed CPU contention was C-level, exposed GIL-bound Python as floor)
-> diagnosis: bottleneck is external API latency + GIL-bound Python, GPU near-idle
-> response: bounded admission control, documented queue+workers for horizontal scale.
