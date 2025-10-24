## Lancer un dé 🎲

Les fonctions sont des blocs de code qui exécutent des tâches spécifiques. Elles peuvent être utilisées à l'infini.

Voici un exemple de fonction :

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one():
    x = 1 + 1
    print(x)

--- /code ---

Le nom de cette fonction s'appelle `add_one_and_one`{:.language-python}.

Le code de la tâche que tu souhaites que la fonction effectue doit être **indenté**, ce qui signifie que tu dois ajouter **quatre espaces** avant chaque ligne de code.

**L'appel** d'une fonction exécute le code qu'elle contient. Tu **appelles** une fonction en utilisant son nom. Ici, `add_one_and_one()`{:.language-python}.


--- task ---

Recherche le commentaire dans le fichier **main.py** qui dit

`# Définitions de fonctions`{:.language-python}.

Crée une fonction appelée `roule_de()`{:.language-python}, qui imprime le nombre 4.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 18-20
---
# Définitions de fonctions        
def roule_de():
    print(f'Tu as obtenu un {4}')
    
# Put code to run under here

--- /code ---

--- /task ---

--- task ---

Ensuite, appelle la fonction en bas de ton code.

--- code ---
---
language: python
line_numbers: true
line_number_start: 26
line_highlights: 27
---
print(f'La date et l\'heure sont {datetime.now()}')
roule_de()

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton projet plusieurs fois pour voir le résultat du dé à chaque fois : ce sera toujours 4.

--- /task ---

--- task ---

Un autre module appelé `random`{:.language-python} peut être utilisé pour créer des nombres aléatoires. Modifie ton code pour utiliser la fonction `randint`{:.language-python} pour choisir un nombre aléatoire entre 1 et 6 pour le lancer de dés.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 19
---
# Définitions de fonctions 
def roule_de():
    print(f'Tu as obtenu un {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** . Maintenant, lorsque tu exécutes ton code, un nouveau nombre aléatoire entre 1 et 6 sera choisi à chaque fois.

--- /task ---

En Python, tu peux multiplier des chaînes de caractères telles que des emojis ou des mots entiers par un nombre, afin qu'elles s'impriment plusieurs fois.

--- task ---

Modifie ta fonction pour stocker le nombre aléatoire dans une variable appelée `roule`{:.language-python}.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 19
---
# Définitions de fonctions        
def roule_de():
    roule = randint(1,6)

--- /code ---

--- /task ---

--- task ---

Multiplie le nombre aléatoire stocké dans `roule`{:.language-python} par l'emoji 🔥 et imprime le résultat.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 20
---
# Définitions de fonctions        
def roule_de():
    roule = randint(1,6)
    print(f'Tu as obtenu un {roule} {feu * roule}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** . Ton code de sortie devrait ressembler à ceci :

```
Bonjour 🌍🌎🌏
Bienvenue à Python 🐍
Python 🐍 est très bon en maths !
27
La date et l'heure sont 2025-10-24 12:41:45.140000
Tu as obtenu un 4 🔥🔥🔥🔥
```

--- /task ---