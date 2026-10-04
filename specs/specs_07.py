# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

Z = "‌"
FA_BE_PRES = ["هستم", "هستی", "است", "هستیم", "هستید", "هستند"]
FA_BE_SUBJ = ["باشم", "باشی", "باشد", "باشیم", "باشید", "باشند"]
FR_ETRE = fr_irr(["suis", "es", "est", "sommes", "êtes", "sont"], "été",
                 ["fus", "fus", "fut", "fûmes", "fûtes", "furent"], "ser",
                 subj=["sois", "sois", "soit", "soyons", "soyez", "soient"],
                 imp=["étais", "étais", "était", "étions", "étiez", "étaient"])

# 0 ensure
S.add("sécherstellen",
  lb=LB("stellen", "d'Qualitéit", "séchergestallt", part="sécher", inf_full="sécherstellen",
        sub=["sécherstellen", "sécherstells", "sécherstellt", "sécherstellen", "sécherstellt", "sécherstellen"]),
  fr=FR(fr_er("assur"), "la qualité"),
  de=DE(*de_weak("stell"), "sichergestellt", "die Qualität", part="sicher", inf="sicherstellen"),
  en=EN("ensure", "ensures", "ensured", "ensuring", "ensured", "the quality"),
  fa=FA("کیفیت را تضمین", "کن", "کرد", sp=""))

# 1 piss
S.add("seechen",
  lb=LB("seechen", "am Gaart", "geseecht"),
  fr=FR(fr_er("piss"), "dans le jardin"),
  de=DE(*de_weak("seich"), "geseicht", "im Garten"),
  en=EN("piss", "pisses", "pissed", "pissing", "pissed", "in the garden"),
  fa=FA("در باغ", "شاش", "شاشید"))

# 2 saw
S.add("seeën",
  lb=LB("seeën", "d'Brett", "geseet"),
  fr=FR(fr_er("sci"), "la planche"),
  de=DE(*de_weak("säg"), "gesägt", "das Brett"),
  en=EN("saw", "saws", "sawed", "sawing", "sawn", "the board"),
  fa=FA("تخته را اره", "کن", "کرد", sp=""))

# 3 sail
S.add("seegelen",
  lb=LB("seegelen", "um Séi", "geseegelt"),
  fr=FR(fr_er("navigu"), "sur le lac"),
  de=DE(*de_weak("segel"), "gesegelt", "auf dem See"),
  en=EN("sail", "sails", "sailed", "sailing", "sailed", "on the lake"),
  fa=FA("روی دریاچه بادبانی", "کن", "کرد", sp=""))

# 4 hem
S.add("seemen",
  lb=LB("seemen", "de Rock", "geseemt"),
  fr=FR(fr_er("ourl"), "la jupe"),
  de=DE(*de_weak("säum"), "gesäumt", "den Rock"),
  en=EN("hem", "hems", "hemmed", "hemming", "hemmed", "the skirt"),
  fa=FA("دامن را لبه" + Z + "دوزی", "کن", "کرد", sp=""))

# 5 bless
S.add("seenen",
  lb=LB("seenen", "d'Kand", "geseent"),
  fr=FR(fr_ir("bén"), "l'enfant"),
  de=DE(*de_weak("segn", dt=True), "gesegnet", "das Kind"),
  en=EN("bless", "blesses", "blessed", "blessing", "blessed", "the child"),
  fa=FA("به کودک برکت", "ده", "داد"))

# 6 weep (ooze)
S.add("sëfferen",
  lb=LB("sëfferen", "staark", "gesëffert"),
  fr=FR(fr_er("suint"), "beaucoup"),
  de=DE(*de_weak("näss", sib=True), "genässt", "stark"),
  en=EN("weep", "weeps", "wept", "weeping", "wept", "heavily"),
  fa=FA("زیاد ترشح", "کن", "کرد", sp=""))

# 7 sow
S.add("séien",
  lb=LB("séien", "Weess um Feld", "gesaat"),
  fr=FR(fr_er("sem", "sèm", "sèmer"), "le blé dans le champ"),
  de=DE(["säe", "säst", "sät", "säen", "sät", "säen"],
        ["säte", "sätest", "säte", "säten", "sätet", "säten"], "gesät", "Weizen auf dem Feld"),
  en=EN("sow", "sows", "sowed", "sowing", "sown", "wheat in the field"),
  fa=FA("گندم را در مزرعه", "کار", "کاشت"))

