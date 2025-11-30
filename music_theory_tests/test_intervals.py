import unittest

import _setup

from music_theory.notes import Note
from music_theory.intervals import Interval, interval_distance, intervals_to_string

class TestIntervalAttributes(unittest.TestCase):
    def test_interval_items(self):
        expected = [Interval.Unison, Interval.m2, Interval.M2, Interval.m3, Interval.M3, Interval.P4, Interval.dim5, Interval.P5, Interval.m6, Interval.M6, Interval.m7, Interval.M7]
        self.assertEqual(Interval.items(), expected)

    def test_all_interval_alias(self):
        expected = [Interval.Unison, Interval.m2, Interval.M2, Interval.m3, Interval.M3, Interval.P4, Interval.dim5, Interval.P5, Interval.m6, Interval.M6, Interval.m7, Interval.M7]
        self.assertEqual(Interval.all(), expected)

    def test_interval_items_same_as_all_alias(self):
        self.assertListEqual(Interval.items(), Interval.all())

class TestIntervalCreation(unittest.TestCase):
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

class TestIntervalDistance(unittest.TestCase):
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

class TestIntervalStringRepresentation(unittest.TestCase):
    def test_intervals_to_string_00(self):
        intervals = intervals_to_string(Interval.items())
        expected = "Unison, m2, M2, m3, M3, P4, dim5, P5, m6, M6, m7, M7"

        self.assertEqual(intervals, expected)

    def test_intervals_to_string_01(self):
        intervals = intervals_to_string([Interval.Unison, Interval.dim5, Interval.M7])
        expected = "Unison, dim5, M7"

        self.assertEqual(intervals, expected)

    def test_interval_label(self):
        result = Interval.M3.label
        expected = "Major 3rd"

        self.assertEqual(result, expected)

    def test_interval_labels(self):
        result = Interval.labels()

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(x, str) for x in result))


if __name__ == '__main__': # pragma: no cover
    unittest.main()