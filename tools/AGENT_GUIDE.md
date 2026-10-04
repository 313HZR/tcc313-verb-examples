# Writing verb specs (read fully, then work)

Goal: for each verb in your chunk file (`specs/chunks/chunk_NN.json`, 50 verbs) write a spec in
`specs/specs_NN.py` that produces the README's example grid: ONE short everyday scene per verb, the SAME
object/context for all 6 persons, 9 tenses, 5 languages (lb Luxembourgish, fr, de, en, fa Persian).
Only the subject and verb form change. `tools/vlib.py` builds the sentences from your compact spec.
Study `specs/example_spec.py` (regular, reflexive, separable/être, modal verbs) and the docstrings in `tools/vlib.py` first.

## File layout
```python
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()
S.add("<verb id exactly as in the chunk>", lb=LB(...), fr=FR(...), de=DE(...), en=EN(...), fa=FA(...))
...
```
Check with `python3 tools/build.py specs/specs_NN.py --chunk specs/chunks/chunk_NN.json --show 3` (run from repo root). Fix every `LINT`/`BUILD ERROR`
until it reports `problems: 0`. Do NOT run with `--merge`, do not touch any other file, do not commit or push.

## Each chunk entry has: id, lb, fr, de, en, meaning_fa, meaning_en
Use lb/fr/de/en as the target verbs in each language (they may be translations, not word-for-word equivalents;
keep one scene that makes sense for all five). `meaning_fa` may contain junk characters (e.g. stray CJK); write
proper Persian from `meaning_en`/the verb itself. If the fr/de/en field is missing or obviously wrong, use the
natural equivalent of the Luxembourgish verb.

## Builders (all return 9 tenses x 6 persons; every argument must be correct, nothing is auto-checked for grammar)
* `LB(inf, rest, pp, pres=None, aux="hunn"|"sinn", part="", inf_full=None, sub=None)`
  - `pres`: 6 forms ech,du,hien,mir,dir,si. Default is a regular weak verb (ech=inf, du -s, hien -t, mir=inf, dir -t, si=inf).
    Give it explicitly for every irregular verb (e.g. goen: ginn, gees, geet, ginn, gitt, ginn; hunn, sinn, kënnen, wëllen...).
  - `pp`: complete participle chunk incl. ge- (gepléckt; plisséiert has no ge-; separable: fortgaang).
  - `rest`: object/context, with correct Eifeler Regel *inside* it. The builder applies the n-rule to the subject/auxiliary/verb itself.
  - `part`: word(s) after `rest` in a main clause (separable particle like "fort"; infinitive complement). `inf_full`: infinitive chunk used with
    wäert/géif (default part+inf). `sub`: 6 verb-final chunks for the "datt ..." clause (default part+pres).
  - past/imperfect use the Perfekt in lb (standard) — nothing to do.
* `DE(pres, praet, pp, rest, aux="haben"|"sein", part="", inf=None, sub=None)`
  - `pres`, `praet`: 6 forms (ich,du,er,wir,ihr,sie). For regular weak verbs: `*de_weak("stem")`, flags `sib=True` (stem ends s/ß/x/z: du -t),
    `dt=True` (stem ends t/d/ or cluster like -tm,-gn: du -est, er -et, -ete). Strong/irregular verbs: write all forms.
  - `pp`: full participle chunk (gepflückt, eingesetzt, besucht, "schwimmen können"). `part`: trailing main-clause word (separable prefix such as "ein",
    or infinitive complement). `inf`: infinitive chunk for werden/würde (default part+pres[3]; give it explicitly for modals and for sein/haben).
    `sub`: 6 verb-final chunks for the "dass ..." clause (default part+pres; give explicitly if the clause needs e.g. "schwimmen kann").
  - Reflexives: put `{r}` (accusative) or `{rd}` (dative) in `rest`, e.g. "{r} im Bad".
* `FR(f, obj, aux="avoir"|"être", refl=False, agree=True)`; `f` from:
  - `fr_er(stem, pres_stem=None, fut_stem=None)` regular -er (handles -ger/-cer; acheter: `fr_er("achet","achèt","achèter")`, appeler: `fr_er("appel","appell","appeller")`, payer/nettoyer: `fr_er("pay","pai","paier")`)
  - `fr_ir(stem)` finir-type, `fr_re(stem)` vendre-type
  - `fr_irr(pres, pp, ps, fut, subj=None, imp=None)` everything else (prendre, venir, voir, écrire...). `ps` = 6 passé-simple forms, `fut` = future stem
    ("viendr"), give `subj`/`imp` when not derivable (être, avoir, aller, faire, savoir, pouvoir, vouloir, falloir...).
  - Compound tenses use passé composé (perfect), plus-que-parfait, conditionnel passé. `past` = passé simple. `obj` = what follows the verb.
  - Pronominal verbs: `refl=True`, `aux="être"`; with a direct object after the verb (se laver les mains) use `agree=False`.
    Verbs with être (aller, venir, partir, arriver, naître, mourir, tomber, rester, devenir, entrer, sortir, monter, descendre...) use `aux="être"`
    (participle agrees automatically with nous/vous/ils).
