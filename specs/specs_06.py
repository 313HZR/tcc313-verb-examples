# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

S.add("schmunzelen",
  lb=LB("schmunzelen", "iwwer de Witz", "geschmunzelt"),
  fr=FR(fr_irr(["souris","souris","sourit","sourions","souriez","sourient"], "souri",
               ["souris","souris","sourit","sourîmes","sourîtes","sourirent"], "sourir"), "à la blague"),
  de=DE(*de_weak("schmunzel"), "geschmunzelt", "über den Witz"),
  en=EN("grin", "grins", "grinned", "grinning", "grinned", "at the joke"),
  fa=FA("به شوخی لبخند", "زن", "زد"))

S.add("schnaarchen",
  lb=LB("schnaarchen", "d'ganz Nuecht", "geschnaarcht"),
  fr=FR(fr_er("ronfl"), "toute la nuit"),
  de=DE(*de_weak("schnarch"), "geschnarcht", "die ganze Nacht"),
  en=EN("snore", "snores", "snored", "snoring", "snored", "all night"),
  fa=FA("تمام شب خروپف", "کن", "کرد", sp=""))

S.add("schnabbelen",
  lb=LB("schnabbelen", "mat de Frënn", "geschnabbelt"),
  fr=FR(fr_er("bavard"), "avec les amis"),
  de=DE(*de_weak("schwatz", sib=True), "geschwatzt", "mit den Freunden"),
  en=EN("chatter", "chatters", "chattered", "chattering", "chattered", "with friends"),
  fa=FA("با دوستان وراجی", "کن", "کرد", sp=""))

S.add("schnadderen",
  lb=LB("schnadderen", "um Weiher", "geschnaddert"),
  fr=FR(fr_er("cancan"), "sur l'étang"),
  de=DE(*de_weak("schnatter"), "geschnattert", "am Teich"),
  en=EN("quack", "quacks", "quacked", "quacking", "quacked", "on the pond"),
  fa=FA("در برکه قات‌قات", "کن", "کرد", sp=""))

S.add("schnäizen",
  lb=LB("schnäizen", "{rd} d'Nues", "geschnäizt"),
  fr=FR(fr_er("mouch"), "dans un mouchoir", aux="être", refl=True),
  de=DE(*de_weak("schnäuz", sib=True), "geschnäuzt", "{rd} die Nase"),
  en=EN("blow", "blows", "blew", "blowing", "blown", "{pos} nose"),
  fa=FA("در دستمال فین", "کن", "کرد", sp=""))

S.add("schnallen",
  lb=LB("schnallen", "den Trick", "geschnallt"),
  fr=FR(fr_er("pig"), "le truc"),
  de=DE(*de_weak("schnall"), "geschnallt", "den Trick"),
  en=EN("get", "gets", "got", "getting", "got", "the trick"),
  fa=FA("ترفند را", "فهم", "فهمید"))

S.add("schnapen",
  lb=LB("schnapen", "frësch Loft am Gaart", "geschnapt"),
  fr=FR(fr_irr(["prends","prends","prend","prenons","prenez","prennent"], "pris",
               ["pris","pris","prit","prîmes","prîtes","prirent"], "prendr"), "l'air dans le jardin"),
  de=DE(*de_weak("schnapp"), "geschnappt", "frische Luft im Garten"),
  en=EN("get", "gets", "got", "getting", "got", "some fresh air in the garden"),
  fa=FA("در باغ هوا", "خور", "خورد"))

S.add("schneeken",
  lb=LB("schneeken", "Séissegkeeten", "geschneekt"),
  fr=FR(fr_er("grignot"), "des friandises"),
  de=DE(*de_weak("nasch"), "genascht", "Süßigkeiten"),
  en=EN("snack", "snacks", "snacked", "snacking", "snacked", "on sweets"),
  fa=FA("شیرینی", "خور", "خورد"))

