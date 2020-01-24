#!/usr/bin/python3.6
"""Module gathering the needed functions to display sounds, sprites etc..."""

import os, sys
import pygame as pg
from pygame.locals import *

class Background(pg.sprite.Sprite):
    """Class used to display the background of the game"""
    
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def load_image(name, colorkey=None):
    """Function that load the sprite, taking string as name"""

    file_name = os.path.join('ressources', name)

    try:
        picture = pg.image.load(file_name)
    except pg.error:
    #if the picture doesn't load, we quit the game
        print ("Couldn't load the picture :", name)
        raise SystemExit(str(pg.compat.geterror()))

   # picture = picture.convert()
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = picture.get_at((0,0))
        picture.set_colorkey(colorkey, RLEACCEL)
    return (picture, picture.get_rect())

def display_screen():
    pg.init()
    screen = pg.display.set_mode((1024, 768))
    pg.display.set_caption('Help McGyver !')
    pg.mouse.set_visible(1)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    if pg.font:
        font = pg.font.Font(None, 36)
        text = font.render("Ceci est une phrase de test", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pg.display.flip()

    displaying = True
    clock = pg.time.Clock()
    while displaying:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT:
                displaying = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                displaying = False
            elif event.type == KEYDOWN and event.key == K_DOWN:
                screen.blit(background, (0, 0))
                background.blit(font.render("OOOK", 1, (10, 10, 10)), textpos)
                screen.blit(background, (0, 0))
                pg.display.flip()

    pg.quit()            