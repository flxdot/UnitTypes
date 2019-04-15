from unittest import TestCase
from pyUnitTypes.mass import KiloGram, Gram, MicroGram, MilliGram, Pound, Ton, Tonne, ShortTon, Ounce
from pyUnitTypes.length import Meter


class TestTimes(TestCase):
    """Tests for time.py module"""

    def test_constructor(self):
        """Tests the constructors of the Length class."""

        self.assertEqual(KiloGram(KiloGram(1)), KiloGram(1))
        self.assertEqual(Gram(KiloGram(1)), KiloGram(1))
        self.assertEqual(KiloGram(Gram(1)), Gram(1))

        # TypeError
        with self.assertRaises(TypeError):
            KiloGram('1')
        with self.assertRaises(TypeError):
            KiloGram([1])
        with self.assertRaises(TypeError):
            KiloGram({'value': 1})
        with self.assertRaises(TypeError):
            KiloGram(Meter(1))

    def test_Conversions(self):
        """Tests for Meter class."""

        prec = 5

        # to base
        self.assertEqual(KiloGram(1000), Tonne(1))
        self.assertEqual(Gram(1000), KiloGram(1))
        self.assertEqual(MilliGram(1000), Gram(1))
        self.assertAlmostEqual(MicroGram(1000), MilliGram(1), places=prec)
        self.assertAlmostEqual(KiloGram(1), Pound(2.204623), places=prec)
        self.assertAlmostEqual(Pound(2240), Ton(1), places=3)
        self.assertAlmostEqual(Pound(2000), ShortTon(1), places=4)
        self.assertAlmostEqual(Pound(1), Ounce(16), places=prec)
