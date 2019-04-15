import copy
import math
from enum import Enum


class System(Enum):
    """Enumeration to switch between unit system. The default system is the metric system."""
    METRIC = 0
    IMPERIAL = 1


class BasicTypes(Enum):
    """Enumeration of all basic unit types supported. A basic unit is length, temperature, etc. Units types like speed etc
    are ComplexTypes."""

    LENGTH = 1
    TEMPERATURE = 2
    MASS = 3
    TIME = 4


class ComplexTypes(Enum):
    """Enumeration of all supported complex unit type."""

    AREA = 1
    VOLUME = 2
    SPEED = 3
    FLOW = 4
    FORCE = 5
    WORK = 6


class UnknownUnitMultiplicationError(Exception):
    """Will be raised by BaseUnit when ever 2 units are multiplied with each other. This needs to be handled in the
    sub classes."""
    pass


class UnknownUnitDivisionError(Exception):
    """Will be raised by BaseUnit when ever 2 units are divided by each other. This needs to be handled in the
    sub classes."""
    pass


class Conversion:
    """The Conversion class defines a conversion from one value to another."""

    def __init__(self, factor=1.0, offset=0.0):
        """Creates new Conversion with given factor and offset.

        :param factor: (optional, float or int) the conversion factor. Default: 1
        :param offset: (optional, float or int) the offset of the conversion Default: 0
        """

        self.factor = factor
        self.offset = offset

    def convert(self, val):
        """Returns the converted value

        :param val: (mandatory, float or int) the numeric value that shall be converted.
        :returns float: the conversion result
        """

        return self.factor * float(val) + self.offset

    def __eq__(self, other):
        """Defines behavior for the equality operator, ==."""

        if isinstance(other, Conversion):
            return self.factor == other.factor and self.offset == other.offset
        else:
            return False

    def __ne__(self, other):
        """Defines behavior for the inequality operator, !=."""

        if isinstance(other, Conversion):
            return self.factor != other.factor or self.offset != other.offset
        else:
            return True

    def __copy__(self):
        """Defines behavior for copy.copy() for instances of your class. copy.copy() returns a shallow copy of your
        object -- this means that, while the instance itself is a new instance, all of its data is referenced
        -- i.e., the object itself is copied, but its data is still referenced (and hence changes to data in a shallow
        copy may cause changes in the original)."""

        return Conversion(factor=self.factor, offset=self.offset)

    def __deepcopy__(self, memodict={}):
        """Defines behavior for copy.deepcopy() for instances of your class. copy.deepcopy() returns a deep copy of
        your object -- the object and its data are both copied. memodict is a cache of previously copied objects
        -- this optimizes copying and prevents infinite recursion when copying recursive data structures. When you want
        to deep copy an individual attribute, call copy.deepcopy() on that attribute with memodict as the first
        argument."""

        return Conversion(factor=self.factor, offset=self.offset)

    def __invert__(self):
        """Creates the inverted conversion of this class."""

        if self.factor != 0:
            self.offset = -(self.offset / self.factor)
            self.factor = 1 / self.factor
        else:
            self.offset = -self.offset
        return self

    def __repr__(self):  # pragma: no cover
        return "Conversion(factor={0}, offset={1})".format(self.factor, self.offset)

    def __str__(self):  # pragma: no cover
        return "y = {0} * x + {1}".format(self.factor, self.factor)


