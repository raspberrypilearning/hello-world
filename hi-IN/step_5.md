## इनपुट प्राप्त करें

आप अपने प्रोग्राम का उपयोग करने वाले व्यक्ति से पाठ दर्ज करने के लिए कहने के लिए `input()`{:.language-python} का उपयोग कर सकते हैं।

--- task ---

अपने फ़ंक्शन को बदलें और अपने प्रोग्राम का उपयोग करने वाले व्यक्ति से पूछें कि पासे में कितनी भुजाएँ हैं, और इसे एक चर के रूप में सहेजें।

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19-20
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** **चलाएँ** बटन पर क्लिक करें और पक्षों की संख्या टाइप करें। सुनिश्चित करें कि आप कितने पक्ष इनपुट करने के बाद <kbd> Enter </kbd> कुंजी दबाएं। जब आप अपना कोड चलाएंगे तो आपको यही दिखाई देगा।

<div class="c-project-output">
```
नमस्कार 🌍🌎🌏
पायथन में आपका स्वागत है 🐍
पायथन 🐍 गणित में अच्छा है!
27
दिनांक और समय है 2025-10-24 13:20:41.323000
आपके पासे में कितने पक्ष हैं?:
20 
यह एक D है 20
आपने 1 रोल किया 🔥
```

--- /task ---

इनपुट हमेशा टेक्स्ट के रूप में संग्रहीत किए जाते हैं, लेकिन हमें रोल की जा सकने वाली सबसे बड़ी संख्या निर्दिष्ट करने के लिए `max` में संग्रहीत इनपुट का उपयोग करने की आवश्यकता है।

--- task ---

`अधिकतम` एक स्ट्रिंग है, इसलिए इसे एक पूर्णांक `int()`{:.language-python}में बदलने की आवश्यकता है।


--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 21
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1, int(max)) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** **चलाएँ** बटन पर क्लिक करें। जांच करें कि पासा हर बार एक यादृच्छिक संख्या फेंकता है।

--- /task ---

