#!/bin/python3

from emoji import * 
from datetime import *
from random import randint

#関数の定義をこの下に書く

def roll_dice():
  print(python, 'で', dice, 'を作ることができます')
  max = input('何面にしますか?') # ユーザーに入力してもらう
  print(max, '面ですね') # ユーザーが入力した数値を使う
  roll = randint(1, int(max)) # ランダムな数値を生成する 
  print('サイコロの目はこれでした', roll) # 変数rollの値を出力する
  print(fire * roll) # サイコロの目の回数だけ炎の文字を繰り返し出力する

def hobbies():
  hobby = input('あなたは何に興味がありますか?')
  print('それはとても', fun, 'そうですね')
  print('あなたは', hobby, 'に関する', python, 'プロジェクトを作ることができます')

# 使える文字 :',()*_/.#

# 動かしたいコードをこの下に書く
print('こんにちは', world)
print(python, 'へ ようこそ')

input() # ユーザーがEnterを たたくのを待つ

print(python, 'は', sums, 'が得意です')
print(230 * 5782 ** 2 / 23781)

input()

print(calendar, clock, 'は', datetime.now()) # 現在の日付と時刻を絵文字と一緒に出力 

input()

roll_dice() # roll_dice関数を呼び出す

input()

hobbies() # hobbies関数を呼び出す




