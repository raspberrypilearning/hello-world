## Reflexión

Bien hecho, has creado un programa interactivo con texto y emoji 👍

Ahora es momento de reflexionar: esta es una parte importante del aprendizaje porque te ayuda a establecer nuevas conexiones en tu cerebro.

Responde las siguientes tres preguntas para reflexionar sobre lo que has aprendido.

Después de cada pregunta, presiona **enviar**. Vamos a guiarte hacia la respuesta correcta. Puedes realizar esta actividad tantas veces como quieras.

¡Qué te diviertas!

--- question ---
---
legend: Pregunta 1 de 3
---

Este código configura la variable `world` para que contenga el texto '🌍🌎🌏' (tres diferentes emojis de mundo):

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

¿Qué código usa correctamente la variable `world` y muestra Hola 🌍🌎🌏?

![El área de salida del editor Trinket mostrando Hola 🌍🌎🌏.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hola' world)

--- /code ---

 --- feedback ---

 No del todo, `output` no es la forma de generar mensajes en la pantalla.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Hola' world)

--- /code ---

 --- feedback ---

 No del todo, en Python `print` genera mensajes en la pantalla, pero en este ejemplo falta algo.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Hola', world)

--- /code ---

 --- feedback ---

 Correcto, en Python `print` genera mensajes en la pantalla. El texto de salida está entre comillas simples `'` , la coma separa dos objetos y proporciona espacio, luego llamamos a la variable `world`, que almacena el emoji 🌍🌎🌏, como aparece en tu proyecto.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Hola, world)

--- /code ---

 --- feedback ---

  No del todo, en Python `print` genera mensajes en la pantalla, pero en este ejemplo falta algo.

 --- /feedback ---

--- /choices ---

--- /question ---
