## Підкинь кубик

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a function for rolling a dice using random numbers. 
  
In Python:
  - **functions**, defined with `def`, are like 'my blocks' in Scratch,
  - `randint` is like 'random' in Scratch, and
  - `input` is like 'ask' in Scratch.

</div>
<div>

![Область виводу з додатковими рядками, в яких користувачу пропонується ввести найбільше число, яке може випасти, та відповідь з випадковим числом.](images/roll_dice.png){:width="300px"} 

</div>
</div>

У Python ти **викликаєш** **функцію()**, щоб здійснити якусь дію. Функція `print()` вже використовувалась тобою раніше, для виведення тексту.

Ти можеш **визначити** нову **функцію**, щоб згрупувати код разом. Це дозволить дати йому ім'я та повторно його використати.

### Define your function

--- task ---

Функції повинні бути визначені до того, як ти будеш їх викликати. Look for the comment in the **main.py** file that says `# Function definitions`.

Визнач нову функцію з назвою `roll_dice()` яка використовує функцію `randint()`, з бібліотеки `random`, щоб згенерувати випадкове 'натуральне' (ціле) число від 1 до 6 та вивести його на екран.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9-12
---

# Помісти сюди визначення функцій
def roll_dice(): #Не забуваймо про двокрапку в кінці цього рядка   
print(python, 'може зробити', dice)   
print('Тобі випало число:', randint(1, 6))

--- /code ---

The line under `def roll_dice():` is **indented**. Щоб зробити це, скористайся кнопкою <kbd>Tab</kbd> на клавіатурі (зазвичай знаходиться над <kbd>CAPSLOCK</kbd>). Код з абзацними відступами вказує Python, що рядки з абзацними відступами є частиною функції.

**Tip:** The underscore `_` is used between words in variable and function names in Python to make them easier to read. Не можна використовувати пробіл.

--- collapse ---
---
title: Набір спеціальних символів на англійській розкладці клавіатури
---

На англійській розкладці клавіатури, двокрапка `:` знаходиться на тій самій клавіші, що і крапка з комою, справа від клавіші <kbd>L</kbd>: утримуй <kbd>Shift</kbd> та натисни на <kbd>;</kbd>, щоб отримати `:`. Символ підкреслення `_` знаходиться на тій самій клавіші, що й `-`, справа від <kbd>0</kbd>, утримуй <kbd>Shift</kbd> та натисни на <kbd>-</kbd>, щоб отримати `_`.

--- /collapse ---

--- /task ---

--- task ---

**Тест:** Якщо запустити твій код зараз, він не спрацює. Це тому, що функція `roll_dice()` була визначена, але ще не викликана.

**Debug:**

--- collapse ---
---
line_highlights: 22
---

- Make sure you have an underscore `_` between roll and dice to make the function name.

- Make sure you have a colon `:` at the end of the line.

- Check that the line under `def roll_dice()` is indented. It's really common to get this wrong in Python, so make sure to check.

![The code editor showing the line of code inside the <code>roll_dice</code> function has not been indented. The line of code with the error is highlighted. The code has been run, with the error 'SyntaxError: bad input on line 17 in main.py'.](images/indent_error.png)

--- /collapse ---

--- /task ---

### Call your function

--- task ---

To use a function, you need to **call** it in the code. Go to the end of your code and add a new line to call the `roll_dice()` function:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 25
title: Що буде, якщо використати код `print(fire * randint(1, 6))`?
---

print('The date and time is', datetime.now())

**Тест:** Запусти свій проєкт декілька разів, щоб побачити випадіння випадкового числа кожного разу.

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project several times to see the random dice roll each time.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Uses of random numbers include cryptography, data science, and adding variety into games and computer art. Computers generate <span style="color: #0faeb0">**random numbers**</span> using an algorithm. For numbers that are really random, you need an unpredictable input from the real world.
</p>

### Use 🔥🔥🔥 for the number rolled

--- task ---

Your function can use the 🔥 emoji variable. The code `print(fire * 3)` outputs three fire emojis '🔥🔥🔥'. You need to output the correct number of emojis to match the random number rolled by the dice.

Change your code to save the value returned by `randint()` in a variable called `roll`. Use that variable to print out the number rolled with the matching number of 🔥 emojis.

--- code ---
---
Хм, а як можна переконатися, що використовується одне й те саме випадкове число?
line_highlights: 11 - 13
---

# Помісти сюди визначення функцій
Зміни код для збереження значення, що повертатиметься за допомогою `randint()` у змінній з назвою `roll` та використовуй цю змінну, щоб вивести число, яке випало з відповідною кількістю емодзі 🔥.

--- /code ---

language: python filename: main.py line_numbers: true line_number_start: 7

--- /task ---

--- task ---

**Test:** Test your project a few times. Make sure you understand how the code works.

--- /task ---

### Choose the number of sides on the dice

Upgrade your dice so that the user can choose the maximum number.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Lots of games use many-sided dice. In the physical world, dice are made from regular geometric shapes. Common dice include D6, D12, and D20. On a computer, you can generate a <span style="color: #0faeb0">random</span> number to make a fair dice with any number of sides.</p>

--- task ---

The `input()` function asks the user a question and then returns their answer.

**Add** code to ask the user for the biggest number on their dice and then save the result in a variable called `max` and `print` the number chosen into the output area:

Вдосконалюй свій кубик так, щоб у користувача була можливість вибрати максимальне число.

When you get input from the user, Python treats it as text. But, `randint` needs an 'integer' (a positive whole number). The `int` function turns the user input into an integer.

--- code ---
---
Функція `input()` задає користувачу питання, а потім отримує його відповідь.
line_highlights: 11-12
---

# Помісти сюди визначення функцій

Додай код, який буде запитувати у користувача найбільше число для його кубика, а потім збереже результат у змінну з іменем `max` та зробить `print` вибраного числа у вихідну область:

--- /code ---

language: python filename: main.py line_numbers: true line_number_start: 7

--- /task ---

--- task ---

**Test:** Run your project. When the program reaches the `input` line, it will wait for you to enter a response before continuing. Type your response and then press <kbd>Enter</kbd>, this will allow the program to collect your response. Try it again with a different `input` number.

--- /task ---

--- save ---
