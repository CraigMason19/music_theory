#-------------------------------------------------------------------------------
# Name:        caller.py
#
# Notes:       A caller that shows the usage of the music classes.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

from notes import Note
from scales import Scale, ScaleType
import chords



def foobar(progression, chord_dict):
    l = []
    for chord in progression:
        if chord in chord_dict:
            l.append(str(chord_dict[chord]))
        else:
            l.append("X")

    return l




def main():
    # s = Scale(Note.C, ScaleType.Dorian)

    # print(s)
    # print(str(s))
    # print(repr(s))

    key = Note.C
    cM = Scale(Note.C, ScaleType.Major)
    paralell = Scale(Note.C, ScaleType.Minor)

    print(cM)
    print(paralell)

    x = chords.chords_in_key(Note.C, True)
    paralell_chords = chords.chords_in_key(Note.C, False) 

    table_data = [
        list(x.keys()), 
        [str(chord) for chord in x.values()],
        ["", "", "", "", "", "", "",],
        [str(chord) for chord in paralell_chords.values()],
        list(paralell_chords.keys()),
    ]

#     table_data = [

#     ['a', 'b', 'c'],
#     ['aaaaaaaaaa', 'b', 'c'], 
#     ['a', 'bbbbbbbbbb', 'c']
# ]
 
    for row in table_data:
        print("{: >5} {: >5} {: >5} {: >5} {: >5} {: >5} {: >5}".format(*row))


    # progression = ['I', 'V', 'vi', 'IV', 'IIIIIII']
    # print(foobar(progression, x))





if __name__ == '__main__':
    main()