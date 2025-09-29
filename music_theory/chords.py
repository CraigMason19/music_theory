from music_theory.notes import Note, transpose
from music_theory.intervals import Interval
from music_theory.chord_type import ChordType

class Chord:
    """ 
    A class representing a musical chord. 

    Attributes:
        root:
            The Note the rest of the chord is built from.
        type:
            A ChordType. 
        notes:
            An array containing the root, 3rd(Major or Minor) & the fifth

    Methods:
        __init__(self, root, chord_type):
            Constructs the chord.
        random(cls):
            A class method to return a random chord.
        __eq__(self, other):
            Compares two chords.
        notation(self):
            Returns the chord's notation without the Note.
        quality(self):
            An alias for notation. Returns the chord's notation without the Note.
        add9(self):
            Returns an array of the chord's notes with the added 9th
        add11(self):
            Returns an array of the chord's notes with the added 11th
        add13(self):
            Returns an array of the chord's notes with the added 13th
        __str__(self):
            Returns a string representation of the Chord.
        __repr__(self):
            Returns a string representation of the Chord.
    """
    def __init__(self, root: Note, chord_type: ChordType = ChordType.Major) -> None:
        """ 
        Constructs the chord.

        Args:
            root:
                The root note to build the chord from.
            chord_type:
                The ChordType to represent the chord.

        Returns:
            None.

        Raises:
            ValueError:
                If the chord_type is not valid.
        """  
        self.root, self.chord_type, self.notes = root, chord_type, []

        match self.chord_type:
            case ChordType.Major:
                self.notes = [self.root, transpose(self.root, Interval.M3), transpose(self.root, Interval.P5)]

            case ChordType.Minor:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.P5)]

            case ChordType.Diminished:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.dim5)]

            case ChordType.Dominant7:
                self.notes = [self.root, transpose(self.root, Interval.M3), transpose(self.root, Interval.P5), transpose(self.root, Interval.m7)]
            
            case ChordType.Major7:
                self.notes = [self.root, transpose(self.root, Interval.M3), transpose(self.root, Interval.P5), transpose(self.root, Interval.M7)]

            case ChordType.Minor7:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.P5), transpose(self.root, Interval.m7)]
            
            case ChordType.Diminished7:
                self.notes = [self.root, transpose(self.root, Interval.m3), transpose(self.root, Interval.dim5), transpose(self.root, Interval.M6)]

            case ChordType.Sus2:
                self.notes = [self.root, transpose(self.root, Interval.M2), transpose(self.root, Interval.P5)]        

            case ChordType.Sus4:
                self.notes = [self.root, transpose(self.root, Interval.P4), transpose(self.root, Interval.P5)]      

            case _:
                raise ValueError(f"Unknown chord type: {self.chord_type}")
    
    @classmethod
    def random(cls) -> ChordType:
        """ 
        A class method that returns a random chord. 

        e.g. Fdim

        Args:
            None.

        Returns:
            A Chord.
        """  
        return Chord(Note.random(), ChordType.random())

    def __eq__(self, other: ChordType) -> bool:
        """ 
        Equality operator to check that both the note and chord type match. 

        e.g. Chord(F, ChordType.Diminished) == Chord(F, ChordType.Diminished)

        Args:
            other:
                The other Chord to compare.

        Returns:
            A bool. True if this and another chord are the same.
        """
        try:
            return self.root == other.root and self.chord_type == other.chord_type
        except AttributeError:
            return False

    @property
    def notation(self) -> str:
        """ 
        A property that returns the chord's notation without the Note. 
        Also known as the quality.

        e.g. 'F°' -> '°'

        Args:
            None.

        Returns:
            A string.
        """    
        match self.chord_type:
            case ChordType.Minor:
                return "m" 
            
            case ChordType.Diminished:
                return "°"
            
            case ChordType.Dominant7:
                return "7"   

            case ChordType.Major7:
                return "Δ7"            

            case ChordType.Minor7:
                return "m7"      

            case ChordType.Diminished7:
                return "°7"   
                        
            case ChordType.Sus2:
                return "sus2"
            
            case ChordType.Sus4:
                return f"sus4"
            
            case _:
                return f"M"
            
    quality = notation  # Alias

    def add9(self) -> str:
        """ 
        Returns an array containing the notes of the chord with the added 9th. 

        e.g. Chord(Note.A).add9() -> [Note.A, Note.Db, Note.E, Note.B]

        Args:
            None.

        Returns:
            An array.
        """    
        return self.notes + [transpose(self.root, Interval.M2)]

    def add11(self) -> str:
        """ 
        Returns an array containing the notes of the chord with the added 11th. 

        e.g. Chord(Note.A).add11() -> [Note.A, Note.Db, Note.E, Note.D]

        Args:
            None.

        Returns:
            An array.
        """    
        return self.notes + [transpose(self.root, Interval.P4)]
    
    def add13(self) -> str:
        """ 
        Returns an array containing the notes of the chord with the added 13th. 

        e.g. Chord(Note.A).add13() -> [Note.A, Note.Db, Note.E, Note.Gb]

        Args:
            None.

        Returns:
            An array.
        """    
        return self.notes + [transpose(self.root, Interval.M6)]
    
    def __str__(self) -> str:
        """ 
        Returns a string representing the Chord name and type. 

        e.g. str(Chord(Note.E, ChordType.Dominant7)) -> E7

        Args:
            None.

        Returns:
            A string.
        """
        return f"{self.root}{self.notation}"

    def __repr__(self) -> str:
        """ 
        Returns a string representing the Chord. 

        e.g. repr(Chord(Note.E, ChordType.Dominant7)) -> Chord(E, Dominant7)

        Args:
            None.

        Returns:
            A string.
        """
        return f"Chord({self.root}, {self.chord_type})"

    
#region Functions

def unique_notes_in_chords(*args: Chord) -> list[Note]:
    """
    Collects all unique notes from the given Chords and returns them as a 
    list, sorted by the Notes enumeration value.

    Example:
        >>> unique_notes_in_chords(
        ...     Chord(Note.A, ChordType.Major),
        ...     Chord(Note.A, ChordType.Minor)
        ... )
        [Note.C, Note.Db, Note.E, Note.A]

    Args:
        *args (Chord): 
            One or more Chord objects to extract notes from.

    Returns:
        list[Note]: 
            A list of unique Notes sorted by their value.
    """ 
    notes: list[Note] = []

    for c in args:
        notes.extend(c.notes)

    return sorted(set(notes), key=lambda n: n.value)

#endregion