"""Module containing the player sprite"""

import pygame as pg
from . import gdisplay

class McSprite(pg.sprite.Sprite) :
    """Class displaying the player sprite.
    
    Gathering all we need to display the player Sprite (position, source picture etc...).
    Inherit the pygame Sprite class.

    Attributes :
        x (int) : the horizontal position of the Sprite.
        y (int) : the vertical position of the Sprite.
        image : the picture representing MacGyver
        rect : the dimensions of the sprite
    """

    def __init__(self, x, y):
        """Class constructor, taking x and y coordinates as parameters
        Args :
          x (int) : horizontal position of MacGyver
          y (int) : vertical position of MacGyver"""
        self.x = x
        self.y = y
        self.image, self.rect = gdisplay.load_image("MacGyver.png", -1)
      
    def update_pos(self, new_x, new_y):
      self.x = new_x
      self.y = new_y

    def print_player(self, screen):
      screen.blit(self.image, (self.x * 50, self.y * 50))