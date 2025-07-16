import unittest

import _setup

from music_theory.notes import Note
from music_theory.instrument_creator import create_standard_bass, create_drop_bass, create_standard_guitar, create_drop_guitar, create_ukulele

class TestBass(unittest.TestCase):
    def test_default_standard_bass_00(self):
        bass = create_standard_bass()
        expected = [Note.E, Note.A, Note.D, Note.G]
        self.assertEqual(bass.tuning, expected)
    
    def test_default_standard_bass_01(self):
        bass = create_standard_bass(Note.E)
        expected = [Note.E, Note.A, Note.D, Note.G]
        self.assertEqual(bass.tuning, expected)

    def test_standard_bass_02(self):
        bass = create_standard_bass(Note.D)
        expected = [Note.D, Note.G, Note.C, Note.F]
        self.assertEqual(bass.tuning, expected)

    def test_default_drop_bass_00(self):
        bass = create_drop_bass()
        expected = [Note.D, Note.A, Note.D, Note.G]
        self.assertEqual(bass.tuning, expected)
    
    def test_default_drop_bass_01(self):
        bass = create_drop_bass(Note.D)
        expected = [Note.D, Note.A, Note.D, Note.G]
        self.assertEqual(bass.tuning, expected)

    def test_drop_bass_02(self):
        bass = create_drop_bass(Note.C)
        expected = [Note.C, Note.G, Note.C, Note.F]
        self.assertEqual(bass.tuning, expected)

class TestGuitar(unittest.TestCase):
    def test_default_standard_guitar_00(self):
        guitar = create_standard_guitar()
        expected = [Note.E, Note.A, Note.D, Note.G, Note.B, Note.E]
        self.assertEqual(guitar.tuning, expected)
    
    def test_default_standard_guitar_01(self):
        guitar = create_standard_guitar(Note.E)
        expected = [Note.E, Note.A, Note.D, Note.G, Note.B, Note.E]
        self.assertEqual(guitar.tuning, expected)

    def test_standard_guitar_02(self):
        guitar = create_standard_guitar(Note.E)
        expected = [Note.E, Note.A, Note.D, Note.G, Note.B, Note.E]
        self.assertEqual(guitar.tuning, expected)

    def test_default_drop_guitar_00(self):
        guitar = create_drop_guitar()
        expected = [Note.D, Note.A, Note.D, Note.G, Note.B, Note.E]
        self.assertEqual(guitar.tuning, expected)
    
    def test_default_guitar_bass_01(self):
        guitar = create_drop_guitar(Note.D)
        expected = [Note.D, Note.A, Note.D, Note.G, Note.B, Note.E]
        self.assertEqual(guitar.tuning, expected)

    def test_drop_guitar_02(self):
        guitar = create_drop_guitar(Note.C)
        expected = [Note.C, Note.G, Note.C, Note.F, Note.A, Note.D]
        self.assertEqual(guitar.tuning, expected)

class TestOtherInstruments(unittest.TestCase):
    def test_default_ukelele(self):
        ukelele = create_ukulele()
        expected = [Note.G, Note.C, Note.E, Note.A]
        self.assertEqual(ukelele.tuning, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()