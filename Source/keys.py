#-------------------------------------------------------------------------------
# Name:        keys.py
#
# Notes:         
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import random

from enum import Enum

from notes import Note, Interval, transpose
from chords import Chord, ChordType
from scales import Scale, ScaleType

# TODO get all chords c, pc = return chords, parallel_chords
# def chords_in_key(key, scaletype):
# only have major minor keys
# add key_type class???

class KeyType(Enum):
    """ Represents a key type. Keys are either Major or Minor.
    
    Attributes:
        class attributes:
            2 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        random(cls):
            A class method to return a random key type.
        __str__(self):
            Returns the name of the key type.
        __repr__(self):
            Returns the Enum name.
    """
    (Major, Minor) = range(2) 

    @classmethod    
    def items(cls):
        """ Returns a list of the key enumerations. 

            e.g. [KeyType.Major, KeyType.Minor ... ]

        Args:
            None.

        Returns:
            A list of key types.
        """  
        return [n for n in cls]

    @classmethod
    def random(cls):
        """ Returns a random key. 

            e.g. KeyTime.Major

        Args:
            None.

        Returns:
            A KeyType.
        """  
        return random.choice(cls.items())

    def __str__(self):
        """ Returns a string representing the key name. 

            e.g. str(KeyType.Major) -> 'Major'

        Args:
            None.

        Returns:
            A string.
        """
        return self.name

    def __repr__(self):
        """ Returns a string representing the key types enum. 

            e.g. repr(KeyType.Major) -> 'KeyType.Major'

        Args:
            None.

        Returns:
            A string representing the key's name.
        """
        return f'KeyType.{self.name}'

def chords_in_key(key, key_type=KeyType.Major):
    scale, numerals, sequence = None, None, None
    
    if key_type == KeyType.Major:
        numerals = ["I", "ii", "iii", "IV", "V", "vi", "vii"]
        scale = Scale(key, ScaleType.Major)
        sequence = [ChordType.Major, ChordType.Minor, ChordType.Minor, 
                    ChordType.Major, ChordType.Major, ChordType.Minor, 
                    ChordType.Diminished]
        
    elif key_type == KeyType.Minor:
        numerals = ["i", "ii", "III", "iv", "v", "VI", "VII"]
        scale = Scale(key, ScaleType.Minor)
        sequence = [ChordType.Minor, ChordType.Diminished, ChordType.Major, 
                    ChordType.Minor, ChordType.Minor, ChordType.Major, 
                    ChordType.Major]

    return  {n[0]: Chord(n[1], n[2]) for n in zip(numerals, scale.notes, sequence)}












# TODO in chords add to method
# dominant
def dominant_chords_in_key(key, key_type=KeyType.Major):
    # dominant is 5th up from root G->D
    # sec dom is everything else
    # [dominant] + [secondary_sominants]

    chords = chords_in_key(key, key_type)

    # shift up a 5th
    dom_notes = [transpose(chord.root, Interval.P5) for k, chord in chords.items()]
    dom_chords = [Chord(n, ChordType.Seven) for n in dom_notes]


    return {f'V7/{n[0]}': n[1] for n in zip(chords.keys(), dom_chords)}

 
def pretty_print_key(key, key_type=KeyType.Major):
    first, second = None, None

    if key_type == KeyType.Major:
        first, second = KeyType.Major, KeyType.Minor
    else:
        first, second = KeyType.Minor, KeyType.Major



    chords = chords_in_key(key, first)
    parallel_chords = chords_in_key(key, second)
    dominant_chords = dominant_chords_in_key(key, first)
    



    print(f"Key of {key} {first}:")

    table_data = [
        [str(chord) for chord in chords.values()],
        list(chords.keys()), 
        ["", "", "", "", "", "", "",],

        [str(chord) for chord in dominant_chords.values()],
        list(dominant_chords.keys()),
        ["", "", "", "", "", "", "",],

        [str(chord) for chord in parallel_chords.values()],
        list(parallel_chords.keys()),
    ]

    for row in table_data:
        print(("{: >10}" * 7).format(*row))

def main():
    pretty_print_key(Note.D)
    print("")
    pretty_print_key(Note.D, KeyType.Minor)

if __name__ == '__main__':
    main()