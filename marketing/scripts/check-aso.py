## Free tier (Chun 2026-10-20): 10 items, 10 records per item.
# Been Ages App Store field checker (en-GB, de-DE, fr-FR).
# Run: python3 check-aso.py [gb|de|fr ...]   (check-aso-gb.py = same file, defaults to gb)
import re, sys, os
F = {}
F["gb"] = dict(
 NAME="Been Ages: Last Time Tracker",
 SUB="Days since chores, MOT & more",
 KW="reminder,habit,routine,oven,boiler,service,toothbrush,kettle,bedding,contacts,clean,radiator,descale",
 PROMO="When did you last descale the kettle, change the bedding or book the boiler service? Tap once when it's done and Been Ages counts the days. Pay once, no subscription.",
 DESC="""Been Ages remembers the jobs you only do every so often, so you don't have to.

Changed the bedding? Descaled the kettle? Swapped your toothbrush head? Tap once and Been Ages saves the date. Open it later and you'll see exactly how long it's been: 1 month 17 days, not "about a month".

WHAT YOU GET
• Log it in one tap. No forms, no faff.
• The exact time since, in months and days. Never rounded off.
• A reminder when it's due: weekly, every fortnight, monthly, yearly or any interval you like. Miss one and it nudges you again 3 days later.
• Overdue items stand out, so you can see what's slipped.
• Full history, notes and simple stats for every item: how often, on average, and the longest gap.
• Add the next due date to your Calendar.
• Share a card when you've finally done it.
• Light or dark mode.
• Deleted something by mistake? Undo it, or find it in Recently Deleted for 30 days.

IDEAS TO START WITH
Boiler service, MOT, car tax, dentist check-up, contact lenses, toothbrush head, bedding, descaling the kettle, bleeding the radiators, defrosting the freezer, cleaning the oven, the cat's flea treatment, or simply the last time you rang your nan.

PRIVATE BY DESIGN
No account and no sign-up. Your data stays on your iPhone, and we can't see what you log.

PAY ONCE
Free to download, with up to 10 items and 10 records per item. A one-off purchase gives you unlimited items and extra share card styles. No subscription. Already bought it? You can restore your purchase at any time.

Made by one developer at Tiny Toolshed. Feedback is always welcome.""",
 CAPTIONS=["Know how long it's been since anything","Exact months and days, never rounded off","A nudge when it's due again","Log it in one tap. No faff.","No account. Your data stays on your phone.","Pay once. No subscription.","Light or dark, your call"],
 BANNED=["widget","icloud","backup","back up","unlock","family sharing","launch price","£3.99","fortnight)","seamless","game-changer","—"],
)
F["de"] = dict(
 NAME="Been Ages: Zuletzt gemacht?",
 SUB="Tage seit TÜV, Wartung & Co.",
 KW="erinnerung,haushalt,putzplan,heizung,zahnbürste,kontaktlinsen,routine,termin,intervall,kalender,abo",
 PROMO="Wann hast du zuletzt die Zahnbürste gewechselt oder die Heizung warten lassen? Einmal tippen, Been Ages zählt die Tage. Einmalkauf, kein Abo, Daten bleiben lokal.",
 DESC="""Been Ages merkt sich die Dinge, die du nur ab und zu erledigst, damit du es nicht musst.

Bettwäsche gewechselt? Wasserkocher entkalkt? Neuen Bürstenkopf eingesetzt? Einmal tippen, und Been Ages speichert das Datum. Später siehst du genau, wie lange es her ist: 1 Monat und 17 Tage statt „ungefähr ein Monat“.

DAS BEKOMMST DU
• Mit einem Tipp eingetragen. Keine Formulare.
• Die genaue Zeit seit dem letzten Mal, in Monaten und Tagen. Nichts wird gerundet.
• Eine Erinnerung, wenn es wieder fällig ist: wöchentlich, alle 2 Wochen, monatlich, jährlich oder in jedem Intervall, das du willst. Verpasst? Dann erinnert dich die App 3 Tage später noch einmal.
• Überfällige Einträge fallen sofort auf.
• Verlauf, Notizen und einfache Statistik für jeden Eintrag: wie oft, im Schnitt und die längste Pause.
• Den nächsten Termin in deinen Kalender eintragen.
• Eine Karte teilen, wenn du es endlich erledigt hast.
• Heller oder dunkler Modus.
• Aus Versehen gelöscht? Rückgängig machen oder 30 Tage lang unter „Zuletzt gelöscht“ wiederfinden.

IDEEN FÜR DEN ANFANG
TÜV (Hauptuntersuchung), Heizungswartung, Reifenwechsel, Zahnarzt-Kontrolle, Kontaktlinsen, Zahnbürste, Bettwäsche, Wasserkocher entkalken, Kühlschrank abtauen, Backofen putzen, Rauchmelder testen, Entwurmung für die Katze oder einfach: wann du zuletzt Oma angerufen hast.

DEINE DATEN BLEIBEN BEI DIR
Kein Konto, keine Anmeldung. Deine Daten bleiben auf deinem iPhone, und wir sehen nicht, was du einträgst.

EINMALKAUF, KEIN ABO
Kostenlos laden, mit bis zu 10 Einträgen und je 10 Aufzeichnungen. Mit einem Einmalkauf bekommst du unbegrenzt viele Einträge und weitere Kartenstile. Kein Abo. Schon gekauft? Du kannst deinen Kauf jederzeit wiederherstellen.

Gemacht von einem einzelnen Entwickler bei Tiny Toolshed. Feedback ist jederzeit willkommen.""",
 CAPTIONS=["Sieh sofort, wie lange es her ist","Genau in Monaten und Tagen, nie gerundet","Erinnert dich, wenn es wieder fällig ist","Mit einem Tipp erledigt","Kein Konto. Deine Daten bleiben auf dem iPhone.","Einmalkauf, kein Abo","Hell oder dunkel, wie du willst"],
 BANNED=["widget","icloud","backup","sicherung","cloud","freischalt","familienfreigabe","rabatt","—"],
)
F["fr"] = dict(
 NAME="Been Ages : la dernière fois",
 SUB="Rappels : ménage, entretien…",
 KW="contrôle,technique,ramonage,chaudière,brosse,dents,lentilles,tâches,maison,routine,suivi,jours",
 PROMO="Quand avez-vous changé votre brosse à dents ou fait ramoner la cheminée pour la dernière fois ? Un geste, et Been Ages compte les jours. Achat unique, sans abonnement.",
 DESC="""Been Ages se souvient à votre place des choses que vous ne faites que de temps en temps.

Draps changés ? Bouilloire détartrée ? Nouvelle tête de brosse à dents ? Un geste, et Been Ages enregistre la date. Plus tard, vous voyez exactement depuis combien de temps : 1 mois et 17 jours, et non « environ un mois ».

CE QUE VOUS AVEZ
• Noté en un seul geste. Aucun formulaire.
• Le temps exact écoulé, en mois et en jours. Sans arrondi.
• Un rappel quand c'est le moment : chaque semaine, toutes les 2 semaines, chaque mois, chaque année ou à l'intervalle de votre choix. Rappel manqué ? L'app vous le redit 3 jours plus tard.
• Les éléments en retard se repèrent tout de suite.
• Historique, notes et statistiques simples pour chaque élément : combien de fois, en moyenne, et le plus long écart.
• Ajout de la prochaine échéance à votre Calendrier.
• Une carte à partager quand c'est enfin fait.
• Mode clair ou sombre.
• Supprimé par erreur ? Annulez, ou retrouvez-le pendant 30 jours dans « Supprimés récemment ».

DES IDÉES POUR COMMENCER
Contrôle technique, ramonage, entretien de la chaudière, rendez-vous chez le dentiste, lentilles, brosse à dents, draps, détartrage de la bouilloire, dégivrage du congélateur, nettoyage du four, vermifuge du chat, ou tout simplement la dernière fois que vous avez appelé votre grand-mère.

VOS DONNÉES RESTENT CHEZ VOUS
Sans compte, sans inscription. Vos données restent sur votre iPhone et nous ne voyons pas ce que vous notez.

ACHAT UNIQUE, SANS ABONNEMENT
Téléchargement gratuit, jusqu'à 10 éléments et 10 enregistrements par élément. Un achat unique vous donne des éléments illimités et d'autres styles de cartes. Sans abonnement. Déjà acheté ? Vous pouvez restaurer votre achat à tout moment.

Créé par un développeur indépendant chez Tiny Toolshed. Vos retours sont les bienvenus.""",
 CAPTIONS=["Voyez d'un coup d'œil depuis quand","En mois et en jours, sans arrondi","Un rappel quand c'est le moment","Noté en un seul geste","Sans compte. Vos données restent sur l'iPhone.","Achat unique, sans abonnement","Clair ou sombre, à vous de choisir"],
 BANNED=["widget","icloud","backup","sauvegarde","cloud","débloqu","partage familial","promo","—"],
)
def words(s): return [w for w in re.split(r"[^\wäöüßàâçéèêëîïôûùüÿœæ]+", s.lower()) if w]
def check(loc):
    f=F[loc]; ok=True; print(f"== {loc}")
    def rep(label,s,limit,bytes_=False):
        nonlocal ok
        n=len(s.encode("utf-8")) if bytes_ else len(s); ok&=n<=limit
        print(f"  {label:12} {len(s):5} chars {len(s.encode('utf-8')):5} bytes  limit {limit}{' bytes' if bytes_ else ' chars'}  {'OK' if n<=limit else 'OVER'}")
    rep("name",f["NAME"],30); rep("subtitle",f["SUB"],30); rep("keywords",f["KW"],100,True)
    rep("promo",f["PROMO"],170); rep("description",f["DESC"],4000)
    for i,c in enumerate(f["CAPTIONS"],1): print(f"  caption {i}    {len(c):3} chars  {c}")
    if len(f["CAPTIONS"])!=7: ok=False; print("  need 7 captions")
    kw=f["KW"].split(","); n=set(words(f["NAME"])); s=set(words(f["SUB"])); k=set(w for x in kw for w in words(x))
    for lab,v in (("name∩subtitle",n&s),("name∩keywords",n&k),("subtitle∩keywords",s&k),("keyword repeats",{x for x in kw if kw.count(x)>1})):
        print(f"  {lab:18} {sorted(v) if v else 'none'}"); ok&=not v
    sp=" " in f["KW"]; print("  spaces in keywords:",sp); ok&=not sp
    allw=n|s|k; pl=[w for w in allw if (w.endswith("s") or w.endswith("n")) and w[:-1] in allw]
    print("  plural overlaps:",pl or "none"); ok&=not pl
    blob=" ".join([f["NAME"],f["SUB"],f["KW"],f["PROMO"],f["DESC"]]+f["CAPTIONS"]).lower()
    hit=[b for b in f["BANNED"] if b in blob]; print("  banned words:",hit or "none"); ok&=not hit
    if loc=="gb":
        us=re.findall(r"\b(\w+iz(?:e|es|ed|ing|ation)|color\w*|favorit\w*|center\w*|tires?|vacuum\w*|mom)\b",blob)
        print("  US spellings:",us or "none"); ok&=not us
    print("  RESULT:","PASS" if ok else "FAIL"); return ok
if __name__=="__main__":
    args=sys.argv[1:] or (["gb"] if "-gb" in os.path.basename(sys.argv[0]) else ["gb","de","fr"])
    res=[check(a) for a in args]; sys.exit(0 if all(res) else 1)
