#!/usr/bin/python3.6
"""Module gathering the needed functions to display sounds, sprites etc..."""

import os, sys
import pygame

def load_image(name, colorkey=None):
    """Function that load the sprite, taking str as name"""
    file_name = os.path.join('../ressources', name)
    try:
        image = pygame.image.load(file_name)
    except pygame.error, message:
    #if the picture doesn't load, we quit the game
        print "Impossible de charger l'image :", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
