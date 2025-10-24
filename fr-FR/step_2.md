## Imprimer (print) Bonjour

En Python, `print()`{:.language-python} affiche des chaînes (mots ou nombres) à l'écran.

--- task ---

Ouvre le projet de démarrage [Bonjour 🌍🌎🌏](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. Le Code Editor s'ouvrira dans un autre onglet du navigateur.

--- /task ---

--- task ---

Find the `# Put code to run under here`{:.language-python} line.

Clique sous cette ligne. Le `|` qui clignote est le curseur et indique où tu taperas.

--- /task ---

--- task ---

Tape le code `print()`{:.language-python} Bonjour à l'écran :

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 21
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** pour exécuter ton code.

You should see `Hello` in the Text output area.

--- /task ---

Une **variable** est utilisée pour stocker des valeurs telles que du texte ou des nombres. Nous avons inclus quelques variables qui stockent les caractères emoji.

--- task ---

Modifie ton code pour également `print()`{:.language-python} le contenu de la variable `world`{:.language-python} . Tu peux le faire en ajoutant le nom de la variable entre accolades `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 20
---
# Mettre le code à exécuter ci-dessous
print(f'Hello {world}')

--- /code ---

Le caractère `f`{:.language-python} à l'intérieur de print te permet d'imprimer facilement des variables avec des chaînes de texte.

--- /task ---

--- task ---

**Test :** exécute ton code pour voir le résultat :

![La ligne de code mise à jour dans la zone de code avec le mot "Bonjour" suivi de trois emojis monde dans la zone de sortie.](images/run_hello_world.png)

--- /task ---

--- task ---

**Ajoute** une autre ligne à ton code pour `print()`{:.language-python} plus de texte et d'emojis :

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 22
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur **Run**.

![La ligne de code supplémentaire dans le Code Editor avec le mot "Bonjour" suivi de trois emojis monde et les mots "Bienvenue sur" suivis d'un serpent emoji et d'un clavier apparaissant dans la zone de sortie.](images/run_multiple.png)

**Astuce :** il est conseillé d'exécuter ton code après chaque modification afin de pouvoir résoudre rapidement les problèmes.


--- /task ---


