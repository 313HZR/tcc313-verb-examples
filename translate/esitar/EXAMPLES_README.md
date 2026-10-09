# TASK (cloud session) — translate ALL example sentences into es / it / ar

You are a **cloud session** (bills cloud-session credits, NOT a Max plan). This is the
EXAMPLES job only. The verb/dictionary MEANINGS are already done — **do not touch them.**

Translate every example sentence into **Spanish (es)**, **Italian (it)** and
**Modern Standard Arabic (ar, فصحى, fully vocalised — harakat on every word, no Latin
letters)**. Source is given in Luxembourgish (lb) + English (en) + German (de) +
French (fr); use all four to get the exact sense, then write a natural sentence that keeps
the **same tense, the same grammatical person, and the same meaning/object** as the source.
For the verb job the only thing that changes across the 6 persons is the subject + verb form.

There are two jobs. **Do `verb` FIRST, finish it completely, then do `dict`.**
- `verb` → 3658 verbs × 54 cells (9 tenses × 6 persons) = 197,532 cells → `verb_examples_esitar.json`
- `dict` → 58,962 sentences → `dict_examples_esitar.json`
Output format for both: `{ "<k>": {"es":"...","it":"...","ar":"..."}, ... }` (keys map 1:1).

## ⚠️ HOW TO RUN IT — this is the important part (last run went single-agent and burned all the money)

A helper script does ALL the bookkeeping so YOU (the orchestrator) never load the big files
and never wander. Work in `translate/esitar/`. The loop is mechanical:

```
cd translate/esitar
python examples_run.py status                 # see remaining
# ---- repeat this wave until status shows remaining 0 ----
python examples_run.py emit verb 10 3          # emit 10 chunk files (3 verbs=162 cells each)
#   -> dispatch 10 PARALLEL sub-agents, one per CHUNK file it printed (see sub-agent prompt below)
python examples_run.py merge verb              # fold all results in, report progress
git add -A && git commit -m "verb examples wave" && git push
# ---- end wave; loop again ----
```
When `verb` shows remaining 0, switch to `dict`: `emit dict 10 8` (8×15=120 cells/chunk), same loop.

### The rules that keep it cheap and focused — FOLLOW EXACTLY
1. **Parallel Haiku sub-agents.** Each wave dispatches **10 sub-agents AT ONCE** (the Task/Agent
   tool), each on ONE chunk file. Use the **Haiku** model for every sub-agent. This is the whole
   speed-up and the whole cost saving.
2. **Sub-agents read & write FILES, not chat.** Each sub-agent reads its chunk file, writes its
   result file, and returns ONE short line. The big data never enters your context. This is what
   stopped the previous run from being cheap.
3. **One sub-agent = its whole chunk in one response.** Never one call per sentence.
4. **Strict focus. No wandering.** A sub-agent reads ONLY its chunk file, translates ONLY those
   rows, writes ONLY its out file. No exploring, no re-reading inputs, no re-doing merged work.
5. **Commit + push after EVERY wave** (the `merge` already wrote the output file). The helper
   skips everything already done, so you can stop/restart any time with zero waste. If the session
   dies, just start the loop again — it resumes.
6. **Do not re-translate** anything already in the output. `emit` only ever hands out pending cells.

### Exact sub-agent prompt (use Haiku, one per chunk file)
> You are a translation worker. Model: Haiku. Read the JSON file `<CHUNK_IN_PATH>` — it has
> `rows`, each `{k, lb, en, de, fr}`. For EVERY row, translate the sentence into:
> `es` (natural European Spanish), `it` (natural Italian), `ar` (Modern Standard Arabic, فصحى,
> FULLY VOCALISED with harakat, Arabic script only, no Latin). Keep the SAME tense, the SAME
> grammatical person, and the SAME meaning and object as the source; for different persons change
> only the subject + verb form. Write a JSON file to the path given in the chunk file's `out`
> field: `{ "<k>": {"es":"...","it":"...","ar":"..."}, ... }` with an entry for EVERY row, keys
> copied exactly (including the \u0001 bytes). No notes, no extra keys, no quotes inside values.
> Return only: `wrote N rows to <out>`.

## Cost note
Examples are large (~256k cells × 3 langs ≈ 769k translations). Because every wave commits,
whatever the budget covers is saved and the rest resumes later. Finish `verb` before `dict` so
the Verb Engine is fully trilingual first even if you stop midway.
