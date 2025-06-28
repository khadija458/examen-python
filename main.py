from membres import *
from cycles import *
from finances import *

def menu_principal():
    global cycle_actuel
    while True:
        print("\n=== Gestion de Tontine ===")
        print("1. Ajouter un membre")
        print("2. Enregistrer une cotisation")
        print("3. Effectuer le tirage du mois")
        print("4. Générer un rapport financier")
        print("5. Afficher l'évolution des fonds")
        print("6. Afficher l'historique des tirages")
        print("7. Vérifier les retards")
        print("8. Appliquer une pénalité")
        print("9. Quitter")
        choix = input("Choix > ")

        if choix == "1":
            nom = input("Nom du membre : ")
            tel = input("Téléphone : ")
            ajouter_membre(nom, tel)

        elif choix == "2":
            membre_id = int(input("ID du membre : "))
            montant = int(input("Montant cotisé : "))
            date = input("Date (AAAA-MM-JJ) : ")
            cycle = int(input("Cycle : "))
            enregistrer_cotisation(membre_id, montant, date, cycle)

        elif choix == "3":
            effectuer_tirage()
            cycle_actuel += 1  # Passer au cycle suivant

        elif choix == "4":
            cycle = int(input("Cycle du rapport : "))
            generer_rapport_mensuel(cycle)

        elif choix == "5":
            afficher_evolution_fonds()

        elif choix == "6":
            afficher_historique()

        elif choix == "7":
            membre_id = int(input("ID du membre à vérifier : "))
            cycle = int(input("Cycle en cours : "))
            verifier_retards(membre_id, cycle)

        elif choix == "8":
            membre_id = int(input("ID du membre : "))
            cycle = int(input("Cycle concerné : "))
            appliquer_penalite(membre_id, cycle)

        elif choix == "9":
            print("💾 Sauvegarde effectuée. À bientôt.")
            break

        else:
            print("⛔ Choix invalide. Réessaye.")

if __name__ == "__main__":
    menu_principal()
