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
    """ An extended scale class that represents a diatonic scale (7 notes) with properties for the scale degrees.

        While the scale degrees for the first six notes are the same for both major and minor scales, the seventh one is special.

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
            The 7th scale degree (NOT for natural Minor scales)
        subtonic (Note):
            The 7th scale degree (ONLY for natural Minor scales, whole step below the tonic)
        __repr__(self):
            Returns a string with the class, root note and ScaleType.

    Methods:        
        __init__(self, root, scale_type):
            Initialises the root and scale type
    """
    def __init__(self, root: Note, scale_type: ScaleType=ScaleType.Major) -> None:
        """ 
        Builds the scale from a root note and a scale type. 

        Example:
            >>> ds = DiatonicScale(Note.E, ScaleType.Dorian)
            
        Raises:
             AttributeError: 
                If the scale does not have a subtonic.

        Args:
            root (Note):
                The note to build the scale from.
            scale_type (ScaleType):
                The type of scale that contains 7 notes (i.e. not pentantonic or blues)      
        """
        super(DiatonicScale, self).__init__(root, scale_type)
        
        if self.num_notes != 7:
            raise ValueError(f"Diatonic scales must contain 7 notes, not {self.num_notes}")
        
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
        Returns the leading tone of the scale, if it exists, raises AttributeError otherwise.

        If the 7th note is a (semitone / half-step / minor 2nd) below the tonic, it is called a leading tone.

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
        Returns the subtonic of the scale, if it exists, raises AttributeError otherwise.

        If the 7th note is a (wholetone / full-step / major 2nd) below the tonic, it is called a subtonic.

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
                
        if distance != Interval.M2:
            raise AttributeError(f"{self.type} scales don't have a subtonic.")
        
        return self.notes[6]
  
    def __repr__(self) -> str:
        """ 
        Returns a string represention of the class, root note and scale type. 

        Example:
            >>> ds = DiatonicScale(Note.E, ScaleType.Dorian)
            >>> repr(ds)
            DiatonicScale(Note.E, ScaleType.Dorian)

        Returns:
            str:
        """
        return f"DiatonicScale(Note.{self.notes[0]}, ScaleType.{self.type})"