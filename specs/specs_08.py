# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()
Z = "‌"
def P6(stem_forms):
    return [("می" + Z + x) for x in stem_forms]
SHAV_P = ["می‌شوم","می‌شوی","می‌شود","می‌شویم","می‌شوید","می‌شوند"]
SHAV_S = ["شوم","شوی","شود","شویم","شوید","شوند"]
BAR = ["بر"]
AVOIR_PS = ["eus","eus","eut","eûmes","eûtes","eurent"]

S.add("spëtzen",
  lb=LB("spëtzen", "de Bläistëft", "gespëtzt"),
  fr=FR(fr_er("taill"), "le crayon"),
  de=DE(*de_weak("spitz", sib=True), "gespitzt", "den Bleistift"),
  en=EN("sharpen", "sharpens", "sharpened", "sharpening", "sharpened", "the pencil"),
  fa=FA("مداد را", "تراش", "تراشید"))

S.add("spezifizéieren",
  lb=LB("spezifizéieren", "d'Konditiounen", "spezifizéiert"),
  fr=FR(fr_er("spécifi"), "les conditions"),
  de=DE(*de_weak("spezifizier"), "spezifiziert", "die Bedingungen"),
  en=EN("specify", "specifies", "specified", "specifying", "specified", "the conditions"),
  fa=FA("شرایط را مشخص", "کن", "کرد", sp=""))

S.add("spieren",
  lb=LB("spieren", "d'Keelt", "gespiert"),
  fr=FR(fr_irr(["sens","sens","sent","sentons","sentez","sentent"], "senti",
               ["sentis","sentis","sentit","sentîmes","sentîtes","sentirent"], "sentir"), "le froid"),
  de=DE(*de_weak("spür"), "gespürt", "die Kälte"),
  en=EN("feel", "feels", "felt", "feeling", "felt", "the cold"),
  fa=FA("سرما را احساس", "کن", "کرد", sp=""))

S.add("spigelen",
  lb=LB("spigelen", "d'Liicht am Waasser", "gespigelt"),
  fr=FR(fr_er("reflét", "reflèt", "refléter"), "la lumière dans l'eau"),
  de=DE(["spiegle","spiegelst","spiegelt","spiegeln","spiegelt","spiegeln"],
        ["spiegelte","spiegeltest","spiegelte","spiegelten","spiegeltet","spiegelten"],
        "gespiegelt", "das Licht im Wasser"),
  en=EN("reflect", "reflects", "reflected", "reflecting", "reflected", "the light in the water"),
  fa=FA("نور را در آب بازتاب", "ده", "داد"))

S.add("spillen",
  lb=LB("spillen", "Schach", "gespillt"),
  fr=FR(fr_er("jou"), "aux échecs"),
  de=DE(*de_weak("spiel"), "gespielt", "Schach"),
  en=EN("play", "plays", "played", "playing", "played", "chess"),
  fa=FA("شطرنج بازی", "کن", "کرد", sp=""))

S.add("splécken",
  lb=LB("splécken", "d'Holz", "gespléckt"),
  fr=FR(fr_re("fend"), "le bois"),
  de=DE(*de_weak("spalt", dt=True), "gespalten", "das Holz"),
  en=EN("chop", "chops", "chopped", "chopping", "chopped", "the wood"),
  fa=FA("هیزم را خرد", "کن", "کرد", sp=""))

S.add("sponseren",
  lb=LB("sponseren", "de Veräin", "gesponsert"),
  fr=FR(fr_er("sponsoris"), "le club"),
  de=DE(["sponsere","sponserst","sponsert","sponsern","sponsert","sponsern"],
        ["sponserte","sponsertest","sponserte","sponserten","sponsertet","sponserten"],
        "gesponsert", "den Verein"),
  en=EN("sponsor", "sponsors", "sponsored", "sponsoring", "sponsored", "the club"),
  fa=FA("از باشگاه حمایت مالی", "کن", "کرد", sp=""))

