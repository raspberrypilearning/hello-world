--- question ---
---
legend: Ερώτηση 3 από 3
---

Αυτή η συνάρτηση εμφανίζει δύο τυχαίους αριθμούς:

--- code ---
---
language: python
---

def two_dice(): 
  print('Πρώτος αριθμός:', randint(1, 6)) 
  print('Δεύτερος αριθμός:', randint(1, 6))

--- /code ---

Ποιος κώδικας θα καλέσει τη συνάρτηση για να την εκτελέσει;

![Το πρόγραμμα επεξεργασίας Trinket με περιοχή εξόδου που εμφανίζει δύο τυχαία δημιουργημένους αριθμούς.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def two_dice(): 
  print('Πρώτος αριθμός:', randint(1, 6)) 
  print('Δεύτερος αριθμός:', randint(1, 6))

--- /code ---

 --- feedback ---

 Όχι, αυτός είναι ο κώδικας για τον ορισμό της συνάρτησης, αλλά δεν εκτελεί τη συνάρτηση. Θα χρειαστεί να χρησιμοποιήσεις διαφορετικό κώδικα για να την καλέσεις.

 --- /feedback ---

- ( )
--- code ---
---
language: python
---

two_dice

--- /code ---

 --- feedback ---

Είναι κοντά! `two_dice` είναι το όνομα της συνάρτησης, αλλά για να την καλέσεις χρειάζεσαι κάτι περισσότερο από το όνομα.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

two_dice[]

--- /code ---

 --- feedback ---

 Όχι ακριβώς, σκέψου το είδος των σημείων στίξης που χρησιμοποίησες για να καλέσεις τις συναρτήσεις στο έργο σου.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

two_dice()

--- /code ---

 --- feedback ---

 Αυτό είναι σωστό, χρησιμοποιώντας το όνομα της συνάρτησης ακολουθούμενο από παρενθέσεις `(` `)` θα καλέσεις τη συνάρτηση.

 --- /feedback ---

--- /choices ---

--- /question ---
