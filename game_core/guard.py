#-*coding: UTF-8-*
#!/usr/bin/python3.8

"""Module containing the EnnemyGuard class"""

class EnnemyGuard:
    """Class defining the ennemy to knock out."""

    def __init__(self,location):
        """Initializing the Ennemy basic attribute located at the exit."""
        self._position = location

    @property
    def position(self):
        return _position
