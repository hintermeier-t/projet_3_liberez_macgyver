#  -*coding: UTF-8-*
"""Module containing the player sprite."""

import pygame as pg
from . import gdisplay


class McSprite(pg.sprite.Sprite):
    """Class displaying the McGyver sprite.

    Gathering all we need to display the 3 items Sprite (position,
    source picture etc...). Inherit the pygame Sprite class.

    Attributes :
        x (int) : the horizontal position of the Sprite.
        y (int) : the vertical position of the Sprite.
        image (Surface): the picture representing MacGyver
        rect (Rect): the dimensions of the sprite
    """

    def __init__(self, x, y):
        """Class constructor.

        Args :
          x (int) : horizontal position of the player.
          y (int) : vertical position of the player.
        """
        self.x = x
        self.y = y
        self.image, self.rect = gdisplay.load_image("MacGyver.png", -1)

    def update_pos(self, new_x, new_y):
        """Update the sprite position.

        When the player moves, we moves the sprite to new coordinates.

        Args:

          new_x (int): new x position of the item.
          new_y (int): new_y position of the item.
        """
        self.x = new_x
        self.y = new_y

    def print_player(self, screen):
      """Method to display the player sprite.

      Arg:
          screen (Surface): Surface used to draw the sprite.
        """
      screen.blit(self.image, (self.x * 50, self.y * 50))
