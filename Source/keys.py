#-------------------------------------------------------------------------------
# Name:        keys.py
#
# Notes:       Contains a KeyType class and methods for building and printing 
#              keys, dominant and parallel keys.
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
            A method to return a parralell (opposite) key type.
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

            e.g. KeyType.Major

        Args:
            None.

        Returns:
            A KeyType.
        """  
        return random.choice(cls.items())


    def parallel(self):
        """ Returns the opposite KeyType. 

            e.g. C Minor is the parallel of C Major.

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


class Key:
    def __init__(self, root, key_type):
        self.root = root
        self.type = key_type

    @classmethod
    def random(cls):
        """ Returns a random key. 

            e.g. C Minor

        Args:
            None.

        Returns:
            A Key.
        """  
        return Key(Note.random(), KeyType.random())

    @property
    def name(self):
        """ Returns the name of the key, the root and key type. 

            e.g. 'C MAJOR'

        Args:
            None.

        Returns:
            A string.
        """
        return f"{self.root} {self.type}"

    def chords(self):
        """ Returns a dict representing all the chords in the key.

            The dict key is a Roman numeral as used in traditional notation. 
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
        
        if self.type == KeyType.Major:
            numerals = ["I", "ii", "iii", "IV", "V", "vi", "vii"]
            scale = Scale(self.root, ScaleType.Major)
            sequence = [ChordType.Major, ChordType.Minor, ChordType.Minor, 
                        ChordType.Major, ChordType.Major, ChordType.Minor, 
                        ChordType.Diminished]
            
        elif self.type == KeyType.Minor:
            numerals = ["i", "ii", "III", "iv", "v", "VI", "VII"]
            scale = Scale(self.root, ScaleType.Minor)
            sequence = [ChordType.Minor, ChordType.Diminished, ChordType.Major, 
                        ChordType.Minor, ChordType.Minor, ChordType.Major, 
                        ChordType.Major]

        return  {n[0]: Chord(n[1], n[2]) for n in zip(numerals, scale.notes, sequence)}
 
    def parallel_chords(self):
        parallel = Key(self.root, self.type.parallel())
        return parallel.chords()

    def dominant_chords(self):
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
        chords = self.chords()

        # Shift root note up a 5th
        dom_notes = [transpose(chord.root, Interval.P5) for k, chord in chords.items()]

        # Create a seventh chord from this new note.
        dom_chords = [Chord(note, ChordType.Seven) for note in dom_notes]

        return {f'V7/{n[0]}': n[1] for n in zip(chords.keys(), dom_chords)}




    def pretty_print(self, dominant=False, parallel=False):
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
        print(f"Key of {self.root} {self.type}:")

        chords = self.chords()
        table_data = [
            [str(chord) for chord in chords.values()],
            list(chords.keys()), 
        ]

        if dominant:
            dominant_chords = self.dominant_chords()
            dominant_data = [
                ["", "", "", "", "", "", "",],
                [str(chord) for chord in dominant_chords.values()],
                list(dominant_chords.keys()),
            ]
            table_data += dominant_data
        
        if parallel:
            parallel_chords = self.parallel_chords()
            parallel_data = [
                ["", "", "", "", "", "", "",],
                [str(chord) for chord in parallel_chords.values()],
                list(parallel_chords.keys()),
            ]
            table_data += parallel_data

        for row in table_data:
            print(("{: >10}" * 7).format(*row)) # Always 7 chords in a key

    def __str__(self):
        return f'{self.root} {self.type}' 

    def __repr__(self):
        return f'Key({self.root} {self.type})' 

def main():
    """ Example Usage """
    key = Key.random()

    print(f"Key of {key.name}:")
    print(f"\tstr() -> {str(key)}")
    print(f"\trep() -> {repr(key)}")
    print(f"\tRoot -> {key.root}")
    print(f"\tType -> {key.type}")

    print(f"\tChords:")
    for numeral, chord in key.chords().items():
        print(f"\t\t{numeral}: {chord}")

    print(f"\tDominant Chords:")
    for numeral, chord in key.dominant_chords().items():
        print(f"\t\t{numeral}: {chord}")

    print(f"\tParallel Chords:")
    for numeral, chord in key.parallel_chords().items():
        print(f"\t\t{numeral}: {chord}")

    key.pretty_print(dominant=True, parallel=True)

if __name__ == '__main__':
    main()