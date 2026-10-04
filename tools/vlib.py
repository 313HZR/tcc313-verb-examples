# -*- coding: utf-8 -*-
"""Helpers for building the 9-tense x 6-person x 5-language example grid.

Every builder returns {tense: [6 sentences]} (order 1s,2s,3s,1p,2p,3p).
Text fields (rest/obj/ctx) may be a string or a list of 6 strings (one per person).
Tokens usable in text fields:
  lb : {r} mech/dech/sech/eis/iech/sech   {rd} mer/der/sech/eis/iech/sech
  de : {r} mich/dich/sich/uns/euch/sich   {rd} mir/dir/sich/uns/euch/sich
  en : {r} myself/yourself/himself/ourselves/yourselves/themselves
       {pos} my/your/his/our/your/their
  fa : {ps} م/ت/ش/مان/تان/شان  (possessive suffix)
"""
import json

PERS = ["1s", "2s", "3s", "1p", "2p", "3p"]
TENSES = ["present", "perfect", "past", "imperfect", "pluperfect",
          "future", "conditional", "conditional_perfect", "subjunctive"]
LANGS = ["lb", "fr", "de", "en", "fa"]
ZWNJ = "‌"


def _pick(x, i):
    return x[i] if isinstance(x, (list, tuple)) else x


def _sub(s, i, table):
    for k, v in table.items():
        s = s.replace("{" + k + "}", v[i])
    return s


# ======================= Luxembourgish =======================
LB_P = ["Ech", "Du", "Hien", "Mir", "Dir", "Si"]
LB_TOK = {"r": ["mech", "dech", "sech", "eis", "iech", "sech"],
          "rd": ["mer", "der", "sech", "eis", "iech", "sech"]}
HUNN = ["hunn", "hues", "huet", "hunn", "hutt", "hunn"]
SINN = ["sinn", "bass", "ass", "sinn", "sidd", "sinn"]
HAT = ["hat", "has", "hat", "haten", "hat", "haten"]
WAR = ["war", "waars", "war", "waren", "waart", "waren"]
WAERT = ["wäert", "wäerts", "wäert", "wäerten", "wäert", "wäerten"]
GEIF = ["géif", "géifs", "géif", "géifen", "géift", "géifen"]
HAETT = ["hätt", "häss", "hätt", "hätten", "hätt", "hätten"]
WIER = ["wier", "wiers", "wier", "wieren", "wiert", "wieren"]
_LBV = set("aeiouyäëéöüâîûàèê")


def eifel(w, nxt):
    """Eifeler Regel: keep final -n only before vowels and d,t,z,h,n."""
    if not nxt or not w.endswith("n"):
        return w
    c = nxt[0].lower()
    if c in _LBV or c in "dtzhn":
        return w
    return w[:-2] if w.endswith("nn") else w[:-1]


def lb_regular(inf):
    """Regular present of a weak verb: ech=inf, du -s, hien -t, mir=inf, dir -t, si=inf."""
    stem = inf[:-2]
    s2 = stem if stem[-1] in "sxz" else stem + "s"
    return [inf, s2, stem + "t", inf, stem + "t", inf]


