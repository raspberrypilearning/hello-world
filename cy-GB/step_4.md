## Taflu dis

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a function for rolling a dice using random numbers. 
  
In Python:
  - **functions**, defined with `def`, are like 'my blocks' in Scratch,
  - `randint` is like 'random' in Scratch, and
  - `input` is like 'ask' in Scratch.

</div>
<div>

![Yr ardal allbwn gyda llinellau ychwanegol i ofyn i'r defnyddiwr roi'r rhif mwyaf ar gyfer ei ddis a'r ymateb gyda'r rhif ar hap.](images/roll_dice.png){:width="300px"} 

</div>
</div>

Yn Python, rydych chi'n **galw** **swyddogaeth()** i gyflawni gweithred. Rydych chi eisoes wedi defnyddio'r swyddogaeth `print()` i allbynnu testun.

Fe allwch chi **ddiffinio** **swyddogaeth** newydd i grwpio cod gyda'i gilydd er mwyn gallu ei henwi a'i hailddefnyddio.

### Define your function

--- task ---

Rhaid diffinio swyddogaethau cyn eu galw. Look for the comment in the **main.py** file that says `# Function definitions`.

Diffiniwch swyddogaeth newydd o'r enw `taflu_dis()` sy'n defnyddio'r swyddogaeth `randint()` o'r llyfrgell `random` i gynhyrchu cyfanrif ar hap rhwng 1 a 6, a'i allbynnu ar y sgrin.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9-12
---

# Rhowch ddiffiniadau swyddogaethau o dan fan hyn
def taflu_dis(): #Cofiwch y colon ar ddiwedd y llinell hon   
print('mae', python, 'yn gallu gwneud', dis)   
print('Rydych chi wedi taflu', randint(1, 6))

--- /code ---

The line under `def roll_dice():` is **indented**. I wneud hyn, defnyddiwch y nod <kbd>Tab</kbd> ar eich bysellfwrdd (uwchben <kbd>CAPSLOCK</kbd> fel arfer). Mae mewnoli cod yn dweud wrth Python bod y llinellau wedi'u mewnoli yn rhan o'r swyddogaeth.

**Tip:** The underscore `_` is used between words in variable and function names in Python to make them easier to read. Chewch chi ddim defnyddio bwlch.

--- collapse ---
---
title: Teipio nodau arbennig ar fysellfwrdd y DU neu UDA
---

Ar fysellfwrdd y DU neu UDA, mae'r colon `:` ar yr un fysell â'r hanner colon, wrth ymyl y fysell <kbd>L</kbd>: daliwch <kbd>Shift</kbd> a tharo <kbd>;</kbd> i deipio `:`. Mae'r tanlinell `_` ar yr un fysell â `-`, wrth ymyl <kbd>0</kbd>, daliwch <kbd>Shift</kbd> a tharo <kbd>-</kbd> i deipio `_`.

--- /collapse ---

--- /task ---

--- task ---

**Profi:** Os byddwch yn 'rhedeg' eich cod nawr, ni fydd yn taflu dis. Mae hynny oherwydd eich bod wedi diffinio'r swyddogaeth `taflu_dis()`, ond heb ei galw eto.

**Debug:**

--- collapse ---
---
line_highlights: 22
---

- Make sure you have an underscore `_` between roll and dice to make the function name.

- Make sure you have a colon `:` at the end of the line.

- Check that the line under `def roll_dice()` is indented. It's really common to get this wrong in Python, so make sure to check.

![The code editor showing the line of code inside the <code>roll_dice</code> function has not been indented. The line of code with the error is highlighted. The code has been run, with the error 'SyntaxError: bad input on line 17 in main.py'.](images/indent_error.png)

--- /collapse ---

--- /task ---

### Call your function

--- task ---

To use a function, you need to **call** it in the code. Go to the end of your code and add a new line to call the `roll_dice()` function:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 25
title: Beth fyddai'n digwydd pe baech chi'n defnyddio `print(fflam * randint(1, 6))`?
---

print('The date and time is', datetime.now())

**Profi:** Rhedwch eich prosiect nifer o weithiau i weld y tafliad dis ar hap bob tro.

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project several times to see the random dice roll each time.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Uses of random numbers include cryptography, data science, and adding variety into games and computer art. Computers generate <span style="color: #0faeb0">**random numbers**</span> using an algorithm. For numbers that are really random, you need an unpredictable input from the real world.
</p>

### Use 🔥🔥🔥 for the number rolled

--- task ---

Your function can use the 🔥 emoji variable. The code `print(fire * 3)` outputs three fire emojis '🔥🔥🔥'. You need to output the correct number of emojis to match the random number rolled by the dice.

Change your code to save the value returned by `randint()` in a variable called `roll`. Use that variable to print out the number rolled with the matching number of 🔥 emojis.

--- code ---
---
Hmm, sut mae gwneud yn siŵr eich bod yn defnyddio'r un rhif ar hap?
line_highlights: 11 - 13
---

# Rhowch ddiffiniadau swyddogaethau o dan fan hyn
Newidiwch eich cod i gadw'r gwerth sy'n cael ei ddychwelyd gan `randint()` mewn newidyn o'r enw `taflu` ac yna defnyddio'r newidyn hwnnw i brintio'r rhif sy'n cael ei rolio gyda nifer yr emoji 🔥 sy'n cyfateb.

--- /code ---

language: python filename: main.py line_numbers: true line_number_start: 7

--- /task ---

--- task ---

**Test:** Test your project a few times. Make sure you understand how the code works.

--- /task ---

### Choose the number of sides on the dice

Upgrade your dice so that the user can choose the maximum number.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Lots of games use many-sided dice. In the physical world, dice are made from regular geometric shapes. Common dice include D6, D12, and D20. On a computer, you can generate a <span style="color: #0faeb0">random</span> number to make a fair dice with any number of sides.</p>

--- task ---

**Cyngor:** Mae newidynnau'n ddefnyddiol pan fydd angen i chi ddefnyddio'r un gwerth fwy nag unwaith yn eich cod. Mae rhoi enw synhwyrol i'ch newidynnau yn gwneud eich cod yn haws ei ddeall hefyd.

**Add** code to ask the user for the biggest number on their dice and then save the result in a variable called `max` and `print` the number chosen into the output area:

Uwchraddiwch eich dis er mwyn i'r defnyddiwr allu dewis y rhif mwyaf.

When you get input from the user, Python treats it as text. But, `randint` needs an 'integer' (a positive whole number). The `int` function turns the user input into an integer.

--- code ---
---
Mae'r swyddogaeth `input()` yn gofyn cwestiwn i'r defnyddiwr, ac yn dychwelyd eu hateb.
line_highlights: 11-12
---

# Rhowch ddiffiniadau swyddogaethau o dan fan hyn

Ychwanegwch god i ofyn i'r defnyddiwr am y rhif mwyaf ar ei ddis ac yna cadw'r canlyniad mewn newidyn o'r enw `mwyaf` a phrintio'r rhif sy'n cael ei ddewis yn yr ardal allbwn:

--- /code ---

language: python filename: main.py line_numbers: true line_number_start: 7

--- /task ---

--- task ---

**Test:** Run your project. When the program reaches the `input` line, it will wait for you to enter a response before continuing. Type your response and then press <kbd>Enter</kbd>, this will allow the program to collect your response. Try it again with a different `input` number.

--- /task ---

--- save ---
