from datetime import datetime
from random import randint

# Змінні з емоджі для твого проєкту
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Емоджі, які ти можеш скопіювати у свій код:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Корисні символи :',()*_/.#


# Визначення функцій
def roll_dice():
    max = input("How many sides on your dice?:")
    print(f"That is a D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Нижче розмісти код, який потрібно виконати
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is good at maths!")
print(f"{3 * 9}")
print(f"The date and time is {datetime.now()}")

roll_dice()  # Виклич функцію, яка кидає кубик
print(f"I ❤️ rainbows 🌈")
print(f"Unicorns 🦄 make me 😃")
print(f"I'd like to make a story 📖 with {python}")
