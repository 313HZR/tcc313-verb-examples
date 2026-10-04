# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()
Z = "‌"
_E = ["م", "ی", "د", "یم", "ید", "ند"]
def P6(stem):
    return ["می" + Z + stem + e for e in _E]
def S6(stem):
    return [stem + e for e in _E]
def fa_(s):
    return s.replace("_", Z)
INDAZ = S6("بیندا" + "ز")

S.add("revendiquéieren",
  lb=LB("revendiquéieren", "méi Loun", "revendiquéiert"),
  fr=FR(fr_er("revendiqu"), "une augmentation"),
  de=DE(["fordere","forderst","fordert","fordern","fordert","fordern"],
        ["forderte","fordertest","forderte","forderten","fordertet","forderten"],
        "eingefordert", "mehr Lohn", part="ein", inf="einfordern"),
  en=EN("demand","demands","demanded","demanding","demanded","a pay rise"),
  fa=FA("افزایش دستمزد را مطالبه", "کن", "کرد", sp=""))

S.add("revidéieren",
  lb=LB("revidéieren", "d'Decisioun", "revidéiert"),
  fr=FR(fr_er("révis"), "la décision"),
  de=DE(*de_weak("revidier"), "revidiert", "die Entscheidung"),
  en=EN("revise","revises","revised","revising","revised","the decision"),
  fa=FA("در تصمیم بازنگری", "کن", "کرد", sp=""))

S.add("reviséieren",
  lb=LB("reviséieren", "den Text", "reviséiert"),
  fr=FR(fr_er("révis"), "le texte"),
  de=DE(*de_weak("revidier"), "revidiert", "den Text"),
  en=EN("revise","revises","revised","revising","revised","the text"),
  fa=FA("متن را اصلاح", "کن", "کرد", sp=""))

S.add("revoltéieren",
  lb=LB("revoltéieren", "d'Noperen", "revoltéiert"),
  fr=FR(fr_er("révolt"), "les voisins"),
  de=DE(*de_weak("empör"), "empört", "die Nachbarn"),
  en=EN("appal","appals","appalled","appalling","appalled","the neighbours"),
  fa=FA(fa_("همسایه_ها را خشمگین"), "کن", "کرد", sp=""))

S.add("revolutionéieren",
  lb=LB("revolutionéieren", "d'Medizin", "revolutionéiert"),
  fr=FR(fr_er("révolutionn"), "la médecine"),
  de=DE(*de_weak("revolutionier"), "revolutioniert", "die Medizin"),
  en=EN("revolutionize","revolutionizes","revolutionized","revolutionizing","revolutionized","medicine"),
  fa=FA("پزشکی را متحول", "کن", "کرد", sp=""))

S.add("revoquéieren",
  lb=LB("revoquéieren", "d'Erlaabnis", "revoquéiert"),
  fr=FR(fr_er("révoqu"), "l'autorisation"),
  de=DE(["hebe","hebst","hebt","heben","hebt","heben"],
        ["hob","hobst","hob","hoben","hobt","hoben"],
        "aufgehoben", "die Genehmigung", part="auf", inf="aufheben"),
  en=EN("revoke","revokes","revoked","revoking","revoked","the permit"),
  fa=FA("مجوز را لغو", "کن", "کرد", sp=""))

S.add("rezenséieren",
  lb=LB("rezenséieren", "e Buch", "rezenséiert"),
  fr=FR(fr_er("critiqu"), "un livre"),
  de=DE(*de_weak("rezensier"), "rezensiert", "ein Buch"),
  en=EN("review","reviews","reviewed","reviewing","reviewed","a book"),
  fa=FA("کتابی را نقد", "کن", "کرد", sp=""))

