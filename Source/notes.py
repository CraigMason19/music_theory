#-------------------------------------------------------------------------------
# Name:        notes.py
#
# Notes:       A collection of objects and methods representing the 12 notes of 
#              the western musical scale.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum

def _index_to_range(index):
    """ Takes a index and converts it into the range -11 to +11.
        12 would be an octave and so the note would not change. 

    Args:
        index:
            An integer representing a positive or negative index.

    Returns:
        A integer index in the range -11 to +11.
    """ 
    sign = 1 if (index >= 0) else -1
    index = abs(index)

    if index >= 12:       
        index = index % 12        

    return sign * index

class Interval(Enum):
    """ Represents a interval (diffence between two notes). Derived from the 
        Enum class.
    
    Attributes:
        class attributes:
            12 class attributes representing a Enum .

    Methods:
        items(cls):
            A class method to return the enums as a list.
        from_index(cls, index):
            A class method to return a enumeration based upon an index.
        from_numeric(cls, numeric):
            A class method to construct an interval from a numeric.
        to_numeric(self):
            Converts an interval to a numeric.
        random(cls):
            Returns a random interval.
        __str__(self):
            Returns the name of the interval.
        __repr__(self):
            Returns the Enum name.
    """
    Unison, m2, M2, m3, M3, P4, dim5, P5, m6, M6, m7, M7 = range(12) 

    @classmethod    
    def items(cls):
        """ Returns a list of the interval enumerations. 

            e.g. [Interval.Unison, Interval.m2, ... ]

        Args:
            None.

        Returns:
            A list of intervals.
        """  
        return [n for n in cls]
 
    @classmethod
    def from_index(cls, index):
        """ Returns a interval based upon it's enumeration value (positive or 
            negative). Positive indices are counted from the start and negative 
            indices are counted from the end.

            e.g. from_index(8) -> Interval.m6
                 from_index(-8) -> Interval.M3

        Args:
            index:
                The index of the value to be retrieved. Can be positive or 
                negative.

        Returns:
            A interval.
        """  
        index = _index_to_range(index)
        return Interval.items()[index]

    @classmethod
    def from_numeric(cls, numeric):
        """ Returns a interval based upon a numeric interval value.
            ('1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7')
            
            e.g. from_numeric('b3') -> Interval.m3

        Args:
            numeric:
                The numeric interval to be translated.

        Returns:
            A interval.
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
        """ Returns a random interval. 

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

class Note(Enum):
    """ Represents a musical note starting at 'middle C'. Derived from the 
        Enum class.

        NOTE: Can't have sharps (#) in variable names

    Attributes:
        class attributes:
            12 class attributes representing note enumerations.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        from_index(cls, index):
            A class method to return a enumeration based upon an index.
        random(cls):
            Returns a random note.
        to_sharp(self):
            Returns a string of a flat note as a sharp.
        __str__(self):
            Returns the name of the note.
        __repr__(self):
            Returns the Enum name.
    """
    C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B = range(12) 

    @classmethod    
    def items(cls):
        """ Returns a list of the note enumerations. 

            e.g. [Note.C, Note.Db, ... ]

        Args:
            None.

        Returns:
            A list of notes.
        """  
        return [n for n in cls]
 
    @classmethod
    def from_index(cls, index):
        """ Returns a note based upon it's enumeration value (positive or 
            negative). Positive indices are counted from the start and negative 
            indices are counted from the end.

            e.g. from_index(3) -> Note.Eb
                 from_index(-3) -> Note.A
                 
        Args:
            index:
                The index of the value to be retrieved. Can be positive or 
                negative.

        Returns:
            A note.
        """  
        index = _index_to_range(index)
        return Note.items()[index]

    @classmethod
    def random(cls):
        """ Returns a random note. 

            e.g. Note.Ab

        Args:
            None.

        Returns:
            A note.
        """  
        return random.choice(cls.items())

    def to_sharp(self):
        """ Returns a sharp rather than a flat. 

            e.g. Note.Eb.to_sharp() -> 'D#'

        Args:
            None.

        Returns:
            A string representing a note.
        """  
        if(len(self.name) == 2):
            lower_note = Note.from_index(self.value-1)
            return lower_note.name + '#'

        return self.name

    def __str__(self):
        """ Returns a string representing the note name. 

            e.g. str(Note.Ab) -> 'Ab'

        Args:
            None.

        Returns:
            A string representing a note's name.
        """
        return self.name

    def __repr__(self):
        """ Returns a string representing the class and note. 

            e.g. repr(Note.Ab) -> 'Note.Ab'

        Args:
            None.

        Returns:
            A string representing a note.
        """
        return f'Note.{self.name}'

