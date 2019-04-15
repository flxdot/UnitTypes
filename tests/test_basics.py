from unittest import TestCase
import copy
import math
from pyUnitTypes.basics import BaseUnit, Conversion
from pyUnitTypes.length import Meter, CentiMeter, MilliMeter
from pyUnitTypes.temperature import Celsius


class TestBaseUnit(TestCase):
    """Tests for basics.py module. Most of the basic tests will be done with the Meter class. But the all magic methods
    are implemented in the BasicUnit class of the basics.py"""

    def test_general(self):
        """Test some general behaviour of the Length superclass"""

        one_meter = Meter(1)

        # __pos__
        self.assertEqual(Meter(5), +Meter(5))

        # __neg__
        self.assertEqual(Meter(-5), -Meter(5))
        self.assertEqual(Meter(-3.33), -Meter(3.33))

        # __copy__
        self.assertEqual(one_meter, copy.deepcopy(one_meter))

        # __deepcopy__
        self.assertEqual(one_meter, copy.copy(one_meter))

    def test_type_conversions(self):
        """Tests the conversion of types."""

        # __int__
        self.assertEqual(int(Meter(1.0)), 1)
        self.assertEqual(int(Meter(1)), 1)
        self.assertEqual(int(Meter(-1.0)), -1)
        self.assertEqual(int(Meter(-1)), -1)
        self.assertEqual(int(Meter(0)), 0)
        self.assertEqual(int(Meter(0.0)), 0)

        # __float__
        self.assertEqual(float(Meter(1.0)), 1.0)
        self.assertEqual(float(Meter(1)), 1.0)
        self.assertEqual(float(Meter(-1.0)), -1.0)
        self.assertEqual(float(Meter(-1)), -1.0)
        self.assertEqual(float(Meter(0)), 0.0)
        self.assertEqual(float(Meter(0.0)), 0.0)

        # __nonzero__
        self.assertTrue(bool(Meter(1)))
        self.assertTrue(bool(Meter(-1)))
        self.assertFalse(bool(Meter(0)))

    def test_eq(self):
        """Tests the equality of different length classes."""

        one_meter = Meter(1)
        self.assertTrue(one_meter == Meter(1))
        self.assertTrue(one_meter == 1)
        self.assertTrue(one_meter == 1.0)
        self.assertFalse(one_meter == Meter(2))
        self.assertFalse(one_meter == CentiMeter(1))
        self.assertFalse(one_meter == [1])

    def test_ne(self):
        """Tests the not equality."""

        one_meter = Meter(1)
        self.assertFalse(one_meter != Meter(1))
        self.assertFalse(one_meter != 1)
        self.assertFalse(one_meter != 1.0)
        self.assertTrue(one_meter != Meter(2))
        self.assertTrue(one_meter != CentiMeter(1))
        self.assertTrue(one_meter != [1])

    def test_comparison(self):
        """Test the <, >, <= and >= operators."""

        # __lt__
        self.assertLess(Meter(1), Meter(2))
        self.assertLess(Meter(1), CentiMeter(101))
        self.assertLess(Meter(1), 2)
        self.assertLess(Meter(0), 1)
        self.assertLess(Meter(-1), 1)
        with self.assertRaises(TypeError):
            a = Meter(1) < [1]
        with self.assertRaises(TypeError):
            a = Meter(1) < Celsius(1)

        # __gt__
        self.assertGreater(Meter(1), Meter(0.5))
        self.assertGreater(Meter(1), CentiMeter(1))
        self.assertGreater(Meter(1), 0.5)
        self.assertGreater(Meter(1), 0)
        self.assertGreater(Meter(1), -1)
        with self.assertRaises(TypeError):
            a = Meter(1) > [1]
        with self.assertRaises(TypeError):
            a = Meter(1) > Celsius(1)

        # __le__
        self.assertLessEqual(Meter(1), Meter(2))
        self.assertLessEqual(Meter(1), Meter(1))
        self.assertLessEqual(Meter(1), CentiMeter(101))
        self.assertLessEqual(Meter(1), CentiMeter(100))
        self.assertLessEqual(Meter(1), 2)
        self.assertLessEqual(Meter(1), 1)
        self.assertLessEqual(Meter(0), 1)
        self.assertLessEqual(Meter(0), 0)
        self.assertLessEqual(Meter(-1), 1)
        self.assertLessEqual(Meter(-1), -1)
        with self.assertRaises(TypeError):
            a = Meter(1) <= [1]
        with self.assertRaises(TypeError):
            a = Meter(1) <= Celsius(1)

        # __ge__
        self.assertGreaterEqual(Meter(1), Meter(0.5))
        self.assertGreaterEqual(Meter(1), Meter(1))
        self.assertGreaterEqual(Meter(1), CentiMeter(1))
        self.assertGreaterEqual(Meter(1), CentiMeter(100))
        self.assertGreaterEqual(Meter(1), 0.5)
        self.assertGreaterEqual(Meter(1), 1)
        self.assertGreaterEqual(Meter(1), 0)
        self.assertGreaterEqual(Meter(0), 0)
        self.assertGreaterEqual(Meter(-1), -1)
        self.assertGreaterEqual(Meter(1), -1)
        with self.assertRaises(TypeError):
            a = Meter(1) >= [1]
        with self.assertRaises(TypeError):
            a = Meter(1) >= Celsius(1)

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

        # other unit of the same unit base type
        meter = Meter(0)
        self.assertEqual(Meter(1) + CentiMeter(100), 2)
        self.assertEqual(2, Meter(1) + CentiMeter(100))

        # __iadd__
        meter += 1
        self.assertEqual(meter, 1)
        meter += 0
        self.assertEqual(meter, 1)
        meter += CentiMeter(100)
        self.assertEqual(meter, 2)

        # unsupported Types
        with self.assertRaises(TypeError):
            a = Meter(1) + Celsius(1)
        with self.assertRaises(TypeError):
            meter += Celsius(1)
        with self.assertRaises(TypeError):
            a = '1' + Meter(1)
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

        # other unit of the same unit base type
        meter = Meter(0)
        self.assertEqual(Meter(1) - CentiMeter(100), 0)
        self.assertEqual(0, Meter(1) - CentiMeter(100))

        # __isub__
        meter -= 1
        self.assertEqual(meter, -1)
        meter -= 0
        self.assertEqual(meter, -1)
        meter -= CentiMeter(100)
        self.assertEqual(meter, -2)

        # unsupported Types
        with self.assertRaises(TypeError):
            a = Meter(1) - Celsius(1)
        with self.assertRaises(TypeError):
            meter -= Celsius(1)
        with self.assertRaises(TypeError):
            a = '1' - Meter(1)
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

    def test_round(self):
        """Tests the round(), math.floor() and math.ceil() functionality."""

        # __round__
        self.assertEqual(Meter(1), round(Meter(1.3)))
        self.assertEqual(Meter(2), round(Meter(1.5)))
        self.assertEqual(Meter(2), round(Meter(1.6)))
        self.assertEqual(Meter(-1), round(Meter(-1.3)))
        self.assertEqual(Meter(-2), round(Meter(-1.5)))
        self.assertEqual(Meter(-2), round(Meter(-1.6)))

        # __floor__
        self.assertEqual(Meter(1), math.floor(Meter(1.3)))
        self.assertEqual(Meter(1), math.floor(Meter(1.5)))
        self.assertEqual(Meter(1), math.floor(Meter(1.6)))
        self.assertEqual(Meter(-2), math.floor(Meter(-1.3)))
        self.assertEqual(Meter(-2), math.floor(Meter(-1.5)))
        self.assertEqual(Meter(-2), math.floor(Meter(-1.6)))

        # __ceil__
        self.assertEqual(Meter(2), math.ceil(Meter(1.3)))
        self.assertEqual(Meter(2), math.ceil(Meter(1.5)))
        self.assertEqual(Meter(2), math.ceil(Meter(1.6)))
        self.assertEqual(Meter(-1), math.ceil(Meter(-1.3)))
        self.assertEqual(Meter(-1), math.ceil(Meter(-1.5)))
        self.assertEqual(Meter(-1), math.ceil(Meter(-1.6)))


