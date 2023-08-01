## Roll a dice 🎲

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a function for rolling a dice using random numbers. 
  
In Python:
  - **functions**, defined with `def`, are like 'my blocks' in Scratch,
  - `randint` is like 'random' in Scratch, and
  - `input` is like 'ask' in Scratch.

</div>
<div>

![The text output area with additional lines to ask the user to input the biggest number for their dice and the response with the random number.](images/roll_dice.png){:width="300px"} 

</div>
</div>

Python में आप एक क्रिया को पूरा करने के लिए **कॉल** ए **फ़ंक्शन()** करते हैं। आपने पहले से ही टेक्स्ट आउटपुट करने के लिए `print()` फंक्शन का उपयोग किया है।

आप कोड को एक साथ समूहीकृत करने के लिए एक नया **फ़ंक्शन** **परिभाषित** कर सकते हैं ताकि आप इसे नाम दे सकें और फिर से उपयोग कर सकें।

### Define your function

--- task ---

फ़ंक्शंस को कॉल करने से पहले उन्हें परिभाषित करना होगा। Look for the comment in the **main.py** file that says `# Function definitions`.

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

The line under `def roll_dice():` is **indented**. ऐसा करने के लिए, अपने कीबोर्ड पर <kbd>टैब</kbd> वर्ण का उपयोग करें (आमतौर पर कीबोर्ड पर <kbd>CAPSLOCK</kbd> के ऊपर होता है)। इंडेंटिंग कोड Python को बताता है कि इंडेंटेड लाइनें फ़ंक्शन का हिस्सा हैं।

**Tip:** The underscore `_` is used between words in variable and function names in Python to make them easier to read. आप स्पेस का उपयोग नहीं कर सकते हैं।

--- collapse ---
---
title: यूके या यूएस कीबोर्ड पर विशेष वर्ण टाइप करना
---

एक यूके या यूएस कीबोर्ड पर, बृहदान्त्र `:` उसी कुंजी पर है जिस पर अर्धविराम है, <kbd>L</kbd> कुंजी के आगे: <kbd>Shift</kbd> रखें और <kbd>;</kbd> को टैप करें, `:` टाइप करने के लिए । अंडरस्कोर `_` उसी कुंजी पर है जिस पर `-` है, <kbd>0</kbd> के आगे, <kbd>Shift</kbd> को दबाए रखें और <kbd>-</kbd> को टैप करें, `_` को टाइप करने के लिए ।

--- /collapse ---

--- /task ---

--- task ---

**परीक्षण:** यदि आप अभी अपना कोड 'चलाएं', तो यह एक पासा रोल नहीं करेगा। ऐसा इसलिए है क्योंकि आपने `रोल_डाइस ()` फ़ंक्शन को परिभाषित किया है, लेकिन इसे अभी तक कॉल नहीं किया है।

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
