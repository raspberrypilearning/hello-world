--- question ---
---
legend: Question 3 sur 3
---

Cette fonction génère deux nombres aléatoires :

--- code ---
---
language: python
---

def deux_des():
    print('Premier nombre :', randint(1, 6))
    print('Deuxième nombre :', randint(1, 6))

--- /code ---

Quel code appellera la fonction pour l'exécuter ?

![Le Code Editor avec une zone de sortie affichant deux nombres générés aléatoirement.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def deux_des():
    print('Premier nombre :', randint(1, 6))
    print('Deuxième nombre :', randint(1, 6))

--- /code ---

 --- feedback ---

 Non, c'est le code pour définir la fonction, mais il n'exécute pas la fonction. Tu dois utiliser un code différent pour l'appeler.

 --- /feedback ---

- ( )
--- code ---
---
language: python
---

deux_des

--- /code ---

 --- feedback ---

Fermer ! `deux_des` est le nom de la fonction, mais pour l'appeler, il faut plus que le nom.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

deux_des[]

--- /code ---

 --- feedback ---

 Pas tout à fait, pense au type de parenthèses que tu as utilisé pour appeler les fonctions de ton projet.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

deux_des()

--- /code ---

 --- feedback ---

 C'est exact, l'utilisation du nom de la fonction suivi de parenthèses `(` `)` appellera la fonction.

 --- /feedback ---

--- /choices ---

--- /question ---