# 8 select
S.add("selektionéieren",
  lb=LB("selektionéieren", "déi bescht Bewerber", "selektionéiert"),
  fr=FR(fr_er("sélectionn"), "les meilleurs candidats"),
  de=DE(*de_weak("wähl"), "ausgewählt", "die besten Bewerber", part="aus", inf="auswählen"),
  en=EN("select", "selects", "selected", "selecting", "selected", "the best candidates"),
  fa=FA("بهترین متقاضیان را انتخاب", "کن", "کرد", sp=""))

# 9 broadcast
S.add("senden",
  lb=LB("senden", "d'Noriichten um Radio", "gesend",
        pres=["senden", "sends", "sent", "senden", "sent", "senden"]),
  fr=FR(fr_er("diffus"), "les informations à la radio"),
  de=DE(*de_weak("send", dt=True), "gesendet", "die Nachrichten im Radio"),
  en=EN("broadcast", "broadcasts", "broadcast", "broadcasting", "broadcast", "the news on the radio"),
  fa=FA("اخبار را از رادیو پخش", "کن", "کرد", sp=""))

# 10 sin
S.add("sënnegen",
  lb=LB("sënnegen", "dacks", "gesënnegt"),
  fr=FR(fr_er("péch", "pèch", "pécher"), "souvent"),
  de=DE(*de_weak("sündig"), "gesündigt", "oft"),
  en=EN("sin", "sins", "sinned", "sinning", "sinned", "often"),
  fa=FA("اغلب گناه", "کن", "کرد", sp=""))

# 11 sort out
S.add("sënneren",
  lb=LB("sënneren", "d'Wäsch", "gesënnert"),
  fr=FR(fr_er("tri"), "le linge"),
  de=DE(*de_weak("sortier"), "sortiert", "die Wäsche"),
  en=EN("sort", "sorts", "sorted", "sorting", "sorted", "the laundry"),
  fa=FA("لباس‌ها را دسته" + Z + "بندی", "کن", "کرد", sp=""))

# 12 sensitise
S.add("sensibiliséieren",
  lb=LB("sensibiliséieren", "d'Leit fir de Klimawandel", "sensibiliséiert"),
  fr=FR(fr_er("sensibilis"), "les gens au changement climatique"),
  de=DE(*de_weak("sensibilisier"), "sensibilisiert", "die Leute für den Klimawandel"),
  en=EN("sensitise", "sensitises", "sensitised", "sensitising", "sensitised", "people to climate change"),
  fa=FA("مردم را نسبت به تغییرات اقلیمی آگاه", "کن", "کرد", sp=""))

# 13 separate
S.add("separéieren",
  lb=LB("separéieren", "d'Eeër", "separéiert"),
  fr=FR(fr_er("sépar"), "les œufs"),
  de=DE(*de_weak("trenn"), "getrennt", "die Eier"),
  en=EN("separate", "separates", "separated", "separating", "separated", "the eggs"),
  fa=FA("تخم" + Z + "مرغ" + Z + "ها را جدا", "کن", "کرد", sp=""))

# 14 sit
S.add("sëtzen",
  lb=LB("sëtzen", "um Sofa", "gesiess"),
  fr=FR(FR_ETRE, "assis sur le canapé"),
  de=DE(["sitze", "sitzt", "sitzt", "sitzen", "sitzt", "sitzen"],
        ["saß", "saßest", "saß", "saßen", "saßt", "saßen"], "gesessen", "auf dem Sofa"),
  en=EN("sit", "sits", "sat", "sitting", "sat", "on the sofa"),
  fa=FA("روی مبل", "نشین", "نشست"))

# 15 put
S.add("setzen",
  lb=LB("setzen", "d'Kand op de Stull", "gesat"),
  fr=FR(fr_irr(["mets", "mets", "met", "mettons", "mettez", "mettent"], "mis",
               ["mis", "mis", "mit", "mîmes", "mîtes", "mirent"], "mettr"),
        "l'enfant sur la chaise"),
  de=DE(*de_weak("setz", sib=True), "gesetzt", "das Kind auf den Stuhl"),
  en=EN("put", "puts", "put", "putting", "put", "the child on the chair"),
  fa=FA("کودک را روی صندلی", "گذار", "گذاشت"))

# 16 dissect
S.add("sezéieren",
  lb=LB("sezéieren", "e Fräsch am Labo", "sezéiert"),
  fr=FR(fr_er("disséqu", "dissèqu", "disséquer"), "une grenouille au laboratoire"),
  de=DE(*de_weak("sezier"), "seziert", "einen Frosch im Labor"),
  en=EN("dissect", "dissects", "dissected", "dissecting", "dissected", "a frog in the lab"),
  fa=FA("یک قورباغه را در آزمایشگاه کالبدشکافی", "کن", "کرد", sp=""))

