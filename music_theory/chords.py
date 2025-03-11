#-------------------------------------------------------------------------------
# Name:        chords.py
#
# Notes:       Contains ChordType and Chord classes. 
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum

from music_theory.notes import Note, transpose, Interval

# A cadence in music is a chord progression of at least 2 chords that ends a 
# phrase or section of a piece of music.
cadence_dict = {
    # Finished
    "Plagal": ["IV", "I"], # Or, Amen
    "Authentic": ["V", "I"], # Or, perfect
    # Unfinished
    "Deceptive": ["V", "VI"], #Or, interupted
}

#region ChordType

class ChordType(Enum):
    """ Represents a chord type. Derived from the Enum class.
    
    Attributes:
        chord attributes:
            4 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        random(cls):
            A class method to return a random chord type.
        __str__(self):
            Returns the name of the chord type.
        __repr__(self):
            Returns the Enum name.
    """
    (
        Major, Minor, Diminished, 
        Dominant7, Major7, Minor7, Diminished7,
        Sus2, Sus4
    ) = range(9)

    @classmethod    
    def items(cls):
        """ A class method that returns a list of the chord enumerations. 

            e.g. [ChordType.Major, ChordType.Minor ... ]

        Args:
            None.

        Returns:
            A list of chord types.
        """  
        return [n for n in cls]

    @classmethod
    def random(cls):
        """ A class method that returns a random chord type. 

            e.g. ChordType.Diminished

        Args:
            None.

        Returns:
            A ChordType.
        """  
        return random.choice(cls.items())

    def __str__(self):
        """ Returns a string representing the chord type name. 

            e.g. str(ChordType.Major) -> 'Major'

        Args:
            None.

        Returns:
            A string.
        """
        return self.name

    def __repr__(self):
        """ Returns a string representing the key types enum. 

            e.g. repr(ChordType.Major) -> 'ChordType.Major'

        Args:
            None.

        Returns:
            A string.
        """
        return f'ChordType.{self.name}'

#endregion

#region Chord

class Chord:
    """ A class representing a musical chord. 

    Attributes:
        root:
            The Note the rest of the chord is built from.
        type:
            A ChordType. 
        notes:
            An array containing the root, 3rd(Major or Minor) & the fifth

    Methods:
        __init__(self, root, chord_type):
            Constructs the chord.
        random(cls):
            A class method to return a random chord.
        __eq__(self, other):
            Compares two chords.
        notation(self):
            Returns the chord's notation without the Note.
        add9(self):
            Returns an array of the chord's notes with the added 9th
        add11(self):
            Returns an array of the chord's notes with the added 11th
        add13(self):
            Returns an array of the chord's notes with the added 13th
        __str__(self):
            Returns a string representation of the Chord.
        __repr__(self):
            Returns a string representation of the Chord.
    """
    def __init__(self, root, chord_type=ChordType.Major):
        """ Constructs the chord.

        Args:
            root:
                The root note to build the chord from.
            chord_type:
                The ChordType to represent the chord.

        Returns:
            None.
        """  
        self.root, self.chord_type, self.notes = root, chord_type, []

        match self.chord_type:
            case ChordType.Major:
                self.notes = [self.root, transpose(self.root, Interval.M3), transpose(self.root, Interval.P5)]

            case ChordType.Minor:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.P5)]

            case ChordType.Diminished:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.dim5)]

            case ChordType.Dominant7:
                self.notes = [self.root, transpose(self.root, Interval.M3), transpose(self.root, Interval.P5), transpose(self.root, Interval.m7)]
            
            case ChordType.Major7:
                self.notes = [self.root, transpose(self.root, Interval.M3), transpose(self.root, Interval.P5), transpose(self.root, Interval.M7)]

            case ChordType.Minor7:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.P5), transpose(self.root, Interval.m7)]
            
            case ChordType.Diminished7:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.dim5), transpose(self.root, Interval.M6)]

            case ChordType.Sus2:
                self.notes = [self.root, transpose(self.root, Interval.M2), transpose(self.root, Interval.P5)]        

            case ChordType.Sus4:
                self.notes = [self.root, transpose(self.root, Interval.P4), transpose(self.root, Interval.P5)]      

            case _:
                pass
    
    @classmethod
    def random(cls):
        """ A class method that returns a random chord. 

            e.g. Fdim

        Args:
            None.

        Returns:
            A Chord.
        """  
        return Chord(Note.random(), ChordType.random())

    def __eq__(self, other):
        """ Equality operator to check that both the note and chord type match. 

            e.g. Chord(F, ChordType.Diminished) == Chord(F, ChordType.Diminished)

        Args:
            other:
                The other Chord to compare.

        Returns:
            A bool. True if this and another chord are the same.
        """
        try:
            return self.root == other.root and self.chord_type == other.chord_type
        except AttributeError:
            return False

    @property
    def notation(self):
        """ A property that returns the chord's notation without the Note. 

            e.g. 'Fdim' -> 'dim'

        Args:
            None.

        Returns:
            A string.
        """    
        match self.chord_type:
            case ChordType.Minor:
                return f"m" 
            
            case ChordType.Diminished:
                return f"dim"
            
            case ChordType.Dominant7:
                return f"7"   

            case ChordType.Major7:
                return f"Δ7"            

            case ChordType.Minor7:
                return f"m7"      

            case ChordType.Diminished7:
                return f"°7"   
                        
            case ChordType.Sus2:
                return f"sus2"
            
            case ChordType.Sus4:
                return f"sus4"
            
            case _:
                return f"M"

    def add9(self):
        """ Returns an array containing the notes of the chord with the added 9th. 

            e.g. Chord(Note.A).add9() -> [Note.A, Note.Db, Note.E, Note.B]

        Args:
            None.

        Returns:
            An array.
        """    
        return self.notes + [transpose(self.root, Interval.M2)]

    def add11(self):
        """ Returns an array containing the notes of the chord with the added 11th. 

            e.g. Chord(Note.A).add11() -> [Note.A, Note.Db, Note.E, Note.D]

        Args:
            None.

        Returns:
            An array.
        """    
        return self.notes + [transpose(self.root, Interval.P4)]
    
    def add13(self):
        """ Returns an array containing the notes of the chord with the added 13th. 

            e.g. Chord(Note.A).add13() -> [Note.A, Note.Db, Note.E, Note.Gb]

        Args:
            None.

        Returns:
            An array.
        """    
        return self.notes + [transpose(self.root, Interval.M6)]
    
    def __str__(self):
        """ Returns a string representing the Chord name and type. 

            e.g. str(Chord(Note.E, ChordType.Dominant7)) -> E7

        Args:
            None.

        Returns:
            A string.
        """
        return f"{self.root}{self.notation}"

    def __repr__(self):
        """ Returns a string representing the Chord. 

            e.g. repr(Chord(Note.E, ChordType.Dominant7)) -> Chord(E, Dominant7)

        Args:
            None.

        Returns:
            A string.
        """
        return f"Chord({self.root}, {self.chord_type})"

#endregion