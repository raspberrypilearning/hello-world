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

![The code editor with output area showing two randomly generated numbers.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): print('Перше число:', randint(1, 6)) print('Друге число:', randint(1, 6))

--- /code ---

 --- feedback ---

 No, this is the code to define the function, but it does not run the function. You'll need to use different code to call it.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

Close! `two_dice` is the name of the function, but to call it you need more than just the name.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 Not quite, think about they type of brackets you used to call the functions in your project.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 That's correct, using the function name followed by `(` `)` brackets will call the function.

 --- /feedback ---

--- /choices ---

--- /question ---
