# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

S.add("positionéieren",
  lb=LB("positionéieren", "d'Kamera um Stativ", "positionéiert"),
  fr=FR(fr_er("plac"), "la caméra sur le trépied"),
  de=DE(*de_weak("positionier"), "positioniert", "die Kamera auf dem Stativ"),
  en=EN("position", "positions", "positioned", "positioning", "positioned", "the camera on the tripod"),
  fa=FA("دوربین را روی سه‌پایه قرار", "ده", "داد"))

S.add("postéieren",
  lb=LB("postéieren", "de Wuechter virun der Dier", "postéiert"),
  fr=FR(fr_er("post"), "le garde devant la porte"),
  de=DE(*de_weak("postier"), "postiert", "den Wächter vor der Tür"),
  en=EN("position", "positions", "positioned", "positioning", "positioned", "the guard at the door"),
  fa=FA("نگهبان را جلوی در مستقر", "کن", "کرد", sp=""))

S.add("posten",
  lb=LB("posten", "e Foto online", "gepost", pres=["posten","posts","post","posten","post","posten"]),
  fr=FR(fr_er("post"), "une photo en ligne"),
  de=DE(*de_weak("post", dt=True), "gepostet", "ein Foto online"),
  en=EN("post", "posts", "posted", "posting", "posted", "a photo online"),
  fa=FA("یک عکس را آنلاین منتشر", "کن", "کرد", sp=""))

S.add("postuléieren",
  lb=LB("postuléieren", "eng nei Theorie", "postuléiert"),
  fr=FR(fr_er("postul"), "une nouvelle théorie"),
  de=DE(*de_weak("postulier"), "postuliert", "eine neue Theorie"),
  en=EN("postulate", "postulates", "postulated", "postulating", "postulated", "a new theory"),
  fa=FA("یک نظریه جدید را فرض", "کن", "کرد", sp=""))

S.add("poteren",
  lb=LB("poteren", "mat der Noperin", "gepotert"),
  fr=FR(fr_er("papot"), "avec la voisine"),
  de=DE(*de_weak("plauder"), "geplaudert", "mit der Nachbarin"),
  en=EN("chat", "chats", "chatted", "chatting", "chatted", "with the neighbour"),
  fa=FA("با همسایه گپ", "زن", "زد"))

S.add("poursuivéieren",
  lb=LB("poursuivéieren", "den Déif duerch d'Stroos", "poursuivéiert"),
  fr=FR(fr_irr(["poursuis","poursuis","poursuit","poursuivons","poursuivez","poursuivent"], "poursuivi",
               ["poursuivis","poursuivis","poursuivit","poursuivîmes","poursuivîtes","poursuivirent"], "poursuivr"),
        "le voleur dans la rue"),
  de=DE(*de_weak("verfolg"), "verfolgt", "den Dieb durch die Straße"),
  en=EN("chase", "chases", "chased", "chasing", "chased", "the thief down the street"),
  fa=FA("دزد را در خیابان تعقیب", "کن", "کرد", sp=""))

S.add("praffen",
  lb=LB("praffen", "e Beemchen am Gaart", "gepraff"),
  fr=FR(fr_er("greff"), "un arbre dans le jardin"),
  de=DE(*de_weak("pfropf"), "gepfropft", "einen Baum im Garten"),
  en=EN("graft", "grafts", "grafted", "grafting", "grafted", "a tree in the garden"),
  fa=FA("درخت را در باغ پیوند", "زن", "زد"))

S.add("prägen",
  lb=LB("prägen", "eng Mënz", "geprägt"),
  fr=FR(fr_er("frapp"), "une pièce de monnaie"),
  de=DE(*de_weak("präg"), "geprägt", "eine Münze"),
  en=EN("mint", "mints", "minted", "minting", "minted", "a coin"),
  fa=FA("یک سکه را ضرب", "کن", "کرد", sp=""))

