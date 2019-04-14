from unittest import TestCase
from pyUnitTypes.length import Meter, CentiMeter, MilliMeter


class TestLengths(TestCase):
    """Tests for length.py module"""

    def test_Meter(self):
        """Tests for Meter class."""

        self.assertEqual(Meter(1), Meter(1))

    def test_eq(self):
        """Tests the equality of the length classes."""

        self.assertTrue(Meter(1) == CentiMeter(100))
        self.assertTrue(Meter(1) == MilliMeter(1000))