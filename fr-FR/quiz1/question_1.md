## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---
---
legend: Question 1 sur 3
---

Ce code définit la variable `monde` pour qu'elle contienne le texte '🌍🌎🌏' (les trois emojis de monde différents) :

--- code ---
---
language: python
---

monde = '🌍🌎🌏'

--- /code ---

Quel code utilise correctement la variable `monde` et affiche Bonjour 🌍🌎🌏 ?

![La zone de sortie du Code Editor avec Bonjour 🌍🌎🌏 affiché.](images/quiz1.png)

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

print(f'Bonjour le monde')

--- /code ---

 --- feedback ---

 Pas tout à fait, dans Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Bonjour {world}')

--- /code ---

 --- feedback ---

 C'est exact, en Python `print` affiche des messages à l'écran. La sortie de texte est à l'intérieur de guillemets simples `'` , puis la variable `monde` contient l'emoji Terre 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Bonjour {world}')

--- /code ---

 --- feedback ---

  Pas tout à fait, dans Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

 --- /feedback ---

--- /choices ---

--- /question ---
