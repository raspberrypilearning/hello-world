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
    max = input('Combien de faces ? :') # Attendre la saisie de l'utilisateur
    print("C\'est un D", max) # Utiliser le nombre entré par l'utilisateur
    rouler = randint(1, int(max)) # Utiliser max pour déterminer le nombre de faces du dé
    print(
        "Tu as obtenu un", roule, feu * roule
    )  # Répéter l'emoji de feu pour correspondre au lancer de dés


# Mettre le code à exécuter ci-dessous
print("Bonjour", monde)
print("Bienvenue sur", python)
print(python, "est très bon en maths !")
print(230 * 5782**2 / 23781) # Imprimer le résultat du calcul
print("La date et l\'heure sont", datetime.now()) # Imprimer la date et l'heure actuelles

roule_de() # Appel la fonction lancer de dés
print("J\' ❤️ les arcs-en-ciel 🌈")
print("Les licornes 🦄 me font 😃")
print("J\'aimerais créer une histoire 📖 avec", python)
