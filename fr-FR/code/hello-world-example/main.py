from datetime import datetime
from random import randint

# Variables Emoji à utiliser dans ton projet
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emojis à copier et coller dans ton code :
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Caractères utiles :',()*_/.#


# Définitions de fonctions
def roule_de():
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    rouler = randint(1, int(max)) # Utiliser max pour déterminer le nombre de faces du dé
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


# Mettre le code à exécuter ci-dessous
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

roule_de() # Appel la fonction lancer de dés
print("I ❤️ rainbows 🌈")
print("Unicorns 🦄 make me 😃")
print("I'd like to make a story 📖 with", python)
