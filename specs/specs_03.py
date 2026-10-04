# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

def L(inf, rest, **kw):
    # regular -éieren verb: no ge- in participle
    return LB(inf, rest, inf[:-2] + "t", **kw)

SHO6 = ["می‌شوم","می‌شوی","می‌شود","می‌شویم","می‌شوید","می‌شوند"]
SHS6 = ["شوم","شوی","شود","شویم","شوید","شوند"]

S.add("regéieren",
  lb=L("regéieren", "d'Land"),
  fr=FR(fr_er("gouvern"), "le pays"),
  de=DE(*de_weak("regier"), "regiert", "das Land"),
  en=EN("govern","governs","governed","governing","governed","the country"),
  fa=FA("بر کشور حکومت", "کن", "کرد", sp=""))

S.add("registréieren",
  lb=L("registréieren", "den Numm op der Lëscht"),
  fr=FR(fr_er("enregistr"), "le nom sur la liste"),
  de=DE(*de_weak("registrier"), "registriert", "den Namen auf der Liste"),
  en=EN("register","registers","registered","registering","registered","the name on the list"),
  fa=FA("نام را در فهرست ثبت", "کن", "کرد", sp=""))

S.add("regléieren",
  lb=L("regléieren", "d'Heizung"),
  fr=FR(fr_er("régl", "règl"), "le chauffage"),
  de=DE(*de_weak("stell"), "eingestellt", "die Heizung", part="ein", inf="einstellen"),
  en=EN("adjust","adjusts","adjusted","adjusting","adjusted","the heating"),
  fa=FA("شوفاژ را تنظیم", "کن", "کرد", sp=""))

S.add("reglementéieren",
  lb=L("reglementéieren", "de Verkéier an der Stad"),
  fr=FR(fr_er("réglement"), "la circulation en ville"),
  de=DE(*de_weak("reglementier"), "reglementiert", "den Verkehr in der Stadt"),
  en=EN("regulate","regulates","regulated","regulating","regulated","the traffic in the city"),
  fa=FA("ترافیک را در شهر قانون‌مند", "کن", "کرد", sp=""))

S.add("regrettéieren",
  lb=L("regrettéieren", "d'Decisioun"),
  fr=FR(fr_er("regrett"), "la décision"),
  de=DE(*de_weak("bedauer"), "bedauert", "die Entscheidung"),
  en=EN("regret","regrets","regretted","regretting","regretted","the decision"),
  fa=FA("از این تصمیم افسوس", "خور", "خورد"))

S.add("rehabilitéieren",
  lb=L("rehabilitéieren", "de Buergermeeschter"),
  fr=FR(fr_er("réhabilit"), "le maire"),
  de=DE(*de_weak("rehabilitier"), "rehabilitiert", "den Bürgermeister"),
  en=EN("rehabilitate","rehabilitates","rehabilitated","rehabilitating","rehabilitated","the mayor"),
  fa=FA("از شهردار اعاده حیثیت", "کن", "کرد", sp=""))

S.add("reiden",
  lb=LB("reiden", "e Päerd am Bësch", "geridden", pres=["reiden","reids","reit","reiden","reit","reiden"]),
  fr=FR(fr_er("mont"), "un cheval dans la forêt"),
  de=DE(["reite","reitest","reitet","reiten","reitet","reiten"],
        ["ritt","rittst","ritt","ritten","rittet","ritten"], "geritten", "ein Pferd im Wald"),
  en=EN("ride","rides","rode","riding","ridden","a horse in the forest"),
  fa=FA("در جنگل اسب‌سواری", "کن", "کرد", sp=""))

S.add("réieren",
  lb=LB("réieren", "d'Publikum", "geréiert"),
  fr=FR(fr_irr(["émeus","émeus","émeut","émouvons","émouvez","émeuvent"], "ému",
               ["émus","émus","émut","émûmes","émûtes","émurent"], "émouvr"),
        "le public"),
  de=DE(*de_weak("rühr"), "gerührt", "das Publikum"),
  en=EN("move","moves","moved","moving","moved","the audience"),
  fa=FA("تماشاگران را متأثر", "کن", "کرد", sp=""))

