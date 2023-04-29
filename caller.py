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

from keys import Key, KeyType, chords_from_progression

def main():
    # Using my song SadHappy to understand how to use the music classes.
    #
    # I, ii, IV, parallel VII
    key = Key(Note.A, KeyType.Major) 
    progression = ['I', 'ii', 'IV', 'IIIIIII']

    cp = chords_from_progression(key, progression)

    key.pretty_print(True, True)

    print(f"\n{progression}")
    print(f"{cp}")



if __name__ == '__main__':
    main()