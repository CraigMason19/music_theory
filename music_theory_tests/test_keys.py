import unittest
from io import StringIO
from unittest.mock import patch

import _setup

from music_theory.notes import Note
from music_theory.chords import Chord, ChordType
from music_theory.keys import Key, KeyType

class TestKeyRandom(unittest.TestCase):
    def test_random_key_vallidity(self):
        k = Key.random()

        self.assertIn(k.root, Note.items())
        self.assertIn(k.type, KeyType.items())

class TestKeyEquality(unittest.TestCase):
    def test_keys_are_equal_same_note_same_type(self):
        a = Key(Note.F, KeyType.Major)
        b = Key(Note.F, KeyType.Major)
        
        self.assertEqual(a, b)

    def test_keys_are_not_equal_different_note_same_type(self):
        a = Key(Note.C, KeyType.Major)
        b = Key(Note.D, KeyType.Major)
        
        self.assertNotEqual(a, b)

    def test_keys_are_not_equal_different_note_different_type(self):
        a = Key(Note.C, KeyType.Major)
        b = Key(Note.G, KeyType.Minor)
        
        self.assertNotEqual(a, b)

    def test_keys_are_not_equal_same_note_different_type(self):
        a = Key(Note.C, KeyType.Major)
        b = Key(Note.C, KeyType.Minor)
        
        self.assertNotEqual(a, b)

    def test_keys_are_not_equal_other_is_not_a_key(self):
        a = Key(Note.C, KeyType.Major)
        b = Chord(Note.C)
        
        self.assertNotEqual(a, b)
    

class TestKeyParallel(unittest.TestCase):
    def test_parallel_key_00(self):
        parallel, expected = Key(Note.C).parallel, Key(Note.C, KeyType.Minor)
        self.assertEqual(parallel, expected)

    def test_parallel_key_01(self):
        parallel, expected = Key(Note.A, KeyType.Minor).parallel, Key(Note.A, KeyType.Major)
        self.assertEqual(parallel, expected)

class TestKeyRelative(unittest.TestCase):
    def test_relative_key_00(self):
        relative, expected = Key(Note.C).relative_key, Key(Note.A, KeyType.Minor)
        self.assertEqual(relative, expected)

    def test_relative_key_01(self):
        relative, expected = Key(Note.D, KeyType.Minor).relative_key, Key(Note.F, KeyType.Major)
        self.assertEqual(relative, expected)

class TestKeySharpsAndFlats(unittest.TestCase):
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

class TestKeyMajorChords(unittest.TestCase):
    def test_chords_in_key_A_major(self):
        chord_dict = Key(Note.A).chords()

        expected = [Chord(Note.A, ChordType.Major),
                    Chord(Note.B, ChordType.Minor),
                    Chord(Note.Db, ChordType.Minor),
                    Chord(Note.D, ChordType.Major),
                    Chord(Note.E, ChordType.Major),
                    Chord(Note.Gb, ChordType.Minor),
                    Chord(Note.Ab, ChordType.Diminished)]
 
        self.assertListEqual(list(chord_dict.values()), expected)   

class TestKeyMinorChords(unittest.TestCase):
    def test_chords_in_key_C_minor(self):
        chord_dict = Key(Note.C, KeyType.Minor).chords()

        expected = [Chord(Note.C, ChordType.Minor),
                    Chord(Note.D, ChordType.Diminished),
                    Chord(Note.Eb, ChordType.Major),
                    Chord(Note.F, ChordType.Minor),
                    Chord(Note.G, ChordType.Minor),
                    Chord(Note.Ab, ChordType.Major),
                    Chord(Note.Bb, ChordType.Major)]
 
        self.assertListEqual(list(chord_dict.values()), expected)    

class TestKeyParalellChords(unittest.TestCase):
    def test_paralell_chords_from_key_A_major(self):
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
        chord_dict = Key(Note.C, KeyType.Minor).parallel_chords()

        expected = [Chord(Note.C, ChordType.Major),
                    Chord(Note.D, ChordType.Minor),
                    Chord(Note.E, ChordType.Minor),
                    Chord(Note.F, ChordType.Major),
                    Chord(Note.G, ChordType.Major),
                    Chord(Note.A, ChordType.Minor),
                    Chord(Note.B, ChordType.Diminished)]
 
        self.assertListEqual(list(chord_dict.values()), expected)      

class TestKeyDominantChords(unittest.TestCase):
    def test_dominant_chords_from_key_A_major(self):
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
        chord_dict = Key(Note.C, KeyType.Minor).dominant_chords()

        expected = [Chord(Note.G, ChordType.Dominant7),
                    Chord(Note.A, ChordType.Dominant7),
                    Chord(Note.Bb, ChordType.Dominant7),
                    Chord(Note.C, ChordType.Dominant7),
                    Chord(Note.D, ChordType.Dominant7),
                    Chord(Note.Eb, ChordType.Dominant7),
                    Chord(Note.F, ChordType.Dominant7)]
 
        self.assertListEqual(list(chord_dict.values()), expected)  


class TestKeyStringRepresentation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Run before all tests, called once
        """
        cls.key = Key(Note.B, KeyType.Minor)

    def test_key_name(self):
        result = self.key.name
        expected = "B Minor"

        self.assertEqual(result, expected)

    def test_key_str(self):
        result = str(self.key)
        expected = "B Minor"

        self.assertEqual(result, expected)

    def test_key_repr(self):
        result = repr(self.key)
        expected = "Key(B Minor)"

        self.assertEqual(result, expected)

    def test_to_string_array_is_a_list_of_strings(self):
        result = self.key.to_string_array()

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(_, str) for _ in result))

    def test_to_string_array_length_chords(self):
        result = len(self.key.to_string_array(dominant=False, parallel=False))
        expected = 3

        self.assertEqual(result, expected)

    def test_to_string_array_length_chords_and_dominants(self):
        result = len(self.key.to_string_array(dominant=True, parallel=False))
        expected = 6

        self.assertEqual(result, expected)

    def test_to_string_array_length_chords_and_dominants_and_parallels(self):
        result = len(self.key.to_string_array(dominant=True, parallel=True))
        expected = 9

        self.assertEqual(result, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_pretty_print_output_matches_to_string_array(self, mock_stdout):
        expected = self.key.to_string_array(dominant=True, parallel=True)

        # Run pretty_print (which prints to stdout) and capture the output
        self.key.pretty_print(dominant=True, parallel=True)
        printed_output = mock_stdout.getvalue().strip().splitlines()

        self.assertEqual(printed_output, expected)


if __name__ == '__main__': # pragma: no cover
    unittest.main()