S.add("reimen",
  lb=LB("reimen", "am Gedicht", "gereimt"),
  fr=FR(fr_er("rim"), "dans le poème"),
  de=DE(*de_weak("reim"), "gereimt", "im Gedicht"),
  en=EN("rhyme","rhymes","rhymed","rhyming","rhymed","in the poem"),
  fa=FA("در شعر قافیه‌بندی", "کن", "کرد", sp=""))

S.add("réischteren",
  lb=LB("réischteren", "de Kaffi", "geréischtert"),
  fr=FR(fr_er("torréfi"), "le café"),
  de=DE(*de_weak("röst", dt=True), "geröstet", "den Kaffee"),
  en=EN("roast","roasts","roasted","roasting","roasted","the coffee"),
  fa=FA("قهوه را برشته", "کن", "کرد", sp=""))

S.add("reiwen",
  lb=LB("reiwen", "de Fleck mat engem Lomp", "geriwwen", pres=["reiwen","reifs","reift","reiwen","reift","reiwen"]),
  fr=FR(fr_er("frott"), "la tache avec un chiffon"),
  de=DE(["reibe","reibst","reibt","reiben","reibt","reiben"],
        ["rieb","riebst","rieb","rieben","riebt","rieben"], "gerieben", "den Fleck mit einem Lappen"),
  en=EN("rub","rubs","rubbed","rubbing","rubbed","the stain with a cloth"),
  fa=FA("لکه را با پارچه", "مال", "مالید"))

S.add("reizen",
  lb=LB("reizen", "den Hond mat engem Knach", "gereizt"),
  fr=FR(fr_er("tent"), "le chien avec un os"),
  de=DE(*de_weak("reiz", sib=True), "gereizt", "den Hund mit einem Knochen"),
  en=EN("tempt","tempts","tempted","tempting","tempted","the dog with a bone"),
  fa=FA("سگ را با یک استخوان وسوسه", "کن", "کرد", sp=""))

S.add("rekapituléieren",
  lb=L("rekapituléieren", "d'Resultater"),
  fr=FR(fr_er("récapitul"), "les résultats"),
  de=DE(*de_weak("rekapitulier"), "rekapituliert", "die Ergebnisse"),
  en=EN("recapitulate","recapitulates","recapitulated","recapitulating","recapitulated","the results"),
  fa=FA("نتایج را جمع‌بندی", "کن", "کرد", sp=""))

S.add("reklaméieren",
  lb=L("reklaméieren", "eng Entschiedegung"),
  fr=FR(fr_er("réclam"), "une indemnité"),
  de=DE(*de_weak("forder"), "gefordert", "eine Entschädigung"),
  en=EN("demand","demands","demanded","demanding","demanded","compensation"),
  fa=FA("غرامت را مطالبه", "کن", "کرد", sp=""))

S.add("rekonstruéieren",
  lb=L("rekonstruéieren", "d'Bréck"),
  fr=FR(fr_irr(["reconstruis","reconstruis","reconstruit","reconstruisons","reconstruisez","reconstruisent"], "reconstruit",
               ["reconstruisis","reconstruisis","reconstruisit","reconstruisîmes","reconstruisîtes","reconstruisirent"], "reconstruir"),
        "le pont"),
  de=DE(*de_weak("rekonstruier"), "rekonstruiert", "die Brücke"),
  en=EN("reconstruct","reconstructs","reconstructed","reconstructing","reconstructed","the bridge"),
  fa=FA("پل را بازسازی", "کن", "کرد", sp=""))

S.add("rekrutéieren",
  lb=L("rekrutéieren", "nei Mataarbechter"),
  fr=FR(fr_er("recrut"), "de nouveaux employés"),
  de=DE(*de_weak("rekrutier"), "rekrutiert", "neue Mitarbeiter"),
  en=EN("recruit","recruits","recruited","recruiting","recruited","new employees"),
  fa=FA("کارمندان جدید را استخدام", "کن", "کرد", sp=""))

