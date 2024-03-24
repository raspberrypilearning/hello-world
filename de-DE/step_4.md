## Wirf einen Würfel 🎲

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Erstelle eine Funktion zum Würfeln mithilfe von Zufallszahlen. 
  
In Python:
  - sind **Funktionen**, definiert durch `def`, wie „Meine Blöcke“ in Scratch,
  - `randint` ist wie 'Zufallszahl' in Scratch, und
  - `input` ist wie 'Frage' in Scratch.

</div>
<div>

![Der Textausgabebereich mit zusätzlichen Zeilen, um den Benutzer aufzufordern, die größte Zahl für seine Würfel einzugeben, und die Antwort mit der Zufallszahl.](images/roll_dice.png){:width="300px"} 

</div>
</div>

In Python kannst Du eine **funktion()** **aufrufen**, um eine Aktion auszuführen. Du hast bereits die Funktion `print()` zum Ausgeben von Text verwendet.

Du kannst eine neue **Funktion** **definieren**, um Code zu gruppieren, sodass Du ihn benennen und wiederverwenden kannst.

### Definiere Deine Funktion

--- task ---

Funktionen müssen definiert werden, bevor Du sie aufrufen kannst. Look for the comment in the **main.py** file that says `# Function definitions`.

Define a new function called `roll_dice()` that uses the `randint()` function from the `random` library, to generate a random 'integer' (whole number) from 1 to 6 and output it to the screen.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 15
line_highlights: 16-17
---

# Function definitions
def roll_dice():  # Don't forget the colon at the end of this line   
print('You rolled a', randint(1, 6))  # randint(1, 6) is used to give a number between 1 and 6.

--- /code ---

The line under `def roll_dice():` is **indented**. To do this, use the <kbd>Tab</kbd> character on your keyboard (usually above <kbd>CAPSLOCK</kbd> on the keyboard). Indenting code tells Python that the indented lines are part of the function.

**Tip:** The underscore `_` is used between words in variable and function names in Python to make them easier to read. You can't use a space.

--- collapse ---
---
title: Typing special characters on a UK or US keyboard
---

On a UK or US keyboard, the colon `:` is on the same key as the semicolon, next to the <kbd>L</kbd> key: hold <kbd>Shift</kbd> and tap <kbd>;</kbd> to type a `:`. The underscore `_` is on the same key as the `-`, next to the <kbd>0</kbd>, hold <kbd>Shift</kbd> and tap <kbd>-</kbd> to type an `_`.

--- /collapse ---

--- /task ---

--- task ---

**Test:** If you ‘Run’ your code now, it won't roll a dice. That’s because you have defined the `roll_dice()` function, but not called it yet.

**Debug:**

--- collapse ---
---
title: I have a syntax error
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
line_highlights: 27
---

print('The date and time is', datetime.now())

roll_dice()  # Call the roll dice function

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
language: python filename: main.py line_numbers: true line_number_start: 15
line_highlights: 17-18
---

# Function definitions
def roll_dice(): roll = randint(1, 6)  # Generate a random number between 1 and 6 and store it in the variable 'roll' print('You rolled a', roll, fire * roll)  # Repeat the fire emoji to match the random dice roll

--- /code ---

**Tip** You can use `star` or `heart` instead of `fire` if you prefer, by creating your own emoji variables.

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

Change your `roll` variable code to use `max` as the maximum value for `randint` when it generates a random number.

When you get input from the user, Python treats it as text. But, `randint` needs an 'integer' (a positive whole number). The `int` function turns the user input into an integer.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 15
line_highlights: 18-20
---

# Function definitions

def roll_dice():   
max = input('How many sides?:')  # Wait for input from the user    
print('That\'s a D', max)  # Use the number the user entered    
roll = randint(1, int(max))  # Use max to determine the number of sides the dice has print('You rolled a', roll, fire * roll)

--- /code ---

To print an apostrophe `'` in a word like `That's`, put a backslash `\` before it so Python knows it's part of the text.

--- /task ---

--- task ---

**Test:** Run your project. When the program reaches the `input` line, it will wait for you to enter a response before continuing. Type your response and then press <kbd>Enter</kbd>, this will allow the program to collect your response. Try it again with a different `input` number.

--- /task ---

--- save ---