S.add("sprangen",
  lb=LB("sprangen", "an de Séi", "gesprongen", pres=["sprangen","sprangs","sprangt","sprangen","sprangt","sprangen"], aux="sinn"),
  fr=FR(fr_er("saut"), "dans le lac"),
  de=DE(["springe","springst","springt","springen","springt","springen"],
        ["sprang","sprangst","sprang","sprangen","sprangt","sprangen"],
        "gesprungen", "in den See", aux="sein"),
  en=EN("jump", "jumps", "jumped", "jumping", "jumped", "into the lake"),
  fa=FA("به دریاچه", "پر", "پرید"))

S.add("sprayen",
  lb=LB("sprayen", "Faarf op d'Mauer", "gesprayt"),
  fr=FR(fr_er("pulvéris"), "de la peinture sur le mur"),
  de=DE(*de_weak("spray"), "gesprayt", "Farbe an die Wand"),
  en=EN("spray", "sprays", "sprayed", "spraying", "sprayed", "paint on the wall"),
  fa=FA("رنگ را روی دیوار", "پاش", "پاشید"))

S.add("spreeden",
  lb=LB("spreeden", "Sand op de Wee", "gespreet", pres=["spreeden","spreets","spreet","spreeden","spreet","spreeden"]),
  fr=FR(fr_re("épand"), "du sable sur le chemin"),
  de=DE(*de_weak("streu"), "gestreut", "Sand auf den Weg"),
  en=EN("spread", "spreads", "spread", "spreading", "spread", "sand on the path"),
  fa=FA("ماسه را روی مسیر", "پاش", "پاشید"))

S.add("sprengen",
  lb=LB("sprengen", "de Fiels am Steebroch", "gesprengt"),
  fr=FR(fr_er("dynamit"), "le rocher dans la carrière"),
  de=DE(*de_weak("spreng"), "gesprengt", "den Felsen im Steinbruch"),
  en=EN("blow up", "blows up", "blew up", "blowing up", "blown up", "the rock in the quarry"),
  fa=FA("صخره را در معدن منفجر", "کن", "کرد", sp=""))

S.add("sprëtzen",
  lb=LB("sprëtzen", "d'Planzen am Gaart", "gesprëtzt"),
  fr=FR(fr_er("trait"), "les plantes dans le jardin"),
  de=DE(*de_weak("spritz", sib=True), "gespritzt", "die Pflanzen im Garten"),
  en=EN("spray", "sprays", "sprayed", "spraying", "sprayed", "the plants in the garden"),
  fa=FA("گیاهان را در باغ سمپاشی", "کن", "کرد", sp=""))

S.add("spriechen",
  lb=LB("spriechen", "d'Uerteel", "gesprach", pres=["spriechen","sprichs","sprécht","spriechen","spriecht","spriechen"]),
  fr=FR(fr_er("prononc"), "le jugement"),
  de=DE(["spreche","sprichst","spricht","sprechen","sprecht","sprechen"],
        ["sprach","sprachst","sprach","sprachen","spracht","sprachen"],
        "gesprochen", "das Urteil"),
  en=EN("pronounce", "pronounces", "pronounced", "pronouncing", "pronounced", "the verdict"),
  fa=FA("حکم را صادر", "کن", "کرد", sp=""))

S.add("sprinten",
  lb=LB("sprinten", "op der Piste", "gesprint", pres=["sprinten","sprints","sprint","sprinten","sprint","sprinten"]),
  fr=FR(fr_er("sprint"), "sur la piste"),
  de=DE(*de_weak("sprint", dt=True), "gesprintet", "auf der Bahn"),
  en=EN("sprint", "sprints", "sprinted", "sprinting", "sprinted", "on the track"),
  fa=FA("در پیست اسپرینت", "کن", "کرد", sp=""))