S.add("richen",
  lb=LB("richen", "d'Rousen am Gaart", "geroch"),
  fr=FR(fr_irr(["sens","sens","sent","sentons","sentez","sentent"], "senti",
               ["sentis","sentis","sentit","sentîmes","sentîtes","sentirent"], "sentir"),
        "les roses du jardin"),
  de=DE(["rieche","riechst","riecht","riechen","riecht","riechen"],
        ["roch","rochst","roch","rochen","rocht","rochen"],
        "gerochen", "die Rosen im Garten"),
  en=EN("smell","smells","smelled","smelling","smelled","the roses in the garden"),
  fa=FA(fa_("گل_های رز را در باغ"), "بوی", "بویید", pres6=P6("بوی"), subj6=S6("ببوی")))

S.add("rieden",
  lb=LB("rieden", "mat der Noperin", "geriet"),
  fr=FR(fr_er("parl"), "avec la voisine"),
  de=DE(*de_weak("red", dt=True), "geredet", "mit der Nachbarin"),
  en=EN("talk","talks","talked","talking","talked","to the neighbour"),
  fa=FA("با همسایه صحبت", "کن", "کرد", sp=""))

S.add("riichten",
  lb=LB("riichten", "d'Taschelamp op d'Dier", "geriicht",
        pres=["riichten","riicht","riicht","riichten","riicht","riichten"]),
  fr=FR(fr_er("braqu"), "la lampe de poche sur la porte"),
  de=DE(*de_weak("richt", dt=True), "gerichtet", "die Taschenlampe auf die Tür"),
  en=EN("point","points","pointed","pointing","pointed","the torch at the door"),
  fa=FA(fa_("چراغ_قوه را به سمت در"), "گیر", "گرفت"))

S.add("ripostéieren",
  lb=LB("ripostéieren", "mat engem Witz", "ripostéiert"),
  fr=FR(fr_er("ripost"), "avec une blague"),
  de=DE(*de_weak("konter"), "gekontert", "mit einem Witz"),
  en=EN("counter","counters","countered","countering","countered","with a joke"),
  fa=FA("با یک شوخی پاسخ", "ده", "داد"))

S.add("riskéieren",
  lb=LB("riskéieren", "eng Strof", "riskéiert"),
  fr=FR(fr_er("risqu"), "une amende"),
  de=DE(*de_weak("riskier"), "riskiert", "ein Bußgeld"),
  en=EN("risk","risks","risked","risking","risked","a fine"),
  fa=FA("خطر جریمه را", "پذیر", "پذیرفت"))

S.add("rivaliséieren",
  lb=LB("rivaliséieren", "mat aneren Equipen", "rivaliséiert"),
  fr=FR(fr_er("rivalis"), "avec d'autres équipes"),
  de=DE(*de_weak("rivalisier"), "rivalisiert", "mit anderen Teams"),
  en=EN("compete","competes","competed","competing","competed","with other teams"),
  fa=FA(fa_("با تیم_های دیگر رقابت"), "کن", "کرد", sp=""))

S.add("roden",
  lb=LB("roden", "d'Äntwert", "gerot"),
  fr=FR(fr_er("devin"), "la réponse"),
  de=DE(["errate","errätst","errät","erraten","erratet","erraten"],
        ["erriet","errietest","erriet","errieten","errietet","errieten"],
        "erraten", "die Antwort"),
  en=EN("guess","guesses","guessed","guessing","guessed","the answer"),
  fa=FA("جواب را حدس", "زن", "زد"))

S.add("rompelen",
  lb=LB("rompelen", "d'Stir", "gerompelt"),
  fr=FR(fr_er("fronc"), "le front"),
  de=DE(*de_weak("runzel"), "gerunzelt", "die Stirn"),
  en=EN("wrinkle","wrinkles","wrinkled","wrinkling","wrinkled","{pos} forehead"),
  fa=FA("پیشانی را چروک", "کن", "کرد", sp=""))

S.add("ronken",
  lb=LB("ronken", "déi ganz Nuecht", "geronkt"),
  fr=FR(fr_er("ronfl"), "toute la nuit"),
  de=DE(*de_weak("schnarch"), "geschnarcht", "die ganze Nacht"),
  en=EN("snore","snores","snored","snoring","snored","all night"),
  fa=FA("تمام شب خروپف", "کن", "کرد", sp=""))

