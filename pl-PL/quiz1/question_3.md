--- question ---
---
legend: Question 3 of 3
---

Ta funkcja wyświetla dwie losowe liczby:

--- code ---
---
language: python
---

def two_dice(): print('Pierwsza liczba:', randint(1, 6)) print('Druga liczba:', randint(1, 6))

--- /code ---

Który kod wywoła funkcję, aby go uruchomić?

![Edytor kodu z obszarem wyjściowym pokazującym dwie losowo wygenerowane liczby.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): print('Pierwsza liczba:', randint(1, 6)) print('Druga liczba:', randint(1, 6))

--- /code ---

 --- feedback ---

 Nie, jest to kod definiujący funkcję, ale nie uruchamia funkcji. Będziesz musiał użyć innego kodu, aby go wywołać.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

Zamknij! ` two_dice` to nazwa funkcji, ale aby ją wywołać, potrzebujesz czegoś więcej niż tylko nazwy.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 Nie do końca, pomyśl o typie nawiasów, których użyłaś/eś do wywołania funkcji w swoim projekcie.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 To prawda, użycie nazwy funkcji i nawiasów `(` `)` spowoduje wywołanie funkcji.

 --- /feedback ---

--- /choices ---

--- /question ---
