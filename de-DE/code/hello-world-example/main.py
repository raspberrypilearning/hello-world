from datetime import datetime
from random import randint

# Emoji-Variablen zur Verwendung in Deinem Projekt
welt = '🌍🌎🌏'
python = 'Python 🐍'
feuer = '🔥'

# Emojis zum Kopieren und Einfügen:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥♻️ 🌳

# Nützliche Zeichen:',()*_/.#

# Funktionsdefinitionen
def würfel_werfen():
    max = input('Wie viele Seiten?:')  # Warte auf Eingabe vom Benutzer
    print('Das ist ein W', max)  # Nutze die Zahl die vom Benutzer eingegeben wurde
    wurf = randint(1, int(max))  # Benutze max als Anzahl Seiten des Würfels
    print('Du hast gewürfelt:', wurf, feuer * wurf) # Wiederhole das Feuer-Emoji so oft wie der Würfelwurf anzeigt

# Hier Code einfügen der ab hier ausgeführt wird
print('Hallo', welt)
print('Willkommen bei', python)
print(python, 'ist sehr gut in Mathe!')
print(230 * 5782 ** 2 / 23781) # Gib das Ergebnis der Rechnung aus
print('Datum und Uhrzeit sind', datetime.now())  # Gib aktuelles Datum und Uhrzeit aus

würfel_werfen() # Rufe die würfeln Funktion auf
print('Ich ❤️ Regenbögen 🌈')
print('Einhörner 🦄 machen mich 😃')
print('Ich möchte eine Geschichte erfinden 📖 mit', Python)
