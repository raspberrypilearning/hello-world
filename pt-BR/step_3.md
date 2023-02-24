## Operações matemáticas e datas

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Python é ótimo para trabalhar com números e datas.
</div>
<div>

![A área de saída com cinco linhas impressas mostrando novas saídas da operação e data atual.](images/sums_dates.png){:width="300px"}

</div>
</div>

Em Python você pode usar operadores matemáticos para fazer contas:

| + | adicionar |   
| - | subtrair |   
| * | multiplicar |   
| / | dividir |   
| ** |exponenciar |

--- task ---

Adicione outras duas linhas `print()` ao seu código, incluindo uma operação para o Python calcular:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 14-15
---

print('Olá', world)   
print('Bem-vindo a', python)   
print(python, 'é muito bom em', sums)   
print(230 * 5782 ** 2 / 23781)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código. O Python calculou a operação corretamente? Só brincando! Python faz a matemática difícil para você, então você não precisa resolver.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A cientista da computação japonesa <span style="color: #0faeb0">**Emma Haruka Iwao**</span> usou um computador para calcular o valor de Pi (*π*) para 31 trilhões de dígitos. Essa resposta é tão longa que levaria mais de 300.000 anos apenas para dizê-la! 
</p>

--- task ---

Tente mudar a operação que o Python faz para uma complicada!

Você também pode usar parênteses se quiser controlar a ordem em que o Python calcula a operação: `print( (2 + 4) * (5 + 3) )`.

--- /task ---

--- task ---

**Teste:** Execute seu código e faça com que o Python calcule sua operação.

**Debug:** Certifique-se de que sua soma tenha um parêntese esquerdo e direito ao redor `( 2 * 45 )`. Se você usar parênteses extras para controlar a ordem, faça com que você tenha um parêntese direito para corresponder a cada parêntese esquerdo.

--- /task ---

--- task ---

Se você pediu ao Python para calcular uma operação muito grande, pode descobrir que a resposta passa por várias linhas na área de saída.

**Dica:** Clique no menu **hambúrger** (o ícone com três linhas) no canto superior esquerdo do seu editor Trinket. Em seguida, clique no botão **Fullscreen** para visualizar seu projeto no modo de tela cheia.

![O editor Trinket com menu do lado esquerdo expandido, através do menu de hambúrguer, para mostrar a opção de tela cheia.](images/full_screen.png)

Para sair do modo de tela cheia, clique no botão **Fullscreen** novamente ou pressione <kbd>Esc</kbd> no teclado.

--- /task ---

A linha `from datetime import *` na parte superior da guia **main.py** inclui uma biblioteca com funções úteis para obter a data e hora atuais.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Uma das grandes coisas sobre Python são todas as <span style="color: #0faeb0">**bibliotecas**</span> de código que estão disponíveis para uso. Uma biblioteca Python permite que você use facilmente o código que outras pessoas escreveram. Existem bibliotecas para desenhar tabelas e gráficos, fazer arte, fazer cálculos e muito mais.
</p>

--- task ---

Adicione outra linha ao seu código para `imprimir` um pouco mais de texto e as variáveis emoji `calendar` e `clock`.

Obtenha a data e hora atuais usando a função `now()` da biblioteca `datetime`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 14
line_highlights: 16-17
---

print(python, 'é muito bom em', sums)    
print(230 * 5782 ** 2 / 23781) # Imprime o resultado da soma     
print('O', calendar, clock, 'é', datetime.now()) #Imprimir com emoji

--- /code ---

**Dica:** Você não precisa digitar os comentários, eles estão lá apenas para ajudá-lo a entender o código. Basta digitar a parte antes do `#`.

--- /task ---

--- task ---

**Teste:** Execute seu código algumas vezes para ver a atualização de data e hora.

**Depuração:** Verifique se você tem um ponto final `.` entre `datetime` e `now`. Verifique cuidadosamente toda a pontuação.

--- /task ---

--- save ---
