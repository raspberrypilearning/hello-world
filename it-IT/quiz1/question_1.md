## Quiz veloce

Rispondi alle tre domande. Ci sono alcuni suggerimenti per aiutarti a trovare la risposta corretta.

Dopo aver risposto a ciascuna domanda, fai clic su **Controlla la mia risposta**.

Divertiti!

--- question ---
---
legend: Domanda 1 di 3
---

Questo codice imposta la variabile `world` per contenere il testo '🌍🌎🌏' (le tre differenti emoji del mondo):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

Quale codice utilizza correttamente la variabile `world` e restituisce Hello 🌍🌎🌏?

![L'area di output dell'editor del codice con Hello 🌍🌎🌏 visualizzato.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hello' world)

--- /code ---

 --- feedback ---

 Non proprio, `output` non è il modo di visualizzare i messaggi sullo schermo.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Hello' world)

--- /code ---

 --- feedback ---

 Non proprio, in Python `print` visualizza messaggi sullo schermo, ma in questo esempio manca qualcosa.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Hello', world)

--- /code ---

 --- feedback ---

 Esatto, in Python `print` visualizza messaggi sullo schermo. L' output del testo è racchiuso tra virgolette singole `'` , una virgola separa i due elementi e aggiunge uno spazio, quindi viene richiamata la variabile `world` , che memorizza l'emoji della terra 🌍🌎🌏, come nel tuo progetto.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Hello, world)

--- /code ---

 --- feedback ---

  Non proprio, in Python `print` visualizza messaggi sullo schermo, ma in questo esempio manca qualcosa.

 --- /feedback ---

--- /choices ---

--- /question ---
