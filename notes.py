NOTES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H')

CHORDS = {
    'C': {'C', 'E', 'G'},
    'C#': {'C#', 'F', 'G#'},
    'D': {'D', 'F#', 'A'},
    'D#': {'D#', 'G', 'B'},
    'E': {'E', 'G#', 'H'},
}


def succ(note):
    try:
        return NOTES[NOTES.index(note)+1]
    except IndexError:
        return NOTES[0]
    
