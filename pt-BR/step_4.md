## Role um dado

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python pode gerar números aleatórios para fazer um dado digital.
</div>
<div>

![A área de saída com linhas adicionais para solicitar que o usuário insira o maior número para seus dados e a resposta com o número aleatório.](images/roll_dice.png){:width="300px"}

</div>
</div>

Em Python você **chama** uma **funcao()** para realizar uma ação. Um nome de função pode conter apenas caracteres alfanuméricos e sublinhados (A-z, 0-9 e _). Você já usou a função `print()` para produzir texto.

Você pode **definir** uma nova **função** para agrupar o código para que você possa nomeá-lo e reutilizá-lo.

--- task ---

As funções precisam ser definidas antes que você possa chamá-las. Procure o comentário próximo ao topo da guia **main.py** que diz `#Coloque definições de função aqui`.

Defina uma nova função chamada `rolar_dado()` que usa a função `randint()`, da biblioteca `random` para gerar um 'inteiro' aleatório (número inteiro) de 1 a 6 e enviá-lo para a tela.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9-12
---

# Coloque as definições da função logo abaixo

def rolar_dado(): #Não esqueça os dois pontos no final desta linha   
print(python, 'pode fazer um', dice)   
print('Você obteve um', randint(1, 6))

--- /code ---

As linhas abaixo de `def rolar_dado():` são **recuadas**. Para fazer isso, use o caractere <kbd>Tab</kbd> no teclado (geralmente acima do <kbd>CAPSLOCK</kbd> no teclado). O código de recuo informa ao Python que as linhas recuadas fazem parte da função.

**Dica:** O sublinhado `_` é usado entre palavras em nomes de variáveis e funções em Python para facilitar a leitura. Você não pode usar um espaço.

--- collapse ---
---
title: Digitando caracteres especiais em um teclado do Reino Unido ou dos Estados Unidos
---

Em um teclado do Reino Unido ou dos EUA, os dois pontos `:` estão na mesma tecla que o ponto e vírgula, ao lado da tecla <kbd>L</kbd>: segure <kbd>Shift</kbd> e toque <kbd>;</kbd> para digitar um `:`. O sublinhado `_` está na mesma tecla que o `-`, próximo ao <kbd>0</kbd>, segure <kbd>Shift</kbd> e toque <kbd>-</kbd> para digitar um `_`.

--- /collapse ---

--- /task ---

--- task ---

**Teste:** Se você 'Executar' seu código agora, ele não rolará um dado. Isso porque você definiu a função `rolar_dado()`, mas ainda não a chamou.

--- /task ---

--- task ---

Para usar uma função, você precisa chamá-la no código. Vá para o final do seu código e adicione uma nova linha para chamar a função `rolar_dado()`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 22
---

print('A', calendar, clock, 'é', datetime.now())

rolar_dado() #Chama a função rolar dados

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu projeto várias vezes para ver o dado aleatório rolar a cada vez.

**Debug:** Certifique-se de ter um sublinhado `_` entre rolar e dado para fazer o nome da função. Certifique-se de ter dois pontos `:` no final da linha.

**Debug:** Verifique se as linhas sob `def rolar_dado()` estão recuadas. É muito comum errar isso em Python, então certifique-se de verificar.

![O editor Trinket mostrando as linhas de código para a função <code>rolar_dado</code> não foi recuado. O código foi executado e está destacado na linha 10, a primeira linha que deve ser recuada, com o erro 'SyntaxError: bad input on line 10 in main.py'.](images/indent_error.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Os usos de números aleatórios incluem criptografia, ciência de dados e adição de variedade em jogos e arte de computador. Os computadores geram <span style="color: #0faeb0">**números aleatórios**</span> usando um algoritmo. Para números que são realmente aleatórios, você precisa de uma entrada imprevisível do mundo real.
</p>

--- task ---

A variável `fire` armazena um emoji 🔥. O código `print(fire * 3)` gera três emojis de fogo '🔥🔥🔥'. Você precisa gerar o número correto de emojis para corresponder ao número rolado.

--- collapse ---
---
title: O que aconteceria se você usasse `print(fire * randint(1, 6))`?
---

Você obteria um novo número aleatório que geralmente é diferente do seu primeiro número aleatório.

--- /collapse ---

Hmm, como você pode ter certeza de usar o mesmo número aleatório?

Altere seu código para salvar o valor retornado por `randint()` em uma variável chamada `jogada` e, em seguida, use essa variável para imprimir o número rolado com o número correspondente de 🔥 emoji.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11 - 13
---

# Coloque as definições da função logo abaixo

def rolar_dado():    
print(python, 'pode fazer um', dice)    
jogada = randint(1, 6) #Gerar um número aleatório entre 1 e 6    
print('Você obteve ', jogada) #Imprima o valor da variável jogada     
print(fire * jogada) #Repita o emoji de fogo para combinar com o lançamento do dado

--- /code ---

Você pode usar `estrela` ou `coração` ao invés de `fogo` se preferir.

O símbolo `*` significa multiplicar então `fire * jogada` multiplica o texto na variável `fire` ('🔥') pelo número contido na variável `jogada`.

--- /task ---

--- task ---

**Teste:** Teste seu projeto algumas vezes. Certifique-se de entender como o código funciona.

**Dica:** As variáveis são úteis quando você precisa usar o mesmo valor várias vezes em seu código. Dar às variáveis um nome sensato também torna seu código mais fácil de entender.

--- /task ---

Atualize seu dado para que o usuário possa escolher o número máximo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">

Muitos jogos usam dados multifacetados. No mundo físico, os dados são feitos de formas geométricas regulares. Dados comuns incluem D6, D12 e D20. Em um computador, você pode gerar um número <span style="color: #0faeb0">aleatório</span> para fazer um dado com qualquer número de lados.</p>

--- task ---

A função `input()` faz uma pergunta ao usuário e então retorna sua resposta.

Adicione código para pedir ao usuário o maior número em seu dado e salve o resultado em uma variável chamada `max` e `imprima` o número escolhido na área de saída:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Coloque as definições da função logo abaixo

def rolar_dado():   
print(python, 'pode fazer um', dice)   
maximo = input('Quantos lados?:') #Aguarda a entrada do usuário    
print('Isso é um D ', maximo) #Use o número digitado pelo usuário    
jogada = randint(1, 6)    
print('Você obteve', jogada)    
print(fire * jogada)

--- /code ---

Para imprimir um apóstrofo `'`, coloque uma barra invertida `\` antes dele para que o Python saiba que é parte do texto.

--- /task ---

--- task ---

Altere seu código de variável `jogada` para usar `maximo` como o valor máximo para `randint` quando ele gerar um número aleatório.

Quando você recebe uma entrada do usuário, o Python a trata como texto. Mas, `randint` precisa de um 'inteiro' (um número inteiro positivo). A função `int` transforma a entrada do usuário em um inteiro.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 13
---

# Coloque as definições da função logo abaixo

def rolar_dado():   
print(python, 'pode fazer um', dice)   
maximo = input('Quantos lados?:') #Aguarda a entrada do usuário   
print('Isso é um D ', maximo) #Use o número digitado pelo usuário   
jogada = randint(1, int(maximo))   
#randint precisa que maximo seja um 'inteiro'   
print('Você obteve', jogada)<0/> print(fire * jogada)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código. Quando o programa atingir a linha `input`, ele aguardará que você insira uma resposta antes de continuar. Tente novamente com um número `de entrada` diferente.

--- /task ---

--- save ---