S.add("rektifizéieren",
  lb=L("rektifizéieren", "e Fehler"),
  fr=FR(fr_er("rectifi"), "une erreur"),
  de=DE(*de_weak("stell"), "richtiggestellt", "einen Fehler", part="richtig", inf="richtigstellen"),
  en=EN("rectify","rectifies","rectified","rectifying","rectified","an error"),
  fa=FA("یک اشتباه را اصلاح", "کن", "کرد", sp=""))

S.add("relancéieren",
  lb=L("relancéieren", "d'Wirtschaft"),
  fr=FR(fr_er("relanc"), "l'économie"),
  de=DE(*de_weak("kurbel"), "angekurbelt", "die Wirtschaft", part="an", inf="ankurbeln"),
  en=EN("boost","boosts","boosted","boosting","boosted","the economy"),
  fa=FA("اقتصاد را احیا", "کن", "کرد", sp=""))

S.add("relativéieren",
  lb=L("relativéieren", "d'Situatioun"),
  fr=FR(fr_er("relativis"), "la situation"),
  de=DE(*de_weak("relativier"), "relativiert", "die Situation"),
  en=EN("put","puts","put","putting","put","the situation in perspective"),
  fa=FA("وضعیت را نسبی", "کن", "کرد", sp=""))

S.add("relaxen",
  lb=LB("relaxen", "am Gaart", "gerelaxt"),
  fr=FR(fr_er("relax"), "au jardin", aux="être", refl=True),
  de=DE(*de_weak("relax", sib=True), "relaxt", "im Garten"),
  en=EN("relax","relaxes","relaxed","relaxing","relaxed","in the garden"),
  fa=FA("در باغ ریلکس", "کن", "کرد", sp=""))

S.add("rembourséieren",
  lb=L("rembourséieren", "d'Käschten"),
  fr=FR(fr_er("rembours"), "les frais"),
  de=DE(*de_weak("erstatt", dt=True), "erstattet", "die Kosten"),
  en=EN("reimburse","reimburses","reimbursed","reimbursing","reimbursed","the costs"),
  fa=FA("هزینه‌ها را بازپرداخت", "کن", "کرد", sp=""))

S.add("remplacéieren",
  lb=L("remplacéieren", "d'Batterie"),
  fr=FR(fr_er("remplac"), "la batterie"),
  de=DE(*de_weak("ersetz", sib=True), "ersetzt", "die Batterie"),
  en=EN("replace","replaces","replaced","replacing","replaced","the battery"),
  fa=FA("باتری را عوض", "کن", "کرد", sp=""))

S.add("renforcéieren",
  lb=L("renforcéieren", "d'Mauer"),
  fr=FR(fr_er("renforc"), "le mur"),
  de=DE(*de_weak("verstärk"), "verstärkt", "die Mauer"),
  en=EN("reinforce","reinforces","reinforced","reinforcing","reinforced","the wall"),
  fa=FA("دیوار را تقویت", "کن", "کرد", sp=""))

S.add("rengegen",
  lb=LB("rengegen", "d'Waasser", "gerengegt"),
  fr=FR(fr_er("purifi"), "l'eau"),
  de=DE(*de_weak("reinig"), "gereinigt", "das Wasser"),
  en=EN("purify","purifies","purified","purifying","purified","the water"),
  fa=FA("آب را تصفیه", "کن", "کرد", sp=""))

S.add("réngen",
  lb=LB("réngen", "an der Sporthal", "geréngt"),
  fr=FR(fr_er("lutt"), "dans la salle de sport"),
  de=DE(["ringe","ringst","ringt","ringen","ringt","ringen"],
        ["rang","rangst","rang","rangen","rangt","rangen"], "gerungen", "in der Sporthalle"),
  en=EN("wrestle","wrestles","wrestled","wrestling","wrestled","in the gym"),
  fa=FA("در سالن ورزشی کشتی", "گیر", "گرفت"))

