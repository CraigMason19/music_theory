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

from music_theory.notes import Note
from music_theory.intervals import Interval
from music_theory.scales import ScaleType, Scale, _intervals_from_numerics, _intervals_from_steps, _notes_from_intervals, _notes_from_steps

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

    #region ScaleType

    def test_scale_type_items(self):
        expected = [ScaleType.Major, ScaleType.Minor, ScaleType.MajorPentatonic, ScaleType.MinorPentatonic, ScaleType.Ionian,
            ScaleType.Dorian, ScaleType.Phrygian, ScaleType.Lydian, ScaleType.Mixolydian, ScaleType.Aeolian, ScaleType.Locrian,
            ScaleType.Blues, ScaleType.HarmonicMinor, ScaleType.MelodicMinor]
        self.assertEqual(ScaleType.items(), expected)

    def test_scale_type_all_alias(self):
        expected = [ScaleType.Major, ScaleType.Minor, ScaleType.MajorPentatonic, ScaleType.MinorPentatonic, ScaleType.Ionian,
            ScaleType.Dorian, ScaleType.Phrygian, ScaleType.Lydian, ScaleType.Mixolydian, ScaleType.Aeolian, ScaleType.Locrian,
            ScaleType.Blues, ScaleType.HarmonicMinor, ScaleType.MelodicMinor]
        self.assertEqual(ScaleType.all(), expected)

    def test_scale_type_items_same_as_all_alias(self):
        self.assertListEqual(ScaleType.items(), ScaleType.all())

    def test_random_scale_type_validity(self):
        type = ScaleType.random()
        self.assertIn(type, list(ScaleType))

    def test_scale_type_str(self):
        type = ScaleType.HarmonicMinor
        self.assertEqual(str(type), "HarmonicMinor")

    def test_scale_type_repr(self):
        type = ScaleType.HarmonicMinor
        self.assertEqual(repr(type), "ScaleType.HarmonicMinor")

    #endregion

    #region MajorScales
    def test_a_major_scale(self):
        scale = Scale(Note.A, ScaleType.Major)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.D, Note.E, Note.Gb, Note.Ab])

    def test_c_major_scale(self):
        scale = Scale(Note.C, ScaleType.Major)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B])

    def test_f_major_scale(self):
        scale = Scale(Note.F, ScaleType.Major)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.A, Note.Bb, Note.C, Note.D, Note.E])
    #endregion

    #region MinorScales
    def test_a_minor_scale(self):
        scale = Scale(Note.A, ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.C, Note.D, Note.E, Note.F, Note.G])

    def test_c_minor_scale(self):
        scale = Scale(Note.C, ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.Eb, Note.F, Note.G, Note.Ab, Note.Bb])

    def test_f_minor_scale(self):
        scale = Scale(Note.F, ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.Ab, Note.Bb, Note.C, Note.Db, Note.Eb])
    #endregion

    #region MajorPentatonicScales
    def test_a_major_pentatonic(self):
        scale = Scale(Note.A, ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.E, Note.Gb])
    
    def test_c_major_pentatonic(self):
        scale = Scale(Note.C, ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.G, Note.A])

    def test_f_major_pentatonic(self):
        scale = Scale(Note.F, ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.A, Note.C, Note.D])
    #endregion

    #region MinorPentatonicScales
    def test_a_minor_pentatonic(self):
        scale = Scale(Note.A, ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.C, Note.D, Note.E, Note.G])

    def test_c_minor_pentatonic(self):
        scale = Scale(Note.C, ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.Eb, Note.F, Note.G, Note.Bb])

    def test_f_minor_pentatonic(self):
        scale = Scale(Note.F, ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.F, Note.Ab, Note.Bb, Note.C, Note.Eb])
    #endregion

    #region NotesFromSteps
    def test_c_major_notes_from_steps(self):
        notes = _notes_from_steps(Note.C, 'wwhwwwh')
        expected = [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B]
        self.assertEqual(notes, expected)

    def test_Bb_mixolydian_notes_from_steps(self):
        notes = _notes_from_steps(Note.Bb, ['w', 'w', 'h', 'w', 'w', 'h', 'w'])
        expected = [Note.Bb, Note.C, Note.D, Note.Eb, Note.F, Note.G, Note.Ab]
        self.assertEqual(notes, expected)
    #endregion

    #region IntervalsFromSteps
    def test_major_intervals_from_steps(self):
        intervals = _intervals_from_steps(['w', 'w', 'h', 'w', 'w', 'w', 'h'])
        expected = [Interval.Unison, Interval.M2, Interval.M3, Interval.P4, Interval.P5, Interval.M6, Interval.M7]
        self.assertEqual(intervals, expected)
    #endregion

    #region IntervalsFromNumerics
    def test_major_intervals_from_numerics(self):
        intervals = _intervals_from_numerics(['1', '2', '3', '4', '5', '6', '7'])
        expected = [Interval.Unison, Interval.M2, Interval.M3, Interval.P4, Interval.P5, Interval.M6, Interval.M7]
        self.assertEqual(intervals, expected)

    def test_harmonic_minor_intervals_from_numerics(self):
        intervals = _intervals_from_numerics(['1', '2', 'b3', '4', '5', 'b6', '7'])
        expected = [Interval.Unison, Interval.M2, Interval.m3, Interval.P4, Interval.P5, Interval.m6, Interval.M7]
        self.assertEqual(intervals, expected)
    #endregion

    #region NotesFromIntervals
    def test_C_major_notes_from_intervals(self):
        notes = _notes_from_intervals(Note.C, [Interval.Unison, Interval.M2, Interval.M3, Interval.P4, Interval.P5, Interval.M6, Interval.M7])
        expected = [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B]
        self.assertEqual(notes, expected)
    #endregion


if __name__ == '__main__': # pragma: no cover
    unittest.main()