#-------------------------------------------------------------------------------
# Name:        test_mnemonics.py
#
# Notes:       A test suite for the instrument script.
#
# Links:        
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest

import _setup

from music_theory.mnemonics import Mnemonics

class TestChords(unittest.TestCase):
    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------

    #region tunings

    def test_custom_instrument_00(self):
        m = Mnemonics.random(Mnemonics.standard_guitar_tuning)
        self.assertIn(m, Mnemonics.standard_guitar_tuning)

    #endregion

if __name__ == '__main__': # pragma: no cover
    unittest.main()