## Lancer un dé 🎲

Les fonctions sont des blocs de code qui exécutent des tâches spécifiques. Elles peuvent être utilisées à l'infini.

Voici un exemple de fonction :

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one(): x = 1 + 1 print(x)

--- /code ---

Le nom de cette fonction s'appelle `add_one_and_one`{:.language-python}.

Le code de la tâche que tu souhaites que la fonction effectue doit être **indenté**, ce qui signifie que tu dois ajouter **quatre espaces** avant chaque ligne de code.

**L'appel ** d'une fonction exécute le code qu'elle contient. Tu **appelles** une fonction en utilisant son nom. Ici, `add_one_and_one()`{:.language-python}.


--- task ---

Recherche le commentaire dans le fichier **main.py** qui dit

`# Définitions de fonctions`{:.language-python}.

Crée une fonction appelée `roule_de()`{:.language-python}, qui imprime le nombre 4.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-18
---
# Définitions de fonctions
def roll_dice(): print(f'You rolled a {4}')

# Put code to run under here

--- /code ---

--- /task ---

--- task ---

Ensuite, appelle la fonction en bas de ton code.

--- code ---
---
language: python line_numbers: true line_number_start: 24
line_highlights: 25
---
print(f'The date and time is {datetime.now()}') roll_dice()

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton projet plusieurs fois pour voir le résultat du dé à chaque fois : ce sera toujours 4.

--- /task ---

--- task ---

Un autre module appelé `random`{:.language-python} peut être utilisé pour créer des nombres aléatoires. Modifie ton code pour utiliser la fonction `randint`{:.language-python} pour choisir un nombre aléatoire entre 1 et 6 pour le lancer de dés.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17
---
# Définitions de fonctions
def roll_dice(): print(f'You rolled a {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** . Maintenant, lorsque tu exécutes ton code, un nouveau nombre aléatoire entre 1 et 6 sera choisi à chaque fois.

--- /task ---

En Python, tu peux multiplier des chaînes de caractères telles que des emojis ou des mots entiers par un nombre, afin qu'elles s'impriment plusieurs fois.

--- task ---

Modifie ta fonction pour stocker le nombre aléatoire dans une variable appelée `rouler`{:.language-python}.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17
---
# Définitions de fonctions
def roll_dice(): roll = randint(1,6)

--- /code ---

--- /task ---

--- task ---

Multiplie le nombre aléatoire stocké dans `rouler`{:.language-python} par l'emoji 🔥 et imprime le résultat.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 18
---
# Function definitions
def roll_dice(): roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** . Ton code de sortie devrait ressembler à ceci :

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:14:45.140000
You rolled a 4 🔥🔥🔥🔥
```

--- /task ---