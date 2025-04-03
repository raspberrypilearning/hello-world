## Hodnoty a operátory

V Pythonu můžete pracovat s čísly a daty.

K výpočtům můžete použít **aritmetické operátory** , například `+` a `-`  :

| + | přidat |   
| - | odečíst |   
| * | násobit |   
| / | rozdělit |   
| ** | mocnina |


--- task ---

Přidejte další dva `print()`{:.language-python} do svého kódu včetně násobení pro Python pro výpočet:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 20-21
---
# Sem vložte kód pro spuštění.
print(f'Ahoj {svet}')
print(f'Vítejte v {python}')
print(f'{python} je dobrý v matematice!')
print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klikni na tlačítko **Run** (Spustit). To je to, co byste měli vidět, když spustíte svůj kód.

```
Ahoj 🌍🌎🌏
Vítejte v Python 🐍
Python 🐍 je dobrý v matematice!
27
```

--- /task ---

Python má mnoho **modulů** , které můžete ve svém kódu použít k provádění určitých úkolů.

Modul `datetime`{:.language-python} pomáhá s psaním kódu, který používá data a časy.

--- task ---

Jako další řádek to tvého kódu přidá současný datum a čas.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 22
---

print(f'{python} je dobrý v matematice!')
print(f'{3 * 9}')
print(f'Datum a čas je {datetime.now()}')

--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte kód několikrát, abyste viděli aktualizaci času.

--- /task ---


