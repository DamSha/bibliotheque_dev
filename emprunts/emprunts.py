# emprunts/emprunt.py
# class Emprunt de base

class Emprunt:
    def __init__(self, livre, membre, date_emprunt, duree_emprunt):
        self.livre = livre
        self.membre = membre
        self.date_emprunt = date_emprunt
        self.duree_emprunt = duree_emprunt

    def __repr__(self):
        return (f"--- EMPRUNT ---\n"
                f"{'Livre emprunté':>20} : {self.livre.titre} ({self.livre.isbn})\n"
                f"{'Membre emprunteur':>20} : {self.membre.nom} (id= {self.membre.identifiant})\n"
                f"{'Date emprunt':>20} : {self.date_emprunt}")