# 17 share
S.add("sharen",
  lb=LB("sharen", "e Stéck Kuch mat anere", "geshart"),
  fr=FR(fr_er("partag"), "un morceau de gâteau avec les autres"),
  de=DE(*de_weak("teil"), "geteilt", "ein Stück Kuchen mit den anderen"),
  en=EN("share", "shares", "shared", "sharing", "shared", "a piece of cake with the others"),
  fa=FA("یک تکه کیک را با دیگران به اشتراک", "گذار", "گذاشت"))

# 18 look for
S.add("sichen",
  lb=LB("sichen", "d'Schlëssel", "gesicht"),
  fr=FR(fr_er("cherch"), "les clés"),
  de=DE(*de_weak("such"), "gesucht", "die Schlüssel"),
  en=EN("look for", "looks for", "looked for", "looking for", "looked for", "the keys"),
  fa=FA("دنبال کلیدها", "گرد", "گشت"))

# 19 seep
S.add("sickeren",
  lb=LB("sickeren", "an de Buedem", "gesickert", aux="sinn"),
  fr=FR(fr_er("filtr"), "dans le sol"),
  de=DE(*de_weak("sicker"), "gesickert", "in den Boden", aux="sein"),
  en=EN("seep", "seeps", "seeped", "seeping", "seeped", "into the ground"),
  fa=FA("به داخل زمین", "تراو", "تراوید",
        pres6=["می‌تراوم", "می‌تراوی", "می‌تراود", "می‌تراویم", "می‌تراوید", "می‌تراوند"],
        subj6=["بتراوم", "بتراوی", "بتراود", "بتراویم", "بتراوید", "بتراوند"]))

# 20 sieve
S.add("siften",
  lb=LB("siften", "d'Miel", "gesift", pres=["siften", "sifts", "sift", "siften", "sift", "siften"]),
  fr=FR(fr_er("tamis"), "la farine"),
  de=DE(*de_weak("sieb"), "gesiebt", "das Mehl"),
  en=EN("sieve", "sieves", "sieved", "sieving", "sieved", "the flour"),
  fa=FA("آرد را الک", "کن", "کرد", sp=""))

# 21 signpost
S.add("signaliséieren",
  lb=LB("signaliséieren", "d'Ëmleeung", "signaliséiert"),
  fr=FR(fr_er("signalis"), "la déviation"),
  de=DE(*de_weak("schilder"), "ausgeschildert", "die Umleitung", part="aus", inf="ausschildern"),
  en=EN("signpost", "signposts", "signposted", "signposting", "signposted", "the detour"),
  fa=FA("مسیر انحرافی را علامت" + Z + "گذاری", "کن", "کرد", sp=""))

# 22 sign (autograph)
S.add("signéieren",
  lb=LB("signéieren", "d'Buch", "signéiert"),
  fr=FR(fr_er("sign"), "le livre"),
  de=DE(*de_weak("signier"), "signiert", "das Buch"),
  en=EN("sign", "signs", "signed", "signing", "signed", "the book"),
  fa=FA("کتاب را امضا", "کن", "کرد", sp=""))

# 23 simplify
S.add("simplifiéieren",
  lb=LB("simplifiéieren", "d'Prozedur", "simplifiéiert"),
  fr=FR(fr_er("simplifi"), "la procédure"),
  de=DE(*de_weak("simplifizier"), "simplifiziert", "das Verfahren"),
  en=EN("simplify", "simplifies", "simplified", "simplifying", "simplified", "the procedure"),
  fa=FA("فرآیند را ساده", "کن", "کرد", sp=""))

# 24 feign
S.add("simuléieren",
  lb=LB("simuléieren", "eng Krankheet", "simuléiert"),
  fr=FR(fr_er("simul"), "une maladie"),
  de=DE(*de_weak("simulier"), "simuliert", "eine Krankheit"),
  en=EN("feign", "feigns", "feigned", "feigning", "feigned", "an illness"),
  fa=FA("تظاهر به بیماری", "کن", "کرد", sp=""))

