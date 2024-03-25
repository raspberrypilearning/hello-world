## Wirf einen Würfel 🎲

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Erstelle eine Funktion zum Würfeln mithilfe von Zufallszahlen. 
  
In Python:
  - sind **Funktionen**, definiert durch `def`, wie „Meine Blöcke“ in Scratch,
  - `randint` ist wie 'Zufallszahl' in Scratch, und
  - `input` ist wie 'Frage' in Scratch.

</div>
<div>

![Der Textausgabebereich mit zusätzlichen Zeilen, um den Benutzer aufzufordern, die größte Zahl für seine Würfel einzugeben, und die Antwort mit der Zufallszahl.](images/roll_dice.png){:width="300px"} 

</div>
</div>

In Python kannst Du eine **funktion()** **aufrufen**, um eine Aktion auszuführen. Du hast bereits die Funktion `print()` zum Ausgeben von Text verwendet.

Du kannst eine neue **Funktion** **definieren**, um Code zu gruppieren, sodass Du ihn benennen und wiederverwenden kannst.

### Definiere Deine Funktion

--- task ---

Funktionen müssen definiert werden, bevor Du sie aufrufen kannst. Finde in der Datei **main.py** den Kommentar `# Funktionsdefinitionen`.

Definiere eine neue Funktion namens `wuerfel_werfen()`, welche die Funktion `randint()` aus der Bibliothek `random` verwendet, um eine zufällige ganze Zahl (engl.: „integer“) von 1 bis 6 zu erzeugen und auf dem Bildschirm auszugeben.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 15
line_highlights: 16-17
---

# Funktionsdefinitionen
def wuerfel_werfen(): # Vergiss nicht den Doppelpunkt am Ende dieser Zeile   
print('Das hast Du gewürfelt:', randint(1, 6)) # randint(1, 6) wird verwendet, um eine Zahl zwischen 1 und 6 zu erzeugen.

--- /code ---

Die Zeile unter `def wuerfel_werfen():` ist **eingerückt**. Verwende dazu die <kbd>Tab</kbd> Taste auf Deiner Tastatur (normalerweise über der <kbd>Feststelltaste</kbd> auf der Tastatur). Durch das Einrücken von Code wird Python mitgeteilt, dass die eingerückten Zeilen Teil der Funktion sind.

**Tipp:** Der Unterstrich `_` wird in Python zwischen Wörtern in Variablen- und Funktionsnamen verwendet, um sie leichter lesbar zu machen. Leerzeichen darfst Du dafür nicht verwenden.

--- collapse ---
---
title: Sonderzeichen auf einer deutschen Tastatur eingeben
---

On a UK or US keyboard, the colon `:` is on the same key as the semicolon, next to the <kbd>L</kbd> key: hold <kbd>Shift</kbd> and tap <kbd>;</kbd> to type a `:`. Der Unterstrich `_` ist auf der gleichen Taste wie `-`, neben der rechten <kbd>Umschalttaste</kbd>. Halte <kbd>Umschalten</kbd> gedrückt und tippe <kbd>-</kbd> um ein `_` zu schreiben.

--- /collapse ---

--- /task ---

--- task ---

**Test:** Wenn Du jetzt Deinen Code ausführst, wird nicht gewürfelt. Das liegt daran, dass Du Deine Funktion `wuerfel_werfen()` zwar definiert hast, sie aber noch nicht aufgerufen hast.

**Fehlersuche:**

--- collapse ---
---
title: Ich habe einen Syntaxfehler
---

- Achte darauf, dass im Funktionsnamen zwischen „wuerfel“ und „werfen“ ein Unterstrich `_` steht.

- Achte darauf, dass am Ende der Zeile ein Doppelpunkt `:` steht.

- Überprüfe, ob die Zeile unter `def wuerfel_werfen():` eingerückt ist. Das ist ein wirklich häufig gemachter Fehler in Python. Sieh also nochmal nach.

![Der Code Editor, der die nicht eingerückte Codezeile innerhalb der Funktion <code>wuerfel_werfen</code> anzeigt. Die Codezeile mit dem Fehler wird hervorgehoben. The code has been run, with the error 'SyntaxError: bad input on line 17 in main.py'.](images/indent_error.png)

