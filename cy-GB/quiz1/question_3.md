--- question ---
---
legend: Cwestiwn 3 o 3
---

Mae'r swyddogaeth hon yn allbynnu dau rif ar hap:

--- code ---
---
language: python
---

def dau_ddis(): print('Rhif cyntaf:', randint(1, 6)) print('Ail rif:', randint(1, 6))

--- /code ---

Pa god fydd yn galw'r swyddogaeth i'w rhedeg?

![The code editor with output area showing two randomly generated numbers.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def dau_ddis(): print('Rhif cyntaf:', randint(1, 6)) print('Ail rif:', randint(1, 6))

--- /code ---

 --- feedback ---

 Na, dyma'r cod i ddiffinio'r swyddogaeth, ond nid yw'n rhedeg y swyddogaeth. Bydd angen i chi ddefnyddio cod gwahanol i'w galw.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

dau_ddis

--- /code ---

 --- feedback ---

Agos! `dau_ddis` yw enw'r swyddogaeth ond i'w galw mae angen mwy na dim ond yr enw arnoch chi.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

dau_ddis[]

--- /code ---

 --- feedback ---

 Ddim yn hollol, meddyliwch am y mathau o fracedi roeddech chi wedi'u defnyddio i alw'r swyddogaethau yn eich prosiect.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

dau_ddis()

--- /code ---

 --- feedback ---

 Cywir, bydd defnyddio enw'r swyddogaeth wedi'i ddilyn gan y cromfachau `(` `)` yn galw'r swyddogaeth.

 --- /feedback ---

--- /choices ---

--- /question ---
