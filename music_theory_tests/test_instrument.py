import unittest

import _setup

from music_theory.notes import Note
from music_theory.intervals import Interval
from music_theory.instrument import StringInstrument, note_at_fret
from music_theory.instrument_creator import create_standard_guitar, E_STANDARD_GUITAR, D_STANDARD_GUITAR, C_STANDARD_GUITAR


class TestInstrumentCreation(unittest.TestCase):
    def test_custom_instrument_00(self):
        instrument = StringInstrument([Note.B, Note.E, Note.A, Note.D, Note.G])
        expected = [Note.B, Note.E, Note.A, Note.D, Note.G]
        self.assertEqual(instrument.tuning, expected)

    def test_custom_instrument_01(self):
        instrument = StringInstrument([Note.B, Note.E, Note.A, Note.D, Note.G])
        expected = 5
        self.assertEqual(instrument.num_strings, expected)

    def test_custom_instrument_no_strings(self):
        self.assertRaises(ValueError, StringInstrument, [])

    def test_tuning_intervals_00(self):
        intervals = [Interval.Unison, Interval.P4, Interval.P4, Interval.P4, Interval.M3, Interval.P4]
        instrument = StringInstrument.from_tuning_intervals(Note.E, intervals)
        
        self.assertEqual(instrument.tuning, E_STANDARD_GUITAR.tuning)


class TestInstrumentCapo(unittest.TestCase):
    def test_add_a_capo_at_second_fret(self):
        guitar = create_standard_guitar()
        guitar.add_capo(2)

        expected_tuning = [Note.Gb, Note.B, Note.E, Note.A, Note.Db, Note.Gb]

        self.assertEqual(guitar.tuning, expected_tuning)

    def test_add_a_capo_at_fourth_fret(self):
        guitar = create_standard_guitar()
        guitar.add_capo(4)

        expected_tuning = [Note.Ab, Note.Db, Note.Gb, Note.B, Note.Eb, Note.Ab]
        self.assertEqual(guitar.tuning, expected_tuning)

    def test_add_a_capo_at_zero_fret(self):
        guitar = create_standard_guitar()

        self.assertRaises(ValueError, guitar.add_capo, 0)

    def test_add_a_capo_at_negative_fret(self):
        guitar = create_standard_guitar()

        self.assertRaises(ValueError, guitar.add_capo, -1)


class TestInstrumentAdjustString(unittest.TestCase):
    def test_adjust_string_up_00(self):
        guitar = create_standard_guitar()
        guitar.adjust_string(0, Interval.M2, "u")

        self.assertEqual(guitar.tuning[0], Note.Gb)

    def test_adjust_string_up_01(self):
        guitar = create_standard_guitar()
        guitar.adjust_string(1, Interval.M2, "d")
        
        self.assertEqual(guitar.tuning[1], Note.G)

    def test_adjust_string_incorrect_string_index_00(self):
        guitar = create_standard_guitar()

        self.assertRaises(ValueError, guitar.adjust_string, -1, Interval.M2, "d")

    def test_adjust_string_incorrect_string_index_01(self):
        guitar = create_standard_guitar()

        self.assertRaises(ValueError, guitar.adjust_string, 6, Interval.M2, "d")

class TestInstrumentDetuning(unittest.TestCase):
    def test_detune_00(self):
        guitar = create_standard_guitar()
        guitar.detune(Interval.M2)
 
        self.assertEqual(guitar.tuning, D_STANDARD_GUITAR.tuning)

    def test_detune_01(self):
        guitar = create_standard_guitar(Note.D)
        guitar.detune(Interval.M2)
        self.assertEqual(guitar.tuning, C_STANDARD_GUITAR.tuning)


class TestInstrumentNoteAtFret(unittest.TestCase):
    def test_note_at_fret_incorrct_string_index_00(self):
        self.assertRaises(ValueError, create_standard_guitar().note_at_fret, -1, 3)

    def test_note_at_fret_incorrct_string_index_01(self):
        self.assertRaises(ValueError, create_standard_guitar().note_at_fret, 6, 3)

    def test_note_at_fret_incorrct_fret(self):
        self.assertRaises(ValueError, create_standard_guitar().note_at_fret, 0, -1)

    def test_note_at_fret_zero_fret(self):
        note = create_standard_guitar().note_at_fret(2, 0)
        self.assertEqual(Note.D, note)

    def test_note_at_fret_00(self):
        note = create_standard_guitar().note_at_fret(2, 0)
        expected = Note.D
        self.assertEqual(note, expected)

    def test_note_at_fret_01(self):
        guitar = create_standard_guitar(Note.D)
        note = guitar.note_at_fret(3, 12)
        expected = Note.F
        self.assertEqual(note, expected)


