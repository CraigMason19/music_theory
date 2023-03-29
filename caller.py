#-------------------------------------------------------------------------------
# Name:        caller.py
#
# Notes:       A caller that shows the usage of the music classes.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from notes import Note, Interval
from scales import Scale, ScaleType
import chords
import scales
import notes as ns
import keys

#TODO change name
# map progression???
def foobar(progression, chord_dict, empty="X"):
    l = []
    for chord in progression:
        if chord in chord_dict:
            l.append(str(chord_dict[chord]))
        else:
            l.append(empty)

    return l



def chords(note, scale_type):
    ''' Shows how to call the chords in a scale type'''
    print(f"Chords in {note} {scale_type}")

    chords = keys.chords_in_key(note, scale_type) 
    
    for _ in chords.values():
        print(f'\t{str(_)}')
     

def chord_progressions():
    ''' Shows which chords match a numerical expresion in a key'''
    chords = keys.chords_in_key(Note.C, ScaleType.Major)

    progression = ['I', 'V', 'vi', 'IV', 'IIIIIII']
    print(progression)
    print(foobar(progression, chords))



def main():
    chords(Note.F, ScaleType.Major)
    chord_progressions()

if __name__ == '__main__':
    main()