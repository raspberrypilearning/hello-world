## Print hello

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

Open the [Hello 🌍🌎🌏 starter project](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. The code editor will open in another browser tab.

--- /task ---

--- task ---

Find the `# Put code to run under here`{:.language-python} line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 21
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**Test:** Click on the **Run** button to run your code.

You should see `Hello` in the Text output area.

--- /task ---

A **variable** is used to store values such as text or numbers. language: python filename: main.py line_numbers: true line_number_start: 11

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 20
---
# Rhowch y cod i'w redeg o dan fan hyn
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

Newidiwch y llinell `from emoji import *` i:

![The updated line of code in the code area with the word 'Hello' followed by three world emojis showing in the output area.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 22
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**Profi:** Cliciwch **run**.

![Y llinell cod ychwanegol yn yr ardal cod gyda'r gair 'Helo' wedi'i ddilyn gan dri emoji byd a'r geiriau 'Croeso i' wedi'u dilyn gan emoji neidr a bysellfwrdd yn yr ardal allbwn.](images/run_multiple.png)

**Cyngor:** Mae'n syniad da rhedeg eich cod ar ôl pob newid er mwyn gallu datrys problemau'n gyflym.


--- /task ---