class TestConversion(TestCase):
    """Tests the Conversion class."""

    def test_general(self):
        """Test some general behaviour of the Length superclass"""

        conv = Conversion(factor=2, offset=3)

        # __eq__
        self.assertTrue(conv == Conversion(factor=2, offset=3))
        self.assertFalse(conv == Conversion(factor=1, offset=3))
        self.assertFalse(conv == Conversion(factor=2, offset=2))
        self.assertFalse(conv == 1)

        # __ne__
        self.assertFalse(conv != Conversion(factor=2, offset=3))
        self.assertTrue(conv != Conversion(factor=1, offset=3))
        self.assertTrue(conv != Conversion(factor=2, offset=2))
        self.assertTrue(conv != 1)

        # __copy__
        self.assertEqual(conv, copy.deepcopy(conv))

        # __deeepcopy__
        self.assertEqual(conv, copy.copy(conv))

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

        # non zero
        conv = Conversion(factor=2, offset=3)
        conv_inv = copy.copy(conv).__invert__()

        self.assertEqual(conv_inv.factor, 1/conv.factor)
        self.assertEqual(conv_inv.offset, -conv.offset/conv.factor)

        # zero factpr
        conv = Conversion(factor=0, offset=1)
        conv_inv = copy.copy(conv).__invert__()

        self.assertEqual(conv_inv.factor, 0)
        self.assertEqual(conv_inv.offset, -conv.offset)

        # zero offset
        conv = Conversion(factor=2, offset=0)
        conv_inv = copy.copy(conv).__invert__()

        self.assertEqual(conv_inv.factor, 1/conv.factor)
        self.assertEqual(conv_inv.offset, 0)

