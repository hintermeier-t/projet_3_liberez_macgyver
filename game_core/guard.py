class EnnemyGuard:
    """Class defining the ennemy to knock out with status and position."""

    def __init__(self,location):
        """Initializing the Ennemy basic attributes, awaken and located
        at the exit."""
        self._is_awake = True
        self._position = location

    @property
    def position(self):
        return _position

    @property
    def is_awake(self):
        return _is_awake

    def switch_status(self):
        self._is_awake = False