S.add("ronnkréien",
  lb=LB("kréien", "et", "ronnkritt", pres=["kréien","kriss","kritt","kréien","kritt","kréien"],
        part="ronn", inf_full="ronnkréien",
        sub=["ronnkréien","ronnkriss","ronnkritt","ronnkréien","ronnkritt","ronnkréien"]),
  fr=FR(fr_ir("réuss"), "à le faire"),
  de=DE(*de_weak("krieg"), "hingekriegt", "es", part="hin", inf="hinkriegen"),
  en=EN("manage","manages","managed","managing","managed","to do it"),
  fa=FA("از پس این کار", "آی", "آمد", pref="بر"))

S.add("ronschelen",
  lb=LB("ronschelen", "d'Nues", "geronschelt"),
  fr=FR(fr_er("fronc"), "le nez"),
  de=DE(*de_weak("runzel"), "gerunzelt", "die Nase"),
  en=EN("wrinkle","wrinkles","wrinkled","wrinkling","wrinkled","{pos} nose"),
  fa=FA("بینی را چین", "ده", "داد"))

S.add("rosen",
  lb=LB("rosen", "am Stau", "gerost"),
  fr=FR(fr_er("rag"), "dans les bouchons"),
  de=DE(*de_weak("tob"), "getobt", "im Stau"),
  en=EN("fume","fumes","fumed","fuming","fumed","in traffic"),
  fa=FA("در ترافیک عصبانی", "شو", "شد", pres6=P6("شو"), subj6=S6("بشو")))

S.add("rotéieren",
  lb=LB("rotéieren", "ëm eng Achs", "rotéiert"),
  fr=FR(fr_er("tourn"), "autour d'un axe"),
  de=DE(*de_weak("rotier"), "rotiert", "um eine Achse"),
  en=EN("rotate","rotates","rotated","rotating","rotated","around an axis"),
  fa=FA("حول یک محور", "چرخ", "چرخید"))

S.add("rotzen",
  lb=LB("rotzen", "op de Buedem", "gerotzt"),
  fr=FR(fr_er("crach"), "par terre"),
  de=DE(*de_weak("spuck"), "gespuckt", "auf den Boden"),
  en=EN("spit","spits","spat","spitting","spat","on the ground"),
  fa=FA("روی زمین تف", "انداز", "انداخت", subj6=INDAZ))

S.add("rouen",
  lb=LB("rouen", "am Gaart", "gerout"),
  fr=FR(fr_er("repos"), "dans le jardin", aux="être", refl=True),
  de=DE(*de_weak("ruh"), "geruht", "im Garten"),
  en=EN("rest","rests","rested","resting","rested","in the garden"),
  fa=FA("در باغ استراحت", "کن", "کرد", sp=""))

S.add("rubbelen",
  lb=LB("rubbelen", "géint d'Präisser", "gerubbelt"),
  fr=FR(fr_er("tonn"), "contre les prix"),
  de=DE(*de_weak("donner"), "gedonnert", "gegen die Preise"),
  en=EN("thunder","thunders","thundered","thundering","thundered","against the prices"),
  fa=FA(fa_("علیه قیمت_ها غرش"), "کن", "کرد", sp=""))

S.add("rudderen",
  lb=LB("rudderen", "um See", "gerudert"),
  fr=FR(fr_er("ram"), "sur le lac"),
  de=DE(*de_weak("ruder"), "gerudert", "auf dem See"),
  en=EN("row","rows","rowed","rowing","rowed","on the lake"),
  fa=FA("روی دریاچه پارو", "زن", "زد"))

