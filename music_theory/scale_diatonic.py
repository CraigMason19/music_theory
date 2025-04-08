#-------------------------------------------------------------------------------
# Name:        scale_diatonic.py
#
# Notes:       A class representing a diatonic scale (7 notes)
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from music_theory.scales import Scale
from music_theory.scale_type import ScaleType


class DiatonicScale(Scale):
    """ An extended scale class that represents a diatonic scale (7 notes).

    Attributes:
        tonic:
            A property that returns the tonic (root). 

    Methods:        
        __init__(self, root, scale_type):
            Initialises the root and scale type.
    """
    def __init__(self, root, scale_type=ScaleType.Major):
        """ Builds the scale from a root note and a scale type. 

        Args:
            root:
                The note to build the scale from.
            scale_type:
                The type of scale that contains 7 notes (i.e. not pentantonic or blues)      
        """
        super(DiatonicScale, self).__init__(root, scale_type)
        
        if self.num_notes != 7:
            raise ValueError(f"Diatonic scales must contain 7 notes, not {self.num_notes}")
        
    @property
    def tonic(self):
        """ Returns the tonic (root) of the scale. 

        Returns:
            A Note.
        """
        return self.notes[0]

    @property
    def supertonic(self):
        return self.notes[1]

    @property
    def mediant(self):
        return self.notes[2]

    @property
    def subdominant(self):
        """ Returns the subdominant (4th) of the scale. 

        Returns:
            A Note.
        """
        return self.notes[3]

    @property
    def dominant(self):
        """ Returns the dominant (5th) of the scale. 

        Returns:
            A Note.
        """
        return self.notes[4]

    @property
    def submediant(self):
        return self.notes[5]

    @property
    def leading_tone(self):
        """ Returns the leading tone of the scale.

            In diatonic scales, the 7th degree is called the leading tone, except in 
            minor scales, where it is referred to as the subtonic instead.

        Returns:
            A Note.

        Raises:
            AttributeError: 
                If the scale is minor, which does not have a leading tone.
        """
        if self.type == ScaleType.Minor:
            raise AttributeError("Minor scales don't have a leading tone")
        
        return self.notes[6]

    @property
    def subtonic(self):
        """ Returns the subtonic of the scale.

            The subtonic is the 7th note in a Minor diatonic scale, where it is 
            a whole tone below the tonic. Major scales do not have a subtonic; they 
            use a leading tone instead.

        Returns:
            A Note.

        Raises:
            AttributeError: 
                If the scale is not Minor.
        """
        if self.type == ScaleType.Minor:
            return self.notes[6]
        
        raise AttributeError("Only Minor scales have a subtonic")