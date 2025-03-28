#-------------------------------------------------------------------------------
# Name:        test_intervals.py
#
# Notes:       A test suite for the intervals script.
#
# Links:       
#
# TODO:
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.notes import Note
from music_theory.intervals import Interval, interval_distance, intervals_to_string

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

    def test_interval_items(self):
        expected = [Interval.Unison, Interval.m2, Interval.M2, Interval.m3, Interval.M3, Interval.P4, Interval.dim5, Interval.P5, Interval.m6, Interval.M6, Interval.m7, Interval.M7]
        self.assertEqual(Interval.items(), expected)

    def test_all_interval_alias(self):
        expected = [Interval.Unison, Interval.m2, Interval.M2, Interval.m3, Interval.M3, Interval.P4, Interval.dim5, Interval.P5, Interval.m6, Interval.M6, Interval.m7, Interval.M7]
        self.assertEqual(Interval.all(), expected)

    def test_interval_items_same_as_all_alias(self):
        self.assertListEqual(Interval.items(), Interval.all())

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

    def test_random_interval_validity(self):
        interval = Interval.random()
        self.assertIn(interval, list(Interval))

    def test_interval_str(self):
        interval = Interval.m7
        self.assertEqual(str(interval), "m7")

    def test_interval_repr(self):
        interval = Interval.m7
        self.assertEqual(repr(interval), "Interval.m7")

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

if __name__ == '__main__': # pragma: no cover
    unittest.main()