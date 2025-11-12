import unittest
from io import StringIO
from unittest.mock import patch

import _setup

from music_theory.notes import Note
from music_theory.scales import Scale
from music_theory.scale_type import ScaleType
from music_theory.scale_diatonic import DiatonicScale


class TestDiatonicScaleContains7Notes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_scale_types = []
        cls.invalid_scale_types = []

        for st in ScaleType.items():
            s = Scale(Note.C, st)

            if s.num_notes == 7:
                cls.valid_scale_types.append(st)
            else:
                cls.invalid_scale_types.append(st)

    def test_diatonic_scale_has_7_notes(self):
        for st in self.valid_scale_types:
            try:
                _ = DiatonicScale(Note.C, st)
            except ValueError as e:
                self.fail(f"{st} unexpectedly raised ValueError: {e}")

    def test_diatonic_scale_non_7_note_scale_types_raises_valueerror(self):
        for st in self.invalid_scale_types:
            with self.assertRaises(ValueError, msg=f"{st} did not raise ValueError"):
                _ = DiatonicScale(Note.C, st)


class TestDiatonicScaleNoteDegrees(unittest.TestCase):
    def test_note_degrees_returns_a_dict_of_str_Note(self):
        result = DiatonicScale(Note.C).note_degrees()

        self.assertIsInstance(result, dict)

        for k, v in result.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, Note)

    def test_note_degrees_major_has_7_items(self):
        result = len(DiatonicScale(Note.C).note_degrees())
        expected = 7

        self.assertEqual(result, expected) 

    def test_note_degrees_minor_has_7_items(self):
        result = len(DiatonicScale(Note.C, ScaleType.Minor).note_degrees())
        expected = 7

        self.assertEqual(result, expected) 

    def test_note_degrees_major_has_leading_tone_and_not_subtonic(self):
        result = DiatonicScale(Note.F, ScaleType.Major).note_degrees()

        self.assertIn("leading_tone", result)
        self.assertNotIn("subtonic", result)

    def test_note_degrees_minor_has_leading_tone_and_not_subtonic(self):
        result = DiatonicScale(Note.F, ScaleType.Minor).note_degrees()

        self.assertIn("subtonic", result)
        self.assertNotIn("leading_tone", result)


class TestDiatonicScaleLeadingTonesAndSubTonics(unittest.TestCase):
    def test_major_scale_leading_tone_and_no_subtonic(self):
        scale = DiatonicScale(Note.C, ScaleType.Major)

        self.assertEqual(scale.leading_tone, Note.B)

        with self.assertRaises(AttributeError):
            _ = scale.subtonic

    def test_minor_scale_no_leading_tone_and_subtonic(self):
        scale = DiatonicScale(Note.C, ScaleType.Minor)

        self.assertEqual(scale.subtonic, Note.Bb)

        with self.assertRaises(AttributeError):
            _ = scale.leading_tone

    def test_harmonic_minor_scale_leading_tone_and_no_subtonic(self):
        scale = DiatonicScale(Note.C, ScaleType.HarmonicMinor)

        self.assertEqual(scale.leading_tone, Note.B)

        with self.assertRaises(AttributeError):
            _ = scale.subtonic

    def test_melodic_minor_scale_leading_tone_and_no_subtonic(self):
        scale = DiatonicScale(Note.C, ScaleType.MelodicMinor)

        self.assertEqual(scale.leading_tone, Note.B)

        with self.assertRaises(AttributeError):
            _ = scale.subtonic


class TestDiatonicScaleMajorProperties(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scale = DiatonicScale(Note.C, ScaleType.Major)

    def test_diatonic_scale_major_tonic(self):
        self.assertEqual(self.scale.tonic, Note.C)

    def test_diatonic_scale_major_supertonic(self):
        self.assertEqual(self.scale.supertonic, Note.D)

    def test_diatonic_scale_major_mediant(self):
        self.assertEqual(self.scale.mediant, Note.E)

    def test_diatonic_scale_major_subdominant(self):
        self.assertEqual(self.scale.subdominant, Note.F)

    def test_diatonic_scale_major_dominant(self):
        self.assertEqual(self.scale.dominant, Note.G)

    def test_diatonic_scale_major_submediant(self):
        self.assertEqual(self.scale.submediant, Note.A)

    def test_diatonic_scale_major_has_leading_tone(self):
        self.assertEqual(self.scale.leading_tone, Note.B)

    def test_diatonic_scale_major_subtonic_raises_exception(self):
        with self.assertRaises(AttributeError):
                _ = self.scale.subtonic


class TestDiatonicScaleMinorProperties(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scale = DiatonicScale(Note.C, ScaleType.Minor)

    def test_diatonic_scale_minor_tonic(self):
        self.assertEqual(self.scale.tonic, Note.C)

    def test_diatonic_scale_minor_supertonic(self):
        self.assertEqual(self.scale.supertonic, Note.D)

    def test_diatonic_scale_minor_mediant(self):
        self.assertEqual(self.scale.mediant, Note.Eb)

    def test_diatonic_scale_minor_subdominant(self):
        self.assertEqual(self.scale.subdominant, Note.F)

    def test_diatonic_scale_minor_dominant(self):
        self.assertEqual(self.scale.dominant, Note.G)

    def test_diatonic_scale_minor_submediant(self):
        self.assertEqual(self.scale.submediant, Note.Ab)

    def test_diatonic_scale_minor_has_subtonic(self):
        self.assertEqual(self.scale.subtonic, Note.Bb)

    def test_diatonic_scale_minor_leading_tone_raises_exception(self):
        with self.assertRaises(AttributeError):
                _ = self.scale.leading_tone

class TestDiatonicScaleStringRepresentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Run before all tests, called once
        """
        cls.scale = DiatonicScale(Note.B, ScaleType.Minor)

    def test_diatonic_scale_repr(self):
        result = repr(self.scale)
        expected = "DiatonicScale(Note.B, ScaleType.Minor)"

        self.assertEqual(result, expected)

    def test_diatonic_scale_to_string_array_is_a_list_of_strings(self):
        result = self.scale.to_string_array()

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(_, str) for _ in result))

    def test_diatonic_scale_to_string_array_length(self):
        result = len(self.scale.to_string_array())
        expected = 8

        self.assertEqual(result, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_pretty_print_output_matches_to_string_array(self, mock_stdout):
        expected = self.scale.to_string_array()

        # Run pretty_print (which prints to stdout) and capture the output
        self.scale.pretty_print()
        printed_output = mock_stdout.getvalue().strip().splitlines()

        self.assertEqual(printed_output, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()