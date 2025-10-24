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
    max = input("How many sides on your dice?:")
    print(f"That is a D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Füge hier den Code ein, der ausgeführt werden soll
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is good at maths!")
print(f"{3 * 9}")
print(f"The date and time is {datetime.now()}")

wuerfel_werfen() # Rufe die Funktion zum Würfel werfen auf
print(f"I ❤️ rainbows 🌈")
print(f"Unicorns 🦄 make me 😃")
print(f"I'd like to make a story 📖 with {python}")
