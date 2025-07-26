import unittest

import _setup

from music_theory.keys import KeyType

class TestKeyTypeAttributes(unittest.TestCase):
    def test_key_type_items(self):
        expected = [KeyType.Major, KeyType.Minor]
        self.assertEqual(KeyType.items(), expected)

    def test_random_key_type_validity(self):
        type = KeyType.random()
        self.assertIn(type, list(KeyType))

class TestKeyTypeParallel(unittest.TestCase):
    def test_parallel_key_type_major_returns_minor(self):
        parallel = KeyType.Major.parallel
        expected = KeyType.Minor

        self.assertEqual(parallel, expected)

    def test_parallel_key_type_minor_returns_major(self):
        parallel = KeyType.Minor.parallel
        expected = KeyType.Major
        
        self.assertEqual(parallel, expected)

class TestKeyTypeStringRepresentation(unittest.TestCase):
    def test_key_type_str(self):
        type = KeyType.Major
        self.assertEqual(str(type), "Major")

    def test_key_type_repr(self):
        type = KeyType.Minor
        self.assertEqual(repr(type), "KeyType.Minor")

if __name__ == '__main__': # pragma: no cover
    unittest.main()