# 25 be
S.add("sinn",
  lb=LB("sinn", "gedëlleg", "gewiescht", pres=["sinn", "bass", "ass", "sinn", "sidd", "sinn"], aux="sinn"),
  fr=FR(FR_ETRE, ["patient", "patient", "patient", "patients", "patients", "patients"]),
  de=DE(["bin", "bist", "ist", "sind", "seid", "sind"], ["war", "warst", "war", "waren", "wart", "waren"],
        "gewesen", "geduldig", aux="sein", inf="sein", sub=["bin", "bist", "ist", "sind", "seid", "sind"]),
  en=EN("be", "is", "was", "being", "been", "patient",
        pres=["am", "are", "is", "are", "are", "are"], past6=["was", "were", "was", "were", "were", "were"]),
  fa=FA("صبور", "باش", "بود", sp="", pres6=FA_BE_PRES, subj6=FA_BE_SUBJ))

# 26 sip
S.add("sippen",
  lb=LB("sippen", "den Téi", "gesippt"),
  fr=FR(fr_er("sirot"), "le thé"),
  de=DE(*de_weak("süffel"), "gesüffelt", "den Tee"),
  en=EN("sip", "sips", "sipped", "sipping", "sipped", "the tea"),
  fa=FA("چای را جرعه" + Z + "جرعه", "نوش", "نوشید"))

# 27 scandalize
S.add("skandaliséieren",
  lb=LB("skandaliséieren", "d'Publikum", "skandaliséiert"),
  fr=FR(fr_er("scandalis"), "le public"),
  de=DE(*de_weak("schockier"), "schockiert", "das Publikum"),
  en=EN("scandalize", "scandalizes", "scandalized", "scandalizing", "scandalized", "the audience"),
  fa=FA("تماشاگران را شوکه", "کن", "کرد", sp=""))

# 28 sketch
S.add("skizzéieren",
  lb=LB("skizzéieren", "e Porträt", "skizzéiert"),
  fr=FR(fr_er("esquiss"), "un portrait"),
  de=DE(*de_weak("skizzier"), "skizziert", "ein Porträt"),
  en=EN("sketch", "sketches", "sketched", "sketching", "sketched", "a portrait"),
  fa=FA("از یک پرتره طرح", "زن", "زد"))

# 29 sniff
S.add("sniffen",
  lb=LB("sniffen", "d'Bluem", "gesnifft"),
  fr=FR(fr_er("renifl"), "la fleur"),
  de=DE(*de_weak("schnüffel"), "geschnüffelt", "an der Blume"),
  en=EN("sniff", "sniffs", "sniffed", "sniffing", "sniffed", "the flower"),
  fa=FA("گل را بو", "کش", "کشید"))

# 30 say
S.add("soen",
  lb=LB("soen", "Moien", "gesot", pres=["soen", "séiss", "seet", "soen", "sot", "soen"]),
  fr=FR(fr_irr(["dis", "dis", "dit", "disons", "dites", "disent"], "dit",
               ["dis", "dis", "dit", "dîmes", "dîtes", "dirent"], "dir"), "bonjour"),
  de=DE(*de_weak("sag"), "gesagt", "Hallo"),
  en=EN("say", "says", "said", "saying", "said", "hello"),
  fa=FA("سلام", "گو", "گفت",
        pres6=["می‌گویم", "می‌گویی", "می‌گوید", "می‌گوییم", "می‌گویید", "می‌گویند"],
        subj6=["بگویم", "بگویی", "بگوید", "بگوییم", "بگویید", "بگویند"]))

# 31 sell off
S.add("soldéieren",
  lb=LB("soldéieren", "d'Wanterjacken zum hallwe Präis", "soldéiert"),
  fr=FR(fr_er("sold"), "les vestes d'hiver à moitié prix"),
  de=DE(*de_weak("verkauf"), "verkauft", "die Winterjacken zum halben Preis"),
  en=EN("sell off", "sells off", "sold off", "selling off", "sold off", "the winter jackets at half price"),
  fa=FA("ژاکت‌های زمستانی را به نصف قیمت", "فروش", "فروخت"))