def LB(inf, rest, pp, pres=None, aux="hunn", part="", inf_full=None, sub=None):
    """inf: infinitive (main verb); rest: object/context; pp: full participle chunk
    (e.g. 'gepléckt', 'plattgedréckt'); pres: 6 present forms (default regular);
    aux 'hunn'|'sinn'; part: trailing word after rest in a main clause (separable
    particle, or an infinitive complement); inf_full: infinitive chunk for
    future/conditional (default part+inf); sub: 6 verb-final chunks for the datt-clause
    (default part+pres)."""
    pres = pres or lb_regular(inf)
    inf_full = inf_full or (part + inf)
    sub = sub or [part + p for p in pres]
    auxp = SINN if aux == "sinn" else HUNN
    auxpl = WAR if aux == "sinn" else HAT
    auxcp = WIER if aux == "sinn" else HAETT

    def sent(i, fin, tail):
        r = _sub(_pick(rest, i), i, LB_TOK)
        rem = (r + " " + tail).strip()
        first = rem.split()[0] if rem else ""
        subj = LB_P[i]
        if i == 2:
            subj = eifel(subj, fin)
        return f"{subj} {eifel(fin, first)} {rem}".replace("  ", " ").strip() + "."

    out = {t: [] for t in TENSES}
    for i in range(6):
        out["present"].append(sent(i, pres[i], part))
        perf = sent(i, auxp[i], pp)
        out["perfect"].append(perf)
        out["past"].append(perf)
        out["imperfect"].append(perf)
        out["pluperfect"].append(sent(i, auxpl[i], pp))
        out["future"].append(sent(i, WAERT[i], inf_full))
        out["conditional"].append(sent(i, GEIF[i], inf_full))
        out["conditional_perfect"].append(sent(i, auxcp[i], pp))
        r = _sub(_pick(rest, i), i, LB_TOK)
        cl = ["ech", "s du", "hien", "mir", "dir", "si"][i]
        if i == 2:
            cl = eifel("hien", r.split()[0] if r else sub[i])
        out["subjunctive"].append(f"Et ass wichteg, datt {cl} {r} {sub[i]}.".replace("  ", " "))
    return out


# ======================= German =======================
DE_P = ["Ich", "Du", "Er", "Wir", "Ihr", "Sie"]
DE_PL = ["ich", "du", "er", "wir", "ihr", "sie"]
DE_TOK = {"r": ["mich", "dich", "sich", "uns", "euch", "sich"],
          "rd": ["mir", "dir", "sich", "uns", "euch", "sich"]}
HABE = ["habe", "hast", "hat", "haben", "habt", "haben"]
HATTE = ["hatte", "hattest", "hatte", "hatten", "hattet", "hatten"]
BIN = ["bin", "bist", "ist", "sind", "seid", "sind"]
WAR_DE = ["war", "warst", "war", "waren", "wart", "waren"]
WERDE = ["werde", "wirst", "wird", "werden", "werdet", "werden"]
WUERDE = ["würde", "würdest", "würde", "würden", "würdet", "würden"]
HAETTE = ["hätte", "hättest", "hätte", "hätten", "hättet", "hätten"]
WAERE = ["wäre", "wärst", "wäre", "wären", "wärt", "wären"]


def de_weak(stem, sib=False, dt=False):
    """Regular weak verb -> (pres6, praet6). sib: stem ends in s/ß/x/z (du -t);
    dt: stem ends in t/d or consonant cluster needing -e- (du -est, er -et, -ete)."""
    en = "n" if (stem.endswith(("er", "el")) and not stem.endswith("ier")) else "en"
    e = "e" if dt else ""
    pres = [stem + "e", stem + e + ("t" if sib else "st"), stem + e + "t",
            stem + en, stem + e + "t", stem + en]
    praet = [stem + e + x for x in ["te", "test", "te", "ten", "tet", "ten"]]
    return pres, praet


def DE(pres, praet, pp, rest, aux="haben", part="", inf=None, sub=None):
    """pres/praet: 6 forms (use de_weak for regular verbs); pp: full participle chunk
    ('gepflückt', 'eingesetzt', 'schwimmen können'); rest: object/context;
    aux 'haben'|'sein'; part: trailing word after rest in a main clause (separable
    particle or infinitive complement); inf: infinitive chunk for future/conditional
    (default part+pres[3]); sub: 6 verb-final chunks for the dass-clause
    (default part+pres)."""
    inf = inf or (part + pres[3])
    sub = sub or [part + p for p in pres]
    auxp = BIN if aux == "sein" else HABE
    auxpl = WAR_DE if aux == "sein" else HATTE
    auxcp = WAERE if aux == "sein" else HAETTE
    out = {t: [] for t in TENSES}

    def s(i, fin, tail):
        r = _sub(_pick(rest, i), i, DE_TOK)
        return f"{DE_P[i]} {fin} {r} {tail}".replace("  ", " ").strip() + "."
    for i in range(6):
        out["present"].append(s(i, pres[i], part))
        out["perfect"].append(s(i, auxp[i], pp))
        out["past"].append(s(i, praet[i], part))
        out["imperfect"].append(s(i, praet[i], part))
        out["pluperfect"].append(s(i, auxpl[i], pp))
        out["future"].append(s(i, WERDE[i], inf))
        out["conditional"].append(s(i, WUERDE[i], inf))
        out["conditional_perfect"].append(s(i, auxcp[i], pp))
        r = _sub(_pick(rest, i), i, DE_TOK)
        out["subjunctive"].append(
            f"Es ist wichtig, dass {DE_PL[i]} {r} {sub[i]}.".replace("  ", " "))
    return out


