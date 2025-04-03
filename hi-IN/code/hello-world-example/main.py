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


# फ़ंक्शन परिभाषाएँ
डीईएफ़ रोल_डाइस():
    max = input("How many sides?:")  # Wait for input from the user
    print("That's a D", max)  # Use the number the user entered
    रोल = रैंडिंट(1, int(max)) # पासे की भुजाओं की संख्या निर्धारित करने के लिए max का उपयोग करें
    print(
        "You rolled a", roll, fire * roll
    )  # Repeat the fire emoji to match the dice roll


यहां चलाने के लिए कोड डालें
print("Hello", world)
print("Welcome to", python)
print(python, "is very good at maths!")
print(230 * 5782**2 / 23781)  # Print the result of the sum
print("The date and time is", datetime.now())  # Print the current date and time

रोल_डाइस() # रोल पासा फ़ंक्शन को कॉल करें
print("I ❤️ rainbows 🌈")
print("Unicorns 🦄 make me 😃")
print("I'd like to make a story 📖 with", python)