# 32 should
S.add("sollen",
  lb=LB("sollen", "", "méi laang schlofe sollen", pres=["soll", "solls", "soll", "sollen", "sollt", "sollen"],
        part="méi laang schlofen", inf_full="méi laang schlofe sollen",
        sub=["méi laang schlofe soll", "méi laang schlofe solls", "méi laang schlofe soll",
             "méi laang schlofe sollen", "méi laang schlofe sollt", "méi laang schlofe sollen"]),
  fr=FR(fr_irr(["dois", "dois", "doit", "devons", "devez", "doivent"], "dû",
               ["dus", "dus", "dut", "dûmes", "dûtes", "durent"], "devr",
               subj=["doive", "doives", "doive", "devions", "deviez", "doivent"]),
        "dormir plus longtemps"),
  de=DE(["soll", "sollst", "soll", "sollen", "sollt", "sollen"],
        ["sollte", "solltest", "sollte", "sollten", "solltet", "sollten"],
        "länger schlafen sollen", "", part="länger schlafen", inf="länger schlafen sollen",
        sub=["länger schlafen soll", "länger schlafen sollst", "länger schlafen soll",
             "länger schlafen sollen", "länger schlafen sollt", "länger schlafen sollen"]),
  en=EN("be supposed to sleep", "is supposed to sleep", "was supposed to sleep", "being supposed to sleep",
        "been supposed to sleep", "longer", pres=["should sleep"] * 6),
  fa=FA("به خوابیدن بیشتر موظف", "باش", "بود", sp="", pres6=FA_BE_PRES, subj6=FA_BE_SUBJ))

# 33 salt / cure
S.add("solperen",
  lb=LB("solperen", "d'Fleesch", "gesolpert"),
  fr=FR(fr_er("sal"), "la viande"),
  de=DE(*de_weak("pökel"), "gepökelt", "das Fleisch"),
  en=EN("salt", "salts", "salted", "salting", "salted", "the meat"),
  fa=FA("گوشت را نمک" + Z + "سود", "کن", "کرد", sp=""))

# 34 sound out
S.add("sondéieren",
  lb=LB("sondéieren", "d'Meenung vun de Leit", "sondéiert"),
  fr=FR(fr_er("sond"), "l'opinion des gens"),
  de=DE(*de_weak("sondier"), "sondiert", "die Meinung der Leute"),
  en=EN("sound out", "sounds out", "sounded out", "sounding out", "sounded out", "people's opinions"),
  fa=FA("نظر مردم را", "سنج", "سنجید"))

# 35 sort
S.add("sortéieren",
  lb=LB("sortéieren", "d'Bréiwer", "sortéiert"),
  fr=FR(fr_er("tri"), "le courrier"),
  de=DE(*de_weak("sortier"), "sortiert", "die Briefe"),
  en=EN("sort", "sorts", "sorted", "sorting", "sorted", "the letters"),
  fa=FA("نامه‌ها را مرتب", "کن", "کرد", sp=""))

# 36 whimper
S.add("soueren",
  lb=LB("soueren", "an der Nuecht", "gesouert"),
  fr=FR(fr_ir("gém"), "pendant la nuit"),
  de=DE(*de_weak("wimmer"), "gewimmert", "in der Nacht"),
  en=EN("whimper", "whimpers", "whimpered", "whimpering", "whimpered", "in the night"),
  fa=FA("در شب ناله", "کن", "کرد", sp=""))

# 37 suspect
S.add("soupçonéieren",
  lb=LB("soupçonéieren", "den Noper", "soupçonéiert"),
  fr=FR(fr_er("soupçonn"), "le voisin"),
  de=DE(*de_weak("verdächtig"), "verdächtigt", "den Nachbarn"),
  en=EN("suspect", "suspects", "suspected", "suspecting", "suspected", "the neighbour"),
  fa=FA("به همسایه شک", "کن", "کرد", sp=""))

# 38 joke
S.add("spaassen",
  lb=LB("spaassen", "mat de Kollegen", "gespaasst"),
  fr=FR(fr_er("plaisant"), "avec les collègues"),
  de=DE(*de_weak("spaß", sib=True), "gespaßt", "mit den Kollegen"),
  en=EN("joke", "jokes", "joked", "joking", "joked", "with the colleagues"),
  fa=FA("با همکاران شوخی", "کن", "کرد", sp=""))

# 39 fill in
S.add("spachtelen",
  lb=LB("spachtelen", "d'Lächer an der Mauer", "gespachtelt"),
  fr=FR(fr_er("colmat"), "les trous du mur"),
  de=DE(*de_weak("spachtel"), "gespachtelt", "die Löcher in der Wand"),
  en=EN("fill", "fills", "filled", "filling", "filled", "the holes in the wall"),
  fa=FA("سوراخ‌های دیوار را پر", "کن", "کرد", sp=""))

# 40 go for a walk
S.add("spadséieren",
  lb=LB("spadséieren", "am Park", "spadséiert", aux="sinn"),
  fr=FR(fr_er("promen", "promèn", "promèner"), "dans le parc", aux="être", refl=True),
  de=DE(*de_weak("spazier"), "spaziert", "im Park", aux="sein"),
  en=EN("walk", "walks", "walked", "walking", "walked", "in the park"),
  fa=FA("در پارک قدم", "زن", "زد"))

