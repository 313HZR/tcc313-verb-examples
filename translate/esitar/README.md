# TASK (for a cloud session) — add Spanish + Italian + Arabic (es / it / ar)

You are a **cloud session** (this runs on cloud-session credits, NOT the Max plan — exactly like the
pt/nl job). You are the translator yourself. Translate the TCC313 Verb Engine + Dictionary content
into **Spanish (es)**, **Italian (it)** and **Arabic (ar)**.

Everything already exists in Luxembourgish (lb) with reference translations in English (en),
German (de) and French (fr). Use ALL of them to get the exact meaning, then write natural,
grammatically perfect translations. Unlike pt/nl, **LOD has no es/it/ar**, so this job does BOTH
the meanings AND the examples.

## Languages
- `es` = standard European Spanish (use *vosotros*, *vosotros* forms where relevant; neutral, natural).
- `it` = standard Italian.
- `ar` = Modern Standard Arabic (MSA, فصحى). Correct Arabic script **with full vocalisation (harakat)**.
  Natural MSA, not dialect. Right-to-left text, no Latin letters.

## There are 4 jobs. Do them in THIS order (cheap → expensive). Commit + push after every ~25 units.

### 1) Verb meanings  →  `verb_meanings_esitar.json`   (cheap · 3,658 verbs · ESSENTIAL)
Input: `verb_meanings_input.json.gz`  →  `{"count":N,"verbs":{"<lb>":{"lb","en","de","fr"}}}`
For each verb write its dictionary form:
```
{ "<lb>": { "es":"<Spanish infinitive>", "it":"<Italian infinitive>",
            "ar":"<the verb, MSA, citation form = 3rd-person-masc-singular past, fully vocalised, e.g. كَتَبَ>" } }
```
(The es/it infinitives feed the offline conjugator later; the Arabic citation verb feeds the Arabic
conjugator. Give the single best, most common equivalent verb.)

### 2) Dictionary meanings  →  `dict_meanings_esitar.json`   (38,735 senses)
Input: `dict_meanings_input.json.gz` → `{"entries":{"<headword>\u0001<ipa>":{"l","i","senses":[{"en","de","fr"},...]}}}`
Translate each sense (keep sense order):
```
{ "<headword>\u0001<ipa>": { "senses": [ {"es":"","it":"","ar":""}, {"es":"","it":"","ar":""}, ... ] } }
```

### 3) Verb examples  →  `verb_examples_esitar.json`   (BIG · 197,532 cells)
Input (reuse, in the PARENT folder): `../verb_examples_input.json.gz`
`{"units":[{"items":[{"k","p","t","lb","en","de","fr"}]}]}` — `k` = `lemma\u0001tense\u0001person`.
```
{ "<k>": {"es":"","it":"","ar":""}, ... }
```
Keep the SAME meaning, tense and grammatical person as the source. Keep the same object/context;
change only the subject + verb form across persons. For Arabic, match person **and gender**
sensibly (e.g. 2s → use masculine أنتَ by default; keep it consistent).

### 4) Dictionary examples  →  `dict_examples_esitar.json`   (58,962 sentences)
Input (reuse, parent folder): `../dict_examples_input.json.gz`
`{"units":[{"id","items":[{"k","lb","en","de","fr"}]}]}`
```
{ "<k>": {"es":"","it":"","ar":""}, ... }
```

## Rules
- Natural everyday wording, not word-for-word. No quotes inside values, no notes, no extra keys.
- Arabic MUST be correct vocalised MSA script (never Latin/transliteration).
- Output JSON only. One output file per job (names above), written in **this** folder.

## HOW TO RUN IT — FAST and CHEAP (read carefully, this is the important part)

The previous run was slow and expensive because ONE agent processed everything serially and
wandered (re-reading, re-doing). **Do NOT do that.** Follow this exactly:

1. **Parallel sub-agents (fan-out).** Split the input into chunks of **~40 units** and dispatch
   **8–12 sub-agents at once** (the Task/Agent tool), each translating ONE chunk and returning
   only its JSON. Merge the returned JSON into the output file. This is the whole speed-up:
   many focused workers instead of one wandering agent.
2. **Cheap model.** Use **Haiku** for the bulk (examples). Use Sonnet only for the meanings
   (jobs 1–2) if you want extra quality. Haiku is plenty for sentence translation and is the
   single biggest cost saving.
3. **Batch inside each call.** One sub-agent call translates its WHOLE chunk (~40 units =
   hundreds of cells) in a single response. Never one call per cell.
4. **Strict focus — do NOT wander.** Each sub-agent gets ONLY its chunk of data in the prompt,
   does ONLY the translation, returns ONLY JSON. No reading other files, no exploring, no
   re-translating anything already present in the output.
5. **Commit + resume.** After each batch of merged chunks, write the output file and
   `git add -A && git commit && git push`. On start, load the existing output and SKIP every
   `k`/verb/sense already done. You can stop and restart any time with no waste.
6. **Keys map 1:1** (`k` / `<lb>` / `<headword>\u0001<ipa>`) so injection back is exact.

## Cost strategy — DO THIS
Budget is tight. **Run jobs 1–2 (meanings) FIRST and stop there.** Meanings are small (~42k) and
cheap, and they already unlock: Spanish/Italian conjugation (offline, free) + the es/it/ar word
columns in both apps. **Jobs 3–4 (examples) are the expensive part (256k cells × 3 langs) — only
run them later if budget allows.** Each job is independent; doing meanings only is a complete,
useful result on its own.
