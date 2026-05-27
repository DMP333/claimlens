# Phase 1 Implementation Validation
Generated: 2026-05-25 17:23:33

## Test 1: Claim Classifier
Type accuracy: 19/19
Domain accuracy: 19/19

## Test 2: Source Routing
Routing correct: 9/12

## Test 3: Dedup
Before: 6, After: 3
  FAIL: URL dedup keeps higher priority
  PASS: Unique source survives

## Test 4: FC Bypass vs Raw NLI
Bypass accuracy: 17/22
Raw NLI accuracy: 29/54
Improvement: +23.6pp

## Test 5: Enrichment Impact
Original snippet accuracy: 29/74
Enriched snippet accuracy: 24/74
Improvement: -6.8pp
Individual: 9 improved, 14 regressed

## Test 6: Extract Scores
FC: 30 scored, DDG: 18 scored, Wiki: 15 scored
