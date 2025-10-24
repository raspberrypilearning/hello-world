## Hodnoty a operátory

V Pythonu můžete pracovat s čísly a daty.

K výpočtům můžete použít **aritmetické operátory**, například `+` a `-`:

| + | přidat |   
| - | odečíst |   
| * | násobit |   
| / | rozdělit |   
| ** | mocnina |


--- task ---

Přidejte další dvě funkce`print()`{:.language-python} do svého kódu včetně násobení, aby Python provedl výpočet:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 23-24
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}') print(f'{python} is good at maths!') print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). To je to, co bys měl vidět, když spustíš svůj kód.

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
```

--- /task ---

Python má mnoho **modulů**, které můžeš ve svém kódu použít k provádění určitých úkolů.

Modul `datetime`{:.language-python} pomůže s psaním kódu, který používá datum a čas.

--- task ---

Jako další řádek do tvého kódu přidej současný datum a čas pomocí metody `now()`{:.language-python} z knihovny `datetime`{:.language-python}:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 23
line_highlights: 25
---

print(f'{python} is good at maths!') print(f'{3 * 9}') print(f'The date and time is {datetime.now()}')

--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte kód několikrát, abyste viděli aktualizaci času.

--- /task ---