S.add("praktizéieren",
  lb=LB("praktizéieren", "Yoga all Moien", "praktizéiert"),
  fr=FR(fr_er("pratiqu"), "le yoga chaque matin"),
  de=DE(*de_weak("praktizier"), "praktiziert", "jeden Morgen Yoga"),
  en=EN("practise", "practises", "practised", "practising", "practised", "yoga every morning"),
  fa=FA("هر صبح یوگا را تمرین", "کن", "کرد", sp=""))

S.add("predominéieren",
  lb=LB("predominéieren", "an der Grupp", "predominéiert"),
  fr=FR(fr_er("prédomin"), "dans le groupe"),
  de=DE(*de_weak("herrsch"), "vorgeherrscht", "in der Gruppe", part="vor"),
  en=EN("predominate", "predominates", "predominated", "predominating", "predominated", "in the group"),
  fa=FA("در گروه غلبه", "دار", "داشت", sp="",
        pres6=["دارم","داری","دارد","داریم","دارید","دارند"],
        subj6=["داشته باشم","داشته باشی","داشته باشد","داشته باشیم","داشته باشید","داشته باشند"]))

S.add("préiwen",
  lb=LB("préiwen", "d'Schüler a Mathematik", "gepréift"),
  fr=FR(fr_er("test"), "les élèves en mathématiques"),
  de=DE(*de_weak("prüf"), "geprüft", "die Schüler in Mathe"),
  en=EN("test", "tests", "tested", "testing", "tested", "the students in maths"),
  fa=FA("دانش‌آموزان را در ریاضی امتحان", "کن", "کرد", sp=""))

S.add("preparéieren",
  lb=LB("preparéieren", "d'Owesiessen", "preparéiert"),
  fr=FR(fr_er("prépar"), "le dîner"),
  de=DE(*de_weak("bereit", dt=True), "vorbereitet", "das Abendessen", part="vor"),
  en=EN("prepare", "prepares", "prepared", "preparing", "prepared", "dinner"),
  fa=FA("شام را آماده", "کن", "کرد", sp=""))

S.add("presentéieren",
  lb=LB("presentéieren", "de Projet an der Sëtzung", "presentéiert"),
  fr=FR(fr_er("présent"), "le projet à la réunion"),
  de=DE(*de_weak("präsentier"), "präsentiert", "das Projekt in der Sitzung"),
  en=EN("present", "presents", "presented", "presenting", "presented", "the project at the meeting"),
  fa=FA("پروژه را در جلسه ارائه", "ده", "داد"))

S.add("presséieren",
  lb=LB("presséieren", "an der Stad", "presséiert"),
  fr=FR(fr_er("press"), "en ville", aux="être", refl=True),
  de=DE(*de_weak("eil"), "geeilt", "durch die Stadt", aux="sein"),
  en=EN("hurry", "hurries", "hurried", "hurrying", "hurried", "through town"),
  fa=FA("در شهر عجله", "کن", "کرد", sp=""))

S.add("pressen",
  lb=LB("pressen", "eng Zitroun", "gepresst"),
  fr=FR(fr_er("press"), "un citron"),
  de=DE(*de_weak("press", sib=True), "gepresst", "eine Zitrone"),
  en=EN("squeeze", "squeezes", "squeezed", "squeezing", "squeezed", "a lemon"),
  fa=FA("یک لیمو را فشار", "ده", "داد"))

S.add("prevenéieren",
  lb=LB("prevenéieren", "de Chef", "prevenéiert"),
  fr=FR(fr_irr(["préviens","préviens","prévient","prévenons","prévenez","préviennent"], "prévenu",
               ["prévins","prévins","prévint","prévînmes","prévîntes","prévinrent"], "préviendr",
               subj=["prévienne","préviennes","prévienne","prévenions","préveniez","préviennent"]),
        "le chef"),
  de=DE(*de_weak("verständig"), "verständigt", "den Chef"),
  en=EN("warn", "warns", "warned", "warning", "warned", "the boss"),
  fa=FA("رئیس را آگاه", "کن", "کرد", sp=""))

S.add("preziséieren",
  lb=LB("preziséieren", "déi exakt Zäit", "preziséiert"),
  fr=FR(fr_er("précis"), "l'heure exacte"),
  de=DE(*de_weak("präzisier"), "präzisiert", "die genaue Uhrzeit"),
  en=EN("specify", "specifies", "specified", "specifying", "specified", "the exact time"),
  fa=FA("زمان دقیق را مشخص", "کن", "کرد", sp=""))

