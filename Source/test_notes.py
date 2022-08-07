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
from notes import Note, Interval, notes_to_string, transpose, interval_distance

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

    #region Interval Numeric
    def test_interval_from_numeric_000(self):
        self.assertEqual(Interval.from_numeric('b3'), Interval.m3)
    #endregion

    #region Interval Distance
    def test_interval_distance_same(self):    
        inteval, expected = interval_distance(Note.Bb, Note.Bb), Interval.Unison
        self.assertEqual(inteval, expected)

    def test_interval_distance_up_00(self):    
        inteval, expected = interval_distance(Note.B, Note.Gb, direction="UP"), Interval.P5 
        self.assertEqual(inteval, expected)

    def test_interval_distance_up_01(self):    
        inteval, expected = interval_distance(Note.A, Note.C, direction="UP"), Interval.m3 
        self.assertEqual(inteval, expected)

    def test_interval_distance_down_00(self):    
        inteval, expected = interval_distance(Note.C, Note.G, direction="below"), Interval.P4 
        self.assertEqual(inteval, expected)

    def test_interval_distance_down_01(self):    
        inteval, expected = interval_distance(Note.A, Note.C, direction="below"), Interval.M6 
        self.assertEqual(inteval, expected)

    def test_interval_distance_value_error(self):
        self.assertRaises(ValueError, interval_distance, Note.C, Note.G, direction='sideways')
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