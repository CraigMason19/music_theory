#-------------------------------------------------------------------------------
# Name:        test_scale_types.py
#
# Notes:       A test for various scale types
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.scale_type import ScaleType

class TestScaleType(unittest.TestCase):
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

if __name__ == '__main__': # pragma: no cover
    unittest.main()