--- question ---
---
legend: Frage 3 von 3
---

Diese Funktion gibt zwei Zufallszahlen aus:

--- code ---
---
language: python
---

def zwei_wuerfel(): print('Erste Zahl:', randint(1, 6)) print('Zweite Zahl:', randint(1, 6))

--- /code ---

Welcher Code ruft die Funktion auf, um sie auszuführen?

![Der Code Editor mit Ausgabebereich, der zwei zufällig generierte Zahlen anzeigt.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def zwei_wuerfel(): print('Erste Zahl:', randint(1, 6)) print('Zweite Zahl:', randint(1, 6))

--- /code ---

 --- feedback ---

 Nein, das ist der Code um die Funktion zu definieren, aber er führt die Funktion nicht aus. Du musst anderen Code verwenden, um sie aufzurufen.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

zwei_wuerfel

--- /code ---

 --- feedback ---

Fast! `zwei_wuerfel` ist der Name der Funktion, aber um sie aufzurufen, braucht man mehr als nur den Namen.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

zwei_wuerfel[]

--- /code ---

 --- feedback ---

 Nicht ganz, denk an die Art von Klammern, die Du zum Aufrufen der Funktionen in Deinem Projekt verwendet hast.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

zwei_wuerfel()

--- /code ---

 --- feedback ---

 Das ist richtig. Wenn Du den Funktionsnamen gefolgt von den Klammern `(` `)` verwendest, wird die Funktion aufgerufen.

 --- /feedback ---

--- /choices ---

--- /question ---
