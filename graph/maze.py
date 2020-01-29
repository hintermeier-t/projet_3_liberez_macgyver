#  -*coding: UTF-8-*
"""Module containing the MazeSpriteClass."""

import pygame as pg
from . import gdisplay


class MazeSprite (pg.sprite.Sprite):
    """Class displaying the maze sprite.

    Gathering all we need to display the walls sprites,
    and the path sprites. (position, source picture etc...).
    Inherit the pygame Sprite class.

    Attributes :
        sheet (Surface) : SpriteSheet used to design the walls and path.
        sheet_rect (Rect) : Area of the sprite.
    """

    def __init__(self):
        """Class constructor.

        Class constructor whiwh resize the spritesheet to make the 20x20
        tiles 2.5 times bigger (50x50).
        """
        self.sheet, self.sheet_rect = gdisplay.load_image(
            "floor-tiles-20x20.png")
        self.sheet = pg.transform.scale(self.sheet, (1000, 650))

    def print_maze(self, board, screen):
        """Method to display the entire maze.

        Args:
        board (GamingBoard): Core maze to get the walls and path positions.
        screen (Surface): Surface used to draw the maze.
        """
        x = 0
        y = 0
        for i in range(226):
            if x > 1 and x % 15 == 0:
                x = 0
                y += 1
            if i in board._walls:
                # 300px from left, 80px from top, size_x, size_y
                screen.blit(self.sheet, (x * 50, y * 50),
                            pg.Rect((650, 200, 50, 50)))
            if i in board._path:
                screen.blit(self.sheet, (x * 50, y * 50),
                            pg.Rect((500, 0, 50, 50)))
            x += 1
