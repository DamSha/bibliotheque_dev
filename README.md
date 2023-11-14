# Bienvenue sur le projet de Bibliothèque en Python
version 1.0  
Auteur: Damien Chauvet  
Contexte: Cours Dév. IA 2023 / Unlock Formation  

## Architecture  
La bibliothèque contient 4 Modules principaux :
- **Livres** : pour la définition et la gestion des Livres
- **Membres** : pour la définition et la gestion des Membres
- **Emprunts** : pour la définition et la gestion des Emprunts
- **Inputs** : pour la définition et la gestion des Entrées utilisateur

## Classes principales
### main.py
Initialise et lance la bibliothèque avec le paramètre ```with_fixtures: bool``` qui permet de générer de fausses données pour les tests / démos.
En tant que classe principale, elle est en charge de lancer les menus, de récupérer les inputs et de les lier à ses propres fonctions.
### livres/livres.py
**Attributs**: isbn, titre, auteur
### livres/catalogue.py
**Fonctions** :
- ajouter_livre()
- supprimer_livre()
- rechercher_livre_par_isbn()
### emprunts/emprunt.py
**Attributs**: livre, membre, date_emprunt, duree_emprunt
### emprunts/emprunts_controller.py
**Fonctions** :
- emprunter()
- retourner()
- rechercher_emprunt_par_livre()
- rechercher_emprunt_par_membre()
### membres/membre.py
**Attributs**: identifiant, nom, adresse
### membres/membres_controller.py
**Fonctions** :
- ajouter_membre()
- supprimer_membre()
- rechercher_membre_par_id()
- supprimer_membre_par_id()
### inputs/input_controller.py
**Fonctions** utiles :
- afficher_menu_principal()
- sub_command()
- save_inputs()
### inputs/text_format.py
**Fonctions** :
- formatText()

## Menus
La bibliothèque est accessible via le terminal (en version 0.1).  
Son accès se fait via un Menu Principal qui découpe les fonctionnalités en groupes et évite ainsi d'avoir un seul menu trop chargé :
```
    ---------------------------------
               MENU PRINCIPAL
    ---------------------------------
    [1] Gestion des Livres
    [2] Gestion des Membres
    [3] Gestion des Emprunts
    [Q] Quitter 
```
Sous-menus de chaque catégories :
```
---------------------------------
        Gestion des Livres
---------------------------------
[1] Liste des livres disponibles
[2] Ajouter un livre
[3] Supprimer un livre
[0] Retour au menu principal
```
```
---------------------------------
        Gestion des Membres
---------------------------------
[1] Liste des membres actifs
[2] Ajouter un membre
[3] Supprimer un membre
[0] Retour au menu principal
```
```
---------------------------------
        Gestion des Emprunts
---------------------------------
[1] Liste des emprunts
[2] Faire un emprunt
[3] Rendre un livre
[0] Retour au menu principal
```

## Workflow
- Le programme principal affiche les menu/sous-menu et vérifie les entrées utilisateurs.
- Les menus et sous-menus sont dans la même boucle pour pouvoir passer d'un menu à l'autre facilement.
- Le résultat des 2 menus est renvoyé au programme principal pour connaitre la commande à exécuter:  
Par exemple : ````[1] Gestion des Livres + [2] Ajouter un livre => renvoie 12````
- La commande est vérifiée, puis une confirmation est demandée pour finaliser la commande.
```
Confirmer ?
[1] OUI
[0] NON
```


## Affichage des instances 
Afin de réduire le code et d'utiliser les méthodes Python,
les objets souvent imprimés dans la console ont une fonction ```__repr__```
qui permet d'altérer la façon dont l'objet est rendu à l'affichage avec ```print(obj)```

## Gestion du terminal
- Pour être modulaire et prévoir d'autres interfaces (Web, tKinker, IA(?)) 
j'ai rajouté la classe ```InputController```, qui pourra être remplacer plus facilement.  
- Pour agayer l'interface triste du terminal, j'ai rajouté ```textFormat``` qui permet de renvoyer un texte dans un format amélioré.

## Amélioration
- Class **Commandes** :
  - Ajouter un classe en charge de la création de Commandes / SubCommandes,
et ainsi créer les menus automatiquement.
- Class **Menus** :
  - Ajouter une classe pour la gestion des menus.