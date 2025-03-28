#-------------------------------------------------------------------------------
# Name:        utils.py
#
# Notes:       
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

UP_DIRECTIONS = ["u", "up", "above"]
DOWN_DIRECTIONS = ["d", "down", "below"]

# Single underscore indicates that this function is not meant to be imported from
# other modules.
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