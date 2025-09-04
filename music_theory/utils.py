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

UP_DIRECTIONS = ["u", "up", "above"]
DOWN_DIRECTIONS = ["d", "down", "below"]

def index_to_range(index):
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