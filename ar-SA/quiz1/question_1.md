## تفكير

Answer the three questions. There are hints to guide you to the correct answer.

حان الوقت الآن للتفكير - يعد التفكير جزءًا مهمًا من التعلم لأنه يساعد في إنشاء روابط جديدة في عقلك.

أجب عن الأسئلة الثلاثة أدناه لتفكر فيما تعلمته.

--- question ---
---
legend: السؤال 1 من 3
---

استمتع!

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

ما المقطع البرمجي الذي يستخدم المتغير `world` بشكل صحيح ويخرج Hello 🌍🌎🌏؟

![منطقة الإخراج من محرر Trinket مع عرض Hello.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hello' world)

--- /code ---

 --- feedback ---

 ليس تمامًا ، `output` ليس هو السبيل لإخراج الرسائل إلى الشاشة.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Hello world')

--- /code ---

 --- feedback ---

 ليس تمامًا ، في لغة Python تُخرج `print` رسائل إلى الشاشة، ولكن هناك شيء مفقود في هذا المثال.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hello{world}')

--- /code ---

 --- feedback ---

 هذا صحيح ، في لغة Python فإن الدالة `print` تقوم باخراج الرسائل الى الشاشة. The text output is inside single quotes `'` , then the `world` variable contains the earth emoji 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello{world}')

--- /code ---

 --- feedback ---

  ليس تمامًا ، في لغة Python تُخرج `print` رسائل إلى الشاشة، ولكن هناك شيء مفقود في هذا المثال.

 --- /feedback ---

--- /choices ---

--- /question ---