* `EN(base, s3, past, ing, pp, obj, pres=None, past6=None)` — e.g. `EN("pick","picks","picked","picking","picked","the apples")`. Irregulars: give true
  forms (go/goes/went/going/gone). `{r}` = myself.. and `{pos}` = my/your/his/our/your/their usable in obj. Phrasal verbs go in `base` etc ("look after").
* `FA(ctx, pres, past, sp="ب", pref="", pres6=None, subj6=None)`
  - `ctx`: everything before the verb: object (+ را), place, and the noun/adjective part of a compound verb ("جدل", "صاف", "حمل").
    Compound verbs with کردن/شدن/دادن/زدن: put the noun in `ctx`, the light verb in pres/past: `FA("بحث را در کلاس سیاسی", "کن", "کرد", sp="")`.
  - `pres`/`past`: present and past STEM (کن/کرد، چین/چید، زن/زد، ده/داد، گیر/گرفت، بین/دید، ...). `sp`: subjunctive prefix "ب" (use "" for compounds with
    کردن/شدن, and for verbs whose subjunctive has no ب like داشتن, or when the stem starts with a vowel-glide).
  - Prefixed verbs (برگشتن, درآوردن, ...): `pref="بر"`, pres "گرد", past "گشت" -> برمی‌گردم, برگشتم, برگردم.
  - Irregular present stems (آمدن، رفتن with "رو", دیدن، گفتن، شدن، بودن، داشتن، دادن with ده...): when the endings differ from the regular pattern
    (stem ending in vowel/ا/و, e.g. می‌آیم, می‌روم is fine regular but می‌شوم vs می‌شویم...), pass `pres6` (6 full present forms *with* می‌ + ZWNJ "‌") and `subj6` (6 full subjunctive forms).
    ALWAYS pass pres6/subj6 for stems ending in ا / و / ی (آ→می‌آیم, گو→می‌گویم, شو→می‌شوم, رو→می‌روم etc.) and check the output.
  - Use real Persian script only; ZWNJ (U+200C) in می‌ and in plurals like سیب‌ها, تخم‌مرغ. Possessive in ctx: `{ps}` -> م ت ش مان تان شان (only when it fits grammatically).
  - Perfect/pluperfect are built from past stem + ه; conditional = می‌ + past (imperfect form), conditional_perfect = pluperfect.

Every text field (`rest`, `obj`, `ctx`) may be a plain string or a list of 6 strings (one per person) if a possessive etc. must change by person; prefer neutral
objects with no person-dependence.

## Scene rules
* One concrete, everyday, natural scene per verb; object/context identical in all languages & persons. Avoid sentences that are odd for 6 different subjects.
* Verbs that need no object (intransitive/weather/modal/state): use a short adverbial context ("am Moien", "au jardin", "in the garden", "در باغ").
* Impersonal/weather verbs (regnen, schneien...): choose a scene where all persons can be subject (e.g. causative/metaphorical or "Ech hunn et gesinn ...") — or
  treat as a person-subject verb sensibly (never leave a cell empty, never write "es" for all persons).
* Reflexive verbs (sech ..., se ..., sich ...): use reflexive tokens/refl=True in every language that has it; English drops it where English isn't reflexive.
* Modals/auxiliary-like verbs (kënnen, müssen, wëllen, sinn, hunn, ginn...): craft scene so perfect/future work (use the pp/inf/sub chunks). For sinn/hunn/"bleiwen"
  etc. use a complement (e.g. "krank", "e Buch").
* Keep to the ONE sense given by meaning_en/de/fr where the verb is polysemous.
* Be careful and exact: correct auxiliaries (lb hunn/sinn, de haben/sein, fr avoir/être), correct strong/irregular forms in all languages, correct Eifeler Regel
  in the `rest` strings, French elision (the builder does j'/qu'/m'), German word order. These forms are the product — accuracy matters more than speed.
* After building, skim `--show` output for a few verbs and fix anything ungrammatical. Then re-run until `problems: 0` and `MISSING from specs: none` and `EXTRA/unknown ids: none`.

## Final report
Reply with ONE line: `done specs/specs_NN.py <n> verbs` plus a brief note of any verbs you were unsure about.