S.add("ruffen",
  lb=LB("ruffen", "d'Kanner", "geruff"),
  fr=FR(fr_er("appel", "appell", "appeller"), "les enfants"),
  de=DE(["rufe","rufst","ruft","rufen","ruft","rufen"],
        ["rief","riefst","rief","riefen","rieft","riefen"],
        "gerufen", "die Kinder"),
  en=EN("call","calls","called","calling","called","the children"),
  fa=FA(fa_("بچه_ها را صدا"), "کن", "کرد", sp=""))

S.add("ruinéieren",
  lb=LB("ruinéieren", "d'Iessen", "ruinéiert"),
  fr=FR(fr_er("ruin"), "le dîner"),
  de=DE(*de_weak("ruinier"), "ruiniert", "das Essen"),
  en=EN("ruin","ruins","ruined","ruining","ruined","the dinner"),
  fa=FA("شام را خراب", "کن", "کرد", sp=""))

S.add("rullen",
  lb=LB("rullen", "de Ball iwwer d'Wiss", "gerullt"),
  fr=FR(fr_er("roul"), "le ballon sur la pelouse"),
  de=DE(*de_weak("roll"), "gerollt", "den Ball über die Wiese"),
  en=EN("roll","rolls","rolled","rolling","rolled","the ball across the meadow"),
  fa=FA("توپ را روی چمن", "غلتان", "غلتاند"))

S.add("sabbelen",
  lb=LB("sabbelen", "de Kaffi um Dësch", "gesabbelt"),
  fr=FR(fr_er("renvers"), "le café sur la table"),
  de=DE(*de_weak("verschütt", dt=True), "verschüttet", "den Kaffee auf den Tisch"),
  en=EN("spill","spills","spilled","spilling","spilled","the coffee on the table"),
  fa=FA("قهوه را روی میز", "ریز", "ریخت"))

S.add("sabotéieren",
  lb=LB("sabotéieren", "de Projet", "sabotéiert"),
  fr=FR(fr_er("sabot"), "le projet"),
  de=DE(*de_weak("sabotier"), "sabotiert", "das Projekt"),
  en=EN("sabotage","sabotages","sabotaged","sabotaging","sabotaged","the project"),
  fa=FA("پروژه را عمداً خراب", "کن", "کرد", sp=""))

S.add("saiséieren",
  lb=LB("saiséieren", "d'Auto", "saiséiert"),
  fr=FR(fr_ir("sais"), "la voiture"),
  de=DE(*de_weak("pfänd", dt=True), "gepfändet", "das Auto"),
  en=EN("seize","seizes","seized","seizing","seized","the car"),
  fa=FA("ماشین را توقیف", "کن", "کرد", sp=""))

S.add("salzen",
  lb=LB("salzen", "d'Zopp", "gesalzt"),
  fr=FR(fr_er("sal"), "la soupe"),
  de=DE(*de_weak("salz", sib=True), "gesalzen", "die Suppe"),
  en=EN("salt","salts","salted","salting","salted","the soup"),
  fa=FA("سوپ را نمک", "زن", "زد"))

S.add("sammelen",
  lb=LB("sammelen", "Muschelen um Stand", "gesammelt"),
  fr=FR(fr_er("ramass"), "des coquillages sur la plage"),
  de=DE(*de_weak("sammel"), "gesammelt", "Muscheln am Strand"),
  en=EN("collect","collects","collected","collecting","collected","shells on the beach"),
  fa=FA(fa_("صدف_ها را در ساحل جمع"), "کن", "کرد", sp=""))

S.add("sanctionéieren",
  lb=LB("sanctionéieren", "d'Firma", "sanctionéiert"),
  fr=FR(fr_er("sanctionn"), "l'entreprise"),
  de=DE(*de_weak("sanktionier"), "sanktioniert", "das Unternehmen"),
  en=EN("sanction","sanctions","sanctioned","sanctioning","sanctioned","the company"),
  fa=FA("شرکت را تحریم", "کن", "کرد", sp=""))

