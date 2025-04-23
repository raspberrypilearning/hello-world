## Rychlý kvíz

Odpověz na následující tři otázky. Zde jsou nápovědy, které tě dovedou ke správné odpovědi.

Po zodpovězení každé otázky klikni na **Zkontrolovat mou odpověď**.

Bav se!

--- question ---
---
legend: Otázka 1 ze 3
---

Tento kód nastavuje proměnnou `world` tak, aby obsahovala text '🌍🌎🌏' (tři různé emotikony světa):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

Který kód správně používá proměnnou `world` a vydává Ahoj 🌍🌎🌏?

![Výstupní oblast z editoru kódu se zobrazením Ahoj 🌍🌎🌏.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Ahoj' world)

--- /code ---

 --- feedback ---

 Ne tak docela, `output` není způsob výstupu zpráv na obrazovku.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

tisknout (f'Ahoj world')

--- /code ---

 --- feedback ---

 Ne tak docela, v Pythonu `print` vypisuje zprávy na obrazovku, ale v tomto příkladu něco chybí.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Ahoj{world}')

--- /code ---

 --- feedback ---

 To je správně, v Pythonu `print` vypisuje zprávy na obrazovku. Textový výstup je v jednoduchých uvozovkách `'` , poté proměnná `world` obsahuje emoji země 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Ahoj{world}')

--- /code ---

 --- feedback ---

  Ne tak docela, v Pythonu `print` vypisuje zprávy na obrazovku, ale v tomto příkladu něco chybí.

 --- /feedback ---

--- /choices ---

--- /question ---
