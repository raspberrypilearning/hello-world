## Αθροίσματα και ημερομηνίες

Στην Python μπορείς να εργαστείς με αριθμούς και ημερομηνίες.

Μπορείς να χρησιμοποιήσεις **αριθμητικούς τελεστές** όπως `+` και `-`  για να κάνεις υπολογισμούς:

| + | πρόσθεση |   
| - | αφαίρεση |   
| * | πολλαπλασιασμός |   
| / | διαίρεση |   
| ** | ύψωση σε δύναμη |


--- task ---

Πρόσθεσε δύο ακόμη γραμμές `print()`{:.language-python} στον κώδικά σου, με έναν πολλαπλασιασμό που θα υπολογίσει η Python:

--- code ---
---
**Δοκιμή:** Εκτέλεσε τον κώδικά σου μερικές φορές για να δεις την ενημέρωση της ημερομηνίας και της ώρας.
line_highlights: 23-24
---
# Put code to run under here
print(f'Hello {world}') print(f'Welcome to {python}') print(f'{python} is good at maths!') print(f'{3 * 9}')

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Κάνε κλικ στο κουμπί **Run**. Αυτό θα πρέπει να δεις όταν εκτελείς τον κώδικά σου.

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
```

--- /task ---

Η Python έχει πολλά **modules** (ενότητες) που μπορείς να χρησιμοποιήσεις στον κώδικά σου για να εκτελέσεις συγκεκριμένες εργασίες.

Το module `datetime`{:.language-python} βοηθά στη σύνταξη κώδικα που χρησιμοποιεί ημερομηνίες και ώρες.

--- task ---

Πρόσθεσε μια ακόμη γραμμή `print`{:.language-python} στον κώδικά σου για να εμφανίσεις την τρέχουσα ημερομηνία και ώρα, χρησιμοποιώντας τη μέθοδο `now()`{:.language-python} από τη βιβλιοθήκη `datetime`{:.language-python}:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 23
line_highlights: 25
---

print(f'{python} is good at maths!') print(f'{3 * 9}') print(f'The date and time is {datetime.now()}')

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικά σου μερικές φορές για να δεις ότι ανανεώνεται η ώρα.

--- /task ---


