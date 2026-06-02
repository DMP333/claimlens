"""
Comprehensive Pre-Fine-Tuning Analysis (v2)

Two modes:
  1. If data/unified_dataset.json exists (from collect_fresh_baseline.py): uses it directly
  2. Otherwise: builds from old decision2_3_data.json + validation_data.json

Run from project root: python analysis/run_comprehensive_analysis.py
"""

import json, csv, os, sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
DATA_DIR.mkdir(exist_ok=True)
ANALYSIS_DIR.mkdir(exist_ok=True)

UNIFIED_PATH = DATA_DIR / "unified_dataset.json"

if UNIFIED_PATH.exists():
    print(f"Loading: {UNIFIED_PATH}")
    with open(UNIFIED_PATH) as f:
        unified = json.load(f)
else:
    print("ERROR: data/unified_dataset.json not found.")
    print("Run collect_fresh_baseline.py first to generate it.")
    sys.exit(1)

total_claims = len(unified)
total_sources = sum(len(c['sources']) for c in unified)
total_sents = sum(sum(len(s.get('sentences',[])) for s in c['sources']) for c in unified)
print(f"Loaded: {total_claims} claims, {total_sources} sources, {total_sents} sentences\n")

# ============================================================
# PATTERN FLAGS
# ============================================================
NEG_WORDS = {'not','no','never','neither','cannot',"don't","doesn't","isn't","aren't","wasn't","weren't","won't","can't","couldn't","shouldn't","wouldn't"}
HEDGE = ['no evidence','failed to','not supported','no significant','not been shown','no proof','no link','insufficient evidence','lacks evidence','unsubstantiated','debunked','disproven','refuted','not true','not accurate','false claim','no basis','no credible','not established']
MYTH = ['claim that','claims that','myth that','theory that','belief that','notion that','idea that','legend','misconception','commonly believed','popular belief','widely believed','often said','often claimed']

def has_neg(t): return any(w in t.lower().split() for w in NEG_WORDS)
def has_q(t): return any(c in t for c in ['"','\u201c','\u201d',"'"])
def has_h(t): return any(p in t.lower() for p in HEDGE)
def has_m(t): return any(p in t.lower() for p in MYTH)
def claim_neg(c): return any(w in c.lower().split() for w in ['not','no','never','neither','cannot'])

# ============================================================
# LEVEL 1: CLAIM SUMMARY
# ============================================================
claim_rows = []
for co in unified:
    ld = Counter(); hc = Counter(); mm = 0; tj = 0
    for src in co['sources']:
        exp = src.get('expected_stance','')
        for s in src.get('sentences',[]):
            l = s.get('label');
            if not l: continue
            ld[l] += 1
            if s.get('confidence',0) > 0.8: hc[l] += 1
            if exp in ('supporting','opposing'):
                tj += 1
                if (exp=='opposing' and l=='supporting') or (exp=='supporting' and l=='opposing'): mm += 1
    ss = Counter(s.get('expected_stance','?') for s in co['sources'])
    claim_rows.append({
        'claim': co['claim'], 'category': co['category'], 'expected_verdict': co['expected_verdict'],
        'num_sources': len(co['sources']),
        'num_sentences': sum(len(s.get('sentences',[])) for s in co['sources']),
        'sent_supporting': ld.get('supporting',0), 'sent_neutral': ld.get('neutral',0), 'sent_opposing': ld.get('opposing',0),
        'hc_supporting': hc.get('supporting',0), 'hc_neutral': hc.get('neutral',0), 'hc_opposing': hc.get('opposing',0),
        'source_supporting': ss.get('supporting',0), 'source_opposing': ss.get('opposing',0),
        'source_mixed': ss.get('mixed',0)+ss.get('neutral',0),
        'judgeable_sents': tj, 'mismatches': mm,
        'mismatch_rate_pct': round(mm/tj*100,1) if tj else 0,
    })
