## Gooi een dobbelsteen 🎲

Functies zijn codeblokken die specifieke taken uitvoeren. Ze kunnen steeds opnieuw gebruikt worden.

Hier is een voorbeeld van een functie:

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one(): x = 1 + 1 print(x)

--- /code ---

De naam van deze functie is `tel_een_en_een_op`{:.language-python}.

De code voor de taak die je wil dat de functie uitvoert, moet **ingesprongen zijn**, wat betekent dat je **vier spaties** moet toevoegen vóór elke regel code.

Door een functie **aan te roepen**, wordt de code erbinnen uitgevoerd. Het **aanroepen** van een functie doe je door de naam in te typen. In dit geval `tel_een_en_een_op()`{:.language-python}.


--- task ---

Vind de opmerking in het bestand **main.py** waarin staat

`# Functiedefinities`{:.language-python}.

Maak een functie genaamd `gooi_dobbelsteen()`{:.language-python}, die het getal 4 afdrukt.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18-20
---
# Function definitions
def roll_dice(): print(f'You rolled a {4}')

# Put code to run under here

--- /code ---

--- /task ---

--- task ---

Roep vervolgens de functie onderaan je code aan.

--- code ---
---
language: python line_numbers: true line_number_start: 26
line_highlights: 27
---
print(f'The date and time is {datetime.now()}') roll_dice()

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project meerdere keren uit en kijk elke keer hoe de dobbelstenen rollen - de uitkomst zal altijd 4 zijn.

--- /task ---

--- task ---

Een andere module, genaamd `random`{:.language-python}, kan worden gebruikt om willekeurige getallen te creëren. Wijzig je code om de functie `randint`{:.language-python} te gebruiken om een willekeurig getal tussen 1 en 6 te kiezen voor de dobbelsteenworp.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Function definitions
def roll_dice(): print(f'You rolled a {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Wanneer je nu je code nog eens uitvoert, zal er elke keer een nieuw willekeurig getal tussen 1 en 6 worden gekozen.

--- /task ---

In Python kun je strings zoals emoji's of hele woorden vermenigvuldigen met een getal, zodat ze meerdere keren worden geprint.

--- task ---

Wijzig je functie om het willekeurige getal op te slaan in een variabele met de naam `worp`{:.language-python}.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Function definitions
def roll_dice(): roll = randint(1,6)

--- /code ---

--- /task ---

--- task ---

Vermenigvuldig het willekeurige getal opgeslagen in `worp`{:.language-python} met de 🔥 emoji en druk het resultaat af.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 20
---
# Function definitions
def roll_dice(): roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Je uitvoer zou er ongeveer zo uit moeten zien:

```
Hallo 🌍🌎🌏
Welkom bij Python 🐍
Python 🐍 is goed in wiskunde!
27
De datum en tijd is 2025-10-24 12:41:45.140000
Je hebt een 4 gegooid 🔥🔥🔥🔥
```

--- /task ---