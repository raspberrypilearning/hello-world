## Uzyskaj dane wejściowe

Za pomocą `input()`{:.language-python} możesz poprosić osobę korzystającą z Twojego programu o wprowadzenie tekstu.

--- task ---

Zmień swoją funkcję tak, aby prosiła osobę korzystającą z Twojego programu o podanie liczby boków kostki, i zapisz ją jako zmienną.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17-18
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Kliknij przycisk **Uruchom** i wpisz liczbę boków. Ensure you press the <kbd> Enter </kbd> key after inputting how many sides. This is what you should see when you run your code.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:20:41.323000
How many sides on your dice?:
20 
That is a D 20
You rolled a 1 🔥
```

--- /task ---

Inputs are always stored as text, but we need to use the input stored in `max` to specify the largest number that could be rolled.

--- task ---

`max` is a string, so it needs to be changed to an integer `int()`{:.language-python}.


--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 19
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1, int(max)) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button a few times. Check that the dice rolls a random number each time.

--- /task ---

