## Diga olá

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Tradicionalmente, ao aprender uma nova linguagem de programação, escrevemos primeiro um programa que exiba "Olá mundo!".
</div>
<div>

![A área de saída do Trinket mostrando as duas linhas impressas de texto e emoji.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Abra o [projeto inicial Olá 🌍🌎🌏 ](https://trinket.io/python/975f35023b){:target="_blank"}. O Trinket será aberto em outra aba do navegador.

![O editor Trinket com o código inicial do projeto à esquerda na área de código. À direita está a área de saída em branco.](images/starter_project.png)

--- /task ---

A linha `#!/bin/python3` informa ao Trinket que Python 3 está sendo utilizado (a última versão). As linhas `import` informam ao Python que você usará um código que não escreveu.

Em Python, `print()` gera texto (palavras ou números) na tela.

As linhas que começam com `#` são comentários que explicam o código aos humanos, e ignorados pelo Python.

--- task ---

Encontre a linha `# Coloque o código para ser executado abaixo `.

Clique abaixo dessa linha. O `|` piscando é o cursor e mostra onde você irá digitar.

Digite o código para `print()` um olá:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Coloque o código para ser executado logo abaixo
print('Olá')

--- /code ---

--- collapse ---
---
title: Digitando caracteres especiais em um teclado do Reino Unido ou dos Estados Unidos
---

Em um teclado do Reino Unido ou dos EUA, os parênteses esquerdo `(` e direito `)` estão nas teclas <kbd>9</kbd> e <kbd>0</kbd>. Para digitar um parêntese esquerdo, mantenha pressionada a tecla <kbd>Shift</kbd> (ao lado de <kbd>Z</kbd>) e toque em <kbd>9</kbd>. A aspa simples `'` está na mesma linha que a tecla <kbd>L</kbd>, logo antes da tecla <kbd>Enter</kbd>. A vírgula `,` está ao lado do <kbd>M</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Teste:** Clique no botão **Run** para executar seu código. No Trinket, a saída aparecerá à direita:

![O ícone Run destacado com 'Olá' aparecendo na área de saída. ](images/run_hello.png)

**Depuração:** Se você receber um erro, verifique seu código com muito cuidado. Neste exemplo, as aspas simples em torno de `Olá` estão faltando, então o Python não sabe que deve ser texto.

![o editor Trinket com aspas simples ausentes e erro 'NameError: name 'Olá' is not defined on line 10 in main.py.](images/hello_error.png)

--- /task ---

Em Python, uma **variável** é usada para armazenar texto ou números. As variáveis tornam mais fácil para os humanos lerem o código. Você pode usar a mesma variável em muitos lugares em seu código.

Incluímos algumas variáveis que armazenam caracteres emoji.

--- task ---

Em seu Trinket, clique na aba **emoji.py**. Encontre a variável `world`, que armazena o texto '🌍🌍🌍'.

--- /task ---

--- task ---

Você pode `print()` mais de um item por vez incluindo uma vírgula `,` entre os itens. `print()` adicionará um espaço entre cada item.

Clique na guia **main.py** para voltar ao seu código `print()`.

Altere seu código para também `print()` o conteúdo da variável `world`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

# Coloque o código para ser executado logo abaixo
print('Olá', world)

--- /code ---

**Dica:** `'Olá'` é uma string de texto porque tem aspas simples, enquanto `world` é uma variável, então o valor armazenado nela será impresso.

--- /task ---

--- task ---

**Teste:** Execute seu código para ver o resultado:

![A linha de código atualizada na área de código com a palavra 'Olá' seguida por três emojis de mundo exibidos na área de saída.](images/run_hello_world.png)

Emoji pode parecer diferente em computadores diferentes, então o seu pode não parecer exatamente o mesmo.

**Depuração:** Certifique-se de ter adicionado uma vírgula entre os itens em `print()` e de ter escrito `world` corretamente.

Neste exemplo está faltando a vírgula `,`. É pequeno, mas muito importante!

![O editor Trinket com aspas simples ausentes e erro 'SyntaxError: bad input on line 12 in main.py' exibido.](images/comma_error.png)

--- collapse ---
---
título: não vejo o emoji
---

A maioria dos computadores permite que você use emojis coloridos. No entanto, se você não pode usar emoji, pode usar 'emoticons', como fazíamos antes de os emojis serem inventados!

Altere a linha `from emoji import *` para:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 3
line_highlights: 3
---

from noemoji import *

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Adicione outra linha `print()` para imprimir mais texto e emoji:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Olá', world)    
print('Bem-vindo a', python)

--- /code ---

**Dica:** O código que você precisa digitar é destacado em uma cor mais clara. O código que não está destacado ajuda a localizar onde você precisa adicionar o novo código.

--- /task ---

--- task ---

**Teste:** Clique **run**.

![A linha de código adicional na área de código com a palavra 'Olá' seguida por três emojis de mundo, e as palavras 'Bem-vindo a' seguidas por um emoji de cobra e teclado exibidos na área de saída.](images/run_multiple.png)

**Dica:** É uma boa ideia executar seu código após cada alteração para que você possa corrigir os problemas rapidamente.

**Depuração:** Verifique cuidadosamente se há parentêses, aspas, vírgulas e ortografia correta. Python precisa que você seja realmente preciso.

--- /task ---

Se você tiver uma conta Trinket, você pode clicar no botão **Remix** para salvar uma cópia em sua biblioteca `My Trinkets`.

Se você não tiver uma conta Trinket, ainda poderá voltar ao seu projeto no futuro no mesmo computador usando o link do projeto inicial.

--- save ---
