Creating your own UnitTypes
===========================

It is possible to build your own units based on the provided classes. If you want to extend a existing Base or Composite
Unit you'll have to inherit the  in your custom class

Extending a existing Unit type
------------------------------

Let's supose we want to create a custom length based unit ``Marathon``. As you might know a Marathon is 42 km.

To get started let's create a new module ``my-custom-units.py``.

.. code-block:: python

  from pyUnitTypes.basics import Conversion
  from pyUnitTypes.length import Length

  class Marathon(Length):
    """Nice."""

    def __init__(self, value=float()):
        """Create instance of the marathon class.

        :param value: (optional, int or float
        """

        super().__init__(name='Marathon', symbol='Marathon', to_base=Conversion(factor=42000, offset=0), value=value)

Quite simple right? See the documentation of ``pyUnitTypes.length.Length`` and  ``pyUnitTypes.basics.BaseUnit`` to
understand the parameter used in the superclass constructor.

Creating your own Unit type
---------------------------

But what if we want to create a new base unit, because length, time, temperature is to boring for you.

So you have a lot of pets and you want to figure our old each of your pets is in human years? No problem.

First let's create a new module ``age.py`` with our super class of the unit type age:

.. code-block:: python

  from pyUnitTypes.basics import BaseUnit, Conversion

  class Age(BaseUnit):
    """
    The Age class is the superclass of all age based unit classes. It provides the magic method to calculate
    with the different length based units.
    """

    def __init__(self, name, symbol, to_base, value, from_base=None):
        """Constructor of the Age Superclass. Please don't use this class as standalone.

        :param name: (mandatory, string) name of the unit as word
        :param symbol: (mandatory, string) symbol of the unit
        :param to_base: (mandatory, pyUnitTypes.basics.Conversion) conversion object to convert the value to the base
        value
        :param value: (mandatory, float, int or subclass of pyUnitTypes.length.Length) The actual value of the class.
        :param from_base: (optional, pyUnitTypes.basics.Conversion) conversion object to convert the value back from
        the base to the value of the actual class. Default: inversion of to_base
        """

        super().__init__(name=name, symbol=symbol, unit_type=Age, base_class=HumanYear, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Age):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))

Note how we set the unit_type, and base_class attribute. And how we allowed a conversion from different Age subclasses.

Now let's add some Units:

.. code-block:: python

  class HumanYear(Length):
    """The BaseClass of the age.py module"""

    def __init__(self, value=float()):
        """Create instance of the Age class.

        :param value: (optional, int or float
        """

        super().__init__(name='HumanYear', symbol='Human Year(s)', to_base=Conversion(), value=value)

  class DogYear(Length):
    """A dog year is generally know as 7 human years."""

    def __init__(self, value=float()):
        """Create instance of the DogYear class.

        :param value: (optional, int or float
        """

        super().__init__(name='DogYear', symbol='Dog Year(s)', to_base=Conversion(factor=7), value=value)

  class CatYear(Length):
    """Funny enough a cat year is also supposed to be 7 human years."""

    def __init__(self, value=float()):
        """Create instance of the DogYear class.

        :param value: (optional, int or float
        """

        super().__init__(name='CatYear', symbol='Cat Year(s)', to_base=Conversion(factor=7), value=value)

That wasn't to hard right? So hold old is your 3.5 year old dog and your 4 year old cat? Let's assume your 24 ;-).

.. code-block:: python

  from age import HumanYear, DogYear, CatYear

  # define the ages
  my_age = HumanYear(24)
  cat_age = CatYear(4)
  dog_age = DogYear(3.5)

  # check who's older
  cat_is_older = cat_age > my_age
  dog_is_older = dog_age > my_age

  if cat_is_older and dog_is_older:
    print('It seems like your the youngest among your furry friends.')
  else:
    if cat_is_older:
      print('Your cat is older. But at least your dog younger.')
    elif dog_is_older:
       print('Your dog is older. But at least your cat is younger.')
    else:
       print('Damn your an old fart.')


