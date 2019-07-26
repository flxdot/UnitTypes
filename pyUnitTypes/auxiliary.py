def class_factory(BaseClass, name, symbol, to_base, value=float()):
    """Helper function to generically create new classes programmatically."""

    # create new local class
    class NewClass(BaseClass):
        def __init__(self, value=value):
            super().__init__(name=name, symbol=symbol, to_base=to_base, value=value)

    NewClass.__name__ = name
    NewClass.__qualname__ = name

    return NewClass
