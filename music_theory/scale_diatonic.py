#-------------------------------------------------------------------------------
# Name:        scale_diatonic.py
#
# Notes:       A class representing a diatonic scale (7 notes)
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from music_theory.intervals import Interval, interval_distance
from music_theory.notes import Note
from music_theory.scale_type import ScaleType
from music_theory.scales import Scale

class DiatonicScale(Scale):
    """ 
    An class that represents a diatonic scale (7 notes) with properties for the 
    scale degrees. Inherited from the Scale class.

    NOTE: 
        While the scale degrees for the first six notes are the same for all 
        scales, the seventh one is special. 

        - If the 7th note is a (wholetone / full-step / major 2nd) below the 
        tonic, it is called a subtonic.
        - If the 7th note is a (semitone / half-step / minor 2nd) below the 
        tonic, it is called a leading tone.

    Attributes:
        tonic (Note):
            The 1st scale degree (root)
        supertonic (Note):
            The 2nd scale degree
        mediant (Note):
            The 3rd scale degree 
        subdominant (Note):
            The 4th scale degree 
        dominant (Note):
            The 5th scale degree 
        submediant (Note):
            The 6th scale degree       
        leading_tone (Note):
            The 7th scale degree (see above)
        subtonic (Note):
            The 7th scale degree (see above)

    Methods:        
        __init__(self, root, scale_type):
            Initialises the root and scale type.
        note_degrees(self):
            Returns a dictionary of all scale degrees.
        to_string_array(self):
            Returns the scale as a list of formatted strings.
        pretty_print(self):
            Prints the `to_string_array` directly to the console.
        __repr__(self):
            Returns a string with the class, root note and ScaleType.
    """
    def __init__(self, root: Note, scale_type: ScaleType=ScaleType.Major) -> None:
        """ 
        Builds the scale from a root note and a scale type. 

        Example:
            >>> ds = DiatonicScale(Note.E, ScaleType.Dorian)

        Raises:
             AttributeError: 
                If the scale does not contain 7 notes.

        Args:
            root (Note):
                The note to build the scale from.
            scale_type (ScaleType):
                The type of scale that contains 7 notes (i.e. not pentantonic
                or blues)      
        """
        super(DiatonicScale, self).__init__(root, scale_type)
        
        if self.num_notes != 7:
            raise ValueError(f"Diatonic scales must contain 7 notes, not {self.num_notes}")
        
    def note_degrees(self) -> dict[str, Note]:
        """ 
        Returns a dictionary mapping each scale degree name to its corresponding
        Note.

        The seventh degree may be either a 'leading_tone' or a 'subtonic' 
        depending on the scale type.

        Returns:
            dict[str, Note]:
                A dictionary containing all seven scale degrees.
        """
        d = {
            "tonic": self.notes[0],
            "supertonic": self.notes[1],
            "mediant": self.notes[2],
            "subdominant": self.notes[3],
            "dominant": self.notes[4],
            "submediant": self.notes[5],
        }

        try:
            d["leading_tone"] = self.leading_tone
        except AttributeError:
            d["subtonic"] = self.subtonic

        return d
            
    @property
    def tonic(self) -> Note:
        """ 
        Returns the tonic (root / 1st) of the scale. 

        Returns:
            Note:
        """
        return self.notes[0]

    @property
    def supertonic(self) -> Note:
        """ 
        Returns the supertonic (2nd) of the scale. 

        Returns:
            Note:
        """
        return self.notes[1]

    @property
    def mediant(self) -> Note:
        """ 
        Returns the mediant (3rd) of the scale. 

        Returns:
            Note:
        """
        return self.notes[2]

    @property
    def subdominant(self) -> Note:
        """ 
        Returns the subdominant (4th) of the scale. 

        Returns:
            Note:
        """
        return self.notes[3]

    @property
    def dominant(self) -> Note:
        """ 
        Returns the dominant (5th) of the scale. 

        Returns:
            Note:
        """
        return self.notes[4]

    @property
    def submediant(self) -> Note:
        """
        Returns the submediant (6th) of the scale. 

        Returns:
            Note:
        """
        return self.notes[5]

    @property
    def leading_tone(self) -> Note:
        """ 
        Returns the leading tone of the scale, if it exists, raises AttributeError
        otherwise.

        If the 7th note is a (semitone / half-step / minor 2nd) below the tonic, it
        is called a leading tone.

        Example:
            >>> DiatonicScale(Note.C, ScaleType.Major).leading_tone
            B

        Raises:
            AttributeError: 
                If the scale does not have a leading tone.

        Returns:
            Note:
        """
        distance = interval_distance(self.notes[6], self.notes[0])

        if distance == Interval.m2:
            return self.notes[6]            
            
        raise AttributeError(f"{self.type} scales don't have a leading tone.")        

    @property
    def subtonic(self) -> Note:
        """ 
        Returns the subtonic of the scale, if it exists, raises AttributeError 
        otherwise.

        If the 7th note is a (wholetone / full-step / major 2nd) below the tonic, 
        it is called a subtonic.

        Example:
            >>> DiatonicScale(Note.A, ScaleType.Minor).subtonic
            G

        Raises:
            AttributeError: 
                If the scale does not have a subtonic.

        Returns:
            Note:
        """
        distance = interval_distance(self.notes[6], self.notes[0])
                
        if distance == Interval.M2:
            return self.notes[6]

        raise AttributeError(f"{self.type} scales don't have a subtonic.")
        
    def to_string_array(self) -> list[str]:
        """
        Returns the scale as a list of formatted strings, suitable for printing
        or exporting to text-based outputs (e.g., files, logs, or GUIs).

        Example:
            >>> ds = DiatonicScale(Note.A, ScaleType.Minor)
            >>> for line in ds.to_string_array():
            ...     print(line)
            Scale Degrees of A Minor:
                tonic       : A
                supertonic  : B
                mediant     : C
                subdominant : D
                dominant    : E
                submediant  : F
                subtonic    : G

        Returns:
            list[str]:
                A list of strings representing each scale degree in a readable format.
        """
        nd = self.note_degrees()
        max_key_len = max(len(k) for k in nd.keys())

        l = [f"Scale Degrees of {self.name}:"]

        for k, v in nd.items():
            l.append(f"\t{k.ljust(max_key_len + 1)}: {v}")

        return l      

    def pretty_print(self) -> None:
        """
        Prints the formatted scale (from `to_string_array`) directly to the console.

        Example:
            >>> ds = DiatonicScale(Note.C, ScaleType.Major)
            >>> ds.pretty_print()
            Scale Degrees of C Major:
                tonic        : C
                supertonic   : D
                mediant      : E
                subdominant  : F
                dominant     : G
                submediant   : A
                leading_tone : B
        """
        for _ in self.to_string_array():
            print(_)
  
    def __repr__(self) -> str:
        """ 
        Returns a string representation of the class, root note and scale type. 

        Example:
            >>> ds = DiatonicScale(Note.E, ScaleType.Dorian)
            >>> repr(ds)
            DiatonicScale(Note.E, ScaleType.Dorian)

        Returns:
            str:
        """
        return f"DiatonicScale(Note.{self.notes[0]}, ScaleType.{self.type})"