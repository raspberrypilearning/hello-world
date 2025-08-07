## Uzyskaj dane wejściowe

Za pomocą `input()`{:.language-python} możesz poprosić osobę korzystającą z Twojego programu o wprowadzenie tekstu.

--- task ---

Zmień swoją funkcję tak, aby prosiła osobę korzystającą z Twojego programu o podanie liczby boków kostki, i zapisz ją jako zmienną.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 17-18
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1,6) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Kliknij przycisk **Uruchom** i wpisz liczbę boków. Upewnij się, że naciśniesz klawisz <kbd>Enter</kbd> po wpisaniu liczby boków. Oto co powinieneś zobaczyć po uruchomieniu kodu.

<div class="c-project-output">
```
Hello 🌍🌎🌏
Welcome to Python 🐍
Python 🐍 is good at maths!
12345678987654321
The date and time is 2023-11-21 16:20:41.323000
How many sides on your dice?:
20 
That is a D 20
You rolled a 1 🔥
```

--- /task ---

Dane wejściowe są zawsze przechowywane jako tekst, ale musimy użyć danych wejściowych przechowywanych w `max`, aby określić największą liczbę, jaka może zostać wyrzucona.

--- task ---

`max` jest ciągiem znaków, więc należy go zamienić na liczbę całkowitą `int()`{:.language-python}.


--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 19
---
# Function definitions
def roll_dice(): max = input('How many sides on your dice?:') print(f'That is a D {max}') roll = randint(1, int(max)) print(f'You rolled a {roll} {fire * roll}')

--- /code ---

--- /task ---

--- task ---

**Test:** Kliknij przycisk **Uruchom** kilka razy. Sprawdź, czy kostka za każdym razem wyrzuca losową liczbę.

--- /task ---

