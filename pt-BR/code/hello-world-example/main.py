from datetime import datetime
from random import randint

# Variáveis de emoji para usar em seu projeto
mundo = '🌍🌎🌏'
python = 'Python 🐍'
fogo = '🔥'

# Emojis para copiar e colar no seu código:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽 🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Caracteres úteis :',()*_/.#

# Definições de função
def rolar_dado():
    maximo = input('Quantos lados?') # Aguarde e entrada do usuário
    print('Esse é um dado D', maximo) # Usa o número que o usuário digitou
    rolar = randint(1, int(maximo)) # Use max para determinar o número de lados que o dado tem
    print('Você rolou um', rolar, fogo * rolar) # Repita o emoji de fogo para combinar com o lançamento dos dados

# Coloque o código para ser executado logo abaixo
print('Olá', mundo)
print('Bem vindo a', python)
print(python, 'é muito bom em matemática!')
print(230 * 5782 ** 2 / 23781) # Imprime o resultado da soma
print('A data e hora são', datetime.now()) # Imprime a data e hora atuais

rolar_dado() #Chama a função rolar dado
print('Eu ❤️ arco-íris 🌈')
print('Unicórnios 🦄 me fazem 😃')
print('Eu gostaria de fazer uma história 📖 com', python)
