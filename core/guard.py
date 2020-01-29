#  -*coding: UTF-8-*

"""Module containing the EnnemyGuard class."""


class EnnemyGuard:
    """Class defining the ennemy to knock out.
    
    Attribute:
        position (int): position of the guard on the maze."""

    def __init__(self, location):
        """Initializing the Ennemy basic attribute located at the exit.
        
        Arg:
            location (int): position of the exit on the maze.
        """
        self._position = location

    @property
    def position(self):
        """int: tile where the guard is set.
        """
        return self._position

    @property
    def x(self):
        """int: x position of the guard on the board.
        """
        return self._position % 15

    @property
    def y(self):
        """int: y position of the guard on the board.
        """
        return self._position // 15
