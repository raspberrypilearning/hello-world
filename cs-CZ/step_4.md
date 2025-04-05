## Hod kostkou 🎲

Funkce jsou bloky kódu, které provádějí specifické úkoly. Lze je používat znovu a znovu.

Zde je příklad funkce:

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one(): x = 1 + 1 print(x)

--- /code ---

Název této funkce je `add_one_and_one`{:.language-python}.

Kód úlohy, kterou má funkce provést, musí být **odsazený**, což znamená, že před každý řádek kódu musíte přidat **čtyři mezery, nebo jeden stisk klávesy Tab**.

**Volání** funkce spustí kód uvnitř těla funkce. Funkci lze**volat** pomocí jejího názvu. V tomto případě `add_one_and_one()`{:.language-python}.


--- task ---

Zkus vyhledat komentář v souboru **main.py**, který říká

`# Definice funkcí`{:.language-python}.

Vytvoř funkci s názvem `roll_dice()`{:.language-python}, která vypíše číslo 4.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-18
---
# Function definitions
def roll_dice(): print(f'You rolled a {4}')

# Put code to run under here

--- /code ---

--- /task ---

--- task ---

Poté zavolej funkci v dolní části kódu.

--- code ---
---
language: python line_numbers: true line_number_start: 24
line_highlights: 25
---
print(f'The date and time is {datetime.now()}') roll_dice()

--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte svůj projekt několikrát, abyste viděli, jak hází kostkou pokaždé - vždy to bude 4.

--- /task ---

--- task ---

Modul s názvem `random`{:.language-python} lze použít k vytváření náhodných čísel. Změň svůj kód tak, aby používal funkci `randint`{:.language-python} pro výběr náhodného čísla mezi 1 a 6 při hodu kostkou.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17
---
# Function definitions
def roll_dice(): print(f'You rolled a {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). Nyní, když spustíte svůj kód, bude pokaždé vybráno nové náhodné číslo mezi 1 a 6.

--- /task ---

V Pythonu můžete řetězce, jako jsou emoji nebo celá slova, násobit číslem, takže se vypíší několikrát.

--- task ---

Změňte svou funkci a uložte náhodné číslo do proměnné s názvem `roll`{:.language-python}.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17
---
# Function definitions
def roll_dice(): roll = randint(1,6)

--- /code ---

--- /task ---

--- task ---

Vynásob náhodné číslo uložené v `roll`{:.language-python} emoji 🔥 a vypíš výsledek.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 18
---
# Function definitions
def roll_dice(): roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). Scéna by teď měla vypadat nějak takto:

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:14:45.140000
You rolled a 4 🔥🔥🔥🔥
```

--- /task ---