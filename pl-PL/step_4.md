## Rzuć kostką 🎲

Funkcje to bloki kodu wykonujące określone zadania. Można ich używać wiele razy.

Oto przykład funkcji:

--- code ---
---
language: python
line_numbers: false
---
def add_one_and_one(): x = 1 + 1 print(x)

--- /code ---

Nazwa tej funkcji to `add_one_and_one`{:.language-python}.

Kod zadania, które ma wykonać funkcja, musi być **wcięty**, co oznacza, że przed każdym wierszem kodu należy dodać **cztery spacje**.

**Wywołanie** funkcji powoduje uruchomienie zawartego w niej kodu. Funkcję **wywołujesz** używając jej nazwy. W tym przypadku `add_one_and_one()`{:.language-python}.


--- task ---

Poszukaj komentarza w pliku **main.py**, w którym jest napisane

`# Definicje funkcji`{:.language-python}.

Utwórz funkcję o nazwie `roll_dice()`{:.language-python}, która wyświetla liczbę 4.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 18-20
---
# Definicje funkcji
def roll_dice(): print(f'You rolled a {4}')

# Put code to run under here

--- /code ---

--- /task ---

--- task ---

Następnie wywołaj funkcję znajdującą się na dole kodu.

--- code ---
---
language: python line_numbers: true line_number_start: 26
line_highlights: 27
---
print(f'The date and time is {datetime.now()}') roll_dice()

--- /code ---

--- /task ---

--- task ---

**Test:** Uruchom swój projekt kilka razy, aby zobaczyć wynik rzutu kostką za każdym razem — zawsze będzie to 4.

--- /task ---

--- task ---

Inny moduł o nazwie `random`{:.language-python} może być używany do tworzenia liczb losowych. Zmień kod, aby użyć funkcji `randint`{:.language-python} do wybrania losowej liczby z zakresu od 1 do 6 w rzucie kostką.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Definicje funkcji
def roll_dice(): print(f'You rolled a {randint(1, 6)}')

--- /code ---

--- /task ---

--- task ---

**Test:** Kliknij przycisk **Uruchom**. Teraz, gdy uruchomisz swój kod, za każdym razem będzie wybierana nowa losowa liczba z zakresu od 1 do 6.

--- /task ---

W Pythonie można mnożyć ciągi znaków, takie jak emotikony lub całe słowa, przez liczbę, dzięki czemu zostaną one wyświetlone kilka razy.

--- task ---

Zmień swoją funkcję tak, aby przechowywała liczbę losową w zmiennej o nazwie `roll`{:.language-python}.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 19
---
# Definicje funkcji
def roll_dice(): roll = randint(1,6)

--- /code ---

--- /task ---

--- task ---

Pomnóż liczbę losową zapisaną w `roll`{:.language-python} przez emotkę 🔥 i wyświetl wynik.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 20
---
# Function definitions
def roll_dice(): roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Kliknij przycisk **Uruchom**. Kod wyjściowy powinien wyglądać mniej więcej tak:

```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
27
The date and time is 2025-10-24 12:41:45.140000
You rolled a 4 🔥🔥🔥🔥
```

--- /task ---