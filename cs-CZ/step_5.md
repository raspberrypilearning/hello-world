## Vstup od uživatele

Můžete použít `input()`{:.language-python} a požádat osobu používající váš program o zadání textu.

--- task ---

Změňte svou funkci a požádejte osobu používající váš program, aby zadala, kolik stran na kostce má, a uložte ji jako proměnnou.

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

**Test:** Klikněte na tlačítko **Spustit** a zadejte počet stran. Ujistěte se, že jste po zadání počtu stran stiskli klávesu <kbd> Enter </kbd> . To je to, co byste měli vidět, když spustíte svůj kód.

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

**Test:** Klikni na tlačítko **Run** (Spustit). Zkontrolujte, zda kostka pokaždé hodí náhodné číslo.

--- /task ---

