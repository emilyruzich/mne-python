# Authors: Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
#          Matti Hamalainen <msh@nmr.mgh.harvard.edu>
#
# License: BSD (3-clause)


class Bunch(dict):
    """ Container object for datasets: dictionnary-like object that
        exposes its keys as attributes.
    """

    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)
        self.__dict__ = self
