## قل مرحبا

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
من المعتاد كتابة برنامج لإخراج "Hello world!" عندما تتعلم لغة برمجة جديدة.
</div>
<div>

![The Trinket output area showing the two printed lines of text and emoji.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Open the [Hello 🌍🌎🌏 starter project](https://trinket.io/python/975f35023b){:target="_blank"}. سيتم فتح Trinket في نافذة متصفح أخرى.

![The Trinket editor with project starter code on the left in the code area. على اليمين توجد منطقة الإخراج الفارغة.](images/starter_project.png)

--- /task ---

يخبر السطر البرمجي هذا `#! / bin / python3` أنك تستخدم لغة Python 3 (أحدث إصدار). تخبر الأسطر هذه `import` لغة Python أنك ستستخدم رمزًا لم تكتبه.

In Python, `print()` outputs text (words or numbers) to the screen.

Lines beginning with `#` are comments, they explain the code to humans and are ignored by Python.

--- task ---

Find the `# Put code to run below here` line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

Type the code to `print()` hello:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Put code to run under here
print('Hello')

--- /code ---

--- collapse ---
---
title: Typing special characters on a UK or US keyboard
---

On a UK or US keyboard, the left `(` and right `)` round brackets are on the <kbd>9</kbd> and <kbd>0</kbd> keys. To type a left round bracket, hold down the <kbd>Shift</kbd> key (next to <kbd>Z</kbd>) and then tap <kbd>9</kbd>. The single quote `'` is on the same row as the <kbd>L</kbd> key, just before the <kbd>Enter</kbd> key. The comma `,` is next to the <kbd>M</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Test:** Click on the **Run** button to run your code. In Trinket, the output will appear on the right:

![The Run icon highlighted with 'Hello' showing in the output area. ](images/run_hello.png)

**Debug:** If you get an error then check your code really carefully. In this example, the single quotes around `Hello` are missing so Python doesn't know it is supposed to be text.

![the Trinket editor with missing single quotes and error 'NameError: name 'Hello' is not defined on line 10 in main.py.](images/hello_error.png)

--- /task ---

In Python, a **variable** is used to store text or numbers. Variables make it easier for humans to read code. You can use the same variable in lots of places in your code.

We have included some variables that store emoji characters.

--- task ---

In your Trinket, click on the **emoji.py** tab. Find the variable `world`, which stores the text '🌍🌍🌍'.

--- /task ---

--- task ---

You can `print()` more than one item at a time by including a comma `,` in between the items. `print()` will add a space between each item.

Click on the **main.py** tab to go back to your `print()` code.

Change your code to also `print()` the contents of the `world` variable:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Put code to run under here
print('Hello', world)

--- /code ---

**Tip:** `'Hello'` is a text string because it has single quotes around it, whereas `world` is a variable so the value stored in it will be printed.

--- /task ---

--- task ---

**Test:** Run your code to see the result:

![The updated line of code in the code area with the word 'Hello' followed by three emoji worlds showing in the output area.](images/run_hello_world.png)

Emoji can look different on different computers, so yours might not look exactly the same.

**Debug:** Make sure that you have added a comma between the items in `print()` and that you have spelled `world` correctly.

This example is missing the comma `,`. It's small but very important!

![The Trinket editor with missing single quotes and error 'SyntaxError: bad input on line 12 in main.py' displayed.](images/comma_error.png)

--- collapse ---
---
title: I don't see the emoji
---

Most computers allow you to use colour emoji. However, if you can't use emoji, then you can use 'emoticons' instead, the way we did before emoji were invented!

Change the `from emoji import *` line to:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 3
line_highlights: 3
---

from noemoji import *

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Add another line to your code to `print()` more text and emoji:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Hello', world)    
print('Welcome to', python)

--- /code ---

**Tip:** The code you need to type is highlighted in a lighter colour. Code that is not highlighted helps you find where you need to add the new code.

--- /task ---

--- task ---

**Test:** Click **run**.

![The additional line of code in the code area with the word 'Hello' followed by three emoji worlds and the words 'Welcome to' followed by an emoji snake and keyboard showing in the output area.](images/run_multiple.png)

**Tip:** It's a good idea to run your code after every change so you can fix problems quickly.

**Debug:** Check carefully for brackets, quotes, commas, and correct spelling. Python needs you to be really accurate.

--- /task ---

If you have a Trinket account, you can click on the **Remix** button to save a copy to your `My Trinkets` library.

If you don't have a Trinket account, you can still come back to your project in the future on the same computer by using the starter project link.

--- save ---
