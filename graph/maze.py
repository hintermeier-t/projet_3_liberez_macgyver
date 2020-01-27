import pygame as pg
from . import gdisplay
class MazeSprite (pg.sprite.Sprite):
    """Class containing the Maze Sprite to display"""
    def __init__(self):
        self.sheet, self.sheet_rect = gdisplay.load_image("floor-tiles-20x20.png")
        self.sheet = pg.transform.scale(self.sheet, (1000,650))
        self.screen = pg.display.get_surface()
        
    def print_maze (self, board, screen):
        x = 0
        y = 0
        for i in range (226):
            if x > 1 and x % 15 == 0:
                x = 0
                y += 1
            if i in board._walls:
                screen.blit(self.sheet, (x * 50, y * 50), pg.Rect((650, 200, 50, 50))) #  300px from left, 80px from top, size_x, size_y 
            if i in board._path:
                screen.blit(self.sheet, (x * 50, y * 50), pg.Rect((500, 0, 50, 50)))
            x +=1