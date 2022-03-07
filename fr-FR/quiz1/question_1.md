## Réflexion

Bravo, tu as réalisé un programme interactif avec du texte et des emoji 👍

Maintenant, il est temps de réfléchir - la réflexion est une partie importante de l'apprentissage, car elle aide à établir de nouvelles connexions dans ton cerveau.

Réponds aux trois questions ci-dessous pour réfléchir à ce que tu as appris.

Après chaque question, appuie sur **soumettre**. Tu seras guidé vers la bonne réponse. Tu peux faire cette activité autant de fois que tu le souhaites.

Amuse-toi bien !

--- question ---
---
legend : Question 1 sur 3
---

Ce code définit la variable `world` pour qu'elle contienne le texte '🌍🌎🌏' (les trois emoji de monde différents) :

--- code ---
---
language: python
---

world = '🌍🌎🌏'

--- /code ---

Quel code utilise correctement la variable `world` et affiche Bonjour 🌍🌎🌏 ?

![La zone de sortie de l'éditeur Trinket avec Bonjour 🌍🌎🌏 affiché.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Bonjour' world)

--- /code ---

 --- feedback ---

 Pas tout à fait, `output` n'est pas le moyen de sortir des messages à l'écran.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print('Bonjour' world)

--- /code ---

 --- feedback ---

 Pas tout à fait, dans Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print('Bonjour', world)

--- /code ---

 --- feedback ---

 C'est exact, en Python `print` affiche des messages à l'écran. La sortie de texte est entre guillemets simples `'` , une virgule sépare les deux éléments et fournit un espace, puis la variable `world` est appelée, qui stocke l'emoji de la terre 🌍🌎🌏, comme dans ton projet.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print(Bonjour, world)

--- /code ---

 --- feedback ---

  Pas tout à fait, dans Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

 --- /feedback ---

--- /choices ---

--- /question ---
