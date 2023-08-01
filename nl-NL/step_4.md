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

![Het uitvoergebied met extra regels om de gebruiker te vragen het grootste getal voor zijn dobbelstenen in te voeren en het antwoord met het willekeurige getal.](images/roll_dice.png){:width="300px"} 

</div>
</div>

In Python **roep** je een **functie()** aan om een actie uit te voeren. Je hebt de functie `print()` al gebruikt om tekst uit te voeren.

Je kunt een nieuwe **functie** **definiëren** om code te groeperen, zodat je deze een naam kunt geven en opnieuw kunt gebruiken.

### Zet de functie definities hier onder

--- task ---

Functies moeten gedefinieerd worden voordat je ze kunt aanroepen. Zoek naar de opmerking bovenaan het tabblad **main.py** met de tekst `#Zet functie definities hier onder`.

Definieer een nieuwe functie genaamd `gooi_dobbelsteen()` die de functie `randint()` gebruikt, uit de `random` bibliotheek, om een willekeurig 'integer' (geheel getal) van 1 tot 6 te genereren en op het scherm uit te tonen.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9-12
---

# Zet hier de functie definities hier onder
def gooi_dobbelsteen(): #Vergeet de dubbele punt aan het einde van deze regel niet   
print(python, 'kan een', dobbelsteen, 'maken')   
print('Je gooit een', randint(1, 6))

--- /code ---

De regels onder `def gooi_dubbelsteen():` zijn **ingesprongen**. Gebruik hiervoor de <kbd>Tab</kbd>-toets op je toetsenbord (meestal boven <kbd>CAPSLOCK</kbd> op het toetsenbord). Inspringende code vertelt Python dat de ingesprongen regels deel uitmaken van de functie.

**Tip:** Het lage streepje `_` wordt gebruikt om woorden in variabele- en functienamen in Python tussen woorden te plaatsen om ze leesbaarder te maken. Je kunt geen spatie gebruiken.

--- collapse ---
---
title: Speciale tekens typen op een Brits of Amerikaans toetsenbord
---

Op een Brits of Amerikaans toetsenbord staat de dubbele punt `:` op dezelfde toets als de puntkomma, naast de <kbd>L</kbd> toets: houd <kbd>Shift</kbd> ingedrukt en tik op <kbd>;</kbd> om een `:` te typen. Het lage streepje `_` staat op dezelfde toets als de `-`, naast de <kbd>0</kbd>, houd <kbd>Shift</kbd> ingedrukt en tik op <kbd>-</kbd> om een `_` te typen.

--- /collapse ---

--- /task ---

--- task ---

**Test:** Als je jouw code nu 'uitvoert' door op Run te klikken, wordt er geen dobbelsteen gegooid. Dat komt omdat je de functie `gooi_dobbelsteen()` wel hebt gedefinieerd, maar nog niet hebt aangeroepen.

**Debug:**

--- collapse ---
---
title: I have a syntax error
---

- **Debuggen:** Zorg dat je een underscore `_` hebt tussen gooi en dobbelsteen om de functienaam te maken.

- Zorg ervoor dat je een dubbele punt `:` aan het einde van de regel hebt staan.

- **Debuggen:** Controleer of de regels onder `def gooi_dobbelsteen()` zijn ingesprongen. Het wordt vaak verkeerd gedaan in Python, dus zorg ervoor dat je het controleert.

