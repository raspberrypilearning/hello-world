## Отримай дані

За допомогою функції `input()`{:.language-python} (англійською «вхідні дані») ти можеш попросити людину, яка використовує твою програму, ввести якийсь текст.

--- task ---

Зміни свою функцію: попроси користувача твоєї програми ввести кількість сторін кубика і збережи це число як змінну.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 17-18
---
# Визначення функцій
def roll_dice():
    max = input('Кількість сторін кубика:')
    print(f'Цей кубик називається D {max}')
    roll = randint(1,6)
    print(f'Тобі випало число {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Протестуй:** натисни кнопку **Run** та введи кількість сторін. Обовʼязково натисни клавішу введення (<kbd>Enter</kbd>) після того, як введеш кількість сторін. Ось що ти маєш побачити.

<div class="c-project-output">
```
Привіт, 🌍🌎🌏
Ласкаво просимо до Python 🐍
Python 🐍 знається на математиці!
12345678987654321
Дата й час: 2023-11-21 16:20:41.323000
Кількість сторін кубика:
20 
Цей кубик називається D 20
Тобі випало число 1 🔥
```

--- /task ---

Вхідні дані завжди зберігаються як текст, але нам потрібно використати дані змінної `max`, щоб вказати найбільше число на кубику.

--- task ---

`max` — це текстовий рядок, тому нам потрібно змінити її на ціле число за допомогою функції `int()`{:.language-python}.


--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 19
---
# Визначення функцій
def roll_dice():
    max = input('Кількість сторін кубика:')
    print(f'Цей кубик називається D {max}')
    roll = randint(1, int(max))
    print(f'Тобі випало число {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Протестуй:** натисни на кнопку **Run** кілька разів. Кубик щоразу має викидати випадкове число.

--- /task ---

