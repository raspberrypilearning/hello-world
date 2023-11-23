## Dweud helo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae'n draddodiadol ysgrifennu rhaglen i allbynnu 'Helo fyd!' pan fyddwch yn dysgu iaith raglennu newydd.
</div>
<div>

![Ardal allbwn Trinket yn dangos y ddwy linell wedi'u printio o destun ac emoji.](images/say_hello.png){:width="200px"}

</div>
</div>

--- task ---

Open the [Hello 🌍🌎🌏 starter project](https://editor.raspberrypi.org/en/projects/hello-world-starter){:target="_blank"}. The code editor will open in another browser tab.

![The code editor with project starter code on the left in the code area. Mae'r ardal allbwn wag ar y dde.](images/starter_project.png)

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

--- collapse ---

---
line_highlights: 12
---

If you're working on a Raspberry Pi using Chromium, you may not see the emojis. You need to install a font that supports them.

Open a terminal and then type:

```bash
sudo apt install fonts-noto-color-emoji
```

Dewch o hyd i'r llinell `# Rhowch y cod i'w redeg o dan fan hyn`.

--- /collapse ---

### Print hello

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Lines beginning with a `#` are <span style="color: #0faeb0">**comments**</span>. They explain what the code will do. Comments are ignored by Python.
</p>

The `import` lines at the start of the code tell Python that you are going to use code you didn't write.

language: python filename: main.py line_numbers: true line_number_start: 11

--- task ---

Find the `# Put code to run below here` line.

Click below that line. The flashing `|` is the cursor and shows where you will type.

--- /task ---

--- task ---

Type the code to `print()` Hello to the screen:

**Tip:** When you type an opening bracket `(` or opening apostrophe `'` the code editor will automatically add a closing bracket `)` or closing apostrophe`'`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
title: Teipio nodau arbennig ar fysellfwrdd y DU neu UDA
---

# Rhowch y cod i'w redeg o dan fan hyn
**Difa chwilod:** Os ydych chi'n cael gwall, gwnewch yn fanwl siŵr bod eich cod yn gywir. Yn yr enghraifft hon, mae'r dyfynodau sengl o amgylch `Helo` ar goll felly dydy Python ddim yn gwybod mai testun sydd i fod yno.

--- /code ---

--- collapse ---
---
line_highlights: 12
---

On a UK or US keyboard, the left `(` and right `)` round brackets are on the <kbd>9</kbd> and <kbd>0</kbd> keys. To type a left round bracket, hold down the <kbd>Shift</kbd> key (next to <kbd>Z</kbd>) and then tap <kbd>9</kbd>. The single quote `'` is on the same row as the <kbd>L</kbd> key, just before the <kbd>Enter</kbd> key. The comma `,` is next to the <kbd>M</kbd>.

--- /collapse ---

--- /task ---

--- task ---

**Test:** Click on the **Run** button to run your code. In the code editor, the output will appear on the right:

![The Run icon highlighted with 'Hello' showing in the output area. ](images/run_hello.png)

**Debug:** If you get an error then check your code really carefully. In this example, the single quotes around `Hello` are missing so Python doesn't know it is supposed to be text.

![The Code Editor with missing single quotes and error 'NameError: name 'Hello' is not defined on line 18 in main.py.](images/hello_error.png)

--- /task ---

## title: Wela' i ddim yr emoji

In Python, a **variable** is used to store values such as text or numbers. Variables make it easier for humans to read code. You can use the same variable in lots of places in your code. Choosing a sensible name for a variable makes it easier for you to remember what it is for.

language: python filename: main.py line_numbers: true line_number_start: 11

--- task ---

In your code editor, scroll to the lines with the emojis stored into two different variables. Find the variable `world`, which stores the text '🌍🌍🌍'.

--- /task ---

--- task ---

You can `print()` more than one item at a time by including a comma `,` in between the items. `print()` will add a space between each item.

**Profi:** Rhedwch eich cod i weld y canlyniad:

--- code ---
---
Mae emoji'n gallu edrych yn wahanol ar wahanol gyfrifiaduron, felly efallai na fydd eich un chi yn edrych union yr un fath.
line_highlights: 3
---

# Rhowch y cod i'w redeg o dan fan hyn
**Difa chwilod:** Gwnewch yn siŵr eich bod wedi ychwanegu coma rhwng yr eitemau yn `print()` ac wedi sillafu `byd` yn gywir.

--- /code ---

**Tip:** `'Hello'` is a text string because it has single quotes around it, whereas `world` is a variable so the value stored in it will be printed.

--- /task ---

--- task ---

Newidiwch y llinell `from emoji import *` i:

![The updated line of code in the code area with the word 'Hello' followed by three world emojis showing in the output area.](images/run_hello_world.png)

language: python filename: main.py line_numbers: true line_number_start: 3

from noemoji import *

This example is missing the comma `,`. It's small but very important!

![The code editor with missing single quotes and error 'SyntaxError: bad input on line 18 in main.py' displayed.](images/comma_error.png)

--- /task ---

--- task ---

Ychwanegwch linell arall at eich cod i brintio mwy o destun ac emoji:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 12
line_highlights: 13
---

print('Helo', byd)    
print('Croeso i', python)

--- /code ---

**Cyngor:** Mae'r cod sydd angen i chi ei deipio wedi'i amlygu mewn lliw goleuach. Mae cod heb ei amlygu yn eich helpu i weld lle mae angen i chi ychwanegu'r cod newydd.

--- /task ---

--- task ---

**Profi:** Cliciwch **run**.

![Y llinell cod ychwanegol yn yr ardal cod gyda'r gair 'Helo' wedi'i ddilyn gan dri emoji byd a'r geiriau 'Croeso i' wedi'u dilyn gan emoji neidr a bysellfwrdd yn yr ardal allbwn.](images/run_multiple.png)

**Cyngor:** Mae'n syniad da rhedeg eich cod ar ôl pob newid er mwyn gallu datrys problemau'n gyflym.

**Difa chwilod:** Gwnewch yn siŵr bod gennych chi gromfachau, dyfynodau, comas a sillafu cywir. Mae angen bod yn fanwl gywir yn Python.

--- /task ---

Os oes gennych chi gyfrif Trinket, fe allwch chi glicio'r botwm **Remix** i gadw copi yn eich llyfrgell `My Trinkets`.

--- save ---