S.add("priedegen",
  lb=LB("priedegen", "an der Kierch", "gepriedegt"),
  fr=FR(fr_er("prêch"), "à l'église"),
  de=DE(*de_weak("predig"), "gepredigt", "in der Kirche"),
  en=EN("preach", "preaches", "preached", "preaching", "preached", "in church"),
  fa=FA("در کلیسا موعظه", "کن", "کرد", sp=""))

S.add("printen",
  lb=LB("printen", "eng Seit", "geprint", pres=["printen","prints","print","printen","print","printen"]),
  fr=FR(fr_er("imprim"), "une page"),
  de=DE(*de_weak("druck"), "gedruckt", "eine Seite"),
  en=EN("print", "prints", "printed", "printing", "printed", "a page"),
  fa=FA("یک صفحه را چاپ", "کن", "کرد", sp=""))

S.add("privatiséieren",
  lb=LB("privatiséieren", "d'Firma", "privatiséiert"),
  fr=FR(fr_er("privatis"), "l'entreprise"),
  de=DE(*de_weak("privatisier"), "privatisiert", "die Firma"),
  en=EN("privatize", "privatizes", "privatized", "privatizing", "privatized", "the company"),
  fa=FA("شرکت را خصوصی", "کن", "کرد", sp=""))

S.add("privilegiéieren",
  lb=LB("privilegiéieren", "d'Clienten", "privilegiéiert"),
  fr=FR(fr_er("privilégi"), "les clients"),
  de=DE(*de_weak("begünstig"), "begünstigt", "die Kunden"),
  en=EN("favour", "favours", "favoured", "favouring", "favoured", "the customers"),
  fa=FA("به مشتریان امتیاز ویژه", "ده", "داد"))

S.add("probéieren",
  lb=LB("probéieren", "e neit Rezept", "probéiert"),
  fr=FR(fr_er("essay", "essai", "essaier"), "une nouvelle recette"),
  de=DE(*de_weak("probier"), "ausprobiert", "ein neues Rezept", part="aus"),
  en=EN("try", "tries", "tried", "trying", "tried", "a new recipe"),
  fa=FA("دستور پخت جدیدی را امتحان", "کن", "کرد", sp=""))

S.add("produzéieren",
  lb=LB("produzéieren", "Hunneg am Gaart", "produzéiert"),
  fr=FR(fr_irr(["produis","produis","produit","produisons","produisez","produisent"], "produit",
               ["produisis","produisis","produisit","produisîmes","produisîtes","produisirent"], "produir"),
        "du miel dans le jardin"),
  de=DE(*de_weak("produzier"), "produziert", "Honig im Garten"),
  en=EN("produce", "produces", "produced", "producing", "produced", "honey in the garden"),
  fa=FA("در باغ عسل تولید", "کن", "کرد", sp=""))

S.add("profanéieren",
  lb=LB("profanéieren", "d'Graf", "profanéiert"),
  fr=FR(fr_er("profan"), "la tombe"),
  de=DE(*de_weak("profanier"), "profaniert", "das Grab"),
  en=EN("profane", "profanes", "profaned", "profaning", "profaned", "the grave"),
  fa=FA("قبر را بی‌حرمت", "کن", "کرد", sp=""))

S.add("profitéieren",
  lb=LB("profitéieren", "vun der Sonn", "profitéiert"),
  fr=FR(fr_er("profit"), "du soleil"),
  de=DE(*de_weak("profitier"), "profitiert", "von der Sonne"),
  en=EN("benefit from", "benefits from", "benefited from", "benefiting from", "benefited from", "the sunshine"),
  fa=FA("از آفتاب بهره", "بر", "برد"))

