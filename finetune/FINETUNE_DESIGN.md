# Project A -- Fine-Tune Design (FROZEN, rev 3)

Hand-off-grade design doc for the DeBERTa fine-tune. Carries the problem, the verified baseline,
every decision, the staged sweep, checkpoint safety, the diagnostic protocol, and the
defensibility rules. Working rules: brutally honest, no em-dashes / no double-hyphen, root-cause
over band-aids, surface problems immediately, never tune to the test set, test scored ONCE.

CHANGES IN REV 3: decision threshold DROPPED from the plan (optional five-minute add-on at the
very end only, if extra rigor is wanted; not load-bearing for the resume number). Dev split set to
exactly 80 inner-train / 20 dev.

---

## 0. Model and task (locked)

- Model: `MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli` (184M). Keep the 3-class head.
- Input = (premise = sentence, hypothesis = claim). IDENTICAL to `nli_service._run_nli_batch`.
- LABEL MAP (locked): supporting=0, neutral=1, opposing=2. (Aligns with the base head:
  entailment->supporting, neutral->neutral, contradiction->opposing.)
- Headline metric: macro-F1 + per-class recall. Overall accuracy near-dead (floor 79.46%); secondary.

---

## 1. The problem (verified BEFORE baseline, 7,452 test sentences)

- accuracy 81.11% (floor 79.46%); macro-F1 0.6146.
- supporting R0.414 / opposing R0.449 / neutral R0.909.
- confusion (rows=gold, cols=pred [supp,neut,opp]): supp[291,400,12] neut[131,5381,409] opp[48,408,372].
- DIAGNOSIS: the model FLATTENS stance to neutral (too timid). 57% of supporting and 49% of
  opposing get called neutral. Sign-flips tiny (60), so direction is known, commitment is missing.
- Fix: class-weighted / focal loss makes flattening expensive, forcing commitment. Favorable setup:
  the dominant error is the learnable kind. Gains expected in macro-F1 and stance recall, NOT in
  overall accuracy (neutral majority caps it).

---

## 2. Data foundation (frozen files, two-files-never-mix discipline)

- `train_split_labels.json` : 17,008 rows, 100 train claims, test-leakage-fixed. TRAIN-side only.
- `test_split_labels_HELDOUT.json` : 7,452 rows, 50 test claims. SCORED ONCE at the very end.
- `dev_split.json` : 80 inner-train claims + 20 dev claims (stratified by category, seed 42).
  inner-train 13,910 sents / dev 3,235 sents. Picks EVERY hyperparameter. Training script applies
  the premise-leakage fix between inner-train and dev.
- max_length = 128 (95th pct = 43 words; 0.22% exceed 128 tokens).

Protocol: selection on DEV only; the 50 test claims are touched once, at the end, via
`eval_baseline.py --model-dir <winner>`. Physical file separation is the guard.

---

## 3. Decision dispositions

HIGH leverage (sweep):
- D14 learning rate: TEST {1e-5, 2e-5, 3e-5, 5e-5}.
- D10/D11 loss + class weighting: TEST {plain CE, weighted-CE effnum, weighted-CE tuned, focal g=2}.
  The direct lever on flattening.
- D16 epochs: early stop on dev macro-F1, save per-epoch, cap 5, patience 2.

MEDIUM leverage (second wave):
- D15 batch size: TEST {16, 32, 64}, paired with LR.
- D2 data balance: TEST {as-is, undersample-neutral, oversample-stance}.
- D3 data scope: TEST {full, pattern-targeted} (added in wave 2 once the harness is validated).
- D8 architecture: TEST {full fine-tune, LoRA}.

LOW leverage (DEFAULT; reopen only if a diagnostic fingerprint points here):
- D17 warmup 0.06 ; D18 weight decay 0.01 ; D19 AdamW + grad-clip 1.0 + default dropout ;
  D6 max_length 128 ; D9 keep head ; D7 input format locked.

DROPPED (reopen only if forced):
- D23 decision threshold: NOT on the path. Optional 5-min add-on at the very end for extra rigor.
- D4 hard-category ablation (kept all in for legitimacy).
- D5 label-noise weighting (no teacher-confidence stored; reopen if supporting recall stalls).
- D13 label smoothing (helps 3K soft-probs, not the hard label; only if spare time).