class BaseUnit:
    """
    The BaseUnit class is the basic class of every Unit class of this package. It provides general magic methods.
    """

    def __init__(self, name, symbol, base_class, to_base, unit_type, from_base=None):
        """
        The default constructor of the BaseUnit class.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param base_class: (mandatory, type) class of the base class
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base value
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from the base
        to the value of the actual class. Default: inversion of to_base
        """

        # Public attributes
        self.name = name
        self.symbol = symbol

        # internal attributes
        self._value = float()
        self._type = unit_type
        self._base_value = float()
        self._base_class = base_class
        self._to_base_converter = to_base
        self.to_base = self._to_base_converter.convert
        if from_base is not None:
            self._from_base_converter = from_base
        else:
            self._from_base_converter = copy.copy(to_base).__invert__()
        self.from_base = self._from_base_converter.convert

    def __repr__(self):  # pragma: no cover
        return "{0} {1}".format(self.value, self.symbol)

    def __str__(self):  # pragma: no cover
        return "{0} {1}".format(self.value, self.symbol)

    def __pos__(self):
        """Implements behavior for unary positive (e.g. +some_object)"""

        return self

    def __neg__(self):
        """Implements behavior for negation (e.g. -some_object)"""

        self.value = -self.value
        return self

    def __eq__(self, other):
        """Defines behavior for the equality operator, ==."""

        if isinstance(other, (float, int)):
            return self.value == other
        elif issubclass(type(other), self.type):
            return self.base_value == other.base_value
        else:
            return False

    def __ne__(self, other):
        """Defines behavior for the inequality operator, !=."""

        if isinstance(other, (float, int)):
            return self.value != other
        elif issubclass(type(other), self.type):
            return self.base_value != other.base_value
        else:
            return True

    def __lt__(self, other):
        """Defines behavior for the less-than operator, <."""

        if isinstance(other, (float, int)):
            return self.value < other
        elif issubclass(type(other), self.type):
            return self.base_value < other.base_value
        else:
            if issubclass(type(other), BaseUnit):
                raise TypeError('Can not compare Unit {0} to Unit {1}'.format(self.name, type(other).__name__))
            else:
                raise TypeError(
                    'Can not compare Unit {0} to object of type {1}'.format(self.name, type(other).__name__))

    def __gt__(self, other):
        """Defines behavior for the greater-than operator, >."""

        if isinstance(other, (float, int)):
            return self.value > other
        elif issubclass(type(other), self.type):
            return self.base_value > other.base_value
        else:
            if issubclass(type(other), BaseUnit):
                raise TypeError('Can not compare Unit {0} to Unit {1}'.format(self.name, type(other).__name__))
            else:
                raise TypeError(
                    'Can not compare Unit {0} to object of type {1}'.format(self.name, type(other).__name__))

    def __le__(self, other):
        """Defines behavior for the less-than-or-equal-to operator, <=."""

        if isinstance(other, (float, int)):
            return self.value <= other
        elif issubclass(type(other), self.type):
            return self.base_value <= other.base_value
        else:
            if issubclass(type(other), BaseUnit):
                raise TypeError('Can not compare Unit {0} to Unit {1}'.format(self.name, type(other).__name__))
            else:
                raise TypeError(
                    'Can not compare Unit {0} to object of type {1}'.format(self.name, type(other).__name__))

    def __ge__(self, other):
        """Defines behavior for the greater-than-or-equal-to operator, >=."""

        if isinstance(other, (float, int)):
            return self.value >= other
        elif issubclass(type(other), self.type):
            return self.base_value >= other.base_value
        else:
            if issubclass(type(other), BaseUnit):
                raise TypeError('Can not compare Unit {0} to Unit {1}'.format(self.name, type(other).__name__))
            else:
                raise TypeError(
                    'Can not compare Unit {0} to object of type {1}'.format(self.name, type(other).__name__))

    def __abs__(self):
        """Implements behavior for the built in abs() function."""

        self.value = abs(self.value)
        return self

    def __round__(self, n=None):
        """Implements behavior for the built in round() function. n is the number of decimal places to round to."""

        if n is not None:
            self.value = round(self.value, ndigits=n)
        else:
            self.value = round(self.value)
        return self

    def __floor__(self):
        """Implements behavior for math.floor(), i.e., rounding down to the nearest integer."""

        self.value = math.floor(self.value)
        return self

    def __ceil__(self):
        """Implements behavior for math.ceil(), i.e., rounding up to the nearest integer."""

        self.value = math.ceil(self.value)
        return self

    def __float__(self):
        """Implements type conversion to float."""

        return float(self.value)

    def __int__(self):
        """Implements type conversion to int."""

        return int(self.value)

    def __nonzero__(self):
        """Defines behavior for when bool() is called on an instance of your class. Should return True or False,
        depending on whether you would want to consider the instance to be True or False."""

        return bool(self.value)

    def __bool__(self):
        """Defines behavior for when bool() is called on an instance of your class. Should return True or False,
        depending on whether you would want to consider the instance to be True or False."""

        return bool(self.value)

    def __add__(self, other):
        """Implements addition."""

        # check input
        if isinstance(other, (int, float)):
            self.value += other
            return self
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not add {0} to {1}.'.format(other._type, self._type))

            self_type = type(self)
            return self_type(self._base_value + other.base_value)
        else:
            raise TypeError('Can not add objects of type {0} to object of type {1}'.format(type(other).__name__,
                                                                                           type(self).__name__))

    def __radd__(self, other):
        """Implements reflected addition."""

        return self + other

    def __iadd__(self, other):
        """Implements addition."""

        # check input
        if isinstance(other, (int, float)):
            self.value += other
            return self
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not add {0} to {1}.'.format(other.type, self._type))

            self.value = self.from_base(self._base_value + other.base_value)
            return self
        else:
            raise TypeError('Can not add objects of type {0} to object of type {1}'.format(type(other).__name__,
                                                                                           type(self).__name__))

    def __sub__(self, other):
        """Implements subtraction."""

        # check input
        if isinstance(other, (int, float)):
            self.value -= other
            return self
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not subtract {0} from {1}.'.format(other.type, self._type))

            self_type = type(self)
            return self_type(self._base_value - other.base_value)
        else:
            raise TypeError('Can not subtract objects of type {0} from object of type {1}'.format(type(other).__name__,
                                                                                                  type(self).__name__))

    def __rsub__(self, other):
        """Implements reflected subtraction."""

        # check input
        if isinstance(other, (int, float)):
            self.value = other - self.value
            return self
        elif issubclass(type(other), BaseUnit):  # pragma: no cover
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not subtract {0} from {1}.'.format(other.type, self._type))

            self_type = type(self)
            return self_type(other.base_value - self._base_value)
        else:
            raise TypeError('Can not subtract objects of type {0} from object of type {1}'.format(type(other).__name__,
                                                                                                  type(self).__name__))

    def __isub__(self, other):
        """Implements subtraction."""

        # check input
        if isinstance(other, (int, float)):
            self.value -= other
            return self
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not subtract {0} from {1}.'.format(other.type, self._type))

            self.value = self.from_base(self._base_value - other.base_value)
            return self
        else:
            raise TypeError('Can not subtract objects of type {0} from object of type {1}'.format(type(other).__name__,
                                                                                                  type(self).__name__))

    def __mul__(self, other):
        """Implements multiplication."""

        if isinstance(other, (float, int)):
            self.value *= other
            return self
        elif issubclass(type(other), BaseUnit):
            raise UnknownUnitMultiplicationError('So far the multiplication of {0} by {1} is unknown.', self.name,
                                                 other.name)
        else:
            raise TypeError(
                'Can not multiply Unit {0} with object of type {1}'.format(self.name, type(other).__name__))

    def __rmul__(self, other):
        """Implements reflected multiplication."""

        return self * other

    def __imul__(self, other):
        """Implements multiplication."""

        if isinstance(other, (float, int)):
            self.value *= other
            return self
        elif issubclass(type(other), BaseUnit):
            raise UnknownUnitMultiplicationError('So far the multiplication of {0} by {1} is unknown.', self.name,
                                                 other.name)
        else:
            raise TypeError(
                'Can not multiply Unit {0} with object of type {1}'.format(self.name, type(other).__name__))

    def __div__(self, other):
        """Implements division using the / operator."""

        if isinstance(other, (float, int)):
            self.value /= other
            return self
        elif issubclass(type(other), BaseUnit):
            raise UnknownUnitDivisionError('So far the division of {0} by {1} is unknown.', self.name,
                                           other.name)
        else:
            raise TypeError(
                'Can not divide Unit {0} by object of type {1}'.format(self.name, type(other).__name__))

    def __truediv__(self, other):
        """Implements true division. Note that this only works when from __future__ import division is in effect."""

        return self.__div__(other)

    def __rdiv__(self, other):
        """Implements reflected division using the / operator."""

        raise UnknownUnitDivisionError('No method to divide by unit {0} has been implemented.'.format(self.name))

    def __rtruediv__(self, other):
        """Implements reflected true division. Note that this only works when from __future__ import division is in
        effect."""

        return self.__rdiv__(other)

    def __idiv__(self, other):
        """Implements division using the / operator."""

        if isinstance(other, (float, int)):
            self.value /= other
            return self
        elif issubclass(type(other), BaseUnit):
            raise UnknownUnitDivisionError('So far the division of {0} by {1} is unknown.', self.name,
                                           other.name)
        else:
            raise TypeError(
                'Can not divide Unit {0} by object of type {1}'.format(self.name, type(other).__name__))

    def __itruediv__(self, other):
        """Implements true division with assignment. Note that this only works when from __future__ import division is
        in effect."""

        return self.__idiv__(other)

    @property
    def value(self):
        # return the private attribute
        return self._value

    @value.setter
    def value(self, new_value):
        # store the value
        self._value = float(new_value)
        # convert the value into the base class
        self._base_value = self.to_base(self._value)

    @property
    def base_value(self):
        return self._base_value

    @property
    def type(self):
        return self._type