S.add("sproochen",
  lb=LB("sproochen", "mat der Noperin", "gesproocht"),
  fr=FR(fr_er("papot"), "avec la voisine"),
  de=DE(["plaudere","plauderst","plaudert","plaudern","plaudert","plaudern"],
        ["plauderte","plaudertest","plauderte","plauderten","plaudertet","plauderten"],
        "geplaudert", "mit der Nachbarin"),
  en=EN("chat", "chats", "chatted", "chatting", "chatted", "with the neighbour"),
  fa=FA("با همسایه گپ", "زن", "زد"))

S.add("spruddelen",
  lb=LB("spruddelen", "vu Freed", "gespruddelt"),
  fr=FR(fr_er("pétill"), "de joie"),
  de=DE(["sprudle","sprudelst","sprudelt","sprudeln","sprudelt","sprudeln"],
        ["sprudelte","sprudeltest","sprudelte","sprudelten","sprudeltet","sprudelten"],
        "gesprudelt", "vor Freude"),
  en=EN("bubble", "bubbles", "bubbled", "bubbling", "bubbled", "with joy"),
  fa=FA("از شادی", "جوش", "جوشید"))

S.add("sprutzen",
  lb=LB("sprutzen", "d'Kanner mat Waasser", "gesprutzt"),
  fr=FR(fr_er("éclabouss"), "les enfants avec de l'eau"),
  de=DE(*de_weak("spritz", sib=True), "gespritzt", "die Kinder mit Wasser"),
  en=EN("splash", "splashes", "splashed", "splashing", "splashed", "the children with water"),
  fa=FA("روی بچه‌ها آب", "پاش", "پاشید"))

S.add("spueren",
  lb=LB("spueren", "Suen fir d'Vakanz", "gespuert"),
  fr=FR(fr_er("économis"), "de l'argent pour les vacances"),
  de=DE(*de_weak("spar"), "gespart", "Geld für den Urlaub"),
  en=EN("save", "saves", "saved", "saving", "saved", "money for the holidays"),
  fa=FA("برای تعطیلات پول پس‌انداز", "کن", "کرد", sp=""))

S.add("spullen",
  lb=LB("spullen", "d'Geschir", "gespullt"),
  fr=FR(fr_er("lav"), "la vaisselle"),
  de=DE(["wasche","wäschst","wäscht","waschen","wascht","waschen"],
        ["wusch","wuschst","wusch","wuschen","wuscht","wuschen"],
        "abgewaschen", "das Geschirr", part="ab", inf="abwaschen",
        sub=["abwasche","abwäschst","abwäscht","abwaschen","abwascht","abwaschen"]),
  en=EN("wash up", "washes up", "washed up", "washing up", "washed up", "the dishes"),
  fa=FA("ظرف‌ها را", "شو", "شست",
        pres6=["می‌شویم","می‌شویی","می‌شوید","می‌شوییم","می‌شویید","می‌شویند"],
        subj6=["بشویم","بشویی","بشوید","بشوییم","بشویید","بشویند"]))

S.add("stabiliséieren",
  lb=LB("stabiliséieren", "d'Leeder", "stabiliséiert"),
  fr=FR(fr_er("stabilis"), "l'échelle"),
  de=DE(*de_weak("stabilisier"), "stabilisiert", "die Leiter"),
  en=EN("stabilize", "stabilizes", "stabilized", "stabilizing", "stabilized", "the ladder"),
  fa=FA("نردبان را ثابت", "کن", "کرد", sp=""))

S.add("stäerken",
  lb=LB("stäerken", "d'Muskelen", "gestäerkt"),
  fr=FR(fr_er("fortifi"), "les muscles"),
  de=DE(*de_weak("stärk"), "gestärkt", "die Muskeln"),
  en=EN("strengthen", "strengthens", "strengthened", "strengthening", "strengthened", "the muscles"),
  fa=FA("ماهیچه‌ها را تقویت", "کن", "کرد", sp=""))

