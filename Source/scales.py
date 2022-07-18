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
    (Major, Minor, 
    MajorPentatonic, MinorPentatonic, 
    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian) = range(11) 

formula_dict = {
    ScaleType.Major: ['w', 'w', 'h', 'w', 'w', 'w', 'h'],
    ScaleType.Minor: ['w', 'h', 'w', 'w', 'h', 'w', 'w'],
    # Modes
    ScaleType.Ionian: ['w', 'w', 'h', 'w', 'w', 'w', 'h'],
    ScaleType.Dorian: ['w', 'h', 'w', 'w', 'w', 'h', 'w'],
    ScaleType.Phrygian: ['h', 'w', 'w', 'w', 'h', 'w', 'w'],
    ScaleType.Lydian: ['w', 'w', 'w', 'h', 'w', 'w', 'h'],
    ScaleType.Mixolydian: ['w', 'w', 'h', 'w', 'w', 'h', 'w'],
    ScaleType.Aeolian: ['w', 'h', 'w', 'w', 'h', 'w', 'w'],
    ScaleType.Locrian: ['h', 'w', 'w', 'h', 'w', 'w', 'w'],
}

def scale_from_steps(root, formula):
    notes = [Note.from_index(root.value)] # Add root first
    
    step_counter = 0
    for step in formula[:-1]: # The last step will be the root
        if (step.lower() == 'h') or (step.lower() == 'half'):
            step_counter += 1
        if (step.lower() == 'w') or (step.lower() == 'whole'):
            step_counter += 2

        notes.append(Note.from_index(root.value + step_counter))

    return notes

def scale_from_intervals(root, formula):   
    return [Note.from_index(root.value + interval.value) for interval in formula]

def form_scale(root, s_type):

    notes, formula = [], []

    if(s_type == ScaleType.MajorPentatonic):
        formula = [Interval.Unison, Interval.M2, Interval.M3, Interval.P5, Interval.M6]
        notes = scale_from_intervals(root, formula)

    elif(s_type == ScaleType.MinorPentatonic):
        formula = [Interval.Unison, Interval.m3, Interval.P4, Interval.P5, Interval.m7]
        notes = scale_from_intervals(root, formula)

    # if not in dict - raise error

    else:
        formula = formula_dict[s_type]
        notes = scale_from_steps(root, formula)   
    
    # Determine the scale formula
    

 

    return notes, formula

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
    print(str(scale.formula))
    print(scale.formula)
    print(scale.type)

if __name__ == '__main__':
    main()