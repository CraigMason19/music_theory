#-------------------------------------------------------------------------------
# Name:        scale_type.py
#
# Notes:       A class representing a type of musical scale
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum

class ScaleType(Enum):
    """ Represents a type of scale (e.g. minor, major, blues, lydian, etc...).
        This determines how the scale will be constructed. Derived from the Enum
        class.
    
    Attributes:
        scale type attributes:
            14 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        all(cls):
            An alias for items(), returning the enums as a list.
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
        """ A class method that returns a list of the scale enumerations. 

            e.g. [ScaleType.Minor, ScaleType.Major ... ]

        Args:
            None.

        Returns:
            A list of ScaleTypes.
        """  
        return [n for n in cls]

    all = items  # Alias

    @classmethod
    def random(cls):
        """ A class method that returns a random scale. 

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
            A string representing the ScaleType.
        """
        return f'ScaleType.{self.name}'