S.add("staffelen",
  lb=LB("staffelen", "d'Präisser", "gestaffelt"),
  fr=FR(fr_er("échelonn"), "les prix"),
  de=DE(["staffle","staffelst","staffelt","staffeln","staffelt","staffeln"],
        ["staffelte","staffeltest","staffelte","staffelten","staffeltet","staffelten"],
        "gestaffelt", "die Preise"),
  en=EN("scale", "scales", "scaled", "scaling", "scaled", "the prices"),
  fa=FA("قیمت‌ها را درجه‌بندی", "کن", "کرد", sp=""))

S.add("stagnéieren",
  lb=LB("stagnéieren", "an der Aarbecht", "stagnéiert"),
  fr=FR(fr_er("stagn"), "au travail"),
  de=DE(*de_weak("stagnier"), "stagniert", "bei der Arbeit"),
  en=EN("stagnate", "stagnates", "stagnated", "stagnating", "stagnated", "at work"),
  fa=FA("در کار راکد", "شو", "شد", sp="", pres6=SHAV_P, subj6=SHAV_S))

S.add("stäipen",
  lb=LB("stäipen", "d'Mauer", "gestäipt"),
  fr=FR(fr_er("étay", "étai", "étaier"), "le mur"),
  de=DE(*de_weak("stütz", sib=True), "abgestützt", "die Mauer", part="ab", inf="abstützen",
        sub=["abstütze","abstützt","abstützt","abstützen","abstützt","abstützen"]),
  en=EN("shore up", "shores up", "shored up", "shoring up", "shored up", "the wall"),
  fa=FA("دیوار را محکم", "کن", "کرد", sp=""))

S.add("stallhalen",
  lb=LB("halen", "bei der Ampel", "stallgehalen", pres=["halen","hëls","hält","halen","hält","halen"],
        part="stall", inf_full="stallhalen",
        sub=["stallhalen","stallhëls","stallhält","stallhalen","stallhält","stallhalen"]),
  fr=FR(fr_er("arrêt"), "au feu rouge", aux="être", refl=True),
  de=DE(["halte","hältst","hält","halten","haltet","halten"],
        ["hielt","hieltst","hielt","hielten","hieltet","hielten"],
        "angehalten", "an der Ampel", part="an", inf="anhalten",
        sub=["anhalte","anhältst","anhält","anhalten","anhaltet","anhalten"]),
  en=EN("stop", "stops", "stopped", "stopping", "stopped", "at the traffic light"),
  fa=FA("پشت چراغ قرمز توقف", "کن", "کرد", sp=""))

S.add("stamen",
  lb=LB("stamen", "aus engem klenge Duerf", "gestamt"),
  fr=FR(fr_irr(["proviens","proviens","provient","provenons","provenez","proviennent"], "provenu",
               ["provins","provins","provint","provînmes","provîntes","provinrent"], "proviendr",
               subj=["provienne","proviennes","provienne","provenions","proveniez","proviennent"]),
        "d'un petit village", aux="être"),
  de=DE(*de_weak("stamm"), "gestammt", "aus einem kleinen Dorf"),
  en=EN("come from", "comes from", "came from", "coming from", "come from", "a small village"),
  fa=FA("از دهکده‌ای کوچک", "آ", "آمد",
        pres6=["می‌آیم","می‌آیی","می‌آید","می‌آییم","می‌آیید","می‌آیند"],
        subj6=["بیایم","بیایی","بیاید","بیاییم","بیایید","بیایند"]))

S.add("standardiséieren",
  lb=LB("standardiséieren", "de Prozess", "standardiséiert"),
  fr=FR(fr_er("standardis"), "le processus"),
  de=DE(*de_weak("standardisier"), "standardisiert", "den Prozess"),
  en=EN("standardize", "standardizes", "standardized", "standardizing", "standardized", "the process"),
  fa=FA("فرآیند را استاندارد", "کن", "کرد", sp=""))

