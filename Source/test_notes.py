#-------------------------------------------------------------------------------
# Name:        test_notes.py
#
# Notes:       A test suite for the Note class
#
# Links:       
#
# TODO:
#-------------------------------------------------------------------------------

import unittest
from notes import Note, Interval, notes_to_string, transpose

class TestNotes(unittest.TestCase):
    #---------------------------------------------------------------------------
    # setUpClass and tearDownClass run before and after all tests, called once
    # NOTE - the camelCase syntax. Important that they are named this way.
    #---------------------------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #---------------------------------------------------------------------------
    # setUp and tearDown run before every single test.
    #---------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------

    def test_notes_to_string_000(self):
        notes = notes_to_string(Note.items())
        expected = "C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B"

        self.assertEqual(notes, expected)
    
    def test_notes_to_string_001(self):
        notes = notes_to_string([Note.A, Note.Db, Note.F])
        expected = "A, Db, F"

        self.assertEqual(notes, expected)

    #region Note Equality
    def test_note_C_equality(self):
        self.assertEqual(Note.C, Note.C)

    def test_note_Bb_equality(self):
        self.assertEqual(Note.Bb, Note.Bb)
    #endregion

    #region Note Index
    def test_note_index_octave_C_up(self):
        self.assertEqual(Note.from_index(0), Note.C)
        self.assertEqual(Note.from_index(12), Note.C)
        self.assertEqual(Note.from_index(24), Note.C)

    def test_note_index_octave_F_down(self):
        index = Note.F.value
        self.assertEqual(Note.from_index(index), Note.F)
        self.assertEqual(Note.from_index(index - 12), Note.F)
        self.assertEqual(Note.from_index(index - 24), Note.F)

    def test_note_index_wrap_around_up(self):
        self.assertEqual(Note.from_index(15), Note.Eb)

    def test_note_index_wrap_around_B_down(self):
        index = Note.B.value
        self.assertEqual(Note.from_index(index - 27), Note.Ab)
    #endregion

    #region Transpose
    def test_transpose_up_00(self):    
        note, expected = transpose(Note.A, Interval.P4, direction='u'), Note.D
        self.assertEqual(note, expected)

    def test_transpose_down_00(self):    
        note, expected = transpose(Note.A, Interval.P4, direction='down'), Note.E
        self.assertEqual(note, expected)

    def test_transpose_C_up_00(self):    
        note, expected = transpose(Note.C, Interval.P4, direction='UP'), Note.F
        self.assertEqual(note, expected)

    def test_transpose_C_down_00(self):    
        note, expected = transpose(Note.C, Interval.P4, direction='Down'), Note.G
        self.assertEqual(note, expected)

    def test_transpose_C_down_01(self):    
        note, expected = transpose(Note.C, Interval.m2, direction='Down'), Note.B
        self.assertEqual(note, expected)

    def test_transpose_value_error(self):
        self.assertRaises(ValueError, transpose, Note.C, Interval.P4, direction='sideways')
    #endregion

if __name__ == '__main__':
    unittest.main()