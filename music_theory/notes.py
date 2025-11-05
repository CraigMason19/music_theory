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
from typing import Self

from music_theory.utils import index_to_range, UP_DIRECTIONS, DOWN_DIRECTIONS

class Note(Enum):
    """ Represents a musical note. Derived from the Enum class.

        NOTE: Can't have sharps (#) in variable names

    Attributes:
        note attributes:
            12 class attributes representing note enumerations. Starting at 'middle C'.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        all(cls):
            An alias for items(), returning the enums as a list.
        from_index(cls, index):
            A class method to return a enumeration based upon an index.
        random(cls):
            A class method that returns a random note.
        to_sharp(self):
            Returns a string of a flat note as a sharp.
        previous(self):
            Returns the note below.
        next(self):
            Returns the note above.
        transpose(self, interval, direction="u"):
            Returns a Note transposed by an interval in either direction.
        chromatics(self, direction="u"):
            Returns a list of all notes from the note to the octave in either direction.
        __str__(self):
            Returns the name of the note.
        __repr__(self):
            Returns the Enum name.
    """
    C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B = range(12) 

    @classmethod    
    def items(cls) -> list[Self]:
        """ 
        A class method that returns a list of the note enumerations. 

        Example:
            >>> Note.items()
            [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab, Note.A, Note.Bb, Note.B]

        Returns:
            list[Note]:
        """  
        return [n for n in cls]
 
    all = items  # Alias

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
        index = index_to_range(index)
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
        """ Returns the enharmonic sharp equivalent of the note, or the note's name 
            if it does not use a flat.

            e.g. Note.Eb.to_sharp() -> 'D#'

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

def transpose(note, interval, direction="u"):
    """ 
    Takes a note and transposes (changes) it into a different note lower or 
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