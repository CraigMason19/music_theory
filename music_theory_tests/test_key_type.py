import unittest

import _setup

from music_theory.keys import KeyType

class TestKeyTypeAttributes(unittest.TestCase):
    pass

class TestKeyTypeMethods(unittest.TestCase):
    def test_parallel_key_type_major_returns_minor(self):
        parallel = KeyType.Major.parallel
        expected = KeyType.Minor

        self.assertEqual(parallel, expected)

    def test_parallel_key_type_minor_returns_major(self):
        parallel = KeyType.Minor.parallel
        expected = KeyType.Major
        
        self.assertEqual(parallel, expected)

class TestKeyTypeRepresentation(unittest.TestCase):
    pass

if __name__ == '__main__': # pragma: no cover
    unittest.main()