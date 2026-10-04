# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

SUBJ_IBEN = ["ب"]
def _fa_say(ctx):
    return FA(ctx, "گو", "گفت",
              pres6=["می‌گویم","می‌گویی","می‌گوید","می‌گوییم","می‌گویید","می‌گویند"],
              subj6=["بگویم","بگویی","بگوید","بگوییم","بگویید","بگویند"])

S.add("schären",
  lb=LB("schären", "d'Stuff", "geschärt"),
  fr=FR(fr_er("balay", "balai", "balaier"), "la pièce"),
  de=DE(*de_weak("feg"), "gefegt", "das Zimmer"),
  en=EN("sweep", "sweeps", "swept", "sweeping", "swept", "the room"),
  fa=FA("اتاق را جارو", "کن", "کرد", sp=""))

S.add("scharjeekelen",
  lb=LB("scharjeekelen", "duerch d'Stad", "gescharjeekelt", aux="sinn"),
  fr=FR(fr_er("traîn"), "dans la ville", aux="être", refl=True),
  de=DE(*de_weak("schlender"), "geschlendert", "durch die Stadt", aux="sein"),
  en=EN("plod", "plods", "plodded", "plodding", "plodded", "through the town"),
  fa=FA("خود را در شهر", "کش", "کشید"))

S.add("schässen",
  lb=LB("schässen", "d'Kaz aus der Kichen", "geschässt"),
  fr=FR(fr_er("chass"), "le chat hors de la cuisine"),
  de=DE(["werfe","wirfst","wirft","werfen","werft","werfen"],
        ["warf","warfst","warf","warfen","warft","warfen"],
        "hinausgeworfen", "die Katze aus der Küche", part="hinaus", inf="hinauswerfen"),
  en=EN("throw out", "throws out", "threw out", "throwing out", "thrown out", "the cat"),
  fa=FA("گربه را از آشپزخانه بیرون", "انداز", "انداخت",
        subj6=["بیندازم","بیندازی","بیندازد","بیندازیم","بیندازید","بیندازند"]))

S.add("schätzen",
  lb=LB("schätzen", "d'Gewiicht vum Kuch", "geschätzt"),
  fr=FR(fr_er("estim"), "le poids du gâteau"),
  de=DE(*de_weak("schätz", sib=True), "geschätzt", "das Gewicht des Kuchens"),
  en=EN("guess", "guesses", "guessed", "guessing", "guessed", "the weight of the cake"),
  fa=FA("وزن کیک را حدس", "زن", "زد"))

S.add("schaueren",
  lb=LB("schaueren", "de Pott", "geschauert"),
  fr=FR(fr_er("récur"), "la casserole"),
  de=DE(*de_weak("scheuer"), "gescheuert", "den Topf"),
  en=EN("scour", "scours", "scoured", "scouring", "scoured", "the pot"),
  fa=FA("قابلمه را", "ساب", "سابید"))

S.add("schaukelen",
  lb=LB("schaukelen", "d'Bëbee", "geschaukelt"),
  fr=FR(fr_er("berc"), "le bébé"),
  de=DE(*de_weak("wieg"), "gewiegt", "das Baby"),
  en=EN("rock", "rocks", "rocked", "rocking", "rocked", "the baby"),
  fa=FA("نوزاد را تاب", "ده", "داد"))

S.add("schauteren",
  lb=LB("schauteren", "d'Haut mat engem rauen Tuch", "geschautert"),
  fr=FR(fr_er("gratt"), "la peau avec un tissu rugueux"),
  de=DE(*de_weak("scheuer"), "gescheuert", "die Haut mit einem rauen Tuch"),
  en=EN("chafe", "chafes", "chafed", "chafing", "chafed", "the skin with a rough cloth"),
  fa=FA("پوست را با پارچه زبر", "ساب", "سابید"))

S.add("schécken",
  lb=LB("schécken", "e Bréif un e Frënd", "geschéckt"),
  fr=FR(fr_irr(["envoie","envoies","envoie","envoyons","envoyez","envoient"], "envoyé",
               ["envoyai","envoyas","envoya","envoyâmes","envoyâtes","envoyèrent"], "enverr"),
        "une lettre à un ami"),
  de=DE(*de_weak("schick"), "geschickt", "einen Brief an einen Freund"),
  en=EN("send", "sends", "sent", "sending", "sent", "a letter to a friend"),
  fa=FA("نامه‌ای برای یک دوست", "فرست", "فرستاد"))