S.add("stanzen",
  lb=LB("stanzen", "Lächer an d'Pabeier", "gestanzt"),
  fr=FR(fr_er("poinçonn"), "des trous dans le papier"),
  de=DE(*de_weak("stanz", sib=True), "gestanzt", "Löcher ins Papier"),
  en=EN("punch", "punches", "punched", "punching", "punched", "holes in the paper"),
  fa=FA("در کاغذ سوراخ", "کن", "کرد", sp=""))

S.add("stapelen",
  lb=LB("stapelen", "d'Bicher", "gestapelt"),
  fr=FR(fr_er("empil"), "les livres"),
  de=DE(["stapele","stapelst","stapelt","stapeln","stapelt","stapeln"],
        ["stapelte","stapeltest","stapelte","stapelten","stapeltet","stapelten"],
        "gestapelt", "die Bücher"),
  en=EN("stack", "stacks", "stacked", "stacking", "stacked", "the books"),
  fa=FA("کتاب‌ها را روی هم", "چین", "چید"))

S.add("starten",
  lb=LB("starten", "de Motor", "gestart", pres=["starten","starts","start","starten","start","starten"]),
  fr=FR(fr_er("démarr"), "le moteur"),
  de=DE(*de_weak("start", dt=True), "gestartet", "den Motor"),
  en=EN("start", "starts", "started", "starting", "started", "the engine"),
  fa=FA("موتور را روشن", "کن", "کرد", sp=""))

S.add("stationéieren",
  lb=LB("stationéieren", "d'Zaldote un der Grenz", "stationéiert"),
  fr=FR(fr_er("post"), "les soldats à la frontière"),
  de=DE(*de_weak("stationier"), "stationiert", "die Soldaten an der Grenze"),
  en=EN("station", "stations", "stationed", "stationing", "stationed", "the soldiers at the border"),
  fa=FA("سربازان را در مرز مستقر", "کن", "کرد", sp=""))

S.add("stattfannen",
  lb=LB("fannen", "am Gaart", "stattfonnt", pres=["fannen","fënns","fënnt","fannen","fënnt","fannen"],
        part="statt", inf_full="stattfannen",
        sub=["stattfannen","stattfënns","stattfënnt","stattfannen","stattfënnt","stattfannen"]),
  fr=FR(fr_irr(["ai","as","a","avons","avez","ont"], "eu", AVOIR_PS, "aur",
               subj=["aie","aies","ait","ayons","ayez","aient"],
               imp=["avais","avais","avait","avions","aviez","avaient"]),
        "lieu dans le jardin"),
  de=DE(["finde","findest","findet","finden","findet","finden"],
        ["fand","fandest","fand","fanden","fandet","fanden"],
        "stattgefunden", "im Garten", part="statt", inf="stattfinden",
        sub=["stattfinde","stattfindest","stattfindet","stattfinden","stattfindet","stattfinden"]),
  en=EN("take place", "takes place", "took place", "taking place", "taken place", "in the garden"),
  fa=FA("در باغ برگزار", "شو", "شد", sp="", pres6=SHAV_P, subj6=SHAV_S))

S.add("stauen",
  lb=LB("stauen", "de Baach", "gestaut"),
  fr=FR(fr_er("endigu"), "le ruisseau"),
  de=DE(*de_weak("stau"), "gestaut", "den Bach"),
  en=EN("dam", "dams", "dammed", "damming", "dammed", "the stream"),
  fa=FA("جویبار را سد", "کن", "کرد", sp=""))

S.add("stëbsen",
  lb=LB("stëbsen", "d'Regal", "gestëbst"),
  fr=FR(fr_er("épouset", "épousset", "épousseter"), "l'étagère"),
  de=DE(*de_weak("entstaub"), "entstaubt", "das Regal"),
  en=EN("dust", "dusts", "dusted", "dusting", "dusted", "the shelf"),
  fa=FA("قفسه را گردگیری", "کن", "کرد", sp=""))

