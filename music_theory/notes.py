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

UP_DIRECTIONS = ["u", "up", "above"]
DOWN_DIRECTIONS = ["d", "down", "below"]

# Single underscore indicates that this function is not meant to be imported from
# other modules.
def _index_to_range(index):
    """ Takes a index and converts it into the range -11 to +11 (+ or - Interval 
        or note). 12 would be an octave and so the note would not change. 

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

# region Interval

class Interval(Enum):
    """ Represents a interval (diffence between two notes). Derived from the 
        Enum class.
    
    Attributes:
        interval attributes:
            12 class attributes representing interval enumerations.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        all_intervals(cls):
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
 
    all_intervals = items # Alias

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
        index = _index_to_range(index)
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

#endregion

#region Note

class Note(Enum):
    """ Represents a musical note. Derived from the Enum class.

        NOTE: Can't have sharps (#) in variable names

    Attributes:
        note attributes:
            12 class attributes representing note enumerations. Starting at 'middle C'.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        all_notes(cls):
            An alias for items(), returning the enums as a list.
        from_index(cls, index):
            A class method to return a enumeration based upon an index.
        random(cls):
            A class method that returns a random note.
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
        """ A class method that returns a list of the note enumerations. 

            e.g. [Note.C, Note.Db, ... ]

        Args:
            None.

        Returns:
            A list of notes.
        """  
        return [n for n in cls]
 
    all_notes = items  # Alias

    @classmethod
    def from_index(cls, index):
        """ A class method that returns a note based upon it's enumeration
            value (positive or negative). Positive indices are counted from
            the start and negative indices are counted from the end.

            e.g. from_index(3) -> Note.Eb
                 from_index(-3) -> Note.A
                 
        Args:
            index:
                The index of the value to be retrieved. Can be positive or 
                negative.

        Returns:
            A Note.
        """  
        index = _index_to_range(index)
        return Note.items()[index]

    @classmethod
    def random(cls):
        """ A class method that returns a random note. 

            e.g. Note.Ab

        Args:
            None.

        Returns:
            A Note.
        """  
        return random.choice(cls.items())

    def to_sharp(self):
        """ Returns a sharp rather than a flat. Or just the name of the note if 
            it doesn't have a flat. 

            e.g. Note.Eb.to_sharp() -> 'D#'

        Args:
            None.

        Returns:
            A string representing a note.
        """  
        if(len(self.name) == 2):
            lower_note = Note.from_index(self.value-1) # move down a semitone
            return lower_note.name + '#'

        return self.name
    
    def previous(self):
        """ Returns the previous note

            e.g. Note.Eb.previous() -> Note.D

        Args:
            None.

        Returns:
            A note.
        """  
        return Note.from_index(self.value-1)
    
    def next(self):
        """ Returns the next note

            e.g. Note.Eb.next() -> Note.E

        Args:
            None.

        Returns:
            A note.
        """  
        return Note.from_index(self.value+1)
    
    def transpose(self, interval, direction="u"):
        """ Transposes (changes) this note into a different note lower or higher
            in pitch. 

            Note.C.transpose(Interval.M3)
            C tranposed a Major 3rd becomes E

        Args:
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
        return transpose(self, interval, direction)
    
    def chromatics(self, direction="u"):
        """ Returns every note between this note and it's octave

            e.g. 
                Note.A.chromatics(direction="down")
                [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]

        Args:
            direction:
                Can either transpose up or down in pitch. acceptable values are
                "u", "up", "above", "d", "down" or "below" in any case.

        Returns:
            A list of notes.

        Raises:
            ValueError:
                If the direction string is not recognized.
        """            
        return chromatic_notes(self, direction)
    
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
        """ Returns a string representing the note. 

            e.g. repr(Note.Ab) -> 'Note.Ab'

        Args:
            None.

        Returns:
            A string representing a note.
        """
        return f'Note.{self.name}'
    
#endregion

#region Functions

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

    if direction in UP_DIRECTIONS:
        return Note.from_index(note.value + interval.value)

    elif direction in DOWN_DIRECTIONS:
        return Note.from_index(note.value - interval.value)

    raise ValueError(f'direction not recognized({direction})')

def chromatic_notes(note, direction="u"):
    """ Takes a note and returns every note between that note and it's octave

        e.g. 
            chromatic_notes(Note.A, direction="down")
            [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]

    Args:
        note:
            The note to start from.
        direction:
            Can either transpose up or down in pitch. acceptable values are
            "u", "up", "above", "d", "down" or "below" in any case.

    Returns:
        A list of notes.

    Raises:
        ValueError:
            If the direction string is not recognized.
    """      
    notes = [note]
    direction = direction.lower()

    for _ in range(11):
        if direction in UP_DIRECTIONS:
            note = note.next()

        elif direction in DOWN_DIRECTIONS:
            note = note.previous()

        else:
            raise ValueError(f'direction not recognized({direction})')

        notes.append(note)

    return notes

#endregion