MANDATORY (defensibility):
- D20 seeds: winner retrained x4-5 seeds; report mean + spread.
- D21 select on dev macro-F1. D22 test scored once.

---

## 4. Staged sweep (~16 training runs + 1 test run)

- Wave 1: LR {1e-5,2e-5,3e-5,5e-5} at batch 32, weighted-CE effnum (4 runs) -> at best LR, batch
  {16,64} (2 runs) -> at best LR/batch, loss {plain CE, tuned wts, focal} (3 runs). ~9 runs.
- Wave 2: best config -> data balance {undersample, oversample} (2) + full vs targeted (2). ~4 runs.
- Wave 3: best config full vs LoRA. 1 run.
- Wave 4: winner x4 seeds. 4 runs.
- Final: ONE test run via `eval_baseline.py --model-dir <winner>`; before/after deltas + CIs.

VALIDATE FIRST: run ONE config end-to-end (script runs, checkpoints land on the volume, dev metrics
log, resume works) BEFORE launching the sweep. De-risks everything.

Every run logs config + per-epoch dev metrics to a CSV. Pick best dev macro-F1; tie-break
within-noise finalists with a quick CV on those only.

---

## 5. Checkpoint safety (the Colab-loss lesson)

- Run on RunPod A100 (or RTX 4090) with a NETWORK VOLUME (persistent, survives pod death).
- Trainer: `save_strategy="epoch"`, `load_best_model_at_end=True`,
  `metric_for_best_model="macro_f1"`, `greater_is_better=True`, `save_total_limit=2`.
- `output_dir` on the Network Volume, NOT the pod local disk.
- `resume_from_checkpoint=True` so a crash costs at most one epoch.
- Save the best model to a named dir per run for the final test run.

---

## 6. Diagnostic protocol (a faltering run is NOT a guess)

Log PER EPOCH: train loss, dev loss, dev macro-F1, dev per-class recall (+ final confusion matrix).
Read against this fingerprint map; several fingerprints REOPEN a dropped decision:

| logs show | cause | reopen / adjust |
|---|---|---|
| train loss down, dev macro-F1 falls after epoch N | overfit silver noise | earlier stop; reopen D18/dropout; try LoRA |
| train & dev loss stuck high | underfit | raise LR; more epochs |
| loss spikes / NaN | LR too high | lower LR; confirm grad clip |
| neutral recall collapses, neutral->stance leak | weights too aggressive | soften weights / lower focal gamma |
| stance still flattening | weights too weak | stronger weights |
| predicts one class for everything | weight/LR collapse | lower LR; re-init |
| supporting recall stuck, opposing improves | teacher noise on supporting (ceiling) | REOPEN D5 or accept ceiling |
| oversample overfits, undersample underperforms | data-level balance wrong tool | prefer loss-level weighting |

One-variable-at-a-time sweep structure attributes cause (e.g. all high-LR runs diverge => LR).

---

## 7. Expectations (honest)

- macro-F1 and stance recall should rise (the resume win); overall accuracy flat or slightly down.
- supporting capped by teacher noise (was the 59% soft spot).
- aggressive weights crater opposing precision (already 0.469); macro-F1 punishes both directions.
- presupposition / causal-import categories will not be learned; expected ceiling.

---

## 8. Open TODOs

- [x] Split + freeze (train/test/dev 80/20). [x] Verified baseline.
- [ ] train.py: HF Trainer; weighted/focal loss; reads frozen splits; inner-train vs dev leakage
      fix; per-epoch diagnostic CSV; checkpoint to Network Volume; resume; LoRA option.
- [ ] Set up RunPod (pod + Network Volume); upload repo/data; install deps.
- [ ] VALIDATE one config end-to-end.
- [ ] Run Wave 1-3; log every run; pick best dev macro-F1.
- [ ] Wave 4 seeds on winner.
- [ ] ONE test run on winner; before/after deltas + CIs.
- [ ] (optional) source-level 3K from saved soft-probs; keyword baseline; threshold; label smoothing.

## Files in play
- eval_baseline.py (done) ; train.py (next) ; dev_split.json (data, 80/20) ;
  metrics_BEFORE_baseline.json (frozen baseline) ; train/test/dev split files (frozen).