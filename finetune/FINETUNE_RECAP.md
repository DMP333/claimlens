# Project A — Stance Model Fine-Tuning: Full Recap

DeBERTa NLI stance model for the ClaimLens / Evidence Intelligence pipeline.
Goal: improve **sentence-level stance accuracy** (supporting / neutral / opposing)
enough to be a defensible resume metric, measured before vs after on a frozen,
held-out test set.

**Final result (sealed test, 7,452 sentences): macro-F1 0.66 -> 0.80, accuracy 84% -> 89%.**

---

## 1. Where we started

- **Base model:** `MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli` (184M params).
- **Task framing:** premise = source sentence, hypothesis = claim (identical to the
  live pipeline). Labels: supporting = 0, neutral = 1, opposing = 2.
- **Data (all frozen):** 100 train claims / 50 held-out test claims, split by claim
  (no claim overlap). Inner split: 80 train / 20 dev claims. Labels are SILVER
  (LLM teacher, ~84% reliable). Class mix is ~80% neutral — heavily imbalanced.
- **Baseline (untuned small base):** test macro-F1 0.6146; dev warm-start 0.6555.
  Weakness: timid — hedges to neutral, missing ~45% of supporting and ~48% of opposing.

---

## 2. The problem: training kept destroying the model

Every attempt at standard full fine-tuning collapsed — the model stopped reading the
input and predicted a single class for everything, flat from epoch 1. Diagnosed in layers:

1. **Mixed precision (bf16) masked a bug.** First runs collapsed under bf16. Switching
   to full fp32 was necessary but exposed the next layer.
2. **A dtype bug in the loss.** Loss computed across mixed dtypes; fixed by computing it in fp32.
3. **Numerical divergence.** In clean fp32 the loss went to `NaN` in epoch 1 — weights
   exploding because the training steps were too violent.
4. **Majority-class collapse.** Once stabilized, full fine-tuning still collapsed: with
   balanced data it thrashed between constant-class solutions (all-neutral -> all-opposing).
   Root cause: full fine-tuning yanks all 184M weights at once and overwrites the good
   pretrained features instantly.

Key insight: the base model is healthy before training; **training itself was the
destroyer**, not the data or the idea.

---

## 3. The breakthroughs, in order

| # | Change | What it fixed | Dev macro-F1 |
|---|--------|---------------|--------------|
| 0 | Untuned small base | — (starting line) | 0.6555 |
| 1 | **fp32 + warmup 0.10 + grad clip + adam eps 1e-6** | Killed NaN divergence | (stable, full FT still degenerate) |
| 2 | **LoRA (freeze base, train adapters)** | Killed the collapse — frozen base can't be destroyed | 0.7256 |
| 3 | **Bigger base: DeBERTa-v3-LARGE NLI** | Raised the model ceiling — biggest single jump | 0.7826 |
| 4 | **Longer context: max_len 128 -> 256** | Truncation was costing stance signal | **0.7957** |

The decisive shifts were #2 (LoRA over full fine-tuning) for stability and #3 (large base)
for ceiling. #4 was the final squeeze.

---

## 4. What did NOT help (tested, ruled out)

- Class weights to out-muscle imbalance (`effnum`, `sqrt`, `4,1,4`): collapsed or barely moved.
- Oversample + strong weights (`over_sqrt`): over-corrected to all-supporting.
- Broad LoRA targets (all dense layers): more capacity just overfit faster.
- Lower LR on large (1e-4): smoother but lower headline.
- Even longer context (max_len 384): no gain over 256.
- Careful full fine-tune with frozen lower layers (small base): capped at small-base ceiling (~0.72).

---

## 5. The final model — every parameter and why

**Config:** `large_len256` — dev macro-F1 0.7957 (peaked epoch 2).

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Base model | `deberta-v3-large-mnli-fever-anli-ling-wanli` | Stronger NLI model — model size was the ceiling |
| Arch | LoRA | Freezes the base so it can't collapse; trains a small correction |
| LoRA rank / alpha / dropout | 32 / 32 / 0.1 | Adapter capacity + scaling + regularization |
| LoRA targets | q/k/v only | Attention projections; adding dense layers overfit |
| Loss | plain cross-entropy | With balanced data, class weights are redundant and over-tip |
| Balance | oversample | Equalizes class counts so the model can't collapse to the majority |
| Learning rate | 2e-4 | LoRA adapters start from scratch and need a higher LR than full FT |
| Batch size | 16 | Fits the large model in fp32 on a 24GB GPU |
| Epochs | best at 2 (cap 3-4) | Overfits after epoch 2 (eval loss rises) |
| Max length | 256 | More context; 128 truncated and lost stance cues |
| Precision | fp32 (`AMP=0`) | DeBERTa-v3 is unstable in mixed precision |
| Warmup ratio | 0.10 | Eases LR in so early steps don't blow up the model |
| Grad clip | 1.0 | Hard ceiling on any single step — anti-divergence |
| Adam epsilon | 1e-6 | Numerical stability for this fragile model |
| NaN-stop guard | on | Aborts instantly if loss goes NaN |

---

## 6. Final results — sealed test set (scored ONCE)

Test set: 50 held-out claims, 7,452 sentences. Metric: macro-F1 against silver
(LLM-validated) labels. Before and after use identical labels, so silver noise cancels
in the delta.

| | macro-F1 | accuracy | supporting R | opposing R |
|---|---|---|---|---|
| BEFORE — large base, untuned | 0.6593 | 83.67% | 0.465 | 0.498 |
| AFTER — large + LoRA (seed 42) | 0.7941 | 88.86% | 0.777 | 0.717 |
| AFTER — large + LoRA (seed 1) | 0.7981 | 89.18% | 0.761 | 0.728 |
| AFTER — large + LoRA (seed 2) | 0.7981 | 89.13% | 0.799 | 0.711 |
| **AFTER — mean of 3 seeds** | **0.797** (+/-0.002) | **89.06%** | **0.779** | **0.719** |
| **DELTA (fine-tuning gain)** | **+0.137** | **+5.4 pts** | **+0.31** | **+0.22** |

Per-class F1 (before -> after mean): supporting 0.503 -> 0.735, opposing 0.571 -> 0.721,
neutral 0.904 -> 0.934. Both precision AND recall rose for the stance classes
(supporting precision 0.55 -> 0.71), so this is a genuinely better model, not recall inflation.

Validation quality: dev and test agree closely (seed 42 scored 0.7957 dev / 0.7941 test),
and the three seeds cluster within 0.004 on test — dev was not optimistic, test confirmed it.

Context: small-base untuned was 0.6146, so the full "upgraded base + fine-tuned" arc is
0.61 -> 0.80; the clean within-base fine-tuning delta is 0.66 -> 0.80.

---

## 7. Discipline maintained

- **Test sealed:** all selection on dev; test scored once at the end.
- **Anti-overfitting:** no fix derived from test; mechanisms designed to generalize.
- **Sweep capped:** stopped deliberately to avoid inflating the dev-best by chance.
- **Seeds on the winner:** 3 seeds confirm it's not a lucky draw.
- **Honest labels:** results reported as macro-F1 vs silver labels; the delta is the robust part.

---

## 8. Status and next step

- Fine-tuning: **DONE.** Final model = `large_len256` LoRA adapter on DeBERTa-v3-large NLI.
- Next: integrate the adapter into `nli_service` (max_len 256), verify it reproduces ~0.797
  on these sentences (catches integration bugs), then optionally measure the end-to-end
  verdict-level lift as a second, complementary number.