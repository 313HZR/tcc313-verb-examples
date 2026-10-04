# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

Z = "‌"
DAD_P = ["می" + Z + x for x in ["دهم", "دهی", "دهد", "دهیم", "دهید", "دهند"]]
DAD_S = ["بدهم", "بدهی", "بدهد", "بدهیم", "بدهید", "بدهند"]
FAIRE = fr_irr(["fais","fais","fait","faisons","faites","font"], "fait",
               ["fis","fis","fit","fîmes","fîtes","firent"], "fer",
               subj=["fasse","fasses","fasse","fassions","fassiez","fassent"],
               imp=["faisais","faisais","faisait","faisions","faisiez","faisaient"])
LESEN = (["lese","liest","liest","lesen","lest","lesen"], ["las","last","las","lasen","last","lasen"])

S.add("quëllen",
  lb=LB("quëllen", "am Waasser", "gequollen", aux="sinn"),
  fr=FR(fr_er("gonfl"), "dans l'eau"),
  de=DE(["quelle","quillst","quillt","quellen","quellt","quellen"], ["quoll","quollst","quoll","quollen","quollt","quollen"], "gequollen", "im Wasser", aux="sein"),
  en=EN("swell", "swells", "swelled", "swelling", "swollen", "in the water"),
  fa=FA("در آب باد", "کن", "کرد", sp=""))

S.add("quëtschen",
  lb=LB("quëtschen", "{rd} d'Fanger an der Dier", "gequëtscht"),
  fr=FR(fr_er("coinc"), "les doigts dans la porte", aux="être", refl=True, agree=False),
  de=DE(*de_weak("quetsch"), "gequetscht", "{rd} die Finger in der Tür"),
  en=EN("catch", "catches", "caught", "catching", "caught", "{pos} fingers in the door"),
  fa=FA("انگشت{ps} را لای در له", "کن", "کرد", sp=""))

S.add("quiiksen",
  lb=LB("quiiksen", "am Stall", "gequiikst"),
  fr=FR(fr_er("couin"), "dans l'étable"),
  de=DE(*de_weak("quiek"), "gequiekt", "im Stall"),
  en=EN("squeal", "squeals", "squealed", "squealing", "squealed", "in the barn"),
  fa=FA("در طویله جیغ", "زن", "زد"))

S.add("quiitschen",
  lb=LB("quiitschen", "wéi eng Dier", "gequiitscht"),
  fr=FR(fr_er("grinc"), "comme une porte"),
  de=DE(*de_weak("quietsch"), "gequietscht", "wie eine Tür"),
  en=EN("squeak", "squeaks", "squeaked", "squeaking", "squeaked", "like a door"),
  fa=FA("مثل در جیرجیر", "کن", "کرد", sp=""))

S.add("raachen",
  lb=LB("raachen", "eng Zigarett am Gaart", "geraacht"),
  fr=FR(fr_er("fum"), "une cigarette dans le jardin"),
  de=DE(*de_weak("rauch"), "geraucht", "eine Zigarette im Garten"),
  en=EN("smoke", "smokes", "smoked", "smoking", "smoked", "a cigarette in the garden"),
  fa=FA("در باغ سیگار", "کش", "کشید"))

S.add("raaspelen",
  lb=LB("raaspelen", "de Kéis fir d'Pizza", "geraaspelt"),
  fr=FR(fr_er("râp"), "le fromage pour la pizza"),
  de=DE(*de_weak("raspel"), "geraspelt", "den Käse für die Pizza"),
  en=EN("grate", "grates", "grated", "grating", "grated", "the cheese for the pizza"),
  fa=FA("پنیر را برای پیتزا رنده", "کن", "کرد", sp=""))

S.add("räätselen",
  lb=LB("räätselen", "iwwer e Rätsel", "geräätselt"),
  fr=FR(fr_er("creus"), "la tête sur une énigme", aux="être", refl=True, agree=False),
  de=DE(*de_weak("rätsel"), "gerätselt", "über ein Rätsel"),
  en=EN("puzzle over", "puzzles over", "puzzled over", "puzzling over", "puzzled over", "a riddle"),
  fa=FA("درباره یک معما فکر", "کن", "کرد", sp=""))

