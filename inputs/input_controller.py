# inputs/inputs_controller.py
# pour la gestion des inputs
# import termcolor
from .text_format import FORMATS, COLORS, ARC_EN_CIEL_COLORS, formatText


class InputsController:
    def __init__(self):
        for color in ARC_EN_CIEL_COLORS:
            print(formatText("Bienvenue dans la Bibliothèque personnelle de Damien.", color=color, format=FORMATS.BOLD))
        print(formatText("\nAppuyez sur une touche pour commencer", color=COLORS.OKCYAN))
        input("")

    # def ask_livre_titre(self):
    #     titre_livre = input(formatText("Qeul est le titre du livre ?", color=COLORS.QUESTION))
    #     return titre_livre

    def afficher_menu_principal(self):
        commande = ""
        while True:
            print("\n".join([
                "---------------------------------",
                "           MENU PRINCIPAL",
                "---------------------------------",
                "[1] Gestion des Livres",
                "[2] Gestion des Membres",
                "[3] Gestion des Emprunts",
                "[Q] Quitter",
                formatText("Choisissez une commande à effectuer en tapant son numéro équivalent :",
                           color=COLORS.QUESTION),
            ]))

            commande = input("Votre commande : ").strip().lower()
            # On quitte
            if commande.lower() == "q":
                return 0
            # Sinon N° Commande
            try:
                commande = int(commande)
                break
            except ValueError:
                self.commande_non_valide()
                continue
            finally:
                if commande not in [1, 2, 3]:
                    # if commande not in [0, 99, 11, 12, 13, 21, 22, 23, 31, 32, 33]:
                    return self.commande_non_valide()
                    continue
                # todo: len(commands)
                if commande not in range(4):
                    return 99  # retour a menu principal
                # sous-menu
                sub_comment = self.sub_command(commande)
                if sub_comment == 0:
                    return 99  # retour a menu principal
                else:
                    return int(str(commande) + str(sub_comment))  # => 13 pour commande 1 et sous commande 3

    def sub_command(self, commande):
        sub_commande = ""
        menu = ""
        if commande == 1:
            menu = "\n".join([
                "---------------------------------",
                "        Gestion des Livres",
                "---------------------------------",
                "[1] Liste des livres disponibles",
                "[2] Ajouter un livre",
                "[3] Supprimer un livre"])
        elif commande == 2:
            menu = "\n".join([
                "---------------------------------",
                "        Gestion des Membres",
                "---------------------------------",
                "[1] Liste des membres actifs",
                "[2] Ajouter un membre",
                "[3] Supprimer un membre"])
        elif commande == 3:
            menu = "\n".join([
                "---------------------------------",
                "        Gestion des Emprunts",
                "---------------------------------",
                "[1] Liste des emprunts",
                "[2] Faire un emprunt",
                "[3] Rendre un livre"])
        while True:
            print("\n".join([
                menu,
                "[0] Retour au menu principal",
                formatText("Choisissez une commande à effectuer en tapant son numéro équivalent :",
                           color=COLORS.QUESTION),
            ]))
            try:
                sub_commande = int(input("Votre commande : ").strip().lower())
                break
            except Exception:
                self.commande_non_valide()
                continue

        return sub_commande

    def save_inputs(self, inputs, action="Sauvegarder") -> bool:
        commande = ""
        while True:
            print("\n".join([
                "---------------------------------",
                f"{action}",
                f"{inputs}",
                "---------------------------------",
                formatText("Confirmer ?",
                           color=COLORS.WARNING),
                "[1] OUI",
                "[0] NON",
            ]))
            try:
                commande = int(input("Votre commande : ").strip().lower())
            except:
                self.commande_non_valide()
                continue
            if commande not in [0, 1]:
                continue
            else:
                if commande == 0:
                    print("Commande Annulée")
                else:
                    print("Commande Sauvegardée")
                return True if commande is True else False

    def quitter(self):
        commande = None
        while True:
            try:
                print(formatText("Etes vous sur de vouloir quitter le programme ?\n", color=COLORS.WARNING),
                      "[0] NON\n"
                      "[1] OUI"
                      )
                print(formatText("Commande : ", color=COLORS.OKCYAN))
                commande = int(input("").strip().lower())
                break
            except Exception:
                self.commande_non_valide()
                continue
        commande = True if commande == 1 else False
        return commande

    def commande_non_valide(self):
        print(formatText(f"###########\n Erreur : Commande non valide. Réessayez.\n###########", color=COLORS.FAIL))

    def ajouter_membre(self):
        membre_id, nom, adresse = ("", "", "")

        membre_id = self.ask_membre_id()
        nom = self.ask_membre_nom()
        while adresse == "":
            print(formatText("Quel est l'adresse du membre (1 seule ligne) ?", color=COLORS.QUESTION)),
            adresse = input("adresse = ")
            if adresse == "":
                print("Entrez un nom valide")

        return membre_id, nom, adresse

    def ask_membre_nom(self):
        nom = ""
        while nom == "":
            print(formatText("Quel est le nom du membre ?", color=COLORS.QUESTION)),
            nom = input("nom = ")
            if nom == "":
                print("Entrez un nom valide")
        return nom

    def ask_membre_id(self):
        membre_id = ""
        while membre_id == "":
            print(formatText("Quel est l'identifiant du membre ?", color=COLORS.QUESTION)),
            membre_id = input("")
            if membre_id == "":
                print("Entrez un identifiant valide")
                continue
            else:
                return membre_id

    def ask_livre_isbn(self):
        isbn = ""
        while type(isbn) is not int:
            print(formatText("Quel est l'ISBN du livre ?", color=COLORS.QUESTION)),
            try:
                isbn = int(input("ISBN = ").strip())
            except Exception:
                print("Erreur : Entrez un ISBN valide.")
            if type(isbn) is not int:
                print("Entrez un ISBN valide")
        return isbn

    def ajouter_livre(self):
        _titre, _auteur, _isbn = ("", "", "")

        _titre = self.ask_livre_titre()
        _auteur = self.ask_livre_auteur()
        _isbn = self.ask_livre_isbn()
        return _titre, _auteur, _isbn

    def ask_livre_auteur(self):
        auteur = ""
        while auteur == "":
            print(formatText("Quel est l'auteur du livre ?", color=COLORS.QUESTION)),
            auteur = input("auteur = ").strip()
            if auteur == "":
                print("Entrez un auteur valide")
                continue
        return auteur

    def ask_livre_titre(self):
        titre = ""
        while titre == "":
            print(formatText("Quel est le titre du livre ?", color=COLORS.QUESTION)),
            titre = input("titre = ").strip()
            if titre == "":
                print("Entrez un titre valide")
                continue
        return titre
