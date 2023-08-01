## قل مرحبا

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
من المعتاد كتابة برنامج لإخراج عبارة "Hello world!" عندما تتعلم لغة برمجة جديدة.
</div>
<div>

![منطقة إخراج Trinket تعرض سطري النص المطبوعين والرموز التعبيرية.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

فتح مشروع البداية [Hello 🌍🌎🌏](https://trinket.io/python/683f0efa91){:target="_blank"}. سيتم فتح Trinket في علامة تبويب متصفح أخرى.

![محرر Trinket مع رمز بدء المشروع على اليسار في منطقة المقطع البرمجي. على اليمين توجد منطقة الإخراج الفارغة.](images/starter_project.png)

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

--- collapse ---

---
title: Working on a Raspberry Pi?
---

If you're working on a Raspberry Pi using Chromium, you may not see the emojis. You need to install a font that supports them.

Open a terminal and then type:

```bash
sudo apt install fonts-noto-color-emoji
```

Restart Chromium and you should see the colour emojis.

--- /collapse ---

### Print hello

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Lines beginning with a `#` are <span style="color: #0faeb0">**comments**</span>. They explain what the code will do. Comments are ignored by Python.
</p>

الأسطر التي تبدأ بالرمز `#` عبارة عن تعليقات، فهي تشرح المقطع البرمجي للبشر وتتجاهلها لغة Python اي لا تنفذ.

في Python، تقوم `()print` بإخراج نص (كلمات أو أرقام) على الشاشة.

--- task ---

جد السطر `# ضع المقطع البرمجي هنا لتشغيله`.

انقر أسفل ذلك السطر. الوميض `|` هو المؤشر ويظهر المكان الذي ستكتب فيه.

--- /task ---

--- task ---

اكتب المقطع البرمجي `()print` لطباعة مرحبًا:

**Tip:** When you type an opening bracket `(` or opening apostrophe `'` the code editor will automatically add a closing bracket `)` or closing apostrophe`'`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# ضع المقطع البرمجي هنا لتشغيله
print('Hello')

--- /code ---

--- collapse ---
---
title: كتابة أحرف خاصة على لوحة مفاتيح المملكة المتحدة أو الولايات المتحدة
---

على لوحة مفاتيح المملكة المتحدة أو الولايات المتحدة، الأقواس المستديرة الأيسر `(` والأيمن `)` موجودة على مفاتيح <kbd>9</kbd> و <kbd>0</kbd>. لكتابة قوس دائري أيسر ، اضغط باستمرار على مفتاح <kbd>Shift</kbd> (بجوار <kbd>Z</kbd>) ثم اضغط على <kbd>9</kbd>. يوجد الاقتباس الفردي `'` في نفس الصف للحرف <kbd>L</kbd>، قبل مفتاح <kbd>Enter</kbd> مباشرةً. الفاصلة `,` موجودة بجوار الحرف <kbd>M</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**اختبار:** انقر فوق الزر **Run** لتشغيل التعليمات البرمجية الخاصة بك. في Trinket ، سيظهر الإخراج على اليمين:

![يظهر المقطع البرمجي التشغيل المميز بعلامة "مرحبًا" في منطقة الإخراج. ](images/run_hello.png)

**تتبع الخطأ:** إذا حصلت على خطأ، فتحقق من المقطع البرمجي بعناية. في هذا المثال ، علامات الاقتباس المفردة حول `Hello` مفقودة ، لذا فإن Python لا تعرف أنه من المفترض أن تكون نصًا.

![محرر Trinket مع علامات الاقتباس المفردة المفقودة والخطأ 'NameError: الاسم' Hello 'غير محدد في السطر 10 في main.py.](images/hello_error.png)

--- /task ---

## Print 🌍🌎🌏

في Python ، يتم استخدام **المتغير** لتخزين النصوص أو الأرقام. المتغيرات تسهل على البشر قراءة التعليمات البرمجية. يمكنك استخدام نفس المتغير في العديد من الأماكن في التعليمات البرمجية الخاصة بك. Choosing a sensible name for a variable makes it easier for you to remember what it is for.

لقد قمنا بتضمين بعض المتغيرات التي تخزن أحرف الرموز التعبيرية.

--- task ---

في Trinket ، انقر فوق علامة التبويب **emoji.py**. ابحث عن المتغير `world`، والذي يخزن النص "🌍🌍🌍".

--- /task ---

--- task ---

يمكنك طباعة أكثر من عنصر واحد في وقت واحد عن طريق تضمين فاصلة `,` بين العناصر داخل دالة `()print`. الدالة `()print` ستضيف مسافة بين كل عنصر.

قم بتغيير المقطع البرمجي الخاص بك ليقوم ايضا بطباعة `()print` محتويات المتغير `world`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 3
---

# ضع المقطع البرمجي هنا لتشغيله
print('Hello', world)

--- /code ---

**نصيحة:** `"Hello"` عبارة عن سلسلة نصية لأنها تحتوي على علامات اقتباس مفردة حولها ، في حين أن `world` عبارة عن متغير لذلك ستتم طباعة القيمة المخزنة فيه.

--- /task ---

--- task ---

**اختبار:** قم بتشغيل المقطع البرمجي الخاص بك لرؤية النتيجة:

![سطر المقطع البرمجي المحدث في منطقة المقطع البرمجي مع كلمة "مرحبًا" متبوعة بثلاثة عوالم رموز تعبيرية تظهر في منطقة الإخراج.](images/run_hello_world.png)

يمكن أن تبدو الرموز التعبيرية مختلفة على أجهزة الكمبيوتر المختلفة ، لذلك قد لا تبدو رموزك نفسها تمامًا.

**تتبع الخطأ:** تأكد من أنك أضفت فاصلة بين العناصر في دالة `()print` وأنك كتبت `world` بشكل صحيح.

يفتقد هذا المثال الفاصلة `,`. إنها صغيرة ولكنها مهمة جدًا!

![تم عرض محرر Trinket مع علامات الاقتباس المفردة المفقودة والخطأ 'SyntaxError: bad input on line 12 in main.py'.](images/comma_error.png)

--- /task ---

--- task ---

أضف سطرًا آخر إلى التعليمات البرمجية الخاصة بك لطباعة `()print` نصوص ورموز تعبيرية اخرى:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Hello', world)    
print('Welcome to', python)

--- /code ---

**نصيحة:** يتم تمييز الرمز الذي تريد كتابته بلون أفتح. يساعدك المقطع البرمجي الذي لم يتم تمييزه في العثور على المكان الذي تريد إضافة الرمز الجديد إليه.

--- /task ---

--- task ---

**اختبار:** انقر **run**.

![سطر المقاطع البرمجية الإضافي في منطقة المقطع البرمجي مع كلمة "مرحبًا" متبوعة بثلاثة عوالم رموز تعبيرية وكلمات "مرحبًا بك في" متبوعة Python رمز تعبيري ولوحة مفاتيح تظهر في منطقة الإخراج.](images/run_multiple.png)

**نصيحة:** من الجيد تشغيل المقطع البرمجي الخاص بك بعد كل تغيير حتى تتمكن من حل المشكلات بسرعة.

**تتبع الخطأ:** تحقق بعناية من وجود الأقواس وعلامات التنصيص والفاصلات والتهجئة الصحيحة. تحتاج Python أن تكون دقيقًا حقًا.

--- /task ---

إذا كان لديك حساب Trinket ، فيمكنك النقر فوق الزر **Remix** لحفظ نسخة في مكتبة `My Trinkets`.

--- save ---
