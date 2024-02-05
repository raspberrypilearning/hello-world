


# Variabili emoji da utilizzare nel tuo progetto
mondo = '🌍🌎🌏'
python = 'Python 🐍'
fuoco = '🔥'

# Emoji da copiare e incollare nel tuo codice:


# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Caratteri utili :',()*_/.#

# Definizione delle funzioni
def tira_dado():
    massimo = input('Quanti lati?:) # Aspetta l'input dell'utente
    print('Questo è un D', massimo) # Usa il numero che l'utente ha inserito
    risultato = randint(1, int(massimo)) # Utilizza il massimo per determinare il numero di lati del dado
    print('Hai tirato un', risultato, fuoco * risultato) # Ripetil l'emoji fuoco tante volte quante il risultato

# Metti qui sotto il codice che verrà eseguito
print('Ciao', mondo)
print('Benvenuti in ', python)
print(python, 'è molto bravo in matematica!')
print(230 * 5782 ** 2 / 23781)  # Stampa il risultato della somma
print('La data e l'ora sono', datetime.now()) # Stampa la data e l'ora corrente

tira_dado() # Chiama la funzione per tirare il dado
print('Io ❤️ gli arcobaleni 🌈')
print('Gli unicorni 🦄 mi rendono 😃')
print('Mi piacerebbe creare una storia 📖 con', python)
