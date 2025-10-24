from datetime import datetime
from random import randint

# Emoji variables to use in your project
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emojis to copy and paste into your code:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Useful characters :',()*_/.#


# Function definitions
def roll_dice():
    max = input("How many sides on your dice?:")
    print(f"That is a D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Put code to run under here
print(f"Hello {world}")
print(f"Welcome to {python}")
print(f"{python} is good at maths!")
print(f"{3 * 9}")
print(f"The date and time is {datetime.now()}")

roll_dice()  # Call the roll dice function
print(f"I ❤️ rainbows 🌈")
print(f"Unicorns 🦄 make me 😃")
print(f"I'd like to make a story 📖 with {python}")
