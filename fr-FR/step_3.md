## Sommes et dates

En Python, tu peux travailler avec des nombres et des dates.

Tu peux utiliser les **opérateurs arithmétiques** tels que `+` et `-`  pour effectuer des calculs :

| + | addition |   
| - | soustraction |   
| * | multiplication |   
| / | division |   
| ** | puissance |


--- task ---

Ajoute deux autres lignes `print()`{:.language-python} à ton code ainsi qu'une multiplication pour que Python puisse calculer :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
line_highlights: 20-21
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}') print(f'{python} is good at maths!') print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** . Tu devrais voir ceci lorsque tu exécutes ton code .

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
```

--- /task ---

Python possède de nombreux **modules** que tu peux utiliser dans ton code pour t'aider à effectuer certaines tâches.

Le module `datetime`{:.language-python} aide à écrire du code qui utilise des dates et des heures.

--- task ---

Ajoute une autre ligne à ton code pour `print`{:.language-python} la date et l'heure actuelles en utilisant la méthode `now()`{:.language-python} de la bibliothèque `datetime`{:.language-python} :

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 22
---

print(f'{python} is good at maths!') print(f'{3 * 9}') print(f'The date and time is {datetime.now()}')

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code plusieurs fois pour voir la mise à jour de la date et de l'heure.

--- /task ---


