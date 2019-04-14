from enum import Enum
import abc
import math


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

    def __invert__(self):
        """Creates the inverted conversion of this class."""

        self.offset = -(self.offset / self.factor)
        self.factor = 1 / self.factor
        return self

    def __repr__(self):
        return "Conversion(factor={0}, offset={1})".format(self.factor, self.offset)


class BaseUnit:
    """
    The BaseUnit class is the basic class of every Unit class of this package. It provides general magic methods.
    """

    __metaclass__ = abc.ABCMeta

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
        self._to_base = to_base
        if from_base is not None:
            self._from_base = from_base
        else:
            self._from_base = not to_base

    def __repr__(self):
        return "{0} {1}".format(self.value, self.symbol)

    def __str__(self):
        return "{0} {1}".format(self.value, self.symbol)

    def __pos__(self):
        """Implements behavior for unary positive (e.g. +some_object)"""

        return self

    def __neg__(self):
        """Implements behavior for negation (e.g. -some_object)"""

        self.value = -self.value
        return self

    def __abs__(self):
        """Implements behavior for the built in abs() function."""

        self.value = abs(self.value)
        return self

    def __round__(self, n=None):
        """Implements behavior for the built in round() function. n is the number of decimal places to round to."""

        self.value = round(self.value, ndigits=n)
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

    def __sub__(self, other):
        """Implements subtraction."""

        # check input
        if isinstance(other, (int, float)):
            self.value -= other
            return self
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not subtract {0} from {1}.'.format(other._type, self._type))

            self_type = type(self)
            return self_type(self._base_value - other.base_value)
        else:
            raise TypeError('Can not subtract objects of type {0} from object of type {1}'.format(type(other).__name__,
                                                                                                  type(self).__name__))

    def __iadd__(self, other):
        """Implements addition."""

        # check input
        if isinstance(other, (int, float)):
            self.value += other
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not add {0} to {1}.'.format(other.type, self._type))

            self.value = self._from_base.convert(self._base_value + other.base_value)
        else:
            raise TypeError('Can not add objects of type {0} to object of type {1}'.format(type(other).__name__,
                                                                                           type(self).__name__))

    def __isub__(self, other):
        """Implements subtraction."""

        # check input
        if isinstance(other, (int, float)):
            self.value -= other
        elif issubclass(type(other), BaseUnit):
            # check if both operands are of the same unit type, because can not add meters to degrees celsius
            if self._type != other.type:
                raise TypeError('Can not subtract {0} from {1}.'.format(other.type, self._type))

            self.value = self._from_base.convert(self._base_value - other.base_value)
        else:
            raise TypeError('Can not subtract objects of type {0} from object of type {1}'.format(type(other).__name__,
                                                                                                  type(self).__name__))

    @property
    def value(self):
        # return the private attribute
        return self._value

    @value.setter
    def value(self, new_value):
        # store the value
        self._value = float(new_value)
        # convert the value into the base class
        self._base_value = self._to_base.convert(self._value)

    @property
    def base_value(self):
        return self._base_value

    @property
    def type(self):
        return self._type

    @abc.abstractmethod
    def __mul__(self, other):
        """Implements multiplication."""
        return

    @abc.abstractmethod
    def __div__(self, other):
        """Implements division using the / operator."""
        return

    @abc.abstractmethod
    def __imul__(self, other):
        """Implements multiplication."""
        return

    @abc.abstractmethod
    def __idiv__(self, other):
        """Implements division using the / operator."""
        return
