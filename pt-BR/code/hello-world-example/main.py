from datetime import datetime
from random import randint

# Variáveis de emoji para usar em seu projeto
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emojis para copiar e colar no seu código:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Caracteres úteis :',()*_/.#


# Definições de função
def rolar_dado():
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    rolar = randint(1, int(maximo)) # Use max para determinar o número de lados que o dado tem
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


# Coloque o código para ser executado logo abaixo
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

rolar_dado() #Chama a função rolar dado
print("I ❤️ rainbows 🌈")
print("Unicorns 🦄 make me 😃")
print("I'd like to make a story 📖 with", python)
