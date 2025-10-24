from datetime import datetime
from random import randint

# Variables Emoji à utiliser dans ton projet
monde = "🌍🌎🌏"
python = "Python 🐍"
feu = "🔥"

# Emojis à copier et coller dans ton code :
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Caractères utiles :',()*_/.#


# Définitions de fonctions
def roule_de():
    max = input("Combien de faces sur ton dé ? :")
    print(f"C'est un D {max}")
    roule = randint(1, int(max))
    print(f"Tu as obtenu un {roule} {feu * roule}")


# Mettre le code à exécuter ci-dessous
print(f"Bonjour {monde}")
print(f"Bienvenue sur {python}")
print(f"{python} est très bon en maths !")
print(f"{3 * 9}")
print(f"La date et l'heure est {datetime.now()}")

roule_de() # Appel la fonction lancer de dés
print(f"J' ❤️ les arcs-en-ciel 🌈")
print(f"Les licornes 🦄 me font 😃")
print(f"J'aimerais créer une histoire 📖 avec {python}")
