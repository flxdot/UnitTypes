from unittest import TestCase
import copy
from pyUnitTypes.basics import Conversion
from pyUnitTypes.length import Meter, CentiMeter, MilliMeter


class TestBaseUnit(TestCase):
    """Tests for basics.py module. Most of the basic tests will be done with the Meter class. But the all magic methods
    are implemented in the BasicUnit class of the basics.py"""

    def test_general(self):
        """Test some general behaviour of the Length superclass"""

        self.assertEqual(Meter(-5), -Meter(5))
        self.assertEqual(Meter(-3.33), -Meter(3.33))

    def test_eq(self):
        """Tests the equality of different length classes."""

        self.assertTrue(Meter(1) == CentiMeter(100))
        self.assertTrue(Meter(1) == MilliMeter(1000))

    def test_ne(self):
        """Tests the not equality."""

        self.assertTrue(Meter(1) != Meter(2))
        self.assertTrue(Meter(1) != CentiMeter(2))

    def test_add(self):
        """Test the addition."""

        # positive values
        self.assertEqual(Meter(10) + 4.5, Meter(14.5))
        self.assertEqual(Meter(10) + 4, Meter(14))
        self.assertEqual(15.5 + Meter(10), Meter(25.5))
        self.assertEqual(15 + Meter(10), Meter(25))

        # negative values
        self.assertEqual(Meter(2) + -4.5, Meter(-2.5))
        self.assertEqual(-4.5 + Meter(2), Meter(-2.5))
        self.assertEqual(Meter(-2) + 4.5, Meter(2.5))
        self.assertEqual(4.5 + Meter(-2), Meter(2.5))
        self.assertEqual(Meter(-2) + -4.5, Meter(-6.5))
        self.assertEqual(-4.5 + Meter(-2), Meter(-6.5))

        # zeros
        self.assertEqual(Meter(0) + 4.5, Meter(4.5))
        self.assertEqual(0 + Meter(2), Meter(2))

        # unsupported Types
        with self.assertRaises(TypeError):
            a = Meter(1) + '1'
        with self.assertRaises(TypeError):
            a = Meter(1) + [1]
        with self.assertRaises(TypeError):
            a = Meter(1) + {'value': 1}

    def test_sub(self):
        """Test the subtraction."""

        # positive values
        self.assertEqual(Meter(10) - 4.5, Meter(5.5))
        self.assertEqual(Meter(10) - 4, Meter(6))
        self.assertEqual(15.5 - Meter(10), Meter(5.5))
        self.assertEqual(15 - Meter(10), Meter(5))

        # negative values
        self.assertEqual(Meter(2) - -4.5, Meter(6.5))
        self.assertEqual(-4.5 - Meter(2), Meter(-6.5))
        self.assertEqual(Meter(-2) - 4.5, Meter(-6.5))
        self.assertEqual(4.5 - Meter(-2), Meter(6.5))
        self.assertEqual(Meter(-2) - -4.5, Meter(2.5))
        self.assertEqual(-4.5 - Meter(-2), Meter(-2.5))

        # zeros
        self.assertEqual(Meter(0) - 4.5, Meter(-4.5))
        self.assertEqual(0 - Meter(2), Meter(-2))

        # unsupported Types
        with self.assertRaises(TypeError):
            a = Meter(1) - '1'
        with self.assertRaises(TypeError):
            a = Meter(1) - [1]
        with self.assertRaises(TypeError):
            a = Meter(1) - {'value': 1}

    def test_mul(self):
        """Tests the multiplication."""

        # positive values
        self.assertEqual(Meter(2) * 4.5, Meter(9))
        self.assertEqual(Meter(2) * 4, Meter(8))
        self.assertEqual(4.5 * Meter(2), Meter(9))
        self.assertEqual(4 * Meter(2), Meter(8))

        # negative values
        self.assertEqual(Meter(2) * -4.5, Meter(-9))
        self.assertEqual(-4.5 * Meter(2), Meter(-9))
        self.assertEqual(Meter(-2) * 4.5, Meter(-9))
        self.assertEqual(4.5 * Meter(-2), Meter(-9))
        self.assertEqual(Meter(-2) * -4.5, Meter(9))
        self.assertEqual(-4.5 * Meter(-2), Meter(9))

        # zeros
        self.assertEqual(Meter(0) * 4.5, Meter(0))
        self.assertEqual(0 * Meter(2), Meter(0))

        # unsupported Types
        with self.assertRaises(TypeError):
            a = Meter(1) * '1'
        with self.assertRaises(TypeError):
            a = Meter(1) * [1]
        with self.assertRaises(TypeError):
            a = Meter(1) * {'value': 1}

        # unsupported Units

    def test_div(self):
        """Test the division."""

        # divide by numbers
        self.assertEqual(Meter(21) / 3, Meter(7))
        self.assertEqual(Meter(14) / 3.5, Meter(4))
        self.assertEqual(Meter(21) / -3, Meter(-7))
        self.assertEqual(Meter(14) / -3.5, Meter(-4))
        self.assertEqual(Meter(0) / -3.5, Meter(0))
        self.assertEqual(Meter(0) / 3.5, Meter(0))

        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(Meter(21) / 0, Meter(7))


