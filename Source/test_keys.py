#-------------------------------------------------------------------------------
# Name:        test_keys.py
#
# Notes:       A test for various chords in a certain key.
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest
from notes import Note
from chords import Chord, ChordType
from keys import KeyType, chords_in_key, dominant_chords_in_key

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

    #region Chords in Major Key
    def test_chords_in_key_A_major(self):
        print('\t\ttest_chords_in_key_A_major')

        chord_dict = chords_in_key(Note.A)

        expected = [Chord(Note.A, ChordType.Major),
                    Chord(Note.B, ChordType.Minor),
                    Chord(Note.Db, ChordType.Minor),
                    Chord(Note.D, ChordType.Major),
                    Chord(Note.E, ChordType.Major),
                    Chord(Note.Gb, ChordType.Minor),
                    Chord(Note.Ab, ChordType.Diminished)]
 
        self.assertListEqual(list(chord_dict.values()), expected)   
    #endregion

    #region Chords in Minor Key
    def test_chords_in_key_C_minor(self):
        print('\t\ttest_chords_in_key_C_minor')

        chord_dict = chords_in_key(Note.C, KeyType.Minor)

        expected = [Chord(Note.C, ChordType.Minor),
                    Chord(Note.D, ChordType.Diminished),
                    Chord(Note.Eb, ChordType.Major),
                    Chord(Note.F, ChordType.Minor),
                    Chord(Note.G, ChordType.Minor),
                    Chord(Note.Ab, ChordType.Major),
                    Chord(Note.Bb, ChordType.Major)]
 
        self.assertListEqual(list(chord_dict.values()), expected)    
    #endregion

    #region Paralell Chords
    def test_paralell_chords_from_key_A_major(self):
        print('\t\ttest_paralell_chords_from_key_A_major')

        chord_dict = chords_in_key(Note.A, KeyType.Major.parallel())

        expected = [Chord(Note.A, ChordType.Minor),
                    Chord(Note.B, ChordType.Diminished),
                    Chord(Note.C, ChordType.Major),
                    Chord(Note.D, ChordType.Minor),
                    Chord(Note.E, ChordType.Minor),
                    Chord(Note.F, ChordType.Major),
                    Chord(Note.G, ChordType.Major)]
 
        self.assertListEqual(list(chord_dict.values()), expected)      

    def test_paralell_chords_from_key_C_minor(self):
        print('\t\ttest_paralell_chords_from_key_C_minor')

        chord_dict = chords_in_key(Note.C, KeyType.Minor.parallel())

        expected = [Chord(Note.C, ChordType.Major),
                    Chord(Note.D, ChordType.Minor),
                    Chord(Note.E, ChordType.Minor),
                    Chord(Note.F, ChordType.Major),
                    Chord(Note.G, ChordType.Major),
                    Chord(Note.A, ChordType.Minor),
                    Chord(Note.B, ChordType.Diminished)]
 
        self.assertListEqual(list(chord_dict.values()), expected)      
    #endregion

    #region Dominant Chords
    def test_dominant_chords_from_key_A_major(self):
        print('\t\ttest_dominant_chords_from_key_A_major')

        chord_dict = dominant_chords_in_key(Note.A, KeyType.Major)

        expected = [Chord(Note.E, ChordType.Seven),
                    Chord(Note.Gb, ChordType.Seven),
                    Chord(Note.Ab, ChordType.Seven),
                    Chord(Note.A, ChordType.Seven),
                    Chord(Note.B, ChordType.Seven),
                    Chord(Note.Db, ChordType.Seven),
                    Chord(Note.Eb, ChordType.Seven)]
 
        self.assertListEqual(list(chord_dict.values()), expected)   

    def test_dominant_chords_from_key_C_minor(self):
        print('\t\ttest_dominant_chords_from_key_C_minor')

        chord_dict = dominant_chords_in_key(Note.C, KeyType.Minor)

        expected = [Chord(Note.G, ChordType.Seven),
                    Chord(Note.A, ChordType.Seven),
                    Chord(Note.Bb, ChordType.Seven),
                    Chord(Note.C, ChordType.Seven),
                    Chord(Note.D, ChordType.Seven),
                    Chord(Note.Eb, ChordType.Seven),
                    Chord(Note.F, ChordType.Seven)]
 
        self.assertListEqual(list(chord_dict.values()), expected)  
    #endregion

if __name__ == '__main__':
    unittest.main()