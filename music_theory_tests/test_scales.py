#-------------------------------------------------------------------------------
# Name:        test_scales.py
#
# Notes:       A test for various scale shapes
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.notes import Note, Interval
import music_theory.scales as s

class TestScales(unittest.TestCase):
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
    # Tests - (Only tests a, c, and f)
    #---------------------------------------------------------------------------

    #region MajorScales
    def test_a_major_scale(self):
        scale = s.Scale(Note.A, s.ScaleType.Major)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.D, Note.E, Note.Gb, Note.Ab])

    def test_c_major_scale(self):
        scale = s.Scale(Note.C, s.ScaleType.Major)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B])

    def test_f_major_scale(self):
        scale = s.Scale(Note.F, s.ScaleType.Major)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.A, Note.Bb, Note.C, Note.D, Note.E])
    #endregion

    #region MinorScales
    def test_a_minor_scale(self):
        scale = s.Scale(Note.A, s.ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.C, Note.D, Note.E, Note.F, Note.G])

    def test_c_minor_scale(self):
        scale = s.Scale(Note.C, s.ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.Eb, Note.F, Note.G, Note.Ab, Note.Bb])

    def test_f_minor_scale(self):
        scale = s.Scale(Note.F, s.ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.Ab, Note.Bb, Note.C, Note.Db, Note.Eb])
    #endregion

    #region MajorPentatonicScales
    def test_a_major_pentatonic(self):
        scale = s.Scale(Note.A, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.E, Note.Gb])
    
    def test_c_major_pentatonic(self):
        scale = s.Scale(Note.C, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.G, Note.A])

    def test_f_major_pentatonic(self):
        scale = s.Scale(Note.F, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.A, Note.C, Note.D])
    #endregion

    #region MinorPentatonicScales
    def test_a_minor_pentatonic(self):
        scale = s.Scale(Note.A, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.C, Note.D, Note.E, Note.G])

    def test_c_minor_pentatonic(self):
        scale = s.Scale(Note.C, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.Eb, Note.F, Note.G, Note.Bb])

    def test_f_minor_pentatonic(self):
        scale = s.Scale(Note.F, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.F, Note.Ab, Note.Bb, Note.C, Note.Eb])
    #endregion

    #region NotesFromSteps
    def test_c_major_notes_from_steps(self):
        notes = s._notes_from_steps(Note.C, 'wwhwwwh')
        expected = [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B]
        self.assertEqual(notes, expected)

    def test_Bb_mixolydian_notes_from_steps(self):
        notes = s._notes_from_steps(Note.Bb, ['w', 'w', 'h', 'w', 'w', 'h', 'w'])
        expected = [Note.Bb, Note.C, Note.D, Note.Eb, Note.F, Note.G, Note.Ab]
        self.assertEqual(notes, expected)
    #endregion

    #region IntervalsFromSteps
    def test_major_intervals_from_steps(self):
        intervals = s._intervals_from_steps(['w', 'w', 'h', 'w', 'w', 'w', 'h'])
        expected = [Interval.Unison, Interval.M2, Interval.M3, Interval.P4, Interval.P5, Interval.M6, Interval.M7]
        self.assertEqual(intervals, expected)
    #endregion

    #region IntervalsFromNumerics
    def test_major_intervals_from_numerics(self):
        intervals = s._intervals_from_numerics(['1', '2', '3', '4', '5', '6', '7'])
        expected = [Interval.Unison, Interval.M2, Interval.M3, Interval.P4, Interval.P5, Interval.M6, Interval.M7]
        self.assertEqual(intervals, expected)

    def test_harmonic_minor_intervals_from_numerics(self):
        intervals = s._intervals_from_numerics(['1', '2', 'b3', '4', '5', 'b6', '7'])
        expected = [Interval.Unison, Interval.M2, Interval.m3, Interval.P4, Interval.P5, Interval.m6, Interval.M7]
        self.assertEqual(intervals, expected)
    #endregion

    #region NotesFromIntervals
    def test_C_major_notes_from_intervals(self):
        notes = s._notes_from_intervals(Note.C, [Interval.Unison, Interval.M2, Interval.M3, Interval.P4, Interval.P5, Interval.M6, Interval.M7])
        expected = [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B]
        self.assertEqual(notes, expected)
    #endregion


if __name__ == '__main__':
    unittest.main()