S.add("schëdden",
  lb=LB("schëdden", "Waasser an d'Glas", "geschott",
        pres=["schëdden","schëdds","schëdd","schëdden","schëdd","schëdden"]),
  fr=FR(fr_er("vers"), "de l'eau dans le verre"),
  de=DE(*de_weak("schütt", dt=True), "geschüttet", "Wasser ins Glas"),
  en=EN("pour", "pours", "poured", "pouring", "poured", "water into the glass"),
  fa=FA("آب را در لیوان", "ریز", "ریخت"))

S.add("scheekeren",
  lb=LB("scheekeren", "mat der Serveuse", "gescheekert"),
  fr=FR(fr_er("flirt"), "avec la serveuse"),
  de=DE(*de_weak("schäker"), "geschäkert", "mit der Kellnerin"),
  en=EN("flirt", "flirts", "flirted", "flirting", "flirted", "with the waitress"),
  fa=FA("با پیشخدمت لاس", "زن", "زد"))

S.add("scheien",
  lb=LB("scheien", "de grousse Hond", "gescheit"),
  fr=FR(fr_er("évit"), "le gros chien"),
  de=DE(*de_weak("scheu"), "gescheut", "den großen Hund"),
  en=EN("shy away from", "shies away from", "shied away from", "shying away from", "shied away from", "the big dog"),
  fa=FA("از سگ بزرگ دوری", "کن", "کرد", sp=""))

S.add("schéirieden",
  lb=LB("rieden", "d'Situatioun", "schéigeriedt", part="schéi",
        pres=["rieden","rieds","riedt","rieden","riedt","rieden"], inf_full="schéirieden"),
  fr=FR(fr_er("enjoliv"), "la situation"),
  de=DE(*de_weak("red", dt=True), "schöngeredet", "die Lage", part="schön", inf="schönreden"),
  en=EN("gloss over", "glosses over", "glossed over", "glossing over", "glossed over", "the situation"),
  fa=FA("وضعیت را زیبا جلوه", "ده", "داد"))

S.add("schéissen",
  lb=LB("schéissen", "op d'Zilscheif", "geschoss"),
  fr=FR(fr_er("tir"), "sur la cible"),
  de=DE(["schieße","schießt","schießt","schießen","schießt","schießen"],
        ["schoss","schossest","schoss","schossen","schosst","schossen"],
        "geschossen", "auf die Zielscheibe"),
  en=EN("shoot", "shoots", "shot", "shooting", "shot", "at the target"),
  fa=FA("به سمت هدف تیراندازی", "کن", "کرد", sp=""))

S.add("scheiteren",
  lb=LB("scheiteren", "bei der Prüfung", "gescheitert", aux="sinn"),
  fr=FR(fr_er("échou"), "à l'examen"),
  de=DE(*de_weak("scheiter"), "gescheitert", "an der Prüfung", aux="sein"),
  en=EN("fail", "fails", "failed", "failing", "failed", "the exam"),
  fa=FA("در امتحان شکست", "خور", "خورد"))

S.add("schellen",
  lb=LB("schellen", "un der Dier", "geschellt"),
  fr=FR(fr_er("sonn"), "à la porte"),
  de=DE(*de_weak("klingel"), "geklingelt", "an der Tür"),
  en=EN("ring", "rings", "rang", "ringing", "rung", "the doorbell"),
  fa=FA("زنگ در را", "زن", "زد"))

S.add("schematiséieren",
  lb=LB("schematiséieren", "de Prozess", "schematiséiert"),
  fr=FR(fr_er("schématis"), "le processus"),
  de=DE(*de_weak("schematisier"), "schematisiert", "den Prozess"),
  en=EN("schematize", "schematizes", "schematized", "schematizing", "schematized", "the process"),
  fa=FA("فرایند را طرح‌بندی", "کن", "کرد", sp=""))

S.add("schéngen",
  lb=LB("schéngen", "hell an der Däischtert", "geschéngt"),
  fr=FR(fr_er("brill"), "dans le noir"),
  de=DE(["scheine","scheinst","scheint","scheinen","scheint","scheinen"],
        ["schien","schienst","schien","schienen","schient","schienen"],
        "geschienen", "hell im Dunkeln"),
  en=EN("shine", "shines", "shone", "shining", "shone", "brightly in the dark"),
  fa=FA("در تاریکی", "درخش", "درخشید"))

