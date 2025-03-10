#-------------------------------------------------------------------------------
# Name:        test_chords.py
#
# Notes:       A test for various chord shapes
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

from music_theory.notes import Note
from music_theory.chords import Chord, ChordType

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

    #region Chords Equal

    def test_chord_equal_A_major(self):
        print('\t\ttest_chord_equal_B_major')
        self.assertEqual(Chord(Note.B, ChordType.Major), Chord(Note.B, ChordType.Major))

    def test_chord_equal_Gb_minor(self):
        print('\t\ttest_chord_equal_Gb_minor')
        self.assertEqual(Chord(Note.Gb, ChordType.Minor), Chord(Note.Gb, ChordType.Minor))
    
    #endregion

    #region string representation

    def test_str_equal_Gb_major(self):
        print('\t\ttest_str_equal_Gb_major')
        expected = str(Chord(Note.Gb, ChordType.Major))
        self.assertEqual("GbM", expected)

    def test_str_equal_Gb_minor(self):
        print('\t\ttest_str_equal_Gb_minor')
        expected = str(Chord(Note.Gb, ChordType.Minor))
        self.assertEqual("Gbm", expected)
        
    def test_str_equal_Gb_diminished(self):
        print('\t\ttest_str_equal_Gb_diminished')
        expected = str(Chord(Note.Gb, ChordType.Diminished))
        self.assertEqual("Gbdim", expected)

    def test_str_equal_Gb_seven(self):
        print('\t\ttest_str_equal_Gb_seven')
        expected = str(Chord(Note.Gb, ChordType.Seven))
        self.assertEqual("Gb7", expected)

    #endregion
    


if __name__ == '__main__':
    unittest.main()