class TestInstrumentNoteInChord(unittest.TestCase):
    def test_notes_in_chord_to_few_strings(self):
        self.assertRaises(ValueError, create_standard_guitar().notes_in_chord, "x x 3 x 6")

    def test_notes_in_chord_to_many_strings(self):
        self.assertRaises(ValueError, create_standard_guitar().notes_in_chord, "x x x x x x 15")

    def test_notes_in_chord_octave(self):
        notes = create_standard_guitar().notes_in_chord("x 3 x 5 x x")
        expected = [Note.C, Note.C]

        self.assertEqual(notes, expected)

    def test_notes_in_chord_power_chord(self):
        notes = create_standard_guitar().notes_in_chord("x 3 5 5 x x")
        expected = [Note.C, Note.G, Note.C]

        self.assertEqual(notes, expected)

    def test_notes_in_chord_open_d(self):
        notes = create_standard_guitar().notes_in_chord("x x 0 2 3 2")
        expected = [Note.D, Note.A, Note.D, Note.Gb]

        self.assertEqual(notes, expected)

    def test_notes_in_chord_hendrix(self):
        notes = create_standard_guitar().notes_in_chord("0 7 6 7 8 x")
        expected = [Note.E, Note.E, Note.Ab, Note.D, Note.G]

        self.assertEqual(notes, expected)


class TestInstrumentIntervalsInChord(unittest.TestCase):
    def test_intervals_in_power_chord(self):
        intervals = create_standard_guitar().intervals_in_chord("x 3 5 5 x x")
        expected = [Interval.Unison, Interval.P5, Interval.Unison]

        self.assertEqual(intervals, expected)

    def test_intervals_in_empty_chord(self):
        intervals = create_standard_guitar().intervals_in_chord("x x x x x x")
        self.assertEqual(intervals, [])

    def test_intervals_in_chord_to_few_strings(self):
        self.assertRaises(ValueError, create_standard_guitar().intervals_in_chord, "x x 3 x 6")

    def test_intervals_in_chord_to_many_strings(self):
        self.assertRaises(ValueError, create_standard_guitar().intervals_in_chord, "x x x x x x 15")

    def test_intervals_in_chord_octave(self):
        intervals = create_standard_guitar().intervals_in_chord("x 3 x 5 x x")
        expected = [Interval.Unison, Interval.Unison]

        self.assertEqual(intervals, expected)

    def test_intervals_in_chord_power_chord(self):
        intervals = create_standard_guitar().intervals_in_chord("x 3 5 5 x x")
        expected = [Interval.Unison, Interval.P5, Interval.Unison]

        self.assertEqual(intervals, expected)

    def test_intervals_in_chord_open_d(self):
        intervals = create_standard_guitar().intervals_in_chord("x x 0 2 3 2")
        expected = [Interval.Unison, Interval.P5, Interval.Unison, Interval.M3]

        self.assertEqual(intervals, expected)


class TestInstrumentNotesInRiff(unittest.TestCase):
    pass


class TestInstrumentStringRepresentation(unittest.TestCase):
    def test_str_method(self):
        expected = "E, A, D, G, B, E"
        self.assertEqual(str(create_standard_guitar()), expected)

    def test_repr_method(self):
        expected = "StringInstrument(6, [E, A, D, G, B, E])"
        self.assertEqual(repr(create_standard_guitar()), expected)


class TestNoteAtFret(unittest.TestCase):
    def test_note_at_fret_A_on_E_string(self):
        result = note_at_fret(Note.E, 5)
        expected = Note.A

        self.assertEqual(result, expected)

    def test_note_at_fret_bigger_than_24_frets(self):
        result = note_at_fret(Note.A, 36)
        expected = Note.A

        self.assertEqual(result, expected)

    def test_note_at_fret_0_on_D_string(self):
        result = note_at_fret(Note.D, 0)
        expected = Note.D

        self.assertEqual(result, expected)

    def test_note_at_fret_negative_fret(self):
        with self.assertRaises(ValueError):
            _ = note_at_fret(Note.B, -1)


if __name__ == '__main__': # pragma: no cover
    unittest.main()