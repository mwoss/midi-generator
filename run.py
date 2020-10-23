import argparse

from musicgenerator import main
from musicgenerator.pianomidigenerator import PianoMidiGenerator


def main():
    parser = argparse.ArgumentParser('Narcotic melody generator :)')
    parser.add_argument('file', type=str, help='Output file name')
    parser.add_argument('pathFile', type=str, help='Location where output file will be stored')
    parser.add_argument('--bmp', type=int, choices=range(50, 250), help='BMP value (50-250)')
    parser.add_argument('--length', type=int, choices=range(10, 40), help='Length of file in seconds(10-40)')
    parser.add_argument('--octave', type=int, choices=range(1, 7), help='Octave mostly used in output file(1-7)')
    parser.add_argument('--math', type=str, choices=('sin', 'cos'), help='Available functions: sin, cos')

    arguments = parser.parse_args()
    generator = PianoMidiGenerator(arguments.bmp, arguments.length, arguments.octave)
    if arguments.math is not None:
        generator.math = str(arguments.math)
    generator.generate(arguments.file, arguments.pathFile)


if __name__ == '__main__':
    main()
