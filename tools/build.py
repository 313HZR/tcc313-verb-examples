# -*- coding: utf-8 -*-
"""Usage: python3 tools/build.py specs/specs_XX.py [--show N]
Loads a spec module (defines S = Specs()), builds + lints every verb, prints problems.
With --merge, writes the built verbs into examples6_remaining.json (only lint-clean ones)."""
import sys, json, re, importlib.util, os
sys.path.insert(0, os.path.dirname(__file__))
from vlib import *

def load(path):
    spec = importlib.util.spec_from_file_location("specmod", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.S.items

def lint(vid, entry):
    probs = []
    for t in TENSES:
        for p in PERS:
            for l in LANGS:
                s = entry[t][p][l]
                if not isinstance(s, str) or not s.strip():
                    probs.append((t, p, l, "empty")); continue
                if "  " in s or s != s.strip(): probs.append((t, p, l, "spacing: " + s))
                if "{" in s or "}" in s: probs.append((t, p, l, "unreplaced token: " + s))
                if not s.endswith("."): probs.append((t, p, l, "no final period: " + s))
                if l == "fa" and re.search(r"[A-Za-z]", s): probs.append((t, p, l, "latin in fa: " + s))
                if l != "fa" and re.search(r"[؀-ۿ]", s): probs.append((t, p, l, "persian in non-fa: " + s))
    return probs

if __name__ == "__main__":
    path = sys.argv[1]
    items = load(path)
    ids = [v for v, _ in items]
    print(f"{len(items)} verbs in {path}")
    dup = {v for v in ids if ids.count(v) > 1}
    if dup: print("DUPLICATE ids:", dup)
    built = {}
    bad = 0
    for vid, spec in items:
        try:
            e = assemble(vid, spec)
        except Exception as ex:
            print("BUILD ERROR", vid, repr(ex)); bad += 1; continue
        pr = lint(vid, e)
        if pr:
            bad += 1
            print("LINT", vid, pr[:4])
        else:
            built[vid] = e
    print(f"clean: {len(built)}  problems: {bad}")
    if "--chunk" in sys.argv:
        want = [x["id"] for x in json.load(open(sys.argv[sys.argv.index("--chunk") + 1], encoding="utf-8"))]
        print("MISSING from specs:", [w for w in want if w not in ids] or "none")
        print("EXTRA/unknown ids:", [w for w in ids if w not in want] or "none")
    if "--show" in sys.argv:
        n = int(sys.argv[sys.argv.index("--show") + 1])
        for vid in list(built)[:n]:
            print("==", vid)
            for t in TENSES:
                for p in ["1s", "3s", "2p"]:
                    c = built[vid][t][p]
                    print(f" {t:20}{p}", " | ".join(c[l] for l in LANGS))
    if "--merge" in sys.argv:
        out = "examples6_remaining.json"
        data = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {"examples": {}}
        data["examples"].update(built)
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1); fh.write("\n")
        print("merged ->", out, "total verbs now", len(data["examples"]))
