from pyUnitTypes.basics import BaseUnit, Conversion, SI_PREFIXES
from pyUnitTypes.auxiliary import class_factory


class Current(BaseUnit):
    """
    The Current class is the superclass of all Current based unit classes. It provides the magic method to calculate
    with the different length based units.
    """

    def __init__(self, name, symbol, to_base, value, from_base=None):
        """Constructor of the Current Superclass. Please don't use this class as standalone.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base
        value
        :param value: (mandatory, float, int or subclass of pyUnitTypes subclass) The actual value of the class.
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from
        the base to the value of the actual class. Default: inversion of to_base
        """

        super().__init__(name=name, symbol=symbol, unit_type=Current, base_class=Ampere, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Current):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))


class Ampere(Current):
    """A Ampere. You know. The constant current which, 
    if maintained in two straight parallel conductors of infinite length, 
    of negligible circular cross-section, and placed one metre apart in a vacuum, 
    would produce between these conductors a force equal to 2 x 10-7 newton per metre of length"""

    def __init__(self, value=float()):
        """Create instance of the Ampere class.

        :param value: (optional, int or float) the amount of ampere
        """

        super().__init__(name='Ampere', symbol='A', to_base=Conversion(), value=value)


# define all SI derives of lengths
for name, symbol, base10 in SI_PREFIXES:
    class_name = '{}Ampere'.format(name)

    # generate the new class
    generatedClass = class_factory(BaseClass=Current, name='{}A'.format(symbol), symbol=symbol,
                                   to_base=Conversion(base10))
    # register the class to the module
    globals()[generatedClass.__name__] = generatedClass
    # get rid of the temporary stuff
    del generatedClass
