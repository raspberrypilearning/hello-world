--- question ---
---
legend: Otázka 3 z 3
---

Tato funkce generuje dvě náhodná čísla:

--- code ---
---
language: python
---

def two_dice(): print('První číslo:', randint(1, 6)) print('Druhé číslo:', randint(1, 6))

--- /code ---

Který kód zavolá funkci, aby ji spustil?

![Editor kódu s výstupní oblastí zobrazující dvě náhodně generovaná čísla.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): print('První číslo:', randint(1,6)) print('Druhé číslo:', randint(1,6))

--- /code ---

 --- feedback ---

 Ne, toto je kód pro definování funkce, ale nespouští funkci. K jeho volání budete muset použít jiný kód.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

dvě_kostky

--- /code ---

 --- feedback ---

Blízko! `two_dice` je název funkce, ale k jejímu volání potřebujete víc než jen název.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

dvě_kostky[]

--- /code ---

 --- feedback ---

 Ne tak docela, přemýšlejte o typu závorek, které jste použili k volání funkcí ve vašem projektu.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

dvě_kostky()

--- /code ---

 --- feedback ---

 To je správně, za použití názvu funkce následovaného `(` `)` hranaté závorky funkci zavolá.

 --- /feedback ---

--- /choices ---

--- /question ---