S.add("sanéieren",
  lb=LB("sanéieren", "d'Haus", "sanéiert"),
  fr=FR(fr_er("rénov"), "la maison"),
  de=DE(*de_weak("sanier"), "saniert", "das Haus"),
  en=EN("renovate","renovates","renovated","renovating","renovated","the house"),
  fa=FA("خانه را بازسازی", "کن", "کرد", sp=""))

S.add("sangen",
  lb=LB("sangen", "e Lidd", "gesongen",
        pres=["sangen","séngs","séngt","sangen","sangt","sangen"]),
  fr=FR(fr_er("chant"), "une chanson"),
  de=DE(["singe","singst","singt","singen","singt","singen"],
        ["sang","sangst","sang","sangen","sangt","sangen"],
        "gesungen", "ein Lied"),
  en=EN("sing","sings","sang","singing","sung","a song"),
  fa=FA("یک آهنگ", "خوان", "خواند"))

S.add("saufen",
  lb=LB("saufen", "Waasser aus dem Bach", "gesoff",
        pres=["saufen","säifs","säift","saufen","sauft","saufen"]),
  fr=FR(fr_irr(["bois","bois","boit","buvons","buvez","boivent"], "bu",
               ["bus","bus","but","bûmes","bûtes","burent"], "boir",
               subj=["boive","boives","boive","buvions","buviez","boivent"]),
        "de l'eau du ruisseau"),
  de=DE(["saufe","säufst","säuft","saufen","sauft","saufen"],
        ["soff","soffst","soff","soffen","sofft","soffen"],
        "gesoffen", "Wasser aus dem Bach"),
  en=EN("drink","drinks","drank","drinking","drunk","water from the stream"),
  fa=FA("از جویبار آب", "خور", "خورد"))

S.add("sausen",
  lb=LB("sausen", "duerch d'Stad", "gesaust", aux="sinn"),
  fr=FR(fr_er("fonc"), "à travers la ville"),
  de=DE(*de_weak("saus", sib=True), "gesaust", "durch die Stadt", aux="sein"),
  en=EN("dash","dashes","dashed","dashing","dashed","through the town"),
  fa=FA("با عجله از میان شهر", "رو", "رفت", pres6=P6("رو"), subj6=S6("برو")))

S.add("saven",
  lb=LB("saven", "d'Datei", "gesaved"),
  fr=FR(fr_er("sauvegard"), "le fichier"),
  de=DE(*de_weak("speicher"), "gespeichert", "die Datei"),
  en=EN("save","saves","saved","saving","saved","the file"),
  fa=FA("فایل را ذخیره", "کن", "کرد", sp=""))

S.add("scannen",
  lb=LB("scannen", "d'Dokument", "gescannt"),
  fr=FR(fr_er("scann"), "le document"),
  de=DE(*de_weak("scann"), "gescannt", "das Dokument"),
  en=EN("scan","scans","scanned","scanning","scanned","the document"),
  fa=FA("سند را اسکن", "کن", "کرد", sp=""))

S.add("schäerfen",
  lb=LB("schäerfen", "d'Messer", "geschäerft"),
  fr=FR(fr_er("affût"), "le couteau"),
  de=DE(*de_weak("schärf"), "geschärft", "das Messer"),
  en=EN("sharpen","sharpens","sharpened","sharpening","sharpened","the knife"),
  fa=FA("چاقو را تیز", "کن", "کرد", sp=""))

S.add("schafen",
  lb=LB("schafen", "e Konschtwierk", "geschaf"),
  fr=FR(fr_er("cré"), "une œuvre d'art"),
  de=DE(["schaffe","schaffst","schafft","schaffen","schafft","schaffen"],
        ["schuf","schufst","schuf","schufen","schuft","schufen"],
        "geschaffen", "ein Kunstwerk"),
  en=EN("create","creates","created","creating","created","a work of art"),
  fa=FA("یک اثر هنری خلق", "کن", "کرد", sp=""))

