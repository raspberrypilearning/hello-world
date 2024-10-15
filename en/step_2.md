## Print hello

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.
</div>
<div>

![The code editor output area showing the two printed lines of text and emojis.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Open the [Hello 🌍🌎🌏 starter project](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. The code editor will open in another browser tab.

![The code editor with project starter code on the left in the code area. On the right is the blank output area.](images/starter_project.png)
--- /task ---

### Print hello



--- task ---

Find the `# Put code to run below here` line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 11
---
# Put code to run under here.
print(f'Hello')
--- /code ---


--- /task ---

--- task ---

**Test:** Click on the **Run** button to run your code. This is what you should see when you run your code:

![The Run icon highlighted with 'Hello' showing in the output area. ](images/run_hello.png) 

--- /task ---

## Print 🌍🌎🌏

A **variable** is used to store values such as text or numbers. Choosing a sensible name for a variable makes it easier for you to remember what it is for.

We have included some variables that store emoji characters.

--- task ---

Change your code to also `print()` the contents of the `world` variable. You can do this by adding the variable name in curly brackets `{}`


--- code ---
---
language: python
line_numbers: true
line_number_start: 17
---
# Put code to run under here
print(f'Hello {world}')
--- /code --- 

The `f` character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**Test:** Run your code to see the result:

![The updated line of code in the code area with the word 'Hello' followed by three world emojis showing in the output area.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()` more text and emojis:

--- code ---
---
language: python
line_numbers: true
line_number_start: 17
line_highlights: 19
---
# Put code to run under here
print(f'Hello {world}')
print(f'Welcome to {python}')
--- /code ---

**Tip:** The code you need to type is highlighted in a lighter colour. Code that is not highlighted helps you find where you need to add the new code.

--- /task ---

--- task ---

**Test:** Click **Run**. 

![The additional line of code in the code editor with the word 'Hello' followed by three world emojis and the words 'Welcome to' followed by an emoji snake and keyboard showing in the output area.](images/run_multiple.png)

**Tip:** It's a good idea to run your code after every change so you can fix problems quickly.


--- /task ---


