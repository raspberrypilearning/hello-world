## Λάβε είσοδο

Μπορείς να χρησιμοποιήσεις την εντολή `input()`{:.language-python} για να ζητήσεις από το άτομο που χρησιμοποιεί το πρόγραμμά σου να εισαγάγει κείμενο.

--- task ---

Άλλαξε τη συνάρτησή σου ώστε να ζητά από το άτομο που χρησιμοποιεί το πρόγραμμά σου να εισαγάγει πόσες πλευρές έχει το ζάρι και αποθήκευσέ την ως μεταβλητή.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19-20
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Κάνε κλικ στο κουμπί **Run** και πληκτρολόγησε έναν αριθμό πλευρών. Βεβαιώσου ότι έχεις πατήσει το πλήκτρο <kbd> Enter </kbd> αφού εισαγάγεις τον αριθμό των πλευρών. Αυτό θα πρέπει να δεις όταν εκτελείς τον κώδικά σου.

<div class="c-project-output">
```
Γεια σου 🌍🌎🌏
Καλώς ήρθες στην Python 🐍
Η Python 🐍 είναι καλή στα μαθηματικά!
27
Η ημερομηνία και η ώρα είναι 2025-10-24 13:20:41.323000
Πόσες πλευρές έχει το ζάρι σου;:
20 
Αυτό είναι D 20
Έριξες 1 🔥
```

--- /task ---

Οι είσοδοι αποθηκεύονται πάντα ως κείμενο, αλλά πρέπει να χρησιμοποιήσουμε την είσοδο που είναι αποθηκευμένη στο `max` για να καθορίσουμε τον μεγαλύτερο αριθμό που μπορεί να φέρει το ζάρι.

--- task ---

Η μεταβλητή `max` είναι μια συμβολοσειρά, επομένως πρέπει να αλλάξει σε ακέραιο `int()`{:.language-python}.


--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 21
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1, int(max)) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Κάνε κλικ στο κουμπί **Run** μερικές φορές. Έλεγξε ότι το ζάρι παράγει έναν τυχαίο αριθμό κάθε φορά.

--- /task ---

