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

from music_theory.intervals import Interval
from music_theory.utils import index_to_range, UP_DIRECTIONS, DOWN_DIRECTIONS, is_valid_note_str

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
        from_string(cls, note_str: str) -> Self | None:
            A class method that converts a validated note string into a `Note` object.
        random(cls):
            A class method that returns a random note.
        to_sharp(self):
            Returns a string of a flat note as a sharp.
        enharmonic(self):
            An alias for to_sharp(), Returns a string of a flat note as a sharp.
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
    def from_index(cls, index: int) -> Self:
        """ 
        A class method that returns a note based upon it's enumeration
        value (positive or negative). Positive indices are counted from
        the start and negative indices are counted from the end.

        Example:
            >>> Note.from_index(3)
            Note.Eb
            >>> Note.from_index(-3)
            Note.A
                 
        Args:
            index (int):
                The index of the value to be retrieved. Can be positive or 
                negative.

        Returns:
            Note:
        """  
        index = index_to_range(index)
        return Note.items()[index]

    @classmethod
    def from_string(cls, note_str: str) -> Self | None:
        """
        A class method that converts a validated note string into a `Note` object.

        The input must be a letter A–G (any case), optionally followed by one or
        two sharps ('#') or flats ('b'). If the string is not a valid note,
        the function returns None.

        Behaviour:
            - Single-letter notes (e.g., "C", "f") are returned directly.
            - One accidental (e.g., "C#", "Eb") applies a minor second transposition.
            - Double accidentals (e.g., "C##", "Ebb") apply a major second transposition.

        Examples:
            >>> note_from_string("C")
            Note.C
            >>> note_from_string("F#")
            Note.Gb
            >>> note_from_string("Ebb")
            Note.D

        Args:
            note_str (str):
                The string representation of the musical note.

        Returns:
            Note | None:
                A corresponding `Note` object if valid, otherwise None.
        """
        if not is_valid_note_str(note_str):
            return None
        
        note_strs = [str(n) for n in Note.items()]
        note_index = note_strs.index(note_str[0].upper())
        note = Note.from_index(note_index)

        if len(note_str) == 1:
            return note
        
        direction = 'u' if (note_str[1] == '#') else 'd'

        # Sharps / flats
        if len(note_str) == 2:
            return note.transpose(Interval.m2, direction)

        # Double sharps / flats
        if len(note_str) == 3:
            return note.transpose(Interval.M2, direction)
    
    @classmethod
    def random(cls) -> Self:
        """ 
        A class method that returns a random note. 

        Returns:
            Note:
        """  
        return random.choice(cls.items())

    def to_sharp(self) -> str:
        """ 
        Returns the enharmonic sharp equivalent of the note, or the note's name 
        if it does not use a flat.

        Example:
            >>> Note.Eb.to_sharp()
            D#

        Returns:
            str:
                A string representing a note.
        """  
        if(len(self.name) == 2):
            lower_note = Note.from_index(self.value-1) # move down a semitone
            return lower_note.name + '#'

        return self.name
    
    enharmonic = to_sharp  # Alias

    def previous(self) -> Self:
        """
        Returns the previous note

        Example:
            >>> Note.Eb.previous()
            Note.D

        Returns:
            Note:
        """  
        return Note.from_index(self.value-1)
    
    def next(self) -> Self:
        """ 
        Returns the next note

        Example:
        >>> Note.Eb.next()
        Note.E

        Returns:
            Note:
        """  
        return Note.from_index(self.value+1)
    
    def transpose(self, interval, direction: str="u") -> Self:
        """ 
        Transposes (changes) this note into a different note lower or higher in 
        pitch. 

        Example:
            >>> Note.C.transpose(Interval.M3)
            Note.E

        Args:
            interval (Interval):
                The interval to transpose the note.
            direction (str):
                Can either transpose up or down in pitch. acceptable values are
                "u", "up", "above", "d", "down" or "below" in any case.

        Raises:
            ValueError:
                If the direction string is not recognized.

        Returns:
            Note: 
                The note after being transposed.
        """   
        return transpose(self, interval, direction)
    
    def chromatics(self, direction: str="u") -> list[Self]:
        """ 
        Returns every note between this note and it's octave

        Example:
            >>> Note.A.chromatics(direction="down")
            [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]

        Args:
            direction (str):
                Can either transpose up or down in pitch. acceptable values are
                "u", "up", "above", "d", "down" or "below" in any case.

        Raises:
            ValueError:
                If the direction string is not recognized.

        Returns:
            list[Note]:
        """            
        return chromatic_notes(self, direction)
    
    def __str__(self) -> str:
        """ 
        Returns a string representing the note name. 

        Example:
            >>> str(Note.Ab)
            Ab

        Returns:
            str:
                A string representing a note's name.
        """
        return self.name

    def __repr__(self) -> str:
        """ 
        Returns a string representing the note. 

        Example:
            >>> repr(Note.Ab)
            Note.Ab

        Returns:
            str:
                A string representing a note along with it's Class name.
        """
        return f'Note.{self.name}'
    
#region Functions

def notes_to_string(note_list: list[Note]) -> str:
    """ 
    Takes a list of notes and returns a string of note names. 

    Example:
        >>> notes_to_string[Note.C, Note.B, Note.D])
        C, B, D

    Args:
        note_list (list[Note]):
            The list of notes to be converted to a string.

    Returns:
        str:
    """  
    return ', '.join([n.name for n in note_list])

def transpose(note, interval, direction: str="u") -> Note:
    """ 
    Takes a note and transposes (changes) it into a different note lower or 
    higher in pitch. 

    Example:
        >>> transpose(Note.C, Intervl.M3, "up")
        Note.E

    Args:
        note (Note):
            The note to be transposed.
        interval (int):
            The interval to transpose the note.
        direction (str):
            Can either transpose up or down in pitch. acceptable values are
            "u", "up", "above", "d", "down" or "below" in any case.

    Raises:
        ValueError:
            If the direction string is not recognized.

    Returns:
        Note:
            The note after being transposed.
    """       
    direction = direction.lower()

    if direction in UP_DIRECTIONS:
        return Note.from_index(note.value + interval.value)

    elif direction in DOWN_DIRECTIONS:
        return Note.from_index(note.value - interval.value)

    raise ValueError(f'direction not recognized({direction})')

def chromatic_notes(note: Note, direction: str="u"):
    """ 
    Returns every note between this note and it's octave

    Example:
        >>> Note.A.chromatics(direction="down")
        [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]

    Args:
        direction (str):
            Can either transpose up or down in pitch. acceptable values are
            "u", "up", "above", "d", "down" or "below" in any case.

    Raises:
        ValueError:
            If the direction string is not recognized.

    Returns:
        list[Note]:
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