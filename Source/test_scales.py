#-------------------------------------------------------------------------------
# Name:        test_scales.py
#
# Notes:       A test for various scale shapes
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest
from notes import Note
import scales as s

class TestNotes(unittest.TestCase):
    #---------------------------------------------------------------------------
    # setUpClass and tearDownClass run before and after all tests, called once
    # NOTE - the camelCase syntax. Important that they are named this way.
    #---------------------------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    #---------------------------------------------------------------------------
    # setUp and tearDown run before every single test.
    #---------------------------------------------------------------------------
    def setUp(self):
        print('\tsetUp')

    def tearDown(self):
        print('\ttearDown')

    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------
    # def test_major_scale(self):
    #     print('\t\ttest_major_scale')

        # scale = s.Scale(Note.C, s.ScaleType.Major)
        # self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B])


    def test_a_major_pentatonic(self):
        print('\t\ttest_a_major_pentatonic')

        scale = s.Scale(Note.A, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.E, Note.Gb])

    def test_a_minor_pentatonic(self):
        print('\t\ttest_a_minor_pentatonic')

        scale = s.Scale(Note.A, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.C, Note.D, Note.E, Note.G])

    def test_c_major_pentatonic(self):
        print('\t\ttest_c_major_pentatonic')

        scale = s.Scale(Note.C, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.G, Note.A])

    def test_c_minor_pentatonic(self):
        print('\t\ttest_c_minor_pentatonic')

        scale = s.Scale(Note.C, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.Eb, Note.F, Note.G, Note.Bb])

if __name__ == '__main__':
    unittest.main()