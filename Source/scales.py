#-------------------------------------------------------------------------------
# Name:        scales.py
#
# Notes:       A collection of scale types. 
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum
from notes import Note, Interval, notes_to_string, intervals_to_string

class ScaleType(Enum):
    (Major, Minor, 
    MajorPentatonic, MinorPentatonic, 
    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian) = range(11) 

    @classmethod    
    def items(cls):
        return [n for n in cls]

    @classmethod
    def random(cls):
        return random.choice(cls.items())

formula_step_dict = {
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

formula_interval_dict = {
    ScaleType.MajorPentatonic: [Interval.Unison, Interval.M2, Interval.M3, Interval.P5, Interval.M6],
    ScaleType.MinorPentatonic: [Interval.Unison, Interval.m3, Interval.P4, Interval.P5, Interval.m7],
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

class Scale:
    def __init__(self, root, scale_type):
        self.root, self.type = root, scale_type
        self._form()

    def _form(self):
        if(self.type in formula_step_dict):
                self.formula = formula_step_dict[self.type]
                self.notes = scale_from_steps(self.root, self.formula)  

        elif(self.type in formula_interval_dict):
                self.formula = formula_interval_dict[self.type]
                self.notes = scale_from_intervals(self.root, self.formula)  

        else:
            raise ValueError(f'Scale is not in either formula dictionary {self.type}')

    @classmethod
    def random(cls):
        return Scale(Note.random(), ScaleType.random())

    def __str__(self):
        return f"{self.notes[0].name} {self.type.name}: { notes_to_string(self.notes) }"

    def __repr__(self):
        return f"Scale({self.notes[0]}, {self.type})"

def main():
    # scale = Scale(Note.A, ScaleType.Dorian)
    scale = Scale.random()

    print("Scale:")
    print(f"\t{scale}")
    print(f"\t{repr(scale)}")

    print(f"\tRoot -> {scale.root}")
    print(f"\tType -> {scale.type})")
    print(f"\tFormula -> {scale.formula})")
    print(f"\tNotes -> {notes_to_string(scale.notes)}")


if __name__ == '__main__':
    main()