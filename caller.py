#-------------------------------------------------------------------------------
# Name:        caller.py
#
# Notes:       A caller that shows the usage of the music classes. The idea is
#              to help me write music.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from notes import Note, Interval
from scales import Scale, ScaleType

import chords

from keys import Key, KeyType, find_chords_from_progression

def chord_progressions(key, progression):
    """ An example of how to find chord progressions in a key. """
    chords = find_chords_from_progression(key, progression)

    # Printouts
    key.pretty_print(True, True)

    print("Progresion:")
    print(f"\t{progression}")
    print(f"\t{chords}")

def main():
    # Using my song SadHappy to understand how to use the music classes.
    #
    # I, ii, IV, parallel VII
    key = Key(Note.A, KeyType.Major) 
    chord_progressions(key, ['I', 'ii', 'IV', 'IIIIIII'])

    scales = []
    scales.append(Scale(Note.A, ScaleType.Major))
    scales.append(Scale(Note.B, ScaleType.Minor))

    for scale in scales:
        print(f"\t{scale}")
        # print(f"\t{scale.interval_formula}")

if __name__ == '__main__':
    main()