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

## How to run (resumable, survives interruptions)
- Process units in order. After every ~25 units: write the output file + `git add -A && git commit && git push`.
- **Resume:** on start, load the existing output file (if present) and SKIP every `k`/verb/sense already done.
- The `k` / `<lb>` / `<headword>\u0001<ipa>` keys map 1:1 back onto the existing data, so injection is exact.

## Cost note
Meanings (jobs 1–2 ≈ 42k) are small; examples (jobs 3–4 ≈ 256k cells × 3 langs) are the expensive part.
You may stop after jobs 1–2 if you want meanings first and examples later — both are independent.
