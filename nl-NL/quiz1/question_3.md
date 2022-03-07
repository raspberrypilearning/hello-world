--- question ---
---
legend: Vraag 3 van 3
---

Deze functie geeft twee willekeurige getallen:

--- code ---
---
language: python
---

def twee_getallen(): print('Eerste getal: ', randint(1, 6)) print('Tweede getal: ', randint(1, 6))

--- /code ---

Welke code roept de functie aan om uit te voeren?

![De Trinket-editor met uitvoergebied met twee willekeurig gegenereerde nummers.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def twee_getallen(): print('Eerste getal: ', randint(1, 6)) print('Tweede getal: ', randint(1, 6))

--- /code ---

 --- feedback ---

 Nee, dit is de code om de functie te definiëren, maar deze voert de functie niet uit. Je moet andere code gebruiken om de functie aan te roepen.

 --- /feedback ---

- ( ) --- code ---
---
language: python
---

twee_getallen

--- /code ---

 --- feedback ---

Bijna! `twee_getallen` is de naam van de functie, maar om deze aan te roepen heb je meer nodig dan alleen de naam.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

twee_getallen[]

--- /code ---

 --- feedback ---

 Niet helemaal, denk aan het type haakjes dat je moet gebruiken om de functies in je project aan te roepen.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

twee_getallen()

--- /code ---

 --- feedback ---

 Dat klopt, het gebruik van de functienaam gevolgd door `(` `)` haakjes zal de functie aanroepen.

 --- /feedback ---

--- /choices ---

--- /question ---
