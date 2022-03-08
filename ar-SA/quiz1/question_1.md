## Reflection

أحسنت صنعًا ، لقد أنشأت برنامجًا تفاعليًا يحتوي على نص ورموز تعبيرية 👍

حان الوقت الآن لتتطور في التعلم او ما يسمى بالانعكاس - و هو يعد جزء مهم من التعلم لأنه يساعد في إنشاء روابط جديدة في عقلك.

أجب عن الأسئلة الثلاثة أدناه لتكون فهم أعمق عنما تعلمته.

بعد كل سؤال ، اضغط على **إدخال**. سيتم توجيهك نحو الإجابة الصحيحة. You can do this activity as many times as you want to.

Have fun!

--- question ---
---
legend: Question 1 of 3
---

يضبط هذا المقطع البرمجي المتغير `world` ليحتوي على النص "🌍🌎🌏" (الرموز التعبيرية الثلاثة المختلفة للعالم):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

ما المقطع البرمجي الذي يستخدم المتغير `world` بشكل صحيح ويخرج Hello 🌍🌎🌏؟

![منطقة الإخراج من محرر Trinket مع عرض Hello🌍🌎🌏.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hello' world)

--- /code ---

 --- feedback ---

 Not quite, `output` is not the way to output messages to the screen.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Hello' world)

--- /code ---

 --- feedback ---

 ليس بصحيح تماما ان في لغة Python يتم إخراج رسائل إلى الشاشة عن طريق المقطع البرمجي `print`، ولكن هناك شيء مفقود في هذا المثال.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Hello', world)

--- /code ---

 --- feedback ---

 يعد صحيحا ان في لغة Python يتم إخراج رسائل إلى الشاشة عن طريق المقطع البرمجي `print`. The text output is inside single quotes `'` , a comma separates the two items and provides a space, then the `world` variable is called, which stores the earth emoji 🌍🌎🌏, like in your project.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Hello, world)

--- /code ---

 --- feedback ---

  Not quite, in Python `print` outputs messages to the screen, but something is missing in this example.

 --- /feedback ---

--- /choices ---

--- /question ---
