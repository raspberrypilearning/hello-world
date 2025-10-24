## Sommen en data

In Python kun je met getallen en data werken.

Je kunt **rekenkundige operatoren** gebruiken, zoals `+` en `-`  om berekeningen uit te voeren:

| + | optellen |   
| - | aftrekken |   
| * | vermenigvuldigen |   
| / | delen |   
| ** | machtsverheffen |


--- task ---

Voeg nog twee `print()`{:.language-python} regels toe aan je code, inclusief een vermenigvuldiging die Python moet berekenen:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 23-24
---
# Zet de code om uit te voeren hieronder
print(f'Hallo {wereld}')
print(f'Welkom bij {python}')
print(f'{python} is goed in wiskunde!')
print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Dit is wat je zou moeten zien wanneer je jouw code uitvoert.

```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
27
```

--- /task ---

Python heeft veel **modules** die je in jouw code kunt gebruiken om bepaalde taken uit te voeren.

De module `datetime`{:.language-python} helpt bij het schrijven van code die gebruik maakt van data en tijden.

--- task ---

Voeg nog een `print`{:.language-python} regel toe voor de huidige datum en tijd door de `now()`{:.language-python} methode te gebruiken van de `datetime`{:.language-python} bibliotheek:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 23
line_highlights: 25
---

print(f'{python} is goed in wiskunde!')
print(f'{3 * 9}')
print(f'De datum en tijd is {datetime.now()}')
 
--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code een paar keer uit om de nieuwe datum- en tijduitvoer te zien.

--- /task ---


