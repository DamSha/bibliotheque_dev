# emprunts/emprunts_controller.py
# Gestion des emprunts
#

from .emprunts import Emprunt


class EmpruntsController:
    def __init__(self):
        self.emprunts = []

    def emprunter(self, livre, membre, date_emprunt, duree_emprunt=25) -> Emprunt:
        emprunt = Emprunt(livre, membre, date_emprunt, duree_emprunt)
        self.emprunts.append(emprunt)
        return emprunt

    def retourner(self, emprunt) -> Emprunt:
        self.emprunts.remove(emprunt)
        return emprunt

    def rechercher_emprunt_par_livre(self, livre) -> Emprunt:
        for emprunt in self.emprunts:
            if emprunt.livre == livre:
                return emprunt

    def rechercher_emprunt_par_membre(self, membre) -> Emprunt:
        for emprunt in self.emprunts:
            if emprunt.membre == membre:
                return emprunt

