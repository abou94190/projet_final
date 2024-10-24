import tkinter as tk
from tkinter import messagebox
from compte_bancaire import CompteBancaire, transfert, verifier_pin
import os

# Charger les PIN des comptes existants depuis le fichier .env
from dotenv import load_dotenv
load_dotenv()

# Dictionnaire pour stocker tous les comptes
comptes = {}

# Fonction pour créer un compte
def creer_compte():
    def confirmer_creation():
        nom = entry_nom.get()
        solde_initial = float(entry_solde.get())
        taux_interet = float(entry_taux.get())
        code_pin = entry_pin.get()

        if nom.lower() in comptes:
            messagebox.showerror("Erreur", "Un compte avec ce nom existe déjà.")
        else:
            nouveau_compte = CompteBancaire(nom, solde_initial, taux_interet, code_pin)
            comptes[nom.lower()] = nouveau_compte
            messagebox.showinfo("Succès", f"Le compte {nom} a été créé avec succès !")
            fenetre_creation.destroy()

    # Fenêtre pour entrer les détails du compte
    fenetre_creation = tk.Toplevel()
    fenetre_creation.title("Créer un compte")

    tk.Label(fenetre_creation, text="Nom du compte :").pack()
    entry_nom = tk.Entry(fenetre_creation)
    entry_nom.pack()

    tk.Label(fenetre_creation, text="Solde initial :").pack()
    entry_solde = tk.Entry(fenetre_creation)
    entry_solde.pack()

    tk.Label(fenetre_creation, text="Taux d'intérêt (%) :").pack()
    entry_taux = tk.Entry(fenetre_creation)
    entry_taux.pack()

    tk.Label(fenetre_creation, text="Code PIN (4 chiffres) :").pack()
    entry_pin = tk.Entry(fenetre_creation, show="*")
    entry_pin.pack()

    tk.Button(fenetre_creation, text="Créer", command=confirmer_creation).pack()

# Fonction pour consulter le solde d'un compte
def consulter_solde():
    def verifier_solde():
        nom = entry_nom.get().lower()
        code_pin = entry_pin.get()
        compte = comptes.get(nom)
        if compte and verifier_pin(compte, code_pin):
            messagebox.showinfo("Solde", f"Le solde de {nom} est de {compte.consulter_solde()} €")
        else:
            messagebox.showerror("Erreur", "Compte introuvable ou PIN incorrect.")

    fenetre_solde = tk.Toplevel()
    fenetre_solde.title("Consulter le solde")

    tk.Label(fenetre_solde, text="Nom du compte :").pack()
    entry_nom = tk.Entry(fenetre_solde)
    entry_nom.pack()

    tk.Label(fenetre_solde, text="Code PIN :").pack()
    entry_pin = tk.Entry(fenetre_solde, show="*")
    entry_pin.pack()

    tk.Button(fenetre_solde, text="Vérifier", command=verifier_solde).pack()

# Fonction pour déposer de l'argent
def deposer_argent():
    def confirmer_depot():
        nom = entry_nom.get().lower()
        code_pin = entry_pin.get()
        montant = float(entry_montant.get())
        compte = comptes.get(nom)
        if compte and verifier_pin(compte, code_pin):
            compte.deposer(montant)
            messagebox.showinfo("Succès", f"Vous avez déposé {montant} € sur {nom}.")
            fenetre_depot.destroy()
        else:
            messagebox.showerror("Erreur", "Compte introuvable ou PIN incorrect.")

    fenetre_depot = tk.Toplevel()
    fenetre_depot.title("Déposer de l'argent")

    tk.Label(fenetre_depot, text="Nom du compte :").pack()
    entry_nom = tk.Entry(fenetre_depot)
    entry_nom.pack()

    tk.Label(fenetre_depot, text="Code PIN :").pack()
    entry_pin = tk.Entry(fenetre_depot, show="*")
    entry_pin.pack()

    tk.Label(fenetre_depot, text="Montant à déposer :").pack()
    entry_montant = tk.Entry(fenetre_depot)
    entry_montant.pack()

    tk.Button(fenetre_depot, text="Déposer", command=confirmer_depot).pack()

# Fonction pour retirer de l'argent
def retirer_argent():
    def confirmer_retrait():
        nom = entry_nom.get().lower()
        code_pin = entry_pin.get()
        montant = float(entry_montant.get())
        compte = comptes.get(nom)
        if compte and verifier_pin(compte, code_pin):
            if compte.retirer(montant):
                messagebox.showinfo("Succès", f"Vous avez retiré {montant} € de {nom}.")
                fenetre_retrait.destroy()
            else:
                messagebox.showerror("Erreur", "Solde insuffisant.")
        else:
            messagebox.showerror("Erreur", "Compte introuvable ou PIN incorrect.")

    fenetre_retrait = tk.Toplevel()
    fenetre_retrait.title("Retirer de l'argent")

    tk.Label(fenetre_retrait, text="Nom du compte :").pack()
    entry_nom = tk.Entry(fenetre_retrait)
    entry_nom.pack()

    tk.Label(fenetre_retrait, text="Code PIN :").pack()
    entry_pin = tk.Entry(fenetre_retrait, show="*")
    entry_pin.pack()

    tk.Label(fenetre_retrait, text="Montant à retirer :").pack()
    entry_montant = tk.Entry(fenetre_retrait)
    entry_montant.pack()

    tk.Button(fenetre_retrait, text="Retirer", command=confirmer_retrait).pack()

# Interface principale


fenetre = tk.Tk()
fenetre.title("Gestionnaire de Banque")

tk.Label(fenetre, text="Bienvenue dans le gestionnaire de banque").pack()

tk.Button(fenetre, text="Créer un compte", command=creer_compte).pack(pady=5)
tk.Button(fenetre, text="Consulter le solde", command=consulter_solde).pack(pady=5)
tk.Button(fenetre, text="Déposer de l'argent", command=deposer_argent).pack(pady=5)
tk.Button(fenetre, text="Retirer de l'argent", command=retirer_argent).pack(pady=5)

tk.Button(fenetre, text="Quitter", command=fenetre.quit).pack(pady=20)

fenetre.mainloop()
