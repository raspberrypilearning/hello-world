## Dire bonjour

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il est traditionnel d'écrire un programme pour afficher "Bonjour le monde!" lorsque tu apprends un nouveau langage de programmation.
</div>
<div>

![La zone de sortie Trinket montrant les deux lignes imprimées de texte et d'emoji.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Ouvre le projet de démarrage [Bonjour 🌍🌎🌏](https://trinket.io/python/975f35023b){:target="_blank"}. Trinket s'ouvrira dans un autre onglet du navigateur.

![L'éditeur Trinket avec le code de démarrage du projet à gauche dans la zone de code. Sur la droite se trouve la zone de sortie vierge.](images/starter_project.png)

--- /task ---

La ligne `#!/bin/python3` précise à Trinket que nous utilisons Python 3 (la version la plus récente). Les lignes `import` indiquent à Python que tu vas utiliser du code que tu n'as pas écrit.

En Python, `print()` affiche du texte (mots ou nombres) à l'écran.

Les lignes commençant par `#` sont des commentaires, elles expliquent le code aux humains et sont ignorées par Python.

--- task ---

Trouve la ligne `# Mettre le code à exécuter ci-dessous `.

Clique sous cette ligne. Le `|` qui clignote est le curseur et indique où tu taperas.

Tape le code `print()` bonjour :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Mettre le code à exécuter ci-dessous
print('Bonjour')

--- /code ---

--- collapse ---
---
title: Saisie de caractères spéciaux sur un clavier français
---

Sur un clavier français, la parenthèse gauche `(` et droite `)` se trouvent sur les touches <kbd>5</kbd> et <kbd>°</kbd>. Le guillemet simple `'` se trouve sur la touche <kbd>4</kbd>. La virgule `,` est à côté du <kbd>N</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Test :** Clique sur le bouton **Run** pour exécuter ton code. Dans Trinket, la sortie apparaîtra à droite :

![L'icône Exécuter en surbrillance avec "Bonjour" affiché dans la zone de sortie. ](images/run_hello.png)

**Débogage :** Si tu obtiens une erreur, vérifie ton code très attentivement. Dans cet exemple, les guillemets simples autour de `Bonjour` manquent donc Python ne sait pas qu'il est censé être du texte.

![L'éditeur Trinket avec des guillemets simples manquants et l'erreur 'NameError: name 'Hello' is not defined on line 10 in main.py.](images/hello_error.png)

--- /task ---

En Python, une **variable** est utilisée pour stocker du texte ou des nombres. Les variables facilitent la lecture du code par les humains. Tu peux utiliser la même variable à de nombreux endroits dans ton code.

Nous avons inclus quelques variables qui stockent les caractères emoji.

--- task ---

Dans ton Trinket, clique sur l'onglet **emoji.py**. Trouve la variable `world`, qui stocke le texte '🌍🌍🌍'.

--- /task ---

--- task ---

Tu peux `print()` plusieurs éléments à la fois en incluant une virgule `,` entre les éléments. `print()` ajoutera un espace entre chaque élément.

Clique sur l'onglet **main.py** pour revenir à ton code `print()`.

Change ton code pour aussi `print()` le contenu de la variable `world` :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Mettre le code à exécuter ci-dessous
print('Bonjour', world)

--- /code ---

**Astuce :** `'Bonjour'` est une chaîne de texte car elle est entourée de guillemets simples, tandis que `world` est une variable de sorte que la valeur qui y est stockée sera imprimée.

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir le résultat :

![La ligne de code mise à jour dans la zone de code avec le mot "Bonjour" suivi de trois mondes emoji affichés dans la zone de sortie.](images/run_hello_world.png)

Les emoji peuvent avoir un aspect différent sur différents ordinateurs, de sorte que le tien peut ne pas être exactement le même.

**Débogage :** Assure-toi que tu as ajouté une virgule entre les éléments dans `print()` et que tu as correctement orthographié `world`.

Il manque la virgule `,` dans cet exemple. C'est petit mais très important !

![L'éditeur Trinket avec des guillemets simples manquants et l'erreur 'SyntaxError: bad input on line 12 in main.py' affiché.](images/comma_error.png)

--- collapse ---
---
titre : Je ne vois pas l'emoji
---

La plupart des ordinateurs te permettent d'utiliser des emoji de couleur. Cependant, si tu ne peux pas utiliser d'emoji, tu peux utiliser des "émoticônes" à la place, comme nous le faisions avant l'invention des emoji !

Remplace la ligne `from emoji import *` par :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 3
line_highlights: 3
---

from noemoji import *

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Ajoute une autre ligne à votre code pour `print()` plus de texte et d'emoji :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Bonjour', world)    
print('Bienvenue dans', python)

--- /code ---

**Astuce :** Le code que tu dois saisir est mis en surbrillance dans une couleur plus claire. Le code qui n'est pas en surbrillance t'aide à trouver où tu dois ajouter le nouveau code.

--- /task ---

--- task ---

**Test :** Clique sur **Run**.

![La ligne de code supplémentaire dans la zone de code avec le mot "Bonjour" suivi de trois mondes emoji et les mots "Bienvenue dans" suivis d'un serpent emoji et d'un clavier affichés dans la zone de sortie.](images/run_multiple.png)

**Astuce :** Il est conseillé d'exécuter ton code après chaque modification afin de pouvoir résoudre rapidement les problèmes.

**Débogage :** Vérifie attentivement les parenthèses, les guillemets, les virgules et l'orthographe correcte. Python a besoin que tu sois vraiment précis.

--- /task ---

Si tu as un compte Trinket, tu peux cliquer sur le bouton **Remix** pour enregistrer une copie dans ta bibliothèque `My Trinkets`.

Si tu n'as pas de compte Trinket, tu peux toujours revenir à ton projet à l'avenir sur le même ordinateur en utilisant le lien du projet de démarrage.

--- save ---