S.add("schenken",
  lb=LB("schenken", "engem Frënd e Buch", "geschenkt"),
  fr=FR(fr_irr(["offre","offres","offre","offrons","offrez","offrent"], "offert",
               ["offris","offris","offrit","offrîmes","offrîtes","offrirent"], "offrir"),
        "un livre à un ami"),
  de=DE(*de_weak("schenk"), "geschenkt", "einem Freund ein Buch"),
  en=EN("give", "gives", "gave", "giving", "given", "a friend a book"),
  fa=FA("به یک دوست یک کتاب هدیه", "ده", "داد"))

S.add("schënnen",
  lb=LB("schënnen", "den Hues", "geschënnt"),
  fr=FR(fr_er("écorch"), "le lièvre"),
  de=DE(*de_weak("häut", dt=True), "gehäutet", "den Hasen"),
  en=EN("flay", "flays", "flayed", "flaying", "flayed", "the hare"),
  fa=FA("پوست خرگوش را", "کن", "کند"))

S.add("schëppen",
  lb=LB("schëppen", "de Schnéi", "geschëppt"),
  fr=FR(fr_er("pellet"), "la neige"),
  de=DE(*de_weak("schaufel"), "geschaufelt", "den Schnee"),
  en=EN("shovel", "shovels", "shoveled", "shoveling", "shoveled", "the snow"),
  fa=FA("برف را بیل", "زن", "زد"))

S.add("schiedegen",
  lb=LB("schiedegen", "de Client", "geschiedegt"),
  fr=FR(fr_er("lés", "lès", "lèser"), "le client"),
  de=DE(*de_weak("schädig"), "geschädigt", "den Kunden"),
  en=EN("wrong", "wrongs", "wronged", "wronging", "wronged", "the customer"),
  fa=FA("به مشتری ضرر", "زن", "زد"))

S.add("schielen",
  lb=LB("schielen", "d'Gromperen", "geschielt"),
  fr=FR(fr_er("épluch"), "les pommes de terre"),
  de=DE(*de_weak("schäl"), "geschält", "die Kartoffeln"),
  en=EN("peel", "peels", "peeled", "peeling", "peeled", "the potatoes"),
  fa=FA("پوست سیب‌زمینی‌ها را", "کن", "کند"))

S.add("schieren",
  lb=LB("schieren", "d'Schof", "geschuer"),
  fr=FR(fr_re("tond"), "les moutons"),
  de=DE(["schere","scherst","schert","scheren","schert","scheren"],
        ["schor","schorst","schor","schoren","schort","schoren"],
        "geschoren", "die Schafe"),
  en=EN("shear", "shears", "sheared", "shearing", "shorn", "the sheep"),
  fa=FA("پشم گوسفندها را", "چین", "چید"))

S.add("schierpsen",
  lb=LB("schierpsen", "an der Heck", "geschierpst"),
  fr=FR(fr_er("stridul"), "dans la haie"),
  de=DE(*de_weak("zirp"), "gezirpt", "in der Hecke"),
  en=EN("chirp", "chirps", "chirped", "chirping", "chirped", "in the hedge"),
  fa=FA("در پرچین جیک‌جیک", "کن", "کرد", sp=""))

S.add("schiffen",
  lb=LB("schiffen", "un de Bam", "geschifft"),
  fr=FR(fr_er("piss"), "contre un arbre"),
  de=DE(*de_weak("schiff"), "geschifft", "an den Baum"),
  en=EN("pee", "pees", "peed", "peeing", "peed", "against a tree"),
  fa=FA("کنار درخت ادرار", "کن", "کرد", sp=""))

S.add("schifgoen",
  lb=LB("goen", "mat dem Plang", "schifgaang", pres=["ginn","gees","geet","ginn","gitt","ginn"],
        aux="sinn", part="schif", inf_full="schifgoen",
        sub=["schifginn","schifgees","schifgeet","schifginn","schifgitt","schifginn"]),
  fr=FR(fr_er("échou"), "dans ce plan"),
  de=DE(["gehe","gehst","geht","gehen","geht","gehen"], ["ging","gingst","ging","gingen","gingt","gingen"],
        "schiefgegangen", "mit dem Plan", aux="sein", part="schief", inf="schiefgehen"),
  en=EN("go wrong", "goes wrong", "went wrong", "going wrong", "gone wrong", "with the plan"),
  fa=FA("در این نقشه شکست", "خور", "خورد"))

