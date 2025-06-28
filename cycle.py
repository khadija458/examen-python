# Module cycles.py (Membre 2)
import random
from datetime import datetime
from membres import membres, charger as charger_membres, sauvegarder
import json

cycle_actuel = 1
historique_tirages = []

def effectuer_tirage():
    charger_membres()
    cotisations_completes = all(
        any(c["cycle"] == cycle_actuel for c in m["cotisations"])
        for m in membres if m["actif"]
    )
    if not cotisations_completes:
        print("⛔ Tirage bloqué : tous les membres n'ont pas cotisé.")
        return

    eligibles = [
        m for m in membres
        if m["actif"] and cycle_actuel not in m["gains_annuels"]
    ]
    if not eligibles:
        print("🎉 Tous les membres ont déjà gagné cette année.")
        return

    gagnant = random.choice(eligibles)
    montant_total = sum(
        sum(c["montant"] for c in m["cotisations"] if c["cycle"] == cycle_actuel)
        for m in membres
    )
    attribuer_gain(gagnant["id"], montant_total)

def attribuer_gain(gagnant_id, montant_total):
    charger_membres()
    for m in membres:
        if m["id"] == gagnant_id:
            m["dernier_gain"] = str(datetime.today().date())
            m["gains_annuels"].append(cycle_actuel)
            historique_tirages.append({
                "cycle": cycle_actuel,
                "gagnant": m["nom"],
                "montant": montant_total
            })
            print(f"📣 {m['nom']} remporte {montant_total} FCFA (cycle {cycle_actuel}) !")
            print(f"📩 SMS envoyé à {m['nom']} (simulé)")
            break
    sauvegarder()

def afficher_historique():
    for t in historique_tirages:
        print(f"Cycle {t['cycle']} — Gagnant: {t['gagnant']} — Montant: {t['montant']} FCFA")
