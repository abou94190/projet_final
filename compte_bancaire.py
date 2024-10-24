import os
from dotenv import load_dotenv
from datetime import datetime

# Charger les variables d'environnement pour les PIN
load_dotenv()


class CompteBancaire:
    def __init__(self, nom, solde_initial, taux_interet, code_pin):
        self.nom = nom
        self.solde = solde_initial
        self.taux_interet = taux_interet
        self.code_pin = code_pin
        self.historique = []
        self.derniere_application_interets = datetime.now()

    # Consulter le solde
    def consulter_solde(self):
        print(f"Le solde actuel de {self.nom} est de {self.solde} €.")

    # Déposer de l'argent
    def deposer(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt de {montant} €")
        print(f"{montant} € ont été déposés sur le compte de {self.nom}.")

    # Retirer de l'argent
    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            self.historique.append(f"Retrait de {montant} €")
            print(f"{montant} € ont été retirés du compte de {self.nom}.")
        else:
            print("Solde insuffisant pour effectuer ce retrait.")

    # Afficher l'historique des transactions
    def afficher_historique(self):
        print(f"Historique des transactions du compte de {self.nom} :")
        if not self.historique:
            print("Aucune transaction enregistrée.")
        else:
            for transaction in self.historique:
                print(transaction)

    # Appliquer des intérêts mensuels
    def appliquer_interets(self):
        maintenant = datetime.now()
        if (maintenant - self.derniere_application_interets).days >= 30:
            interet = self.solde * self.taux_interet / 100
            self.solde += interet
            self.historique.append(f"Intérêts appliqués de {interet} €")
            self.derniere_application_interets = maintenant
            print(f"Des intérêts de {interet} € ont été appliqués au compte de {self.nom}.")
        else:
            print("Les intérêts ne peuvent être appliqués qu'une fois par mois.")

# Transfert d'argent entre comptes


def transfert(compte_source, compte_cible, montant):
    if compte_source.solde >= montant:
        compte_source.solde -= montant
        compte_cible.solde += montant
        compte_source.historique.append(f"Transfert de {montant} € vers {compte_cible.nom}")
        compte_cible.historique.append(f"Réception de {montant} € de {compte_source.nom}")
        print(f"Transfert de {montant} € effectué de {compte_source.nom} à {compte_cible.nom}.")
    else:
        print("Solde insuffisant pour effectuer ce transfert.")

# Vérification du code PIN


def verifier_pin(compte, code_pin_saisi):
    if compte.code_pin == code_pin_saisi:
        return True
    else:
        print("Code PIN incorrect.")
        return False
