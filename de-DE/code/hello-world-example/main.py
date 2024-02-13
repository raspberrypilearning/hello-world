from datetime import datetime
from random import randint

# Emoji-Variablen zur Verwendung in Deinem Projekt
welt = '🌍🌎🌏'
python = 'Python 🐍'
feuer = '🔥'

# Emojis zum Kopieren und Einfügen in den Code:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥♻️ 🌳

# Hilfreiche Zeichen:',()*_/.#

# Funktionsdefinitionen
def wuerfel_werfen():
    max = input('Wie viele Seiten?:')  # Warte auf Eingabe vom Benutzer
    print('Das ist ein W', max)  # Verwende die vom Benutzer eingegebene Zahl
    wurf = randint(1, int(max))  # Verwende max, um die Anzahl der Seiten des Würfels zu bestimmen
    print('Du hast gewürfelt:', wurf, feuer * wurf) # Wiederhole das Feuer-Emoji so oft wie der Würfelwurf anzeigt

# Füge hier den Code ein, der ausgeführt werden soll
print('Hallo', welt)
print('Willkommen bei', python)
print(python, 'ist sehr gut in Mathe!')
print(230 * 5782 ** 2 / 23781) # Gib das Ergebnis der Rechnung aus
print('Datum und Uhrzeit sind', datetime.now())  # Gib aktuelles Datum und Uhrzeit aus

wuerfel_werfen() # Rufe die Funktion zum Würfel werfen auf
print('Ich ❤️ Regenbögen 🌈')
print('Einhörner 🦄 machen mich 😃')
print('Ich möchte eine Geschichte erfinden 📖 mit', Python)
