## Sommes et dates

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python est excellent pour travailler avec des nombres et des dates.
</div>
<div>

![La zone de sortie avec cinq lignes imprimées montrant les nouvelles sorties de somme et de date actuelle.](images/sums_dates.png){:width="300px"} 

</div>
</div>

En Python, tu peux utiliser des opérateurs mathématiques pour faire des sommes :

| + | addition |   
| - | soustraction |   
| * | multiplication |   
| / | division |   
| ** | puissance |

### Créer un calcul

--- task ---

Ajoute deux autres lignes `print()` à ton code, incluant une somme à calculer par Python :

**Astuce :**pour obtenir un symbole `*`, appuie simultanément sur <kbd>Maj</kbd> et <kbd>8</kbd>.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---

print('Bonjour', monde)   
print('Bienvenue sur', python)   
print(python, 'est très bon en math !')   
print(230 * 5782 ** 2 / 23781)  # Imprime le résultat de la somme

--- /code ---

**Astuce :** tu n'as pas besoin de taper les commentaires, ils sont juste là pour t'aider à comprendre le code. Tape simplement la partie avant le `#`.

--- /task ---

--- task ---

**Test :** exécute ton code. Python a-t-il calculé la somme correctement ? Je plaisante ! Python fait les calculs difficiles pour toi, tu n'as donc pas besoin de les faire.

**Débogage :**

--- collapse ---
---
title: Jai une erreur de syntaxe
---

Assure-toi d'avoir ajouté une virgule `,` entre les éléments dans `print()` et d'avoir orthographié `python` correctement.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
L'informaticienne japonaise <span style="color: #0faeb0">**Emma Haruka Iwao**</span> a utilisé un ordinateur pour calculer la valeur de Pi (*π*) à 31 000 milliards de chiffres. Cette réponse est si longue qu'il faudrait plus de 300 000 ans rien que pour la dire ! 
</p>

--- task ---

Essaie de remplacer la somme que fait Python par une somme compliquée !

Tu peux également utiliser des parenthèses si tu souhaites contrôler l'ordre dans lequel Python calcule la somme : `print( (2 + 4) * (5 + 3) )`.

--- /task ---

--- task ---

**Test :** exécute ton code et demande à Python de calculer ta somme.

**Débogage :**assure-toi que ta somme est entourée d'une parenthèse gauche et droite `( 2 * 45 )`. Si tu utilises des parenthèses supplémentaires pour contrôler l'ordre, assure-toi d'avoir une parenthèse droite pour correspondre à chaque parenthèse gauche.

--- /task ---

--- task ---

Dans le Code Editor, tu pourrais trouver le texte trop gros ou trop petit pour être lu. Tu peux facilement modifier ces paramètres en fonction de tes préférences.

**Astuce :** clique sur le menu **Settings** à gauche de ton Code Editor. Clique ensuite sur l'un des boutons **Text Size** pour modifier la taille du texte.

![Le Code Editor avec le menu des paramètres développé pour montrer les options Color Mode et Text Size.](images/full_screen.png)

Tu peux également basculer entre les modes de couleur, clique sur les boutons **Light & Dark** pour voir les changements.

--- /task ---

La ligne `from datetime import *` en haut de l'onglet **main.py** inclut une bibliothèque avec des fonctions utiles pour obtenir la date et l'heure actuelles.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
L'un des avantages de Python est l'ensemble des <span style="color: #0faeb0">**bibliothèques**</span> de code disponibles. Une bibliothèque Python te permet d'utiliser facilement du code que d'autres personnes ont écrit. Il existe des bibliothèques pour dessiner des tableaux et des graphiques, faire de l'art, faire des calculs et bien plus encore.
</p>

--- task ---

Ajoute une autre ligne à ton code pour `print` la date et l'heure actuelles.

Obtiens la date et l'heure actuelles en utilisant la fonction `now()` de la bibliothèque `datetime` :

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 22
---

print(python, 'est très bon en math !')    
print(230 * 5782 ** 2 / 23781)  # Imrpime le résultat de la somme     
print('La date et l\'heure est', datetime.now())  # Imprime la date et l'heure actuelle

--- /code ---

**Astuce :** tu n'as pas besoin de taper les commentaires, ils sont juste là pour t'aider à comprendre le code. Tape simplement la partie avant le `#`.

--- /task ---

--- task ---

**Test :** exécute ton code plusieurs fois pour voir la mise à jour de la date et de l'heure.

**Debogage :** vérifie que tu as bien un point `.` entre `datetime` et `now`. Vérifie bien la ponctuation.

--- /task ---

--- save ---