S.add("programméieren",
  lb=LB("programméieren", "d'Reunioun fir Méindeg", "programméiert"),
  fr=FR(fr_er("programm"), "la réunion pour lundi"),
  de=DE(*de_weak("setz", sib=True), "angesetzt", "das Treffen für Montag", part="an"),
  en=EN("plan", "plans", "planned", "planning", "planned", "the meeting for Monday"),
  fa=FA("جلسه را برای دوشنبه برنامه‌ریزی", "کن", "کرد", sp=""))

S.add("projezéieren",
  lb=LB("projezéieren", "e Film op d'Mauer", "projezéiert"),
  fr=FR(fr_er("projet", "projett", "projetter"), "un film sur le mur"),
  de=DE(*de_weak("projizier"), "projiziert", "einen Film an die Wand"),
  en=EN("project", "projects", "projected", "projecting", "projected", "a film onto the wall"),
  fa=FA("یک فیلم را روی دیوار پخش", "کن", "کرد", sp=""))

S.add("proklaméieren",
  lb=LB("proklaméieren", "d'Onofhängegkeet", "proklaméiert"),
  fr=FR(fr_er("proclam"), "l'indépendance"),
  de=DE(*de_weak("proklamier"), "proklamiert", "die Unabhängigkeit"),
  en=EN("proclaim", "proclaims", "proclaimed", "proclaiming", "proclaimed", "independence"),
  fa=FA("استقلال را اعلام", "کن", "کرد", sp=""))

S.add("promovéieren",
  lb=LB("promovéieren", "jonk Talenter", "promovéiert"),
  fr=FR(fr_irr(["promeus","promeus","promeut","promouvons","promouvez","promeuvent"], "promu",
               ["promus","promus","promut","promûmes","promûtes","promurent"], "promouvr",
               subj=["promeuve","promeuves","promeuve","promouvions","promouviez","promeuvent"]),
        "les jeunes talents"),
  de=DE(*de_weak("förder"), "gefördert", "junge Talente"),
  en=EN("promote", "promotes", "promoted", "promoting", "promoted", "young talent"),
  fa=FA("از استعدادهای جوان حمایت", "کن", "کرد", sp=""))

S.add("prononcéieren",
  lb=LB("prononcéieren", "d'Wuert richteg", "prononcéiert"),
  fr=FR(fr_er("prononc"), "le mot correctement"),
  de=DE(["spreche","sprichst","spricht","sprechen","sprecht","sprechen"],
        ["sprach","sprachst","sprach","sprachen","spracht","sprachen"],
        "ausgesprochen", "das Wort richtig", part="aus"),
  en=EN("pronounce", "pronounces", "pronounced", "pronouncing", "pronounced", "the word correctly"),
  fa=FA("کلمه را درست تلفظ", "کن", "کرد", sp=""))

S.add("propagéieren",
  lb=LB("propagéieren", "eng Iddi am Dorf", "propagéiert"),
  fr=FR(fr_er("propag"), "une idée dans le village"),
  de=DE(*de_weak("verbreit", dt=True), "verbreitet", "eine Idee im Dorf"),
  en=EN("propagate", "propagates", "propagated", "propagating", "propagated", "an idea in the village"),
  fa=FA("یک ایده را در روستا ترویج", "کن", "کرد", sp=""))

S.add("prophezeien",
  lb=LB("prophezeien", "gutt Wieder fir muer", "prophezeit"),
  fr=FR(fr_er("annonc"), "du beau temps pour demain"),
  de=DE(*de_weak("prophezei"), "prophezeit", "gutes Wetter für morgen"),
  en=EN("forecast", "forecasts", "forecast", "forecasting", "forecast", "good weather for tomorrow"),
  fa=FA("هوای خوب را برای فردا پیش‌بینی", "کن", "کرد", sp=""))

S.add("proposéieren",
  lb=LB("proposéieren", "en Ausflug", "proposéiert"),
  fr=FR(fr_er("propos"), "une excursion"),
  de=DE(["schlage","schlägst","schlägt","schlagen","schlagt","schlagen"],
        ["schlug","schlugst","schlug","schlugen","schlugt","schlugen"],
        "vorgeschlagen", "einen Ausflug", part="vor"),
  en=EN("propose", "proposes", "proposed", "proposing", "proposed", "a trip"),
  fa=FA("یک گردش را پیشنهاد", "ده", "داد"))

