# Music generator (Python)
Solution for Python course at AGH UST.

## Example of usage
```shell
>py run.py music C:\Users\user1\ --bmp 128 --length 20 --octave 3
>py run.py music C:\Users\user1\ --bmp 128 --length 20 --octave 3 --math sin
or just run it with above arguments in pycharm or sth like that
```
```
1st arg -> file name
2nd arg -> directory of storage output file
--bmp [bmp] -> beats per second, range(50,250), required
--length [length] -> length of music, range(10-40), required
--octave [octave] -> notes shift, range (1-7), required
--math [mathf] -> generate music using trigonometrical functions instead of using chord progression samples,
                  choices=(sin,cos),required = False
```
## Requirements
 - Python 3.X
 - Miditime library installed (for example: https://pypi.python.org/pypi/miditime or just use terminal and input pip install miditime)

## Task
```Programowanie w jezyku Python 2016/2017 zadanie 1
Uporczywe narkotyczne melodie potrafią czasem na długo przylgnąć do umysłu.
Napisz program, który generuje narkotyczne melodie. Program powinien generować różne melodie w zależności od tego, jakie użytkownik poda opcje. Użytkownik będzie tak długo modyfikował opcje programu aż wygenerowana melodia utkwi mu na stałe w głowie.

Melodie te powinny być generowane w postaci plików midi i zapisywane na dysku twardym, przy czym użytkownik powinien mieć możliwość podania lokalizacji. Obsługa karty dźwiękowej w celu odtworzenia wygenerowanej melodii nie jest konieczna. Można użyć dowolnej biblioteki do obslugi formatu midi, przykladowo https://pypi.python.org/pypi/miditime


Program ten powinien wykorzystywać następujące elementy:
 - klasy
 - funkcje
 - parsowanie argumentów linii poleceń za pomocą modułu argparse ze standardowej biblioteki
 - zewnętrzna biblioteka do obsługi formatu midi

Tresc zadania w Google Drive: https://goo.gl/dbfwo3

Termin oddania zadania: 3 kwietnia 2017, 20:00
```