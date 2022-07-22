#-------------------------------------------------------------------------------
# Name:        chords.py
#
# Notes:       A collection of chord shapes.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------



from enum import Enum

# class ScaleType(Enum):
#     (Major, Minor, 
#     MajorPentatonic, MinorPentatonic, 
#     Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian) = range(11) 

# MajorChords = ['i']

class MajorChord(Enum):
    (I, II, III, IV, V, VI, VII) = range(7)

class MinorChord(Enum):
    (i, ii, iii, iv, v, vi, vii) = range(7)