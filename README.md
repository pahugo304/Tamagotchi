# Tamagotchi virtuel (Projet Python)

## Présentation

Petit jeu en console qui simule un Tamagotchi :
- Gestion de plusieurs jauges : Faim, Énergie, Humeur, Propreté
- Actions du joueur à chaque tour
- ASCII art pour afficher l'état de la créature
- Sauvegarde et chargement de la partie en JSON

## Règles du jeu

- Faim : `0 = rassasié`, `100 = affamé` → **Game Over**
- Énergie : `0 = épuisé` → **Game Over**
- Humeur : `0 = dépression` → **Game Over**
- Propreté : `0 = trop sale` → **Game Over**

À chaque tour :
- Les jauges évoluent automatiquement.
- Le joueur choisit une action :
  - **Nourrir** : réduit la faim.
  - **Dormir** : augmente l'énergie.
  - **Jouer** : augmente l'humeur mais consomme de l'énergie et augmente la faim.
  - **Laver** : améliore la propreté.

Vous pouvez sauvegarder la partie et la recharger plus tard.

## Lancer le programme

```bash
python game.py
