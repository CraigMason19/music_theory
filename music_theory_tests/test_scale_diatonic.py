#-------------------------------------------------------------------------------
# Name:        test_scale_diatonic.py
#
# Notes:       A test for the Diatonic scale class
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.notes import Note
from music_theory.scale_type import ScaleType
from music_theory.scale_diatonic import DiatonicScale

class TestDiatonicScale(unittest.TestCase):
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

    def test_diatonic_scale_valid(self):
        valid_types = [
            ScaleType.Major,
            ScaleType.Minor,
            ScaleType.HarmonicMinor,
            ScaleType.MelodicMinor,
            ScaleType.Locrian,
        ]
        
        for scale_type in valid_types:
            try:
                scale = DiatonicScale(Note.A, scale_type)
            except ValueError as e:
                self.fail(f"DiatonicScale raised ValueError unexpectedly for {scale_type}: {e}")

    def test_diatonic_scale_invalid(self):
        self.assertRaises(ValueError, DiatonicScale, Note.A, ScaleType.Blues)

    #region properties

    def test_diatonic_scale_tonic(self):
        ds = DiatonicScale(Note.A, ScaleType.Lydian)
        expected = Note.A
        self.assertEqual(ds.tonic, expected)

    #endregion


if __name__ == '__main__': # pragma: no cover
    unittest.main()