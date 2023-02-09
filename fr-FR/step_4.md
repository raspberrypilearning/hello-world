## Lancer un dé

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python peut générer des nombres aléatoires pour créer des dés numériques.
</div>
<div>

![La zone de sortie avec des lignes supplémentaires pour demander à l'utilisateur de saisir le plus grand nombre pour son dé et la réponse avec le nombre aléatoire.](images/roll_dice.png){:width="300px"}

</div>
</div>

En Python, tu **appelles** une **fonction()** pour effectuer une action. Tu as déjà utilisé la fonction `print()` pour afficher du texte.

Tu peux **définir** une nouvelle **fonction** pour regrouper le code afin de pouvoir le nommer et le réutiliser.

--- task ---

Les fonctions doivent être définies avant de pouvoir les appeler. Recherche le commentaire en haut de l'onglet **main.py** qui indique `#Mettre les définitions de fonction ci-dessous`.

Définis une nouvelle fonction appelée `roule_de()` qui utilise la fonction `randint()` , de la bibliothèque `random` , pour générer un « entier » aléatoire (nombre entier) de 1 à 6 et le sortir à l'écran.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9-12
---

# Mettre les définitions de fonction ci-dessous

def roule_de(): #N'oublie pas les deux-points à la fin de cette ligne   
print(python, 'peut faire un ', dice)   
print('Tu as tiré un', randint(1, 6))

--- /code ---

Les lignes sous `def roule_de() :` sont **indentées**. Pour ce faire, utilise le caractère <kbd>Tab</kbd> de ton clavier (généralement au-dessus de <kbd>VER MAJ</kbd> sur le clavier). Le code d'indentation indique à Python que les lignes indentées font partie de la fonction.

**Astuce :** Le trait de soulignement `_` est utilisé entre les mots dans les noms de variables et de fonctions en Python pour les rendre plus faciles à lire. Tu ne peux pas utiliser d'espace.

--- collapse ---
---
title: Saisie de caractères spéciaux sur un clavier français
---

Sur un clavier français, le deux-points `:` se trouve sur la même touche que la barre de division (/), à côté de la touche <kbd>=</kbd>. Le trait de soulignement `_` est sur la même touche que le `-`, à côté du <kbd>)</kbd>, maintiens <kbd>Maj</kbd> et appuie sur <kbd>-</kbd> pour taper un `_`.

--- /collapse ---

--- /task ---

--- task ---

**Test :** Si tu « exécutes » ton code maintenant, il ne lancera pas de dé. C'est parce que tu as défini la fonction `roule_de()`, mais que tu ne l'as pas encore appelée.

--- /task ---

--- task ---

Pour utiliser une fonction, tu dois l'appeler dans le code. Va à la fin de ton code et ajoute une nouvelle ligne pour appeler la fonction `roule_de()` :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 22
---

print('Le', calendar, clock, 'est', datetime.now())

roule_de() #Appelle la fonction lancer de dés

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet plusieurs fois pour voir les dés aléatoires lancés à chaque fois.

**Debogage :** Assure-toi d'avoir un trait de soulignement `_` entre le roule et de pour créer le nom de la fonction. Assure-toi d'avoir un deux-points `:` à la fin de la ligne.

**Debogage :** Vérifie que les lignes sous `def roule_de()` sont indentées. Il est très courant de se tromper en Python, alors assure-toi de vérifier.