S.add("schneiden",
  lb=LB("schneiden", "d'Brout", "geschnidden", pres=["schneiden","schneits","schneit","schneiden","schneit","schneiden"]),
  fr=FR(fr_er("coup"), "le pain"),
  de=DE(["schneide","schneidest","schneidet","schneiden","schneidet","schneiden"],
        ["schnitt","schnittst","schnitt","schnitten","schnittet","schnitten"], "geschnitten", "das Brot"),
  en=EN("cut", "cuts", "cut", "cutting", "cut", "the bread"),
  fa=FA("نان را", "بر", "برید"))

S.add("schneideren",
  lb=LB("schneideren", "e Kleed", "geschneidert"),
  fr=FR(fr_er("confectionn"), "une robe"),
  de=DE(*de_weak("schneider"), "geschneidert", "ein Kleid"),
  en=EN("tailor", "tailors", "tailored", "tailoring", "tailored", "a dress"),
  fa=FA("لباس را", "دوز", "دوخت"))

S.add("schneien",
  lb=LB("schneien", "Konfetti iwwer d'Bühn", "geschneit"),
  fr=FR(fr_er("neig"), "des confettis sur la scène"),
  de=DE(*de_weak("schnei"), "geschneit", "Konfetti über die Bühne"),
  en=EN("snow", "snows", "snowed", "snowing", "snowed", "confetti over the stage"),
  fa=FA("بر صحنه کنفتی", "بار", "بارید"))

S.add("schnëppelen",
  lb=LB("schnëppelen", "d'Zwiebelen", "geschnëppelt"),
  fr=FR(fr_er("éminc"), "les oignons"),
  de=DE(*de_weak("schnippel"), "geschnippelt", "die Zwiebeln"),
  en=EN("chop", "chops", "chopped", "chopping", "chopped", "the onions"),
  fa=FA("پیاز را ریز", "کن", "کرد", sp=""))

S.add("schnëssen",
  lb=LB("schnëssen", "um Telefon", "geschnësst"),
  fr=FR(fr_er("palabr"), "au téléphone"),
  de=DE(*de_weak("quatsch"), "gequatscht", "am Telefon"),
  en=EN("natter", "natters", "nattered", "nattering", "nattered", "on the phone"),
  fa=FA("پشت تلفن وراجی", "کن", "کرد", sp=""))

S.add("schnëtzelen",
  lb=LB("schnëtzelen", "e Stär aus Holz", "geschnëtzelt"),
  fr=FR(fr_er("découp"), "une étoile en bois"),
  de=DE(*de_weak("säg"), "ausgesägt", "einen Stern aus Holz", part="aus"),
  en=EN("cut out", "cuts out", "cut out", "cutting out", "cut out", "a wooden star"),
  fa=FA("یک ستاره چوبی را با اره‌مویی", "بر", "برید"))

S.add("schnëtzen",
  lb=LB("schnëtzen", "eng Figur aus Holz", "geschnëtzt"),
  fr=FR(fr_er("sculpt"), "une figurine en bois"),
  de=DE(*de_weak("schnitz", sib=True), "geschnitzt", "eine Figur aus Holz"),
  en=EN("carve", "carves", "carved", "carving", "carved", "a figure from wood"),
  fa=FA("یک مجسمه چوبی را", "تراش", "تراشید"))

S.add("schnoffelen",
  lb=LB("schnoffelen", "an der Kichen", "geschnoffelt"),
  fr=FR(fr_er("renifl"), "dans la cuisine"),
  de=DE(*de_weak("schnüffel"), "geschnüffelt", "in der Küche"),
  en=EN("sniff", "sniffs", "sniffed", "sniffing", "sniffed", "around the kitchen"),
  fa=FA("در آشپزخانه بو", "کش", "کشید"))

S.add("schnupperen",
  lb=LB("schnupperen", "u Rousen", "geschnuppert"),
  fr=FR(fr_er("renifl"), "les roses"),
  de=DE(*de_weak("schnupper"), "geschnuppert", "an den Rosen"),
  en=EN("sniff", "sniffs", "sniffed", "sniffing", "sniffed", "at the roses"),
  fa=FA("گل‌های رز را بو", "کن", "کرد", sp=""))

