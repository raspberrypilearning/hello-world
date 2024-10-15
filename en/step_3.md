## Sums and dates

In Python you can work with numbers and dates.

You can use **arithmetic operators** such as `+` and `-`  to do calculations:

| + | add |   
| - | subtract |   
| * | multiply |   
| / | divide |   
| ** | to the power |   

### Create a calculation

--- task ---

Add two more `print()` lines to your code including a multiplication for Python to calculate:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 20-21
---
# Put code to run under here
print(f'Hello {world}')
print(f'Welcome to {python}')
print(f'{python} is good at maths!')
print(f'{111111111 * 111111111}')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button.
This is what you should see when you run your code.

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
```

--- /task ---

Python has many **modules** that you can use in your code to help perform certain tasks. To use a module, you first need to **import** it. 

The `datetime` module helps with writing code that uses dates and times.
--- task ---

Add another line to your code to `print` the current date and time.

Get the current date and time by using the `now()` function from the `datetime` library:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 22
---

print(f'{python} is good at maths!')
print(f'{111111111 * 111111111}')
print(f'The date and time is {datetime.now()}')
 
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code a couple of times to see the time update.

--- /task ---


