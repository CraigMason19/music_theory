import unittest

import _setup

from music_theory.mnemonics import Mnemonics

class TestMnemonics(unittest.TestCase):
    def test_random_guitar_tuning_mnemonic(self):
        m = Mnemonics.random(Mnemonics.standard_guitar_tuning)
        self.assertIn(m, Mnemonics.standard_guitar_tuning)

    def test_random_raises_on_empty_list(self):
        with self.assertRaises(IndexError):
            Mnemonics.random([])

if __name__ == '__main__': # pragma: no cover
    unittest.main()