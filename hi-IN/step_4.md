## एक डाईस रोल करें

फंक्शन कोड के ब्लॉक होते हैं जो विशिष्ट कार्य करते हैं। इनका उपयोग बार-बार किया जा सकता है।

यहाँ एक फ़ंक्शन का उदाहरण दिया गया है:

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one(): x = 1 + 1 print(x)

--- /code ---

इस फ़ंक्शन का नाम `add_one_and_one`{:.language-python}है।

जिस कार्य के लिए आप फ़ंक्शन से कोड करवाना चाहते हैं, उसे **इंडेंट**होना चाहिए, जिसका अर्थ है कि आपको कोड की प्रत्येक पंक्ति से पहले **चार स्पेस** जोड़ने की आवश्यकता है।

**** फ़ंक्शन को कॉल करने से उसके अंदर कोड चलता है। आप **किसी फ़ंक्शन को उसके नाम का उपयोग करके** कॉल करते हैं। In this case `add_one_and_one()`{:.language-python}.


--- task ---

**main.py** फ़ाइल में यह टिप्पणी देखें जो कहती है

27 दिनांक और समय है 2025-10-24 12:41:45.140000 आपने 4 🔥🔥🔥🔥 रोल किया

`roll_dice()`{:.language-python}नामक एक फ़ंक्शन बनाएं, जो संख्या 4 प्रिंट करता है।

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18-20
---
# फ़ंक्शन परिभाषाएँ
def roll_dice(): print(f'You rolled a {4}')

# Put code to run under here

--- /code ---

--- /task ---

--- task ---

फिर, अपने कोड के नीचे दिए गए फ़ंक्शन को कॉल करें।

--- code ---
---
language: python line_numbers: true line_number_start: 26
line_highlights: 27
---
print(f'The date and time is {datetime.now()}') roll_dice()

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** प्रत्येक बार पासा लुढ़कते देखने के लिए अपने प्रोजेक्ट को कई बार चलाएँ - यह हमेशा 4 ही होगा।

--- /task ---

--- task ---

`random`{:.language-python} नामक एक अन्य मॉड्यूल का उपयोग यादृच्छिक संख्याएँ बनाने के लिए किया जा सकता है। पासा रोल के लिए 1 और 6 के बीच एक यादृच्छिक संख्या चुनने के लिए `randint`{:.language-python} फ़ंक्शन का उपयोग करने के लिए अपना कोड बदलें।

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# फ़ंक्शन परिभाषाएँ
def roll_dice(): print(f'You rolled a {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** **चलाएँ** बटन पर क्लिक करें। अब जब आप अपना कोड चलाएंगे, तो हर बार 1 से 6 के बीच एक नया यादृच्छिक नंबर चुना जाएगा।

--- /task ---

पायथन में आप इमोजी या पूरे शब्दों जैसे स्ट्रिंग्स को किसी संख्या से गुणा कर सकते हैं, जिससे वे कई बार प्रिंट हो जाते हैं।

--- task ---

यादृच्छिक संख्या को `रोल`{:.language-python}नामक चर में संग्रहीत करने के लिए अपने फ़ंक्शन को बदलें।

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# फ़ंक्शन परिभाषाएँ
def roll_dice(): roll = randint(1,6)

--- /code ---

--- /task ---

--- task ---

`रोल`{:.language-python} में संग्रहीत यादृच्छिक संख्या को 🔥 इमोजी से गुणा करें, और परिणाम प्रिंट करें।

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 20
---
# Function definitions
def roll_dice(): roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** **चलाएँ** बटन पर क्लिक करें। आपका आउटपुट कोड कुछ इस तरह दिखना चाहिए:

```
नमस्कार 🌍🌎🌏
पायथन में आपका स्वागत है 🐍
पायथन 🐍 गणित में अच्छा है!
27
दिनांक और समय है 2025-10-24 12:41:45.140000
आपने 4 🔥🔥🔥🔥 रोल किया
```

--- /task ---