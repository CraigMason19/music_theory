#-------------------------------------------------------------------------------
# Name:        keys.py
#
# Notes:       Contains KeyType and Key class and methods for building and 
#              printing standard, dominant and parallel keys.
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

""" The circle of 5th's and keys.

Going to the right of the circle goes up a 5th and to the left goes down a 5th.

The outside are Major keys, the inside is Minor keys. This shows the relative 
connection between the keys.

The circle shows how many sharps and flats are in the key.

# Order of Sharps 
# F C G D A E B
# Fast Cars Go Dangerously Around Every Bend
# 
# Order of flats (the reverse)
# B E A D G C F
# Before Eating A Doughnut Get Coffee First.
"""

class KeyType(Enum):
    """ Represents a key type. Keys are either Major or Minor.
    
    Attributes:
        Type attributes:
            2 class attributes representing a Enum.

    Methods:
        items(cls):
            A class method to return the enums as a list.
        random(cls):
            A class method to return a random key type.
        parallel(self):
            A property that returns a parallel (opposite) key type.
        __str__(self):
            Returns the name of the key type.
        __repr__(self):
            Returns the Enum name.
    """
    (Major, Minor) = range(2) 

    @classmethod    
    def items(cls):
        """ A class method that returns a list of the key enumerations. 

            e.g. [KeyType.Major, KeyType.Minor ... ]

        Args:
            None.

        Returns:
            A list of key types.
        """  
        return [n for n in cls]

    @classmethod
    def random(cls):
        """ A class method that returns a random key type. 

            e.g. KeyType.Major

        Args:
            None.

        Returns:
            A KeyType.
        """  
        return random.choice(cls.items())

    @property
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
        """ Returns a string representing the key type name. 

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
            A string representing the key type's name.
        """
        return f'KeyType.{self.name}'

