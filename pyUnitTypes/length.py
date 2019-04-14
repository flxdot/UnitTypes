from pyUnitTypes.basics import BaseUnit, Conversion


class Length(BaseUnit):
    """
    The Length class is the superclass of all length based unit classes. It provides the magic method to calculate
    with the different length based units.
    """

    def __init__(self, name, symbol, to_base, value, from_base=None):
        """Constructor of the Length Superclass. Please don't use this class as standalone.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base
        value
        :param value: (mandatory, float, int or subclass of pyUnitTypes.length.Length) The actual value of the class.
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from
        the base to the value of the actual class. Default: inversion of to_base
        """

        super().__init__(name=name, symbol=symbol, unit_type=Length, base_class=Meter, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Length):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))


class Meter(Length):
    """The base SI unit of lengths."""

    def __init__(self, value=float()):
        """Create instance of the meter class.

        :param value: (optional, int or float
        """

        super().__init__(name='Meter', symbol='m', to_base=Conversion(), value=value)


class CentiMeter(Length):
    """The base SI unit of lengths."""

    def __init__(self, value=float()):
        """Create instance of the meter class.

        :param value: (optional, int or float
        """

        super().__init__(name='CentiMeter', symbol='cm', to_base=Conversion(0.01), value=value)


class MilliMeter(Length):
    """The base SI unit of lengths."""

    def __init__(self, value=float()):
        """Create instance of the meter class.

        :param value: (optional, int or float
        """

        super().__init__(name='CentiMeter', symbol='cm', to_base=Conversion(0.001), value=value)
