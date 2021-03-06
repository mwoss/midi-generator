import random

chords_dict = {
    'C': [[1, 24, 100, 3],
          [1, 28, 100, 3],
          [1, 31, 100, 3]],

    'C1': [[1, 24, 100, 3],
           [1, 31, 100, 3],
           [1, 40, 100, 3]],

    'C2': [[1, 24, 100, 3],
           [1, 40, 100, 3],
           [1, 43, 100, 3]],
    # D
    'D': [[1, 26, 100, 3],
          [1, 30, 100, 3],
          [1, 33, 100, 3]],

    'D1': [[1, 26, 100, 3],
           [1, 33, 100, 3],
           [1, 42, 100, 3]],

    'D2': [[1, 26, 100, 3],
           [1, 42, 100, 3],
           [1, 45, 100, 3]],
    # E
    'E': [[1, 28, 100, 3],
          [1, 32, 100, 3],
          [1, 35, 100, 3]],

    'E1': [[1, 28, 100, 3],
           [1, 35, 100, 3],
           [1, 44, 100, 3]],

    'E2': [[1, 28, 100, 3],
           [1, 44, 100, 3],
           [1, 47, 100, 3]],
    # F
    'F': [[1, 29, 100, 3],
          [1, 33, 100, 3],
          [1, 36, 100, 3]],
    'F1': [[1, 29, 100, 3],
           [1, 36, 100, 3],
           [1, 45, 100, 3]],

    'F2': [[1, 29, 100, 3],
           [1, 45, 100, 3],
           [1, 48, 100, 3]],

    'F3': [[1, 29, 100, 3],
           [1, 48, 100, 3],
           [1, 57, 100, 3]],

    'W#': [[1, 30, 100, 3],
           [1, 34, 100, 3],
           [1, 37, 100, 3]],

    'W#1': [[1, 30, 100, 3],
            [1, 37, 100, 3],
            [1, 46, 100, 3]],

    'W#2': [[1, 30, 100, 3],
            [1, 46, 100, 3],
            [1, 49, 100, 3]],

    'W#3': [[1, 30, 100, 3],
            [1, 49, 100, 3],
            [1, 58, 100, 3]],
    # G
    'G': [[1, 31, 100, 3],
          [1, 35, 100, 3],
          [1, 38, 100, 3]],

    'G1': [[1, 31, 100, 3],
           [1, 38, 100, 3],
           [1, 47, 100, 3]],

    'G2': [[1, 31, 100, 3],
           [1, 47, 100, 3],
           [1, 50, 100, 3]],

    'G3': [[1, 31, 100, 3],
           [1, 50, 100, 3],
           [1, 59, 100, 3]],
    # A
    'A': [[1, 33, 100, 3],
          [1, 37, 100, 3],
          [1, 40, 100, 3]],

    'A1': [[1, 33, 100, 3],
           [1, 40, 100, 3],
           [1, 49, 100, 3]],

    'A2': [[1, 33, 100, 3],
           [1, 49, 100, 3],
           [1, 52, 100, 3]],
    # B
    'B': [[1, 35, 100, 3],
          [1, 39, 100, 3],
          [1, 42, 100, 3]],

    'B1': [[1, 35, 100, 3],
           [1, 42, 100, 3],
           [1, 51, 100, 3]],

    'B2': [[1, 35, 100, 3],
           [1, 51, 100, 3],
           [1, 54, 100, 3]],

    'Qb': [[1, 34, 100, 3],
           [1, 38, 100, 3],
           [1, 41, 100, 3]],

    'Qb1': [[1, 34, 100, 3],
            [1, 41, 100, 3],
            [1, 50, 100, 3]],

    'Qb2': [[1, 34, 100, 3],
            [1, 50, 100, 3],
            [1, 53, 100, 3]]
}


def random_value_dict():
    rand = random.choice(list(chords_dict.items()))
    return rand


# def randTimeOctave(time, octave):
#     randChord = random.choice(list(chordsDict.values()))
#     start = time  # round(random.uniform(-1.5,1.0),1) #rand in range 0-1
#     end = round(random.uniform(1.0, 2.0), 1)  # rand in range 1,5-4
#     for i in range(len(randChord)):
#         randChord[i][0] = time + start
#         randChord[i][1] = randChord[i][1] + (12 * (octave - 1))
#         randChord[i][3] = time + end
#
#     return randChord

def progression(chord1, chord2):
    while True:
        prog_chord = random_value_dict()
        if prog_chord[0].startswith((chord1, chord2)):
            return prog_chord
