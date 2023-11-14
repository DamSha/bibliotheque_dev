# livres/livre.py
# pour la gestion des livres

class Livre:
    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur

    def __repr__(self):
        # return WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
        return (f"\n--- LIVRE ---\n"
                f" {'Titre':>7} : {self.titre}\n"
                f" {'Auteur':>7} : {self.auteur}\n"
                f" {'ISBN':>7} : {self.isbn}")