S.add("schikanéieren",
  lb=LB("schikanéieren", "de Kolleeg", "schikanéiert"),
  fr=FR(fr_er("brim"), "le collègue"),
  de=DE(*de_weak("schikanier"), "schikaniert", "den Kollegen"),
  en=EN("harass", "harasses", "harassed", "harassing", "harassed", "the colleague"),
  fa=FA("همکار را اذیت", "کن", "کرد", sp=""))

S.add("schimmeren",
  lb=LB("schimmeren", "am Liicht", "geschimmert"),
  fr=FR(fr_er("scintill"), "dans la lumière"),
  de=DE(*de_weak("schimmer"), "geschimmert", "im Licht"),
  en=EN("shimmer", "shimmers", "shimmered", "shimmering", "shimmered", "in the light"),
  fa=FA("در نور سوسو", "زن", "زد"))

S.add("schinnen",
  lb=LB("schinnen", "e gebrachenen Aarm", "geschinnt"),
  fr=FR(fr_er("éclis"), "un bras cassé"),
  de=DE(*de_weak("schien"), "geschient", "einen gebrochenen Arm"),
  en=EN("splint", "splints", "splinted", "splinting", "splinted", "a broken arm"),
  fa=FA("دست شکسته را آتل", "بند", "بست"))

S.add("schlabberen",
  lb=LB("schlabberen", "d'Mëllech", "geschlabbert"),
  fr=FR(fr_er("lap"), "le lait"),
  de=DE(*de_weak("schlabber"), "geschlabbert", "die Milch"),
  en=EN("lap up", "laps up", "lapped up", "lapping up", "lapped up", "the milk"),
  fa=FA("شیر را لیس", "زن", "زد"))

S.add("schläifen",
  lb=LB("schläifen", "d'Messer", "geschläift"),
  fr=FR(fr_er("aiguis"), "le couteau"),
  de=DE(["schleife","schleifst","schleift","schleifen","schleift","schleifen"],
        ["schliff","schliffst","schliff","schliffen","schlifft","schliffen"],
        "geschliffen", "das Messer"),
  en=EN("sharpen", "sharpens", "sharpened", "sharpening", "sharpened", "the knife"),
  fa=FA("چاقو را تیز", "کن", "کرد", sp=""))

S.add("schläimen",
  lb=LB("schläimen", "beim Chef", "geschläimt"),
  fr=FR(fr_irr(["fais","fais","fait","faisons","faites","font"], "fait",
               ["fis","fis","fit","fîmes","fîtes","firent"], "fer",
               subj=["fasse","fasses","fasse","fassions","fassiez","fassent"],
               imp=["faisais","faisais","faisait","faisions","faisiez","faisaient"]),
        "de la lèche au chef"),
  de=DE(*de_weak("schleim"), "geschleimt", "beim Chef"),
  en=EN("crawl", "crawls", "crawled", "crawling", "crawled", "to the boss"),
  fa=FA("پیش رئیس چاپلوسی", "کن", "کرد", sp=""))

S.add("schläissen",
  lb=LB("schläissen", "d'Bounen", "geschläisst"),
  fr=FR(fr_er("effil"), "les haricots"),
  de=DE(*de_weak("fädel"), "abgefädelt", "die Bohnen", part="ab", inf="abfädeln"),
  en=EN("string", "strings", "strung", "stringing", "strung", "the beans"),
  fa=FA("لوبیاها را پاک", "کن", "کرد", sp=""))

S.add("schlappen",
  lb=LB("schlappen", "duerch de Gank", "geschlappt", aux="sinn"),
  fr=FR(fr_er("traîn"), "les pieds dans le couloir"),
  de=DE(*de_weak("schlurf"), "geschlurft", "durch den Flur", aux="sein"),
  en=EN("shuffle", "shuffles", "shuffled", "shuffling", "shuffled", "along the hallway"),
  fa=FA("در راهرو پاکشان راه", "رو", "رفت",
        pres6=["می‌روم","می‌روی","می‌رود","می‌رویم","می‌روید","می‌روند"],
        subj6=["بروم","بروی","برود","برویم","بروید","بروند"]))

