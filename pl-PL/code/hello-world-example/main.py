from datetime import datetime
from random import randint

# Zmienne emoji do wykorzystania w Twoim projekcie
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emoji do skopiowania i wklejenia do kodu:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Przydatne znaki :',()*_/.#


# Definicje funkcji
def roll_dice():
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    Rzuć = randint(1, int(max)) # Użyj max, aby określić liczbę boków kości
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


# Wstaw kod do uruchomienia tutaj
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

Roll_dice() # Wywoływanie funkcji kości rzutu
print("I ❤️ rainbows 🌈")
print("Unicorns 🦄 make me 😃")
print("I'd like to make a story 📖 with", python)
