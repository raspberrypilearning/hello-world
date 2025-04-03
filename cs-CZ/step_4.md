## Hod kostkou 🎲

Funkce jsou bloky kódu, které provádějí specifické úkoly. Lze je používat znovu a znovu.

Zde je příklad funkce:

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one():
    x = 1 + 1
    print(x)

--- /code ---

Název této funkce je `add_one_and_one`{:.language-python}.

Kód úlohy, kterou má funkce provést, musí být **odsazený**, což znamená, že před každý řádek kódu musíte přidat **čtyři mezery** .

**Volání** funkce spustí kód uvnitř ní. Funkci můžeš vyvolat napsáním jejího názvu. V tomto případě `add_one_and_one()`{:.language-python}.


--- task ---

Hledejte komentář v souboru **main.py** , který říká

`# Definice funkcí`{:.language-python}.

Vytvořte funkci s názvem `hod_kostkami()`{:.language-python}, která vypíše číslo 4.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 16-18
---
# Definice funkcí
def hod_kostkami():
    print(f'Hodili jste {4}')

# Sem vložte kód pro spuštění

--- /code ---

--- /task ---

--- task ---

Poté zavolejte funkci v dolní části kódu.

--- code ---
---
language: python
line_numbers: true
line_number_start: 24
line_highlights: 25
---
print(f'Datum a čas je {datetime.now()}')
hod_kostkami()

--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte svůj projekt několikrát, abyste viděli, jak hází kostkou pokaždé - vždy to bude 4.

--- /task ---

--- task ---

Další modul s názvem `random`{:.language-python} lze použít k vytváření náhodných čísel. Změňte svůj kód tak, aby používal funkci `randint`{:.language-python} pro výběr náhodného čísla mezi 1 a 6 pro hod kostkou.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 17
---
# Definice funkcí
def hod_kostkami():
    print(f'Hodili jste {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). Nyní, když spustíte svůj kód, bude pokaždé vybráno nové náhodné číslo mezi 1 a 6.

--- /task ---

V Pythonu můžete řetězce, jako jsou emoji nebo celá slova, násobit číslem, takže se vytisknou několikrát.

--- task ---

Změňte svou funkci a uložte náhodné číslo do proměnné s názvem `hod`{:.language-python}.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 17
---
# Definice funkcí
def hod_kostkami():
    hod = randint(1,6)

--- /code ---

--- /task ---

--- task ---

Vynásobte náhodné číslo uložené v `hod`{:.language-python} emoji 🔥 a vytiskněte výsledek.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 18
---
# Definice funkcí
def hod_kostkami():
    hod = randint(1,6)
    print(f'Hodili jste {hod} {ohen * hod}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). Scéna by teď měla vypadat nějak takto:

```
Ahoj 🌍🌎🌏
Vítejte v Python 🐍
Python 🐍 je dobrý v matematice!
12345678987654321
Datum a čas je 2023-11-21 16:14:45.140000
Hodili jste 4 🔥🔥🔥🔥
```

--- /task ---