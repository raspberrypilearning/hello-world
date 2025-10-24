from datetime import datetime
from random import randint

# Emoji-variabelen die je in je project kunt gebruiken
wereld = "🌍🌎🌏"
python = "Python 🐍"
vuur = "🔥"

# Emoji's om te kopiëren en in je code te plakken:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Nuttige tekens :',()*_/.#


# Functiedefinities
def gooi_dobbelsteen():
    max = input("Hoeveel zijden heeft jouw dobbelsteen?:")
    print(f"Dat is een D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Zet de code om uit te voeren hieronder
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is good at maths!")
print(f"{3 * 9}")
print(f"The date and time is {datetime.now()}")

gooi_dobbelsteen() # Roep de dobbelsteen functie aan
print(f"I ❤️ rainbows 🌈")
print(f"Unicorns 🦄 make me 😃")
print(f"I'd like to make a story 📖 with {python}")
