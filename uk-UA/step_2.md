## Скажи "привіт"

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Традиція при вивченні нової мови програмування - написати програму, яка виведе "Привіт, світ!".
</div>
<div>

![Область видачі у Trinket, яка показує два надруковані рядки тексту та емодзі.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Open the [Hello 🌍🌎🌏 starter project](https://staging-editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. The code editor will open in another browser tab.

![The code editor with project starter code on the left in the code area. Праворуч знаходиться порожнє поле для виведення даних.](images/starter_project.png)

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

--- collapse ---

---
line_highlights: 12
---

If you're working on a Raspberry Pi using Chromium, you may not see the emojis. You need to install a font that supports them.

Open a terminal and then type:

```bash
sudo apt install fonts-noto-color-emoji
```

Знайди рядок `# Розмісти код для виконання тут`.

--- /collapse ---

### Print hello

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Lines beginning with a `#` are <span style="color: #0faeb0">**comments**</span>. They explain what the code will do. Comments are ignored by Python.
</p>

The `import` lines at the start of the code tell Python that you are going to use code you didn't write.

language: python filename: main.py line_numbers: true line_number_start: 11

--- task ---

Find the `# Put code to run below here` line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()` Hello to the screen:

**Tip:** When you type an opening bracket `(` or opening apostrophe `'` the code editor will automatically add a closing bracket `)` or closing apostrophe`'`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
title: Набір спеціальних символів на англійській розкладці клавіатури
---

# Розмісти код для виконання тут
print('Hello')

--- /code ---

--- collapse ---
---
line_highlights: 12
---

On a UK or US keyboard, the left `(` and right `)` round brackets are on the <kbd>9</kbd> and <kbd>0</kbd> keys. To type a left round bracket, hold down the <kbd>Shift</kbd> key (next to <kbd>Z</kbd>) and then tap <kbd>9</kbd>. The single quote `'` is on the same row as the <kbd>L</kbd> key, just before the <kbd>Enter</kbd> key. The comma `,` is next to the <kbd>M</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Test:** Click on the **Run** button to run your code. In the code editor, the output will appear on the right:

![The Run icon highlighted with 'Hello' showing in the output area. ](images/run_hello.png)

**Debug:** If you get an error then check your code really carefully. In this example, the single quotes around `Hello` are missing so Python doesn't know it is supposed to be text.

![The Code Editor with missing single quotes and error 'NameError: name 'Hello' is not defined on line 18 in main.py.](images/hello_error.png)

--- /task ---

## title: Я не бачу емодзі

In Python, a **variable** is used to store values such as text or numbers. Variables make it easier for humans to read code. You can use the same variable in lots of places in your code. Choosing a sensible name for a variable makes it easier for you to remember what it is for.

language: python filename: main.py line_numbers: true line_number_start: 11

--- task ---

In your code editor, scroll to the lines with the emojis stored into two different variables. Find the variable `world`, which stores the text '🌍🌍🌍'.

--- /task ---

--- task ---

You can `print()` more than one item at a time by including a comma `,` in between the items. `print()` will add a space between each item.

**Тест:** Запусти свій код, щоб побачити результат:

--- code ---
---
Емодзі можуть виглядати по-різному на різних комп'ютерах, тому на твоєму комп'ютері вони можуть виглядати не зовсім однаково.
line_highlights: 3
---

# Розмісти код для виконання тут
**Налагодження:** Переконайся, що кома додана між елементами в рядках `print()` і що `world` написано правильно.

--- /code ---

**Tip:** `'Hello'` is a text string because it has single quotes around it, whereas `world` is a variable so the value stored in it will be printed.

--- /task ---

--- task ---

Зміни рядок `from emoji import *` на:

![The updated line of code in the code area with the word 'Hello' followed by three world emojis showing in the output area.](images/run_hello_world.png)

language: python filename: main.py line_numbers: true line_number_start: 3

from noemoji import *

This example is missing the comma `,`. It's small but very important!

![The code editor with missing single quotes and error 'SyntaxError: bad input on line 18 in main.py' displayed.](images/comma_error.png)

--- /task ---

--- task ---

Додай ще один рядок до коду, щоб зробити `print()` додаткового тексту та емодзі:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Hello', world)    
print('Welcome to', python)

--- /code ---

**Порада:** Код, який потрібно ввести, виділено світлішим кольором. Код, який не підсвічується, допомагає знайти місце, де необхідно додати новий код.

--- /task ---

--- task ---

**Тест:** Клацни на кнопку **запуску**.

![Додатковий рядок коду в області коду зі словом "Привіт", за яким слідують три емодзі світу та слова "Ласкаво просимо", за якими слідує емодзі змії та клавіатура, що відображається в області виводу.](images/run_multiple.png)

**Порада:** Рекомендується запускати код після кожної зміни, щоб можна було швидко усунути помилки.

**Налагодження:** Уважно перевіряй наявність дужок, лапок, ком та правопис. Python вимагає від тебе особливої уважності.

--- /task ---

Якщо у тебе є обліковий запис в Trinket, ти можеш натиснути на кнопку **Remix**, щоб зберегти копію у свою бібліотеку `My Trinkets`.

--- save ---
