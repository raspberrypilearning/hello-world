## Rychlý kvíz

Odpověz na následující tři otázky. Zde jsou nápovědy, které tě dovedou ke správné odpovědi.

Po zodpovězení každé otázky klikni na **Zkontrolovat mou odpověď**.

Bav se!

--- question ---
---
legend: Question 1 of 3
---

Tento kód nastavuje proměnnou `world` tak, aby obsahovala text '🌍🌎🌏' (tři různé emotikony světa):

--- code ---
---
language: python
---

svět = '🌍🌎🌏'

--- /code ---

Který kód správně používá proměnnou `world` a vydává Ahoj 🌍🌎🌏?

![Výstupní oblast z editoru kódu se zobrazením Ahoj 🌍🌎🌏.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

výstup ('Ahoj' světe)

--- /code ---

 --- feedback ---

 Ne tak docela, výstup `` není způsob výstupu zpráv na obrazovku.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

tisknout (f'Ahoj světe')

--- /code ---

 --- feedback ---

 Ne tak docela, v Pythonu `tisk` vypisuje zprávy na obrazovku, ale v tomto příkladu něco chybí.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

tisknout(f'Ahoj{world}')

--- /code ---

 --- feedback ---

 To je správně, v Pythonu `tisk` vypisuje zprávy na obrazovku. Textový výstup je v jednoduchých uvozovkách `'` , poté proměnná `world` obsahuje emoji země 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Ahoj{world}')

--- /code ---

 --- feedback ---

  Ne tak docela, v Pythonu `tisk` vypisuje zprávy na obrazovku, ale v tomto příkladu něco chybí.

 --- /feedback ---

--- /choices ---

--- /question ---
