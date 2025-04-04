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
    def __init__(self, root, scale_type=ScaleType.Major):
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
        # Raise error for Minor scales as they do not have a leading tone
        if self.type == ScaleType.Minor:
            raise AttributeError("Minor scales don't have a leading tone")
        
        return self.notes[6]

    @property
    def subtonic(self):
        # For Minor scales, the 7th note is the subtonic
        if self.type == ScaleType.Minor:
            return self.notes[6]
        
        raise AttributeError("Only minor scales have a subtonic")