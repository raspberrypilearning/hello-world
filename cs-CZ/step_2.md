## Napiš ahoj

Pomocí funkce `print()`{:.language-python} vypíšeš na obrazovku řetězce (slova nebo čísla).

--- task ---

Otevři [úvodní projekt výzvy Mission Zero](https://missions.astro-pi.org/cs/mz/code_submissions/new){:target="_blank"}. Editor kódu se otevře v nové záložce prohlížeče.

![Editor kódu se spouštěcím kódem projektu vlevo v oblasti kódu. Vpravo je prázdná výstupní oblast.](images/starter_project.png)

--- /task ---

--- task ---

Zde najdete řádek `# Sem vložte kód ke spuštění`{:.language-python}.

Klikněte pod tímto řádkem. Blikající `|` je kurzor a ukazuje, kam budete psát.

--- /task ---

--- task ---

Napište kód pro funkci`print()`{:.language-python}, která vypíše Ahoj na obrazovku:

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

**Test:** Kliknutím na tlačítko **Run** spustíš svůj kód. Toto bys měl vidět při spuštění kódu:

![Ikona Run zvýrazněná s 'Hello' zobrazeným ve výstupní oblasti. ](images/run_hello.png)

--- /task ---

**Proměnná** se používá k uložení hodnot, jako je text nebo čísla. Zahrnuli jsme některé proměnné, které ukládají emoji znaky.

--- task ---

Změňte svůj kód a také funkci`print()`{:.language-python} včetně obsahu proměnné `world`{:.language-python}. Můžete to udělat přidáním názvu proměnné do složených závorek `{}`{:.language-python}


--- code ---
---
language: python line_numbers: true
line_number_start: 17
---
# Put code to run under here
print(f'Hello {world}')

--- /code ---

Znak `f`{:.language-python} uvnitř tisku umožňuje snadno tisknout proměnné spolu s řetězci textu, tzv. f-string.

--- /task ---

--- task ---

**Test:** Spusťte svůj kód a uvidíte výsledek:

![Aktualizovaný řádek kódu v oblasti kódu se slovem „Ahoj“ následovaným třemi světovými emotikony zobrazenými ve výstupní oblasti.](images/run_hello_world.png)

--- /task ---

--- task ---

**Přidejte do svého kódu** další řádek `print()`{:.language-python}, který vitiskne další text a emotikony:

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

**Test:** Klikni na tlačítko **Run**.

![Dodatečný řádek kódu v editoru kódu se slovem „Ahoj“ následovaným třemi světovými emotikony a slovy „Vítejte“ následovaným hadem emoji a klávesnicí zobrazenou ve výstupní oblasti.](images/run_multiple.png)

**Tip:** Je dobrý nápad spustit kód po každé změně, abyste mohli rychle opravit problémy.


--- /task ---


