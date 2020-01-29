#  -*coding: UTF-8-*
"""Module gathering the needed functions to display, sprites etc..."""

import os
import sys
import pygame as pg
from pygame.locals import *
from . import player
from . import maze
from . import item
from . import guard
import core


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


def display_sprites(core_maze: core.board.GamingBoard,
                    graph_maze: maze.MazeSprite,
                    player: player.McSprite,
                    needle: item.ItemSprite,
                    tube: item.ItemSprite,
                    ether: item.ItemSprite,
                    ennemy: guard.GuardSprite, screen):
    """Displays all the sprite.

    Display all the sprites in the right order.

    Args:
        core_maze (GamingBoard): Core class containing all the
        informations about the maze.
        graph_maze (MazeSprite): sprite of the entire maze.
        player (McSprite): McGyver (player) sprite.
        needle (ItemSprite): Needle item sprite.
        tube (ItemSprite): Tube item sprite.
        ether (ItemSprite): Ether item sprite.
        ennemy (GuardSprite): Guard sprite.
        screen (Surface): Screen used to draw the sprites.
    """
    graph_maze.print_maze(core_maze, screen)
    needle.print_item(screen)
    tube.print_item(screen)
    ether.print_item(screen)
    ennemy.print_guard(screen)
    player.print_player(screen)


def manage_event(game: core.game.Game, player: player.McSprite):
    """One of the main loops of the game.

    This loop manage every action in the game. The exit commands
    and the move commands.

    Args:
        game (Game): Game class to get the core informations and update the
        McGyver position.
        player (McSprite): Sprite class of the player to update the position
        to display on the maze.
    """
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


def manage_item(game: core.game.Game,
                needle: item.ItemSprite,
                tube: item.ItemSprite,
                ether: item.ItemSprite):
    """Manage the position of the items if collected.

    Args:
        game (Game): Game class needed to interact with the core items.
        needle (ItemSprite): sprite of the needle.
        tube (ItemSprite): sprite of the tube.
        ether (ItemSprite): sprite of the ether.
    """
    needle.update_pos(game.collect(game.needle), 18, 1)
    ether.update_pos(game.collect(game.ether), 18, 2)
    tube.update_pos(game.collect(game.tube), 18, 3)


def display_screen(game: core.game.Game,
                   maze: maze.MazeSprite,
                   player: player.McSprite,
                   needle: item.ItemSprite,
                   tube: item.ItemSprite,
                   ether: item.ItemSprite,
                   ennemy: item.ItemSprite):
    """Main loop of the game.

    Sets up the screen, displays the sprites and the win or lose panes.

    Args:
        game (Game): Game class to interact with the core classes.
        maze (MazeSprite): sprite of the entire maze.
        player (McSprite): McGyver (player) sprite.
        needle (ItemSprite): Needle item sprite.
        tube (ItemSprite): Tube item sprite.
        ether (ItemSprite): Ether item sprite.
        ennemy (GuardSprite): Guard sprite.
    """
    pg.init()
    pg.display.set_caption('Help McGyver !')
    screen = pg.display.set_mode((1000, 750))
    while 1:
        screen.fill((0, 0, 0))
        display_sprites(game.maze, maze, player, needle,
                        tube, ether, ennemy, screen)
        manage_event(game, player)
        manage_item(game, needle, tube, ether)
        if game.win_or_lose() is True:
            success, sucess_rect = load_image("win.png", -1)
            screen.blit(success, (150, 250))
            break
        if game.win_or_lose() is False:
            success, sucess_rect = load_image("lose.png", -1)
            screen.blit(success, (150, 250))
            break
        pg.display.flip()
    pg.quit()
