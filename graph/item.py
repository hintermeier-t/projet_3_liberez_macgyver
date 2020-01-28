"""Module containing ItemSprite class"""

import pygame as pg
from . import gdisplay
class ItemSprite (pg.sprite.Sprite):
    def __init__(self, file_name:str, x:int, y:int):
        self.x = x
        self.y = y
        self.image, self.rect = gdisplay.load_image(file_name, -1)
        self.image = pg.transform.scale(self.image, (50,50))

    def update_pos (self,state, new_x, new_y):
        if state is True:
            self.x = new_x
            self.y = new_y


    def print_item(self, screen):
        screen.blit(self.image, (self.x * 50, self.y * 50))