#-------------------------------------------------------------------------------
# Name:        test_utils.py
#
# Notes:       A test suite for the utils script.
#
# Links:       
#
# TODO:
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.utils import UP_DIRECTIONS, DOWN_DIRECTIONS, index_to_range

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

    def test_index_to_range_negative_00(self):
        result = index_to_range(-12)
        expected = 0
        self.assertEqual(result, expected)

    def test_index_to_range_negative_01(self):
        result = index_to_range(-144)
        expected = 0
        self.assertEqual(result, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()