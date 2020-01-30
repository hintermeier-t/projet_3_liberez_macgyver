#  -*coding: UTF-8-*
"""Module containing the player sprite."""

import pygame as pg
from . import gdisplay


class McSprite(pg.sprite.Sprite):
    """Class displaying the McGyver sprite.

    Gathering all we need to display the 3 items Sprite (position,
    source picture etc...). Inherit the pygame Sprite class.

    Attributes :
        image (Surface): the picture representing MacGyver
        rect (Rect): the dimensions of the sprite
    """

    def __init__(self, x, y):
        """Class constructor.

        Args :
          x (int) : horizontal position of the player.
          y (int) : vertical position of the player.
        """
        super(McSprite, self).__init__()
        self.image, self.rect = gdisplay.load_image("MacGyver.png", -1)
        self.rect.topleft = (x*50, y*50)
