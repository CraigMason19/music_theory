#-------------------------------------------------------------------------------
# Name:        test_notes.py
#
# Notes:       A test suite for the Note script.
#
# Links:       
#
# TODO:
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.notes import (Note, Interval, transpose, interval_distance, notes_to_string,
                   intervals_to_string, chromatic_notes)

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

    #region Interval

    def test_interval_from_index_00(self):
        self.assertEqual(Interval.from_index(0), Interval.Unison)

    def test_interval_from_index_01(self):
        self.assertEqual(Interval.from_index(13), Interval.m2)

    def test_interval_from_index_02(self):
        self.assertEqual(Interval.from_index(-4), Interval.m6)

    def test_interval_to_numeric_00(self):
        self.assertEqual(Interval.P4.to_numeric(), "4")

    def test_interval_to_numeric_01(self):
        self.assertEqual(Interval.Unison.to_numeric(), "1")

    def test_interval_from_numeric_00(self):
        self.assertEqual(Interval.from_numeric('b3'), Interval.m3)

    def test_interval_from_numeric_01(self):
        self.assertEqual(Interval.from_numeric('5'), Interval.P5)

    def test_interval_from_numeric_02(self):
        self.assertEqual(Interval.from_numeric('b5'), Interval.dim5)

    #endregion

    #region Note

    def test_items(self):
        expected = [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab, Note.A, Note.Bb, Note.B]
        self.assertEqual(Note.items(), expected)

    def test_all_notes_alias(self):
        expected = [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab, Note.A, Note.Bb, Note.B]
        self.assertEqual(Note.all_notes(), expected)

    def test_items_same_as_all_notes_alias(self):
        self.assertListEqual(Note.items(), Note.all_notes())

    def test_note_C_equality(self):
        self.assertEqual(Note.C, Note.C)

    def test_note_Bb_equality(self):
        self.assertEqual(Note.Bb, Note.Bb)

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

    def test_to_sharp_00(self):
        sharp = Note.to_sharp(Note.Db)
        self.assertEqual(sharp, "C#")

    def test_to_sharp_01(self):
        sharp = Note.to_sharp(Note.F)
        self.assertEqual(sharp, "F")

    def test_to_sharp_02(self):
        sharp = Note.to_sharp(Note.Gb)
        self.assertEqual(sharp, "F#")

    def test_previous_01(self):
        self.assertEqual(Note.C.previous(), Note.B)

    def test_previous_02(self):
        self.assertEqual(Note.Gb.previous(), Note.F)

    def test_next_01(self):
        self.assertEqual(Note.A.next(), Note.Bb)

    def test_next_02(self):
        self.assertEqual(Note.B.previous(), Note.Bb)

    #endregion

    #region ListsToStrings
    def test_notes_to_string_00(self):
        notes = notes_to_string(Note.items())
        expected = "C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B"

        self.assertEqual(notes, expected)
    
    def test_notes_to_string_01(self):
        notes = notes_to_string([Note.A, Note.Db, Note.F])
        expected = "A, Db, F"

        self.assertEqual(notes, expected)

    def test_intervals_to_string_00(self):
        intervals = intervals_to_string(Interval.items())
        expected = "Unison, m2, M2, m3, M3, P4, dim5, P5, m6, M6, m7, M7"

        self.assertEqual(intervals, expected)

    def test_intervals_to_string_01(self):
        intervals = intervals_to_string([Interval.Unison, Interval.dim5, Interval.M7])
        expected = "Unison, dim5, M7"

        self.assertEqual(intervals, expected)
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

    #region chromatic_notes

    def test_chromatic_notes_up_00(self):
        note, expected = Note.A, [Note.A, Note.Bb, Note.B, Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab]
        self.assertEqual(chromatic_notes(note), expected)

    def test_chromatic_notes_down_01(self):
        note, expected = Note.A, [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]
        self.assertEqual(chromatic_notes(note, direction="down"), expected)

    def test_chromatic_notes_direction_error(self):
        note, expected = Note.A, [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]
        
        with self.assertRaises(ValueError):
            chromatic_notes(Note, "Uppy Up")

    #endregion

if __name__ == '__main__':
    unittest.main()