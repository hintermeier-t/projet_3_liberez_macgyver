# -*coding: UTF-8-*

"""Module containing the McGyver class, wich represent the player in the
game."""


class McGyver:
    """Class representing the player.

    It manages the player's position and the 4 way to move.
    """

    def __init__(self, init_position):
        """Initializing the Hero at the start_place of the map.

        Set the initial position.

        Arg:
            init_position (int): start position on the maze.
        """

        self._position = init_position

    @property
    def position(self):
        """int: tile where the player is set.
        """
        return self._position

    @property
    def x(self):
        """int: x position of the player on the board.
        """
        return self._position % 15

    @property
    def y(self):
        """int: y position of the player on the board.
        """
        return self._position // 15

    def _set_position(self, move):
        """Update the player's position.

        Changes the player's position with a number of tiles,
        representing the way to move.

        Arg:
        move (int): number of tile to move.
        """
        self._position += move

    def move_left(self, path: set):
        """Verify if the player can move to the left.

        If the leftward tile is in the path, we update the position.

        Arg:
            path (set of int): set of every path tile of the maze.
        """
        if self._position-1 in path:
            self._set_position(-1)

    def move_right(self, path: set):
        """Verify if the player can move to the right.

        If the rightward tile is in the path, we update the position.

        Arg:
            path (set of int): set of every path tile of the maze.
        """
        if self._position+1 in path:
            self._set_position(+1)

    def move_up(self, path: set):
        """Verify if the player can move up.

        If the uptward tile is in the path, we update the position.

        Arg:
            path (set of int): set of every path tile of the maze.
        """
        if self._position-15 in path:
            self._set_position(-15)

    def move_down(self, path: set):
        """Verify if the player can move down.

        If the downward tile is in the path, we update the position.

        Arg:
            path (set of int): set of every path tile of the maze.
        """
        if self._position+15 in path:
            self._set_position(+15)
