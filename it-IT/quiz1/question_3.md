--- question ---
---
legend: Domanda 3 di 3
---

Questa funzione restituisce due numeri casuali:

--- code ---
---
language: python
---

def due_dadi():
  print('Primo numero:', randint(1, 6))
  print('Secondo numero:', randint(1, 6))

--- /code ---

Quale codice richiamerà la funzione per eseguirla?

![L'editor di codice con l'area di output che mostra due numeri generati casualmente.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def due_dadi():
  print('Primo numero:', randint(1, 6))
  print('Secondo numero:', randint(1, 6))

--- /code ---

 --- feedback ---

 No, questo è il codice per definire la funzione, ma non esegue la funzione. Dovrai utilizzare un codice diverso per chiamarlo.

 --- /feedback ---

- ( )
--- code ---
---
language: python
---

due_dadi

--- /code ---

 --- feedback ---

Vicino! `due_dadi` è il nome della funzione, ma per chiamarla è necessario qualcosa di più del semplice nome.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

due_dadi[]

--- /code ---

 --- feedback ---

 Non proprio, pensa al tipo di parentesi che hai usato per chiamare le funzioni nel tuo progetto.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

due_dadi()

--- /code ---

 --- feedback ---

 Esatto, l'utilizzo del nome della funzione seguito dalle parentesi `(` `)` chiamerà la funzione.

 --- /feedback ---

--- /choices ---

--- /question ---
