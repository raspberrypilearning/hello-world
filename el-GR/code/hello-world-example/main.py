from datetime import datetime
from random import randint

# Μεταβλητές emoji για χρήση στο έργο σου
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emojis για αντιγραφή και επικόλληση στον κώδικά σου:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Χρήσιμοι χαρακτήρες :',()*_/.#


# Ορισμοί συναρτήσεων
def roll_dice():
    max = input("Πόσες πλευρές έχει το ζάρι σου;:")
    print(f"Αυτό είναι ένα D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire * roll}")


# Βάλε κώδικα για εκτέλεση εδώ
print(f"Γεια σου {world}")
print (f"Καλώς ήρθες στην {python}")
print(f"Η {python} είναι καλή στα μαθηματικά!")
print(f"{3 * 9}")
print(f"Η ημερομηνία και η ώρα είναι {datetime.now()}")

roll_dice() # Κάλεσε τη συνάρτηση για ρίψη ζαριού
print(f"Εγώ❤️ ουράνια τόξα 🌈")
print(f"Οι μονόκεροι🦄 με κάνουν 😃")
print(f"Θα ήθελα να κάνω μια ιστορία 📖 με {python}")
