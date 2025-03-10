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

import _setup

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

    #region Chords Notes

    def test_chord_notes_A_major(self):
        print('\t\ttest_chord_notes_for_A_major')
        chord = Chord(Note.A, ChordType.Major)
        expected_notes = [Note.A, Note.Db, Note.E]
        self.assertEqual(chord.notes, expected_notes)
    
    def test_chord_notes_for_A_minor(self):
        print('\t\ttest_chord_notes_for_A_minor')
        chord = Chord(Note.A, ChordType.Minor)
        expected_notes = [Note.A, Note.C, Note.E]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_diminished(self):
        print('\t\ttest_chord_notes_for_A_diminished')
        chord = Chord(Note.A, ChordType.Diminished)
        expected_notes = [Note.A, Note.C, Note.Eb] 
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_seven(self):
        print('\t\ttest_chord_notes_for_A_seven')
        chord = Chord(Note.A, ChordType.Seven)
        expected_notes = [Note.A, Note.Db, Note.E, Note.G]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_sus2(self):
        print('\t\ttest_chord_notes_for_A_sus2')
        chord = Chord(Note.A, ChordType.Sus2)
        expected_notes = [Note.A, Note.B, Note.E]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_sus4(self):
        print('\t\ttest_chord_notes_for_A_sus4')
        chord = Chord(Note.A, ChordType.Sus4)
        expected_notes = [Note.A, Note.D, Note.E]
        self.assertEqual(chord.notes, expected_notes)
    
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