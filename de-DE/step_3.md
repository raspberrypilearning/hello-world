## Sums and dates

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python eignet sich hervorragend für die Arbeit mit Zahlen und Datumsangaben.
</div>
<div>

![The text output area with five printed lines showing new sum and current date outputs.](images/sums_dates.png){:width="300px"} 

</div>
</div>

In Python kannst Du mathematische Operatoren verwenden, um Rechenergebnisse zu erzeugen:

| + | addieren |   
| - | subtrahieren |   
| * | multiplizieren |   
| / | dividieren |   
| ** | Exponent |

### Erstelle eine Berechnung

--- task ---

Füge Deinem Code zwei weitere Zeilen mit `print()` Ausdrücken hinzu, einschließlich einer Summe, die Python berechnen kann:

**Tipp:** Um das `*` Symbol zu erhalten, halte <kbd>Umschalten</kbd> gedrückt und klicke das <kbd>+</kbd> (neben der Enter Taste).

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 20-21
---

print('Hallo', welt)   
print('Willkommen bei', python)   
print(python, 'ist sehr gut in Mathe!')   
print(230 * 5782 ** 2 / 23781)  # Gib das Ergebnis der Rechnung aus

--- /code ---

**Tipp:** Du musst die Kommentare nicht eingeben. Sie dienen nur dazu, Dir das Verständnis des Codes zu erleichtern. Gib einfach den Code vor dem `#` ein.

--- /task ---

--- task ---

**Test:** Führe Deinen Code aus. Hat Python richtig gerechnet? Nur ein Scherz! Python erledigt die schwierigen Berechnungen für Dich, sodass Du nicht selbst rechnen musst.

**Fehlersuche:**

--- collapse ---
---
title: Ich habe einen Syntaxfehler
---

Achte darauf, dass Du in dem Aufruf von `print()` ein Komma `,` zwischen den Elementen gesetzt hast und `python` richtig geschrieben ist.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Die japanische Informatikerin <span style="color: #0faeb0">**Emma Haruka Iwao**</span> berechnete mit einem Computer den Wert von Pi (*π*) auf 31 Billionen Stellen. Diese Antwort ist so lang, dass es über 300.000 Jahre dauern würde, sie nur auszusprechen! 
</p>

--- task ---

Versuche mal, die Rechnung, die Python macht, komplizierter zu machen!

Du kannst auch Klammern verwenden, wenn Du die Reihenfolge steuern möchten, in der Python das Ergebnis berechnet: `print( (2 + 4) * (5 + 3) )`.

--- /task ---

--- task ---

**Test:** Führe Deinen Code aus und lass Python das Ergebnis berechnen.

**Fehlersuche:** Achte darauf, dass Dein Rechnungsausdruck linke und rechte runde Klammer hat `( 2 * 45 )`. If you use extra brackets to control the order, make sure you have a right bracket to match every left bracket.

--- /task ---

--- task ---

On the code editor, you might find the text too big or too small to read. You can easily change these settings to suit your preference.

**Tip:** Click on the **Settings menu**  on the left of your code editor. Then click on any of the **Text Size** buttons to change the size of the text.

![The code editor with the settings menu expanded, to show the Colour Mode and Text Size options.](images/full_screen.png)

You can also switch between colour modes, click on the **Light & Dark** buttons to see the changes.

--- /task ---

The line `from datetime import *` at the top of the **main.py** tab includes a library with helpful functions for getting the current date and time.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
One of the great things about Python is all the <span style="color: #0faeb0">**libraries**</span> of code that are available to use. A Python library allows you to easily use code that other people have written. There are libraries for drawing charts and graphs, making art, doing calculations, and lots more.
</p>

--- task ---

Add another line to your code to `print` the current date and time.

Get the current date and time by using the `now()` function from the `datetime` library:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 22
---

print(python, 'is very good at maths!')    
print(230 * 5782 ** 2 / 23781)  # Print the result of the sum     
print('The date and time is', datetime.now())  # Print the current date and time

--- /code ---

**Tip:** You don't need to type the comments, they are just there to help you understand the code. Just type the part before the `#`.

--- /task ---

--- task ---

**Test:** Run your code a couple of times to see the time update.

**Debug:** Check that you have a fullstop `.` between `datetime` and `now`. Check all the punctuation carefully.

--- /task ---

--- save ---
