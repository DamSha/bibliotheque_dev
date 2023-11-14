"""
bibliotheque /
    | -- __init__.py
    | -- main.py
    | -- livres /
    | | -- __init__.py
    | | -- livre.py
    | | -- catalogue.py
    | -- membres /
    | | -- __init__.py
    | | -- membre.py
    | | -- membres_controller.py
    | -- emprunts /
    | | -- __init__.py
    | | -- emprunt.py
    | | -- emprunts_controller.py
"""
import time
from livres.livre import Livre
from livres.catalogue import Catalogue
from membres.membres import Membre
from membres.membres_controller import MembresController
from emprunts.emprunts_controller import EmpruntsController
from inputs.input_controller import InputsController


class Bibliotheque:
    def __init__(self):
        # Initialisation des instances
        self.catalogue = Catalogue()
        self.gestion_membres = MembresController()
        self.gestion_emprunt = EmpruntsController()
        self.inputController = InputsController()

    def add_fixtures(self):
        """
        Ajoute des données fictives
        :return:
        """
        # FAKE LIVRES
        livre1 = Livre(isbn=123456, titre="1Q84", auteur="Haruki Murakami")
        livre2 = Livre(isbn=4506789, titre="La fin des temps", auteur="Haruki Murakami")
        livre3 = Livre(isbn=45678900, titre="Les Aventures d'Alice au pays des merveilles",
                       auteur="Lewis Carroll")
        livre4 = Livre(isbn=456120003, titre="De l'autre côté du miroir", auteur="Lewis Carroll")

        # AJOUT AU CATALOGUE
        self.catalogue.ajouter_livre(livre1)
        self.catalogue.ajouter_livre(livre2)
        self.catalogue.ajouter_livre(livre3)
        self.catalogue.ajouter_livre(livre4)

        # FAKE MEMBRES
        membre1 = Membre(identifiant=123, nom="Damien C", adresse="97190 - le Gosier - Guadeloupe")
        membre2 = Membre(identifiant=456, nom="Louison C", adresse="75001 - Paris 1")
        self.gestion_membres.ajouter_membre(membre=membre1)
        self.gestion_membres.ajouter_membre(membre=membre2)

        # FAKE EMPRUNTS
        self.gestion_emprunt.emprunter(livre=livre1, membre=membre1, date_emprunt="01/11/2023", duree_emprunt="15")
        self.gestion_emprunt.emprunter(livre=livre2, membre=membre1, date_emprunt="01/11/2023", duree_emprunt="15")
        self.gestion_emprunt.emprunter(livre=livre3, membre=membre2, date_emprunt="01/11/2023", duree_emprunt="15")

    def run(self, with_fixtures: bool = False):
        """
        Lance la gestion de la bibliotheque
        :param with_fixtures: Vrai si on ajoute des données de test
        """
        if with_fixtures:
            self.add_fixtures()

        # Boucle principale
        while True:
            commande = self.inputController.afficher_menu_principal()

            if commande not in [0, 99, 11, 12, 13, 21, 22, 23, 31, 32, 33]:
                self.inputController.commande_non_valide()
                continue

            # RETOUR AU MENU PRINCIPAL
            if commande == 99:
                continue

            # QUITTER
            elif commande == 0:
                sur_de_sur = self.inputController.quitter()
                if sur_de_sur:
                    print("BYE BYE !")
                    exit()
                else:
                    continue

            # LISTE LIVRES DISPO
            elif commande == 11:
                print(self.voir_livres())
            # Ajouter un Livre
            elif commande == 12:
                self.ajouter_livre()
            # LISTE MEMBRES
            # Supprimer un livre
            elif commande == 13:
                self.supprime_livre()
            elif commande == 21:
                print(self.voir_membres_actifs())
            # Ajouter membre
            elif commande == 22:
                self.ajouter_membre()
            # LISTE EMPRUNTS
            # Supprimer un membre
            elif commande == 23:
                self.supprimer_membre()
            elif commande == 31:
                print(self.voir_emprunts())
            # Faire un emprunt
            elif commande == 32:
                self.faire_un_emprunt()
            # Rendre un livre
            elif commande == 33:
                self.rendre_un_livre()

    def voir_livres(self):
        print("\n".join([
            "---------------------------------",
            "  LISTE DES LIVRES DISPONIBLES",
            "---------------------------------"]))
        for livre in self.catalogue.liste_livres:
            print(livre)

    def voir_membres_actifs(self):
        print("\n".join([
            "---------------------------------",
            "          MEMBRES ACTIFS",
            "---------------------------------"]))
        for member in self.gestion_membres.membres:
            print(member)

    def voir_emprunts(self):

        print("\n".join([
            "---------------------------------",
            "        EMPRUNTS EN COURS",
            "---------------------------------"]))
        for emprunt in self.gestion_emprunt.emprunts:
            print(emprunt)

    def ajouter_membre(self):
        membre_id, nom, adresse = self.inputController.ajouter_membre()
        membre = Membre(identifiant=membre_id, nom=nom, adresse=adresse)
        # confirmation de sauvegarde
        if self.inputController.save_inputs(inputs=membre):
            self.gestion_membres.ajouter_membre(membre)
            print("\n".join([
                "---------------------------------",
                "          NOUVEAU MEMBRE",
                "---------------------------------"]))
            print(membre)

    def supprimer_membre(self):
        membre_a_supprime = ""
        while membre_a_supprime == "":
            id_membre_a_supp = self.inputController.ask_membre_id()

            # Si le membre existe
            membre_a_supprime = self.gestion_membres.rechercher_membre_par_id(id_membre_a_supp)
            if membre_a_supprime is None:
                print("Numéro de membre invalide")
                continue

            # Si le membre n'a pas un emprunt
            else:
                emprunt_membre_a_supprime = self.gestion_emprunt.rechercher_emprunt_par_membre(membre_a_supprime)
                if emprunt_membre_a_supprime is not None:
                    print(f"Suppression impossible : Le membre {membre_a_supprime.nom} a un livre emprunté\n"
                          f"Livre : {emprunt_membre_a_supprime.livre.titre}")
                    continue

            # Alors on le supprime (en demandant)
            if self.inputController.save_inputs(action="Supprimer", inputs=membre_a_supprime):
                self.gestion_membres.supprimer_membre_par_id(id_membre_a_supp)
                print("\n".join([
                    "---------------------------------",
                    f" MEMBRE n°{id_membre_a_supp} SUPPRIME",
                    "---------------------------------"]))
                break

    def faire_un_emprunt(self):
        membre = None
        livre = None

        # Si le Memnre existe
        while membre is None:
            membre_id = self.inputController.ask_membre_id()
            membre = self.gestion_membres.rechercher_membre_par_id(membre_id)
            if membre is None:
                print("Erreur : pas de membte trouvé")
                # print("voulez-vous le créer ?")
                # todo: demande création Membre
                continue

        # Si le Livre existe
        while livre is None:
            livre_isbn = self.inputController.ask_livre_isbn()
            livre = self.catalogue.rechercher_livre_par_isbn(livre_isbn)
            if livre is None:
                print("Erreur : pas de livre trouvé")
                # print("voulez-vous le créer ?")
                # todo: demande création Livre
                continue

            # Si le livre n'est pas deja emprunté
            emprunt = self.gestion_emprunt.rechercher_emprunt_par_livre(livre)
            if emprunt is not None:
                print(f"Erreur : livre déjà emprunté par le membre n°{emprunt.membre.identifiant}")
                # print("voulez-vous ramener le livre ?")
                # todo: demande suppression emprunt
                continue
            else:
                # Alors Ajout de l'emprunt (en demandant confirmation)
                if self.inputController.save_inputs(action=f"Ajouter Emprunt à {membre}", inputs=livre):
                    time_now = time.time()
                    self.gestion_emprunt.emprunter(membre=membre, livre=livre, date_emprunt=time_now)

    def rendre_un_livre(self):
        livre = None

        # Si le Livre existe
        while livre is None:
            livre_isbn = self.inputController.ask_livre_isbn()
            livre = self.catalogue.rechercher_livre_par_isbn(livre_isbn)
            if livre is None:
                print("Erreur : pas de livre trouvé")
                # print("voulez-vous le créer ?")
                # todo: demande création Livre
                continue

            # Si le livre est bien emprunté par
            emprunt = self.gestion_emprunt.rechercher_emprunt_par_livre(livre)
            if emprunt is None:
                print(f"Erreur : livre non emprunté")
                continue
            else:
                # Alors Supprime de l'emprunt (en demandant confirmation)
                if self.inputController.save_inputs(action=f"Retour", inputs=emprunt):
                    self.gestion_emprunt.retourner(emprunt=emprunt)
                    print("\n".join([
                        "---------------------------------",
                        "          LIVRE RENDU",
                        "---------------------------------"]))
                    print("Livre : ", emprunt.livre.titre)
                    print("Membre : ", emprunt.membre.nom)

    def supprime_livre(self):
        livre_isbn_a_supp = None

        # Si le livre existe
        while livre_isbn_a_supp is None:
            livre_isbn_a_supp = self.inputController.ask_livre_isbn()
            livre_a_supp = self.catalogue.rechercher_livre_par_isbn(livre_isbn_a_supp)
            if livre_a_supp is None:
                print("Pas de livre trouvé")
                livre_isbn_a_supp = None
                continue

            # Si pas dans les emprunts
            livre_emprunte = self.gestion_emprunt.rechercher_emprunt_par_livre(livre_a_supp)
            if livre_emprunte is None:
                print("Livre déjà emprunté")
                # todo: Demande le retour ?

            else:
                # Alors Supprime de l'emprunt (en demandant confirmation)
                if self.inputController.save_inputs(action="Supprimer", inputs=livre_a_supp):
                    self.catalogue.supprimer_livre(livre_a_supp)
                    print("\n".join([
                        "---------------------------------",
                        "          LIVRE SUPPRIME",
                        "---------------------------------"]))
                    print(livre_a_supp)

    def ajouter_livre(self):
        titre, auteur, isbn = self.inputController.ajouter_livre()
        if titre == "":
            return
        # On ajoute le livre (en demandant confirmation)
        livre = Livre(titre=titre, auteur=auteur, isbn=isbn)
        if self.inputController.save_inputs(action=f"Ajout", inputs=livre):
            self.catalogue.ajouter_livre(livre)
            print("\n".join([
                "---------------------------------",
                "          NOUVEAU LIVRE",
                "---------------------------------"]))
            print(livre)


if __name__ == "__main__":
    # initialisation de la Bibliotheque
    biblio = Bibliotheque()
    # Lancement de la console
    biblio.run(with_fixtures=True)
