#-------------------------------------------------------------------------------
# Name:        progressions.py
#
# Notes:       A collection of objects and methods for working with chord 
#              progressions and cadences.
#
# TODO:
#-------------------------------------------------------------------------------

from music_theory.keys import Key

#region Progressions

class Progression:
    """Represents a chord progression.
    """
    def __init__(self, key, numeral_progression):
        self.key = key
        self.numerals = numeral_progression
        self.chords = chords_from_progression(key, self.numerals)

    def __str__(self):
        return f'{self.key} - {self.numerals}'

    def __repr__(self):
        return f'Progression({self.key}, {self.numerals})'

class NumeralProgressions:
    """Represents common musical chord progressions.

    Attributes:
        axis (list of str): Very common in western music. (Axis of Awesome 4 Chord Song).
        royal_road (list of str): Very common in Japanese music.
        twelve_bar_blues (list of str): A very common blues progression.
        andalusian (list of str): Often referred to as a cadence, though technically a progression.
    """
    axis = ["I", "V", "vi", "IV"]
    axis_alt = ["vi", "IV", "I", "V"]
    royal_road = ["IV", "V", "iii", "vi"]
    twelve_bar_blues = ["I", "IV", "V"]
    andalusian = ["i", "VII", "VI", "V"]
    andalusian_alt = ["i", "VII", "VI", "VII"]
    doo_wop = ["I", "vi", "IV", "V"]
    doo_wop_changes = ["I", "vi", "ii", "V"]

class SongProgressions:
    """Represents famous songs and their chord progressions.

    Attributes:
        kiss_from_a_rose (list of str): dreamy, modal feel.
    """
    seal_kiss_from_a_rose = ["VI", "VII", "I"],
    beatles_hey_jude = ["I", "vii", "IV", "I"]
    
#endregion
 
#region Cadences

class NumeralCadences:
    """Represents common musical cadences.

    A cadence is a chord progression of at least two chords that concludes a musical phrase or section.

    Notes:
        - The Major/Minor Plagal Cadences differ from a standard Plagal Cadence in their respective keys.

    Attributes:
        plagal (list of str): Also known as the Amen Cadence.
        minor_plagal (list of str): A variation of the Plagal Cadence in a minor key.
        authentic (list of str): Also called a Perfect Cadence.

        deceptive (list of str): Also known as interupted. It decieves or interupts the resolution.
        imperfect (list of str): Also called half-cadance. Doesn't resolve and hangs. Used mainly at the end of songs.

        super_mario (list of str): The end of level fanfare.
    """
    # Finished
    plagal = ["IV", "I"]
    minor_plagal = ["iv", "I"]
    authentic = ["V", "I"]

    # Unfinished
    deceptive = ["V", "VI"]
    imperfect = ["V"]

    # More casual uses / terminology. These are like mini chord progressions
    super_mario = ["VI", "VII", "i"]

#endregion

#region Functions

def chords_from_progression(key, progression, error='X'):
    """ Returns a list of chords that match a progression in a key. Can be in 
        either the chords or parallel chords.
            
        error string is used if a chord can't be found in the progression.

        Diminished chords can be passed as '°' or 'dim' ('ii°' or 'viidim')

        e.g. key=C Major, progression=['I', 'i', 'IV', 'V']
            -> [CM, Cm, FM, GM]
            
    Args:
        key:
            The key the chords are from.
        progression:
            A list of roman numerals notating the chords.
        error:
            A placeholder for missing or invalid chords in the key.

    Returns:
        A List of chords.
    """
    progression = [numeral.replace('dim', '°') if isinstance(numeral, str) else numeral for numeral in progression]

    chord_dict = key.chords() | key.parallel_chords()

    return [chord_dict[numeral] if (numeral in chord_dict) else error for numeral in progression]

#endregion