S.add("rabbelen",
  lb=LB("rabbelen", "mam Schlësselbond", "gerabbelt"),
  fr=FR(fr_er("cliquet", "cliquett", "cliquetter"), "avec le trousseau de clés"),
  de=DE(*de_weak("klapper"), "geklappert", "mit dem Schlüsselbund"),
  en=EN("rattle", "rattles", "rattled", "rattling", "rattled", "the key ring"),
  fa=FA("با دسته‌کلید سروصدا", "کن", "کرد", sp=""))

S.add("rächen",
  lb=LB("rächen", "e Frënd", "gerächt"),
  fr=FR(fr_er("veng"), "un ami"),
  de=DE(*de_weak("räch"), "gerächt", "einen Freund"),
  en=EN("avenge", "avenges", "avenged", "avenging", "avenged", "a friend"),
  fa=FA("انتقام یک دوست را", "گیر", "گرفت"))

S.add("rafen",
  lb=LB("rafen", "d'Blieder um Buedem", "geraft"),
  fr=FR(fr_er("ramass"), "les feuilles par terre"),
  de=DE(LESEN[0], LESEN[1], "aufgelesen", "die Blätter vom Boden", part="auf", inf="auflesen"),
  en=EN("pick up", "picks up", "picked up", "picking up", "picked up", "the leaves from the ground"),
  fa=FA("برگ‌ها را از زمین", "چین", "چید"))

S.add("raffinéieren",
  lb=LB("raffinéieren", "den Zocker an der Fabrik", "raffinéiert"),
  fr=FR(fr_er("raffin"), "le sucre à l'usine"),
  de=DE(*de_weak("raffinier"), "raffiniert", "den Zucker in der Fabrik"),
  en=EN("refine", "refines", "refined", "refining", "refined", "the sugar at the factory"),
  fa=FA("شکر را در کارخانه تصفیه", "کن", "کرد", sp=""))

S.add("rafistoléieren",
  lb=LB("rafistoléieren", "de Pneu", "rafistoléiert"),
  fr=FR(fr_er("rafistol"), "le pneu"),
  de=DE(*de_weak("flick"), "geflickt", "den Reifen"),
  en=EN("patch up", "patches up", "patched up", "patching up", "patched up", "the tire"),
  fa=FA("لاستیک را وصله", "کن", "کرد", sp=""))

S.add("räifen",
  lb=LB("räifen", "d'Glieser mat Zocker", "geräift"),
  fr=FR(fr_er("givr"), "les verres avec du sucre"),
  de=DE(*de_weak("bereif"), "bereift", "die Gläser mit Zucker"),
  en=EN("frost", "frosts", "frosted", "frosting", "frosted", "the glasses with sugar"),
  fa=FA("لبه لیوان‌ها را با شکر", "پوشان", "پوشاند"))

S.add("räissen",
  lb=LB("räissen", "e Blat aus dem Heft", "gerass"),
  fr=FR(fr_er("arrach"), "une page du cahier"),
  de=DE(["reiße","reißt","reißt","reißen","reißt","reißen"], ["riss","risst","riss","rissen","risst","rissen"], "gerissen", "ein Blatt aus dem Heft"),
  en=EN("tear out", "tears out", "tore out", "tearing out", "torn out", "a page from the notebook"),
  fa=FA("یک برگ را از دفتر", "کن", "کند"))

S.add("ramoueren",
  lb=LB("ramoueren", "um Späicher", "ramouert"),
  fr=FR(FAIRE, "du bruit au grenier"),
  de=DE(*de_weak("polter"), "gepoltert", "auf dem Dachboden"),
  en=EN("bang about", "bangs about", "banged about", "banging about", "banged about", "in the attic"),
  fa=FA("در اتاق زیر شیروانی سروصدا", "کن", "کرد", sp=""))

S.add("ramponéieren",
  lb=LB("ramponéieren", "d'Auto bei engem Accident", "ramponéiert"),
  fr=FR(fr_er("esquint"), "la voiture dans un accident"),
  de=DE(*de_weak("ramponier"), "ramponiert", "das Auto bei einem Unfall"),
  en=EN("smash up", "smashes up", "smashed up", "smashing up", "smashed up", "the car in an accident"),
  fa=FA("ماشین را در تصادف داغان", "کن", "کرد", sp=""))