S.add("prosten",
  lb=LB("prosten", "op d'Gesondheet", "geprost", pres=["prosten","prosts","prost","prosten","prost","prosten"]),
  fr=FR(fr_er("trinqu"), "à la santé de tous"),
  de=DE(["stoße","stößt","stößt","stoßen","stoßt","stoßen"],
        ["stieß","stießt","stieß","stießen","stießt","stießen"],
        "angestoßen", "auf die Gesundheit aller", part="an"),
  en=EN("drink", "drinks", "drank", "drinking", "drunk", "to everyone's health"),
  fa=FA("به سلامتی همه", "نوش", "نوشید"))

S.add("protegéieren",
  lb=LB("protegéieren", "d'Kanner virun der Sonn", "protegéiert"),
  fr=FR(fr_er("protég", "protèg", "protéger"), "les enfants contre le soleil"),
  de=DE(*de_weak("schütz", sib=True), "geschützt", "die Kinder vor der Sonne"),
  en=EN("protect", "protects", "protected", "protecting", "protected", "the children from the sun"),
  fa=FA("از کودکان در برابر آفتاب محافظت", "کن", "کرد", sp=""))

S.add("protestéieren",
  lb=LB("protestéieren", "géint dat neit Gesetz", "protestéiert"),
  fr=FR(fr_er("protest"), "contre la nouvelle loi"),
  de=DE(*de_weak("protestier"), "protestiert", "gegen das neue Gesetz"),
  en=EN("protest", "protests", "protested", "protesting", "protested", "against the new law"),
  fa=FA("علیه قانون جدید اعتراض", "کن", "کرد", sp=""))

S.add("protokolléieren",
  lb=LB("protokolléieren", "d'Decisiounen", "protokolléiert"),
  fr=FR(fr_er("consign"), "les décisions"),
  de=DE(*de_weak("protokollier"), "protokolliert", "die Beschlüsse"),
  en=EN("record", "records", "recorded", "recording", "recorded", "the decisions"),
  fa=FA("تصمیم‌ها را ثبت", "کن", "کرد", sp=""))

S.add("prouwen",
  lb=LB("prouwen", "d'Theaterstéck", "geprouwt"),
  fr=FR(fr_er("répét", "répèt", "répéter"), "la pièce de théâtre"),
  de=DE(*de_weak("prob"), "geprobt", "das Theaterstück"),
  en=EN("rehearse", "rehearses", "rehearsed", "rehearsing", "rehearsed", "the play"),
  fa=FA("نمایش را تمرین", "کن", "کرد", sp=""))

S.add("provozéieren",
  lb=LB("provozéieren", "den Noper", "provozéiert"),
  fr=FR(fr_er("provoqu"), "le voisin"),
  de=DE(*de_weak("provozier"), "provoziert", "den Nachbarn"),
  en=EN("provoke", "provokes", "provoked", "provoking", "provoked", "the neighbour"),
  fa=FA("همسایه را تحریک", "کن", "کرد", sp=""))

S.add("publizéieren",
  lb=LB("publizéieren", "e Buch", "publizéiert"),
  fr=FR(fr_er("publi"), "un livre"),
  de=DE(*de_weak("veröffentlich"), "veröffentlicht", "ein Buch"),
  en=EN("publish", "publishes", "published", "publishing", "published", "a book"),
  fa=FA("یک کتاب را منتشر", "کن", "کرد", sp=""))

S.add("puchen",
  lb=LB("puchen", "de Ball iwwer d'Mauer", "gepucht"),
  fr=FR(fr_er("jet", "jett", "jetter"), "la balle par-dessus le mur"),
  de=DE(["schmeiße","schmeißt","schmeißt","schmeißen","schmeißt","schmeißen"],
        ["schmiss","schmissest","schmiss","schmissen","schmisst","schmissen"],
        "geschmissen", "den Ball über die Mauer"),
  en=EN("throw", "throws", "threw", "throwing", "thrown", "the ball over the wall"),
  fa=FA("توپ را از روی دیوار پرت", "کن", "کرد", sp=""))

