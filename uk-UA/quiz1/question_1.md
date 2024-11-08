## Швидкий тест

Дай відповідь на три запитання. Підказки допоможуть знайти правильну відповідь.

Відповівши на кожне питання, натисни на **Перевірити мою відповідь**.

Розважайся!

--- question ---
---
legend: Питання 1 з 3
---

Цей код встановлює змінну `world`, яка буде містити текст '🌍🌎🌏' (три різні емодзі світу):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

Який код коректно використовує змінну `world` та видає «Привіт 🌍🌎🌏»?

![Область виведення у редакторі Code Editor з виведенням на екран повідомлення «Привіт 🌍🌎🌏».](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Привіт' world)

--- /code ---

 --- feedback ---

 Не зовсім так, `output` не виводить повідомлення на екран.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Hello world')

--- /code ---

 --- feedback ---

 Не зовсім. У Python `print` виводить повідомлення на екран, але в цьому прикладі чогось не вистачає.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hello{world}')

--- /code ---

 --- feedback ---

 Правильно! У Python `print` виводить повідомлення на екран. The text output is inside single quotes `'` , then the `world` variable contains the earth emoji 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello{world}')

--- /code ---

 --- feedback ---

  Не зовсім. У Python `print` виводить повідомлення на екран, але в цьому прикладі чогось не вистачає.

 --- /feedback ---

--- /choices ---

--- /question ---
