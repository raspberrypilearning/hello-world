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
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    roll = randint(1, int(max))  # Використай змінну max, щоб вказати кількість сторін кубика
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


# Нижче розмісти код, який потрібно виконати
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

roll_dice()  # Виклич функцію, яка кидає кубик
print("I ❤️ rainbows 🌈")
print("Unicorns 🦄 make me 😃")
print("I'd like to make a story 📖 with", python)
