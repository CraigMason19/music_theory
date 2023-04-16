#-------------------------------------------------------------------------------
# Name:        chords.py
#
# Notes:       Contains ChordType and chord classes. 
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random

from enum import Enum

from notes import Note

#region Cadences

# A cadence in music is a chord progression of at least 2 chords that ends a 
# phrase or section of a piece of music.
cadence_dict = {
    # Finished
    "Plagal": ["IV", "I"], # Or, Amen
    "Authentic": ["V", "I"], # Or, perfect
    # Unfinished
    "Deceptive": ["V", "VI"], #Or, interupted
}

#endregion

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
    (Major, Minor, Diminished, Seven) = range(4)

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

class Chord:
    """ A class representing a musical chord. 

    Attributes:
        root:
            The Note the rest of the chord is built from.
        type:
            A ChordType. 

    Methods:
        __init__(self, root, chord_type):
            Constructs the chord.
        random(cls):
            A class method to return a random chord.
        __eq__(self, other):
            Compares two chords.
        notation(self):
            Returns the chord's notation without the Note.
        __str__(self):
            Returns a string representation of the Chord.
        __repr__(self):
            Returns a string representation of the Chord.
    """
    def __init__(self, root, chord_type):
        """ Constructs the chord.

        Args:
            root:
                The root note to build the chord from.
            chord_type:
                The ChordType to represent the chord.

        Returns:
            None.
        """  
        self.root, self.chord_type = root, chord_type
    
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
        if self.chord_type == ChordType.Diminished:
            return f"dim"

        elif self.chord_type == ChordType.Minor:
            return f"m"

        elif self.chord_type == ChordType.Seven:
            return f"7"

        return f"M"

    def __str__(self):
        """ Returns a string representing the Chord name and type. 

            e.g. str(Chord(Note.E, ChordType.Seven)) -> E7

        Args:
            None.

        Returns:
            A string.
        """
        return f"{self.root}{self.notation}"

    def __repr__(self):
        """ Returns a string representing the Chord. 

            e.g. repr(Chord(Note.E, ChordType.Seven)) -> Chord(E, Seven)

        Args:
            None.

        Returns:
            A string.
        """
        return f"Chord({self.root}, {self.chord_type})"

def main():
    ct = ChordType.random()
    print(f"ChordType {ct}:")
    print(f"\tstr() -> {str(ct)}")
    print(f"\trep() -> {repr(ct)}")

    c = Chord.random()
    print(f"Chord {c}:")
    print(f"\tstr() -> {str(c)}")
    print(f"\trep() -> {repr(c)}")
    print(f"\tnotation -> {c.notation}")

if __name__ == '__main__':
    main()