class Key:
    """ Represents a musical key. A key is important to find what chords can be 
        used.

    Attributes:
        root:
            A note that the key starts on. (defines the I chord)
        type:
            A KeyType. (Major or Minor)

    Methods:
        __init__(root, key_type=KeyType.Major):
            Contructs the key.
        __eq__(self, other):
            Compares two keys.
        random(cls):
            A class method that returns a random Key from a random Note.
        parallel(self):
            A property that returns the paralell (opposite) key.
        relative_key(self):
            A property that returns the key relative to this one.
        name(self):
            A property that returns the name of the key.
        sharp_count(self):
            A property that returns the number of sharps in a key.
        flat_count(self):
            A property that returns the number of flats in a key.
        sharps(self):
            A property that returns a list of the sharp notes.
        flats(self):
            A property that returns a list of the flat notes.
        chords(self):
            Returns a dict containing the chords of the key.
        parallel_chords(self):
            Returns a dict containing the parallel chords of the key.
        dominant_chords(self):
            Returns a dict containing the dominant chords of the key.
        pretty_print(self, dominant=False, parallel=False):
            Prints out the chords in a easy to read table format.
        __str__(self):
            Returns the name of the key.
        __repr__(self):
            Returns the name of the key.
    """
    def __init__(self, root, key_type=KeyType.Major):
        """ Constructs the key 

            e.g. C Minor

        Args:
            root:
                The note to build the key from
            key_type:
                The type of the key to be built.

        Returns:
            None.
        """  
        self.root = root
        self.type = key_type

    def __eq__(self, other):
        """ Equality operator to check that both the note and key type match. 

            e.g. Key(Note.F, KeyType.Major) == Key(Note.F, KeyType.Major)

        Args:
            other:
                The other Key to compare.

        Returns:
            A bool. True if this and another key are the same.
        """
        try:
            return self.root == other.root and self.type == other.type
        except AttributeError:
            return False

    @classmethod
    def random(cls):
        """ A class method that returns a random key. 

            e.g. C Minor

        Args:
            None.

        Returns:
            A Key.
        """  
        return Key(Note.random(), KeyType.random())

    @property
    def parallel(self):
        """ Returns the paralell (opposite) key. 

            e.g. C Minor -> C Major

        Args:
            None.

        Returns:
            A Key.
        """  
        return Key(self.root, self.type.parallel)

    @property
    def relative_key(self):
        """ Returns the relative key. If a Key is Major it will have a relative 
            Minor key (and vice-versa). This can be easily found on a instrument
            by going up or down 3 semitones.   

        Args:
            None.

        Returns:
            A Key.        
        """
        if self.type == KeyType.Major:
            new_note = transpose(self.root, Interval.m3, direction='d')
            return Key(new_note, KeyType.Minor)

        else:
            new_note = transpose(self.root, Interval.m3, direction='u')
            return Key(new_note, KeyType.Major)

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

    @property
    def sharp_count(self):
        """ Returns the number of sharps in this key. 
        
        Args:
            None.

        Returns:
            An integer.        
        """
        if self.type == KeyType.Minor:
            return self.relative_key.sharp_count

        note = Note.C

        for i in range(7+1):
 
            if note == self.root:
                return i

            note = transpose(note, Interval.P5) 

        return 0

    @property
    def flat_count(self):
        """ Returns the number of flats in this key.
        
        Args:
            None.

        Returns:
            An integer.        
        """
        if self.type == KeyType.Minor:
            return self.relative_key.flat_count

        note = Note.C

        for i in range(7+1):
            if note == self.root:
                return i

            note = transpose(note, Interval.P5, direction='d') 

        return 0

    @property
    def sharps(self):
        """ Returns a list of the sharps in this key.
        
        Order of Sharps 
        F C G D A E B
        Fast Cars Go Dangerously Around Every Bend

        Args:
            None.

        Returns:
            An list of Notes.        
        """
        order_of_sharps = [Note.F, Note.C, Note.G, Note.D, Note.A, Note.E, Note.B]
        return order_of_sharps[:self.sharp_count]

    @property
    def flats(self):
        """ Returns a list of the flats in this key.

        Order of flats (the reverse of the order of sharps)
        B E A D G C F
        Before Eating A Doughnut Get Coffee First.

        Args:
            None.

        Returns:
            An list of Notes.        
        """
        order_of_flats = [Note.B, Note.E, Note.A, Note.D, Note.G, Note.C, Note.F]
        return order_of_flats[:self.flat_count]

    def chords(self):
        """ Returns a dict representing all the chords in the key.

            The dict key is a Roman numeral as used in traditional notation. 
            A upper case numneral represents a major chord and a lower case numeral
            represents a minor chord (or diminished).

            Args:
                None.
                
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
        """ Returns a dict representing all the parallel chords in the key.

            These are the chords that are constructed from the parallel (opposite)
            key. e.g. the paralell chords of C Major are the chords of C Minor. 

        Args:
            None
                
        Returns:
                A dict in the form. key=RomanNumeral value=Chord
                e.g. { "I": Chord(C, ChordType.Major) ... }
        """
        return self.parallel.chords()

    def dominant_chords(self):
        """ Returns a dict representing all the chords in dominant the key.

            The dominant key is created by raising the root note of the chord in 
            the main key up a 5th. It is then turned into a seventh cord.     
            
            e.g. C Major
                I        ii       iii        IV         V        vi       vii
                V7/I     V7/ii    V7/iii     V7/IV      V7/V     V7/vi    V7/vii

        Args:
            None.
                
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
                Chords of C Minor:
                        Cm      Ddim       EbM        Fm        Gm       AbM       BbM
                        i        ii       III        iv         v        VI       VII

                        G7        A7       Bb7        C7        D7       Eb7        F7
                    V7/i     V7/ii    V7/III     V7/iv      V7/v     V7/VI    V7/VII

                        CM        Dm        Em        FM        GM        Am      Bdim
                        I        ii       iii        IV         V        vi       vii

        Args:
            dominant: 
                A bool indicating whether you want to print the dominant chords.
            parallel: 
                A bool indicating whether you want to print the parallel chords.
                
        Returns:
                None.
        """      
        print(f"Chords of {self.root} {self.type}:")

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
        """ Returns a string representing the key. 

            e.g. str(Key(Note.G, KeyType.Major)) -> 'G Major'

        Args:
            None.

        Returns:
            A string.
        """
        return f'{self.root} {self.type}' 

    def __repr__(self):
        """ Returns a string representing the key. 

            e.g. repr(Key(Note.G, KeyType.Major)) -> 'Key(G Major)'

        Args:
            None.

        Returns:
            A string representing the key type's name.
        """
        return f'Key({self.root} {self.type})' 

def chords_from_progression(key, progression, error='X'):
    """ Returns a list of chords that match a progression in a key. Error is 
        used if a chord can't be found in the progression.

        e.g. key=C Major, progression=['I', 'IV', 'V']'
            -> [C Major, F Major, G Major]

    Args:
        key:
            The key the chords are from.
        progression:
            A list of roman numerals notating the chords.
        error:
            A empty value representing a missing of invalid chord in the key.

    Returns:
        A List of chords.
    """
    chord_dict = key.chords()

    l = []
    for numeral in progression:
        if numeral in chord_dict:
            l.append(str(chord_dict[numeral]))
        else:
            l.append(error)

    return l

def main():
    """ Example Usage """
    key = Key.random()

    print(f"Key of {key.name}:")
    print(f"\tstr() -> {str(key)}")
    print(f"\trepr() -> {repr(key)}")
    print(f"\tRoot -> {key.root}")
    print(f"\tType -> {key.type}")
    print(f"\tParallel -> {key.parallel}")
    print(f"\tRelative -> {key.relative_key}")
    print(f"\tSharp Count -> {key.sharp_count}")
    print(f"\tSharps -> {key.sharps}")
    print(f"\tFlat Count -> {key.flat_count}")
    print(f"\tFlats -> {key.flats}")
    
    # print(f"\tChords:")
    # for numeral, chord in key.chords().items():
    #     print(f"\t\t{numeral}: {chord}")

    # print(f"\tDominant Chords:")
    # for numeral, chord in key.dominant_chords().items():
    #     print(f"\t\t{numeral}: {chord}")

    # print(f"\tParallel Chords:")
    # for numeral, chord in key.parallel_chords().items():
    #     print(f"\t\t{numeral}: {chord}")

    print('')
    key.pretty_print(dominant=True, parallel=True)

if __name__ == '__main__':
    main()