S.add("rangéieren",
  lb=LB("rangéieren", "d'Geschier am Schaf", "rangéiert"),
  fr=FR(fr_er("rang"), "la vaisselle dans le placard"),
  de=DE(*de_weak("räum"), "eingeräumt", "das Geschirr in den Schrank", part="ein", inf="einräumen"),
  en=EN("put away", "puts away", "put away", "putting away", "put away", "the dishes in the cupboard"),
  fa=FA("ظرف‌ها را در کمد", "گذار", "گذاشت"))

S.add("rappen",
  lb=LB("rappen", "dem Déif d'Täsch aus der Hand", "gerappt"),
  fr=FR(fr_er("arrach"), "le sac des mains du voleur"),
  de=DE(["reiße","reißt","reißt","reißen","reißt","reißen"], ["riss","risst","riss","rissen","risst","rissen"], "gerissen", "dem Dieb die Tasche aus der Hand"),
  en=EN("snatch", "snatches", "snatched", "snatching", "snatched", "the bag from the thief's hand"),
  fa=FA("کیف را از دست دزد", "قاپ", "قاپید"))

S.add("rapportéieren",
  lb=LB("rapportéieren", "dem Chef d'Gespréich", "rapportéiert"),
  fr=FR(fr_er("rapport"), "la conversation au chef"),
  de=DE(*de_weak("erzähl"), "weitererzählt", "dem Chef das Gespräch", part="weiter", inf="weitererzählen"),
  en=EN("repeat", "repeats", "repeated", "repeating", "repeated", "the conversation to the boss"),
  fa=FA("گفتگو را به رئیس گزارش", "ده", "داد", pres6=DAD_P, subj6=DAD_S))

S.add("raschelen",
  lb=LB("raschelen", "an dréche Blieder", "geraschelt"),
  fr=FR(fr_irr(["bruis","bruis","bruit","bruissons","bruissez","bruissent"], "bruit",
               ["bruis","bruis","bruit","bruîmes","bruîtes","bruirent"], "bruir"),
        "dans les feuilles sèches"),
  de=DE(*de_weak("raschel"), "geraschelt", "im trockenen Laub"),
  en=EN("rustle", "rustles", "rustled", "rustling", "rustled", "in the dry leaves"),
  fa=FA("در برگ‌های خشک خش‌خش", "کن", "کرد", sp=""))

S.add("raschten",
  lb=LB("raschten", "am fiichte Keller", "gerascht", pres=["raschten","raschts","rascht","raschten","rascht","raschten"]),
  fr=FR(fr_er("rouill"), "dans la cave humide"),
  de=DE(*de_weak("rost", dt=True), "gerostet", "im feuchten Keller"),
  en=EN("rust", "rusts", "rusted", "rusting", "rusted", "in the damp cellar"),
  fa=FA("در زیرزمین نمناک زنگ", "زن", "زد"))

S.add("raséieren",
  lb=LB("raséieren", "{r} am Bad", "raséiert"),
  fr=FR(fr_er("ras"), "dans la salle de bain", aux="être", refl=True),
  de=DE(*de_weak("rasier"), "rasiert", "{r} im Bad"),
  en=EN("shave", "shaves", "shaved", "shaving", "shaved", "in the bathroom"),
  fa=FA("صورت{ps} را در حمام", "تراش", "تراشید"))

S.add("räsonéieren",
  lb=LB("räsonéieren", "iwwer e Problem", "räsonéiert"),
  fr=FR(fr_er("raisonn"), "sur un problème"),
  de=DE(*de_weak("überleg"), "überlegt", "über ein Problem"),
  en=EN("reason", "reasons", "reasoned", "reasoning", "reasoned", "about a problem"),
  fa=FA("درباره یک مسئله استدلال", "کن", "کرد", sp=""))

S.add("rassuréieren",
  lb=LB("rassuréieren", "d'Kand", "rassuréiert"),
  fr=FR(fr_er("rassur"), "l'enfant"),
  de=DE(*de_weak("beruhig"), "beruhigt", "das Kind"),
  en=EN("reassure", "reassures", "reassured", "reassuring", "reassured", "the child"),
  fa=FA("کودک را آرام", "کن", "کرد", sp=""))

S.add("ratifizéieren",
  lb=LB("ratifizéieren", "den Traité am Parlament", "ratifizéiert"),
  fr=FR(fr_er("ratifi"), "le traité au parlement"),
  de=DE(*de_weak("ratifizier"), "ratifiziert", "den Vertrag im Parlament"),
  en=EN("ratify", "ratifies", "ratified", "ratifying", "ratified", "the treaty in parliament"),
  fa=FA("معاهده را در مجلس تصویب", "کن", "کرد", sp=""))

