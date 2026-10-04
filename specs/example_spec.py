# -*- coding: utf-8 -*-
# Reference example: shows the API for regular, reflexive, irregular/être, and modal/complement verbs.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from vlib import *
S = Specs()

# 1) regular verbs everywhere: pick apples
S.add("plécken",
  lb=LB("plécken", "d'Äppel am Gaart", "gepléckt"),
  fr=FR(fr_irr(["cueille","cueilles","cueille","cueillons","cueillez","cueillent"], "cueilli",
               ["cueillis","cueillis","cueillit","cueillîmes","cueillîtes","cueillirent"], "cueiller"),
        "les pommes dans le jardin"),
  de=DE(*de_weak("pflück"), "gepflückt", "die Äpfel im Garten"),
  en=EN("pick", "picks", "picked", "picking", "picked", "the apples in the garden"),
  fa=FA("سیب‌ها را در باغ", "چین", "چید"))

# 2) reflexive: {r} tokens in rest; fr refl=True + aux être (agree=False when a direct object follows)
S.add("sech wäschen",
  lb=LB("wäschen", "{r} am Bad", "gewäsch", pres=["wäschen","wäschs","wäscht","wäschen","wäscht","wäschen"]),
  fr=FR(fr_er("lav"), "dans la salle de bain", aux="être", refl=True),
  de=DE(["wasche","wäschst","wäscht","waschen","wascht","waschen"],
        ["wusch","wuschst","wusch","wuschen","wuscht","wuschen"], "gewaschen", "{r} im Bad"),
  en=EN("wash", "washes", "washed", "washing", "washed", "{r} in the bathroom"),
  fa=FA("خود را در حمام", "شو", "شست",
        pres6=["می‌شویم","می‌شویی","می‌شوید","می‌شوییم","می‌شویید","می‌شویند"],
        subj6=["بشویم","بشویی","بشوید","بشوییم","بشویید","بشویند"]))

# 3) separable verb + être/sein verb: part= trailing particle in main clause
S.add("fortgoen",
  lb=LB("goen", "op de Maart", "fortgaang", pres=["ginn","gees","geet","ginn","gitt","ginn"],
        aux="sinn", part="fort", inf_full="fortgoen", sub=["fortginn","fortgees","fortgeet","fortginn","fortgitt","fortginn"]),
  fr=FR(fr_irr(["pars","pars","part","partons","partez","partent"], "parti",
               ["partis","partis","partit","partîmes","partîtes","partirent"], "partir"),
        "pour le marché", aux="être"),
  de=DE(["gehe","gehst","geht","gehen","geht","gehen"], ["ging","gingst","ging","gingen","gingt","gingen"],
        "losgegangen", "zum Markt", aux="sein", part="los", inf="losgehen"),
  en=EN("leave", "leaves", "left", "leaving", "left", "for the market"),
  fa=FA("برای رفتن به بازار", "رو", "رفت",
        pres6=["می‌روم","می‌روی","می‌رود","می‌رویم","می‌روید","می‌روند"],
        subj6=["بروم","بروی","برود","برویم","بروید","بروند"]))

# 4) modal verb with infinitive complement: part=, pp= and inf=/sub= give explicit chunks
S.add("kënnen",
  lb=LB("kënnen", "gutt", "schwamme kënnen", pres=["kann","kanns","kann","kënnen","kënnt","kënnen"],
        part="schwamme", inf_full="schwamme kënnen", sub=["schwamme kann","schwamme kanns","schwamme kann","schwamme kënnen","schwamme kënnt","schwamme kënnen"]),
  fr=FR(fr_irr(["peux","peux","peut","pouvons","pouvez","peuvent"], "pu",
               ["pus","pus","put","pûmes","pûtes","purent"], "pourr",
               subj=["puisse","puisses","puisse","puissions","puissiez","puissent"],
               imp=["pouvais","pouvais","pouvait","pouvions","pouviez","pouvaient"]),
        "bien nager"),
  de=DE(["kann","kannst","kann","können","könnt","können"], ["konnte","konntest","konnte","konnten","konntet","konnten"],
        "schwimmen können", "gut", part="schwimmen", inf="schwimmen können",
        sub=["schwimmen kann","schwimmen kannst","schwimmen kann","schwimmen können","schwimmen könnt","schwimmen können"]),
  en=EN("be able to swim", "is able to swim", "was able to swim", "being able to swim",
        "been able to swim", "well", pres=["can swim"]*6),
  fa=FA("خوب شنا", "کن", "کرد", sp=""))
