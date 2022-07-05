[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Github Actions](https://github.com/DocstringFr/2022-Mentorat-yoyonel-Goban/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/DocstringFr/2022-Mentorat-yoyonel-Goban/actions/workflows/test.yml)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
# Comment lancer le projet

Pour commencer et lancer les tests :

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pytest .
```

# Exercice

Le thème de cet exercice est le jeu de go.

Le but est d'écrire une fonction qui détermine si la pierre à une position x, y sur un goban est prise ou pas.

Vocabulaire :

* Goban : le plateau sur lequel on place des pierres pour jouer
* Forme : un groupe d'une ou plusieurs pierres adjacente de la même couleur (adjacente : des pierres qui sont à gauche, droite, dessus, dessous l'une de l'autre, les diagonales ne comptent pas)
* Liberté : espace vide adjacent à une forme

Rappel des règles :

1. Le goban a une taille indéfinie
2. Il y a deux joueurs et chacun joue une couleur de pierre : noir ou blanc
3. Les pierres sont posées les unes après les autres chacun son tour
5. Lorsqu'une forme n'a plus de liberté elle est prise

L'objectif de l'exercice est d'écrire une fonction `is_taken` qui prend en paramètre x, y et qui retourne vrai si la pierre à la position x, y est prise et faux sinon.
Pour faire cette fonction, on se base sur une fonction `get_status(x, y)` qui retourne :

* Status.BLACK : quand la pierre à la position x, y est noire
* Status.WHITE : quand la pierre à la position x, y est blanche
* Status.EMPTY : quand il n'y a pas de pierre à la position x, y
* Status.OUT : quand la position x, y est hors du goban


Complétez la méthode `Goban.is_taken` avec votre solution (vous pouvez ajouter des paramètres à la méthode si besoin).
Celle-ci doit respecter les bonnes pratiques du Python.
Vous pouvez tester votre solution à tout moment avec `py.test` (les tests sont dans le fichier test_goban.py).

Exemples :

```
# = noir
o = blanc
. = vide


.#.
#o#    <= o est prise parce qu'elle n'a pas de liberté, elle n'a aucun espace vide adjacent
.#.


...
#o#    <= o n'est pas prise parce qu'elle a une liberté au dessus
.#.


o#    <= o est prise parce qu'elle n'a pas de liberté (le haut et la gauche sont hors du goban donc ce ne sont pas des libertés)
#.


oo.
##o    <= la forme # est prise parce qu'elle n'a pas de liberté
o#o
.o.


oo.
##.   <= la forme # n'est pas prise parce qu'elle a une liberté en x=2, y=1 (0, 0 en haut à gauche)
o#o
.o.
```

---
