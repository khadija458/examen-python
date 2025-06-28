# . Module finances.py (Membre 3)
from membres import membres, charger as charger_membres, sauvegarder
from datetime import datetime, timedelta
import csv
import matplotlib.pyplot as plt

COTISATION_MENSUELLE = 5000

def calculer_montant_cycle(cycle):
    charger_membres()
    total = 0
    for m in membres:
        for c in m["cotisations"]:
            if c["cycle"] == cycle:
                total += c["montant"]
    return total

def generer_rapport_mensuel(cycle):
    charger_membres()
    with open(f"rapport_cycle_{cycle}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Nom", "En retard", "Montant Cotisé"])
        for m in membres:
            cotisation = sum(c["montant"] for c in m["cotisations"] if c["cycle"] == cycle)
            retard = not any(c["cycle"] == cycle for c in m["cotisations"])
            writer.writerow([m["nom"], "Oui" if retard else "Non", cotisation])
    print(f"📄 Rapport généré pour le cycle {cycle}.")

def appliquer_penalite(membre_id, cycle):
    charger_membres()
    for m in membres:
        if m["id"] == membre_id:
            for c in m["cotisations"]:
                if c["cycle"] == cycle:
                    date_cot = datetime.strptime(c["date"], "%Y-%m-%d")
                    if datetime.today() - date_cot > timedelta(days=14):
                        penalite = 0.10 * c["montant"]
                        c["montant"] -= penalite
                        print(f"⚠️ Pénalité appliquée à {m['nom']}: -{penalite} FCFA")
            sauvegarder()

def afficher_evolution_fonds():
    charger_membres()
    cycles = set()
    fonds = {}
    for m in membres:
        for c in m["cotisations"]:
            cycle = c["cycle"]
            fonds[cycle] = fonds.get(cycle, 0) + c["montant"]
            cycles.add(cycle)
    cycles = sorted(cycles)
    valeurs = [fonds[c] for c in cycles]

    plt.plot(cycles, valeurs, marker="o")
    plt.title("Évolution de la cagnotte")
    plt.xlabel("Cycle")
    plt.ylabel("Montant total (FCFA)")
    plt.grid(True)
    plt.show()