![L'éditeur Trinket affichant les lignes de code pour la fonction <code>roule_de</code> n'a pas été indenté. Le code a été exécuté et est mis en surbrillance sur la ligne 10, la première ligne qui doit être indentée, avec l'erreur 'SyntaxError: bad input on line 10 in main.py'.](images/indent_error.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Les utilisations des nombres aléatoires incluent la cryptographie, la science des données et l'ajout de variété dans les jeux et l'infographie. Les ordinateurs génèrent des <span style="color: #0faeb0">**nombres aléatoires**</span> à l'aide d'un algorithme. Pour les nombres vraiment aléatoires, tu as besoin d'une entrée imprévisible du monde réel.
</p>

--- task ---

La variable `feu` stocke un emoji 🔥. Le code `print(feu * 3)` génère trois emoji de feu '🔥🔥🔥'. Tu dois sortir le nombre correct d'emoji pour correspondre au nombre obtenu.

--- collapse ---
---
title: Que se passerait-il si tu utilisais `print(feu * randint(1, 6))` ?
---

Tu obtiendrais un nouveau nombre aléatoire qui est généralement différent de ton premier nombre aléatoire.

--- /collapse ---

Hmm, comment peux-tu t'assurer que tu utilises le même nombre aléatoire ?

Modifie ton code pour enregistrer la valeur renvoyée par `randint()` dans une variable appelée `roule`, puis utilise cette variable pour afficher le nombre obtenu avec le nombre correspondant d'emoji 🔥.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11 - 13
---

# Mettre les définitions de fonction ci-dessous

def roule_de():    
print(python, 'peut faire un', dice)    
roll = randint(1, 6) #Génère un nombre aléatoire entre 1 et 6    
print('Tu as tiré un', roule) #Imprime la valeur de la variable roule     
print(feu * roule) #Répéte l'emoji de feu pour qu'il corresponde au lancer de dés

--- /code ---

Tu peux utiliser `etoile` ou `coeur` au lieu de `feu` si tu préfères.

Le symbole `*` signifie multiplier donc `feu * roule` multiplie le texte dans la variable `feu` ('🔥') par le nombre contenu dans la variable `roule`.

--- /task ---

--- task ---

**Test :** Teste ton projet plusieurs fois. Assure-toi de bien comprendre le fonctionnement du code.

**Astuce :** Les variables sont utiles lorsque tu dois utiliser la même valeur plusieurs fois dans ton code. Donne un nom judicieux aux variables rend également ton code plus facile à comprendre.

--- /task ---

Améliore tes dés afin que l'utilisateur puisse choisir le nombre maximum.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">

De nombreux jeux utilisent des dés à plusieurs côtés. Dans le monde physique, les dés sont fabriqués à partir de formes géométriques régulières. Les dés courants incluent D6, D12 et D20. Sur un ordinateur, tu peux générer un nombre <span style="color: #0faeb0">aléatoire</span> pour faire un dé équitable avec n'importe quel nombre de côtés.</p>

--- task ---

La fonction `input()` pose une question à l'utilisateur puis renvoie sa réponse.

Ajoute du code pour demander à l'utilisateur le plus grand nombre sur ses dés, puis enregistre le résultat dans une variable appelée `max` et `print` le nombre choisi dans la zone de sortie :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Mettre les définitions de fonction ci-dessous

def roule_de():   
print(python, 'peut faire un, dice)   
max = input('Combien de côtés ? :') #Attend l'entrée de l'utilisateur    
print('C\'est un D ', max) #Utilise le nombre que l'utilisateur a entré    
roule = randint(1, 6)    
print('Tu as tiré un', roule)    
print(feu * roule)

--- /code ---

Pour afficher une apostrophe `'` dans un mot comme `C'est`, place une barre oblique inverse `\` devant afin que Python sache que cela fait partie du texte.

--- /task ---

--- task ---

Modifie ton code variable `roule` pour utiliser `max` comme valeur maximale pour `randint` lorsqu'il génère un nombre aléatoire.

Lorsque tu reçois une entrée de l'utilisateur, Python la traite comme du texte. Mais, `randint` a besoin d'un « entier » (un nombre entier positif). La fonction `int` transforme l'entrée utilisateur en entier.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 13
---

# Mettre les définitions de fonction ci-dessous

def roule_de():   
print(python, 'peut faire un', dice)   
max = input('Combien de côtés ? :') #Attend l'entrée de l'utilisateur   
print('C\'est un D ', max) #Utilise le nombre que l'utilisateur a entré   
roule = randint(1, int(max)) #randint a besoin que max soit un "entier"   
print('Tu as obtenu un', roule)   
print(feu * roule)

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet. Lorsque le programme atteint la ligne `input` , il attendra que tu saisisses une réponse avant de continuer. Essaie à nouveau avec un autre nombre dans `input`.

--- /task ---

--- save ---
