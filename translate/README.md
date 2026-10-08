# TASK (for a cloud session) — add Portuguese + Dutch to the example sentences

You are a cloud session. Translate existing example sentences into **Portuguese (pt)** and
**Dutch (nl)**, for the TCC313 Verb Engine and Dictionary. The sentences already exist in
Luxembourgish (lb) with reference translations in English (en), German (de) and French (fr).
This task only ADDS pt + nl. Do it yourself (you are the translator) — this runs on cloud-session
credits, exactly like the verb-examples job last time.

> Word/verb MEANINGS are already done for free (see `meanings/`). This task is ONLY the examples.

## Inputs (gzipped JSON, in this folder)
- `verb_examples_input.json.gz` — 3,658 verb units, 197,532 cells (9 tenses × 6 persons each)
- `dict_examples_input.json.gz` — 3,931 units, 58,962 dictionary sentences

Read with Python, e.g.:
```python
import json, gzip
data = json.load(gzip.open("verb_examples_input.json.gz", "rt", encoding="utf-8"))
for unit in data["units"]:
    for it in unit["items"]:
        # it["k"] unique id · it["lb"],it["en"],it["de"],it["fr"] · verbs also it["p"],it["t"]
        ...
```

## What to produce
For EVERY item, write a natural, grammatically perfect translation:
- `pt` = European Portuguese (use `estava a + inf`, `vocês`, etc. — NOT Brazilian)
- `nl` = standard Dutch (split separable verbs correctly: `opgeven` → `geef op`)
- Keep the SAME meaning, tense and grammatical person as the source. Keep the same object/context;
  change only subject + verb form across persons. No quotes inside values, no notes.

## Output — write these two files in this folder
- `verb_examples_ptnl.json` — `{ "<k>": {"pt": "...", "nl": "..."}, ... }`  (k from the verb input)
- `dict_examples_ptnl.json` — `{ "<k>": {"pt": "...", "nl": "..."}, ... }`  (k from the dict input)

The `k` keys map 1:1 back onto the existing cells, so injection is exact.

## How to run it (so it finishes and survives interruptions)
- Process units in order. After every ~25 units, write the output file and `git commit` + `git push`.
- **Resume:** on start, load the existing output file (if any) and SKIP every item whose `k` is
  already present and has non-empty pt and nl. Re-running continues where it stopped.
- Do verbs first (`verb_examples_input.json.gz` → `verb_examples_ptnl.json`), then the dictionary.
- ~7,600 units total. Grind through all of them; commit progress as you go.

## Quality bar
This goes to the Institut National des Langues (INL) — it must be institute-grade. If unsure of a
verb form, prefer the standard dictionary conjugation. Never leave a cell empty.

---
`translate_run.py` in this folder is an OPTIONAL local fallback that calls `claude -p` — it bills a
Max/Pro subscription, NOT cloud credits, so do not use it for the cloud run.
