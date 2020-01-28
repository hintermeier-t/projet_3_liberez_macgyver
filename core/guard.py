#-*coding: UTF-8-*
#!/usr/bin/python3.6

"""Module containing the EnnemyGuard class"""

class EnnemyGuard:
    """Class defining the ennemy to knock out."""

    def __init__(self,location):
        """Initializing the Ennemy basic attribute located at the exit."""
        self._position = location

    @property
    def position(self):
        return self._position
    @property
    def x(self):
        return self._position % 15
    @property
    def y(self):
        return self._position // 15