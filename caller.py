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

def foobar(progression, chord_dict):
    l = []
    for chord in progression:
        if chord in chord_dict:
            l.append(str(chord_dict[chord]))
        else:
            l.append("X")

    return l




def chord_progressions():
    # s = Scale(Note.C, ScaleType.Dorian)

    # print(s)
    # print(str(s))
    # print(repr(s))

    key = Note.G
    scale = Scale(key, ScaleType.Major)
    paralell = Scale(key, ScaleType.Minor)

    print(scale)
    print(paralell)

    x = chords.chords_in_key(key, True)
    paralell_chords = chords.chords_in_key(key, False) 

# dominant is 5th up from root G->D
# sec dom is everything else
# [dominant] + [secondary_sominants]

    dom_notes = [ns.transpose(n, Interval.P5) for n in scale.notes]
    dom_chords = [chords.Chord(n, chords.ChordType.Seven) for n in dom_notes]

    table_data = [
        [str(chord) for chord in x.values()],
        list(x.keys()), 
        ["", "", "", "", "", "", "",],
        [str(chord) for chord in dom_chords],

        [f"V7/{dunno}" for dunno in list(x.keys())],


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
        # print("{: >5} {: >5} {: >5} {: >5} {: >5} {: >5} {: >5}".format(*row))

        print(("{: >10}" * 7).format(*row))



    # progression = ['I', 'V', 'vi', 'IV', 'IIIIIII']
    # print(foobar(progression, x))



def main():
    # x = ['1', 'b3', '4', 'b5', '5', 'b7']
    
    # Gb, Ab, A, B, Db, D, E
    # print(scales.formula_from_steps(sf))

    print(Interval.P4.to_numeric())

    # c = scales.formula_from_numerics(x)
    # print(c)

    # s = Scale(Note.C, ScaleType.HarmonicMinor)
    # print(s)
    # s = Scale(Note.C, ScaleType.MelodicMinor)
    # print(s)

if __name__ == '__main__':
    chord_progressions()
    main()