S.add("rationaliséieren",
  lb=LB("rationaliséieren", "d'Aarbecht am Büro", "rationaliséiert"),
  fr=FR(fr_er("rationalis"), "le travail au bureau"),
  de=DE(*de_weak("rationalisier"), "rationalisiert", "die Arbeit im Büro"),
  en=EN("streamline", "streamlines", "streamlined", "streamlining", "streamlined", "the work in the office"),
  fa=FA("کار را در دفتر بهینه", "کن", "کرد", sp=""))

S.add("rationéieren",
  lb=LB("rationéieren", "d'Waasser am Summer", "rationéiert"),
  fr=FR(fr_er("rationn"), "l'eau en été"),
  de=DE(*de_weak("rationier"), "rationiert", "das Wasser im Sommer"),
  en=EN("ration", "rations", "rationed", "rationing", "rationed", "the water in summer"),
  fa=FA("آب را در تابستان جیره‌بندی", "کن", "کرد", sp=""))

S.add("raumen",
  lb=LB("raumen", "d'Zëmmer", "geraumt"),
  fr=FR(fr_er("rang"), "la chambre"),
  de=DE(*de_weak("räum"), "aufgeräumt", "das Zimmer", part="auf", inf="aufräumen"),
  en=EN("tidy up", "tidies up", "tidied up", "tidying up", "tidied up", "the room"),
  fa=FA("اتاق را مرتب", "کن", "کرد", sp=""))

S.add("reagéieren",
  lb=LB("reagéieren", "op eng Noriicht", "reagéiert"),
  fr=FR(fr_ir("réag"), "à un message"),
  de=DE(*de_weak("reagier"), "reagiert", "auf eine Nachricht"),
  en=EN("react", "reacts", "reacted", "reacting", "reacted", "to a message"),
  fa=FA("به یک پیام واکنش نشان", "ده", "داد", pres6=DAD_P, subj6=DAD_S))

S.add("realiséieren",
  lb=LB("realiséieren", "en Dram", "realiséiert"),
  fr=FR(fr_er("réalis"), "un rêve"),
  de=DE(*de_weak("realisier"), "realisiert", "einen Traum"),
  en=EN("realize", "realizes", "realized", "realizing", "realized", "a dream"),
  fa=FA("رویا را محقق", "کن", "کرد", sp=""))

S.add("reaniméieren",
  lb=LB("reaniméieren", "de Patient am Spidol", "reaniméiert"),
  fr=FR(fr_er("réanim"), "le patient à l'hôpital"),
  de=DE(*de_weak("beleb"), "wiederbelebt", "den Patienten im Krankenhaus", part="wieder", inf="wiederbeleben"),
  en=EN("revive", "revives", "revived", "reviving", "revived", "the patient in the hospital"),
  fa=FA("بیمار را در بیمارستان احیا", "کن", "کرد", sp=""))

S.add("rebelléieren",
  lb=LB("rebelléieren", "géint de Chef", "rebelléiert"),
  fr=FR(fr_er("rebell"), "contre le chef", aux="être", refl=True),
  de=DE(*de_weak("rebellier"), "rebelliert", "gegen den Chef"),
  en=EN("rebel", "rebels", "rebelled", "rebelling", "rebelled", "against the boss"),
  fa=FA("علیه رئیس شورش", "کن", "کرد", sp=""))

S.add("rechnen",
  lb=LB("rechnen", "d'Zomm am Kapp", "gerechent", pres=["rechnen","rechens","rechent","rechnen","rechent","rechnen"]),
  fr=FR(fr_er("calcul"), "la somme de tête"),
  de=DE(*de_weak("rechn", dt=True), "gerechnet", "die Summe im Kopf"),
  en=EN("calculate", "calculates", "calculated", "calculating", "calculated", "the sum in {pos} head"),
  fa=FA("جمع را در ذهن حساب", "کن", "کرد", sp=""))

S.add("rechtfertegen",
  lb=LB("rechtfertegen", "d'Decisioun virum Chef", "gerechtfertegt"),
  fr=FR(fr_er("justifi"), "la décision devant le chef"),
  de=DE(*de_weak("rechtfertig"), "gerechtfertigt", "die Entscheidung vor dem Chef"),
  en=EN("justify", "justifies", "justified", "justifying", "justified", "the decision to the boss"),
  fa=FA("تصمیم را نزد رئیس توجیه", "کن", "کرد", sp=""))

