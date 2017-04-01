from miditime.miditime import MIDITime


class Generator(object):
    def __init__(self, bpm):
        self.bmp = bpm

    def generate(self, file, path):
        midi = MIDITime(self.bmp, path + file + '.mid', 6, 3, 1)
        notes = [

            # Testing chords which ill be using to create music

        ]
        midi.add_track(notes)
        midi.save_midi()
