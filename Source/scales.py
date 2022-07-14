#-------------------------------------------------------------------------------
# Name:        scales.py
#
# Notes:       A collection of scale types. 
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from enum import Enum
from notes import Note, Interval, notes_to_string, intervals_to_string


class ScaleType(Enum):
    Major, Minor, MajorPentatonic, MinorPentatonic = range(4) 

def scale_from_notes(root, formula):
    pass

def scale_from_steps(root, formula):
    pass

#For example, the C major scale is C-D-E-F-G-A-B. To form the C Major pentatonic scale,
# # you would take the 1 = C, 2 = D, 3 = E, 5 = G, 6 = A. To form the C minor pentatonic 
# #scale, you would take the 1 = C, b3 = Eb, 4 = F, 5 = G, b7 = Bb.
def form_scale(root, s_type):
    notes, formula = [], []

    # Determine the scale formula
    if(s_type == ScaleType.Major):
        formula = ['w', 'w', 'h', 'w', 'w', 'w', 'h']

    if(s_type == ScaleType.Minor):
        formula = ['w', 'h', 'w', 'w', 'h', 'w', 'w']

    if(s_type == ScaleType.MajorPentatonic):
        formula = ['1', '2', '3', '5', '6']
        formula = [Interval.Unison, Interval.M2, Interval.M3, Interval.P5, Interval.M6]

    if(s_type == ScaleType.MinorPentatonic):
        formula = ['1', 'b3', '4', '5', 'b7']
        formula = [Interval.Unison, Interval.m3, Interval.P4, Interval.P5, Interval.m7]


    # Determine the notes from the correct formula
    return [root], intervals_to_string(formula)


class Scale:
    def __init__(self, root, s_type):
        self.notes, self.formula = form_scale(root, s_type) # calculate notes
        self.type = s_type

    @property
    def root(self):
        return self.notes[0].name

    def __str__(self):
        return f"{self.notes[0].name} {self.type.name}: { notes_to_string(self.notes) }"

    def __repr__(self):
        return f"Scale({self.notes[0]}, {self.type})"

def main():
    scale = Scale(Note.A, ScaleType.MajorPentatonic)

    print(str(scale))
    print(repr(scale))
    print(scale.root)
    print(scale.formula)
    print(scale.type)

if __name__ == '__main__':
    main()