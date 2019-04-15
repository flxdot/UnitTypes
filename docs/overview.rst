Overview
========

This package is designed to easily work with different units. The main usage is to display different units and unit
systems in FrontEnds. **Warning: It should never be used to make precise calculations, since the accuracy is
limited to 3-4 digits at the moment. Especially when converting SI units to imperial units.**

Converting your first value
----------------------------

The following example illustrates how to convert from one unit to another in the same type of physical unit (e.g. lengths):

.. code-block:: python

  from pyUnitTypes.length import Meter, KiloMeter, MilliMeter, Inch

  # define the value as KiloMeter
  a_long_distance = KiloMeter(2.5)
  a_short_distance = Inch(1)

  # print the value as Meter
  print(Meter(a_long_distance))
  print(MilliMeter(a_short_distance))

The output will look like this:

.. code-block::

  2500.0 m
  25.4 mm

Calculating with units
----------------------

Calculation with unit values is as easy as normal calculation. Sofar following operators are implemented:

Operators
^^^^^^^^^
* **add (+)**: Works as within a UnitType package. Raises a TypeError if Units from different modules are used.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    print(Meter(1000) + KiloMeter(1))

  prints: ``2.0 km``

* **sub (-)**: Works as within a UnitType package. Raises a TypeError if Units from different modules are used.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    print(KiloMeter(1) - Meter(250))

  prints: ``0.75 km``

* **mul (*)**: Works when multiplied with ``float`` or ``int``.

  Raises ``pyUnitTypes.basics.UnknownUnitMultiplicationError`` when multiplication of the two units has not been implemented
  Raises ``TypeError`` if multiplied with objects which are not inherited from ``pUnitTypes.basics.BaseUnit``.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    print(KiloMeter(1) * 2.5)

  prints: ``2.5 km``

* **div (*)**: Works when divided by ``float`` or ``int``.

  Raises ``pyUnitTypes.basics.UnknownUnitDivisionError`` when divided of the two units has not been implemented or
  if division of ``float`` or `´int`` by the unit is not implemented.
  Raises ``TypeError`` if multiplied with objects which are not inherited from ``pUnitTypes.basics.BaseUnit``.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    print(KiloMeter(10) / 2.5)

  prints: ``4 km``


