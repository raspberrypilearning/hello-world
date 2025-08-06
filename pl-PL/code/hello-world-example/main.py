from datetime import datetime
from random import randint

# Zmienne emoji do wykorzystania w Twoim projekcie
world = "🌍🌎🌏"
python = "Python 🐍"
fire = "🔥"

# Emoji do skopiowania i wklejenia do kodu:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Przydatne znaki :',()*_/.#


# Definicje funkcji
def roll_dice():
    max = input("Ile boków ma kostka?") #Zaczekaj na odpowiedź użytkownika
    print("Liczba boków kostki to", max) # Użyj liczby, którą wprowadził użytkownik
    roll = randint(1, int(max)) # Użyj max, aby określić liczbę boków kości
    print(
        "Rzuciłaś/eś" roll, fire * roll
    ) Powtórz liczbę fire emoji aby pasowała do wyniku rzutu kością


# Wstaw kod tutaj aby uruchomić
print("Cześć", world)
print("Witaj w", python)
print(python, "jest dobry z matematyki!")
print(230 * 5782**2 / 23781)  # Wyświetl wynik
print("Aktualna data i godzina to", datetime.now())  # Wyświetl aktualną datę i godzinę

roll_dice() # Wywołaj funkcjie rzutu kością
print("Ja ❤️ tęcze 🌈")
print("Jednorożce 🦄 sprawiają, że jestem 😃")
print("Chciałabym/chciałbym stworzyć historię 📖 z" python)
