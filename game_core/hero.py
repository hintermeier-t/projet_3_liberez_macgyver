#-*coding: UTF-8-*
#!/usr/bin/python3.8

class McGyver :
    """Class representing the player, with a position on the map, and the items
    he posess, and the action he can do like moving, catching and item or
    knocking the guard"""

    def __init__(self, init_position):
        """Initializing the Hero at the start_place of the map.
        We get the tuple containing the starting coordinates and change
        them into a list of coordinates we can work on"""
        self._position = init_position

    @property
    def position(self):
        return self._position

    def _set_position(self, move):
        self._position += move

    def move_left(self, path):
        if self._position+1 in path:
            self._set_position(-1)

    def move_right(self, path):
        if self._position+1 in path:
            self._set_position(+1)

    def move_up(self, path):
        if self._position+1 in path:
            self._set_position(+15)

    def move_down(self,path):
        if self._position+1 in path:
            self._set_position(-15)