S.add("schlécken",
  lb=LB("schlécken", "d'Pëll", "geschléckt"),
  fr=FR(fr_er("aval"), "le comprimé"),
  de=DE(*de_weak("schluck"), "geschluckt", "die Tablette"),
  en=EN("swallow", "swallows", "swallowed", "swallowing", "swallowed", "the pill"),
  fa=FA("قرص را قورت", "ده", "داد"))

S.add("schleefen",
  lb=LB("schleefen", "e schwéieren Sak iwwer de Buedem", "geschleeft"),
  fr=FR(fr_er("traîn"), "un lourd sac sur le sol"),
  de=DE(*de_weak("schleif"), "geschleift", "einen schweren Sack über den Boden"),
  en=EN("drag", "drags", "dragged", "dragging", "dragged", "a heavy sack across the floor"),
  fa=FA("یک کیسه سنگین را روی زمین", "کش", "کشید"))

S.add("schleideren",
  lb=LB("schleideren", "e Steen an de Floss", "geschleidert"),
  fr=FR(fr_er("lanc"), "une pierre dans la rivière"),
  de=DE(*de_weak("schleuder"), "geschleudert", "einen Stein in den Fluss"),
  en=EN("hurl", "hurls", "hurled", "hurling", "hurled", "a stone into the river"),
  fa=FA("یک سنگ را به رودخانه پرتاب", "کن", "کرد", sp=""))

S.add("schleisen",
  lb=LB("schleisen", "e Schëff duerch d'Schleis", "geschleist"),
  fr=FR(fr_er("éclus"), "un bateau"),
  de=DE(*de_weak("schleus", sib=True), "geschleust", "ein Schiff durch die Schleuse"),
  en=EN("lock", "locks", "locked", "locking", "locked", "a boat through the lock"),
  fa=FA("کشتی را از دریچه آب عبور", "ده", "داد"))

S.add("schléissen",
  lb=LB("schléissen", "d'Kand an d'Häerz", "geschloss"),
  fr=FR(fr_irr(["prends","prends","prend","prenons","prenez","prennent"], "pris",
               ["pris","pris","prit","prîmes","prîtes","prirent"], "prendr"),
        "l'enfant en affection"),
  de=DE(["schließe","schließt","schließt","schließen","schließt","schließen"],
        ["schloss","schlossest","schloss","schlossen","schlosst","schlossen"],
        "geschlossen", "das Kind ins Herz"),
  en=EN("take", "takes", "took", "taking", "taken", "the child to {pos} heart"),
  fa=FA("کودک را در دل{ps} جا", "ده", "داد"))

S.add("schlichten",
  lb=LB("schlichten", "de Sträit", "geschlicht",
        pres=["schlichten","schlichts","schlicht","schlichten","schlicht","schlichten"]),
  fr=FR(fr_er("régl", "règl", "régler"), "le conflit"),
  de=DE(*de_weak("schlicht", dt=True), "geschlichtet", "den Streit"),
  en=EN("settle", "settles", "settled", "settling", "settled", "the dispute"),
  fa=FA("اختلاف را حل", "کن", "کرد", sp=""))

S.add("schlidderen",
  lb=LB("schlidderen", "iwwer d'Äis", "geschliddert", aux="sinn"),
  fr=FR(fr_er("gliss"), "sur la glace"),
  de=DE(*de_weak("schlitter"), "geschlittert", "über das Eis", aux="sein"),
  en=EN("skid", "skids", "skidded", "skidding", "skidded", "on the ice"),
  fa=FA("روی یخ سر", "خور", "خورد"))

S.add("schloen",
  lb=LB("schloen", "op den Nol", "geschloen",
        pres=["schloen","schléis","schléit","schloen","schlot","schloen"]),
  fr=FR(fr_er("frapp"), "sur le clou"),
  de=DE(["schlage","schlägst","schlägt","schlagen","schlagt","schlagen"],
        ["schlug","schlugst","schlug","schlugen","schlugt","schlugen"],
        "geschlagen", "auf den Nagel"),
  en=EN("hit", "hits", "hit", "hitting", "hit", "the nail"),
  fa=FA("به میخ ضربه", "زن", "زد"))

