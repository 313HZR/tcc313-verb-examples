#!/usr/bin/env python3
# Deterministic driver for the es/it/ar EXAMPLE translation job.
# It does ALL the bookkeeping (chunking, resume, merge) so the orchestrating
# agent never has to hold the big files in context. The agent only:
#   1) run:  python examples_run.py emit <job> <nchunks> <units_per_chunk>
#   2) dispatch one Haiku sub-agent per emitted chunk file (translate -> write .out.json)
#   3) run:  python examples_run.py merge <job>        # folds results + reports
#   4) git add -A && git commit && git push ; repeat until status shows remaining 0
#
# job = "verb"  -> ../verb_examples_input.json.gz  -> verb_examples_esitar.json
# job = "dict"  -> ../dict_examples_input.json.gz  -> dict_examples_esitar.json
#
# Output format (both jobs):  { "<k>": {"es":"","it":"","ar":""}, ... }
import json, gzip, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "_work")
JOBS = {
    "verb": (os.path.join(HERE, "..", "verb_examples_input.json.gz"),
             os.path.join(HERE, "verb_examples_esitar.json")),
    "dict": (os.path.join(HERE, "..", "dict_examples_input.json.gz"),
             os.path.join(HERE, "dict_examples_esitar.json")),
}

def load_input(job):
    return json.load(gzip.open(JOBS[job][0]))["units"]

def load_output(job):
    p = JOBS[job][1]
    if os.path.exists(p):
        try: return json.load(open(p, encoding="utf-8"))
        except Exception: return {}
    return {}

def done_key(out, k):
    v = out.get(k)
    return bool(v) and bool(v.get("es")) and bool(v.get("it")) and bool(v.get("ar"))

def pending_units(job):
    units = load_input(job); out = load_output(job)
    pend = []
    for u in units:
        if any(not done_key(out, it["k"]) for it in u["items"]):
            pend.append(u)
    return units, out, pend

def cmd_status(job=None):
    for j in ([job] if job else ["verb", "dict"]):
        units, out, pend = pending_units(j)
        total = sum(len(u["items"]) for u in units)
        done  = sum(1 for u in units for it in u["items"] if done_key(out, it["k"]))
        print(f"[{j}] units: {len(pend)} pending / {len(units)} total | "
              f"cells: {done}/{total} done ({100*done//max(total,1)}%) | remaining {total-done}")

def cmd_emit(job, nchunks, upc):
    nchunks = int(nchunks); upc = int(upc)
    _, _, pend = pending_units(job)
    os.makedirs(WORK, exist_ok=True)
    # clear old chunk files for this job
    for f in glob.glob(os.path.join(WORK, f"{job}_chunk_*.json")): os.remove(f)
    take = pend[: nchunks * upc]
    if not take:
        print("NOTHING_PENDING"); return
    chunks = [take[i:i+upc] for i in range(0, len(take), upc)]
    emitted = []
    for i, ch in enumerate(chunks):
        rows = []
        for u in ch:
            for it in u["items"]:
                rows.append({"k": it["k"], "lb": it.get("lb",""), "en": it.get("en",""),
                             "de": it.get("de",""), "fr": it.get("fr","")})
        inp = os.path.join(WORK, f"{job}_chunk_{i:02d}.json")
        outp = os.path.join(WORK, f"{job}_chunk_{i:02d}.out.json")
        json.dump({"out": outp, "rows": rows}, open(inp,"w",encoding="utf-8"), ensure_ascii=False)
        emitted.append((inp, outp, len(rows)))
    print(f"EMITTED {len(emitted)} chunks for job={job} "
          f"({sum(e[2] for e in emitted)} cells, {sum(e[2] for e in emitted)*3} translations)")
    for inp, outp, n in emitted:
        print(f"  CHUNK in={inp}  out={outp}  cells={n}")

def cmd_merge(job):
    out = load_output(job); added = 0
    for f in sorted(glob.glob(os.path.join(WORK, f"{job}_chunk_*.out.json"))):
        try: res = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print("  SKIP bad", os.path.basename(f), e); continue
        for k, v in res.items():
            if isinstance(v, dict) and v.get("es") and v.get("it") and v.get("ar"):
                out[k] = {"es": v["es"], "it": v["it"], "ar": v["ar"]}; added += 1
    json.dump(out, open(JOBS[job][1],"w",encoding="utf-8"), ensure_ascii=False)
    # clean processed chunk + out files
    for f in glob.glob(os.path.join(WORK, f"{job}_chunk_*")): os.remove(f)
    print(f"MERGED job={job} added/updated {added} cells -> {os.path.basename(JOBS[job][1])}")
    cmd_status(job)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: cmd_status(); sys.exit()
    c = a[0]
    if c == "status": cmd_status(a[1] if len(a)>1 else None)
    elif c == "emit":  cmd_emit(a[1], a[2], a[3])
    elif c == "merge": cmd_merge(a[1])
    elif c == "clean":
        import shutil; shutil.rmtree(WORK, ignore_errors=True); print("cleaned _work")
    else: print("usage: status | emit <job> <nchunks> <units_per_chunk> | merge <job> | clean")
