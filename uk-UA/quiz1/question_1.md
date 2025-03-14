## Швидкий тест

Дай відповідь на три запитання. Підказки допоможуть знайти правильну відповідь.

Відповівши на кожне питання, натисни на **Перевірити мою відповідь**.

Успіхів!

--- question ---
---
legend: Питання 1 з 3
---

Цей код встановлює змінну `world` (англійською «світ»), яка буде містити текст «🌍🌎🌏» (три різні емоджі земної кулі):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

Який код правилько використовує змінну `world` та видає «Привіт, 🌍🌎🌏»?

![Область виведення у редакторі Code Editor, де видно повідомлення «Привіт, 🌍🌎🌏».](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Привіт,' world)

--- /code ---

 --- feedback ---

 Не зовсім так, `output` не виводить повідомлення на екран.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Привіт, world')

--- /code ---

 --- feedback ---

 Не зовсім. У Python `print` виводить повідомлення на екран, але в цьому прикладі чогось не вистачає.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Привіт, {world}')

--- /code ---

 --- feedback ---

 Правильно! У Python `print` виводить повідомлення на екран. Текст знаходиться в одинарних лапках `'`, а змінна `world` містить емоджі земної кулі 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Привіт, {world}')

--- /code ---

 --- feedback ---

  Не зовсім. У Python `print` виводить повідомлення на екран, але в цьому прикладі чогось не вистачає.

 --- /feedback ---

--- /choices ---

--- /question ---
