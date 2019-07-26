from unittest import TestCase

from pyUnitTypes.length import *
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

        prec = 4

        # to base
        self.assertEqual(Meter(1), KiloMeter(1e-3))
        self.assertEqual(Meter(1), Meter(1))
        self.assertEqual(Meter(1), DeciMeter(1e1))
        self.assertEqual(Meter(1), CentiMeter(1e2))
        self.assertEqual(Meter(1), MilliMeter(1e3))
        self.assertEqual(Meter(1), MicroMeter(1e6))
        self.assertEqual(Meter(1), NanoMeter(1e9))
        self.assertAlmostEqual(KiloMeter(1), Mile(0.62137121212), prec)
        self.assertAlmostEqual(Meter(1), Yard(1.093613), prec)
        self.assertAlmostEqual(Meter(1), Feet(3.28084), prec)
        self.assertAlmostEqual(MilliMeter(1), Inch(0.03937008), prec)

        # from base
        self.assertEqual(KiloMeter(1), Meter(1e3))
        self.assertEqual(Meter(1), Meter(1))
        self.assertEqual(DeciMeter(1), Meter(1e-1))
        self.assertEqual(CentiMeter(1), Meter(1e-2))
        self.assertEqual(MilliMeter(1), Meter(1e-3))
        self.assertEqual(MicroMeter(1), Meter(1e-6))
        self.assertEqual(NanoMeter(1), Meter(1e-9))
        self.assertAlmostEqual(Mile(1), KiloMeter(1.609344), prec)
        self.assertAlmostEqual(Yard(1), Meter(0.9144), prec)
        self.assertAlmostEqual(Feet(1), Meter(0.3048), prec)
        self.assertAlmostEqual(Inch(1), MilliMeter(25.4), prec)
