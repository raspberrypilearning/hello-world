--- question ---
---
legend: Pergunta 3 de 3
---

Esta função gera dois números aleatórios:

--- code ---
---
language: python
---

def dois_dados():
    print('Primeiro número:', randint(1, 6))
    print('Segundo número:', randint(1, 6))

--- /code ---

Qual código chamará a função para executá-la?

![O editor código com área de saída mostrando dois números gerados aleatoriamente.](images/quiz3.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

def dois_dados():
    print('Primeiro número:', randint(1, 6))
    print('Segundo número:', randint(1, 6))

--- /code ---

 --- feedback ---

 Não, este é o código para definir a função, mas não executa a função. Você precisará usar um código diferente para chamá-la.

 --- /feedback ---

- ( )
--- code ---
---
language: python
---

dois_dados

--- /code ---

 --- feedback ---

Fechar! `dois_dados` é o nome da função, mas para chamá-la você precisa mais do que apenas o nome.

 --- /feedback ---

- ()

--- code ---
---
language: python
---

dois_dados[]

--- /code ---

 --- feedback ---

 Não exatamente, pense nos parênteses que você usou para chamar as funções em seu projeto.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

dois_dados()

--- /code ---

 --- feedback ---

 Isso mesmo, usar o nome da função seguido por `(` `)` parênteses chamará a função.

 --- /feedback ---

--- /choices ---

--- /question ---
