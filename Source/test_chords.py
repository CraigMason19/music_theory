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
from notes import Note
# from chords import chords_in_key, Chord, ChordType

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
    # def test_chord_equal_A_major(self):
    #     print('\t\ttest_chord_equal_A_major')
    #     self.assertEqual(Chord(Note.A, ChordType.Major), Chord(Note.A, ChordType.Major))

    # def test_chord_equal_Gb_minor(self):
    #     print('\t\ttest_chord_equal_Gb_minor')
    #     self.assertEqual(Chord(Note.Gb, ChordType.Minor), Chord(Note.Gb, ChordType.Minor))
    #endregion

    #region Chords in Major Key
    # def test_chords_in_key_A_major(self):
    #     print('\t\ttest_chords_in_key_A_major')

    #     chord_dict = chords_in_key(Note.A, True)
    #     expected = [Chord(Note.A, ChordType.Major),
    #                 Chord(Note.B, ChordType.Minor),
    #                 Chord(Note.Db, ChordType.Minor),
    #                 Chord(Note.D, ChordType.Major),
    #                 Chord(Note.E, ChordType.Major),
    #                 Chord(Note.Gb, ChordType.Minor),
    #                 Chord(Note.Ab, ChordType.Diminished)]
 
    #     self.assertCountEqual(list(chord_dict.values()), expected)
    #endregion

if __name__ == '__main__':
    unittest.main()