#-*coding: UTF-8-*
#!/usr/bin/python3.6

"""Module containing the Position class, used to create the visual part of the game"""

class Position:

    def __init__(self, value):
        self.pos = value

    def __add__(self, value):
        self.pos += value
    def __sub__(self, value):
        self.pos -= value
    @property
    def y(self):
        """Returning a y coordinate"""
        return int(self.pos) // 15

    @property
    def x(self):
        """Returning an x coordinate"""
        return int(self.pos) % 15

    @property
    def yx(self):
        return self.y, self.x