S.add("schnurren",
  lb=LB("schnurren", "wéi eng Kaz", "geschnurrt"),
  fr=FR(fr_er("ronronn"), "comme un chat"),
  de=DE(*de_weak("schnurr"), "geschnurrt", "wie eine Katze"),
  en=EN("purr", "purrs", "purred", "purring", "purred", "like a cat"),
  fa=FA("مثل گربه خرخر", "کن", "کرد", sp=""))

S.add("schockéieren",
  lb=LB("schockéieren", "d'Famill mat där Noriicht", "schockéiert"),
  fr=FR(fr_er("choqu"), "la famille avec cette nouvelle"),
  de=DE(*de_weak("schockier"), "schockiert", "die Familie mit dieser Nachricht"),
  en=EN("shock", "shocks", "shocked", "shocking", "shocked", "the family with the news"),
  fa=FA("خانواده را با این خبر شوکه", "کن", "کرد", sp=""))

S.add("schocken",
  lb=LB("schocken", "d'Gäscht mat engem groben Witz", "geschockt"),
  fr=FR(fr_er("choqu"), "les invités avec une blague grossière"),
  de=DE(*de_weak("schock"), "geschockt", "die Gäste mit einem derben Witz"),
  en=EN("shock", "shocks", "shocked", "shocking", "shocked", "the guests with a crude joke"),
  fa=FA("مهمانان را با یک شوخی زشت شوکه", "کن", "کرد", sp=""))

S.add("schosselen",
  lb=LB("schosselen", "d'Problem", "geschosselt"),
  fr=FR(fr_er("goupill"), "l'affaire"),
  de=DE(*de_weak("krieg"), "hingekriegt", "das Problem", part="hin"),
  en=EN("fix", "fixes", "fixed", "fixing", "fixed", "the problem"),
  fa=FA("مشکل را حل", "کن", "کرد", sp=""))

S.add("schoulen",
  lb=LB("schoulen", "déi nei Mataarbechter", "geschoult"),
  fr=FR(fr_er("form"), "les nouveaux employés"),
  de=DE(*de_weak("schul"), "geschult", "die neuen Mitarbeiter"),
  en=EN("train", "trains", "trained", "training", "trained", "the new employees"),
  fa=FA("کارمندان جدید را آموزش", "ده", "داد"))

S.add("schounen",
  lb=LB("schounen", "d'Ëmwelt", "geschount"),
  fr=FR(fr_er("ménag"), "l'environnement"),
  de=DE(*de_weak("schon"), "geschont", "die Umwelt"),
  en=EN("spare", "spares", "spared", "sparing", "spared", "the environment"),
  fa=FA("محیط زیست را حفظ", "کن", "کرد", sp=""))

S.add("schrauwen",
  lb=LB("schrauwen", "d'Regal u d'Mauer", "geschrauwt"),
  fr=FR(fr_er("viss"), "l'étagère au mur"),
  de=DE(*de_weak("schraub"), "geschraubt", "das Regal an die Wand"),
  en=EN("screw", "screws", "screwed", "screwing", "screwed", "the shelf to the wall"),
  fa=FA("قفسه را با پیچ به دیوار", "کن", "کرد", sp=""))

S.add("schredderen",
  lb=LB("schredderen", "al Dokumenter", "geschreddert"),
  fr=FR(fr_er("déchiquet", "déchiquett", "déchiquetter"), "les vieux documents"),
  de=DE(*de_weak("schredder"), "geschreddert", "alte Dokumente"),
  en=EN("shred", "shreds", "shredded", "shredding", "shredded", "old documents"),
  fa=FA("اسناد قدیمی را خرد", "کن", "کرد", sp=""))

S.add("schréipsen",
  lb=LB("schréipsen", "d'Auto", "geschréipst"),
  fr=FR(fr_er("érafl"), "la voiture"),
  de=DE(*de_weak("schramm"), "geschrammt", "das Auto"),
  en=EN("scratch", "scratches", "scratched", "scratching", "scratched", "the car"),
  fa=FA("ماشین را", "خراش", "خراشید"))

