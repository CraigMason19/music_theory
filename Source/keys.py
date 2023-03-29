#-------------------------------------------------------------------------------
# Name:        keys.py
#
# Notes:       Contains a KeyType class and methods for building and printing 
#              keys and dominant keys
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
        parralell(self):
            A class method to return a parralell (opposite) key type.
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


    def parralell(self):
        """ Returns the opposite KeyType. 

            e.g. C Minor is the parralell of C Major.

        Args:
            None.

        Returns:
            A KeyType
        """
        if self.name == 'Major':
            return KeyType.Minor
         
        return KeyType.Major


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

def chords_in_key(note, key_type=KeyType.Major):
    """ Returns a dict representing all the chords in the key.

        The key is a Roman numeral as used in traditional notation. 
        A upper case numneral represents a major chord and a lower case numeral
        represents a minor chord (or diminished).

        Args:
            note: 
                The note the key is based on.
            key_type: 
                A KeyType class that can be either major or minor.
            
       Returns:
            A dict in the form. key=RomanNumeral value=Chord
            e.g. { "I": Chord(C, ChordType.Major) ... }
    """
    scale, numerals, sequence = None, None, None
    
    if key_type == KeyType.Major:
        numerals = ["I", "ii", "iii", "IV", "V", "vi", "vii"]
        scale = Scale(note, ScaleType.Major)
        sequence = [ChordType.Major, ChordType.Minor, ChordType.Minor, 
                    ChordType.Major, ChordType.Major, ChordType.Minor, 
                    ChordType.Diminished]
        
    elif key_type == KeyType.Minor:
        numerals = ["i", "ii", "III", "iv", "v", "VI", "VII"]
        scale = Scale(note, ScaleType.Minor)
        sequence = [ChordType.Minor, ChordType.Diminished, ChordType.Major, 
                    ChordType.Minor, ChordType.Minor, ChordType.Major, 
                    ChordType.Major]

    return  {n[0]: Chord(n[1], n[2]) for n in zip(numerals, scale.notes, sequence)}
 
def dominant_chords_in_key(note, key_type=KeyType.Major):
    """ Returns a dict representing all the chords in dominant the key.

        The dominant key is created by raising the root note of the chord in 
        the main key up a 5th. It is then turned into a seventh cord.     
        
        e.g. C Major
            I        ii       iii        IV         V        vi       vii
            V7/I     V7/ii    V7/iii     V7/IV      V7/V     V7/vi    V7/vii

        Args:
            note: 
                The note the key is based on.
            key_type: 
                A KeyType class that can be either major or minor.
            
       Returns:
            A dict in the form. key='V7/RomanNumeral' value=Chord
            e.g. { "V7/I": Chord(C, ChordType.Seven) ... }
    """
    chords = chords_in_key(note, key_type)

    # Shift root note up a 5th
    dom_notes = [transpose(chord.root, Interval.P5) for k, chord in chords.items()]

    # Create a seventh chord from this new note.
    dom_chords = [Chord(note, ChordType.Seven) for note in dom_notes]

    return {f'V7/{n[0]}': n[1] for n in zip(chords.keys(), dom_chords)}

def pretty_print_key(note, key_type=KeyType.Major):
    """ Prints out the key information in a formatted table view. 
    
        First row is the chords in the key.
        Second row is the chords in the dominant key (Seventh Chords).
        Last row is the parralel chords in (the opposite key).
    
        E.g.

            Key of C Minor:
                    Cm      Ddim       EbM        Fm        Gm       AbM       BbM
                     i        ii       III        iv         v        VI       VII

                    G7        A7       Bb7        C7        D7       Eb7        F7
                  V7/i     V7/ii    V7/III     V7/iv      V7/v     V7/VI    V7/VII

                    CM        Dm        Em        FM        GM        Am      Bdim
                     I        ii       iii        IV         V        vi       vii

        Args:
            note: 
                The note the key is based on.
            key_type: 
                A KeyType class that can be either major or minor.
            
       Returns:
            None.
    """
    chords = chords_in_key(note, key_type)
    parallel_chords = chords_in_key(note, key_type.parralell())
    dominant_chords = dominant_chords_in_key(note, key_type)
    
    print(f"Key of {note} {key_type}:")

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
    """ Example Usage """
    pretty_print_key(Note.C)
    print("")
    pretty_print_key(Note.C, KeyType.Minor)

if __name__ == '__main__':
    main()