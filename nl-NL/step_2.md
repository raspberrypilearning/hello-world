## Zeg hallo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Het is traditie om een programma te schrijven om 'Hallo wereld!' uit te voeren. wanneer je een nieuwe programmeertaal leert.
</div>
<div>

![Het Trinket-uitvoergebied met de twee afgedrukte regels tekst en emoji.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Open het [Hallo 🌍🌎🌏 startproject](https://trinket.io/python/ac1985a5b8){:target="_blank"}. Trinket wordt geopend in een ander browser tabblad.

![De Trinket-editor met project-startcode aan de linkerkant in het codegebied. Aan de rechterkant is het lege uitvoergebied.](images/starter_project.png)

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

--- collapse ---

---
title: Working on a Raspberry Pi?
---

If you're working on a Raspberry Pi using Chromium, you may not see the emojis. You need to install a font that supports them.

Open a terminal and then type:

```bash
sudo apt install fonts-noto-color-emoji
```

Restart Chromium and you should see the colour emojis.

--- /collapse ---

### from noemoji import *

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Lines beginning with a `#` are <span style="color: #0faeb0">**comments**</span>. They explain what the code will do. Comments are ignored by Python.
</p>

De `import`-regels vertellen Python dat je code gaat gebruiken die je niet zelf hebt geschreven.

In Python voert `print()` tekst (woorden of cijfers) uit naar het scherm.

--- task ---

Zoek de `# Zet de code om uit te voeren hieronder` regel.

Klik onder die regel. De knipperende `|` is de cursor en geeft aan waar je gaat typen.

--- /task ---

--- task ---

Typ de code voor `print()` hallo:

Klik op het tabblad **main.py** om terug te gaan naar jouw `print()`-code.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Zet de code om uit te voeren hier onder
print('Hallo')

--- /code ---

--- collapse ---
---
title: Speciale tekens typen op een Brits of Amerikaans toetsenbord
---

Op een Brits of Amerikaans toetsenbord staan de linker `(` en rechter `)` ronde haakjes op de toetsen <kbd>9</kbd> en <kbd>0</kbd>. Om een linker rond haakje te typen, houdt je de <kbd>Shift</kbd>-toets ingedrukt (naast <kbd>Z</kbd>) en tikt vervolgens op <kbd>9</kbd>. Het enkele aanhalingsteken `'` staat in dezelfde rij als de <kbd>L</kbd> toets, net voor de <kbd>Enter</kbd> toets. De komma `,` staat naast de <kbd>M</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run** om je code uit te voeren. In Trinket verschijnt de uitvoer aan de rechterkant:

![Het pictogram Uitvoeren gemarkeerd met 'Hallo' wordt weergegeven in het uitvoergebied. ](images/run_hello.png)

**Debuggen:** Als je een foutmelding krijgt, controleer dan je code heel goed. In dit voorbeeld ontbreken de enkele aanhalingstekens rond `Hallo` zodat Python niet weet dat het tekst moet zijn.

![de Trinket-editor met ontbrekende enkele aanhalingstekens en fout 'NameError: naam 'Hallo' is niet gedefinieerd op regel 10 in main.py.](images/hello_error.png)

--- /task ---

## Print 🌍🌎🌏

In Python wordt een **-variabele** gebruikt om tekst of getallen op te slaan. Variabelen maken het voor mensen gemakkelijker om code te lezen. Je kunt dezelfde variabele op veel plaatsen in je code gebruiken. Choosing a sensible name for a variable makes it easier for you to remember what it is for.

We hebben enkele variabelen opgenomen die emoji-tekens opslaan.

--- task ---

Klik in Trinket op het tabblad **emoji.py**. Zoek de variabele `wereld`, die de tekst '🌍🌍🌍' opslaat.

--- /task ---

--- task ---

Je kunt met `print()` meer dan één item tegelijk laten zien door een komma `,` tussen de items op te nemen. `print()` voegt een spatie toe tussen elk item.

Verander je `print()` code om ook de inhoud van de `wereld` variabele te tonen:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 3
---

# Zet de code om uit te voeren hier onder
print('Hallo', wereld)

--- /code ---

**Tip:** `'Hallo'` is een tekenreeks omdat er enkele aanhalingstekens omheen staan, terwijl `wereld` een variabele is, zodat de erin opgeslagen waarde wordt getoond.

--- /task ---

--- task ---

**Test:** Voer je code uit om het resultaat te zien:

![De bijgewerkte regel code in het codegebied met het woord 'Hallo' gevolgd door drie emoji-werelden die worden weergegeven in het uitvoergebied.](images/run_hello_world.png)

Emoji kunnen er op verschillende computers anders uitzien, dus de jouwe ziet er misschien niet precies hetzelfde uit.

**Debuggen:** Zorg ervoor dat je een komma hebt toegevoegd tussen de items `print()` en dat je `wereld` correct hebt gespeld.

In dit voorbeeld ontbreekt de komma `,`. Het is klein maar heel belangrijk!

![De Trinket-editor met ontbrekende enkele aanhalingstekens en fout 'SyntaxError: slechte invoer op regel 12 in main.py' weergegeven.](images/comma_error.png)

--- /task ---

--- task ---

Voeg nog een regel toe aan je `print()` code om meer tekst en emoji te maken:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Hallo', wereld)    
print('Welkom bij', python)

--- /code ---

**Tip:** De code die je moet typen, is in een lichtere kleur gemarkeerd. Code die niet gemarkeerd is, helpt je te ontdekken waar je de nieuwe code moet toevoegen.

--- /task ---

--- task ---

**Testen:** Klik op **Run**.

![De extra regel code in het codegebied met het woord 'Hallo' gevolgd door drie emoji-werelden en de woorden 'Welkom bij' gevolgd door een emoji-slang en toetsenbord in het uitvoergebied.](images/run_multiple.png)

**Tip:** Het is een goed idee om je code na elke wijziging uit te voeren, zodat je problemen snel kunt oplossen.

**Debuggen:** Controleer zorgvuldig op haakjes, aanhalingstekens, komma's en correcte spelling. In Python moet je echt nauwkeurig zijn.

--- /task ---

Als je een Trinket-account hebt, kun je op de knop **Remix** klikken om een kopie op te slaan in je `My Trinkets`-bibliotheek.

--- save ---
