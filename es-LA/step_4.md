## Roll a dice 🎲

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a function for rolling a dice using random numbers. 
  
In Python:
  - **functions**, defined with `def`, are like 'my blocks' in Scratch,
  - `randint` is like 'random' in Scratch, and
  - `input` is like 'ask' in Scratch.

</div>
<div>

![El área de salida con líneas adicionales para pedirle al usuario que introduzca el mayor número para su dado y la respuesta con el número aleatorio.](images/lanzar_dado.png){:width="300px"} 

</div>
</div>

En Python, puedes **llamar** a una **función()** para realizar una acción. Ya usaste la función `print()` para generar texto.

Puedes **definir** una nueva **función** para agrupar un código con el fin de nombrarlo y volver a usarlo.

### Pon las definiciones de función aquí abajo

--- task ---

Necesitas definir las funciones antes de llamarlas. Busca el comentario cerca de la parte superior de la pestaña **main.py** que dice `#Pon la definición de función aquí abajo`.

Define una nueva función que se llame `lanzar_dado()` que use la función `randint()`, de la biblioteca `random`, para generar un 'entero' (número entero) aleatorio del 1 al 6 y generarlo en la pantalla.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9-12
---

# Pon las definiciones de función aquí abajo
def lanzar_dado(): #No olvides los dos puntos al final de esta línea   
print(python, 'puede crear un', dice)   
print('Lanzaste un', randint(1, 6))

--- /code ---

Las líneas debajo de `def lanzar_dado():` están **indentadas**. Para hacer esto, usa el caracter <kbd>Tab</kbd> de tu teclado (generalmente arriba de <kbd>CAPSLOCK</kbd> en el teclado). El código de identación le dice a Python que las líneas indentadas son parte de la función.

**Tip:** En Python, se usa el guion bajo `_` entre las palabras de los nombres de las variables y funciones para facilitar la lectura. No puedes usar un espacio.

--- collapse ---
---
title: Tipear caracteres especiales en un teclado del Reino Unido o de los Estados Unidos
---

En un teclado del Reino Unido o de los Estados Unidos, los dos puntos `:` están en la misma tecla que el punto y coma, al lado de la tecla <kbd>L</kbd>: mantén presionado <kbd>Shift</kbd> y presiona <kbd>;</kbd> para tipear `:`. El guion bajo `_` está en el mismo teclado que el `-`, al lado del <kbd>0</kbd>, mantén presionado <kbd>Shift</kbd> y presiona <kbd>-</kbd> para tipear `_`.

--- /collapse ---

--- /task ---

--- task ---

**Prueba:** Si tú 'Run' tu código ahora, no lanzará un dado. Esto es porque definiste la función `roll_dice()`, pero aún no la has llamado.

**Debug:**

--- collapse ---
---
title: I have a syntax error
---

- **Debug:** Asegúrate de tener un guion bajo `_` entre lanzar y dice para crear el nombre de la función.

- Asegúrate de tener dos puntos `:` al final de la línea.

- **Debug:** Verifica que las líneas abajo de `def lanzar_dado()` estén indentadas. Es bastante común equivocarse en esto en Python, así que asegúrate de verificar.

![El editor Trinket mostrando las líneas de código para la función@@  The line of code with the error is highlighted. El código se ha ejecutado y está resaltado en la línea 10, la primera línea que debería estar indentada, con el error 'SyntaxError: bad input on line 10 in main.py'."](images/indent_error.png)

--- /collapse ---

--- /task ---

### Call your function

--- task ---

Para usar una función, necesitas llamarla en el código. Ve al final de tu código y añade una nueva línea para llamar a la función `lanzar_dado()`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 22
---

print('La', calendar, clock, 'es', datetime.now())

roll_dice()  # Call the roll dice function

--- /code ---

--- /task ---

--- task ---

**Test:** Ejecuta tu proyecto varias veces para ver lanzar un dado aleatorio.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Los usos de los números aleatorios incluyen la criptografía, la ciencia de datos y la adición de diversidad en los juegos y el arte computacional. Las computadoras generan <span style="color: #0faeb0">**números aleatorios**</span> usando un algoritmo. Para los números realmente aleatorios, necesitas una entrada impredecible del mundo real.
</p>

### Use 🔥🔥🔥 for the number rolled

--- task ---

La variable `fire` almacena un emoji 🔥. El código `print(fire * 3)` genera tres emojis de fuego '🔥🔥🔥'. Necesitas generar el número correcto de emojis para que encaje con el número obtenido.

Cambia tu código para guardar el valor devuelto por `randint()` en una variable llamada `lanzar` y luego usa esa variable para imprimir el número obtenido con el número que corresponde al emoji 🔥. Use that variable to print out the number rolled with the matching number of 🔥 emojis.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11 - 13
---

# Pon las definiciones de función aquí abajo
def lanzar_dado():    
print(python, 'puede crear un', dice)    
lanzar = randint(1, 6) #Generar un número aleatorio entre 1 y 6    
print('Lanzaste un', lanzar) #Imprimir el valor de la variable del tiro      
print(fire * lanzar) #Repite el emoji de fuego para que corresponda al resultado del dado lanzado

--- /code ---

Si prefieres, puedes usar `star` o `heart` en lugar de `fire`.

--- /task ---

--- task ---

**Test:** Prueba tu proyecto un par de veces. Asegúrate de entender cómo funciona el código.

--- /task ---

### Choose the number of sides on the dice

Actualiza tu dado para que el usuario pueda elegir el número máximo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Muchos juegos usan dados de muchas caras. En el mundo físico, los dados se hacen de formas geométricas regulares. Un dado común incluye D6, D12 y D20. En una computadora, puedes generar un número <span style="color: #0faeb0">aleatorio</span> para crear un dado equitativo con cualquier cantidad de caras.</p>

--- task ---

La función `input()` le hace una pregunta al usuario y luego devuelve su respuesta.

Añade un código para pedirle al usuario el mayor número de su dado y guardar el resultado en una variable llamada `max` y `print` el número elegido en el área de salida:

Cambia la variable `lanzar` en tu código para usar `max` como valor máximo para `randint` cuando genera un número aleatorio.

Cuando recives entrada del usuario, Python lo trata como texto. Pero `randint` necesita un 'entero' (un número entero positivo). La función `int` transforma la entrada del usuario en un entero.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Pon las definiciones de función aquí abajo

def lanzar_dado():   
print(python, 'puede crear un', dice)   
max = input('¿Cuántas caras?:') #Esperar la entrada del usuario    
print('Es un D', max) #Usar el número introducido por el usuario    
lanzar = randint(1, 6)    
print('Lanzaste un', lanzar)    
print(fire * lanzar)

--- /code ---

To print an apostrophe `'` in a word like `That's`, put a backslash `\` before it so Python knows it's part of the text.

--- /task ---

--- task ---

**Test:** Ejecuta tu proyecto. Cuando el programa alcanza la línea `input`, esperará a que introduzcas una respueta antes de continuar. Type your response and then press <kbd>Enter</kbd>, this will allow the program to collect your response. Intenta otra vez con un número diferente de `input`.

--- /task ---

--- save ---
