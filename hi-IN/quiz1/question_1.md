## सोचिए

तीन प्रश्नों के उत्तर दीजिए। आपको सही उत्तर के लिए मार्गदर्शन करने के लिए संकेत हैं।

आपने `Events`{:class="block3events"}, `Control`{:class="block3control"}, `Sensing`{:class="block3sensing"}, `Operators`{:class="block3operators"}, `Motion`{:class="block3motion"}, `Looks`{:class="block3looks"}, and `Sound`{:class="block3sound"} ब्लॉक का इस्तेमाल किया है!

अब चिंतन करने का समय है - चिंतन करना सीखने का एक महत्वपूर्ण हिस्सा है, क्योंकि यह आपके मस्तिष्क में नए संबंध बनाने में मदद करता है।

--- question ---
---
legend: 3 में से पहला प्रश्न
---

यह कोड '🌍🌎🌏' (तीन अलग-अलग विश्व इमोजी) टेक्स्ट को शामिल करने के लिए `world` को सेट करता है:

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

कौन सा कोड सही ढंग से `world` वेरिएबल का उपयोग करते हुए "Hello 🌍🌎🌏" का आउटपुट देता है?

![Hello 🌍🌎🌏 के साथ Trinket एडिटर से आउटपुट दिखाया जा रहा है।](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hello' world)

--- /code ---

 --- feedback ---

 बिल्कुल नहीं, `output` स्क्रीन पर संदेशों को आउटपुट करने का तरीका नहीं है।

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Hello' world)

--- /code ---

 --- feedback ---

 काफी नहीं, Python `print` स्क्रीन पर संदेशों को आउटपुट करता है, लेकिन इस उदाहरण में कुछ गायब है।

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Hello', world)

--- /code ---

 --- feedback ---

 यह सही है, Python में `print` स्क्रीन पर संदेशों का आउटपुट देते है। टेक्स्ट आउटपुट एकल उद्धरण `'` के अंदर है, एक अल्पविराम दो वस्तुओं को अलग करता है और एक जगह प्रदान करता है, फिर `world` वेरिएबल कहा जाता है, जो पृथ्वी इमोजी को स्टोर करता है 🌍🌎🌏, जैसे आपके प्रोजेक्ट में।

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Hello, world)

--- /code ---

 --- feedback ---

  काफी नहीं, Python `print` स्क्रीन पर संदेशों को आउटपुट करता है, लेकिन इस उदाहरण में कुछ गायब है।

 --- /feedback ---

--- /choices ---

--- /question ---
