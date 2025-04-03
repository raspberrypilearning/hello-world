## Print hello

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

فتح مشروع البداية [Hello 🌍🌎🌏](https://trinket.io/python/683f0efa91){:target="_blank"}. سيتم فتح Trinket في علامة تبويب متصفح أخرى.

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
line_highlights: 12
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**اختبار:** انقر فوق الزر **Run** لتشغيل التعليمات البرمجية الخاصة بك. This is what you should see when you run your code:

![يظهر المقطع البرمجي التشغيل المميز بعلامة "مرحبًا" في منطقة الإخراج. ](images/run_hello.png)

--- /task ---

A **variable** is used to store values such as text or numbers. لقد قمنا بتضمين بعض المتغيرات التي تخزن أحرف الرموز التعبيرية.

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 17
---
# ضع المقطع البرمجي هنا لتشغيله
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**اختبار:** قم بتشغيل المقطع البرمجي الخاص بك لرؤية النتيجة:

![سطر المقطع البرمجي المحدث في منطقة المقطع البرمجي مع كلمة "مرحبًا" متبوعة بثلاثة عوالم رموز تعبيرية تظهر في منطقة الإخراج.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 13
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**اختبار:** انقر **run**.

![سطر المقاطع البرمجية الإضافي في منطقة المقطع البرمجي مع كلمة "مرحبًا" متبوعة بثلاثة عوالم رموز تعبيرية وكلمات "مرحبًا بك في" متبوعة Python رمز تعبيري ولوحة مفاتيح تظهر في منطقة الإخراج.](images/run_multiple.png)

**نصيحة:** من الجيد تشغيل المقطع البرمجي الخاص بك بعد كل تغيير حتى تتمكن من حل المشكلات بسرعة.


--- /task ---


