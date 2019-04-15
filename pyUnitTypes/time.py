from pyUnitTypes.basics import BaseUnit, Conversion


class Time(BaseUnit):
    """
    The Time class is the superclass of all time based unit classes. It provides the magic method to calculate
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

        super().__init__(name=name, symbol=symbol, unit_type=Time, base_class=Day, to_base=to_base,
                         from_base=from_base)

        # store the value and calculate the value in the base class
        if isinstance(value, (float, int)):
            self.value = value
        elif issubclass(type(value), Time):
            self.value = self.from_base(value.base_value)
        else:
            raise TypeError('Can not create object of type {0} from object of type {1}'.format(type(self).__name__,
                                                                                               type(value).__name__))


class Day(Time):
    """A day. You know. / of those and you'll have a week."""

    def __init__(self, value=float()):
        """Create instance of the Day class.

        :param value: (optional, int or float) the amount of days
        """

        super().__init__(name='Day', symbol='d', to_base=Conversion(), value=value)


class Week(Time):
    """A week 7 days of endless repeating."""

    def __init__(self, value=float()):
        """Create instance of the Week class.

        :param value: (optional, int or float) the amount of weeks
        """

        super().__init__(name='Week', symbol='w', to_base=Conversion(7), value=value)


class Year(Time):
    """365.25 days or almost 52 weeks."""

    def __init__(self, value=float()):
        """Create instance of the Year class.

        :param value: (optional, int or float) the amount of years
        """

        super().__init__(name='Year', symbol='y', to_base=Conversion(365.25), value=value)


class Hour(Time):
    """24 of then and you'll have your self a good ol' day."""

    def __init__(self, value=float()):
        """Create instance of the Hour class.

        :param value: (optional, int or float) the amount of years
        """

        super().__init__(name='Hour', symbol='h', to_base=Conversion(1 / 24), value=value)


class Minute(Time):
    """60 Minutes... like that movie with nicolas cage."""

    def __init__(self, value=float()):
        """Create instance of the Minute class.

        :param value: (optional, int or float) the amount of years
        """

        super().__init__(name='Minute', symbol='min', to_base=Conversion(1 / 1440), value=value)


class Second(Time):
    """A second that thing that passes so fast, but then not really."""

    def __init__(self, value=float()):
        """Create instance of the Seconds class.

        :param value: (optional, int or float) the amount of years
        """

        super().__init__(name='Seconds', symbol='s', to_base=Conversion(1 / 86400), value=value)


class MilliSecond(Time):
    """A whiplash is about 100ms."""

    def __init__(self, value=float()):
        """Create instance of the MilliSecond class.

        :param value: (optional, int or float) the amount of years
        """

        super().__init__(name='MilliSecond', symbol='ms', to_base=Conversion(1 / 86400000), value=value)


class MicroSecond(Time):
    """5.4 microseconds – the time taken by light to travel one mile in a vacuum (or radio waves point-to-point in a
    near vacuum)"""

    def __init__(self, value=float()):
        """Create instance of the MicroSecond class.

        :param value: (optional, int or float) the amount of years
        """

        super().__init__(name='MicroSecond', symbol='μs', to_base=Conversion(1 / 86400000000), value=value)