S.add("schreiwen",
  lb=LB("schreiwen", "e Bréif", "geschriwwen", pres=["schreiwen","schreifs","schreift","schreiwen","schreift","schreiwen"]),
  fr=FR(fr_irr(["écris","écris","écrit","écrivons","écrivez","écrivent"], "écrit",
               ["écrivis","écrivis","écrivit","écrivîmes","écrivîtes","écrivirent"], "écrir"), "une lettre"),
  de=DE(["schreibe","schreibst","schreibt","schreiben","schreibt","schreiben"],
        ["schrieb","schriebst","schrieb","schrieben","schriebt","schrieben"], "geschrieben", "einen Brief"),
  en=EN("write", "writes", "wrote", "writing", "written", "a letter"),
  fa=FA("یک نامه", "نویس", "نوشت"))

S.add("schrumpfen",
  lb=LB("schrumpfen", "an der Wäsch", "geschrumpft", aux="sinn"),
  fr=FR(fr_ir("rétréc"), "au lavage"),
  de=DE(*de_weak("schrumpf"), "geschrumpft", "in der Wäsche", aux="sein"),
  en=EN("shrink", "shrinks", "shrank", "shrinking", "shrunk", "in the wash"),
  fa=FA("در ماشین لباسشویی کوچک", "شو", "شد",
        pres6=["می‌شوم","می‌شوی","می‌شود","می‌شویم","می‌شوید","می‌شوند"],
        subj6=["بشوم","بشوی","بشود","بشویم","بشوید","بشوند"]))

S.add("schruppen",
  lb=LB("schruppen", "de Buedem", "geschruppt"),
  fr=FR(fr_er("frott"), "le sol"),
  de=DE(*de_weak("schrubb"), "geschrubbt", "den Boden"),
  en=EN("scrub", "scrubs", "scrubbed", "scrubbing", "scrubbed", "the floor"),
  fa=FA("کف را با برس", "ساب", "سایید"))

S.add("schubsen",
  lb=LB("schubsen", "de Frënd an de Pool", "geschubst"),
  fr=FR(fr_er("pouss"), "l'ami dans la piscine"),
  de=DE(*de_weak("schubs", sib=True), "geschubst", "den Freund ins Wasser"),
  en=EN("push", "pushes", "pushed", "pushing", "pushed", "the friend into the pool"),
  fa=FA("دوست را به داخل استخر هل", "ده", "داد"))

S.add("schudderen",
  lb=LB("schudderen", "vu Keelt", "geschuddert"),
  fr=FR(fr_er("frisson"), "de froid"),
  de=DE(*de_weak("fröstel"), "gefröstelt", "vor Kälte"),
  en=EN("shiver", "shivers", "shivered", "shivering", "shivered", "from the cold"),
  fa=FA("از سرما", "لرز", "لرزید"))

S.add("schuppen",
  lb=LB("schuppen", "e Bonbon am Buttek", "geschuppt"),
  fr=FR(fr_er("chip"), "un bonbon au magasin"),
  de=DE(*de_weak("klau"), "geklaut", "ein Bonbon im Laden"),
  en=EN("nick", "nicks", "nicked", "nicking", "nicked", "a sweet from the shop"),
  fa=FA("یک آب‌نبات از مغازه", "دزد", "دزدید"))

S.add("schützen",
  lb=LB("schützen", "d'Kanner virun der Sonn", "geschützt"),
  fr=FR(fr_er("protég", "protèg", "protéger"), "les enfants du soleil"),
  de=DE(*de_weak("schütz", sib=True), "geschützt", "die Kinder vor der Sonne"),
  en=EN("protect", "protects", "protected", "protecting", "protected", "the children from the sun"),
  fa=FA("کودکان را از آفتاب محافظت", "کن", "کرد", sp=""))

S.add("schwabbelen",
  lb=LB("schwabbelen", "wéi e Pudding", "geschwabbelt"),
  fr=FR(fr_er("ballott"), "comme un flan"),
  de=DE(*de_weak("schwabbel"), "geschwabbelt", "wie ein Pudding"),
  en=EN("wobble", "wobbles", "wobbled", "wobbling", "wobbled", "like a jelly"),
  fa=FA("مثل ژله", "لرز", "لرزید"))

