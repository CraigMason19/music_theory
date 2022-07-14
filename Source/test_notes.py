#-------------------------------------------------------------------------------
# Name:        test_notes.py
#
# Notes:       A test suite for the Note class
#
# Links:       
#
# TODO:
#-------------------------------------------------------------------------------

import unittest
from notes import Note

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
    def test_next_note(self):
        print('\t\ttest_next_note')

        # note, expected = notes.Notes.C, notes.Notes.D
        # self.assertEqual(1, 1) Notes
        

if __name__ == '__main__':
    unittest.main()