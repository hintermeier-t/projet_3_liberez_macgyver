#  -*coding: UTF-8-*
"""Module containing the Interface class."""
import pygame as pg
from pygame.locals import *
from . import player
from . import maze
from . import item
from . import guard
from . import gdisplay
import core


class Interface:
    """Class managing the graphic interface wih the player.

    Attributes :
        maze (MazeSprite): Sprite of the maze.
        player (McSprite): Sprite of the player.
        needle (ItemSprite): Sprite of the needle item.
        tube (ItemSprite): Sprite of the tube item.
        ether (ItemSprite): Sprite of the ether item.
        ennemy (GuardSprite): sprite of the guard.
        running (bool): Boolean to make the main loop works
        screen (Surface): Surface used to draw the scene.
    """

    def __init__(self, game: core.game.Game):
        """Class constructor.

        Create all the sprites and the necessary attributes to run the game.

        Arg:
        game (Game): Game object is used to interact with the core part.
        """
        self.maze = maze.MazeSprite()
        self.player = player.McSprite(game.player.x, game.player.y)
        self.needle = item.ItemSprite("aiguille.png", game.needle.x,
                                      game.needle.y)
        self.tube = item.ItemSprite("tube_plastique.png", game.tube.x,
                                    game.tube.y)
        self.ether = item.ItemSprite("ether.png", game.ether.x,
                                     game.ether.y)
        self.ennemy = guard.GuardSprite(game.ennemy.x, game.ennemy.y)
        self.running = True
        self.screen = pg.display.set_mode((1000, 750))
        self.sprite_group = pg.sprite.RenderPlain(
            (self.ennemy, self.tube, self.needle, self.ether, self.player))

    def manage_event(self, game: core.game.Game):
        """One of the main loops of the game.

        This loop manage every action in the game. The exit commands
        and the move commands.

        Args:
            game (Game): Game class to get the core informations and update the
            McGyver position.
        """
        for event in pg.event.get():
            #: First we manage the exit commands
            if event.type == pg.QUIT:
                self.running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.running = False
            #:  Then we manage the keyboard commands
            if event.type == KEYDOWN and event.key == K_DOWN:
                game.player.move_down(game.maze._path)
                self.player.rect.topleft = (game.player.x*50,
                                            game.player.y*50)
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                game.player.move_right(game.maze._path)
                self.player.rect.topleft = (game.player.x*50,
                                            game.player.y*50)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                game.player.move_left(game.maze._path)
                self.player.rect.topleft = (game.player.x*50,
                                            game.player.y*50)
            elif event.type == KEYDOWN and event.key == K_UP:
                game.player.move_up(game.maze._path)
                self.player.rect.topleft = (game.player.x*50,
                                            game.player.y*50)

    def manage_item(self, game: core.game.Game):
        """Manage the position of the items if collected.

        Args:
            game (Game): Game class needed to interact with the core items.
        """
        if game.collect(game.needle):
            self.needle.rect.topleft = (16*50, 1*50)
        if game.collect(game.ether):
            self.ether.rect.topleft = (16*50, 2*50)
        if game.collect(game.tube):
            self.tube.rect.topleft = (16*50, 3*50)

    def run_game(self, game: core.game.Game):
        """Main loop of the game.

        Sets up the screen, displays the sprites and the win or lose panes.

        Arg:
            game (Game): Game class to interact with the core classes.
        """
        pg.init()
        pg.display.set_caption('Help McGyver !')
        while self.running:
            self.screen.fill((0, 0, 0))
            self.manage_event(game)
            self.manage_item(game)
            self.maze.print_maze(game.maze, self.screen)
            self.sprite_group.draw(self.screen)
            if game.win_or_lose() is True:
                success, sucess_rect = gdisplay.load_image("win.png", -1)
                self.screen.blit(success, (150, 250))
            if game.win_or_lose() is False:
                success, sucess_rect = gdisplay.load_image("lose.png", -1)
                self.screen.blit(success, (150, 250))
            self.sprite_group.update()
            pg.display.flip()
        pg.quit()
