from miditime.miditime import MIDITime
from musicgenerator.chords import random_value_dict, progression
from random import randint
import random
import copy
import math


class Generator(object):
    def __init__(self, bpm, length, octave):
        self.bmp = bpm
        self.lenghth = length
        self.shift = 12 * (octave - 1)
        self._math = 'none'
        self.speed = round(random.uniform(0.3, 1.5), 1)

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, fun):
        self._math = fun

    def prep_time(self, time, chord):
        newchord = copy.deepcopy(chord)
        for i in range(len(chord)):
            newchord[i][0] = time
            newchord[i][1] += self.shift
            newchord[i][3] = self.speed
        return newchord

    def dict_progression(self, x):
        return {
            'A': progression('D', 'E'),
            'B': progression('W#', 'E'),
            'C': progression('F', 'G'),
            'D': progression('G', 'A'),
            'E': progression('A', 'B'),
            'F': progression('Qb', 'C'),
            'G': progression('C', 'D'),
            'Q': progression('C', 'D'),
            'W': progression('E', 'E')
        }.get(x)

    def create_sample(self):
        chordper_sample = randint(5, 10)
        sample = []
        endtime = 1.0
        chord = random_value_dict()
        for i in range(chordper_sample):
            edited = self.prep_time(endtime, chord[1])
            endtime = edited[0][3] + edited[0][0]
            sample.extend(edited)
            chord = self.dict_progression(chord[0][:1])
        return sample

    def time_fix_sample(self, sample, endtime):
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
        totaltime = self.lenghth * (self.bmp // 60)
        if self._math == 'none':
            notes = self.generate_chords_music(notes, totaltime)
        else:
            notes = self.generate_math(totaltime, notes)

        midi.add_track(notes)
        midi.save_midi()

    def generate_math(self, totaltime, notes):
        time = 0
        while totaltime > time:
            pitch = int(abs(getattr(math, self._math)(time / 10)) * 50 + self.shift)
            note = [time, pitch, 127, self.speed]
            notes.append(note)
            time += self.speed
        return notes

    def generate_chords_music(self, notes, totaltime):
        sample = self.create_sample()
        notes.extend(sample)
        endtime = self.speed + sample[len(sample) - 1][0]
        while totaltime > endtime:
            fix = self.time_fix_sample(sample, endtime)
            notes.extend(fix)
            endtime = self.speed + fix[len(fix) - 1][0]
        return notes
