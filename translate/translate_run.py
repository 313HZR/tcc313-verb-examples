#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TCC313 pt/nl Example Translator — same proven method as gen_examples6.py.
Translates EXISTING example sentences (already in lb/fr/de/en) into Portuguese (pt)
and Dutch (nl), via your local Claude Code CLI (`claude -p`). No API key. Resumable.

RUN (PowerShell, inside this `translate` folder):
    python translate_run.py --input verb_examples_input.json.gz --output verb_examples_ptnl.json --model sonnet --conc 3
    python translate_run.py --input dict_examples_input.json.gz --output dict_examples_ptnl.json --model sonnet --conc 3
    $env:TCC_MOCK=1; python translate_run.py --input dict_examples_input.json.gz --output x.json --limit 3   # dry run

Each "unit" is one call to Claude. Output is written after every few units and is
resumable: re-running skips units already complete in the output file.
"""
import os, sys, json, gzip, time, subprocess, threading, argparse, shutil, re
from concurrent.futures import ThreadPoolExecutor

PERS={"1s":"I","2s":"you (singular)","3s":"he/she","1p":"we","2p":"you (plural)","3p":"they"}
TENSE={"present":"simple present","perfect":"present perfect (have done)","past":"simple past (did)",
       "imperfect":"past continuous / used to","pluperfect":"past perfect (had done)","future":"future (will do)",
       "conditional":"conditional (would do)","conditional_perfect":"conditional perfect (would have done)",
       "subjunctive":"present subjunctive"}

SYS=(
 "You are a professional translator for a Luxembourgish language-learning product used by the "
 "Institut National des Langues (INL). You translate short example sentences into Portuguese (pt) "
 "and Dutch (nl).\n"
 "You are given sentences that ALREADY exist in Luxembourgish (lb) with reference translations in "
 "English (en), German (de) and French (fr). Use ALL of them to get the exact meaning, then write a "
 "natural, grammatically perfect translation into European Portuguese (pt) and standard Dutch (nl).\n"
 "Rules: keep the SAME meaning, tense and grammatical person as the source. Natural everyday wording, "
 "not word-for-word. Keep the same object/context. No quotes inside values, no notes, no extra keys.\n"
 "Return ONLY a JSON object mapping each item's \"k\" to {\"pt\":\"...\",\"nl\":\"...\"}. Nothing else."
)

_lock=threading.Lock(); _out={}

def load_input(path):
    op=gzip.open if path.endswith(".gz") else open
    return json.load(op(path,"rt",encoding="utf-8"))

def load_done(path):
    if os.path.exists(path):
        try: return json.load(open(path,encoding="utf-8")) or {}
        except Exception: return {}
    return {}

def save(path):
    tmp=path+".tmp"; json.dump(_out,open(tmp,"w",encoding="utf-8"),ensure_ascii=False); os.replace(tmp,path)

def unit_done(unit):
    for it in unit["items"]:
        c=_out.get(it["k"])
        if not isinstance(c,dict) or not str(c.get("pt","")).strip() or not str(c.get("nl","")).strip():
            return False
    return True

def obj_from_text(t):
    if "```" in t:
        m=re.search(r"```(?:json)?\s*([\s\S]*?)```",t)
        if m: t=m.group(1)
    d=0; st=-1
    for i,ch in enumerate(t):
        if ch=="{":
            if d==0: st=i
            d+=1
        elif ch=="}":
            d-=1
            if d==0 and st>=0:
                try: return json.loads(t[st:i+1])
                except Exception: pass
    return None

def build_prompt(unit):
    lines=[]
    for it in unit["items"]:
        tag=""
        if it.get("t"): tag=" ["+PERS.get(it.get("p"),it.get("p",""))+", "+TENSE.get(it["t"],it["t"])+"]"
        lines.append(json.dumps({"k":it["k"],"lb":it.get("lb",""),"en":it.get("en",""),
                                 "de":it.get("de",""),"fr":it.get("fr","")},ensure_ascii=False)+tag)
    return SYS+"\n\nTranslate these items to pt and nl. Return JSON { k: {pt, nl} } for EVERY k:\n"+"\n".join(lines)

def call_claude(unit, model, timeout=300):
    if os.environ.get("TCC_MOCK"):
        return {it["k"]:{"pt":"[pt] "+it.get("lb",""),"nl":"[nl] "+it.get("lb","")} for it in unit["items"]}
    prompt=build_prompt(unit)
    exe=shutil.which("claude") or "claude"
    args=[exe,"-p",prompt,"--output-format","json","--max-turns","1"]
    if model: args+=["--model",model]
    r=subprocess.run(args,capture_output=True,text=True,encoding="utf-8",timeout=timeout)
    if r.returncode!=0: raise RuntimeError("claude exit %s: %s"%(r.returncode,(r.stderr or r.stdout or "")[:160]))
    out=(r.stdout or "").strip()
    try:
        env=json.loads(out); txt=env.get("result") or env.get("content") or ""
        if env.get("is_error"): raise RuntimeError("is_error")
    except json.JSONDecodeError: txt=out
    return obj_from_text(txt)

def process(unit, model):
    for attempt in range(4):
        try:
            o=call_claude(unit,model)
            if isinstance(o,dict):
                good=True
                for it in unit["items"]:
                    c=o.get(it["k"])
                    if not isinstance(c,dict) or not str(c.get("pt","")).strip() or not str(c.get("nl","")).strip():
                        good=False; break
                if good:
                    with _lock:
                        for it in unit["items"]:
                            c=o[it["k"]]; _out[it["k"]]={"pt":c["pt"].strip(),"nl":c["nl"].strip()}
                    return True
        except Exception as e:
            sys.stderr.write("  %s: %s\n"%(unit["id"],str(e)[:120]))
        time.sleep(min(90,5*(2**attempt)))
    return False

def main():
    global _out
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--model",default=os.environ.get("TCC_MODEL","sonnet"))
    ap.add_argument("--conc",type=int,default=int(os.environ.get("TCC_CONC","3")))
    ap.add_argument("--limit",type=int,default=int(os.environ.get("TCC_LIMIT","0")))
    a=ap.parse_args()
    if not os.environ.get("TCC_MOCK"):
        try:
            vr=subprocess.run([shutil.which("claude") or "claude","--version"],capture_output=True,text=True,timeout=30)
            print("claude:",(vr.stdout or vr.stderr or "").strip()[:60])
        except Exception as e:
            print("ERROR: cannot run `claude`. Open PowerShell where Claude Code works, then re-run.\n ",e); return
    data=load_input(a.input); units=data["units"]
    _out=load_done(a.output)
    todo=[u for u in units if not unit_done(u)]
    if a.limit: todo=todo[:a.limit]
    print("units=%d  done=%d  to-do=%d  model=%s  parallel=%d  -> %s"%(
          len(units),len(units)-len(todo),len(todo),a.model,a.conc,a.output))
    n=0; t0=time.time()
    with ThreadPoolExecutor(max_workers=a.conc) as ex:
        futs=[ex.submit(process,u,a.model) for u in todo]
        for f in futs:
            f.result(); n+=1
            if n%5==0:
                with _lock: save(a.output)
                el=time.time()-t0
                print("  %d/%d  (%.1f u/min)"%(n,len(todo),n/el*60 if el else 0))
    with _lock: save(a.output)
    filled=len(_out)
    print("DONE. items translated: %d  -> %s"%(filled,a.output))

if __name__=="__main__": main()
