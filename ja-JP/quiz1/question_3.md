--- question ---
---
legend: 質問3/3
---

この関数は、2つの乱数を出力します。

--- code ---
---
language: python
---

def two_dice(): print('最初の数字:', randint(1, 6)) print('2番目の数字:', randint(1, 6))

--- /code ---

関数を呼び出して実行するコードはどれですか？

![ランダムに生成された2つの数値を出力領域に表示したTrinketエディター。](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): print('最初の数字:', randint(1, 6)) print('2番目の数字:', randint(1, 6))

--- /code ---

 --- feedback ---

 いいえ、これは関数を定義するためのコードですが、関数を実行しません。 それを呼び出すには、別のコードを使用する必要があります。

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

惜しい！ `two_dice`は関数の名前ですが、それを呼び出すには、名前だけでは不十分です。

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 残念。プロジェクトで関数を呼び出すために使用した、かっこの種類について考えてみてください。

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 正解です。関数名の後に`(` `)`のかっこを使用して関数を呼び出します。

 --- /feedback ---

--- /choices ---

--- /question ---
