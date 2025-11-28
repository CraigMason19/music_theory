import unittest

import _setup

from music_theory.notes import Note, transpose, notes_to_string, chromatic_notes
from music_theory.intervals import Interval, interval_distance, intervals_to_string

class TestNoteAttributes(unittest.TestCase):
    def test_items(self):
        expected = [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab, Note.A, Note.Bb, Note.B]
        self.assertEqual(Note.items(), expected)

    def test_all_alias(self):
        expected = [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab, Note.A, Note.Bb, Note.B]
        self.assertEqual(Note.all(), expected)

    def test_items_same_as_all_alias(self):
        self.assertListEqual(Note.items(), Note.all())

    def test_note_C_equality(self):
        self.assertEqual(Note.C, Note.C)

    def test_note_Bb_equality(self):
        self.assertEqual(Note.Bb, Note.Bb)

    def test_random_note_validity(self):
        note = Note.random()
        self.assertIn(note, list(Note))
        
class TestNoteCreation(unittest.TestCase):
    def test_note_index_octave_C_up(self):
        self.assertEqual(Note.from_index(0), Note.C)
        self.assertEqual(Note.from_index(12), Note.C)
        self.assertEqual(Note.from_index(24), Note.C)

    def test_note_index_octave_F_down(self):
        index = Note.F.value
        self.assertEqual(Note.from_index(index), Note.F)
        self.assertEqual(Note.from_index(index - 12), Note.F)
        self.assertEqual(Note.from_index(index - 24), Note.F)

    def test_note_index_wrap_around_up(self):
        self.assertEqual(Note.from_index(15), Note.Eb)

    def test_note_index_wrap_around_B_down(self):
        index = Note.B.value
        self.assertEqual(Note.from_index(index - 27), Note.Ab)

class TestNoteToSharp(unittest.TestCase):
    def test_to_sharp_00(self):
        sharp = Note.to_sharp(Note.Db)
        self.assertEqual(sharp, "C#")

    def test_to_sharp_01(self):
        sharp = Note.to_sharp(Note.F)
        self.assertEqual(sharp, "F")

    def test_to_sharp_02(self):
        sharp = Note.to_sharp(Note.Gb)
        self.assertEqual(sharp, "F#")


class TestNoteFromString(unittest.TestCase):
    def test_from_string_valid(self):
        inputs = [
            "C",
            "A#",
            "b##",
            "Dbb",
        ]

        for _ in inputs:
            self.assertIsNotNone(Note.from_string(_))

    def test_from_string_invalid(self):
        inputs = [
            "",
            " ",
            "      ",
            " C ",
            "V",
            "A~",
            "N~",
            "DBB",
        ]

        for _ in inputs:
            self.assertIsNone(Note.from_string(_))

    def test_from_string_enharmonic_correct(self):
        input = 'c#'
        result = Note.from_string(input).enharmonic()
        expected = "C#"

        self.assertEqual(result, expected)

    def test_from_string_from_enharmonic_correct(self):
        input = Note.Db.enharmonic() # C#
        result = Note.from_string(input)
        expected = Note.Db

        self.assertEqual(result, expected)


class TestNotePreviousAndNext(unittest.TestCase):
    def test_previous_01(self):
        self.assertEqual(Note.C.previous(), Note.B)

    def test_previous_02(self):
        self.assertEqual(Note.Gb.previous(), Note.F)

    def test_next_01(self):
        self.assertEqual(Note.A.next(), Note.Bb)

    def test_next_02(self):
        self.assertEqual(Note.B.previous(), Note.Bb)

class TestNoteStringRepresentation(unittest.TestCase):
    def test_note_str(self):
        note = Note.Db
        self.assertEqual(str(note), "Db")

    def test_note_repr(self):
        note = Note.Db
        self.assertEqual(repr(note), "Note.Db")

    def test_notes_to_string_00(self):
        notes = notes_to_string(Note.items())
        expected = "C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B"

        self.assertEqual(notes, expected)
    
    def test_notes_to_string_01(self):
        notes = notes_to_string([Note.A, Note.Db, Note.F])
        expected = "A, Db, F"

        self.assertEqual(notes, expected)

class TestNoteTranspose(unittest.TestCase):
    def test_transpose_up_00(self):    
        note, expected = transpose(Note.A, Interval.P4, direction='u'), Note.D
        self.assertEqual(note, expected)

    def test_transpose_down_00(self):    
        note, expected = transpose(Note.A, Interval.P4, direction='down'), Note.E
        self.assertEqual(note, expected)

    def test_transpose_C_up_00(self):    
        note, expected = transpose(Note.C, Interval.P4, direction='UP'), Note.F
        self.assertEqual(note, expected)

    def test_transpose_C_down_00(self):    
        note, expected = transpose(Note.C, Interval.P4, direction='Down'), Note.G
        self.assertEqual(note, expected)

    def test_transpose_C_down_01(self):    
        note, expected = transpose(Note.C, Interval.m2, direction='Down'), Note.B
        self.assertEqual(note, expected)

    def test_transpose_value_error(self):
        self.assertRaises(ValueError, transpose, Note.C, Interval.P4, direction='sideways')

    def test_transpose_from_class_up(self):
        note = Note.C.transpose(Interval.P4)
        self.assertEqual(note, Note.F)

    def test_transpose_from_class_down(self):
        note = Note.C.transpose(Interval.P4, direction='Down')
        self.assertEqual(note, Note.G)

class TestNoteChromatics(unittest.TestCase):
    def test_chromatic_notes_up_00(self):
        note, expected = Note.A, [Note.A, Note.Bb, Note.B, Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab]
        self.assertEqual(chromatic_notes(note), expected)

    def test_chromatic_notes_down_00(self):
        note, expected = Note.A, [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]
        self.assertEqual(chromatic_notes(note, direction="down"), expected)

    def test_chromatic_notes_direction_error(self):
        note, expected = Note.A, [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]
        
        with self.assertRaises(ValueError):
            chromatic_notes(Note, "Uppy Up")

    def test_chromatics_from_class_up(self):
        notes = Note.A.chromatics()
        expected = [Note.A, Note.Bb, Note.B, Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G, Note.Ab]
        self.assertEqual(notes, expected)

    def test_chromatics_from_class_down(self):
        notes = Note.A.chromatics("d")
        expected = [Note.A, Note.Ab, Note.G, Note.Gb, Note.F, Note.E, Note.Eb, Note.D, Note.Db, Note.C, Note.B, Note.Bb]
        self.assertEqual(notes, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()