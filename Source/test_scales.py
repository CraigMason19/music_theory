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

class TestScales(unittest.TestCase):
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

    #region MajorScales
    def test_a_major_scale(self):
        scale = s.Scale(Note.A, s.ScaleType.Major)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.D, Note.E, Note.Gb, Note.Ab])

    def test_c_major_scale(self):
        scale = s.Scale(Note.C, s.ScaleType.Major)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B])

    def test_f_major_scale(self):
        scale = s.Scale(Note.F, s.ScaleType.Major)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.A, Note.Bb, Note.C, Note.D, Note.E])
    #endregion

    #region MinorScales
    def test_a_minor_scale(self):
        scale = s.Scale(Note.A, s.ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.C, Note.D, Note.E, Note.F, Note.G])

    def test_c_minor_scale(self):
        scale = s.Scale(Note.C, s.ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.Eb, Note.F, Note.G, Note.Ab, Note.Bb])

    def test_f_minor_scale(self):
        scale = s.Scale(Note.F, s.ScaleType.Minor)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.Ab, Note.Bb, Note.C, Note.Db, Note.Eb])
    #endregion

    #region MajorPentatonicScales
    def test_a_major_pentatonic(self):
        scale = s.Scale(Note.A, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.B, Note.Db, Note.E, Note.Gb])
    
    def test_c_major_pentatonic(self):
        scale = s.Scale(Note.C, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.D, Note.E, Note.G, Note.A])

    def test_f_major_pentatonic(self):
        scale = s.Scale(Note.F, s.ScaleType.MajorPentatonic)
        self.assertEqual(scale.notes, [Note.F, Note.G, Note.A, Note.C, Note.D])
    #endregion

    #region MinorPentatonicScales
    def test_a_minor_pentatonic(self):
        scale = s.Scale(Note.A, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.A, Note.C, Note.D, Note.E, Note.G])

    def test_c_minor_pentatonic(self):
        scale = s.Scale(Note.C, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.C, Note.Eb, Note.F, Note.G, Note.Bb])

    def test_f_minor_pentatonic(self):
        scale = s.Scale(Note.F, s.ScaleType.MinorPentatonic)
        self.assertEqual(scale.notes, [Note.F, Note.Ab, Note.Bb, Note.C, Note.Eb])
    #endregion

if __name__ == '__main__':
    unittest.main()