from pyUnitTypes.basics import BaseUnit, Conversion, SI_PREFIXES
from pyUnitTypes.auxiliary import class_factory


class Mass(BaseUnit):
    """
    The Mass class is the superclass of all time mass unit classes. It provides the magic method to calculate
    with the different length based units.
    """

    def __init__(self, name, symbol, to_base, value, from_base=None):
        """Constructor of the Time Superclass. Please don't use this class as standalone.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base
        value
        :param value: (mandatory, float, int or subclass of pyUnitTypes.length.Length) The actual value of the class.
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from
        the base to the value of the actual class. Default: inversion of to_base
        """

        super().__init__(name=name, symbol=symbol, unit_type=Mass, base_class=KiloGram, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Mass):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))


class Tonne(Mass):
    """A bunch of those and you'll have yo' momas weight."""

    def __init__(self, value=float()):
        """Create instance of the Tonne class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='Tonne', symbol='t', to_base=Conversion(1e3), value=value)


class KiloGram(Mass):
    """A bunch of those and you'll have your weight."""

    def __init__(self, value=float()):
        """Create instance of the KiloGram class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='KiloGram', symbol='kg', to_base=Conversion(), value=value)


class Gram(Mass):
    """If your into techno you might have bought a bunch of those.."""

    def __init__(self, value=float()):
        """Create instance of the Gram class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='KiloGram', symbol='g', to_base=Conversion(1e-3), value=value)


class Pound(Mass):
    """Not the english currency."""

    def __init__(self, value=float()):
        """Create instance of the Tonne class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='Pound', symbol='lbs', to_base=Conversion(0.45359237), value=value)


class Ounce(Mass):
    """Not the english currency."""

    def __init__(self, value=float()):
        """Create instance of the Tonne class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='Ounce', symbol='oz', to_base=Conversion(0.02834952), value=value)


class Ton(Mass):
    """Yeah... of course the british hat to create their own ton. It's 2000lbs"""

    def __init__(self, value=float()):
        """Create instance of the Ton class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='Ton', symbol='ton (UK)', to_base=Conversion(1016.047), value=value)


class ShortTon(Mass):
    """And the us also..."""

    def __init__(self, value=float()):
        """Create instance of the ShortTon class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='ShortTon', symbol='ton (US)', to_base=Conversion(907.1847), value=value)


# define all SI derives of lengths
for name, symbol, base10 in SI_PREFIXES:
    if name == 'Kilo':
        continue
    class_name = '{}Meter'.format(name)

    # account for the fact that kilogram is the base unit of the mass
    base10 /= 1e3

    # generate the new class
    generatedClass = class_factory(BaseClass=Mass, name=class_name, symbol=symbol, to_base=Conversion(base10))
    # register the class to the module
    globals()[generatedClass.__name__] = generatedClass
    # get rid of the temporary stuff
    del generatedClass
