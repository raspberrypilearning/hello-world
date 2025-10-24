## Imprimir olá

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

Abra o [projeto inicial Olá 🌍🌎🌏 ](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. O Trinket será aberto em outra aba do navegador.

--- /task ---

--- task ---

Find the `# Put code to run under here`{:.language-python} line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 21
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

**Teste:** Clique no botão **Run** para executar seu código.

You should see `Hello` in the Text output area.

--- /task ---

A **variable** is used to store values such as text or numbers. Incluímos algumas variáveis que armazenam caracteres emoji.

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 20
---
# Put code to run under here
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

**Teste:** Execute seu código para ver o resultado:

![A linha de código atualizada na área de código com a palavra 'Olá' seguida por três emojis de mundo exibidos na área de saída.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 20
line_highlights: 22
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

**Teste:** Clique **Run**.

![A linha de código adicional no editor de código com a palavra 'Olá' seguida por três emojis do mundo e as palavras 'Bem-vindo a' seguidas por uma cobra emoji e teclado exibidos na área de saída.](images/run_multiple.png)

**Dica:** É uma boa ideia executar seu código após cada alteração para que você possa corrigir os problemas rapidamente.


--- /task ---


