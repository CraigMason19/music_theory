#-------------------------------------------------------------------------------
# Name:        intervals.py
#
# Notes:       Contains a Interval class and related functions
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum

from music_theory.utils import index_to_range, UP_DIRECTIONS, DOWN_DIRECTIONS

class Interval(Enum):
    """ Represents a interval (diffence between two notes). Derived from the 
        Enum class.
    
    Attributes:
        interval attributes:
            12 class attributes representing interval enumerations.

    Methods:
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

    @classmethod    
    def items(cls):
        """ A class method that returns a list of the interval enumerations. 

            e.g. [Interval.Unison, Interval.m2, ... ]

        Args:
            None.

        Returns:
            A list of intervals.
        """  
        return [n for n in cls]
 
    all = items # Alias

    @classmethod
    def from_index(cls, index):
        """ A class methd that returns a interval based upon it's enumeration 
            value (positive or negative). Positive indices are counted from the
            start and negative indices are counted from the end.

            e.g. from_index(8) -> Interval.m6
                 from_index(-8) -> Interval.M3

        Args:
            index:
                The index of the value to be retrieved. Can be positive or 
                negative.

        Returns:
            A Interval.
        """  
        index = index_to_range(index)
        return Interval.items()[index]

    @classmethod
    def from_numeric(cls, numeric):
        """ A class method that returns a interval based upon a numeric interval
            value.
            ('1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7')
            
            e.g. from_numeric('b3') -> Interval.m3

        Args:
            numeric:
                The numeric interval to be translated.

        Returns:
            A Interval.
        """  
        numerics = ['1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7']
        index = numerics.index(numeric)
        return Interval.items()[index]

    def to_numeric(self):
        """ Returns the numeric value of an interval. 

            e.g. Interval.P4.to_numeric() -> '4'

        Args:
            None.

        Returns:
            A string representing the numeric value.
        """  
        numerics = ['1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7']
        return numerics[self.value]

    @classmethod
    def random(cls):
        """ A class method that returns a random interval. 

            e.g. Interval.P4

        Args:
            None.

        Returns:
            A interval.
        """  
        return random.choice(cls.items())

    def __str__(self):
        """ Returns a string representing the interval name. 

            e.g. str(Interval.P5) -> 'P5'

        Args:
            None.

        Returns:
            A string representing a interval's name.
        """
        return self.name

    def __repr__(self):
        """ Returns a string representing the interval. 

            e.g. repr(Interval.P5) -> 'Interval.P5'

        Args:
            None.

        Returns:
            A string representing a interval.
        """
        return f'Interval.{self.name}'
    
#region Functions

def intervals_to_string(interval_list):
    """ Takes a list of intervals and returns a string of interval names. 

        e.g. [Interval.M3, Interval.P4, Interval.P5] -> "M3, P4, P5"

    Args:
        note_list:
            The list of intervals to be converted to a string.

    Returns:
        The string of interval names.
    """  
    return ', '.join([i.name for i in interval_list])

def interval_distance(first_note, second_note, direction="u"):
    """ Takes two notes and calculates the interval distance between them, 
        either up or down.

        NOTE: A perfect 5th up is the same as a perfect 4th down and vice-versa

        e.g. Note.C, Note.G, 'u' -> interval.P5
             Note.C, Note.G, 'd' -> interval.P4

    Args:
        first_note:
            The note to start measuring from.
        second_note:
            The note above or below the first.
        direction:
            Can either check distance up or down in pitch. acceptable values are
            "u", "up", "above", "d", "down" or "below" in any case.

    Returns:
        A Interval representing the difference between two notes.

    Raises:
        ValueError:
            If the direction string is not recognized.
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