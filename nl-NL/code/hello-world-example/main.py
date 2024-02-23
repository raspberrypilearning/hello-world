from datetime import datetime
from random import randint

# Emoji-variabelen die je in je project kunt gebruiken
wereld = '🌍🌎🌏'
python = 'Python 🐍'
vuur = '🔥'

# Emoji's om te kopiëren en in je code te plakken:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Nuttige tekens :',()*_/.#

# Functiedefinities
def gooi_dobbelsteen():
    max = input('Hoeveel zijden?:') # Wacht op invoer van de gebruiker
    print('Dat is een D', max) # Gebruik het getal dat de gebruiker heeft ingevoerd
    worp = randint(1, int(max)) # Gebruik max om het aantal zijden van de dobbelsteen te bepalen
    print('Je hebt een', worp, vuur * worp, 'gegooid') # Herhaal de vuur-emoji zodat deze overeenkomt met de dobbelsteenworp

# Zet de code om uit te voeren hieronder
print('Hallo', wereld)
print('Welkom bij', python)
print(python, 'is erg goed in wiskunde!')
print(230 * 5782 ** 2 / 23781) # Laat het resultaat van de som zien
print('De datum en tijd is', datetime.now()) # Laat de huidige datum en tijd zien

gooi_dobbelsteen() #Roep de dobbelsteen functie aan
print('Ik ❤️ regenbogen 🌈')
print('Eenhoorns 🦄 maken mij 😃')
print('Ik wil graag een verhaal 📖 maken met', python)
