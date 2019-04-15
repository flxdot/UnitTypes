Overview
========

This package is designed to easily work with physical units. The main usage is to display different units and unit
systems in FrontEnds. Typical use case would be: Your application make it's calculation in SI units and then you'll need
to deploy your application in the US. So instead of display temperatures in °C you'll now have to display it in °F.

**Warning: It should never be used to make precise calculations, since the accuracy is
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

Arithmetic Operators
^^^^^^^^^^^^^^^^^^^^

The following mathematical operators can be used to calculate with the units.

* **add (+)**: Works as within a UnitType package. Raises a TypeError if Units from different modules are used.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    two_kilometer = Meter(1000) + KiloMeter(1)


* **sub (-)**: Works as within a UnitType package. Raises a TypeError if Units from different modules are used.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    half_kilometer = KiloMeter(1) - Meter(500)


* **mul (*)**: Works when multiplied with ``float`` or ``int``.

  Raises ``pyUnitTypes.basics.UnknownUnitMultiplicationError`` when multiplication of the two units has not been implemented

  Raises ``TypeError`` if multiplied with objects which are not inherited from ``pUnitTypes.basics.BaseUnit``.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    five_kilometer = KiloMeter(2) * 2.5


* **div (*)**: Works when divided by ``float`` or ``int``.

  Raises ``pyUnitTypes.basics.UnknownUnitDivisionError`` when division of the two units has not been implemented or
  if division of ``float`` or ``int`` by the unit is not implemented.

  Raises ``TypeError`` if multiplied with objects which are not inherited from ``pUnitTypes.basics.BaseUnit``.

  .. code-block:: python

    from pyUnitTypes.length import Meter, KiloMeter

    four_kilometer = KiloMeter(10) / 2.5


Comparison Operators
^^^^^^^^^^^^^^^^^^^^

Any pyUnitTypes object can be compared to another object from the same module. Comparing to a object of a different
package or any other object will raise as ``TypeError``.

.. code-block:: python

  from pyUnitTypes.length import Meter, KiloMeter

  is_eq = Meter(1000) == KiloMeter(1)
  is_ne = Meter(0) != KiloMeter(1)
  is_lt = Meter(1) < KiloMeter(1)
  is_gt = Meter(2000) > KiloMeter(1)
  is_le = Meter(1000) >= KiloMeter(1)
  is_ge = Meter(1000) <= KiloMeter(1)

Other numeric functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Besides the four basic arithmetic operators several other mathematical operations are supported:

* ``round()``
* ``math.ceil()``
* ``math.floor()``
* ``__neg__``: ``Meter(-1)`` is equal to ``-Meter(1)``
* ``__pos__``: ``Meter(+1)`` is equal to ``+Meter(1)``

All pyUnitType objects can be converted to ``int`` or ``float``.
