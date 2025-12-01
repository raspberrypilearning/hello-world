## रकम और दिनांक

पायथन में आप संख्याओं और तिथियों के साथ काम कर सकते हैं।

आप गणना करने के लिए **अंकगणितीय ऑपरेटर** जैसे `+` और `-`  का उपयोग कर सकते हैं:

| + | add |   
| - | subtract |   
| * | multiply |   
| / | divide |   
| ** | to the power |


--- task ---

अपने कोड में दो और `print()`{:.language-python} पंक्तियाँ जोड़ें, जिनमें पायथन द्वारा गणना करने के लिए गुणन शामिल हो:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 23-24
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}') print(f'{python} is good at maths!') print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** **चलाएँ** बटन पर क्लिक करें। जब आप अपना कोड चलाएंगे तो आपको यही दिखाई देगा।

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
```

--- /task ---

पायथन में कई **मॉड्यूल** हैं जिनका उपयोग आप अपने कोड में कुछ कार्यों को करने में मदद के लिए कर सकते हैं।

`datetime`{:.language-python} मॉड्यूल दिनांक और समय का उपयोग करने वाले कोड लिखने में मदद करता है।

--- task ---

अपने कोड में एक और पंक्ति जोड़ें ``{:.language-python} वर्तमान दिनांक और समय प्रिंट करने के लिए `now()`{:.language-python} विधि का उपयोग करके `datetime`{:.language-python} लाइब्रेरी से:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 23
line_highlights: 25
---

print(f'{python} is good at maths!') print(f'{3 * 9}') print(f'The date and time is {datetime.now()}')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** दिनांक और समय अपडेट देखने के लिए अपना कोड कुछ बार चलाएं।

--- /task ---