# ======================= French =======================
FR_P = ["je", "tu", "il", "nous", "vous", "ils"]
FR_CL = ["me", "te", "se", "nous", "vous", "se"]
AVOIR = ["ai", "as", "a", "avons", "avez", "ont"]
AVAIS = ["avais", "avais", "avait", "avions", "aviez", "avaient"]
AURAIS = ["aurais", "aurais", "aurait", "aurions", "auriez", "auraient"]
ETRE = ["suis", "es", "est", "sommes", "êtes", "sont"]
ETAIS = ["étais", "étais", "était", "étions", "étiez", "étaient"]
SERAIS = ["serais", "serais", "serait", "serions", "seriez", "seraient"]
_FRV = set("aeiouyéèêëâîôûàhAEIOUÉ")


def _end(stem, ends):
    out = []
    for e in ends:
        s = stem
        if e[0] in "aoâ":
            if s.endswith("g"):
                s += "e"
            elif s.endswith("c"):
                s = s[:-1] + "ç"
        out.append(s + e)
    return out


def fr_er(stem, pres_stem=None, fut_stem=None):
    """-er verb. pres_stem: stem for je/tu/il/ils and subj sg/3p (acheter -> 'achèt',
    appeler -> 'appell', payer -> 'pai'); fut_stem: for future/conditional
    (default stem+'er'; acheter -> 'achèter')."""
    ps = pres_stem or stem
    fs = fut_stem or (stem + "er")
    return {
        "pres": [ps + "e", ps + "es", ps + "e", *_end(stem, ["ons"]), stem + "ez", ps + "ent"],
        "imp": _end(stem, ["ais", "ais", "ait", "ions", "iez", "aient"]),
        "ps": _end(stem, ["ai", "as", "a", "âmes", "âtes", "èrent"]),
        "fut": [fs + e for e in ["ai", "as", "a", "ons", "ez", "ont"]],
        "cond": [fs + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]],
        "subj": [ps + "e", ps + "es", ps + "e", stem + "ions", stem + "iez", ps + "ent"],
        "pp": _end(stem, ["é"])[0],
    }


def fr_ir(stem):
    """finir-type (2nd group)."""
    return {
        "pres": [stem + e for e in ["is", "is", "it", "issons", "issez", "issent"]],
        "imp": [stem + e for e in ["issais", "issais", "issait", "issions", "issiez", "issaient"]],
        "ps": [stem + e for e in ["is", "is", "it", "îmes", "îtes", "irent"]],
        "fut": [stem + "ir" + e for e in ["ai", "as", "a", "ons", "ez", "ont"]],
        "cond": [stem + "ir" + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]],
        "subj": [stem + e for e in ["isse", "isses", "isse", "issions", "issiez", "issent"]],
        "pp": stem + "i",
    }


def fr_re(stem):
    """vendre-type (regular -re)."""
    return {
        "pres": [stem + e for e in ["s", "s", "", "ons", "ez", "ent"]],
        "imp": [stem + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]],
        "ps": [stem + e for e in ["is", "is", "it", "îmes", "îtes", "irent"]],
        "fut": [stem + "r" + e for e in ["ai", "as", "a", "ons", "ez", "ont"]],
        "cond": [stem + "r" + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]],
        "subj": [stem + e for e in ["e", "es", "e", "ions", "iez", "ent"]],
        "pp": stem + "u",
    }


