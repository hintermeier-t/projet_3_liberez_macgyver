#  -*coding: UTF-8-*

"""Module containing the UseableItem class."""


class UseableItem:
    """Class defining an item on the maze.

    This class is used to create the items needed in order to escape.

    Attributes:
        _position (int): position where the item will appear.
        _is_collected (bool): collected status of the item.
    """

    def __init__(self, loc):
        """Initializes the itel object.

        Arg:
            loc (int): position of the item.
        """
        self._position = loc
        self._is_collected = False

    def switch(self):
        """When the player get an item, switch the _is_collected status to
        True."""
        self._is_collected = True

    @property
    def position(self):
        """int: tile number of the item on the board.
        """
        return self._position

    @property
    def x(self):
        """int: x position of the item on the board.
        """
        return self._position % 15

    @property
    def y(self):
        """int: y position of the player on the board.
        """
        return self._position // 15

    @property
    def is_collected(self):
        """bool: True if the item is collected by the player.
        """
        return self._is_collected
