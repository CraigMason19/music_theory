"""
Defines the Interval class representing a offset from a Note in music.

This module provides:
- An Enum class `Interval` with 12 values: From Unison to Major 7th.
- Utility methods to create from index or a numeric string, select a random Interval type.
- String representations for clean display and debugging.

Example:
    >>> from music_theory.intervals import Interval
    >>> i = Interval.M3
    >>> print(repr(i))
    Interval.M3
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: # pragma: no cover
    from music_theory.notes import Note
    
import random
from enum import Enum

from music_theory.utils import index_to_range, UP_DIRECTIONS, DOWN_DIRECTIONS

LABELS: list[str] = [
    "Unison",
    "Minor 2nd",
    "Major 2nd",
    "Minor 3rd",
    "Major 3rd",
    "Perfect 4th",
    "Diminished 5th",
    "Perfect 5th",
    "Minor 6th",
    "Major 6th",
    "Minor 7th",
    "Major 7th",
]

class Interval(Enum):
    """ 
    Represents a interval (diffence between two notes). Derived from the 
    Enum class.
    
    Attributes:
        intervals:
            12 class attributes representing interval enumerations.

    Properties:
        label(self) -> str:
            A property to return the Interval as a more descriptive, human 
            readable string.

    Methods:
        labels(cls):
            A class method that returns a list of all the interval labels.        
        items(cls):
            A class method to return the enums as a list.
        all(cls):
            An alias for items(), returning the enums as a list.
        from_index(cls, index):
            A class method to return a enum based upon an index.
        from_numeric(cls, numeric):
            A class method to construct an interval from a numeric.
        to_numeric(self):
            Converts an interval to a numeric.
        random(cls):
            A class method that returns a random interval.
        __str__(self):
            Returns the name of the interval.
        __repr__(self):
            Returns the Enum name.
    """
    Unison, m2, M2, m3, M3, P4, dim5, P5, m6, M6, m7, M7 = range(12) 
    
    @property
    def label(self) -> str:
        """
        A property to return the Interval as a more descriptive, human readable 
        string.
        
        Example:
            >>> Interval.m2
            Minor 2nd

        Returns:
            str:
        """
        return LABELS[self.value]

    @classmethod
    def labels(cls) -> list[str]:
        """ 
        A class method that returns a list of all the interval labels. 

        Labels are a more descriptive, human readable string of the interval.  

        Returns:
            list(str):
        """  
        return LABELS
    
    @classmethod    
    def items(cls):
        """ 
        A class method that returns a list of the interval enumerations. 

        Returns:
            list(Interval):
        """  
        return [n for n in cls]
 
    all = items # Alias

    @classmethod
    def from_index(cls, index):
        """ 
        A class methd that returns a interval based upon it's enumeration 
        value (positive or negative). Positive indices are counted from the
        start and negative indices are counted from the end.

        Examples:
            >>> from_index(8)
            m6
            >>> from_index(-8)
            M3

        Args:
            index (int):
                The index of the value to be calculated. Can be positive or 
                negative.

        Returns:
            Interval:
        """  
        index = index_to_range(index)
        return Interval.items()[index]

    @classmethod
    def from_numeric(cls, numeric: str):
        """ 
        A class method that returns a interval based upon a numeric interval
        value.
        
        ('1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7')
        
        Example:
            >>> Interval.from_numeric('b3')
            m3

        Args:
            numeric (str):
                The numeric interval to be translated.

        Returns:
            Interval:
        """  
        numerics = ['1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7']
        index = numerics.index(numeric)
        return Interval.items()[index]

    def to_numeric(self) -> str:
        """ 
        Returns the numeric value of a Interval as a string. 
        'b' is included if it is a flat.

        Example:
            >>> Interval.dim5.to_numeric()
            b5

        Returns:
            str:
                A string representing the numeric value.
        """  
        numerics = ['1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7']
        return numerics[self.value]

    @classmethod
    def random(cls):
        """ 
        A class method that returns a random interval. 

        Example:
            >>> Interval.random()
            P5

        Returns:
            Interval:
        """  
        return random.choice(cls.items())

    def __str__(self) -> str:
        """ 
        Returns a string representing the interval name. 

        Examples:
            >>> str(Interval.P5)
            P5

        Returns:
            str:
                A string representing a interval's name.
        """
        return self.name

    def __repr__(self) -> str:
        """ 
        Returns a string representing the interval. 

        Examples:
            >>> repr(Interval.P5)
            Interval.P5

        Returns:
            str:
                A string representing a interval.
        """
        return f'Interval.{self.name}'
    
#region Functions

def intervals_to_string(interval_list: list[Interval]) -> str:
    """ 
    Takes a list of intervals and returns a string of interval names. 

    Example:
        >>> [Interval.M3, Interval.P4, Interval.P5]
        M3, P4, P5

    Args:
        interval_list (list[Interval]):
            The list of intervals to be converted to a string.

    Returns:
        str:
            A string of Interval names.
    """  
    return ', '.join([i.name for i in interval_list])

def interval_distance(first_note: "Note", second_note: "Note", direction="u") -> Interval:
    """ 
    Takes two notes and calculates the interval distance between them, either up
    or down.

    NOTE: A perfect 5th up is the same as a perfect 4th down and vice-versa

    Examples:
        >>> interval_distance(Note.C, Note.G, 'u')
        P5
        >>> interval_distance(Note.C, Note.G, 'd')
        P4

    Args:
        first_note (Note):
            The note to start measuring from.
        second_note (Note):
            The note above or below the first.
        direction (str):
            Can either check distance up or down in pitch. acceptable values are
            "u", "up", "above", "d", "down" or "below" in any case.

    Raises:
        ValueError:
            If the direction string is not recognized.

    Returns:
        Interval:
            A Interval object representing the difference between two notes.
    """  
    if(first_note == second_note):
        return Interval.Unison

    direction = direction.lower()
    dif = abs(first_note.value - second_note.value)

    if direction in UP_DIRECTIONS:
        if first_note.value > second_note.value:
            return Interval.from_index(12 - dif)  

        return Interval.from_index(dif)        

    elif direction in DOWN_DIRECTIONS:
        if first_note.value > second_note.value:
            return Interval.from_index(dif) 
         
        return Interval.from_index(12 - dif) 

    raise ValueError(f'direction not recognized({direction})') 

#endregion