S.add("stéckelen",
  lb=LB("stéckelen", "d'Kaartespill", "gestéckelt"),
  fr=FR(fr_er("mélang"), "les cartes"),
  de=DE(*de_weak("misch"), "gemischt", "die Karten"),
  en=EN("shuffle", "shuffles", "shuffled", "shuffling", "shuffled", "the cards"),
  fa=FA("ورق‌ها را بر", "زن", "زد"))

S.add("stécken",
  lb=LB("stécken", "eng Rous", "gestéckt"),
  fr=FR(fr_er("brod"), "une rose"),
  de=DE(*de_weak("stick"), "gestickt", "eine Rose"),
  en=EN("embroider", "embroiders", "embroidered", "embroidering", "embroidered", "a rose"),
  fa=FA("یک گل رز گلدوزی", "کن", "کرد", sp=""))

S.add("stëften",
  lb=LB("stëften", "e Buch fir d'Bibliothéik", "gestëft", pres=["stëften","stëfts","stëft","stëften","stëft","stëften"]),
  fr=FR(fr_irr(["offre","offres","offre","offrons","offrez","offrent"], "offert",
               ["offris","offris","offrit","offrîmes","offrîtes","offrirent"], "offrir"),
        "un livre à la bibliothèque"),
  de=DE(*de_weak("stift", dt=True), "gestiftet", "ein Buch für die Bibliothek"),
  en=EN("donate", "donates", "donated", "donating", "donated", "a book to the library"),
  fa=FA("یک کتاب به کتابخانه اهدا", "کن", "کرد", sp=""))

S.add("stéieren",
  lb=LB("stéieren", "de Noper bei der Aarbecht", "gestéiert"),
  fr=FR(fr_er("dérang"), "le voisin au travail"),
  de=DE(*de_weak("stör"), "gestört", "den Nachbarn bei der Arbeit"),
  en=EN("disturb", "disturbs", "disturbed", "disturbing", "disturbed", "the neighbour at work"),
  fa=FA("مزاحم همسایه", "شو", "شد", sp="", pres6=SHAV_P, subj6=SHAV_S))

S.add("steieren",
  lb=LB("steieren", "d'Schëff", "gesteiert"),
  fr=FR(fr_er("manœuvr"), "le bateau"),
  de=DE(["steuere","steuerst","steuert","steuern","steuert","steuern"],
        ["steuerte","steuertest","steuerte","steuerten","steuertet","steuerten"],
        "gesteuert", "das Schiff"),
  en=EN("steer", "steers", "steered", "steering", "steered", "the ship"),
  fa=FA("کشتی را هدایت", "کن", "کرد", sp=""))

S.add("steigeren",
  lb=LB("steigeren", "d'Präisser", "gesteigert"),
  fr=FR(fr_er("augment"), "les prix"),
  de=DE(["steigere","steigerst","steigert","steigern","steigert","steigern"],
        ["steigerte","steigertest","steigerte","steigerten","steigertet","steigerten"],
        "gesteigert", "die Preise"),
  en=EN("increase", "increases", "increased", "increasing", "increased", "the prices"),
  fa=FA("قیمت‌ها را افزایش", "ده", "داد"))

S.add("steiwen",
  lb=LB("steiwen", "d'Hiem", "gesteiwt"),
  fr=FR(fr_er("empes", "empès", "empèser"), "la chemise"),
  de=DE(*de_weak("stärk"), "gestärkt", "das Hemd"),
  en=EN("starch", "starches", "starched", "starching", "starched", "the shirt"),
  fa=FA("پیراهن را آهار", "زن", "زد"))

S.add("stellen",
  lb=LB("stellen", "d'Vas op den Dësch", "gestallt"),
  fr=FR(fr_irr(["mets","mets","met","mettons","mettez","mettent"], "mis",
               ["mis","mis","mit","mîmes","mîtes","mirent"], "mettr"),
        "le vase sur la table"),
  de=DE(*de_weak("stell"), "gestellt", "die Vase auf den Tisch"),
  en=EN("stand", "stands", "stood", "standing", "stood", "the vase on the table"),
  fa=FA("گلدان را روی میز", "گذار", "گذاشت"))

