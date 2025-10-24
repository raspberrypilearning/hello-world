## from noemoji import *

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

[こんにちは 🌍🌎🌏 基本プロジェクト](https://trinket.io/python/a7fcb2ede7){:target="_blank"}を開きます。 Trinketは別のブラウザタブで開きます。

--- /task ---

--- task ---

Find the `# Put code to run under here`{:.language-python} line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 21
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**テスト：** **Run**ボタンをクリックしてコードを実行します。

You should see `Hello` in the Text output area.

--- /task ---

A **variable** is used to store values such as text or numbers. 絵文字を格納する変数をいくつか含めました。

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 20
---
# 動かしたいコードをこの下に書く
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**テスト：**コードを実行して、結果を確認します。

![出力領域に「こんにちは」という単語の後に3つの地球の絵文字が表示された、コード領域の更新されたコード行。](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 22
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**テスト：****Run**をクリックします。

![出力領域に「こんにちは」という単語の後に3つの地球の絵文字が表示され、ヘビの絵文字の後に「へ ようこそ」という単語が表示された、コード領域の追加されたコード行。](images/run_multiple.png)

**ヒント：**問題をすばやく修正できるように、変更のたびにコードを実行することをお勧めします。


--- /task ---


