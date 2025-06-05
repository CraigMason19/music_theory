#-------------------------------------------------------------------------------
#
# Name:        chord_type.py
#
# Notes:       A class representing a type of chord.
#
#-------------------------------------------------------------------------------

import random
from enum import Enum

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