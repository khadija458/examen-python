# Module membres.py (Membre 1)
import json
from datetime import datetime
from encrypt import chiffrer_tel
FICHIER = "tontine_data.json"

membres = []

def charger():
    global membres
    try:
        with open(FICHIER, "r") as f:
            membres.clear()
            membres.extend(json.load(f))
    except FileNotFoundError:
        membres.clear()

def sauvegarder():
    with open(FICHIER, "w") as f:
        json.dump(membres, f, indent=2)

def tel_existe(tel_chiffre):
    return any(m["tel"] == tel_chiffre for m in membres)

def ajouter_membre(nom, tel):
    charger()
    tel_chiffre = chiffrer_tel(tel)
    if tel_existe(tel_chiffre):
        print("⚠️ Membre déjà inscrit.")
        return
    new_id = max((m["id"] for m in membres), default=0) + 1
    membre = {
        "id": new_id,
        "nom": nom,
        "tel": tel_chiffre,
        "actif": True,
        "cotisations": [],
        "retards": 0,
        "dernier_gain": None,
        "gains_annuels": []
    }
    membres.append(membre)
    sauvegarder()
    print(f"✅ Membre {nom} ajouté.")

def desactiver_membre(membre_id):
    charger()
    for m in membres:
        if m["id"] == membre_id:
            m["actif"] = False
            sauvegarder()
            print(f"🔕 {m['nom']} désactivé.")
            return

def enregistrer_cotisation(membre_id, montant, date, cycle):
    charger()
    for m in membres:
        if m["id"] == membre_id:
            if any(c["cycle"] == cycle for c in m["cotisations"]):
                print("⚠️ Déjà cotisé ce cycle.")
                return
            m["cotisations"].append({
                "montant": montant,
                "date": date,
                "cycle": cycle
            })
            sauvegarder()
            return

def verifier_retards(membre_id, cycle):
    charger()
    for m in membres:
        if m["id"] == membre_id:
            cotise = any(c["cycle"] == cycle for c in m["cotisations"])
            if not cotise:
                m["retards"] += 1
                if m["retards"] >= 3:
                    m["actif"] = False
            sauvegarder()
            return not cotise
