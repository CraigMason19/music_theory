#-------------------------------------------------------------------------------
# Name:        notes.py
#
# Notes:       A representation of the 12 notes of the musical scale
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random
from enum import Enum

# TODO - Remove global
# NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def _index_to_range(index):
    """ Takes a index and converts it into the range -11 to +11.

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
    Unison, m2, M2, m3, M3, P4, dim5, P5, m6, M6, m7, M7 = range(12) 

    @classmethod    
    def items(cls):
        return [n for n in cls]
 
    @classmethod
    def from_index(cls, index):
        index = _index_to_range(index)
        return Interval.items()[index]

class Note(Enum):
    # Note:
    #   - Can't have sharps (#) in variable names
    #   - Start at 'middle c'
    C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B = range(12) 

    @classmethod    
    def items(cls):
        return [n for n in cls]
 
    @classmethod
    def from_index(cls, index):
        index = _index_to_range(index)
        return Note.items()[index]

    @classmethod
    def random(cls):
        r = random.choice(cls.items())
        return r

    def __str__(self):
        return self.name

def notes_to_string(note_list):
    return ', '.join([n.name for n in note_list])

def intervals_to_string(interval_list):
    return ', '.join([i.name for i in interval_list])



    # Note: A perfect 5th down is the same as a perfect 5th up and vice-versa
# def interval_distance(first_note, second_note, direction="u"):
#     if(first_note == second_note):
#         return Interval.Unison

#     direction = direction.lower()

#     if direction in ["u", "up", "above"]:
#         dif = 12 - abs(first_note.value - second_note.value)
#         return Interval.from_index(dif)
        

#     elif direction in ["d", "down", "below"]:
#         dif = 12 + abs(first_note.value - second_note.value)
#         return Interval.from_index(dif)

#     raise ValueError(f'direction not recognized({direction})')


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
    # n = Note.C
    # ns = notes_to_string([Note.C, Note.B, Note.D])

    # print(n)
    # print(ns)

    # print(Note.random())

    # ac = interval_distance(Note.A, Note.C) # -> m3
    # cf = interval_distance(Note.C, Note.F) # ->
    # ag = interval_distance(Note.A, Note.G) # ->
    # print(ac, cf, ag)

 
    pass
 

if __name__ == '__main__':
    main()