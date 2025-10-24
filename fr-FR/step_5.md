## Obtenir une entrée

Tu peux utiliser `input()`{:.language-python} pour demander à la personne qui utilise ton programme de saisir du texte.

--- task ---

Modifie ta fonction pour demander à la personne qui utilise ton programme d'indiquer le nombre de faces du dé, et enregistre-le comme variable.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 19-20
---
# Définitions de fonctions
def roule_de():
    max = input('Combien de faces sur ton dé ? :')
    print(f'C\'est un D {max}')
    roule = randint(1,6)
    print(f'Tu as obtenu un {roule} {feu * roule}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Exécuter** et saisis un nombre de faces. Assure-toi d'appuyer sur la touche <kbd>Entrée</kbd> après avoir saisi le nombre de faces. Tu devrais voir ceci lorsque tu exécutes ton code .

<div class="c-project-output">
```
Bonjour 🌍🌎🌏
Bienvenue à Python 🐍
Python 🐍 est très bon en maths !
27
La date et l'heure sont 2025-10-24 13:20:41.323000
Combien de faces sur ton dé ? :
20 
C'est un D 20
Tu as obtenu un 1 🔥
```

--- /task ---

Les entrées sont toujours stockées sous forme de texte, mais nous devons utiliser l'entrée stockée dans `max` pour spécifier le plus grand nombre qui pourrait être obtenu.

--- task ---

`max` est une chaîne, elle doit donc être changée en un entier `int()`{:.language-python}.


--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 21
---
# Définitions de fonctions        
def roule_de():
    max = input('Combien de faces sur ton dé ? :')
    print(f'C\'est un D {max}')
    roule = randint(1, int(max))
    print(f'Tu as obtenu un {roule} {feu * roule}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Exécuter** plusieurs fois. Vérifie que le dé génère un nombre aléatoire à chaque fois.

--- /task ---

