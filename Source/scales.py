#-------------------------------------------------------------------------------
# Name:        scales.py
#
# Notes:       A collection of objects and methods representing a Scale (A
#              collection of musical notes).
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum
from notes import Note, Interval, notes_to_string, intervals_to_string

class ScaleType(Enum):
    """ Represents a scale type. This determines how the scale will be constructed.
        Derived from the Enum class.
    
    Attributes:
        class attributes:
            14 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        random(cls):
            A class method to return a random scale type.
        __str__(self):
            Returns the name of the scale type.
        __repr__(self):
            Returns the Enum name.
    """
    (Major, Minor, 
    MajorPentatonic, MinorPentatonic, 
    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian,
    Blues, HarmonicMinor, MelodicMinor) = range(14) 

    @classmethod    
    def items(cls):
        """ Returns a list of the scale enumerations. 

            e.g. [ScaleType.Minor, ScaleType.Major ... ]

        Args:
            None.

        Returns:
            A list of scale types.
        """  
        return [n for n in cls]

    @classmethod
    def random(cls):
        """ Returns a random scale. 

            e.g. ScaleType.MelodicMinor

        Args:
            None.

        Returns:
            A ScaleType.
        """  
        return random.choice(cls.items())

    def __str__(self):
        """ Returns a string representing the scale name. 

            e.g. str(ScaleType.Major) -> 'Major'

        Args:
            None.

        Returns:
            A string representing the scale's name.
        """
        return self.name

    def __repr__(self):
        """ Returns a string representing the scale types enum. 

            e.g. repr(ScaleType.Major) -> 'ScaleType.Major'

        Args:
            None.

        Returns:
            A string representing the scale's name.
        """
        return f'ScaleType.{self.name}'

# 3 ways to load a scale (step formula, interval, formula)
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

def interval_formula_from_steps(formula):
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

def interval_formula_from_numerics(formula):
    return [Interval.from_numeric(n) for n in formula]

def scale_from_intervals(root, interval_formula):   
    return [Note.from_index(root.value + interval.value) for interval in interval_formula]

class Scale:
    def __init__(self, root, scale_type):
        self.root, self.type = root, scale_type
        self._construct()

    def _construct(self):
        """ Method is private so not to pollute the __init__ method. 

            Build the scale from 3 different ways. Some scales are defined by intervals, 
            some are defined by steps and some are defined by numerics.

        Args:
            None.

        Returns:
            None.
        
        Raises:
            ValueError:
                Raised if the Scale's type is not in any dictionaries.
        """
        # First, try to build the scale from intervals e.g. (Unison M2 M3 M5 M6) 
        if(self.type in formula_interval_dict):
            self.creation_formula = formula_interval_dict[self.type]
            self.interval_formula = self.creation_formula

        # If the formula is not in interval form, convert it from step 
        # e.g. (w w h w w w h) -> (M2 M3 P4 P5 M6 M7, Unison)
        #      NOTE: The first letter is the step from the root. 
        elif(self.type in formula_step_dict):    
            steps = formula_step_dict[self.type]

            self.creation_formula = steps
            self.interval_formula = interval_formula_from_steps(steps)
 
        # Last way to construct a scale is from numerics.
        # e.g. (1 b3 4 b5 5 b7) -> (Unison, m3, P4, dim5 5 m7)
        elif(self.type in formula_numeric_dict):
            numerics = formula_numeric_dict[self.type]

            self.creation_formula = numerics
            self.interval_formula = interval_formula_from_numerics(numerics) 
            
        else:
            raise ValueError(f'Scale is not in either formula dictionary ({self.type})')

        # Once we have a formula in interval format we can build the scale from it.
        self.notes = scale_from_intervals(self.root, self.interval_formula) 
        self.numeric_formula = [i.to_numeric() for i in self.interval_formula]  

    @property
    def name(self):
        """ Returns the name of the scale. 

            e.g. 'C MAJOR'

        Args:
            None.

        Returns:
            A string.
        """
        return f"{self.root} {self.type}"

    @property
    def number_of_flats(self):
        """ Returns the number of flats in the scale. 

        Args:
            None.

        Returns:
            An integer.
        """
        return sum(map(lambda x : len(x.name) == 2, self.notes))

    @classmethod
    def random(cls):
        """ A class method to return a random Scale from a random note and type. 

        Args:
            None.

        Returns:
            An Scale.
        """
        return Scale(Note.random(), ScaleType.random())

    def __str__(self):
        """ Returns a string representing the Scale name, type and notes. 

            e.g. str(Scale(Note.E, ScaleType.Dorian)) -> E Dorian: E, Gb, G, A, B, Db, D

        Args:
            None.

        Returns:
            A string.
        """
        return f"{self.notes[0].name} {self.type.name}: { notes_to_string(self.notes) }"

    def __repr__(self):
        """ Returns a string representing the Scale name and type. 

            e.g. repr(Scale(Note.E, ScaleType.Dorian)) -> Scale(Note.E, ScaleType.Dorian)

        Args:
            None.

        Returns:
            A string.
        """
        return f"Scale(Note.{self.notes[0]}, ScaleType.{self.type})"

def modes_from_note(note):
    """ Returns a list of Scales depicting all the modes from a starting note. 

        Each subsequent mode starts from the next note in the scale (effectively 
        shifts the notes up). This repeats until it wraps back to the start.
        There are always 7 modes and they are always in the same order and are
        named (note -> mode).

        e.g. Mode 1 - C Ionian - C D E F G A B
            Mode 2 - D Dorian - D E F G A B C
            Mode 3 - E Phrygian: E, F, G, A, B, C, D
            Mode 4 - F Lydian: F, G, A, B, C, D, E
            Mode 5 - G Mixolydian: G, A, B, C, D, E, F
            Mode 6 - A Aeolian: A, B, C, D, E, F, G
            Mode 7 - B Locrian: B, C, D, E, F, G, A

    Args:
        note:
            The note to build the modes from.

    Returns:
        A list of 7 Scales.
    """
    m, s = [], Scale(note, ScaleType.Ionian)

    m.append(s)
    m.append(Scale(s.notes[1], ScaleType.Dorian))
    m.append(Scale(s.notes[2], ScaleType.Phrygian))
    m.append(Scale(s.notes[3], ScaleType.Lydian))
    m.append(Scale(s.notes[4], ScaleType.Mixolydian))
    m.append(Scale(s.notes[5], ScaleType.Aeolian))
    m.append(Scale(s.notes[6], ScaleType.Locrian))

    return m

def main():
    """ Example Usage """
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