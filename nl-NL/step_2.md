## Druk hallo af

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

Open het [Hallo 🌍🌎🌏 startproject](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. De code-editor wordt geopend in een ander browsertabblad.

![The code editor with project starter code on the left in the code area. On the right is the blank output area.](images/starter_project.png)

--- /task ---

--- task ---

Find the `# Put code to run below here`{:.language-python} line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run** om je code uit te voeren. This is what you should see when you run your code:

![Het pictogram Uitvoeren gemarkeerd terwijl 'Hallo' weergegeven wordt in het uitvoergebied. ](images/run_hello.png)

--- /task ---

A **variable** is used to store values such as text or numbers. We hebben enkele variabelen opgenomen die emoji-tekens opslaan.

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 17
---
# Zet de code om uit te voeren hier onder
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**Test:** Voer je code uit om het resultaat te zien:

![De bijgewerkte regel code in het codegebied met het woord 'Hallo' gevolgd door drie emoji-werelden die worden weergegeven in het uitvoergebied.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**Testen:** Klik op **Run**.

![De extra regel code in het codegebied met het woord 'Hallo' gevolgd door drie emoji-werelden en de woorden 'Welkom bij' gevolgd door een emoji-slang en toetsenbord in het uitvoergebied.](images/run_multiple.png)

**Tip:** Het is een goed idee om je code na elke wijziging uit te voeren, zodat je problemen snel kunt oplossen.


--- /task ---