S.add("réckelen",
  lb=LB("réckelen", "de Sessel an de Eck", "geréckelt"),
  fr=FR(fr_er("déplac"), "le fauteuil dans le coin"),
  de=DE(*de_weak("verrück"), "verrückt", "den Sessel in die Ecke"),
  en=EN("move", "moves", "moved", "moving", "moved", "the armchair into the corner"),
  fa=FA("صندلی راحتی را به گوشه جابه‌جا", "کن", "کرد", sp=""))

S.add("recommandéieren",
  lb=LB("recommandéieren", "engem Frënd e Buch", "recommandéiert"),
  fr=FR(fr_er("recommand"), "un livre à un ami"),
  de=DE(["empfehle","empfiehlst","empfiehlt","empfehlen","empfehlt","empfehlen"],
        ["empfahl","empfahlst","empfahl","empfahlen","empfahlt","empfahlen"], "empfohlen", "einem Freund ein Buch"),
  en=EN("recommend", "recommends", "recommended", "recommending", "recommended", "a book to a friend"),
  fa=FA("یک کتاب را به یک دوست توصیه", "کن", "کرد", sp=""))

S.add("recuperéieren",
  lb=LB("recuperéieren", "d'Sue vun der Bank", "recuperéiert"),
  fr=FR(fr_er("récupér", "récupèr", "récupérer"), "l'argent de la banque"),
  de=DE(["bekomme","bekommst","bekommt","bekommen","bekommt","bekommen"],
        ["bekam","bekamst","bekam","bekamen","bekamt","bekamen"], "wiederbekommen", "das Geld von der Bank",
        part="wieder", inf="wiederbekommen"),
  en=EN("get back", "gets back", "got back", "getting back", "gotten back", "the money from the bank"),
  fa=FA("پول را از بانک پس", "گیر", "گرفت"))

S.add("recycléieren",
  lb=LB("recycléieren", "d'Fläschen am Container", "recycléiert"),
  fr=FR(fr_er("recycl"), "les bouteilles dans le conteneur"),
  de=DE(*de_weak("recycel"), "recycelt", "die Flaschen im Container"),
  en=EN("recycle", "recycles", "recycled", "recycling", "recycled", "the bottles in the bin"),
  fa=FA("بطری‌ها را در سطل بازیافت", "کن", "کرد", sp=""))

S.add("redigéieren",
  lb=LB("redigéieren", "e Bréif un de Buergermeeschter", "redigéiert"),
  fr=FR(fr_er("rédig"), "une lettre au maire"),
  de=DE(*de_weak("verfass", sib=True), "verfasst", "einen Brief an den Bürgermeister"),
  en=EN("write", "writes", "wrote", "writing", "written", "a letter to the mayor"),
  fa=FA("نامه‌ای برای شهردار", "نویس", "نوشت"))

S.add("redresséieren",
  lb=LB("redresséieren", "e Feeler am Rapport", "redresséiert"),
  fr=FR(fr_er("redress"), "une erreur dans le rapport"),
  de=DE(*de_weak("berichtig"), "berichtigt", "einen Fehler im Bericht"),
  en=EN("correct", "corrects", "corrected", "correcting", "corrected", "a mistake in the report"),
  fa=FA("اشتباه را در گزارش اصلاح", "کن", "کرد", sp=""))

S.add("reduzéieren",
  lb=LB("reduzéieren", "d'Käschte vum Projet", "reduzéiert"),
  fr=FR(fr_irr(["réduis","réduis","réduit","réduisons","réduisez","réduisent"], "réduit",
               ["réduisis","réduisis","réduisit","réduisîmes","réduisîtes","réduisirent"], "réduir"),
        "les coûts du projet"),
  de=DE(*de_weak("reduzier"), "reduziert", "die Kosten des Projekts"),
  en=EN("reduce", "reduces", "reduced", "reducing", "reduced", "the costs of the project"),
  fa=FA("هزینه‌های پروژه را کاهش", "ده", "داد", pres6=DAD_P, subj6=DAD_S))

