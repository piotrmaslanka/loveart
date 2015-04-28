from notes import succ, CHORDS
from itertools import product

class Chordophone(object):
    """A n-string chordophone with particular tuning and number of frets"""
    def __init__(self, tuning, frets=10):
        """Tuning is a tuple of note names"""
        self.tuning = tuning
        self.strings = len(tuning)
        self.frets = frets
        
        
    def play(self, sequence):
        """sequence is a tuple of fret number on which
        string is pressed. If string is not played, None is passed
        @return: set of notes played"""
        
        notes = set()
        for base_tuning, fretno in zip(self.tuning, sequence):
            if fretno == None: continue                
            if fretno == 'X': continue
            note = base_tuning                
            for i in xrange(0, fretno): note = succ(note)
            notes.add(note)
            
        return notes
    
    
p = Chordophone('EADGHE')

play = ['X'] + range(0, 8)
play2 = range(0, 8)

for allsets in product(play, play, play2, play2, play, play):
    s = p.play(allsets)
    if s == CHORDS['C']:
        print '%s is C major' % (allsets, )

