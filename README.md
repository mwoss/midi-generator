# MIDI generator
Simple as hell MIDI piano generator :3. What I can tell, just try it!

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
