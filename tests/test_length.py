from unittest import TestCase
from pyUnitTypes.length import Meter, CentiMeter, MilliMeter


class TestLengths(TestCase):
    """Tests for length.py module"""

    def test_Conversions(self):
        """Tests for Meter class."""

        self.assertEqual(Meter(1), Meter(1))
        self.assertEqual(Meter(1), CentiMeter(100))
        self.assertEqual(Meter(1), MilliMeter(1000))