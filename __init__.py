"""
    Version 1.0
    Architecture + business logic


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
        | | -- gestion_membres.py
        | -- emprunts /
        | | -- __init__.py
        | | -- emprunt.py
        | | -- gestion_emprunts.py
        | -- inputs /
        | | -- __init__.py
        | | -- input_controller.py
        | | -- text_format.py
"""

"""
    Version 1.1 : Ajout d'un Menu Interactif
    
    Objectif : Enrichir l'expérience utilisateur de votre gestionnaire de bibliothèque en ajoutant un menu interactif.
    
    Instructions :
    
    1. Afficher le Menu Principal :
        o Créez une fonction afficher_menu_principal() qui affiche les différentes options du menu.
        o Utilisez un système de numérotation pour chaque option afin de faciliter la sélection par l'utilisateur.
    
    2. Gestion des Options :
        o Modifiez la boucle principale du programme pour afficher le menu à chaque itération.
        o Utilisez une instruction input() pour permettre à l'utilisateur de saisir son choix.
    
    3. Ajout d'Options :
        o Pour chaque option du menu, créez une fonction dédiée qui implémente le comportement associé à cette option.
        o Par exemple, pour l'option "Ajouter un livre au catalogue", créez une fonction ajouter_livre_au_catalogue().
        
    4. Intégration avec le Programme Principal :
        o Appelez les fonctions appropriées en fonction du choix de l'utilisateur dans la boucle principale.
        o Assurez-vous que chaque fonction est correctement définie et teste son bon fonctionnement.
        
    5. Sortie du Programme :
        o Ajoutez une option "Quitter" qui permet à l'utilisateur de sortir proprement du programme.
        o Modifiez la boucle principale pour permettre la sortie lorsque l'utilisateur choisit cette option.
"""