S.add("schaffen",
  lb=LB("schaffen", "am Büro", "geschafft"),
  fr=FR(fr_er("travaill"), "au bureau"),
  de=DE(*de_weak("arbeit", dt=True), "gearbeitet", "im Büro"),
  en=EN("work","works","worked","working","worked","at the office"),
  fa=FA("در دفتر کار", "کن", "کرد", sp=""))

S.add("schäffen",
  lb=LB("schäffen", "Waasser aus dem Brunnen", "geschäfft"),
  fr=FR(fr_er("puis"), "de l'eau du puits"),
  de=DE(*de_weak("schöpf"), "geschöpft", "Wasser aus dem Brunnen"),
  en=EN("draw","draws","drew","drawing","drawn","water from the well"),
  fa=FA("آب را از چاه", "کش", "کشید"))

S.add("schaimen",
  lb=LB("schaimen", "vu Wut", "geschaimt"),
  fr=FR(fr_er("écum"), "de rage"),
  de=DE(*de_weak("schäum"), "geschäumt", "vor Wut"),
  en=EN("foam","foams","foamed","foaming","foamed","with rage"),
  fa=FA("از خشم کف", "کن", "کرد", sp=""))

S.add("schäissen",
  lb=LB("schäissen", "an de Bësch", "geschass",
        pres=["schäissen","schäiss","schäisst","schäissen","schäisst","schäissen"]),
  fr=FR(fr_er("chi"), "dans les bois"),
  de=DE(["scheiße","scheißt","scheißt","scheißen","scheißt","scheißen"],
        ["schiss","schissest","schiss","schissen","schisst","schissen"],
        "geschissen", "in den Wald"),
  en=EN("shit","shits","shat","shitting","shat","in the woods"),
  fa=FA("در جنگل مدفوع", "کن", "کرد", sp=""))

S.add("schakeren",
  lb=LB("schakeren", "wéi e Kueb", "geschakert"),
  fr=FR(fr_er("croass"), "comme un corbeau"),
  de=DE(*de_weak("krächz", sib=True), "gekrächzt", "wie ein Rabe"),
  en=EN("caw","caws","cawed","cawing","cawed","like a crow"),
  fa=FA("مثل کلاغ قارقار", "کن", "کرد", sp=""))

S.add("schalen",
  lb=LB("schalen", "duerch d'Hal", "geschalt"),
  fr=FR(fr_ir("retent"), "dans le hall"),
  de=DE(*de_weak("schall"), "geschallt", "durch die Halle"),
  en=EN("resound","resounds","resounded","resounding","resounded","through the hall"),
  fa=FA("در تالار طنین", "انداز", "انداخت", subj6=INDAZ))

S.add("schalten",
  lb=LB("schalten", "an den zweete Gang", "geschalt",
        pres=["schalten","schalts","schalt","schalten","schalt","schalten"]),
  fr=FR(fr_er("pass"), "en seconde"),
  de=DE(*de_weak("schalt", dt=True), "geschaltet", "in den zweiten Gang"),
  en=EN("shift","shifts","shifted","shifting","shifted","into second gear"),
  fa=FA("دنده را روی دو", "گذار", "گذاشت"))

S.add("schännen",
  lb=LB("schännen", "d'Griewer", "geschänt"),
  fr=FR(fr_er("profan"), "les tombes"),
  de=DE(*de_weak("schänd", dt=True), "geschändet", "die Gräber"),
  en=EN("profane","profanes","profaned","profaning","profaned","the graves"),
  fa=FA("به قبرها بی‌حرمتی", "کن", "کرد", sp=""))

S.add("schappen",
  lb=LB("schappen", "d'Gromperen", "geschappt"),
  fr=FR(fr_er("épluch"), "les pommes de terre"),
  de=DE(*de_weak("schäl"), "geschält", "die Kartoffeln"),
  en=EN("peel","peels","peeled","peeling","peeled","the potatoes"),
  fa=FA(fa_("پوست سیب_زمینی_ها را"), "کن", "کند"))
