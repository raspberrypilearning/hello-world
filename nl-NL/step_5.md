## Input ophalen

Je kunt `input()`{:.language-python} gebruiken om de persoon die jouw programma gebruikt te vragen tekst in te voeren.

--- task ---

Wijzig je functie zodat de persoon die jouw programma gebruikt, moet invoeren hoeveel zijden de dobbelsteen heeft en sla dit op als een variabele.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 19-20
---
# Functiedefinities
def gooi_dobbelsteen():
    max = input('Hoeveel zijden heeft jouw dobbelsteen?:')
    print(f'Dat is een D {max}')
    worp = randint(1,6)
    print(f'Je hebt een {worp} {vuur * worp} gegooid')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run** en typ een aantal zijden in. Zorg ervoor dat je op de knop <kbd>Enter</kbd> klikt nadat je het aantal kanten hebt ingevoerd. Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

<div class="c-project-output">
```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
27
De datum en tijd is 2025-10-24 13:20:41.323000
Hoeveel zijden heeft jouw dobbelsteen?:
20 
Dat is een D 20
Je hebt een 1 🔥 gegooid
```

--- /task ---

Invoer wordt altijd opgeslagen als tekst, maar we moeten de invoer die is opgeslagen in `max` gebruiken om het grootste getal op te geven dat kan worden gerold.

--- task ---

`max` is een string, dus deze moet worden gewijzigd in een integer (geheel getal) `int()`{:.language-python}.


--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 21
---
# Functiedefinities        
def gooi_dobbelsteen():
    max = input('Hoeveel zijden heeft jouw dobbelsteen?:')
    print(f'Dat is een D {max}')
    worp = randint(1, int(max))
    print(f'Je hebt een {worp} {vuur * worp} gegooid')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik een paar keer op de knop **Run**. Controleer of de dobbelsteen iedere keer een willekeurig getal gooit.

--- /task ---

