from unittest import TestCase

from pyUnitTypes.temperature import Kelvin, Celsius, Fahrenheit


class TestTemperature(TestCase):
    """Tests the Temperature module."""

    def test_constructor(self):
        """Tests the constructors of the Length class."""

        self.assertEqual(Celsius(Celsius(1)), Celsius(1))
        self.assertEqual(Kelvin(Celsius(1)), Celsius(1))
        self.assertEqual(Kelvin(Celsius(1)), Kelvin(274.15))

        with self.assertRaises(TypeError):
            Celsius('1')
        with self.assertRaises(TypeError):
            Celsius([1])
        with self.assertRaises(TypeError):
            Celsius({'value': 1})

    def test_Conversions(self):
        """Tests for Meter class."""

        prec = 4

        # positive values
        self.assertAlmostEqual(Celsius(100), Celsius(100), places=prec)
        self.assertAlmostEqual(Fahrenheit(100), Fahrenheit(100), places=prec)
        self.assertAlmostEqual(Kelvin(100), Kelvin(100), places=prec)
        self.assertAlmostEqual(Celsius(100), Kelvin(373.15), places=prec)
        self.assertAlmostEqual(Celsius(101), Fahrenheit(213.8), places=prec)
        self.assertAlmostEqual(Kelvin(100), Celsius(-173.15), places=prec)
        self.assertAlmostEqual(Kelvin(100), Fahrenheit(-279.67), places=prec)
        self.assertAlmostEqual(Fahrenheit(100), Celsius(37.77778), places=prec)
        self.assertAlmostEqual(Fahrenheit(100), Kelvin(310.9278), places=prec)
