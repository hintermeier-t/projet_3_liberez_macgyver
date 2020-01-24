#-*coding: UTF-8-*
#!/usr/bin/python3.6

import os, sys
import pygame as pg
from pygame.locals import *
import graph as g
import core as c
pg.init()
size = width, height = 1024, 768
playing_board = g.maze.MazeSprite()
game = c.game.Game()
screen = pg.display.set_mode(size)
black = 0, 0 ,0
while 1:
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
    screen.fill(black)
    playing_board.print_maze(game.maze)
    pg.display.flip()