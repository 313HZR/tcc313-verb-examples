# TCC313 — Portuguese + Dutch EXAMPLE translation task

Add **Portuguese (pt)** and **Dutch (nl)** to the existing example sentences — for both the
**Verb Engine** and the **Dictionary**. The sentences already exist in Luxembourgish (lb) with
reference translations in English (en), German (de) and French (fr); this task only adds pt + nl.

> Word/verb **meanings** are NOT in this task — they come free from LOD (`meanings/` folder). Only
> example sentences need translating, because LOD has no example translations.

## Inputs (in this folder)
- `verb_examples_input.json.gz` — 3,658 verb units, 197,532 cells (9 tenses × 6 persons each)
- `dict_examples_input.json.gz` — 3,931 units, 58,962 dictionary example sentences

Each unit = one `claude` call. Each item has a unique `"k"`, plus `lb/en/de/fr` (and for verbs
`p`=person, `t`=tense). Translate every item to `pt` and `nl`, keeping the SAME meaning, tense and
grammatical person. European Portuguese; standard Dutch.

## Run it (PowerShell, inside this `translate` folder) — proven method, resumable
```powershell
python translate_run.py --input verb_examples_input.json.gz --output verb_examples_ptnl.json --model sonnet --conc 3
python translate_run.py --input dict_examples_input.json.gz --output dict_examples_ptnl.json --model sonnet --conc 3
```
- Uses your local Claude Code CLI (`claude -p`) — no API key.
- Writes output every few units; **safe to stop and re-run** — it skips what is already done.
- Dry run first if you want: `$env:TCC_MOCK=1; python translate_run.py --input dict_examples_input.json.gz --output test.json --limit 3`

## Outputs — the two files you send back, ready for injection
- `verb_examples_ptnl.json` — `{ "<verb>\u0001<tense>\u0001<person>": {"pt":"","nl":""}, ... }`
- `dict_examples_ptnl.json` — `{ "<headword>\u0001<senseIndex>\u0001<exampleIndex>": {"pt":"","nl":""}, ... }`

The keys map 1:1 back onto the existing example cells, so injection into the master (and then the
separated editions) is exact — nothing is guessed.

## Scale / time
~7,600 calls total (3,658 verb + 3,931 dict). With `--conc 3` this runs overnight; if it doesn't
finish, just re-run the same command next session — it resumes.
