#-*coding: UTF-8-*
#!/usr/bin/python3.8
"""Module containing the GamingBoard Class, wich is used to design the maze"""
class GamingBoard:
    """Class designing the board wich will be used to play.
    It is defined by 2D list with x and y coordinates, each one related to a
    letter that will be used to design the structure as follow :
    -'S' is the Start
    -'W' is a wall
    -'X' is the Exit
    -'C' is a path"""

    def __init__(self,map_file):
        """Initializing the maze with 2 sets, gathering the walls on one hand
        and the path on the other hand, as well as the Start and the Exit"""
        with open(map_file,'r', encoding='utf-8') as file:
            self._walls = set()
            self._path = set()
            self._start = 0
            self._exit = 0
            i=0
            tmp = file.read().replace("\n","")
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
            print(self.walls, '\n', self.path,"\n", self.start,"\n",self.exit)

    @property
    def walls(self):
        return self._walls

    @property
    def path(self):
        return self._path

    @property
    def start(self):
        return self._start

    @property
    def exit(self):
        return self._exit
