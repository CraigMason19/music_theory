#-------------------------------------------------------------------------------
# Name:        test_keys.py
#
# Notes:       A test for various chords in a certain key.
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.progressions import chords_from_progression
from music_theory.keys import Key, KeyType
from music_theory.notes import Note

class TestProgressions(unittest.TestCase):
    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------

    #region Chord Progressions

    def test_chord_progressions_C_major(self):
        prog = ['I', 'IV', 'V']
        
        result = chords_from_progression(Key(Note.C), prog)
        expected = ['CM', 'FM', 'GM']
        
        self.assertListEqual(result, expected)

    def test_chord_progressions_A_major_upper_lower_numerals(self):
        prog = ['i', 'I', 'iv', 'IV', 'vii', 'VII']
        
        result = chords_from_progression(Key(Note.A), prog)
        expected = ['Am', 'AM', 'Dm', 'DM', 'Ab°', 'GM']
        
        self.assertListEqual(result, expected)

    def test_chord_progressions_A_minor_upper_lower_numerals(self):
        prog = ['i', 'I', 'iv', 'IV', 'vii', 'VII']
        
        result = chords_from_progression(Key(Note.A, KeyType.Minor), prog)
        expected = ['Am', 'AM', 'Dm', 'DM', 'Ab°', 'GM']
        
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

    #endregion

if __name__ == '__main__': # pragma: no cover
    unittest.main()