--- question ---
---
legend: Pregunta 3 de 3
---

Esta función genera dos números aleatorios:

--- code ---
---
language: python
---

def dos_dados(): 
  print('Primer número:', randint(1, 6)) 
  print('Segundo número:', randint(1, 6))

--- /code ---

¿Qué código llamará a la función para ejecutarla?

![El editor Trinket y el área de salida mostrando dos números generados aleatoriamente.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def dos_dados(): 
  print('Primer número:', randint(1, 6)) 
  print('Segundo número:', randint(1, 6))

--- /code ---

 --- feedback ---

 No, este código es para definir la función, pero no ejecuta la función. Necesitarás usar un código diferente para llamarla.

 --- /feedback ---

- ( )
--- code ---
---
language: python
---

dos_dados

--- /code ---

 --- feedback ---

¡Casi! `dos_dados` es el nombre de la función, pero para llamarla vas a necesitar más que el nombre.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

dos_dados[]

--- /code ---

 --- feedback ---

 No del todo, piensa en el tipo de paréntesis que usaste para llamar a las funciones en tu proyecto.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

dos_dados()

--- /code ---

 --- feedback ---

 Correcto, usar el nombre de función seguido de los paréntesis `(` `)` llamará a la función.

 --- /feedback ---

--- /choices ---

--- /question ---