--- /collapse ---

--- /task ---

### Ruf Deine Funktion auf

--- task ---

Um eine Funktion zu verwenden, musst Du sie im Code **aufrufen**. Geh bis zum Ende Deines Codes und füge eine neue Zeile hinzu, um die Funktion `wuerfel_werfen()` aufzurufen:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 25
line_highlights: 27
---

print('Datum und die Uhrzeit sind', datetime.now())

wuerfel_werfen() # Rufe die würfeln Funktion auf

--- /code ---

--- /task ---

--- task ---

**Test:** Führe Dein Projekt mehrmals aus, um zufällige Würfelwürfe zu sehen.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Zu den Einsatzmöglichkeiten von Zufallszahlen gehören Kryptographie, Datenwissenschaft und um Abwechslung in Spielen und Computerkunst zu erzeugen. Computer erzeugen mithilfe eines Algorithmus <span style="color: #0faeb0">**Zufallszahlen**</span>. Für Zahlen, die wirklich zufällig sind, benötigst Du eine unvorhersehbare Eingabe aus der realen Welt.
</p>

### Verwende 🔥🔥🔥 für die gewürfelte Zahl

--- task ---

Deine Funktion kann die Emoji-Variable 🔥 verwenden. Der Code `print(feuer * 3)` gibt drei Feuer-Emojis „🔥🔥🔥“ aus. Du musst die richtige Anzahl an Emojis ausgeben, um gewürfelten Zufallszahl zu entsprechen.

Ändere Deinen Code, um den von `randint()` zurückgegebenen Wert in einer Variablen namens `wurf` zu speichern. Verwende diese Variable, um die gewürfelte Zahl mit der entsprechenden Anzahl an 🔥-Emojis auszudrucken.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 15
line_highlights: 17-18
---

# Funktionsdefinitionen
def wuerfel_werfen(): wurf = randint(1, 6) # Erzeuge eine Zufallszahl zwischen 1 und 6 und speichere sie in der Variable 'wurf' print('Das hast Du gewürfelt:', wurf, feuer * wurf) # Wiederhole das Feuer-Emoji so oft wie es der gewürfelten Zahl entspricht

--- /code ---

**Tipp** Erstelle Deine eigenen Emoji Variablen `stern` oder `herz` und nutze diese anstelle von `feuer`.

--- /task ---

--- task ---

**Test:** Teste Dein Projekt ein paar Mal. Achte darauf, dass Du verstehst, wie der Code funktioniert.

--- /task ---

### Wähle die Anzahl der Würfelseiten

Werte Deinen Würfel auf, sodass der Benutzer die maximale Anzahl auswählen kann.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Viele Spiele verwenden Würfel mit vielen Seiten. In der echten Welt bestehen Würfel aus regelmäßigen geometrischen Formen. Zu den üblichen Würfeln gehören W6, W12 und W20. Auf einem Computer kannst Du eine <span style="color: #0faeb0">Zufallszahl</span> generieren, um einen fairen Würfel mit beliebig vielen Seiten zu erstellen.</p>

--- task ---

Die Funktion `input()` stellt dem Benutzer eine Frage und gibt dann seine Antwort zurück.

**Add** code to ask the user for the biggest number on their dice and then save the result in a variable called `max` and `print` the number chosen into the output area:

Change your `roll` variable code to use `max` as the maximum value for `randint` when it generates a random number.

When you get input from the user, Python treats it as text. But, `randint` needs an 'integer' (a positive whole number). The `int` function turns the user input into an integer.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 15
line_highlights: 18-20
---

# Function definitions

def roll_dice():   
max = input('How many sides?:')  # Wait for input from the user    
print('That\'s a D', max)  # Use the number the user entered    
roll = randint(1, int(max))  # Use max to determine the number of sides the dice has print('You rolled a', roll, fire * roll)

--- /code ---

To print an apostrophe `'` in a word like `That's`, put a backslash `\` before it so Python knows it's part of the text.

--- /task ---

--- task ---

**Test:** Run your project. When the program reaches the `input` line, it will wait for you to enter a response before continuing. Type your response and then press <kbd>Enter</kbd>, this will allow the program to collect your response. Try it again with a different `input` number.

--- /task ---

--- save ---