S.add("puddelen",
  lb=LB("puddelen", "am Bach", "gepuddelt"),
  fr=FR(fr_er("barbot"), "dans le ruisseau"),
  de=DE(*de_weak("plansch"), "geplanscht", "im Bach"),
  en=EN("splash about", "splashes about", "splashed about", "splashing about", "splashed about", "in the stream"),
  fa=FA("در جویبار آب‌بازی", "کن", "کرد", sp=""))

S.add("pudderen",
  lb=LB("pudderen", "de Kuch mat Zocker", "gepuddert"),
  fr=FR(fr_er("poudr"), "le gâteau avec du sucre glace"),
  de=DE(*de_weak("puder"), "gepudert", "den Kuchen mit Puderzucker"),
  en=EN("powder", "powders", "powdered", "powdering", "powdered", "the cake with icing sugar"),
  fa=FA("کیک را با پودر قند", "پاش", "پاشید"))

S.add("pupen",
  lb=LB("pupen", "am Bus", "gepupt"),
  fr=FR(fr_er("prout"), "dans le bus"),
  de=DE(*de_weak("pup", dt=True), "gepupt", "im Bus"),
  en=EN("break wind", "breaks wind", "broke wind", "breaking wind", "broken wind", "on the bus"),
  fa=FA("در اتوبوس", "گوز", "گوزید"))

S.add("purgen",
  lb=LB("purgen", "d'Partei", "gepurgt"),
  fr=FR(fr_er("purg"), "le parti"),
  de=DE(*de_weak("säuber"), "gesäubert", "die Partei"),
  en=EN("purge", "purges", "purged", "purging", "purged", "the party"),
  fa=FA("حزب را پاکسازی", "کن", "کرد", sp=""))

S.add("pushen",
  lb=LB("pushen", "den Akafswon", "gepusht"),
  fr=FR(fr_er("pouss"), "le caddie"),
  de=DE(["schiebe","schiebst","schiebt","schieben","schiebt","schieben"],
        ["schob","schobst","schob","schoben","schobt","schoben"],
        "geschoben", "den Einkaufswagen"),
  en=EN("push", "pushes", "pushed", "pushing", "pushed", "the trolley"),
  fa=FA("چرخ خرید را هل", "ده", "داد"))

S.add("quaken",
  lb=LB("quaken", "am Weier", "gequaakt"),
  fr=FR(fr_er("coass"), "dans l'étang"),
  de=DE(*de_weak("quak"), "gequakt", "im Teich"),
  en=EN("croak", "croaks", "croaked", "croaking", "croaked", "in the pond"),
  fa=FA("در برکه قورقور", "کن", "کرد", sp=""))

S.add("quälen",
  lb=LB("quälen", "d'Déieren", "gequält"),
  fr=FR(fr_er("maltrait"), "les animaux"),
  de=DE(*de_weak("quäl"), "gequält", "die Tiere"),
  en=EN("mistreat", "mistreats", "mistreated", "mistreating", "mistreated", "the animals"),
  fa=FA("حیوانات را آزار", "ده", "داد"))

S.add("quaselen",
  lb=LB("quaselen", "um Telefon", "gequaselt"),
  fr=FR(fr_er("papot"), "au téléphone"),
  de=DE(["quassle","quasselst","quasselt","quasseln","quasselt","quasseln"],
        ["quasselte","quasseltest","quasselte","quasselten","quasseltet","quasselten"],
        "gequasselt", "am Telefon"),
  en=EN("prattle", "prattles", "prattled", "prattling", "prattled", "on the phone"),
  fa=FA("پشت تلفن وراجی", "کن", "کرد", sp=""))

S.add("quatschen",
  lb=LB("quatschen", "an der Klass", "gequatscht"),
  fr=FR(fr_er("bavard"), "en classe"),
  de=DE(*de_weak("quatsch"), "gequatscht", "im Unterricht"),
  en=EN("witter on", "witters on", "wittered on", "wittering on", "wittered on", "in class"),
  fa=FA("در کلاس پرحرفی", "کن", "کرد", sp=""))
