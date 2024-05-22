## Rechnen und Daten

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python eignet sich hervorragend für die Arbeit mit Zahlen und Datumsangaben.
</div>
<div>

![Der Textausgabebereich mit fünf Zeilen, die neue Rechnungs- und aktuelle Datumsausgaben anzeigen.](images/sums_dates.png){:width="300px"} 

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
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---

print('Hallo', welt)   
print('Willkommen bei', python)   
print(python, 'ist sehr gut in Mathe!')   
print(230 *5 782 ** 2 / 23781)  # Gib das Ergebnis der Rechnung aus

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

**Fehlersuche:** Achte darauf, dass Dein Rechnungsausdruck linke und rechte runde Klammer hat `( 2 * 45 )`. Wenn Du zusätzliche Klammern verwendest, um die Reihenfolge zu kontrollieren, achte darauf, dass Du für jede linke Klammer eine rechte passende rechte Klammer setzt.

--- /task ---

--- task ---

Im Code Editor ist der Text möglicherweise zu groß oder zu klein zum Lesen. Du kannst diese Einstellungen ganz einfach nach Belieben ändern.

**Tipp:** Klick auf das **Settings menu** (**Einstellungen Menü**)  links in Deinem Code Editor. Klick dann auf eine der **Text Size** (**Textgröße**) Schaltflächen, um die Größe des Texts zu ändern.

![Der Code Editor mit Einstellungen Menü aufgeklappt, um die Optionen Farbmodus und Textgröße anzuzeigen.](images/full_screen.png)

Du kannst auch zwischen den Farbmodi wechseln. Klick auf die Schaltflächen **Light & Dark** (**Hell & Dunkel**), um die Änderungen anzuzeigen.

--- /task ---

Die Zeile `from datetime import *` oben auf dem **main.py** Tab enthält eine Bibliothek mit hilfreichen Funktionen zum Abrufen des aktuellen Datums und der aktuellen Uhrzeit.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Eines der großartigen Dinge an Python sind die vielen <span style="color: #0faeb0">**Bibliotheken**</span>, die man verwenden kann. Eine Python Bibliothek erlaubt es, Code zu verwenden, den andere geschrieben haben. Es gibt Bibliotheken zum Zeichnen von Diagrammen und Grafiken, zum Erstellen von Kunstwerken, zum Durchführen von Berechnungen und vielem mehr.
</p>

--- task ---

Füge Deinem Code eine weitere Zeile hinzu, um mit `print` das aktuelle Datum und die aktuelle Uhrzeit auszugeben.

Ruf das aktuelle Datum und die aktuelle Uhrzeit ab, indem Du die Funktion `now()` aus der Bibliothek `datetime` verwendest:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 22
---

print(python, 'ist sehr gut in Mathe!')    
print(230 *5 782  ** 2 / 23781)  # Gib das Ergebnis der Rechnung aus     
print('Datum und Uhrzeit sind', datetime.now())  # Gib aktuelles Datum und Uhrzeit aus

--- /code ---

**Tipp:** Du musst die Kommentare nicht eingeben. Sie dienen nur dazu, Dir das Verständnis des Codes zu erleichtern. Gib einfach den Code vor dem `#` ein.

--- /task ---

--- task ---

**Test:** Führe Deinen Code ein paar Mal aus, um die Zeitaktualisierung zu sehen.

**Fehlersuche:** Achte darauf, dass Du einen Punkt `.` zwischen `datetime` und `now` stehen hast. Überprüfe alle Satzzeichen sorgfältig.

--- /task ---

--- save ---
