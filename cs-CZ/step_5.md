## Vstup od uživatele

Můžete použít `input()`{:.language-python} a požádat osobu používající váš program o zadání textu.

--- task ---

Změňte svou funkci a požádejte osobu používající váš program, aby zadala, kolik stran na kostce má, a uložte ji jako proměnnou.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 17-18
---
# Function definitions
def hod_kostkami():
    max = input('Kolik stran máš na kostce?:')
    print(f'To je D  {max}')
    hod = randint(1,6)
    print(f'Hodili jste {hod} {ohen * hod}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikněte na tlačítko **Run** (Spustit) a zadejte počet stran. Ujistěte se, že jste po zadání počtu stran stiskli klávesu <kbd>Enter</kbd> . To je to, co byste měli vidět, když spustíte svůj kód.

<div class="c-project-output">
```
Ahoj 🌍🌎🌏
Vítejte v Python 🐍
Python 🐍 je dobrý v matematice!
12345678987654321
Datum a čas je 2023-11-21 16:20:41.323000
Kolik stran máš na kostce?:
20 
To je D  20
Hodili jste a 1 🔥
```

--- /task ---

Vstupy jsou vždy uloženy jako text, ale musíme použít vstup uložený v `max` k určení největšího čísla, které lze hodit.

--- task ---

`max` je řetězec, takže je třeba jej změnit na celé číslo `int()`{:.language-python}.


--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 19
---
# Function definitions        
def hod_kostkami():
    max = input('Kolik stran máš na kostce?:')
    print(f'To je D {max}')
    hod = randint(1, int(max))
    print(f'Hodili jste a {hod} {ohen * hod}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). Zkontrolujte, zda kostka pokaždé hodí náhodné číslo.

--- /task ---

