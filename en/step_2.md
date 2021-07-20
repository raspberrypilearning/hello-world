## Say hello

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
It's traditional to write a program to output 'Hello world!' when you learn a new programming language.
</div>
<div>
![The Trinket output area showing the two printed lines of text and emoji.](images/say_hello.png){:width="300px"}
</div>
</div>

--- task ---

Open the [Hello 🌍🌎🌏 starter project](https://trinket.io/library/trinkets/cb8194643f){:target="_blank"}. Trinket will open in another browser tab.

[[[working-offline]]]

![The Trinket editor with project starter code on the left in the code area. On the right is the blank output area.](images/starter_project.png)

--- /task ---

The line `#!/bin/python3` tells Trinket that you are using Python 3 (the latest version). The `import` lines tell Python that you are going to use some code you didn't write.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
One of the great things about Python is all the <span style="color: #0faeb0">**libraries**</span> of code that are available to use. This means that you can easily use code that other people have written.
</p>

In Python, `print` outputs text to the screen.

Lines beginning with `#` are comments. 

--- task ---

Find the `# Put code to run below here` line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

**Tip:** The code you need to type is highlighted in a lighter colour. Code that is not highlighted helps you find where you need to add the new code.

Type the code to `print` hello:

--- code ---
---
language: python
filename: main.py
line_highlights: 2
---
# Put code to run under here
print('Hello')
--- /code ---

--- collapse ---

---
title: Typing special characters on a UK or US keyboard
---

On a UK or US keyboard, the left `(` and right `)` round brackets are on the '9' and '0' keys. To type a left round bracket, hold down the Shift key (next to 'Z') and then tap '8'.
The single quote `'` is on the same row as the 'L' key, just before the 'Enter' key.
The comma `,` is next to the 'M'.

--- /collapse ---

--- /task ---

--- task ---
**Test:** Click on the Run button to run your code. In Trinket, the output will appear on the right:

![The Run icon highlighted with 'Hello' showing in the output area. ](images/run_hello.png)

--- /task ---

In Python, a **variable** is used to store text or numbers. 

The `emoji.py` file contains variable definitions including: `world = '🌍🌎🌏'`.

`world` is a variable and it stores the text string '🌍🌎🌏'. Emoji are special characters.

You can `print` more than one item at a time by including a comma ',' in between the items.

--- task ---
Change your code to also print the contents of the `world` variable:

--- code ---
---
language: python
filename: main.py
line_highlights: 1
---
print('Hello', world)
--- /code ---

--- /task ---

--- task ---
**Test:** Run your code to see the result:

![The updated line of code in the code area with 'Hello 🌍🌎🌏' showing in the output area. ](images/run_hello_world.png)

Emoji can look different on different computers so your might not look quite the same.

--- collapse ---

---
title: I don't see the emoji
---

Most computers allow you to use colour emoji. If you can't use emoji then you can use 'emoticons' instead, the way we did before emoji were invented!

Change the `from emoji import *` line to:

--- code ---
---
language: python
filename: main.py
line_highlights: 1
---
from noemoji import *
--- /code ---

--- /collapse ---

--- /task ---

--- task ---
Add another line to your code to print more text and emoji:

--- code ---
---
language: python
filename: main.py
line_highlights: 2
---
print('Hello', world)
print('Welcome to', python)
--- /code ---
--- /task ---

--- task ---
**Test:** Click run. It's a good idea to run your code after every change so you can fix problems quickly.

![The additional line of code in the code area with 'Hello 🌍🌎🌏' and 'Welcome to 🐍⌨️' showing in the output area. ](images/run_multiple.png)

--- /task ---

--- save ---