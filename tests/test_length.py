from unittest import TestCase
from pyUnitTypes.length import KiloMeter, Meter, DeciMeter, CentiMeter, MilliMeter, MicroMeter, NanoMeter
from pyUnitTypes.temperature import Celsius


class TestLengths(TestCase):
    """Tests for length.rst module"""

    def test_constructor(self):
        """Tests the constructors of the Length class."""

        self.assertEqual(Meter(Meter(1)), Meter(1))
        self.assertEqual(CentiMeter(Meter(1)), Meter(1))
        self.assertEqual(CentiMeter(Meter(1)), CentiMeter(100))

        # TypeError
        with self.assertRaises(TypeError):
            CentiMeter('1')
        with self.assertRaises(TypeError):
            CentiMeter([1])
        with self.assertRaises(TypeError):
            CentiMeter({'value': 1})
        with self.assertRaises(TypeError):
            CentiMeter(Celsius(1))

    def test_Conversions(self):
        """Tests for Meter class."""

        # to base
        self.assertEqual(Meter(1), KiloMeter(1e-3))
        self.assertEqual(Meter(1), Meter(1))
        self.assertEqual(Meter(1), DeciMeter(1e1))
        self.assertEqual(Meter(1), CentiMeter(1e2))
        self.assertEqual(Meter(1), MilliMeter(1e3))
        self.assertEqual(Meter(1), MicroMeter(1e6))
        self.assertEqual(Meter(1), NanoMeter(1e9))

        # from base
        self.assertEqual(KiloMeter(1), Meter(1e3))
        self.assertEqual(Meter(1), Meter(1))
        self.assertEqual(DeciMeter(1), Meter(1e-1))
        self.assertEqual(CentiMeter(1), Meter(1e-2))
        self.assertEqual(MilliMeter(1), Meter(1e-3))
        self.assertEqual(MicroMeter(1), Meter(1e-6))
        self.assertEqual(NanoMeter(1), Meter(1e-9))