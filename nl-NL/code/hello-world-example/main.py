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
    worp = randint(1, int(max))
    print(f"Je hebt een {worp} {vuur * worp} gegooid")


# Zet de code om uit te voeren hieronder
print(f"Hallo {wereld}")
print(f"Welkom bij {python}")
print(f"{python} is goed in wiskunde!")
print(f"{3 * 9}")
print(f"De datum en tijd is {datetime.now()}")

gooi_dobbelsteen() # Roep de dobbelsteen functie aan
print(f"Ik ❤️ regenbogen 🌈")
print(f"Eenhoorns 🦄 maken mij 😃")
print(f"Ik wil graag een verhaal 📖 maken met {python}")
