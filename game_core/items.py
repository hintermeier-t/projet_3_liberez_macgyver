#-*coding: UTF-8-*
#!/usr/bin/python3.

"""Module containing the UseableItem class"""

class UseableItem:
    """Class defining an item, wich will be used by the player, identified by:
    -its name
    -its location (on an empty space)
    -wherever it is collected or not"""

    def __init__(self, name_string,loc):
        """Initializing the item with its name (Needle, Tube, Ether), the loc will
        be defined randomly, and the collected state is False at the begining."""
        self.name = name_string
        self._position = loc
        self._is_collected = False

    def switch(self):
        self._is_collected = True

    @property
    def position(self):
        return self._position

    @property
    def is_collected(self):
        return self._is_collected