S.add("renkelen",
  lb=LB("renkelen", "de Camion duerch d'Gaass", "gerenkelt"),
  fr=FR(fr_er("manœuvr"), "le camion dans la ruelle"),
  de=DE(*de_weak("lenk"), "gelenkt", "den Lastwagen durch die Gasse"),
  en=EN("manoeuvre","manoeuvres","manoeuvred","manoeuvring","manoeuvred","the truck through the alley"),
  fa=FA("کامیون را از میان کوچه هدایت", "کن", "کرد", sp=""))

S.add("rennen",
  lb=LB("rennen", "duerch de Park", "gerannt", aux="sinn"),
  fr=FR(fr_irr(["cours","cours","court","courons","courez","courent"], "couru",
               ["courus","courus","courut","courûmes","courûtes","coururent"], "courr"),
        "dans le parc"),
  de=DE(["renne","rennst","rennt","rennen","rennt","rennen"],
        ["rannte","ranntest","rannte","rannten","ranntet","rannten"], "gerannt", "durch den Park", aux="sein"),
  en=EN("run","runs","ran","running","run","through the park"),
  fa=FA("در پارک", "دو", "دوید",
        pres6=["می‌دوم","می‌دوی","می‌دود","می‌دویم","می‌دوید","می‌دوند"],
        subj6=["بدوم","بدوی","بدود","بدویم","بدوید","بدوند"]))

S.add("rënnen",
  lb=LB("rënnen", "d'Eck vum Dësch", "gerënnt"),
  fr=FR(fr_ir("arrond"), "le coin de la table"),
  de=DE(*de_weak("rund", dt=True), "abgerundet", "die Ecke des Tisches", part="ab", inf="abrunden"),
  en=EN("round off","rounds off","rounded off","rounding off","rounded off","the corner of the table"),
  fa=FA("گوشه میز را گرد", "کن", "کرد", sp=""))

S.add("renovéieren",
  lb=L("renovéieren", "d'Kichen"),
  fr=FR(fr_er("rénov"), "la cuisine"),
  de=DE(*de_weak("renovier"), "renoviert", "die Küche"),
  en=EN("renovate","renovates","renovated","renovating","renovated","the kitchen"),
  fa=FA("آشپزخانه را نوسازی", "کن", "کرد", sp=""))

S.add("rëntgen",
  lb=LB("rëntgen", "d'Lunge", "gerëntgt"),
  fr=FR(fr_er("radiographi"), "les poumons"),
  de=DE(*de_weak("röntg"), "geröntgt", "die Lunge"),
  en=EN("X-ray","X-rays","X-rayed","X-raying","X-rayed","the lungs"),
  fa=FA("ریه‌ها را رادیوگرافی", "کن", "کرد", sp=""))

S.add("reparéieren",
  lb=L("reparéieren", "de Vëlo"),
  fr=FR(fr_er("répar"), "le vélo"),
  de=DE(*de_weak("reparier"), "repariert", "das Fahrrad"),
  en=EN("repair","repairs","repaired","repairing","repaired","the bicycle"),
  fa=FA("دوچرخه را تعمیر", "کن", "کرد", sp=""))

S.add("repiquéieren",
  lb=L("repiquéieren", "d'Plänzercher"),
  fr=FR(fr_er("repiqu"), "les plants"),
  de=DE(*de_weak("vereinzel"), "vereinzelt", "die Setzlinge"),
  en=EN("prick out","pricks out","pricked out","pricking out","pricked out","the seedlings"),
  fa=FA("نهال‌ها را نشا", "کن", "کرد", sp=""))

S.add("representéieren",
  lb=L("representéieren", "d'Firma"),
  fr=FR(fr_er("représent"), "l'entreprise"),
  de=DE(["vertrete","vertrittst","vertritt","vertreten","vertretet","vertreten"],
        ["vertrat","vertratst","vertrat","vertraten","vertratet","vertraten"], "vertreten", "die Firma"),
  en=EN("represent","represents","represented","representing","represented","the company"),
  fa=FA("شرکت را نمایندگی", "کن", "کرد", sp=""))

