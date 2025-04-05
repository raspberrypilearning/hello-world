## Vstup od uživatele

Můžeš použít `input()`{:.language-python} a požádat osobu používající tvůj program o zadání textu.

--- task ---

Změň svou funkci a požádej osobu používající tvůj program, aby zadala, kolik stran má kostka. Hodnotu ulož jako proměnnou.

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

**Test:** Klikněte na tlačítko **Spustit** a zadej počet stran. Ujisti se, že po zadání počtu stran byla stisknuta klávesa <kbd> Enter </kbd>. To je to, co bys měl vidět, když spustíš svůj kód.

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

Vstupy jsou vždy uloženy jako text, ale musíme použít vstup uložený v `max` k určení největšího čísla, které lze hodit.

--- task ---

`max` je řetězec, takže je třeba jej změnit na celé číslo `int()`{:.language-python}.


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

**Test:** Klikni na tlačítko **Run** (Spustit). Zkontroluj, zda kostka pokaždé hodí náhodné číslo.

--- /task ---