def fr_irr(pres, pp, ps, fut, subj=None, imp=None):
    """Irregular verb. pres: 6 forms; pp: past participle (masc. sg.); ps: 6 passé
    simple forms; fut: future/conditional stem WITHOUT endings (e.g. 'ir', 'aur',
    'viendr'); subj: 6 forms (default: derived from ils-form); imp: 6 forms (default
    derived from nous-form)."""
    if imp is None:
        b = pres[3][:-3]
        imp = [b + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]]
    if subj is None:
        b = pres[5][:-3]
        bn = pres[3][:-3]
        subj = [b + "e", b + "es", b + "e", bn + "ions", bn + "iez", b + "ent"]
    return {
        "pres": pres, "imp": imp, "ps": ps, "pp": pp, "subj": subj,
        "fut": [fut + e for e in ["ai", "as", "a", "ons", "ez", "ont"]],
        "cond": [fut + e for e in ["ais", "ais", "ait", "ions", "iez", "aient"]],
    }


def FR(f, obj, aux="avoir", refl=False, agree=True):
    """f: dict from fr_er/fr_ir/fr_re/fr_irr. obj: text after the verb (string or 6-list).
    aux 'avoir'|'être'. refl: pronominal verb (me/te/se...; use aux='être').
    agree: with aux être, add -s to the participle for nous/vous/ils (set False for
    pronominal verbs whose direct object follows, e.g. se laver les mains)."""
    a_p, a_pl, a_cp = (ETRE, ETAIS, SERAIS) if aux == "être" else (AVOIR, AVAIS, AURAIS)

    def core(i, fin):
        if refl:
            cl = FR_CL[i]
            if cl in ("me", "te", "se") and fin[0] in _FRV:
                w = cl[0] + "'" + fin
            else:
                w = cl + " " + fin
            return FR_P[i] + " " + w
        if i == 0 and fin[0] in _FRV:
            return "j'" + fin
        return FR_P[i] + " " + fin

    def ppf(i):
        p = f["pp"]
        if aux == "être" and agree and i >= 3 and not p.endswith(("s", "x")):
            p += "s"
        return p

    def cap(s):
        return s[0].upper() + s[1:]
    out = {t: [] for t in TENSES}
    for i in range(6):
        o = _pick(obj, i)
        sp = lambda fin, tail="": cap((core(i, fin) + " " + tail + " " + o).replace("  ", " ").strip()) + "."
        out["present"].append(sp(f["pres"][i]))
        out["perfect"].append(sp(a_p[i], ppf(i)))
        out["past"].append(sp(f["ps"][i]))
        out["imperfect"].append(sp(f["imp"][i]))
        out["pluperfect"].append(sp(a_pl[i], ppf(i)))
        out["future"].append(sp(f["fut"][i]))
        out["conditional"].append(sp(f["cond"][i]))
        out["conditional_perfect"].append(sp(a_cp[i], ppf(i)))
        c = core(i, f["subj"][i])
        que = "qu'" if c.startswith(("il", "ils")) else "que "
        out["subjunctive"].append(f"Il est important {que}{c} {o}.".replace("  ", " "))
    return out


# ======================= English =======================
EN_P = ["I", "You", "He", "We", "You", "They"]
EN_TOK = {"r": ["myself", "yourself", "himself", "ourselves", "yourselves", "themselves"],
          "pos": ["my", "your", "his", "our", "your", "their"]}
_WAS = ["was", "were", "was", "were", "were", "were"]
_HAVE = ["have", "have", "has", "have", "have", "have"]