S.add("reproduzéieren",
  lb=L("reproduzéieren", "d'Bild"),
  fr=FR(fr_irr(["reproduis","reproduis","reproduit","reproduisons","reproduisez","reproduisent"], "reproduit",
               ["reproduisis","reproduisis","reproduisit","reproduisîmes","reproduisîtes","reproduisirent"], "reproduir"),
        "le tableau"),
  de=DE(*de_weak("reproduzier"), "reproduziert", "das Gemälde"),
  en=EN("reproduce","reproduces","reproduced","reproducing","reproduced","the painting"),
  fa=FA("تابلو را بازتولید", "کن", "کرد", sp=""))

S.add("repsen",
  lb=LB("repsen", "no dem Iessen", "gerepst"),
  fr=FR(fr_er("rot"), "après le repas"),
  de=DE(*de_weak("rülps", sib=True), "gerülpst", "nach dem Essen"),
  en=EN("burp","burps","burped","burping","burped","after the meal"),
  fa=FA("بعد از غذا آروغ", "زن", "زد"))

S.add("rëschten",
  lb=LB("rëschten", "de Chrëschtbam", "gerëscht", pres=["rëschten","rëschts","rëscht","rëschten","rëscht","rëschten"]),
  fr=FR(fr_er("décor"), "le sapin de Noël"),
  de=DE(*de_weak("schmück"), "geschmückt", "den Weihnachtsbaum"),
  en=EN("decorate","decorates","decorated","decorating","decorated","the Christmas tree"),
  fa=FA("درخت کریسمس را تزئین", "کن", "کرد", sp=""))

S.add("rëselen",
  lb=LB("rëselen", "d'Fläsch", "gerëselt"),
  fr=FR(fr_er("secou"), "la bouteille"),
  de=DE(*de_weak("schüttel"), "geschüttelt", "die Flasche"),
  en=EN("shake","shakes","shook","shaking","shaken","the bottle"),
  fa=FA("بطری را تکان", "ده", "داد"))

S.add("reservéieren",
  lb=L("reservéieren", "en Dësch am Restaurant"),
  fr=FR(fr_er("réserv"), "une table au restaurant"),
  de=DE(*de_weak("reservier"), "reserviert", "einen Tisch im Restaurant"),
  en=EN("reserve","reserves","reserved","reserving","reserved","a table at the restaurant"),
  fa=FA("یک میز را در رستوران رزرو", "کن", "کرد", sp=""))

S.add("residéieren",
  lb=L("residéieren", "an der Haaptstad"),
  fr=FR(fr_er("résid"), "dans la capitale"),
  de=DE(*de_weak("residier"), "residiert", "in der Hauptstadt"),
  en=EN("reside","resides","resided","residing","resided","in the capital"),
  fa=FA("در پایتخت سکونت", "کن", "کرد", sp=""))

S.add("resignéieren",
  lb=L("resignéieren", "no der Néierlag"),
  fr=FR(fr_er("résign"), "après la défaite", aux="être", refl=True),
  de=DE(*de_weak("resignier"), "resigniert", "nach der Niederlage"),
  en=EN("give up","gives up","gave up","giving up","given up","after the defeat"),
  fa=FA("پس از شکست تسلیم", "شو", "شد", pres6=SHO6, subj6=SHS6))

S.add("resistéieren",
  lb=L("resistéieren", "der Versuchung"),
  fr=FR(fr_er("résist"), "à la tentation"),
  de=DE(["widerstehe","widerstehst","widersteht","widerstehen","widersteht","widerstehen"],
        ["widerstand","widerstandest","widerstand","widerstanden","widerstandet","widerstanden"],
        "widerstanden", "der Versuchung"),
  en=EN("resist","resists","resisted","resisting","resisted","the temptation"),
  fa=FA("در برابر وسوسه مقاومت", "کن", "کرد", sp=""))

