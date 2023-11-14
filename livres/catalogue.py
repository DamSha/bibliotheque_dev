# livres/catalog.py
# pour la gestion du catalogue
#
#  Ajout
#  Suppression
#  Recherche

from .livre import Livre


class Catalogue:
    def __init__(self):
        self.liste_livres = []

    def ajouter_livre(self, livre: Livre):
        # Si ISBN existe pas dans la liste
        if self.rechercher_livre_par_isbn(livre.isbn) is None:
            self.liste_livres.append(livre)
            return livre

    def supprimer_livre(self, livre: Livre) -> Livre | None:
        self.liste_livres.remove(livre)
        return livre

    def rechercher_livre_par_isbn(self, isbn) -> Livre | None:
        for livre in self.liste_livres:
            if str(livre.isbn) == str(isbn):
                return livre
