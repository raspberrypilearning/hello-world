## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---
---
legend : Question 1 sur 3
---

Ce code définit la variable `monde` pour qu'elle contienne le texte '🌍🌎🌏' (les trois emojis de monde différents) :

--- code ---
---
language: python
---

monde = '🌍🌎🌏'

--- /code ---

Quel code utilise correctement la variable `monde` et affiche Bonjour 🌍🌎🌏 ?

![La zone de sortie de l'éditeur Trinket avec Bonjour 🌍🌎🌏 affiché.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Bonjour' monde)

--- /code ---

 --- feedback ---

 Pas tout à fait, `output` n'est pas le moyen de sortir des messages à l'écran.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Bonjour' monde)

--- /code ---

 --- feedback ---

 Pas tout à fait, dans Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Bonjour', monde)

--- /code ---

 --- feedback ---

 C'est exact, en Python `print` affiche des messages à l'écran. La sortie de texte est entre guillemets simples `'` , une virgule sépare les deux éléments et fournit un espace, puis la variable `monde` est appelée, qui stocke l'emoji de la terre 🌍🌎🌏, comme dans ton projet.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Bonjour, monde)

--- /code ---

 --- feedback ---

  Pas tout à fait, dans Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

 --- /feedback ---

--- /choices ---

--- /question ---
