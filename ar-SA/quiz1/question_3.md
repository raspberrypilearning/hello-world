--- question ---
---
legend: السؤال 3 من 3
---

تنتج هذه الدالة رقمين عشوائيين:

--- code ---
---
language: python
---

def two_dice():
  print('First number:', randint(1, 6))
  print('Second number:', randint(1, 6))

--- /code ---

ما هو المقطع البرمجي الذي سيستدعي الدالة لتشغيله؟

![يُظهر محرر Trinket بمنطقة الإخراج رقمين تم إنشاؤهما عشوائيًا.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice():
  print('First number:', randint(1, 6))
  print('Second number:', randint(1, 6))

--- /code ---

 --- feedback ---

 لا ، هذا هو المقطع البرمجي الخاص بتعريف الدالة البرمجية ، لكنه لا يقوم بتنفيذ الدالة. ستحتاج إلى استخدام مقطع برمجي مختلف لاستدعائه.

 --- /feedback ---

- ( )
--- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

قريب! `two_dice` هو اسم الدالة البرمجية ، ولكن لتسميتها فإنك تحتاج إلى أكثر من مجرد الاسم.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 ليس تمامًا ، فكر في نوع الأقواس التي استخدمتها لاستدعاء الدالة البرمجية في مشروعك.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 هذا صحيح ، فإن استخدام اسم الدالة البرمجية متبوعًا بأقواس `(` `)` سيؤدي إلى استدعاء الدالة البرمجية.

 --- /feedback ---

--- /choices ---

--- /question ---
