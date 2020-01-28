
"""Module gathering the needed functions to display sounds, sprites etc..."""
from . import player
from . import maze
from . import item
from . import guard
import core
import os, sys
import pygame as pg
from pygame.locals import *

def load_image(name, colorkey=None):
    """Function that load the sprite, taking string as name"""

    file_name = os.path.join('ressources', name)

    try:
        picture = pg.image.load(file_name)
    except pg.error:
    #: If the picture doesn't load, we quit the game
        print ("Couldn't load the picture :", name)
        raise SystemExit(str(pg.compat.geterror()))
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = picture.get_at((0,0))
        picture.set_colorkey(colorkey, RLEACCEL)
    return (picture, picture.get_rect())

def display_sprites(core_maze,
 graph_maze:maze.MazeSprite,
 player:player.McSprite,
 needle:item.ItemSprite,
 tube:item.ItemSprite,
 ether:item.ItemSprite,
 ennemy:guard.GuardSprite, screen):
    graph_maze.print_maze(core_maze, screen)
    needle.print_item(screen)
    tube.print_item(screen)
    ether.print_item(screen)
    ennemy.print_guard(screen)
    player.print_player(screen)
    
def manage_event(game:core.game.Game, maze, player, needle, tube, ether, ennemy):
    for event in pg.event.get():
        #: First we manage the exit commands
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pg.quit()
            sys.exit()
        #:  Then we manage the keyboard commands
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

def manage_game(game:core.game.Game, maze, player, needle, tube, ether, ennemy, screen):
    
    needle.update_pos(game.collect(game.needle), 18, 1)
    ether.update_pos(game.collect(game.ether), 18, 2)
    tube.update_pos(game.collect(game.tube), 18, 3)


def display_screen(game:core.game.Game, maze, player, needle, tube, ether, ennemy):
    pg.init()
    pg.display.set_caption('Help McGyver !')
    screen = pg.display.set_mode((1000, 750))
    while 1:
        screen.fill((0, 0, 0))
        display_sprites(game.maze, maze, player, needle, tube, ether, ennemy, screen)
        manage_event(game, maze, player, needle, tube, ether, ennemy)
        manage_game(game, maze, player, needle, tube, ether, ennemy, screen)
        if game.win_or_lose():
            success, sucess_rect = load_image("win.png", -1)
            screen.blit (success, (150, 250))
        if game.win_or_lose() is False:
            success, sucess_rect = load_image("lose.png", -1)
            screen.blit (success, (150, 250))       
        pg.display.flip()
    pg.quit()