class TestConversion(TestCase):
    """Tests the Conversion class."""

    def test_convert(self):
        """Tests the convert method."""

        # both positive
        conv = Conversion(factor=2, offset=3)
        self.assertEqual(conv.convert(4), 11)
        self.assertEqual(conv.convert(4.5), 12)
        self.assertEqual(conv.convert(0), 3)
        self.assertEqual(conv.convert(-4), -5)
        self.assertEqual(conv.convert(-4.5), -6)

        # factor negative
        conv = Conversion(factor=-2, offset=3)
        self.assertEqual(conv.convert(4), -5)
        self.assertEqual(conv.convert(4.5), -6)
        self.assertEqual(conv.convert(0), 3)
        self.assertEqual(conv.convert(-4), 11)
        self.assertEqual(conv.convert(-4.5), 12)

        # offset negative
        conv = Conversion(factor=2, offset=-3)
        self.assertEqual(conv.convert(4), 5)
        self.assertEqual(conv.convert(4.5), 6)
        self.assertEqual(conv.convert(0), -3)
        self.assertEqual(conv.convert(-4), -11)
        self.assertEqual(conv.convert(-4.5), -12)

        # both negative
        conv = Conversion(factor=-2, offset=-3)
        self.assertEqual(conv.convert(4), -11)
        self.assertEqual(conv.convert(4.5), -12)
        self.assertEqual(conv.convert(0), -3)
        self.assertEqual(conv.convert(-4), 5)
        self.assertEqual(conv.convert(-4.5), 6)

        # factor 0
        conv = Conversion(factor=0, offset=3)
        self.assertEqual(conv.convert(4), 3)
        self.assertEqual(conv.convert(4.5), 3)
        self.assertEqual(conv.convert(0), 3)
        self.assertEqual(conv.convert(-4), 3)
        self.assertEqual(conv.convert(-4.5), 3)

        # offset 0
        conv = Conversion(factor=2, offset=0)
        self.assertEqual(conv.convert(4), 8)
        self.assertEqual(conv.convert(4.5), 9)
        self.assertEqual(conv.convert(0), 0)
        self.assertEqual(conv.convert(-4), -8)
        self.assertEqual(conv.convert(-4.5), -9)

        # both 0
        conv = Conversion(factor=0, offset=0)
        self.assertEqual(conv.convert(4), 0)
        self.assertEqual(conv.convert(4.5), 0)
        self.assertEqual(conv.convert(0), 0)
        self.assertEqual(conv.convert(-4), 0)
        self.assertEqual(conv.convert(-4.5), 0)

    def test_invert(self):
        """Tests the invert functionality."""

        conv = Conversion(factor=2, offset=3)
        conv_inv = copy.copy(conv).__invert__()

        self.assertEqual(conv_inv.factor, 1/conv.factor)
        self.assertEqual(conv_inv.offset, -conv.offset/conv.factor)
