"""
This module defines symbolic direction aliases for upward and downward movement
in musical space, and provides a utility to constrain arbitrary integer indices
to the musically meaningful range of ±11 semitones. Values ≥12 are treated as
octave-equivalent and reduced modulo 12, preserving directional intent.

Constants:
    UP_DIRECTIONS:    Aliases for upward movement.
    DOWN_DIRECTIONS:  Aliases for downward movement.

Functions:
    index_to_range(index): 
        Normalizes an integer index to the range -11 to +11, preserving sign.
"""
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
    order. For example:

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