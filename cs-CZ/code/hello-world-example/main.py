from datetime import datetime
from random import randint

# Proměnné emotikonů k použití ve vašem projektu
svet = "🌍🌎🌏"
python = "Python 🐍"
ohen = "🔥"

# Emojis ke zkopírování a vložení do kódu:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Užitečné znaky :',()*_/.#


# Definice funkcí
def hod_kostkami():
    max = input("Kolik stran?:") # Počkejte na vstup od uživatele
    print("To je D", max) # Použijte číslo zadané uživatelem
    hod = randint(1, int(max)) # Použijte max k určení počtu stran, které má kostka
    print(
        "Hodil jsi", hod, ohen * hod
    ) # Opakujte emotikon ohně tak, aby odpovídal hodu kostkou


# Sem vložte kód pro spuštění
print("Ahoj", svet)
print("Vítejte", python)
print(python, "je velmi dobrý v matematice!")
print(230 * 5782**2 / 23781) # Tisk výsledku součtu
print("Datum a čas je", datetime.now()) # Vytiskne aktuální datum a čas

hod_kostkami() # Volání funkce hod kostkou
print("Já ❤️ duhy 🌈")
print("Unicorns 🦄 make me 😃")
print("Chtěl bych vytvořit příběh 📖 s", python)
