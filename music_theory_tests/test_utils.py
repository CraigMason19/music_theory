import unittest

import _setup

from music_theory.utils import UP_DIRECTIONS, DOWN_DIRECTIONS, index_to_range

class TestUtilsIndexToRange(unittest.TestCase):
    def test_index_to_range_negative_00(self):
        result = index_to_range(-12)
        expected = 0
        
        self.assertEqual(result, expected)

    def test_index_to_range_negative_01(self):
        result = index_to_range(-144)
        expected = 0

        self.assertEqual(result, expected)

    def test_index_to_range_positive_00(self):
        result = index_to_range(144)
        expected = 0

        self.assertEqual(result, expected)

    def test_index_to_range_positive_01(self):
        result = index_to_range(121)
        expected = 1

        self.assertEqual(result, expected)

class TestUtilsDirections(unittest.TestCase):
    def test_direction_in_up_directions_correct(self):
        self.assertIn('up', UP_DIRECTIONS)

    def test_direction_in_up_directions_incorrect(self):
        self.assertNotIn('uppy', UP_DIRECTIONS)

    def test_direction_in_down_directions_correct(self):
        self.assertIn('down', DOWN_DIRECTIONS)

    def test_direction_in_down_directions_incorrect(self):
        self.assertNotIn('downy', DOWN_DIRECTIONS)

if __name__ == '__main__': # pragma: no cover
    unittest.main()