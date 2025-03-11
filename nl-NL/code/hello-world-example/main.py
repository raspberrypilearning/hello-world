from datetime import datetime
from random import randint

# Emoji-variabelen die je in je project kunt gebruiken
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emoji's om te kopiëren en in je code te plakken:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Nuttige tekens :',()*_/.#


# Functiedefinities
def gooi_dobbelsteen():
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    worp = randint(1, int(max)) # Gebruik max om het aantal zijden van de dobbelsteen te bepalen
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


# Zet de code om uit te voeren hieronder
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

gooi_dobbelsteen() # Roep de dobbelsteen functie aan
print("I ❤️ rainbows 🌈")
print("Unicorns 🦄 make me 😃")
print("I'd like to make a story 📖 with", python)
