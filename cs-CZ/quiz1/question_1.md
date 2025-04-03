## Rychlý kvíz

Odpověz na následující tři otázky. Zde jsou nápovědy, které tě dovedou ke správné odpovědi.

Po zodpovězení každé otázky klikni na **Zkontrolovat mou odpověď**.

Bav se!

--- question ---
---
legend: Otázka 1 ze 3
---

Tento kód nastavuje proměnnou `svet` tak, aby obsahovala text '🌍🌎🌏' (tři různé emotikony světa):

--- code ---
---
language: python
---

svet = '🌍🌎🌏'

--- /code ---

Který kód správně používá proměnnou `svet` a vydává Ahoj 🌍🌎🌏?

![Výstupní oblast z editoru kódu se zobrazením Ahoj 🌍🌎🌏.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Ahoj' svet)

--- /code ---

 --- feedback ---

 Ne tak docela, `output` není způsob výstupu zpráv na obrazovku.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

tisknout (f'Ahoj světe')

--- /code ---

 --- feedback ---

 Ne tak docela, v Pythonu `print` vypisuje zprávy na obrazovku, ale v tomto příkladu něco chybí.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Ahoj{svet}')

--- /code ---

 --- feedback ---

 To je správně, v Pythonu `print` vypisuje zprávy na obrazovku. Textový výstup je v jednoduchých uvozovkách `'` , poté proměnná `svet` obsahuje emoji země 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Ahoj{svet}')

--- /code ---

 --- feedback ---

  Ne tak docela, v Pythonu `print` vypisuje zprávy na obrazovku, ale v tomto příkladu něco chybí.

 --- /feedback ---

--- /choices ---

--- /question ---
