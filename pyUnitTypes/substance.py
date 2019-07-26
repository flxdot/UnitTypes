from pyUnitTypes.basics import BaseUnit, Conversion, SI_PREFIXES
from pyUnitTypes.auxiliary import class_factory


class Substance(BaseUnit):
    """
    The Substance class is the superclass of all Substance based unit classes. It provides the magic method to calculate
    with the different length based units.
    """

    def __init__(self, name, symbol, to_base, value, from_base=None):
        """Constructor of the Substance Superclass. Please don't use this class as standalone.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base
        value
        :param value: (mandatory, float, int or subclass of pyUnitTypes.length.Length) The actual value of the class.
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from
        the base to the value of the actual class. Default: inversion of to_base
        """

        super().__init__(name=name, symbol=symbol, unit_type=Substance, base_class=Mole, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Substance):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))


class Mole(Substance):
    """A Mole. You know. The amount of substance of a system which contains 
    as many elementary entities as there are atoms in 0.012 kilogram of carbon 12 
    (elementary entities, which must be specified, may be atoms, molecules, ions, 
    electrons, other particles or specified groups of such particles)."""

    def __init__(self, value=float()):
        """Create instance of the Mole class.

        :param value: (optional, int or float) the amount of Moles
        """

        super().__init__(name='Mole', symbol='mol', to_base=Conversion(), value=value)


for name, symbol, base10 in SI_PREFIXES:
    class_name = '{}Mole'.format(name)

    # generate the new class
    generatedClass = class_factory(BaseClass=Substance, name='{}mol'.format(symbol), symbol=symbol,
                                   to_base=Conversion(base10))
    # register the class to the module
    globals()[generatedClass.__name__] = generatedClass
    # get rid of the temporary stuff
    del generatedClass
