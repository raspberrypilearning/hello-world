## Dire bonjour

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il est de coutume d'écrire un programme pour afficher « Bonjour le monde ! » lorsque tu apprends un nouveau langage de programmation.
</div>
<div>

![La zone de sortie du Code Editor montrant les deux lignes imprimées de texte et d'emojis.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Ouvre le projet de démarrage [Bonjour 🌍🌎🌏](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. Le Code Editor s'ouvrira dans un autre onglet du navigateur.

![Le Code Editor avec le code de démarrage du projet à gauche dans la zone de code. Sur la droite se trouve la zone de sortie vierge.](images/starter_project.png)

Si tu as d'un compte Raspberry Pi, tu peux cliquer sur le bouton **Enregistrer** pour enregistrer une copie dans tes **Projets**.

--- /task ---

--- collapse ---

---
title: Travailler sur Raspberry Pi ?
---

Si tu travailles sur un Raspberry Pi en utilisant Chromium, il se peut que tu ne voies pas les emojis. Tu dois installer une police qui les prend en charge.

Ouvre un terminal puis tape :

```bash
sudo apt install fonts-noto-color-emoji
```

Redémarre Chromium et tu devrais voir les emojis de couleur.

--- /collapse ---

### Print Bonjour

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Les lignes commençant par un `#` sont <span style="color: #0faeb0">**des commentaires**</span>. Ils expliquent ce que fera le code. Les commentaires sont ignorés par Python.
</p>

Les lignes `import` au début du code indiquent à Python que tu vas utiliser du code que tu n'as pas écrit.

En Python, `print()` affiche du texte (mots ou nombres) à l'écran.

--- task ---

Trouve la ligne `# Mettre le code à exécuter ci-dessous`.

Clique sous cette ligne. Le `|` qui clignote est le curseur et indique où tu taperas.

--- /task ---

--- task ---

Tape le code pour `print()` Bonjour à l'écran :

**Astuce :** lorsque tu tapes une parenthèse ouvrante `(` ou une apostrophe ouvrante `'`, le Code Editor ajoute automatiquement une parenthèse fermante `)` ou une apostrophe fermante`'` :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
line_highlights: 18
---

# Mettre le code à exécuter ci-dessous
print('Bonjour')

--- /code ---

--- collapse ---
---
title: Saisie de caractères spéciaux sur un clavier français
---

Sur un clavier français, la parenthèse gauche `(` et droite `)` se trouvent sur les touches <kbd>5</kbd> et <kbd>°</kbd>. Pour saisir un crochet gauche, maintiens la touche <kbd>Maj</kbd> enfoncée (à côté de <kbd>Z</kbd>), puis appuie sur <kbd>9</kbd>. Le guillemet simple `'` se trouve sur la touche <kbd>4</kbd>. La virgule `,` est à côté du <kbd>N</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** pour exécuter ton code. Dans le Code Editor, la sortie apparaîtra à droite :

![L'icône Run est mise en évidence avec "Bonjour" dans la zone de sortie. ](images/run_hello.png)

**Débogage :** si tu obtiens une erreur, vérifie ton code très attentivement. Dans cet exemple, les guillemets simples autour de `Bonjour` sont manquants donc Python ne sait pas qu'il est censé être du texte.

![Le Code Editor avec des guillemets simples manquants et l'erreur 'NameError: name 'Bonjour' is not defined on line 18 in main.py.](images/hello_error.png)

--- /task ---

## Print 🌍🌎🌏

En Python, une **variable** est utilisée pour stocker du texte ou des nombres. Les variables facilitent la lecture du code par les humains. Tu peux utiliser la même variable à de nombreux endroits dans ton code. Choisir un nom judicieux pour une variable te permet de te rappeler plus facilement à quoi elle sert.

Nous avons inclus quelques variables qui stockent les caractères emoji.

--- task ---

Dans ton Code Editor, fais défiler jusqu'aux lignes où les emojis sont stockés dans deux variables différentes. Trouve la variable `monde`, qui stocke le texte '🌍🌍🌍'.

--- /task ---

--- task ---

Tu peux `print()` plus d'un élément à la fois en incluant une virgule `,` entre les éléments. `print()` ajoutera un espace entre chaque élément.

Change ton code pour aussi `print()` le contenu de la variable `monde` :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
line_highlights: 18
---

# Mettre le code à exécuter ci-dessous
print('Bonjour', monde)

--- /code ---

**Astuce :** `'Bonjour'` est une chaîne de texte car elle est entourée de guillemets simples, alors que `monde` est une variable, donc la valeur qui y est stockée sera imprimée.

--- /task ---

--- task ---

**Test :** exécute ton code pour voir le résultat :

![La ligne de code mise à jour dans la zone de code avec le mot "Bonjour" suivi de trois emojis monde dans la zone de sortie.](images/run_hello_world.png)

**Astuce :** Les emojis peuvent avoir un aspect différent selon les ordinateurs, il se peut donc que le tien ne soit pas exactement le même.

**Débogage :** assure-toi que tu as ajouté une virgule entre les éléments dans `print()` et que tu as correctement orthographié `monde`.

Dans cet exemple, il manque la virgule `,`. C'est petit mais très important !

![Le Code Editor avec les guillemets simples manquants et l'erreur 'SyntaxError: bad input on line 18 in main.py' s'affiche.](images/comma_error.png)

--- /task ---

--- task ---

**Ajoute** une autre ligne à ton code pour `print()` plus de texte et d'emojis :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 19
---

print('Bonjour', monde)    
print('Bienvenue dans', python)

--- /code ---

**Astuce :** Le code que tu dois saisir est mis en surbrillance dans une couleur plus claire. Le code qui n'est pas en surbrillance t'aide à trouver où tu dois ajouter le nouveau code.

--- /task ---

--- task ---

**Test :** clique sur **Run**.

![La ligne de code supplémentaire dans le Code Editor avec le mot "Bonjour" suivi de trois emojis monde et les mots "Bienvenue sur" suivis d'un serpent emoji et d'un clavier apparaissant dans la zone de sortie.](images/run_multiple.png)

**Astuce :** il est conseillé d'exécuter ton code après chaque modification afin de pouvoir résoudre rapidement les problèmes.

**Débogage :** vérifie attentivement les parenthèses, les guillemets, les virgules et l'orthographe correcte. Python a besoin que tu sois vraiment précis.

--- /task ---

Si tu as un compte Raspberry Pi, sur ton Code Editor, tu peux cliquer sur le bouton **Enregistrer** pour enregistrer une copie de ton projet dans tes Projets.

--- save ---
