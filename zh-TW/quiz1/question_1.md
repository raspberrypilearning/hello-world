## 快速測驗

回答以下三個問題。 我們會提供提示引導你找到正確答案。

回答問題後，請點選**檢查我的答案**。

玩得開心！

--- question ---
---
legend: Question 1 of 3
---

此程式碼將 `world` 變數設定為包含文字「🌍🌎🌏」（三個不同世界的表情符號）：

--- code ---
---
language: python
---

世界='🌍🌎🌏'

--- /code ---

哪個程式碼正確使用 `世界` 變數並輸出「哈囉 🌍🌎🌏」？

![代碼編輯器的輸出區域顯示「哈囉 🌍🌎🌏」。](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('哈囉'世界)

--- /code ---

 --- feedback ---

 不正確，`output` 不能將訊息輸出。

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Hello world')

--- /code ---

 --- feedback ---

 不正確，在 Python 裡，`print`可以將訊息輸出，但此範例中還缺少一些內容。

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hello{world}')

--- /code ---

 --- feedback ---

 沒錯，在 Python 中 `print` 可以將訊息輸出到螢幕。 The text output is inside single quotes `'` , then the `world` variable contains the earth emoji 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello{world}')

--- /code ---

 --- feedback ---

  不正確，在 Python 裡，`print`可以將訊息輸出，但此範例中還缺少一些內容。

 --- /feedback ---

--- /choices ---

--- /question ---
