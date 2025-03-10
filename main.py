#-------------------------------------------------------------------------------
# Name:        main.py
#
# Notes:       A caller that shows the usage of the music classes. The idea is
#              to help me write music.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'music_theory')))

from music_theory.notes import Note, Interval
from music_theory.scales import Scale, ScaleType
from music_theory.keys import Key, KeyType, chords_from_progression

import music_theory.chords

def main():
    # Using my song SadHappy to understand how to use the music classes.
    #
    # I, ii, IV, parallel VII
    key = Key(Note.C, KeyType.Major) 
    progression = ['I', 'ii', 'IV', 'IIIIIII']

    cp = chords_from_progression(key, progression)

    key.pretty_print(True, True)

    print(f"\n{progression}")
    print(f"{cp}")



if __name__ == '__main__':
    main()