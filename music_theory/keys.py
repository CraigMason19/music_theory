#-------------------------------------------------------------------------------
# Name:        keys.py
#
# Notes:       Contains KeyType and Key class and methods for building and 
#              printing standard, dominant and parallel keys.
#
#-------------------------------------------------------------------------------

from typing import Self

from music_theory.notes import Note, transpose
from music_theory.intervals import Interval
from music_theory.chords import Chord
from music_theory.chord_type import ChordType
from music_theory.scales import Scale, ScaleType
from music_theory.key_type import KeyType

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

class Key:
    """ 
    Represents a musical key. A key is important to find what chords can be 
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
        to_string_array(self, dominant=False, parallel=False):
            Returns the chords in the key as an array of strings.
        pretty_print(self, dominant=False, parallel=False):
            Prints out the chords in a easy to read table format.
        __str__(self):
            Returns the name of the key.
        __repr__(self):
            Returns the name of the key.
    """
    def __init__(self, root: Note, key_type: KeyType=KeyType.Major) -> None:
        """
        Constructs the key from a Note and a KeyType. 

        Example:
            >>> Key(Note.C, KeyType.Major)
            C Minor

        Args:
            root (Note):
                The note to build the key from.
            key_type (KeyType):
                The type of the key to be built.
        """  
        self.root = root
        self.type = key_type

    def __eq__(self, other: Self) -> bool:
        """ 
        Equality operator to check that both the note and key type match. 

        Example:
            >>> Key(Note.F, KeyType.Major) == Key(Note.F, KeyType.Major)
            True

        Args:
            other (Key):
                The other Key to compare.

        Returns:
            bool: 
                True if this and another key have the same note and key_type properties. False otherwise. 
        """
        try:
            return self.root == other.root and self.type == other.type
        except AttributeError:
            return False

    @classmethod
    def random(cls) -> Self:
        """
        A class method that returns a random key. 

        Returns:
            Key:
        """  
        return Key(Note.random(), KeyType.random())

    @property
    def parallel(self) -> Self:
        """ 
        Returns the paralell (opposite) key. 

        Example:
            >>> F Minor.parallel
            F Major

        Returns:
            Key:
        """  
        return Key(self.root, self.type.parallel)

    @property
    def relative_key(self) -> Self:
        """ 
        Returns the relative key. If a Key is Major it will have a relative 
        Minor key (and vice-versa). This can be easily found on a instrument
        by going up or down 3 semitones.   

        Returns:
            Key:
        """  
        if self.type == KeyType.Major:
            new_note = transpose(self.root, Interval.m3, direction='d')
            return Key(new_note, KeyType.Minor)

        else:
            new_note = transpose(self.root, Interval.m3, direction='u')
            return Key(new_note, KeyType.Major)

    @property
    def name(self) -> str:
        """ 
        Returns the name of the key, the root and key type. 

        e.g. 'C MAJOR'

        Returns:
            str:
                Representing the Key's Note and KeyType.
        """
        return f"{self.root} {self.type}"

    @property
    def sharp_count(self) -> int:
        """ 
        Returns the number of sharps in this key. 

        Returns:
            int:     
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
    def flat_count(self) -> int:
        """ 
        Returns the number of flats in this key.

        Returns:
            int:     
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

        Returns:
            An list of Notes.        
        """
        order_of_flats = [Note.B, Note.E, Note.A, Note.D, Note.G, Note.C, Note.F]
        return order_of_flats[:self.flat_count]

    def chords(self) -> dict[str, Chord]:
        """ 
        Returns a dict representing all the chords in the key.

        The dict key is a Roman numeral as used in traditional notation. 
        A upper case numneral represents a major chord and a lower case numeral
        represents a minor chord.

        Note: The major key has a diminished 7th (vii°) and the minor a diminished 2nd (ii°)
                
        Returns:
            dict[str, Chord]:
                key=RomanNumeral value=Chord
                e.g. { "I": Chord(C, ChordType.Major) ... }
        """
        scale, numerals, sequence = None, None, None
        
        if self.type == KeyType.Major:
            numerals = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
            scale = Scale(self.root, ScaleType.Major)
            sequence = [ChordType.Major, ChordType.Minor, ChordType.Minor, 
                        ChordType.Major, ChordType.Major, ChordType.Minor, 
                        ChordType.Diminished]
            
        elif self.type == KeyType.Minor:
            numerals = ["i", "ii°", "III", "iv", "v", "VI", "VII"]
            scale = Scale(self.root, ScaleType.Minor)
            sequence = [ChordType.Minor, ChordType.Diminished, ChordType.Major, 
                        ChordType.Minor, ChordType.Minor, ChordType.Major, 
                        ChordType.Major]

        return  {n[0]: Chord(n[1], n[2]) for n in zip(numerals, scale.notes, sequence)}
 
    def parallel_chords(self):
        """ Returns a dict representing all the parallel chords in the key.

            These are the chords that are constructed from the parallel (opposite)
            key. e.g. the paralell chords of C Major are the chords of C Minor. 
                
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
                
        Returns:
                A dict in the form. key='V7/RomanNumeral' value=Chord
                e.g. { "V7/I": Chord(C, ChordType.Dominant7) ... }
        """
        chords = self.chords()

        # Shift root note up a 5th
        dom_notes = [transpose(chord.root, Interval.P5) for k, chord in chords.items()]

        # Create a seventh chord from this new note.
        dom_chords = [Chord(note, ChordType.Dominant7) for note in dom_notes]

        return {f'V7/{n[0]}': n[1] for n in zip(chords.keys(), dom_chords)}

    def to_string_array(self, dominant=False, parallel=False):
        """
        Generates a formatted chord table for the current key as a list of strings.

        The output includes:
            - Diatonic chords in the key (e.g. C Major or C Minor)
            - [Optional] dominant seventh chords (V7 of each degree)
            - [Optional] parallel key chords (relative major/minor)

        Example output:
            Chords of C Minor:
                CM        Dm        Em        FM        GM        Am        B°
                 I        ii       iii        IV         V        vi       vii

                G7        A7        B7        C7        D7        E7       Gb7
              V7/I     V7/ii    V7/iii     V7/IV      V7/V     V7/vi    V7/vii

                Cm        D°       EbM        Fm        Gm       AbM       BbM
                 i        ii       III        iv         v        VI       VII

        Args:
            dominant: 
                A bool indicating whether you want to print the dominant chords.
            parallel: 
                A bool indicating whether you want to print the parallel chords.
                
        Returns:
            List[str]: An array of strings representing the formatted chord lines.
        """     
        data = [f"Chords of {self.root} {self.type}:"] 

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
            data.append(("{: >10}" * 7).format(*row)) # Always 7 chords in a key

        return data

    def pretty_print(self, dominant=False, parallel=False) -> None:
        """ Prints out the key information in a formatted table view. 
        
        The output includes:
            - Diatonic chords in the key (e.g. C Major or C Minor)
            - [Optional] dominant seventh chords (V7 of each degree)
            - [Optional] parallel key chords (relative major/minor)

        Example output:
            Chords of C Minor:
                CM        Dm        Em        FM        GM        Am        B°
                 I        ii       iii        IV         V        vi       vii

                G7        A7        B7        C7        D7        E7       Gb7
              V7/I     V7/ii    V7/iii     V7/IV      V7/V     V7/vi    V7/vii

                Cm        D°       EbM        Fm        Gm       AbM       BbM
                 i        ii       III        iv         v        VI       VII

        Args:
            dominant: 
                A bool indicating whether you want to print the dominant chords.
            parallel: 
                A bool indicating whether you want to print the parallel chords.
        """      
        for line in self.to_string_array(dominant, parallel):
            print(line)

    def __str__(self) -> str:
        """ 
        Returns a string representing the key. 

        Example:
            >>> str(Key(Note.G, KeyType.Major))
            G Major

        Returns:
            str:
        """
        return f'{self.root} {self.type}' 

    def __repr__(self) -> str:
        """ 
        Returns a string representing the key. 

        Example:
            >>> repr(Key(Note.G, KeyType.Major))
            Key(G Major)

        Returns:
            str:
                A string representing the key type's name.
        """
        return f'Key({self.root} {self.type})' 