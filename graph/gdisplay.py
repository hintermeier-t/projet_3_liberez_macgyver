#  -*coding: UTF-8-*
"""Module gathering the needed functions to display, sprites etc..."""

import os
import pygame as pg
from pygame.locals import *


def load_image(name: str, colorkey=None):
    """Function that load the sprite, taking string as name.

    Load the picture of the sprite. Every picture is in the "ressource"
    folder.

    Args:
        name (str): name of the file with extension
        colorkey (int): transparent colorkey

    Returns:
        picture (Surface): the loaded picture
        picture.get_rect() (Rect): the area of the sprite

    Raises:
        pygame.error : standard ppygame error. In this case if the picture
        is not found.
    """

    file_name = os.path.join('ressources', name)

    try:
        picture = pg.image.load(file_name)
    except pg.error:
        # If the picture doesn't load, we quit the game
        print("Couldn't load the picture :", name)
        raise SystemExit()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = picture.get_at((0, 0))
        picture.set_colorkey(colorkey, RLEACCEL)
    return (picture, picture.get_rect())