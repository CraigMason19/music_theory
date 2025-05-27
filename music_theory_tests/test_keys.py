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

import _setup

from music_theory.notes import Note
from music_theory.chords import Chord, ChordType
from music_theory.keys import Key, KeyType

class TestKeys(unittest.TestCase):
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

    #region KeyTypes
    def test_parallel_key_type_00(self):
        parallel, expected = KeyType.Major.parallel, KeyType.Minor
        self.assertEqual(parallel, expected)

    def test_parallel_key_type_01(self):
        parallel, expected = KeyType.Minor.parallel, KeyType.Major
        self.assertEqual(parallel, expected)
    #endregion

    #region Parallel Keys
    def test_parallel_key_00(self):
        parallel, expected = Key(Note.C).parallel, Key(Note.C, KeyType.Minor)
        self.assertEqual(parallel, expected)

    def test_parallel_key_01(self):
        parallel, expected = Key(Note.A, KeyType.Minor).parallel, Key(Note.A, KeyType.Major)
        self.assertEqual(parallel, expected)
    #endregion

    #region Relative Keys
    def test_relative_key_00(self):
        relative, expected = Key(Note.C).relative_key, Key(Note.A, KeyType.Minor)
        self.assertEqual(relative, expected)

    def test_relative_key_01(self):
        relative, expected = Key(Note.D, KeyType.Minor).relative_key, Key(Note.F, KeyType.Major)
        self.assertEqual(relative, expected)
    #endregion

    #region Sharps & flats
    def test_sharp_count_00(self):
        sharps, expected = Key(Note.Db).sharp_count, 7
        self.assertEqual(sharps, expected)

    def test_sharp_count_01(self):
        sharps, expected = Key(Note.A).sharp_count, 3
        self.assertEqual(sharps, expected)

    def test_sharp_count_02(self):
        sharps, expected = Key(Note.F, KeyType.Minor).sharp_count, 0
        self.assertEqual(sharps, expected)

    def test_flat_count_00(self):
        flats, expected = Key(Note.B).flat_count, 7
        self.assertEqual(flats, expected)

    def test_flat_count_01(self):
        flats, expected = Key(Note.C, KeyType.Minor).flat_count, 3
        self.assertEqual(flats, expected)

    def test_sharps_00(self):
        sharps = Key(Note.B, KeyType.Minor).sharps
        expected = [Note.F, Note.C]
        self.assertListEqual(sharps, expected)

    def test_sharps_01(self):
        sharps = Key(Note.B, KeyType.Minor).sharps
        expected = [Note.F, Note.C]
        self.assertListEqual(sharps, expected)

    def test_flats_00(self):
        flats = Key(Note.Ab).flats
        expected = [Note.B, Note.E, Note.A, Note.D]
        self.assertListEqual(flats, expected)

    def test_flats_01(self):
        flats = Key(Note.B, KeyType.Minor).flats
        expected = []
        self.assertListEqual(flats, expected)
#endregion

    #region Chords in Major Key
    def test_chords_in_key_A_major(self):
        print('\t\ttest_chords_in_key_A_major')

        chord_dict = Key(Note.A).chords()

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

        chord_dict = Key(Note.C, KeyType.Minor).chords()

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

        chord_dict = Key(Note.A).parallel_chords()

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

        chord_dict = Key(Note.C, KeyType.Minor).parallel_chords()

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

        chord_dict = Key(Note.A, KeyType.Major).dominant_chords()

        expected = [Chord(Note.E, ChordType.Dominant7),
                    Chord(Note.Gb, ChordType.Dominant7),
                    Chord(Note.Ab, ChordType.Dominant7),
                    Chord(Note.A, ChordType.Dominant7),
                    Chord(Note.B, ChordType.Dominant7),
                    Chord(Note.Db, ChordType.Dominant7),
                    Chord(Note.Eb, ChordType.Dominant7)]
 
        self.assertListEqual(list(chord_dict.values()), expected)   

    def test_dominant_chords_from_key_C_minor(self):
        print('\t\ttest_dominant_chords_from_key_C_minor')

        chord_dict = Key(Note.C, KeyType.Minor).dominant_chords()

        expected = [Chord(Note.G, ChordType.Dominant7),
                    Chord(Note.A, ChordType.Dominant7),
                    Chord(Note.Bb, ChordType.Dominant7),
                    Chord(Note.C, ChordType.Dominant7),
                    Chord(Note.D, ChordType.Dominant7),
                    Chord(Note.Eb, ChordType.Dominant7),
                    Chord(Note.F, ChordType.Dominant7)]
 
        self.assertListEqual(list(chord_dict.values()), expected)  

    #endregion

if __name__ == '__main__': # pragma: no cover
    unittest.main()