## Drukuj cześć

In Python, `print()`{:.language-python} outputs strings (words or numbers) to the screen.

--- task ---

Otwórz [ Cześć ??? projekt startowy ](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. Edytor kodu otworzy się w innej karcie przeglądarki.

![The code editor with project starter code on the left in the code area. On the right is the blank output area.](images/starter_project.png)

--- /task ---

--- task ---

Find the `# Put code to run below here`{:.language-python} line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()`{:.language-python} Hello to the screen:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18
---
# Put code to run under here.
print(f'Hello')

--- /code ---

--- /task ---

--- task ---

** Test:** Kliknij przycisk ** **, aby uruchomić swój kod. This is what you should see when you run your code:

![Ikona Uruchom podświetlona, a w obszarze wyjściowym wyświetlany jest komunikat „Cześć”. ](images/run_hello.png)

--- /task ---

A **variable** is used to store values such as text or numbers. Dodaliśmy kilka zmiennych, które przechowują znaki emoji.

--- task ---

Change your code to also `print()`{:.language-python} the contents of the `world`{:.language-python} variable. You can do this by adding the variable name in curly brackets `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 17
---
# Umieść tutaj kod do uruchomienia
print(f'Hello {world}')

--- /code ---

The `f`{:.language-python} character inside the print lets you easily print variables along with strings of text.

--- /task ---

--- task ---

** Test:** Uruchom swój kod, aby zobaczyć wynik:

![Zaktualizowana linia kodu w obszarze kodu ze słowem „Hello”, a następnie trzema emotikonami świata wyświetlanymi w obszarze wyjściowym.](images/run_hello_world.png)

--- /task ---

--- task ---

**Add** another line to your code to `print()`{:.language-python} more text and emojis:

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}')

--- /code ---

--- /task ---

--- task ---

Test **:** Kliknij ** **.

![Dodatkowa linia kodu w edytorze kodu ze słowem „Hello”, po którym znajdują się trzy emoji świata i słowa „Welcome to”, a następnie wąż emoji i klawiatura wyświetlane w obszarze wyjściowym.](images/run_multiple.png)

** Wskazówka:** dobrze jest uruchomić kod po każdej zmianie, aby szybko rozwiązać problemy.


--- /task ---


