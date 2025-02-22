## Imprimer (print) Bonjour

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

Ouvre le projet de démarrage [Bonjour 🌍🌎🌏](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. Le Code Editor s'ouvrira dans un autre onglet du navigateur.

![The code editor with project starter code on the left in the code area. On the right is the blank output area.](images/starter_project.png)

--- /task ---

--- task ---

Find the `# Put code to run below here`{:.language-python} line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** pour exécuter ton code. This is what you should see when you run your code:

![L'icône Run est mise en évidence avec "Bonjour" dans la zone de sortie. ](images/run_hello.png)

--- /task ---

A **variable** is used to store values such as text or numbers. Nous avons inclus quelques variables qui stockent les caractères emoji.

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 17
---
# Mettre le code à exécuter ci-dessous
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**Test :** exécute ton code pour voir le résultat :

![La ligne de code mise à jour dans la zone de code avec le mot "Bonjour" suivi de trois emojis monde dans la zone de sortie.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
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


