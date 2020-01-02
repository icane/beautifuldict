class Baseconfig(dict):
    """
    Manages configuration parameters.

    A Baseconfig object stores the configuration parameters as a parameter
    tree. It gives access to parameters in two ways: as dictionary keys or
    as attributes of the object.

    Example:

    from beautifuldict.baseconfig import Baseconfig

    CONFIG_DICT = {'example1': 'hello world'}

    config = Baseconfig(CONFIG_DICT)
    config.example1     # returns 'hello world'
    config['example1']  # returns 'hello world'

    .. automethod:: __init__
    .. automethod:: add
    .. automethod:: __getattr__
    .. automethod:: __setitem__
    .. automethod:: __setattr__
    .. automethod:: clean
    .. automethod:: __getstate__
    .. automethod:: __setstate__
    """

    def __init__(self, dictionary):
        """Constructor.

        Args:
          dictionary: configuration dictionary.

        Returns:
          obj (Baseconfig): Baseconfig instance initialized.

        """
        super(Baseconfig, self).__init__(dictionary)

        for key in self:
            items = self[key]

            if isinstance(items, list):
                for index, item in enumerate(items):
                    if isinstance(item, dict):
                        items[index] = Baseconfig(item)

            elif isinstance(items, dict):
                self[key] = items

    def add(self, dictionary):
        """Add new entries dictionary to Baseconfig instance.

        Args:
          dictionary: configuration params dictionary.
        """
        if not isinstance(dictionary, dict):
            raise(TypeError('Expected a dictionary'))

        for key in dictionary:
            items = dictionary[key]

            if isinstance(items, list):
                for index, item in enumerate(items):
                    if isinstance(item, dict):
                        items[index] = Baseconfig(item)

                self[key] = items
            elif isinstance(items, dict):
                if key in self:
                    self[key].add(items)
                else:
                    self[key] = items
            else:
                self[key] = items

    def __getattr__(self, key):
        """Get dictionary key as attribute. Overriden method.

        Args:
          key (string): key of the dictionary.

        Returns:
          value: key associated value.

        """
        return self[key]

    def __setitem__(self, key, value):
        """Overriden method."""
        if isinstance(value, dict):
            super(Baseconfig, self).__setitem__(key, Baseconfig(value))
        else:
            super(Baseconfig, self).__setitem__(key, value)

    def __setattr__(self, key, value):
        """Overriden method."""
        if isinstance(value, dict):
            super(Baseconfig, self).__setitem__(key, Baseconfig(value))
        else:
            super(Baseconfig, self).__setitem__(key, value)

    def clean(self, key):
        """Do cleanup for an attribute."""
        del(self[key])

    def __getstate__(self):
        """Overriden method."""
        return self.__dict__

    def __setstate__(self, dictionary):
        """Overriden method."""
        self.__dict__ = dictionary
