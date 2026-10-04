# TCC313 Verb Examples — cloud generation task

Generate example sentences for a multilingual verb trainer: Luxembourgish (lb), French (fr), German (de), English (en), Persian/Dari (fa).

## What to do
For EACH verb in the input file, invent ONE short everyday scene with a fixed object/context. Write that SAME scene for ALL 6 persons, in 9 tenses, in 5 languages. Keep the object/context identical everywhere; change ONLY the subject and the verb form (correct conjugation + word order per person/tense).

- Persons (keys): `1s,2s,3s,1p,2p,3p` = I, you(sg), he/she, we, you(pl), they
  - lb: ech/du/hien/mir/dir/si · de: ich/du/er/wir/ihr/sie · fr: je/tu/il/nous/vous/ils · en: I/you/he/we/you/they · fa: من/تو/او/ما/شما/آنها
- Tenses (keys): `present, perfect, past, imperfect, pluperfect, future, conditional, conditional_perfect, subjunctive`
- Languages (keys): `lb, fr, de, en, fa`
- fa MUST be correct Persian script (never Latin/Finglish), grammatically correct, natural.

## Output format — write `examples6_remaining.json`
```
{"examples": {"<verb_id>": {
  "present": {"1s":{"lb":"","fr":"","de":"","en":"","fa":""}, "2s":{...}, "3s":{...}, "1p":{...}, "2p":{...}, "3p":{...}},
  "perfect": {...}, "past": {...}, "imperfect": {...}, "pluperfect": {...},
  "future": {...}, "conditional": {...}, "conditional_perfect": {...}, "subjunctive": {...}
}}}
```
Every verb = 9 tenses × 6 persons × 5 languages = 270 filled cells. No empty cells.

Commit after every 25 verbs. If `examples6_remaining.json` already exists, skip verbs already complete in it (resume).
