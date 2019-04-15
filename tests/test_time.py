from unittest import TestCase

from pyUnitTypes.length import Meter
from pyUnitTypes.time import Year, Week, Day, Hour, Minute, Second, MilliSecond, MicroSecond


class TestTimes(TestCase):
    """Tests for time.py module"""

    def test_constructor(self):
        """Tests the constructors of the Length class."""

        self.assertEqual(Day(Day(1)), Day(1))
        self.assertEqual(Hour(Day(1)), Day(1))
        self.assertEqual(Hour(Day(1)), Hour(24))

        # TypeError
        with self.assertRaises(TypeError):
            Day('1')
        with self.assertRaises(TypeError):
            Day([1])
        with self.assertRaises(TypeError):
            Day({'value': 1})
        with self.assertRaises(TypeError):
            Day(Meter(1))

    def test_Conversions(self):
        """Tests for Meter class."""

        # to base
        self.assertEqual(Day(1), Year(1 / 365.25))
        self.assertEqual(Day(1), Week(1 / 7))
        self.assertEqual(Day(1), Day(1))
        self.assertEqual(Day(1), Hour(24))
        self.assertEqual(Day(1), Minute(1440))
        self.assertEqual(Day(1), Second(86400))
        self.assertEqual(Second(1), MilliSecond(1000))
        self.assertEqual(MilliSecond(1), MicroSecond(1000))
