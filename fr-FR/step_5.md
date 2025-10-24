## Obtenir une entrée

Tu peux utiliser `input()`{:.language-python} pour demander à la personne qui utilise ton programme de saisir du texte.

--- task ---

Modifie ta fonction pour demander à la personne qui utilise ton programme d'indiquer le nombre de faces du dé, et enregistre-le comme variable.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19-20
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** et saisis un nombre de faces. Assure-toi d'appuyer sur la touche <kbd> Entrée</kbd> après avoir saisi le nombre de faces. Tu devrais voir ceci lorsque tu exécutes ton code .

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
The date and time is 2025-10-24 13:20:41.323000
How many sides on your dice?:
20 
That is a D 20
You rolled a 1 🔥
```

--- /task ---

Les entrées sont toujours stockées sous forme de texte, mais nous devons utiliser l'entrée stockée dans `max` pour spécifier le plus grand nombre qui pourrait être obtenu.

--- task ---

`max` est une chaîne, elle doit donc être changée en un entier `int()`{:.language-python}.


--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 21
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1, int(max)) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** plusieurs fois. Vérifie que le dé génère un nombre aléatoire à chaque fois.

--- /task ---

