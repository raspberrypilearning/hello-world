## नमस्ते प्रिंट करें

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

[हेलो 🌍🌎🌏 स्टार्टर प्रोजेक्ट](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target='_blank'} खोलें। कोड संपादक दूसरे ब्राउज़र टैब में खुलेगा.

![The code editor with project starter code on the left in the code area. On the right is the blank output area.](images/starter_project.png)

--- /task ---

--- task ---

Find the `# Put code to run below here`{:.language-python} line.

उस पंक्ति के नीचे क्लिक करें. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** अपने कोड को चलाने के लिए **Run** बटन पर क्लिक करें। This is what you should see when you run your code:

![आउटपुट क्षेत्र में 'Hello' के साथ हाइलाइट किया गया Run आइकन। ](images/run_hello.png)

--- /task ---

A **variable** is used to store values such as text or numbers. हमने कुछ वेरिएबल शामिल किए हैं जो इमोजी वर्णों को स्टोर करते हैं।

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 17
---
# यहां चलाने के लिए कोड डालें
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**परीक्षण:** परिणाम देखने के लिए अपना कोड चलाएं:

![The updated line of code in the code area with the word 'Hello' followed by three world emojis showing in the output area.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**Test:** Click **Run**.

![The additional line of code in the code editor with the word 'Hello' followed by three world emojis and the words 'Welcome to' followed by an emoji snake and keyboard showing in the output area.](images/run_multiple.png)

**टीप:** प्रत्येक बदलाव के बाद अपना कोड चलाना एक अच्छा विचार है ताकि आप समस्याओं को तुरंत ठीक कर सकें।


--- /task ---


