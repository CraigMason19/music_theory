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

from music_theory.notes import Note, Interval, transpose, interval_distance
from music_theory.scales import Scale, ScaleType, notes_to_string, modes_from_note
from music_theory.keys import Key, KeyType, chords_from_progression
from music_theory.chords import Chord, ChordType

def demo_notes():
    print("Notes Demo:\n")

    test_range = 3
    note, interval = Note.random(), Interval.random()

    # Notes
    print(f"Note {note}:")
    print(f"\tstr() -> {str(note)}")
    print(f"\trepr() -> {repr(note)}\n")

    # Intervals
    print(f"Interval {interval}:")
    print(f"\tstr() -> {str(interval)}")
    print(f"\trepr() -> {repr(interval)}\n")

    print(f"Interval distances")
    for i in range(test_range):
        note_a, note_b = Note.random(), Note.random()

        dif = interval_distance(note_a, note_b) 
        print(f"\t{note_a}, {note_b} -> {dif}")

        dif = interval_distance(note_a, note_b, direction='down')  
        print(f"\t{note_a}, {note_b} <- {dif}\n")

    # Transpose
    print(f"Transpose:")
    for i in range(test_range):
        note, interval = Note.random(), Interval.random()

        new_note = transpose(note, interval)  
        print(f"\t{note}, {interval} -> {new_note}")

        new_note = transpose(note, interval, direction='down')  
        print(f"\t{note}, {interval} <- {new_note}\n") 

def demo_scale():
    print("Scale Demo:\n")

    scale = Scale.random()

    print(f"{scale.name}:")
    print(f"\tstr() -> {str(scale)}")
    print(f"\trepr() -> {repr(scale)}")
    print(f"\tRoot -> {scale.root}")
    print(f"\tType -> {scale.type}")
    print(f"\tNotes -> {notes_to_string(scale.notes)}")
    print(f"\tNumber of flats -> {scale.number_of_flats}")
    print(f"\tCreation Formula -> {scale.creation_formula})")
    print(f"\tInterval Formula -> {scale.interval_formula})")
    print(f"\tNumeric Formula -> {scale.numeric_formula})\n")

    # Modes
    note = Note.random()
    print(f"Modes of {note}:")
    for mode in modes_from_note(note):
        print(f"\t{mode}")

def demo_chords():
    print("Chords Demo:\n")

    ct = ChordType.random()
    print(f"ChordType {ct}:")
    print(f"\tstr() -> {str(ct)}")
    print(f"\trep() -> {repr(ct)}")

    c = Chord.random()
    print(f"Chord {c}:")
    print(f"\tNotes {c.notes}:")
    print(f"\tstr() -> {str(c)}")
    print(f"\trep() -> {repr(c)}")
    print(f"\tnotation -> {c.notation}")

def demo_keys():
    print("Keys Demo:\n")

    key = Key.random()

    print(f"Key of {key.name}:")
    print(f"\tstr() -> {str(key)}")
    print(f"\trepr() -> {repr(key)}")
    print(f"\tRoot -> {key.root}")
    print(f"\tType -> {key.type}")
    print(f"\tParallel -> {key.parallel}")
    print(f"\tRelative -> {key.relative_key}")
    print(f"\tSharp Count -> {key.sharp_count}")
    print(f"\tSharps -> {key.sharps}")
    print(f"\tFlat Count -> {key.flat_count}")
    print(f"\tFlats -> {key.flats}")
    
    # print(f"\tChords:")
    # for numeral, chord in key.chords().items():
    #     print(f"\t\t{numeral}: {chord}")

    # print(f"\tDominant Chords:")
    # for numeral, chord in key.dominant_chords().items():
    #     print(f"\t\t{numeral}: {chord}")

    # print(f"\tParallel Chords:")
    # for numeral, chord in key.parallel_chords().items():
    #     print(f"\t\t{numeral}: {chord}")

    print('')
    key.pretty_print(dominant=True, parallel=True)

def main():
    demo_notes()
    demo_scale()
    demo_chords()
    demo_keys()

if __name__ == '__main__':
    main()