import unittest

import _setup

from music_theory.chords import ChordType

class TestChordTypeMethods(unittest.TestCase):
    def test_chord_type_items(self):
        expected = [ChordType.Major, ChordType.Minor, ChordType.Diminished, ChordType.Dominant7, ChordType.Major7, ChordType.Minor7, ChordType.Diminished7, ChordType.Sus2, ChordType.Sus4]
        
        self.assertEqual(ChordType.items(), expected)

    def test_random_chord_type_validity(self):
        type = ChordType.random()
        
        self.assertIn(type, list(ChordType))

class TestChordTypeRepresentation(unittest.TestCase):
    def test_chord_type_str(self):
        type = ChordType.Dominant7
        expected = "Dominant7"

        self.assertEqual(str(type), expected)

    def test_chord_type_repr(self):
        type = ChordType.Dominant7
        expected = "ChordType.Dominant7"

        self.assertEqual(repr(type), expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()