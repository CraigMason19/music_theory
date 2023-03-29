#-------------------------------------------------------------------------------
# Name:        chords.py
#
# Notes:       A collection of chord shapes.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from enum import Enum

from notes import Note
from scales import Scale, ScaleType

# Just out of interest
cadence_dict = {"Plagal": "IV->I",
                "Authentic": "V->I",
}

class ChordType(Enum):
    (Major, Minor, Diminished, Seven) = range(4)

class Chord():
    def __init__(self, note, chord_type):
        self.root, self.chord_type = note, chord_type
    
    def __eq__(self, other):
        try:
            return self.root == other.root and self.chord_type == other.chord_type
        except AttributeError:
            return False

    def __str__(self):
        if self.chord_type == ChordType.Diminished:
            return f"{self.root}dim"

        elif self.chord_type == ChordType.Minor:
            return f"{self.root}m"

        elif self.chord_type == ChordType.Seven:
            return f"{self.root}7"

        return f"{self.root}M"

    def __repr__(self):
        return f"Chord({self.root}, {self.chord_type})"
 

def main():
    c = Chord(Note.C, ChordType.Seven)

    print(str(c))
    print(repr(c))

if __name__ == '__main__':
    main()