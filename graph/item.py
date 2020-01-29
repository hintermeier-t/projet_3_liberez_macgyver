#  -*coding: UTF-8-*
"""Module containing ItemSprite class."""

import pygame as pg
from . import gdisplay


class ItemSprite (pg.sprite.Sprite):
    """Class displaying the item sprite.

    Gathering all we need to display the 3 items Sprite (position,
    source picture etc...). Inherit the pygame Sprite class.

    Attributes :
        x (int) : the horizontal position of the Sprite.
        y (int) : the vertical position of the Sprite.
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
        self.x = x
        self.y = y
        self.image, self.rect = gdisplay.load_image(file_name, -1)
        self.image = pg.transform.scale(self.image, (50, 50))

    def update_pos(self, state: bool, new_x: int, new_y: int):
        """Update the sprite position.

        If collected, the sprite is set apart.

        Args:
            state (bool): needed to make sure the item is collected.
            new_x (int): new x position of the item.
            new_y (int): new_y position of the item.
        """
        if state is True:
            self.x = new_x
            self.y = new_y

    def print_item(self, screen):
        """Method to display the item sprite.

        Arg:
        screen (Surface): Surface used to draw the sprite.
        """
        screen.blit(self.image, (self.x * 50, self.y * 50))
