from miditime.miditime import MIDITime


class Generator(object):

    def __init__(self, bpm):
        self.bmp = bpm



    def generate(self,file,path):
        midi = MIDITime(self.bmp,path+file+'.mid',6,3,1)
        notes = [
            [0, 60, 127, 6],
            [0.5, 50, 100, 1],
            [0.5, 57, 100, 0.6],
            [1.4, 50, 100, 1.9],
            [1.4, 57, 100, 1.5],
            [1.9, 50, 100, 2.4],
            [1.9, 57, 100, 2.0],
            [2.4, 50, 100, 2.9],
            [2.4, 57, 100, 2.5],

            [2.5, 56, 100, 3.5],
            [3.5, 55, 100, 4.1],
            [4.1, 56, 100, 4.7],
            [4.7, 55, 100, 5.3],

            [5.9, 57, 100, 6.9],
            [7.5, 56, 100, 8.1],
            [8.7, 57, 100, 9.3],
            [9.6, 56, 100, 10.2]

        ]
        midi.add_track(notes)
        midi.save_midi()