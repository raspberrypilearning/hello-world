## Examen rapido

Responde las siguientes tres preguntas para reflexionar sobre lo que has aprendido. Hay pistas para guiarte hacia la respuesta correcta.

Cuando hayas respondido a cada pregunta, haz clic en **Revisar mi respuesta**.

¡Qué te diviertas!

--- question ---
---
legend: Question 1 of 3
---

Este código configura la variable `mundo` para que contenga el texto '🌍🌎🌏' (tres diferentes emojis de mundo):

--- code ---
---
language: python
---

mundo = '🌍🌎🌏'

--- /code ---

¿Qué código usa correctamente la variable `mundo` y muestra Hola 🌍🌎🌏?

![El área de salida del editor Trinket mostrando Hola 🌍🌎🌏.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hola' mundo)

--- /code ---

 --- feedback ---

 No del todo, `output` no es la forma de generar mensajes en la pantalla.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Hello world')

--- /code ---

 --- feedback ---

 No del todo, en Python `print` genera mensajes en la pantalla, pero en este ejemplo falta algo.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hello{world}')

--- /code ---

 --- feedback ---

 Correcto, en Python `print` genera mensajes en la pantalla. The text output is inside single quotes `'` , then the `world` variable contains the earth emoji 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello{world}')

--- /code ---

 --- feedback ---

  No del todo, en Python `print` genera mensajes en la pantalla, pero en este ejemplo falta algo.

 --- /feedback ---

--- /choices ---

--- /question ---