def EN(base, s3, past, ing, pp, obj, pres=None, past6=None):
    """base 'pick', s3 'picks', past 'picked', ing 'picking', pp 'picked'; obj: text after
    the verb ('' allowed). pres/past6: optional 6 forms for be/have-like verbs."""
    out = {t: [] for t in TENSES}
    for i in range(6):
        o = _sub(_pick(obj, i), i, EN_TOK)
        j = lambda *w: " ".join(x for x in w if x).strip() + "."
        P = EN_P[i]
        out["present"].append(j(P, pres[i] if pres else (s3 if i == 2 else base), o))
        out["perfect"].append(j(P, _HAVE[i], pp, o))
        out["past"].append(j(P, past6[i] if past6 else past, o))
        out["imperfect"].append(j(P, _WAS[i], ing, o))
        out["pluperfect"].append(j(P, "had", pp, o))
        out["future"].append(j(P, "will", base, o))
        out["conditional"].append(j(P, "would", base, o))
        out["conditional_perfect"].append(j(P, "would have", pp, o))
        sp = P if i == 0 else P.lower()
        out["subjunctive"].append(j("It is important that", sp, base, o))
    return out


# ======================= Persian =======================
FA_P = ["من", "تو", "او", "ما", "شما", "آنها"]
FA_TOK = {"ps": ["م", "ت", "ش", "مان", "تان", "شان"]}
_EP = ["م", "ی", "د", "یم", "ید", "ند"]
_EPAST = ["م", "ی", "", "یم", "ید", "ند"]
_BUD = ["بودم", "بودی", "بود", "بودیم", "بودید", "بودند"]
_KHAH = ["خواهم", "خواهی", "خواهد", "خواهیم", "خواهید", "خواهند"]
_PERF = ["ام", "ای", "", "ایم", "اید", "اند"]
_MI = "می" + ZWNJ


def FA(ctx, pres, past, sp="ب", pref="", pres6=None, subj6=None):
    """ctx: everything before the verb, incl. object and the noun part of a compound
    verb (e.g. 'دارو را با پنبه روی زخم', 'جدل'); pres: present stem (کن، چین، زن);
    past: past stem (کرد، چید، زد); sp: subjunctive prefix 'ب' ('' for compound verbs
    with کردن/شدن, auto '' when pref is set); pref: verbal prefix that precedes می‌
    (برگشتن -> pref='بر', pres='گرد', past='گشت'); pres6/subj6: explicit 6 forms for
    irregular stems (include می‌ in pres6), e.g. آمدن."""
    part = pref + past + "ه"
    pr = pres6 or [pref + _MI + pres + e for e in _EP]
    if subj6 is None:
        spx = "" if pref else sp
        subj6 = [pref + spx + pres + e for e in _EP]
    perf = [part + " است" if i == 2 else part + ZWNJ + _PERF[i] for i in range(6)]
    out = {t: [] for t in TENSES}
    for i in range(6):
        c = _sub(_pick(ctx, i), i, FA_TOK)
        f = lambda v: f"{FA_P[i]} {c} {v}.".replace("  ", " ")
        past_i = pref + past + _EPAST[i]
        imp_i = pref + _MI + past + _EPAST[i]
        out["present"].append(f(pr[i]))
        out["perfect"].append(f(perf[i]))
        out["past"].append(f(past_i))
        out["imperfect"].append(f(imp_i))
        out["pluperfect"].append(f(part + " " + _BUD[i]))
        out["future"].append(f(_KHAH[i] + " " + pref + past))
        out["conditional"].append(f(imp_i))
        out["conditional_perfect"].append(f(part + " " + _BUD[i]))
        out["subjunctive"].append(f"مهم است که {FA_P[i]} {c} {subj6[i]}.".replace("  ", " "))
    return out


# ======================= registry / assembly =======================
class Specs:
    def __init__(self):
        self.items = []

    def add(self, vid, lb, fr, de, en, fa):
        self.items.append((vid, dict(lb=lb, fr=fr, de=de, en=en, fa=fa)))


def assemble(vid, spec):
    entry = {}
    for t in TENSES:
        entry[t] = {}
        for i, p in enumerate(PERS):
            entry[t][p] = {l: spec[l][t][i] for l in LANGS}
    return entry
