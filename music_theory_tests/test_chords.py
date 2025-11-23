import unittest

import _setup

from music_theory.notes import Note
from music_theory.chords import Chord, ChordType, unique_notes_in_chords

class TestChordValidity(unittest.TestCase):
    def test_chord_valid_00(self):
        chord = Chord(Note.Gb, ChordType.Minor)
        expected = Chord(Note.Gb, ChordType.Minor)
        self.assertEqual(chord, expected)

    def test_chord_invalid_00(self):
        with self.assertRaises(ValueError):
                Chord(Note.A, 5)

    def test_chord_invalid_01(self):
        with self.assertRaises(ValueError):
                Chord(Note.A, 17)

    def test_chord_invalid_02(self):
        with self.assertRaises(ValueError):
                Chord(Note.A, -1)

    def test_random_chord_validity(self):
        chord = Chord.random()
        self.assertIn(chord.root, list(Note))
        self.assertIn(chord.chord_type, list(ChordType))

class TestChordEquality(unittest.TestCase):
    def test_chord_equal_A_major(self):
        self.assertEqual(Chord(Note.B, ChordType.Major), Chord(Note.B, ChordType.Major))

    def test_chord_equal_Gb_minor(self):
        self.assertEqual(Chord(Note.Gb, ChordType.Minor), Chord(Note.Gb, ChordType.Minor))

    def test_chord_not_equal_Gb_minor_and_Gb_major(self):
        self.assertNotEqual(Chord(Note.Gb, ChordType.Minor), Chord(Note.Gb, ChordType.Major))
    
    def test_chord_not_equal_with_non_chord(self):
        chord = Chord(Note.Gb, ChordType.Minor)
        
        self.assertFalse(chord == 5)
        self.assertFalse(chord == "string")
        self.assertFalse(chord == None)

class TestChordNotes(unittest.TestCase):
    def test_chord_notes_A_major(self):
        chord = Chord(Note.A, ChordType.Major)
        expected_notes = [Note.A, Note.Db, Note.E]
        self.assertEqual(chord.notes, expected_notes)
    
    def test_chord_notes_for_A_minor(self):
        chord = Chord(Note.A, ChordType.Minor)
        expected_notes = [Note.A, Note.C, Note.E]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_diminished(self):
        chord = Chord(Note.A, ChordType.Diminished)
        expected_notes = [Note.A, Note.C, Note.Eb] 
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_dominant_seven(self):
        chord = Chord(Note.A, ChordType.Dominant7)
        expected_notes = [Note.A, Note.Db, Note.E, Note.G]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_major_seven(self):
        chord = Chord(Note.A, ChordType.Major7)
        expected_notes = [Note.A, Note.Db, Note.E, Note.Ab]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_minor_seven(self):
        chord = Chord(Note.A, ChordType.Minor7)
        expected_notes = [Note.A, Note.C, Note.E, Note.G]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_diminished_seven(self):
        chord = Chord(Note.A, ChordType.Diminished7)
        expected_notes = [Note.A, Note.C, Note.Eb, Note.Gb]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_sus2(self):
        chord = Chord(Note.A, ChordType.Sus2)
        expected_notes = [Note.A, Note.B, Note.E]
        self.assertEqual(chord.notes, expected_notes)

    def test_chord_notes_for_A_sus4(self):
        chord = Chord(Note.A, ChordType.Sus4)
        expected_notes = [Note.A, Note.D, Note.E]
        self.assertEqual(chord.notes, expected_notes)

class TestChordExtensions(unittest.TestCase):
    def test_chord_A_major_add9(self):
        notes = Chord(Note.A, ChordType.Major).add9()
        expected_notes = [Note.A, Note.Db, Note.E, Note.B]
        self.assertEqual(notes, expected_notes)

    def test_chord_A_major_add11(self):
        notes = Chord(Note.A, ChordType.Major).add11()
        expected_notes = [Note.A, Note.Db, Note.E, Note.D]
        self.assertEqual(notes, expected_notes)

    def test_chord_A_major_add13(self):
        notes = Chord(Note.A, ChordType.Major).add13()
        expected_notes = [Note.A, Note.Db, Note.E, Note.Gb]
        self.assertEqual(notes, expected_notes)

class TestChordNotation(unittest.TestCase):
    def test_chord_A_major_notation(self):
        notation = Chord(Note.A, ChordType.Major).notation
        expected_notation = 'M'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_minor_notation(self):
        notation = Chord(Note.A, ChordType.Minor).notation
        expected_notation = 'm'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_diminished_notation(self):
        notation = Chord(Note.A, ChordType.Diminished).notation
        expected_notation = '°'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_dominant_7_notation(self):
        notation = Chord(Note.A, ChordType.Dominant7).notation
        expected_notation = '7'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_major_7_notation(self):
        notation = Chord(Note.A, ChordType.Major7).notation
        expected_notation = 'Δ7'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_minor_7_notation(self):
        notation = Chord(Note.A, ChordType.Minor7).notation
        expected_notation = 'm7'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_diminished_7_notation(self):
        notation = Chord(Note.A, ChordType.Diminished7).notation
        expected_notation = '°7'
        self.assertEqual(notation, expected_notation)

    def test_chord_A_sus2_notation(self):
        notation = Chord(Note.A, ChordType.Sus2).notation
        expected_notation = 'sus2'
        self.assertEqual(notation, expected_notation)    

    def test_chord_A_sus4_notation(self):
        notation = Chord(Note.A, ChordType.Sus4).notation
        expected_notation = 'sus4'
        self.assertEqual(notation, expected_notation)   


class TestChordInversions(unittest.TestCase):
    def test_chord_inversions_A_minor(self):
        result = Chord(Note.A, ChordType.Minor).inversions()
        expected = [
            [Note.C, Note.E, Note.A],
            [Note.E, Note.A, Note.C],
        ]

        self.assertEqual(result, expected)


class TestChordStringRepresentation(unittest.TestCase):
    def test_str_equal_Gb_major(self):
        expected = str(Chord(Note.Gb, ChordType.Major))
        self.assertEqual("GbM", expected)

    def test_str_equal_Gb_minor(self):
        expected = str(Chord(Note.Gb, ChordType.Minor))
        self.assertEqual("Gbm", expected)
        
    def test_str_equal_Gb_diminished(self):
        expected = str(Chord(Note.Gb, ChordType.Diminished))
        self.assertEqual("Gb°", expected)

    def test_str_equal_Gb_seven(self):
        expected = str(Chord(Note.Gb, ChordType.Dominant7))
        self.assertEqual("Gb7", expected)

    def test_chord_str(self):
        chord = Chord(Note.F, ChordType.Diminished7)
        self.assertEqual(str(chord), "F°7")

    def test_chord_repr(self):
        chord = Chord(Note.F, ChordType.Diminished7)
        self.assertEqual(repr(chord), "Chord(F, Diminished7)")
    
class TestUniqueNotesInChord(unittest.TestCase):
    def test_unique_A_major_A_minor(self):
        aM = Chord(Note.A, ChordType.Major)
        am = Chord(Note.A, ChordType.Minor)

        result = unique_notes_in_chords(aM, am)
        expected = [Note.C, Note.Db, Note.E, Note.A]
        self.assertEqual(result, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()