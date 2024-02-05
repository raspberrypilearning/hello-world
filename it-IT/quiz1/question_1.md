## Quiz veloce

Rispondi alle tre domande. Ci sono alcuni suggerimenti per aiutarti a trovare la risposta corretta.

Dopo aver risposto a ciascuna domanda, fai clic su **Controlla la mia risposta**.

Divertiti!

--- question ---
---
legend: Domanda 1 di 3
---

Questo codice imposta la variabile `mondo` per contenere il testo '🌍🌎🌏' (le tre differenti emoji del mondo):

--- code ---
---
language: python
---

mondo = '🌍🌎🌏'

--- /code ---

Quale codice utilizza correttamente la variabile `mondo` e restituisce Ciao 🌍🌎🌏?

![L'area di output dell'editor del codice con Ciao 🌍🌎🌏 visualizzato.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Ciao' mondo)

--- /code ---

 --- feedback ---

 Non proprio, `output` non è il modo di visualizzare i messaggi sullo schermo.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Ciao' mondo)

--- /code ---

 --- feedback ---

 Non proprio, in Python `print` visualizza messaggi sullo schermo, ma in questo esempio manca qualcosa.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Ciao', mondo)

--- /code ---

 --- feedback ---

 Esatto, in Python `print` visualizza messaggi sullo schermo. L' output del testo è racchiuso tra virgolette singole `'` , una virgola separa i due elementi e aggiunge uno spazio, quindi viene richiamata la variabile `mondo` , che memorizza l'emoji della terra 🌍🌎🌏, come nel tuo progetto.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Ciao, mondo)

--- /code ---

 --- feedback ---

  Non proprio, in Python `print` visualizza messaggi sullo schermo, ma in questo esempio manca qualcosa.

 --- /feedback ---

--- /choices ---

--- /question ---