# 41 store
S.add("späicheren",
  lb=LB("späicheren", "d'Datei um Computer", "gespäichert"),
  fr=FR(fr_er("stock"), "le fichier sur l'ordinateur"),
  de=DE(*de_weak("speicher"), "gespeichert", "die Datei auf dem Computer"),
  en=EN("store", "stores", "stored", "storing", "stored", "the file on the computer"),
  fa=FA("فایل را روی رایانه ذخیره", "کن", "کرد", sp=""))

# 42 spit
S.add("späizen",
  lb=LB("späizen", "d'Kiischtekären an d'Schossel", "gespäizt"),
  fr=FR(fr_er("crach"), "les noyaux de cerise dans le bol"),
  de=DE(*de_weak("spuck"), "gespuckt", "die Kirschkerne in die Schüssel"),
  en=EN("spit", "spits", "spat", "spitting", "spat", "the cherry stones into the bowl"),
  fa=FA("هسته‌های گیلاس را در کاسه تف", "کن", "کرد", sp=""))

# 43 stretch
S.add("spanen",
  lb=LB("spanen", "e Seel tëscht de Beem", "gespaant"),
  fr=FR(fr_re("tend"), "une corde entre les arbres"),
  de=DE(*de_weak("spann"), "gespannt", "ein Seil zwischen den Bäumen"),
  en=EN("stretch", "stretches", "stretched", "stretching", "stretched", "a rope between the trees"),
  fa=FA("یک طناب را بین درخت‌ها", "کش", "کشید"))

# 44 spin
S.add("spannen",
  lb=LB("spannen", "d'Woll", "gesponn"),
  fr=FR(fr_er("fil"), "la laine"),
  de=DE(["spinne", "spinnst", "spinnt", "spinnen", "spinnt", "spinnen"],
        ["spann", "spannst", "spann", "spannen", "spannt", "spannen"], "gesponnen", "die Wolle"),
  en=EN("spin", "spins", "spun", "spinning", "spun", "the wool"),
  fa=FA("پشم را", "ریس", "ریسید"))

# 45 close
S.add("spären",
  lb=LB("spären", "d'Strooss", "gespaart"),
  fr=FR(fr_er("ferm"), "la rue"),
  de=DE(*de_weak("sperr"), "gesperrt", "die Straße"),
  en=EN("close", "closes", "closed", "closing", "closed", "the street"),
  fa=FA("خیابان را", "بند", "بست"))

# 46 speculate
S.add("spekuléieren",
  lb=LB("spekuléieren", "op der Bourse", "spekuléiert"),
  fr=FR(fr_er("spécul"), "en bourse"),
  de=DE(*de_weak("spekulier"), "spekuliert", "an der Börse"),
  en=EN("speculate", "speculates", "speculated", "speculating", "speculated", "on the stock market"),
  fa=FA("در بورس سفته" + Z + "بازی", "کن", "کرد", sp=""))

# 47 pod
S.add("spellen",
  lb=LB("spellen", "d'Äerbsen", "gespellt"),
  fr=FR(fr_er("écoss"), "les petits pois"),
  de=DE(*de_weak("enthüls", sib=True), "enthülst", "die Erbsen"),
  en=EN("pod", "pods", "podded", "podding", "podded", "the peas"),
  fa=FA("نخودفرنگی‌ها را پوست", "کن", "کند"))

# 48 donate
S.add("spenden",
  lb=LB("spenden", "Suen fir déi Aarm", "gespend", pres=["spenden", "spends", "spent", "spenden", "spent", "spenden"]),
  fr=FR(fr_er("donn"), "de l'argent aux pauvres"),
  de=DE(*de_weak("spend", dt=True), "gespendet", "Geld für die Armen"),
  en=EN("donate", "donates", "donated", "donating", "donated", "money to the poor"),
  fa=FA("به فقرا پول اهدا", "کن", "کرد", sp=""))

# 49 pin
S.add("spéngelen",
  lb=LB("spéngelen", "de Stoff", "gespéngelt"),
  fr=FR(fr_er("épingl"), "le tissu"),
  de=DE(*de_weak("steck"), "abgesteckt", "den Stoff", part="ab", inf="abstecken"),
  en=EN("pin", "pins", "pinned", "pinning", "pinned", "the fabric"),
  fa=FA("پارچه را سنجاق", "کن", "کرد", sp=""))
