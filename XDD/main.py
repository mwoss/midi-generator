from XDD.generator import Generator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Output file name')
parser.add_argument('pathFile', type=str, help='Location where output file will be stored')
parser.add_argument('--bmp', type=int, choices=range(50, 250), help='BMP value')
parser.add_argument('--length', type=int, choices=range(5, 60), help='Length of file in seconds')
parser.add_argument('--octave', type=int, choices=range(1, 7), help='Octave mostly used in output file')


def main():
    arguments = parser.parse_args()
    print(arguments.file, arguments.pathFile, arguments.bmp)
    midigenerator = Generator(arguments.bmp)
    midigenerator.generate(arguments.file, arguments.pathFile)
