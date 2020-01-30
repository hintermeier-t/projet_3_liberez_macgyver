#  -*coding: UTF-8-*
"""Module containing the GuardSprite Class."""

import pygame as pg
from . import gdisplay


class GuardSprite(pg.sprite.Sprite):
    """Class displaying the ennemy sprite.

    Gathering all we need to display the ennemy Sprite (position,
    source picture etc...). Inherit the pygame Sprite class.

    Attributes :
        image : the picture representing MacGyver.
        rect : the dimensions of the sprite.
    """

    def __init__(self, x: int, y: int):
        """Class constructor.

        Args :
          x (int) : horizontal position of the Guard.
          y (int) : vertical position of the Guard.
        """
        super(GuardSprite, self).__init__()
        self.image, self.rect = gdisplay.load_image("Gardien.png", -1)
        self.rect.topleft = (x*50, y*50)
