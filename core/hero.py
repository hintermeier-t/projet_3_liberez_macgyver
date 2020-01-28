#-*coding: UTF-8-*
#!/usr/bin/python3.6

"""Module containing the McGyver class, wich represent the player in the game"""

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
    
    @property
    def x(self):
        return self._position % 15
    
    @property
    def y(self):
        return self._position // 15   

    def _set_position(self, move):
        self._position += move

    def move_left(self, path:set):
        if self._position-1 in path:
            self._set_position(-1)

    def move_right(self, path:set):
        if self._position+1 in path:
            self._set_position(+1)

    def move_up(self, path:set):
        if self._position-15 in path:
            self._set_position(-15)

    def move_down(self,path:set):
        if self._position+15 in path:
            self._set_position(+15)
