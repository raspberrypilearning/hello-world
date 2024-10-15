## Roll a dice 🎲

Functions are blocks of code that perform specific tasks. They can be used over and over again.

Here is an example of a function:

--- code ---
---
language: python
line_numbers: false
---
# Function definitions
def add_one_and_one():
    x = 1 + 1
    print(x)
--- /code ---

The name of this function is `add_one_and_one`{:.language-python}. 

The code for the task you want the function to do needs to be **indented**, which means that you need to add **four spaces** before each line of code.

**Calling** a function runs the code inside it. You **call** a function by using its name. In this case `add_one_and_one()`{:.language-python}.


--- task ---

Look for the comment in the **main.py** file that says `# Function definitions`{:.language-python}.

Create a function called `roll_dice()`{:.language-python}, that prints out the number 4. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 16-18
---
# Function definitions        
def roll_dice():
    print(f'You rolled a {4}')
    
# Put code to run under here
--- /code ---
--- /task ---

--- task ---

Then, call the function at the bottom of your code.

--- code ---
---
language: python
line_numbers: true
line_number_start: 24
line_highlights: 25
---
print(f'The date and time is {datetime.now()}')
roll_dice()
--- /code ---

--- /task ---

--- task ---

**Test:** Run your project several times to see the dice roll each time - it will always be 4.

--- /task ---

--- task ---
Another module called `random`{:.language-python} can be used to create random numbers. 
Change your code to use the `randint`{:.language-python} function to choose a random number between 1 and 6 for the dice roll.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 17
---
# Function definitions 
def roll_dice():
    print(f'You rolled a {randint(1, 6)}')
--- /code ---
--- /task ---

--- task ---
**Test:** Click the **Run** button.
Now when you run your code, a new random number between 1 and 6 will be chosen each time.
--- /task ---

In Python you can multiply strings such as emojis or whole words by a number, so they print out several times.

--- task ---
Change your function to store the random number in a variable called `roll`{:.language-python}.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 17
---
# Function definitions        
def roll_dice():
    roll = randint(1,6)
--- /code ---
--- /task ---

--- task ---
Multiply the random number stored in `roll`{:.language-python} by the 🔥 emoji, and print the result.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 18
---
# Function definitions        
def roll_dice():
    roll = randint(1,6)
    print(f'You rolled a {roll} {fire * roll}')
--- /code ---
--- /task ---

--- task ---
**Test:** Click the **Run** button.
Your output code should look something like this:

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:14:45.140000
You rolled a 4 🔥🔥🔥🔥
```
--- /task ---