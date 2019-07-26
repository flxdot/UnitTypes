from pyUnitTypes.basics import BaseUnit, Conversion


class Luminous(BaseUnit):
    """
    The Luminous class is the superclass of all Luminous based unit classes. It provides the magic method to calculate
    with the different length based units.
    """

    def __init__(self, name, symbol, to_base, value, from_base=None):
        """Constructor of the Luminous Superclass. Please don't use this class as standalone.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base
        value
        :param value: (mandatory, float, int or subclass of pyUnitTypes subclass) The actual value of the class.
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from
        the base to the value of the actual class. Default: inversion of to_base
        """

        super().__init__(name=name, symbol=symbol, unit_type=Luminous, base_class=Candela, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Luminous):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))


class Candela(Luminous):
    """A Candela. You know. The luminous intensity, in a given direction, 
    of a source that emits monochromatic radiation of frequency 540 × 1012 hertz 
    and that has a radiant intensity in that direction of 1/683 watts per steridian."""

    def __init__(self, value=float()):
        """Create instance of the Candela class.

        :param value: (optional, int or float) the amount of Candela
        """

        super().__init__(name='Candela', symbol='cd', to_base=Conversion(), value=value)