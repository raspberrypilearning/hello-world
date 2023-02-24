## Reflexión

Responde las siguientes tres preguntas para reflexionar sobre lo que has aprendido. There are hints to guide you to the correct answer.

Después de cada pregunta, presiona **enviar**. Vamos a guiarte hacia la respuesta correcta.

¡Qué te diviertas!

--- question ---
---
legend: Pregunta 1 de 3
---

¡Qué te diviertas!

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
