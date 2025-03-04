## Input ophalen

Je kunt `input()`{:.language-python} gebruiken om de persoon die jouw programma gebruikt te vragen tekst in te voeren.

--- task ---

Wijzig je functie zodat de persoon die jouw programma gebruikt, moet invoeren hoeveel zijden de dobbelsteen heeft en sla dit op als een variabele.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17-18
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run** en typ een aantal zijden in. Zorg ervoor dat je op de knop <kbd>Enter</kbd> klikt nadat je het aantal kanten hebt ingevoerd. Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:20:41.323000
How many sides on your dice?:
20 
That is a D 20
You rolled a 1 🔥
```

--- /task ---

Invoer wordt altijd opgeslagen als tekst, maar we moeten de invoer die is opgeslagen in `max` gebruiken om het grootste getal op te geven dat kan worden gerold.

--- task ---

`max` is een string, dus deze moet worden gewijzigd in een integer (geheel getal) `int()`{:.language-python}.


--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 19
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1, int(max)) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik een paar keer op de knop **Run**. Controleer of de dobbelsteen iedere keer een willekeurig getal gooit.

--- /task ---

