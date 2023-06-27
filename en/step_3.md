## Sums and dates

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python is great at working with numbers and dates.
</div>
<div>

![The text output area with five printed lines showing new sum and current date outputs.](images/sums_dates.png){:width="300px"} #TODO

</div>
</div>

In Python you can use maths operators to do sums:

| + | add |   
| - | subtract |   
| * | multiply |   
| / | divide |   
| ** | to the power |   

### Create a calculation

--- task ---

Add another two `print()` lines to your code including a sum for Python to work out:

**Tip:** To get a `*` symbol press <kbd>Shift</kbd> and <kbd>8</kbd> at the same time.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---

print('Hello', world)   
print('Welcome to', python)   
print(python, 'is very good at maths!')   
print(230 * 5782 ** 2 / 23781) # Print the result of the sum

--- /code ---

**Tip:** You don't need to type the comments, they are just there to help you understand the code. Just type the code before the `#`.

--- /task ---

--- task ---

**Test:** Run your code. Did Python calculate the sum correctly? Only joking! Python does the hard maths for you so you don't need to work it out.

**Debug:**

--- collapse ---
---
title: I have a syntax error
---

Make sure that you have added a comma `,` between the items in `print()` and that you have spelled `python` correctly.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Japanese computer scientist <span style="color: #0faeb0">**Emma Haruka Iwao**</span> used a computer to calculate the value of Pi (*π*) to 31 trillion digits. That answer is so long that it would take over 300,000 years just to say it! 
</p>

--- task ---

Try changing the sum that Python does to a complicated one!

You can also use brackets if you want to control the order that Python calculates the sum: `print( (2 + 4) * (5 + 3) )`.

--- /task ---

--- task ---

**Test:** Run your code and get Python to calculate your sum.

**Debug:** Make sure your sum has a left and right round bracket around it `( 2 * 45 )`. If you use extra brackets to control the order, make sure you have a right bracket to match every left bracket.

--- /task ---

--- task ---

On the code editor, you might find the text too big or too small to read. You can easily change these settings to suit your preference. 

**Tip:** Click on the **Settings menu** (the icon next to the Save button) in the top-right of your code editor. Then click on any of the **Text Size** buttons to change the size of the text. 

![The code editor with the settings menu expanded, to show the Colour Mode and Text Size options.](images/full_screen.png) #TODO

You can also switch between colour modes, click on the **Light & Dark** buttons to see the changes.

--- /task ---

The line `from datetime import *` at the top of the **main.py** tab includes a library with helpful functions for getting the current date and time.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
One of the great things about Python is all the <span style="color: #0faeb0">**libraries**</span> of code that are available to use. A Python library allows you to easily use code that other people have written. There are libraries for drawing charts and graphs, making art, doing calculations, and lots more.
</p>

--- task ---

Add another line to your code to `print` the current date and time.

Get the current date and time by using the `now()` function from the `datetime` library:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 21-22
---

print(python, 'is very good at maths!')    
print(230 * 5782 ** 2 / 23781) # Print the result of the sum     
print('The date and time is', datetime.now()) # Print the current date and time
 
--- /code ---

**Tip:** You don't need to type the comments, they are just there to help you understand the code. Just type the part before the `#`.

--- /task ---

--- task ---

**Test:** Run your code a couple of times to see the time update.

**Debug:** Check that you have a fullstop `.` between `datetime` and `now`. Check all the punctuation carefully.

--- /task ---

--- save ---
