import unittest

import _setup

from music_theory.progressions import chords_from_progression
from music_theory.keys import Key, KeyType
from music_theory.notes import Note
from music_theory.chords import Chord, ChordType

class TestChordsFromProgression(unittest.TestCase):
    def test_chord_progressions_C_major(self):
        prog = ['I', 'IV', 'V']
        
        result = chords_from_progression(Key(Note.C), prog)
        expected = [Chord(Note.C, ChordType.Major), Chord(Note.F, ChordType.Major), Chord(Note.G, ChordType.Major)]
        
        self.assertListEqual(result, expected)

    def test_chord_progressions_A_major_upper_lower_numerals_4th(self):
        prog = ['iv', 'IV']
        
        result = chords_from_progression(Key(Note.A), prog)
        expected = [Chord(Note.D, ChordType.Minor), Chord(Note.D, ChordType.Major)]

        self.assertListEqual(result, expected)

    def test_chord_progressions_A_minor_upper_lower_numerals_4th(self):
        prog = ['iv', 'IV']
        
        result = chords_from_progression(Key(Note.A, KeyType.Minor), prog)
        expected = [Chord(Note.D, ChordType.Minor), Chord(Note.D, ChordType.Major)]
        
        self.assertListEqual(result, expected)

    def test_invalid_chord_progression_produces_default_error(self):
        prog = ['guitar', 'Qm', 'X', None, 1]
        error = 'X'

        result = chords_from_progression(Key(Note.A), prog)
        expected = [error] * len(prog)

        self.assertListEqual(result, expected)

    def test_invalid_chord_progression_produces_custom_error(self):
        prog = ['guitar', 'Qm', 'X', None, 1]
        error = 'null'

        result = chords_from_progression(Key(Note.A), prog, error)
        expected = [error] * len(prog)

        self.assertListEqual(result, expected)

class TestChordsFromProgressionDiminished(unittest.TestCase):
    def test_C_Major_chords_diminished_7th(self):
        prog = ['I', 'vii°']

        result = chords_from_progression(Key(Note.C), prog)
        expected = [Chord(Note.C, ChordType.Major), Chord(Note.B, ChordType.Diminished)]

        self.assertListEqual(result, expected)

    def test_C_Major_parallel_chords_diminished_2nd(self):
        prog = ['I', 'ii°']

        result = chords_from_progression(Key(Note.C), prog)
        expected = [Chord(Note.C, ChordType.Major), Chord(Note.D, ChordType.Diminished)]

        self.assertListEqual(result, expected)

    def test_C_Major_multiple_diminished_declarations(self):
        prog = ['ii°', 'iidim']

        result = chords_from_progression(Key(Note.C), prog)
        expected = [Chord(Note.D, ChordType.Diminished), Chord(Note.D, ChordType.Diminished)]

        self.assertListEqual(result, expected)

    def test_C_Major_multiple_vii_diminished_declarations(self):
        prog = ['vii', 'vii°', 'viidim']

        result = chords_from_progression(Key(Note.C), prog)
        expected = [Chord(Note.B, ChordType.Diminished), Chord(Note.B, ChordType.Diminished), Chord(Note.B, ChordType.Diminished)]

        self.assertListEqual(result, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()