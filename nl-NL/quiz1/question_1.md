## Snelle quiz

Beantwoord de drie vragen. Je krijgt hints die je naar het juiste antwoord leiden.

Druk na elke vraag op **Controleer mijn antwoord**. Je wordt naar het juiste antwoord geleid.

Veel plezier!

--- question ---
---
legend: Question 1 of 3
---

Deze code stelt de `wereld`-variabele in om de tekst '🌍🌎🌏' te bevatten (de drie verschillende wereldemoji):

--- code ---
---
language: python
---

wereld = '🌍🌎🌏'

--- /code ---

Welke code gebruikt de `wereld` variabele correct en geeft Hallo 🌍🌎🌏 als resultaat?

![Het uitvoergebied van de code-editor waarin Hallo 🌍🌎🌏 wordt weergegeven.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Hallo' wereld)

--- /code ---

 --- feedback ---

 Niet helemaal, `output` is niet de manier om berichten naar het scherm te sturen.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Hallo wereld')

--- /code ---

 --- feedback ---

 Niet helemaal, in Python stuurt `print` berichten naar het scherm, maar er ontbreekt iets in dit voorbeeld.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hallo{wereld}')

--- /code ---

 --- feedback ---

 Dat klopt, in Python stuurt `print` berichten naar het scherm. De tekstuitvoer staat tussen enkele aanhalingstekens `'`, waarna de variabele `wereld` de aarde-emoji bevat 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hallo{wereld}')

--- /code ---

 --- feedback ---

  Niet helemaal, in Python stuurt `print` berichten naar het scherm, maar er ontbreekt iets in dit voorbeeld.

 --- /feedback ---

--- /choices ---

--- /question ---
