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
    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian,
    Blues, HarmonicMinor, MelodicMinor) = range(14) 

    @classmethod    
    def items(cls):
        return [n for n in cls]

    @classmethod
    def random(cls):
        return random.choice(cls.items())

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'ScaleType.{self.name}'

# 3 ways to load a scale
formula_step_dict = {
    ScaleType.Major: ['w', 'w', 'h', 'w', 'w', 'w', 'h'],
    ScaleType.Minor: ['w', 'h', 'w', 'w', 'h', 'w', 'w'],
    # Modes
    ScaleType.Ionian: ['w', 'w', 'h', 'w', 'w', 'w', 'h'], # Major
    ScaleType.Dorian: ['w', 'h', 'w', 'w', 'w', 'h', 'w'],
    ScaleType.Phrygian: ['h', 'w', 'w', 'w', 'h', 'w', 'w'],
    ScaleType.Lydian: ['w', 'w', 'w', 'h', 'w', 'w', 'h'],
    ScaleType.Mixolydian: ['w', 'w', 'h', 'w', 'w', 'h', 'w'],
    ScaleType.Aeolian: ['w', 'h', 'w', 'w', 'h', 'w', 'w'], # Minor
    ScaleType.Locrian: ['h', 'w', 'w', 'h', 'w', 'w', 'w'],
}

formula_interval_dict = {
    ScaleType.MajorPentatonic: [Interval.Unison, Interval.M2, Interval.M3, Interval.P5, Interval.M6],
    ScaleType.MinorPentatonic: [Interval.Unison, Interval.m3, Interval.P4, Interval.P5, Interval.m7],
}

formula_numeric_dict = {
    ScaleType.Blues: ['1', 'b3', '4', 'b5', '5', 'b7'],
    ScaleType.HarmonicMinor: ['1', '2', 'b3', '4', '5', 'b6', '7'],
    ScaleType.MelodicMinor: ['1', '2', 'b3', '4', '5', '6', '7'],
}

def scale_from_steps(root, formula):
    notes = [Note.from_index(root.value)] # Add root first
    
    step_counter = 0
    for step in formula[:-1]: # The last step will be the root
        step = step.lower()
        if (step == 'h') or (step == 'half'):
            step_counter += 1
        if (step == 'w') or (step == 'whole'):
            step_counter += 2

        notes.append(Note.from_index(root.value + step_counter))

    return notes

def formula_from_steps(formula):
    notes = [Interval.Unison] # Add root first
    
    step_counter = 0
    for step in formula[:-1]: # The last step will be the root
        step = step.lower()
        if (step == 'h') or (step == 'half'):
            step_counter += 1
        if (step == 'w') or (step == 'whole'):
            step_counter += 2

        notes.append(Interval.from_index(step_counter))

    return notes

def formula_from_numerics(formula):
    return [Interval.from_numeric(n) for n in formula]

def scale_from_intervals(root, interval_formula):   
    return [Note.from_index(root.value + interval.value) for interval in interval_formula]

class Scale:

    def __init__(self, root, scale_type):
        self.root, self.type = root, scale_type
        self._construct()

    # private so not to pollute the __init__ method
    def _construct(self):
        if(self.type in formula_interval_dict):
            self.creation_formula = formula_interval_dict[self.type]
            self.interval_formula = self.creation_formula

        # If the formula is not in interval form, convert it first and then construct it from there
        elif(self.type in formula_step_dict):    
            self.creation_formula = formula_step_dict[self.type]
            self.interval_formula = formula_from_steps(formula_step_dict[self.type])
 
        elif(self.type in formula_numeric_dict):
            self.creation_formula = formula_numeric_dict[self.type]
            self.interval_formula = formula_from_numerics(formula_numeric_dict[self.type]) 
            
        else:
            raise ValueError(f'Scale is not in either formula dictionary {self.type}')

        self.notes = scale_from_intervals(self.root, self.interval_formula) 
        self.numeric_formula = [i.to_numeric() for i in self.interval_formula]  

    @property
    def name(self):
        return f"{self.root} {self.type}"

    @property
    def number_of_flats(self):
        return sum(map(lambda x : len(x.name) == 2, self.notes))

    @classmethod
    def random(cls):
        return Scale(Note.random(), ScaleType.random())

    def __str__(self):
        return f"{self.notes[0].name} {self.type.name}: { notes_to_string(self.notes) }"

    def __repr__(self):
        return f"Scale(Note.{self.notes[0]}, ScaleType.{self.type})"

def modes_from_note(root):
    m, s = [], Scale(root, ScaleType.Ionian)

    m.append(s)
    m.append(Scale(s.notes[1], ScaleType.Dorian))
    m.append(Scale(s.notes[2], ScaleType.Phrygian))
    m.append(Scale(s.notes[3], ScaleType.Lydian))
    m.append(Scale(s.notes[4], ScaleType.Mixolydian))
    m.append(Scale(s.notes[5], ScaleType.Aeolian))
    m.append(Scale(s.notes[6], ScaleType.Locrian))

    return m

def main():
    scale = Scale(Note.C, ScaleType.Major)
    print(f"{scale.name}:")
    print(f"\tstr() -> {str(scale)}")
    print(f"\trepr() -> {repr(scale)}\n")

    scale = Scale.random()

    print(f"{scale.name}:")
    print(f"\tstr() -> {str(scale)}")
    print(f"\trepr() -> {repr(scale)}")
    print(f"\tRoot -> {scale.root}")
    print(f"\tType -> {scale.type}")
    print(f"\tNotes -> {notes_to_string(scale.notes)}")
    print(f"\tNumber of flats -> {scale.number_of_flats}")
    print(f"\tCreation Formula -> {scale.creation_formula})")
    print(f"\tInterval Formula -> {scale.interval_formula})")
    print(f"\tNumeric Formula -> {scale.numeric_formula})\n")

    # Print modes
    note = Note.random()
    print(f"Modes of {note}:")
    for mode in modes_from_note(note):
        print(f"\t{mode}")

if __name__ == '__main__':
    main()