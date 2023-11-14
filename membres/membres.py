# membres/membre.py
# class Membre pour la gestion des Membres

class Membre:
    def __init__(self, identifiant, nom, adresse):
        self.identifiant = identifiant
        self.nom = nom
        self.adresse = adresse

    def __repr__(self):
        return (f"--- MEMBRE ---\n"
                f"{'N° membre':>10} : {self.identifiant}\n"
                f"{'Nom':>10} : {self.nom}")

    def voir_identifiant(self):
        return self.identifiant

    def voir_adresse(self):
        return self.adresse

    def voir_nom(self):
        return self.nom
