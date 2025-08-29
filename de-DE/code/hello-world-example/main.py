from datetime import datetime
from random import randint

# Emoji-Variablen zur Verwendung in Deinem Projekt
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emojis zum Kopieren und Einfügen in den Code:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥♻️ 🌳

# Hilfreiche Zeichen:',()*_/.#


# Funktionsdefinitionen
def wuerfel_werfen():
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    wurf = randint(1, int(max))  # Verwende max, um die Anzahl der Seiten des Würfels zu bestimmen
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


# Füge hier den Code ein, der ausgeführt werden soll
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

wuerfel_werfen() # Rufe die Funktion zum Würfel werfen auf
print("I ❤️ rainbows 🌈")
print('Einhörner 🦄 lassen mich 😃")
print("I'd like to make a story 📖 with", python)