S.add("schwächen",
  lb=LB("schwächen", "de Géigner", "geschwächt"),
  fr=FR(fr_ir("affaibl"), "l'adversaire"),
  de=DE(*de_weak("schwäch"), "geschwächt", "den Gegner"),
  en=EN("weaken", "weakens", "weakened", "weakening", "weakened", "the opponent"),
  fa=FA("حریف را تضعیف", "کن", "کرد", sp=""))

S.add("schwadronéieren",
  lb=LB("schwadronéieren", "am Café", "schwadronéiert"),
  fr=FR(fr_er("palabr"), "au café"),
  de=DE(*de_weak("palaver"), "gepalavert", "im Café"),
  en=EN("palaver", "palavers", "palavered", "palavering", "palavered", "in the café"),
  fa=FA("در کافه چرت و پرت", "گو", "گفت",
        pres6=["می‌گویم","می‌گویی","می‌گوید","می‌گوییم","می‌گویید","می‌گویند"],
        subj6=["بگویم","بگویی","بگوید","بگوییم","بگویید","بگویند"]))

S.add("schwäerzen",
  lb=LB("schwäerzen", "d'Gesiicht mat Kuel", "geschwäerzt"),
  fr=FR(fr_ir("noirc"), "le visage avec du charbon"),
  de=DE(*de_weak("schwärz", sib=True), "geschwärzt", "das Gesicht mit Kohle"),
  en=EN("blacken", "blackens", "blackened", "blackening", "blackened", "the face with charcoal"),
  fa=FA("صورت را با زغال سیاه", "کن", "کرد", sp=""))

S.add("schwammen",
  lb=LB("schwammen", "am See", "geschwommen", pres=["schwammen","schwëmms","schwëmmt","schwammen","schwëmmt","schwammen"]),
  fr=FR(fr_er("nag"), "dans le lac"),
  de=DE(["schwimme","schwimmst","schwimmt","schwimmen","schwimmt","schwimmen"],
        ["schwamm","schwammst","schwamm","schwammen","schwammt","schwammen"], "geschwommen", "im See"),
  en=EN("swim", "swims", "swam", "swimming", "swum", "in the lake"),
  fa=FA("در دریاچه شنا", "کن", "کرد", sp=""))

S.add("schwänzen",
  lb=LB("schwänzen", "d'Schoul", "geschwänzt"),
  fr=FR(fr_er("sèch", "sèch", "sécher"), "les cours"),
  de=DE(*de_weak("schwänz", sib=True), "geschwänzt", "die Schule"),
  en=EN("skive off", "skives off", "skived off", "skiving off", "skived off", "school"),
  fa=FA("از مدرسه غیبت", "کن", "کرد", sp=""))

S.add("schwätzen",
  lb=LB("schwätzen", "Lëtzebuergesch", "geschwat"),
  fr=FR(fr_er("parl"), "luxembourgeois"),
  de=DE(["spreche","sprichst","spricht","sprechen","sprecht","sprechen"],
        ["sprach","sprachst","sprach","sprachen","spracht","sprachen"], "gesprochen", "Luxemburgisch"),
  en=EN("speak", "speaks", "spoke", "speaking", "spoken", "Luxembourgish"),
  fa=FA("به لوکزامبورگی صحبت", "کن", "کرد", sp=""))

S.add("schweessen",
  lb=LB("schweessen", "bei der Hëtzt", "geschweesst"),
  fr=FR(fr_er("transpir"), "par cette chaleur"),
  de=DE(*de_weak("schwitz", sib=True), "geschwitzt", "bei der Hitze"),
  en=EN("sweat", "sweats", "sweated", "sweating", "sweated", "in the heat"),
  fa=FA("در گرما عرق", "کن", "کرد", sp=""))

S.add("schwëllen",
  lb=LB("schwëllen", "vu Stolz", "geschwollen", aux="sinn"),
  fr=FR(fr_er("enfl"), "de fierté"),
  de=DE(["schwelle","schwillst","schwillt","schwellen","schwellt","schwellen"],
        ["schwoll","schwollst","schwoll","schwollen","schwollt","schwollen"], "geschwollen", "vor Stolz", aux="sein"),
  en=EN("swell", "swells", "swelled", "swelling", "swollen", "with pride"),
  fa=FA("از غرور باد", "کن", "کرد", sp=""))

