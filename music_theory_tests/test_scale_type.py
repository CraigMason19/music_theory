import unittest

from music_theory.scale_type import ScaleType

class TestScaleTypeAttributes(unittest.TestCase):
    def test_scale_type_items(self):
        expected = [ScaleType.Major, ScaleType.Minor, ScaleType.MajorPentatonic, ScaleType.MinorPentatonic, ScaleType.Ionian,
            ScaleType.Dorian, ScaleType.Phrygian, ScaleType.Lydian, ScaleType.Mixolydian, ScaleType.Aeolian, ScaleType.Locrian,
            ScaleType.Blues, ScaleType.HarmonicMinor, ScaleType.MelodicMinor]
        self.assertEqual(ScaleType.items(), expected)

    def test_scale_type_all_alias(self):
        expected = [ScaleType.Major, ScaleType.Minor, ScaleType.MajorPentatonic, ScaleType.MinorPentatonic, ScaleType.Ionian,
            ScaleType.Dorian, ScaleType.Phrygian, ScaleType.Lydian, ScaleType.Mixolydian, ScaleType.Aeolian, ScaleType.Locrian,
            ScaleType.Blues, ScaleType.HarmonicMinor, ScaleType.MelodicMinor]
        self.assertEqual(ScaleType.all(), expected)

    def test_scale_type_items_same_as_all_alias(self):
        self.assertListEqual(ScaleType.items(), ScaleType.all())

    # Modes
    def test_scale_type_modes(self):
        result = ScaleType.modes()
        expected = [
            ScaleType.Ionian,
            ScaleType.Dorian,
            ScaleType.Phrygian,
            ScaleType.Lydian,
            ScaleType.Mixolydian,
            ScaleType.Aeolian,
            ScaleType.Locrian,
        ]

        self.assertEqual(result, expected)

    def test_random_scale_type_validity(self):
        type = ScaleType.random()
        self.assertIn(type, list(ScaleType))


class TestScaleTypeIsDiatonic(unittest.TestCase):
    def test_is_diatonic_true(self):
        result = ScaleType.Dorian.is_diatonic
        expected = True

        self.assertEqual(result, expected)

    def test_is_diatonic_major_true(self):
        result = ScaleType.Major.is_diatonic
        expected = True

        self.assertEqual(result, expected)

    def test_is_diatonic_minor_true(self):
        result = ScaleType.Minor.is_diatonic
        expected = True

        self.assertEqual(result, expected)

    def test_is_diatonic_false(self):
        result = ScaleType.Blues.is_diatonic
        expected = False

        self.assertEqual(result, expected)           


class TestScaleTypeStringRepresentation(unittest.TestCase):
    def test_scale_type_str(self):
        type = ScaleType.HarmonicMinor
        self.assertEqual(str(type), "HarmonicMinor")

    def test_scale_type_repr(self):
        type = ScaleType.HarmonicMinor
        self.assertEqual(repr(type), "ScaleType.HarmonicMinor")

if __name__ == '__main__': # pragma: no cover
    unittest.main()