![The code editor showing the line of code inside the <code>roll_dice</code> function has not been indented. The line of code with the error is highlighted. De code is uitgevoerd en is gemarkeerd op regel 10, de eerste regel die moet worden ingesprongen, met de fout 'SyntaxError: bad input on line 10 in main.py'." />](images/indent_error.png)

--- /collapse ---

--- /task ---

### Call your function

--- task ---

Om een functie te gebruiken, moet je deze in de code aanroepen. Ga naar het einde van je code en voeg een nieuwe regel toe om de functie `gooi_dobbelsteen()` aan te roepen:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 22
---

print('De', kalendar, klok, 'is', datetime.now())

gooi_dobbelsteen() #Roep de dobbelsteen functie aan

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project meerdere keren uit om elke keer de willekeurige dobbelsteen te zien rollen.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Het gebruik van willekeurige getallen omvat cryptografie, datawetenschap en het toevoegen van variatie in games en computerkunst. Computers genereren <span style="color: #0faeb0">**willekeurige getallen**</span> met behulp van een algoritme. Voor getallen die echt willekeurig zijn, heb je een onvoorspelbare invoer vanuit de echte wereld nodig.
</p>

### Use 🔥🔥🔥 for the number rolled

--- task ---

De variabele `vuur` bevat een 🔥-emoji. De code `print(vuur * 3)` geeft drie vuur-emoji '🔥🔥🔥' weer. Je wilt het aantal emoji's tonen dat gelijk is aan het door de dobbelsteen gegooide getal.

Wijzig je code om de waarde die wordt teruggegeven door `randint()` op te slaan in een variabele met de naam `worp` en gebruik die variabele vervolgens om het gegooide nummer te tonen met het overeenkomende aantal 🔥-emoji's. Use that variable to print out the number rolled with the matching number of 🔥 emojis.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11 - 13
---

# Zet hier de functie definities hier onder
def roll_dice(): roll = randint(1, 6)  # Generate a random number between 1 and 6 and store it in the variable 'roll' print('You rolled a', roll, fire * roll)  # Repeat the fire emoji to match the random dice roll

--- /code ---

Je kunt `ster` of `hart` gebruiken in plaats van `vuur` als je dat liever hebt.

--- /task ---

--- task ---

**Test:** Test je project een paar keer. Zorg ervoor dat je begrijpt hoe de code werkt.

--- /task ---

### Choose the number of sides on the dice

Verbeter je dobbelsteen zodat de gebruiker het maximale getal kan kiezen.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Veel spellen gebruiken veel-kantige dobbelstenen. In de fysieke wereld worden dobbelstenen gemaakt van regelmatige geometrische vormen. Veel voorkomende dobbelstenen zijn D6, D12 en D20. Op een computer kun je een <span style="color: #0faeb0">willekeurig</span> getal genereren om een eerlijke dobbelsteen te maken met een willekeurig aantal kanten.</p>

--- task ---

De functie `input()` stelt de gebruiker een vraag en geeft vervolgens het antwoord terug.

Voeg code toe om de gebruiker om het grootste getal op zijn dobbelsteen te vragen en sla het resultaat vervolgens op in een variabele genaamd `max` en `print` het gekozen nummer in het uitvoergebied:

Verander je `worp` variabele code om `max` te gebruiken als de maximale waarde voor `randint` wanneer het een willekeurig getal genereert.

Wanneer je invoer van een gebruiker krijgt, behandelt Python deze als tekst. Maar `randint` heeft een 'integer' nodig (een positief geheel getal). De functie `int` verandert de gebruikersinvoer in een geheel getal.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Zet de functie definities hier onder

def gooi_dobbelsteen():   
print(python, 'kan een', dobbelsteen, 'maken')   
max = input('Hoeveel kanten?:') #Wacht op input van de gebruiker   
print('Dat is een D ', max) #Gebruik het nummer dat de gebruiker heeft ingevoerd   
worp = randint(1, int(max)) # voor randint  moet max een integer zijn    
print('Je hebt een', worp, 'gegooid')   
print(vuur * worp)

--- /code ---

To print an apostrophe `'` in a word like `That's`, put a backslash `\` before it so Python knows it's part of the text.

--- /task ---

--- task ---

**Test:** Voer je project uit. Wanneer het programma de regel `input` bereikt, wacht het totdat je een antwoord invoert voordat het verder gaat. Type your response and then press <kbd>Enter</kbd>, this will allow the program to collect your response. Probeer het opnieuw met een ander `input` nummer.

--- /task ---

--- save ---
