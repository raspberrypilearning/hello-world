## Teste rápido

Responda às três perguntas. Há dicas para guiá-lo para a resposta correta.

Após responder cada pergunta, clique em **Verificar resposta**.

Divirta-se!

--- question ---
---
legend: Pergunta 1 de 3
---

Este código define a variável `world` para conter o texto '🌍🌎🌏' (os três emojis diferentes de mundos):

--- code ---
---
language: python
---

mundo = '🌍🌎🌏'

--- /code ---

Qual código usa corretamente a variável `world` e gera Olá 🌍🌎🌏?

![A área de saída do editor Trinket com Olá 🌍🌎🌏 aparecendo.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Olá', mundo)

--- /code ---

 --- feedback ---

 Não exatamente, `output` não é a maneira de enviar mensagens para a tela.

 --- /feedback ---


- ( )

--- code ---
---
language: python
---

print(f'Hello world')

--- /code ---

 --- feedback ---

 Não exatamente, em Python `print` envia mensagens para a tela, mas algo está faltando neste exemplo.

 --- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Hello{world}')

--- /code ---

 --- feedback ---

 Está correto, em Python `print` envia mensagens para a tela. The text output is inside single quotes `'` , then the `world` variable contains the earth emoji 🌍🌎🌏.

 --- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Hello{world}')

--- /code ---

 --- feedback ---

  Não exatamente, em Python `print` envia mensagens para a tela, mas algo está faltando neste exemplo.

 --- /feedback ---

--- /choices ---

--- /question ---