S.add("respektéieren",
  lb=L("respektéieren", "d'Reegelen"),
  fr=FR(fr_er("respect"), "les règles"),
  de=DE(*de_weak("acht", dt=True), "geachtet", "die Regeln"),
  en=EN("respect","respects","respected","respecting","respected","the rules"),
  fa=FA("به قوانین احترام", "گذار", "گذاشت"))

S.add("restauréieren",
  lb=L("restauréieren", "d'Kierch"),
  fr=FR(fr_er("restaur"), "l'église"),
  de=DE(*de_weak("restaurier"), "restauriert", "die Kirche"),
  en=EN("restore","restores","restored","restoring","restored","the church"),
  fa=FA("کلیسا را مرمت", "کن", "کرد", sp=""))

S.add("restrukturéieren",
  lb=L("restrukturéieren", "d'Ofdeelung"),
  fr=FR(fr_er("restructur"), "le service"),
  de=DE(*de_weak("restrukturier"), "restrukturiert", "die Abteilung"),
  en=EN("restructure","restructures","restructured","restructuring","restructured","the department"),
  fa=FA("ساختار بخش را بازسازی", "کن", "کرد", sp=""))

S.add("resüméieren",
  lb=L("resüméieren", "den Text"),
  fr=FR(fr_er("résum"), "le texte"),
  de=DE(*de_weak("fass", sib=True), "zusammengefasst", "den Text", part="zusammen", inf="zusammenfassen"),
  en=EN("summarize","summarizes","summarized","summarizing","summarized","the text"),
  fa=FA("متن را خلاصه", "کن", "کرد", sp=""))

S.add("rëtschen",
  lb=LB("rëtschen", "um Äis", "gerëtscht", aux="sinn"),
  fr=FR(fr_er("gliss"), "sur la glace"),
  de=DE(*de_weak("rutsch"), "gerutscht", "auf dem Eis", aux="sein"),
  en=EN("slip","slips","slipped","slipping","slipped","on the ice"),
  fa=FA("روی یخ لیز", "خور", "خورد"))

S.add("retten",
  lb=LB("retten", "d'Kand aus dem Feier", "gerett", pres=["retten","rettst","rett","retten","rett","retten"]),
  fr=FR(fr_er("sauv"), "l'enfant du feu"),
  de=DE(*de_weak("rett", dt=True), "gerettet", "das Kind aus dem Feuer"),
  en=EN("rescue","rescues","rescued","rescuing","rescued","the child from the fire"),
  fa=FA("کودک را از آتش نجات", "ده", "داد"))

S.add("retuschéieren",
  lb=L("retuschéieren", "d'Box"),
  fr=FR(fr_er("retouch"), "le pantalon"),
  de=DE(*de_weak("änder"), "umgeändert", "die Hose", part="um", inf="umändern"),
  en=EN("alter","alters","altered","altering","altered","the trousers"),
  fa=FA("شلوار را اصلاح", "کن", "کرد", sp=""))

S.add("rëtzen",
  lb=LB("rëtzen", "e Häerz an de Bam", "gerëtzt"),
  fr=FR(fr_er("grav"), "un cœur dans l'arbre"),
  de=DE(*de_weak("ritz", sib=True), "geritzt", "ein Herz in den Baum"),
  en=EN("carve","carves","carved","carving","carved","a heart in the tree"),
  fa=FA("روی درخت یک قلب حک", "کن", "کرد", sp=""))

S.add("reusséieren",
  lb=L("reusséieren", "am Examen"),
  fr=FR(fr_ir("réuss"), "l'examen"),
  de=DE(["bestehe","bestehst","besteht","bestehen","besteht","bestehen"],
        ["bestand","bestandest","bestand","bestanden","bestandet","bestanden"], "bestanden", "die Prüfung"),
  en=EN("pass","passes","passed","passing","passed","the exam"),
  fa=FA("در امتحان موفق", "شو", "شد", pres6=SHO6, subj6=SHS6))
