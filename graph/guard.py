"""Module containing the GuardSprite Class"""

import pygame as pg
from . import gdisplay

class GuardSprite(pg.sprite.Sprite) :
    """Class displaying the ennemy sprite.
    
    Gathering all we need to display the ennemy Sprite (position, source picture etc...).
    Inherit the pygame Sprite class.

    Attributes :
        x (int) : the horizontal position of the Sprite.
        y (int) : the vertical position of the Sprite.
        image : the picture representing MacGyver
        rect : the dimensions of the sprite
    """

    def __init__(self, x:int, y:int):
        """Class constructor, taking x and y coordinates as parameters
        Args :
          x (int) : horizontal position of the Guard
          y (int) : vertical position of the Guard"""
        self.x = x
        self.y = y
        self.image, self.rect = gdisplay.load_image("Gardien.png", -1)

    def print_guard(self, screen):
      screen.blit(self.image, (self.x * 50, self.y * 50))