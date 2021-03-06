## こんにちはと言う

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
新しいプログラミング言語を学ぶとき、伝統的に「Hello world!」(ハローワールド！)と出力するプログラムを作成します。
</div>
<div>

![テキストと絵文字からなる2行を表示するTrinketの出力領域。](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

[こんにちは 🌍🌎🌏 基本プロジェクト](https://trinket.io/python/a7fcb2ede7){:target="_blank"}を開きます。 Trinketは別のブラウザタブで開きます。

![基本プロジェクトコードを左側のコード領域を表示するTrinketエディター。 右側は空白の出力領域。](images/starter_project.png)

--- /task ---

`#!/bin/python3`という行は、Python 3（Pythonの最新バージョン）を使用していることをコンピュータに伝えます。 `import`行は、自分が書いたのではないコードを使用することをPythonに伝えます。

Pythonでは、 `print()`はテキスト（言葉や数字）を画面に出力します。

`#`で始まる行はコメントで、コードを人間に説明するために書きますが、Pythonは無視します。

--- task ---

`# 動かしたいコードをこの下に書く`の行を探します。

その行の下をクリックします。 点滅する`|`はカーソルで、文字入力する場所を示しています。

こんにちはを表示(`print()`)するコードを入力します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 11
line_highlights: 12
---

#動かしたいコードをこの下に書く
print('こんにちは')

--- /code ---

--- collapse ---
---
title: 英国または米国のキーボードで特殊文字を入力する
---

英国または米国のキーボードでは、左丸括弧`(`および右丸括弧`)` は<kbd>9</kbd>と<kbd>0</kbd>のキーにあります。 左丸括弧を入力するには、（<kbd>Z</kbd>の横にある）<kbd>Shift</kbd>キーを押したまま<kbd>9</kbd>をたたきます。 引用符`'`は<kbd>L</kbd>キーと同じ行の、 <kbd>Enter</kbd>キーの直前にあります。 コンマ`,`は<kbd>M</kbd>の隣にあります。

--- /collapse ---

--- /task ---

--- task ---

**テスト：** **Run**ボタンをクリックしてコードを実行します。 Trinketでは、出力は右側に表示されます。

![出力領域に「こんにちは」と表示されている、強調表示されたRunアイコン。 ](images/run_hello.png)

**デバッグ：**エラーが発生した場合は、コードを注意深く確認してください。 この例では、 `こんにちは`の前後の引用符が抜けているため、Pythonはそれがテキストだということが分かりません。

![引用符が抜け、NameError: name 'Hello' is not defined on line 10 in main.pyのエラーが表示されたTrinketエディター。](images/hello_error.png)

--- /task ---

Pythonでは、**変数**を使用してテキストまたは数値を格納します。 変数は人間がコードを読むのを簡単にしてくれます。 コード内の多くの場所で同じ変数を使用できます。

絵文字を格納する変数をいくつか含めました。

--- task ---

Trinketで、**emoji.py**タブをクリックします。 変数`world`を探してください。「🌍🌍🌍」というテキストが格納されています。

--- /task --- 

--- task ---

一度に複数のアイテムを`print()`するには、アイテムの間にコンマ`,`を入れます。 `print()`は、各アイテムの間にスペースを追加します。

**main.py**タブをクリックして`print()`コードに戻ります。

コードを変更して、変数`world`の内容も`print()`します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 11
line_highlights: 12
---

#動かしたいコードをこの下に書く
print('こんにちは', world)

--- /code ---

**ヒント：**`'こんにちは'`は一重引用符で囲まれているためテキスト文字列ですが、`world` は変数であるため、そこに格納されている値が出力されます。

--- /task ---

--- task ---

**テスト：**コードを実行して、結果を確認します。

![出力領域に「こんにちは」という単語の後に3つの地球の絵文字が表示された、コード領域の更新されたコード行。](images/run_hello_world.png)

絵文字はパソコンによって見た目が異なる場合があるため、まったく同じようには見えない場合があります。

**デバッグ：**`print()`のアイテムの間にコンマを追加していること、`world`のスペルが正しいことを確認してください。

この例では、コンマ`,`がありません。 小さなことですがとても重要です！

![引用符が抜け、'SyntaxError: bad input on line 12 in main.py'のエラーが表示されたTrinketエディター](images/comma_error.png)

--- collapse ---
---
title: 絵文字が表示されません
---

ほとんどのコンピューターでは、カラーの絵文字を使用できます。 ただし、絵文字を使用できない場合は、代わりに「顔文字」を使用できます。これは、絵文字が発明される前に使われていた方法です。

`from emoji import *`行を以下のように変更します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 3
line_highlights: 3
---

from noemoji import *

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

コードに別の行を追加して、ほかのテキストや絵文字を`print()`します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 12
line_highlights: 13
---

print('こんにちは', world)    
print(python, 'へ ようこそ')

--- /code ---

**ヒント：**入力する必要のあるコードは、明るい色で強調表示されています。 強調表示されていないコードを見て、新しいコードを追加する必要がある場所を見つけることができます。

--- /task ---

--- task ---

**テスト：****Run**をクリックします。

![出力領域に「こんにちは」という単語の後に3つの地球の絵文字が表示され、ヘビの絵文字の後に「へ ようこそ」という単語が表示された、コード領域の追加されたコード行。](images/run_multiple.png)

**ヒント：**問題をすばやく修正できるように、変更のたびにコードを実行することをお勧めします。

**デバッグ：**角かっこ、引用符、コンマ、および正しいスペルを注意深く確認します。 Pythonはあなたが本当に正確であることを求めます。

--- /task ---

Trinketアカウントをお持ちの場合は、**Remix**ボタンをクリックして、 `My Trinkets`ライブラリにコピーを保存できます。

Trinketアカウントをお持ちでない場合でも、同じコンピューターでは基本プロジェクトのリンクを使用して、今後プロジェクトに戻ることができます。

--- save ---