S.add("reechen",
  lb=LB("reechen", "dem Nopesch d'Salz", "gereecht"),
  fr=FR(fr_er("pass"), "le sel au voisin"),
  de=DE(*de_weak("reich"), "gereicht", "dem Nachbarn das Salz"),
  en=EN("pass", "passes", "passed", "passing", "passed", "the salt to the neighbor"),
  fa=FA("نمک را به همسایه", "ده", "داد", pres6=DAD_P, subj6=DAD_S))

S.add("reecheren",
  lb=LB("reecheren", "de Fësch", "gereechert"),
  fr=FR(fr_er("fum"), "le poisson"),
  de=DE(*de_weak("räucher"), "geräuchert", "den Fisch"),
  en=EN("smoke", "smokes", "smoked", "smoking", "smoked", "the fish"),
  fa=FA("ماهی را دودی", "کن", "کرد", sp=""))

S.add("reegelen",
  lb=LB("reegelen", "d'Heizung am Haus", "gereegelt"),
  fr=FR(fr_er("régl", "règl", "régler"), "le chauffage de la maison"),
  de=DE(*de_weak("regel"), "geregelt", "die Heizung im Haus"),
  en=EN("regulate", "regulates", "regulated", "regulating", "regulated", "the heating in the house"),
  fa=FA("گرمایش خانه را تنظیم", "کن", "کرد", sp=""))

S.add("reenen",
  lb=LB("reenen", "Konfetti op d'Braut", "gereent"),
  fr=FR(fr_irr(["pleus","pleus","pleut","pleuvons","pleuvez","pleuvent"], "plu",
               ["plus","plus","plut","plûmes","plûtes","plurent"], "pleuvr",
               subj=["pleuve","pleuves","pleuve","pleuvions","pleuviez","pleuvent"]),
        "des confettis sur la mariée"),
  de=DE(*de_weak("regn", dt=True), "geregnet", "Konfetti auf die Braut"),
  en=EN("rain", "rains", "rained", "raining", "rained", "confetti on the bride"),
  fa=FA("روی عروس کنفتی", "باران", "باراند"))

S.add("reesen",
  lb=LB("reesen", "mam Zuch op Paräis", "gereest", aux="sinn"),
  fr=FR(fr_er("voyag"), "en train à Paris"),
  de=DE(*de_weak("reis", sib=True), "gereist", "mit dem Zug nach Paris", aux="sein"),
  en=EN("travel", "travels", "traveled", "traveling", "traveled", "by train to Paris"),
  fa=FA("با قطار به پاریس سفر", "کن", "کرد", sp=""))

S.add("reezen",
  lb=LB("reezen", "de Schinken an der Raachkummer", "gereezt"),
  fr=FR(fr_er("fum"), "le jambon dans le fumoir"),
  de=DE(*de_weak("räucher"), "geräuchert", "den Schinken in der Räucherkammer"),
  en=EN("smoke", "smokes", "smoked", "smoking", "smoked", "the ham in the smokehouse"),
  fa=FA("ژامبون را در دودخانه دودی", "کن", "کرد", sp=""))

S.add("reflektéieren",
  lb=LB("reflektéieren", "iwwer d'Zukunft", "reflektéiert"),
  fr=FR(fr_ir("réfléch"), "à l'avenir"),
  de=DE(*de_weak("reflektier"), "reflektiert", "über die Zukunft"),
  en=EN("reflect", "reflects", "reflected", "reflecting", "reflected", "on the future"),
  fa=FA("درباره آینده تأمل", "کن", "کرد", sp=""))

S.add("reforméieren",
  lb=LB("reforméieren", "de Schoulsystem", "reforméiert"),
  fr=FR(fr_er("réform"), "le système scolaire"),
  de=DE(*de_weak("reformier"), "reformiert", "das Schulsystem"),
  en=EN("reform", "reforms", "reformed", "reforming", "reformed", "the school system"),
  fa=FA("نظام آموزشی را اصلاح", "کن", "کرد", sp=""))

S.add("refuséieren",
  lb=LB("refuséieren", "d'Offer vum Chef", "refuséiert"),
  fr=FR(fr_er("refus"), "l'offre du patron"),
  de=DE(*de_weak("lehn"), "abgelehnt", "das Angebot des Chefs", part="ab", inf="ablehnen"),
  en=EN("refuse", "refuses", "refused", "refusing", "refused", "the boss's offer"),
  fa=FA("پیشنهاد رئیس را رد", "کن", "کرد", sp=""))
