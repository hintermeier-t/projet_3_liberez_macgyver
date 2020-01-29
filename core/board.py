#  -*coding: UTF-8-*

"""Module containing the GamingBoard Class, wich is used to design the maze."""


class GamingBoard:
    """Class designing the labyrinth.

    Core class designing the maze wich will be used to play. It is defined by
    2D  (x and y) coordinates.

    Attributes :
        _walls (set: Set of every position of the wall tiles
            ("W" in the text file).
        _path (set): Set of every position of the path tiles
            ("C" in the text file).
        _start (int): Position where the player will appear
            ("S" in the text file).
        _exit (int): Position where the ennemy will stand
            ("X" in the text file).
    """

    def __init__(self, map_file: str):
        """Initializing the board.

        Uses the .txt file sent as parameter to generate the maze by reading
        every letter, and assigning it to the proper attribute.

        Args:
           map_file (str): Name of the maze file.
        """

        with open(map_file, "r", encoding="utf-8") as file:
            self._walls = set()
            self._path = set()
            self._start = 0
            self._exit = 0
            i = 0
            tmp = file.read().replace("\n", "")
            for i in range(len(tmp)):
                if tmp[i].upper() == "W":
                    self._walls.add(i)
                if tmp[i].upper() == "C":
                    self._path.add(i)
                if tmp[i].upper() == "S":
                    self._start = i
                    self._path.add(i)
                if tmp[i].upper() == "X":
                    self._exit = i
                    self._path.add(i)

    @property
    def walls(self):
        """
        :obj:`set` of :obj:`int` : every position of the wall tiles.
        """
        return self._walls

    @property
    def path(self):
        """
        :obj:`set` of :obj:`int` : every position of the path tiles.
        """
        return self._path

    @property
    def start(self):
        """
        int: start position of the player.
        """
        return self._start

    @property
    def exit(self):
        """
        int: the exit position also the ennemy position.
        """
        return self._exit
