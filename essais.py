#-*coding: UTF-8-*
#!/usr/bin/python3.6

import os, sys
import pygame as pg
from pygame.locals import *
import graph as g
import core as c
pg.init()
size = width, height = 750, 750
playing_board = g.maze.MazeSprite()
game = c.game.Game()
player = g.player.McSprite(game.player.x, game.player.y)
screen = pg.display.set_mode(size)
black = 0, 0 ,0
while 1:
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_DOWN:
            game.player.move_down(game.maze._path)
            player.update_pos(game.player.x, game.player.y)
        if event.type == KEYDOWN and event.key == K_RIGHT:
            game.player.move_right(game.maze._path)
            player.update_pos(game.player.x, game.player.y)
        if event.type == KEYDOWN and event.key == K_LEFT:
            game.player.move_left(game.maze._path)
            player.update_pos(game.player.x, game.player.y)
        if event.type == KEYDOWN and event.key == K_UP:
            game.player.move_up(game.maze._path)
            player.update_pos(game.player.x, game.player.y)
    screen.fill(black)
    playing_board.print_maze(game.maze, screen)
    player.print_player(screen)

    
    pg.display.flip()