claim_rows.sort(key=lambda r: r['mismatch_rate_pct'], reverse=True)
with open(ANALYSIS_DIR/'01_claim_summary.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=claim_rows[0].keys()); w.writeheader(); w.writerows(claim_rows)
print(f"01_claim_summary.csv: {len(claim_rows)} claims")

# ============================================================
# LEVEL 2: SOURCE SUMMARY
# ============================================================
source_rows = []
for co in unified:
    for src in co['sources']:
        sents = src.get('sentences',[]); exp = src.get('expected_stance','?')
        ld = Counter(s.get('label') for s in sents if s.get('label'))
        dom = ld.most_common(1)[0][0] if ld else 'none'
        mm=0; wc=0; wt=''
        for s in sents:
            l=s.get('label')
            if not l: continue
            is_mm = (exp=='opposing' and l=='supporting') or (exp=='supporting' and l=='opposing')
            if is_mm:
                mm+=1
                if s.get('confidence',0)>wc: wc=s['confidence']; wt=s.get('text','')[:100]
        tot=len([s for s in sents if s.get('label')])
        source_rows.append({
            'claim':co['claim'],'category':co['category'],'title':src.get('title','')[:80],
            'source_type':src.get('source_type',''),'expected_stance':exp,
            'num_sentences':tot,'sent_supporting':ld.get('supporting',0),
            'sent_neutral':ld.get('neutral',0),'sent_opposing':ld.get('opposing',0),
            'dominant_label':dom,'mismatches':mm,
            'mismatch_rate_pct':round(mm/tot*100,1) if tot else 0,
            'worst_mismatch_conf':round(wc,3),'worst_mismatch_text':wt,
        })
source_rows.sort(key=lambda r: r['mismatch_rate_pct'], reverse=True)
with open(ANALYSIS_DIR/'02_source_summary.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=source_rows[0].keys()); w.writeheader(); w.writerows(source_rows)
print(f"02_source_summary.csv: {len(source_rows)} sources")

# ============================================================
# LEVEL 3: EVERY SENTENCE
# ============================================================
sent_rows = []
for co in unified:
    cl=co['claim']; cat=co['category']
    for src in co['sources']:
        exp=src.get('expected_stance','?'); sents=src.get('sentences',[])
        ti=src.get('title','')[:60]; st=src.get('source_type','')
        for i,s in enumerate(sents):
            l=s.get('label');
            if not l: continue
            txt=s.get('text','')
            is_mm=False; mt=''
            if exp in ('supporting','opposing'):
                if exp=='opposing' and l=='supporting': is_mm=True; mt='supp_in_opp_source'
                elif exp=='supporting' and l=='opposing': is_mm=True; mt='opp_in_supp_source'
                elif exp=='opposing' and l=='neutral': mt='neut_in_opp_source'
                elif exp=='supporting' and l=='neutral': mt='neut_in_supp_source'
                else: mt='correct'
            else: mt='unjudgeable'
            pl=sents[i-1].get('label','') if i>0 else ''
            nl=sents[i+1].get('label','') if i<len(sents)-1 else ''
            sent_rows.append({
                'claim':cl,'category':cat,'source_title':ti,'source_type':st,
                'expected_stance':exp,'sent_index':i,'text':txt[:200],
                'word_count':len(txt.split()),'label':l,
                'confidence':round(s.get('confidence',0),4),
                'p_supp':round(s.get('p_supp',0),4),'p_neut':round(s.get('p_neut',0),4),
                'p_opp':round(s.get('p_opp',0),4),'mismatch_type':mt,'is_hard_mismatch':is_mm,
                'prev_label':pl,'next_label':nl,
                'has_negation':has_neg(txt),'has_quotes':has_q(txt),
                'has_hedge':has_h(txt),'has_myth_cue':has_m(txt),
                'claim_has_negation':claim_neg(cl),
            })

with open(ANALYSIS_DIR/'03_all_sentences.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=sent_rows[0].keys()); w.writeheader(); w.writerows(sent_rows)
print(f"03_all_sentences.csv: {len(sent_rows)} sentences")

hard_mm=[r for r in sent_rows if r['is_hard_mismatch']]
hard_mm.sort(key=lambda r: r['confidence'], reverse=True)
with open(ANALYSIS_DIR/'04_hard_mismatches.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=hard_mm[0].keys()); w.writeheader(); w.writerows(hard_mm)
print(f"04_hard_mismatches.csv: {len(hard_mm)} hard mismatches")

weak=[r for r in sent_rows if r['mismatch_type']=='neut_in_opp_source' and r['has_hedge']]
if weak:
    weak.sort(key=lambda r: float(r['p_opp']), reverse=True)
    with open(ANALYSIS_DIR/'05_potential_weak_negation.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=weak[0].keys()); w.writeheader(); w.writerows(weak)
print(f"05_potential_weak_negation.csv: {len(weak)} potential weak negation")

correct=[r for r in sent_rows if r['mismatch_type']=='correct']
correct.sort(key=lambda r: r['confidence'], reverse=True)
with open(ANALYSIS_DIR/'06_correct_sentences.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=correct[0].keys()); w.writeheader(); w.writerows(correct)
print(f"06_correct_sentences.csv: {len(correct)} correctly classified")

# ============================================================
# BASELINE SUMMARY
# ============================================================
jdg=[r for r in sent_rows if r['mismatch_type']!='unjudgeable']
neut_j=[r for r in sent_rows if r['mismatch_type'] in ('neut_in_opp_source','neut_in_supp_source')]
sio=[r for r in hard_mm if r['mismatch_type']=='supp_in_opp_source']
ois=[r for r in hard_mm if r['mismatch_type']=='opp_in_supp_source']

lines=[]
def p(l=''):
    print(l); lines.append(l)

p("="*70); p("PRE-FINE-TUNING BASELINE REPORT"); p("="*70); p()
p(f"Data: {total_claims} claims, {total_sources} sources, {total_sents} sentences")
p(f"Judgeable sentences: {len(jdg)}"); p()
p("SENTENCE CLASSIFICATION:")
p(f"  Correct:      {len(correct):5d} / {len(jdg)} ({len(correct)/len(jdg)*100:.1f}%)")
p(f"  Neutral:      {len(neut_j):5d} / {len(jdg)} ({len(neut_j)/len(jdg)*100:.1f}%)")
p(f"  Hard mismatch:  {len(hard_mm):5d} / {len(jdg)} ({len(hard_mm)/len(jdg)*100:.1f}%)")
p()
p(f"HARD MISMATCHES: {len(hard_mm)} total")
p(f"  Supporting-in-opposing: {len(sio)} across {len(Counter(r['claim'] for r in sio))} claims")
p(f"  Opposing-in-supporting: {len(ois)} across {len(Counter(r['claim'] for r in ois))} claims")
p()
p("SUPP-IN-OPP by claim:")
for c,n in Counter(r['claim'] for r in sio).most_common():
    p(f"  {n:3d} | {c}")
p()
p("OPP-IN-SUPP by claim:")
for c,n in Counter(r['claim'] for r in ois).most_common():
    p(f"  {n:3d} | {c}")
p()
for desc,sub in [('Supp-in-opp',sio),('Opp-in-supp',ois)]:
    p(f"{desc} ({len(sub)}):")
    p(f"  negation_in_text: {sum(1 for r in sub if r['has_negation'])}")
    p(f"  quotes: {sum(1 for r in sub if r['has_quotes'])}")
    p(f"  hedge: {sum(1 for r in sub if r['has_hedge'])}")
    p(f"  myth_cue: {sum(1 for r in sub if r['has_myth_cue'])}")
    p(f"  claim_negation: {sum(1 for r in sub if r['claim_has_negation'])}")
    confs=[r['confidence'] for r in sub]
    p(f"  avg_conf: {sum(confs)/len(confs):.3f}, >0.8: {sum(1 for c in confs if c>0.8)}")
    p()
p(f"WEAK NEGATION: {len(weak)}")
p()
p("SOURCE TYPE MISMATCH RATES:")
for st in ['fact_check','encyclopedia','web','academic']:
    js=[r for r in source_rows if r['expected_stance'] in ('supporting','opposing') and r['source_type']==st]
    if js:
        ts=sum(r['num_sentences'] for r in js); tm=sum(r['mismatches'] for r in js)
        p(f"  {st}: {tm}/{ts} = {tm/ts*100:.1f}% ({len(js)} sources)")
p()
p(f"CORRECT: {len(correct)} (high-conf: {sum(1 for r in correct if r['confidence']>0.8)})")
cl=Counter(r['label'] for r in correct)
p(f"  By label: {dict(cl)}")
p(); p("="*70)
p("These are BASELINE numbers. Fine-tuning improvement measured against these.")
p("="*70)

with open(ANALYSIS_DIR/'baseline_summary.txt','w') as f:
    f.write('\n'.join(lines))
print(f"\nbaseline_summary.txt saved. Done.")