# -*coding: UTF-8-*
"""Main module of the game."""

import core as c
import graph as g


def main():
    """Main function of the game.

    Runs eveyrthind, initialize the sprites and the game.
    """
    game = c.game.Game()
    maze = g.maze.MazeSprite()
    player = g.player.McSprite(game.player.x, game.player.y)
    needle = g.item.ItemSprite("aiguille.png", game.needle.x, game.needle.y)
    tube = g.item.ItemSprite("tube_plastique.png", game.tube.x, game.tube.y)
    ether = g.item.ItemSprite("ether.png", game.ether.x, game.ether.y)
    ennemy = g.guard.GuardSprite(game.ennemy.x, game.ennemy.y)
    g.gdisplay.display_screen(game, maze, player, needle, tube, ether, ennemy)


main()
