#  -*coding: UTF-8-*
"""Module containing ItemSprite class."""

import pygame as pg
from . import gdisplay


class ItemSprite (pg.sprite.Sprite):
    """Class displaying the item sprite.

    Gathering all we need to display the 3 items Sprite (position,
    source picture etc...). Inherit the pygame Sprite class.

    Attributes :
        image (Surface): the picture representing MacGyver
        rect (Rect): the dimensions of the sprite
    """

    def __init__(self, file_name: str, x: int, y: int):
        """Class constructor.

        Args :
            file_name (str): name of the sprite picture.
            x (int) : horizontal position of the item.
            y (int) : vertical position of the item.
        """
        super(ItemSprite, self).__init__()
        self.image, self.rect = gdisplay.load_image(file_name, -1)
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect.topleft = (x*50, y*50)
