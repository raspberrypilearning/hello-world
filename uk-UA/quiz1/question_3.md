--- question ---
---
legend: Питання 3 з 3
---

Ця функція виводить два випадкових числа:

--- code ---
---
language: python
---

def two_dice(): print('Перше число:', randint(1, 6)) print('Друге число:', randint(1, 6))

--- /code ---

Яким кодом можна викликати і запустити цю функцію?

![Редактор Code Editor з областю виведення двох випадково згенерованих чисел.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): print('Перше число:', randint(1, 6)) print('Друге число:', randint(1, 6))

--- /code ---

 --- feedback ---

 Ні, це код для визначення функції, але він не запускає функцію. Використовуй інший код для виклику.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

Близько! `two_dice` — це назва функції. Але для її виклику потрібно більше, ніж просто назва.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 Не зовсім так. Подумай про тип дужок, які використовувалися для виклику функцій у твоєму проєкті.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 Правильно! Використовуй назву функції в дужках `(` `)`, щоб викликати функцію.

 --- /feedback ---

--- /choices ---

--- /question ---