S.add("schwéngen",
  lb=LB("schwéngen", "d'Äerm", "geschwéngt"),
  fr=FR(fr_er("balanc"), "les bras"),
  de=DE(["schwinge","schwingst","schwingt","schwingen","schwingt","schwingen"],
        ["schwang","schwangst","schwang","schwangen","schwangt","schwangen"], "geschwungen", "die Arme"),
  en=EN("swing", "swings", "swung", "swinging", "swung", "{pos} arms"),
  fa=FA("دست‌ها را تاب", "ده", "داد"))

S.add("schwenken",
  lb=LB("schwenken", "d'Glieser", "geschwenkt"),
  fr=FR(fr_er("rinc"), "les verres"),
  de=DE(*de_weak("spül"), "ausgespült", "die Gläser", part="aus"),
  en=EN("rinse", "rinses", "rinsed", "rinsing", "rinsed", "the glasses"),
  fa=FA("لیوان‌ها را آبکشی", "کن", "کرد", sp=""))

S.add("schwieren",
  lb=LB("schwieren", "en Eed", "geschwuer"),
  fr=FR(fr_er("jur"), "fidélité"),
  de=DE(["schwöre","schwörst","schwört","schwören","schwört","schwören"],
        ["schwor","schworst","schwor","schworen","schwort","schworen"], "geschworen", "einen Eid"),
  en=EN("swear", "swears", "swore", "swearing", "sworn", "an oath"),
  fa=FA("سوگند", "خور", "خورد"))

S.add("schwiewelen",
  lb=LB("schwiewelen", "de Wäin", "geschwiewelt"),
  fr=FR(fr_er("soufr"), "le vin"),
  de=DE(*de_weak("schwefel"), "geschwefelt", "den Wein"),
  en=EN("sulphur", "sulphurs", "sulphured", "sulphuring", "sulphured", "the wine"),
  fa=FA("به شراب گوگرد", "زن", "زد"))

S.add("schwiewen",
  lb=LB("schwiewen", "iwwer dem Séi", "geschwiewt"),
  fr=FR(fr_er("plan"), "au-dessus du lac"),
  de=DE(*de_weak("schweb"), "geschwebt", "über dem See"),
  en=EN("glide", "glides", "glided", "gliding", "glided", "over the lake"),
  fa=FA("بر فراز دریاچه", "لغز", "لغزید"))

S.add("scolariséieren",
  lb=LB("scolariséieren", "d'Kand an der Grondschoul", "scolariséiert"),
  fr=FR(fr_er("scolaris"), "l'enfant à l'école primaire"),
  de=DE(*de_weak("schul"), "eingeschult", "das Kind in die Grundschule", part="ein"),
  en=EN("enroll", "enrolls", "enrolled", "enrolling", "enrolled", "the child in primary school"),
  fa=FA("کودک را در مدرسه ابتدایی ثبت‌نام", "کن", "کرد", sp=""))

S.add("sculptéieren",
  lb=LB("sculptéieren", "eng Statu aus Steen", "sculptéiert"),
  fr=FR(fr_er("sculpt"), "une statue dans la pierre"),
  de=DE(*de_weak("skulptier"), "skulptiert", "eine Statue aus Stein"),
  en=EN("sculpt", "sculpts", "sculpted", "sculpting", "sculpted", "a statue from stone"),
  fa=FA("یک مجسمه از سنگ", "تراش", "تراشید"))

S.add("sécheren",
  lb=LB("sécheren", "d'Dier mat engem Schlass", "geséchert"),
  fr=FR(fr_er("sécuris"), "la porte avec un verrou"),
  de=DE(*de_weak("sicher"), "gesichert", "die Tür mit einem Schloss"),
  en=EN("secure", "secures", "secured", "securing", "secured", "the door with a lock"),
  fa=FA("در را با یک قفل ایمن", "کن", "کرد", sp=""))
