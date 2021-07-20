## Roll a dice

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an introductory sentence. What will learners achieve by the end of this step?
</div>
<div>
![The output area with additional lines to ask the user to input the biggest number for their dice and the response with the random number.](images/roll_dice.png){:width="300px"}
</div>
</div>

In Python, **functions** are used to organise a block of code and give it a name. You have already used the `print` function to output text.
You can also define your own functions and then call them in your code.

You are going to define a function called `roll_dice` which will generate a random number.

--- task ---
Look for the comment near the top of `main.py` which says `# Put function definitions under here` and add a function definition underneath it:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 9-12
---
### Put function definitions under here

def roll_dice():
  print(python, 'can make a', dice)
  roll = randint(1, 6) # Choose a random number between 1 and 6
  print('You rolled a', roll)
--- /code ---

**Tip:** The underscore `_` in Python is used to between words in variable and function names in Python to make them easier to read. You can't use a space. 

--- collapse ---

---
title: Typing special characters on a UK or US keyboard
---

On a UK or US keyboard, the colon `:` is on the same key as the semicolon, next to the <kbd>L</kbd> key, hold <kbd>Shift</kbd> and tap <kbd>;<kbd> to type a `:`.
The underscore `_` is on the same key as the '-', next to the '0', hold <kbd>Shift</kbd> and tap '-' to type an `_`.

--- /collapse ---

--- /task ---

The `from random import randint` line at the top of `main.py` allows you to use the `randint` function to generate random numbers. 

--- task ---

To use a function you need to call it in the code. Go to the end of your code and add a new line to call the `roll_dice` function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 15
line_highlights: 18
---
now = datetime.now()
print('The', calendar, clock, 'is', now)

roll_dice()
--- /code ---

--- /task ---

--- task ---

**Test:** Run your project several times to see the random dice roll each time. 

--- /task ---

--- task ---

The `fire` variable stores a 🔥 emoji. 

Add a line of code at the end of your `roll_dice` function to `print` one 🔥 emoji for each number rolled: 
 
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 13
---
### Put function definitions under here

def roll_dice():
  print(python, 'can make a', dice)
  roll = randint(1, 6)
  print('You rolled a', roll)
  print(fire * roll) # repeats the fire text roll times
--- /code ---

You can use `star` or `heart` instead of `fire` if you prefer.

`*` means multiply so `fire * roll` multiples the text in the `fire` variable ('🔥') by the number containing in the `roll` variable.

--- /task ---

--- task ---

**Test:** Test your project a few times. Make sure you understand how the code works. 

--- /task ---

Upgrade your dice so that the user can choose the maximum number. 

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">

Lots of games use many-sided dice. In the physical world, dice are made from regular geometric shapes. Common dice include D6, D12 and D20. On a computer, you can generate a <span style="color: #0faeb0">random</span> number to make a fair dice with any number of sides.</p>

--- task ---

Create a variable called `max` to store a number `input` by the user. Then `print` the number chosen into the output area: 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 11-12
---
### Put function definitions under here

def roll_dice():
  print(python, 'can make a', dice)
  max = input('How many sides?:')
  print('That is a D', max)
  roll = randint(1, int(max))
  print('You rolled a', roll)
  print(fire * roll)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your project. When the programe reaches the `input` line it will wait for you to enter a response before continuing. Try it again with a different a`input` number. 

--- /task ---

--- save ---