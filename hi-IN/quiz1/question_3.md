--- question ---
---
legend: ३ का प्रश्न ३
---

यह फंक्शन दो यादृच्छिक संख्याओं का आउटपुट देता है:

--- code ---
---
language: python
---

def two_dice(): print('First number:', randint(1, 6)) print('Second number:', randint(1, 6))

--- /code ---

इसे चलाने के लिए कौन सा कोड फंक्शन को कॉल करेगा?

![The code editor with output area showing two randomly generated numbers.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): print('First number:', randint(1, 6)) print('Second number:', randint(1, 6))

--- /code ---

 --- feedback ---

 नहीं, यह कोड फ़ंक्शन को परिभाषित करने के लिए है, लेकिन यह फ़ंक्शन नहीं चलाता है। आपको इसे कॉल करने के लिए अलग कोड का उपयोग करना होगा।

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

बंद करें! `two_dice` फ़ंक्शन का नाम है, लेकिन इसे कॉल करने के लिए आपको केवल नाम से अधिक की आवश्यकता है।

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 बिल्कुल नहीं, उनके बारे में सोचें कि आपने अपने प्रोजेक्ट के फ़ंक्शन को कॉल करने के लिए किस प्रकार के कोष्ठक का उपयोग किया था।

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 यह सही है, फ़ंक्शन नाम का उपयोग करने के बाद `(` `)` कोष्ठक फ़ंक्शन को कॉल करेगा।

 --- /feedback ---

--- /choices ---

--- /question ---
