from datetime import datetime
from random import randint

# Proměnné emotikonů k použití ve vašem projektu
world = "🌍🌎🌏"
python = "Python 🐍"
oheň = "🔥"

# Emojis ke zkopírování a vložení do kódu:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Užitečné znaky :',()*_/.#


# Definice funkcí
def roll_dice():
    max = input("How many sides on your dice?:")
    print(f"That is a D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Sem vložte kód pro spuštění
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is good at maths!")
print(f"{3 * 9}")
print(f"The date and time is {datetime.now()}")

roll_dice() # Volání funkce hod kostkou
print(f"I ❤️ rainbows 🌈")
print(f"Unicorns 🦄 make me 😃")
print(f"I'd like to make a story 📖 with {python}")
