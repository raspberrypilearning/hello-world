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
    max = input("How many sides on your dice?:")
    print(f"That is a D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Coloque o código para ser executado logo abaixo
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is good at maths!")
print(f"{3 * 9}")
print(f"The date and time is {datetime.now()}")

rolar_dado() #Chama a função rolar dado
print(f"I ❤️ rainbows 🌈")
print(f"Unicorns 🦄 make me 😃")
print(f"I'd like to make a story 📖 with {python}")
