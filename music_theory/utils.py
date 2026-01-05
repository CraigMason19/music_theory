"""
This module defines symbolic direction aliases for upward and downward movement
in musical space, and provides a utility to constrain arbitrary integer indices
to the musically meaningful range of ±11 semitones. Values ≥12 are treated as
octave-equivalent and reduced modulo 12, preserving directional intent.

Constants:
    UP_DIRECTIONS:    Aliases for upward movement.
    DOWN_DIRECTIONS:  Aliases for downward movement.

Functions:
    index_to_range(index: int) -> int:
        Normalizes an integer index to the range -11 to +11, preserving sign.
    list_rotations(seq: Sequence[T]) -> list[list[T]]:
        Return all cyclic rotations of a sequence.
    is_valid_note_str(note_str: str) -> bool:
        Determine whether a string represents a valid musical note.
    is_empty_or_whitespace(s: str) -> bool:
        A simple function to determine if a string is empty or made of whitespaces. 
"""
import re

from typing import Sequence, TypeVar

T = TypeVar("T")

UP_DIRECTIONS = ["u", "up", "above"]
DOWN_DIRECTIONS = ["d", "down", "below"]

def index_to_range(index: int) -> int:
    """ 
    Converts an index into the range -11 to +11 (+ or - Interval or Note). 
    
    12 would be an octave and so the note would not change. 

    Args:
        index (int):
            An integer representing a positive or negative index.

    Returns:
        int:    
            An integer index in the range -11 to +11.
    """ 
    sign = 1 if (index >= 0) else -1
    index = abs(index)

    if index >= 12:       
        index = index % 12        

    return sign * index


def list_rotations(seq: Sequence[T]) -> list[list[T]]:
    """
    Return all cyclic rotations of a sequence.

    A cyclic rotation moves the first element(s) to the end while preserving
    order.

    Example:
        >>> list_rotations([1, 2, 3, 4])
        [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]

    Args:
        seq (Sequence[T]):
            The input sequence.

    Returns:
        list[list[T]]:
            A list containing all cyclic rotations of the input sequence.
    """
    return [list(seq[i:] + seq[:i]) for i in range(len(seq))]


def is_valid_note_str(note_str: str) -> bool:
    """
    Determine whether a string represents a valid musical note.

    A valid note consists of a letter A-G (any case), optionally followed by
    one or two flats ('b') or sharps ('#').

    Notes:
        - The function does not handle the natural symbol ('♮').
        - Whitespace causes validation to fail. For example, " C" is invalid.
     
    Examples:
        >>> is_valid_note_str('c')
        True
        >>> is_valid_note_str('cb')
        True
        >>> is_valid_note_str('cbb')
        True
        >>> is_valid_note_str('cb#')
        False  

    Args:
        note_str (str):
            The note string to validate.

    Returns:
        bool:
    """
    pattern = re.compile(r'^[a-gA-G](?:#{1,2}|b{1,2})?$', re.ASCII)

    return bool(pattern.match(note_str))

def is_empty_or_whitespace(s: str) -> bool:
    """
    A simple function to determine if a string is empty or made of whitespaces.

    Args:
        s (str):
            The string to validate.

    Returns:
        bool:
    """
    return not s or s.isspace()