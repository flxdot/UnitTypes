from unittest import TestCase
from pyUnitTypes.length import Meter, CentiMeter, MilliMeter


class TestLengths(TestCase):
    """Tests for length.py module"""

    def test_constructor(self):
        """Tests the constructors of the Length class."""

        self.assertEqual(Meter(Meter(1)), Meter(1))
        self.assertEqual(CentiMeter(Meter(1)), Meter(1))
        self.assertEqual(CentiMeter(Meter(1)), CentiMeter(100))

        with self.assertRaises(TypeError):
            CentiMeter('1')
        with self.assertRaises(TypeError):
            CentiMeter([1])
        with self.assertRaises(TypeError):
            CentiMeter({'value': 1})

    def test_Conversions(self):
        """Tests for Meter class."""

        self.assertEqual(Meter(1), Meter(1))
        self.assertEqual(Meter(1), CentiMeter(100))
        self.assertEqual(Meter(1), MilliMeter(1000))