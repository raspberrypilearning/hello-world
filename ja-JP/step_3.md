## 計算と日付

In Python you can work with numbers and dates.

You can use **arithmetic operators** such as `+` and `-`  to do calculations:

| + | 足し算 |   
| - | 引き算 |   
| * | 掛け算 |   
| / | 割り算 |   
| ** | べき乗 |


--- task ---

Add two more `print()`{:.language-python} lines to your code including a multiplication for Python to calculate:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
line_highlights: 14-15
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}') print(f'{python} is good at maths!') print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. This is what you should see when you run your code.

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
```

--- /task ---

Python has many **modules** that you can use in your code to help perform certain tasks.

The `datetime`{:.language-python} module helps with writing code that uses dates and times.

--- task ---

Add another line to your code to `print`{:.language-python} the current date and time by using the `now()`{:.language-python} method from the `datetime`{:.language-python} library:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 16-17
---

print(f'{python} is good at maths!') print(f'{3 * 9}') print(f'The date and time is {datetime.now()}')

--- /code ---

--- /task ---

--- task ---

**テスト：**コードを数回実行して、日付と時刻変わるのを確認します。

--- /task ---


