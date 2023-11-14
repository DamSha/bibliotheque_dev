# membres/membre_controller.py
# class Membre pour la gestion des Membres
# Ajout
# Suppression
# Recherche
#
from .membres import Membre


class MembresController:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre: Membre) -> Membre:
        self.membres.append(membre)
        return membre

    def supprimer_membre(self, membre: Membre) -> Membre:
        self.membres.remove(membre)
        return membre

    def rechercher_membre_par_nom(self, nom) -> Membre:
        for membre in self.membres:
            if membre.nom == nom:
                return membre

    def rechercher_membre_par_id(self, id) -> Membre:
        for membre in self.membres:
            if str(membre.identifiant) == str(id):
                return membre
    def supprimer_membre_par_id(self, id) -> Membre | None:
        membre = self.rechercher_membre_par_id(id)
        if membre is None:
            return None
        self.supprimer_membre(membre)
        return membre

