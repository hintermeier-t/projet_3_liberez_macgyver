#-*coding: UTF-8-*
#!/usr/bin/python3.8

"""Module containing the Position class, used to create the visual part of the game"""

class Position(int):

    def __new__(cls, value):
        return super().__new__(cls, value)

    @property
    def y(self):
        """Returning a y coordinate"""
        return int(self) // 15

    @property
    def x(self):
        """Returning an x coordinate"""
        return int(self) % 15

    @property
    def yx(self):
        return self.y, self.x
