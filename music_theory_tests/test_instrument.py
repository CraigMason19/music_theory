#-------------------------------------------------------------------------------
# Name:        test_instrument.py
#
# Notes:       A test suite for the instrument script.
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.notes import Note, Interval
from music_theory.instrument import StringInstrument
from music_theory.instrument_creator import create_standard_guitar, E_STANDARD_GUITAR

class TestChords(unittest.TestCase):
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

    #region Creation

    def test_custom_instrument_00(self):
        instrument = StringInstrument([Note.B, Note.E, Note.A, Note.D, Note.G])
        expected = [Note.B, Note.E, Note.A, Note.D, Note.G]
        self.assertEqual(instrument.tuning, expected)

    def test_custom_instrument_01(self):
        instrument = StringInstrument([Note.B, Note.E, Note.A, Note.D, Note.G])
        expected = 5
        self.assertEqual(instrument.num_strings, expected)

    def test_custom_instrument_no_strings(self):
        self.assertRaises(ValueError, StringInstrument, [])

    def test_tuning_intervals_00(self):
        intervals = [Interval.Unison, Interval.P4, Interval.P4, Interval.P4, Interval.M3, Interval.P4]
        instrument = StringInstrument.from_tuning_intervals(Note.E, intervals)
        
        self.assertEqual(instrument.tuning, E_STANDARD_GUITAR.tuning)

    #endregion

    #region Capo
    def test_add_a_capo_at_second_fret(self):
        guitar = create_standard_guitar(Note.E)
        guitar.add_capo(2)

        expected_tuning = [Note.Gb, Note.B, Note.E, Note.A, Note.Db, Note.Gb]
        self.assertEqual(guitar.tuning, expected_tuning)

    def test_add_a_capo_at_fourth_fret(self):
        guitar = create_standard_guitar(Note.E)
        guitar.add_capo(4)

        expected_tuning = [Note.Ab, Note.Db, Note.Gb, Note.B, Note.Eb, Note.Ab]
        self.assertEqual(guitar.tuning, expected_tuning)

    def test_add_a_capo_at_zero_fret(self):
        guitar = create_standard_guitar(Note.E)
        self.assertRaises(ValueError, guitar.add_capo, 0)

    def test_add_a_capo_at_negative_fret(self):
        guitar = create_standard_guitar(Note.E)
        self.assertRaises(ValueError, guitar.add_capo, -1)

    #endregion

    #region Adjust String

    def test_adjust_string_up_00(self):
        guitar = create_standard_guitar(Note.E)
        guitar.adjust_string(0, Interval.M2, "u")
        self.assertEqual(guitar.tuning[0], Note.Gb)

    def test_adjust_string_up_01(self):
        guitar = create_standard_guitar(Note.E)
        guitar.adjust_string(1, Interval.M2, "d")
        self.assertEqual(guitar.tuning[1], Note.G)

    def test_adjust_string_incorrect_string_index_00(self):
        guitar = create_standard_guitar(Note.E)
        self.assertRaises(ValueError, guitar.adjust_string, -1, Interval.M2, "d")

    def test_adjust_string_incorrect_string_index_01(self):
        guitar = create_standard_guitar(Note.E)
        self.assertRaises(ValueError, guitar.adjust_string, 6, Interval.M2, "d")

    #endregion

if __name__ == '__main__':
    unittest.main()