def notes_to_string(note_list):
    """ Takes a list of notes and returns a string of note names. 

        e.g. [Note.C, Note.B, Note.D] -> "C, B, D"

    Args:
        note_list:
            The list of notes to be converted to a string.

    Returns:
        The string of note names.
    """  
    return ', '.join([n.name for n in note_list])

def intervals_to_string(interval_list):
    """ Takes a list of intervals and returns a string of interval names. 

        e.g. [Interval.M3, Interval.P4, Interval.P5] -> "M3, P4, P5"

    Args:
        note_list:
            The list of intervals to be converted to a string.

    Returns:
        The string of interval names
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
        A interval representing the difference between two notes.

    Raises:
        ValueError:
            If the direction string is not recognized.
    """  
    if(first_note == second_note):
        return Interval.Unison

    direction = direction.lower()
    dif = abs(first_note.value - second_note.value)

    if direction in ["u", "up", "above"]:
        if first_note.value > second_note.value:
            return Interval.from_index(12 - dif)  

        return Interval.from_index(dif)        

    elif direction in ["d", "down", "below"]:
        if first_note.value > second_note.value:
            return Interval.from_index(dif) 
         
        return Interval.from_index(12 - dif) 

    raise ValueError(f'direction not recognized({direction})')

def transpose(note, interval, direction="u"):
    """ Takes a note and transposes (changes) it into a different note lower or 
        higher in pitch. 

        e.g. C tranposed a Major 3rd becomes E

    Args:
        note:
            The note to be transposed.
        interval:
            The interval to transpose the note.
        direction:
            Can either transpose up or down in pitch. acceptable values are
            "u", "up", "above", "d", "down" or "below" in any case.

    Returns:
        The note after being transposed.

    Raises:
        ValueError:
            If the direction string is not recognized.
    """       
    direction = direction.lower()

    if direction in ["u", "up", "above"]:
        return Note.from_index(note.value + interval.value)

    elif direction in ["d", "down", "below"]:
        return Note.from_index(note.value - interval.value)

    raise ValueError(f'direction not recognized({direction})')

def main():
    """ Example Usage """
    test_range = 3
    note, interval = Note.random(), Interval.random()

    # Notes
    print(f"Note: {note}:")
    print(f"\tstr() -> {str(note)}")
    print(f"\trepr() -> {repr(note)}\n")

    # Intervals
    print(f"Interval: {interval}:")
    print(f"\tstr() -> {str(interval)}")
    print(f"\trepr() -> {repr(interval)}\n")

    print(f"Interval distances:")
    for i in range(test_range):
        note_a, note_b = Note.random(), Note.random()

        dif = interval_distance(note_a, note_b) 
        print(f"\t{note_a}, {note_b} -> {dif}")

        dif = interval_distance(note_a, note_b, direction='down')  
        print(f"\t{note_a}, {note_b} <- {dif}\n")

    # Transpose
    print(f"Transpose:")
    for i in range(test_range):
        note, interval = Note.random(), Interval.random()

        new_note = transpose(note, interval)  
        print(f"\t{note}, {interval} -> {new_note}")

        new_note = transpose(note, interval, direction='down')  
        print(f"\t{note}, {interval} <- {new_note}\n") 

if __name__ == '__main__':
    main()