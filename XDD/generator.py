from miditime.miditime import MIDITime
from XDD.chords import randomValueDict, progresion
from random import randint
import random
import copy
from math import sin


class Generator(object):
    def __init__(self, bpm, length, octave):
        self.bmp = bpm
        self.lenghth = length
        self.octave = octave
        self.shift = 12 * (octave - 1)
        self.speed = round(random.uniform(0.3, 2), 1)

    def prepTime(self, time, chord):
        newchord = copy.deepcopy(chord)
        for i in range(len(chord)):
            newchord[i][0] = time
            newchord[i][1] += self.shift
            newchord[i][3] = self.speed
        return newchord

    def f(self, x):
        return {
            'A': progresion('D', 'E'),
            'B': progresion('W#', 'E'),
            'C': progresion('F', 'G'),
            'D': progresion('G', 'A'),
            'E': progresion('A', 'B'),
            'F': progresion('Qb', 'C'),
            'G': progresion('C', 'D'),
            'Q': progresion('C', 'D'),
            'W': progresion('E', 'E')
        }.get(x)

    def createSample(self):
        chordperSample = randint(5, 10)
        sample = []
        endtime = 1.0
        chord = randomValueDict()
        for i in range(chordperSample):
           #print(chord)
            edited = self.prepTime(endtime, chord[1])
            endtime = edited[0][3] + edited[0][0]
            sample.extend(edited)
            str = chord[0]
            chord = self.f(str[:1])
        return sample

    def timeFixSample(self, sample, endtime):
        length = len(sample) - 1
        fix = copy.deepcopy(sample)
        for i in range(0, length):
            if fix[i][0] == fix[i + 1][0]:
                fix[i][0] = endtime
            else:
                fix[i][0] = endtime
                endtime += self.speed

        fix[length][0] = fix[length - 1][0]
        return fix

    def generate(self, file, path):
        midi = MIDITime(self.bmp, path + file + '.mid')
        notes = []
        totalTime = self.lenghth * (self.bmp // 60)

        sample = self.createSample()
        notes.extend(sample)
        endtime = self.speed + sample[len(sample) - 1][0]
        print(endtime)
        while totalTime > endtime:
            fix = self.timeFixSample(sample, endtime)
            notes.extend(fix)
            endtime = self.speed + fix[len(fix) - 1][0]
        # time = 0
        # while totalTime > time:
        #     pitch = int(abs(sin(time / 10)) * 50 + 30)  # random.randint(0, 60) + 30
        #     note = [time, pitch, 127, random.randint(0, 12 - 10) + 1]
        #     notes.append(note)
        #     time += random.randint(0, 4 - random.randint(0, 3))



        midi.add_track(notes)
        midi.save_midi()