S.add("schlofen",
  lb=LB("schlofen", "déif", "geschlof",
        pres=["schlofen","schléifs","schléift","schlofen","schlooft","schlofen"]),
  fr=FR(fr_irr(["dors","dors","dort","dormons","dormez","dorment"], "dormi",
               ["dormis","dormis","dormit","dormîmes","dormîtes","dormirent"], "dormir",
               subj=["dorme","dormes","dorme","dormions","dormiez","dorment"]),
        "profondément"),
  de=DE(["schlafe","schläfst","schläft","schlafen","schlaft","schlafen"],
        ["schlief","schliefst","schlief","schliefen","schlieft","schliefen"],
        "geschlafen", "tief"),
  en=EN("sleep", "sleeps", "slept", "sleeping", "slept", "deeply"),
  fa=FA("عمیق", "خواب", "خوابید"))

S.add("schluechten",
  lb=LB("schluechten", "e Schwäin", "geschluecht",
        pres=["schluechten","schluechts","schluecht","schluechten","schluecht","schluechten"]),
  fr=FR(fr_irr(["abats","abats","abat","abattons","abattez","abattent"], "abattu",
               ["abattis","abattis","abattit","abattîmes","abattîtes","abattirent"], "abattr"),
        "un cochon"),
  de=DE(*de_weak("schlacht", dt=True), "geschlachtet", "ein Schwein"),
  en=EN("slaughter", "slaughters", "slaughtered", "slaughtering", "slaughtered", "a pig"),
  fa=FA("یک خوک را سر", "بر", "برید",
        pres6=["می‌برم","می‌بری","می‌برد","می‌بریم","می‌برید","می‌برند"],
        subj6=["ببرم","ببری","ببرد","ببریم","ببرید","ببرند"]))

S.add("schluppen",
  lb=LB("schluppen", "d'Zopp", "geschluppt"),
  fr=FR(fr_er("sirot"), "la soupe"),
  de=DE(*de_weak("schlürf"), "geschlürft", "die Suppe"),
  en=EN("slurp", "slurps", "slurped", "slurping", "slurped", "the soup"),
  fa=FA("سوپ را هورت", "کش", "کشید"))

S.add("schmaachen",
  lb=LB("schmaachen", "d'Salz an der Zopp", "geschmaacht"),
  fr=FR(fr_irr(["sens","sens","sent","sentons","sentez","sentent"], "senti",
               ["sentis","sentis","sentit","sentîmes","sentîtes","sentirent"], "sentir"),
        "le sel dans la soupe"),
  de=DE(*de_weak("schmeck"), "geschmeckt", "das Salz in der Suppe"),
  en=EN("taste", "tastes", "tasted", "tasting", "tasted", "the salt in the soup"),
  fa=FA("طعم نمک را در سوپ حس", "کن", "کرد", sp=""))

S.add("schmäissen",
  lb=LB("schmäissen", "de Ball iwwer d'Mauer", "geschmass"),
  fr=FR(fr_er("jet", "jett", "jetter"), "la balle par-dessus le mur"),
  de=DE(["schmeiße","schmeißt","schmeißt","schmeißen","schmeißt","schmeißen"],
        ["schmiss","schmissest","schmiss","schmissen","schmisst","schmissen"],
        "geschmissen", "den Ball über die Mauer"),
  en=EN("throw", "throws", "threw", "throwing", "thrown", "the ball over the wall"),
  fa=FA("توپ را از روی دیوار پرت", "کن", "کرد", sp=""))

S.add("schmeechelen",
  lb=LB("schmeechelen", "dem Chef", "geschmeechelt"),
  fr=FR(fr_er("flatt"), "le chef"),
  de=DE(*de_weak("schmeichel"), "geschmeichelt", "dem Chef"),
  en=EN("flatter", "flatters", "flattered", "flattering", "flattered", "the boss"),
  fa=_fa_say("به رئیس تملق"))

S.add("schmidden",
  lb=LB("schmidden", "d'Eisen", "geschmiddt"),
  fr=FR(fr_er("forg"), "le fer"),
  de=DE(*de_weak("schmied", dt=True), "geschmiedet", "das Eisen"),
  en=EN("forge", "forges", "forged", "forging", "forged", "the iron"),
  fa=FA("آهن را شکل", "ده", "داد"))

S.add("schmieren",
  lb=LB("schmieren", "d'Kette vum Vëlo", "geschmiert"),
  fr=FR(fr_er("graiss"), "la chaîne du vélo"),
  de=DE(*de_weak("schmier"), "geschmiert", "die Fahrradkette"),
  en=EN("grease", "greases", "greased", "greasing", "greased", "the bike chain"),
  fa=FA("زنجیر دوچرخه را گریس", "زن", "زد"))
