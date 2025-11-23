"""
Defines the ChordType enumeration for musical chords.

This module provides:
- An Enum class `ChordType` with various declarations of chord types.
- Utility methods to list all chord types and select a random chord type.
- String representations for clean display and debugging.

Example:
    >>> from music_theory.chord_type import ChordType
    >>> ct = ChordType.Major
    >>> str(ct)
    Major
"""
import random

from enum import Enum
from typing import Self

class ChordType(Enum):
    """ 
    Represents a chord type. Derived from the Enum class.
    
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
    def items(cls) ->list[Self]:
        """ 
        A class method that returns a list of the chord enumerations. 
 
        Returns:
            list[ChordType]:
                A list of all supported ChordTypes.
        """  
        return [n for n in cls]

    @classmethod
    def random(cls) -> Self:
        """ 
        A class method that returns a random chord type. 

        Returns:
            ChordType:
                A random ChordType
        """  
        return random.choice(cls.items())

    def __str__(self) -> str:
        """ 
        Returns a string representing the chord types name. 

        Example:
            >>> str(ChordType.Major)
            Major

        Returns:
            str:
        """
        return self.name

    def __repr__(self) -> str:
        """ 
        Returns a string representing the chord types enum along with the objects name. 

        Example:
            >>> repr(ChordType.Major)
            ChordType.Major

        Returns:
            str:
        """
        return f'ChordType.{self.name}'