S.add("stëmmen",
  lb=LB("stëmmen", "d'Gesetz", "gestëmmt"),
  fr=FR(fr_er("vot"), "la loi"),
  de=DE(*de_weak("verabschied", dt=True), "verabschiedet", "das Gesetz"),
  en=EN("pass", "passes", "passed", "passing", "passed", "the law"),
  fa=FA("قانون را تصویب", "کن", "کرد", sp=""))

S.add("stemmen",
  lb=LB("stemmen", "d'Gewiichter", "gestemmt"),
  fr=FR(fr_er("soulev", "soulèv", "soulèver"), "les poids"),
  de=DE(*de_weak("stemm"), "gestemmt", "die Gewichte"),
  en=EN("lift", "lifts", "lifted", "lifting", "lifted", "the weights"),
  fa=FA("وزنه‌ها را بلند", "کن", "کرد", sp=""))

S.add("stempelen",
  lb=LB("stempelen", "de Bréif", "gestempelt"),
  fr=FR(fr_er("timbr"), "la lettre"),
  de=DE(["stemple","stempelst","stempelt","stempeln","stempelt","stempeln"],
        ["stempelte","stempeltest","stempelte","stempelten","stempeltet","stempelten"],
        "gestempelt", "den Brief"),
  en=EN("stamp", "stamps", "stamped", "stamping", "stamped", "the letter"),
  fa=FA("نامه را مهر", "زن", "زد"))

S.add("stengegen",
  lb=LB("stengegen", "d'Hex am Theaterstéck", "gestengegt"),
  fr=FR(fr_er("lapid"), "la sorcière dans la pièce"),
  de=DE(*de_weak("steinig"), "gesteinigt", "die Hexe im Theaterstück"),
  en=EN("stone", "stones", "stoned", "stoning", "stoned", "the witch in the play"),
  fa=FA("جادوگر را در نمایش سنگسار", "کن", "کرد", sp=""))

S.add("sténken",
  lb=LB("sténken", "no Knuewelek", "gestonk"),
  fr=FR(fr_er("pu"), "l'ail"),
  de=DE(["stinke","stinkst","stinkt","stinken","stinkt","stinken"],
        ["stank","stankst","stank","stanken","stankt","stanken"],
        "gestunken", "nach Knoblauch"),
  en=EN("smell", "smells", "smelled", "smelling", "smelled", "of garlic"),
  fa=FA("بوی سیر", "ده", "داد"))

S.add("stëppelen",
  lb=LB("stëppelen", "de klenge Brudder", "gestëppelt"),
  fr=FR(fr_er("taquin"), "le petit frère"),
  de=DE(["stichle","stichelst","stichelt","sticheln","stichelt","sticheln"],
        ["stichelte","sticheltest","stichelte","stichelten","sticheltet","stichelten"],
        "gestichelt", "gegen den kleinen Bruder"),
  en=EN("wind up", "winds up", "wound up", "winding up", "wound up", "the little brother"),
  fa=FA("برادر کوچک را اذیت", "کن", "کرد", sp=""))

S.add("steppen",
  lb=LB("steppen", "de Stoff", "gesteppt"),
  fr=FR(fr_er("piqu"), "le tissu"),
  de=DE(*de_weak("stepp"), "gesteppt", "den Stoff"),
  en=EN("stitch", "stitches", "stitched", "stitching", "stitched", "the fabric"),
  fa=FA("پارچه را", "دوز", "دوخت"))

S.add("steriliséieren",
  lb=LB("steriliséieren", "d'Flasch", "steriliséiert"),
  fr=FR(fr_er("stérilis"), "la bouteille"),
  de=DE(*de_weak("sterilisier"), "sterilisiert", "die Flasche"),
  en=EN("sterilize", "sterilizes", "sterilized", "sterilizing", "sterilized", "the bottle"),
  fa=FA("بطری را ضدعفونی", "کن", "کرد", sp=""))
